from taskmanager import db


class Category(db.Model):
    #schema for category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    #links foreign key, backref references this to establish connection
    tasks = db.relationship("Task", backref = "category", cascade = "all, delete", lazy=True)

    def __repr__(self):
        #__repr__ to represent class objects in the form of a string
        # self is python equivalent of this in js
        return self.category_name 



class Task(db.Model):
    #schema for task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    #cascade below means if a category is deleted anything using it as a foreign key is also deleted
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete = "CASCADE"), nullable=False)

    def __repr__(self):
        #__repr__ to represent class objects in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )