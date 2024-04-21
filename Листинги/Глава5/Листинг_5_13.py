path('products/', views.products), # маршрут по умолчанию
path('products/<int:productid>/', views.products),
path('users/', views.users), # маршрут по умолчанию
path('users/<int:id>/<str:name>/', views.users),
