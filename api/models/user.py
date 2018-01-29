from pymodm import fields, MongoModel, EmbeddedMongoModel

class User(MongoModel):
    # Use 'email' as the '_id' field in MongoDB.
    email = fields.EmailField(primary_key=True)
    fname = fields.CharField()
    lname = fields.CharField()