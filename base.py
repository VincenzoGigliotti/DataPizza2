from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Dict

class NLPModule(ABC):
    @abstractmethod
    def run(self, input_data: Dict) -> Dict:

class InputModel(BaseModel):

class OutputModel(BaseModel):
