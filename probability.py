import enum, random


class Kid(enum.Enum):

       BOY = 0
       GIRL = 1

def random_kid()  -> Kid:
   return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
either_girl = 0
older_girl = 0


random.seed(0)

for _ in range(10000):
     younger = random_kid()
     older = random_kid()

     if older == Kid.GIRL:
      older_girl += 1
     if older == Kid.GIRL  and younger == Kid.GIRL:
      both_girls += 1
     if  older == Kid.GIRL  or younger == Kid.GIRL:
      either_girl += 1

#both children are girls and the older child is a girl
print("P(both | older):", both_girls / older_girl)

#“both children are girls and at least one of the children is a girl
print("P(both | either):", both_girls / either_girl)
