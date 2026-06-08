# 📘 Assignment: Database Integration with SQLAlchemy and FastAPI

## 🎯 Objective

Move beyond in-memory data storage by integrating a SQLite database into your FastAPI application using SQLAlchemy ORM. You will learn how to define database models, manage database sessions, perform CRUD operations on persistent data, and handle relationships between entities.

## 📝 Tasks

### 🛠️ Set Up SQLAlchemy and Create Database Models

#### Description
Initialize SQLAlchemy with FastAPI and define a Book model that maps to a database table. Create the database and understand how ORM models work.

#### Requirements
Completed program should:

- Install SQLAlchemy and create a database connection to SQLite
- Define a `Book` model with fields: `id`, `title`, `author`, `year_published`, and `created_at` (timestamp)
- Create a `SessionLocal` function to manage database sessions
- Initialize the database with `Base.metadata.create_all()`
- Verify the SQLite database file is created


### 🛠️ Migrate API Endpoints to Use Database Queries

#### Description
Refactor the FastAPI endpoints from the previous assignment to use SQLAlchemy queries instead of in-memory lists. Replace your mock data with database operations.

#### Requirements
Completed program should:

- Update GET `/books` to query all books from the database
- Update POST `/books` to insert new books into the database
- Update GET `/books/{book_id}` to query a specific book by ID from the database
- Update PUT `/books/{book_id}` to modify an existing book in the database
- Update DELETE `/books/{book_id}` to remove a book from the database
- All endpoints should use proper database session management and error handling


### 🛠️ Add Relationship Models and Implement Author Management

#### Description
Extend the database schema to include an Author model and establish a relationship between books and authors. Implement endpoints to manage authors.

#### Requirements
Completed program should:

- Create an `Author` model with fields: `id`, `name`, and `email`
- Establish a one-to-many relationship (one author can write many books)
- Modify the Book model to include a foreign key to Author
- Create endpoints: POST, GET, DELETE for authors
- Update book endpoints to accept an `author_id` instead of author name
- Implement cascade delete behavior (deleting an author deletes their books)


### 🛠️ Add Database Migrations with Alembic (Stretch Goal)

#### Description
Learn version control for your database schema using Alembic, the migration tool for SQLAlchemy. Create and apply migrations as you modify your data model.

#### Requirements
Completed program should:

- Initialize Alembic in your project
- Create an initial migration for the current database schema
- Add a new field to the Book model (e.g., `isbn` or `genre`)
- Generate an auto-migration for the schema change
- Apply the migration and verify the database updates
