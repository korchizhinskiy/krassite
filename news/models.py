from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class New(models.Model):
    """New Model"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    content = models.TextField(verbose_name="Контент")
    create_date = models.DateTimeField(verbose_name="Дата создания",
                                       auto_now_add=True,
                                       )
    upgrade_date = models.DateTimeField(verbose_name="Дата изменения",
                                        auto_now=True,
                                        )
    image = models.ImageField(verbose_name="Изображение", upload_to="img")
    preview_image = models.ImageField(verbose_name="Превью",
                                      upload_to="prev_img",
                                      null=True, blank=True)
    author = models.ForeignKey(User,
                               verbose_name="Автор",
                               on_delete=models.CASCADE
                               )

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        image = Image.open(self.image.path)
        image_path, image_extension = self.image.path.split(".")

        # Get new path for preview image with suffix _prev
        preview_path = f"{image_path}_prev.{image_extension}"

        if image.height > 200 or image.width > 200:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(preview_path)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        db_table = "new"
