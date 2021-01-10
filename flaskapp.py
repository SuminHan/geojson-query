from flask import Flask, request, render_template
import os
import myconstants
app = Flask(__name__)

host = myconstants.host
appkey = myconstants.appkey
lat, lng = 37.558309, 126.925776

@app.route('/')
def home():
    return render_template('createpolygon.html', appkey=appkey, lat=lat, lng=lng)
    
if __name__ == '__main__':
    app.run(host=host, port=5000, debug=True)