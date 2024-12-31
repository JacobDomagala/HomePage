# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Home Route - About Me Section
@app.route('/')
def home():
    return render_template('index.html')

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