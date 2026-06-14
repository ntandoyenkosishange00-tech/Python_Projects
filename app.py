from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#route for the about page 
@app.route('/about')
def about():    
    return render_template('about.html')

@app.route('/contact')
def contact():
    if request.method == 'POST':
        # Handle form submission here
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can add code to process the form data, such as sending an email or saving it to a database
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')     

if __name__ == '__main__':
    app.run(debug=False)
    


