
import bpy
from bpy.types import Panel, Operator
 
class ADDONNAME_PT_main_panel(Panel):
    bl_label = "Main Panel"
    bl_idname = "COINCOUNTER_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Count Coins"
 
    def draw(self, context):
        layout = self.layout
 
        layout.operator("coincounter.myop_operator")
 
 
class ADDONNAME_OT_my_op(Operator):
    bl_label = "Count Coins"
    bl_idname = "coincounter.myop_operator"
    
    coin_num : bpy.props.IntProperty(default= 10)
    
    def execute(self, context):    
        
        
        self.report({'INFO'}, "Number of coins: %i" %
        (self.coin_num)
        )
        
        return {'FINISHED'}
 
 
classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
