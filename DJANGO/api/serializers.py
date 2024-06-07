from rest_framework import serializers
from api.models import CodeExplainer
from api.utils import send_code_to_api


class CodeExplainSerializers(serializers.ModelSerializer):
    class Meta:
        model = CodeExplainer
        fields = ['id', "_input","system_role", "_output"]
        extra_kwargs = {
            "_output": {"read_only": True}
        }

    def create(self, validated_data):
        co = CodeExplainer(**validated_data)
        print(validated_data)
        _output = send_code_to_api(validated_data["_input"],validated_data["system_role"] )
        co._output = _output
        co.save()
        return co
