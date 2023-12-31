import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

from schemas import StoreSchema

blp = Blueprint("Stores", __name__, description="Operations on Stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort (404, message="Store not found.")            
    
    
    def delete(self, store_id):
        try: 
            del stores[store_id]
            return { "message": "Store deleted."}
        except KeyError:
            abort (404, message="Store not found.")
            

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        try:
            return stores.values()
            #return {"stores": list(stores.values())} . Not used due to marshmallow validation approach
        except KeyError:
            abort(404, message="Stores not found.")
            

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)        
    def post(self, store_data):
        ############### 
        ## The commented lines below are no longer needed due to use of marshmallow for validation                
        #store_data = request.get_json()
        #if "name" not in store_data:
        #    abort(
        #        400,
        #        message=" Bad request. Ensure 'name' is included in the JSON payload."
        #    )
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists.")
                
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        
        return store, 201 # HTTP Status Code: 201 Created - It indicates that the 
                        #request has succeeded and has led to the creation of a resource        if 