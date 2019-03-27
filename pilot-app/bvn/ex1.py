from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(mongo_uri)

ex1 = client.c4e

post = ex1['posts']

new_post = {
    'title':'Đơn xin nghỉ học',
    'author':'Thanh Hai Pham',
    'content':'Em xin anh Quân cho em nghỉ học'
}
post.insert_one(new_post)

