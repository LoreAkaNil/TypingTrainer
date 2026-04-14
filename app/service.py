import random
import sys
import time
from pathlib import Path

from app.models import TestStats
from app.translations import LANGUAGE_FILES


class TypingTrainerService:
    def __init__(self) -> None:
        self.stats = TestStats()

    def set_language(self, language: str) -> None:
        if language not in LANGUAGE_FILES:
            raise ValueError(f"Lingua non supportata: {language}")
        self.stats.language = language

    def get_base_dir(self) -> Path:
        if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS)
        return Path(__file__).resolve().parent.parent

    def load_dictionary(self, filename: str) -> list[str]:
        base_dir = self.get_base_dir()
        file_path = base_dir / "data" / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Dizionario non trovato: {file_path}")

        words: list[str] = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()

                if not word:
                    continue
                if len(word) < 2 or len(word) > 15:
                    continue
                if not all(char.isalpha() for char in word):
                    continue

                words.append(word)

        if not words:
            raise ValueError(f"Il dizionario '{filename}' è vuoto o non contiene parole valide.")

        return words

    def generate_text(self, words_count: int = 15) -> str:
        filename = LANGUAGE_FILES[self.stats.language]
        words = self.load_dictionary(filename)

        generated = " ".join(random.choices(words, k=words_count))
        self.stats.target_text = generated
        self.reset_progress_only()
        return generated

    def set_custom_text(self, text: str) -> None:
        cleaned = text.strip()
        self.stats.target_text = cleaned
        self.reset_progress_only()

    def start_test(self) -> None:
        if not self.stats.started:
            self.stats.started = True
            self.stats.finished = False
            self.stats.start_time = time.time()

    def update_typed_text(self, typed_text: str) -> None:
        self.stats.typed_text = typed_text

        if typed_text and not self.stats.started:
            self.start_test()

        if self.stats.started and self.stats.start_time is not None:
            self.stats.elapsed_seconds = time.time() - self.stats.start_time

        self.stats.errors = self.count_errors()
        self.stats.accuracy = self.calculate_accuracy()
        self.stats.wpm = self.calculate_wpm()

        if typed_text == self.stats.target_text and self.stats.target_text:
            self.stats.finished = True

    def count_errors(self) -> int:
        typed = self.stats.typed_text
        target = self.stats.target_text

        errors = 0
        min_len = min(len(typed), len(target))

        for i in range(min_len):
            if typed[i] != target[i]:
                errors += 1

        if len(typed) > len(target):
            errors += len(typed) - len(target)

        return errors

    def calculate_accuracy(self) -> float:
        typed = self.stats.typed_text
        if not typed:
            return 100.0

        correct_chars = 0
        target = self.stats.target_text
        min_len = min(len(typed), len(target))

        for i in range(min_len):
            if typed[i] == target[i]:
                correct_chars += 1

        accuracy = (correct_chars / len(typed)) * 100
        return round(accuracy, 1)

    def calculate_wpm(self) -> int:
        if not self.stats.started or self.stats.elapsed_seconds <= 0:
            return 0

        minutes = self.stats.elapsed_seconds / 60
        gross_wpm = (len(self.stats.typed_text) / 5) / minutes
        adjusted_wpm = gross_wpm * (self.stats.accuracy / 100)

        return max(0, round(adjusted_wpm))

    def get_progress_text(self) -> str:
        return f"{min(len(self.stats.typed_text), len(self.stats.target_text))} / {len(self.stats.target_text)}"

    def reset_progress_only(self) -> None:
        language = self.stats.language
        target = self.stats.target_text

        self.stats = TestStats(
            target_text=target,
            language=language
        )

    def full_reset(self) -> None:
        language = self.stats.language
        self.stats = TestStats(language=language)