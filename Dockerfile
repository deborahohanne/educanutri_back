FROM python:3

RUN mkdir code/
COPY . code/
WORKDIR /code/educanutri_api
COPY requirements.txt /code/educanutri_api

RUN pip3 install -r requirements.txt
    
WORKDIR /code

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
