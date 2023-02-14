from . import sicilian
from . import french
from . import carokann
from . import pirc
from . import modern
from . import scandinavian
from . import alekhine
book = {}


book |= sicilian.book
book |= french.book
book |= carokann.book
book |= pirc.book
book |= modern.book
book |= scandinavian.book
book |= alekhine.book
