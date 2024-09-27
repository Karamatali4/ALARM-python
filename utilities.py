import time
import threading
from tkinter import messagebox
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

def get_current_time():
    """Returns the current time in 12-hour format with AM/PM."""
    return time.strftime("%I:%M %p")

def play_alarm_sound():
    """Plays an alarm sound."""
    pygame.mixer.music.load("alarm.wav")  # Replace with your alarm sound file path
    pygame.mixer.music.play()

def show_alarm_notification():
    """Displays a pop-up notification when the alarm goes off."""
    messagebox.showinfo("Alarm", "Time to wake up!")

def check_time_for_alarm(alarm_time):
    """Continuously checks if the current time matches the alarm time."""
    while True:
        current_time = get_current_time()
        if current_time == alarm_time:
            play_alarm_sound()
            show_alarm_notification()
            break
        time.sleep(1)

def set_alarm(hour, minute, period, window):
    """Sets the alarm time and starts the thread to check the time."""
    alarm_time = f"{hour}:{minute} {period}"
    messagebox.showinfo("Alarm Set", f"Alarm is set for {alarm_time}")

    # Start a new thread to avoid blocking the GUI
    alarm_thread = threading.Thread(target=check_time_for_alarm, args=(alarm_time,))
    alarm_thread.start()
