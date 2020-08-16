from django import forms


class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                               attrs={'id': 'new-todo-item', 'class': 'new-todo-item',
                                      'placeholder': 'Enter todo', 'name': 'todo'}
                           ))
