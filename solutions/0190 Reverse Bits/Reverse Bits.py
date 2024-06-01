def reverse_bits(n):
    # handle leading 0s
    bit_length = 32

    result = 0
    for _ in range(bit_length):
        result = result << 1
        curr_bit = n & 1
        result += curr_bit
        n = n >> 1
    return result
