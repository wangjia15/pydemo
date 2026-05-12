def add(a: int, b: int) -> int:
    """加法函数"""
    return a + b

def test_add():
    """测试加法"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(0, 1) == 1