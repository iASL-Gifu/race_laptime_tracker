import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import requests

class WebPublisherNode(Node):
    def __init__(self):
        super().__init__('web_publisher_node')
        self.subscriber = self.create_subscription(Float64, '/lap_time', self.time_callback, 10)
        self.server_url = 'http://localhost:5000/lap_time'  # FlaskサーバーのURL

    def time_callback(self, msg):
        lap_time = msg.data
        try:
            response = requests.post(self.server_url, json={'lap_time': lap_time})
            self.get_logger().info(f'⏱️ {lap_time:.3f} 秒 をWebに送信（status={response.status_code}）')
        except Exception as e:
            self.get_logger().error(f'送信失敗: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = WebPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
