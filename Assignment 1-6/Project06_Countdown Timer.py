import time

def countdown(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("⏰ Time's up!\a")  

try:
    t = int(input("Enter the time in seconds: "))
    if t < 0:
        raise ValueError("Time must be a non-negative integer.")
    countdown(t)
except ValueError as e:
    print("Invalid input:", e)
