from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "World!"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, "x")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 2)

    assert encrypt_message(message, 2) == "!dlr_oW"
    assert encrypt_message(message, 3) == "roW_!dl"
    assert encrypt_message(message, -2) == "!dlroW"
