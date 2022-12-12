from celery_with_fastapi.models import RecordsResponse, RecordDataRequest, RecordsResponseList

def process_task(input_text: str) -> RecordsResponseList:
    return [RecordsResponse(output_string = f'Request accepted for {input_text}')]