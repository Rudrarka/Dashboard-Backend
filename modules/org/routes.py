from flask import Blueprint, request, jsonify, make_response
from modules.db import Database
from modules import app
from functools import wraps
from flask import Response

module = Blueprint('org', __name__)

@module.route('/super-app', methods=['GET'])
def super_app():
    db_instance = Database()
    db = db_instance.mongodb_conn()
    stats_collection = db['appStatistics']
    super_app_stats = stats_collection.find({'app': {'$ne' : 'organization'}}).sort([('totalVisits',-1)]).limit(1)
    print(super_app_stats)
    response_list = []
    for stats in super_app_stats:
        response_list = [
            stats['app'],
            stats['price'],
            {   
                'id':str(stats['_id']),
                'heading':'Total Visits',
                'value' : stats['totalVisits']
            },
            {
                'id':str(stats['_id']),
                'heading':'New Visits',
                'value' : stats['newVisits']
            },
            {
                'id':str(stats['_id']),
                'heading':'Sales',
                'value' : stats['purchases']
            },
            {
                'id':str(stats['_id']),
                'heading':'Active Users',
                'value' : stats['activeUsers']
            }
        ]
        
    response = {
        'data': response_list
        }
    print(response)    
    return jsonify(response)

@module.route('/stats', methods=['GET'])
def stats():
    db_instance = Database()
    db = db_instance.mongodb_conn()
    stats_collection = db['appStatistics']
    app_stats = stats_collection.find_one({'app':'organization'})
    if app_stats:
        response = {
            'data' : [
                {
                    'header' : 'New Visits',
                    'percent' : app_stats['nvPercent'],
                    'value' : app_stats['newVisits']
                },
                {
                    'header' : 'Purchases',
                    'percent' : app_stats['pPercent'],
                    'value' : app_stats['purchases']
                },
                {
                    'header' : 'Active Users',
                    'percent' : app_stats['auPercent'],
                    'value' : app_stats['activeUsers']
                },
                {
                    'header' : 'Returned',
                    'percent' : app_stats['ruPercent'],
                    'value' : app_stats['returnedUsers']
                }
            ]
        }
    
    return jsonify(response)