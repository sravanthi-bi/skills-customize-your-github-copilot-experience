# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using the FastAPI framework. You will create endpoints to manage a collection of books, including reading, creating, updating, and deleting data. By the end of this assignment, you'll understand how to structure API endpoints, handle request/response data, and work with HTTP methods.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Application

#### Description
Set up a basic FastAPI application with a simple GET endpoint that returns a welcome message and book collection list.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Create a GET endpoint at `/` that returns a welcome message with the text `{"message": "Welcome to the Book API"}`
- Create a GET endpoint at `/books` that returns a list of sample books (as JSON)
- Run the application using `uvicorn` and verify both endpoints work in your browser or with a tool like curl/Postman


### 🛠️ Add POST Endpoint to Create Books

#### Description
Extend the API to accept new book submissions through a POST request. You'll need to define a data model for books and handle incoming request data.

#### Requirements
Completed program should:

- Define a Pydantic model `Book` with fields: `id` (int), `title` (str), `author` (str), and `year_published` (int)
- Create a POST endpoint at `/books` that accepts a Book object in the request body
- Store the new book in an in-memory list (you can use a global list variable)
- Return the created book with a 201 status code
- Verify the endpoint works by sending a POST request with JSON data


### 🛠️ Add GET, PUT, and DELETE Endpoints for Individual Books

#### Description
Implement endpoints to retrieve, update, and delete specific books by ID, giving users full CRUD functionality.

#### Requirements
Completed program should:

- Create a GET endpoint at `/books/{book_id}` that returns a specific book by ID, or a 404 error if not found
- Create a PUT endpoint at `/books/{book_id}` that updates a specific book's information
- Create a DELETE endpoint at `/books/{book_id}` that removes a book from the collection
- Test all three endpoints to ensure they work correctly


### 🛠️ Add Query Parameters and Filtering

#### Description
Enhance the GET `/books` endpoint to support filtering and searching, making the API more powerful and practical.

#### Requirements
Completed program should:

- Add an optional `author` query parameter to `/books` that filters books by author name
- Add an optional `year` query parameter to `/books` that filters books published after a given year
- Support combining both filters (if provided)
- Return an empty list if no books match the filter criteria
- Test the filtering functionality with various parameter combinations
