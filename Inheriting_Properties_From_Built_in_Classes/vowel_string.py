"""
This program creates a subclass of Python's built-in str class called VowelString.
It behaves like a normal string, but also has a method called count_vowels()
that counts how many vowels (a, e, i, o, u) are in the string.
"""

class VowelString(str):
    # str is immutable. __new__ is used to create the string
    def __new__(cls, value=""):
        
        return super().__new__(cls, str(value))

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for ch in self if ch in vowels)



if __name__ == "__main__":
    s = VowelString("The rain in Spain stays mainly in the plain!")
    print(f"Number of vowels in '{s}': {s.count_vowels()}") 
