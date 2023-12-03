from dataclasses import dataclass


@dataclass
class Config:
    mail: str
    password: str
