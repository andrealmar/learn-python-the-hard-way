# -*- coding: utf-8 -*-

# atribui o valor 100 à variável cars
cars = 100

# atribui o valor float 4.0 à variável space_in_a_car
space_in_a_car = 4.0

# atribui o valor 30 à variável drivers
drivers = 30

# atribui o valor 90 à variável passengers
passengers = 90

# atribui o valor da subtração (cars - drivers) que é = 70 à variável drivers
cars_not_driven = cars - drivers

# atribui o valor da variável drivers que no caso é 30 à variável cars_driven
cars_driven = drivers

# atribui o valor multiplicação cars_driven x space_in_a_car que é = 120 à
# variável carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# atribui o valor da divisão passengers / cars_driven que é 3
# à variável average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
