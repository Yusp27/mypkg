import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def _init_(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, cb)

def cb():
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    talker.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
