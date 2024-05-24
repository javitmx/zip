from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    # Cargar datos ficticios de inflación desde un archivo CSV
    df = pd.read_csv('datos.csv')

    # Graficar los datos de inflación
    plt.plot(df['Año'], df['Inflación'])
    plt.xlabel('Año')
    plt.ylabel('Inflación')
    plt.title('Inflación en Colombia (Últimos 10 años)')
    # Guardar la imagen del gráfico en el directorio static
    plt.savefig('static/inflacion.png')
    plt.close()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
