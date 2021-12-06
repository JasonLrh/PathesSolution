# PathesSolution

1. run
~~~shell
python3 find.py r
~~~
>  press `q` to quit  
2. config param
~~~python
# edit in config_param.py
~~~

## variable expalantion
`dictionary`
> `simulation_pos` : generate in random; [simulation varuiable]  

> `result_pos` : 这是视觉做出来的结果， 仿真的时候就直接simulation_pos在真区间，对应添加元素

`list`
> `pos` : current robot position，这玩意是计算了摄像机偏移量的位置哦  

> `target_position` :  目标位置，算法算出来的，各位铁子们要做的目标规划就是这玩意


## launch in real world

1. 首先得把DEBUG置False
2. 根据目前我方颜色设置运行参数，红方：`r`， 蓝方：`b`


## ros transform
1. 订阅机器人位置信息
2. 把while循环加上ros sleep
3. while循环添加发送节点信息
   * 信息格式
   ~~~json
   {
       "header": {
           "seq": 0, // count here
           "stamp": 1201  // timestamp here
       },
       "nodes": [
           {
               "color": "r",
               "position": [20,40],
               "state": 0,
           },
           {
                "color": "b",
                "position": [30,20],
                "state": 1,
           }
       ]
   }
   ~~~
   * 数据解释
      1. `color` : "r" or "b", 表示是红方还是蓝方
      2. `position` : [x,y] 表示盘子的位置
      3. `state` : 
           ||状态|
           |-|-|
           |0|盘子在当前视野中且|
           |1|在当前视野中竖立的盘子|
           |2|在当前视野中需要翻面的盘子|
           |3|盘子在历史视野中（状态不进行记忆）|
           |4|(球)|
