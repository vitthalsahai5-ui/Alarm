import tkinter as tk
from tkinter import messagebox
import time
import threading

def start_alarm():
    try:
        seconds = int(entry.get())
        if seconds <= 0:
            messagebox.showerror("Error", "Please enter a positive number of seconds.")
            return
        start_button.config(state=tk.DISABLED)
        entry.config(state=tk.DISABLED)
        threading.Thread(target=countdown, args=(seconds,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

def countdown(seconds):
    remaining = seconds
    while remaining > 0:
        root.after(0, lambda: countdown_label.config(text=f"Time remaining: {remaining} seconds"))
        time.sleep(1)
        remaining -= 1
    root.after(0, lambda: countdown_label.config(text="ALARM! Time's up!"))
    root.after(0, lambda: messagebox.showinfo("Alarm", "Time's up!"))
    try:
        import winsound
        winsound.Beep(1000, 1000)
    except ImportError:
        pass
    root.after(0, lambda: start_button.config(state=tk.NORMAL))
    root.after(0, lambda: entry.config(state=tk.NORMAL))

root = tk.Tk()
root.title("Python Alarm Timer")
root.geometry("300x200")

tk.Label(root, text="Enter alarm time in seconds:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
start_button = tk.Button(root, text="Start Alarm", command=start_alarm)
start_button.pack(pady=10)
countdown_label = tk.Label(root, text="Time remaining: --")
countdown_label.pack(pady=10)

root.mainloop()