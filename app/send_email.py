import string
import random

N = 25
res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=N))

print("The generated random string : " + str(res))