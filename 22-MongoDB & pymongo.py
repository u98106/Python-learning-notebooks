
# coding: utf-8

# # MongoDB

# In[1]:

from IPython.core.display import HTML
css = "table td:nth-child(1) {font-weight:bold; background-color: #fec; }"
HTML('<style>{}</style>'.format(css))


# ### What is `nosql`?

# > A NoSQL database provides a mechanism for storage and retrieval of data which is modeled in <b>means other than the tabular relations</b> used in relational databases.

# - MongoDB is a `document database`
# - Binary JSON (BSON) data constitutes a document
# - Each data-base constitutes `collection`s of such documents
# - Each document includes the `schema` for the data it stores
#     - could potentially vary between objects
#     - usually is the same across 

# ### Why nosql?

# Relational databases were not designed to cope with the scale and agility challenges of modern applications
# 
# - Developers are working with applications that create massive volumes of new, rapidly changing data types — structured, semi-structured, unstructured and polymorphic data.
# - Waterfall development cycle is long gone. Now small teams work in agile sprints, iterating quickly and pushing code every week or two
# - Applications `always-on`, accessible from many different devices and scaled globally to millions of users.
# - scale-out architectures using open source software, commodity servers and cloud computing instead of large monolithic servers and storage infrastructure.

# ### nosql benefits

# - Large volumes of rapidly changing structured, semi-structured, and unstructured data
# - Agile sprints, quick schema iteration, and frequent code pushes
# - Object-oriented programming that is easy to use and flexible
# - Geographically distributed scale-out architecture instead of expensive, monolithic architecture

# ### mongoDB elements

# RDBMS | MongoDB
# ------|---------
# Database | Database
# Table | Collection
# Tuple/Row | Document
# column | Field
# Table Join | Embedded Documents
# Primary Key | Primary Key (Default key `_id` provided by mongodb itself)

# ### Sample Document

# ```json
# {
#    _id: ObjectId(7df78ad8902c)
#    title: 'MongoDB Overview', 
#    description: 'MongoDB is no sql database',
#    tags: ['mongodb', 'database', 'NoSQL'],
#    likes: 100, 
#    comments: [	
#       {
#          user:'user1',
#          message: 'My first comment',
#          dateCreated: new Date(2011,1,20,2,15),
#          like: 0 
#       },
#       {
#          user:'user2',
#          message: 'My second comments',
#          dateCreated: new Date(2011,1,25,7,45),
#          like: 5
#       }
#    ]
# }
# ```

# - `_id` is a 12 bytes hexadecimal number which assures the uniqueness of every document.
# - If not provided, is supplied by mongoDB

# - `mongod` is the server (daemon)
# - `mongo` is the client
#     - provides a command line shell
#     - standard javascript acceptable as commands

# ### PyMongo

# - python module to access mongodb database and documents
# - Provides all CRUD capabilities along with admin tasks as well

# In[2]:

# m.py

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db

def add_country(db):
    db.countries.insert({"name" : "Canada"})
    
def get_country(db):
    return db.countries.find_one()

if __name__ == "__main__":

    db = get_db() 
    add_country(db)
    print get_country(db)


# ```
# $ python m.py
# /usr/lib/python2.7/dist-packages/pkg_resources.py:1031: UserWarning: /home/k/.python-eggs is writable by group/others and vulnerable to attack when used with get_resource_filename. Consider a more secure location (set with .set_extraction_path or the PYTHON_EGG_CACHE environment variable).
#   warnings.warn(msg, UserWarning)
# {u'_id': ObjectId('53c181ce8ce4b12ad763c1dd'), u'name': u'Canada'}
# ```

# In[ ]:

# mongo1.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# data base name : 'test-database-1'
mydb = client['test-database-1']

import datetime

myrecord = {
        "author": "Duke",
        "title" : "PyMongo 101",
        "tags" : ["MongoDB", "PyMongo", "Tutorial"],
        "date" : datetime.datetime.utcnow()
        }

record_id = mydb.mytable.insert(myrecord)

print record_id
print mydb.collection_names()


# ### Inserting multiple documents

# In[ ]:

# mongo3.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
mydb = client['test-database']

mydb.posts.drop()

import datetime
post = {
        "author": "Duke 5",
        "title" : "PyMongo 101 - 5",
        "tags" : ["MongoDB 5", "PyMongo 101 - A5", "Tutorial 5"],
        "date" : datetime.datetime.utcnow()
        }

posts = mydb.posts
post_id = posts.insert(post)

print post_id
print mydb.collection_names()

new_posts = [{"author": "Duke 6",
              "title" : "PyMongo 101-A6",
              "tags" : ["MongoDB 6", "PyMongo 6", "Tutorial 6"],
              "date" : datetime.datetime(2015, 11, 28, 01, 13)},
             {"author": "Adja",
              "title": "MongoDB 101-A7",
              "note": "Schema free MongoDB",
              "date": datetime.datetime(2015, 11, 29, 11, 42)}
            ]
mydb.posts.insert(new_posts)


# ### Querying

# In[ ]:

for post in mydb.mytable.find():
    post
 
{u'date': datetime.datetime(2015, 11, 28, 5, 18, 40, 945000), u'_id': ObjectId('5659393d312f910b5b05c18a'), u'author': u'Duke', u'tags': [u'MongoDB', u'PyMongo', u'Tutorial'], u'title': u'PyMongo 101'}
{u'date': datetime.datetime(2015, 11, 28, 6, 11, 6, 496000), u'_id': ObjectId('5659457a312f91162bf20276'), u'author': u'Duke II', u'tags': [u'MongoDB II', u'PyMongo II', u'Tutorial II'], u'title': u'PyMongo II 101'}
{u'date': datetime.datetime(2015, 11, 28, 6, 11, 6, 496000), u'_id': ObjectId('5659457a312f91162bf20277'), u'author': u'Duke III', u'tags': [u'MongoDB III', u'PyMongo III', u'Tutorial III'], u'title': u'PyMongo III 101'}
{u'date': datetime.datetime(2015, 11, 28, 7, 2, 37, 317000), u'_id': ObjectId('56595481312f9119e4bace31'), u'author': u'Duke 4', u'tags': [u'MongoDB 4', u'PyMongo 4', u'Tutorial 4'], u'title': u'PyMongo 4 101'}


# In[ ]:

for post in mydb.mytable.find({"author": "Adja"}):
    post
 
{u'note': u'Schema free MongoDB', u'date': datetime.datetime(2015, 11, 29, 11, 42), u'_id': ObjectId('56595cf0312f912bc242f79e'), u'author': u'Adja', u'title': u'MongoDB 101-A7'}


# In[ ]:

mydb.mytable.count()
7

mydb.mytable.find({"author": "Adja"}).count()
1


# #### Range queries

# In[ ]:

import datetime
for post in mydb.mytable.find({"date": {"$lt": datetime.datetime(2015, 12, 1)}}).sort("author"):
    post
 
{u'note': u'Schema free MongoDB', u'date': datetime.datetime(2015, 11, 29, 11, 42), u'_id': ObjectId('56595cf0312f912bc242f79e'), u'author': u'Adja', u'title': u'MongoDB 101-A7'}
{u'date': datetime.datetime(2015, 11, 28, 5, 18, 40, 945000), u'_id': ObjectId('5659393d312f910b5b05c18a'), u'author': u'Duke', u'tags': [u'MongoDB', u'PyMongo', u'Tutorial'], u'title': u'PyMongo 101'}


# ### Indexing

# - Indexes needed for speeding up queries
# - One of more fields may be specified as index for a document collection

# In[ ]:

result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                  unique=True)
list(db.profiles.index_information())
[u'user_id_1', u'_id_']


# In[ ]:

user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)


# Indexes prevent us from inserting a document whose `user_id` is already present

# In[ ]:

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile)
Traceback (most recent call last):
pymongo.errors.DuplicateKeyError: E11000 duplicate key error index: test_database.profiles.$user_id_1 dup key: { : 212 }


# In[ ]:




# In[ ]:



