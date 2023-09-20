string = "0123456789"
substring = ""

print(f"Main string: {string}")

substring = string[0]
print(f"\nSubstringwith index at position[0] is: {substring}")

substring = string[5]
print(f"\nSubstringwith index at position [5] is: {substring}")

substring = string[-4]
print(f"\nSubstringwith index at position[-4] is: {substring}")

substring = string[0:3]
print(f"\nSubstringwith index at position[0:3] is: {substring}")

substring = string[:3]
print(f"\nSubstringwith index at position[:3] is: {substring}")

substring = string[5:]
print(f"\nSubstringwith index at position[5:] is: {substring}")

substring = string[-4:-1]
print(f"\nSubstringwith index at position[-4:-1] is: {substring}")

substring = string[:]
print(f"\nSubstringwith index at position[:] is: {substring}")

substring = string[1:6:2]
print(f"\nSubstringwith index at position[1:6:2] is: {substring}")

substring = string[::3]
print(f"\nSubstringwith index at position[::3] is: {substring}")
