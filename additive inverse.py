def is_additive_seq(s):
    length = len(s)

    for i in range(1, length):
        for j in range(i + 1, length):
            num1 = int(s[:i])
            num2 = int(s[i:j])
            k = j

            while k < length:
                num3 = num1 + num2
                str_num3 = str(num3)  # rename this variable

                if not s.startswith(str_num3, k):
                    break

                k += len(str_num3)
                num1, num2 = num2, num3

                if k == length:
                    return True

            if k != length:
                break

    return False


str_val = "235813"  # rename this variable
result = is_additive_seq(str_val)
print(result)
