import sys
from datetime import datetime

# Makes sure an argument is provided (checked by driver)
#if len(sys.argv) < 2:
#    print("Error: log file name not provided")
#    sys.exit(1)

logFileName = sys.argv[1]

# Opens log file in append mode
with open(logFileName, 'a') as logFile:

    # Continuously read lines from stdin
    for line in sys.stdin:

        # Gets rid of whitespace
        line = line.strip()

        if line == "QUIT":
            break

        # Only splits once based on first space
        parts = line.split(maxsplit=1)
        action = parts[0]

        if len(parts) > 1:
            message = parts[1]
        else:
            message = ""

        timestamp = str(datetime.now())
        # Cuts off seconds and smaller from timestamp
        timestamp = timestamp[:16]
        
        logEntry = f"{timestamp} [{action}] {message}\n"

        logFile.write(logEntry)

        logFile.flush()

        # Makes sure every response is outputted from the pipe instantly.
        sys.stdout.flush()


        