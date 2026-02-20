def polynomial_evaluation(coeffs, x):
    if not coeffs:
        return 0

    result = coeffs[-1]

    for i in range(len(coeffs) - 2, -1, -1):
        result = result * x + coeffs[i]

    return result


if __name__ == "__main__":
    coeffs = list(map(float, input().split()))
    x = float(input())
    print(polynomial_evaluation(coeffs, x))
