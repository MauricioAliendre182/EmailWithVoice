import speech_recognition as sr
import smtplib  # Protocol SMTP
from email.message import EmailMessage

email = EmailMessage()  # We will create the object 'email'
r = sr.Recognizer()     # We will create the object 'r' to recognize your voice

while True:
    with sr.Microphone() as source:
        print("Say your subject...")
        audio = r.listen(source)

    # Now we will put all the data to send the email
    email['from'] = 'Name'
    email['to'] = 'example@gmail.com'
    try:
        subject_1 = email['subject'] = r.recognize_google(  # Email Subject
            audio, language="en-US")
        print(f'What did you say: {subject_1}')
    except:
        print('I am sorry! I can not understand!')
        break

    with sr.Microphone() as source_2:
        print("Say the content of your email...")
        audio_2 = r.listen(source_2)

    try:
        email_content = r.recognize_google(
            audio_2, language="en-US")  # Email Content
        email.set_content(email_content)
        print(
            f'What did you say: {email_content}')
    except:
        print('I am sorry! I can not understand!')
        break

    # We will configure an SMTP client session object
    with smtplib.SMTP(host='smtp.gmail.com', port=25) as smtp:
        smtp.ehlo()      # This is kind of like 'Hello' message
        smtp.starttls()  # TLS is an encryption mechanism

        # We have to login to our account to send the email
        smtp.login('something@gmail.com', 'XXXXYYYYZZZ')
        smtp.send_message(email)   # Send the message
        print('all good boss!')
        break

# IMPORTANT_NOTE: The name of the file must be different to 'email'
