import logging
from gateway.models import ExtractedPattern

def extract_patterns(data):

    stories = []

    for pattern in data['patterns']:
        if(pattern.has_key('name')):
            name = data['name']
            stories.append(name)

        if(pattern.has_key('subject')):
            subject = data['subject']
            stories.append(subject)

        if(pattern.has_key('relation')):
            relation = data['relation']
            stories.append(relation)

        if(pattern.has_key('object')):
            object = data['object']
            stories.append(object)

        logging.info("Received pattern: name: %s subject: %s relation: %s object: %s " % (name,subject,relation,object))

        query = ExtractedPattern.objects.filter(subject=subject, relation=relation, object=object)

        if query.count() == 0:
            p = ExtractedPattern(subject=subject, relation=relation, object=object)
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

def get_patterns(data):
    subject = data['subject']
    query = ExtractedPattern.objects.filter(subject=subject)
    patterns = [p for p in query if p.count > 2]
    return patterns
