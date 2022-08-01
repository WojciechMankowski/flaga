from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class GmailAdapter:

    def __init__(self, port: int, host: str, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.server = smtplib.SMTP_SSL(host, port)

    def login(self) -> None:
        self.server.login(self.username, self.password)

    def sendemail(self, to_emails: str, subject: str, content: str):
        messege = self.__compose_messege(content, subject, to_emails)
        self.server.sendmail(self.username,to_emails,messege.as_string())

    def __compose_messege(self, content, subject, to_emails) -> MIMEMultipart:
        message = MIMEMultipart('alternative')
        message["Subject"] = subject
        message["From"] = self.username
        message["To"] = to_emails
        message.attach(
            MIMEText(content, "html")
        )
        return message

    def __del__(self) -> None:
        self.server.close()
