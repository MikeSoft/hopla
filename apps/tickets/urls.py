from django.urls import path
from .views import TicketCreateView, TicketDetailView, TicketListView

app_name = "tickets"

urlpatterns = [
    path("list/", TicketListView.as_view(), name="ticket-list"),
    path("create/", TicketCreateView.as_view(), name="ticket-create"),
    path("<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
]
