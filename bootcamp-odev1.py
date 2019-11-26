#1 Döngüylede yapılabilir. 
bitcoin = 1000

gunlukArtıs = bitcoin * 12 / 100
bitcoin1 = bitcoin + gunlukArtıs
gunlukArtıs = bitcoin1 * 12 / 100
bitcoin1 = bitcoin1 + gunlukArtıs
gunlukArtıs = bitcoin1 * 12 / 100
bitcoin1 = bitcoin1 + gunlukArtıs
gunlukArtıs = bitcoin1 * 12 / 100
bitcoin1 = bitcoin1 + gunlukArtıs
gunlukArtıs = bitcoin1 * 12 / 100
bitcoin1 = bitcoin1 + gunlukArtıs
gunlukArtıs = bitcoin1 * 12 / 100
bitcoin1 = bitcoin1 + gunlukArtıs
gunlukArtıs = bitcoin1 * 12 / 100
bitcoin1 = bitcoin1 + gunlukArtıs
print(bitcoin1)

#While döngüsü ile
#
# x = 0
# bitcoin = 1000
# gunlukArtis = bitcoin * 12 / 100
# bitcoin1 = bitcoin + gunlukArtis
# 
# while (x < 6):
#     gunlukArtis = bitcoin1 * 12 / 100
#     bitcoin1 = bitcoin1 + gunlukArtis
#     x += 1
# print(bitcoin1)



#2
metin = 'Hafta başında {} dolarlık bitcoin aldığımızda günde ortalama %12 kazançla, bir hafta sonunda {:.2f} dolar kazanırdık.'
print(metin.format(bitcoin,bitcoin1))

#3

dosyaAdı = input('Dosya adı: ')
print("{}.py".format(dosyaAdı))