# flask_graphene_mongo/app.py

#imports necessary objects from modules
from database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

#sets up the GraphQL web application
app = Flask(__name__)
app.debug = True

#sets up the URL for the GraphQL web application
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

#creates the database and runs the application if the app has been defined
if __name__ == '__main__':
    init_db()
    app.run()