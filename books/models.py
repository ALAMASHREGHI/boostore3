from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_('author'),  on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=200)
    description = models.TextField(verbose_name=_('text'))
    price = models.DecimalField(verbose_name=_('price'), max_digits=5, decimal_places=2)
    cover = models.ImageField(verbose_name=_('cover'), upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return self.text




