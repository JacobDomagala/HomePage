# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Home Route - About Me Section
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    # Example projects data
    projects = [
        {'id': 1, 'title': 'Looper', 'description': 'A brief description of Project One.', 'image': 'project1.jpg'},
        {'id': 2, 'title': 'Shady', 'description': 'A brief description of Project Two.', 'image': 'project2.jpg'},
        {'id': 3, 'title': 'Chefy', 'description': 'A brief description of Project Three.', 'image': 'project3.jpg'},
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

if __name__ == '__main__':
    app.run(debug=True)