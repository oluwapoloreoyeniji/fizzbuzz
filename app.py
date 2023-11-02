from flask import Flask, render_template
app = Flask(__name__)

@app.route('/fizzbuzz')
def fizz_buzz():
    numbers = range(1, 101)
    return_list = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            return_list.append('FizzBuzz')
        elif num % 3 == 0:
            return_list.append('Fizz')
        elif num % 5 == 0:
            return_list.append('Buzz')
        else:
            return_list.append(num)

    return render_template('fizzbuzz.html', return_list=return_list)