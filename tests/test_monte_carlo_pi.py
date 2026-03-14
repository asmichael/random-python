import random
from scripts.monte_carlo_pi import estimate_pi


def test_returns_float():
    assert isinstance(estimate_pi(100), float)


def test_result_in_valid_range():
    # pi must be between 2 and 4 regardless of randomness
    result = estimate_pi(1000)
    assert 2.0 < result < 4.0


def test_converges_near_pi():
    # with a fixed seed, result should be close to pi
    random.seed(42)
    result = estimate_pi(100_000)
    assert abs(result - 3.14159) < 0.05


def test_single_iteration():
    result = estimate_pi(1)
    assert result in (0.0, 4.0)


def test_large_iteration_count():
    random.seed(0)
    result = estimate_pi(1_000_000)
    assert abs(result - 3.14159) < 0.01
