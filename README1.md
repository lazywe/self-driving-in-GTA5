# self-driving-in-GTA5
此项目在游戏GTA5中实现自动驾驶
使用方法及顺序如下：
1、启动collect_data.py，然后将GTA5分辨率设置为（1280*720），放置于屏幕左上角（坐标（0,0）处），然后直接在游戏里开车就行
2、启动split_data.py切分数据
3、启动train_model.py训练数据
4、启动test_model.py进行预测

# 文件说明
alexnet.py：AlexNet神经网络模型，包括一个自己改进过的模型（alexnet_pro）,本项目默认使用原始的AlexNet进行训练，如果有需要，可以在train_model.py中修改要使用的模型。

aug_funcs.py：
