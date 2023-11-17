from rest_framework import viewsets, parsers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Candidate, Education, Referee
from .serializers import CandidateSerializer, EducationSerializer, RefereeSerializer
from .permissions import IsCandidateOwner



class CandidateViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class EducationViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsCandidateOwner]

    def list(self, request, *args, **kwargs):
        current_user = self.request.user
        print(current_user)
        candidate = get_object_or_404(Candidate, user=current_user)
        educations = Education.objects.filter(candidate=candidate)
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data)


class RefereeViewSet(viewsets.ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser]
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer
    permission_classes = [IsCandidateOwner]

    def list(self, request, *args, **kwargs):
        current_user = self.request.user
        candidate = get_object_or_404(Candidate, user=current_user)
        referees = Referee.objects.filter(candidate=candidate)
        serializer = EducationSerializer(referees, many=True)
        return Response(serializer.data)
