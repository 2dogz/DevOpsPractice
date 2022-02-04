#lint.py
import sys
from pylint import lint

t = 8
run = lint.Run(["factorial.py"])
score = run.linter.stats["global_note"]

if score < t:
    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)
