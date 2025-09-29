from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):

    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    response.set_cookie('mouse', 'Cookie')

    return response

@app.route('/clear')
def clear_session():
    session.clear()
    return jsonify({'message': 'Session cleared'})

@app.route('/sessions/<key>/<value>')
def set_session(key, value):
    session[key] = value
    return jsonify({'message': f'Set {key} to {value}'})

@app.route('/secure-cookie')
def secure_cookie():
    response = make_response(jsonify({'message': 'Secure cookie set'}))
    response.set_cookie('secure_cookie', 'secure_value', secure=True, httponly=True)
    return response

if __name__ == '__main__':
    app.run(port=5555)
    