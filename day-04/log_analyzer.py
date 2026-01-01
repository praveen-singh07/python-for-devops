import json # Used to store log summary in JSON format

# Read the app.log file and return all log lines as a list
def get_data():
    with open("app.log","r") as file:
        return (file.readlines())

# Analyze log lines and count INFO, WARNING, and ERROR messages     
def log_analyze(lines):
    log_count = {
        "INFO" : 0 ,
        "WARNING" : 0 ,
        "ERROR" : 0
    }
    
# Loop through each log entry and update the count based on log level
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO" : log_count["INFO"]+1})    
        elif "WARNING" in line:
            log_count.update({"WARNING" : log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR" : log_count["ERROR"]+1})
        else:
            pass
    return log_count

# Save the analyzed log counts into a JSON file
def write_json(counts):
    with open("output.json","w+") as Json_file:
        json.dump(counts,Json_file)
        print("Output has also save on output.json file")
        
# Call functions to read logs, analyze them, and display the result                           
lines = get_data()
counts = log_analyze(lines)
print("log count are : ",counts)
write_json(counts)
