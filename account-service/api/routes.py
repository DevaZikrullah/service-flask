from api import app,Blueprint
from .models import Item,itemSerialized
from .repositories.userRepository import userRoute
from .domain.authDomain import authRoute
from .controllers.authControllers import authentication

api = Blueprint('api', __name__, url_prefix='/api')
# web = Blueprint('web',__name__)

api.register_blueprint(userRoute)
api.register_blueprint(authRoute)

app.register_blueprint(api)

web.register_blueprint(authentication)

# app.register_blueprint(web)