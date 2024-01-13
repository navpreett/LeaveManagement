# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import LeaveRequest

@app.route('/')
def leave_list():
    # return 'Xarlos is amazing.'
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
