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

## Áudio v04: SFX do Victor (pacote SFX Pires Visuals)

- 12 sons do pacote, com prefixo `pv_`: Whoosh 1, 2 e 3 (graves e pesados), Impact, Suspense Riser, Metallic Riser, Shine, Echo Snap, Phone typing, Digital Camera Power On, Digital Camera click e Digital autofocus.
- Os whooshes do pacote ficam nas trocas de cena, com a trajetória 3D de antes. O Impact está nas 4 batidas principais: 0,88, 3,40, 15,10 e 23,25 s.
- Suspense Riser gira subindo até o "Caralho"; Metallic Riser dá duas voltas até a logo. Shine no holograma (2,95 s), em "três dias grátis" e na logo. Echo Snap nas palavras batendo, autofocus e power on no iPhone, Phone typing na caixa de comentário.
- Dos sons sintetizados ficam só as camadas de cinema: braam, sub drop, boom, queda de grave, swell reverso e um pouco do mergulho. O hit metálico fica só no "Caralho", mais baixo.
- Eventos em `sfx_3d_v04.json`. Os arquivos do pacote não vão para o repositório.

## Esboço v01 (prancha + preview)

- `anim/anim.html`: página vertical de 1080x1920 com `__setTime(t)`, no mesmo esquema do motor da skill. Usa os prints do perfil do Victor, que ficam em `assets/` fora do repositório: `tela.jpg` (perfil com a grade), `avatar.png` e `post1..9.jpg`.
- Cenas: iPhone gira (0–1,25 s) → mergulho com os posts saltando (1,25–2,6) → avatar vira holograma (2,6–3,4) → "Caralho, é muito FODA isso!" em fundo claro (3,4–6,0) → balão de vidro digitando o pedido (6,0–8,4) → cubo de vidro Claude/Higgsfield/vídeo com palavras orbitando (8,4–11,3) → neon "sem After" riscado, "madrugada" e 03:47 (11,3–14,2) → "e o melhor: 3 DIAS GRÁTIS" com tremida (14,2–19,6) → caixa de comentário cai e digita "Higgsfield" (19,6–23,25) → assinatura Victor-Dias.mp4 (23,25–25,5).
- O preview junta os 765 quadros com o áudio v04. É só esboço: sem o fundo de luz líquida e sem o corte de lâmina, que entram na versão final.

## Versão 16:9 v01 (nova referência: Higgsfield Katana + Claude Motion)

- Referência nova: vídeo de 56 s em que um motion 16:9 roda num monitor. Fundo preto, verde-limão (#c6ff2e) e rosa, tipo pesado em caixa alta, header pequeno com chip verde na palavra-chave, nós de interface ligados por linha com um ponto viajando, caixa de prompt com palavras marcadas em verde, pilha de ferramentas rosa com contador de horas, fundo verde cheio com letras esticando, corte de katana com faíscas e assinatura final cortada.
- `anim_16x9/anim.html`: 1920x1080, 30 fps, 11 cenas sincronizadas palavra a palavra. Os tempos das palavras vieram da transcrição com faster-whisper no sandbox do Higgsfield.
- SFX: biblioteca CC0 do Katana (Kenney e outros, licenças no pacote), mais Impact, Metallic Riser e Shine do Pires Visuals e as camadas sintéticas de cinema. 100 eventos em `sfx_16x9.json`, gerados por `sfx_16x9.py`, espacializados em 3D por `mix_3d.py`.
- Fontes: Inter Display Black, JetBrains Mono e League Gothic (OFL, do pacote do Katana).

## Versão 16:9 v03 (laranja, câmera dançando, Seedance, 34,8 s)

- Paleta: verde trocado por laranja #ff7a1a (como a ref. 4, Claude Code), violeta #9d6bff no lugar do rosa. O logo do Higgsfield vem em vetor, do site oficial.
- Fundo em camadas (ref. 3, Mintlify): luz líquida em WebGL que segue o grave da música (`peaks.js`), painéis de vidro desfocados em profundidade, feixes de luz nas batidas, grão e vinheta. Vidro do Wakizashi nas caixas, no prompt, no comentário e no cartão.
- Câmera: pan esquerda/direita alternando por cena, rotação 3D, zoom que pulsa no grave e chicote com desfoque na entrada de cada cena.
- Vitrine Seedance 2.0 Mini (Higgsfield, 720p, 5 s): dragão, cerco cômico à torre e duelo na escola de magia, entre 10,95 s e 20,25 s. A narração abre 9,3 s de silêncio ali. O primeiro prompt do dragão foi barrado pelo filtro de propriedade intelectual e refeito com visual original. Gasto: 4 jobs de cerca de 5 créditos.
- Selos fixos: "COMENTA HIGGSFIELD PRO PASSO A PASSO" (ref. 4) e "patrocinado por Higgsfield". Final: Higgsfield + KATANA.

## RETOMAR (estado salvo em 12/11/2026)

Versão atual: **v14** (`anim_16x9_v14/anim.html`: todas as cenas, com iPhone, fundos, celular voando e cinematic em tela cheia que vira card; textos = narração). Antes: v13 (`anim_16x9_v13/anim.html`: todo texto grande é a narração do Victor, palavra por palavra no tempo da voz). Base visual: v12, no visual da `salvo/previews/referencia_aprovada_v07.jpg`. Estrutura: a narração com motion alterna com cinematics em card de vidro 3D (8 batidas cada, corte no meio, frase da narração no card), e as caixas usam o vidro estilo iPhone. São 1920x1080, 30 fps e 31,8 s.

Para refazer numa sessão nova:
1. Ambiente "Wakizashi (Higgsfield)" (rede do Higgsfield e do Hugging Face liberada).
2. Montar a pasta de trabalho: `anim.html`, `peaks.js` e `fonts/` de `anim_16x9_v12/`. Os clipes vão em `clips/<id>/f_0001.jpg`... a 30 fps, extraídos de `salvo/clipes/` (c1 = dragão com a cara, cortado 80% para tirar a vinheta; c2 = cerco com fogo; o1 e o2 = clipes antigos): `ffmpeg -i X.mp4 -vf "fps=30,scale=1440:810:force_original_aspect_ratio=increase,crop=1440:810" -q:v 3 clips/c2/f_%04d.jpg`.
3. Áudio: `build_audio.py '[[3.288,"c1"],[11.18,"c2"]]' v12`. Precisa da narração (`salvo/audio/`), da música FEN (que o Victor reenvia, entrando no segundo 29), dos SFX (`salvo/sfx_cc0/`, mais o pacote Pires Visuals que o Victor tem) e de `trilha_cinematica.py`. O script refaz `peaks.js`.
4. Render: `FPS=60 node render_all.js anim.html fr 0 1909` (60 fps, como no PDF da Wakizashi; o ffmpeg junta com -framerate 60), com o Chrome usando swiftshader (4 processos), e depois o ffmpeg junta com `mix.wav`.

Cena dos orcs cancelada pelo Victor em 12/11/2026: a v14 fica só com as duas inserções (c1 e c2).

### Status em 12/11/2026, antes do /clear
- O render da v14 em 60 fps (1909 quadros) estava em 1693/1909. Quando terminar, `higgsfield_claude_16x9_v14_60fps.mp4` e `higgsfield_claude_16x9_v14_30fps.mp4` são copiados para `projetos/higgsfield_claude/entrega_v14/`. Essa pasta fica fora do git porque tem a música FEN; se o container for reiniciado, os vídeos se perdem e é preciso renderizar de novo pela seção RETOMAR.
- Próximos passos: Victor testar 60 fps contra 30 fps no Instagram.

## Versão 16:9 v15 (cenas Seedance mais longas, 38,1 s)

- Pedido do Victor: depois de cada frase da narração, a música segura e as cenas geradas no Seedance ficam mais tempo na tela. Depois a narração volta, e o final é o mesmo.
- Cada inserção agora tem 16 batidas (6,3 s, antes eram 3,2 s): 8 batidas de tomada contínua em tela cheia com o título, mais 8 no card de vidro, com corte entre dois clipes na batida 12.
  - Inserção 1 (3,288 s, "O QUE EU CONSIGO FAZER"): c1 em tela cheia; no card, o1 e depois c1.
  - Inserção 2 (11,18 s, "TRANSFORMA EM VÍDEO"): c2 em tela cheia; no card, o2 e depois c2.
- Áudio: `build_audio.py '[[3.288,"c1"],[11.18,"c2"]]' v15 16`, rodado com `salvo/venv/bin/python`. O terceiro argumento é o número de batidas de cada inserção; o padrão continua 8, como na v14. Com 16, entram um crack, um impact e um whoosh no corte da batida 12.
- Render: `FPS=60 node render_all.js anim.html fr 0 2288`, com `anim_16x9_v15/anim.html`. Os vídeos ficam em `entrega_v15/`, fora do git.

## Versão 16:9 v16 (corte seco na batida, mais 3D, SFX refeitos)

- Pedido do Victor: o motion está aprovado, mas precisa de mais 3D; quando a batida cair, o corte tem que ser seco ("pá"); e os SFX têm que ficar mais gostosos.
- Cortes: cada troca de cena foi movida para a batida mais próxima (152 BPM, até 0,22 s de ajuste; a cena final não muda). A fusão de 0,5 s com blur saiu: agora o corte é seco, com soco de zoom (1,14 → 1 em 0,22 s), flash branco de 1 quadro (30%) e tranco de câmera. Os cinematics também entram sem blur.
- 3D: a câmera gira mais (balanço de ±13° em Y e ±7° em X), entra em 3D mais forte, dá um tranco em profundidade e vira para lados alternados a cada batida. As letras da narração ganharam extrusão (volume) e inclinam junto com a câmera.
- SFX (`sfx_v16.py`): saíram os sons sci-fi de interface (erro, bip, scan, data, glitch, metralhadora de teclas), e o reverb dos SFX foi reduzido. Sons novos sintetizados: swoosh de ar que cresce e para seco no corte, kick de sub, kick leve, pop nas palavras-chave, tick e swell reverso. Cada corte leva swoosh + kick + cauda + impact baixo. Nas inserções: riser → kick, braam e sub → brilho no título. A digitação agora é de celular. O final leva o riser metálico.
- Passo a passo do áudio: rodar `anim_16x9_v16/times16.js` para exportar os tempos para `times16.json`, depois `sfx_v16.py times16.json salvo/sfx sfx_v16.json`, e por fim `mix_3d.py voz_v15.wav trilha_v15.wav salvo/sfx sfx_v16.json saida --dur 38.1316 --fim 35.8816`. A voz e a trilha são as mesmas da v15.

## Versão 16:9 v17 (cerco mais longo, 41,3 s)

- Pedido do Victor: deixar mais tempo na cena dos cavaleiros, para mostrar eles sendo queimados e depois fugindo pela ponte. O texto continua sendo o da narração, sem mudança.
- Cada inserção agora tem a própria duração em `INSB` (`anim.html`): o dragão continua com 16 batidas (8 em tela cheia e 8 no card); o cerco passou para 24 batidas (12 + 12, 9,5 s).
  - Cerco em tela cheia: c2 de 1,0 s a 5,7 s numa tomada só (eles chegam na ponte, o dragão solta fogo, eles fogem com a bunda pegando fogo).
  - Card: o2 de 0 a 3,2 s (correndo pela ponte em direção à câmera); na batida 20, corte para c2 a partir de 4,0 s (fugindo queimados).
- Áudio: `build_audio.py '[[3.288,"c1",16],[11.18,"c2",24]]' v17` (o terceiro item de cada inserção é o número de batidas); tempos exportados com `anim_16x9_v17/times.js` para `times17.json`; SFX gerados por `sfx_v17.py` (o mesmo som da v16, com os tempos lidos da animação); depois `mix_3d.py ... sfx_v17.json --dur 41.2895 --fim 39.0395`.
- Render: `FPS=60 node render_all.js anim.html fr 0 2478`.

## Versão 16:9 v18 (dragão também com 24 batidas, 44,4 s)

- Pedido do Victor: a cena da moça no dragão também fica mais longa, como a dos cavaleiros.
- Dragão (24 batidas): em tela cheia, c1 de 0,2 s a 4,9 s (cara do dragão, rugido, a moça aparece montada); no card, o1 de 0 a 3,2 s (a moça voando, sorrindo) e, na batida 20, corte para o1 a partir de 3,4 s (o dragão saindo para o pôr do sol).
- Correções: o flash do corte dentro do card estava 100% branco (desde a v15) e agora está igual aos outros cortes secos; a frase anterior não volta mais por um instante depois de cada cena Seedance.
- Áudio: `build_audio.py '[[3.288,"c1",24],[11.18,"c2",24]]' v18`; `times.js` → `times18.json`; `sfx_v17.py times18.json salvo/sfx sfx_v18.json` (a digitação do prompt agora segue a palavra "falo"); `mix_3d.py ... --dur 44.4474 --fim 42.1974`.
- Render: `FPS=60 node render_all.js anim.html fr 0 2667`.
- O Victor mandou a legenda: o texto é igual ao do `FR`.

## Versão 16:9 v19 (só o texto da narração na tela)

- Pedido do Victor: no lugar do texto que eu tinha posto, usar só o texto da narração dele, acompanhando a voz.
- Saíram das cenas Seedance o título repetido ("O QUE EU CONSIGO FAZER", "TRANSFORMA EM VÍDEO.") e o prompt digitado ("uma mulher montando um dragão" etc.). Durante as pausas da voz, só a cena roda com a música; fica apenas o selo pequeno HIGGSFIELD · SEEDANCE 2.0.
- A caixa de prompt não digita mais "Cria um vídeo cinematográfico…": agora digita "Eu só falo o que eu quero," palavra por palavra no tempo da voz, com "falo" e "quero" em destaque.
- O áudio é o mesmo da v18 (`entrega_v18x/mix.wav`). Os 4 clipes Seedance foram enviados separados para o Victor (`salvo/clipes/`).

## Versão 16:9 v20

- O Victor aprovou a v19 ("ficou perfeito"). Único ajuste: a fala "Eu só falo o que eu quero" aparece só dentro da caixa de vidro, e a legenda grande em cima dela saiu (`caption()` pula a frase das 6,18 s).

## Versão 16:9 v21 (visual da v18 com a narração nas cenas Seedance)

- O Victor mandou a prévia da v18 e disse que quer aquele visual (título por cima, prompt digitado, título no card), só que com o texto da narração dele no lugar.
- `CLIPS` agora tem [texto digitado/passando, título em tela cheia, título do card, segmentos]:
  - Dragão: "Olha só o que eu consigo fazer com o Higgsfield e o Claude." (título em tela cheia em 2 linhas; no card, "COM O HIGGSFIELD E O CLAUDE.").
  - Cavaleiros: "Eu só falo o que eu quero, o Claude monta a ideia e o Higgsfield transforma em vídeo." (título "O CLAUDE MONTA A IDEIA E O HIGGSFIELD TRANSFORMA EM VÍDEO."; no card, "TRANSFORMA EM VÍDEO.").
- Em tela cheia, a pílula digita a frase em 2,6 s; se a frase não cabe, mostra só o final. No card, a frase passa como letreiro (260 px/s).
- Continuam da v20 a fala só dentro da caixa de vidro e o flash suave. O áudio é o mesmo da v18.
- Os prompts originais do Seedance (do histórico do Higgsfield) e a legenda do post, com a collab, estão em `entrega_v20/legenda_post_instagram.txt` (fora do git).

## v21 em 24 fps, com som das cenas

- O Victor pediu o vídeo em 24 quadros por segundo: `FPS=24 node render_all.js anim.html fr 0 1067` e `ffmpeg -framerate 24`.
- Ele também pediu os sons das próprias cenas (fogo, dragão, vento), baixos, com cara de cinema. O Higgsfield estava com 0,5 crédito, então os sons foram sintetizados em `sfx_cenas_v21.py`: vento com rajadas, rugido (rosnado com formantes), batida de asa, baforada de fogo, brasas, passo em ponte de madeira e passagem do dragão. Os eventos são somados aos do `sfx_v18.json` e saem em `sfx_v21.json`.
- Medição: as cenas ficam de 8 a 15 dB abaixo da mixagem; a cena como um todo sobe só 0,2 dB.
- Áudio: `sfx_cenas_v21.py times18.json salvo/sfx sfx_v18.json sfx_v21.json`, depois `mix_3d.py voz_v18.wav trilha_v18.wav salvo/sfx sfx_v21.json saida --dur 44.4474 --fim 42.1974`. O vídeo de 24 fps é remontado com esse `mix.wav` (`-c:v copy`).

## v21: sons reais nas cenas

- O Victor achou os sons sintetizados pouco reais. Agora são gravações reais do Freesound, todas CC0 (sem crédito obrigatório e com uso comercial liberado), tiradas do dataset `0x3/freesound-laion-640k` no Hugging Face.
- Rede: foram liberados `us.aws.cdn.hf.co` (onde ficam os arquivos parquet) e `datasets-server.huggingface.co` no ambiente "Wakizashi (Higgsfield)".
- Busca: leitura só das colunas de metadados de 400 parquets (`fs_tools/scan.py`, cerca de 130 mil sons, licença CC0) e depois download só das linhas escolhidas (`fs_tools/dl.py`). As gravações ficam em `salvo/fs_dl` (fora do git).
- `sons_reais_v21.py`: recorta e junta as gravações (os ids estão no cabeçalho do script) e gera `sfx_v21r.json` (base `sfx_v18.json` + cenas).
  - Dragão: vento, rugido (Dragon Roar com Monster Growl por baixo), asas gigantes e passagem.
  - Cavaleiros: passos na madeira, ponte rangendo, rugido na janela, baforada (burning air com fire torch), dois gritos, brasas e corrida acelerada 1,45x.
- Mix: `mix_3d.py voz_v18.wav trilha_v18.wav salvo/sfx sfx_v21r.json saida --dur 44.4474 --fim 42.1974`; depois o vídeo de 24 fps é remontado com esse áudio.

## v22: todos os efeitos com gravações reais

- O Victor ainda achou os efeitos ruins e pediu efeitos "mais fodas", tanto no motion quanto nas cenas e nos personagens.
- Varredura dos 1352 parquets (`fs_tools/scan2.py`, só CC0) atrás de whooshes de trailer, impactos de cinema, sub, risers, braams, prato reverso, cliques, digitação, brilhos, armadura e risada feminina. Os escolhidos foram baixados em `salvo/fs_dl2`.
- `sfx_v22.py`: refaz o mapa inteiro só com gravações reais.
  - Cortes: whoosh de trailer (EpicSoundEffects e outros) + kick grande + impacto.
  - Cenas Seedance: riser + prato reverso → "Michael Bay Hit" + BWAAAM + sub; no card, whoosh grave.
  - Palavras: cliques reais baixos. Digitação de iPhone. "3 dias grátis": swell + sinos. Final: prato reverso, Michael Bay Hit, BRAAM, sub e sinos.
  - Personagens: armadura do cavaleiro andando e correndo e o tranco do susto; a moça rindo no dragão; continuam os sons reais da v21.
- Mix: `mix_3d.py voz_v18.wav trilha_v18.wav salvo/sfx sfx_v22.json saida --dur 44.4474 --fim 42.1974`; o vídeo de 24 fps da v21 é remontado com esse áudio (`entrega_v22/`). Também sai `so_efeitos_v22.mp3`, só com os efeitos.

## v23: volta para a v21 (sons reais), com efeitos mais baixos e música mais alta

- O Victor preferiu a v21 à v22 e pediu os efeitos um pouco mais baixos e a música um pouquinho mais alta.
- `mix_3d.py` ganhou `--sfx_lufs` e `--mus_lufs` (padrões -22,5 e -27,5, os mesmos de antes). A v23 usa `--sfx_lufs -25.5 --mus_lufs -26`: efeitos 3 dB mais baixos e música 1,5 dB mais alta.
- Em relação à voz: efeitos de +1,7 para −1,3 dB; música de −2,3 para −0,8 dB. Os eventos são os mesmos da v21 (`sfx_v21r.json`).
- O vídeo é o de 24 fps da v21 remontado com esse áudio (`entrega_v23/`).

## v24: trilha limpa, leve e mais 3D

- O Victor achou a trilha "poluída" e pediu algo mais leve, mais 3D, com um conjunto de efeitos mais limpo e os sons das cenas (vento, dragão, corrida) mais baixos, sem estrondar.
- Música: `trilha_cinematica.py` com `LIMPA=1` tira o eco da intro (gera `trilha_v24.wav`). `mix_3d.py --limpa`: sem o pad grave e quase sem reverb na música (0,08); o giro em volta da cabeça fica lento (1 volta a cada 14 s), sem aceleração no fim, com elevação suave; mais lados abertos (correlação L/R 0,59 contra 0,65 da v23); reverb dos efeitos mais curto.
- Efeitos (`sfx_v24.py`, 45 eventos contra 146): um whoosh suave por corte, atravessando da esquerda para a direita; nas cenas Seedance, swell + boom suave; digitação, cliques e sinos baixinhos; sem bumbos, impactos empilhados, braams ou cliques nas palavras.
- Cenas: vento, rugido, asas, risada, passagem, passos, fogo, gritos, brasas e corrida bem mais baixos e com pouco eco.
- Mix: `--sfx_lufs -29.5 --mus_lufs -25.2 --limpa` → efeitos 6,3 dB abaixo da voz, música 0,7 dB abaixo da voz; sons das cenas de 6 a 8 dB abaixo da música.

## v25: menos movimento e motion blur

- O Victor achou o vídeo movimentado demais e travado em 24 fps; pediu menos movimento e motion blur.
- Câmera mais calma (`anim_16x9_v25/anim.html`):
  - Balanço de ±13°/±7° para ±6°/±3°, mais lento; tranco na batida de 3,5° para 1,2° e profundidade de 75 para 30.
  - Entrada das cenas de 38°/50° para 24°/30°; tremida de 28 para 11 px; soco do corte de 1,14 para 1,06.
  - Zoom na batida da câmera de 1,2% para 0,5%; cenas Seedance balançando bem menos.
- Motion blur: a cada quadro, a câmera é calculada também meio quadro antes (1/48 s), e o desfoque é proporcional à velocidade (como um obturador de 180°). Limite de 2,2 px, sem desfoque no quadro do corte. Mediana de 0,2 px, 90% dos quadros com até 2 px.
- O áudio é o da v24 (os cortes não mudaram de tempo). Render em 24 fps.

## RETOMAR (estado salvo antes do /clear, 12/11/2026)

**Versão atual: v25** (imagem `anim_16x9_v25/anim.html` + som da v24), 24 fps, 1920x1080, 44,4 s.
- Imagem: visual da v18/v21, com o texto da narração nas cenas Seedance (título, digitação e letreiro), as duas cenas Seedance com 24 batidas, a fala do prompt só dentro da caixa de vidro, cortes secos na batida, câmera calma e motion blur.
- Som: v24, limpo (`sfx_v24.py` + `mix_3d.py --limpa --sfx_lufs -29.5 --mus_lufs -25.2`, música `trilha_v24.wav` feita com `LIMPA=1 trilha_cinematica.py`). O mix pronto está em `salvo/entrega_v24/mix.wav` (pasta de trabalho, fora do git).
- O render da v25 estava rodando: quadros em `k16/fr25` (pasta de trabalho), saída em `projetos/higgsfield_claude/entrega_v25/higgsfield_claude_16x9_v25_24fps.mp4`, mais a folha `sheet25.jpg`. Se tiver parado, rode de novo (os quadros que já existem são pulados): `cd k16 && FPS=24 node render_all.js anim.html fr25 0 1067` (em 4 processos, por faixas), depois `ffmpeg -framerate 24 -i fr25/f_%05d.jpg -i entrega_v24/mix.wav -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a aac -b:a 320k -shortest`.
- Próximo passo: conferir a folha de quadros da v25 e mandar o vídeo para o Victor.
- Entregas que já foram para o Victor: v23 e v24 em 24 fps, os 4 clipes Seedance, `legenda_v17.srt` e a legenda do post com a collab e os prompts (`entrega_v20/legenda_post_instagram.txt`).
- Preferências do Victor: o texto na tela é sempre o da narração dele; som leve, limpo e 3D; sons das cenas baixos; menos movimento; 24 fps.
