`app = Flask(__name__)`
The argument is the name of the main module or package of the application.

---
##### Macros


---
##### SQLAlchemy
`date = db.Column(db.DateTime, default=datetime.utcnow)`  
The above is called everytime a new bookmark is created. Date sets when created
 
A `Model class` represents a database table.  
Every instance represents a row in that table  
Inherit from `db.Model`  
`Columns` are defined as class attributes on the `Model Class`  
The name of the database column will be the name of the attribute
```python
id = db.Column(db.Integer, primary_key=True)
url = db.Column(db.Text, nullable=False)
description = db.Column(db.String(300))
```  

```python
db.session.add(item)  
db.session.commit()  
```  
The `session` is the 'local store' in sqlalchemy.   

`backref='model'`  
Adding this adds a link to the user class meaning we dont have to use the `user_id` all the time but have access to the `User` object.  

`item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)`  
The above is on the many side 
Then on the one side you have  
`db.relationship('Item', backref='item', lazy='dynamic')`  
`db.relationship` defines a 1-many relationship.  
FIrst argument gives many side of the relation ('item' in this example.)  
`backref` - name of an attribute on the related object  
`lazy` - how the related rows should be loaded  
 * Options:  

  * 'select': load the data lazily, when its requested
  * 'joined': load the data in the same query as the parent using a `JOIN` statement  
  * 'subquery': like joined but use a subquery  
  * 'dynamic': useful if you have many items. Returns a query object which you can further refine before loading items. Usually what you want if you expect more than a handful of items.  
  
`lazy=dynamic`  

---  

##### Jinja2  
  
```python
{% with variable_name=expression %}
```  
This creates a new scope with variable_name in it.  
This is handy for including variables in partials and keeping them abstract. (can leave the variable name as abstract as you like and match it with this expression)  
  
---  

#### Many To Many Realtionship  
Create a junction table with two foreign keys
```python  
# set up a junction table for many to many relationships
tags = db.Table('bookmark_tag',  
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),  
    db.Column('bookmark_id', db.Integer, db.ForeignKey('bookmark.id'))  
    )  

# in the bookmark class  
 _tags = db.relationship('Tag', secondary=tags, lazy='joined', backref=db.backref('bookmarks', lazy='dynamic'))  
```  

### Make somethign available in the global context   
Make a function available in templates  
```python  
#makes something available in the global context
@main.app_context_processor
def inject_tags():
    return dict(all_tags=Tag.all)  
```   
The above references the Tags.all() method in the Tags model.   



## OTHER NOTES  
##### Decorators   

 * Find common API patterns and turn them into decorators  
 * Keep the "plumbing" out of your endpoints  
 * Use libraries like Gevent to run tasks asynchronously  
 * Use rate limits everywhere  
 * Let errors bubble up from your decorators and endpoints  
 * request, session, and g make powerful decorators possible  
 * Dont ignore flasks built in decorators

##### Error Handlers  
Dont do error handling in endpoints, write JSON-friendly error handlers like this:  
Exception from `models/user.py`  
```python  
class ValidationError(Exception):  
    def __init__(self, field, message):  
        self.field = field  
        self.message = message  
```  
Handler from `errors.py`  
```python  
@api.errorhandler(user.ValidationError)  
def handle_user_validation_error(error):  
    response = jsonify({  
        'msg': error.message,  
        'type': 'validation',  
        'field': error.field  
    })  
    response.status_code = 400  
    return response  
```











