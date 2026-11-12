"""SFX da v27: mesma marcacao da v24, com os sons do pacote de referencia do Victor (Drive).

Whooshes com peso no grave nos cortes, riser + impacto de sub nas entradas das cenas Seedance e no
KATANA, cliques de UI e moedas no "3 dias gratis". Som das cenas igual ao da v24 (baixo).
Os sons do pacote ficam na pasta de SFX como pk_* (convertidos para wav 48 kHz).
Uso: python sfx_v27.py times.json saida.json
"""
import json, sys
J = json.load(open(sys.argv[1])); SAIDA = sys.argv[2]; INS = J['ins']
E = []
def ev(nome, t, db, az=(0, 0), el=(0, 0), rev=.08, al='pico'):
    if t >= 0: E.append({"nome": nome, "t": round(t, 3), "db": round(db, 1), "az": list(az), "el": list(el), "rev": rev, "alinhar": al})
def kw(w, n=0):
    L = [t for t, x in J['kw'] if x.lower().strip('“') == w.strip('“')]
    return L[min(n, len(L) - 1)]

# cortes: whoosh do pacote (grave), atravessando de um lado para o outro
WH = ['pk_wh1', 'pk_wh2', 'pk_wh4', 'pk_wh6']
for i, c in enumerate(J['cuts']):
    s = -1 if i % 2 == 0 else 1
    ev(WH[i % 4], c, -12, (s * 100, -s * 100), (.2, -.1))

# cenas Seedance: riser curto chegando na entrada + impacto de sub; whoosh cinematic na troca para o card
for k, I in enumerate(INS):
    a = I['t']; s = -1 if k % 2 == 0 else 1
    ev('pk_riser_curto', a, -15, (s * 80, 0), (.3, 0))
    ev('pk_imp3' if k == 0 else 'pk_imp4', a, -13, rev=.1)
    ev('pk_whc1', a + I['half'], -14, (s * 110, -s * 110))
    ev('pk_whc6', a + I['q'], -16, (-s * 100, s * 100))

# abertura, digitacao, "sem After", "3 dias gratis"
ev('pk_imp4', .88, -15)
ev('m_typing', kw('falo') - .02, -20, (15, 15), al='inicio')
ev('m_typing', kw('higgsfield”', 1), -20, (15, 15), al='inicio')
ev('pk_click', kw('higgsfield”', 1) + .69, -18, al='inicio')
for j, t in enumerate([kw('after,') + d for d in (.72, .98, 1.26, 1.58)]):
    ev('pk_mouse', t, -20, ((-1) ** j * 60, 0), al='inicio')
ev('pk_coins', kw('grátis'), -17, (-50, 50), (.4, .4), rev=.12, al='inicio')

# final KATANA: riser sci-fi chegando, impacto de sub e brilho
e = J['end']
ev('pk_riser_fim', e + .05, -15, (0, 0), (0, .4)); ev('pk_imp_sub', e + .05, -12, rev=.15)
ev('m_chimes', e + .45, -18, (60, -60), (.4, .4), rev=.2, al='inicio')

# som das cenas: igual a v24 (baixo, perto da imagem, pouco eco)
a, b = INS[0]['t'], INS[1]['t']; I1, I2 = INS
def evc(nome, t, db, az=(0, 0), el=(0, 0), rev=.1): ev(nome, t, db, az, el, rev, 'inicio')
evc('real_vento', a - .1, -26, (-90, 90), (.2, .3))
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
