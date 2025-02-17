from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class BasePydanticModel(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class MakeSchema(BasePydanticModel):
    name: str


class ModelSchema(BasePydanticModel):
    name: str
    make_id: int


class SubModelSchema(BasePydanticModel):
    name: str
    model_id: int


class CarSchema(BasePydanticModel):
    name: str
    make_id: int
    year: int
    color: str
    category: str
    engine_type: str
    seats: Optional[int] = 0
    transmission: str
    top_speed: Optional[int] = 0
    model_id: int
    sub_model_id: int
