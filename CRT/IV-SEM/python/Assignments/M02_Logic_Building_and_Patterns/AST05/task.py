def number_triangle(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        row = "".join(str(j) for j in range(1, i + 1))
        result += row + "\n"
    return result.rstrip("\n")  

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))