def mencari_min(nilai):
    nilai_min = nilai[0]
    for i in nilai :
        if i < nilai_min:
            nilai_min = i
    return nilai_min

def mencari_max(nilai):
    nilai_max = nilai[0]
    for i in nilai :
        if i > nilai_max:
            nilai_max = i
    return nilai_max

def mencari_sum(nilai):
    nilai_sum = 0
    for i in nilai:
        nilai_sum += i
    return nilai_sum

def mencari_len(nilai):
    nilai_len = 0
    for i in nilai:
        nilai_len += 1
    return nilai_len