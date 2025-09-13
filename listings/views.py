from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer

@api_view(['GET'])
def api_overview(request):
    """
    API Overview endpoint
    """
    api_urls = {
        'API Overview': '/api/overview/',
        'Listings': '/api/listings/',
        'Admin': '/admin/',
        'Swagger Documentation': '/swagger/',
        'ReDoc Documentation': '/redoc/',
    }
    return Response(api_urls)

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer