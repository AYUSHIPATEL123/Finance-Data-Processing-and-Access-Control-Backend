from fastapi_mail import FastMail,MessageSchema
import dotenv
import os
from config.email_config import conf

dotenv.load_dotenv()


async def send_reg_mail(email):
        mail = MessageSchema(
                subject="<h1>Welcome To APP From FINTECH COMPANY</h1>",
                body="Nice to meet you cline hope you will like our services from now in future.",
                from_email= os.getenv("EMAIL"),
                recipients=[email],
                subtype="html"
        )

        conn = FastMail(conf)
        await conn.send_message(mail)

        return "send email"