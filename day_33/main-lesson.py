import requests
import os
import smtplib
from datetime import datetime
from time import sleep
from dotenv import load_dotenv

MY_LAT = 52.438671
MY_LNG = 4.825480


def sendmail(email, message, subject):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=username,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{message}"
        )


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_longitude, iss_latitude)


def get_sunup_sundown():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return (sunrise, sunset)


def iss_close_by():  # Your position is within +5 or -5 degrees of the ISS position.
    iss_longitude, iss_latitude = get_iss_position()
    lat_close = (MY_LAT - 5) < iss_latitude < (MY_LAT + 5)
    lng_close = (MY_LNG - 5) < iss_longitude < (MY_LNG + 5)
    return (lat_close and lng_close)


load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
email = os.getenv("TOEMAIL")


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    sunrise, sunset = get_sunup_sundown()
    time_now = datetime.now()
    if (sunset < time_now.hour < sunrise) & iss_close_by():
        sendmail(
            email=email,
            message="Hi,\n\nISS is currently overhead!\nYou might want to look up",
            subject="ISS Overhead"
        )
        break
    else:
        sleep(60)
