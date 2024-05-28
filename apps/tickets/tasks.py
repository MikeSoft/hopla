import base64

import cloudinary.uploader
from django.core.files.base import ContentFile

from hopla.celery import app
from .models import Ticket, ImageUpload


@app.task
def upload_image(ticket_id, filename, image_data_base64):
    ticket = Ticket.objects.prefetch_related("uploaded_images").get(id=ticket_id)

    # Decodificar el archivo desde base64
    image_data = base64.b64decode(image_data_base64)
    image_content = ContentFile(image_data, name=filename)

    response = cloudinary.uploader.upload(image_content)
    image_url = response.get("secure_url")

    ImageUpload.objects.create(ticket=ticket, image=image_url)

    if ticket.num_images >= ImageUpload.objects.filter(ticket=ticket).count():
        ticket.status = Ticket.STATUS_CHOICES.COMPLETE
        ticket.save()
