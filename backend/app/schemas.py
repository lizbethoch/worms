from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: str
    description: str | None
    cover_url: str | None
    page_count: int

class BookCreate(BaseModel):
    title: str
    author: str
    description: str | None = None
    cover_url: str | None = None
    page_count: int

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    description: str | None = None
    cover_url: str | None = None
    page_count: int | None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserBookCreate(BaseModel):
    book_id: int
    status: Literal["want_to_read", "currently_reading", "read"]
    access_type: Literal[
        "physical",
        "ebook",
        "audiobook",
        "borrowed_from_library",
        "need_to_purchase",
    ]
    current_page: int = Field(default=0, ge=0)


class UserBookUpdate(BaseModel):
    status: Literal[
        "want_to_read",
        "currently_reading",
        "read",
    ] | None = None

    access_type: Literal[
        "physical",
        "ebook",
        "audiobook",
        "borrowed_from_library",
        "need_to_purchase",
    ] | None = None

    current_page: int | None = Field(default=None, ge=0)

class UserBookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    book_id: int
    status: str
    access_type: str
    current_page: int