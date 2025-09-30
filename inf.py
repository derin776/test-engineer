#for i in range(100, 1000):
#    fs = (i // 100) * (i % 100 // 10)
#    ft = (i // 100) * (i % 10)
#    res = int(str(max(fs, ft)) + str(min(fs, ft)))
#    if res == 2412:
#        print(i)
#        break


#def to_system(n, system):
#    res = ''
#    while n > 0:
#        res = str(n % system) + res
#        n //= system
#    return res
#
#for x in range(10000):
#    res = to_system(x, 5)
#    res += str(sum([int(i) for i in res]) % 5)
#    res += str(sum([int(i) for i in res]) % 5)
#    if int(res, 5) > 561:
#        print(x)
#        break


#for i in range(10000):
#    binary = bin(i)[2:]
#    if i % 3 == 0:
#        binary += binary[-3:]
#    else:
#        binary += bin(3 * (1 % 3))[2:]
#    if int(binary, 2) > 143:
#        print(i)
#        break


#x = 4 ** 2014 + 2 ** 2015 - 8
#print(bin(x)[2:].count('1'))


#def to_system(n, system):
#    res = ''
#    while n > 0:
#        res = str(n % system) + res
#        n //= system
#    return res
#
#x = 27**11 + 3**19 - 9**7 - 9
#lmao = to_system(x, 3)
#print(lmao.count('2'))


#x = bin((32**32 + 4**4 - 1) * 16 ** 16 + 8 ** 8 - 1)
#print(x[2:].count('1'))

#res = []
#for N in range(1, 1000):
#    bin_n = bin(N)[2:]
#    if N % 3 == 0:
#        bin_n += '000'
#    else:
#        bin_n += bin(N % 3 * 3)[2:]
#    res.append(int(bin_n, 2))
#res.sort()
#max_count = 0
#for left in range(len(res) - 1):
#    for right in range(left + 1, len(res)):
#        if res[right] - res[left] <= 60:
#            max_count = max(max_count, right - left)
#print(max_count)


#alph = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
#
#def to_system(n, syst):
#    res = ''
#    while n > 0:
#        res = alph[n % syst] + res
#        n //= syst
#    return res
#
#print(to_system(4*3125**9 + 5*625**8 - 2*625**7 + 7 * 125**5 - 9*25**4 - 2024, 25).count('0'))



#res = []
#for N in range(10**4, 10**5):
#    summ = N // 10 ** 4 + N % 10 ** 4 // 10 ** 3 + N % 10 ** 3 // 10 ** 2 + N % 10 ** 2 // 10 + N % 10
#    res.extend([N * 10 + (summ % int(i)) for i in str(N) if i != '0'])
#print(len(set(res)))


#for x in range(15):
#    a = 2 * 15 ** 4 + 8 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
#    b = 1 * 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 4 * 15 + 3
#    if (a + b) % 11 == 0:
#        print((a + b) // 11)
#        break


#def to3(num):
#    res = ''
#    while num > 0:
#        res = str(num % 3) + res
#        num //= 3
#    return res
#
#for x in range(3699, 0, -1):
#    if to3(3**100 - x).count('0') == 2:
#        print(x)
#        break


from itertools import *
#
#alph = 'ABCD'
#alph2 = 'EFGH'
#k = 2
#print([i for i in permutations(alph)])
#print([i for i in permutations(alph, k)])
#print([i for i in combinations(alph, k)])
#print([i for i in product(alph, repeat=k)])
#print([i for i in product(alph, alph2)])


#alph = sorted('УРОК')
#res = [''.join(item) for item in product(alph, repeat=4)]
#for ind in range(len(res)):
#    if 'K' not in res[ind] and 'ОО' not in res[ind]:
#        print(ind + 1)
#        break
#
#print(len([item for item in product('01', repeat=4) if item.count("") == 2]))


from ipaddress import IPv4Address, ip_network

counter = 0
raw_net = IPv4Address('172.16.168.0')
mask = IPv4Address('255.255.248.0')
net = ip_network(f'{raw_net}/{mask}')
for host in net:
    tmp = sum([bin(int(el))[2:].count('1') for el in str(host).split('.')])
    if tmp % 5 != 0:
        counter += 1
print(counter)