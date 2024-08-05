import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="00:00:00.000", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

        self.update_clock()

    def update_clock(self):
        if self.running:
            now = datetime.now()
            self.elapsed_time = (now - self.start_time).total_seconds()
            time_str = self.format_time(self.elapsed_time)
            self.time_label.config(text=time_str)
        self.root.after(1, self.update_clock)

    def format_time(self, elapsed):
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - timedelta(seconds=self.elapsed_time)
            self.running = True

    def pause(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00.000")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()