from sqline import get_engine_string


def test_get_engine_string():
    final_string = "postgresql://scott:tiger@15.64.52.69:1521/mydatabase"
    result = get_engine_string("postgresql", "scott", "tiger",
                               "15.64.52.69", "mydatabase", 1521)

    assert final_string == result
