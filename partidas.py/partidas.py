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

choice = input(str("Opção: "))
if choice == 1:
        print(input("Mapa a visualizar: "))
elif input() == 2:
        if mapas > [8]:
            print("Limite antigido")
        while choice == 2:
            new_map = input("Mapa a adicionar: ")
        mapas.append(new_map)
        new_score = input("Pontos a adicionar: ")
        if new_score > 100:
            print("Pontuação inválida")
        pontos.append(new_score)
        print(mapas)
        print(pontos)
elif choice == 3:
        print("Até à próxima partida!")
else:
        print("Comando inválido")