#Masukkan Nilai
nilai = float(input("Masukkan Nilai: "))

#Perhitungan Grade
if nilai >= 86 and nilai <= 100:
    grade = "(A) Kamu terlalu hebat"
elif nilai >= 76 and nilai <= 85:
    grade = "(B) Kamu hebat"
elif nilai >= 61 and nilai <= 75:
    grade = "(C) Kamu cukup hebat"
elif nilai >= 41 and nilai <= 60:
    grade = "(D) Kamu harus berusaha lagi"
else :
    grade = "(E) Mati aja bli"

#Output
print (f"Grade kamu: {grade}")
