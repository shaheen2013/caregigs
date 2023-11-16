from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import Candidate,Education,Referee



class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'



class CandidateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    educations = EducationSerializer(many=True)
    referees = RefereeSerializer(many=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Candidate
        fields = '__all__'

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['user'] = CustomUserSerializer(
    #         instance.id,
    #         instance.email,
    #         instance.first_name,
    #         instance.is_active,
    #     ).data
    #     return data
    
    def create(self, validated_data):
        user_data = {
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password')
        }

        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        validated_data['user'] = user


        educations = validated_data.pop('educations', [])

        education_serializer = EducationSerializer(many=True,data = educations)
        education_serializer.is_valid(raise_exception=True)
        education_serializer.create(education_serializer.validated_data)


        referees = validated_data.pop('referees', [])
        referee_serializer = RefereeSerializer(many=True,data = referees)
        referee_serializer.is_valid(raise_exception=True)
        referee_serializer.create(referee_serializer.validated_data)


        return candidate


