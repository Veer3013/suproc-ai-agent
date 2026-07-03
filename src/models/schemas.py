from typing import List, Optional
from pydantic import BaseModel


class Requirement(BaseModel):
    category: str
    location: str
    certification: Optional[str] = None
    min_capacity: Optional[int] = None
    max_delivery_days: Optional[int] = None
    top_k: int = 3


class SupplierResponse(BaseModel):
    id: str
    name: str
    category: str
    location: str
    certification: str
    capacity: int
    delivery_days: int
    rating: float
    available: bool


class SearchResult(BaseModel):
    query: Requirement
    suppliers: List[SupplierResponse]