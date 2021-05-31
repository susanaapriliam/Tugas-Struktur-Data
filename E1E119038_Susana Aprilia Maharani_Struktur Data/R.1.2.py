# Tulis fungsi Python pendek, genap(k), yang mengambil nilai integer dan mengembalikan True jika k genap,
# dan False sebaliknya. Namun, fungsi Anda tidak dapat menggunakan operator perkalian, modulo, atau pembagian.

def is_multiple(n,m):
    return (True if m%n==0 else  False)

print(is_multiple(10,20))
print(is_multiple(10,31))
