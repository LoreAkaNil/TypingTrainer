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

        # =========================
        # TOP BAR
        # =========================
        top_frame = ttk.Frame(frame)
        top_frame.grid(row=0, column=0, sticky="ew", pady=(0, self.app.scaled(10)))
        top_frame.columnconfigure(20, weight=1)

        self.menu_button = ttk.Button(
            top_frame,
            text="☰ Menu",
            command=self.open_hamburger_menu
        )
        self.menu_button.grid(row=0, column=0, padx=(0, self.app.scaled(12)))

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

        ttk.Label(top_frame, text=self.app.tr("word_count")).grid(row=0, column=4, padx=4)

        words_spin = ttk.Spinbox(
            top_frame,
            from_=5,
            to=500,
            textvariable=self.app.words_count_var,
            width=6
        )
        words_spin.grid(row=0, column=5, padx=4)
        words_spin.bind("<Return>", self.on_word_count_enter)

        ttk.Button(
            top_frame,
            text=self.app.tr("restart"),
            command=self.app.restart_test
        ).grid(row=0, column=6, padx=4)

        ttk.Button(
            top_frame,
            text=self.app.tr("end_run"),
            command=self.app.end_run
        ).grid(row=0, column=7, padx=4)

        # =========================
        # MAIN AREA
        # =========================
        main_frame = ttk.Frame(frame)
        main_frame.grid(row=1, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=2)
<<<<<<< HEAD

        # solo una riga "spacer" finale espandibile
        main_frame.rowconfigure(4, weight=1)
        main_frame.rowconfigure(5, weight=2)
        
=======
        main_frame.rowconfigure(5, weight=1)

>>>>>>> 1080e11 (Surviaval mode update)
        # -------------------------
        # LEFT COLUMN
        # -------------------------
        ttk.Label(
            main_frame,
            text=self.app.tr("typing_text"),
            font=("Segoe UI", self.app.scaled(12), "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, self.app.scaled(8)))

        target_container = ttk.Frame(main_frame)
        target_container.grid(row=1, column=0, sticky="ew", padx=(0, self.app.scaled(16)))
        target_container.columnconfigure(0, weight=1)

        self.app.target_box = tk.Text(
            target_container,
            wrap="word",
            height=4,
            font=("Consolas", self.app.scaled(20)),
            padx=self.app.scaled(16),
            pady=self.app.scaled(16),
            state="disabled",
            bg="#ffffff",
            relief="solid",
            bd=1
        )
        self.app.target_box.grid(row=0, column=0, sticky="ew")

<<<<<<< HEAD
        target_scrollbar = ttk.Scrollbar(target_container, orient="vertical", command=self.app.target_box.yview)
        target_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.target_box.configure(yscrollcommand=target_scrollbar.set)

=======
        target_scrollbar = ttk.Scrollbar(
            target_container,
            orient="vertical",
            command=self.app.target_box.yview
        )
        target_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.target_box.configure(yscrollcommand=target_scrollbar.set)

        # =========================
        # KEYBOARD UNDER TARGET
        # =========================
        keyboard_container = ttk.LabelFrame(
            main_frame,
            text="Tastiera",
            padding=self.app.scaled(10)
        )
        keyboard_container.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=(0, self.app.scaled(16)),
            pady=(self.app.scaled(12), 0)
        )
        keyboard_container.columnconfigure(0, weight=1)

        keyboard_frame = tk.Frame(
            keyboard_container,
            bg="#2b2b2b",
            bd=2,
            relief="solid",
            padx=self.app.scaled(10),
            pady=self.app.scaled(10),
        )
        keyboard_frame.grid(row=0, column=0, sticky="w")

        self.key_widgets = {}

        def make_key(parent, key, label, width):
            btn = tk.Label(
                parent,
                text=label,
                width=width,
                height=2,
                bg="#3a3a3a",
                fg="#f2f2f2",
                relief="raised",
                bd=1,
                font=("Segoe UI", self.app.scaled(9), "bold"),
                activebackground="#3a3a3a",
                activeforeground="#f2f2f2",
            )
            self.key_widgets[key] = btn
            return btn

        # Riga 1
        row1 = tk.Frame(keyboard_frame, bg="#2b2b2b")
        row1.grid(row=0, column=0, pady=self.app.scaled(2), sticky="w")

        row1_keys = [
            ("backslash", "\\", 4),
            ("1", "1", 4),
            ("2", "2", 4),
            ("3", "3", 4),
            ("4", "4", 4),
            ("5", "5", 4),
            ("6", "6", 4),
            ("7", "7", 4),
            ("8", "8", 4),
            ("9", "9", 4),
            ("0", "0", 4),
            ("apostrophe", "'", 4),
            ("igrave", "ì", 4),
            ("backspace", "BACK", 8),
        ]
        for key, label, width in row1_keys:
            make_key(row1, key, label, width).pack(side="left", padx=self.app.scaled(2))

        # Riga 2
        row2 = tk.Frame(keyboard_frame, bg="#2b2b2b")
        row2.grid(row=1, column=0, pady=self.app.scaled(2), sticky="w")

        row2_keys = [
            ("tab", "TAB", 6),
            ("q", "Q", 4),
            ("w", "W", 4),
            ("e", "E", 4),
            ("r", "R", 4),
            ("t", "T", 4),
            ("y", "Y", 4),
            ("u", "U", 4),
            ("i", "I", 4),
            ("o", "O", 4),
            ("p", "P", 4),
            ("egrave", "è", 4),
            ("plus", "+", 4),
            ("enter", "ENTER", 8),
        ]
        for key, label, width in row2_keys:
            make_key(row2, key, label, width).pack(side="left", padx=self.app.scaled(2))

        # Riga 3
        row3 = tk.Frame(keyboard_frame, bg="#2b2b2b")
        row3.grid(row=2, column=0, pady=self.app.scaled(2), sticky="w")

        row3_keys = [
            ("capslock", "CAPS", 7),
            ("a", "A", 4),
            ("s", "S", 4),
            ("d", "D", 4),
            ("f", "F", 4),
            ("g", "G", 4),
            ("h", "H", 4),
            ("j", "J", 4),
            ("k", "K", 4),
            ("l", "L", 4),
            ("ograve", "ò", 4),
            ("agrave", "à", 4),
            ("ugrave", "ù", 4),
            ("shift_r", "SHIFT", 10),
        ]
        for key, label, width in row3_keys:
            make_key(row3, key, label, width).pack(side="left", padx=self.app.scaled(2))

        # Riga 4
        row4 = tk.Frame(keyboard_frame, bg="#2b2b2b")
        row4.grid(row=3, column=0, pady=self.app.scaled(2), sticky="w")

        row4_keys = [
            ("shift_l", "SHIFT", 9),
            ("less", "<", 4),
            ("z", "Z", 4),
            ("x", "X", 4),
            ("c", "C", 4),
            ("v", "V", 4),
            ("b", "B", 4),
            ("n", "N", 4),
            ("m", "M", 4),
            ("comma", ",", 4),
            ("period", ".", 4),
            ("minus", "-", 4),
        ]
        for key, label, width in row4_keys:
            make_key(row4, key, label, width).pack(side="left", padx=self.app.scaled(2))

        make_key(row4, "up", "↑", 4).pack(
            side="left",
            padx=(self.app.scaled(22), self.app.scaled(2))
        )

        # Riga 5
        row5 = tk.Frame(keyboard_frame, bg="#2b2b2b")
        row5.grid(row=4, column=0, pady=self.app.scaled(2), sticky="w")

        row5_keys = [
            ("ctrl_l", "CTRL", 6),
            ("fn", "FN", 5),
            ("super", "WIN", 5),
            ("alt_l", "ALT", 5),
            ("space", "SPACE", 24),
            ("altgr", "ALTGR", 6),
            ("ctrl_r", "CTRL", 6),
            ("left", "←", 4),
            ("down", "↓", 4),
            ("right", "→", 4),
        ]
        for key, label, width in row5_keys:
            make_key(row5, key, label, width).pack(side="left", padx=self.app.scaled(2))

        self.app.key_widgets = self.key_widgets

        # -------------------------
        # INPUT UNDER KEYBOARD
        # -------------------------
>>>>>>> 1080e11 (Surviaval mode update)
        ttk.Label(
            main_frame,
            text=self.app.tr("your_input"),
            font=("Segoe UI", self.app.scaled(12), "bold")
<<<<<<< HEAD
        ).grid(row=2, column=0, sticky="w", pady=(self.app.scaled(14), self.app.scaled(8)))

        input_container = ttk.Frame(main_frame)
        input_container.grid(row=3, column=0, sticky="ew", padx=(0, self.app.scaled(16)))
=======
        ).grid(row=3, column=0, sticky="w", pady=(self.app.scaled(14), self.app.scaled(8)))

        input_container = ttk.Frame(main_frame)
        input_container.grid(row=4, column=0, sticky="ew", padx=(0, self.app.scaled(16)))
>>>>>>> 1080e11 (Surviaval mode update)
        input_container.columnconfigure(0, weight=1)

        self.app.input_box = tk.Text(
            input_container,
            wrap="word",
            height=3,
            font=("Consolas", self.app.scaled(18)),
            padx=self.app.scaled(16),
            pady=self.app.scaled(16),
            relief="solid",
            bd=1
        )
        self.app.input_box.grid(row=0, column=0, sticky="ew")
        self.app.input_box.bind("<KeyRelease>", self.app.on_key_release)

<<<<<<< HEAD
        input_scrollbar = ttk.Scrollbar(input_container, orient="vertical", command=self.app.input_box.yview)
        input_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.input_box.configure(yscrollcommand=input_scrollbar.set)
        
        # =========================
        # BOTTOM AREA (futura tastiera / feedback)
        # =========================
        bottom_container = ttk.Frame(main_frame)
        bottom_container.grid(
            row=5,
            column=0,
            sticky="nsew",
            padx=(0, self.app.scaled(16)),
            pady=(self.app.scaled(12), 0)
        )
        bottom_container.columnconfigure(0, weight=1)
        bottom_container.rowconfigure(0, weight=1)

        self.bottom_placeholder = ttk.Label(
            bottom_container,
            text="(area futura tastiera / feedback)",
            anchor="center",
            foreground="#888"
        )
        self.bottom_placeholder.grid(row=0, column=0, sticky="nsew")
=======
        input_scrollbar = ttk.Scrollbar(
            input_container,
            orient="vertical",
            command=self.app.input_box.yview
        )
        input_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.input_box.configure(yscrollcommand=input_scrollbar.set)

        ttk.Frame(main_frame).grid(row=5, column=0, sticky="nsew")
>>>>>>> 1080e11 (Surviaval mode update)

        # -------------------------
        # RIGHT COLUMN
        # -------------------------
        stats_frame = ttk.LabelFrame(
            main_frame,
            text=self.app.tr("stats"),
            padding=self.app.scaled(14)
        )
<<<<<<< HEAD
        stats_frame.grid(row=0, column=1, rowspan=2, sticky="new")
=======
        stats_frame.grid(row=0, column=1, rowspan=3, sticky="new")
>>>>>>> 1080e11 (Surviaval mode update)
        stats_frame.columnconfigure(1, weight=1)

        self.app._add_stat_row(stats_frame, 0, self.app.tr("wpm"), self.app.wpm_var)
        self.app._add_stat_row(stats_frame, 1, self.app.tr("accuracy"), self.app.accuracy_var)
        self.app._add_stat_row(stats_frame, 2, self.app.tr("errors"), self.app.errors_var)
        self.app._add_stat_row(stats_frame, 3, self.app.tr("error_limit"), self.app.error_limit_var)
        self.app._add_stat_row(stats_frame, 4, self.app.tr("time"), self.app.time_var)
        self.app._add_stat_row(stats_frame, 5, self.app.tr("progress"), self.app.progress_var)

        custom_frame = ttk.LabelFrame(
            main_frame,
            text=self.app.tr("custom_text"),
            padding=self.app.scaled(14)
        )
<<<<<<< HEAD
        custom_frame.grid(row=3, column=1, sticky="new")
=======
        custom_frame.grid(row=4, column=1, sticky="new")
>>>>>>> 1080e11 (Surviaval mode update)
        custom_frame.columnconfigure(0, weight=1)
        custom_frame.rowconfigure(2, weight=1)

        ttk.Label(
            custom_frame,
            text=self.app.tr("custom_text_hint"),
            wraplength=self.app.scaled(320),
            justify="left"
        ).grid(row=0, column=0, sticky="w", pady=(0, self.app.scaled(8)))

        custom_buttons = ttk.Frame(custom_frame)
        custom_buttons.grid(row=1, column=0, sticky="w", pady=(0, self.app.scaled(8)))

        ttk.Button(
            custom_buttons,
            text=self.app.tr("use_custom_text"),
            command=self.app.use_custom_text
        ).pack(side="left", padx=(0, self.app.scaled(8)))

        ttk.Button(
            custom_buttons,
            text=self.app.tr("import_txt"),
            command=self.app.import_text_file
        ).pack(side="left")

        custom_container = ttk.Frame(custom_frame)
        custom_container.grid(row=2, column=0, sticky="nsew")
        custom_container.columnconfigure(0, weight=1)
        custom_container.rowconfigure(0, weight=1)

        self.app.custom_text_box = tk.Text(
            custom_container,
            wrap="word",
            height=5,
            font=("Consolas", self.app.scaled(14))
        )
        self.app.custom_text_box.grid(row=0, column=0, sticky="nsew")

<<<<<<< HEAD
        custom_scrollbar = ttk.Scrollbar(custom_container, orient="vertical", command=self.app.custom_text_box.yview)
=======
        custom_scrollbar = ttk.Scrollbar(
            custom_container,
            orient="vertical",
            command=self.app.custom_text_box.yview
        )
>>>>>>> 1080e11 (Surviaval mode update)
        custom_scrollbar.grid(row=0, column=1, sticky="ns")
        self.app.custom_text_box.configure(yscrollcommand=custom_scrollbar.set)

        footer = ttk.Label(
            frame,
            text=self.app.tr("survival_footer"),
            padding=(0, self.app.scaled(10), 0, 0)
        )
        footer.grid(row=2, column=0, sticky="w")

        return frame

    def open_hamburger_menu(self):
        menu = tk.Menu(self.app.container, tearoff=0)
        menu.add_command(label=self.app.tr("main_menu"), command=self.app.show_main_menu)
        menu.add_command(label=self.app.tr("settings"), command=self.app.show_settings_menu)

        x = self.menu_button.winfo_rootx()
        y = self.menu_button.winfo_rooty() + self.menu_button.winfo_height()

        menu.tk_popup(x, y)

    def on_word_count_enter(self, event=None):
        self.app.load_generated_text()
        self.app.input_box.focus_set()