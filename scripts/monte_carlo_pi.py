import random


def estimate_pi(iterations: int) -> float:
    inside = 0
    for _ in range(iterations):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / iterations


if __name__ == "__main__":
    iterations = 31_415_927
    result = estimate_pi(iterations)
    print(f"Iterations : {iterations:,}")
    print(f"Estimated π: {result}")
    print(f"Actual π   : 3.14159265358979...")
    print(f"Error      : {abs(result - 3.14159265358979):.6f}")
