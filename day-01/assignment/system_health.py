import psutil

def system_health():
    threshold = int(input("Enter your cpu threshold: "))
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > threshold:
        print("Warning! system overload")
    else:
        print("System in safe condition")

system_health()