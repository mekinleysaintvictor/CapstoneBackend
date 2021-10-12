from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                    UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    #Importing to attach a profile to user upon creation
    # profile = MusicianSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(sel, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        #Creating profile
        # profile_data = validated_data.pop('profile')

        # profile = Musician.objects.create(
        #     user = user
        #     aboutMe = profile_data['aboutMe'],
        #     instruments = profile_data['instruments'],
        #     influences = profile_data['instruments'],
        #     genres = profile_data['genres'],
        # )

        user.set_password(validated_data['password'])
        user.save()

        return user

