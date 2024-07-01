from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
api_key = '96690eec3258fb'

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr


    # Using ipinfo.io to get location
    location = requests.get(f"https://ipinfo.io/{client_ip}?token=96690eec3258fb").json()
    city = location.get('city', 'Unknown')

    temperature = "11 degrees Celsius"

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} in {city}"

    return jsonify({
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    })

if __name__ == "__main__":
    app.run(debug=True)