# Operacyii s mnozhestvami
# - ob'edineniye     |
# - peresecheniye    &
# - raznost          -
#  i drugiye metodyi

max_things = {'Mobilnik', 'Britva', 'Rubashka', 'Shortyi'}
kate_things = {'Pomada', 'Zont', 'Mobilnik', 'Shortyi'}

# operacyia ob'edineniye | Povtoryayushiecya veshi otsutstvuyut v spiske
print(max_things|kate_things)
# peresecheniye  & Odikaviye veshi
print(max_things&kate_things)
# raznost - veshi kotoryie ne vzyala Kate
print(max_things-kate_things)