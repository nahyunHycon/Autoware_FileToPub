from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Set environment variables
        SetEnvironmentVariable('ROS_SECURITY_KEYSTORE', '~/sros2_demo/demo_keystore'),
        SetEnvironmentVariable('ROS_SECURITY_ENABLE', 'true'),
        SetEnvironmentVariable('ROS_SECURITY_STRATEGY', 'Enforce'),

        # Launch ROS2gRPCPublisher node
        Node(
            package='my_package',
            executable='ros2_grpc_publisher',
            name='grpc_publisher_node',
            namespace='grpc_namespace',
            output='screen'
        )
    ])
