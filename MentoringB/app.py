from flask import Flask, jsonify, request
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello BOAZ!</h1>"

@app.route("/<name>")
def hello(name):
    now = dt.datetime.now()
    return jsonify(
        date=now,
        text=f'Hi, {name}!',
    )


'''
gogo~
'''

members = [
    {"id": 1, "unit": 18, "part": "engineering", "name": "nayeon"},
    {"id": 2, "unit": 18, "part": "analysis", "name": "kyuyeon"},
    {"id": 3, "unit": 19, "part": "analysis", "name": "bogyeom"},
    {"id": 4, "unit": 19, "part": "engineering", "name": "jiwon"},
    {"id": 5, "unit": 19, "part": "engineering", "name": "wooseok"},
    {"id": 6, "unit": 19, "part": "analysis", "name": "hyogeun"},
    {"id": 7, "unit": 19, "part": "analysis", "name": "ara"},
    {"id": 8, "unit": 19, "part": "engineering", "name": "jaejun"},
    {"id": 9, "unit": 19, "part": "engineering", "name": "sungyoon"},
]

# GET /members
@app.route("/members")
def get_members():
    return jsonify(members)


# POST /members
@app.route("/members", methods=['POST'])
def add_member():
    request_data = request.get_json()  # {"unit": ..., "part": ..., "name": ...}
    new = {
        "id": members[-1]['id'] + 1,
        "unit": request_data['unit'],
        "part": request_data['part'],
        "name": request_data['name'],
    }
    members.append(new)
    return jsonify(members)

# PUT /members/<int:id>
@app.route("/members/<int:id>", methods=['PUT'])
def edit_member(id):
    request_data = request.get_json()
    new = {
        "id": int(id),
        "unit": request_data['unit'],
        "part": request_data['part'],
        "name": request_data['name'],
    }
    for i in range(len(members)):
        if members[i]['id'] == int(id):
            members[i] = new
    return jsonify(new)

# DELETE /members/<int:id>
@app.route("/members/<int:id>", methods=['DELETE'])
def delete_member(id):
    for i in range(len(members)):
        if members[i]['id'] == int(id):
            members.remove(members[i])
    return jsonify(members)


if __name__ == "__main__":
    # host default: localhost(127.0.0.1)
    # port default: 5000
    app.run(host="0.0.0.0", port="5000", debug=True)