from rest_framework import routers, serializers, viewsets
from .models import JobPosting, Category


class JobPostingSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField(many=False, read_only = True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = JobPosting
        fields = [
            'title',
            'company',
            'id',
            'description',
            'summary',
            'logo_url',
            'category',
            'category_id',
            'posted_date',
        ]
        
        
class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    
     
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'title',
            'id'
        ]
        
        
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

