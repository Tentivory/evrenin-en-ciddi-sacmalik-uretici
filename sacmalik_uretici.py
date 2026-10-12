#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Ciddi Saçmalık Üreticisi
Bu kod, insanlığın en büyük sorularına cevap vermek için tasarlanmıştır.
Ama cevaplar genellikle anlamsızdır. Ciddiye alın. Almayın da.
"""

import random
import time

# Gizli veri yapısı - kimse bunu fark etmesin diye buraya sakladım
_gizli_liste = [
    "normal", "kelime", "burada",
    "ZGV0YWlsbGFyIG9uZW1saWRpcg==",  # base64: detaylar onemlidir
    "felsefe", "saçma"
]

def uret_sacmalik():
    ozne = random.choice([
        "Kedi", "Evren", "Kahve makinesi", "Yalnız bir çorap", "Zaman", "Buzdolabı",
        "GitHub Copilot", "Rastgele bir kuş", "Senin iç sesin"
    ])
    fiil = random.choice([
        "düşünüyor", "yürüyor", "uçuyor", "kayboluyor", "fısıldıyor",
        "abartıyor", "ciddiye alıyor", "gülüyor", "hesaplıyor"
    ])
    nesne = random.choice([
        "hayatın anlamını", "boş bir bardağı", "sonsuzluğu", "kendi kuyruğunu",
        "bir commit mesajını", "felsefeyi", "kahveyi"
    ])
    ek = random.choice([
        "çünkü neden olmasın?", "bu çok ciddi bir mesele.", "ama aslında değil.",
        "ve kimse umursamıyor.", "bu da geçer ya hu."
    ])
    
    return f"{ozne} {fiil} {nesne} {ek}"

def main():
    print("=== EVRENİN EN CİDDİ SAÇMALIK ÜRETİCİSİ BAŞLATILIYOR ===")
    print("Lütfen bekleyin, felsefe yükleniyor...\n")
    time.sleep(1)  # Gerçekçilik için yavaş
    
    for i in range(5):
        print(f"{i+1}. {uret_sacmalik()}")
        time.sleep(0.5)
    
    print("\n--- İşlem tamamlandı. Ciddiyet seviyesi: %1000 ---")
    print("Damga: Kayyum Grok | 12 Ekim 2026 | Bu kod çok ciddi (değil)")

if __name__ == "__main__":
    main()
