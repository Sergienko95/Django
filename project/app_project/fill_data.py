# management/commands/fill_data.py
from django.core.management.base import BaseCommand
from .models import Organization, Period, Line, Form, Data


class Command(BaseCommand):
    help = 'Fill the database with test data'

    def handle(self, *args, **kwargs):
        organization = Organization.objects.create(name='Test Organization')
        period = Period.objects.create(month='January', year=2023)

        line1 = Line.objects.create(name='Общая численность специалистов', period=period)
        line11 = Line.objects.create(name='направлен комиссией', period=period)
        line12 = Line.objects.create(name='принят из других источников', period=period)

        line2 = Line.objects.create(name='Количество уволенных специалистов', period=period)
        line21 = Line.objects.create(name='по истечению срока контракта', period=period)
        line22 = Line.objects.create(name='переезд в другую местность', period=period)
        line23 = Line.objects.create(name='призыв на срочную службу', period=period)

        form = Form.objects.create(organization=organization, period=period)

        Data.objects.create(line=line1, form=form, under_31=10, over_31=20)
        Data.objects.create(line=line11, form=form, under_31=5, over_31=10)
        Data.objects.create(line=line12, form=form, under_31=5, over_31=10)

        Data.objects.create(line=line2, form=form, under_31=15, over_31=25)
        Data.objects.create(line=line21, form=form, under_31=5, over_31=10)
        Data.objects.create(line=line22, form=form, under_31=5, over_31=10)
        Data.objects.create(line=line23, form=form, under_31=5, over_31=10)

        self.stdout.write(self.style.SUCCESS('Test data added successfully'))