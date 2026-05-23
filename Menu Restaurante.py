#Menu Restaurante
# Encabezado en consola
print("=" * 60)
print("              MENÚ DE RESTAURANTE - PROMOCIÓN")
print("=" * 60)

# Matriz de productos: [Nombre, Categoría, Precio Base]
menu = [
    ["Hamburguesa", "Comida Rápida", 30000],
    ["Pizza", "Comida Rápida", 21000],
    ["Ensalada", "Saludable", 12000],
    ["Sopa", "Tradicional", 10000],
    ["Jugo Natural", "Bebida", 8000],
    ["Café", "Bebida", 6000]
]

# Categoría objetivo y umbral
categoria_objetivo = "Comida Rápida"
umbral_precio = 20000

# Función para calcular precio final
def calcular_precio_final(producto):
    nombre, categoria, precio_base = producto
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        precio_final = precio_base * 0.85  # aplica 15% descuento
    else:
        precio_final = precio_base
    return precio_final

# Encabezado de la tabla
print(f"{'Producto':<15}{'Categoría':<20}{'Precio Base':<15}{'Precio Final':<15}")
print("-" * 60)

# Mostrar resultados organizados
for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(producto)
    print(f"{nombre:<15}{categoria:<20}${precio_base:<14}{'$'+str(int(precio_final)):<15}")  