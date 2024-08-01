from mongoengine import connect


MONGODB_URI = "mongodb+srv://irohanrajput:12345@cluster0.xwtbcyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#exposed intentionally

    
def connect_database(app):
        try:
            connect(
                host=MONGODB_URI,
                alias='default' )
        except:
            print("Error connecting to the database")
            
