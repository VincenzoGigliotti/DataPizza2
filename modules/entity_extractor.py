from typing import Dict, List
from pydantic import BaseModel, Field
from .base import BaseModule

class EntityExtractorInput(BaseModel):
    text: str = Field(..., description="Testo da analizzare")

class EntityExtractorOutput(BaseModel):
    entities: List[str] = Field(..., description="Lista di entità estratte")

class EntityExtractor(BaseModule):
    def run(self, input_data: Dict) -> Dict:
        inp = EntityExtractorInput(**input_data)
        extracted = ['entity1', 'entity2']
        out = EntityExtractorOutput(entities=extracted)
        return out.dict()
