from flask import Flask, request, jsonify
from collections import deque
import Person
import json
import datetime
import threading
app = Flask(__name__)

reserveBathroom = deque([])
bathroomOccupied = False
now = datetime.datetime.now()
thirty_minutes_seconds = 30 * 60 * 60

@app.route('/')
def hello():
    return 'Hello, welcome to Bathroom Server'

## Constraints only 1 person can have 1 reservation at a time
@app.route('/reserve', methods = ['POST'])
def reserve_bathroom():
    error = None
    if request.method == 'POST':
        data = list(request.values.to_dict().keys())[0]
        print(data)
        #data = json.loads(data)
        #user = data.user_id
        ## first check, whether this user has a reservation
        #userReservation = checkUserReseravation(user)
        print
        if userReservation:
            data = {'text': 'You\'ve already made a reservation'}
            return jsonify(data)
        else:
            #reserveBathroom.append(Person(user))
            #respond back with their reservation time

@app.route('/available', methods = ['POST'])
def bathroom_availability():
    if request.method == 'POST':
        data = request.data
        bathroomOccupied = data.occupancy


# Check whether this user has made a reservation
@staticmethod
def checkUserReservation(user):
    for user_id in reserveBathroom:
        if user == user_id:
            return true
    return false


# check the users whose reservation have gone over limit
@staticmethod
def remove_reservation_waisters():
    threading.Timer(10.0, remove_reservation_waisters).start()
    for person in reserve_bathroom:
        if person.date is not None and now.timestamp() - person.date.timestamp() >= thirty_minutes_seconds:
            removed_user = reserve_bathroom.popLeft()
            # TO-DO: alert the removed user, their reservation has gone over limit

if __name__ == '__main__':
    app.run(debug=True, port=33507)
