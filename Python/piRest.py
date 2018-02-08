#!/home/pi/flask/bin/python
import urllib
from flask import Flask
from flask import request
from flask import Response
import json, os.path, time

#path = "\\Temp\\gpio"
path = "/sys/class/gpio"

app = Flask(__name__)

def toJSONP(callback,json):
    if (not callback):
        callback="callback"
    return ""+callback+"("+json+");"

class Data:
    port=-1
    direction="undefined"
    value=-1
    error=""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def getValue(gpio):
    data=Data();    
    data.port=gpio
    try:
        f = open(os.path.join("",path+"/gpio"+gpio,'value')) 
        data.value=f.readline()
        data.value=data.value[:1]
        f.close();
        data.direction="OUT"
        return data
    except IOError: 
        data.error="GPIO Port not defined!"
        return data

def initPort(gpio):
    data=Data();
    data.direction="OUT"
    data.port=gpio
    data.value=0
    try:        
        f = open(os.path.join("",path,'export'),"w") 
        f.write(gpio);
        f.close()
        time.sleep(1);
        f2 = open(os.path.join("",path+"/gpio"+gpio,'direction'),"w") 
        f2.write("out");
        f2.close()
        return data
    except IOError: 
        data.error="Direction not defined!"
        return data

def clearPort(gpio):
    data=Data()
    data.port=gpio
    data.direction="CLEARED"
    try:
        f = open(os.path.join("",path,'unexport'),"w") 
        f.write(gpio);
        f.close()        
    except IOError: 
        data.error="Direction not defined!"
    return data;   

def setPort(gpio,value):
    data=Data();
    data.direction="OUT"
    data.port=gpio
    try:
        f = open(os.path.join("",path+"/gpio"+gpio,'value'),"w") 
        f.write(value);
        f.close()
        data.value=value
    except IOError: 
        data.error="Port not defined!"
    return data;

@app.route('/gpio/api/v1.0/<string:gpio_nr>', methods=['GET'])
def get_port(gpio_nr):
    data=getValue(gpio_nr); 
    return Response(data.toJSON(), mimetype='application/json')


@app.route('/gpio/api/v1.0/', methods=['POST'])
def create_port():
    if not request.json or not 'port' in request.json:
        data=Data();
        data.error=" Missing attribute port"
    else:        
        data = initPort(request.json['port']);
    return Response(data.toJSON(), mimetype='application/json')

@app.route('/gpio/api/v1.0/jsonp/post/<string:gpio_nr>', methods=['GET'])
def get_portp(gpio_nr):
    data=initPort(gpio_nr); 
    print(data.toJSON())
    return Response(toJSONP(request.args.get('callback'), data.toJSON()), mimetype='application/javascript')


@app.route('/gpio/api/v1.0/<string:gpio_nr>', methods=['DELETE'])
def delete_port(gpio_nr):
    data=clearPort(gpio_nr);
    return Response(data.toJSON(), mimetype='application/json')

@app.route('/gpio/api/v1.0/jsonp/delete/<string:gpio_nr>', methods=['GET'])
def delete_portp(gpio_nr):
    data=clearPort(gpio_nr); 
    print(data.toJSON())
    return Response(toJSONP(request.args.get('callback'), data.toJSON()), mimetype='application/javascript')


    
@app.route('/gpio/api/v1.0/<string:gpio_nr>', methods=['PUT'])
def update_port(gpio_nr):
    if not request.json or not 'value' in request.json:
        data=Data();
        data.error=" Missing attribute value"
    else:        
        data=setPort(gpio_nr,request.json['value']);
    return Response(data.toJSON(), mimetype='application/json')

@app.route('/gpio/api/v1.0/jsonp/put/<string:gpio_nr>', methods=['GET'])
def update_portp(gpio_nr):
    payload = request.query_string[request.query_string.find('&')+1:]
    payload = payload[:payload.find('&')]
    payload = urllib.unquote(payload)
    obj = json.loads(payload)
    print("INFO:"+obj['value'])


    #task = data.get('value')
    #print(value)
    #print("Info:"+request.args.get(1))
    data=setPort(gpio_nr,obj['value']); 
    return Response(toJSONP(request.args.get('callback'), data.toJSON()), mimetype='application/javascript')

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)