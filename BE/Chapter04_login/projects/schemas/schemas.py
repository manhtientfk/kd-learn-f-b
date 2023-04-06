from datetime import date, datetime, time
from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional


class Account(BaseModel):
    us : str
    pw : str
