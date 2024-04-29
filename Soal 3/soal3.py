handle = open('berita.txt')
kata_unik = []

print("===== ISI BERITA =====")
for kata in handle:
    print(kata.strip())
    x = kata.split()

    for kata in x:
        i = kata.strip(",.?!-")

        if i not in kata_unik:
            if i != "":
                if i.lower() not in kata_unik:
                    kata_unik.append(i)

print("\n===== KATA UNIK PADA BERITA =====")
print(kata_unik)

