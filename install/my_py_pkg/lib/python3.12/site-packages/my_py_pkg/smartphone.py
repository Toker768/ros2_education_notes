#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraViewer(Node):
    def __init__(self):  # <- Düzeltildi
        super().__init__('camera_viewer')  # <- Düzeltildi
        self.bridge = CvBridge()

        self.create_subscription(
            Image,
            '/world/zephyr_runway/model/zephyr_with_ardupilot/model/zephyr/link/camera_link/sensor/camera_sensor/image',
  # <- Bu topic köprüde kullanılacak
            self.image_callback,
            10
        )

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            cv2.imshow("Camera View", frame)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f"Görüntü dönüştürme hatası: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = CameraViewer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':  # <- Düzeltildi
    main()
