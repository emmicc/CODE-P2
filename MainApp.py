from Operations import Operations
class MainApp:
    
    @staticmethod
    def mostrar_menu(incluirPn):
        print("\n--- Menú de Operaciones ---")
        print("1. Longitud promedio de la línea (Lq)")
        print("2. Tiempo de espera promedio (Wq)")
        print("3. Longitud promedio del sistema (Ls)")
        print("4. Tiempo de espera promedio del sistema (Ws)")
        print("5. Porcentaje de ocupación del servidor (U)")
        print("6. Probabilidad de que haya personas esperando (PLs)")
        print("7. Tiempo de distracción (ocio)")
        if incluirPn:
            print("8. Probabilidad de n clientes en el sistema (Pn)")
        print("9. Mostrar todos los resultados")
        print("0. Salir")
        print("Seleccione una opción: ", end="")

    @staticmethod
    def mostrar_todos_los_resultados(operations, incluirPn):
        print("\n--- Resultados Completos ---")
        print("Longitud promedio de la línea (Lq):", operations.Lq())
        print("Tiempo de espera promedio (Wq):", operations.Wq(), "minutos")
        print("Longitud promedio del sistema (Ls):", operations.Ls(), "clientes")
        print("Tiempo de espera promedio del sistema (Ws):", operations.Ws(), "minutos")
        print("Porcentaje de ocupación del servidor (U):", operations.U(), "%")
        print("Probabilidad de que haya personas esperando (PLs):", operations.PLs(), "%")
        print("Tiempo de distracción (ocio):", operations.ocio(), "%")
        if incluirPn:
            print(f"Probabilidad de {int(operations.n)} clientes en el sistema (Pn):", operations.Pn(), "%")
        print("-----------------------------\n")

    @staticmethod
    def main():
        # Pedir valores de A y S
        A = Operations.leer_numero_positivo("A")
        S = Operations.leer_numero_positivo("S")

        # Preguntar si se desea calcular Pn
        incluirPn = False
        n = 1  # Valor predeterminado para n

        respuesta = input("¿Desea calcular Pn? (si/no): ").strip().lower()
        if respuesta == "si":
            incluirPn = True
            n = Operations.leer_numero_positivo("n")

        # Crear instancia de Operations con los valores de A, S y n
        operations = Operations(A, S, n)

        while True:
            MainApp.mostrar_menu(incluirPn)
            try:
                opcion = int(input())
            except ValueError:
                print("Opción no válida. Por favor, elige una opción correcta.")
                continue

            if opcion == 1:
                print("La longitud promedio de la línea es:", operations.Lq())
            elif opcion == 2:
                print("El tiempo de espera promedio es de:", operations.Wq(), "minutos")
            elif opcion == 3:
                print("La longitud promedio del sistema es de", operations.Ls(), "clientes")
            elif opcion == 4:
                print("El tiempo de espera promedio del sistema es de", operations.Ws(), "minutos")
            elif opcion == 5:
                print("El porcentaje de tiempo que el servidor está ocupado es de:", operations.U(), "%")
            elif opcion == 6:
                print("La probabilidad de que haya personas esperando es de:", operations.PLs(), "%")
            elif opcion == 7:
                print("El tiempo de distracción es de", operations.ocio(), "%")
            elif opcion == 8:
                if incluirPn:
                    print(f"La probabilidad de que haya {int(n)} clientes en el sistema es de:", operations.Pn(), "%")
                else:
                    print("Opción no válida. Por favor, elige una opción correcta.")
            elif opcion == 9:
                MainApp.mostrar_todos_los_resultados(operations, incluirPn)
            elif opcion == 0:
                Lq = operations.Lq()
                LqRedondeado = operations.redondear_hacia_abajo(Lq)
                print(f"En conclusión, el cliente promedio espera {operations.Wq()} minutos\n"
                      f"antes de ser servido. En promedio hay {LqRedondeado} clientes en la línea \n"
                      f"y {operations.Ls()} en el sistema. El proceso completo lleva un \n"
                      f"promedio de {operations.Ws()} minutos. La caja está ocupada \n"
                      f"el {operations.U()}% y finalmente el {operations.PLs()}%\n\n")
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elige una opción correcta.")

if __name__ == "__main__":
    MainApp.main()
