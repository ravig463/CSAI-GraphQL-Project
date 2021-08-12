# flask_graphene_mongo/models.py

#Imports necessary elements from mongoengine and mongoengine.fields
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField, ReferenceField, EmbeddedDocumentField, ListField 
)

"""
Defines a Location class. Represents a location on campus where some form of teaching occurs. Has five fields to show
the general name of the location, a building that may or may not be at the location, a room that may or may not be
in the building, the location latitude, and the location longitude. Has three references fields to show the professor
who teaches at the location, the textbook which is used at the location, and the courses taught at the location.
"""
class Location(Document):
    meta = {'collection': 'location'}
    name = StringField()
    building_name = StringField(default = "UNSPECIFIED")
    room_number = StringField(default = "UNSPECIFIED")
    latitude = StringField()
    longitude = StringField()
    professor = ReferenceField("Professor")
    textbook = ReferenceField("Textbook")
    courses = ListField(ReferenceField("Course"))

"""
Defines a Textbook class. Represents a textbook that is used for learning course content. Has three fields that indicate
the name of the textbook, the author of the textbook, and the ISBN of the textbook. Has three reference reference fields
to show the professor who uses the textbook, the location where the textbook is used, and the courses that require
the textbook.
"""
class Textbook(Document):
    meta = {'collection': 'textbook'}
    name = StringField()
    author = StringField()
    isbn = StringField()
    professor = ReferenceField("Professor")
    location = ReferenceField("Location")
    courses = ListField(ReferenceField("Course"))

"""
Defines a Professor class. Represents a teacher for a particular college class. Has one field that indicates the
name of the professor. Has three references fields to show the location of the professor when he is teaching,
the textbook used by the professor, and the course the professor teaches(reference fields allow for circular dependency).
"""
class Professor(Document):
    meta = {'collection': 'professor'}
    name = StringField()
    location = ReferenceField("Location")
    textbook = ReferenceField("Textbook")
    course = ReferenceField("Course")

"""
Defines a CourseMetrics class. Represents the workload and difficulty for a class. Has two fields that track the 
hours of homework per week that are a part of the course and the passing rate for the course in terms of percentage of
students who scored a 'C' or higher.
"""
class CourseMetrics(EmbeddedDocument):
    meta = {'collection': 'coursemetrics'}
    homework_hours_per_week = StringField()
    average_pass_rate = StringField()

"""
Defines a Course class. Represents a class that college students can take during academic quarters. Has one field that
shows the name of the course. Has one required field that states the difficulty and workload of the Course(CourseMetrics). 
Has three required reference fields to show what professor teaches the course, what textbook is needed for the course, 
and where the course is located(reference fields allow for circular dependency).
"""
class Course(Document):
    meta = {'collection': 'course'}
    name = StringField()
    metrics = EmbeddedDocumentField("CourseMetrics", required = True)
    professor = ReferenceField("Professor", required = True)
    textbook = ReferenceField("Textbook", required = True)
    course_location = ReferenceField("Location", required = True)