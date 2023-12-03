import config
import mail_service
import os
import dotenv


def test_send_mail():
    dotenv.load_dotenv()
    cfg = config.Config(mail=os.getenv("EMAIL"), password=os.getenv("EMAIL_PASSWORD"))

    mail_service.send_notification_email(cfg)
