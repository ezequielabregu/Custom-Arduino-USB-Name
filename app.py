from flask import Flask, render_template, request, send_file
import random
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'data')
template_path = os.path.join(TEMPLATE_DIR, "yourBoard_template.txt")


@app.route("/", methods=["GET", "POST"])
def index():
    pid = f"0x{random.randint(0x1000, 0xFFFF):04X}"
    generated_content = ""  # Initialize as empty

    if request.method == "POST":
        device_name = request.form["device_name"]
        manufacturer = request.form["manufacturer"]
        pid = request.form["pid"]

        # Read template and replace placeholders
        with open(template_path, "r") as template:
            content = template.read()
        generated_content = content.format(device_name=device_name, manufacturer=manufacturer, pid=pid)

        # Write to yourBoard.txt
        with open("yourBoard.txt", "w") as file:
            file.write(generated_content)

        return render_template("index.html", pid=pid, generated_content=generated_content)

    # Render the page with an empty text box for GET requests
    return render_template("index.html", pid=pid, generated_content=generated_content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
#    app.run(debug=True)