from devoir2_q1 import get_rand_power, get_h, get_shared_k

def test_public_key_exchange():
    # 1. Alice and Bob chose b=2 and p=2
    b = 2
    p = 2**255

    # 2. Alice sends h_a to bob
    k_a = 2**get_rand_power(0, 128)
    h_a = get_h(k_a, b, p)
    print(f"Alice sends to Bob: {h_a}")

    # 3. Bob sends h_b to alice
    k_b = 2**get_rand_power(0, 128)
    h_b = get_h(k_b, b, p)
    print(f"Bob sends to Alice: {h_b}")

    # 4. Alice calcule la cle avec h_b
    kA = get_shared_k(h_b, k_a, p)

    # 5. Bob calcule la cle avec h_a
    kB = get_shared_k(h_a, k_b, p)

    assert(kA==kB)

def test_man_in_middle():
    # 1. Alice and Bob chose b=2 and p=2
    b = 2
    p = 2**255

    # 2. Alice sends h_a to bob
    k_a = 2**get_rand_power(0, 128)
    h_a = get_h(k_a, b, p)

    # 3. Bob sends h_b to alice
    k_b = 2**get_rand_power(0, 128)
    h_b = get_h(k_b, b, p)

    # 3. Eve, man-in-the-middle, attack
    # pretends to be Bob for Alice
    k_ae = 2**get_rand_power(0, 128)
    h_ae = get_h(k_ae, b, p)
    # pretends to be Alice for Bob
    k_be = 2**get_rand_power(0, 128)
    h_be = get_h(k_be, b, p)

    # 4. Alice calcule la cle avec h_b
    kA = get_shared_k(h_ae, k_a, p)
    kAE = get_shared_k(h_a, k_ae, p)

    # 5. Bob calcule la cle avec h_a
    kB = get_shared_k(h_be, k_b, p)
    kBE = get_shared_k(h_b, k_be, p)

    assert(kA==kAE)
    assert(kB==kBE)
    assert(kB!=kA)


