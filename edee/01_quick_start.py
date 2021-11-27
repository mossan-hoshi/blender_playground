"""
このスクリプトはBlender 公式python APIドキュメント(2.93)の解説ページコードを実行するためのものです
https://docs.blender.org/api/current/info_quickstart.html
"""

import bpy
import numpy as np

print("オブジェクトへのアクセス")
print(bpy.data.objects)
print(list(bpy.data.objects))

print("シーンへのアクセス")
print(bpy.data.scenes)
print(list(bpy.data.scenes))

print("マテリアル（＝シェーダーへのアクセス）")
print(bpy.data.materials)
print(list(bpy.data.materials))


print("プロパティへのアクセス")
print(bpy.data.objects[0].name)

print("個別の要素へのアクセス")
print(bpy.data.scenes["Scene"])

print("python APIからアクセスできるデータはbpy.data内部のデータだけ")
print("新しいオブジェクトを作成する場合はbpy.data内のメソッドを使用する")
print("マテリアル（＝シェーダー）の新規作成")
bpy.data.materials.new("MyMaterial")
print("作ったマテリアル（＝シェーダー）の削除")
bpy.data.materials.remove(bpy.data.materials["MyMaterial"])
print("メッシュの新規作成")
mesh = bpy.data.meshes.new(name="MyMesh")
print("メッシュの新規作成")
print(mesh)
print("作ったメッシュの削除")
bpy.data.materials.remove(mesh)
