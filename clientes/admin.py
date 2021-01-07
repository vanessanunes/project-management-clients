from django.contrib import admin
from .models import Documento
from .models import Person
from .models import Produto
from .models import Venda

admin.site.register(Documento)
admin.site.register(Person)
admin.site.register(Produto)
admin.site.register(Venda)
