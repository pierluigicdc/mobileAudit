from rest_framework import serializers
from app.models import *


class ScanSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Scan
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on', 'user', 'status', 'progress', 'apk_name', 'findings', 'file_size', 'md5', 'sha1', 'sha256', 'package', 'icon', 'version_code', 'version_name', 'min_sdk_version', 'max_sdk_version', 'target_sdk_version', 'effective_target_sdk_version' ,'manifest')

          
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on', 'user')


class FindingSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Finding
        fields = '__all__'
        read_only_fields = ('created_on', 'updated_on', 'user')