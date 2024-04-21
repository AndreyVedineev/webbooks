def products(request, productid):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id, name):
    output = "<h2>Пользователь</h2><h3>id:" \
             " {0} Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)
