# ADD YOUR IMPORTS HERE
from datetime import datetime

# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE


def get_todays_date():
    today = datetime.now().strftime("%d %B, %Y")
    return today


print(get_todays_date())
