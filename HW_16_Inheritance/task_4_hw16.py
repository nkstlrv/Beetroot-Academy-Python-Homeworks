
# Default Custom exception class that only raises Exception
class CustomException(Exception):

    def __init__(self, message = "Custom exception occured "):
        self.message = message

    def raise_exception(self):
        raise CustomException(self.message)
    

# New class that inherits previos and logs Exception message to txt file
class PrintCustomException(CustomException):

    def __init__(self, message="Custom exception occured and printed "):
        super().__init__(message)

    def raise_exception(self):
        print_message = str(CustomException(self.message))
        with open ("Module_2\HW_16_Inheritance\log.txt", "a") as f:
            f.write(print_message + "\n\n")
        return super().raise_exception()
    
ex = PrintCustomException()
ex.raise_exception()