from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    if not data:
        return jsonify({'status': 'fail', 'message': 'No data received'}), 400
    
    temperature = data.get('temperature')
    humidity = data.get('humidity')

    if temperature is None or humidity is None:
        return jsonify({'status': 'fail', 'message': 'Invalid data received'}), 400

    # Process the data here (e.g., save to a database)
    print(f"Received data - Temperature: {temperature} *C, Humidity: {humidity} %")

    return jsonify({'status': 'success', 'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
