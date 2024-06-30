from pymongo import MongoClient
from urllib.parse import quote_plus

def get_db():
    username = quote_plus("triple6ixxx")
    password = quote_plus("KmTplivNotIdent@#")
    uri = f"mongodb+srv://{username}:{password}@cluster0.0gxcvik.mongodb.net/target_app?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client.get_database("target_app")
    return db

def save_results(user_id, image_path, analysis):
    db = get_db()
    results = {
        'user_id': user_id,
        'image_path': image_path,
        'analysis': analysis
    }
    db.results.insert_one(results)

def get_user_history(user_id):
    db = get_db()
    history = db.results.find({'user_id': user_id})
    return list(history)
