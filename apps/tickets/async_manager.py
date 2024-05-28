from hopla.celery import app


def upload_image(ticket_id: int, image: str):
    app.send_task(
        "apps.tickets.tasks.upload_image",
        args=[],
    )
