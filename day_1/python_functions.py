#1. Parameters vs Arguments 

def greet(name): #Parameter
  print("Hello ,"+name)

greet("Vignesh") #Argumennt

def artificial_planet(name, position="10.5 11.3"):
  print(f"The planet {name} is located at {position} position.")

artificial_planet("Planet 10") #Default type

artificial_planet(position="9.8 6.5", name="Planet Z") #Keyword type

artificial_planet("ShipX", "-10.2 0.2") #Positional type
  