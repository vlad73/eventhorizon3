import logging
from gateway.models import ExtractedPattern

def extract_patterns(data):

    stories = []

    for pattern in data['patterns']:

        if pattern.has_key('subject'):
            subject = pattern['subject']
            stories.append(subject)

        if pattern.has_key('relation'):
            relation = pattern['relation']

        if pattern.has_key('object'):
            object = pattern['object']
            stories.append(object)

        logging.info("Received pattern subject: %s relation: %s object: %s " % (subject,relation,object))

        query = ExtractedPattern.objects.filter(subject=subject, relation=relation, object=object)

        if query.count() == 0:
            p = ExtractedPattern(subject=subject, relation=relation, object=object, count = 1)
            p.save()
            p.name = "pattern_%s" % p.id
        else:
            p = query[0]
            p.count +=p.count

        p.save()

    result = []
    for story in set(stories):
        result.extend(get_patterns(story))

    return result

def get_patterns(story):
    subjects = list(ExtractedPattern.objects.filter(subject=story,count__gte=2).values())  #TODO fix bug
    objects = list(ExtractedPattern.objects.filter(object=story,count__gte=2).values())
    subjects.extend(objects)
    logging.info(subjects)
    return subjects
