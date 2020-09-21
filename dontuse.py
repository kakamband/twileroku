from flask import Flask, jsonify, request
import pandas as pd
import csv
from twilio.rest import Client

app = Flask(__name__)

account_sid = 'AC315b7a8ffd4d15940a9a43a0753e740f'
auth_token = 'e23380ccbf49eae6ec7e0504e49ce3ca'
client = Client(account_sid, auth_token)


@app.route('/api/echo-json', methods=['GET', 'POST', 'DELETE', 'PUT'])
def add():
    data = request.get_json()
    #data2 = data.to_csv('csvtemp.csv')
    with open('testercsv.csv', 'w') as f:
        for key in data.keys():
            f.write('%s,%s\n'%(key,data[key]))
    phone_number = client.lookups \
                         .phone_numbers(data.get('number')) \
                         .fetch(type=['caller-name'])

    print(data.keys())
    print(data.values())
    print(data.get('number'))
    print(phone_number.caller_name)
    return jsonify(data)
    return phone_number.caller_name






'''
phone_number = client.lookups \
                     .phone_numbers('+16182501164') \
                     .fetch(type=['caller-name'])

print(phone_number.caller_name)
'''







if __name__ == '__main__':
    app.run(host= '127.0.0.1',debug=True)
