from django.db import models
from django.template.defaultfilters import truncatechars


JS_GENERATE_RANDOM = (
    '<a onclick="genRand()">Generate new random key</a>'
    '<script>'
    'function genRand() {'
    'var result = "INSECURE-";'
    'for (var i = 1; i < 21; i++) {'
    'result += "abcdefghijklmnopqrstuvwxyz0123456789".charAt(Math.floor(Math.random() * 36));'
    'if (i % 5 == 0 && i != 20) result += "-"'
    '}'
    'document.getElementById("id_api_key").value = result;'
    '}'
    'if (!document.getElementById("id_api_key").value) genRand()'
    '</script>'
)


class Flight(models.Model):
    # TODO: GPS location
    
    api_key = models.CharField(
        verbose_name='API Key',
        max_length=32,
        unique=True,
        help_text=JS_GENERATE_RANDOM,
    )
    
    class Meta:
        verbose_name = 'дрон'
        verbose_name_plural = 'дроны'
    
    def __str__(self) -> str:
        return f'flight_{self.id}'


class Station(models.Model):
    api_key = models.CharField(
        verbose_name='API Key',
        max_length=32,
        unique=True,
        help_text=JS_GENERATE_RANDOM,
    )
    aruco = models.IntegerField(
        verbose_name='Aruco ID',
        unique=True,
    )
    opened = models.BooleanField(
        verbose_name='Is station open',
        editable=False,
        default=False,
    )
    done = models.BooleanField(
        verbose_name='Is work done',
        editable=False,
        default=False,
    )
    disabled = models.BooleanField(
        verbose_name='Busy',
        default=False,
        editable=False,
    )
    
    class Meta:
        verbose_name = 'зарядная станция'
        verbose_name_plural = 'зарядные станции'
    
    def __str__(self) -> str:
        return f'{self.id}. {self.get_status()}, {self.get_busyness()} | aruco_{self.aruco}'
    
    def get_status(self):
        if self.opened and self.done:
            return 'Opened (11)'
        if self.opened:
            return 'Opening (10)'
        if not self.opened and self.done:
            return 'Closed (01)'
        return 'Closing (00)'
    
    get_status.allow_tags = True
    get_status.short_description = "Статус"
    
    def get_busyness(self):
        if self.disabled:
            return 'Busy'
        return 'Vacate'

    get_busyness.allow_tags = True
    get_busyness.short_description = "Занятость"


class Question(models.Model):
    text = models.TextField(
        verbose_name='Текст вопроса',
    )
    contact = models.CharField(
        verbose_name='Обратная связь',
        max_length=128,
    )
    date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    rewiewed = models.BooleanField(
        verbose_name='Обработано',
        default=False,
    )
    
    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
    
    def __str__(self) -> str:
        return f'{self.date.strftime("%d.%m.%Y")} - {self.truncate_text(32)} - {self.truncate_contact()}'
    
    def truncate_text(self, chars=50):
        return truncatechars(self.text, chars)
    
    truncate_text.allow_tags = True
    truncate_text.short_description = "Текст вопроса"
    
    def truncate_contact(self, chars=16):
        return truncatechars(self.contact, chars)
    
    truncate_contact.allow_tags = True
    truncate_contact.short_description = "Обратная связь"
