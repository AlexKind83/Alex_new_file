total_sales = [52_000, 51_000, 48_000]
production_cost = [46_800, 45_900, 43_200]
month = ["January =", "February =", "March ="]

for a, b, c in zip(total_sales, production_cost, month):
    res = (a - b)
    print("Общая прибыль в", c, res)
