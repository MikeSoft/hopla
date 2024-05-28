from app.celery_init import app


def upload_image(ticket_id: int, image: str):
    app.send_task(
        "apps.tasks.upload_image",
        args=[],
    )
