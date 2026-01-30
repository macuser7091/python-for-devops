class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    def read_log(self):
        try:
            with open(self.log_file, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def analyze(self):
        lines = self.read_log()
        if not lines:
            return False
        
        if not lines:
            print("Error: Log file is empty")
            return False
        
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
        
        return True
    
    def print_summary(self):
        print("\n=== Log Summary ===")
        print(f"INFO: {self.counts['INFO']}")
        print(f"WARNING: {self.counts['WARNING']}")
        print(f"ERROR: {self.counts['ERROR']}")
        print("==================\n")
    
    def write_summary(self, output_file):
        try:
            with open(output_file, 'w') as f:
                f.write("=== Log Summary ===\n")
                f.write(f"INFO: {self.counts['INFO']}\n")
                f.write(f"WARNING: {self.counts['WARNING']}\n")
                f.write(f"ERROR: {self.counts['ERROR']}\n")
                f.write("==================\n")
            print(f"Summary written to {output_file}")
        except Exception as e:
            print(f"Error writing summary: {e}")

def main():
    analyzer = LogAnalyzer("../app.log")
    if analyzer.analyze():
        analyzer.print_summary()
        analyzer.write_summary("log_summary.txt")

if __name__ == "__main__":
    main()
