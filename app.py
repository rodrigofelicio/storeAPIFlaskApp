from flask import Flask


app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name":  "chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_store():
    return {"stores": stores}