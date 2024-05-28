from django.core.files.uploadedfile import InMemoryUploadedFile

from hopla.celery import app


# Se crea este archivo para manejar las tareas asíncronas sin importaciones circulares


def upload_image(ticket_id: int, image_name: str, image_data: str):
    app.send_task(
        "apps.tickets.tasks.upload_image",
        args=[ticket_id, image_name, image_data],
    )
