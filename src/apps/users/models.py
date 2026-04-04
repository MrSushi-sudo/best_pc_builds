from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _


class BaseUser(AbstractUser):
    """Модель пользователя"""

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ("-date_joined",)

    def __str__(self) -> str:
        return self.get_username()


class BaseGroup(Group):
    """Прокси модель групп"""

    class Meta:
        proxy = True
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")
