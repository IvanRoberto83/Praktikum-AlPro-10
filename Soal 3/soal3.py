handle = open('berita.txt')

print("===== ISI BERITA =====")
for kata in handle:
    print(kata)
    kata_unik = kata.split()

print("\n===== KATA UNIK PADA BERITA =====")
print(kata_unik)