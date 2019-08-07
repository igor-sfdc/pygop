import pygop

pygop = pygop.pygop()

# Set desk lapmp to DIM=50
# TODO: need to use room id instead device id
pygop.setBulbLevelByDid(216593688913573236, 1, 50)
