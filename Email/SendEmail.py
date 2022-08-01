from dotenv import load_dotenv
from os import getenv
from gmail_adapter import GmailAdapter
from thanks_message import ThanksMessage


def send_thanks_emails(to_email: str, nameuser: str, subject: str, contemt: str):
    load_dotenv(dotenv_path="../.env")
    adapter = GmailAdapter(host="smtp.gmail.com", port=465, 
    username=getenv("EMAIL"), password=getenv("CODEGMAIL")
    )
    adapter.login()
    messege = ThanksMessage()
    adapter.sendemail(to_email, "Dziękuję za Twoją wiadomość.", messege.render(name=nameuser, subject=subject,contemt=contemt))



    