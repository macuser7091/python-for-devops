What problem am I solving?
- Application logs are created every day, but manually checking them is time-consuming
- Need a quick way to identify INFO, WARNING, and ERROR messages
- Must summarize logs without reading entire files manually

What input does my script need?
- Path to a log file (app.log)
- Can optionally specify which log level to filter

What output should my script give?
- Terminal display showing count of INFO, WARNING, ERROR
- Summary written to a file (log_summary.txt)
- Clear, readable format

What are the main steps?
- Read the log file line by line
- Search for "INFO", "WARNING", "ERROR" keywords
- Count occurrences of each level
- Print summary to terminal
- Write summary to output file
- Handle errors gracefully (file not found, empty file)
