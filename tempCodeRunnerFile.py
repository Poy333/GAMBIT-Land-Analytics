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

# Add the new route for land_mapping
@app.route('/land_mapping')
def land_mapping():
    return render_template('land_mapping.html')  # Create this template

# Add the new route for team
@app.route('/team')
def team():
    return render_template('team.html')  # Create this template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
