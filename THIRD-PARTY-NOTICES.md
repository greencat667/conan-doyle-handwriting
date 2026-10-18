# Third-party tools

Dependencies are installed separately; their code and binary distributions are not vendored here. Retain their own notices when redistributing them.

| Tool | Licence | Role |
| --- | --- | --- |
| [FontTools](https://github.com/fonttools/fonttools/blob/main/LICENSE) | MIT | Build TTF and OpenType tables |
| [Pillow](https://github.com/python-pillow/Pillow/blob/main/LICENSE) | MIT-CMU | Source/proof images |
| [NumPy](https://github.com/numpy/numpy/blob/main/LICENSE.txt) | BSD-3-Clause, plus component notices | Extraction/layout calculations |
| [OpenCV Python](https://github.com/opencv/opencv-python/blob/4.x/LICENSE.txt) | MIT wrapper; Apache-2.0 OpenCV and component notices | Scan extraction/layout profiles |
| [Playwright](https://github.com/microsoft/playwright/blob/main/LICENSE) | Apache-2.0 | Browser checks |

The supported vector-only font build needs FontTools. The extraction and proof pipelines need the other Python packages. Browser binaries have their own notices and are not included.

The independent implementation was informed by the research paper *My Text in Your Handwriting* (Haines et al., 2016). No code from its AGPL handwriting engine is incorporated, and no paper figures are included in the public package.

Artwork has separate terms; see the font licence and source-rights register. The code licence does not license historical photographs or letter text.
