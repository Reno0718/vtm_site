from flask import Flask
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Verticle Tank Maintainance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='Verticle Tank Maintainance')

@app.route('/estimate', methods = ['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['Radius'])
        height = float(form['Height'])
        print(radius)
        print(height)
        
        pi = 3.14
        tank_top = pi * radius**2
        area_side = 2 * (pi * (radius * height))
        total_area = tank_top + area_side
        square_feet = total_area/144
        material = square_feet * 25
        labor = square_feet * 15
        quote = labor + material


        return render_template('estimate.html', pageTitle='Verticle Tank Maintainance', estimate = quote)
    return render_template('estimate.html', pageTitle='Verticle Tank Maintainance')




if __name__ == '__main__':
    app.run(debug=True)


