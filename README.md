# 青少年Python 100天学习计划 🐍

一套面向 **12-16岁、零编程基础** 青少年的100天Python自学课程。最初是为自己孩子做的，现在整理出来，希望对其他家庭也有用。

不需要安装任何软件，用浏览器打开 [Google Colab](https://colab.research.google.com) 就能直接学习和写代码（下面有详细说明）。

## 这个课程是什么样的

- **100天，分成约15周**，从"变量、print()"这种最基础的概念开始，逐步学到函数、面向对象、文件操作，最后用 `pygame` 做出几个完整的小游戏。
- 每周都是一个独立的 Jupyter Notebook（`.ipynb`文件），**里面已经包含**：
  - 📖 **知识点讲解**：每天的教学内容，用青少年能看懂的语言，配生活化的例子
  - ✏️ **练习题**：每道题都是"填空"形式（函数体先留空），写代码的地方有明确标注
  - 🔍 **自动检测**：写完代码运行一下，程序会自动告诉你对不对（✅/❌），不需要家长一直盯着答案
  - 🔊 **语音讲解**（目前只有第1周试点版本有）：每天的讲解配了一段AI语音朗读，点开就能听
- **这个notebook本身不包含任何参考答案**，这是故意的——目的是让孩子自己动手思考、自己调试，这也是学编程最重要的能力之一。遇到卡住的地方，建议家长/老师用"引导提问"的方式帮忙（给提示、举别的例子），而不是直接把答案告诉孩子。

## 课程目录

| 周数 | 内容主题 | 在Colab中打开 |
|---|---|---|
| 第1周（Day1-7，**语音试点版**） | Python入门：变量、数据类型、运算符、f-string | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC1%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day1-7-%E8%AF%95%E7%82%B9%E7%89%88%28%E5%90%AB%E8%AF%AD%E9%9F%B3%29.ipynb) |
| 前3周（Day1-21，经典版，无语音） | 入门 + 字符串/if判断 + 循环/列表 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E5%89%8D3%E5%91%A8%E7%BB%83%E4%B9%A0-Day1-21.ipynb) |
| 第4周（Day22-28） | 函数、参数、返回值、math模块 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC4%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day22-28.ipynb) |
| 第5周（Day29-35） | 列表进阶、元组、集合 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC5%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day29-35.ipynb) |
| 第6周（Day36-42） | 字典、嵌套数据结构 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC6%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day36-42.ipynb) |
| 第7周（Day43-49） | 文件读写、异常处理 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC7%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day43-49.ipynb) |
| 第8周（Day50-56） | 面向对象入门：类与对象 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC8%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day50-56.ipynb) |
| 第9周（Day57-63） | 面向对象进阶：继承、封装 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC9%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day57-63.ipynb) |
| 第10周（Day64-70） | pygame入门：窗口、事件、键盘 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC10%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day64-70.ipynb) |
| 第11周（Day71-77） | pygame：碰撞检测、游戏逻辑 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC11%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day71-77.ipynb) |
| 第12周（Day78-84） | pygame：完整小游戏综合练习 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC12%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day78-84.ipynb) |
| 第13周（Day85-91） | pygame：游戏状态、UI、音效 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC13%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day85-91.ipynb) |
| 第14周（Day92-98） | pygame：完整游戏项目 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC14%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day92-98.ipynb) |
| 第15周（Day101-107，计划延长） | 游戏进阶：排行榜、AI、粒子特效 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Foyang-Liu/Kids_Python_Learning/blob/main/%E7%AC%AC15%E5%91%A8%E8%AF%BE%E7%A8%8B%E4%B8%8E%E7%BB%83%E4%B9%A0-Day101-107.ipynb) |

> 💡 关于**第1周**：目前有两个版本可以选——新的"语音试点版"（讲解+语音朗读+练习在一个文件里，正在试验的新格式）和"前3周"合集里包含的经典版（Day1-21，没有语音，内容相同）。两个版本的练习题完全一样，选哪个都行；如果喜欢语音讲解这种新格式，欢迎告诉作者，后面会考虑把更多周都做成这样。

部分周还配有更详细的文字版讲解文档（`第N周详细课程-xxx.md`），内容和notebook里的📖讲解基本一致，适合想要更完整阅读体验、或者想打印出来看的人；也有一份 [`100天学习计划-总览.md`](100天学习计划-总览.md) 介绍整体安排。

## 怎么用（推荐：Google Colab，零安装）

[Google Colab](https://colab.research.google.com) 是Google提供的免费在线Jupyter Notebook环境，直接在浏览器里跑Python代码，不需要在电脑上装任何东西，只需要一个Google账号（和Gmail账号一样，免费注册）。

**第一步：打开notebook**

点击上面目录表格里任意一周的 **"Open In Colab"** 按钮，会直接在新标签页打开Colab，并自动加载好那一周的notebook内容。

（也可以手动打开：先登录 [colab.research.google.com](https://colab.research.google.com)，点左上角 `文件(File) → 打开笔记本(Open notebook)`，切换到 `GitHub` 这个标签页，粘贴仓库地址 `Foyang-Liu/Kids_Python_Learning`，就能看到所有notebook供选择。）

**第二步：保存一份自己的副本（重要！）**

直接从GitHub打开的notebook是"只读"模式，没办法保存你写的代码。第一次打开之后，记得点 `文件(File) → 在云端硬盘中保存一份副本(Save a copy in Drive)`，这样会在你自己的Google Drive里生成一份可以编辑、自动保存的副本，以后写代码、保存进度都在这份副本上进行。

**第三步：从上到下运行**

- 每个代码块（cell）左边有一个▶️小三角，点一下或者按 `Shift + Enter` 就会运行这一格代码。
- 必须**从上到下按顺序**运行——后面的练习经常要用到前面cell里定义好的工具函数，跳着运行会报错。
- 看到注释写着 `# ✏️ 你的代码` 的cell，把里面的 `pass` 删掉，换成你自己写的代码。
- 写完运行一下，再运行紧跟着的 `# 🔍 检测` cell，看看输出的是 ✅（通过）还是 ❌（有问题，看提示信息再改改）。

**关于语音讲解**（第1周试点版）：每天📖讲解后面有一个带🔊标记的cell，运行后会出现一个音频播放条，点播放就能听。这份notebook里的语音已经提前生成好并保存在文件里了，所以哪怕不点运行、第一次打开的时候也应该已经能看到播放条（Colab会显示notebook里保存好的输出）。

**如果Colab提示"无法识别的笔记本"或一直转圈**：刷新一下页面，或者检查一下网络；中国大陆访问Google服务可能需要能正常访问Google的网络环境。

## 适合谁

- 12-16岁、从零开始学编程的青少年，自学或者家长/老师陪同学习都可以。
- 建议每天投入45-60分钟：10-15分钟看/听讲解，30-40分钟动手写练习。
- 遇到调试不出来的问题，建议优先自己尝试、查报错信息、多试几次；实在卡住了再找别人帮忙，帮忙时建议多给提示少直接给答案，这样学到的东西才是自己的。

## 反馈和贡献

这套课程还在持续完善。如果发现内容有错误、练习题检测逻辑有bug、或者有改进建议，欢迎在这个仓库开一个 [Issue](https://github.com/Foyang-Liu/Kids_Python_Learning/issues)，或者直接联系作者。
