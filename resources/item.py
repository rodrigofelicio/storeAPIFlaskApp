import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items

from schemas import ItemSchema, ItemUpdateSchema



blp = Blueprint("ItemsStores", __name__, description="Operations on Items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")
            
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")
            
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemUpdateSchema)        
    def put(self, item_data, item_id):  # the 2nd parameter must always be the JSON used by
                                        # marshmallow for validation (in this case, item_data)
        ############### 
        ## The commented lines below are no longer needed due to use of marshmallow for validation        
        #item_data = request.get_json()
        #if "price" not in item_data or "name" not in item_data:
        #    abort(400, message="Bad request. Ensure 'price', and 'name'are included in the JSON payloar.")
        
        try:
            item = items[item_id]
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values() # this will return a list of items. Marshmallow approach
        #return {"items": list(items.values())} this is not needed when marshmallow is used for validation
    

    @blp.arguments(ItemSchema)
    def post(self, item_data):  # This 2nd parameter (item_data) is going to contain JSON,
                                # which is the validated fields that the schema requested.
                                # The JSON that the client sends is passed through the ItemSchema,                            
                                # it checks that the fields are there and they're the valid types
                                # and so forth, and it gives the method, an argument, which is
                                # that validated dictionary.
        ############### 
        ## The commented lines below are no longer needed due to use of marshmallow for validation
        # Here not only we need to validate data exists,
        # But also what type of data. Price should be a float,
        # for example.
        #item_data = request.get_json()
        #if(
        #    "price" not in item_data 
        #    or "store_id" not in item_data
        #    or "name" not in item_data        
        #):
        #    abort(
        #        400,
        #        message="Bad request. Ensure 'price', 'store_id', and 'name' are in the JSON payload."
        #    )
        ###############    
        for item in items.values(): # validating if there is a duplicated item. 
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="Item already exists.")
                
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201