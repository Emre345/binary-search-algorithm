def binary_search_introduction():  # O(log n) - Fonksiyonun toplam yürütme hızı
    """
    İkili arama algoritması kullanarak kendimi tanıtan fonksiyon
    """
    # Kişisel özelliklerim bir sözlük içinde (anahtar-değer çiftleri)
    ben = {  # O(1) - Sabit zamanlı bir atama işlemi
        "ad": "Emre DEMIRKAYA",  # O(1) - Sabit zamanlı bir atama
        "okul":"Beykoz Üniversitesi",  # Bir anahtar-değer çifti olarak okul bilgisini sözlüğe ekler
        "bölüm": "Yazılım Mühendisliği",  # O(1) - Sabit zamanlı bir atama
        "sınıf": 2,  # O(1) - Sabit zamanlı bir atama
        "ilgi_alanları": ["Veri Yapıları", "Algoritmalar", "Yapay Zeka"],  # O(1) - Sabit boyutta liste oluşturma
        "güçlü_yönler": ["Analitik düşünme", "Problem çözme", "Takım çalışması"],  # O(1) - Sabit boyutta liste oluşturma
        "diller": ["Python", "Java", "C++", "JavaScript"],  # O(1) - Sabit boyutta liste oluşturma
        "hedefler": ["Mezuniyet sonrası iyi bir iş bulmak", "Açık kaynak projelere katkıda bulunmak"]  # O(1) - Sabit boyutta liste oluşturma
    }
    
    # Başlangıç mesajı
    print(f"Merhaba! Ben {ben['ad']} {ben['okul']} {ben['bölüm']} {ben['sınıf']}. sınıf öğrencisiyim.")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Sözlükten ad, okul, bölüm ve sınıf bilgilerini alarak karşılama mesajını ekrana yazdırır
    
    print("İkili arama algoritması kullanarak kendimi tanıtacağım.\n")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Fonksiyonun amacını belirten bir mesajı ekrana yazdırır ve bir satır boşluk bırakır
    
    # İlgi alanlarımı arayalım - ikili arama algoritmasını kullanarak
    print("İlgi alanlarımı aramak için ikili arama algoritmasını kullanıyorum:")  # O(1) - Sabit zamanlı yazdırma işlemi
    # İlgi alanlarını arayacağını belirten bir mesajı ekrana yazdırır
    
    # İlgi alanlarımı alfabetik sıraya dizelim (binary search için gerekli)
    ilgi_alanlarim = sorted(ben["ilgi_alanları"])  # O(k log k) - k, ilgi alanları sayısı (burada sabit)
    # "ben" sözlüğündeki "ilgi_alanları" anahtarına karşılık gelen listeyi alfabetik olarak sıralar ve ilgi_alanlarim değişkenine atar
    
    print(f"Sıralanmış ilgi alanlarım: {ilgi_alanlarim}")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Sıralanmış ilgi alanlarını ekrana yazdırır
    
    # Aramak istediğim ilgi alanı
    aranan_ilgi = "Algoritmalar"  # O(1) - Sabit zamanlı bir atama
    # Aranacak ilgi alanını "Algoritmalar" olarak belirler ve aranan_ilgi değişkenine atar
    
    # İkili arama algoritmasının başlangıcı
    sol = 0  # O(1) - Sabit zamanlı bir atama
    # İkili arama için sol sınırı 0 olarak belirler
    
    sag = len(ilgi_alanlarim) - 1  # O(1) - Sabit zamanlı bir işlem (listenin uzunluğunu hesaplama ve çıkarma)
    # İkili arama için sağ sınırı, listenin uzunluğunun bir eksiği olarak belirler
    
    bulundu = False  # O(1) - Sabit zamanlı bir atama
    # İlgi alanının bulunup bulunmadığını takip etmek için bulundu değişkenini False olarak başlatır
    
    adim_sayisi = 0  # O(1) - Sabit zamanlı bir atama
    # İkili arama sırasında atılan adım sayısını takip etmek için adim_sayisi değişkenini 0 olarak başlatır
    
    # İkili arama döngüsü
    while sol <= sag and not bulundu:  # O(log n) - n, dizinin eleman sayısı
    # Sol sınır sağ sınırdan küçük veya eşit olduğu ve aranan ilgi alanı henüz bulunmadığı sürece döngüyü çalıştırır
    
        adim_sayisi += 1  # O(1) - Sabit zamanlı aritmetik işlem
        # Her döngü iterasyonunda adım sayısını bir arttırır
        
        orta = (sol + sag) // 2  # O(1) - Sabit zamanlı aritmetik işlem
        # Sol ve sağ sınırların ortasındaki indeksi hesaplar (tam bölme işlemi)
        
        print(f"Adım {adim_sayisi}: Bakılan ilgi: '{ilgi_alanlarim[orta]}'")  # O(1) - Sabit zamanlı yazdırma işlemi
        # Mevcut adım numarasını ve o adımda kontrol edilen ilgi alanını ekrana yazdırır
        
        if ilgi_alanlarim[orta] == aranan_ilgi:  # O(1) - Sabit zamanlı karşılaştırma
        # Ortadaki ilgi alanının aranan ilgi alanıyla aynı olup olmadığını kontrol eder
        
            bulundu = True  # O(1) - Sabit zamanlı bir atama
            # Aranan ilgi alanı bulunduğunda bulundu değişkenini True olarak ayarlar
            
            print(f"'{aranan_ilgi}' ilgi alanımı {adim_sayisi}. adımda buldum!")  # O(1) - Sabit zamanlı yazdırma işlemi
            # Aranan ilgi alanının bulunduğunu ve kaç adımda bulunduğunu belirten bir mesajı ekrana yazdırır
            
            print(f"Bu da benim {aranan_ilgi} konusuna olan ilgimi gösteriyor.")  # O(1) - Sabit zamanlı yazdırma işlemi
            # Aranan ilgi alanına olan ilgiyi belirten bir mesajı ekrana yazdırır
            
            print("Bu algoritma gibi ben de problemleri çözerken sistematik ilerlerim.")  # O(1) - Sabit zamanlı yazdırma işlemi
            # Kişisel çalışma tarzıyla algoritma arasında bağlantı kuran bir mesajı ekrana yazdırır
        
        elif ilgi_alanlarim[orta] < aranan_ilgi:  # O(1) - Sabit zamanlı karşılaştırma
        # Ortadaki ilgi alanının aranan ilgi alanından alfabetik olarak önce gelip gelmediğini kontrol eder
        
            sol = orta + 1  # O(1) - Sabit zamanlı aritmetik işlem
            # Aranan ilgi alanı ortadaki ilgi alanından alfabetik olarak sonra geliyorsa, sol sınırı ortanın bir sonraki indeksine ayarlar
            
            print(f"  İlgi alanım daha sonra geliyor, {sol}-{sag} aralığına bakıyorum")  # O(1) - Sabit zamanlı yazdırma işlemi
            # Arama aralığının sağ yarısına bakılacağını belirten bir mesajı ekrana yazdırır
        
        else:  # O(1) - Sabit zamanlı koşul kontrolü
        # Ortadaki ilgi alanı, aranan ilgi alanından alfabetik olarak sonra geliyorsa
        
            sag = orta - 1  # O(1) - Sabit zamanlı aritmetik işlem
            # Sağ sınırı ortanın bir önceki indeksine ayarlar
            
            print(f"  İlgi alanım daha önce geliyor, {sol}-{sag} aralığına bakıyorum")  # O(1) - Sabit zamanlı yazdırma işlemi
            # Arama aralığının sol yarısına bakılacağını belirten bir mesajı ekrana yazdırır
    
    # Algoritma tamamlandıktan sonra
    print("\nİkili arama algoritması ve benim özelliklerimin karşılaştırılması:")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Bir satır boşluk bırakarak ikili arama algoritmasının özellikleri ve kişisel özellikler hakkında bilgi verileceğini belirten bir başlığı ekrana yazdırır
    
    print("1. İkili arama algoritması gibi ben de problemlere sistematik yaklaşırım")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Kişisel problem çözme tarzını açıklayan bir maddeyi ekrana yazdırır
    
    print("2. Her adımda problemi küçülterek (sol-sağ aralığını daraltarak) çözüme ulaşırım")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Kişisel problem çözme stratejisini açıklayan bir maddeyi ekrana yazdırır
    
    print("3. Logaritmik karmaşıklıkla çalışırım - yani zamanımı verimli kullanırım")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Kişisel verimlilik anlayışını açıklayan bir maddeyi ekrana yazdırır
    
    print(f"4. {len(ilgi_alanlarim)} adet ilgi alanım olsa da, aradığımı sadece {adim_sayisi} adımda bulabildim")  # O(1) - Sabit zamanlı yazdırma işlemi
    # İkili arama algoritmasının verimliliğini gösteren bir maddeyi ekrana yazdırır
    
    print("5. Düzenli ve planlı çalışmayı severim (dizinin sıralı olması gibi)")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Kişisel çalışma tarzını açıklayan bir maddeyi ekrana yazdırır
    
    # Programlama dillerini ve yetkinliklerimi karşılaştıralım
    print("\nPROGRAMLAMA DİLLERİNDEKİ YETKİNLİKLERİM:")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Bir satır boşluk bırakarak programlama dillerindeki yetkinlikler hakkında bilgi verileceğini belirten bir başlığı ekrana yazdırır
    
    dil_yetkinlikleri = {  # O(1) - Sabit boyutta sözlük oluşturma
        "Python": 65,  # Yüzde cinsinden yetkinlik - O(1) - Sabit zamanlı bir atama
        "Java": 55,  # O(1) - Sabit zamanlı bir atama
        "C++": 65,  # O(1) - Sabit zamanlı bir atama
        "JavaScript": 50  # O(1) - Sabit zamanlı bir atama
    }
    # Programlama dillerindeki yetkinlik düzeylerini yüzde cinsinden bir sözlük olarak tanımlar
    
    # Dilleri yetkinliğe göre sıralama
    diller_sirali = sorted(dil_yetkinlikleri.items(), key=lambda x: x[1], reverse=True)  # O(m log m) - m, dil sayısı (burada sabit)
    # Programlama dillerini yetkinlik düzeyine göre azalan şekilde sıralar. Bu adım, her dil-yetkinlik çiftini içeren bir tuple listesi döndürür
    
    # İkili arama mantığıyla yetkinliklerimi gösterelim
    print("Yetkinliklerim (ikili arama mantığıyla):")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Yetkinliklerin gösterileceğini belirten bir mesajı ekrana yazdırır
    
    i = 0  # O(1) - Sabit zamanlı bir atama
    # Döngü değişkenini 0 olarak başlatır
    
    while i < len(diller_sirali):  # O(m) - Dil sayısı kadar döngü (burada sabit)
    # Sıralanmış diller listesindeki her bir eleman için döngüyü çalıştırır
    
        dil, yetkinlik = diller_sirali[i]  # O(1) - Sabit zamanlı bir atama
        # Sıralanmış listedeki mevcut elemanın dil ve yetkinlik değerlerini ayrı değişkenlere atar
        
        # İkili arama algoritmasındaki gibi, yetkinlik seviyemi görselleştirelim
        bar_size = 20  # O(1) - Sabit zamanlı bir atama
        # İlerleme çubuğunun toplam uzunluğunu 20 karakter olarak belirler
        
        filled = int((yetkinlik / 100) * bar_size)  # O(1) - Sabit zamanlı aritmetik işlem
        # Yetkinlik yüzdesine göre doldurulacak karakter sayısını hesaplar
        
        bar = '[' + '#' * filled + ' ' * (bar_size - filled) + ']'  # O(1) - Sabit zamanlı string oluşturma (bar_size sabittir)
        # İlerleme çubuğunu oluşturur: '#' karakteriyle dolu kısım ve boşluklarla dolu kısım
        
        print(f"{dil:12} {bar} {yetkinlik}%")  # O(1) - Sabit zamanlı yazdırma işlemi
        # Dil adını, ilerleme çubuğunu ve yetkinlik yüzdesini ekrana yazdırır (dil adı için 12 karakterlik alan ayrılır)
        
        i += 1  # O(1) - Sabit zamanlı aritmetik işlem
        # Döngü değişkenini bir arttırarak bir sonraki dile geçer
    
    # Kişisel hedeflerimi gösterelim
    print("\nHEDEFLERİM:")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Bir satır boşluk bırakarak hedefler hakkında bilgi verileceğini belirten bir başlığı ekrana yazdırır
    
    for i, hedef in enumerate(ben["hedefler"], 1):  # O(h) - h, hedef sayısı (burada sabit)
    # "ben" sözlüğündeki "hedefler" listesindeki her bir hedef için döngüyü çalıştırır, i değişkeni 1'den başlar
    
        print(f"{i}. {hedef}")  # O(1) - Sabit zamanlı yazdırma işlemi
        # Hedefin numarasını ve açıklamasını ekrana yazdırır
    
    # Algoritmanın karmaşıklık analizi ve kişisel yansıma
    print("\nALGORİTMA KARMAŞIKLIK ANALİZİ VE KİŞİSEL YANSIMA:")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Bir satır boşluk bırakarak algoritma analizi ve kişisel yansıma hakkında bilgi verileceğini belirten bir başlığı ekrana yazdırır
    
    print("Zaman Karmaşıklığı: O(log n) - Her adımda arama alanını yarıya indiririm")  # O(1) - Sabit zamanlı yazdırma işlemi
    # İkili arama algoritmasının zaman karmaşıklığını ve kişisel çalışma tarzı arasındaki bağlantıyı açıklayan bir mesajı ekrana yazdırır
    
    print("Alan Karmaşıklığı: O(1) - Verimli çalışır, minimum kaynak kullanırım")  # O(1) - Sabit zamanlı yazdırma işlemi
    # İkili arama algoritmasının alan karmaşıklığını ve kişisel kaynak kullanım tarzı arasındaki bağlantıyı açıklayan bir mesajı ekrana yazdırır
    
    print("\nBu algoritma benim çalışma tarzımı yansıtıyor: Sistematik, verimli ve sonuç odaklı.")  # O(1) - Sabit zamanlı yazdırma işlemi
    # Bir satır boşluk bırakarak algoritma ve kişisel çalışma tarzı arasındaki bağlantıyı özetleyen bir mesajı ekrana yazdırır

# Programı çalıştır
if __name__ == "__main__":  # O(1) - Sabit zamanlı koşul kontrolü
    # Bu dosyanın doğrudan çalıştırılıp çalıştırılmadığını kontrol eder
    
    binary_search_introduction()  # O(log n) - Fonksiyonu çağırma (fonksiyonun kendi karmaşıklığı)
    # binary_search_introduction fonksiyonunu çağırarak programı başlatır

# Toplam Yürütme Hızı: O(log n)
# Algoritmanın karmaşıklık analizi: O(log n) - İkili arama algoritması logaritmik zamanda çalışır