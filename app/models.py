# Класс для хранения данных

from dataclasses import dataclass
from typing import List


# Можно и обойтись без датакласса, но тогда сделать через список экземпляров класса
@dataclass
class Developer:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: List[str]
    team: str
    experience_years: int

    @classmethod
    def from_dict(cls, data: dict):
        """Создает объект Developer из словаря"""
        return cls(
            name=data["name"],
            position=data["position"],
            completed_tasks=int(data["completed_tasks"]),
            performance=float(data["performance"]),
            skills=[skill.strip() for skill in data["skills"].split(",")],
            team=data["team"],
            experience_years=int(data["experience_years"]),
        )
