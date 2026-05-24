from flask import Flask, render_template
import os

app = Flask(__name__)

# Create count.txt if it doesn't exist
if not os.path.exists("count.txt"):
    with open("count.txt", "w") as f:
        f.write("0")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):

    # Read count
    with open("count.txt", "r") as f:
        count = int(f.read())

    # Increment count
    count += 1

    # Save updated count
    with open("count.txt", "w") as f:
        f.write(str(count))

    return render_template('hello.html', name=name, count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)