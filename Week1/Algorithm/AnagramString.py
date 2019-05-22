from Week1.Util import IsAnagram

try:
    str1 = input("Enter First String : ")
    str2 = input("Enter Second String : ")
    str1, str2 = IsAnagram(str1, str2)

    if str1 == str2:                               # Comparing Both Strings If True Then Anagram
        print("\nStrings Are Anagram ")
    else:
        print("\nStrings Are Not Anagram ")
except ValueError:
    print("Invalid Strings")
