from app.steering import Steering

steering = Steering(17, 0, 180, 18, 0, 160, 90, 90)

steering.setup()

steering.up()
steering.down()
steering.left()
steering.right()

steering.cleanup()
