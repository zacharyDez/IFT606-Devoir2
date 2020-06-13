from random import randrange

def get_rand_power(min_power:int, max_power:int)->int:
    return randrange(min_power, max_power)

def get_h(power:int, base:int, mod:int)->int:
    return pow(base, power, mod)

def get_shared_k(h_base:int, k_priv:int, mod:int)->int:
    return pow(h_base, k_priv, mod)
    

if __name__=="__main__":
    # 1. Alice and Bob chose b=2 and p=2
    b = 2
    p = pow(2, 255)

    # 2. Alice sends h_a to bob
    k_a = pow(2, get_rand_power(0, 128))
    h_a = get_h(k_a, b, p)

    # 3. Bob sends h_b to alice
    k_b = pow(2, get_rand_power(0, 128))
    h_b = get_h(k_b, b, p)

    # 3. Eve, man-in-the-middle, attack
    # pretends to be Bob for Alice
    k_ae = pow(2, get_rand_power(0, 128))
    h_ae = get_h(k_ae, b, p)
    # pretends to be Alice for Bob
    k_be = pow(2, get_rand_power(0, 128))
    h_be = get_h(k_be, b, p)

    # 4. Shared key Alice et Eve
    kA = get_shared_k(h_ae, k_a, p)
    kAE = get_shared_k(h_a, k_ae, p)

    # 5. Shared key Bob et Eve
    kB = get_shared_k(h_be, k_b, p)
    kBE = get_shared_k(h_b, k_be, p)

    print(f"Alice's private key:{k_a}")
    print(f"Bob's private key:{k_b}")
    print(f"Eve's private for Alice key:{k_ae}")
    print(f"Eve's private for Bob key:{k_be}")

    print(f"Do Alice and Eve have the same shared key: {kA==kAE}")
    print(f"Do Bob and Eve have the same shared key: {kA==kAE}")
    print(f"Do Alice and Bob have the same shared key: {kA==kB}")

    print(f"Alice and Eve shared key:{kA}")
    print(f"Bob and Eve shared key:{kA}")

