import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, QoSReliabilityPolicy

class autoware_pub(Node):

  def __init__(self):
    super().__init__('autoware_pub')
    qos_profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT)
    self.publisher_ = self.create_publisher(String, 'topic1', qos_profile)
    timer_period = 0.5  # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0

  def timer_callback(self):
    msg = String()
    msg.data = 'Hello World: %d' % self.i
    self.publisher_.publish(msg)
    self.get_logger().info('Publishing: "%s"' % msg.data)
    self.i += 1

#   def __init__(self):
#         super().__init__('autoware_pub')
#         qos_profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT)

#         #self.subscription = self.create_subscription(
#         #     String,
#         #     'topic',
#         #     self.listener_callback,
#         #     qos_profile)

#         #self.subscription

#         self.publisher_ = self.create_publisher(String, 'topic', 10)
#         timer_period = 0.5  # seconds
#         self.timer = self.create_timer(timer_period, self.listener_callback)
#         self.i = 0

#         self.publisher_ = self.create_publisher(String, 'topic1', qos_profile)

#   def listener_callback(self, msg):

#       # self.get_logger().info('I heard: "%s"' % CameraInfo)
#       msg = String()
#       msg.data = 'injection message: %d' % self.i
#       self.publisher_.publish(msg)
#       self.get_logger().info('Publishing: "%s"' % msg.data)
#       self.i += 1

def main(args=None):
    rclpy.init(args=args)

    autowarepub = autoware_pub()

    rclpy.spin(autowarepub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    autowarepub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
