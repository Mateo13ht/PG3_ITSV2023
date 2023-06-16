import pytest
import math

def calculate_statistics(numbers):
    n = len(numbers)
    if n == 0:
        return None

    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_deviation = math.sqrt(variance)

    return mean, std_deviation

def test_calculate_statistics():
    assert calculate_statistics([]) == None

    assert calculate_statistics([5]) == (5, 0)

    assert calculate_statistics([1, 2, 3, 4, 5]) == (3, pytest.approx(1.414, 0.001))

    assert calculate_statistics([-1, -2, -3, -4, -5]) == (-3, pytest.approx(1.414, 0.001))

    assert calculate_statistics([-1, 2, -3, 4, -5]) == (-0.6, pytest.approx(3.682, 0.001))

    assert calculate_statistics([1.5, 2.75, 3.25, 4.8, 5.2]) == (3.5, pytest.approx(1.496, 0.001))
