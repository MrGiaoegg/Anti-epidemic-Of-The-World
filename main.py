"""
程序简介:
本程序有一个大板块(主页面),其下有三个小板块。本程序主要分为一个大部分
大板块(root):
程序的主界面,有两个超链接,分别通往游戏界面和提示信息两个小板块;
小板块1(main):
游戏的主界面；
小板块2(info):
关于本程序的相关信息,包括开源地址；
"""
# package 抗疫长城(Anti-epidemic Of The World)
# 这里使用风格不统一的写法(非驼峰)是因为这不遵循PEP标准
from webbrowser import open_new as open_new_web_page
from random import randint
from time import sleep

# 变量
FirstTime = True
PersonNumList = [1000, 2000, 5000, 10000]


# 防止代码重用

def IntQuestion(took, tlist):
    """tlist为可用的值的集合"""
    while True:
        try:
            a = int(input(f'{took}:'))
            if a not in tlist:
                raise ValueError
            else:
                return a
        except ValueError:
            print('输入错误,请重新输入!')


def StrQuestion(took):
    """took为字典参数"""
    while True:
        try:
            x = ''
            for i, j in took.items():
                x += f'输入{i}{j} '
            x = x[:-1]
            a = input(f'{x}:')
            if a not in list(took.keys()):
                raise ValueError
            else:
                return a
        except ValueError:
            print('输入错误,请重新输入!')


def BoolQuestion(took):
    while True:
        try:
            a = input(f'是否{took}?(是/否)')
            if a != '是' and a != '否':
                raise ValueError
            else:
                if a == '是':
                    return True
                else:
                    return False
        except ValueError:
            print('输入错误,请重新输入!')


# 程序主循环
while True:
    """root部分"""
    if FirstTime:
        print('欢迎来到抗疫长城!')
        FirstTime = False
    print('现在,你要做什么呢?')
    DictOfThingsPlayerWantDo = {'start': '开始游戏', 'info': '浏览程序相关信息', 'quit': '退出本程序'}
    ThingsPlayerWantDo = StrQuestion(DictOfThingsPlayerWantDo)
    # main部分
    if ThingsPlayerWantDo == 'start':
        print('\n' * 10)
        print('欢迎来到抗疫长城游戏!')
        print('这是一个回合制游戏,本游戏的胜利规则是隐性和确认感染者人数清零')
        print('如果全部模拟玩家都确认感染或全部玩家死亡,则游戏失败!')
        print('本游戏的模拟玩家分为健康、隐性感染、确认感染3种状态')
        print('感染者有3/10的概率痊愈')
        print('当游戏中的模拟明性感染者的数量超过总模拟人数的1/10后,所有健康玩家和隐性感染玩家会自动戴上口罩,而确认感染者将会自动进入医院')
        print('在医院的感染者会根据random模块生成的伪随机数确定是否痊愈,而医院的医生不会被感染,也不算进总模拟人数之中')
        print('当然,以上这些介绍仅供参考,具体数值要看你选择的毒株为准')
        # 游戏中会用到的变量
        DictOfVaccineOfResearch = {'轻型': '则疫苗持续一小段时间', '完全型': '则疫苗永久有效'}
        DictOfStrVariableOfGameOfPlace = {'all': '选择全局防控模式(上帝视角)', 'station': '设置火车站为地点'}
        DictOfStrVariableOfVirusStrain = {'Alpha': '阿尔法毒株', 'Beta': '贝塔毒株', 'Gamma': '伽马毒株', 'Delta': '德尔塔毒株'}
        Place = StrQuestion(DictOfStrVariableOfGameOfPlace)
        PersonNum = IntQuestion('模拟人数(1000人,2000人,5000人或10000人)', PersonNumList)
        print('选择毒株:', end='')
        VirusStrain = StrQuestion(DictOfStrVariableOfVirusStrain)
        Infected = IntQuestion('初始感染人数(1~10人)', [x for x in range(1, 11)])
        print('可研究疫苗种类选择:')
        VaccineTime = StrQuestion(DictOfVaccineOfResearch)

        # 初始化
        DiePerson = 0
        SimPlePerson = int()
        if PersonNum == 1000:
            SimPlePerson = 1000 - Infected
        elif PersonNum == 2000:
            SimPlePerson = 2000 - Infected
        elif SimPlePerson == 5000:
            SimPlePerson = 5000 - Infected
        elif SimPlePerson == 10000:
            SimPlePerson = 10000 - Infected

        GameRound = 0
        Vaccine = 0
        InfectionRate = 0
        RecoveryRate = 0
        if Place == '火车站':
            print('由于您选择了火车站作为地点,所以需要额外输入几个变量')
            HumanTraffic = BoolQuestion('每日人流量')
        if VaccineTime == '持续一小段时间':
            Vaccine = 1 / 9
        elif VaccineTime == ' 永久有效':
            Vaccine = 1 / 15
        if VirusStrain == 'Alpha':
            RecoveryRate = 1 / 11
            InfectionRate = 1 / 11
        elif VirusStrain == 'Beta':
            InfectionRate = 1 / 9
            RecoveryRate = 1 / 11
            if VaccineTime == '持续一小段时间':
                Vaccine = 1 / 8
            elif VaccineTime == ' 永久有效':
                Vaccine = 1 / 16
        elif VirusStrain == 'Gamma':
            RecoveryRate = 1 / 11
            InfectionRate = 1 / 8
            if VaccineTime == '持续一小段时间':
                Vaccine = 1 / 10
            elif VaccineTime == ' 永久有效':
                Vaccine = 1 / 16
        elif VirusStrain == 'Delta':
            InfectionRate = 1 / 4
            RecoveryRate = 1 / 11
            if VaccineTime == '持续一小段时间':
                Vaccine = 1 / 12
            elif VaccineTime == ' 永久有效':
                Vaccine = 1 / 20

        # 游戏内的一些其他变量
        FirstVaccine = True
        GlobalHealthyPerson = SimPlePerson
        GlobalRecessiveInfectionPerson = 0
        GlobalDetermineInfectionPerson = 1
        GlobalDiePerson = 0
        VacJ, VacJ1, VacJ2 = 0, 0, 0
        TEMPGR, NOWGR = 0, 0

        print('开始游戏!')
        # 游戏主循环
        while True:
            if GlobalDetermineInfectionPerson == SimPlePerson:
                print('全部模拟玩家已确认感染!')
                print('很遗憾,你输掉了本局游戏')
                print('再接再厉吧!')
                print('\n' * 10)
                break
            print('新的回合!')
            GameRound += 1
            if VaccineTime:
                print(f'疫苗研究进度为{VacJ}')
                if VacJ == VacJ2:
                    print('研究成功!')
                    TEMPGR = 5 + GameRound
                    NOWGR = GameRound
            if NOWGR == TEMPGR:
                print('全员接种成功!')
                if VirusStrain == 'Alpha':
                    RecoveryRate = 1 / 9
                    InfectionRate = 1 / 12
                elif VirusStrain == 'Beta':
                    InfectionRate = 1 / 10
                    RecoveryRate = 1 / 11
                elif VirusStrain == 'Gamma':
                    RecoveryRate = 1 / 6
                    InfectionRate = 1 / 6.5
                elif VirusStrain == 'Delta':
                    InfectionRate = 1 / 7
                    RecoveryRate = 1 / 9
            print('病毒传染了!')
            if Place == 'all':
                a1 = randint(1, round(GameRound * InfectionRate * 10))
                b1 = randint(1, round(GameRound * InfectionRate * 10))
                c1 = randint(1, round(GameRound * RecoveryRate * 10))
                GlobalHealthyPerson -= a1
                GlobalRecessiveInfectionPerson = GlobalRecessiveInfectionPerson + a1 - b1
                GlobalDetermineInfectionPerson = GlobalDetermineInfectionPerson + b1 - c1
                GlobalHealthyPerson += c1
            elif Place == 'station':
                a1 = randint(1, GameRound * InfectionRate * 10)
                b1 = randint(1, GameRound * InfectionRate * 10)
                c1 = randint(1, GameRound * RecoveryRate * 10)
                d1 = randint(1, GameRound * RecoveryRate * randint(10, 18))
                GlobalHealthyPerson -= a1
                GlobalRecessiveInfectionPerson = GlobalRecessiveInfectionPerson + a1 - b1 + d1 / 2
                GlobalDetermineInfectionPerson = GlobalDetermineInfectionPerson + b1 - c1 + d1 / 2
                GlobalHealthyPerson += c1
            while True:
                ChoiceOfMainGame = {'GlobalData': '浏览全局数据', 'StartVaccineResearch': '开始研究疫苗', 'next': '开始新的回合'}
                Choice = StrQuestion(ChoiceOfMainGame)
                if Choice == 'GlobalData':
                    print('\n' * 7)
                    print(f'目前健康人数:{GlobalHealthyPerson}')
                    print(f'目前隐性感染人数:{GlobalRecessiveInfectionPerson}')
                    print(f'目前确认感染人数:{GlobalDetermineInfectionPerson}')
                    print(f'目前死亡人数:{GlobalDiePerson}')
                    continue
                elif Choice == 'StartVaccineResearch':
                    if GameRound <= 10:
                        print('你目前还不能开始研究疫苗!')
                        print('你至少需要游玩十回合才能开始研究!')
                        continue
                    else:
                        print('开始研究!')
                        VaccineS = True
                        VacJ = Vaccine
                        VacJ1 = 1
                        VacJ2 = 1
                elif Choice == 'next':
                    break

    # info部分
    elif ThingsPlayerWantDo == 'info':
        print('\n' * 3)
        print('本程序的额外信息如下:')
        print("本程序为第十九届'广东省少年儿童发明奖'的参赛作品。")
        print("本程序没有使用任何一个第三方库!import的'time'、'webbrowser'、'random'皆为Python标准库。")
        print('本程序已在GitHub开源,遵循GPL2.0协议')
        DictOfThingsPlayerWantDoInInfoPage = {'quit': '退出本页面', 'SourceCode': '浏览源代码'}
        ThingsPlayerWantDoInInfoPage = StrQuestion(DictOfThingsPlayerWantDoInInfoPage)
        if ThingsPlayerWantDoInInfoPage == 'quit':
            continue
        elif ThingsPlayerWantDoInInfoPage == 'SourceCode':
            print('正在打开网址,若没有自动打开,请手动输入地址https://github.com/MrGiaoegg/Anti-epidemic-Of-The-World')
            open_new_web_page(r'https://github.com/MrGiaoegg/Anti-epidemic-Of-The-World')
    elif ThingsPlayerWantDo == 'quit':  # 此处若使用else,会触发bug
        SureToExit = BoolQuestion('确定退出?')
        if SureToExit:
            print('感谢使用本程序!')
            sleep(0.7)
            exit()
        else:
            continue
