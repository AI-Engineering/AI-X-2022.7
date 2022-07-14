number = 10
day = "three"
str1 = "I ate %d apples.\nSo I was sick for %s days." % (number, day)
print(str1)
str1 = f"I ate {number} apples.\nSo I was sick for {day} days."
print(str1)

str1 = "%4s\n%4s\n%4s\n%4s" % ("a", "ab", "abc", "abcd")
print(str1)

str1 = "%-10sjane" % ("hi")
print(str1, len(str1))

print(f"{3.42134234:0.4f}")
str2 = f"{3.42134234:10.3f}"
print(str2, len(str2))
