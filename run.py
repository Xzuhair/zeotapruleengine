from app.api import app
from app.database import create_tables

if __name__ == '__main__':
    # Create the database tables if they don't exist
    create_tables()
    
    # Start the Flask app
    app.run(debug=True)