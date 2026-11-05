#!/bin/bash
# Renderiza em 6 processos. Uso: render_all.sh anim.html pasta_saida num_quadros
PY="$HOME/video-tools/venv-vidro/Scripts/python.exe"; [ -x "$PY" ] || PY="$HOME/video-tools/venv-vidro/bin/python"
AQUI="$(cd "$(dirname "$0")" && pwd)"
PAGE="$1"; OUT="$2"; N="$3"; W=6; S=$((N/W+1)); FALHOU=0; PIDS=()
for i in $(seq 0 $((W-1))); do
  A=$((i*S)); B=$(((i+1)*S)); [ $B -gt $N ] && B=$N
  "$PY" "$AQUI/render.py" "$PAGE" "$OUT" $A $B & PIDS+=($!)
done
for p in "${PIDS[@]}"; do wait "$p" || FALHOU=1; done
FEITOS=$(ls "$OUT" | grep -c '^f_.*png$')
echo "$FEITOS de $N quadros"
[ "$FALHOU" = 0 ] && [ "$FEITOS" = "$N" ] || { echo "RENDER INCOMPLETO"; exit 1; }
