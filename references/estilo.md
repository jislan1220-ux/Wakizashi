# Estilo aprovado

Tudo aqui veio de pedidos e reações do criador da skill, Victor (@diasl_uisvictor), ao fazer o Claude Wakizashi parte 2 (05/11/2026). Os valores são um ponto de partida; a régua é o resultado visto.

## O que define o estilo

- Fundo quase preto com luz verde e azul-petróleo.
- Cada cena tem um objeto de interface que conta a história: terminal, arquivo com a linha trocada, onda sonora real, painéis, curva de animação, caixa de comentário.
- Texto médio, sem caixa alta, entrando letra a letra. A palavra importante fica em verde.
- Cor só com significado: vermelho é erro, verde é solução.
- Vidro de iPhone "só um toque": sutil, com um filete claro na borda de cima, sem virar efeito principal.
- Nenhum corte seco: a câmera atravessa de uma cena para a outra.

## O que ele rejeitou, e por quê

| Tentativa | Reação | O que fazer no lugar |
|---|---|---|
| Tech-HUD laranja, quase só texto grande | "Achei genérica" | Um objeto de interface conduzindo cada cena |
| Bolhas verdes borradas de fundo | "O blur verde tá estourado" | Luz líquida contínua, sem bolha redonda e com teto de brilho |
| Fundo parado | Quer "dinâmico" para "sentir a cor do vidro" | Fundo segue a música e a luz fica atrás do painel da cena |
| Animação calma | "Um pouco lenta", quer prender quem vê | Trocas de cerca de 0,24 s, molas curtas, algo acontecendo o tempo todo |
| Movimento plano | "Quero mais 3D" | Rotações fortes na troca e peças soltas em profundidade |
| Clarão de tela cheia na logo com leque de linhas | "Muito artificial" | Corte de lâmina (receita abaixo) |
| Nome pequeno, digitado no fim da cena | "Não esquece de botar meu nome" | Crédito maior e completo pelo menos 0,45 s antes da troca |
| Luz texturizada como tinta ou mármore | Avaliação minha nos testes: briga com o texto | Luz suave, poucos detalhes |
| Mesma luz, baixa demais | Avaliação minha nos testes: vidro perde a cor | Conferir a cor atrás de cada painel |

## Receita do fundo

Luz líquida com distorção do próprio ruído, em duas camadas com velocidades de câmera diferentes, o que dá profundidade.

- Velocidade: acumula os picos da música, então acelera nas partes fortes sem saltar.
- Foco: a luz concentra atrás do painel da cena (`FOC`) e passeia entre eles.
- Câmera: cada troca de cena desloca o fundo na mesma direção (`uP`).
- Impacto: cada batida forte (`HITS`) solta uma onda que empurra a luz e acelera o fluxo.
- Teto de brilho por curva suave, para nunca estourar.
- Grão fino para não aparecer faixa de cor no degradê.

Em cenas com texto verde grande, confira se a luz atrás não apaga o texto.

## Receita da logo: corte de lâmina

Dura cerca de 1,5 s até o impacto e mais 0,9 s depois, com o impacto em uma batida forte da música.

1. **Tensão:** o fundo apaga até cerca de 36% e sobra um fio de luz fino crescendo, com um brilho correndo por ele. O nome da marca acima entra pouco antes.
2. **Respiro:** o fio some nos dois ou três últimos quadros antes do impacto.
3. **Corte:** o fio cruza a tela inteira, com brilho forte e clarão vindo só dele, misturado a ruído. A luz nasce do fio e cai com a distância; a tela nunca fica lisa.
4. **Encaixe:** a palavra chega em duas metades separadas pelo fio, deslizando em direções opostas por cerca de 0,26 s até se encaixarem. Leva rastro, separação de cor vermelha e ciano por uns quadros e uma tremida curta.
5. **Rescaldo:** cerca de 110 faíscas saem do fio, um brilho varre as letras, o fundo volta e o crédito é digitado rápido.

Som do impacto: riser subindo até a batida, whoosh reverso um pouco antes, whoosh grave e clique grave no ponto exato.

## Áudio

- A música entra no ponto indicado e não do começo do arquivo.
- Ele pediu a música mais baixa, o SFX mais alto e a trilha "indo para os dois lados do ouvido, tipo 3D", e aprovou esse resultado. Os graves ficam parados no centro para o efeito não incomodar.
- Trilha abaixa sozinha sob a voz e sobe na chamada final.
- Master final em -14 LUFS, pico em -1 dB.

### Efeitos (aprendido no vídeo Higgsfield + Claude, aprovado na versão final)

- **Um efeito para cada coisa que acontece na tela, e só ali.** Antes de montar o `sfx.json`, faça o mapa visual do vídeo pronto: uma grade de quadros a 2 fps com o tempo escrito em cada um, mais os picos de diferença entre quadros (cortes, flashes, lasers). Ligue cada evento a um som:
  - corte → whoosh atravessando de um lado para o outro;
  - laser ou lâmina → blade whoosh;
  - chip, menu, caixa de texto, botão → tique ou pop seco de interface;
  - tela forte (clarão, tela de cor) → riser curto, de no máximo 1,5 s, chegando na batida;
  - cena gerada (dragão, fogo, vento) → o som da própria cena.
- **Texto cinético palavra por palavra leva um toque de digitação de interface em cada palavra.** Foi o detalhe que o criador mais gostou ("fica foda"). Use eventos `{"tecla": [tempos das palavras], "db": ...}` do `mixar.py`, com os tempos da transcrição. O toque fica baixinho, com um pouco de sala (reverb), em 3 ou 4 tons levemente diferentes e alternando de lado, um pouco mais alto nas palavras de destaque. Não toque duas vezes no mesmo instante nem em cima de outro som de interface.
- **Peso vem do grave, não do volume.** Whooshes finos, só de ar, parecem baixos mesmo com +3 dB. Prefira whooshes com corpo abaixo de 120 Hz. Se a pessoa disser que o efeito está baixo, troque por sons mais graves antes de só subir o volume.
- **Sem exagero de trailer.** Impactos pesados de trailer em telas de cor e riser de sci-fi com sub na logo foram reprovados. Na revelação da logo ficaram blade whoosh, um boom suave e sinos. Nunca ponha impacto sem algo forte na imagem, nem riser longo crescendo por baixo da voz na abertura.
- **Cenas geradas bem presentes.** O momento forte da cena (no caso, a rosnada do dragão) fica uns 8 dB acima dos outros sons da cena, com um grave embaixo, para a pessoa sentir o impacto. O resto do som da cena fica com pouco eco.
- **Trilha limpa.** Leve, quase sem reverb, girando devagar em volta da cabeça.
- **Pacote de efeitos como referência.** Se a pessoa mandar um pacote, meça cada pasta (volume, grave abaixo de 120 Hz, brilho, largura estéreo), compare com os efeitos em uso e troque só os sons, mantendo a marcação de tempo aprovada. Mudança só de som não precisa de render novo: remonte o vídeo com o áudio novo usando `-c:v copy`.

## Entrega

Sempre com arquivo editável: vídeo em ProRes, faixas separadas e FCPXML, além de uma versão com áudio junto. O fundo fica embutido, porque o vidro depende dele.

Texto digitado pela pessoa vale mais que a transcrição. Antes de terminar, aponte qualquer diferença entre o texto na tela e o que a transcrição ouviu.
