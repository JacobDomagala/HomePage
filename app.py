# app.py
from flask import Flask, render_template, request, jsonify
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail as SendGridMail
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/handle_contact', methods=['POST'])
def handle_contact():
    data = request.get_json()
    email = data.get('email')
    message_content = data.get('message')

    errors = {}

    # Basic validation
    if not email:
        errors['email'] = "Email is required."
    else:
        # Validate email format
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as e:
            errors['email'] = str(e)

    if not message_content:
        errors['message'] = "Message is required."

    if errors:
        return jsonify({'errors': errors}), 400

    # Compose the email using SendGrid
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    sg_mail = SendGridMail(
        from_email=os.getenv('MAIL_ADDRESS'),
        to_emails=os.getenv('MAIL_RECIPIENT'),
        subject="New Contact Form Submission",
        plain_text_content=f"From: {email}\n\nMessage:\n{message_content}"
    )

    try:
        response = sg.send(sg_mail)
        if response.status_code in [200, 202]:
            return jsonify({'success': "Your message has been sent successfully!"}), 200
        else:
            return jsonify({'errors': {'general': "Failed to send your message. Please try again later."}}), 500
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'errors': {'general': "An error occurred while sending your message. Please try again later."}}), 500

if __name__ == '__main__':
    app.run(debug=True)