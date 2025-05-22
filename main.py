from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WeatherResponse(BaseModel):
    city: str
    temperature_celsius: float
    description: str


weather_data = {
    "belem": {"temperature_celsius": 35.0, "description": "Sunny"},
    "brasilia": {"temperature_celsius": 25.0, "description": "Sunny"},
    "tokyo": {"temperature_celsius": 22.0, "description": "Sunny"},
    "sydney": {"temperature_celsius": 25.0, "description": "Sunny"},
    "mumbai": {"temperature_celsius": 30.0, "description": "Humid"},
    "cairo": {"temperature_celsius": 35.0, "description": "Hot"},
    "london": {"temperature_celsius": 15.0, "description": "Cloudy"},
    "paris": {"temperature_celsius": 18.0, "description": "Sunny"},
    "new york": {"temperature_celsius": 20.0, "description": "Rainy"},

}

@app.get("/weather/{city}", response_model=WeatherResponse)
def get_weather(city: str):
    city_lower = city.lower()
    if city_lower in weather_data:
        data = weather_data[city_lower]
        return WeatherResponse(city=city.title(), **data)
    return {"error": "City not found"}