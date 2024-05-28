import base64

from django.core.files.uploadedfile import InMemoryUploadedFile

from hopla.celery import app
from django.core.files.base import ContentFile
import cloudinary.uploader
from .models import Ticket, ImageUpload


@app.task
def upload_image(ticket_id, filename, image_data_base64):
    ticket = Ticket.objects.get(id=ticket_id)

    # Decodificar el archivo desde base64
    image_data = base64.b64decode(image_data_base64)
    image_content = ContentFile(image_data, name=filename)

    response = cloudinary.uploader.upload(image_content)
    image_url = response.get("secure_url")

    ImageUpload.objects.create(ticket=ticket, image=image_url)
