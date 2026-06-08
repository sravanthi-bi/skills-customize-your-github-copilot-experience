"""
Building REST APIs with FastAPI
Starter Code: Basic FastAPI Application Structure

This file provides a foundation for building a REST API with FastAPI.
Complete the tasks in the assignment to add endpoints and functionality.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI app
app = FastAPI(title="Book API", version="1.0.0")

# Define the Book data model using Pydantic
class Book(BaseModel):
    """Data model for a book"""
    id: int
    title: str
    author: str
    year_published: int


# In-memory database (replace with a real database in production)
books_db: List[Book] = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year_published=1925),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year_published=1960),
    Book(id=3, title="1984", author="George Orwell", year_published=1949),
]


# TODO: Task 1 - Create a GET endpoint at "/" that returns a welcome message
# Example response: {"message": "Welcome to the Book API"}


# TODO: Task 1 - Create a GET endpoint at "/books" that returns the list of all books
# Example response: [{"id": 1, "title": "...", "author": "...", "year_published": ...}, ...]


# TODO: Task 2 - Create a POST endpoint at "/books" that adds a new book
# It should accept a Book object and return a 201 status code


# TODO: Task 3 - Create a GET endpoint at "/books/{book_id}" to get a specific book
# It should return a 404 error if the book doesn't exist


# TODO: Task 3 - Create a PUT endpoint at "/books/{book_id}" to update a book


# TODO: Task 3 - Create a DELETE endpoint at "/books/{book_id}" to delete a book


# TODO: Task 4 - Modify the GET "/books" endpoint to support filtering
# Add optional query parameters: author (str) and year (int)


# To run this application:
# 1. Install FastAPI: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Open http://127.0.0.1:8000/docs to interact with your API using Swagger UI
