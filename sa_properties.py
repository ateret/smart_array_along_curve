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
    bl_description = 'Bunch of properties used by Edge to Curve'

    e2c_type: bpy.props.EnumProperty(
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
    e2c_resolution: bpy.props.IntProperty(
        name = "Curve Resolution" ,
        default = 64,
        description = "TargetCurveResolution",
    )

    e2c_smooth_iteration: bpy.props.IntProperty(
        name = "Curve Smooth Iterations" ,
        default = 1,
        description = "Smooth iterations",
    )

    e2c_decimation_ratio: bpy.props.FloatProperty(
        name = "DecimationRatio" ,
        default = 0.85,
        max = 1,
        min = 0,
        description = "Decimation Ratio",
    )

    e2c_curves_coll: bpy.props.PointerProperty(
        type = bpy.types.Collection,
        name = "Collection to put created curves in ",
        description = "Collection to put created curves in ",
    )
