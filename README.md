# Cronômetro Simples 🕒

Descrição: pequeno utilitário em Python para medir tempo com duas opções — cronômetro crescente (conta o tempo até que o usuário pare) e contagem regressiva (a partir de um tempo em segundos definido pelo usuário).

---

## ✅ Funcionalidades

- Cronômetro crescente: inicia a contagem e exibe o tempo decorrido em H:MM:SS.ms até que o usuário pressione qualquer tecla para parar.
- Contagem regressiva: o usuário informa um tempo em segundos; o programa decrementa até zero mostrando minutos e segundos, podendo ser interrompido pelo usuário a qualquer momento.

## ⚙️ Requisitos

- Python 3.6+ (testado com CPython no Windows)
- Plataforma: Windows (usa o módulo interno `msvcrt` para leitura não-bloqueante do teclado). Em macOS/Linux é preciso adaptar a leitura de teclado (ex.: biblioteca `keyboard`, `pynput` ou `curses`).

## 📦 Arquivos

- `crometro_simples.py` — script principal (interface de linha de comando interativa).

## ▶️ Como executar

1. Abra o PowerShell (Windows) no diretório do projeto.
2. Execute:

```powershell
python .\crometro_simples.py
```

3. Siga o menu na tela e escolha:
- 1 — Cronômetro Crescente
- 2 — Contagem Regressiva
- 3 — Sair

Para parar o cronômetro crescente ou interromper a contagem regressiva pressione qualquer tecla.

## ✍️ Exemplos de uso

- Cronômetro crescente: escolha a opção 1 no menu. O programa exibirá o tempo em H:MM:SS.ms (atualizado a cada 0.1s). Para parar, pressione qualquer tecla.
- Contagem regressiva: escolha a opção 2 e informe o tempo em segundos (por exemplo `90` → 1 minuto e 30 segundos). A contagem exibirá `MM:SS.s` e terminará em `0` ou se você pressionar uma tecla.

## 📝 Observações e melhorias possíveis

- Atualmente o projeto depende de `msvcrt`, logo roda apenas no Windows sem mudanças.
- Para rodar no macOS/Linux: substituir a lógica de input não-bloqueante por outra biblioteca (ex.: `keyboard`, ou usar threads para input com timeout) ou usar `curses` para uma interface de terminal onde disponível.
- Melhorias possíveis:
  - Adicionar suporte multiplataforma.
  - Adicionar argumentos de linha de comando (ex.: `--start-countdown 60`).
  - Registrar tempos/voltar para múltiplas voltas (lap times).




