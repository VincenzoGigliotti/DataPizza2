from typing import Dict
from pydantic import BaseModel, Field
from .base import BaseModule

class TextGeneratorInput(BaseModel):
    prompt: str = Field(..., description="Prompt per generare testo")
    max_length: int = Field(..., description="Lunghezza massima del testo generato")

class TextGeneratorOutput(BaseModel):
    generated_text: str = Field(..., description="Testo generato")

class TextGenerator(BaseModule):
    def run(self, input_data: Dict) -> Dict:
        inp = TextGeneratorInput(**input_data)
        gen_text = f"Generated text based on: {inp.prompt}"
        if len(gen_text) > inp.max_length:
            gen_text = gen_text[:inp.max_length]
        out = TextGeneratorOutput(generated_text=gen_text)
        return out.dict()
