# Camera Calibration

## Requirements

- VsCode
- Python

## Instrustions

Setup up env

```sh
python -m venv .venv
source .venv/bin/activate
```

Install dependencies

```sh
pip install -r requirements.txt
```
<!-- 
Capture images

```sh
python captureImage.py
```

- Press `s` to save
- Press `esc` to exit -->

Calibrate camera and save calibration result

```sh
python calibrate.py
```

Test

```sh
python check.py
```
