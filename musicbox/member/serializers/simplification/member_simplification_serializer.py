from rest_framework import serializers

from member.models.member import Member


class MemberSimplificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            Member.seq.field.name,
            Member.username.field.name,
            Member.status.field.name,
            Member.create_at.field.name,
            Member.update_at.field.name,
        ]
