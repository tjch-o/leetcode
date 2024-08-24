def defang_ip_addr(address):
    result = ""

    for c in address:
        if c == ".":
            result += "[.]"
        else:
            result += c
    return result
