# main.py
import tkinter as tk
from logic import CalculatorBackend

class CalculatorUI:
    def __init__(self, root):
        self.backend = CalculatorBackend()
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("380x520")
        self.root.configure(bg="#D2A374") # Wood-like background

        self._setup_styles()
        self._build_ui()

    def _setup_styles(self):
        self.colors = {
            "header": "#263238", "body": "#F0E4D3",
            "num": "#BBB4A9", "op": "#D28D4F", "clr": "#D35C5C"
        }

    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg=self.colors["header"], height=50)
        header.pack(fill="x")
        tk.Label(header, text="🐍 Python", bg=self.colors["header"], fg="#E6AF4B", font=("Arial", 14, "bold")).pack(side="left", padx=10)

        # Body
        body = tk.Frame(self.root, bg=self.colors["body"], bd=1, relief="solid")
        body.pack(fill="both", expand=True, padx=15, pady=15)

        # Screen
        self.display_var = tk.StringVar(value="0")
        screen = tk.Label(body, textvariable=self.display_var, bg="#EDE0CD", fg="#263238", 
                          font=("Arial", 30, "bold"), anchor="e", padx=10, pady=20, bd=1, relief="sunken")
        screen.pack(fill="x", padx=20, pady=20)

        # Buttons
        grid_frame = tk.Frame(body, bg=self.colors["body"])
        grid_frame.pack(pady=10)

        buttons = [
            ('7', 0, 0, 'num'), ('8', 0, 1, 'num'), ('9', 0, 2, 'num'), ('/', 0, 3, 'op'), ('C', 0, 4, 'clr'),
            ('4', 1, 0, 'num'), ('5', 1, 1, 'num'), ('6', 1, 2, 'num'), ('*', 1, 3, 'op'),
            ('1', 2, 0, 'num'), ('2', 2, 1, 'num'), ('3', 2, 2, 'num'), ('-', 2, 3, 'op'),
            ('0', 3, 0, 'num', 2), ('=', 3, 2, 'op', 2), ('+', 3, 4, 'op')
        ]

        for b in buttons:
            text, r, c, theme = b[:4]
            span = b[4] if len(b) > 4 else 1
            
            btn = tk.Button(grid_frame, text=text, font=("Arial", 16, "bold"), 
                            bg=self.colors[theme], fg="white" if theme != 'num' else "#263238",
                            width=4 if span == 1 else 10, height=2,
                            command=lambda t=text: self._press(t))
            btn.grid(row=r, column=c, columnspan=span, padx=5, pady=5, sticky="nsew")

    def _press(self, key):
        # Send to backend and get the new display string
        result = self.backend.process_input(key)
        self.display_var.set(result)

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorUI(root)
    root.mainloop()