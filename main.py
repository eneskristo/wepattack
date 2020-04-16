import router
from utils import Utils

utils = Utils()
a = router.Router(256, utils.keygenFromWord("Key"))
print(a.encrypt("Plaintext"))
with open("beemovie.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
while "" in content:
    content.remove("")
print(content)
for c in content:
    print(a.encrypt(c))
