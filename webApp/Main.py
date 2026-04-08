from flask import Flask, render_template, request

app = Flask(__name__)

subjects = [
    {'id': 'subj-1', 'name': 'Math Review', 'difficulty': 4, 'estimatedMinutes': 55},
    {'id': 'subj-2', 'name': 'English Reading', 'difficulty': 2, 'estimatedMinutes': 30},
    {'id': 'subj-3', 'name': 'Science Lab Prep', 'difficulty': 3, 'estimatedMinutes': 40},
    {'id': 'subj-4', 'name': 'History Essay', 'difficulty': 3, 'estimatedMinutes': 45},
    {'id': 'subj-5', 'name': 'Chemistry Problems', 'difficulty': 4, 'estimatedMinutes': 50},
    {'id': 'subj-6', 'name': 'Spanish Vocabulary', 'difficulty': 2, 'estimatedMinutes': 25},
    {'id': 'subj-7', 'name': 'Physics Project', 'difficulty': 5, 'estimatedMinutes': 90},
    {'id': 'subj-8', 'name': 'Literature Analysis', 'difficulty': 3, 'estimatedMinutes': 35}
]

estimation = {
    'totalEstimatedTime': sum(subject['estimatedMinutes'] for subject in subjects),
    'subjectCount': len(subjects)
}

@app.route('/')
def main_screen():
    return render_template('template.html', subjects=subjects, page='select')

@app.route('/process-subjects', methods=['POST'])
def process_subjects():
    selected_ids = request.form.getlist('subjects')
    selected_subjects = [s for s in subjects if s['id'] in selected_ids]
    total_time = sum(s['estimatedMinutes'] for s in selected_subjects)
    return render_template('template.html', 
                         selected_subjects=selected_subjects,
                         total_time=total_time,
                         page='review')

if __name__ == '__main__':
    app.run(debug=True)
