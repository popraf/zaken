from dataclasses import dataclass
from typing import List, Literal

# import torch
import os

SAFETY_CHECKER = os.environ.get("SAFETY_CHECKER", "False") == "True"


@dataclass
class Config:
    """
    The configuration for the API.
    """
    pass