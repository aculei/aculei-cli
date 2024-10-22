# aculei cli

![hugging-face](https://img.shields.io/badge/Hugging%20Face-FFD21E.svg?style=plain&logo=Hugging-Face&logoColor=black)
![python](https://img.shields.io/badge/Python-3776AB.svg?style=plain&logo=Python&logoColor=white)
![TYOER](https://img.shields.io/badge/Typer-000000.svg?style=plaine&logo=Typer&logoColor=white)

Cli tool to generate a dataset from hunter-camera images

- [x] Generate unique ids
- [x] Read metadata using [exiftool](https://exiftool.org/)
- [ ] Use OCR to extract more information
- [x] Classify images using [Zero-shot image classification](https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification) (current model: `openai/clip-vit-large-patch14`)
- [x] Store results in a dataframe

## Install

Clone the repository

```console
git clone https://github.com/micheledinelli/aculei-cli.git
```

Install requirements

```console
pip install -r requirements.txt
```

## Run

### The full cli

```console
python aculei-cli.py --help
```

A sample folder containing some images is available under `./images`

### Datframe to sql conversion

> [!WARNING]
> You may need to downgrade pandas `pip install psycopg2-binary~=2.9.9 SQLAlchemy~=2.0.25 pandas~=2.2.0`

```console
python to_sql.py
```
