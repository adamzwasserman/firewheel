# version 1.0 May 8 2018

# Python 3.6 modules
import os
import sys
import re
import time
import datetime
from pathlib import Path


# Main program
# Capture pathname of input_file
while True:
    input_file = (
        input("\nPlease enter the FULL pathname (inluding the file name) of the file with emails that you would "
              "like to replace:\n"))

    if not Path(input_file).is_file():
        print("\n\n***WARNING*** This is not a valid FULL pathname to a file. Please try again or press 0 to quit.\n\n")

    elif input_file is 0:
        sys.exit()

    else:
        filename, file_extension = os.path.splitext(input_file)
        raw = [line.strip() for line in open(input_file, 'r')]
        break

# Capture replacement_string
while True:
    replacement_string = (
        input("\nPlease enter the text that you would like to use to replace all email addresses in the file "
            "(leave empty to use redacted@example.com):\n"))

    if not replacement_string:
        replacement_string = 'redacted@example.com'
        break

    elif replacement_string is 0:
        sys.exit()

    else:
        break

# Confirm job
while True:
    green_light = (
        input("\nEvery email address in your file will be replaced by: {}\nPlease confirm that "
              "you want to proceed by typing y to continue, or n to quit:\n".format(replacement_string)))

    if green_light is "y":
        break

    elif green_light is "n":
        sys.exit()

    else:
        continue


# Start job
print("\n")
print("Let the replacment begin...")
search_pattern = re.compile(
    "[a-zA-Z0-9\!\#\$\%\'\*\+\-\^\_\`\{\|\}\~\.]+@(?!(\w+\.)*(jpg|png))(([\w\-]+\.)+([\w\-]+))|"
    "[a-zA-Z0-9\!\#\$\%\'\*\+\-\^\_\`\{\|\}\~\.]+\%40(?!(\w+\.)*(jpg|png))(([\w\-]+\.)+([\w\-]+))")
repl = "r'" + replacement_string + "'"

results = [(re.sub(search_pattern, replacement_string, i)) for i in raw]

# Save file
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M')
if len(results) > 0:
    print("\nCreating new file with anonymized emails...")
    output_filename = input_file + "-" + replacement_string + "-" + st + file_extension
    output_file = open(output_filename, 'w')
    for line in results:
        output_file.write(line + '\n')
    output_file.flush()

print("\nJob finished.")