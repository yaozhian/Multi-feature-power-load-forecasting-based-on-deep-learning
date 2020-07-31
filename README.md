# 多特征电能负荷预测 #
电能负荷预测按细粒度划分可分为粗度预测和细度预测。其中粗度预测则是将整个时间段的电能负荷数据进行训练，进而进行预测。而细度预测这是要考虑电能负荷季节，时间周期影响因子。  
在进行城市居民电能负荷粗度预测时需要考虑比较如下三种情况的准确率：   
1.	利用上一时刻的电能负荷（power），温度（temperature），湿度（humidity），风速（speed）预测此刻的电能负荷，power_load_forecasting_V1   
2.	利用上一时刻的电能负荷（power）和此刻的温度（temperature），湿度（humidity），风速（speed）预测此刻的电能负荷，见电能负荷预测(二)   
3.	利用上一若干时刻的电能负荷（power），温度（temperature），湿度（humidity），风速（speed）预测此刻的电能负荷，见电能负荷预测(三)   
在进行城市居民电能负荷细度预测时，除了要考虑如上问题时，还需要考虑季节，时间周期等影响因子：  
1.	电力负荷往往具有周期性，夏季，冬季，过渡季（春季和秋季）用户用电量往往差距很大，因此在预测是可以考虑分开预测，见电能负荷预测(四)   
2.	在各个季节进行预测是，我们还可以按天，周，月进行划分，见电能负荷预测(五)  
# 多特征预测可以参考Jason Brownlee博士的教程 #
[Jason Brownlee博士主页]<https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/>  
[Jason Brownlee博士博客]<https://blog.csdn.net/tMb8Z9Vdm66wH68VX1/article/details/78463811> 
# 实验环境 #
编译语言：Python3.6  
深度学习框架：tensorflow2.0， keras  
依赖库：pandas，sklearn，matplotlib，numpy
