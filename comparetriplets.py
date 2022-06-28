def compare_triplets(a,b):
    arr = []
    Ap = 0
    Bp = 0
    for i in range (0, len(a)):
        if a[i] > b[i]:
            Ap = Ap +1
        elif b[i] > a[i]:
            Bp = +1
        else:
            continue
    arr.append(Ap)
    arr.append(Bp)
    return arr
a = [2,3,6]
b = [7,2,1]
print(compare_triplets(a,b))