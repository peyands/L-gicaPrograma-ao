
precos_tamanho = {
    '1': 20.00,  # Pequena
    '2': 30.00,  # Média
    '3': 40.00   # Grande

}

precos_ingredientes = {
    'Queijo': 3.00,
    'Pepperoni': 4.00,
    'Cogumelos': 2.50,
    'Azeitonas': 2.00,
    'Bacon': 5.00
}

def calcular_total():
    total = 0.00

    # Escolher tamanho da pizza
    print("Escolha o tamanho da pizza:")
    print("(1) Pequena - R$20.00")
    print("(2) Média - R$30.00")
    print("(3) Grande - R$40.00")
    
    tamanho = input("Digite o número do tamanho: ")
    
    if tamanho in precos_tamanho:
        total += precos_tamanho[tamanho]
    else:
        print("Tamanho inválido.")
        return

    # Escolher ingredientes adicionais
    print("Escolha os ingredientes adicionais (separados por vírgula):")
    print(", ".join(precos_ingredientes.keys()))
    
    ingredientes = input("Digite os ingredientes: ").split(", ")
    
    for ingrediente in ingredientes:
        if ingrediente in precos_ingredientes:
            total += precos_ingredientes[ingrediente]
        else:
            print(f"Ingrediente '{ingrediente}' não reconhecido. Ignorando.")

    # Mostrar valor total do pedido
    print(f"O valor total do seu pedido é: R${total:.2f}")

if == "_main_":
    calcular_total(print)