from flask import Flask, request
from os.path import exists
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
	string = request.environ['QUERY_STRING']
	hname = str(hash(string))
	if not(exists(hname)):
		with open(hname, 'w') as wf:
			wf.write('0')
	with open(hname) as rf:
		num = rf.read().strip()
		return 'document.getElementById("{}").innerText = {}'.format(string, num)
	return 'error'

@app.route('/add', methods=['GET'])
def add():
	string = request.environ['QUERY_STRING']
	hname = str(hash(string))
	if not(exists(hname)):
		with open(hname, 'w') as wf:
			wf.write('0')
	with open(hname) as rf:
		num = int(rf.read().strip())
		with open(hname, 'w') as wf:
			wf.write(str(num + 1))
			return 'console.log("successful")'
	return 'error'

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)