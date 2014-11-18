from rest_framework import serializers

from TLKdb.models import *


# Serializers define the API representation.

class MemberSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Member
        fields = ('year', 'type')


class BoardSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Board
        fields = ('year', 'type')


class OfficialSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Official
        fields = ('year', 'type')


class MeritSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Merit
        fields = ('year', 'type')


class CommitteeSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Committee
        fields = ('year', 'type')


class PersonSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    boards = BoardSerializer(many=True)
    officials = OfficialSerializer(many=True)
    merits = MeritSerializer(many=True)
    committees = CommitteeSerializer(many=True)

    class Meta:
        model = Person
        fields = ('firstname', 'middlenames', 'lastname',
                  'dob', 'dod', 'birthplace', 'email',
                  'address', 'city', 'zip', 'country',
                  'joined', 'graduated', 'company',
                  'company_email', 'company_phone',
                  'notes', 'members', 'boards',
                  'officials', 'merits', 'committees')

        # Untested !!
        def create(self, validated_data):
            members_data = validated_data.pop['members']
            boards_data = validated_data.pop['boards']
            officials_data = validated_data.pop['officials']
            merits_data = validated_data.pop['merits']
            committees_data = validated_data.pop['committees']
            person = Person.objects.create(**validated_data)
            Member.objects.create(person=person, **members_data)
            Board.objects.create(person=person, **boards_data)
            Official.objects.create(person=person, **officials_data)
            Merit.objects.create(person=person, **merits_data)
            Committee.objects.create(person=person, **committees_data)
            return person

        def update(self, instance, validated_data):
            pass