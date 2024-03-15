def checkVowel(n):
  match n:
    case 'a': return "Vowel"
    case 'e': return "Vowel"
    case 'i': return "Vowel"
    case 'o': return "Vowel"
    case 'u': return "Vowel"
    case _: return "Simple alphabet"
    
print(checkVowel('a'))
print(checkVowel('b'))
print(checkVowel('i'))
print(checkVowel('p'))