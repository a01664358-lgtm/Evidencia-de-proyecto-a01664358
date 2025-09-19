import pandas as pd

# Definir funciones
def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro


def circulo(radio):
    area = 3.1416 * radio ** 2
    perimetro = 2 * 3.1416 * radio
    return area, perimetro


def triangulo(base, altura):
    area = base * altura / 2
    # perímetro suponiendo triángulo rectángulo
    perimetro = base + altura + (base ** 2 + altura ** 2) ** 0.5
    return area, perimetro


# Función para cada fila del DataFrame
def calcular_area_perimetro(row):
    if row["FIGURA"] == "r":
        return rectangulo(row["MEDIDA1"], row["MEDIDA2"])
    elif row["FIGURA"] == "c":
        return circulo(row["MEDIDA1"])
    elif row["FIGURA"] == "t":
        return triangulo(row["MEDIDA1"], row["MEDIDA2"])
    else:
        return None, None


if __name__ == "__main__":
    try:
        # Leer CSV (debe estar en la misma carpeta que este .py)
        df = pd.read_csv("figuras.csv")
        print("✅ El archivo ha sido leído correctamente.\n")

        # Calcular área y perímetro
        df[["AREA", "PERIMETRO"]] = df.apply(
            lambda row: pd.Series(calcular_area_perimetro(row)), axis=1
        )

        # Mostrar resultados
        print("📊 Resultados calculados:")
        print(df)

        # Guardar en un nuevo archivo
        df.to_csv("resultados.csv", index=False)
        print("\n💾 Resultados guardados en 'resultados.csv'")

    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'figuras.csv'.")
        print("Asegúrate de que esté en la misma carpeta que este script.")
