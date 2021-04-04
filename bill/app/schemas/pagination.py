from typing import Optional

from pydantic import BaseModel


class PaginationInfo(BaseModel):
    total_pages: Optional[int]
    total_number_of_items: Optional[int]
    current_page: Optional[int]
    previous_page: Optional[int]
    next_page: Optional[int]


class PaginationResponse(BaseModel):
    pagination: Optional[PaginationInfo]
