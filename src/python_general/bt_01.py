#!/usr/bin/env python3 

import time
from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.composites import Selector
from py_trees.composites import Sequence
from py_trees import logging

class Action(Behaviour):
    def __init__(self, name):
        super(Action, self).__init__(name=name)
    
    def setup(self) :
        self.logger.debug(f"Action :: Setup {self.name}")

    def initialise(self):
        self.logger.debug(f"Action :: Update {self.name}")
    
    def update(self):
        if self.name == 'Forward':
            self.logger.error(f"Action :: Forward {self.name}")
            time.sleep(1)    
            return Status.FAILURE
        elif self.name == 'Center_Pocket':
            self.logger.warning(f"Action :: Aligning with center {self.name}")
            time.sleep(1)
            return Status.SUCCESS
        else:
            self.logger.debug(f"Action :: Update {self.name}")
            time.sleep(1)
            return Status.SUCCESS
    
    def terminate(self, new_status):
        self.logger.debug(f"Action :: Terminate {self.name} to {new_status}")

class Condition(Behaviour):
    def __init__(self, name):
        super(Condition, self).__init__(name=name)

    def setup(self):
        self.logger.debug(f"Condition :: Setup {self.name}")
    
    def initialise(self):
        self.logger.debug(f"Condition :: Initialize {self.name}")

    def update(self):
        self.logger.debug(f"Condition :: Update {self.name}")
        time.sleep(1)
        return Status.SUCCESS
    
    def terminate(self, new_status):
        self.logger.debug(f"Condition :: Termination {self.name} to {new_status}")

def make_bt ():
    
    root = Sequence('pallet_alignment', memory=True)

    check_yaw_control = Condition('Check_Camera')
    aling_with_left_pocket = Action('Left_Pocket')
    aling_with_right_pocket = Action('Right_Pocket')
    align_center= Action('Center_Pocket')
    move_forward = Action('Forward')
    move_reverse = Action('Reverse')
    realign_with_center = Action('Center_Again')
    move_forward_again = Action('Forward_Again')

    root.add_children([
        check_yaw_control, 
        aling_with_left_pocket,
        aling_with_right_pocket, 
        align_center,
        move_forward,
        move_reverse,
        realign_with_center,
        move_forward_again
    ])
    return root

if __name__ == '__main__':
    logging.level = logging.Level.DEBUG
    tree = make_bt()
    tree.tick_once()    

