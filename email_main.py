import smtplib
import ssl
from email.message import EmailMessage
import datetime
from email_content import content

recipients_list = ['enter recipient(s) email']
email_sender = 'enter sender email'
email_password = 'enter your email password here'

msg = EmailMessage()
msg['Subject'] = f'Python email automation - {datetime.date.today().strftime("%d %b %Y")}'
msg['From'] = email_sender
msg['To'] = ', '.join(recipients_list)

msg.set_content(content, subtype='html')

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:    
    smtp.login(email_sender, email_password)    
    smtp.sendmail(email_sender, recipients_list, msg.as_string())
# as_string() - This method returns an entire message as string