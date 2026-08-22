# Import the function from the utils.py file
# Import the numbers from the file in the nested data directory

# You should see the number 35
from utils import sum_nums
import sys
#sys.path.append('/Users/rossmckaig/de-prep-steps/modules-and-imports/01_section/04_challenge/data/nested_data')
from data.nested_data.example_numbers import num_1, num_2

result = sum_nums(num_1, num_2)
print(result)
