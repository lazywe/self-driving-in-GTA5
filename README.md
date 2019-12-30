# self-driving-in-GTA5
此项目在游戏GTA5中实现自动驾驶  

首先由真人玩家驾驶车辆，同时搜集数据，数据包括图像和对应的操作。让电脑以这些数据进行训练，最终学会模仿人类开车，以上端到端（end-to-end）自动驾驶思想，本项目在实现此基础之上，还增加了道路线检测和目标检测和碰撞检测，以此提高自动驾驶的准确度。

使用方法及顺序如下：

1、启动collect_data.py，手动将GTA5分辨率设置为（1280*720） ，放置于屏幕左上角（坐标（0,0）处），然后直接在游戏里开车就行，不用考虑窗口顶部的bar，在截取图像的代码里已经将那部分排除掉了

2、启动split_data.py，切分数据，这里需要根据你的路径对应修改代码里的路径  

3、启动train_model.py训练数据，这里需要根据你的路径对应修改代码里的路径   

4、启动test_model.py，手动将GTA5分辨率设置为（1280*720） ，放置于屏幕左上角（坐标（0,0）处），然后由模型预测出结果然后电脑就会自动驾驶车辆

# 配置要求
1、道路线检测功能主要吃CPU，中低负载吧  
2、目标检测+碰撞检测功能因为使用YOLOv3，建议6G显存及以上（你也可以使用YOLOv3-tiny，网络比较小，速度更快，但是准确率有所下降）  
3、最终的自动驾驶，包括以上两个功能，还有一个模型对驾驶的实时决策，所以这个项目是有2个模型一起工作的，建议显存11G及以上 

# mod
Drive Modes & Custom Vehicle Cameras:修改第一人称视角，不然以第一人称开车的话，有大部分画面都被车内装饰占据 
https://www.gta5-mods.com/scripts/drive-modes#description_tab  
SpeedLimiter:限制车辆速度，不然按游戏车辆设定，一直加速下去的话，即便真人玩家也很难操控  
https://www.gta5-mods.com/scripts/speedlimiter-net  
Enhanced Native Trainer：一个很万能的修改器，可以限制环境天气变化，防止被警察通缉等  
https://www.gta5-mods.com/scripts/enhanced-native-trainer-zemanez-and-others  

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
