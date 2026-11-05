---
name: motion-vidro-liquido
description: Cria vídeo de motion no estilo explicador de produto SaaS, com interface real em vidro, luz líquida verde reagindo à música, câmera 3D rápida, revelação da logo com corte de lâmina, narração, trilha e SFX sincronizados e pacote para o DaVinci. Na primeira vez, conhece a pessoa e ensina a usar em 8 passos. Também melhora um vídeo que ela enviar e aceita outros vídeos como referência. Use sempre que a pessoa pedir para melhorar um vídeo, adicionar referências, um motion ou vídeo "nesse estilo", "igual ao Wakizashi", "com vidro", um vídeo novo sobre o tema da pessoa, ou mudanças de um vídeo feito assim, mesmo sem citar a skill. Não use para editar vídeo gravado com apresentador; nesse caso, ofereça a skill Fluxo de edição, descrita em references/dependencias.md.
---

# Motion vidro líquido

Transforma o tema, a narração, o texto e a música da pessoa em um motion pronto, renderizado quadro a quadro de uma página HTML. O resultado aprovado que serve de régua é o Claude Wakizashi parte 2, do criador da skill. O vídeo novo copia o estilo e o motor, nunca o assunto: fala, cenas, logo e crédito são da pessoa.

Antes de criar qualquer cena, leia [references/estilo.md](references/estilo.md): ele guarda o gosto aprovado pelo criador da skill e o que ele rejeitou. Ao mexer no código ou se algo quebrar, leia [references/tecnica.md](references/tecnica.md).

## Primeiro uso

Se `~/video-tools/motion-vidro/perfil.md` não existir, siga [references/primeiro_contato.md](references/primeiro_contato.md) antes de tudo. Se existir, leia o perfil, cumprimente pelo nome e pergunte qual caminho seguir. As preferências do perfil valem em todos os vídeos.

## Caminhos

- **A. Criar um vídeo novo:** siga as etapas abaixo.
- **B. Melhorar um vídeo enviado:** siga [references/melhorar_video.md](references/melhorar_video.md) e, depois da aprovação do diagnóstico, as etapas abaixo.
- **Adicionar referências:** a qualquer momento, siga a parte de referências de `references/melhorar_video.md`.

O conceito visual é sempre o do Wakizashi, descrito em `references/estilo.md`. Referências extras e guias externos complementam esse conceito, sem substituí-lo, a não ser que a pessoa peça.

Fale em português, de forma curta. A pessoa aprova vendo, então mostre arquivos e imagens em vez de descrever.

## O que pedir

- O tema do vídeo e o público, se o perfil não tiver.
- Narração em áudio e o texto digitado. Se ela ainda não tiver, escreva o roteiro sobre o tema, peça a aprovação e espere ela gravar.
- Música escolhida por ela, e o segundo em que deve começar.
- Formato (o padrão é 16:9, 1920x1080, 30 fps).
- Nome da logo e crédito (pergunte; no vídeo de referência está `BY CREATOR: @diasl_uisvictor`, troque pelo crédito da pessoa).

Peça também uma pasta com os SFX em `.wav`, que ela escolhe. Os nomes em `sfx.json` são os nomes desses arquivos, sem a extensão, e a pasta entra em `--biblioteca`.

Se faltar programa, SFX ou música, siga [references/dependencias.md](references/dependencias.md): mostre de onde baixar e peça aprovação antes de cada item.

## Etapas

Pare para aprovação nos pontos marcados. Refazer depois do render completo custa cerca de 10 minutos a cada vez, por isso os erros precisam aparecer antes.

### 1. Preparar

Confira Python, FFmpeg e Chrome e, se faltar algo, siga `references/dependencias.md`. Com a aprovação da pessoa, rode `scripts/preparar_ambiente.sh` uma vez. Ele cria o Python em `~/video-tools/venv-vidro`, e nos próximos passos `$PY` é `~/video-tools/venv-vidro/Scripts/python.exe` no Windows ou `~/video-tools/venv-vidro/bin/python` no Mac e no Linux. Trabalhe em uma pasta do projeto, com versões novas a cada entrega (`entrega_v01`, `entrega_v02`), sem sobrescrever o que já foi entregue.

### 2. Ouvir

```bash
$PY scripts/analisar.py narracao.mp3 musica.mp3 INICIO_MUSICA "texto digitado"
```

Gera `analise/palavras.json` (tempo de cada palavra), pausas, batidas e `anim/peaks.js` (a música por quadro, que move o fundo e a onda sonora). O texto digitado é o certo; a transcrição serve só para os tempos, porque ela erra palavras (ouviu "edita" onde o texto dizia "dita").

### 3. Prancha (aprovação)

Divida a narração em cenas pelas frases. Com a skill Fluxo de edição instalada, leia `guias/oficio-motion.md` e `guias/etapa-motion-mapa.md` dela para planejar o movimento. Para cada frase, defina o objeto de interface que conta a história, a entrada, a direção da câmera e os SFX. Copie `assets/wakizashi_referencia.html` para `anim/anim.html` e troque a lista `SC`, mantendo o motor. Crie um objeto de interface ligado ao tema em cada cena. Troque também a logo, o crédito, o `<title>` e as palavras de `FL`, e confira no fim se não sobrou nada do Wakizashi. Ignore as partes do guia sobre HyperFrames: aqui o motor é a página HTML. Ajuste `DUR`, `HITS` (batidas fortes), `FOC` (onde a luz fica em cada cena) e `BL` (hora e posição do corte da logo).

Mostre uma imagem por cena:

```bash
$PY scripts/render.py anim/anim.html analise/t --times 1.5,5.0,6.5
$PY scripts/folha.py analise/t analise/prancha.png
```

Junto, passe a tabela: tempo, fala, imagem e SFX. Só siga com a aprovação da pessoa.

### 4. Áudio (aprovação)

Com a skill Fluxo de edição instalada, leia `guias/etapa-sfx.md` dela para escolher onde cada som entra. Monte `sfx.json` com os eventos (formato em `scripts/mixar.py`) e rode:

```bash
$PY scripts/mixar.py narracao.mp3 musica.mp3 INICIO_MUSICA DUR sfx.json entrega_v01 --biblioteca PASTA_DOS_SFX
```

Mande `audio_para_aprovar.mp3`. Os níveis de partida são os aprovados: a música fica baixa, os SFX aparecem, a trilha gira entre os ouvidos e abaixa sozinha na fala. Se a pessoa pedir mudança, ajuste só o que pediu.

### 5. Teste de quadros (aprovação se mudou algo visual grande)

Renderize de 12 a 16 tempos pela folha, incluindo vários quadros em volta do corte da logo. Veja a folha você mesmo e confira o seguinte: texto cortado, verde sobre verde, luz estourada, vidro sem cor atrás e crédito inteiro na tela.

### 6. Render e preview (aprovação)

```bash
bash scripts/render_all.sh anim/anim.html entrega_v01/_frames NUM_QUADROS
$PY scripts/empacotar.py entrega_v01 motion_nome_v01 --so-preview
```

Rode o render em segundo plano. Mande `preview` e diga o que você conferiu e o que não viu em movimento.

### 7. Pacote

Com o "aprovado" da pessoa:

```bash
$PY scripts/empacotar.py entrega_v01 motion_nome_v01
```

Gera ProRes 422 HQ, o mesmo vídeo com áudio junto, faixas de voz, trilha e SFX, `mix.wav` e `timeline.fcpxml`. O script confere os quadros e a duração e para com erro se algo não bater. Explique qual arquivo usar para editar e qual usar para postar.

## Ao receber correção

Aplique a mudança pedida e preserve o que a pessoa já aprovou. Refaça só as partes afetadas e teste em quadros antes do render completo. Toda correção que valer para outros vídeos entra em `~/video-tools/motion-vidro/perfil.md`, com a data, depois de confirmar com a pessoa. Não mude `references/estilo.md`: ele guarda o estilo original, e uma atualização da skill pode sobrescrevê-lo.
