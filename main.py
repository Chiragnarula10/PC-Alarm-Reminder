#Chirag Narula
import winsound
from win10toast import ToastNotifier


def timer(reminder,sec):
    notificator = ToastNotifier()
    notificator.show_toast("Reminder", f"""Alarm set successfully""", duration=sec)
    notificator.show_toast(f"Reminder", reminder, duration=2)

    frequency = 2000
    duration = 1000
    winsound.Beep(frequency, duration)


if __name__ == "__main__":
    words = input("Reminder of ??   ")
    sec = int(input("Enter seconds   "))
    timer(words,sec)
