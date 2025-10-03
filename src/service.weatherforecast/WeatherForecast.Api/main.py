from fastapi import FastAPI

app = FastAPI(title="Weather Forecast API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Weather Forecast Service"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/weather")
def get_weather():
    return {"temperature": 22, "condition": "sunny"}