"""「The Blender Python API: Precision 3D Modeling and Add-on Development」
    https://www.amazon.co.jp/Blender-Python-API-Add-Development-ebook/dp/B0721S6G8Q
   の学習メモ的なスクリプト
   第1,2章
   【注意事項】
   - 書籍中のスクリプトを全てを載せているわけではない
   - 書籍ではBlender2.78を対象にしているが、本ファイル中ではBlender2.93向けに書き直している
"""

from typing import Sized
import bpy
import math

# ##################################
# ## ユーティリティ(VSCodeからスクリプト呼び出す場合はソウタイパスによるインポートはできない)


def delete_all_objects():
    "全オブジェクトを削除"
    if len(bpy.context.scene.objects) > 0:
        bpy.ops.object.delete({"selected_objects": bpy.context.scene.objects})
    bpy.ops.object.select_all(action="DESELECT")


def delete_all_meshes():
    "全メッシュを削除"
    if len(bpy.data.meshes) > 0:
        [bpy.data.meshes.remove(mesh) for mesh in bpy.data.meshes]


# ## ユーティリティ
# ##################################

# ##################################
# ## オブジェクト作成
def step_01_generate_object():
    print("全メッシュを削除")
    delete_all_meshes()

    print("格子状に🐵を配置")
    for k in range(5):
        for j in range(5):
            for i in range(5):
                # bpy.ops.mesh.primitive_monkey_add(size=0.25, location=(i, j, k))
                bpy.ops.mesh.primitive_cone_add(location=(i, j, k))


# ## オブジェクト作成
# ##################################

# ##################################
# ## アニメーション
def step_02_animation():
    # if bpy.context.object is not None:
    #     print("全メッシュを削除")
    #     delete_all_objects()
    if bpy.context.object is None:
        print("適当に１つオブジェクト作成")
        bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0))

    print("アニメーションを付ける")
    obj = bpy.context.object
    for i in range(1000):
        obj.location[0] = math.sin(i)
        obj.location[1] = math.cos(i)
        obj.location[2] = math.sin(i) * math.cos(i)
        obj.keyframe_insert(data_path="location", frame=3 * i)
        obj.scale = (math.sin(i) + 1, math.sin(i) + 1, math.sin(i) + 1)
        obj.keyframe_insert(data_path="scale", frame=3 * i)


# ## アニメーション
# ##################################


def main():
    print("オブジェクト作成")
    # step_01_generate_object()

    print("アニメーション")
    step_02_animation()


if __name__ == "<run_path>":
    main()
