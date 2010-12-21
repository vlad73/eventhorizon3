import logging
from gateway.models import ExtractedPattern

def save_or_update_pattern(data):
    if(data.has_key('name')):
        name = data['name']

    if(data.has_key('subject')):
        subject = data['subject']

    if(data.has_key('relation')):
        relation = data['relation']

    if(data.has_key('object')):
        object = data['object']

    logging.info("Received pattern: name: %s subject: %s relation: %s object: %s " % (name,subject,relation,object))

    query = ExtractedPattern.objects.filter(subject=subject, relation = relation, object=object)

    if query.count() == 0:
        p = ExtractedPattern(subject=subject, relation = relation, object=object)
        p.save()
        p.name = "pattern_%s" % p.id
    else:
        p = query[0]
        p.count +=p.count

    p.save()

    return "pattern saved successfully"

def get_patterns(data):
    subject = data['subject']
    query = ExtractedPattern.objects.filter(subject=subject)
    patterns = [p for p in query if p.count > 2]
    return patterns
