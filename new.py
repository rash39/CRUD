from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:newpassword@localhost/baby-tracker'
db = SQLAlchemy(app)

# create app context
app_ctx = app.app_context()
app_ctx.push()

# Create the database tables
db.create_all()

# Release the application context when done
app_ctx.pop()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80),nullable=False)
    create_at = db.Column(db.DateTime,nullable=False,default=db.func.current_timestamp())

    def __repr__(self):
        return f'Event {self.description}'
    
    def __init__(self,description):
        self.description = description


def format_event(event):
    return {
        "description" : event.description,
        "id" : event.id,
        "create_at" : event.create_at
    }   

@app.route('/')
def hello():
    return "Hey!"

# create event
@app.route('/event',methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

# get all events
@app.route('/event',methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events':event_list}

# get single event
@app.route('/event/<id>',methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {'event':formatted_event}

# delete an event
@app.route('/event/<id>',methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event {id} deleted'

# update an event
@app.route('/event/<id>',methods=['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description,create_at = db.func.current_timestamp()))
    db.session.commit()
    return {'event':format_event(event.one())}

# Run flask app
if __name__ == '__main__':
    app.run(debug=True)

