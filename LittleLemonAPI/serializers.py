from rest_framework import serializers

class MenuItemSerializers(serializers.ModelSerializer):
    
    title=serializers.CharField(max_length=255,db_index=True)
    price=serializers.DecimalField(max_digits=6,decimal_places=2,db_index=True)
    featured=serializers.BooleanField(db_index=True)
  