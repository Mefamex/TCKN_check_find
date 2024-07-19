# -*- coding: utf-8 -*-
# Created on Friday, July 19 15:30:00 2024
# @author: mefamex
print("\n","#" * 30 ,"""  Module loading...
          TC Kimlik No Doğrulama ve Tekrarlama

Bu modül, bir TC Kimlik Numarası'nın formatını doğrular ve bir sonraki geçerli
numarayı bulur. Ayrıca bir aralıktaki geçerli numaraları arama işlevi de sağlar.

Özellikler:
- Luhn algoritması kullanarak TC Kimlik No doğrulama
- Bir sonraki geçerli TC Kimlik No'yu bulma
- Belirli bir aralıktaki geçerli TC Kimlik Numaralarını bulma.

Harici kütüphaneler:
- time.sleep

Uyarı:
- Herhangi bir veri merkezinden kontrol sağlanmamaktadır
- Kimlik numaralarının varlığını değil kurallara uygunluğunu test etme amaçlıdır\n
##################################################################################""",sep="")

from time import sleep
from typing import List, Union
sleep(1)
class TCKN_class:
    """TC Kimlik No ile ilgili işlemleri yönetir."""
    def tc_check(self, tc: int) -> bool or str:
        """Bir TC Kimlik No'nun formatını ve kontrol rakamını doğrular.
        Args:
            tc_no (int): Doğrulanacak TC Kimlik No.
        Returns:
            str:  11 haneli değil veya sayılardan oluşmuyorsa: Invalid Format
            bool: Numara geçerliyse: True, değilse: False.
            """
        if not isinstance(tc, int) or len(str(tc)) != 11: return "TC, int türünde 11 haneli olmalıdır"
        tc=list(map(int, str(tc)))
        A, B = tc[0] + tc[2] + tc[4] + tc[6] + tc[8], tc[1] + tc[3] + tc[5] + tc[7]
        if (A * 7 - B) % 10 != tc[9] or (A + B + tc[9]) % 10 != tc[10]: return False
        return True


    def tc_next(self, tc: int, kontrol_sayisi: bool = False) -> List[int] or List[int, int] or None:
        """Verilen numaradan sonraki ilk geçerli TC Kimlik No'yu bulur.
        Args:
            tc (int): Başlangıç TC Kimlik No.
            kontrol_sayisi (bool, optional): Kontrol edilen TC Kimlik Nolarının sayısını
                                            döndürür (varsayılan: False).
        Returns:
            - list[int]:      ('kontrol_sayisi'='False') Bir sonraki geçerli TC Kimlik No .
            - list[int, int]: ('kontrol_sayisi'='True') (Bir sonraki geçerli TC Kimlik No, kontrol
                                edilen TC Kimlik Nolarının sayısı) .
            - None:           Bir sonraki geçerli TC Kimlik No bulunmazsa.
            - TypeError: 'tc' parametresi 'int' türünde değilse veya 'tc' parametresinin uzunluğu 11 değilse."""

        if not isinstance(tc, int) or len(str(tc)) != 11: raise TypeError("TC, int türünde 11 haneli olmalıdır")
        old = tc + 0
        while len(str(tc))==11:
            tc+=1
            if self.tc_check(tc) is True: break
        if tc>old and self.tc_check(tc):        
            if kontrol_sayisi: return [tc, old-tc]
            return [tc]
        return None


    def which_tc_between(self, tc, end, get_list=False):
        """Bu fonksiyon, 'tc' değerinden başlayarak 'end' değerine kadar olan
        geçerli TC kimlik numaralarını sırayla geçerek sayısını veya listesini döndürür.
        Args:
            tc (str): Başlangıç TC kimlik numarası (kapsayıcı).
            end (str): Bitiş TC kimlik numarası (kapsam dışı).
            get_list (bool, opsiyonel): True ise TC kimlik numaralarının listesini, 
                                        False ise sayısını döndürür (varsayılan: False).
        Returns:
            Union[int, Tuple[int, int]:
                - int:             ('get_list'='False') 'tc' ve 'end' arasındaki geçerli TC kimlik numaralarının sayısı
                - Tuple[int, int]: ('get_list'='True') [geçerli TC kimlik numaralarının sayısı, TC kimlik numaraları listesi]"""

        if get_list is True:
            tc_list=[]
            while tc < end:
                tc = self.tc_next(tc)[0]
                tc_list.append(tc)
            return [len(tc_list),tc_list]
        else:
            count = 0
            while tc < end:
                tc = self.tc_next(tc)[0]
                count += 1
            return count



if __name__ == "__main__":

    tckn = TCKN_class()

    while True:
        print("\nMenü Seçenekleri:")
        print("1. TC Kontrol")
        print("2. Bir Sonraki Geçerli TC")
        print("3. Belirli Bir Aralıktaki Geçerli TC Sayısı")

        secim = input("Seçiminizi giriniz (1-3): ")

        try:
            secim = int(secim)
            if  not 1 <= secim <= 3:
                print("Geçersiz seçim. Lütfen 1-4 arasında bir değer giriniz.")
                continue
        except ValueError: print("Geçersiz giriş. Lütfen bir sayı giriniz.")

        if secim == 1:
            while True:
                try:
                    tc_no = int(input("\nTC Kimlik No giriniz: "))
                    break
                except ValueError:print("Geçersiz giriş. Lütfen bir sayı giriniz.")

            sonuc = tckn.tc_check(tc_no)
            if isinstance(sonuc, str): 
                print(sonuc)
            else: print(f"TC Kimlik No {tc_no} {'✓ geçerli ' if sonuc else 'x geçersiz '}")

        elif secim == 2:
            while True:
                try:
                    baslangic_tc = int(input("\nBaşlangıç TC Kimlik No giriniz: "))
                    break
                except ValueError: print("Geçersiz giriş. Lütfen bir sayı giriniz.")

            sonuc = tckn.tc_next(baslangic_tc)
            if sonuc is None: print("Bir sonraki geçerli TC Kimlik No bulunamadı.")
            else: print(f"Bir sonraki geçerli TC Kimlik No: {sonuc[0]}")

        elif secim == 3:
            while True:
                try:
                    baslangic_tc = int(input("\nBaşlangıç TC Kimlik No giriniz: "))
                    bitis_tc = int(input("Bitiş TC Kimlik No giriniz: "))
                    if baslangic_tc > bitis_tc:
                        raise ValueError
                    break
                except ValueError:
                    print("Geçersiz giriş. Lütfen başlangıç TC'nin bitiş TC'den küçük olduğundan emin olun.")

            sayisi = tckn.which_tc_between(baslangic_tc, bitis_tc)
            print(f"Belirtilen aralıktaki ({baslangic_tc}-{bitis_tc}), {bitis_tc-baslangic_tc} adet numara kontrol edildi.\n\t\t\tgeçerli TC Kimlik Numarası sayısı: {sayisi}")

        else:
            print("Çıkış yapılıyor...")
            break
        sleep(1)
