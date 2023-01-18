def get_totals(orders):
   return [x['total'] for x in orders]

def calc_total(totals):
   return sum(totals)