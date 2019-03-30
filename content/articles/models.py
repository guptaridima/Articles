from django.db import models
# Create your models here.


class Article(models.Model):
    """
    This models helps one to persist the title, content,
    author_name & vote count
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    class Meta:
        """
        The title and the author name should be a unique combination.
        """
        unique_together = (('title', 'author_name'),)

    def __str__(self):
        return str(self.id)
