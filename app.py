# app.py
from flask import Flask, render_template, request, jsonify
import os
import resend
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

    try:
        resend.api_key = os.getenv('RESEND_API_KEY')
        resend.Emails.send({
            "from": os.getenv('MAIL_RECIPIENT'),
            "to": [os.getenv('MAIL_ADDRESS')],
            "subject": "New Contact Form Submission",
            "text": f"From: {email}\n\nMessage:\n{message_content}",
        })
        return jsonify({'success': "Your message has been sent successfully!"}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'errors': {'general': "An error occurred while sending your message. Please try again later."}}), 500

if __name__ == '__main__':
    app.run(debug=True)
