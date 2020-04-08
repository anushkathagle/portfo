from flask import Flask, render_template,url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/index.html')
def hello_world():
    return render_template('index.html')
    
@app.route('/<string:page_name>')
def work_func(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',newline=' ', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['msg']
        database.write(f'\n{email} , {name} , {message}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email = data['email']
        name = data['name']
        message = data['msg']
        csv_writer = csv.writer(database2,delimiter=',',quotechar=':', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email , name , message])

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return'something went wrong'


# @app.route('/about.html')
# def about_func():
#     return render_template('about.html')

# @app.route('/components.html')
# def component_func():
#     return render_template('components.html')
    
# @app.route('/contact.html')
# def contact_func():
#     return render_template('contact.html')
    
    