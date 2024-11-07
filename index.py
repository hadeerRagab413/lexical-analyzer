import re
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk

token_specification = [
    ('KEYWORD', r'\b(int|return|if|else|while|for|float|char|double|void|printf)\b'),
    ('NUMBER', r'\b\d+(\.\d*)?\b'),
    ('IDENTIFIER', r'\b[A-Za-z_]\w*\b'),
    ('OPERATOR', r'[+\-*/=><!]+'),
    ('BRACE', r'[\{\}\(\)]'),
    ('SEMICOLON', r';'),
    ('COMMENT', r'//.*?$|/\*.*?\*/'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.'),
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def lexical_analyze(c_code):
    tokens = []
    for match in re.finditer(token_regex, c_code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP' or kind == 'COMMENT':
            continue
        elif kind == 'MISMATCH':
            print(f"Warning: Unexpected character {value}")
            continue
        tokens.append((kind, value))
    return tokens

def analyze_code():
    c_code = code_input.get("1.0", tk.END).strip()
    if not c_code:
        messagebox.showerror("Input Error", "Please enter some C code to analyze.")
        return

    try:
        tokens = lexical_analyze(c_code)
        output_display.delete("1.0", tk.END)
        for token in tokens:
            output_display.insert(tk.END, f'{token[0]}: {token[1]}\n')
    except RuntimeError as e:
        messagebox.showerror("Error", str(e))

def create_interface():
    window = tk.Tk()
    window.title("C Lexical Analyzer")
    window.geometry("600x600")

    frame = ttk.Frame(window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    title_label = ttk.Label(frame, text="C Lexical Analyzer", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)

    instruction_label = ttk.Label(frame, text="Enter your C code below:", font=("Arial", 12))
    instruction_label.pack(anchor=tk.W)

    code_input_frame = ttk.Frame(frame)
    code_input_frame.pack(fill=tk.BOTH, expand=True)

    code_input = scrolledtext.ScrolledText(code_input_frame, height=10, font=("Courier New", 12))
    code_input.pack(fill=tk.BOTH, expand=True, pady=5)

    analyze_button = ttk.Button(frame, text="Lexical Analyze", command=analyze_code, style='TButton')
    analyze_button.pack(pady=10)

    output_label = ttk.Label(frame, text="Lexical Analysis Output:", font=("Arial", 12))
    output_label.pack(anchor=tk.W)

    output_display_frame = ttk.Frame(frame)
    output_display_frame.pack(fill=tk.BOTH, expand=True)

    output_display = scrolledtext.ScrolledText(output_display_frame, height=10, font=("Courier New", 12))
    output_display.pack(fill=tk.BOTH, expand=True, pady=5)

    return window, code_input, output_display

window, code_input, output_display = create_interface()

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), padding=10)

window.mainloop()
