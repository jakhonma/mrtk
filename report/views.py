from rest_framework import views, generics
from report.models import Report
from report.serializers import ReportSerializer


class ReportListAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportUpdateAPIView(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDeleteAPIView(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
