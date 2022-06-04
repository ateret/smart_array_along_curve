bl_info = {
    "name": "Smart Array Along Curve",
    "author": "Tomasz Radwan, atereten@gmail.com",
    "version": (0, 17, 2),
    "blender": (3, 1, 0),
    "location": "View3D > Panel",
    "description": "Tools aimed to improve workflow with curves",
    "warning": "",
    "GitHub": "github.com/ateret/smart_array_along_curve",
    "category": "Generic",
}

import bpy

from  . sa_panels import *
from  . sa_properties import *
from  . sa_tools import *



classes = (sa_smart_array_along_curve, sa_edge_to_curve, sa_PT_panel, sa_props,e2c_props,sa_tools_PT_main,sa_tools_PT_edge_to_curve,sa_tools_PT_Array)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.sa_props = bpy.props.PointerProperty(type=sa_props)
    bpy.types.Scene.e2c_props = bpy.props.PointerProperty(type=e2c_props)
    


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

