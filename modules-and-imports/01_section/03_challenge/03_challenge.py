# Create a greeting variable for the mentor using the data imported from the nested files
# Print the greeting to your terminal

# It should look something like "Good afternoon Simon Jackson!"
import sys
#sys.path.append('/Users/rossmckaig/de-prep-steps/modules-and-imports/01_section/03_challenge/data')
from data.file_1 import mentor_first_name
from data.file_2 import mentor_last_name

def greeting(first_name, last_name):
    return f'Good afternoon {first_name} {last_name}!'

print(greeting(mentor_first_name, mentor_last_name))
