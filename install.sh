pip install -r requirements.txt
pyinstaller --onefile --name pfm path-maker.py
mv dist/pfm /usr/local/bin/
rm -rf build/ dist/ pfm.spec
