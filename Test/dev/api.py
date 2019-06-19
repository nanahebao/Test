from flask import Flask, request
from flask_pymongo import PyMongo
from config import MongoDB
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mongo = PyMongo(app)


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     # users = mongo.db.api.insert({"ss":3})
#     #return render_template('index.html',onlines_users=onlines_users)
#     # if users:
#         # return "aa"
#     # else:
#         # return  "add"
#     return render_template('index.html')

@app.route('/apilist', methods=['GET'])
def apilist():
    apilist = mongo.db.api.find()
    api = []
    for i in apilist:
        i.pop('_id')
        api.append(i)

    # return dict(result='success',li=api )
    return json.dumps(api)


@app.route('/api/saveapi', methods=['POST'])
def saveapi():
    requestData = request.get_data()
    if requestData == None:
        return json.dumps({"code": 400, "msg": "requestData  for None"})
        print
        "\trequest data:", type(requestData), "\tdata:" + requestData
    else:
        try:
            print
            "\trequest data:", type(requestData), "\tdata:" + requestData
            dataOb = eval(requestData)
            print
            "\tto dict data:", type(dataOb), "\t", dataOb

            return ""
        except Exception as ex:
            print
            "\nconvert object fail"
            return json.dumps({"code": 500, "msg": "service fail"})






            # isin=data.find('url')


            # dataob=json.loads(datajson)


            # dataob=dict(data)

            # dict={'url':url,'method':method,'head':head,'body':body}
            # users = mongo.db.api.insert(dict)
            # dict={'url':url}

            # if isin==-1:
            #     print isin
            #     print "no saveapicon"
            #     return "no saveapi"
            # else:
            #     #mongo.db.api.insert(datajson)
            #     print "saveapi"
            #     return "saveapi to data success"



            # return render_template('index.html')


if __name__ == '__main__':
    app.run()
    app.debug = true
