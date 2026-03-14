# CS 4348.003 Project 1
Josh Sebastian JXS230046

## Project Overview
This project uses a multi-process system with a frontend driver and two backend processes for encryption and logging. It uses the Vigenere cipher for encryption and decryption, and the user can input text along with a key in the form of a password. All interprocess communication is handled through standard input and output pipes.

## Files and Their Roles:

### driver.py:
This is the main frontend program. It launches the backend processes, provides a menu with commands for the user, validates all user input, and manages temporary session history.
### encryption.py:
This is the backend encryption program. It runs continuously, stores a passkey that can be changed, and does the Vigenere cipher math when encrypting or decrypting text. It assumes all inputs are uppercase and valid, which is handled by the driver.
### logger.py:
This is the backend logging program. It runs continuously, listening for logging events from the driver and writes them to a specified log file. Each log entry includes a timestamp, an action, and a message. It includes all history between multiple runs.
### devlog.md:
This is my development log. It records my planning, progress, and any problems I came across as I was working on this project across four coding sessions.

## How to Compile and Run:
Since the project runs on Python, there is no compilation needed. The project can be run directly from the command line using the following:
```bash
python driver.py log.txt
```