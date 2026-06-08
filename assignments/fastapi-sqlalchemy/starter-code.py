"""
Database Integration with SQLAlchemy and FastAPI
Starter Code: SQLAlchemy Setup with FastAPI

This file provides the foundation for integrating a SQLite database with your FastAPI application.
Complete the tasks in the assignment to add database operations and relationships.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

# Database URL (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()


# ============================================================================
# DATABASE MODELS
# ============================================================================

class BookModel(Base):
    """Database model for books"""
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    year_published = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # TODO: Task 3 - Add a foreign key to Author model
    # author_id = Column(Integer, ForeignKey("authors.id"))
    # author_rel = relationship("AuthorModel", back_populates="books")


# TODO: Task 3 - Create an Author model with fields: id, name, email
# Add a relationship back to BookModel for one-to-many mapping


# ============================================================================
# PYDANTIC SCHEMAS (for request/response validation)
# ============================================================================

class BookCreate(BaseModel):
    """Schema for creating a book"""
    title: str
    author: str
    year_published: int


class BookUpdate(BaseModel):
    """Schema for updating a book"""
    title: Optional[str] = None
    author: Optional[str] = None
    year_published: Optional[int] = None


class BookResponse(BaseModel):
    """Schema for book responses"""
    id: int
    title: str
    author: str
    year_published: int
    created_at: datetime
    
    class Config:
        from_attributes = True


# TODO: Task 3 - Create AuthorCreate and AuthorResponse Pydantic schemas


# ============================================================================
# DEPENDENCY INJECTION
# ============================================================================

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================================================
# FASTAPI APPLICATION
# ============================================================================

app = FastAPI(title="Book API with Database", version="2.0.0")


# Initialize the database
@app.on_event("startup")
def startup_event():
    """Create database tables on startup"""
    Base.metadata.create_all(bind=engine)


# ============================================================================
# BOOK ENDPOINTS
# ============================================================================

# TODO: Task 2 - Implement GET /books endpoint that queries all books from database
# Use: db.query(BookModel).all()
# Return: List of BookResponse


# TODO: Task 2 - Implement POST /books endpoint that creates a new book
# Use: db.add() and db.commit()
# Return: BookResponse with 201 status code


# TODO: Task 2 - Implement GET /books/{book_id} endpoint
# Use: db.query(BookModel).filter(BookModel.id == book_id).first()
# Return: BookResponse or 404 if not found


# TODO: Task 2 - Implement PUT /books/{book_id} endpoint to update a book
# Use: update model attributes, then db.commit()
# Return: Updated BookResponse


# TODO: Task 2 - Implement DELETE /books/{book_id} endpoint
# Use: db.delete() and db.commit()
# Return: {"message": "Book deleted"}


# ============================================================================
# AUTHOR ENDPOINTS (Task 3)
# ============================================================================

# TODO: Task 3 - Implement GET /authors endpoint
# TODO: Task 3 - Implement POST /authors endpoint
# TODO: Task 3 - Implement GET /authors/{author_id} endpoint
# TODO: Task 3 - Implement DELETE /authors/{author_id} endpoint (with cascade)


# ============================================================================
# SETUP INSTRUCTIONS
# ============================================================================

"""
To run this application:

1. Install required packages:
   pip install fastapi uvicorn sqlalchemy

2. Run the server:
   uvicorn starter-code:app --reload

3. Access the API:
   - Interactive docs: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

4. For Alembic migrations (Task 4):
   pip install alembic
   alembic init alembic
   
   Then configure alembic/env.py to use your database URL and models.
"""
