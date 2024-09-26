from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, welcome to my first web app!"

# Run the app on the local development server
if __name__ == '__main__':
    app.run(debug=True)





# Django is a high level web framework which is used in python for complex applications where as flask is used for simple 
# applications.
# Django is a backend program. 

# difference between js and java frontend and backend. 

# ORM (Object Relational Mapping) Django functions CRUD (Create, Read, Update, Delete)

