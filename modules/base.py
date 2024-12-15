from typing import Dict
from ..base import NLPModule

class BaseModule(NLPModule):
    def __init__(self, **params):
        self.params = params
