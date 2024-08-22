#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from sensor_msgs.msg import CameraInfo
from std_msgs.msg import String
import os

class autoware_pub(Node):

    def __init__(self):
        super().__init__('autoware_pub')
        qos_profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT)

        # self.subscription = self.create_subscription(
        #      String,
        #      'topic3',
        #      self.listener_callback,
        #      qos_profile)

        # self.subscription

        self.file_path = os.path.expanduser('~/autoware_node/ros2_data.txt')
        self.file = open(self.file_path, 'r')

        self.publisher_ = self.create_publisher(String, 'topic1', qos_profile)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.listener_callback)
        self.i = 0

        #self.publisher_ = self.create_publisher(String, 'topic1', qos_profile)

    def listener_callback(self):
      #test
      line = self.file.readline()

      if line:
          msg = String()
          msg.data = line.strip()
          self.publisher_.publish(msg)
          self.get_logger().info(f'published: "{msg.data}"')
      else:
          self.get_logger().info('End of file reached.')

    #   msg = String()
    #   msg.data = 'injection message: %d' % self.i
    #   self.publisher_.publish(msg)
    #   self.get_logger().info('Publishing: "%s"' % msg.data)
    #   self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = autoware_pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

