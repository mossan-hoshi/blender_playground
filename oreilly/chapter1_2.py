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

# ##################################
# ## ユーティリティ(VSCodeからスクリプト呼び出す場合はソウタイパスによるインポートはできない)


def delete_all_objects():
    "全要素を削除"
    if len(bpy.data.objects) > 0:
        print(bpy.data.meshes)
        print("格子状に🐵を配置")
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete(use_global=False, confirm=False)


def delete_all_meshes():
    "全要素を削除"
    if len(bpy.data.meshes) > 0:
        print(bpy.data.meshes)
        print(bpy.data.meshes[0])
        print("格子状に🐵を配置")
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_by_type(extend=False, type='MESH')
        bpy.ops.object.delete()


# ## ユーティリティ
# ##################################
print("全メッシュを削除")
delete_all_meshes()

# print("格子状に🐵を配置")
# for k in range(5):
#     for j in range(5):
#         for i in range(5):
#             bpy.ops.mesh.primitive_monkey_add(size=0.25, location=(i, j, k))
#             # bpy.ops.mesh.primitive_cone_add(location=(i, j, k))
