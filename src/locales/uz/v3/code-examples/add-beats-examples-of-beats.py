# Zarbalarga misollar: Turli janrlarda zarbalar yaratish

# Sozlash
from earsketch import *
setTempo(120)

# Ovozli kliplar
kick = OS_KICK05  # Bu "bum" tovushi.
snare = OS_SNARE01  # Bu "mushuk" tovushi.
hihat = OS_CLOSEDHAT01  # Bu "ts" tovushi.

# Rock zarbasi 1-o'lchovda
makeBeat(kick, 1, 1, "0+++----0+++----")
makeBeat(snare, 2, 1, "----0+++----0+++")
makeBeat(hihat, 3, 1, "0+0+0+0+0+0+0+0+")

# Hip hop zarbasi 3-o'lchovda
makeBeat(kick, 1, 3, "0+++------0+++--")
makeBeat(snare, 2, 3, "----0++0+0++0+++")
makeBeat(hihat, 3, 3, "0+0+0+0+0+0+0+0+")

# Jazz zarbasi 5-o'lchovda
makeBeat(hihat, 3, 5, "0++0+00++0+0")

# Dembou (lotin, karib dengizi) zarbasi 7-o'lchovda
makeBeat(kick, 1, 7, "0+++0+++0+++0+++")
makeBeat(snare, 2, 7, "---0++0+---0++0+")