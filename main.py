from fastapi import FastAPI
from api.routes import algoritmo_genetico
import uvicorn


app = FastAPI(
    title="Educanutri API",
    description="API Educanutri",
    version='0.1.0'
)


@app.get("/")
def index():
    return {"Welcome Educanutri"}

app.include_router(algoritmo_genetico.algoritmo, tags=['Algoritmo genético'])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
