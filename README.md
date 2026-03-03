Python version == 3.12.10

1. Create virtual environment (If you want to use local - skip this step):
    1. `python -m venv .venv`
    2. Active .venv (In my console i use: `.\.venv\Scripts\activate`, but could be different)

2. Downloading requirements:
    1. `pip install -r requirements.txt`

3. Run script:
    1. Open `main.py` script directory
    2. `python main.py --image "D:\dir\dir\image.png"`
    3. Result saving to file `output.json` (in script directory), also printing result to terminal