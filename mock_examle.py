
# https://pypi.org/project/Faker/0.7.4/

import csv

from faker import Factory
from random import randint, choice
from pprint import pprint


fake = Factory.create('uk_UA')

USER_TABLE = 'data/users.csv'

users: list[dict] = []
genders = ["female", "male"]

amount = int(input("Введіть кількість юзерів для генерації: "))
for _ in range(amount):
   
    gender = choice(genders)

    """simpe"""
    # if gender == 'male':
    #     first_name = fake.first_name_male()
    # else:
    #     first_name = fake.first_name_female()

    """ternar"""
    first_name = fake.first_name_female() if gender == 'female' else fake.first_name_male()
    last_name = fake.last_name_female() if gender == 'female' else fake.last_name_male()
    age = fake.random_int(min=5, max=60)
    phone = fake.phone_number()
    email = fake.email()
    user={"first_name": first_name, 
                 "last_name": last_name,
                 "age": age,
                 "gender": gender,
                 "phone": phone,
                 "email": email}
    users.append(user)

# pprint(users)

# write table
# with open(USER_TABLE, 'w', encoding="utf-8", newline='') as csvfile:
#     fieldnames = list(users[0].keys())
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
#     writer.writeheader()
#     writer.writerows(users)
#     print("Table saved")
    
# read table
with open(USER_TABLE, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    # simple way
    # info = []
    # for row in reader:
    #     info.append(row)

    # list comprehention
    # info = [row for row in reader]

    # super simple
    info = list(reader)

    pprint(info)


