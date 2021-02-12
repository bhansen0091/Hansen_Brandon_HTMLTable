from flask import Flask, render_template
app = Flask(__name__)

users = [
    {'first_name': 'Michael', 'last_name': 'Choi'},
    {'first_name': 'John', 'last_name': 'Supsupin'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'},
]

def add_full_name(list_of_dicts):
    for dictionary in list_of_dicts:
        temp_first = dictionary["first_name"]
        temp_last = dictionary["last_name"]
        dictionary["full_name"] = f"{temp_first} {temp_last}"
    return list_of_dicts

users = add_full_name(users)
t_headers = ["First Name", "Last Name", "Full Name"]

@app.route("/")
def index():
    return render_template("index.html", t_headers = t_headers, data = users )

if __name__=="__main__":
    app.run(debug=True)
