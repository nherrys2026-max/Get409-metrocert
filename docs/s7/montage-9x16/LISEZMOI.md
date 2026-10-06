# Montage vertical 9:16 du teaser

Depuis la racine du dépôt (Python 3 + Pillow, ffmpeg avec libass, polices Inter) :

```
python3 docs/s7/montage-9x16/compose.py     # cartes verticales (v/)
python3 docs/s7/montage-9x16/render.py      # images 1080 × 1920, 30 i/s → video_muet.mp4
cd docs/s7/montage-9x16
ffmpeg -i video_muet.mp4 -i ../../../livrables/GET409-MetroCert_Teaser_S7.mp4 \
  -filter_complex "[0:v]ass=sous-titres-9x16.ass[v]" -map "[v]" -map 1:a \
  -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a copy -movflags +faststart -shortest \
  ../../../livrables/GET409-MetroCert_Teaser_S7_9x16.mp4
```

Même minutage que la version 16:9 : la voix off et la musique sont reprises telles quelles.
