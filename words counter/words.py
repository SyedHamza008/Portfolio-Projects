from datetime import date

from flask import Blueprint, render_template, request, current_app


bp = Blueprint('words', __name__, url_prefix='/words')

dateToday = date.today().strftime("%d-%m-%y")
dateToday2 = date.today().strftime("%d-%b-%y")

def paragrapgh_counter(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

@bp.route('/', methods=('GET',))
def index():
    return render_template('index.html', datetoday=dateToday, datetoday2=dateToday2)

@bp.route('/count', methods=('POST',))
def count():
    text = request.form['text']

    chars = len(text)

    words = text.split()
    word_le = len(words)

    paras = paragrapgh_counter(text)
    text = text.replace('\n', "")

    return render_template('index.html', chars=chars, word_le=word_le, paras = paras, datetoday=dateToday, datetoday2=dateToday2)