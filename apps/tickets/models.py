from django.conf import settings
from django.db import models


class Ticket(models.Model):
    class STATUS_CHOICES(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETE = "complete", "Complete"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tickets"
    )
    num_images = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES.choices, default=STATUS_CHOICES.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.status}"


class ImageUpload(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="uploaded_images"
    )
    image = models.ImageField(upload_to="images/", blank=True, null=True, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Ticket {self.ticket.id} - {self.uploaded_at}"
