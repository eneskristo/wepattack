import router
from utils import Utils
from hack import Hack

utils = Utils()
a = router.Router(256, utils.keygenFromWord("Blank"))
print(a.encrypt("Plaintext"))
print(a.decrypt(a.encrypt("Plaintext")))
with open("beemovie.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
while "" in content:
    content.remove("")
hackIt = Hack(3,5, 256, "s")
for i in range(300):
    print("iter ", i)
    for c in content:
        hackIt.getPacket(a.encrypt(c))
print(hackIt.solveWEP())
