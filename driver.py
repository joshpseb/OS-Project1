import sys
import subprocess

# makes sure an argument is provided
if len(sys.argv) < 2:
    print("Error: log file name not provided")
    sys.exit(1)

logFile = sys.argv[1]

loggerProcess = subprocess.Popen(
    ['python', 'encryption.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

encryptionProcess = subprocess.Popen(
    ['python', 'encryption.py'],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE
)

loggerProcess.stdin.write("START Driver program started.\n")
