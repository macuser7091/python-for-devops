"""Improved System Health script for Day 03 assignment.

Enhancements:
- Structured with functions
- Input validation
- Basic exception handling
- Clear, user-friendly messages
"""
import sys
import time

try:
    import psutil
except Exception as e:
    print("psutil is required to run this script. Install it with: pip install psutil")
    sys.exit(1)


def get_threshold(prompt="Enter CPU threshold (0-100): "):
    while True:
        try:
            val = input(prompt).strip()
            if val == "":
                print("No input provided. Please enter a number between 0 and 100.")
                continue
            threshold = int(val)
            if not 0 <= threshold <= 100:
                print("Please enter a value between 0 and 100.")
                continue
            return threshold
        except ValueError:
            print("Invalid input. Please enter an integer value.")
        except KeyboardInterrupt:
            print("\nUser cancelled input. Exiting.")
            raise


def check_cpu(threshold, interval=1.0):
    try:
        cpu_percent = psutil.cpu_percent(interval=interval)
        return cpu_percent
    except Exception as e:
        print(f"Failed to read CPU usage: {e}")
        return None


def report(cpu_percent, threshold):
    if cpu_percent is None:
        print("Could not determine CPU usage. Please try again later.")
        return

    print(f"Current CPU usage: {cpu_percent:.1f}%")
    if cpu_percent > threshold:
        print("Warning: System overload — take action!")
    else:
        print("System in safe condition.")


def main():
    try:
        threshold = get_threshold()
    except KeyboardInterrupt:
        return

    print("Measuring CPU usage... (this may take a second)")
    cpu = check_cpu(threshold)
    report(cpu, threshold)


if __name__ == "__main__":
    main()
