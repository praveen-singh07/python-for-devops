import json

class LogAnalyzer:
    
    """Analyzes application log files and summarizes log levels."""
    
    def __init__(self, log_file = "app.log", output_file = "output.json"):
        self.log_file = log_file
        self.output_file = output_file
        self.log_count = {"INFO" : 0 ,"WARNING" : 0 ,"ERROR" : 0}
        
    # Read log file and return all log entries.
    def read_log_file(self):
        with open("app.log","r") as file:
            return (file.readlines())

    # Count INFO, WARNING, and ERROR log entries.     
    def analyze_logs(self):
        log_count = {"INFO" : 0 ,"WARNING" : 0 ,"ERROR" : 0}
        lines = self.read_log_file()
        
        if not lines:
            print("NO logs to analyze.")
            return
        
    # Loop through each log entry and update the count based on log level
        for line in lines:
            if "INFO" in line:
                #log_count.update({"INFO" : log_count["INFO"]+1})  
                self.log_count["INFO"] += 1 
            elif "WARNING" in line:
                #log_count.update({"WARNING" : log_count["WARNING"]+1})
                self.log_count["WARNING"] += 1
            elif "ERROR" in line:
                #log_count.update({"ERROR" : log_count["ERROR"]+1})
                self.log_count["ERROR"] += 1
            else:
                pass
        self.write_summary_to_json(self.log_count)
        return self.log_count

    def write_summary_to_json(self,counts):
        # Write log summary to a JSON file."
        with open("output.json","a") as json_file:
            json.dump(counts,json_file)
            json_file.write("\n")
            print("Output has also save on output.json file")

if __name__ == "__main__":       
    log_analyzer = LogAnalyzer() # Creating a object 
    count = log_analyzer.analyze_logs()
    print("Log count are : ",count)