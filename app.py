from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)




##################
# All the code below was written before using the flask_smorest library based on Blueprint
# The code is presented in store.py and item.py, under the resources folder.
# All the endpoint methods below are there.
##################
###################  STORE  ENDPOINTS  ################################################ll a
#    
#@app.get("/store")
#def get_all_stores():
#    return {"stores": list(stores.values())}  


#@app.get("/store/<string:store_id>")
#def get_a_store(store_id):
#    try:
#        return stores[store_id]
#    except KeyError:
#        abort (404, message="Store not found.")            

    
#@app.post("/store")
#def create_store():
#    store_data = request.get_json()
#    if "name" not in store_data:
#        abort(
#            400,
#            message=" Bad request. Ensure 'name' is included in the JSON payload."
#        )
#    for store in stores.values():
#        if store_data["name"] == store["name"]:
#            abort(400, message=f"Store already exists.")
#            
#    store_id = uuid.uuid4().hex
#    store = {**store_data, "id": store_id}
#    stores[store_id] = store
#    return store, 201 # HTTP Status Code: 201 Created - It indicates that the 
#                      #request has succeeded and has led to the creation of a resource


#@app.delete("/store/<string:store_id>")
#def delete_store(store_id):
#    try: 
#        del stores[store_id]
#        return { "message": "Store deleted."}
#    except KeyError:
#        abort (404, message="Store not found.")
        
        
#@app.put("/store/<string:store_id>")
#def update_store(store_id):
#    store_data = request.get_json()
#    if "name" not in store_data:
#        abort(400, message="Bad request. Ensure 'name' is included in the JSON payloar.")
#    
#    try:
#        store = stores[store_id]
#        store |= store_data
#
#        return store
#    except KeyError:
#        abort(404, message="Store not found.")


###################  ITEM ENDPOINTS ################################################

#@app.get("/item")
#def get_all_items():
#    return {"items": list(items.values())}


#@app.get("/item/<string:item_id>")
#def get_item(item_id):
#    try: 
#        return items[item_id]
#    except KeyError:
#        abort (404, message="Item not found.")       


#@app.post("/item")
#def create_item():
#    item_data = request.get_json()
    # Here not only we need to validate data exists,
    # But also what type of data. Price should be a float,
    # for example.
#    if(
#        "price" not in item_data 
#        or "store_id" not in item_data
#        or "name" not in item_data        
#    ):
#        abort(
#            400,
#            message="Bad request. Ensure 'price', 'store_id', and 'name' are in the JSON payload."
#       )
        
#    for item in items.values(): # validating if there is a duplicated item
#        if (
#            item_data["name"] == item["name"]
#            and item_data["store_id"] == item["store_id"]
#        ):
#            abort(400, message="Item already exists.")
            
#    item_id = uuid.uuid4().hex
#    item = {**item_data, "id": item_id}
#    items[item_id] = item
#    return item, 201


#@app.delete("/item/<string:item_id>")
#def delete_item(item_id):
#    try: 
#        del items[item_id]
#        return { "message": "Item deleted."}
#    except KeyError:
#       abort (404, message="Item not found.")
        
        
#@app.put("/item/<string:item_id>")
#def update_item(item_id):
#    item_data = request.get_json()
#    if "price" not in item_data or "name" not in item_data:
#        abort(400, message="Bad request. Ensure 'price', and 'name'are included in the JSON payloar.")
    
#    try:
#        item = items[item_id]
#        item |= item_data

#        return item
#    except KeyError:
#        abort(404, message="Item not found.")
###################################################################        
# docker commands:
# build:   docker build -t flask-smorest-api .                  
# volume:  docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api