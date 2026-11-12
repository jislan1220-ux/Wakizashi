"""SFX da v24: limpo e leve. Pouca coisa, tudo real, passando em volta (3D), sem empilhar camadas.

Usa os recortes ja salvos na pasta de SFX por sons_reais_v21.py (real_*) e sfx_v22.py (m_*, p_*).
Uso: python sfx_v24.py times.json saida.json
"""
import json, sys
J = json.load(open(sys.argv[1])); SAIDA = sys.argv[2]; INS = J['ins']
E = []
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.08, al='pico'):
    if t >= 0: E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})
def kw(w, n=0):
    L = [t for t, x in J['kw'] if x.lower().strip('“') == w.strip('“')]
    return L[min(n, len(L) - 1)]

# cortes: um whoosh suave por corte, atravessando de um lado para o outro
WH = ['m_wh1', 'm_wh2', 'm_wh4']
for i, c in enumerate(J['cuts']):
    s = -1 if i % 2 == 0 else 1
    ev(WH[i % 3], c, -13, (s * 100, -s * 100), (.2, -.1))

# cenas Seedance: um swell que cresce ate a entrada + um boom grave suave; whoosh na troca para o card
for k, I in enumerate(INS):
    a = I['t']; s = -1 if k % 2 == 0 else 1
    ev('m_swell', a, -15, (s * 80, 0), (.4, 0))
    ev('m_boom', a, -17, al='inicio', rev=.12)
    ev('m_wh3', a + I['half'], -15, (s * 110, -s * 110))
    ev('m_wh2', a + I['q'], -17, (-s * 100, s * 100))

# abertura, digitacao, "sem After", "3 dias gratis"
ev('m_energy', .88, -16)
ev('m_typing', kw('falo') - .02, -20, (15, 15), al='inicio')
ev('m_typing', kw('higgsfield”', 1), -20, (15, 15), al='inicio')
ev('m_click', kw('higgsfield”', 1) + .69, -20, al='inicio')
for j, t in enumerate([kw('after,') + d for d in (.72, .98, 1.26, 1.58)]):
    ev('m_click2', t, -22, ((-1) ** j * 60, 0), al='inicio')
ev('m_chimes', kw('grátis'), -17, (-60, 60), (.5, .5), rev=.2, al='inicio')

# final KATANA: swell, boom suave e brilho
e = J['end']
ev('m_swell', e + .05, -14); ev('m_boom', e + .05, -15, al='inicio', rev=.15)
ev('m_chimes', e + .45, -18, (60, -60), (.4, .4), rev=.2, al='inicio')

# som das cenas: baixo, perto da imagem, pouco eco (o vento e o povo correndo nao podem estrondar)
a, b = INS[0]['t'], INS[1]['t']; I1, I2 = INS
def evc(nome, t, db, az=(0, 0), el=(0, 0), rev=.1): ev(nome, t, db, az, el, rev, 'inicio')
evc('real_vento', a - .1, -26, (-90, 90), (.2, .3))          # vento passando em volta enquanto voam
evc('real_rugido', a + 1.0, -17, rev=.15)
evc('real_asas', a + 3.0, -22, (-30, 30))
evc('p_risada', a + I1['half'] + .5, -23, (25, 15))
evc('real_passagem', a + I1['q'] - .25, -19, (-90, 90), (.3, 0))
evc('real_andando', b + .02, -21, (-15, 15))
evc('real_rugido_janela', b + .55, -24, (60, 40), (.4, .4), rev=.2)
evc('real_fogo', b + .95, -15, (70, -30), (.3, 0), rev=.12)
evc('real_grito', b + 1.95, -22, (-25, -25))
evc('real_grito2', b + 2.15, -25, (30, 30))
evc('real_brasa', b + 2.3, -24, (-10, 10))
evc('real_correndo', b + 2.55, -21, (0, -40))
evc('real_correndo', b + I2['half'] + .05, -20)
evc('real_brasa', b + I2['q'], -23)
evc('real_correndo', b + I2['q'] + .02, -21, (10, -20))

E.sort(key=lambda x: x['t'])
json.dump(E, open(SAIDA, 'w'), indent=0)
print(len(E), 'eventos')
