
# My Django Project

## Description

This is a Django project for managing clients and projects with CRUD functionality.

## Features

- List all clients
- Create a new client
- Retrieve client details along with associated projects
- Update client information
- Delete clients
- Create new projects
- List projects assigned to the logged-in user
- Delete projects

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

- **Clients**
  - `GET /clients/` - List of all clients
  - `POST /clients/` - Create a new client
  - `GET /clients/:id/` - Retrieve information of a client
  - `PUT /clients/:id/` - Update information of a client
  - `DELETE /clients/:id/` - Delete a client

- **Projects**
  - `POST /projects/` - Create a new project
  - `GET /projects/` - List of all projects assigned to the logged-in user
  - `DELETE /projects/:id/` - Delete a project





## Deployment

To deploy this project run

```bash
  npm run deploy
```

