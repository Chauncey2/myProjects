from django.db import models
import mongoengine


class zhilian(mongoengine.Document):

    jobType = mongoengine.StringField()
    jobName = mongoengine.StringField()
    emplType = mongoengine.StringField()
    eduLevel = mongoengine.StringField()
    companyName = mongoengine.StringField()
    salary = mongoengine.ListField()
    welfare = mongoengine.ListField()
    city = mongoengine.StringField()
    workingExp = mongoengine.ListField()
    infoComLink = mongoengine.StringField()
    positionUrl = mongoengine.StringField()
    extractSkillTag = mongoengine.ListField()

