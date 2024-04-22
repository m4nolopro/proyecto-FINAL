# Importando lo necesario
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/n')
def reciclar():
    return render_template(
                            'reciclar.html', 
                            
                           )

# La tercera página
@app.route('/h')
def electronics():
    return render_template(
                            'manualidades.html',                           
                                                    
                           )

app.run(debug=True)

