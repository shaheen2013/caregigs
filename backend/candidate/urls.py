from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, EducationViewSet, RefereeViewSet

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet, basename='candidate')
router.register('educations', EducationViewSet, basename='education')
router.register('referees', RefereeViewSet, basename='referee')

urlpatterns = router.urls