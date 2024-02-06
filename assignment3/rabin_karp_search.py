def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(haystack, needle):
    # Довжини основного рядка та підрядка пошуку
    needle_length = len(needle)
    haystack_length = len(haystack)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    needle_hash = polynomial_hash(needle, base, modulus)
    current_slice_hash = polynomial_hash(haystack[:needle_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, needle_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(haystack_length - needle_length + 1):
        if needle_hash == current_slice_hash:
            if haystack[i:i+needle_length] == needle:
                return i

        if i < haystack_length - needle_length:
            current_slice_hash = (current_slice_hash - ord(haystack[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(haystack[i + needle_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


if __name__ == "__main__":
    haystack = "Being a developer is not easy"
    needle = "developer"

    position = rabin_karp_search(haystack, needle)
    if position != -1:
        print(f"Needle found at index {position}")
    else:
        print("Needle not found")
