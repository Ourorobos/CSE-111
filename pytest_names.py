from names import make_full_name, extract_family_name, extract_given_name
import pytest


names = [
    ["Mark-King","Stephen","Mark-King; Stephen"],
    ["Verylonglastname","Bill","Verylonglastname; Bill"],
    ["Quick", "Verylongfirstname", "Quick; Verylongfirstname"],
    ["Last-name","First-name","Last-name; First-name"],
    ["billybobbyjoe","Southman","billybobbyjoe; Southman"],
    ["Normal","Human","Normal; Human"],
    ]

def test_make_full_name():
    for name in names:
        last, first, full = name
        result = make_full_name(first,last)
        print(result)

def test_extract_family_name():
    for name in names:
        result = extract_family_name(name[2])
        print(result)

def test_extract_given_name():
    for name in names:
        result = extract_given_name(name[2])
        print(result)

test_extract_given_name()
print()
test_extract_family_name()
print()
test_make_full_name()
