import flet as ft

def main(page: ft.Page):
    page.title = "Mini-dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Ejemplo de datos
    ventas = {"Enero": 1200, "Febrero": 1500, "Marzo": 1700}
    total = ft.Text(f"Total: ${sum(ventas.values())}")

    def actualizar(e):
        ventas["Abril"] = 1800
        total.value = f"Total: ${sum(ventas.values())}"
        page.update()

    # Elementos
    grafica = ft.Column(
        [ft.Text(f"{mes}: ${monto}") for mes, monto in ventas.items()]
    )
    boton = ft.ElevatedButton("Actualizar", on_click=actualizar)

    # Agregamos a la página
    page.add(grafica, total, boton)

ft.app(target=main)
