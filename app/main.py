from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Employee model definition
class Employee(db.Model):
    __tablename__ = 'Employee'
    
    EmployeeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    Age = db.Column(db.Integer, nullable=False)

# Create the database and table (if not exists)
with app.app_context():
    db.create_all()

    # Check if the table is empty, then insert hardcoded data
    if Employee.query.count() == 0:
        # Hardcoded insertion of two employees
        employee1 = Employee(FirstName='Gyan', LastName='Shukla', Age=21)
        employee2 = Employee(FirstName='Harry', LastName='Potter', Age=25)

        # Add employees to the session and commit to save
        db.session.add_all([employee1, employee2])
        db.session.commit()

# Route to fetch all employees
@app.route('/')
def index():
    try:
        employees = Employee.query.all()
        result = [
            {
                "EmployeeID": emp.EmployeeID,
                "FirstName": emp.FirstName,
                "LastName": emp.LastName,
                "Age": emp.Age
            } for emp in employees
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
