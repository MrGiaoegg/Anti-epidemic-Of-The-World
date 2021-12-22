"""
程序简介:
本程序有一个大板块(主页面),其下有三个小板块。本程序主要分为一个大部分
大板块(root):
程序的主界面,有两个超链接,分别通往游戏界面和提示信息两个小板块;
小板块1(main):
游戏的主界面；
小板块2(info):
关于本程序的相关信息,包括开源地址；
小板块3(GameVarInfo):
关于游戏选项的解释和说明；
"""
"""
游戏主体简介:
"""

import tkinter
import webbrowser
from random import randint, shuffle, choice
from tkinter.ttk import *

# 创建窗口
root = tkinter.Tk()
root['background'] = 'LightSlateGray'

# 创建组件
RootTitle = tkinter.Label(root, text='抗疫长城', font=('华文行楷', 48), bg='LightSlateGray', fg='red')
RootTitle.pack()


# 信息界面
def VInfo():
    info = tkinter.Tk()

    def back():
        info.destroy()

    info['background'] = 'LightSlateGray'
    info.title('更多信息')
    info.geometry('640x260')
    TextOfInfoPage1 = "本程序为第十九届'广东省少年儿童发明奖'的参赛作品"
    TextOfInfoPage2 = '本程序没有使用任何一个第三方库!'
    TextOfInfoPage3 = 'GUI界面由Tk组件提供支持'
    TextOfInfoPage4 = '(已在github开源,遵循GPL2.0协议)'
    Text1 = tkinter.Label(info, text=TextOfInfoPage1)
    Text2 = tkinter.Label(info, text=TextOfInfoPage2)
    Text3 = tkinter.Label(info, text=TextOfInfoPage3)
    Text4 = tkinter.Label(info, text=TextOfInfoPage4)
    Text1.pack(anchor='center')
    Text2.pack(anchor='center')
    Text3.pack(anchor='center')
    Text4.pack(anchor='center')

    def OpenGitHubPage():
        webbrowser.open(r'https://github.com')

    BackBTN = tkinter.Button(info, text='返回', fg='black', command=back)
    BackBTN.pack(side='bottom', anchor='se')

    GitHubPage = tkinter.Button(info, text='github开源仓库地址', fg='black', command=OpenGitHubPage)
    GitHubPage.pack(side='bottom', anchor='se')
    info.mainloop()


def main():
    def SettingMain():
        setting = tkinter.Tk()

        def ExitSetting():
            setting.destroy()

        setting['background'] = 'LightSlateGray'
        BackB1 = tkinter.Button(setting, text='退出', fg='black', command=ExitSetting)
        BackB1.pack(side='bottom', anchor='se')
        setting.title('游戏设置')
        setting.geometry('640x260')

        # 游戏选项设置
        PersonNum = tkinter.IntVar()

        PersonNumT = Label(setting, text='模拟人数')
        PersonNumT.pack(ipadx='0.5c', padx='1m', side='left')

        PersonNumC = Combobox(setting)
        PersonNumC['values'] = ('1000人', '2000人', '5000人', '10000人')
        PersonNumC.current('0')
        PersonNumC.pack(padx='1m', side='left')

        PlaceT = Label(setting, text='地点')
        PlaceT.pack(ipadx='0.5c', padx='1m', side='left')

        PlaceC = Radiobutton(setting, text='学校(简单)', value=1)
        Place1C = Radiobutton(setting, text='火车站(困难)', value=0)
        PlaceC.pack(padx='1m', side='left')
        Place1C.pack(padx='1m', side='left')

    def StartMain():
        game = tkinter.Tk()

        def back():
            game.destroy()

        game['background'] = 'LightSlateGray'
        game.title('主游戏')
        game.geometry('640x260')
        Text = tkinter.Label(game, text='123')
        Text.pack()
        In = tkinter.Entry(game, height=210, width=60)
        BackBTN = tkinter.Button(game, text='返回', fg='black', command=back)
        BackBTN.pack(side='bottom', anchor='se')
        game.mainloop()

    SettingMain()


def ExitRoot():
    exit()


StartGame = tkinter.Button(root, text='开始游戏', fg='black', command=main)
ViewInfo = tkinter.Button(root, text='更多信息', fg='black', command=VInfo)
BackB = tkinter.Button(root, text='退出', fg='black', command=ExitRoot)
BackB.pack(side='bottom', anchor='se')
StartGame.pack(side='left', padx='4.5c', anchor='center')
ViewInfo.pack(side='left', anchor='center')

# 设置窗口属性
root.title('抗疫长城')
root.geometry('640x260')
root.mainloop()
