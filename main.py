import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Freddie Welch'
email['to'] = 'welch.freddie@gmail.com'
email['subject'] = 'Did you get this'

email.set_content(html.substitute({'name': 'Fredo','age': '26'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('fsandersw1994@gmail.com', 'Lilsizzle3')
    smtp.send_message(email)
