from django.forms import ModelForm

from accounting_tools.models import ExpenseClaimLine, CashBookLine


class ExpenseClaimLineForm(ModelForm):

    class Meta:
        model = ExpenseClaimLine
        exclude = ('expense_claim', 'order',)


class CashBookLineForm(ModelForm):

    class Meta:
        model = CashBookLine
        exclude = ('cashbook', 'order',)
