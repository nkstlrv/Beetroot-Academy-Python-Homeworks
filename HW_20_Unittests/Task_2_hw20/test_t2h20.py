from module_to_test_t1hw20 import SignUp
import pytest


def test_successful_sign_up():
    s = SignUp('example@mail.com')
    assert s.email == 'example@mail.com'

    s = SignUp('EXAmpL@mail.c')
    assert s.email == "EXAmpL@mail.c"

    s = SignUp('e@.c')
    assert s.email == "e@.c"


def test_unsupported_chars():
    with pytest.raises(ValueError) as ex_info_1:
        u_1 = SignUp('ex(*am#ple@mail.com%')
    assert "Email can not contain unsupported chars" == str(ex_info_1.value)

    with pytest.raises(ValueError) as ex_info_1:
        u_2 = SignUp('!example@mail.com')
    assert "Email can not contain unsupported chars" == str(ex_info_1.value)


def test_wrong_len():
    with pytest.raises(ValueError) as ex_info_2:
        mx = SignUp('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexample@mail.com')
    assert "Inappropriate email length" == str(ex_info_2.value)

    with pytest.raises(ValueError) as ex_info_2:
        mn = SignUp('')
    assert "Inappropriate email length" == str(ex_info_2.value)


def test_email_ends_with_dot_or_at():
    with pytest.raises(ValueError) as ex_3:
        dt = SignUp("example@mail.")
    assert "Email can not end by '@' or '.'" == str(ex_3.value)

    with pytest.raises(ValueError) as ex_3:
        dt = SignUp("example@mail.com.")
    assert "Email can not end by '@' or '.'" == str(ex_3.value)

    with pytest.raises(ValueError) as ex_3:
        att = SignUp("example@")
    assert "Email can not end by '@' or '.'" == str(ex_3.value)


def test_at_or_dot_not_in_email():
    with pytest.raises(ValueError) as ex_4:
        ndt = SignUp("example@mailcom")
    assert "Wrong email format! Example: example@mail.com" == str(ex_4.value)

    with pytest.raises(ValueError) as ex_4:
        nat = SignUp("examplemail.com")
    assert "Wrong email format! Example: example@mail.com" == str(ex_4.value)

    with pytest.raises(ValueError) as ex_4:
        nadt = SignUp("examplemailcom")
    assert "Wrong email format! Example: example@mail.com" == str(ex_4.value)


def test_ats_more_then_one():
    with pytest.raises(ValueError) as ex_5:
        tat = SignUp("ex@ample@mail.com")
    assert "Wrong email format! Example: example@mail.com" == str(ex_5.value)

    with pytest.raises(ValueError) as ex_5:
        mat = SignUp("ex@amp@le@@mail.@com")
    assert "Wrong email format! Example: example@mail.com" == str(ex_5.value)
