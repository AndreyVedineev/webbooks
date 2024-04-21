# функция формирования списка авторов
def display_author(self):
    return ', '.join([author.last_name for author in
                                  self.author.all()])
