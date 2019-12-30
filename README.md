# self-driving-in-GTA5
此项目在游戏GTA5中实现自动驾驶 使用方法及顺序如下：

1、启动collect_data.py，手动将GTA5分辨率设置为（1280*720） ，放置于屏幕左上角（坐标（0,0）处），然后直接在游戏里开车就行，不用考虑窗口顶部的bar，在截取图像的代码里已经将那部分排除掉了

2、启动split_data.py，切分数据 

3、启动train_model.py训练数据 

4、启动test_model.py，手动将GTA5分辨率设置为（1280*720） ，放置于屏幕左上角（坐标（0,0）处），然后由模型预测出结果然后电脑就会自动驾驶车辆

# 配置要求

# mod
Drive Modes & Custom Vehicle Cameras:修改第一人称视角，不然以第一人称开车的话，有大部分画面都被车内装饰占据
https://www.gta5-mods.com/scripts/drive-modes#description_tab
# 修改分辨率

# 文件说明
alexnet.py：AlexNet神经网络模型，包括一个自己改进过的模型（alexnet_pro）,本项目默认使用原始的AlexNet进行训练，如果有需要，可以在train_model.py中修改要使用的模型。

aug_funcs.py：图像增强，不过本项目最终取消这个使用功能

collect_data.py：负责收集训练数据

collision_detection.py：碰撞检测，不同大小的物体有不同的阈值，当物体超过这个阈值，则判定过近并减速。

directkeys.py：因为GTA5使用Scan Codes才能控制，所以将所需要的按键直接封装起来

find_lane.py：道路线检测

getkeys.py：获取正在按下的按键

grabscreen.py：屏幕截图，采用Windows API，实测下来比PIL速度快很多

roi_test.py：道路线检测中要进行roi（region of interest）检测，可以先用这个小文件尝试达到较好效果再修改find_lane.py里的内容

split_data.py：切分数据

test_model.py：进行模型预测，达到最终的自动驾驶

train_model.py：训练模型

view_data.py：查看收集到的数据的每一样本的图像数据和按键标签

yolo.py：YOLOv3，实现目标检测
