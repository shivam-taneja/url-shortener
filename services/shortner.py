import secrets
import string


def generate_code(length: int = 6) -> str:
    if length <= 0:
        raise ValueError("length must be positive")

    chars = string.ascii_letters + string.digits
    code = ""

    for _ in range(length):
        code += secrets.choice(chars)

    return code
