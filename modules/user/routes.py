from flask import Blueprint, request, jsonify, make_response
from modules.db import Database
from modules import app
from flask import Response

module = Blueprint('user', __name__)

@module.route('/feeds', methods=['GET'])
def feeds():
    db_instance = Database()
    db = db_instance.mongodb_conn()
    feeds_collection = db['feeds']
    user_collection = db['users']
    feeds = feeds_collection.find().sort("_id",-1).limit(10)
    response = {}
    feed_list = []
    for feed in feeds:
        print(feed['userId'])
        user = user_collection.find_one({'userId':feed['userId']},{'_id':0, 'displayName':1, 'profileImageUrl': 1})
        if user:
            response_item = {
                'id': str(feed['_id']),
                'displayName' : user['displayName'], 
                'avatar' : user['profileImageUrl'],
                'feed' : feed['feed']
            }
            feed_list.append(response_item)
    response = {
        'data': feed_list
        }
    print(response)    
    return jsonify(response)

@module.route('/country-data', methods=['GET'])
def country_data():
    db_instance = Database()
    db = db_instance.mongodb_conn()
    user_collection = db['users']
    count_object = user_collection.aggregate(
            [{'$group' : { '_id' : '$region', 'count' : {'$sum' : 1}}}]
        )
    response = {}
    count_list = []
    count_list.append(['Country', 'Popularity'])
    for count in count_object:
        item = [count['_id'],count['count']]
        count_list.append(item)
    response = {
        'data':count_list
    }

    return jsonify(response)
    

