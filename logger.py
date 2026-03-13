import sys
from datetime import datetime

# makes sure an argument is provided
if len(sys.argv) < 2:
    print("Error: log file name not provided")
    sys.exit(1)

logFileName = sys.argv[1]

# opens log file in append mode
with open(logFileName, 'a') as logFile:

    # continuously read lines from stdin
    for line in sys.stdin:

        # gets rid of whitespace
        line = line.strip()

        if line == "QUIT":
            break

        # only splits once based on first space
        parts = line.split(maxsplit=1)
        action = parts[0]

        if len(parts) > 1:
            message = parts[1]
        else:
            message = ""

        timestamp = str(datetime.now())
        # cuts off seconds and smaller from timestamp
        timestamp = timestamp[:16]
        
        logEntry = f"{timestamp} [{action}] {message}\n"

        logFile.write(logEntry)


        