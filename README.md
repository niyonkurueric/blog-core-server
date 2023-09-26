# blog-core-server
blog-core-server


## Getting Started

Follow these steps to get the project up and running on your local environment:

### Prerequisites

Make sure you have Python and Sqlite installed on your system.

### Installation

1. Clone the repository to your local machine:

    ```
    git clone github-link
    ```

2. Change to the project directory:

    ```
    cd blog-server
   

4. Create the Sqlite database by running migrations:

    ```
    python manage.py migrate
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

### Accessing the Django Admin

To access the Django admin panel, you'll need to create a superuser account:
 ```
    python manage.py createsuperuser
    Username: admin
    Email address: admin@example.com
    ```

Follow the prompts to set up your admin account, and then you can access the admin panel at `/admin`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django - The web framework used
- Bootstrap - The front-end framework used
- Sqlite - The database system used
