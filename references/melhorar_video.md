# Vídeo enviado e referências extras

A pessoa envia um vídeo arrastando o arquivo para o chat ou colando o caminho dele. Nos dois casos, comece assim:

```bash
$PY scripts/analisar_video.py VIDEO analise/video_enviado
```

Gera `folha.png` com quadros do vídeo, `resumo.json` com duração, resolução, cortes secos, ritmo e volume, e `audio.wav` se o vídeo tiver som. Abra a folha e olhe. Os números ajudam, mas não substituem ver o vídeo.

## Melhorar um vídeo da pessoa

1. **Entenda:** pergunte o objetivo do vídeo e o que incomoda nele.
2. **Avalie:** transcreva o áudio com `scripts/analisar.py` para ter a fala e os tempos.
3. **Mostre o diagnóstico:** faça uma tabela curta com o que funciona, o que melhorar e como. Compare com `references/estilo.md`: cenas só de texto, ritmo lento, cor sem significado, cortes secos, fundo parado, som fraco.
4. **Combine o caminho e espere a aprovação:**
   - **Refazer como motion:** para vídeos de tela, slides ou narração. Mantenha a mensagem e reconstrua as imagens nas etapas normais da skill.
   - **Editar a gravação:** para vídeos com a pessoa falando para a câmera. Esta skill não faz isso, então ofereça a skill Fluxo de edição.
5. **Pegue o áudio limpo:** peça a narração separada. Se o vídeo tiver música por baixo, explique que `audio.wav` traz os sons misturados e que a voz sairá com a música antiga. Se ela não tiver a narração separada, ofereça regravar.

Preserve o que a pessoa disser que já funciona. Mostre a prancha antes de refazer.

## Usar outros vídeos como referência

Os vídeos extras complementam o estilo do Victor. Analise cada um e anote em `perfil.md`:

- Ritmo: tempo entre trocas e momentos de pausa.
- Cor: paleta e o que cada cor significa.
- Tipografia: tamanho, peso e como o texto entra.
- Transições e movimento de câmera.
- Som: quanto SFX aparece e em que momentos.

Mostre à pessoa o que pretende usar e o que vai deixar de fora, e espere a aprovação.

**O que pode mudar:** ritmo, paleta, tipografia, transições, densidade de SFX.

**O que define o estilo e só muda se a pessoa pedir:** interface como protagonista de cada cena, vidro sobre luz que reage à música, câmera atravessando as cenas e revelação de logo com corte de lâmina.

Se a referência entrar em conflito com essa base, avise e pergunte qual seguir.

Aprenda a técnica, sem copiar o trabalho de ninguém: não reproduza logo, personagem, arte, texto ou cena de outro criador. Não use trechos, imagens ou áudio dos vídeos de referência no vídeo final, a não ser que sejam da própria pessoa.

Com a skill Fluxo de edição instalada, leia `guias/referencias.md` dela para medir melhor.
