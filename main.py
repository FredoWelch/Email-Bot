import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'recipient@email.com'
email['subject'] = 'Subject Of Email'

email.set_content(html.substitute({'name': 'Fredo','age': '26'}), 'html')
#Contents of email; contents of this email will consists of text from an html file that can be made unique to each reciipient.

with smtplib.SMTP(host='smtp.email.com', port=587) as smtp:
#smtp.email.com will vary depending on the email server you use i.e (gmail)    
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email@email.com', 'your_password')
    smtp.send_message(email)
