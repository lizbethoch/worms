from fastapi import FastAPI

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Base, Book
from app.schemas import BookResponse

app = FastAPI()

@app.get("/books", response_model=list[BookResponse])
def get_books():
        with Session(engine) as session:
                result = session.execute(select(Book))
                books = result.scalars().all()

        return books