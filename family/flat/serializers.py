from rest_framework import serializers
from .models import Member, Parent, Children


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        # fields = ('flat')
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    childs = ChildrenSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        # fields = ('flat')
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    parents = ParentSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        # fields = ('flat')
        fields = "__all__"
