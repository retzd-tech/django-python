from django.db import models

class CrawlResult(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    fetched_at = models.DateTimeField(auto_now_add=True)
    books = models.JSONField(default=list, blank=True)  # ✅ Add this line
