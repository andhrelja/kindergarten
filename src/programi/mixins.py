from django.http import HttpResponse
from django.core import serializers


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, queryset, **response_kwargs):
        """
        Returns a JSON response, transforming 'queryset' to make the payload.
        """
        return HttpResponse(
            self.get_serialized_queryset(queryset),
            content_type='application/json'
        )

    def get_serialized_queryset(self, queryset):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        return serializers.serialize('json', queryset)