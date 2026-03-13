
## 3/12/26 5:45PM:

I know this project requires three programs: a logger, an encryption program, and a driver program. The logger writes log messages to a log file, and will include the time, an action, and a message for each entry. The encryption program accepst commands from standard input and is used to set a password, encrypt and decrypt words using the password, and quit the program. The encryption program will always respond with either a result or an error. The driver will create two processes to execute the logger and encryption programs, and prompts the user to use the following commands: password, encrypt, decrypt, history, quit.

My plan is to complete the project in 3 or 4 sessions, with each session focusing on a specfic program. I'll first start with the logger since it just needs to accept standard input and write to a file. Then, I'll work on the encryption program and make sure the Vigenere cipher and passkey logic work. Last, I'll build the driver program to handle user menus and fork the other processes.

## 3/12/26 6:15PM:

Thoughts so far:
I created my repository and made an initial commit. I'm ready to start working on the project, beginning with the logger since I think it's the most straightforward.

Plans for this session:
The goal is to fully implement the logger program. I will:
1. Set up the program to accept a single command line argument, which will be the name of the log file.
2. Create a continuous loop that reads lines of text from standard input until the word "QUIT" is inputted.
3. Parse the input so that the first group of characters is treated as the ACTION and the rest of the line is the MESSAGE.
4. Make a timestamp using the format YYYY-MM-DD HH:MM.
5. Format the final output string as "YYYY-MM-DD HH:MM [ACTION] MESSAGE" and append it to the log file.

## 3/12/26 7:30PM:

Reflections on Session 1:
I accomplished my goal to finish the logger program. During this session, I set up the code to accept the log file as a command line argument, then created a stdin loop to read incoming messages and used datetime to get the current time for the timestamp.

Some issues I faced were that I didn't add a new line to my log entry so all the entries appended on one line. This was easily fixed by adding "\n" to the end of the log entry. When getting the date and time through datetime.now(), I didn't realize it included seconds and smaller at first so I removed that after. Also, when I was writing log entries to the file I first opened the log file in write mode so it was removing all the previous logs each time I ran the program. This was fixed by changing to append mode instead.

Next session I plan on working on the encryption program and finishing most of if not all of it. I'll need to set up the command loop to handle PASS, ENCRYPT, and DECRYPT, and I also need to correctly implement and test the Vigenere cipher.