#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):  # __init__() is the constructor. It runs when the object is created.
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello world")
        self.get_logger().info("runs start")
        self.create_timer(0.4, self.timer_callback)
        self.get_logger().info("runs start2")

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1
        self.get_logger().info("runs finish")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    