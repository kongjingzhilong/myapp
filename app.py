def add(a,b):
    return a+b
def test_add():
    assert add(-1, 2)==1
    assert add(-1, 1)==0
    print("All Test Passed")
if __name__=="__main__":
    test_add()
