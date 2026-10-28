import smtplib
import os

from dotenv import load_dotenv

load_dotenv()

APP_PASSWORD = os.getenv("APP_PASSWORD") 

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("you@gmail.com", "APP_PASSWORD")
server.sendmail("you@gmail.com", "someone@example.com", "Subject: Daily Report∖n∖nInventory check completed.")
server.quit()