from flask import Flask, jsonify


app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/imc/<stude>/<sex>/<v1>/<v2>/<lang>')
def calc(stude, sex, v1, v2, lang):
  data = {
    'Estudante' : str(stude),
    'Sexo': str(sex),
    'Peso' : int(v1),
    'Altura' : float(v2),
    'Idioma': str(lang),
    'IMC' : round(int(v1) /  (float(v2) * float(v2)), 2)
  }


  if (data['Sexo'] == 'F'):
    percentual = (data['IMC'] / 100) * 12.7
    data['IMC'] = round(data['IMC'] - percentual, 2)

    
  
  if (data['IMC'] < 18.5):
    data['Categoria'] = 'Baixo peso'
    
  elif (data['IMC'] >= 18.5 and data['IMC'] <= 24.9):
     data['Categoria'] = 'Peso normal'
    
  elif (data['IMC'] >= 25 and data['IMC'] <= 29.9):
     data['Categoria'] = 'Sobrepeso'  
    
  elif (data['IMC'] == 30):
    data['Categoria'] = 'Obesidade'
    
  elif (data['IMC'] > 30 and data['IMC'] <= 34.9):
    data['Categoria'] = 'Obesidade grau I'

  elif (data['IMC'] > 35 and data['IMC'] <= 39.9):
    data['Categoria'] = 'Obesidade grau II'

  elif (data['IMC'] >= 40):
    data['Categoria'] = 'Obesidade mórbida'

  

  if(lang == 'pt_br'):
    data.pop('Idioma')
    return jsonify(data)

  dataEng = {
    'Student' : str(stude),
    'Gender': str(sex),
    'Weight' : int(v1),
    'Height' : float(v2),
    'Language': str(lang),
    'BIC' : round(int(v1) /  (float(v2) * float(v2)), 2)
  }

  if (dataEng['Gender'] == 'F'):
    percentage = (dataEng['BIC'] / 100) * 12.7
    dataEng['BIC'] = round(dataEng['BIC'] - percentage, 2)

    
  if (dataEng['BIC'] < 18.5):
    dataEng['Category'] = 'Underweight'
    
  elif (dataEng['BIC'] >= 18.5 and dataEng['BIC'] <= 24.9):
     dataEng['Category'] = 'Normal weight'
    
  elif (dataEng['BIC'] >= 25 and dataEng['BIC'] <= 29.9):
     dataEng['Category'] = 'Overweight'  
    
  elif (dataEng['BIC'] == 30):
    dataEng['Category'] = 'Obese'
    
  elif (dataEng['BIC'] > 30 and dataEng['BIC'] <= 34.9):
    dataEng['Category'] = 'Obese I degree'

  elif (dataEng['BIC'] > 35 and dataEng['BIC'] <= 39.9):
    dataEng['Category'] = 'Obese II degree'

  elif (dataEng['BIC'] >= 40):
    dataEng['Category'] = 'Morbid obesity'

  
  if(lang == 'eng'): 
    dataEng.pop('Language')
    #return jsonify(dataEng)
    dataEngJson = jsonify(dataEng)
    return dataEngJson


app.run(host='0.0.0.0', port=81, debug=True)


