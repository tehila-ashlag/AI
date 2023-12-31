from flask import Flask, jsonify,request
from book_store import load_books, get_json_catalog, search_books, get_json_cart, add_to_cart, checkout, refer_friend

app = Flask(__name__)

@app.route('/books')
def get_catalog():
    return get_json_catalog()


@app.route('/search')
def search():
    # Get the value of the 'q' query parameter
    keyword = request.args.get('q')
    return search_books(keyword)


@app.route('/cart',methods=['GET'])
def get_user_cart():
    return get_json_cart()



@app.route('/cart', methods=['POST'])
def add_book_to_cart():
    request_body=request.json
    book_id=request_body['bookId']
    report={
        'status':'',
        'message':''
    }
    if not add_to_cart(book_id):
        report['staus']='failed'
        report['message']="Failed to add book to cart - bookId is not valid!"
        status_code=400
    else:
        report['status']='success'
        report['message']="Book added to cart!"
        status_code=200
    return jsonify(report), status_code

@app.route('/checkout', methods=['POST'])
def pay_bill():
    checkout_done=checkout()
    if checkout_done:
        report="checkout succeeded!"
    else:
        report="checkout failed!"
    return report

@app.route('/bringFriend', methods=['POST'])
def bring_friend():
    mail=request.json['mail']
    stars=request.json['stars']
    return refer_friend(mail,stars)  

if __name__ == '__main__':
    load_books()
    app.run(host="0.0.0.0")