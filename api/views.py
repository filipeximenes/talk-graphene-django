from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView as GrapheneGraphQLView



class GraphQLView(GrapheneGraphQLView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
