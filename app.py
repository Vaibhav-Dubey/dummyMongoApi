from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
PORT = 3000

# MongoDB Atlas connection URI (replace with your connection string)
uri = 'mongodb+srv://hackrtfm:YPpEK604DLIfIb1o@cluster0.lame0pq.mongodb.net/'

# Endpoint to fetch data from MongoDB Atlas
@app.route('/api/data')
def get_data():
    try:
        # Connect to MongoDB Atlas
        client = MongoClient(uri)

        # Access the database and collection
        db = client.obdtwo
        collection = db.obdtwo

        # Fetch data from MongoDB
        data = list(collection.find({}))

        # Close the connection
        client.close()

        # Convert ObjectId to string for JSON serialization
        for item in data:
            item['_id'] = str(item['_id'])

        # Send the fetched data as JSON response
        return jsonify(data), 200
    except Exception as e:
        print('Error fetching data:', e)
        return jsonify({'error': 'Internal Server Error'}), 500

# Start the server
if __name__ == '__main__':
    app.run(port=PORT)
