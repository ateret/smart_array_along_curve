import bpy, bmesh, random


# Smart Array
class sa_smart_array_along_curve(bpy.types.Operator):
    bl_label ='Smart Array Along Curve'
    bl_idname = 'object.smart_array_along_curve'
    bl_description = 'Creates array with predefined smart setup along selected curve'
    bl_space_type="VIEW_3D"
    bl_region_type="UI"
    bl_option= {'REGISTER','UNDO'}

    @classmethod
    def poll(cls, context):
        try:
            return context.object.select_get() and context.object.type == 'CURVE'
        except AttributeError:
            pass


    def execute(self, contex):
        cScene = bpy.context.scene

        # tmplObjName = name of object tamplate in the .blend file
        # objName = created object name

        tmplObjName = cScene.arrProps.cArrayObject.name

        # getting Objects names
        if cScene.arrProps.cArrObjName != "":
            objName = cScene.arrProps.cArrObjName
        else:
            objName = cScene.arrProps.cArrayObject.name

        # getting Curve names
        if cScene.arrProps.cArrCurveName != "":
            curveName = cScene.arrProps.cArrCurveName
            bpy.context.active_object.name = curveName
        else:
            curveName = bpy.context.active_object.name

        #not a curve Error handler
        try:
            curveLoc = bpy.context.active_object.location
        except:
            self.report({'ERROR'}, "You have not selected a curve object")
            raise Exception("You have not selected a curve object")


        # deselecting curve
        bpy.context.active_object.select_set(0)

        #selecting and copying object tamplate
        bpy.data.objects[tmplObjName].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[tmplObjName]


        if cScene.arrProps.cArrDuplType == 'Duplicate':
            bpy.ops.object.duplicate()
        else:
            bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":0, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})


        # bpy.context.active_object.name = objName


        #moving sidewalk to the beggining of the curve
        bpy.context.active_object.location = curveLoc

        #adding and setting up Array modifier
        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.active_object.modifiers["Array"].name=objName+'_Array'
        bpy.context.active_object.modifiers[objName+'_Array'].fit_type='FIT_CURVE'
        bpy.context.active_object.modifiers[objName+'_Array'].curve=bpy.data.objects[curveName]
        bpy.context.active_object.modifiers[objName+'_Array'].use_merge_vertices = True
        bpy.context.active_object.modifiers[objName+'_Array'].merge_threshold = 0.05

        ##
        try:
            bpy.context.object.modifiers[objName+'_Array'].start_cap = cScene.arrProps.cArrayStartCapObject
        except:
            pass


        try:
            bpy.context.object.modifiers[objName+'_Array'].end_cap = cScene.arrProps.cArrayEndCapObject
        except:
            pass
        #bpy.context.object.modifiers["SidewalkArray"].end_cap = cArrayEndCapObject


        #adding and setting up Curve modifier
        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.active_object.modifiers["Curve"].name=objName+'_Curve'
        bpy.context.active_object.modifiers[objName+'_Curve'].object=bpy.data.objects[curveName]

        #adding and setting up Decimate modifier
        # bpy.ops.object.modifier_add(type='DECIMATE')
        # bpy.context.active_object.modifiers["Decimate"].name=objName+'_Decimate'
        # bpy.context.object.modifiers[objName+'_Decimate'].decimate_type = 'DISSOLVE'
        # bpy.context.object.modifiers[objName+'_Decimate'].angle_limit = cScene.arrProps.trDecimateAngleLimit
        # bpy.context.object.modifiers[objName+'_Decimate'].delimit = {'UV'}



        #print(trDecimateAngleLimit)
        bpy.context.active_object.name = objName

        # print(bpy.context.active_object.name)
        # print(objName)

        #bpy.ops.object.duplicate_move(bpy.data.objects[tmplObjName], curveLoc)


        #Moving to target Collections:
        #Objects Collection
        to_unlink =[]
        for y in range(len(bpy.data.objects[objName].users_collection)):
            to_unlink.append(bpy.data.objects[objName].users_collection[y].name)

        # #changing objName, if overriden by user
        # if cScene.arrProps.cArrObjName is not None:
        #     objName = cScene.arrProps.cArrObjName

        #if Object Target collection isnt null, manage collections
        if cScene.arrProps.cArrObjectsColl is not None:
            if cScene.arrProps.cArrObjectsColl.name in to_unlink:
                to_unlink.remove(cScene.arrProps.cArrObjectsColl.name)
            try:
                to_unlink.remove("Master Collection")
                cScene.collection.objects.unlink(bpy.data.objects[objName])
            except ValueError:
                pass


            if cScene.arrProps.cArrObjectsColl not in bpy.data.objects[tmplObjName].users_collection:
                try:
                    bpy.data.collections[cScene.arrProps.cArrObjectsColl.name].objects.link(bpy.data.objects[objName])
                except RuntimeError:
                    pass

            for z in range(len(to_unlink)):
                bpy.data.collections[to_unlink[z]].objects.unlink(bpy.data.objects[objName])

        #Curve Collection management:
        to_unlink =[]
        for y in range(len(bpy.data.objects[curveName].users_collection)):
            to_unlink.append(bpy.data.objects[curveName].users_collection[y].name)

        if cScene.arrProps.cArrCurvesColl is not None:
            if cScene.arrProps.cArrCurvesColl.name in to_unlink:
                to_unlink.remove(cScene.arrProps.cArrCurvesColl.name)

            try:
                to_unlink.remove("Master Collection")
                cScene.collection.objects.unlink(bpy.data.objects[curveName])
            except ValueError:
                pass


            if cScene.arrProps.cArrCurvesColl not in bpy.data.objects[curveName].users_collection:
                bpy.data.collections[cScene.arrProps.cArrCurvesColl.name].objects.link(bpy.data.objects[curveName])

            for z in range(len(to_unlink)):
                bpy.data.collections[to_unlink[z]].objects.unlink(bpy.data.objects[curveName])

        #Decimation
        if cScene.arrProps.cArrDec == 1:
            bpy.ops.object.modifier_add(type='DECIMATE')
            bpy.context.active_object.modifiers["Decimate"].name='tr_Decimate'
            bpy.context.object.modifiers["tr_Decimate"].decimate_type = 'COLLAPSE'
            bpy.context.object.modifiers["tr_Decimate"].ratio = 0.1
            # bpy.context.object.modifiers["MB_Decimate"].angle_limit = 1.5708
            # bpy.context.object.modifiers["MB_Decimate"].delimit = {'UV'}

        bpy.context.view_layer.objects.active = bpy.data.objects[curveName]



        return {'FINISHED'}

# Edge to Curve 
class sa_edge_to_curve(bpy.types.Operator):
    bl_label ='Points to Bezier Curve'
    bl_idname = 'object.points_to_curve'
    bl_description = 'Creates a curve from selected object or verticles'
    bl_space_type="VIEW_3D"
    bl_region_type="UI"
    bl_option= {'REGISTER','UNDO'}

    @classmethod
    def poll(cls, context):
        try:
            return context.object.select_get() and context.object.type == 'MESH'
        except AttributeError:
            pass

    def execute(self, contex):
        cScene = bpy.context.scene
        # n = Smooth iterations
        n = cScene.P2CProps.P2CSmoothIt
        # d = Decimation ratio (0.00 - 1.00)
        d = cScene.P2CProps.P2CDecRatio


        #If Edit mode is active
        cm = bpy.context.object.mode
        if cm == 'EDIT':
            print('Script launched in edit mode: duplicating selected object and getting rid of unwanted verticles')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.duplicate()
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='INVERT')
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.object.mode_set(mode='OBJECT')
        else:
            bpy.ops.object.duplicate()

        #Applying Transforms!!
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # Converting to Bezier curve, handles set to automatic
        bpy.ops.object.convert(target='CURVE')
        bpy.ops.object.mode_set(mode='EDIT')
        if cScene.P2CProps.P2CType=='Bezier':
            bpy.ops.curve.spline_type_set(type='BEZIER')
            bpy.ops.curve.select_all(action='SELECT')
        bpy.ops.curve.handle_type_set(type='AUTOMATIC')
        if cScene.P2CProps.P2CType=='Bezier Points':
            bpy.ops.curve.spline_type_set(type='BEZIER')
            bpy.ops.curve.select_all(action='SELECT')
            bpy.ops.curve.handle_type_set(type='VECTOR')
        else:
            bpy.ops.curve.select_all(action='SELECT')
            bpy.ops.curve.handle_type_set(type='AUTOMATIC')

        obj = bpy.context.active_object

        # Smoothing the curve
        for x in range(n):
            bpy.ops.curve.smooth()

        # Decimating the curve
        bpy.ops.curve.decimate(ratio=d)

        # Setting U Resolution higher
        bpy.context.object.data.resolution_u = cScene.P2CProps.P2CResolution




        # Setting up origin at the first curve point
        bpy.ops.curve.select_all(action='DESELECT')
        bpy.ops.curve.de_select_first()

        if cScene.P2CProps.P2CType=='Bezier' or cScene.P2CProps.P2CType=='Bezier Points':
            startingPoint = obj.data.splines[0].bezier_points[0]
        else:
            startingPoint = obj.data.splines[0].points[0]


        #Trimming to vector [3]
        bpy.context.scene.cursor.location = startingPoint.co[:3]
        print (bpy.context.scene.cursor.location)

        #bpy.context.object.mode_set(mode='OBJECT')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        #Moving to collections
        # to_unlink =[]
        # for y in range(len(bpy.context.object.users_collection)):
        #     to_unlink.append(bpy.context.object.users_collection[y].name)
        #
        #
        # if cScene.P2CProps.P2CCurvesColl is not None:
        #     if cScene.P2CProps.P2CCurvesColl.name in to_unlink:
        #         to_unlink.remove(cScene.P2CProps.P2CCurvesColl.name)
        #     try:
        #         to_unlink.remove("Master Collection")
        #         cScene.collection.objects.unlink(bpy.context.object)
        #     except ValueError:
        #         pass
        #
        #
        #     if cScene.P2CProps.P2CCurvesColl not in bpy.context.object.users_collection:
        #         bpy.data.collections[cScene.P2CProps.P2CCurvesColl.name].objects.link(bpy.context.object)
        #
        #     for z in range(len(to_unlink)):
        #         bpy.data.collections[to_unlink[z]].objects.unlink(bpy.context.object)
        #

        return {'FINISHED'}

