# Weather Forecast API with Python & FastAPI

This project provides a simple Weather Forecast API built with **Python** and **FastAPI**, designed for deployment and management using **Azure API Management**.

## Features

- RESTful endpoints for weather data
- FastAPI for high performance and easy development
- Ready for Azure API Management integration

## Prerequisites

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (for local development)
- Azure Subscription (for API Management)

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Install dependencies:**
    ```bash
    pip install fastapi uvicorn
    ```

3. **Run the API locally:**
    ```bash
    uvicorn main:app --reload
    ```

4. **Access the API docs:**
    - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## Deploying to Azure API Management

1. Deploy your FastAPI app to Azure (e.g., Azure App Service or Azure Container Apps).
2. Import your API into Azure API Management.
3. Configure policies, security, and monitoring as needed.

## Example Endpoint

```http
GET /weather
```

**Response:**
```json
{
  "city": "London",
  "temperature": 18,
  "description": "Cloudy"
}
```

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Azure API Management Documentation](https://learn.microsoft.com/en-us/azure/api-management/)

---

© 2025 Everton Vasconcelos