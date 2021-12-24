# 1) 주문하기(POST): 정보 입력 후 '주문하기' 버튼클릭 시 주문목록에 추가
# 2) 주문내역보기(GET): 페이지 로딩 후 하단 주문 목록이 자동으로 보이기
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.likelion                      # 'likelion'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('hw.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']
    # print(name_receive)
    order = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'number': number_receive
    }
    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/orders', methods=['GET'])
def read_reviews():
    orders = list(db.orders.find({}, {'_id':0}))
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'
    ,'orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)