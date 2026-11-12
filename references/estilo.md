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
- Aprovado no vídeo Higgsfield + Claude (v24 a v27): trilha limpa e leve, sem pad grave e quase sem reverb, girando devagar em volta da cabeça (uma volta a cada 14 s). Poucos efeitos, um por momento, sem empilhar camadas: um whoosh por corte atravessando de um lado para o outro, riser + impacto na entrada de cada cena forte, cliques de interface baixinhos. Os sons das cenas (vento, rugido, passos) ficam baixos, de 6 a 8 dB abaixo da música e com pouco eco.
- Peso do efeito vem do grave, não do volume. O Victor achou os efeitos baixos com whooshes finos (de ar); com +3 dB ainda pareciam baixos. A referência dele é um pacote de efeitos de trailer em que os whooshes, impactos e risers têm a maior parte da energia abaixo de 120 Hz. Prefira esse tipo de som: whoosh grave nos cortes, impacto de sub na batida, riser largo chegando na batida. Nível de partida dos efeitos: 4 a 5 dB abaixo da voz (`mix_3d.py --sfx_lufs -26.5` com a voz em -19,5 LUFS).
- Nos sons de interface, o Victor prefere o pacote "ui sfx" dele (Epidemic Sound e afins: slide whoosh, Sci-Fi Riser, blade whoosh, cliques e pop-ups curtos, "Happy Twinkle" para recompensa). Ele quer sentir o impacto dos momentos fortes da cena: a rosnada do dragão ficou 8 dB acima dos outros sons da cena, com um sub embaixo.
- Efeito só onde acontece algo na tela. Antes de mixar, faça o mapa visual do vídeo pronto (grade de quadros a 2 fps com o tempo escrito e picos de diferença entre quadros) e ligue cada evento a um som: corte = whoosh; laser = blade whoosh; chip, menu e caixa de texto = tique ou pop seco de interface; tela forte = riser curto (no máximo 1,5 s) + impacto. Nunca ponha impacto sem algo forte na imagem nem riser longo crescendo por baixo da voz na abertura: o Victor achou estranho.
- Reprovados pelo Victor: os impactos pesados de trailer (pasta tension, "impact_4") nas telas laranja e o riser de sci-fi + sub no final da logo. Na logo, ele ficou com blade whoosh, boom suave e sinos.
- Texto cinético aparecendo palavra por palavra leva um toque curto de digitação de interface em cada palavra (o Victor achou que "fica foda"): o mesmo som em 3 ou 4 tons levemente diferentes, alternando um pouco de lado, baixinho, e um pouco mais alto nas palavras de destaque. Não toque duas vezes no mesmo instante nem em cima de outro som de interface.
- Se a pessoa mandar um pacote de efeitos como referência, meça cada pasta (volume, grave abaixo de 120 Hz, centro do espectro, largura estéreo) e compare com os efeitos em uso antes de trocar. Depois troque só os sons, mantendo a marcação de tempo aprovada; a imagem não precisa de render novo, basta remontar o vídeo com `-c:v copy`.

## Entrega

Sempre com arquivo editável: vídeo em ProRes, faixas separadas e FCPXML, além de uma versão com áudio junto. O fundo fica embutido, porque o vidro depende dele.

Texto digitado pela pessoa vale mais que a transcrição. Antes de terminar, aponte qualquer diferença entre o texto na tela e o que a transcrição ouviu.
