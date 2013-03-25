from events.models import NewsItem

def news_items(request):
    return {"new_items":NewsItem.objects.all()}
