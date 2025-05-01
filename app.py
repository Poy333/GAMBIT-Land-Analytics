from flask import Flask, render_template  # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/soil_science')
def soil_science():
    return render_template('soil_science.html')

@app.route('/land_mapping')
def land_mapping():
    barangays = [
        {
            'name': 'Babag',
            'sitios': [
                {
                    'name': 'Sitio 1',
                    'suitable': ['images/land_mapping/babag/sitio1/suitable1.jpg'],
                    'not_suitable': ['images/land_mapping/babag/sitio1/not_suitable1.jpg']
                },
                {
                    'name': 'Sitio 2',
                    'suitable': ['images/land_mapping/babag/sitio2/suitable1.jpg'],
                    'not_suitable': ['images/land_mapping/babag/sitio2/not_suitable1.jpg']
                },
                {
                    'name': 'Sitio 3',
                    'suitable': [],
                    'not_suitable': []
                },
                {
                    'name': 'Sitio 4',
                    'suitable': [],
                    'not_suitable': []
                },
                {
                    'name': 'Sitio 5',
                    'suitable': [],
                    'not_suitable': []
                }
            ]
        },
        {
            'name': 'Bon-bon',
            'sitios': [
                {'name': 'Sitio 1', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 2', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 3', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 4', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 5', 'suitable': [], 'not_suitable': []}
            ]
        },
        {
            'name': 'Buot',
            'sitios': [
                {'name': 'Sitio 1', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 2', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 3', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 4', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 5', 'suitable': [], 'not_suitable': []}
            ]
        },
        {
            'name': 'Sudlon 1',
            'sitios': [
                {'name': 'Sitio 1', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 2', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 3', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 4', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 5', 'suitable': [], 'not_suitable': []}
            ]
        },
        {
            'name': 'Malubog',
            'sitios': [
                {'name': 'Sitio 1', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 2', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 3', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 4', 'suitable': [], 'not_suitable': []},
                {'name': 'Sitio 5', 'suitable': [], 'not_suitable': []}
            ]
        }
    ]
    return render_template('land_mapping.html', barangays=barangays)

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
