from pydantic import BaseModel
from typing import List

class DashboardStats(BaseModel):
    total_questions: int
    top_topics: List[str]
    weak_areas: List[str]
