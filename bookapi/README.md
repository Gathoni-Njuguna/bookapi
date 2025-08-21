# BookAPI

BookAPI is a RESTful API for managing a collection of books. It allows users to create, read, update, and delete book records.

## Features

- Add new books to the collection
- Retrieve details of all books or a single book
- Update existing book information
- Delete books from the collection

## Technologies Used

- Python
- Django / Django REST Framework (DRF)
- SQLite (default) or other supported databases

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Gathoni-Njuguna/bookapi.git
    cd bookapi
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

| Method | Endpoint         | Description           |
|--------|-----------------|-----------------------|
| GET    | /api/books/     | List all books        |
| POST   | /api/books/     | Create a new book     |
| GET    | /api/books/{id}/| Retrieve a book       |
| PUT    | /api/books/{id}/| Update a book         |
| DELETE | /api/books/{id}/| Delete a book         |

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.