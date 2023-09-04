import smtplib
from email.message import EmailMessage
from .mail_template import html_header, body_content, html_end


def send_mail(userprofile):
    EMAIL_ADDRESS = 'bhuvish22@gmail.com'
    EMAIL_PASSWORD = 'drkiktsgedrbmgfq'
    msg = EmailMessage()
    msg['Subject'] = 'SOP'
    msg['From'] = EMAIL_ADDRESS 
    msg['To'] = userprofile.email
    email_content = ''
    email_content += html_header
    email_content += body_content(userprofile)
    email_content += html_end
    msg.set_content(email_content, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)



