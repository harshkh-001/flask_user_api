from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient,errors
from bson import ObjectId
import config


app = Flask(__name__)

# connection with mongodb
client = MongoClient(config.ATLAS_URL)
db = client[config.DB_NAME]
user_collection = db[config.COLLECTION_NAME]


@app.route('/')
def home():
    return render_template("home.html")
    
    
@app.route('/get_route', methods=['GET'])
def get_users():
    users = list(user_collection.find({},{"_id" : 0}))
    return jsonify(users),200


@app.route('/insert_user_form')
def form():
    return render_template("form.html")


@app.route('/post_route', methods=['POST'])
def insert_user():
    try:
        # dict for user data
        data = {}
        
        # find next user id
        last_user = user_collection.find_one(sort=[('id',-1)])
        last_user_id = last_user['id'] if last_user else 0
        data['id'] = last_user_id+1
        
        # convert form data to dictionary
        for k,v in request.form.items():
            if(v.strip() != ""):
                data[k] = v
            else:
                data[k] = None
        
        # insert data
        result = user_collection.insert_one(data)
        
        # Convert ObjectId to string for JSON serialization
        data['_id'] = str(result.inserted_id)
        
        # return response
        return jsonify({"data": data, "message" : "user data inserted successfuly"}),200
    
    except errors.PyMongoError as e:
        # Handle MongoDB errors
        return jsonify({
            "error": "Database error",
            "message": str(e)
        }), 500

    except Exception as e:
        # Handle any other errors
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500
 

@app.route('/delete_user_form')
def delete_form():
    return render_template("delete_form.html")  

  
@app.route('/delete_route', methods=['DELETE'])
def delete_user():
    try:
        # taking form data
        data = request.get_json()
        print("hello")
        print(data['id'])
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request must contain JSON body"}), 400

        query = {}
        if(data['id'] != 0 and data['firstName'] != ''):
            return jsonify({"error": "Bad Request", "message": "JSON must contain only one 'id' or 'firstName"}), 400
        
        elif(data['id'] != 0 and data['id']):
            query['id'] = data['id']
                
        elif(data['firstName'] != '' and data['firstName']):
            query['firstName'] = data['firstName']
            
        else:
            return jsonify({"error": "Bad Request", "message": "JSON must contain 'id' or 'firstName'"}), 400

        result = user_collection.delete_many(query) 

        if result.deleted_count == 0:
            return jsonify({"error": "Not Found", "message": "No user found with the given criteria"}), 404

        return jsonify({
            "message": "User(s) deleted successfully",
            "Detail" : query,
            "deleted_count": result.deleted_count
        }), 200

    except errors.PyMongoError as e:
        return jsonify({"error": "Database error", "message": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "Internal server error", "message": str(e)}), 500
    
    

if __name__ == '__main__':
    app.run(debug=True)
