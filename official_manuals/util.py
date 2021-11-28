# This sample shows the an efficient way of doing image processing
# over Blender's images using Python.

import bpy
import numpy as np

def select_object(obj_name, additive=False):
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[obj_name].select_set(state=True)

# オブジェクトへのアクセス
bpy.data.objects