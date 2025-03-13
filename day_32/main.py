import datetime as dt
import smtplib
from dotenv import load_dotenv
import os
from random import choice


def sendmail(message, subject="Happy Monday!"):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{message}"
        )


def get_qoute():
    with open("./quotes.txt") as file:
        data = file.readlines()
        return choice(data)


load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
to_email = os.getenv("TOEMAIL")

if dt.datetime.now().weekday() == 0:
    sendmail(message=get_qoute())
else:
    print(f'Not Monday({dt.datetime.now().weekday()})')
