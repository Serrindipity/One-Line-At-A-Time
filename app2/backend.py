from typing import Optional
from sqlmodel import Field
import reflex as rx

class Lines(rx.Model, table=True):
    ip: Optional[str] = Field(default=None, primary_key=True)
    line: str
    timestamp: str