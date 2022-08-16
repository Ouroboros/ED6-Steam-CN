import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0410   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0410.x'
    header.mapIndex       = 13
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
    ]

# id: 0x10001 offset: 0x116
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '弗兰兹',
            x                   = 550,
            z                   = 0,
            y                   = 34500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '汉娜',
            x                   = 2580,
            z                   = 0,
            y                   = 36100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '查儿',
            x                   = 1730,
            z                   = 0,
            y                   = 23000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
    )

# id: 0x10002 offset: 0x176
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x176
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x176
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 720,
            triggerZ            = 0,
            triggerY            = 33340,
            triggerRange        = 800,
            actorX              = 550,
            actorZ              = 1500,
            actorY              = 34500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 6, 0x22E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B0',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    OP_64(0x00, 0x0001)

    def _loc_1B0(): pass

    label('loc_1B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1DC',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    OP_64(0x00, 0x0001)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    Jump('loc_208')

    def _loc_1DC(): pass

    label('loc_1DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1F4',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    OP_64(0x00, 0x0001)

    Jump('loc_208')

    def _loc_1F4(): pass

    label('loc_1F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1FE',
    )

    Jump('loc_208')

    def _loc_1FE(): pass

    label('loc_1FE')

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    def _loc_208(): pass

    label('loc_208')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_21C'),
        (0x00000064, 'loc_2AF'),
        (0x00000066, 'loc_2AF'),
        (-1, 'loc_2EE'),
    )

    def _loc_21C(): pass

    label('loc_21C')

    ChrSetPos(0x0101, 400, 0, 22000, 0)
    ChrSetPos(0x0102, 1600, 0, 22000, 0)
    ChrSetPos(0x0008, 300, 0, 24400, 180)
    ChrSetPos(0x0009, 1400, 0, 24900, 180)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)
    MapClearFlags(0x00000001)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0B_E24)

    Jump('loc_2EE')

    def _loc_2AF(): pass

    label('loc_2AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 0, 0x230)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 6, 0x22E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EB',
    )

    ChrSetPos(0x0008, 450, 0, 32400, 0)
    ChrSetPos(0x0009, 480, 0, 34510, 180)
    Event(0, func_08_646)
    MapSetFlags(0x00400000)
    MapClearFlags(0x00000001)

    def _loc_2EB(): pass

    label('loc_2EB')

    Jump('loc_2EE')

    def _loc_2EE(): pass

    label('loc_2EE')

    Return()

# id: 0x0001 offset: 0x2EF
@scena.Code('func_01_2EF')
def func_01_2EF():
    Return()

# id: 0x0002 offset: 0x2F0
@scena.Code('func_02_2F0')
def func_02_2F0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_305',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2F0')

    def _loc_305(): pass

    label('loc_305')

    Return()

# id: 0x0003 offset: 0x306
@scena.Code('func_03_306')
def func_03_306():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_329',
    )

    OP_8D(0x00FE, 560, 22800, 2860, 25700, 3000)

    Jump('func_03_306')

    def _loc_329(): pass

    label('loc_329')

    Return()

# id: 0x0004 offset: 0x32A
@scena.Code('func_04_32A')
def func_04_32A():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x32F
@scena.Code('func_05_32F')
def func_05_32F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0008,
        (
            '这次你们真是帮了大忙。\n',
            '这下就能恢复蔬菜的输出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '感谢你们的\n',
            '还有那些等着\n',
            '我们农场蔬菜的人们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '必须加把劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40C')

    def _loc_3BD(): pass

    label('loc_3BD')

    ChrTalk(
        0x0008,
        (
            '这次你们真是帮了大忙，\n',
            '这下就能恢复蔬菜的输出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真的十分感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40C(): pass

    label('loc_40C')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x410
@scena.Code('func_06_410')
def func_06_410():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_510',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '这不是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前多亏你们，\n',
            '现在孩子们晚上\n',
            '可以安心地睡觉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是要好好睡觉\n',
            '才能安心工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50D')

    def _loc_4AE(): pass

    label('loc_4AE')

    ChrTalk(
        0x00FE,
        (
            '之前多亏你们，\n',
            '现在孩子们晚上\n',
            '可以安心地睡觉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是要好好睡觉\n',
            '才能安心工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50D(): pass

    label('loc_50D')

    Jump('loc_5A6')

    def _loc_510(): pass

    label('loc_510')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_5A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_581',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚，\n',
            '你们已经成为很棒的游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但希望你们\n',
            '工作也不要太过蛮干哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A6')

    def _loc_581(): pass

    label('loc_581')

    ChrTalk(
        0x00FE,
        (
            '有空就再来玩，\n',
            '我们会等你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A6(): pass

    label('loc_5A6')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x5AA
@scena.Code('func_07_5AA')
def func_07_5AA():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_5FB',
    )

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那个……\n',
            '你是为了见我而来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_642')

    def _loc_5FB(): pass

    label('loc_5FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_642',
    )

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚，\n',
            '好想……你再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和维鲁等着你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_642(): pass

    label('loc_642')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x646
@scena.Code('func_08_646')
def func_08_646():
    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    OP_67(0, 7600, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    CreateThread(0x0001, 0x01, 0x00, func_09_DF6)
    CreateThread(0x0000, 0x01, 0x00, func_0A_E12)
    ChrWalkTo(0x0101, 300, 0, 24400, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0009, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001370V#001F叔叔、阿姨，\n',
            '你们早上好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001371V#010F早上好，很久没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0900001372V哎呀……\n',
            '原来是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '#0910001373V真是好久不见了。\n',
            '来找缇欧玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001374V#501F啊，刚才已经见到她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001375V#010F其实今天是为了协会的工作而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    CameraMove(-560, 200, 28600, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2550, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, -800, 200, 29120, 180)
    ChrSetPos(0x0009, 1150, 200, 29120, 180)
    ChrSetPos(0x0101, -800, 250, 26900, 0)
    ChrSetPos(0x0102, 1150, 250, 26800, 0)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    PlaySE(17, 0x00, 0x64)
    RemoveItem(0x0320, 1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '两人交出了介绍信，\n',
            '并说明了代替卡西乌斯执行任务的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0900001376V#2P……原来是这样啊，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001377V#2P但是，只派你们两个来清除魔兽，\n',
            '是不是太危险了点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001378V#2P是啊。\n',
            '万一被魔兽弄伤了怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001379V#006F叔叔你们别担心，\n',
            '我们毕竟已经是游击士了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001380V#006F清除魔兽之类的不算什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001381V#010F而且我们已经得到协会的许可。\n',
            '这件事就交给我们好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001382V#2P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001383V#2P好吧，那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001384V#501F谢谢叔叔⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001385V对了……那些魔兽是什么样子的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001386V#2P不太清楚到底是什么……\n',
            '样子看起来像大胖猫那样的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001387V#2P通常是三、四只在半夜里结伴出现，\n',
            '把田里的菜咬得遍地残渣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001388V#2P虽说不是很凶暴，\n',
            '不过动作却敏捷得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001389V#2P当你想要抓它的时候，\n',
            '它总会很快地转身溜走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001390V#002F嗯……好奇怪的魔兽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001391V#012F半夜才出现……\n',
            '也就是说我们要等到那个时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001392V#2P啊，天黑之前\n',
            '你们就好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001393V#2P你们两个今晚\n',
            '就在这里吃顿便饭吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001394V#001F嘿嘿，当然啦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001395V#001F汉娜阿姨做的菜最美味了，\n',
            '我好期待呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001396V#2P你这孩子真会说话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001397V#2P好了，为了不负你们的期待，\n',
            '我也会做出最拿手的好菜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/T0401._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0xDF6
@scena.Code('func_09_DF6')
def func_09_DF6():
    ChrWalkTo(0x0102, 1400, 0, 24900, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0009, 0)

    Return()

# id: 0x000A offset: 0xE12
@scena.Code('func_0A_E12')
def func_0A_E12():
    CameraMove(0, 0, 28000, 2000)

    Return()

# id: 0x000B offset: 0xE24
@scena.Code('func_0B_E24')
def func_0B_E24():
    EventBegin(0x00)
    MapSetFlags(0x00400000)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0910001623V谢谢啊。\n',
            '这次你们真是帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001624V不过最后却害你们没能完成任务。\n',
            '实在是有点过意不去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001625V#010F请不要介意。\n',
            '我们从这次任务中学到了很多东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001626V#010F如果以后再有需要帮助的地方，\n',
            '尽管联络游击士协会就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0910001627V一定会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0900001628V工作不忙的话要经常来这里住哦。\n',
            '到时候煮些更好吃的菜给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001629V#000F谢谢啦，缇欧，还有阿姨。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001630V#010F我们一定会再来拜访的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0000, 0x01, 0x00, func_0C_102C)
    Sleep(800)

    CreateThread(0x0001, 0x01, 0x00, func_0C_102C)
    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/T0400._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x102C
@scena.Code('func_0C_102C')
def func_0C_102C():
    ChrWalkTo(0x00FE, 1000, 0, 21300, 1500, 0x00)
    ChrWalkTo(0x00FE, 1000, 0, 19700, 1500, 0x00)
    ChrSetFlags(0x00FE, 0x0008)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
