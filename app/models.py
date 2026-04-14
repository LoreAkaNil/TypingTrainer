from dataclasses import dataclass
from typing import Optional


@dataclass
class TestStats:
    target_text: str = ""
    typed_text: str = ""
    language: str = "Italiano"
    errors: int = 0
    accuracy: float = 100.0
    wpm: int = 0
    elapsed_seconds: float = 0.0
    started: bool = False
    finished: bool = False
    start_time: Optional[float] = None