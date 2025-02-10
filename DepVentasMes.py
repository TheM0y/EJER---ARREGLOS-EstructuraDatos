import json
import os

class Tienda:
    def __init__(self, archivo="ventas.json"):
        self.archivo = archivo
        self.departamentos = ["Ropa", "Deportes", "Jugueteria"]
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.ventas = self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            self.ventas = {d: {mes: [] for mes in self.meses} for d in self.departamentos}
            self.guardar_datos()
        try:
            with open(self.archivo, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {d: {mes: [] for mes in self.meses} for d in self.departamentos}

    def guardar_datos(self):
        with open(self.archivo, "w") as f:
            json.dump(self.ventas, f, indent=4, ensure_ascii=False)

    def insertar_venta(self, departamento, mes, item, precio):
        if departamento in self.ventas and mes in self.meses:
            self.ventas[departamento][mes].append((item, precio))
            self.guardar_datos()
            print(f"Venta añadida: {item} (${precio}) en {departamento}, mes {mes}.")
        else:
            print("Departamento o mes inválido.")

    def eliminar_venta(self, departamento, mes, item):
        if departamento in self.ventas and mes in self.meses:
            ventas_mes = self.ventas[departamento][mes]
            for venta in ventas_mes:
                if venta[0] == item:
                    ventas_mes.remove(venta)
                    self.guardar_datos()
                    print(f"Venta eliminada: {item} en {departamento}, mes {mes}.")
                    return
            print("Venta no encontrada.")
        else:
            print("Departamento o mes inválido.")

    def buscar_venta(self, departamento, mes, item):
        if departamento in self.ventas and mes in self.meses:
            ventas_mes = self.ventas[departamento][mes]
            for venta in ventas_mes:
                if venta[0] == item:
                    print(f"Venta encontrada: {item} (${venta[1]}) en {departamento}, mes {mes}.")
                    return venta
            print("Venta no encontrada.")
        else:
            print("Departamento o mes inválido.")

    def mostrar_ventas(self):
        for departamento, meses in self.ventas.items():
            print(f"\nVentas en {departamento}:")
            for mes, ventas in meses.items():
                print(f"  {mes}: {ventas if ventas else 'Sin ventas'}")

    def menu(self):
        while True:
            print("\n--- Menú de Ventas ---")
            print("1. Insertar venta")
            print("2. Eliminar venta")
            print("3. Buscar venta")
            print("4. Mostrar ventas")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion in ["1", "2", "3"]:
                print("Seleccione el departamento:")
                for i, dep in enumerate(self.departamentos, 1):
                    print(f"{i}. {dep}")
                dep_index = int(input("Ingrese el número del departamento: ")) - 1
                if 0 <= dep_index < len(self.departamentos):
                    departamento = self.departamentos[dep_index]
                else:
                    print("Selección inválida.")
                    continue
                
                print("Seleccione el mes:")
                for i, mes in enumerate(self.meses, 1):
                    print(f"{i}. {mes}")
                mes_index = int(input("Ingrese el número del mes: ")) - 1
                if 0 <= mes_index < len(self.meses):
                    mes = self.meses[mes_index]
                else:
                    print("Selección inválida.")
                    continue
                
                if opcion == "1":
                    item = input("Ingrese el nombre del artículo: ")
                    precio = float(input("Ingrese el precio: "))
                    self.insertar_venta(departamento, mes, item, precio)
                elif opcion == "2":
                    item = input("Ingrese el nombre del artículo a eliminar: ")
                    self.eliminar_venta(departamento, mes, item)
                elif opcion == "3":
                    item = input("Ingrese el nombre del artículo a buscar: ")
                    self.buscar_venta(departamento, mes, item)
            
            elif opcion == "4":
                self.mostrar_ventas()
            
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción no válida. Intente de nuevo.")

tienda = Tienda()
tienda.menu()
