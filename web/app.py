from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def terminal():
    return render_template("terminal.html")

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    cmd = data.get("cmd")

    # ❗ CỰC KỲ NGUY HIỂM – chỉ dùng học tập
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout + result.stderr

if __name__ == "__main__":
    app.run(debug=True)
