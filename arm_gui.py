from enable.api import ComponentEditor
from traits.api import HasTraits, Instance, Float, Int, Str, Button
from traitsui.api import View, Item, HSplit, VSplit
from traitsui.menu import CancelButton
from traitsui.key_bindings import KeyBinding, KeyBindings
from ArmMove import MoveArm, ConnectArm


class armgui(HasTraits):

    light_on = [0,0,1]
    light_off = [0,0,0]
    grip_close = [1,0,0]
    grip_open = [2,0,0]
    shoulder_in = [64,0,0]
    shoulder_out = [128,0,0]  
    elbow_down = [16,0,0]
    elbow_up = [32,0,0]
    wrist_up = [4,0,0]
    wrist_down = [8,0,0]  
    base_clock = [0,1,0]
    base_anti = [0,2,0]
    stop = [0,0,0]
    
    flag_connected = 0
    
    
    base_label = Str('Base motor')
    base_clockwise = Button('->')
    base_anticlockwise = Button('<-')
    shoulder_label = Str('Shoulder motor')
    shoulder_forward = Button('->')
    shoulder_back = Button('<-')
    elbow_label = Str('Elbow Motor')
    elbow_forward = Button('->')
    elbow_back = Button('<-')
    wrist_label = Str('Wrist motor')
    wrist_forward = Button('^')
    wrist_back = Button('v')
    light_label = Str('Light')
    light_active = Button('on')
    light_deactive = Button('off')
    
    key_bindings = KeyBindings(
        KeyBinding(binding1 = 'a',
        method_name = 'keybind_test'),
        
    )
    
    def keybind_test():
        print 'thing done'
        
    def connection_check(self):
        if self.flag_connected == 0:
            self.RoboArm = ConnectArm()
            self.flag_connected =1
    
    def _base_clockwise_fired(self):
        self.connection_check()
        MoveArm(1,self.base_clock,self.RoboArm)
        
    def _base_anticlockwise_fired(self):
        print 'did thing'
        self.connection_check()
        MoveArm(1,self.base_anticlock,self.RoboArm)
        
    def _shoulder_forward_fired(self):
        self.connection_check()
        MoveArm(1,self.shoulder_out,self.RoboArm)
        
    def _shoulder_back_fired(self):
        self.connection_check()
        MoveArm(1,self.shoulder_in,self.RoboArm)
        
    def _elbow_forward_fired(self):
        self.connection_check()
        MoveArm(1,self.elbow_up,self.RoboArm)
        
    def _elbow_back_fired(self):
        self.connection_check()
        MoveArm(1,self.elbow_down,self.RoboArm)
        
    def _wrist_forward_fired(self):
        self.connection_check()
        MoveArm(1,self.wrist_up,self.RoboArm)
        
    def _wrist_back_fired(self):
        self.connection_check()
        MoveArm(1,self.wrist_down,self.RoboArm)
        
    def _light_active_fired(self):
        self.connection_check()
        MoveArm(1,self.light_on,self.RoboArm)
        
    def _light_deactive_fired(self):
        self.connection_check()
        MoveArm(1,self.light_off,self.RoboArm)
    
    view = View(
        HSplit(
            VSplit(
                Item('base_label',show_label=False,style='readonly'),
                '_',
                HSplit(
                    Item('base_anticlockwise',show_label=False),
                    Item('base_clockwise',show_label=False)),
                '_',
                '_',    
                Item('shoulder_label',show_label=False,style='readonly'),
                '_',
                HSplit(
                    Item('shoulder_back',show_label=False),
                    Item('shoulder_forward',show_label=False)),
                ),
            '_',
            '_',
            VSplit(
                Item('elbow_label',show_label=False,style='readonly'),
                '_',
                HSplit(
                    Item('elbow_back',show_label=False),
                    Item('elbow_forward',show_label=False)),
                '_',
                '_',
                Item('wrist_label',show_label=False,style='readonly'),
                '_',
                HSplit(
                    Item('wrist_back',show_label=False),
                    Item('wrist_forward',show_label=False)),
                ),
            '_',
            '_',
            VSplit(
                Item('light_label',show_label=False,style='readonly'),
                
                HSplit(
                Item('light_active',show_label=False),
                Item('light_deactive',show_label=False)),
                )
            ),
            key_bindings = key_bindings,
            title = 'Robot Arm Interface'
        )
    
    
if __name__ == "__main__":
    armgui().configure_traits()