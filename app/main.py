from fastapi import FastAPI

from .db import engine, session_local
from .problem.api_models.factory import ModelCreator
from .problem.api_models import Base
from .problem.schema import RequestSchema

Base.metadata.create_all(bind=engine)
app = FastAPI()
model_creator = ModelCreator()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
async def recieve(phase_id: int, prob_id: int, request_data: RequestSchema):
    session = session_local()
    api_model = model_creator.create_model(phase_id, prob_id)

    for info in request_data["columns"]:
        # add each record to the db
        record = {
            col_name: info[idx]
            for idx, col_name in enumerate(request_data["rows"])
        }
        session.add(api_model(**record, request_id=request_data["id"]))
        session.commit()

    return {
        "phase_id": phase_id,
        "prob_id": prob_id,
        # response with the number of records added to the db
        "message": f'success: {len(request_data["rows"])} records added to db',
    }
