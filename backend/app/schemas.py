from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    description: str | None
    cover_url: str | None
    page_count: int