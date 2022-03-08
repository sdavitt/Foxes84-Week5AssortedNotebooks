print('this file will mimic the existance of a larger project')
from dice import Greed;

roll1 = Greed()
print(roll1.__dict__)


# how does this example fit in the larger context of Flask? Why did we do this?
    # it shows us what is going in the background of imports and class instantiations
    # what we see here on line 4 (and line 5)
    # is going to be similar to a lot of what we'll see in the setup of a flask app
    # and seeing this example will hopefully make it a little easier to understand what exactly is happening with a lot of flask imports
    # and instantiation lines

# tomorrow when we talk about setting up a flask project
# we'll be looking at a lot of imports and instantiation lines
# and asking ourself the age old question in the words of Captain Jack Sparrow
# "To what point and purpose?"
# because most of flask is utlizing prebuilt modules and libraries to add functionality you can then customize to your app

# for example the line that kind of "creates" the Flask app
# app = Flask(__name__)
# the point and purpose of this line is to instantiate a flask object