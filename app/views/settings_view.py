import tkinter as tk
from tkinter import ttk


class SettingsView:
    def __init__(self, app) -> None:
        self.app = app

    def build(self) -> ttk.Frame:
        outer_frame = ttk.Frame(self.app.container)
        outer_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(outer_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, padding=self.app.scaled(30))

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        def resize_scrollable_frame(event):
            canvas.itemconfig(canvas_window, width=event.width)

        canvas.bind("<Configure>", resize_scrollable_frame)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        scrollable_frame.columnconfigure(0, weight=1)
        scrollable_frame.columnconfigure(1, weight=1)

        ttk.Label(
            scrollable_frame,
            text=self.app.tr("settings_title"),
            font=("Segoe UI", self.app.scaled(28), "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(self.app.scaled(10), self.app.scaled(30)))

        ttk.Label(
            scrollable_frame,
            text=self.app.tr("app_language"),
            font=("Segoe UI", self.app.scaled(12), "bold")
        ).grid(row=1, column=0, sticky="e", padx=self.app.scaled(10), pady=self.app.scaled(10))

        ttk.Combobox(
            scrollable_frame,
            textvariable=self.app.app_language_var,
            values=list(self.app.ui_translations.keys()),
            state="readonly",
            width=25
        ).grid(row=1, column=1, sticky="w", padx=self.app.scaled(10), pady=self.app.scaled(10))

        ttk.Label(
            scrollable_frame,
            text=self.app.tr("screen_mode"),
            font=("Segoe UI", self.app.scaled(12), "bold")
        ).grid(row=2, column=0, sticky="e", padx=self.app.scaled(10), pady=self.app.scaled(10))

        ttk.Combobox(
            scrollable_frame,
            textvariable=self.app.screen_mode_var,
            values=[
                "Windowed 1280x720",
                "Maximized",
                "Fullscreen",
            ],
            state="readonly",
            width=25
        ).grid(row=2, column=1, sticky="w", padx=self.app.scaled(10), pady=self.app.scaled(10))

        ttk.Label(
            scrollable_frame,
            text=self.app.tr("ui_scale"),
            font=("Segoe UI", self.app.scaled(12), "bold")
        ).grid(row=3, column=0, sticky="e", padx=self.app.scaled(10), pady=self.app.scaled(10))

        ttk.Combobox(
            scrollable_frame,
            textvariable=self.app.ui_scale_var,
            values=["75%", "100%", "125%", "150%"],
            state="readonly",
            width=25
        ).grid(row=3, column=1, sticky="w", padx=self.app.scaled(10), pady=self.app.scaled(10))

        ttk.Label(
            scrollable_frame,
            text=self.app.tr("note_text"),
            font=("Segoe UI", self.app.scaled(11)),
            justify="left"
        ).grid(row=4, column=0, columnspan=2, pady=(self.app.scaled(20), self.app.scaled(30)))

        buttons_frame = ttk.Frame(scrollable_frame)
        buttons_frame.grid(row=5, column=0, columnspan=2, pady=self.app.scaled(20))

        ttk.Button(
            buttons_frame,
            text=self.app.tr("apply"),
            command=self.app.apply_settings,
            width=18
        ).pack(side="left", padx=self.app.scaled(10), ipady=self.app.scaled(6))

        ttk.Button(
            buttons_frame,
            text=self.app.tr("back_to_menu"),
            command=self.app.show_main_menu,
            width=18
        ).pack(side="left", padx=self.app.scaled(10), ipady=self.app.scaled(6))

        self.app.bind_mousewheel(canvas)

        return outer_frame