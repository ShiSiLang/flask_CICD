from func001 import function1, function2


def setUp():
    print("start test")


def tearDown():
    print("function teardown")


def Test1():
    rt = function1()
    assert rt == 200


def Test2():
    rt = function2()
    assert rt == 200
