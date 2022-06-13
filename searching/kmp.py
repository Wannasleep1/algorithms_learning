def get_prefix_list(pattern: str):
    i = 1
    j = 0
    prefix_list = [0] * len(pattern)
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            prefix_list[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                prefix_list[i] = 0
                i += 1
            else:
                j = prefix_list[j-1]
    return prefix_list


def simple_kmp(prefix_func, pattern, text):
    prefix_list = prefix_func(pattern)
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - len(pattern)
        else:
            if j > 0:
                j = prefix_list[j-1]
            else:
                i += 1

    if i == len(text):
        return None



def all_matches_kmp(prefix_func, pattern, text):
    prefix_list = prefix_func(pattern)
    result_lst = []
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                result_lst.append(i - len(pattern))
                j = 0
        else:
            if j > 0:
                j = prefix_list[j-1]
            else:
                i += 1

    return result_lst


if __name__ == "__main__":
    text = "лилилось лилилась"
    pattern = "лилила"
    pattern_all = "лилил"
    result = simple_kmp(get_prefix_list, pattern, text)
    result_all = all_matches_kmp(get_prefix_list, pattern_all, text)
    print(result)
    print(result_all)
