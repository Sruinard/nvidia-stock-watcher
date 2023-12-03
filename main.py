import scraper
import dotenv
import config
import mail_service
import os
import time

if __name__ == "__main__":
    dotenv.load_dotenv()
    cfg = config.Config(mail=os.getenv("EMAIL"), password=os.getenv("EMAIL_PASSWORD"))

    task = scraper.Nvidia4090Available(
        url="https://store.nvidia.com/nl-nl/geforce/store/?page=1&limit=9&locale=nl-nl"
    )

    while True:
        is_available = scraper.Scraper().do_task(task)
        if is_available:
            mail_service.send_notification_email(cfg)

        n_minutes = 10
        n_seconds = 60

        time.sleep(n_minutes * n_seconds)
