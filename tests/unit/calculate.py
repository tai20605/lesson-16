def calculate_summary(numbers: list) -> dict:
    """Calculates the sum, count, and average of a list of numbers"""

    if not numbers:
        return {"sum": 0, "count": 0, "average": 0.0}

    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count

    return {
        "sum": total_sum,
        "count": count,
        "average": round(average, 2)
    }


if __name__ == "__main__":
    raw = input("Enter numbers (separated by spaces): ")

    try:
        numbers = [float(x) for x in raw.split()]
    except ValueError:
        print("Invalid input: please enter numbers only.")
    else:
        result = calculate_summary(numbers)
        print(f"Sum: {result['sum']}")
        print(f"Count: {result['count']}")
        print(f"Average: {result['average']}")