from views import db 
from models import Task 
from datetime import date 

#create the database and table
db.create_all()

#insert data 
#db.session.add(Task('Finish this Tuut', date(2016, 5, 17), 10, 1))
#db.session.add(Task('Finish Real Python Tuut', date(2016, 5, 21), 10, 1))

# commit changes to db 
db.session.commit()