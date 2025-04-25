from browser import document, alert, html

def calcular_conceito(nota):
    if nota < 15:
        return "insuficiente"
    elif nota < 21:
        return "regular"
    elif nota < 27:
        return "bom"
    else:
        return "excelente"

def exibir_resultados(ev):
    try:
        nota_total = 0
        for i in range(1, int(document["avaliacao"].value) + 1):
            valor = float(document[f"nota{i}"].value)
            nota_total += valor

        conceito = calcular_conceito(nota_total)
        media = round(nota_total / 3, 2)

        resultado = f"\nSeu conceito até o momento é {conceito} com média {media}\n"

        if conceito != "excelente":
            resultado += "Para alcançar os próximos conceitos você precisa de:\n"
            if conceito == "insuficiente":
                resultado += f"- Regular: {round(15 - nota_total, 2)} pontos\n"
            if conceito in ["insuficiente", "regular"]:
                resultado += f"- Bom: {round(21 - nota_total, 2)} pontos\n"
            if conceito in ["insuficiente", "regular", "bom"]:
                resultado += f"- Excelente: {round(27 - nota_total, 2)} pontos\n"
        else:
            resultado += "Parabéns! Você já foi aprovado com Excelente.\n"

        document["resultado"].text = resultado

    except Exception as e:
        alert(f"Erro ao calcular: {e}")

def gerar_campos(ev):
    try:
        container = document["notas-container"]
        container.clear()
        qtd = int(document["avaliacao"].value)
        for i in range(1, qtd + 1):
            container <= html.LABEL(f"Nota da Avaliação {i}:")
            container <= html.INPUT(type="number", id=f"nota{i}", min="0", max="10", step="0.1")
        document["calcular"].style.display = "inline"
    except Exception as e:
        alert(f"Erro: {e}")

document["calcular"].bind("click", exibir_resultados)
document["calcular"].bind("touchend", exibir_resultados)
document["avaliacao"].bind("change", gerar_campos)
