from flask import Flask, render_template,request,redirect
from auth import login,register
from dotenv import load_dotenv
import os
app = Flask(__name__)
#load_dotenv()
#dashboard = os.getenv('DASHBOARD_URI')


@app.route('/', methods=['GET', 'POST'])  # Ensure the route handles both GET and POST
def home():
    message = None  # Default to no message
    color = None  # Default to no color
    if request.method == 'POST':
        if 'login-submit' in request.form:  # Login form submission
            # Retrieve username and password from the form
            username = request.form['username']
            password = request.form['password']
            message,color,role = login(username,password)
            return redirect("https://cloud-chat-cnewvelucijbasrhvjuazv.streamlit.app/")
            #if role == "admin" :
                #return redirect(dashboard)
        elif 'register-submit' in request.form:  # Registration form submission
            # Retrieve registration details
            reg_username = request.form['reg-username']
            reg_password = request.form['reg-password']
            reg_email = request.form['reg-email']
            message,color = register(reg_username,reg_email,reg_password)
    return render_template('index.html', message=message, color=color)

if __name__ == "__main__":
    app.run(debug=True)  # Runs on http://127.0.0.1:5000/
