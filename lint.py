#lint.py

import sys

from pylint import lint

THRESHOLD = 9

run = lint.Run(["factorial.py"])

score = run.linter.stats["global_note"]
print(score)
if score < THRESHOLD:

    print("Linter failed: Score < threshold value")


else:
    print(score)
