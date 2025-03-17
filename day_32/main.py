# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
#    name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import os
import smtplib
from dotenv import load_dotenv
from random import choice
from datetime import datetime

TEMPLATEDIR = './letter_templates'
BIRTHDAY_DB = './birthdays.csv'


def sendmail(email, message, subject="Happy Birtday!"):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=username,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{message}"
        )


load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

today = datetime.now()
data = pandas.read_csv(BIRTHDAY_DB)
active_birthdays = data[(data['month'] == today.month) & (data['day'] == today.day)].to_dict("records")
templates = os.listdir(TEMPLATEDIR)

if not active_birthdays == []:
    for bd in active_birthdays:
        with open(f"./letter_templates/{choice(templates)}") as file:
            message = file.read()
            message = message.replace("[NAME]", bd['name'])
        sendmail(email=bd['email'], message=message)
else:
    print("No birthdays today!")
