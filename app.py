from flask import Flask
import logging

logging.basicConfig(filename='flask-access.log', level=logging.DEBUG)

app = Flask(__name__)

counter = 1
post_requests_file = 'post_requests.txt'

@app.route('/count/', methods=['GET'])
def getcount():
    with open(post_requests_file, 'r') as file : 
        data = file.read()
    return "Post requests: " + data

@app.route('/count/', methods=['POST'])
def addcount():    
    with open(post_requests_file, 'r') as file : 
        data = file.read() 

    count = str(int(data) + 1)    
    
    with open(post_requests_file, 'w') as file:
        file.write(count)
    return "Post requests: " + count

@app.route("/")
def hello():    
    return "Hello World!!!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
