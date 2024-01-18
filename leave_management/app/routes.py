# app/routes.py
from datetime import datetime
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import LeaveRequest
from app.forms import LoginForm 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()  
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register_form.html')


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
    
#     elif request.method == 'POST':
#         loginForm = request.form
#         username = loginForm['username']
#         cur = mysql.connection.cursor()
#         queryStatement = f"SELECT * FROM user WHERE username = '{username}'"
#         numRow = cur.execute(queryStatement)

#         if numRow > 0:
#             user = cur.fetchone()

#             if check_password_hash(user['password'], loginForm['password']):
#                 # Record session information
#                 session['login'] = True
#                 session['username'] = user['username']
#                 session['firstName'] = user['first_name']
#                 session['lastName'] = user['last_name']

#                 if user['role_id'] == 1:
#                     return redirect('/admin')
                
#                 print(session['username'])
#                 flash('Welcome ' + session['firstName'], 'success')
#                 # flash("Log In successful",'success')
#                 return redirect('/')
            
#             else:
#                 cur.close()
#                 flash("Password is incorrect", 'danger')

#         else:
#             cur.close()
#             flash('User not found', 'danger')
#             return render_template('login.html')
        
#         cur.close()
#         return render_template('login.html')
    
#     return render_template('login.html')


# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     if request.method == 'GET':
#         return render_template('register_form.html')
    
#     elif request.method == 'POST':
#         userDetails = request.form
#         queryStatement = f"SELECT * FROM user"
#         cur = mysql.connection.cursor()
#         numRow = cur.execute(queryStatement)

#         if numRow > 0:
#             user = cur.fetchone()

#             if userDetails['username'] in user['username']:
#                 flash('This username isn\'t available. Please try another.', 'danger')
#                 return render_template('register.html')
#         # Check the password and confirm password
#         if userDetails['password'] != userDetails['confirm_password']:
#             flash('Passwords do not match!', 'danger')
#             return render_template('register.html')

#         p1 = userDetails['first_name']
#         p2 = userDetails['last_name']
#         p3 = userDetails['username']
#         p4 = userDetails['email']
#         p5 = userDetails['password']
#         p6 = userDetails['phone_number']

#         hashed_pw = generate_password_hash(p5)
#         print(p1 + "," + p2 + "," + p3 + "," + p4 + "," + p5 + "," + p6 + "," + hashed_pw)

#         queryStatement = (
#             f"INSERT INTO "
#             f"user(first_name, last_name, username, email, phone_number, password, role_id) "
#             f"VALUES('{p1}', '{p2}', '{p3}', '{p4}', '{p6}', '{hashed_pw}', {2})"
#         )
#         print(check_password_hash(hashed_pw, p5))
#         print(queryStatement)
#         cur = mysql.connection.cursor()
#         cur.execute(queryStatement)
#         mysql.connection.commit()
#         cur.close()

#         flash("Form Submitted Successfully.", "success")
#         return redirect('/')
    
#     return render_template('register.html')


@app.route('/leave_list')
def leave_list():
    leave_requests = LeaveRequest.query.all()
    return render_template('leave_list.html', leave_requests=leave_requests)

@app.route('/request_leave', methods=['GET', 'POST'])
def request_leave():
    if request.method == 'POST':
        reason = request.form.get('reason')
        date_str = request.form.get('date')

        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

        new_leave_request = LeaveRequest(reason=reason, date=date_obj)
        db.session.add(new_leave_request)
        db.session.commit()

        return redirect(url_for('leave_list'))

    return render_template('leave_form.html')
