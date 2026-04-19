import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

from app.service import TypingTrainerService
from app.settings_manager import SettingsManager
from app.translations import LANGUAGE_FILES, UI_TRANSLATIONS
from app.views.menu_view import MenuView
from app.views.settings_view import SettingsView
from app.views.survival_view import SurvivalView


class TypingTrainerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry("1280x720")
        self.root.minsize(1000, 650)

        self.base_dir = Path(__file__).resolve().parent.parent
        self.service = TypingTrainerService()
        self.settings_manager = SettingsManager(self.base_dir)

        self.timer_job = None
<<<<<<< HEAD
=======
        self.key_reset_job = None
>>>>>>> 1080e11 (Surviaval mode update)

        self.language_files = LANGUAGE_FILES
        self.ui_translations = UI_TRANSLATIONS

        self.app_language_var = tk.StringVar(value="Italiano")
        self.typing_language_var = tk.StringVar(value="Italiano")
        self.words_count_var = tk.IntVar(value=15)
        self.screen_mode_var = tk.StringVar(value="Windowed 1280x720")
        self.ui_scale_var = tk.StringVar(value="100%")

        self.wpm_var = tk.StringVar(value="0")
        self.accuracy_var = tk.StringVar(value="100.0%")
        self.errors_var = tk.StringVar(value="0")
        self.error_limit_var = tk.StringVar(value="0 / 3")
        self.time_var = tk.StringVar(value="0.0 s")
        self.progress_var = tk.StringVar(value="0 / 0")

        self.target_box = None
        self.input_box = None
        self.custom_text_box = None
<<<<<<< HEAD
=======
        self.key_widgets = {}
>>>>>>> 1080e11 (Surviaval mode update)

        self.load_settings()

        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.current_frame = None

        self.service.set_language(self.typing_language_var.get())
        self.apply_screen_mode()
        self.refresh_title()
        self.show_main_menu()

        self.root.bind("<Escape>", self.on_escape)

<<<<<<< HEAD
    # =========================
    # SETTINGS PERSISTENCE
    # =========================
=======
>>>>>>> 1080e11 (Surviaval mode update)
    def load_settings(self) -> None:
        settings = self.settings_manager.load()
        self.app_language_var.set(settings["app_language"])
        self.typing_language_var.set(settings["typing_language"])
        self.screen_mode_var.set(settings["screen_mode"])
        self.ui_scale_var.set(settings["ui_scale"])
        self.words_count_var.set(settings["words_count"])

    def save_settings(self) -> None:
        try:
            self.settings_manager.save(
                app_language=self.app_language_var.get(),
                typing_language=self.typing_language_var.get(),
                screen_mode=self.screen_mode_var.get(),
                ui_scale=self.ui_scale_var.get(),
                words_count=self.words_count_var.get(),
            )
        except Exception as error:
            messagebox.showerror(self.tr("error"), f"{self.tr('settings_save_error')}:\n{error}")

<<<<<<< HEAD
    # =========================
    # TRANSLATIONS / SCALE
    # =========================
=======
>>>>>>> 1080e11 (Surviaval mode update)
    def tr(self, key: str) -> str:
        lang = self.app_language_var.get()
        return self.ui_translations.get(lang, self.ui_translations["English"]).get(key, key)

    def get_scale_factor(self) -> float:
        mapping = {
            "75%": 0.75,
            "100%": 1.0,
            "125%": 1.25,
            "150%": 1.5,
        }
        return mapping.get(self.ui_scale_var.get(), 1.0)

    def scaled(self, value: int) -> int:
        return max(1, int(value * self.get_scale_factor()))

    def refresh_title(self) -> None:
        self.root.title(self.tr("app_title"))

<<<<<<< HEAD
    # =========================
    # SCREEN
    # =========================
=======
>>>>>>> 1080e11 (Surviaval mode update)
    def apply_screen_mode(self) -> None:
        mode = self.screen_mode_var.get()

        self.root.attributes("-fullscreen", False)

        if mode == "Windowed 1280x720":
            self.root.state("normal")
            self.root.geometry("1280x720")
        elif mode == "Maximized":
            self.root.state("zoomed")
        elif mode == "Fullscreen":
            self.root.state("normal")
            self.root.attributes("-fullscreen", True)

    def on_escape(self, event=None) -> None:
        if self.root.attributes("-fullscreen"):
            self.root.attributes("-fullscreen", False)
            self.screen_mode_var.set("Windowed 1280x720")
            self.root.geometry("1280x720")
            self.save_settings()

<<<<<<< HEAD
    # =========================
    # FRAME MGMT
    # =========================
=======
>>>>>>> 1080e11 (Surviaval mode update)
    def clear_current_frame(self) -> None:
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

        self.target_box = None
        self.input_box = None
        self.custom_text_box = None
<<<<<<< HEAD
=======
        self.key_widgets = {}
>>>>>>> 1080e11 (Surviaval mode update)

    def show_main_menu(self) -> None:
        self.clear_current_frame()
        self.refresh_title()
        self.current_frame = MenuView(self).build()

    def show_settings_menu(self) -> None:
        self.clear_current_frame()
        self.refresh_title()
        self.current_frame = SettingsView(self).build()

    def show_survival_mode(self) -> None:
        self.clear_current_frame()
        self.refresh_title()
        self.current_frame = SurvivalView(self).build()
        self.load_generated_text()
<<<<<<< HEAD
        
    # =========================
    # SETTINGS ACTIONS
    # =========================
    
=======

>>>>>>> 1080e11 (Surviaval mode update)
    def bind_mousewheel(self, canvas: tk.Canvas) -> None:
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def apply_settings(self) -> None:
        self.apply_screen_mode()
        self.refresh_title()
        self.save_settings()
        messagebox.showinfo(self.tr("settings"), self.tr("settings_applied"))
        self.show_settings_menu()
<<<<<<< HEAD
        
    # =========================
    # SETTINGS START/END SESSION
    # =========================   
=======
>>>>>>> 1080e11 (Surviaval mode update)

    def prepare_active_session(self) -> None:
        current_target = self.service.stats.target_text
        current_language = self.service.stats.language
        max_errors = self.service.stats.max_errors

<<<<<<< HEAD
        # Ricrea uno stato pulito della sessione
=======
>>>>>>> 1080e11 (Surviaval mode update)
        self.service.stats = self.service.stats.__class__(
            target_text=current_target,
            language=current_language,
            max_errors=max_errors
        )

        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

<<<<<<< HEAD
=======
        if self.key_reset_job is not None:
            self.root.after_cancel(self.key_reset_job)
            self.key_reset_job = None

        self._reset_keyboard_highlight()

>>>>>>> 1080e11 (Surviaval mode update)
        if self.input_box is not None:
            self.input_box.config(state="normal")
            self.input_box.delete("1.0", "end")
            self.input_box.focus_set()

<<<<<<< HEAD
    # =========================
    # SURVIVAL ACTIONS
    # =========================
=======
>>>>>>> 1080e11 (Surviaval mode update)
    def _add_stat_row(self, parent: ttk.Widget, row: int, label: str, variable: tk.StringVar) -> None:
        ttk.Label(parent, text=label, font=("Segoe UI", self.scaled(12), "bold")).grid(
            row=row, column=0, sticky="w", pady=self.scaled(8)
        )
        ttk.Label(parent, textvariable=variable, font=("Segoe UI", self.scaled(12))).grid(
            row=row, column=1, sticky="e", pady=self.scaled(8)
        )

    def on_language_change(self, event=None) -> None:
        self.service.set_language(self.typing_language_var.get())
        self.save_settings()
        self.load_generated_text()

    def load_generated_text(self) -> None:
        try:
            self.service.set_language(self.typing_language_var.get())

<<<<<<< HEAD
            # VALIDAZIONE INPUT  
=======
>>>>>>> 1080e11 (Surviaval mode update)
            word_count = self.words_count_var.get()

            if isinstance(word_count, str):
                if not word_count.isdigit():
                    return
                word_count = int(word_count)

            if word_count <= 0:
                return

            generated = self.service.generate_text(word_count)

        except Exception as error:
            messagebox.showerror(self.tr("error"), str(error))
            return

        self.prepare_active_session()

        if self.target_box is not None:
            self._set_target_text(generated)

        self._reset_ui_stats()

<<<<<<< HEAD
        # UX MIGLIORIA
=======
>>>>>>> 1080e11 (Surviaval mode update)
        if self.input_box is not None:
            self.input_box.focus_set()

    def use_custom_text(self) -> None:
        if self.custom_text_box is None:
            return

        custom_text = self.custom_text_box.get("1.0", "end").strip()
        if not custom_text:
            messagebox.showwarning(self.tr("warning"), self.tr("insert_custom_text"))
            return

        self.service.set_custom_text(custom_text)
        self.prepare_active_session()
        self._set_target_text(custom_text)
        self._reset_ui_stats()
<<<<<<< HEAD
        
=======

>>>>>>> 1080e11 (Surviaval mode update)
    def import_text_file(self) -> None:
        if self.custom_text_box is None:
            return

        file_path = filedialog.askopenfilename(
            title=self.tr("select_text_file"),
            filetypes=[("Text files", "*.txt")]
        )

        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        except Exception:
            messagebox.showerror(self.tr("error"), self.tr("invalid_text_file"))
            return

        self.custom_text_box.delete("1.0", "end")
        self.custom_text_box.insert("1.0", content)

    def restart_test(self) -> None:
        current_target = self.service.stats.target_text
        if not current_target:
            self.load_generated_text()
            return

        self.service.reset_progress_only()
        self.prepare_active_session()
        self._set_target_text(self.service.stats.target_text)
        self._reset_ui_stats()

    def end_run(self) -> None:
        if self.input_box is None:
            return

        self.service.stats.finished = True

        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.input_box.config(state="disabled")

        messagebox.showinfo(
            self.tr("session_ended"),
            f"{self.tr('session_ended_message')}\n\n"
            f"WPM: {self.service.stats.wpm}\n"
            f"{self.tr('accuracy')} {self.service.stats.accuracy}%\n"
            f"{self.tr('errors')} {self.service.stats.errors}\n"
            f"{self.tr('error_limit')} {self.service.stats.mistakes_made} / {self.service.stats.max_errors}\n"
            f"{self.tr('time')} {self.service.stats.elapsed_seconds:.1f} s"
        )

    def trigger_game_over(self) -> None:
        if self.input_box is None:
            return

        self.service.stats.finished = True

        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.input_box.config(state="disabled")

        messagebox.showinfo(
            self.tr("game_over"),
            f"{self.tr('game_over_message')}\n\n"
            f"WPM: {self.service.stats.wpm}\n"
            f"{self.tr('accuracy')} {self.service.stats.accuracy}%\n"
            f"{self.tr('errors')} {self.service.stats.errors}\n"
            f"{self.tr('error_limit')} {self.service.stats.mistakes_made} / {self.service.stats.max_errors}\n"
            f"{self.tr('time')} {self.service.stats.elapsed_seconds:.1f} s"
        )

    def _set_target_text(self, text: str) -> None:
        if self.target_box is None:
            return

        self.target_box.config(state="normal")
        self.target_box.delete("1.0", "end")
        self.target_box.insert("1.0", text)
        self.target_box.config(state="disabled")
<<<<<<< HEAD
   
=======

>>>>>>> 1080e11 (Surviaval mode update)
    def _reset_ui_stats(self) -> None:
        self.wpm_var.set("0")
        self.accuracy_var.set("100.0%")
        self.errors_var.set("0")
        self.error_limit_var.set(f"0 / {self.service.stats.max_errors}")
        self.time_var.set("0.0 s")
        self.progress_var.set(f"0 / {len(self.service.stats.target_text)}")

        if self.target_box is not None:
            self._clear_highlighting()

    def _clear_highlighting(self) -> None:
        if self.target_box is None:
            return

        self.target_box.config(state="normal")
        self.target_box.tag_delete("correct")
        self.target_box.tag_delete("incorrect")
        self.target_box.tag_delete("pending")
        self.target_box.config(state="disabled")

<<<<<<< HEAD
    def on_key_release(self, event=None) -> None:
=======
    def _reset_keyboard_highlight(self) -> None:
        if not self.key_widgets:
            return

        for btn in self.key_widgets.values():
            btn.config(bg="#3a3a3a", fg="#f2f2f2")

    def _map_event_to_key(self, event) -> str | None:
        if event is None:
            return None

        keysym = event.keysym
        char = event.char

        special_map = {
            "BackSpace": "backspace",
            "Tab": "tab",
            "Return": "enter",
            "Shift_L": "shift_l",
            "Shift_R": "shift_r",
            "Control_L": "ctrl_l",
            "Control_R": "ctrl_r",
            "Alt_L": "alt_l",
            "Alt_R": "altgr",
            "Left": "left",
            "Right": "right",
            "Up": "up",
            "Down": "down",
            "space": "space",
            "Caps_Lock": "capslock",
            "Super_L": "super",
            "Super_R": "super",
        }

        if keysym in special_map:
            return special_map[keysym]

        if len(char) == 1:
            char_map = {
                "\\": "backslash",
                "'": "apostrophe",
                "+": "plus",
                ",": "comma",
                ".": "period",
                "-": "minus",
                "<": "less",
                "ì": "igrave",
                "è": "egrave",
                "ò": "ograve",
                "à": "agrave",
                "ù": "ugrave",
            }

            lowered = char.lower()

            if lowered in char_map:
                return char_map[lowered]

            if lowered.isalpha() or lowered.isdigit():
                return lowered

        return None

    def _highlight_key(self, event=None) -> None:
        if not self.key_widgets:
            return

        lookup = self._map_event_to_key(event)
        if lookup is None:
            return

        self._reset_keyboard_highlight()

        btn = self.key_widgets.get(lookup)
        if btn is not None:
            btn.config(bg="#4cc9f0", fg="#111111")

            if self.key_reset_job is not None:
                self.root.after_cancel(self.key_reset_job)

            self.key_reset_job = self.root.after(120, self._reset_keyboard_highlight)

    def on_key_release(self, event=None) -> None:
        self._highlight_key(event)

>>>>>>> 1080e11 (Surviaval mode update)
        if self.input_box is None or self.service.stats.finished:
            return

        previous_typed = self.service.stats.typed_text
        typed_text = self.input_box.get("1.0", "end-1c")

<<<<<<< HEAD
        # Conta solo i nuovi caratteri aggiunti
=======
>>>>>>> 1080e11 (Surviaval mode update)
        if len(typed_text) > len(previous_typed):
            added_text = typed_text[len(previous_typed):]
            start_index = len(previous_typed)

            for offset, char in enumerate(added_text):
                target_index = start_index + offset
                expected_char = (
                    self.service.stats.target_text[target_index]
                    if target_index < len(self.service.stats.target_text)
                    else None
                )

                if expected_char is None or char != expected_char:
                    self.service.stats.mistakes_made += 1

        self.service.update_typed_text(typed_text)

        self._refresh_stats()
        self._highlight_text()

        if self.service.stats.mistakes_made >= self.service.stats.max_errors:
            self.trigger_game_over()
            return

        if self.service.stats.started and self.timer_job is None and not self.service.stats.finished:
            self._update_timer()

        if self.service.stats.finished:
            if self.timer_job is not None:
                self.root.after_cancel(self.timer_job)
                self.timer_job = None

            self.input_box.config(state="disabled")

            messagebox.showinfo(
                self.tr("completed"),
                f"WPM: {self.service.stats.wpm}\n"
                f"{self.tr('accuracy')} {self.service.stats.accuracy}%\n"
                f"{self.tr('errors')} {self.service.stats.errors}\n"
                f"{self.tr('error_limit')} {self.service.stats.mistakes_made} / {self.service.stats.max_errors}\n"
                f"{self.tr('time')} {self.service.stats.elapsed_seconds:.1f} s"
            )
<<<<<<< HEAD
            
=======

>>>>>>> 1080e11 (Surviaval mode update)
    def _update_timer(self) -> None:
        if self.service.stats.started and not self.service.stats.finished:
            self.time_var.set(f"{self.service.stats.elapsed_seconds:.1f} s")
            self.timer_job = self.root.after(100, self._update_timer)

    def _refresh_stats(self) -> None:
        stats = self.service.stats
        self.wpm_var.set(str(stats.wpm))
        self.accuracy_var.set(f"{stats.accuracy}%")
        self.errors_var.set(str(stats.errors))
        self.error_limit_var.set(f"{stats.mistakes_made} / {stats.max_errors}")
        self.time_var.set(f"{stats.elapsed_seconds:.1f} s")
        self.progress_var.set(self.service.get_progress_text())

    def _highlight_text(self) -> None:
        if self.target_box is None:
            return

        typed = self.service.stats.typed_text
        target = self.service.stats.target_text

        self.target_box.config(state="normal")
        self.target_box.tag_remove("correct", "1.0", "end")
        self.target_box.tag_remove("incorrect", "1.0", "end")
        self.target_box.tag_remove("pending", "1.0", "end")

        self.target_box.tag_configure("correct", background="#d8f3dc")
        self.target_box.tag_configure("incorrect", background="#ffccd5")
        self.target_box.tag_configure("pending", background="#f3c96e")

<<<<<<< HEAD
        # Evidenzia ogni carattere digitato confrontandolo con il target
=======
>>>>>>> 1080e11 (Surviaval mode update)
        for i, char in enumerate(typed):
            start = f"1.0 + {i} chars"
            end = f"1.0 + {i + 1} chars"

            if i < len(target) and char == target[i]:
                self.target_box.tag_add("correct", start, end)
            else:
                self.target_box.tag_add("incorrect", start, end)

<<<<<<< HEAD
        # Evidenzia il testo ancora non digitato
=======
>>>>>>> 1080e11 (Surviaval mode update)
        if len(target) > len(typed):
            self.target_box.tag_add(
                "pending",
                f"1.0 + {len(typed)} chars",
                f"1.0 + {len(target)} chars"
            )

        self.target_box.config(state="disabled")

<<<<<<< HEAD
=======

>>>>>>> 1080e11 (Surviaval mode update)
def main() -> None:
    root = tk.Tk()
    app = TypingTrainerApp(root)
    root.mainloop()