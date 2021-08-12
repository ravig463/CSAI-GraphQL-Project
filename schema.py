# flask_graphene_mongo/schema.py

#Imports necessary libraries, modules, and objects to build the GraphQl schema
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Location as LocationModel
from models import Textbook as TextbookModel
from models import Professor as ProfessorModel
from models import CourseMetrics as CourseMetricsModel
from models import Course as CourseModel

"""
Defines the Location type within the schema which is based on the Location object in models.py and implements Node 
interface to allow user to traverse fields in an efficient and systematic manner. 
"""
class Location(MongoengineObjectType):

    class Meta:
        model = LocationModel
        interfaces = (Node,)

"""
Defines the Textbook type within the schema which is based on the Textbook object in models.py and implements Node 
interface to allow user to traverse fields in an efficient and systematic manner. 
"""
class Textbook(MongoengineObjectType):

    class Meta:
        model = TextbookModel
        interfaces = (Node,)

"""
Defines the Professor type within the schema which is based on the Professor object in models.py and implements Node 
interface to allow user to traverse fields in an efficient and systematic manner. 
"""
class Professor(MongoengineObjectType):

    class Meta:
        model = ProfessorModel
        interfaces = (Node,)

"""
Defines the CourseMetrics type within the schema which is based on the CourseMetrics object in models.py and implements Node 
interface to allow user to traverse fields in an efficient and systematic manner. 
"""
class CourseMetrics(MongoengineObjectType):

    class Meta:
        model = CourseMetricsModel
        interfaces = (Node,)

"""
Defines the Course type within the schema which is based on the Course object in models.py and implements Node 
interface to allow user to traverse fields in an efficient and systematic manner. 
"""
class Course(MongoengineObjectType):

    class Meta:
        model = CourseModel
        interfaces = (Node,)

"""
Defines the Query root type within the schema with Location, Textbook, Professor, CourseMetrics, and Course as fields
that can be traversed when the user enters a query. Includes resolve() method that enables users to utilize field-based
filtering for more accurate results.
"""
class Query(graphene.ObjectType):
    node = Node.Field()
    location = MongoengineConnectionField(Location, search = graphene.String())
    textbook = MongoengineConnectionField(Textbook, search = graphene.String())
    professor = MongoengineConnectionField(Professor, search = graphene.String())
    course_metrics = MongoengineConnectionField(CourseMetrics, search = graphene.String())
    course = MongoengineConnectionField(Course, search = graphene.String())
    """
    resolve: Searches for specific objects and fields based on what the users enters as a parameter(can be field or object)

    args:
        search: Field in string form used to filter through database to find the desired object or field

    returns: Objects or field the user wanted when entering the query
    """
    def resolve(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(name=search)
            )
            return Link.objects.filter(filter)
        return Link.objects.all()

#Initializes and builds the schema
schema = graphene.Schema(query=Query, types=[Location, Textbook, Professor, CourseMetrics, Course])