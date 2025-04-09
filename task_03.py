def move_disk(towers, source, target):
    """Переміщує верхній диск зі стрижня source на стрижень target."""
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {towers}")


def hanoi(n, source, auxiliary, target, towers):  # recursive call
    if n == 1:
        move_disk(towers, source, target)
    else:
        hanoi(n - 1, source, target, auxiliary, towers)
        move_disk(towers, source, target)
        hanoi(n - 1, auxiliary, source, target, towers)


def solve_hanoi(n):
    towers = {"A": list(range(n, 0, -1)), "B": [], "C": []}  # [n, n-1, ..., 1]
    print(f"Початковий стан: {towers}")
    hanoi(n, "A", "B", "C", towers)
    print(f"Кінцевий стан: {towers}")


if __name__ == "__main__":
    try:
        n = int(input("Введіть кількість дисків: "))
        if n <= 0:
            raise ValueError("Кількість дисків має бути додатною!")
    except ValueError as e:
        print(f"Помилка: {e}")
    else:
        solve_hanoi(n)

# The number of moves required to solve this test with n disks is given by the formula:
n = 3
steps = 2**n - 1
print(steps)  # 7
