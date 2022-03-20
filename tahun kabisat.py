# hari tiap bulan
bulan_hari = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def kabisat(tahun):
    #apabila tahun kabisat akan return True
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)
def feb_kabisat(tahun,bulan):
    if not 0 < bulan < 13:
        return "salah bulan"
    if kabisat(tahun) and bulan == 2:
        return 29
    return bulan_hari[bulan]

print(feb_kabisat(2020,2))
