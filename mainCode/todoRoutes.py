import functools

import os
from werkzeug.utils import secure_filename
from flask import Blueprint, flash, redirect, render_template, request, current_app
import pdfplumber
import pandas as pd

bp = Blueprint('todo', __name__, url_prefix='/todo')

""" def login_required(view):
   @functools.wraps(view)
   def wrapped_view(**kwargs):
       if g.user is None:
           return redirect(url_for('auth.login'))

       return view(**kwargs)

   return wrapped_view

@bp.before_app_request
def load_logged_in_user():
   user_id = session.get('user_id')

   if user_id is None:
       g.user = None
   else:
       g.user = get_db().execute(
           'SELECT * FROM user WHERE id = ?', (user_id,)
       ).fetchone() """

Allowed_Extensions = ('pdf',)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Allowed_Extensions

def extract_text(file_path):
    tables = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                table = pd.DataFrame(table)
                table = table.fillna(value='')  # Fill NaN values with empty strings
                table.columns = table.iloc[0]
                table.drop(0, inplace=True)
                tables.append(table)
    return tables

@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        tables = []
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            tables = extract_text(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            with pd.ExcelWriter('extracted_tables.xlsx') as writer:
                for i, df in enumerate(tables):
                    df.to_excel(writer, sheet_name=f'Table_{i+1}', index=False)
            flash('File uploaded and processed successfully!')

            tables = [table.to_html() for table in tables]
            
    return render_template('index.html', tables=tables, ntables=len(tables))