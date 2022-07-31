from itertools import starmap
from dotenv import load_dotenv
from os import getenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jinja2

load_dotenv(dotenv_path="./.env")


