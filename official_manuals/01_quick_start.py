"""
このスクリプトはBlender 公式python APIドキュメント(2.93)の解説ページコードを実行するためのものです
https://docs.blender.org/api/current/info_quickstart.html
   【注意事項】
   - 書籍中のスクリプトを全てを載せているわけではない
"""

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


def step_01_access_to_data():
    print("######################")
    print("## 各種データへのアクセス")
    print("オブジェクトへのアクセス")
    print(bpy.data.objects)
    print(list(bpy.data.objects))

    print("シーンへのアクセス")
    print(bpy.data.scenes)
    print(list(bpy.data.scenes))

    print("マテリアル（＝シェーダーへのアクセス）")
    print(bpy.data.materials)
    print(list(bpy.data.materials))

    print(
        "プロパティへのアクセス",
    )
    print(bpy.data.objects[0].name)

    print("個別の要素へのアクセス")
    print(bpy.data.scenes["Scene"])
    print("## 各種データへのアクセス")
    print("######################")


def step_02_1_access_to_data():
    print("######################")
    print("## オブジェクト作成／削除（その１）")

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
    print("作ったメッシュの削除(削除するデータの種類ごとにremove()がある。")
    bpy.data.meshes.remove(mesh)
    # bpy.data.materials.remove(mesh)  # これはエラーになる
    print("==============================")
    print("環境要素へのアクセス（読み取り専用")
    print("https://docs.blender.org/api/current/bpy.context.html")
    print("【選択中のオブジェクト】", list(bpy.context.selected_objects))
    print("【見えているボーン】", bpy.context.visible_bones)

    print("## オブジェクト作成／削除（その１）")
    print("######################")


# ##################################
# ## オブジェクト作成
def step_02_2_access_to_data():
    print("######################")
    print("## オブジェクト作成／削除（その２）")
    print("全メッシュを削除")
    delete_all_meshes()

    print("格子状に🐵を配置")
    for k in range(5):
        for j in range(5):
            for i in range(5):
                # bpy.ops.mesh.primitive_monkey_add(size=0.25, location=(i, j, k))
                bpy.ops.mesh.primitive_cone_add(
                    scale=(0.3, 0.3, 0.3), location=(i, j, k)
                )
    print("## オブジェクト作成／削除（その２）")
    print("######################")


# ## オブジェクト作成
# ##################################

# ##################################
# ## アニメーション
def step_03_animation():
    print("######################")
    print("## アニメーション")
    # if bpy.context.object is not None:
    #     print("全メッシュを削除")
    #     delete_all_objects()
    # if bpy.context.object is None:
    #     print("適当に１つオブジェクト作成")
    #     bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0))

    print("アニメーションを付ける")
    obj = bpy.context.object
    for i in range(1000):
        obj.location[0] = math.sin(i)
        obj.location[1] = math.cos(i)
        obj.location[2] = math.sin(i) * math.cos(i)
        obj.keyframe_insert(data_path="location", frame=3 * i)
        obj.scale = (math.sin(i) + 1, math.sin(i) + 1, math.sin(i) + 1)
        obj.keyframe_insert(data_path="scale", frame=3 * i)
    print("## アニメーション")
    print("######################")


# ## アニメーション
# ##################################


def main():
    step_01_access_to_data()
    step_02_1_access_to_data()
    # step_03_animation()
    step_02_2_access_to_data()


if __name__ == "<run_path>":
    main()
