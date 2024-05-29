from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/home')
def home():
    # Redirect to login or signup based on user action on the home page
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume login form processing here
        user_role = request.form.get('role')  # Assuming a role field in your form
        session['user_role'] = user_role
        if user_role == 'patient':
            return redirect(url_for('patient_index'))
        elif user_role == 'doctor':
            return redirect(url_for('doctor_index'))
        elif user_role == 'admin':
            return redirect(url_for('admin_index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process signup form
        return redirect(url_for('profile'))
    return render_template('signup.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Process profile form
        return redirect(url_for('login'))
    return render_template('profile.html')

@app.route('/patient/index')
def patient_index():
    return render_template('patient/index.html')

@app.route('/doctor/index')
def doctor_index():
    return render_template('doctor/index.html')

@app.route('/admin/index')
def admin_index():
    return render_template('admin/index.html')

@app.route('/patient/appointment')
def appointment():
    return render_template('patient/appointment.html')

@app.route('/patient/booking')
def patient_booking():
    return render_template('patient/booking.html')

@app.route('/patient/schedule')
def patient_schedule():
    return render_template('patient/schedule.html')

@app.route('/patient/doctors')
def patient_doctors():
    return render_template('patient/doctors.html')

@app.route('/patient/settings')
def patient_settings():
    return render_template('patient/settings.html')

@app.route('/google-login')
def google_login():
    # Here you can add logic to handle Google login
    # For now, let's assume it redirects to a JavaScript file or triggers it
    return redirect(url_for('static', filename='js/main.js'))

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for('splash'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)