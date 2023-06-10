# this Dockerfile is copied from the sample solution from the Judges

FROM python:3.9-slim

WORKDIR /mlflow/

RUN pip install --no-cache-dir mlflow==2.3.2
