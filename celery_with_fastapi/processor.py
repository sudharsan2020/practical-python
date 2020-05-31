from celery_with_fastapi.models import RecordsResponse, RecordDataRequest, RecordsResponseList

def process_task(input_text: str) -> RecordsResponseList:
    tasks_list= []
    tasks_list.append(
        RecordsResponse(
        output_string = f'Request accepted for {input_text}'
    ))
    return tasks_list