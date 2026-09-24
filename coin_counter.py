
import bpy
from bpy.types import Panel, Operator
 
class COINCOUNTER_PT_main_panel(Panel):
    bl_label = "Main Panel"
    bl_idname = "COINCOUNTER_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Count Coins"
 
    def draw(self, context):
        layout = self.layout
 
        layout.operator("coincounter.myop_operator")

class COINCOUNTER_OT_my_op(Operator):
    bl_label = "Count Coins"
    bl_idname = "coincounter.myop_operator"
    
    def execute(self, context):    
        
        coin_num = 0

        for obj in context.scene.objects:
            if "coin" in obj.name.lower():
                coin_num = coin_num + 1
        
        self.report({'INFO'}, f"Number of coins: {coin_num}")
        
        return {'FINISHED'}
 
 
classes = [COINCOUNTER_PT_main_panel, COINCOUNTER_OT_my_op]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
