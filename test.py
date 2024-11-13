for i in range(10):
    user_input = input("Döngüyü devam ettirmek için bir şey yazın (çıkmak için 'q' yazın): ")
    if user_input.lower() == 'q':
        print("Döngü durduruldu.")
        break  # Döngüyü durdur
    pass  # Henüz bir işlem yok