import sys

def analyze_log(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    if not lines:
        print("Error: Log file is empty")
        return
    
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    for line in lines:
        if "INFO" in line:
            counts["INFO"] += 1
        elif "WARNING" in line:
            counts["WARNING"] += 1
        elif "ERROR" in line:
            counts["ERROR"] += 1
    
    return counts

def print_summary(counts):
    print("\n=== Log Summary ===")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")
    print("==================\n")

def write_summary(filename, counts):
    try:
        with open(filename, 'w') as f:
            f.write("=== Log Summary ===\n")
            f.write(f"INFO: {counts['INFO']}\n")
            f.write(f"WARNING: {counts['WARNING']}\n")
            f.write(f"ERROR: {counts['ERROR']}\n")
            f.write("==================\n")
        print(f"Summary written to {filename}")
    except Exception as e:
        print(f"Error writing summary: {e}")

def main():
    log_file = "../app.log"
    output_file = "log_summary.txt"
    
    counts = analyze_log(log_file)
    if counts:
        print_summary(counts)
        write_summary(output_file, counts)

if __name__ == "__main__":
    main()
