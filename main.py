def PrimeList(N):
    primes = []
    # 遍历2到N-1的所有数，判断是否为质数
    for num in range(2, N):
        is_prime = True
        # 检查num是否能被2到其平方根之间的数整除
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 将质数列表转为空格分隔的字符串（末尾无空格）
    return ' '.join(primes)
