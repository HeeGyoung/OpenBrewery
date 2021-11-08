from enum import Enum
from typing import Optional

from fastapi import FastAPI

from handler import get_by_state, get_by_type

app = FastAPI()


class Types(str, Enum):
    MICRO = "micro"
    NANO = "nano"
    REGIONAL = "regional"
    BREWPUP = "brewpub"
    LARGE = "large"
    PLANNING = "planning"
    BAR = "bar"
    CONTRACT = "contract"
    PROPRIETOR = "proprietor"
    CLOSED = "closed"


@app.get("/state/{state}")
def list_by_state(state: str, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None):
    return get_by_state(state, page, per_page, sort)


@app.get("/type/{type}/")
def list_by_type(type: Types, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None):
    return get_by_type(type, page, per_page, sort)