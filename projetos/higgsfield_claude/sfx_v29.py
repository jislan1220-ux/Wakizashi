"""SFX da v29: um efeito para cada coisa que acontece na tela, mapeado quadro a quadro na v28.

Correcoes da v28: a abertura tinha um impacto de sub no 0,88 s e um riser de 2,8 s crescendo por baixo
da voz desde o 0,5 s (soava estranho); os tiques de interface entravam em todo corte, ate nos cortes de
cena. Agora: tique so onde aparece interface (chip, menu, caixa de texto); laser = blade whoosh;
corte = whoosh; tela laranja = riser curto + impacto; cenas Seedance com o som delas.
ui_* = pacote "ui sfx" do Victor; pk_* = pacote de referencia (v27); m_*/real_*/p_* = biblioteca antiga.
Uso: python sfx_v29.py times.json saida.json   (tempos em segundos do video final)
"""
import json, sys
J = json.load(open(sys.argv[1])); SAIDA = sys.argv[2]; INS = J['ins']
E = []
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.08, al='pico'):
    if t >= 0: E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})
def ui(nome, t, db, az=(0, 0)): ev(nome, t, db, az, (.1, .1), .05, 'inicio')      # interface: seco e na frente
def kw(w, n=0):
    L = [t for t, x in J['kw'] if x.lower().strip('“') == w.strip('“')]
    return L[min(n, len(L) - 1)]
C = J['cuts']; a, b = INS[0]['t'], INS[1]['t']; I1, I2 = INS; e = J['end']

def corte(t, i, db=-14):
    s = -1 if i % 2 == 0 else 1
    ev('ui_slide' if i % 2 == 0 else 'pk_wh1', t, db, (s * 100, -s * 100), (.2, -.1))

# ---- abertura (0 a 3,3 s): celular entra, flash, chips Higgsfield e Claude, laser, cena do dragao
ui('ui_swipe', .02, -20, (70, 0))                    # celular de vidro entrando
ui('ui_vidro', .36, -25)                             # brilho do vidro do celular
ev('m_energy', .88, -19)                             # batida da musica (o suave aprovado na v24)
corte(C[0], 0, -14)                                  # flash branco e corte para "COM O"
ui('ui_chip', kw('higgsfield') + .04, -19, (-25, 0))  # chip HIGGSFIELD aparece
ui('ui_chip', kw('claude') + .04, -20, (25, 0))       # chip CLAUDE aparece
ev('ui_blade', 3.08, -14, (-80, 80), (.1, 0))        # laser cortando a tela
ev('ui_riser_curto', a, -17, (0, 0), (.2, .3))       # sobe so no ultimo 1,5 s
ev('pk_imp3', a, -13, rev=.1)                         # entra o dragao

# ---- cena Seedance 1 (dragao)
evc = lambda n, t, db, az=(0, 0), el=(0, 0), rev=.1: ev(n, t, db, az, el, rev, 'inicio')
evc('real_vento', a - .1, -26, (-90, 90), (.2, .3))
evc('real_rugido', a + 1.0, -9, rev=.15)              # rosnada alta (pedido do Victor)
evc('pk_imp_sub', a + 1.0, -17, rev=.1)
evc('real_asas', a + 3.0, -22, (-30, 30))
ev('ui_blade', a + I1['half'], -15, (90, -90))        # laser da troca para o card
ui('ui_glitch', a + I1['half'], -25)
evc('p_risada', a + I1['half'] + .5, -23, (25, 15))
ev('pk_whc6', a + I1['q'], -17, (-100, 100))          # corte para o dragao voando
evc('real_passagem', a + I1['q'] - .25, -19, (-90, 90), (.3, 0))

# ---- "CARALHO, E MUITO FODA ISSO!"
corte(C[1], 1, -15)
ev('pk_imp4', 13.05, -15, rev=.1)                      # tela laranja
ev('m_glitter', kw('foda'), -19, (0, 0), (.4, .4), rev=.15, al='inicio')   # faiscas no "FODA"

# ---- caixa de texto: "Eu so falo o que eu quero"
corte(C[2], 2, -16)
ui('ui_abre', C[2] + .03, -19)                        # caixa de vidro abre
ui('ui_typing', kw('falo') - .02, -21, (15, 0))
ui('ui_typing', kw('quero') - .1, -23, (15, 0))

# ---- "O CLAUDE MONTA A IDEIA E O HIGGSFIELD TRANSFORMA EM VIDEO": chips aparecendo um a um
corte(C[3], 3, -16)
for j, t in enumerate([C[3] + .1, kw('claude', 1) + .3, 18.2, kw('higgsfield', 1)]):
    ui('ui_chip' if j % 2 == 0 else 'ui_pop', t, -20, ((-1) ** j * 30, 0))
ev('ui_riser_curto', 20.08, -16, (0, 0), (.2, .3))   # card do castelo sobe ate o clarao laranja
ev('pk_imp4', 20.08, -14, rev=.1)
corte(C[4], 4, -16)

# ---- cena Seedance 2 (castelo, fogo, cavaleiros)
ev('pk_whc6', b, -17, (90, -90))
evc('real_andando', b + .02, -21, (-15, 15))
evc('real_rugido_janela', b + .55, -18, (60, 40), (.4, .4), rev=.2)
evc('real_fogo', 21.85, -15, (70, -30), (.3, 0), rev=.12)   # labaredas (21,9 a 22,9 s)
evc('ui_fogo', 21.85, -17, (70, -30), (.3, 0))
evc('real_grito', b + 1.95, -22, (-25, -25))
evc('real_grito2', b + 2.15, -25, (30, 30))
evc('real_brasa', b + 2.3, -24, (-10, 10))
evc('real_correndo', b + 2.55, -21, (0, -40))
ev('ui_blade', b + I2['half'], -15, (-90, 90))        # laser da troca para o card
ui('ui_glitch', b + I2['half'], -25)
evc('real_correndo', b + I2['half'] + .05, -20)
ev('pk_whc6', b + I2['q'], -17, (100, -100))
evc('real_brasa', b + I2['q'], -23)
evc('real_correndo', b + I2['q'] + .02, -21, (10, -20))

# ---- "SEM AFTER, SEM PASSAR A MADRUGADA EDITANDO": itens do menu aparecendo, laser corta o menu
corte(30.17, 5, -16)
for j, t in enumerate([30.55, 31.0, 31.4, 31.75, 32.05]):
    ui('ui_pop' if j % 2 == 0 else 'ui_chip', t, -20 - j * .5, ((-1) ** j * 40, 0))
ev('ui_blade', 32.5, -13, (-80, 80), (.1, 0))
ui('ui_glitch', 32.54, -22)

# ---- "E O MELHOR:" / tela laranja "O HIGGSFIELD TA DANDO 3 DIAS GRATIS"
corte(C[5], 6, -16)
ev('pk_imp3', kw('melhor:'), -18, rev=.1)
ev('ui_riser_curto', 34.17, -16, (0, 0), (.2, .3))
ev('ui_slide', 34.17, -14, (-90, 90))
ui('ui_conta', kw('3') - .02, -19)                    # "3"
ui('ui_sucesso', kw('grátis'), -15)                   # "GRATIS"

# ---- "PRA VOCE QUE ASSINAR O CLAUDE" / "COMENTA AQUI HIGGSFIELD"
corte(C[7], 7, -16)
ui('ui_vidro', C[7] + .1, -24)
ui('ui_09', kw('claude', 2) + .05, -21)
corte(C[8], 8, -16)
ui('ui_abre', C[8] + .08, -19)                        # caixa de comentario abre
ui('ui_typing', kw('higgsfield”', 1), -21, (15, 0))
ui('ui_confirm', kw('higgsfield”', 1) + .69, -17)     # enviar
ev('m_glitter', 41.21, -20, (0, 0), (.4, .4), rev=.15, al='inicio')   # faiscas no "PASSO A PASSO"

# ---- final KATANA
ev('pk_riser_fim', e + .05, -15, (0, 0), (0, .4)); ev('pk_imp_sub', e + .05, -12, rev=.15)
ev('ui_blade', e + .05, -12, (-90, 90), (.2, 0))
ev('ui_chimes', e + .45, -18, (60, -60), (.4, .4), rev=.2, al='inicio')

E.sort(key=lambda x: x['t'])
json.dump(E, open(SAIDA, 'w'), indent=0)
print(len(E), 'eventos')
