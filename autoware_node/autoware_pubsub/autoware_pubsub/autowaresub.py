import multiprocessing.process
import rclpy
from std_msgs.msg import String
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from sensor_msgs.msg import CameraInfo
import difflib
from colorama import Fore, Style
from sklearn.metrics import jaccard_score
import numpy as np
from geometry_msgs.msg import Vector3Stamped
import multiprocessing
import os


def write_to_file(queue):
    filename = os.path.expanduser('~/autoware_node/ros2_data.txt')
    while True:
        data = queue.get()
        if data is None:
            break
        with open(filename, 'a') as file:
            file.write(data+ '\n')
        #time.sleep(1)

class autoware_sub(Node):

    def __init__(self, queue):
        super().__init__('autoware_sub')
        qos_profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT)
        self.subscription = self.create_subscription(
        CameraInfo,
        '/sensing/camera/traffic_light/camera_info',
        #Vector3Stamped,
        #'/sensing/imu/gyro_bias',
        self.listener_callback,
        qos_profile)
        self.subscription  # prevent unused variable warning
        #self.publisher_ = self.create_publisher(String, 'topic2', qos_profile)
        self.i=0
        self.queue = queue

    #def listener_callback(self, msg: CameraInfo):
    def listener_callback(self, msg):

        msg = String()
        msg.data = 'injection message: %d' % self.i
        #self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

        self.queue.put(msg.data)

        #test
        #data = f"{msg.data}\n"
        #with open(self.file_name, 'a') as f:
        #    f.write(data)



def main(args=None):

    rclpy.init(args=args)

    write_queue = multiprocessing.Queue()
    writer_process = multiprocessing.Process(target=write_to_file, args=(write_queue,))
    writer_process.start()

    autowaresub = autoware_sub(write_queue)

    try:
        rclpy.spin(autowaresub)
    except KeyboardInterrupt:
        pass

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    autowaresub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
