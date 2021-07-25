import sys

raise ValueError()

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, PROJECT_DIR)

from is_it_rick import app as application