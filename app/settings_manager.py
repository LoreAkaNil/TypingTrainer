import json
from pathlib import Path
from typing import Any


class SettingsManager:
    VALID_SCREEN_MODES = [
        "Windowed 1280x720",
        "Windowed 1920x1080",
        "Maximized",
        "Fullscreen",
    ]

    VALID_UI_SCALES = ["75%", "100%", "125%", "150%"]

    def __init__(self, base_dir: Path) -> None:
        self.settings_file = base_dir / "user_settings.json"

    def load(self) -> dict[str, Any]:
        defaults = {
            "app_language": "Italiano",
            "typing_language": "Italiano",
            "screen_mode": "Windowed 1280x720",
            "ui_scale": "100%",
            "words_count": 15,
        }

        if not self.settings_file.exists():
            return defaults

        try:
            with open(self.settings_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception:
            return defaults

        app_language = data.get("app_language", defaults["app_language"])
        typing_language = data.get("typing_language", defaults["typing_language"])
        screen_mode = data.get("screen_mode", defaults["screen_mode"])
        ui_scale = data.get("ui_scale", defaults["ui_scale"])
        words_count = data.get("words_count", defaults["words_count"])

        if screen_mode not in self.VALID_SCREEN_MODES:
            screen_mode = defaults["screen_mode"]

        if ui_scale not in self.VALID_UI_SCALES:
            ui_scale = defaults["ui_scale"]

        if not isinstance(words_count, int) or not (5 <= words_count <= 50):
            words_count = defaults["words_count"]

        return {
            "app_language": app_language,
            "typing_language": typing_language,
            "screen_mode": screen_mode,
            "ui_scale": ui_scale,
            "words_count": words_count,
        }

    def save(
        self,
        app_language: str,
        typing_language: str,
        screen_mode: str,
        ui_scale: str,
        words_count: int,
    ) -> None:
        data = {
            "app_language": app_language,
            "typing_language": typing_language,
            "screen_mode": screen_mode,
            "ui_scale": ui_scale,
            "words_count": words_count,
        }

        with open(self.settings_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)