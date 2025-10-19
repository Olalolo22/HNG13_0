Project is a dynamic RESTful API built with Python FastAPI, designed to serve personalized user profile information enhanced with real-time cat facts! 🚀 This project demonstrates robust API development, asynchronous operations, and seamless integration with external services, perfect for showcasing modern backend skills. ✨

# Profile API with Cat Facts

## Overview
A high-performance RESTful API developed with Python and FastAPI, designed to provide user profile information dynamically augmented with randomized cat facts fetched from an external API.

## Features
- `FastAPI`: High-performance, asynchronous web framework for building robust APIs.
- `httpx`: Asynchronous HTTP client for efficient external API calls to `catfact.ninja`.
- `python-dotenv`: Seamless management of environment variables for configuration.
- `CORS Middleware`: Configured for flexible Cross-Origin Resource Sharing.
- `Structured Logging`: Implemented for enhanced operational monitoring and debugging.
- `Automatic API Documentation`: Built-in interactive API documentation (`/docs`, `/redoc`).

## Getting Started
### Installation
Follow these steps to set up the project locally:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Olalolo22/HNG13_0.git
    cd HNG13_0
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment**:
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables
Create a `.env` file in the root directory of the project and define the following variables. These are crucial for configuring the API's behavior and user profile details.

```env
PORT=8000
CAT_FACT_API_URL=https://catfact.ninja/fact
API_TIMEOUT=5
USER_EMAIL=your.email@example.com
USER_NAME=Your Full Name
USER_STACK=Python/FastAPI
```
*   `PORT`: The port on which the FastAPI application will run (default: `8000`).
*   `CAT_FACT_API_URL`: The URL of the external Cat Facts API (default: `https://catfact.ninja/fact`).
*   `API_TIMEOUT`: Timeout in seconds for external API requests (default: `5`).
*   `USER_EMAIL`: The email address to be displayed in the profile (default: `your.email@example.com`).
*   `USER_NAME`: The full name to be displayed in the profile (default: `Your Full Name`).
*   `USER_STACK`: The technology stack to be displayed in the profile (default: `Python/FastAPI`).

## API Documentation
### Base URL
The API is accessible at: `http://localhost:8000` (or your deployed instance URL).

### Endpoints
#### GET /me
Retrieves a personalized user profile, including a dynamic cat fact.

**Request**:
No request payload required.

**Response**:
```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2023-10-27T10:30:00.123456+00:00",
  "fact": "Cats sleep 70% of their lives."
}
```

**Errors**:
- `500 Internal Server Error`: Occurs if there's an issue fetching the cat fact from the external API (e.g., timeout, network error, or API unavailability). The `fact` field will contain a fallback message.

#### GET /
Provides basic information about the API and its main endpoints.

**Request**:
No request payload required.

**Response**:
```json
{
  "message": "Profile API with Cat Facts",
  "endpoints": {
    "/me": "GET - Returns profile information with a cat fact",
    "/docs": "GET - Interactive API documentation",
    "/redoc": "GET - Alternative API documentation"
  }
}
```

**Errors**:
No specific error scenarios documented for this endpoint under normal operation.

#### GET /health
A simple health check endpoint to verify the API's operational status.

**Request**:
No request payload required.

**Response**:
```json
{
  "status": "healthy",
  "timestamp": "2023-10-27T10:35:00.123456+00:00"
}
```

**Errors**:
No specific error scenarios documented for this endpoint under normal operation.

## Usage
After installation and setting environment variables, run the application:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT --reload
```
Alternatively, if you are using the `Procfile` for deployment (e.g., on Heroku), the command is:
```bash
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Once the server is running, you can access the API endpoints:

*   **View your profile**: Open `http://localhost:8000/me` in your browser or use a tool like cURL:
    ```bash
    curl http://localhost:8000/me
    ```

*   **Check API status**: Navigate to `http://localhost:8000/health`.

*   **Explore interactive documentation**: Visit `http://localhost:8000/docs` (Swagger UI) or `http://localhost:8000/redoc` (ReDoc).

## Technologies Used
| Technology         | Description                                        | Version |
| :----------------- | :------------------------------------------------- | :------ |
| Python             | Primary programming language                       | 3.10.12 |
| FastAPI            | Modern, fast (high-performance) web framework      | 0.115.0 |
| Uvicorn            | ASGI server for running FastAPI applications       | 0.31.0  |
| httpx              | Asynchronous HTTP client for making API requests   | 0.27.2  |
| python-dotenv      | Manages environment variables from a `.env` file   | 1.0.1   |
| Pydantic           | Data validation and settings management            | 2.9.2   |

## Contributing
We welcome contributions to enhance this project! To contribute:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3.  **Implement your changes**, ensuring they adhere to the project's coding standards.
4.  **Write comprehensive tests** for your new code.
5.  **Commit your changes** with a clear and concise message: `git commit -m "feat: Add new feature X"`.
6.  **Push your branch** to your forked repository: `git push origin feature/your-feature-name`.
7.  **Open a Pull Request** to the `main` branch of the original repository, describing your changes in detail.

## Author Info
*   **Name**: [Your Full Name]
*   **LinkedIn**: [Your LinkedIn Profile URL]
*   **Twitter**: [Your Twitter Handle URL]
*   **Portfolio**: [Your Portfolio Website URL]

## Badges
[![Python 3.10.12](https://img.shields.io/badge/Python-3.10.12-blue?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-31012/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.31.0-orange?logo=uvicorn&logoColor=white)](https://www.uvicorn.org/)
[![HTTPX](https://img.shields.io/badge/HTTPX-0.27.2-red?logo=httpx&logoColor=white)](https://www.python-httpx.org/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-1.0.1-purple?logo=dot-env&logoColor=white)](https://github.com/theskumar/python-dotenv)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.9.2-green?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/latest/)
[![Deploy on Heroku](https://img.shields.io/badge/Deploy%20on-Heroku-430098?style=flat&logo=heroku&logoColor=white)](https://heroku.com/deploy?template=https://github.com/Olalolo22/HNG13_0)

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://www.npmjs.com/package/dokugen)