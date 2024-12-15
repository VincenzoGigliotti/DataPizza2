from typing import Dict
from pydantic import BaseModel, Field
from .base import BaseModule

class SentimentAnalyzerInput(BaseModel):
    text: str = Field(..., description="Testo su cui calcolare il sentiment")

class SentimentAnalyzerOutput(BaseModel):
    sentiment: float = Field(..., description="Valore del sentiment tra -1 e 1")

class SentimentAnalyzer(BaseModule):
    def run(self, input_data: Dict) -> Dict:
        inp = SentimentAnalyzerInput(**input_data)
        score = 0.8
        out = SentimentAnalyzerOutput(sentiment=score)
        return out.dict()
