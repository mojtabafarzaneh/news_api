from django.db import models

class Article(models.Model):
    id_number = models.CharField(max_length=256, null=False, blank=False)
    url = models.CharField(max_length=256, null= False, blank = False)
    title = models.CharField(max_length=256, null=False, blank=False)
    content_html = models.CharField(max_length=256, null=False, blank= False)
    summary = models.CharField(max_length=256, null= False, blank = False)
    date_published = models.CharField(max_length=256, null=False, blank=False)
    
    def __str__(self):
        return f"{self.title}"