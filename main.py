import re
import smtplib
from email.message import EmailMessage
user_email = "ghjk"


def check_email(user_email):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    return pattern.search(user_email)


while not check_email(user_email):
    print('What is your email?  ')
    user_email = input()
    if check_email(user_email):
        user_name = user_email[:user_email.index('@')]
        domain_name = user_email[user_email.index('@') + 1:].split('.')[0]
        if domain_name == 'gmail':
            print(f'Hi {user_name.capitalize()} I see your email is registered with Google')
        elif domain_name == 'yahoo':
            print(f'Hi {user_name.capitalize()} I see your email is registered with Yahoo')
        elif domain_name == 'hotmail' or domain_name == 'outlook':
            print(f'Hi {user_name.capitalize()} I see your email is registered with Microsoft')
        else:
            print(f'Hi {user_name.capitalize()} it seems like you have your own custom domain at {domain_name}!')
        email = EmailMessage()
        email['from'] = '@Your name or name of your organization'
        email['to'] = user_email
        email['subject'] = 'Your email know is in our list'
        email.set_content('We are so happy, that you join our community!')
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('email', 'password')
            smtp.send_message(email)
        print('We sent you an email')
    else:
        print('Please, enter a correct email. Thank you!')
