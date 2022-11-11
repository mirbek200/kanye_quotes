from django.urls import path
from .views import (QuoteAPIView,
                    QuoteListAPIView,
                    QuoteDetailAPIView
                    )


urlpatterns = [path('get/', QuoteAPIView.as_view(), name='quote_get'),
               path('list/', QuoteListAPIView.as_view(), name='quote_list'),
               path('detail/<int:id>', QuoteDetailAPIView.as_view(), name='quote_detail'),

]
