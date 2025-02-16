from pydantic import BaseModel, Field


class MakeSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)


class ModelSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    make: int
