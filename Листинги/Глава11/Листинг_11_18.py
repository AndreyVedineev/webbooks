@property
def is_overdue(self):
    if self.due_back and date.today() > self.due_back:
        return True
    return False
