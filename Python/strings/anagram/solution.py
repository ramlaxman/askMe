#!/usr/bin/env python

def isAnagram(string1, string2):

    return sorted(string1) == sorted(string2)

# Test the function
# -----------------
print isAnagram("the eyes","they see") # Should print True
print isAnagram("school master", "the classroom") # Should print True
print isAnagram("Mario", "Luigi") # Should print False
