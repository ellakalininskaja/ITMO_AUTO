def task_1():
    a: int = 1
    print("a", type(a))
    b: float = 1.1
    print("b", type(b))
    c: str = "str"
    print("c", type(c))
    d: list = [1, 2, 3]
    print("d", type(d))
    e: bool = True
    print("e", type(e))


task_1()


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print(task_2())


def task_3(a: int) -> int:
    return a ** 2


print(task_3(8))
