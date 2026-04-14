from tkinter import ttk
import tkinter as tk


class SurvivalView:
    def __init__(self, app) -> None:
        self.app = app

    def build(self) -> ttk.Frame:
        frame = ttk.Frame(
            self.app.container,
            padding=(
                self.app.scaled(16),
                self.app.scaled(12),
                self.app.scaled(16),
                self.app.scaled(16),
            ),
        )
        frame.pack(fill="both", expand=True)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        top_frame = ttk.Frame(frame)
        top_frame.grid(row=0, column=0, sticky="ew", pady=(0, self.app.scaled(10)))
        top_frame.columnconfigure(20, weight=1)

        ttk.Button(
            top_frame,
            text=self.app.tr("menu_button"),
            command=self.app.show_main_menu
        ).grid(row=0, column=0, padx=(0, self.app.scaled(12)))

        ttk.Label(
            top_frame,
            text=self.app.tr("survival_title"),
            font=("Segoe UI", self.app.scaled(22), "bold")
        ).grid(row=0, column=1, padx=(0, self.app.scaled(20)))

        ttk.Label(top_frame, text=self.app.tr("typing_language")).grid(row=0, column=2, padx=4)

        language_box = ttk.Combobox(
            top_frame,
            textvariable=self.app.typing_language_var,
            values=list(self.app.language_files.keys()),
            state="readonly",
            width=12
        )
        language_box.grid(row=0, column=3, padx=4)
        language_box.bind("<<ComboboxSelected>>", self.app.on_language_change)

        ttk.Label(top_frame, text="N° parole:").grid(row=0, column=4, padx=4)

        words_spin = ttk.Spinbox(
            top_frame,
            from_=5,
            to=50,
            textvariable=self.app.words_count_var,
            width=6
        )
        words_spin.grid(row=0, column=5, padx=4)

        ttk.Button(top_frame, text=self.app.tr("generate_test"), command=self.app.load_generated_text).grid(row=0, column=6, padx=4)
        ttk.Button(top_frame, text=self.app.tr("use_custom_text"), command=self.app.use_custom_text).grid(row=0, column=7, padx=4)
        ttk.Button(top_frame, text=self.app.tr("restart"), command=self.app.restart_test).grid(row=0, column=8, padx=4)
        ttk.Button(top_frame, text=self.app.tr("settings"), command=self.app.show_settings_menu).grid(row=0, column=9, padx=4)

        main_frame = ttk.Frame(frame)
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(1, weight=5)
        main_frame.rowconfigure(3, weight=2)

        ttk.Label(
            main_frame,
            text=self.app.tr("typing_text"),
            font=("Segoe UI", self.app.scaled(12), "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, self.app.scaled(8)))

        self.app.target_box = tk.Text(
            main_frame,
            wrap="word",
            height=10,
            font=("Consolas", self.app.scaled(18)),
            padx=self.app.scaled(14),
            pady=self.app.scaled(14),
            state="disabled",
            bg="#f5f5f5"
        )
        self.app.target_box.grid(row=1, column=0, sticky="nsew", padx=(0, self.app.scaled(16)))

        stats_frame = ttk.LabelFrame(main_frame, text=self.app.tr("stats"), padding=self.app.scaled(14))
        stats_frame.grid(row=1, column=1, sticky="nsew")
        stats_frame.columnconfigure(1, weight=1)

        self.app._add_stat_row(stats_frame, 0, self.app.tr("wpm"), self.app.wpm_var)
        self.app._add_stat_row(stats_frame, 1, self.app.tr("accuracy"), self.app.accuracy_var)
        self.app._add_stat_row(stats_frame, 2, self.app.tr("errors"), self.app.errors_var)
        self.app._add_stat_row(stats_frame, 3, self.app.tr("time"), self.app.time_var)
        self.app._add_stat_row(stats_frame, 4, self.app.tr("progress"), self.app.progress_var)

        ttk.Label(
            main_frame,
            text=self.app.tr("your_input"),
            font=("Segoe UI", self.app.scaled(12), "bold")
        ).grid(row=2, column=0, sticky="w", pady=(self.app.scaled(14), self.app.scaled(8)))

        input_container = ttk.Frame(main_frame)
        input_container.grid(row=3, column=0, sticky="nsew", padx=(0, self.app.scaled(16)))
        input_container.columnconfigure(0, weight=1)
        input_container.rowconfigure(0, weight=1)

        self.app.input_box = tk.Text(
            input_container,
            wrap="word",
            height=5,
            font=("Consolas", self.app.scaled(16)),
            padx=self.app.scaled(14),
            pady=self.app.scaled(14)
        )
        self.app.input_box.grid(row=0, column=0, sticky="nsew")
        self.app.input_box.bind("<KeyRelease>", self.app.on_key_release)

        input_scrollbar = ttk.Scrollbar(input_container, orient="vertical", command=self.app.input_box.yview)
        input_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.input_box.configure(yscrollcommand=input_scrollbar.set)

        custom_frame = ttk.LabelFrame(main_frame, text=self.app.tr("custom_text"), padding=self.app.scaled(14))
        custom_frame.grid(row=3, column=1, sticky="nsew")
        custom_frame.columnconfigure(0, weight=1)
        custom_frame.rowconfigure(1, weight=1)

        ttk.Label(
            custom_frame,
            text=self.app.tr("custom_text_hint"),
            wraplength=self.app.scaled(320),
            justify="left"
        ).grid(row=0, column=0, sticky="w", pady=(0, self.app.scaled(8)))

        custom_container = ttk.Frame(custom_frame)
        custom_container.grid(row=1, column=0, sticky="nsew")
        custom_container.columnconfigure(0, weight=1)
        custom_container.rowconfigure(0, weight=1)

        self.app.custom_text_box = tk.Text(
            custom_container,
            wrap="word",
            height=5,
            font=("Consolas", self.app.scaled(14))
        )
        self.app.custom_text_box.grid(row=0, column=0, sticky="nsew")

        custom_scrollbar = ttk.Scrollbar(custom_container, orient="vertical", command=self.app.custom_text_box.yview)
        custom_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.custom_text_box.configure(yscrollcommand=custom_scrollbar.set)

        footer = ttk.Label(
            frame,
            text=self.app.tr("survival_footer"),
            padding=(0, self.app.scaled(10), 0, 0)
        )
        footer.grid(row=2, column=0, sticky="w")

        return frame