Day Counter Timer ⏳

A simple and persistent day counter desktop app built with Python and Tkinter. This app helps you track a custom number of days and keeps counting even if you close the app or shut down your PC. Perfect for goals, challenges, or habit tracking.

Features
Enter any number of days as a target.
Start a timer that counts the days passed.
Persistent tracking: The counter continues even after closing the app or restarting your computer.
Shows:
Days Passed
Days Remaining
Progress percentage
Simple graphical user interface (GUI) using Tkinter.
Minimalist design with a progress bar.
Reset option to start over.
Placeholder input with proper validation and error handling.
Installation & Usage
Clone the repository:
git clone https://github.com/yourusername/day-counter-timer.git
Navigate into the folder:
cd day-counter-timer
Run the app with Python 3:
python day_counter.py
Screenshots

Add a screenshot of your app here for better visibility.

How it Works
The app saves the start date and total target days in a local JSON file (day_counter_data.json).
On reopening, it calculates the elapsed days based on the real-time date.
The progress bar updates automatically, and the app prevents multiple timers from starting simultaneously.
Requirements
Python 3.x
Tkinter (usually comes pre-installed with Python)
License

This project is open source and available under the MIT License.
