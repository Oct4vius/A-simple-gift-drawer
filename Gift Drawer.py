from dotenv import load_dotenv
from email.message import EmailMessage
import os
import ssl
import smtplib
import random


load_dotenv() 

email_sender = 'octaluper2@gmail.com'
email_password = os.environ['APP_PASSWORD']


participants = { 
    # here goes the persons going to the drawer
    # example => "name" : "email"

}

to_recive_gift = []

for participant in participants:
    to_recive_gift.append(participant)

subject = 'Here the subject'

body = ''

for participant in list(participants):

    randomParticipant = random.choice(to_recive_gift)

    print(participants)

    while(randomParticipant == participant):
        randomParticipant = random.choice(to_recive_gift)

    to_recive_gift.remove(randomParticipant)


    #Here goes the body of the email use {randomParticipant} to put the name of the random person
    body = f"""
    Hey {randomParticipant}!
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = participants[participant]
    em['Subject'] = subject
    em.set_content(body)

    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, participants[participant], em.as_string())