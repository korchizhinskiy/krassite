from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from PIL import Image
from os import path


class Contact(models.Model):
    """Contact Model"""
    name = models.CharField(verbose_name="Имя", max_length=255)
    email = models.EmailField(verbose_name="Почтовый адрес")


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
                                      null=True, blank=True)
    author = models.ForeignKey(User,
                               verbose_name="Автор",
                               on_delete=models.CASCADE
                               )

    def __str__(self):
        return mark_safe(self.title)

    def save(self):
        super().save()
        self.save_preview_image()
        return super(New, self).save()

    def save_preview_image(self):
        """Define preview_image from main image by reducing image size"""
        image = Image.open(self.image.path)
        image_name, image_extension = path.splitext(self.image.path)

        # Get new path for preview image with suffix _prev
        preview_path = f"{image_name}_prev{image_extension}"

        if image.height > 200 or image.width > 200:
            self.resize_photo(image, preview_path)

        self.preview_image.name = "img/" + path.basename(preview_path)

    def resize_photo(self, image: Image.Image, preview_path: str):
        """Function of resize photo by given values"""
        output_size = (200, 200)
        image.thumbnail(output_size)
        image.save(preview_path)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        db_table = "new"


@receiver(pre_delete, sender=New)
def images_model_delete(instance, **kwargs):
    """Signal which delete image and preview_image from media path"""
    if instance.image.name:
        instance.image.delete(False)
        instance.preview_image.delete(False)
