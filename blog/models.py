from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='name post')
    content = models.TextField(verbose_name='text post')
    publish = models.BooleanField(default=True)
    datearticle = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'New post'
        verbose_name_plural = 'All posts'

    def __str__(self):
        return self.title
