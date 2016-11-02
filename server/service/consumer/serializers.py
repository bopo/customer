# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Address, Profile


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)
    # phone = serializers.CharField(source='profile.phone', read_only=True)
    # name = serializers.CharField(source='profile.name', read_only=True)

    # menus = serializers.SerializerMethodField()
    # is_active = serializers.BooleanField(source='profile.is_cms_active')

    # def get_menus(self, user):
    #     return get_menus(user)

    class Meta:
        depth = 1
        model = get_user_model()
        # fields = ('id', 'username', 'name', 'email', 'phone', 'groups', 'is_active')


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)


class AvatarRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.url


# class BestsProfileSerializer(serializers.ModelSerializer):
#     avatar = AvatarRelatedField(many=False, read_only=True, source='profile.avatar')
#     nick = serializers.StringRelatedField(many=False, read_only=True, source='profile.nick')
#     name = serializers.StringRelatedField(many=False, read_only=True, source='profile.name')
#
#     class Meta:
#         depth = 1
#         model = get_user_model()
#         fields = ("id", "avatar", "nick", "name", "avatar")

# class BestsProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ("name", "nick", "avatar", 'owner')


class ProfileSerializer(serializers.ModelSerializer):
    qrcode = serializers.URLField(read_only=True)
    jpush_registration_id = serializers.CharField(source='owner.jpush_registration_id', read_only=True)

    class Meta:
        model = Profile
        read_only_fields = ("payment", "balance", "total",)
        fields = ("name", "nick", "phone", "avatar", "gender", "zodiac", "chinese_zodiac", "birthday", "alipay", "qq",
        "payment", "balance", "total", "qrcode", "jpush_registration_id")


class AccountDetailsSerializer(serializers.ModelSerializer):
    # gender = serializers.ChoiceField((('male', '男'), ('female', '女')))
    # favorites = serializers.HyperlinkedIdentityField(many=True, view_name='me-favorites-list', lookup_field='pk')
    avatar = serializers.ReadOnlyField(source='profile.avatar')
    zodiac = serializers.ReadOnlyField(source='profile.zodiac')
    birthday = serializers.ReadOnlyField(source='profile.birthday')
    nick = serializers.ReadOnlyField(source='profile.nick')
    name = serializers.ReadOnlyField(source='profile.name')
    gender = serializers.ReadOnlyField(source='profile.gender')
    chinese_zodiac = serializers.ReadOnlyField(source='profile.chinese_zodiac')

    class Meta:
        # depth = 1
        model = get_user_model()
        fields = ('url', 'nick', 'name', 'mobile', 'avatar', 'email', 'chinese_zodiac', 'zodiac', 'birthday', 'gender')

        # read_only_fields = ('email', 'username',)
        extra_kwargs = {
            # 'favorites': {'view_name': 'me-favorites-list', 'lookup_field': 'pk'},
            # 'profile': {'view_name': 'profile-detail', 'lookup_field': 'username', 'read_only': True, 'many': True},
        }


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        # fields = ('url', 'profile', 'address')
        # extra_kwargs = {
        # 'url': {'view_name': 'address-list', 'lookup_field': 'pk'},
        # 'profile': {'view_name': 'profile-detail', 'lookup_field': 'pk', 'read_only': True, 'many': True},
        # 'address': {'view_name': 'address-detail', 'lookup_field': 'pk', 'read_only': True, 'many': True},
        # }