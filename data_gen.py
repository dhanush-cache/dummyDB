from faker import Faker
from random import randint, choice


def get_us_number():
    """ Returns an United States phone number. """
    x = randint(200, 999)
    y = randint(1000, 9999)
    return f"({x}) {x}-{y}"


def get_email(name, domains=["gmail.com", "outlook.com"]):
    """ Returns an email address. """
    fname, lname, *trash = name.lower().split()
    username = choice([fname, fname + lname]) + str(randint(0, 1000))
    domain = choice(domains)
    return f"{username}@{domain}"


def get_person():
    """ Returns an imaginary person's info. """
    fake = Faker()
    person = {}

    person["name"] = fake.name()
    person["email"] = get_email(person["name"])
    person["phone"] = get_us_number()
    person["address"] = fake.address()

    return person
