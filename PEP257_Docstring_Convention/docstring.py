# Sample Python program without comments and docstrings

"""
This is a calculator program demonstrating basic math operations. The operations in this program, our addition, subtraction, multiplication, division, and these are demonstrated using a class.

 This assignment is for practicing the PEP 257 docstring convention.

"""

class Calculator:
    """
        A calculator class to perform math operations.
        
         Attributes: 
            value: the current value stored in the calculator
        """
    def __init__(self, value=0):
        
        """
        Initialize the calculator with a starting value.
        
        Args: 
            Value: the initial value of the calculator is set to a default of 0.
        
        """
        self.value = value
        

    def add(self, num):
        """
        Add a number to the current value.

        Args:
            num: The number to add.
        """
        
        self.value += num
       

    def subtract(self, num):
        """
        Subtract a number from the current value.

        Args:
            num: The number to subtract.
        """
        self.value -= num
        

    def multiply(self, num):
        """Multiply the current value by a number.

        Args:
            num: The number to multiply by.
        """
        self.value *= num
        

    def divide(self, num):
        """Divide the current value by a number.

        Args:
            num: The number to divide by.

        Raises:
            ValueError: If the number is zero (cannot divide by zero).
        """
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Cannot divide by zero")

    def clear(self):
        """Reset the calculator value to zero."""
        self.value = 0

    def get_value(self):
        """Return the current value stored in the calculator."""
        return self.value

def main():
    """
    Demonstrate the usage of the Calculator class with example operations.

    This includes addition, subtraction, multiplication, and division.
    Also demonstrates error handling when attempting division by zero.
    """
    calc = Calculator() # create a new calculator in instance
    calc.add(10) # add 10
    calc.subtract(2) # subtract 2
    calc.multiply(5) # multiplied by 5
    try:
        calc.divide(0) # try to divide by zero(it will raise error)
    except ValueError as e:
        print(e) # print an error message
    calc.divide(4) # divided by 4
    print(f"Final value: {calc.get_value()}") #print the final value
    
    # TODO: add more math operations in future.

if __name__ == "__main__":
    main()
    


help(Calculator.add) # show us the docstring for the add() method, can also do same for (calculator.divide) or more
    
