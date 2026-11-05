# Técnica e armadilhas

## Como a página funciona

`assets/wakizashi_referencia.html` é o vídeo aprovado completo. `window.__setTime(t)` desenha o instante `t`, sempre o mesmo para cada tempo, então vários processos podem renderizar sem combinar nada entre si.

Partes para trocar em um vídeo novo:

| Nome | Para que serve |
|---|---|
| `DUR` | Duração em segundos |
| `SC` | Lista de cenas: `s` início, `e` fim, `dir` direção da câmera, `f()` retorna o HTML, `nofl` sem peças soltas, `a3` força do balanço, `push` avanço da câmera |
| `HITS` | `[tempo, força]` das batidas fortes; força 1 é a da logo |
| `FOC` | `[tempo, x, y]` da luz, com x de 0 a 1,78 e y de 0 a 1 |
| `BL` | Posição, ângulo e hora do corte da logo |
| `FL` | Palavras das peças de vidro soltas |
| `BEATS` | Batidas regulares: ajuste início e intervalo pelo `analisar.py` |

Ajudantes prontos: `rt` (texto letra a letra), `typed`, `cursor`, `roll`, `wave`, `tracks`, `burst`, `spring`, `eo`, `eio`, `P`, `fade`, `wrap`.

Para estudar vídeos enviados, use `scripts/analisar_video.py`. O corte de câmera atravessando as cenas não conta como corte seco, então um vídeo neste estilo pode mostrar poucos cortes mesmo com ritmo rápido. Olhe a folha.

Para vídeo vertical, os tamanhos estão fixos em 1920x1080 no CSS, em `render.py` e nas cenas. Conte com adaptação de verdade em vez de só trocar um número.

## Armadilhas que já custaram tempo

- **Canvas apagado no render:** o WebGL precisa de `--use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`, sem `--disable-gpu`, e de `preserveDrawingBuffer:true`.
- **Vidro sem cor:** `backdrop-filter` só enxerga o que está dentro da mesma raiz. O canvas fica fixo em `#stage` e só `#fg` é reescrito a cada quadro. Refazer o `innerHTML` do palco inteiro apaga o WebGL.
- **Texto sumindo em 3D:** `preserve-3d` cortava textos entre planos. Use `perspective()` em cada elemento.
- **Peças soltas em cima de títulos:** calcule a paralaxe a partir da câmera e mantenha as peças nas laterais.
- **Moiré:** linhas SVG finas em leque tremem depois de comprimir. Desenhe luz no shader, com queda suave.
- **Fundo em 1280x720:** é proposital. O fundo é suave, e isso mantém cerca de 3 s por quadro em um processo.
- **Filtro nas duas metades:** o filtro que rasga as letras fica no pai das metades e tem região larga (`brush2`). Com menos área, as metades somem ao chegar. No quadro final troque por uma cópia inteira para não sobrar emenda.
- **`drawtext` do ffmpeg:** falhou no Windows do criador por falta de fontconfig. Não escreva texto em folha de quadros por ele.
- **Glob do ffmpeg:** não funciona no Windows. Use sequência numerada.
- **`.mov` corrompido:** o primeiro pacote saiu sem índice e passou despercebido. `empacotar.py` confere com ffprobe, então não pule essa etapa.
- **Faixa curta:** a trilha pode sair uns décimos menor que o vídeo, então `mixar.py` completa com silêncio.
- **Scripts grandes pelo terminal:** aspas quebram o heredoc. Grave em arquivo com a ferramenta de escrita.
- **Python em temporário:** o primeiro ambiente ficou em uma pasta da sessão e some com ela. Use `preparar_ambiente.sh`.

## Tempo de render

1020 quadros em 6 processos levam cerca de 10 minutos. A renderização retoma de onde parou, porque pula quadros que já existem. Depois de mudar a animação, use uma pasta nova para não misturar quadros antigos.
