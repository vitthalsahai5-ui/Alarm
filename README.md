# Alarm
***
A simple application used to set alarms :D
***
### Overall purpose
The program allows a user to set an alarm by entering a duration in seconds, after which the program prints an alarm message and, on compatible systems, emits an audible tone. It is intended to be run in a terminal or command prompt, where the user can see printed messages and, if available, hear the beep.

### Imports and dependencies
At the top level, the script imports the standard library module time, which is used to suspend execution for a given number of seconds. Inside the alarm function, the script conditionally imports the winsound module, which is a Windows‑specific standard library module that can produce simple sounds through the system speaker. No third‑party dependencies are required.

### Alarm function behavior
The function set_alarm(seconds) encapsulates all logic related to starting and triggering the alarm for a specified duration. When called, it first prints a status message showing how many seconds the alarm has been set for, giving immediate visual feedback to the user about the configured delay. After this, it calls time.sleep(seconds), which blocks the current thread of execution for exactly the provided number of seconds, effectively creating the countdown.

Once the sleep period has completed, the function prints the message "ALARM! Time's up!" to indicate that the requested duration has fully elapsed. This print statement serves as the primary notification mechanism and will always be executed as long as the program is running normally and not interrupted. Immediately after printing the alarm message, the function attempts to play a short beep using the winsound.Beep function. It performs a try/except ImportError around the winsound import so that the program does not crash on non‑Windows systems where this module is unavailable. If winsound is successfully imported, it calls winsound.Beep(1000, 1000), producing a tone of frequency 1000 Hz for 1000 milliseconds (1 second). If the import fails, it instead prints a fallback message, "Beep not available on this system.", letting the user know that an audible alert could not be produced.

### User input and validation
Outside the function definition, the script handles interaction with the user via the console. It wraps input handling and conversion in a try/except block to guard against invalid input. The program calls input("Enter alarm time in seconds: "), which displays a prompt and waits for the user to type a value and press Enter. The returned string is then passed to int(...) in an attempt to convert it to an integer number of seconds.

If the conversion to int succeeds, the script then checks whether the resulting value is greater than zero. For strictly positive values, it calls set_alarm(seconds), starting the countdown for the requested duration. This ensures that the alarm only runs when a meaningful, positive delay has been provided. If the user enters zero or a negative value, the program does not call the alarm function; instead, it prints "Please enter a positive number." to inform the user that the input must be a positive integer and that no alarm has been scheduled.

If any error occurs during the integer conversion—most commonly when the user types a non‑numeric string—the int call raises a ValueError. This is caught by the surrounding except ValueError: block. In this case, the program prints "Invalid input. Please enter a number." and terminates without attempting to set an alarm. This prevents the program from crashing and provides clear feedback on what kind of input is expected.

### Program flow summary
From start to finish, the script follows a straightforward, linear control flow. First, it defines the helper function set_alarm(seconds), which is responsible for waiting and then triggering the notification, including the optional beep. Then, execution reaches the input section, where the user is prompted for a duration in seconds. The program attempts to convert this input to an integer and validates that it is positive. If validation passes, the alarm function is invoked and the script blocks for the given duration while time.sleep is running. After the wait completes, it prints an alarm message and either plays a beep on supported systems or prints a message indicating that the beep feature is not available. If the input is invalid—either non‑numeric or non‑positive—the program prints an explanatory error message and exits without setting any alarm.

