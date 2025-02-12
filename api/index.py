from flask import Flask, render_template, request

app = Flask(__name__)

def message(i):
    a = (i + 1) % 10
    if a == 1 and not (11 <= i + 1 <= 20):
        return 'день'
    elif 2 <= a <= 4 and not (11 <= i + 1 <= 20):
        return 'дня'
    else:
        return 'дней'

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        try:
            N = int(request.form['days'])  # Количество дней похода
            total_sum = float(request.form['total_sum'])  # Общая сумма
            participants = []

            # Заполняем данные об участниках
            for i in range(N):
                participants.append(int(request.form[f'participant_{i}']))

            # Вычисляем общий коэффициент
            alpha = sum(participants)

            # Проверяем, чтобы не делить на 0
            if alpha == 0:
                return render_template('index.html', result=None, N=N, error="Количество участников не может быть 0")

            # Расчет суммы на каждого участника
            result = [
                {'day': i + 1, 'amount': round(total_sum * participants[i] / alpha, 2)}
                for i in range(N)
            ]

            return render_template('index.html', result=result, N=N)

        except Exception as e:
            return render_template('index.html', result=None, N=None, error=str(e))

    return render_template('index.html', result=None, N=None)

if __name__ == '__main__':
    app.run(debug=True)
