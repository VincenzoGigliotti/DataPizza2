import yaml
from typing import List, Dict
from my_nlp_pipeline.modules.text_cleaner import TextCleaner
from my_nlp_pipeline.modules.entity_extractor import EntityExtractor
from my_nlp_pipeline.modules.sentiment_analyzer import SentimentAnalyzer
from my_nlp_pipeline.modules.text_generator import TextGenerator

MODULE_CLASSES = {
    "TextCleaner": TextCleaner,
    "EntityExtractor": EntityExtractor,
    "SentimentAnalyzer": SentimentAnalyzer,
    "TextGenerator": TextGenerator
}

class Pipeline:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

        self.steps = []
        for step_conf in self.config.get('pipeline', []):
            module_type = step_conf['type']
            params = step_conf.get('params', {})
            module_class = MODULE_CLASSES[module_type]
            module_instance = module_class(**params)
            self.steps.append((step_conf['name'], module_instance))

    def run(self, initial_input: Dict) -> Dict:
        data = initial_input
        for name, module in self.steps:
            data = module.run(data)
        return data
