from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

# username = us.user_name()

# Find data in json
@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        user = request.form.get('username')
    

        _user = us.find_username(user)
        if _user:
            us.user_name_delete(user)
            return jsonify({'message': 'Delete successfully.'}), 200
        else:
            return jsonify({'message': 'Delete unsuccessfully.'}), 401
    except: 
        return jsonify({'message': 'User not found.'}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1