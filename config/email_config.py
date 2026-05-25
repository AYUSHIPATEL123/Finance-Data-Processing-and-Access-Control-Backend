from fastapi_mail import ConnectionConfig
import os
import dotenv

dotenv.load_dotenv()


conf = ConnectionConfig(
    MAIL_FROM=os.getenv("EMAIL"),
    MAIL_PASSWORD=os.getenv("EMAIL_APP_PASSWORD"),
    MAIL_USERNAME=os.getenv("EMAIL"),
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS=True,
)
