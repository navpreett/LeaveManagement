# app/routes.py
from datetime import datetime  # Add this import
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import LeaveRequest

@app.route('/')
def leave_list():
    leave_requests = LeaveRequest.query.all()
    return render_template('leave_list.html', leave_requests=leave_requests)

@app.route('/request_leave', methods=['GET', 'POST'])
def request_leave():
    if request.method == 'POST':
        reason = request.form.get('reason')
        date_str = request.form.get('date')

        # Convert the string date to a Python date object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

        new_leave_request = LeaveRequest(reason=reason, date=date_obj)
        db.session.add(new_leave_request)
        db.session.commit()

        return redirect(url_for('leave_list'))

    return render_template('leave_form.html')
