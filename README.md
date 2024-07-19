# TC Kimlik No Doğrulama ve Bulma Modülü

Bu modül, TC Kimlik Numarası (TCKN) ile ilgili işlemleri gerçekleştirmek için tasarlanmıştır. Aşağıdakileri sağlar:

* **TCKN Doğrulama:** Luhn algoritması kullanarak bir TCKN'nin formatını ve kontrol rakamını doğrular
* **Bir Sonraki Geçerli TCKN:** Verilen bir TCKN'den sonraki ilk geçerli TCKN'yi bulur
* **Belirli Bir Aralıktaki Geçerli TCKN Sayısı:** Belirli bir aralıktaki geçerli TCKN'lerin sayısını hesaplar veya listesini verir

## Kullanım

Modülü kullanmak için:

1. `TCKN_class` sınıfını kodunuza ekleyin.
2. Sınıfın `tc_check`, `tc_next` ve `which_tc_between` fonksiyonlarını kullanarak TCKN ile ilgili işlemleri gerçekleştirin.

**Örnek Kullanım:**

```python
from tckn_module import TCKN_class

tckn = TCKN_class()

# TCKN doğrulaması
tc_no = 12345678901
sonuc = tckn.tc_check(tc_no)
print(f"TC Kimlik No kontrolu: {tc_no} {sonuc}.")

# Bir sonraki geçerli TCKN
baslangic_tc = 12345678900
sonuc = tckn.tc_next(baslangic_tc)
print(f"{baslangic_tc}'den bir sonraki geçerli TC Kimlik No: {sonuc[0]}")

# Belirli bir aralıktaki geçerli TCKN sayısı
baslangic_tc = 10000000000
bitis_tc = 10000001000
sonuc = tckn.which_tc_between(baslangic_tc, bitis_tc, get_list=True)
print(f"Belirtilen aralıktaki ({baslangic_tc}-{bitis_tc}) geçerli TC Kimlik Numarası sayısı: {sonuc[0]}\nNumaralar: {sonuc[1]}")
```

## Kurulum
Modülü kullanmak için aşağıdaki adımları izleyin:

1. tckn_module.py dosyasını indirin ve projenize ekleyin.
2. Kodunuzda from tckn_module import TCKN_class satırını ekleyin.
3. Yukarıdaki örneklerde gösterildiği gibi işlevleri kullanın.
### Python Version:

This module requires **Python 3.9** or above to run properly.

## Uyarılar

* Herhangi bir veri merkezinden kontrol sağlanmamaktadır.
* Kimlik numaralarının varlığını değil kurallara uygunluğunu test etme amaçlıdır.
