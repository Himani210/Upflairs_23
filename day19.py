from flask import Flask,render_template
app=Flask(__name__)
@app.route('/') #decorator
#def sample():
 #   return 'kuch bhi sample'


@app.route('/new')
def new():
    return '<h1> THIS IS HEADING</h1>'

def some_function():
    return ''' 
    <html>
    <head><title>HOME </title>
    <body>
    <h3 style="color: red;">Home page</h3>
    <p>Tjis is our new brand</p>
    </body>
    </html>'''

app.run(debug='True')


