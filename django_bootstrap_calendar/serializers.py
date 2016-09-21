# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

import json
from django.db.models.query import QuerySet


def event_serializer(events):
    """
    serialize event model
    """
    objects_body = []

    if isinstance(events, QuerySet):
        for event in events:
            field = {
                "id": event.pk,
                "title": event.title,
                "url": event.url,
                "class": event.css_class,
                "start": event.start_timestamp, #Currently changed to UNIX timestamp. Need to convert back to datetimefield to display on events-lists.html
                "end": event.end_timestamp
                #"zID": event.zID,              To display student on events-lists.html !Currently unable to serialize "TypeError: <student: z5017993 - Ryder Cao> is not JSON serializable"
            }
            objects_body.append(field)

    objects_head = {"success": 1}
    objects_head["result"] = objects_body
    return json.dumps(objects_head)
