import uvicorn
from typing import List
from fastapi import Depends, FastAPI, HTTPException


from api.model import crud, models, schemas
from api.model.database import SessionLocal, engine
from api.routes import algorithm_genetic, food_route, plate_route, export_data


app = FastAPI(
    title="Educanutri API",
    description="API Educanutri",
    version='0.1.0'
)


models.Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"Welcome Educanutri"}


app.include_router(food_route.alimento, tags=['Alimento'])
app.include_router(plate_route.prato, tags=['Prato'])
app.include_router(algorithm_genetic.algoritmo, tags=['Algoritmo genético'])
app.include_router(export_data.data, tags=['Data'])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)