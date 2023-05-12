# Email validator from HW_18


class SignUp:
    def __init__(self, email):
        self.email_validator(email)
        self.email = email
        print("Congratulations! You have successfully signed-up")

    def email_validator(self, email: str):
        email_list = list(email)
        unsupported_chars = [
            "!",
            "#",
            "$",
            "%",
            "^",
            ";",
            ":",
            "&",
            "?",
            "*",
            ")",
            "(",
            "=",
            "+",
            "}",
            "{",
        ]

        if any(item in unsupported_chars for item in email_list):
            raise ValueError(
                "Email can not contain unsupported chars"
            )

        elif len(email) > 30 or len(email) == 0:
            raise ValueError("Inappropriate email length")

        elif email[-1] == "@" or email[-1] == ".":
            raise ValueError("Email can not end by '@' or '.'")

        elif "@" not in email_list:
            raise ValueError("Wrong email format! Example: example@mail.com")

        elif "." not in email_list:
            raise ValueError("Wrong email format! Example: example@mail.com")

        elif email_list.count("@") > 1:
            raise ValueError("Wrong email format! Example: example@mail.com")


#
