# 仓库说明

这是游戏战舰世界朱雀院椿舰长语音包的工程文件备份。展示视频为：https://www.bilibili.com/video/BV1WN4y1n7J6

仅阅读本文档也许并不能够达到你阅读本文档的目的。

# 文件**结构说明**

## Audio_list文件夹

保存由模型生成的原语音，便于管理。

## Suzakuin_tsubaki文件夹

这是工程主目录。

Suzakuin_tsubaki.rvm为核心工程文件，非常重要。需要使用SoundModCreator打开。

Audio文件夹内为SoundModCreator读取的语音。


SoundModCreator不会读取外面的Audio_list文件夹内的语音！

SoundModCreator不会读取外面的Audio_list文件夹内的语音！

SoundModCreator不会读取外面的Audio_list文件夹内的语音！

## 原版参考文件夹

战舰世界原版日系舰长语音。

## enhance.py文件

使用SoundModCreator生成的语音包音量偏低。因此需要手动修正。

**使用方法：**

1、在使用SoundModCreator保存并检查项目后，不要立刻生成语音包banks文件夹。

2、运行该py文件。该文件作用是将Audio_list文件夹内的语音增益后放入Suzakuin_tsubaki\Audio目录内。

3、使用SoundModCreator生成语音包banks文件夹。此时将直接调用增益后的音频文件生成。

4、生成后的banks文件夹位于战舰世界res_mods文件夹内。

# 想要运行起来额外需要

1、用来生成语音的模型

2、WwiseLauncher安装在电脑上

3、免安装软件SoundModCreator

制作语音包的教程见：https://www.bilibili.com/video/BV1Ws4y1E7va

# 联系方式

stevenhayatori@outlook.com
