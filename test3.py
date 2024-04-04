import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)


def radians_to_degrees(radians):
    return radians * (180 / math.pi)


def sin_taylor(degrees, n):
    radians = degrees_to_radians(degrees)
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (radians ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result


def cos_taylor(degrees, n):
    radians = degrees_to_radians(degrees)
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (radians ** (2 * i)) / factorial(2 * i)
        result += term
    return result


def arcsin_taylor(x, n):
    result = 0
    for i in range(n):
        coef = factorial(2 * i) / (4 ** i * factorial(i) ** 2 * (2 * i + 1))
        term = coef * (x ** (2 * i + 1))
        result += term
    return radians_to_degrees(result)


def arctan_taylor(x, n):
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (x ** (2 * i + 1)) / (2 * i + 1)
        result += term
    return radians_to_degrees(result)


def test_trig_functions():
    inputs = [0, 30, 45, 60, 90]
    n_terms = 10

    for angle in inputs:
        radians = degrees_to_radians(angle)
        sin_taylor_result = sin_taylor(angle, n_terms)
        cos_taylor_result = cos_taylor(angle, n_terms)

        # Make sure arcsin input is within -1 to 1 range
        arcsin_input = min(max(math.sin(radians), -1), 1)
        arcsin_taylor_result = arcsin_taylor(arcsin_input, n_terms)

        arctan_taylor_result = arctan_taylor(radians, n_terms)

        sin_math_result = math.sin(radians)
        cos_math_result = math.cos(radians)
        arcsin_math_result = math.asin(arcsin_input)
        arctan_math_result = math.atan(radians_to_degrees(radians))

        sin_diff = abs(sin_taylor_result - sin_math_result)
        cos_diff = abs(cos_taylor_result - cos_math_result)
        arcsin_diff = abs(arcsin_taylor_result - arcsin_math_result)
        arctan_diff = abs(arctan_taylor_result - arctan_math_result)

        print(f"Angle: {angle} degrees")
        print(f"sin: Taylor series = {sin_taylor_result}, Math library = {sin_math_result}, Difference = {sin_diff}")
        print(f"cos: Taylor series = {cos_taylor_result}, Math library = {cos_math_result}, Difference = {cos_diff}")
        print(
            f"arcsin: Taylor series = {arcsin_taylor_result}, Math library = {arcsin_math_result}, Difference = {arcsin_diff}")
        print(
            f"arctan: Taylor series = {arctan_taylor_result}, Math library = {arctan_math_result}, Difference = {arctan_diff}")
        print()


test_trig_functions()
