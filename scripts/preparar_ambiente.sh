#!/bin/bash
# Cria o Python do motion em ~/video-tools/venv-vidro. Usa o Chrome ja instalado para renderizar.
set -e
V="$HOME/video-tools/venv-vidro"
if [ ! -x "$V/Scripts/python.exe" ] && [ ! -x "$V/bin/python" ]; then
  if command -v python3 >/dev/null; then python3 -m venv "$V"; else python -m venv "$V"; fi
fi
PY="$V/Scripts/python.exe"; [ -x "$PY" ] || PY="$V/bin/python"
"$PY" -m pip install -q --upgrade pip
"$PY" -m pip install -q playwright numpy scipy librosa faster-whisper
"$PY" -c "import playwright, librosa, faster_whisper, scipy; print('ambiente ok')"
command -v ffmpeg >/dev/null && command -v ffprobe >/dev/null && echo "ffmpeg ok" || echo "FALTA ffmpeg ou ffprobe"
