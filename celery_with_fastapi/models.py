from pydantic import BaseModel
from typing import List


class RecordDataRequest(BaseModel):
    input_string: str

class RecordsResponse(BaseModel):
    output_string: str

class RecordsResponseList(BaseModel):
    entities_list: List[RecordsResponse]


