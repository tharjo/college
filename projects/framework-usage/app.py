from flask import Flask, render_template, request, jsonify
import qrcode, json, os, base64
from io import BytesIO
from datetime import datetime
import platform
import socket

app = Flask(__name__)
DATA_FILE = 'data/attendance.json'
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"attendances": [], "device_info": []}
    return {"attendances": [], "device_info": []}

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_base64, qr_code_link = None, None
    if request.method == 'POST':
        student_name = request.form['student_name']
        local_ip = get_local_ip()
        qr_code_data = f"http://192.168.137.1:5000/attendance?student={student_name.replace(' ', '%20')}"
        qr = qrcode.make(qr_code_data)
        buffered = BytesIO()
        qr.save(buffered, format="PNG")
        qr_code_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        qr_code_link = qr_code_data

        data = load_data()
        data['attendances'].append({"student_name": student_name, "qr_code": qr_code_base64})
        save_data(data)
        return render_template('index.html', qr_code_base64=qr_code_base64, qr_code_link=qr_code_link, device_info=data['device_info'])
    return render_template('index.html', device_info=load_data()['device_info'])

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/attendance')
def attendance():
    student_name = request.args.get('student')
    user_agent = request.headers.get('User-Agent')
    system_info = platform.system() + " " + platform.release()
    access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_data()
    data['device_info'].append({
        "student_name": student_name,
        "access_time": access_time,
        "user_agent": user_agent,
        "system_info": system_info
    })
    save_data(data)
    return jsonify({"message": f"Presença registrada para {student_name}!", "student_name": student_name})

@app.route('/get_attendance_data')
def get_attendance_data():
    return jsonify(load_data()['device_info'])

@app.route('/get_entry_count')
def get_entry_count():
    data = load_data()
    return jsonify({"count": len(data['device_info'])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)