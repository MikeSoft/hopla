import base64
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema

from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.utils.timezone import make_aware
import apps.tickets.async_manager as async_manager
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class TicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Ticket.objects.filter(user=user)

        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)

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
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "image",
                openapi.IN_FORM,
                description="Image file to upload",
                type=openapi.TYPE_FILE,
                required=True,
            ),
        ],
        responses={
            202: openapi.Response("Image upload started"),
            400: openapi.Response("No image provided"),
        },
    )
    def post(self, request, *args, **kwargs):
        ticket = self.get_object()
        image_data = request.FILES.get("image")
        if image_data:
            # Aquí se lanza la tarea Celery
            image_data_base64 = base64.b64encode(image_data.read()).decode("utf-8")
            async_manager.upload_image(ticket.id, image_data.name, image_data_base64)
            return Response(
                {"message": "Image upload started"}, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {"message": "No image provided"}, status=status.HTTP_400_BAD_REQUEST
        )
