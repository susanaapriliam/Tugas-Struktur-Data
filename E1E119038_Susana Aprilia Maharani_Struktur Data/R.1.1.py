# Tulis fungsi Python singkat, multipel (n, m), yang mengambil dua nilai integer dan mengembalikan
# True jika n adalah kelipatan dari m, yaitu, n = mi untuk beberapa bilangan bulat i, dan False sebaliknya.

def is_multiple(n,m):
    return (True if m%n==0 else  False)

print(is_multiple(10,20))
print(is_multiple(10,31))
