import cherrypy
import pymysql

# Set up the MySQL connection
conn = pymysql.connect(
    host='localhost',      # Your MySQL host
    user='root',           # Your MySQL root user
    password='Kelsey2003!', # MySQL password
    database='extended_contact_db'  # The database name
)
cursor = conn.cursor()

# Function to get all contacts from the database
def get_all_contacts():
    cursor.execute("SELECT name, surname, sex, age, dob, email FROM long_contact;")
    result = cursor.fetchall()
    contacts = [{'name': row[0], 'surname': row[1], 'sex': row[2], 'age': row[3], 'dob': row[4], 'email': row[5]} for row in result]
    return contacts

# CherryPy-exposed function to serve the contacts list
@cherrypy.expose
def index():
    contacts = get_all_contacts()
    contact_list = "<br>".join(f"Contact Name: {contact['name']}, Surname: {contact['surname']}, Sex: {contact['sex']}, Date of Birth: {contact['dob']}, Age: {contact['age']}, Email: {contact['email']}" for contact in contacts)
    return f"<h1>Contact List</h1><div>{contact_list}</div>"

# Close the cursor and connection when the app is stopped
def close_resources():
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# Start the CherryPy server
if __name__ == '__main__':
    cherrypy.engine.subscribe('exit', close_resources)  # Ensure resources are closed on exit
    cherrypy.quickstart(index, '/', {                   # Use the index function directly
        'global': {
            'server.socket_host': '0.0.0.0',  # Listen on all interfaces
            'server.socket_port': 8080,        # Or your desired port
        }
    })
