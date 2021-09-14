# Good Cat Dector

1. 项目目的：检测猫咪是否上桌，防止猫咪上桌乱翻；


2. 项目介绍：
    1. 硬件： 树莓派3B+(建议4B), CSI camera, 双自由度舵机
    2. 关键算法：
        * opecv2录像
        * 目标检测
            1. 检测算法：yolo
            2. 推理引擎：MNN

    
3. How to run ?
    1. burn a raspberry image, prepare ssh, network connnection and camera
    2. Enter the os via ssh, 'cd GoodCat/Yolo-Fastest-MNN/build && cmake .. && make && sudo ./yolo'


4. 拓展：
    有20个类别可供检测，如人，可修改对应的目标索引；  
    20个类别分别为[	"Aeroplane","Bicycle","Bird","Boat","Bottle","Bus","Car","Cat","Chair",
    "Cow","Diningtable","Dog","Horse","Motorbike","Person","Pottedplant","Sheep","Sofa","Train","Tvmonitor"]


5. Reference
> 目标检测: https://github.com/dog-qiuqiu/Yolo-Fastest 
        https://github.com/geekzhu001/Yolo-Fastest-MNN
> MNN: https://github.com/alibaba/MNN
    

