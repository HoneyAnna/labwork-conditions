year = input("введите год ")
if year.isdigit():
    if len(year) == 4:
        year = int(year)
        if year >= 1000 and year <= 9999:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                print(f"{year} високосный год")
                
            else:
                print(f"{year} не високосный")
                
        else:
            print("год не входит в диапазон")
            
    else:
        print("длина не равна 4")
else:
    print("год не число")
