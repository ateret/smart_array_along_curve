import bpy

from bpy.props import (
    EnumProperty,
    FloatProperty,
    PointerProperty,
    BoolProperty,
    StringProperty,
    IntProperty,
)

from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    Property,
)

class sa_props(bpy.types.PropertyGroup):
    bl_label ='Smart Array property group'
    bl_idname = 'scene.sa_props'
    bl_description = 'Bunch of properties used by SmartArrayAlongCurve'

    #Properties

    cArrDuplType: bpy.props.EnumProperty(
        name = "Array Objects mesh duplication method" ,
        items=[
            ('Duplicate', 'Duplicate', 'Duplicate','DUPLICATE',0),
            ('Link', 'Link', 'Link','DECORATE_LINKED',1)
        ],
        description = "Duplicate creates true copy of the mesh, Link creates mesh linked to the template mesh",
        default ='Link',
    )

    cArrObjName: bpy.props.StringProperty(
        name = "Created object name" ,
        description = "Created object name",
    )

    cArrCurveName: bpy.props.StringProperty(
        name = "Curve name" ,
        description = "Curve name",
    )

    trDecimateAngleLimit: bpy.props.FloatProperty(
        name = "Decimate Angle Limit" ,
        subtype ="ANGLE",
        default = 0.0,
        description = "Decimate Modifier: Angle limit",
    )

    cArrDec: bpy.props.BoolProperty(
        name = "Add Decimate?",
        description = "True = Add, False = Dont add",
    )
    #False = Collapse, True = Planar
    cDecimateType: bpy.props.BoolProperty(
        name = "Decimate type",
        description = "False = Collapse, True = Planar",
    )


    #bpy.types.Scene.cArrayObject =  bpy.props.PointerProperty(
    cArrayObject :  bpy.props.PointerProperty(
        type = bpy.types.Object,
        name = "Object to populate curve with",
        description = "Object to populate curve with",
        )

    cArrayStartCapObject :  bpy.props.PointerProperty(
        type = bpy.types.Object,
        name = "Object to start curve with",
        description = "Object to start curve with",
        )

    cArrayEndCapObject :  bpy.props.PointerProperty(
        type = bpy.types.Object,
        name = "Object to end curve with",
        description = "Object to end curve with",
        )

    cArrCurvesColl: bpy.props.PointerProperty(
        type = bpy.types.Collection,
        name = "Collection to put array curves in ",
        description = "Collection to put array curves in ",
    )
    cArrObjectsColl: bpy.props.PointerProperty(
        type = bpy.types.Collection,
        name = "Collection to put array objects in ",
        description = "Collection to put array objects in ",
    )

class e2c_props(bpy.types.PropertyGroup):
    bl_label ='Edge to Curve property group'
    bl_idname = 'scene.e2c_props'
    bl_description = 'Bunch of properties used by Points2Curve'

    P2CType: bpy.props.EnumProperty(
        name = "Points Type" ,
        items=[
            ('Bezier', 'Bezier', 'Bezier','IPO_BEZIER',0),
            ('Points', 'Points', 'Points','IPO_LINEAR',1),
            ('Bezier Points','Bezier Points','Bezier Points', 'IPO_LINEAR',2)
        ],
        description = "Either Bezier or regular points",
        default ='Bezier',
    )


    #IPO_BEZIER
    #IPO_LINEAR
    P2CResolution: bpy.props.IntProperty(
        name = "CurveResolution" ,
        #subtype ="ANGLE",
        default = 64,
        description = "TargetCurveResolution",
    )

    P2CSmoothIt: bpy.props.IntProperty(
        name = "SmoothIterations" ,
        #subtype ="ANGLE",
        default = 1,
        description = "Smooth iterations",
    )

    P2CDecRatio: bpy.props.FloatProperty(
        name = "DecimationRatio" ,
        #subtype ="ANGLE",
        default = 0.85,
        max = 1,
        min = 0,
        description = "Decimation Ratio",
    )

    P2CCurvesColl: bpy.props.PointerProperty(
        type = bpy.types.Collection,
        name = "Collection to put created curves in ",
        description = "Collection to put created curves in ",
    )


    bl_label ='Select By Volume properties'
    bl_idname = 'scene.SbVProps'
    bl_description = 'Bunch of properties used by Select By Volume'

    vThreshold: bpy.props.FloatProperty(
        name = "Volume Threshold" ,
        subtype ="PERCENTAGE",
        default = (0.0),
        description = "Volume Threshold",
    )

    sColl: bpy.props.PointerProperty(
        type = bpy.types.Collection,
        name = "Collection to check objects volume within ",
        description = "Collection to check objects volume within ",
    )

    sType: bpy.props.EnumProperty(
        name = "Comparision Type" ,
        items=[
            ('less','less','less',0),
            ('less or equal','less or equal','less or equal', 1),
            ('equal', 'equal', 'equal',2),
            ('more or equal', 'more or equal', 'more or equal',3),
            ('more', 'more', 'more',4),
        ],
        description = "Do You want to select objects with similiar, bigger or smaller volume",
        default ='less or equal',
    )

