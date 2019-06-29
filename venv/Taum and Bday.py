t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    b = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    bc = int(second_multiple_input[0])

    wc = int(second_multiple_input[1])

    z = int(second_multiple_input[2])

    if bc==wc:
        a=b*bc + w*wc
        print(a)

    elif bc>wc and bc>z:
        d=w+b
        a=d*wc+b*z
        if a<(b*bc + w*wc):
            print(a)
        else:
            print(b*bc + w*wc)

    elif wc>bc and wc>z:
        d = w + b
        a = d * bc + w * z
        if a<(b*bc + w*wc):
            print(a)
        else:
            print(b*bc + w*wc)

    elif z>wc or z>bc:
        a = b * bc + w * wc
        print(a)
