# на основе класса Company создаем объект firma с именем Электрон
firma = Company.objects.create(name=" Электрон")

# создание товара компании
firma.product_set.create(name="Samsung S20", price=42000)

# создание продукта с последующим добавлением его в БД
ipad = Product(name="iPad", price=34200)
# при добавлении необходимо указать параметр bulk =False
firma.product_set.add(ipad, bulk =False)

# исключает из компании все товары,
# при этом товары остаются в БД и не привязаны к компании
# работает, если в зависимой модели ForeignKey(Company, null = True)
# firma.product_set.clear()

# то же самое, только в отношении одного объекта
# ipad = Product.objects.get(name="iPad")
# firma.product_set.remove(ipad)
