import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os
from datetime import datetime

# File to store timer data
DATA_FILE = "day_counter_data.json"


class DayCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day Counter")
        self.root.geometry("360x320")
        self.root.resizable(False, False)

        self.start_time = None
        self.total_days = None

        self.create_ui()
        self.load_data()
        self.update_display()

    def create_ui(self):
        # Title
        tk.Label(self.root, text="Day Counter", font=("Arial", 16, "bold")).pack(pady=10)

        # Input field with placeholder
        self.entry = tk.Entry(self.root, justify="center", font=("Arial", 12), fg="grey")
        self.entry.pack(pady=5)
        self.entry.insert(0, "Enter days")

        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start", width=10, command=self.start_timer).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Reset", width=10, command=self.reset_timer).grid(row=0, column=1, padx=5)

        # Display labels
        self.passed_label = tk.Label(self.root, text="Days Passed: 0", font=("Arial", 12))
        self.passed_label.pack(pady=5)

        self.remaining_label = tk.Label(self.root, text="Days Remaining: 0", font=("Arial", 12))
        self.remaining_label.pack(pady=5)

        self.percent_label = tk.Label(self.root, text="Progress: 0%", font=("Arial", 12))
        self.percent_label.pack(pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=260, mode="determinate")
        self.progress.pack(pady=10)

    # Placeholder functions
    def clear_placeholder(self, event):
        if self.entry.get() == "Enter days":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Enter days")
            self.entry.config(fg="grey")

    def start_timer(self):
        # Prevent multiple timers
        if self.start_time is not None:
            messagebox.showinfo("Info", "Timer already running!")
            return

        try:
            value = self.entry.get()
            if value == "Enter days":
                raise ValueError

            days = int(value)
            if days <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of days!")
            return

        self.start_time = datetime.now()
        self.total_days = days

        self.save_data()
        self.update_display()

    def reset_timer(self):
        self.start_time = None
        self.total_days = None

        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

        # Reset UI
        self.passed_label.config(text="Days Passed: 0")
        self.remaining_label.config(text="Days Remaining: 0")
        self.percent_label.config(text="Progress: 0%")
        self.progress["value"] = 0

        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Enter days")
        self.entry.config(fg="grey")

    def save_data(self):
        data = {
            "start_time": self.start_time.isoformat(),
            "total_days": self.total_days
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.start_time = datetime.fromisoformat(data["start_time"])
                    self.total_days = data["total_days"]
            except Exception:
                self.start_time = None
                self.total_days = None

    def update_display(self):
        if self.start_time and self.total_days:
            now = datetime.now()
            elapsed = now - self.start_time

            days_passed = elapsed.days
            remaining = max(self.total_days - days_passed, 0)

            percent = min((days_passed / self.total_days) * 100, 100)

            self.passed_label.config(text=f"Days Passed: {days_passed}")
            self.remaining_label.config(text=f"Days Remaining: {remaining}")
            self.percent_label.config(text=f"Progress: {percent:.2f}%")
            self.progress["value"] = percent

        # Refresh every second
        self.root.after(1000, self.update_display)


if __name__ == "__main__":
    root = tk.Tk()
    app = DayCounterApp(root)
    root.mainloop()
