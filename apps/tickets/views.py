from datetime import datetime
from rest_framework import generics, permissions
from django.utils.timezone import make_aware
from .models import ImageUpload
from .serializers import ImageUploadSerializer
from .models import Ticket
from .serializers import TicketSerializer


class TicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)

        # Filtrado por estado
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)

        # Filtrado por rango de fechas
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        if start_date and end_date:
            start = make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
            end = make_aware(datetime.strptime(end_date, "%Y-%m-%d"))
            queryset = queryset.filter(created_at__range=(start, end))

        return queryset


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(user=user)


class ImageUploadView(generics.CreateAPIView):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(ticket=self.request.user.tickets.last())
