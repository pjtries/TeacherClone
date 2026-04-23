from pydantic import BaseModel
from typing import List

class DashboardResponse(BaseModel):
    total_questions: int
    top_topics: List[str]
    weak_areas: List[str]
    recent_questions: List[str]
