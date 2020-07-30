import calendar
import datetime

hariini = datetime.date.today()
haridibulanini = calendar.monthrange(hariini.year, hariini.month)[1]
sisaharidibulanini = haridibulanini - hariini.day
tanggalmulai = hariini + datetime.timedelta(days=sisaharidibulanini + 1)
tanggalakhir = tanggalmulai
stoptanggal = datetime.date(2050, 8, 30)


deposito = 70000
bunga = 0.01
hariini = hariini.strftime("%B %d, %Y")
print(f"Tanggal = {hariini} | Deposito = {int(deposito)}")
deposito += deposito * sisaharidibulanini * bunga / 12 / haridibulanini
tanggalmulai = tanggalmulai.strftime("%B %d, %Y")

print(f"Tanggal = {tanggalmulai} | Deposito = {int(deposito)}")

while stoptanggal > tanggalakhir:
    haridibulanini = calendar.monthrange(tanggalakhir.year, tanggalakhir.month)[1]
    tanggalakhir = tanggalakhir + datetime.timedelta(days=haridibulanini)
    bungaperbulan = deposito * bunga / 12
    deposito += bungaperbulan
    deposito = round(deposito, 0)
    tanggalterformat = tanggalakhir.strftime("%B %d, %Y")

    print(f"Tanggal = {tanggalterformat} | Deposito = {int(deposito)}")
