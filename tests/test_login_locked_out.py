def test_login_locked(login_locked):
    """
    Test login with a locked-out user.
    Ensures the correct error message is displayed when attempting login.
    """
    error_message = login_locked.get_error_message()
    assert error_message == "Epic sadface: Sorry, this user has been locked out."