vowels = ["a", "e", "i", "o","u"]
print(f"List: {vowels}")
del vowels[3]
print(f"del vowels[3]: {vowels}")

vowels = ["a", "e", "i", "o","u"]
print(f"\nList: {vowels}")
del vowels[0:2]
print(f"del vowels[0:2]: {vowels}")

vowels = ["a", "e", "i", "o","u"]
print(f"\nList: {vowels}")
del vowels[:]
print(f"del vowels[:]: {vowels}")

vowels = ["a", "e", "i", "o","u"]
print(f"\nList: {vowels}")
del vowels
print(f"del vowels: {vowels}")