# Log Analyzer Script – Design Plan

## What problem am I solving?
- Application log files get very big
- Manually checking how many INFO, WARNING, and ERROR logs is time-consuming
- I want a script that:
  - Reads a log file
  - Counts log levels
  - Gives a clear summary
  - Saves the result for future use

## What input does my script need?
- User will give:
  - Log file path (example: app.log)
  - Output file path to save result (example: summary.json)
- Optional input:
  - Log level filter (INFO, WARNING, or ERROR)
  

## What output should my script give?
- Terminal output:
  - Dictionary showing count of log levels
  - Example:
    {'INFO': 10, 'WARNING': 3, 'ERROR': 2}

- JSON file output:
  - Same summary saved in a JSON format
  - Useful for reports or automation pipelines

If user gives a log level filter:
- Output will contain only that level
  - Example:
    {'ERROR': 2}

## What are the main steps?
- Take command-line arguments from user
- Read the log file line by line
- Check each line for:
  - INFO
  - WARNING
  - ERROR
- Increase count for each log level
- If level filter is provided:
  - Show only that log level
- Print result on terminal
- Save summary to JSON file
