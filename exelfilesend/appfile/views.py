from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import generics, permissions
from .models import Student
import xlwings as xl
# from .models import CartOrder  # Import your actual model
# from .serializers import CartOrderListSerializer  # Import your actual serializer
# from .pagination import CustomPagination  # Import your actual pagination class

class AdminTransactionListView(generics.ListAPIView):
    # serializer_class = CartOrderListSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # pagination_class = CustomPagination

   

    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        print(queryset)
        # Convert data into pandas dataframe
        data = pd.DataFrame(list(queryset.values()))
        print('data',data)

        # exel file settings
        excel_file = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
        print('excel_file',excel_file)
        data.to_excel(excel_file, index=False)
        with open('output.xlsx', 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=output.xlsx'

        return response
        

       
        
        
        

        
        

