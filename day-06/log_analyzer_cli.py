import json
import argparse

class LogAnalyzer:
    
    """Analyzes application log files and summarizes log levels."""
    
    def __init__(self, log_file = None, output_file = None, level = None):
        # Initialize with input file, output JSON file, and optional level filter
        
        self.log_file = log_file
        self.output_file = output_file
        self.level_filtered = level
        
        # Dictionary to count occurrences of each log level
        self.log_count = {"INFO" : 0 ,"WARNING" : 0 ,"ERROR" : 0}
        
    # Read log file and return all log entries.
    def read_log_file(self,log_file):
        
        # Open file in read mode and return list of lines
        with open(log_file,"r") as file:
            return (file.readlines())

    # Count INFO, WARNING, and ERROR log entries.     
    def analyze_logs(self,log_file):
        
        # Read all lines from the file
        lines = self.read_log_file(log_file)
        
        # If file is empty, inform user and exit early
        if not lines:
            print("NO logs to analyze.")
            return
        
    # Loop through each log entry and update the count based on log level
        for line in lines:
            
            # If "INFO" appears in the line, increase its count
            if "INFO" in line:  
                self.log_count["INFO"] += 1
                
            # If "WARNING" appears, increase its count
            elif "WARNING" in line:
                self.log_count["WARNING"] += 1
                
            # If "ERROR" appears, increase its count
            elif "ERROR" in line:
                self.log_count["ERROR"] += 1
                
            else:
                pass
            
            # If the user asked for only one level (e.g., only ERROR), return only that level and its count
        if self.level_filtered:
            return {self.level_filtered: self.log_count.get(self.level_filtered, 0)}
        
        # Otherwise return counts for all levels
        return self.log_count
    
    # Save the summary counts to a JSON file
    def write_summary_to_json(self,counts,output_file):
        
        # Open file in append mode so we don't overwrite previous results
        with open(output_file,"a") as json_file:
            json.dump(counts,json_file)
            json_file.write("\n")
            print(f"Output has also save on {output_file} file")
            
def main():
    
    # Create parser to accept command line arguments
    parser = argparse.ArgumentParser()
    
    # Required argument: path to log file
    parser.add_argument("--file", "-f", required=True, help="Path to the log file")
    
    # Required argument: where to save the JSON summary
    parser.add_argument("--out", "-o", required=True, help="output for for saving Json summary")
    
    # Optional argument to filter output for single log level
    parser.add_argument("--level", "-l", choices=["INFO","WARNING","ERROR"], help="Filter output for a single log level")

    # Parse the arguments
    args = parser.parse_args()    
    
    # Create LogAnalyzer object with optional level filter
    log_analyzer = LogAnalyzer(level=args.level)
    counts = log_analyzer.analyze_logs(log_file=args.file)
    print("Log counts are : ",counts)
    log_analyzer.write_summary_to_json(counts, output_file=args.out)
    
# Makes sure this script runs only when executed directly (not when imported)  
if __name__ == "__main__":
    main()