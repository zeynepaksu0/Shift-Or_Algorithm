def shift_or_search(kelime, dosya_adi): #kelimenin metide kac kez gectigini arayan ve shift or algoritmasını kullanan bir fonksiyon olusturuyoruz
    #shift-or algoritmasıı kullanarak hesaplamaların hepsini önceden yapıyoruz
    maske = {} #kelimenin her harfi icin bir maske olusturuyoruz
    bit = 1 
    for harf in kelime:
        maske[harf] = bit
        bit <<= 1

    #dosyayı açıp tüm kelimeleri taratiyoruz
    sayac = 0
    with open(dosya_adi, "r") as dosya:
        for satir in dosya:
            #satiri maskeye göre ayarlatiyoruz
            satir_maske = 0
            for harf in satir:
                satir_maske = (satir_maske << 1 | 1) & maske.get(harf, 0)
                if satir_maske & (1 << len(kelime) - 1):
                    sayac += 1
    return sayac

# kullanıcıdan metinde aramak istedigi 5 tane kelime girmesini istiyoruz
kelimeler = []
for i in range(5): # siz aramak istediginiz kelime sayısını kendiniz kısıtlandırabilirsiniz
    kelime = input(f"Lütfen {i+1}. kelimeyi giriniz: ")
    kelimeler.append(kelime)

# Dosya adını belirle
dosya_adi = "alice_in_wonderland.txt" #dosyaanın icerigini ve burdaki adını degistirerek istediginiz metin üzerinde calıstırtabilirsiniz

# Her kelimenin kaç kez geçtiğini saydırdık
for kelime in kelimeler:
    sayac = shift_or_search(kelime, dosya_adi)
    if sayac > 0:
        print(f" Aradığınız'{kelime}' kelimesi {sayac} kez geçiyor.")
    else:
        print(f" Aradığınız'{kelime}' kelimesi maalesef metinde geçmiyor.")