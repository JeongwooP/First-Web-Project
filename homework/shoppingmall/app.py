from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    print(name_receive)

    doc = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.shopping.insert_one(doc)

    return jsonify({'result':'success', 'msg': '주문이 들어갔습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    lists = list(db.shopping.find({}, {'_id': False}))
    return jsonify({'result':'success', 'all_lists': lists})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)