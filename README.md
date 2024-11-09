#Django User Management System

A Django-based web application for managing users with MySQL as the database. This system provides module access control, allowing admins to assign access to specific modules for each user.

### Prerequisites

1. Python (version 3.8 or higher)
2. MySQL database server
3. Django (version 3.x or higher)

## Installation

1. **Create Project folder**
   Open that folder in your code editor.

2. **Create a virtual environment and install dependencies**:

   ```bash
   virtualenv "your env name"
   "your env name"\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure MySQL Database**:

   - Create a new MySQL database.
   - Update the `DATABASES` setting in `settings.py` with your MySQL configuration:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Open `http://127.0.0.1:8000` in your browser.
   - Login as an admin at `http://127.0.0.1:8000/admin`.

## Usage

- **User Management**:
  - Admins can create and manage users with specific access permissions.
  - Access the user list at `/users/list/`.

## Project Structure

- **models.py**: Contains the custom `CustomUser` model for module access control.
- **views.py**: Contains views for user creation, listing, updating, and deleting.
- **urls.py**: Configures the routes for user management.
- **templates/**: Contains HTML templates, including user list , update and delete.

## API Endpoints

Method - Endpoint- Description
Get - /users/list/ - List all users
Post - /users/create/ - Creates a new user
Post - /users/<int:pk>/edit/ - Edit a user
Post - /users/<int:pk>/delete/ - Delete a user

This is a basic user management system. Feel free to customize and extend it for your own needs.
