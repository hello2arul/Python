import smtplib
import datetime
import pandas
import random
from constants import email, password


EMAIL = email
PASSWORD = password

day = datetime.datetime.now()
today = (day.month, day.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    person = birthday_dict[today]

    with open(file_path) as letter:
        contents = letter.read()
        # print(contents)
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # for secure transfer
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
