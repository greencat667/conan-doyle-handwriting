# The Doyle Desk

### A little Victorian correspondence, in your browser.

Write a letter, leave a cryptic clue, or send a distinctly unusual invitation — in a recreation of **Arthur Conan Doyle’s handwriting**. The Doyle Desk pairs a free installable font with a browser tool that turns your words into handwritten notes.

**[Open the desk →](https://greencat667.github.io/the-doyle-desk/)** · **[Download the latest release](https://github.com/greencat667/the-doyle-desk/releases/latest)**

![Conan Doyle Letters — traced handwriting and reconstructed characters](outputs/v08-review.png)

## From manuscript to message

The project began with a question: could the handwriting in Doyle’s surviving letters and manuscripts become something people could write with today? The result brings together traced letterforms, carefully disclosed reconstructions and a small writing desk you can use without installing anything.

Type your message, adjust its size and spacing, and export an **SVG or PNG**. Choose a transparent background for a design, or keep the paper for a ready-made note. Everything runs in your browser; your text stays on your device. Download the desk to use it offline.

## Make it your own

- **Try it first:** [open the live desk](https://greencat667.github.io/the-doyle-desk/), type a note and export an image.
- **Install the font:** download [Conan Doyle Letters](outputs/conan-doyle-letters-study.ttf) and open it in your system’s font installer. Replace an older installation and restart apps that cache fonts.
- **Keep an offline copy:** [download the release ZIP](https://github.com/greencat667/the-doyle-desk/releases/latest), extract it, then open `outputs/handwriting-desk.html`. No account or server is needed. Text and settings are saved in your browser.

The font covers all 95 printable ASCII characters and selected Latin/Welsh accents: 216 visible mappings, ordinary/nonbreaking spaces and an alternate capital A. Doyle’s signature-style A is the default; a rounded body-text A is available in the desk and through OpenType `ss01`.

## How close is it to Doyle?

**58/62 English letters and digits are source-traced.** X, Z, 6 and 7 are contemporary inferred designs. Six punctuation forms are traced: period, comma, !, ?, apostrophe and dash. £, &, double quotes, + and = are inferred, as are the other unverified symbols. In total, 32 basic forms and seven accent marks use image-assisted designs; accents and smart aliases are composed.

These are distinct fixed forms assembled from different writing periods, not a complete reproduction of Doyle's handwriting. Generated forms are not historical attestations. The desk's amber status identifies inferred/composed characters, and unsupported characters appear as boxes. There is no claim of complete Unicode coverage or a completed archive search.

The desktop font and SVG desk share optical kerning. Supporting desktop apps must enable kerning. The desk's optional joins are inferred short bridges, not historical ligatures; font-proof mode adds none. The previous spacing treatment is available for comparison.

## GitHub Pages

The online demo is served from `main` at the repository root. `index.html` opens the same self-contained desk in `outputs/`; `.nojekyll` keeps the files static. Rebuilding `outputs/handwriting-desk.html` updates both the downloadable tool and the hosted demo when pushed to `main`. No separate application server is needed.

## Under the blotter: build it yourself

Python 3.10 or later:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python working/build-from-vectors.py
.venv/bin/python working/make-renderer.py
```

On Windows use `.venv\Scripts\python`. The vector build needs only FontTools and the included reviewed vectors; no scans, image service, API key or network access is needed after installing dependencies. A rebuild reproduces outlines, metrics and OpenType tables, rather than promising identical TTF timestamps.

Browser checks:

```sh
npm ci
npx playwright install chromium
npm test
```

`CHROME_EXECUTABLE` selects an existing Chrome/Chromium binary; `PLAYWRIGHT_MODULE` can select an existing Playwright installation.

## Licences and attribution

- **Software code:** [MIT](LICENSE).
- **Font, glyph vectors and artwork:** [Creative Commons Attribution-ShareAlike 2.0](LICENSE-FONT). Retain the source credits, licence link and modification notices; distribute adapted artwork under the same licence or a permitted later ShareAlike version.
- The HTML includes both MIT application code and CC BY-SA font/glyph artwork. An MIT code licence does not replace the embedded artwork's licence.

[Source credits and modifications](outputs/notice.md), [current source register](sources/source-register.json), [per-character provenance](sources/complete-provenance.json), [third-party tools](THIRD-PARTY-NOTICES.md).

Primary sources: Special Collections Toronto Public Library; Harry Ransom Center, The University of Texas at Austin; the public-domain-tagged 1886 draft on Wikimedia Commons. Original scans, paper figures, private notes and previous unresolved-source font versions are not included. Institutional US public-domain statements do not determine copyright status in every other country. No endorsement by the institutions or Doyle's estate is implied.

## AI-assisted work

The project was developed with AI coding assistance. ChatGPT Images supplied the explicitly inferred forms, using reviewed handwriting as a reference. The v0.8 [design master](working/image-design/generated-sheet-v08.png), [style reference](working/image-design/approved-reference-v08.png) and [exact prompt](outputs/image-design-prompt-v08.txt) are included. Other inferred forms and accent marks are frozen in the vector bank with provenance; no live image generation is required to build or use the font.

The approach was informed by *My Text in Your Handwriting* (Haines et al., 2016), but this project does not incorporate that system's AGPL engine or reproduce its paper figures.

This public repository starts with a reviewed v0.8 snapshot. Earlier personal research history was kept separately rather than published with unresolved source material.
