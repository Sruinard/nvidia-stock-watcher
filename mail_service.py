import config
import smtplib


# Function to send email notification
def send_notification_email(config: config.Config):
    # Replace the following placeholders with your email information

    # send to self
    sender_email = config.mail
    sender_password = config.password
    receiver_email = config.mail

    # Setup the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a secure connection with the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to your email account
    server.login(sender_email, sender_password)

    # Compose the email message
    subject = "Product in Stock Notification"
    body = "Hooray! The product you wanted is now in stock."

    # Construct the email
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email, receiver_email, message)

    # Quit the server
    server.quit()
