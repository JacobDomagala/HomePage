# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Home Route - About Me Section
@app.route('/')
def home():
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Projects Route
@app.route('/projects')
def projects():
    # Example projects data
    projects = [
        {'id': 1, 'title': 'Project One', 'description': 'A brief description of Project One.', 'image': 'project1.jpg'},
        {'id': 2, 'title': 'Project Two', 'description': 'A brief description of Project Two.', 'image': 'project2.jpg'},
        {'id': 3, 'title': 'Project Three', 'description': 'A brief description of Project Three.', 'image': 'project3.jpg'},
        # Add more projects as needed
    ]
    return render_template('projects.html', projects=projects)

# Project Detail Route
@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    # In a real application, fetch project details from a database
    project = {
        'id': project_id,
        'title': f'Project {project_id}',
        'description': f'Detailed description for Project {project_id}.',
        'image': f'project{project_id}.jpg',
        'link': 'https://github.com/yourusername/project{}'.format(project_id)
    }
    return render_template('project_detail.html', project=project)

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Handle Contact Form Submission
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Process the form data (e.g., send an email, save to database)
    # For demonstration, we'll just return a success message
    success_message = f"Thank you, {name}! Your message has been received."
    return render_template('contact_success.html', message=success_message)

if __name__ == '__main__':
    app.run(debug=True)