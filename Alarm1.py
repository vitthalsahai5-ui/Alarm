import time

# Function to set and trigger the alarm
def set_alarm(seconds):
    print(f"Alarm set for {seconds} seconds. Waiting...")
    time.sleep(seconds)  # Pause for the specified time
    print("ALARM! Time's up!")  # Notification
    # Optional: Add a beep (Windows only)
    try:
        import winsound
        winsound.Beep(1000, 1000)  # Frequency 1000 Hz, duration 1000 ms
    except ImportError:
        print("Beep not available on this system.")

# Get user input for the alarm time
try:
    seconds = int(input("Enter alarm time in seconds: "))
    if seconds > 0:
        set_alarm(seconds)
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input. Please enter a number.")