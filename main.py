import smtplib
import datetime as dt
import random

MY_EMAIL = #put your e-mail here, as string
MY_PASSWORD = #put your password here as string
DAY_TO_SEND = 4
today = dt.datetime.now()
day_of_the_week = today.weekday()

with open('quotes.txt') as file:
    data = file.readlines()
    new_data = [(line.split('-')) for line in data]
    quotes = [(line[0].strip(), line[1].strip()) for line in new_data]

chosen_quote = random.choice(quotes)
quote = f"{chosen_quote[0]} - {chosen_quote[1]}"
e_mail_to_send_to = #put an e-mail here as string

if day_of_the_week is DAY_TO_SEND:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=e_mail_to_send_to,
                            msg=f"Subject: Monday Quotes!!\n\n{quote}")
