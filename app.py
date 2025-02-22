from flask import Flask, render_template, request, send_file, url_for
import os
from calendar_generator import create_calendar

app = Flask(__name__)

# carpeta donde guardar calendarios generados
output_folder = 'generated'
os.makedirs(output_folder, exist_ok = True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods = ['POST'])
def generate():
    # coger mes y año del form
    year = int(request.form['year'])
    month = int(request.form['month'])

    # generar calendario
    calendar_name = create_calendar(year, month, output_folder)
    
    calendar_url = f'generated/{calendar_name}'

    return render_template('index.html', calendar_url = calendar_url)

if __name__ == '__main__':
    app.run(debug = True)