from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 70)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(Category, blank=True)


    class Meta:
        verbose_name = 'Публікацію'
        verbose_name_plural = 'Публікації'

    def __str__(self):
        return '{} / {:%Y-%m-%d %H:%M:%S}'.format(self.title,
                                                  self.created_at)
