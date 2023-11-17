from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import Candidate,Education,Referee
from accounts.models import CustomUser



class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        extra_kwargs = {
            'candidate': {'required': False}
        }

class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'
        extra_kwargs = {
            'candidate': {'required': False}
        }



class CandidateSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    educations = EducationSerializer(many=True)
    referees = RefereeSerializer(many=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Candidate
        fields = '__all__'
        extra_kwargs = {
                'educations': {'required': False},
                'referees': {'required': False},
            }

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
        # user_data = {
        #     'email': validated_data.pop('email'),
        #     'password': validated_data.pop('password')
        # }
        # user_serializer = CustomUserSerializer(data=user_data)
        # user_serializer.is_valid(raise_exception=True)
        # user = user_serializer.save()

        email =  validated_data.pop('email')
        password =  validated_data.pop('password')

        user = CustomUser(email=email)
        user.set_password(password)
        user.save()

        validated_data['user'] = user


        # candidate_serializer = CandidateSerializer(data=validated_data)
        # candidate_serializer.is_valid(raise_exception=True)
        # candidate = candidate_serializer.save()
        educations = validated_data.pop('educations', [])
        referees = validated_data.pop('referees', [])

        candidate = Candidate.objects.create(**validated_data)

        print(candidate)
        
        for education in educations:
            education['candidate'] = candidate.id
            education_serializer = EducationSerializer(data = education)
            education_serializer.is_valid(raise_exception=True)
            education_serializer.save()
   
        for referee in referees:
            referee['candidate'] = candidate.id
            referee_serializer = RefereeSerializer(data = referee)
            referee_serializer.is_valid(raise_exception=True)
            referee_serializer.save()


        return candidate


