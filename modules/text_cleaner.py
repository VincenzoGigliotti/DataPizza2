from typing import Dict
from pydantic import BaseModel, Field
from .base import BaseModule

# Definiamo modelli input/output
class TextCleanerInput(BaseModel):
    text: str = Field(..., description="Testo da pulire")

class TextCleanerOutput(BaseModel):
    text: str = Field(..., description="Testo pulito")

class TextCleaner(BaseModule):
    def run(self, input_data: Dict) -> Dict:
        inp = TextCleanerInput(**input_data)

        cleaned_text = inp.text.strip()

        out = TextCleanerOutput(text=cleaned_text)
        return out.dict()
