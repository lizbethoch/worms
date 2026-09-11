from sqlalchemy import BigInteger, CheckConstraint, Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    cover_url = Column(Text, nullable=True)
    page_count = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

class UserBook(Base):
    __tablename__ = "user_books"

    id = Column(BigInteger, primary_key=True)

    user_id = Column(
        BigInteger, 
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    book_id = Column(
        BigInteger,
        ForeignKey("books.id"),
        nullable=False
    )

    status = Column(String(20), nullable=False)

    access_type = Column(String(30), nullable=False)

    current_page = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "status IN ('want_to_read', 'currently_reading', 'read')",
            name="user_books_status_check"
        ),
        CheckConstraint(
            "access_type IN ('physical', 'ebook', 'audiobook', 'borrowed_from_library', 'need_to_purchase')",
            name="user_books_access_type_check"
        ),
        CheckConstraint(
            "current_page >= 0",
            name="user_books_current_page_check"
        ),
    )

class Review(Base):
    __tablename__ = "reviews"

    id = Column(BigInteger, primary_key=True)

    user_book_id = Column(
        BigInteger,
        ForeignKey("user_books.id", ondelete="CASCADE"),
        nullable=False
    )

    rating = Column(
        Numeric(2, 1),
        nullable=True
    )

    review_text = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "rating >= 0.5 AND rating <= 5.0 AND MOD(rating * 10, 5) = 0",
            name="reviews_rating_check"
        ),
    )