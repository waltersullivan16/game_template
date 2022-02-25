import argparse
import os
import shutil
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('name', help='character\'s name')
args = parser.parse_args()
character = args.name
character_path = os.path.join(os.getcwd(), "images", character)
pathlib.Path(character_path).mkdir(parents=True, exist_ok=True)
from pathlib import Path, PurePath
def t():
	images = Path('../images').rglob('*png')
	img_file = Path('img_list')
	try:
		img_file.unlink()
	except:
		img_file.touch()
	img_file.write_text("dad")
import os
GAME_PATH = os.path.abspath('.')
