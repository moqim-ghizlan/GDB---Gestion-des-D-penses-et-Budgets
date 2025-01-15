from .models import Spent

def functions(request):
    return {
        'get_all_months' : Spent.MONTHS,
        'current_month' : Spent.CURRENT_MONTH,
        'current_month_display' : Spent.MONTHS[Spent.CURRENT_MONTH - 1][1],
    }



