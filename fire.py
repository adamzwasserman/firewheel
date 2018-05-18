# version 1.0 May 8 2018

# Python 3.6 modules
import os
import sys
import re
import warnings
from pathlib import Path

# 3rd party modules
import arrow
from tqdm import tqdm, TqdmSynchronisationWarning


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
        with warnings.catch_warnings():  # tqdm has a minor bug causing it throw warnings that would just confuse the user
            warnings.simplefilter("ignore", TqdmSynchronisationWarning)
            raw = [line.strip() for line in tqdm(open(input_file, 'r'), unit=" lines read")]
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
job_start = arrow.now()
search_pattern = re.compile(
    "[a-zA-Z0-9\!\#\$\%\'\*\+\-\^\_\`\{\|\}\~\.]+@(?!(\w+\.)*(jpg|png))(([\w\-]+\.)+([\w\-]+))|"
    "[a-zA-Z0-9\!\#\$\%\'\*\+\-\^\_\`\{\|\}\~\.]+\%40(?!(\w+\.)*(jpg|png))(([\w\-]+\.)+([\w\-]+))")
repl = "r'" + replacement_string + "'"

with warnings.catch_warnings():  # tqdm has a minor bug causing it throw warnings that would just confuse the user
    warnings.simplefilter("ignore", TqdmSynchronisationWarning)
    results = [(re.sub(search_pattern, replacement_string, i)) for i in tqdm(raw, unit="lines")]

# Save file
if len(results) > 0:
    print("\nCreating new file with anonymized emails...")
    output_filename = input_file + "-" + replacement_string + "-" + arrow.now().format('YYYY-MM-DD HH:mm') + file_extension
    output_file = open(output_filename, 'w')
    with warnings.catch_warnings():  # tqdm has a minor bug causing it throw warnings that would just confuse the user
        warnings.simplefilter("ignore", TqdmSynchronisationWarning)
        for i, line in tqdm(enumerate(results), total=len(results), unit="lines"):
            output_file.write(line + '\n')
        output_file.flush()

job_finish = arrow.now()
print("\nEnded run at: ", arrow.now().format('YYYY-MM-DD HH:mm:ss'), "and took ", (job_finish-job_start), "to run.")