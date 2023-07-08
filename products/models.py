from django.db import models
from simple_history.models import HistoricalRecords

from base.models import BaseModel


class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return  self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    desciption = models.CharField('Descripción', max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'

    def __str__(self):
        return self.desciption

class Indicator(BaseModel):
    """Model definition for Indicator."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,
                                         verbose_name='Indicador de Oferta')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):

        return f'Oferta de la categoría {self.category_product} : {self.descount_value}%'


class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,
                                         verbose_name='Categoria de Producto', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name