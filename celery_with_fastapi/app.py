import uvicorn
from fastapi import FastAPI, BackgroundTasks
from celery_with_fastapi.worker.celery_app import celery_app
from starlette.responses import RedirectResponse
from celery_with_fastapi.models import RecordsResponseList, RecordDataRequest
from celery_with_fastapi.processor import process_task


app = FastAPI(title="NER", description="Celery", docs_url="/swagger")


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse("/swagger")


@app.post("/process-tasks", response_model=RecordsResponseList)
def extract_entities(body: RecordDataRequest):
    """Extract Named Entities from the input text."""

    entities_results = process_task(body.input_string)
    return {"entities_list": entities_results}

def celery_on_message(body):
    print(body)

def background_on_message(task):
    print(task.get(on_message=celery_on_message, propagate=False))


@app.get("/{word}")
async def root(word: str, background_task: BackgroundTasks):
    task = celery_app.send_task(
        "worker.celery_worker.test_celery", args=[word])
    print(task)
    background_task.add_task(background_on_message, task)
    return {"message": "Word received"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000, log_level="info")



