name = "Harry"
# first function of len =length
print(len(name))

# second .endswith return me true ya false hoga or same startswith me
print(name.endswith("rry"))
print(name.startswith("ha"))#ye false hoga qki h small likha he
Name = "harry"
print(Name.capitalize())

# chatgpt se copy
s = "  hello, World!  "
print(s.strip().title())  # -> "Hello, World!" extra space clear krata hai
print("-".join(s.split()))  # -> "hello,-World!"is me {","} lagta hai
print(s.replace("World", "Python"))  # -> "  hello, Python!  " replace karta hai
print("123".isdigit(), "abc".isalpha())  # -> True False
txt = "one,two,three".split(",")
print(txt[::-1])  # -> ['three','two','one']
