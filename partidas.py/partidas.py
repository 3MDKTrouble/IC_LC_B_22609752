max_partidas = 8
pontos_max = 100

mapas = ["Deserto", "Floresta", "Vulcão"]
pontos = [45, 80, 62]
m = 0
p = 0
index = 0

print("===== REGISTO DE PARTIDAS =====")
print("1 - Ver estatísticas")
print("2 - Registar partida")
print("3 - Sai")

while True:
    choice = input(str("Opção: "))
    if choice(input()) == 1:
        print(input("Mapa a visualizar: "))
    elif input() == 2:
        if mapas > [8]:
            print("Limite antigido")
        while choice(input()) == 2:
            print(input("Mapa: "))
        mapas.append(input())
        print(input("Pontos: "))
        pontos.append(input())
        print(mapas)
        print(pontos)
    elif choice(input()) == 3:
        print("Até à próxima partida!")
    else:
        print("Comando inválido")