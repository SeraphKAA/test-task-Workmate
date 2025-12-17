# Создание отчета
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from collections import defaultdict
from .models import Developer


class Report(ABC):
    """Абстрактный базовый класс"""

    @abstractmethod
    def generate(self, developers: List[Developer]) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class PerformanceReport(Report):
    def generate(self, developers: List[Developer]) -> List[Dict[str, Any]]:
        position_data = defaultdict(list)

        for dev in developers:
            position_data[dev.position].append(dev.performance)

        report_data = []
        for position, performances in position_data.items():
            avg_performance = sum(performances) / len(performances)
            report_data.append(
                {
                    "position": position,
                    "avg_performance": round(avg_performance, 2),
                    "count": len(performances),
                }
            )

        report_data.sort(key=lambda x: x["avg_performance"], reverse=True)
        return report_data

    def get_name(self) -> str:
        return "performance"


class ReportOut:
    """Результирующий класс для отчета"""

    _reports = {"performance": PerformanceReport}

    @classmethod
    def create_report(cls, report_name: str) -> Report:
        if report_name not in cls._reports:
            available = list(cls._reports.keys())
            raise ValueError(
                f"Отчет {report_name} не поддерживается.\nДоступные отчеты: {available}"
            )
        return cls._reports[report_name]()

    @classmethod
    def register_report(cls, report_name: str, report_class):
        cls._reports[report_name] = report_class

    @classmethod
    def get_available_reports(cls) -> List[str]:
        return list(cls._reports.keys())


# мейби изменить классы для отчетов по другим параметрам
