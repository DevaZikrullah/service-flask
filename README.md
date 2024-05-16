# Flask Application

This is a Flask application using Flask-RESTful for API endpoints, SQLAlchemy for database ORM, Flask-Migrate for database migrations, and Flask-JWT-Extended for JWT authentication.

## Installation

### Using Virtual Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/DevaZikrullah/service-flask.git
   cd service-flask
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Using Docker Compose

1. Clone the repository:

   ```bash
   git clone https://github.com/DevaZikrullah/service-flask.git
   cd service-flask
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

## Usage

### Running with Virtual Environment

```bash
# Activate virtual environment if not activated
source venv/bin/activate   # On Windows use `venv\Scripts\activate`


### Running with Docker Compose

```bash
# Build and run Docker containers
docker-compose up
```


## API Documentation

Document your API endpoints and any other relevant information here.

## License

This project is licensed under the [MIT License](LICENSE).
