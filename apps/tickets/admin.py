from django.contrib import admin
from .models import Ticket, ImageUpload


@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ticket",
        "image_url",
        "uploaded_at",
    ]


class ImageUploadInline(admin.StackedInline):
    model = ImageUpload
    extra = 1


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "num_images",
        "status",
    ]
    inlines = [ImageUploadInline]
