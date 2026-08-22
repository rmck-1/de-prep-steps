#  Using the data stored in the nested file_1.py create a mentor_name variable
#  which stores the mentor name.

#  Make sure you print only the name, not the whole dictionary!
import sys
print(sys.path)
# sys.path.append('/Users/rossmckaig/de-prep-steps/modules-and-imports/01_section/02_challenge/data')
from data.file_1 import mentor

print(mentor['name'])
