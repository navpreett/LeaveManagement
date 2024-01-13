# app/routes.py
from flask import Flask
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import LeaveRequest
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# Initialize the SQLAlchemy instance without passing the app instance
db = SQLAlchemy()

# Initialize the app with the SQLAlchemy instance
db.init_app(app)


@app.route('/')
def leave_list():
    #return 'Xarlos is amazing.'
    leave_requests = LeaveRequest.query.all()
    return render_template('leave_list.html', leave_requests=leave_requests)

@app.route('/request_leave', methods=['GET', 'POST'])
def request_leave():
    if request.method == 'POST':
        reason = request.form.get('reason')
        date = request.form.get('date')

        new_leave_request = LeaveRequest(reason=reason, date=date)
        db.session.add(new_leave_request)
        db.session.commit()

        return redirect(url_for('leave_list'))

    return render_template('leave_form.html')