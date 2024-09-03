from pydantic import BaseModel
from typing import List


class PortfolioRequest(BaseModel):
    assets: List[str]
    start_date: str
    end_date: str
