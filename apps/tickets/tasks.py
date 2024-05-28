from hopla.celery import app

from .models import Ticket


@app.task
def upload_image():
    print("Uploading image...")
