from my_project.main import add


def test_add():
    # Test cases with expected outputs
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, 5) == 15
    assert add(-5, -5) == -10
