#HOLA ENTE
class Arca: 
    def __init__(self, capacidad_maxima):
        self.animales = []
        self.alimentos = []
        self.agua = 0
        self.capacidad_maxima = capacidad_maxima

    def agregar_animal(self, animal):
        if len(self.animales) + len(self.alimentos) < self.capacidad_maxima:
            self.animales.append(animal)
            print(f"{animal.nombre} ha sido agregado al arca.")
        else:
            print("No se puede agregar más animales. Capacidad máxima alcanzada.")

    def agregar_alimento(self, alimento):
        if len(self.animales) + len(self.alimentos) < self.capacidad_maxima:
            self.alimentos.append(alimento)
            print(f"{alimento.tipo} ha sido agregado al arca.")
        else:
            print("No se puede agregar más alimentos. Capacidad máxima alcanzada.")

    def agregar_agua(self, cantidad):
        self.agua += cantidad
        print(f"{cantidad} unidades de agua han sido agregadas al arca.")

    def alimentar_animal(self, animal):
        if animal in self.animales:
            for alimento in self.alimentos:
                if alimento.cantidad > 0:
                    animal.alimentar()
                    alimento.usar(1)  # Usar una unidad de alimento
                    print(f"{animal.nombre} ha sido alimentado.")
                    return
            print(f"No hay alimento disponible para {animal.nombre}.")
        else:
            print(f"{animal.nombre} no está en el arca.")

    def dar_agua(self, animal):
        if animal in self.animales and self.agua > 0:
            animal.dar_agua()
            self.agua -= 1  # Usar una unidad de agua
            print(f"{animal.nombre} ha recibido agua.")
        else:
            print(f"No hay agua disponible para {animal.nombre}.")

    @staticmethod
    def estado_arca(arca):
        return {
            "Número de animales": len(arca.animales),
            "Número de alimentos": len(arca.alimentos),
            "Cantidad de agua": arca.agua
        }


class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 5  # Nivel de hambre inicial
        self.sed = 5     # Nivel de sed inicial

    def alimentar(self):
        self.hambre = max(0, self.hambre - 1)  # Reducir hambre

    def dar_agua(self):
        self.sed = max(0, self.sed - 1)  # Reducir sed

    def estado(self):
        return {
            "Nombre": self.nombre,
            "Tipo": self.tipo,
            "Hambre": self.hambre,
            "Sed": self.sed
        }


class Alimento:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad

    def usar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            print("No hay suficiente alimento disponible.")

    @staticmethod
    def es_alimento_adecuado(tipo_animal):
        return tipo_animal in ["perro", "gato", "conejo", "pájaro"]


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")


class Heno(Alimento):
    def __init__(self, cantidad):
        super().__init__("Heno", cantidad)


class Croquetas(Alimento):
    def __init__(self, cantidad):
        super().__init__("Croquetas", cantidad)


def mostrar_estado_animales(arca):
    if arca.animales:
        for animal in arca.animales:
            print(animal.estado())
    else:
        print("No hay animales en el arca.")


def menu():
    arca = Arca(capacidad_maxima=10)

    while True:
        print("\n--- Menú del Arca de Noé ---")
        print("1. Agregar Animal")
        print("2. Agregar Alimento")
        print("3. Agregar Agua")
        print("4. Alimentar Animal")
        print("5. Dar Agua a Animal")
        print("6. Ver Estado del Arca")
        print("7. Mostrar Estado de Animales")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del animal: ")
            tipo = input("Ingrese el tipo de animal (perro/gato): ").lower()
            if tipo == 'perro':
                animal = Perro(nombre)
            elif tipo == 'gato':
                animal = Gato(nombre)
            else:
                print("Tipo de animal no válido.")
                continue
            arca.agregar_animal(animal)

        elif opcion == '2':
            tipo_alimento = input("Ingrese el tipo de alimento (heno/croquetas): ").lower()
            cantidad = int(input("Ingrese la cantidad de alimento: "))
            if tipo_alimento == 'heno':
                alimento = Heno(cantidad)
            elif tipo_alimento == 'croquetas':
                alimento = Croquetas(cantidad)
            else:
                print("Tipo de alimento no válido.")
                continue
            arca.agregar_alimento(alimento)

        elif opcion == '3':
            cantidad = int(input("Ingrese la cantidad de agua a agregar: "))
            arca.agregar_agua(cantidad)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del animal a alimentar: ")
            for animal in arca.animales:
                if animal.nombre == nombre:
                    arca.alimentar_animal(animal)
                    break
            else:
                print(f"No se encontró un animal llamado {nombre}.")

        elif opcion == '5':
            nombre = input("Ingrese el nombre del animal a dar agua: ")
            for animal in arca.animales:
                if animal.nombre == nombre:
                    arca.dar_agua(animal)
                    break
            else:
                print(f"No se encontró un animal llamado {nombre}.")

        elif opcion == '6':
            estado = Arca.estado_arca(arca)
            print(f"Número de animales: {estado['Número de animales']}")
            print(f"Número de alimentos: {estado['Número de alimentos']}")
            print(f"Cantidad de agua: {estado['Cantidad de agua']}")

        elif opcion == '7':
            mostrar_estado_animales(arca)

        elif opcion == '8':
            print("Saliendo del programa. ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 8.")


# Ejecutar el menú
menu()
