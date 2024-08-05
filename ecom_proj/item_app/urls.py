from django.urls import path
from .views import All_items, Item_by_category, An_item


urlpatterns = [
    path("", All_items.as_view(), name="all_items"),
    path("category/<str:category>/", Item_by_category.as_view(), name="items_by_category"),
    path("<int:item_id>/", An_item.as_view(), name="an_item")
]
