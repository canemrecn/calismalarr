import cv2
#OpenCV kütüphanesini kullanmak için cv2 modülünü içe aktarır.
def dodge(kare, maske):
    return cv2.divide(kare, 255-maske, scale=256)
#dodge adında bir fonksiyon tanımlanır. Bu fonksiyon, verilen kare ve maske görüntülerini
# kullanarak bir işlem gerçekleştirir ve sonucunu döndürür.
kamera = cv2.VideoCapture(0)
#kamera adında bir değişken oluşturulur ve VideoCapture sınıfını kullanarak bir video
# kaynağına bağlanır. Bu durumda 0, yerel bir kamerayı temsil eder.
while True:
    kare = kamera.read()[-1]
    image = kare
    gri = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_inv = 255 - gri
    blur = cv2.GaussianBlur(gri, ksize=(11, 11), sigmaX=0, sigmaY=0)
    yeni = dodge(gri, blur)
#Sonsuz bir döngü oluşturulur. Her döngüde, kameradan bir kare alınır. Ardından, bu kare üzerinde
# bazı görüntü işleme adımları gerçekleştirilir:
#İmage adlı değişkene karenin kendisi atanır.
#gri adlı değişkene, image'in renkli (BGR) formattan gri formata dönüştürülmüş hali atanır.
#gray_inv adlı değişkene, gri görüntüsünün tersi alınmış halini elde eder.
#blur adlı değişkene, gri görüntüsüne Gaussian bulanıklaştırma uygulanmış halini elde eder.
#yeni adlı değişkene, gri görüntüsü ile blur görüntüsü arasında dodge fonksiyonuyla birleştirme
# işlemi yaparak yeni bir görüntü oluşturur.
    arkaplan = cv2.imread('resimler/hpasa.jpeg')
    if arkaplan is None:
        print("Dosya okunamadı")
        break
    arkaplan = cv2.cvtColor(arkaplan, cv2.COLOR_BGR2GRAY)
    arkaplan = cv2.resize(arkaplan,(yeni.shape[1], yeni.shape[0]))
    yeni = cv2.multiply(yeni, arkaplan, scale=1.10/256.0)
    cv2.imshow('yeni', yeni)
#Belirli bir dosya yolundan (resimler/hpasa.jpeg) arkaplan görüntüsü okunur. Eğer dosya okunamazsa
# bir hata mesajı yazdırılır ve döngüden çıkılır. Ardından, arkaplan
    k = cv2.waitKey(1) & 0xFF
#Kullanıcının bir tuşa basmasını bekler ve k değişkenine basılan tuşun değerini atar. waitKey(1)
# fonksiyonu 1 milisaniye boyunca tuşa basılmasını bekler.
    if k == 27 or k == ('q'):
#Eğer basılan tuşun değeri ESC tuşunun ASCII değeri (27) veya q tuşunun ASCII değeri ile eşleşiyorsa:
        break
#Döngüden çıkılır ve program sonlanır.
kamera.release()
#Kamera kaynağı serbest bırakılır. Bu, kamera kaynağının kullanımını tamamladıktan sonra kaynağı
# serbest bırakmak için yapılır.
cv2.destroyAllWindows()
#Açık olan tüm penceler kapatılır. Bu, program sonlandığında açık kalan pencerelerin kapatılmasını
# sağlar ve sistem kaynaklarının doğru bir şekilde serbest bırakılmasını sağlar.