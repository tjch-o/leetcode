def largest_altitude(gain):
    if len(gain) == 1:
        return gain[0] if gain[0] > 0 else 0
    
    n = len(gain)
    altitudes = [0 for _ in range(n + 1)]
    altitudes[1] = gain[0]
    
    for i in range(2, n + 1):
        net_altitude_at_point = gain[i - 1]
        altitudes[i] = altitudes[i - 1] + net_altitude_at_point
    return max(altitudes)
