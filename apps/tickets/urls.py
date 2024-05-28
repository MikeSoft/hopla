from django.urls import path
from .views import TicketCreateView, TicketDetailView, ImageUploadView, TicketListView

app_name = "tickets"

urlpatterns = [
    path("create/", TicketCreateView.as_view(), name="ticket-create"),
    path("<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("upload-image/", ImageUploadView.as_view(), name="upload-image"),
    path("list/", TicketListView.as_view(), name="ticket-list"),
]
