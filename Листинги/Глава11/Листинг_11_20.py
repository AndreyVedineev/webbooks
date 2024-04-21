from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    # Универсальный класс представления списка книг,
    # находящихся в заказе у текущего пользователя
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user).filter(
            status__exact='2').order_by('due_back')
