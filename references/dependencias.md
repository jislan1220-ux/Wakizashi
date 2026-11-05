# O que baixar e de onde

A skill não traz programas, sons nem música. Confira o que a pessoa já tem e ofereça só o que falta.

## Como pedir aprovação

Muita gente só quer colar e seguir, então faça uma pergunta só. Junte tudo o que falta em uma lista, com nome, site, para que serve e tamanho aproximado de cada item, e peça um "sim". Esse "sim" vale apenas para os itens da lista, e a pessoa pode tirar qualquer um deles. Se depois surgir outro item, pergunte de novo.

Quem colou o comando de instalação do README já aprovou as skills citadas nele.

Não crie contas, não faça login e não pague nada pela pessoa. Se o site exigir conta, passe o link e deixe a pessoa baixar. Depois, peça a pasta onde os arquivos foram salvos.

## Programas

Rode `scripts/preparar_ambiente.sh` só depois de explicar o que ele faz. Ele cria o ambiente em `~/video-tools/venv-vidro` e baixa os pacotes `playwright`, `numpy`, `scipy`, `librosa` e `faster-whisper`.

| Item | Para que serve | Windows | Mac |
|---|---|---|---|
| Git | Baixa as skills | `winget install Git.Git` ou [git-scm.com](https://git-scm.com/downloads) | `brew install git` |
| Python 3.12 | Roda os scripts | `winget install Python.Python.3.12` ou [python.org](https://www.python.org/downloads/) | `brew install python` |
| FFmpeg | Monta o áudio e o vídeo | `winget install Gyan.FFmpeg` ou [ffmpeg.org](https://ffmpeg.org/download.html) | `brew install ffmpeg` |
| Google Chrome | Desenha os quadros | [google.com/chrome](https://www.google.com/chrome/) | [google.com/chrome](https://www.google.com/chrome/) |

No primeiro uso, `analisar.py` baixa sozinho o modelo de transcrição Whisper `base`, com cerca de 150 MB. A página de animação carrega as fontes do Google Fonts, então o render precisa de internet. Avise a pessoa disso.

## SFX

A pessoa escolhe os próprios sons. Peça uma pasta com arquivos `.wav`, e use os nomes deles, sem a extensão, em `sfx.json`. O vídeo pede estes tipos: whoosh curto, whoosh grave, whoosh reverso, riser, clique grave e digitação.

Se ela não tiver sons, ofereça estes sites:

| Site | Observação |
|---|---|
| [Mixkit](https://mixkit.co/free-sound-effects/) | Gratuito |
| [Pixabay](https://pixabay.com/sound-effects/) | Gratuito |
| [Freesound](https://freesound.org/) | Precisa de conta, e a licença muda a cada som |
| [ZapSplat](https://www.zapsplat.com/) | Precisa de conta, e o plano grátis pede atribuição |

Se o arquivo vier em `.mp3`, converta para `.wav` com o FFmpeg.

## Música

A pessoa escolhe a própria música e informa o segundo em que ela deve começar. Se ela não tiver uma, ofereça:

| Site | Observação |
|---|---|
| [Pixabay Music](https://pixabay.com/music/) | Gratuito |
| [Mixkit](https://mixkit.co/free-stock-music/) | Gratuito |
| [Biblioteca de áudio do YouTube](https://studio.youtube.com/) | Precisa de conta do YouTube |
| [Incompetech](https://incompetech.com/) | Gratuito, com atribuição |

## Licença dos sons e da música

As regras desses sites mudam. Antes de a pessoa postar, peça que ela confira a licença de cada som e música na página do download. Não afirme que um arquivo está liberado sem ver isso.

## Skill de SFX e motion: Fluxo de edição

É a skill gratuita de Lucas Leite, com licença MIT e cerca de 150 KB. Se `~/.claude/skills/fluxo-de-edicao/SKILL.md` não existir, coloque na lista do primeiro uso, porque os guias dela ensinam o ofício que complementa esta skill:

- `guias/oficio-motion.md` e `guias/etapa-motion-mapa.md`: como planejar e mover as animações.
- `guias/etapa-sfx.md`: onde e como colocar cada som.
- `guias/referencias.md`: como medir vídeos de referência.

Ela também serve para editar vídeo gravado com apresentador. O conceito visual continua sendo o desta skill.

```bash
git clone https://github.com/LeiteZ/fluxo-de-edicao ~/.claude/skills/fluxo-de-edicao
```

Se a pasta já existir, não baixe de novo. Esta skill funciona sem ela, então siga em frente se a pessoa recusar ou se o download falhar.
