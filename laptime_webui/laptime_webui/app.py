from flask import Flask, render_template, request
from flask_socketio import SocketIO
from datetime import datetime
import json
import os

app = Flask(__name__)
socketio = SocketIO(app)
DATA_FILE = "lap_times.json"

# ラップタイム履歴 [{time: 12.345, timestamp: "...", name: ""}]
lap_times = []

# 起動時に履歴を読み込む
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        lap_times = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', lap_times=lap_times)

@app.route('/lap_time', methods=['POST'])
def lap_time():
    data = request.get_json()
    lap_time = data.get('lap_time')
    if lap_time is not None:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'time': round(lap_time, 3),
            'timestamp': now,
            'name': ""
        }
        lap_times.append(entry)
        lap_times.sort(key=lambda x: x['time'])  # タイムが速い順に並べ替え

        save_lap_times()

        socketio.emit('new_lap', {'lap_times': lap_times})
    return '', 200

@app.route('/update_name', methods=['POST'])
def update_name():
    data = request.get_json()
    index = data.get('index')
    name = data.get('name')

    if index is not None and 0 <= index < len(lap_times):
        lap_times[index]['name'] = name
        save_lap_times()
        socketio.emit('new_lap', {'lap_times': lap_times})
        return '', 200
    return 'Invalid index', 400

@app.route('/start_timer', methods=['POST'])
def start_timer():
    socketio.emit('start_timer')  # 全クライアントに通知
    return '', 200

@app.route('/delete', methods=['POST'])
def delete_entry():
    data = request.get_json()
    index = data.get('index')
    if index is not None and 0 <= index < len(lap_times):
        lap_times.pop(index)
        save_lap_times()
        socketio.emit('new_lap', {'lap_times': lap_times})
        return '', 200
    return 'Invalid index', 400

def save_lap_times():
    with open(DATA_FILE, "w") as f:
        json.dump(lap_times, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
