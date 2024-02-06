def compute_lps(needle):
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(haystack, needle):
    M = len(needle)
    N = len(haystack)

    lps = compute_lps(needle)

    i = j = 0

    while i < N:
        if needle[j] == haystack[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено


if __name__ == '__main__':
    raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."

    needle = "алг"

    print(kmp_search(raw, needle))
