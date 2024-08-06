# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organization, Period, Line, Form, Data
from .serializers import OrganizationSerializer, PeriodSerializer, LineSerializer, FormSerializer, DataSerializer
from django.shortcuts import get_object_or_404
import xlsxwriter
from django.http import HttpResponse


class OrganizationView(APIView):
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeriodView(APIView):
    def get(self, request):
        periods = Period.objects.all()
        serializer = PeriodSerializer(periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LineView(APIView):
    def get(self, request):
        lines = Line.objects.all()
        serializer = LineSerializer(lines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormView(APIView):
    def get(self, request):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataView(APIView):
    def get(self, request):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportView(APIView):
    def get(self, request, period_id):
        period = get_object_or_404(Period, id=period_id)
        forms = Form.objects.filter(period=period)
        output = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        output['Content-Disposition'] = 'attachment; filename=report.xlsx'
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        row = 0
        for form in forms:
            data = Data.objects.filter(form=form, line__is_active=True)
            for item in data:
                worksheet.write(row, 0, form.organization.name)
                worksheet.write(row, 1, item.line.name)
                worksheet.write(row, 2, item.under_31)
                worksheet.write(row, 3, item.over_31)
                row += 1

        workbook.close()
        return output

