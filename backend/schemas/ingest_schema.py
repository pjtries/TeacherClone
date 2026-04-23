from pydantic import BaseModel

class IngestResponse(BaseModel):
    file_id: str
    status: str

class StatusResponse(BaseModel):
    file_id: str
    status: str
