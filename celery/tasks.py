from celery import Celery
from api.src.config import settings

app = Celery(
    "ai_request_handler",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

app.conf.update(
    task_serializer="json",
    accept_content=["application/json"],
    result_serializer="json",
    task_track_started=True,
    task_time_limit=300,
    task_soft_time_limit=60,
    worker_prefetch_multiplier=1,
    result_expires=3600,
)


@app.task(name="process_request_async")
def process_request_async(text: str) -> str:
    """
    Asynchronously processes user requests using the OpenAI API.

    Args:
        text: The user's request text.

    Returns:
        A formatted OpenAI response.
    """
    try:
        # Import necessary modules here to avoid circular imports
        from api.src.services.request_service import process_request

        response = process_request(text)  # Use the existing request_service function
        return response
    except Exception as e:
        # Log the error using the appropriate logger (e.g., using the `app.logger`)
        # app.logger.error(f"Error processing request: {e}")
        raise


if __name__ == "__main__":
    app.start()