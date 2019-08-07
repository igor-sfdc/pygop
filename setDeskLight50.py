import pygop
import sys
from ConfigParser import SafeConfigParser

# Read config options
config = SafeConfigParser()
config.read('config')
deskLightDid = int(config.get('main', 'deskLightDid'))
deskLightBrightness = int(config.get('main', 'deskLightBrightness'))

pygop = pygop.pygop()

# Set desk lapmp to the value specified in the config file (1-100, not validated) or default to 50
brightness = deskLightBrightness if (deskLightBrightness > 0 and deskLightBrightness <= 100) else 50
pygop.setBulbLevelByDid(deskLightDid, 1, brightness)
