from rest_framework.serializers import ModelSerializer, StringRelatedField 
from base.models import Product, Store

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','brand','price','description']



class StoreSerializer(ModelSerializer):
    class Meta:
        
        
        model = Store
        fields = ['city','street','owner','contact','products']
        depth = 1