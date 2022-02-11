# Sending an email to gmail via Python. : https://www.youtube.com/watch?v=Oz3W-LKfafE
import smtplib # SMTP cline session that can be used to send e-mail to a machine
import ssl # secure socket layer
from email.message import EmailMessage # {email} read, write and send simple messages
import imghdr

import os

def get_files_in_dir(path):
    with os.scandir(path) as entries:
        return [(file.name, file.path) for file in entries if file.is_file()]

def main():
    subject = 'Python test by Python'
    body = 'Test e-mail from Python'
    send_to_email = 'e-mail-to-send@gmail.com'
    send_from_email = 'your-email-to-send-from@gmail.com'
    password = 'your-email-to-send-from-password'

    message = EmailMessage()
    message['From'] = send_from_email
    message['To'] = send_to_email
    message['Subject'] = subject
    message.set_content(body)

    for file, path in get_files_in_dir('./img'):
        with open(path, 'rb') as fp:
            img_data = fp.read()
        message.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

    context = ssl.create_default_context() # creating secure connection



    print('SENDING E-MAIL ...')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server: # connecting to gmail server
        server.login(send_from_email, password)
        server.sendmail(send_from_email, send_to_email, message.as_string())
    print('DONE!')


if __name__ == '__main__':
    main()
    # print(get_files_in_dir('./img'))
