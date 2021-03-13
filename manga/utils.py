from .models import Manga, Chapter, User, Author
from datetime import datetime

def top3recentchapter(manga):
    chapters = []
    for item in manga.chapter_set.order_by('-last_updated')[:3]:
    # for item in manga.chapter_set.all()[:3]:
        chapters.append(item)
    return chapters

def updated_time_templates(item):
    delta = datetime.now() - item.last_updated
    days = delta.days
    if days == 0:
        hours = delta.seconds // 3600
        if hours == 0:
            minutes = delta.seconds // 60
            if minutes == 0:
                return('Vài giây trước')
            else:
                return('%s phút trước' % minutes)
        else:
            return('%s tiếng trước' % hours)
    elif days <= 7: 
        return ('%s ngày trước' % days)
    else:
        return('%s/%s/%s' % (item.last_updated.day, item.last_updated.month, item.last_updated.year))

def get_rating(item):
    pass

# def updated_time_templates(chapter : Chapter):
#     pass