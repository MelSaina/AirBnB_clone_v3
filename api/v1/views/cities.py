#!/usr/bin/python3
""" View for City objects that handles default API actions """
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State
from models.city import City

@app_views.route('/states/<state_id>/cities', methods=['GET'],
                     strict_slashes=False)
def cities(state_id):
    """ 
    Retrieves the list of all City objects 
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities])

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def r_city_id(city_id):
    """ Retrieves a City object """
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())
def del_city(city_id):
        """ 
        Deletes a City object 
        """
        city = storage.get("City", city_id)
        if not city:
            abort(404)
        city.delete()
        storage.save()
return make_response(jsonify({}), 200)
