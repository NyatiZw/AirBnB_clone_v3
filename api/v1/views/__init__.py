from flask import Blueprint

# Create a Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import of everything in the package
from api.v1.views.index import *

# Wildcard import of everything in the package
from api.v1.views.states import *

# Wildcard import of everything in the package
from api.v1.views.cities import *

# Wildcard import of everything in the package
from api.v1.views.amenities import *

# Wildcard import of everything in the package
from api.v1.views.users import *

# Wildcard import of everything in the package
from api.v1.views.places import *

# Wildcard import of everything in the package
from api.v1.views.places_reviews import *
