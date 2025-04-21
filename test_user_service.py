from user_service import get_user

def test_get_user():
    assert get_user() == "Sanju"
