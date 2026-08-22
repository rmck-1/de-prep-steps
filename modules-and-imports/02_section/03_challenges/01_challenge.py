# ADD YOUR IMPORTS HERE
from faker import Faker

# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE

fake = Faker()


def generate_dating_profile():
    profile = {
        "name": fake.name(),
        "birthday": f"{fake.day_of_month()} {fake.month_name()}",
        "credit_card_number": fake.credit_card_number(),
        "credit_card_security_code": fake.credit_card_security_code(),
        "quote_that_describes_my_life": fake.catch_phrase(),
        "file_extension_that_describes_my_personality": fake.file_extension(),
        "my_favourite_http_method": fake.http_method(),
        "my_least_favourite_cryptocurrency": fake.cryptocurrency_name()

    }
    return profile


fake_profile = generate_dating_profile()
print(fake_profile)