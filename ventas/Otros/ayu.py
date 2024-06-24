from datetime import datetime
ventas=[ #folio,    fecha,  id, cantidad,   total
    [10001,"10-06-2024","l001",2,25000],
    [10002,"10-06-2024","l002",3,81120]]

def rescatar_folio():
    folio=0
    for valor in ventas:
        folio=valor[0]
    return folio

date =datetime.now()
day_month_year=date.strftime("%d-%m-%Y")
print(day_month_year)