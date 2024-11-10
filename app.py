from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML para el formulario
form_html = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Formulario</title>
  </head>
  <body>
    <h1>Captura de Datos</h1>
    <form method="post" action="/">
      <label for="name">Nombre:</label><br>
      <input type="text" id="name" name="name" required><br><br>
      <label for="age">Edad:</label><br>
      <input type="number" id="age" name="age" required><br><br>
      <input type="submit" value="Enviar">
    </form>
    {% if name and age %}
      <h2>La edad de {{ name }} es {{ age }}.</h2>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def hello():
    name = None
    age = None
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
    return render_template_string(form_html, name=name, age=age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
