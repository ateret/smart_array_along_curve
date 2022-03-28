import bpy
from  . sa_tools import *

class sa_PT_panel(bpy.types.Panel):
    bl_idname = "sa_PT_panel"
    bl_label = "Smart Array tools"
    bl_category = "sa_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=sa_ue, factor=0.3)


        mrow0 = layout.row()
        mrow0.label(text="Set of context sensitive tools aimed at improving city landscape creation workflow")
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
        split = layout.split(align=sa_ue, factor=0.3)


        mrow0 = layout.row()
        

class sa_tools_PT_Points2Curve(bpy.types.Panel):
    bl_idname = "sa_tools_PT_Points2Curve"
    bl_label = "Points to Curve"
    bl_category = "sa_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "sa_tools_PT_main"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=sa_ue, factor=0.3)

        row0 = layout.row()
        row0.label(text="Points to Curve")

        # Point to curve scripts
        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Points to curve propeties")



        row1 = column0.row(align=sa_ue)
        row3 = column0.row(align=sa_ue)
        row4 = column0.row(align=sa_ue)

        row1.prop(scene.P2CProps, "P2CResolution",text="Curve Resolution")
        row1.prop(scene.P2CProps, "P2CSmoothIt",text="Smooth Iterations")
        row1.prop(scene.P2CProps, "P2CDecRatio",text="Decimation Ratio")
        row3.prop(scene.P2CProps, "P2CType",text="Test", expand=sa_ue)
        row4.prop(scene.P2CProps, "P2CCurvesColl", text="Curves Collection")

        box1 = layout.box()
        column1 = box1.column()
        row2 = column1.row(align=sa_ue)
        row2.scale_y = 2.0
        if scene.P2CProps.P2CType=='Bezier':
            row2.operator('object.points2beziercurve' ,text="Points to Bezier Curve",icon="IPO_BEZIER")
        else :
            row2.operator('object.points2beziercurve' ,text="Points to Points Curve",icon="IPO_LINEAR")


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
        split = layout.split(align=sa_ue, factor=0.3)


        row0 = layout.row()
        row0.label(text="Smart Array Along Curve")



        #Duplication method
        box01 = layout.box()
        column01=box01.column()
        column01.label(text="Duplication method")
        row01=column01.row(align=sa_ue)

        row01.prop(scene.arrProps, "cArrDuplType", text="Duplication method",  expand=sa_ue)


        #Objects
        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Objects (Caps are optional) :")

        row1 = column0.row(align=sa_ue)
        row2 = column0.row(align=sa_ue)
        row3 = column0.row(align=sa_ue)


        row1.prop(scene.arrProps, "cArrayObject",text="Array Object")
        row2.prop(scene.arrProps, "cArrayStartCapObject",text="Start Cap Object")
        row3.prop(scene.arrProps, "cArrayEndCapObject",text="End Cap Object")


        #Collections
        box1 = layout.box()
        column1 = box1.column()
        row4 = column1.split(factor=0.33)
        column1.label(text="Collections for created objects:")

        row5 = column1.row(align=sa_ue)
        row6 = column1.row(align=sa_ue)

        row5.prop(scene.arrProps, "cArrCurvesColl",text="Curves Collection")
        row5.prop(scene.arrProps, "cArrObjectsColl",text="Objects Collection")

        #Names

        box2 = layout.box()
        column2 = box2.column()
        row6 = column2.split(factor=0.33)
        column2.label(text="Name overrides for created objects: ")

        row7 = column2.row(align=sa_ue)
        row8 = column2.row(align=sa_ue)

        row7.prop(scene.arrProps, "cArrCurveName",text="Curves Name")
        row8.prop(scene.arrProps, "cArrObjName",text="Objects Name")

        box3 = layout.box()
        column3 = box3.column()
        row9 = column3.split(factor=0.33)
        column3.label(text="Manage Decimate modifier ")

        row10 = column3.split(factor=0.9)
        row10.prop(scene.arrProps, "cArrDec", text="Use Decimate modifier?")

        if scene.arrProps.cArrDec == 1 :
            row11 = column3.split(factor=0.33)
            row11.prop(scene.arrProps, "cDecimateType", text="Decimate Type")


        #Decimate modifier
        # row4 = layout.row(align=sa_ue)
        #
        # row4.prop(scene, "sa_DecimateType",text="Decimate modifier: Type")
        # row4.prop(scene, "sa_DecimateAngleLimit",text="Decimate modifier: Angle limit")

        row6 = layout.row(align=sa_ue)
        row6.scale_y = 2.0
        row6.operator('object.arrayalongcurve' ,text="Smart Array (Curve)")
