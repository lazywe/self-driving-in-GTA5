**tips：**

**1.README分中文版和英文版，英文版在下面  
2.记得手动下载model_data/yolo.h5文件并放到项目model_data文件夹里面，因为它是大文件，git clone的时候没有自动下载  
1.README is divided into Chinese version and English version, English version is at the bottom  
2.Remember to  download the model_data / yolo.h5 file manually and put it in the project model_data folder manually.Because it is a large file, it does not download automatically when git clone**  

# self-driving-in-GTA5
此项目在游戏GTA5中实现自动驾驶  
![Image text](https://github.com/linlihan-1/self-driving-in-GTA5/blob/master/picture/GIF8.gif)  
首先由真人玩家驾驶车辆，同时搜集数据，数据包括图像和对应的操作。让电脑以这些数据进行训练，最终学会模仿人类开车，以上就是端到端（end-to-end）自动驾驶思想，本项目在实现此基础之上，还增加了道路线检测和目标检测和碰撞检测，以此进一步提高自动驾驶的准确度。

使用方法及顺序如下：

1、启动**collect_data.py**，手动将GTA5分辨率设置为（1280*720） ，放置于屏幕左上角（坐标（0,0）处），然后直接在游戏里开车就行，不用考虑窗口顶部的bar，在截取图像的代码里已经将那部分排除掉了

2、启动**split_data.py**，切分数据，这里需要根据你的路径对应修改代码里的路径  

3、启动**train_model.py**训练数据，这里需要根据你的路径对应修改代码里的路径   

4、启动**test_model.py**，手动将GTA5分辨率设置为（1280*720） ，放置于屏幕左上角（坐标（0,0）处），然后由模型预测出结果然后电脑就会自动驾驶车辆

# 配置要求
1、道路线检测功能主要吃CPU，中低负载吧  

2、目标检测+碰撞检测功能因为使用YOLOv3，**建议6G显存及以上**（你也可以使用YOLOv3-tiny，网络比较小，配置要求没那么高，但是准确率有所下降）  

3、最终的自动驾驶，包括以上两个功能，还有一个模型对驾驶的实时决策，所以这个项目是有2个模型一起工作的，**建议显存11G及以上** 

# 所需mod
Drive Modes & Custom Vehicle Cameras:  修改第一人称视角，不然以第一人称开车的话，有大部分画面都被车内装饰占据 
https://www.gta5-mods.com/scripts/drive-modes#description_tab  
![Image text](https://github.com/linlihan-1/self-driving-in-GTA5/blob/master/picture/2.png)  

SpeedLimiter:  限制车辆速度，不然按游戏车辆设定，一直加速下去的话，即便真人玩家也很难操控  
https://www.gta5-mods.com/scripts/speedlimiter-net  

Enhanced Native Trainer：  一个很万能的修改器，可以限制环境天气变化，防止被警察通缉等，减少干扰因素  
https://www.gta5-mods.com/scripts/enhanced-native-trainer-zemanez-and-others  


# 文件说明
**alexnet.py**：AlexNet神经网络模型，包括一个自己改进过的模型（alexnet_pro）,本项目默认使用原始的AlexNet进行训练，如果有需要，可以在**train_model.py**中修改要使用的模型。

**aug_funcs.py**：图像增强，不过本项目最终取消使用这个功能

**collect_data.py**：负责收集训练数据

**collision_detection.py**：碰撞检测，不同大小的物体有不同的阈值，当物体超过这个阈值，则判定过近，发出警告并强制减速。

**directkeys.py**：因为GTA5使用Scan Codes才能控制，所以将所需要的按键直接封装起来

**find_lane.py**：道路线检测

**getkeys.py**：获取正在按下的按键

**grabscreen.py**：屏幕截图，采用Windows API，实测下来比PIL速度快很多

**roi_test.py**：道路线检测中要进行roi（region of interest）检测，可以先用这个小文件尝试达到较好效果再修改find_lane.py里的内容

**split_data.py**：切分数据

**test_model.py**：进行模型预测，达到最终的自动驾驶

**train_model.py**：训练模型

**view_data.py**：查看收集到的数据的每一样本的图像数据和按键标签

**yolo.py**：YOLOv3，实现目标检测


# English：
# self-driving-in-GTA5
This project implements autopilot in game GTA5  
![Image text](https://github.com/linlihan-1/self-driving-in-GTA5/blob/master/picture/GIF8.gif)  

First, a real player drives the vehicle and collects data at the same time. The data includes images and corresponding operations. Let the computer train with this data, and finally learn to imitate human driving. The above is the end-to-end autonomous driving idea.
On the basis of the above functions, this project also adds road line detection, object detection and collision detection.
Thereby further improving the accuracy of autonomous driving.

The usage method and sequence are as follows:

1. Start **collect_data.py**, set GTA5 resolution to (1280*720) manually, place it in the upper left corner of the screen (coordinates (0,0)), and then drive directly in the game, without considering the bar at the top of the window, because that part has been excluded in the code of image capture

2. Start **split_data.py** to split the data. You need to change the path in the code according to your path

3. Start **train_model.py** training data, where you need to modify the path in the code according to your path

4. Start **test_model.py**, manually set the resolution of GTA5 to (1280*720), place it in the upper left corner of the screen (coordinates (0,0)), predict the result by the model, and then the computer will drive the vehicle automatically

# configuration requirements
1. Route detection will take up some CPU resources, but it has little impact  

2.Because of the use of YOLOv3-3 for object detection and collision detection, **it is recommended to use 6G video memory or above** (you can also use yolov3-tiny, the network is small, the configuration requirements are not as high, but the accuracy is decreased).  

3.Complete automatic driving, including the above two functions, and a model for real-time decision-making on driving, so this project has two models working together, **it is recommended to use 11G video memory or above**  

# mod
Drive Modes & Custom Vehicle Cameras:  Modify the first-person perspective, or if driving in the first person, most of the screen will be occupied by the scene in the car  
https://www.gta5-mods.com/scripts/drive-modes#description_tab  
![Image text](https://github.com/linlihan-1/self-driving-in-GTA5/blob/master/picture/2.png)  

SpeedLimiter:  Limit vehicle speed.Otherwise, according to the game vehicle settings, it will be difficult to control even real players if you keep accelerating.  
https://www.gta5-mods.com/scripts/speedlimiter-net  

Enhanced Native Trainer：  A useful modifier that can limit environmental weather changes, prevent wanted by the police, etc., reduce the interference factors of the experiment  
https://www.gta5-mods.com/scripts/enhanced-native-trainer-zemanez-and-others  

# file description
**alexnet.py**：Including an original AlexNet model and an improved model (alexnet_pro), this project uses the original AlexNet for training by default. If necessary, you can modify the model to be used in **train_model.py**.

**aug_funcs.py**：Image enhancement, however, was eventually eliminated in this project

**collect_data.py**：Collect training data

**collision_detection.py**：In collision detection, objects of different sizes have different thresholds. When an object exceeds this threshold, it is determined to be too close, a warning is issued and a deceleration is forced.

**directkeys.py**：GTA5 uses Scan Codes to control, so the required keys are directly packaged

**find_lane.py**：lane lines detection

**getkeys.py**：Get the key that is being pressed

**grabscreen.py**：Screenshot, using Windows API, measured much faster than PIL

**roi_test.py**：To detect roi (region of interest) in lane lines detection, you can use this small file to try to achieve better results and then modify the content in find_lane.py

**split_data.py**：split_data

**test_model.py**：model predictions,achieve autonomous driving

**train_model.py**：train_model

**view_data.py**：View collected data, including image data and key labels

**yolo.py**：YOLOv3，achieving object detection
