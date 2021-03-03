from flask import jsonify, abort
from database.operations import search_db_data, get_db_data

def __generate_json(results):
    """
    Generates json from sqlalchemy results object and returns jsonify object
    """
    data = []
    """ Dictionary to hold data for json genetation """
    line = 0
    """ Current line for loop """

    for row in results:
        r = [row.id, row.name ,row.address, row.postcode,  row.city,  row.license_granting_date,  row.license_type, row.business_id]
        data.insert(line, r)
        line +=1

    response = jsonify({'data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_json(all=True, search_keyword=None):
    """ 
    Either returns all rows found in database as jsonify object or seaches for a specific rows.

    if all=True > Return all rows
    if all=False & search_keyword!=None > return rows matching search_keyword
    """
    if all==True:
        results = get_db_data()
        return __generate_json(results)
    elif all==False and search_keyword!=None:
        results = search_db_data(search_keyword)
        return __generate_json(results)
    else:
        abort(404)