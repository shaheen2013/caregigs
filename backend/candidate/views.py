from rest_framework import viewsets, parsers
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
