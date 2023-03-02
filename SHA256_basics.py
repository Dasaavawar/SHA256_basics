# Python - SHA256 Hashing Algorithm: Basics


# Python SHA256 for a Single String

# Hash a single string with hashlib.sha256
import hashlib

a_string = 'this string holds important and private information'

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)

# Returns:
# 4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1


# Python SHA256 for an Entire File

# Hash a file with hashlib.sha256
import hashlib

with open('/Users/datagy/Desktop/sample.txt', 'rb') as f:
    for line in f:
        hashed_line = hashlib.sha256(line.rstrip()).hexdigest()
        print(hashed_line)


# Python SHA256 with Unicode Strings

# Hash a single string with hashlib.sha256
import hashlib

a_string = 'this string holds important and private information'

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)

# Returns:
# 4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1

# Hash a list of strings with hashlib.sha256
import hashlib

strings = ['this string holds important and private information', 'this is another string', 'and yet another secret string']
hashed_strings = []

for string in strings:
    hashed_strings.append(hashlib.sha256(string.encode('utf-8')).hexdigest())
print(hashed_strings)

# Returns:
# ['4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1', 'adc93c2130934bbb28f652d77980e94d65e4b9b44e6100484ca2e77ab432caa1', 'd16bdaf20806fd89f9a08eec1c9002a12c1c5978157b25f40e79e42a76013a31']


# Python SHA256 a Pandas Column

# Hashing a Pandas Dataframe column with SHA256
import hashlib
import pandas as pd

df = pd.DataFrame.from_dict({
    'ID': [1,2,3,4,5,6,7],
    'Password': ['cookies', 'ponies', 'iloveyou123', 'p4ssw0rd', 'passwordsaresilly!', 'ilikecoffee987', 'spaceagents444']
})

print(df.head())

# Returns
#    ID            Password
# 0   1             cookies
# 1   2              ponies
# 2   3         iloveyou123
# 3   4            p4ssw0rd
# 4   5  passwordsaresilly!

def hash_unicode(a_string):
    return hashlib.sha256(a_string.encode('utf-8')).hexdigest()

df['Hashed Password'] = df['Password'].apply(hash_unicode)

print(df.head())

# Returns:
#    ID            Password                                    Hashed Password
# 0   1             cookies  2f0030c535193fc164e4e2b5371e8e676510cf0a64b268...
# 1   2              ponies  ebe85ca5dd0d48cd1fb0f96853830536283aba62425dd8...
# 2   3         iloveyou123  dce7a17f9bff4aa7efebf32c3b3a082033be7e5f103143...
# 3   4            p4ssw0rd  48d2a5bbcf422ccd1b69e2a82fb90bafb52384953e77e3...
# 4   5  passwordsaresilly!  62e8c65bda8914ab8f76dd5d94136d056d19f04861ce18...


