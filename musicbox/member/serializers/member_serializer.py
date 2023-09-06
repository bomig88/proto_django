from rest_framework import serializers

from member.models.member import Member


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class MemberListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class MemberDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'
