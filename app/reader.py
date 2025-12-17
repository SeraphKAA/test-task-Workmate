# Чтение csv фаайлов
import csv
from typing import List
from .models import Developer


class ReadCsv:
    @staticmethod
    def read_file(filepath: str) -> List[Developer]:
        developers = []
        
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
            
                # Если не нужна эта проверка - убрать все до добавления строк
                required_columns = ["name", "position", "completed_tasks", 
                                    "performance", "skills", "team", "experience_years"]
                
                if not all(col in reader.fieldnames for col in required_columns):
                    missing = [col for col in required_columns 
                              if col not in reader.fieldnames]
                    
                    raise ValueError(f"В файле отсутствуют обязательные колонки: {missing}")
                
                for row in reader:
                    developers.append(Developer.from_dict(row))
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {filepath}")
        
        except Exception as e:
            raise ValueError(f"Ошибка при чтении файла {filepath}: {str(e)}")
            
        return developers