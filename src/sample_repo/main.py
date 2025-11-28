def add(a: int, b: int) -> int:
    """整数の足し算

    Args:
        a (int): 計算値a
        b (int): 計算値b

    Returns:
        (int): 計算結果
    """
    if not isinstance(a, int): raise TypeError("a is not integer.")
    if not isinstance(b, int): raise TypeError("b is not integer.")
    return a + b
