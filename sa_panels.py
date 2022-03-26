import bpy
from  . sa_tools import *

class sa_PT_panel(bpy.types.Panel):
    bl_idname = "sa_PT_panel"
    bl_label = "Smart Array Tools"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)


        mrow0 = layout.row()
        mrow0.label(text="Set of context sensitive tools aimed at improving city landscape creation workflow")
        mrow1 = layout.row()
        mrow1.label(text="@Tomasz Radwan")

class TRTools_PT_Main(bpy.types.Panel):
    bl_idname = "TR_Tools_PT_Main"
    bl_label = "Main Tools"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "sa_PT_panel"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)


        mrow0 = layout.row()
        #mrow0.label(text="Working in 3.1")




class TRTools_PT_Points2Curve(bpy.types.Panel):
    bl_idname = "TR_Tools_PT_Points2Curve"
    bl_label = "Points to Curve"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "TR_Tools_PT_Main"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split(align=True, factor=0.3)

        row0 = layout.row()
        row0.label(text="Points to Curve")

        # Point to curve scripts
        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Points to curve propeties")



        row1 = column0.row(align=True)
        row3 = column0.row(align=True)
        row4 = column0.row(align=True)

        row1.prop(scene.P2CProps, "P2CResolution",text="Curve Resolution")
        row1.prop(scene.P2CProps, "P2CSmoothIt",text="Smooth Iterations")
        row1.prop(scene.P2CProps, "P2CDecRatio",text="Decimation Ratio")
        row3.prop(scene.P2CProps, "P2CType",text="Test", expand=True)
        row4.prop(scene.P2CProps, "P2CCurvesColl", text="Curves Collection")

        box1 = layout.box()
        column1 = box1.column()
        row2 = column1.row(align=True)
        row2.scale_y = 2.0
        if scene.P2CProps.P2CType=='Bezier':
            row2.operator('object.points2beziercurve' ,text="Points to Bezier Curve",icon="IPO_BEZIER")
        else :
            row2.operator('object.points2beziercurve' ,text="Points to Points Curve",icon="IPO_LINEAR")


class TRTools_PT_Array(bpy.types.Panel):
    bl_idname = "TR_Tools_PT_Array"
    bl_label = "Smart Array Along Curve"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "TR_Tools_PT_Main"
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

        row01.prop(scene.arrProps, "cArrDuplType", text="Duplication method",  expand=True)


        #Objects
        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Objects (Caps are optional) :")

        row1 = column0.row(align=True)
        row2 = column0.row(align=True)
        row3 = column0.row(align=True)


        row1.prop(scene.arrProps, "cArrayObject",text="Array Object")
        row2.prop(scene.arrProps, "cArrayStartCapObject",text="Start Cap Object")
        row3.prop(scene.arrProps, "cArrayEndCapObject",text="End Cap Object")


        #Collections
        box1 = layout.box()
        column1 = box1.column()
        row4 = column1.split(factor=0.33)
        column1.label(text="Collections for created objects:")

        row5 = column1.row(align=True)
        row6 = column1.row(align=True)

        row5.prop(scene.arrProps, "cArrCurvesColl",text="Curves Collection")
        row5.prop(scene.arrProps, "cArrObjectsColl",text="Objects Collection")

        #Names

        box2 = layout.box()
        column2 = box2.column()
        row6 = column2.split(factor=0.33)
        column2.label(text="Name overrides for created objects: ")

        row7 = column2.row(align=True)
        row8 = column2.row(align=True)

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
        # row4 = layout.row(align=True)
        #
        # row4.prop(scene, "trDecimateType",text="Decimate modifier: Type")
        # row4.prop(scene, "trDecimateAngleLimit",text="Decimate modifier: Angle limit")

        row6 = layout.row(align=True)
        row6.scale_y = 2.0
        row6.operator('object.arrayalongcurve' ,text="Smart Array (Curve)")

class TRTools_PT_CurbGenerator(bpy.types.Panel):
    bl_idname = "TRTools_PT_CurbGenerator"
    bl_label = "CurbGenerator"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "TR_Tools_PT_Main"
    bl_order = 0


    def draw(self, context):
        layout = self.layout
        cScene = context.scene
        split = layout.split(align=True, factor=0.3)


        row0 = layout.row()
        row0.label(text="Curb Generator")

        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Curb Generator properties: ")

        row1 = column0.row()
        # row2 = column0.row()
        row3 = column0.row()
        row4 = column0.row()
        # row5 = column0.row()
        row1.prop(cScene.CurbProps, "zOffset", text="Z offset", expand=True)
        row1.prop(cScene.CurbProps, "cThickness", text="Curb Thickness", expand=True)
        row1.prop(cScene.CurbProps, "zHeight", text="Curb Height", expand=True)
        # row2.prop(cScene.P2BProps, 'P2B_min_edge_slide_val', text="Minimum Edge Slide Value", expand = True)
        row3.prop(cScene.CurbProps, 'bWidth', text="Bevel Width", expand = True)
        row3.prop(cScene.CurbProps, 'bSegments', text="Bevel Segments", expand = True)
        row4.prop(cScene.CurbProps, "mMaterial",text="Curb Material")
        


        row6 = layout.row(align=True)
        row6.scale_y = 2.0
        row6.operator('object.curbgenerator' ,text="Curb Generator")


class TRTools_PT_Planes2Buildings(bpy.types.Panel):
    bl_idname = "TR_Tools_PT_Planes2Buildings"
    bl_label = "Planes2Buildings"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "TR_Tools_PT_Legacy"
    bl_order = 4


    def draw(self, context):
        layout = self.layout
        cScene = context.scene
        split = layout.split(align=True, factor=0.3)


        row0 = layout.row()
        row0.label(text="Planes to Buildings")

        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="Planes to Buildings properties: ")

        row1 = column0.row()
        row2 = column0.row()
        row3 = column0.row()
        row4 = column0.row()
        row5 = column0.row()
        row1.prop(cScene.P2BProps, "P2B_rand_seed", text="Random Seed", expand=True)
        row1.prop(cScene.P2BProps, "P2B_rand_perc", text="Random Selection Percent", expand=True)
        row2.prop(cScene.P2BProps, 'P2B_min_edge_slide_val', text="Minimum Edge Slide Value", expand = True)
        row3.prop(cScene.P2BProps, 'P2B_min_roof_height', text="Minimum Roof Height", expand = True)
        row3.prop(cScene.P2BProps, 'P2B_max_roof_height', text="Maximum Roof Height", expand = True)
        row4.prop(cScene.P2BProps, 'P2B_roof_thickness', text="Roof Thickness", expand = True)
        row4.prop(cScene.P2BProps, 'P2B_roof_inset', text="Roof Inset", expand = True)
        row5.prop(cScene.P2BProps, 'P2B_min_build_height', text="Miniumum Building Height", expand = True)
        row5.prop(cScene.P2BProps, 'P2B_max_build_height', text="Maximum Building Height", expand = True)



        row6 = layout.row(align=True)
        row6.scale_y = 2.0
        row6.operator('object.planes2buildings' ,text="Planes To Buildings")



class TRTools_PT_MB_Optimizer(bpy.types.Panel):
    bl_idname = "TR_Tools_PT_MB_Optimizer"
    bl_label = "MB_Optimizer"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "TR_Tools_PT_Legacy"
    bl_order = 5


    def draw(self, context):
        layout = self.layout
        cScene = context.scene
        split = layout.split(align=True, factor=0.3)


        row0 = layout.row()
        row0.label(text="MapBox Optimizer")

        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="MapBox Optimizer properties: ")
        row1 = column0.row()
        row1.prop(cScene.MBoProps, "MBoRandomSelPercent", text="Emissive Windows Percentage", expand=True)

        row6 = layout.row(align=True)
        row6.scale_y = 2.0
        row6.operator('object.mb_optimizer' ,text="MapBox Optimizer")

        # row7 = layout.row(align=True)
        # row7.operator('object.SimiliarVolObj' ,text="Select Similiar Volume Objects")


class TRTools_PT_SelectByVolume(bpy.types.Panel):
    bl_idname = "TRTools_PT_SelectByVolume"
    bl_label = "SelectByVolume"
    bl_category = "TR Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "TR_Tools_PT_Main"
    bl_order = 0


    def draw(self, context):
        layout = self.layout
        cScene = context.scene
        split = layout.split(align=True, factor=0.3)


        row0 = layout.row()
        row0.label(text="Select By Volume")

        box0 = layout.box()
        column0 = box0.column()
        row = column0.split(factor=0.33)
        column0.label(text="SelectByVolume properties: ")
        row1 = column0.row()
        row2 = column0.row()
        row3 = column0.row()
        row1.prop(cScene.SbVProps, "sColl" ,text=" Collection to check objects volume within")
        row2.prop(cScene.SbVProps, "vThreshold", text="Volume Threshold", expand=True)
        row3.prop(cScene.SbVProps, "sType", text="Comparision Type", expand=True)


        row6 = layout.row(align=True)
        row6.scale_y = 2.0
        row6.operator('object.selectbyvolume' ,text="Select similiar by volume")

        # row7 = layout.row(align=True)
        # row7.operator('object.SimiliarVolObj' ,text="Select Similiar Volume Objects")
