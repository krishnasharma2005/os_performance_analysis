from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU: {cpu}, Mem: {memory}, Disk: {disk}")  # <-- Add this

    return jsonify({
        'cpu': cpu,
        'memory': memory,
        'disk': disk
    })

if __name__ == "__main__":
    app.run(debug=True)
