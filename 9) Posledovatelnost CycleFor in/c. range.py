# eto - funkciya
# Pozvolyaet sozdat posledovatelnost celiyh chisel
# Chashe vsego ispolzuetsya s ciklom for

# parametry
# range (start_or_stop, stop[, step])
# start_or_stop - nachalo ili konecy posledovatelnosti
# stop - konecy
# step - shag


# for vs for range vs while

# for - perebor posledovatelnosti. Index ne nuzhen.
# for range - perebor posledovatelnosti. Nuzhen index.
# for range - neobhodimo propustit nekotoriye elementiy ili idti s koncya v nachalo
# while - cycle svyazan s usloviem, no ne s posledovatelnostyu


numbers = range(10)
print(numbers)
print(type(numbers))

print(list(numbers))

numbers = reversed(range(10, 50))
print(numbers)
print(type(numbers))

print(list(numbers))