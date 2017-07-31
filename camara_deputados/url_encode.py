# Codificar cada linha da entrada como um parametro URL

import sys
import six.moves.urllib as urllib 


lines = sys.stdin.readlines()

for line in lines:
    print(urllib.parse.quote_plus(line.strip()))
