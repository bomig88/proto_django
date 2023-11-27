from rest_framework import serializers

from member.models.member import Member


class MemberSimplificationSerializer(serializers.ModelSerializer):
    """
    회원 간소화 Serializer
    """
    class Meta:
        model = Member
        fields = [
            Member.seq.field.name,
            Member.username.field.name,
            Member.status.field.name,
            Member.tag.field.name,
            Member.create_at.field.name,
            Member.update_at.field.name,
        ]


class MemberSimplificationLoginSerializer(serializers.ModelSerializer):
    """
    회원 간소화 로그인 용 Serializer
    """
    class Meta:
        model = Member
        fields = [
            Member.seq.field.name,
            Member.username.field.name,
            Member.status.field.name,
            Member.tag.field.name,
            Member.create_at.field.name,
        ]
