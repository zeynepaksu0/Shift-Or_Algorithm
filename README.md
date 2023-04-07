Shift Or algoritması, metin içinde bir desenin aranması için kullanılan bir string eşleştirme algoritmasıdır.Algoritmanın çalışma prensibi, bit düzeyinde işlem yapmaya dayanır.
 Bu yüzden düşük maaliyetli donanımlarda ve sınırlı kaynaklara sahip sistemlerde kullanılmak üzere tasarlanmıştır.

Algoritma çalışırken aranmak istenilen desenin her bir karakteri icin bir bit maskesi oluşturur. 
Daha sonra desen sola dogru kaydırılır ve maske güncellenir. Metin içindeki karakterlerle karşılaştırılı ve eşleşme olmadığında tekrar sola kaydırılarak bu işlem tekrarlanmaya devam eder. Eger metinde aranılan desen yoksa bile hızlı çalışan bir algoritmadır. Çunku bit işlemlemlerihızlı ve basittir. Birden fazla deseni aramak için de kullnaılabilmektedir.

En iyi durumda: 
Aranılan desenin metinde hiçbir yerde bulunmadığı durumdur. Bu durumda, algoritma sadece metni bir kez tarar ve hiçbir sonuca ulaşamadığı için sabit kalır. Karmaşıklık O(n) olacaktır, burada n metin uzunluğunu temsil eder. Yani metin ne kadar kısa olursa o kadar hızlı sonuc verir.

En kötü durum:
Aranılan desenin metnin sonunda bulunduğu durumdur. Bu durumda, algoritma deseni metnin her pozisyonunda kontrol edecek ve her bir pozisyonda bit işlemleri yapacak. Karmaşıklık O(nm) olacaktır, burada n metin uzunluğunu ve m desen uzunluğunu temsil eder.

Ortalama durum: 
Aranılan desenin metnin herhangi bir yerinde bulunabileceği varsayılır. Bu durumda, Shift-Or algoritması yine de metnin her pozisyonunda bit işlemleri yapacak, ancak ortalama olarak birkaç pozisyonda duracaktır. Bu nedenle, ortalama durum karmaşıklığı O(nm) 'den daha düşük, ancak en kötü durum karmaşıklığından daha yüksek olacaktır. Ancak, Shift-Or algoritması diğer string eşleştirme algoritmalarına göre oldukça hızlıdır ve pratik uygulamalarda genellikle en iyi durumda veya ortalamada çalışır.



