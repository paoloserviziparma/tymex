# Guida utente (PDF)

Sorgente della guida `public/docs/guida-utente-tymex.pdf`, nello stile del sito.

Per rigenerarla (serve Node con Playwright):

```
cd src/guida
cp ../../public/fonts/*.woff2 ../../public/img/tymex-logo.png .
python3 make.py      # crea guida.html
node pdf.js          # crea guida-utente-tymex.pdf (A4)
cp guida-utente-tymex.pdf ../../public/docs/
```

I testi sono in `make.py`; le schermate sono i file `p*.png`.
