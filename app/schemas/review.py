from pydantic import BaseModel
from datetime import datetime


class ReviewBase(BaseModel):
    contact_number: str
    user_name: str
    product_name: str
    product_review: str


class ReviewCreate(ReviewBase):
    pass


class ReviewOut(ReviewBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True