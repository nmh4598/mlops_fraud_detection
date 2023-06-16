from pydantic import BaseModel
from typing import List, Union


class BaseSchema(BaseModel):
    id: int

    def __getitem__(self, item):
        return getattr(self, item)


class RequestSchema(BaseSchema):
    """Data Scheme of the Request Body,
    that will be received by /predict/ route

    - `id` of the request
    - `rows` contains names of features
    - `columns` 2D array data
    """

    rows: List[str]
    columns: List[List[Union[None, float, int, str, bool]]]


class ResponseSchema(BaseSchema):
    """Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `rows` contains names of features
    - `columns` 2D array data
    """

    predictions: List[Union[None, float, int, str, bool]]
