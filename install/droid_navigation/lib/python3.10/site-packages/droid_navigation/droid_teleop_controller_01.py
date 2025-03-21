#!/usr/bin/env python3

import serial.serialutil
import rclpy
import time
import serial
from rclpy.node import Node
from std_msgs.msg import String, Bool
from geometry_msgs.msg import Twist

class TeleopController(Node):
    def __init__(self):

        super().__init__('arduino_controller')

        self.angular_z = 0.0
        self.linear_x = 0.0

        self.twist_msg = Twist()

        self.port = '/dev/ttyACM0'
        self.baudrate = 57600

        self.stop = 'z'
        self.forward = 'a'
        self.reverse = 'b'
        self.turn_right = 'c'
        self.turn_left = 'd'
        self.curve = 'e'
        
        
        try:
            self.arduino_01 = serial.Serial(self.port, self.baudrate, timeout=0.1)
        
        except serial.serialutil.SerialException as e:
            self.get_logger().error(e)
        
        print(f"Opening port {self.port} with baudrate {self.baudrate}")
        
        self.create_subscription(Twist, '/cmd_vel', self.teleop_callback, 10)
        self.create_timer(0.1, self.compute)

    def compute(self):

        if self.linear_x != None and self.angular_z != None:
        
            data_msg = f"<{int(self.linear_x)}#{int(self.angular_z)}>"
            return_msg = self.arduino_01.readline().decode().strip()
            self.arduino_01.write(data_msg.encode('ascii'))
            self.get_logger().info(return_msg)
            self.get_logger().info(data_msg)

        else:
            self.get_logger('Velocities == 0')
            data_msg = f"<{int(0.0)}#{int(0.0)}>"
            return_msg = self.arduino_01.readline().decode().strip()
        
            
    def teleop_callback(self, msg):

        self.angular_z = msg.angular.z 
        self.linear_x = msg.linear.x 
        # print(f"linear velocity --> {self.linear_x}")
        # print(f"angular velocity --> {self.angular_z}")

def main():

    rclpy.init()
    teleop_control = TeleopController()
    rclpy.spin(teleop_control)
    # rclpy.shutdown()

if __name__=='__main__':
    main()