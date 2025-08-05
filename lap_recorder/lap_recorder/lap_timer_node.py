import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float64
import time
import requests

class LapTimerNode(Node):
    def __init__(self):
        super().__init__('lap_timer_node')
        self.subscriber = self.create_subscription(Bool, '/laser_bool', self.lap_callback, 10)
        self.publisher = self.create_publisher(Float64, '/lap_time', 10)

        self.is_timing = False
        self.start_time = None
        self.last_lap_time = 0.0  # 最後の通過処理時間
        self.debounce_seconds = 5.0  # デバウンス時間（秒）

    def lap_callback(self, msg):
        now = time.time()

        if msg.data:
            # 直近の通過から一定時間以内なら無視
            if now - self.last_lap_time < self.debounce_seconds:
                return

            self.last_lap_time = now  # 最後の通過処理時間を更新

            if not self.is_timing:
                self.start_time = now
                self.is_timing = True
                self.get_logger().info('▶️ 計測開始')
                requests.post('http://localhost:5000/start_timer')
            else:
                lap_time = now - self.start_time
                self.is_timing = False

                msg = Float64()
                msg.data = lap_time
                self.publisher.publish(msg)
                self.get_logger().info(f'🏁 周回完了: {lap_time:.3f} 秒')

def main(args=None):
    rclpy.init(args=args)
    node = LapTimerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
