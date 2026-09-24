from datetime import datetime, timezone

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Book, Review, User, UserBook
from app.schemas import (
    BookCreate,
    BookResponse,
    BookUpdate,
    UserBookCreate,
    UserBookResponse,
    UserBookUpdate,
    UserCreate,
    UserLogin,
    ReviewCreate,
    ReviewResponse,
    ReviewUpdate,
)
from app.security import (
    create_access_token,
    hash_password,
    verify_access_token,
    verify_password,
)

app = FastAPI()

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    try:
        user_id = verify_access_token(token)
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    with Session(engine) as session:
        result = session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user

@app.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
    }

@app.post("/user-books", response_model=UserBookResponse)
def add_book_to_library(
    user_book: UserBookCreate,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(Book).where(Book.id == user_book.book_id)
        )
        book = result.scalar_one_or_none()

        if book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )
        if user_book.current_page > book.page_count:
            raise HTTPException(
                status_code=400,
                detail="Current page cannot exceed the book's page count",
            )

        new_user_book = UserBook(
            user_id=current_user.id,
            book_id=user_book.book_id,
            status=user_book.status,
            access_type=user_book.access_type,
            current_page=user_book.current_page,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        session.add(new_user_book)
        session.commit()
        session.refresh(new_user_book)

        return new_user_book

@app.get("/user-books", response_model=list[UserBookResponse])
def get_user_books(
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(UserBook).where(UserBook.user_id == current_user.id)
        )

        user_books = result.scalars().all()

        return user_books

@app.get("/user-books/{user_book_id}", response_model=UserBookResponse)
def get_user_book(
    user_book_id: int,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(UserBook).where(
                UserBook.id == user_book_id,
                UserBook.user_id == current_user.id,
            )
        )

        user_book = result.scalar_one_or_none()

        if user_book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        return user_book

@app.patch("/user-books/{user_book_id}", response_model=UserBookResponse)
def update_user_book(
    user_book_id: int,
    user_book: UserBookUpdate,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(UserBook).where(
                UserBook.id == user_book_id,
                UserBook.user_id == current_user.id,
            )
        )

        existing_user_book = result.scalar_one_or_none()

        if existing_user_book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        book_result = session.execute(
            select(Book).where(Book.id == existing_user_book.book_id)
        )

        book = book_result.scalar_one_or_none()

        if book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        updates = user_book.model_dump(exclude_unset=True)

        if "current_page" in updates:
            if updates["current_page"] > book.page_count:
                raise HTTPException(
                    status_code=400,
                    detail="Current page cannot exceed the book's page count",
                )

        for field, value in updates.items():
            setattr(existing_user_book, field, value)

        existing_user_book.updated_at = datetime.now(timezone.utc)

        session.commit()
        session.refresh(existing_user_book)

        return existing_user_book

@app.delete("/user-books/{user_book_id}")
def delete_user_book(
    user_book_id: int,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(UserBook).where(
                UserBook.id == user_book_id,
                UserBook.user_id == current_user.id,
            )
        )

        existing_user_book = result.scalar_one_or_none()

        if existing_user_book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        session.delete(existing_user_book)
        session.commit()

        return {"detail": "Book removed from library"}

@app.get("/books", response_model=list[BookResponse])
def get_books():
        with Session(engine) as session:
                result = session.execute(select(Book))
                books = result.scalars().all()

        return books

@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    with Session(engine) as session:
        now = datetime.now(timezone.utc)

        new_book = Book(
            title=book.title,
            author=book.author,
            description=book.description,
            cover_url=book.cover_url,
            page_count=book.page_count,
            created_at=now,
            updated_at=now,
        )

        session.add(new_book)
        session.commit()
        session.refresh(new_book)

        return new_book

@app.patch("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    with Session(engine) as session:
        result = session.execute(
            select(Book).where(Book.id == book_id)
        )
        existing_book = result.scalar_one_or_none()

        if existing_book is None:
            return {"detail": "Book not found"}

        updates = book.model_dump(exclude_unset=True)

        for field, value in updates.items():
                setattr(existing_book, field, value)

        existing_book.updated_at = datetime.now(timezone.utc)

        session.commit()
        session.refresh(existing_book)

        return existing_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    with Session(engine) as session:
        result = session.execute(
            select(Book).where(Book.id == book_id)
        )
        existing_book = result.scalar_one_or_none()

        if existing_book is None:
            return {"detail": "Book not found"}

        session.delete(existing_book)
        session.commit()

        return {"detail": "Book deleted successfully"}

@app.post("/users")
def create_user(user: UserCreate):
    with Session(engine) as session:
        password_hash = hash_password(user.password)

        now = datetime.now(timezone.utc)

        new_user = User(
            username=user.username,
            email=user.email,
            password_hash=password_hash,
            created_at=now,
            updated_at=now,
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return {"id": new_user.id, "username": new_user.username, "email": new_user.email}

@app.post("/login")
def login(user: UserLogin):
    with Session(engine) as session:
        result = session.execute(
            select(User).where(User.email == user.email)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user is None:
            return {"detail": "Invalid email or password"}

        if not verify_password(user.password, existing_user.password_hash):
            return {"detail": "Invalid email or password"}

        access_token = create_access_token(existing_user.id)

        return {
                "message": "Login successful",
                "access_token": access_token,
                "user_id": existing_user.id,
                "username": existing_user.username,
        }

@app.post("/reviews", response_model=ReviewResponse)
def create_review(
    review: ReviewCreate,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(UserBook).where(
                UserBook.id == review.user_book_id,
                UserBook.user_id == current_user.id,
            )
        )

        user_book = result.scalar_one_or_none()

        if user_book is None:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        existing_review_result = session.execute(
            select(Review).where(
                Review.user_book_id == review.user_book_id
            )
        )

        existing_review = existing_review_result.scalar_one_or_none()

        if existing_review is not None:
            raise HTTPException(
                status_code=409,
                detail="Review already exists for this book",
            )

        now = datetime.now(timezone.utc)

        new_review = Review(
            user_book_id=review.user_book_id,
            rating=review.rating,
            review_text=review.review_text,
            created_at=now,
            updated_at=now,
        )

        session.add(new_review)
        session.commit()
        session.refresh(new_review)

        return new_review

@app.get("/reviews/{review_id}", response_model=ReviewResponse)
def get_review(
    review_id: int,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(Review)
            .join(UserBook, Review.user_book_id == UserBook.id)
            .where(
                Review.id == review_id,
                UserBook.user_id == current_user.id,
            )
        )

        review = result.scalar_one_or_none()

        if review is None:
            raise HTTPException(
                status_code=404,
                detail="Review not found",
            )

        return review

@app.patch("/reviews/{review_id}", response_model=ReviewResponse)
def update_review(
    review_id: int,
    review: ReviewUpdate,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(Review)
            .join(UserBook, Review.user_book_id == UserBook.id)
            .where(
                Review.id == review_id,
                UserBook.user_id == current_user.id,
            )
        )

        existing_review = result.scalar_one_or_none()

        if existing_review is None:
            raise HTTPException(
                status_code=404,
                detail="Review not found",
            )

        updates = review.model_dump(exclude_unset=True)

        for field, value in updates.items():
            setattr(existing_review, field, value)

        existing_review.updated_at = datetime.now(timezone.utc)

        session.commit()
        session.refresh(existing_review)

        return existing_review

@app.delete("/reviews/{review_id}")
def delete_review(
    review_id: int,
    current_user: User = Depends(get_current_user),
):
    with Session(engine) as session:
        result = session.execute(
            select(Review)
            .join(UserBook, Review.user_book_id == UserBook.id)
            .where(
                Review.id == review_id,
                UserBook.user_id == current_user.id,
            )
        )

        existing_review = result.scalar_one_or_none()

        if existing_review is None:
            raise HTTPException(
                status_code=404,
                detail="Review not found",
            )

        session.delete(existing_review)
        session.commit()

        return {"detail": "Review deleted successfully"}