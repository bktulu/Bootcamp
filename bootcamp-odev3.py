# 1-Kullanıcıdan Santigrat ya da Fahrenheit olarak sıcaklık değerini alacak ve diğer sıcaklık birimine çevirecek bir kod yazın.
print("Santigrat girecekseniz 1'i, Fahrenheit girecekseniz 2'yi seçiniz.")

x = int(input('Değeri giriniz: '))

if x == 1:
    C = int(input('Santigrat: '))
    F = (9/5)*C + 32
    print(F)

elif x == 2:
    F = int(input('Fahrenheit: '))
    C = (5/9) * (F - 32)
    print(C)

# 2-Kullanıcının girdiği kelimeyi ters çeviren bir kod yazınız.
# kelime = input('Kelime: ')
# print('Kelimenin tersten yazılışı: ',kelime[::-1])

# 3-1'den 50'ye kadar olan Fibonacci sayılarından oluşan bir liste oluşturun. İlk iki Fibonacci sayısı 1'dir. Sonraki sayılar, önceki iki sayının toplamıdır.
# x=1
# y=1
# print(x)
# print(y)

# i = 2
# while i <= 50:
#     eski_x = x
#     eski_y = y
#     x = eski_y
#     y = eski_x + eski_y
#     print(y)
#     i += 1

# 4-Girilen bir sayı için çarpım tablosunu yazdırın.
# sayi = int(input('Bir sayi giriniz: '))
# for i in range(0,10):
#     print(sayi," x ",i," = ",sayi * i)

# 5-List comprehension kullanarak, 1'den 20'ye kadar tek sayıların karesini, çift sayıların küpünü içeren bir liste oluşturun.
# my_list = [x**2 if x % 2 == 1 else x**3 for x in range(1,20)]
# print(my_list)