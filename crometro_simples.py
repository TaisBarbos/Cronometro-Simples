import time
import sys
import msvcrt # Módulo essencial para entrada não-bloqueante no Windows

def check_for_input():
    """Verifica se uma tecla foi pressionada (não-bloqueante, Windows)."""
    return msvcrt.kbhit()

def cronometro_crescente():
    """Conta o tempo para cima até o usuário pressionar qualquer tecla."""
    
    print("\n---------------------------------------------------------")
    print(" CRONÔMETRO DE MEDIÇÃO INICIADO! Pressione **QUALQUER TECLA** para PARAR.")
    print("---------------------------------------------------------")

    inicio = time.time()
    
    try:
        while True:
            # 1. Verifica a entrada do usuário
            if check_for_input():
                msvcrt.getch() # Limpa o buffer de teclas
                break
                
            # 2. Cálculo e exibição do tempo
            tempo_decorrido = time.time() - inicio
            
            # Formata o tempo para H:MM:SS.ms
            horas = int(tempo_decorrido // 3600)
            minutos = int((tempo_decorrido % 3600) // 60)
            segundos = tempo_decorrido % 60
            
            formato_tempo = f"{horas:02d}:{minutos:02d}:{segundos:.2f}"
            
            sys.stdout.write(f"\rTempo decorrido: {formato_tempo}")
            sys.stdout.flush()
            
            time.sleep(0.1) # Pausa curta para fluidez

        # 3. Finalização
        tempo_final = time.time() - inicio
        
        horas_f = int(tempo_final // 3600)
        minutos_f = int((tempo_final % 3600) // 60)
        segundos_f = tempo_final % 60
        
        formato_final = f"{horas_f:02d}:{minutos_f:02d}:{segundos_f:.2f}"
        
        sys.stdout.write(f"\r\n--- Cronômetro PARADO! ---\n")
        print(f"Tempo Total: {formato_final} (H:MM:SS.ms)")
        print("------------------------------------------")
        
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")


def cronometro_regressivo():
    """Conta o tempo a partir de um valor definido pelo usuário, permitindo parada manual."""
    
    while True:
        try:
            tempo_total = int(input("Digite o tempo em **segundos** para a contagem regressiva: "))
            if tempo_total < 1:
                print("O tempo deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")
    
    print(f"\n---------------------------------------------------------")
    print(f"1 INICIANDO Contagem Regressiva de {tempo_total} segundos...")
    print("Pressione **QUALQUER TECLA** para interromper.")
    print("---------------------------------------------------------")

    inicio = time.time()
    parado_manualmente = False
    
    while True:
        # 1. Verifica a entrada do usuário para parada
        if check_for_input():
            msvcrt.getch() # Limpa o buffer de teclas
            parado_manualmente = True
            break
        
        # 2. Cálculo do tempo restante
        tempo_decorrido = time.time() - inicio
        tempo_restante = tempo_total - tempo_decorrido
        
        if tempo_restante < 0:
            tempo_restante = 0
            break
            
        # 3. Formatação e exibição
        minutos = int(tempo_restante // 60)
        segundos = tempo_restante % 60
        formato_tempo = f"{minutos:02d}:{segundos:.1f}"
        
        sys.stdout.write(f"\rTempo restante: {formato_tempo}")
        sys.stdout.flush() 
        
        time.sleep(0.1) # Pausa curta para atualização

    # 4. Finalização
    if parado_manualmente:
        sys.stdout.write(f"\r\n--- Contagem Regressiva INTERROMPIDA! ---\n")
        
        minutos_r = int(tempo_restante // 60)
        segundos_r = tempo_restante % 60
        formato_restante = f"{minutos_r:02d}:{segundos_r:.1f}"
        
        print(f"Tempo restante ao parar: {formato_restante}")
    else:
        sys.stdout.write("\rContagem regressiva finalizada!           \n")
        print(" TEMPO ESGOTADO!")
    print("------------------------------------------")


def menu_principal():
    """Exibe o menu de opções e executa a escolha do usuário."""
    
    while True:
        print("\n===== ESCOLHA UMA OPÇÃO DE CRONÔMETRO =====")
        print("1. Cronômetro Crescente")
        print("2. Contagem Regressiva")
        print("3. Sair")
        print("==========================================")
        
        escolha = input("Digite o número da sua escolha: ")
        
        if escolha == '1':
            cronometro_crescente()
        elif escolha == '2':
            cronometro_regressivo()
        elif escolha == '3':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Executa o programa
menu_principal()