# Higgsfield + Claude: análise da referência e mapa de cenas

Referência: vídeo enviado pelo Victor (snapinsta, 15,5 s, 720x1280, 30 fps, 466 quadros). Todos os quadros foram extraídos e vistos em folhas a cada 0,1 s.

## Números da referência

- Música a cerca de 152 BPM, batida a cada ~0,39 s.
- Batidas fortes (onsets): 0,07 · 0,63 · 1,90 · 2,07 · 6,22 · 7,01 · 7,38 · 8,54 · 8,92 · 9,29 · 9,87 · 10,03 · 11,68 · 11,84 s.
- A música para em ~13,3 s; o final (logo) fica em silêncio.
- Quase nenhum corte seco: a câmera atravessa as cenas. Os cortes secos ficam nas batidas de 4,4 s, 6,5 s e 9,3 s.

## Plano a plano

| Tempo | O que acontece | Técnica |
|---|---|---|
| 0,0–1,2 | iPhone flutuando num vazio azul-escuro, gira 360° e mostra a tela | Câmera fixa, objeto girando em Y, luz azul de fundo |
| 1,2–3,0 | Câmera mergulha na tela do perfil do Instagram; posts saltam da tela em camadas 3D | Dolly-in rápido, motion blur forte, inclinação de perspectiva |
| 3,0–4,3 | Macro no avatar; a logo se solta da tela como holograma azul sobre anéis | Push-in no avatar, extrusão 3D com glow |
| 4,4–6,4 | Corte para vazio azul: logo vira cubo de vidro girando, palavra orbitando | Corte seco na batida, cubo de vidro com refração |
| 6,5–9,2 | Fundo branco/cinza com vinheta: tipografia cinética palavra por palavra | Palavras entram giradas em 3D, câmera panorâmica, destaque em caixa preta, cor só na palavra forte, máscara oval na batida de 8,2 |
| 9,3–11,9 | Fundo preto: palavras em neon colorido (vermelho, amarelo, azul, branco), uma pingando | Glow forte, cada cor uma ideia, troca no ritmo |
| 12,0–13,1 | Frase em vermelho; grades 3D descem na frente | Objeto 3D entrando na batida |
| 13,1–15,5 | Logo branca entra por desfoque e fica parada com brilho até o fim | Blur-in, sem música |

## Mapa para o vídeo do Victor (9:16, 1080x1920, 30 fps)

Narração (texto digitado, vale mais que a transcrição):

> Olha só o que eu consigo fazer com o Higgsfield e o Claude. Caralho, é muito foda isso! O Higgsfield tá dando três dias grátis pra você que assinar o Claude. Comenta aqui "Higgsfield" que eu te mando o passo a passo.

| Fala | Cena (estrutura da referência) | Conteúdo do Victor |
|---|---|---|
| "Olha só o que eu consigo fazer" | iPhone gira no vazio e mergulha na tela | Perfil @diasl_uisvictor (Victor-Dias.mp4, grade com os posts reais: REGRAS, BRAZIL, PRIME, Sicoob...) |
| "com o Higgsfield e o Claude" | Avatar se solta como holograma → cubo de vidro | Foto do Victor vira holograma; no cubo, as palavras "Higgsfield" e "Claude" orbitando |
| "Caralho, é muito foda isso!" | Tipografia cinética em fundo claro | "muito" em caixa preta, "FODA" na cor forte, máscara oval na batida |
| "O Higgsfield tá dando três dias grátis" | Neon em fundo preto | "3 DIAS" grande, "GRÁTIS" pingando, cada palavra numa cor |
| "pra você que assinar o Claude" | Neon continua | "Claude" em destaque |
| "Comenta aqui 'Higgsfield'" | No lugar das grades: caixa de comentário do Instagram descendo em 3D | "Higgsfield" sendo digitado no comentário |
| "que eu te mando o passo a passo" | Assinatura com blur-in e brilho | Victor-Dias.mp4 · @diasl_uisvictor |

Regras da skill que entram: cortes no ritmo da música (as falas se encaixam nas batidas fortes), SFX nas trocas (whoosh, riser antes da batida, impacto no corte), música baixa e abaixando sob a voz, crédito completo na tela pelo menos 0,45 s antes do fim. Nomes de marcas aparecem só como texto: nada de logo, arte ou trecho da referência.

## Falta do Victor

- A música e o segundo em que ela começa.
- A dublagem final na voz dele (o guia gerado no Higgsfield serve de tempo).

## Áudio v01 (cinematográfico)

- Narração: gravação do Victor, 22,9 s. Frases em 0,0 · 3,40 · 6,01 · 11,33 · 14,21 · 15,10 · 19,64 s.
- Música: FEN (Travis Scott ft. Playboi Carti), 152 BPM, o mesmo andamento da referência. Entra no segundo 26,48 da faixa, para o 808 cair (29,88 s) exatamente no "Caralho" (3,40 s do vídeo).
- Intro de 0 a 3,40 s abafada (passa-baixa e eco), abrindo até o drop. Daí em diante, música cheia, abaixando sob a voz e girando entre os ouvidos.
- Corte seco da música em 23,25 s, com braam e boom com cauda. A logo fica em silêncio até 25,5 s, como na referência.
- Camadas cinematográficas sintéticas (`trilha_cinematica.py`): braam, sub drop e boom com cauda, mais o kit de `scripts/gerar_sfx.py`. Eventos em `sfx.json`.
- Master: -14 LUFS, pico -1 dB. Duração do vídeo: 25,5 s.
- A música não vai para o repositório. Antes de postar, confira os direitos: o Instagram pode silenciar ou bloquear o áudio.

## Áudio v02

- Pedido do Victor: música a partir do segundo 29 da faixa.
- O 808 (29,88 s da faixa) agora cai em 0,88 s do vídeo, com impacto e sub drop. O "Caralho" (3,40 s) mantém riser, braam e impacto, e fica a 0,06 s de uma batida.
- A pausa do grave da faixa (45,54 s) cai em 16,54 s do vídeo, sob "três dias grátis" e a chamada. O corte final continua em 23,25 s.

## Áudio v03: 3D imersivo (ouvir de fone)

- Pedido do Victor: música mais cinematográfica, girando em 3D e subindo e descendo, com SFX fortes e imersivos.
- `mix_3d.py`: a música acima de 140 Hz gira em volta da cabeça. A posição vem da diferença de tempo e de volume entre os ouvidos, da sombra da cabeça e de um timbre mais escuro quando o som está atrás. A volta leva 9 s antes do drop, 4,6 s depois dele e acelera nos últimos 4 s. Ela sobe e desce a cada 3,1 s, com mais brilho em cima e mais escuro embaixo. O grave fica parado no centro.
- Reverb de sala de cinema: forte na intro, mais leve depois do drop. Um pad grave na tônica (A♯) gira no sentido contrário, bem baixo.
- `sfx_cinema.py`: passagem com doppler, mergulho, hit metálico, swell reverso, riser de cinema e queda de grave. Tudo sintetizado, sem som de terceiros.
- `sfx_3d.json`: cada SFX tem trajetória (`az` e `el`) ligada à animação. O iPhone girando passa por trás da cabeça. O mergulho vai da frente para trás e para cima. Os risers dão a volta subindo. A caixa de comentário cai de cima.
- Níveis: voz -19,5, música -27,5 (8 dB abaixo da voz, eram 12), SFX -22,5 LUFS. Master -14 LUFS, pico -1 dB.
