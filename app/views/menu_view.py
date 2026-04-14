from tkinter import ttk


class MenuView:
    def __init__(self, app) -> None:
        self.app = app

    def build(self) -> ttk.Frame:
        frame = ttk.Frame(self.app.container, padding=self.app.scaled(30))
        frame.pack(fill="both", expand=True)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=2)
        frame.rowconfigure(2, weight=1)

        title_frame = ttk.Frame(frame)
        title_frame.grid(row=0, column=0, sticky="n")

        ttk.Label(
            title_frame,
            text=self.app.tr("app_title"),
            font=("Segoe UI", self.app.scaled(32), "bold")
        ).pack(pady=(self.app.scaled(30), self.app.scaled(10)))

        ttk.Label(
            title_frame,
            text=self.app.tr("select_mode"),
            font=("Segoe UI", self.app.scaled(14))
        ).pack()

        center_frame = ttk.Frame(frame)
        center_frame.grid(row=1, column=0)

        ttk.Button(
            center_frame,
            text=self.app.tr("survival"),
            command=self.app.show_survival_mode,
            width=24
        ).pack(pady=self.app.scaled(12), ipady=self.app.scaled(10))

        ttk.Button(
            center_frame,
            text=self.app.tr("settings"),
            command=self.app.show_settings_menu,
            width=24
        ).pack(pady=self.app.scaled(12), ipady=self.app.scaled(10))

        ttk.Button(
            center_frame,
            text=self.app.tr("timed_mode"),
            state="disabled",
            width=24
        ).pack(pady=self.app.scaled(12), ipady=self.app.scaled(10))

        ttk.Button(
            center_frame,
            text=self.app.tr("error_training"),
            state="disabled",
            width=24
        ).pack(pady=self.app.scaled(12), ipady=self.app.scaled(10))

        footer = ttk.Label(
            frame,
            text=f"{self.app.tr('current_language')}: {self.app.app_language_var.get()}   |   {self.app.tr('current_screen')}: {self.app.screen_mode_var.get()}   |   UI: {self.app.ui_scale_var.get()}",
            font=("Segoe UI", self.app.scaled(11))
        )
        footer.grid(row=2, column=0, sticky="s", pady=(self.app.scaled(10), self.app.scaled(20)))

        return frame