from app import hello_world

def test_hello_world():
    response = hello_world();
    assert response == "Hello, World!"