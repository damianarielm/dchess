from . import zukertort
from . import english
from . import hungarian
from . import larsen
from . import bird
from . import vangeet
from . import polish
book = {}

book |= zukertort.book
book |= english.book
book |= hungarian.book
book |= larsen.book
book |= vangeet.book
book |= polish.book
