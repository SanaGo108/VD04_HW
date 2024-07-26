from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    timezone = pytz.timezone('Europe/Moscow')  # Установка часового пояса
    now = datetime.now(timezone)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('home.html', current_time=current_time)  # Передача переменной в шаблон

if __name__ == '__main__':
    app.run(debug=True)


