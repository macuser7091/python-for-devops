import argparse

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
    
    def analyze(self, level=None):
        lines = self.read_log()
        if not lines:
            return False
        
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
        
        return True
    
    def get_summary(self, level=None):
        if level:
            return {level: self.counts.get(level, 0)}
        return self.counts
    
    def print_summary(self, level=None):
        summary = self.get_summary(level)
        print("\n=== Log Summary ===")
        for key, val in summary.items():
            print(f"{key}: {val}")
        print("==================\n")
    
    def write_summary(self, output_file, level=None):
        try:
            summary = self.get_summary(level)
            with open(output_file, 'w') as f:
                f.write("=== Log Summary ===\n")
                for key, val in summary.items():
                    f.write(f"{key}: {val}\n")
                f.write("==================\n")
            print(f"Summary written to {output_file}")
        except Exception as e:
            print(f"Error writing summary: {e}")

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--out", default="log_summary.txt", help="Output file path")
    parser.add_argument("--level", choices=["INFO", "WARNING", "ERROR"], help="Filter by log level")
    
    args = parser.parse_args()
    
    analyzer = LogAnalyzer(args.file)
    if analyzer.analyze():
        analyzer.print_summary(args.level)
        analyzer.write_summary(args.out, args.level)

if __name__ == "__main__":
    main()
