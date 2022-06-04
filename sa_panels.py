import bpy
from  . sa_tools import *

class sa_PT_panel(bpy.types.Panel):
    bl_idname = "sa_PT_panel"
    bl_label = "Smart Array Tools"
    bl_category = "sa_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)


        mrow0 = layout.row()
        mrow0.label(text="Set of context-sensitive tools aimed to improve workflow with curves")
        mrow1 = layout.row()
        mrow1.label(text="@Tomasz Radwan")

class sa_tools_PT_main(bpy.types.Panel):
    bl_idname = "sa_tools_PT_main"
    bl_label = "Main tools"
    bl_category = "sa_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "sa_PT_panel"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)


        mrow0 = layout.row()
        

class sa_tools_PT_edge_to_curve(bpy.types.Panel):
    bl_idname = "sa_tools_PT_edge_to_curve"
    bl_label = "Edge to Curve"
    bl_category = "sa_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "sa_tools_PT_main"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)

        row0 = layout.row()
        row0.label(text="Edge to Curve")

        # Point to curve scripts
        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Edge to Curve propeties")



        row1 = column0.row(align=True)
        row3 = column0.row(align=True)
        row4 = column0.row(align=True)

        row1.prop(scene.e2c_props, "P2CResolution",text="Curve Resolution")
        row1.prop(scene.e2c_props, "P2CSmoothIt",text="Smooth Iterations")
        row1.prop(scene.e2c_props, "P2CDecRatio",text="Decimation Ratio")
        row3.prop(scene.e2c_props, "P2CType",text="Test", expand=True)
        row4.prop(scene.e2c_props, "P2CCurvesColl", text="Curves Collection")

        box1 = layout.box()
        column1 = box1.column()
        row2 = column1.row(align=True)
        row2.scale_y = 2.0
        if scene.e2c_props.P2CType=='Bezier':
            row2.operator('object.edge_to_curve' ,text="Edge to Bezier Curve",icon="IPO_BEZIER")
        else:
            row2.operator('object.edge_to_curve' ,text="Edge to Simple Curve",icon="IPO_LINEAR")


class sa_tools_PT_Array(bpy.types.Panel):
    bl_idname = "sa_tools_PT_Array"
    bl_label = "Smart Array Along Curve"
    bl_category = "sa_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "sa_tools_PT_main"
    bl_order = 2


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)


        row0 = layout.row()
        row0.label(text="Smart Array Along Curve")



        #Duplication method
        box01 = layout.box()
        column01=box01.column()
        column01.label(text="Duplication method")
        row01=column01.row(align=True)

        row01.prop(scene.sa_props, "cArrDuplType", text="Duplication method",  expand=True)


        #Objects
        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Objects (Caps are optional) :")

        row1 = column0.row(align=True)
        row2 = column0.row(align=True)
        row3 = column0.row(align=True)


        row1.prop(scene.sa_props, "cArrayObject",text="Array Object")
        row2.prop(scene.sa_props, "cArrayStartCapObject",text="Start Cap Object")
        row3.prop(scene.sa_props, "cArrayEndCapObject",text="End Cap Object")


        #Collections
        box1 = layout.box()
        column1 = box1.column()
        row4 = column1.split(factor=0.33)
        column1.label(text="Collections for created objects:")

        row5 = column1.row(align=True)
        row6 = column1.row(align=True)

        row5.prop(scene.sa_props, "cArrCurvesColl",text="Curves Collection")
        row5.prop(scene.sa_props, "cArrObjectsColl",text="Objects Collection")

        #Names

        box2 = layout.box()
        column2 = box2.column()
        row6 = column2.split(factor=0.33)
        column2.label(text="Name overrides for created objects: ")

        row7 = column2.row(align=True)
        row8 = column2.row(align=True)

        row7.prop(scene.sa_props, "cArrCurveName",text="Curves Name")
        row8.prop(scene.sa_props, "cArrObjName",text="Objects Name")

        box3 = layout.box()
        column3 = box3.column()
        row9 = column3.split(factor=0.33)
        column3.label(text="Manage Decimate modifier ")

        row10 = column3.split(factor=0.9)
        row10.prop(scene.sa_props, "cArrDec", text="Use Decimate modifier?")

        if scene.sa_props.cArrDec == 1 :
            row11 = column3.split(factor=0.33)
            row11.prop(scene.sa_props, "cDecimateType", text="Decimate Type")


        #Decimate modifier
        # row4 = layout.row(align=True)
        #
        # row4.prop(scene, "sa_DecimateType",text="Decimate modifier: Type")
        # row4.prop(scene, "sa_DecimateAngleLimit",text="Decimate modifier: Angle limit")

        row6 = layout.row(align=True)
        row6.scale_y = 2.0
        row6.operator('object.arrayalongcurve' ,text="Smart Array (Curve)")
