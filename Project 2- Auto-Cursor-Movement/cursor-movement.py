

# =============================
# Auto-install required packages
# =============================
import sys
import subprocess

def ensure_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for pkg in ["pywinauto", "tkinter"]:
    ensure_package(pkg)

# =============================
# Imports
# =============================
import time
import random
from pywinauto import Desktop
import pywinauto.mouse
import tkinter as tk
from tkinter import ttk, messagebox

# =============================
# Professional Tkinter Dialog
# =============================
class IntervalDialog:
    def __init__(self):
        self.value = None
        self.root = tk.Tk()
        self.root.title("Cursor Mover Settings")
        self.root.geometry("420x220")
        self.root.resizable(False, False)
        self.root.configure(bg="#232946")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#232946", foreground="#eebbc3", font=("Segoe UI", 14, "bold"))
        style.configure('TButton', font=("Segoe UI", 12, "bold"), foreground="#232946", background="#eebbc3", borderwidth=0)
        style.map('TButton', background=[('active', '#d4939d')])
        style.configure('TEntry', font=("Segoe UI", 13), fieldbackground="#eebbc3", foreground="#232946")

        label = ttk.Label(self.root, text="How many seconds between cursor moves?", anchor="center")
        label.pack(pady=(35, 10))

        self.entry_var = tk.StringVar()
        entry = ttk.Entry(self.root, textvariable=self.entry_var, width=12, justify="center")
        entry.pack(pady=8)
        entry.focus()

        ok_btn = ttk.Button(self.root, text="OK", command=self.on_ok)
        ok_btn.pack(pady=(18, 0))

        self.root.bind('<Return>', lambda event: self.on_ok())

    def on_ok(self):
        try:
            val = int(self.entry_var.get())
            if val < 1:
                raise ValueError
            self.value = val
            self.root.destroy()
        except Exception:
            messagebox.showerror("Invalid Input", "Please enter a positive integer.")

    def get_value(self):
        self.root.mainloop()
        return self.value

# =============================
# Foreground window and mouse movement
# =============================

def get_screen_size():
    try:
        import ctypes
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return screensize
    except Exception:
        # fallback to pywinauto
        from pywinauto import Application
        app = Application().connect(path="explorer.exe")
        desktop = app.top_window()
        rect = desktop.rectangle()
        return rect.right, rect.bottom

def move_mouse_drag_screen(steps=50, duration=1.2):
    width, height = get_screen_size()
    try:
        from pywinauto.mouse import get_cursor_pos
        start_x, start_y = get_cursor_pos()
    except Exception:
        # If unable to get current position, pick a random start
        start_x = random.randint(20, width - 20)
        start_y = random.randint(20, height - 20)

    # Always start from current position, and animate to a random end position
    end_x = random.randint(20, width - 20)
    end_y = random.randint(20, height - 20)

    # Animate the cursor from start to end
    for i in range(1, steps + 1):
        x = int(start_x + (end_x - start_x) * i / steps)
        y = int(start_y + (end_y - start_y) * i / steps)
        pywinauto.mouse.move(coords=(x, y))
        time.sleep(duration / steps)

# =============================
# Main logic
# =============================
def main():
    print("Bot is running. Press Ctrl+C to exit.")
    dialog = IntervalDialog()
    interval = dialog.get_value()
    if not interval:
        print("No interval provided. Exiting.")
        return
    while True:
        try:
            move_mouse_drag_screen()
            print(f"Moved mouse on screen. Waiting {interval} seconds.")
        except Exception as e:
            print(f"Error moving mouse: {e}. Retrying in 5 seconds...")
            time.sleep(5)
            continue
        time.sleep(interval)

if __name__ == "__main__":
    main()
