from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone


def post_images_directory_path(instance: 'Post', filename: str) -> str:

    return 'images/thumbnails/{post_name}/{filename}'.format(
        post_name=instance.title,
        filename=filename,
    )


class Post(models.Model):
    """
    Модель для создания поста.
    """

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to=post_images_directory_path,
        validators=[
          FileExtensionValidator(
              allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif')
          )]
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title


