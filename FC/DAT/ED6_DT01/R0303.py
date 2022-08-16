import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0303   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0303.x'
    header.mapIndex       = 21
    header.bgm            = 22
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
            dword_00        = 0xFFFFFA24,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFF92A0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 315,
            word_34         = 315,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 21,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFFFA24,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFF92A0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 315,
            word_34         = 315,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 21,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000FA0,
            dword_08        = 0xFFFFD8F0,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 315,
            word_34         = 315,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 21,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFFFA24,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFF92A0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3200,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 315,
            word_34         = 315,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 21,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0x174
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
    ]

# id: 0x10001 offset: 0x196
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 8600,
            z                   = 4000,
            y                   = -8230,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '矿工兰古',
            x                   = -166100,
            z                   = 100,
            y                   = 127500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '见习矿工',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛鲁加山道方向',
            x                   = -167010,
            z                   = -70,
            y                   = 78790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛鲁加山道方向',
            x                   = -2070,
            z                   = -120,
            y                   = -72730,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x256
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x256
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2500,
            y           = -1000,
            z           = -45000,
            range       = 4000,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF38C8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = -2000,
            y           = 4000,
            z           = -7442,
            range       = 2000,
            dword_10    = 0x00001770,
            dword_14    = 0xFFFFE4E4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -168250,
            y           = -1000,
            z           = 128000,
            range       = -164500,
            dword_10    = 0x000007D0,
            dword_14    = 0x0001EBCC,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -2472,
            y           = -1000,
            z           = -21384,
            range       = 2537,
            dword_10    = 0x00001770,
            dword_14    = 0xFFFFB32C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x2D6
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('Init')
def Init():
    MapClearFlags(0x00400000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 4, 0x23C)),
            Expr.Return,
        ),
        'loc_2F3',
    )

    ChrSetPos(0x0009, -167300, 0, 128100, 180)

    def _loc_2F3(): pass

    label('loc_2F3')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000003, 'loc_2FF'),
        (-1, 'loc_339'),
    )

    def _loc_2FF(): pass

    label('loc_2FF')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    CameraMove(-166000, 0, 128270, 0)
    ChrSetPos(0x000A, -166200, 0, 131180, 0)
    Event(0, func_0F_1878)

    Jump('loc_339')

    def _loc_339(): pass

    label('loc_339')

    Return()

# id: 0x0001 offset: 0x33A
@scena.Code('func_01_33A')
def func_01_33A():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_352'),
        (0x00000065, 'loc_352'),
        (0x00000066, 'loc_36C'),
        (0x00000067, 'loc_36C'),
        (-1, 'loc_386'),
    )

    def _loc_352(): pass

    label('loc_352')

    OP_16(0x02, 4000, -128000, -166000, 196625)
    ChrClearFlags(0x000B, 0x0004)

    Jump('loc_386')

    def _loc_36C(): pass

    label('loc_36C')

    OP_16(0x02, 4000, -294000, -17000, 196714)
    ChrClearFlags(0x000C, 0x0004)

    Jump('loc_386')

    def _loc_386(): pass

    label('loc_386')

    Return()

# id: 0x0002 offset: 0x387
@scena.Code('func_02_387')
def func_02_387():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_387')

    def _loc_39C(): pass

    label('loc_39C')

    Return()

# id: 0x0003 offset: 0x39D
@scena.Code('func_03_39D')
def func_03_39D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_433',
    )

    ChrTalk(
        0x0009,
        (
            '哟，这不是\n',
            '游击士小姑娘小兄弟吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '坑道里面的魔兽\n',
            '终于停止骚动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '老大他很长时间没回家了，\n',
            '这次终于能回去好好休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BD')

    def _loc_433(): pass

    label('loc_433')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_48D',
    )

    ChrTalk(
        0x0009,
        (
            '我一稍不留神，\n',
            '提恩特那家伙\n',
            '就趁机溜走出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那家伙肯定又去翘班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BD')

    def _loc_48D(): pass

    label('loc_48D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    ChrTalk(
        0x0009,
        (
            '哦，这不是游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '有什么事吗？\n',
            '里面很暗，请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BD')

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_541',
    )

    ChrTalk(
        0x0009,
        (
            '哎呀哎呀，\n',
            '事情变得一塌糊涂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，\n',
            '多亏你们来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '没你们的话，\n',
            '事情可就糟啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BD')

    def _loc_541(): pass

    label('loc_541')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 4, 0x23C)),
            Expr.Return,
        ),
        'loc_58E',
    )

    ChrTalk(
        0x0009,
        (
            '里面很暗，请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '找加通老大的话，\n',
            '他应该在地下坑道里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BD')

    def _loc_58E(): pass

    label('loc_58E')

    ChrTalk(
        0x0009,
        (
            '喂，这里是玛鲁加矿山。\n',
            '无关人员不能进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BD(): pass

    label('loc_5BD')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x5C1
@scena.Code('func_04_5C1')
def func_04_5C1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 4, 0x254)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_126B',
    )

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x004A, 4, 0x254))
    CreateThread(0x000D, 0x01, 0x00, func_05_126C)
    CreateThread(0x000D, 0x02, 0x00, func_06_1276)
    CreateThread(0x0000, 0x01, 0x00, func_07_1288)
    CameraMove(0, 5200, -6500, 3000)
    Sleep(1000)

    Fade(1000)
    ChrSetPos(0x0101, -845, 0, -22467, 0)
    ChrSetPos(0x0102, 471, 0, -22527, 0)
    ChrSetPos(0x010F, -1170, 0, -24389, 0)
    ChrSetPos(0x0110, 72, 0, -24459, 0)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3000, 0)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x10F, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x10F, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x10F, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 0)
    OP_0D()

    ChrTalk(
        0x0110,
        (
            '#0280010582V#153F#4P哇……\n',
            '好高的建筑物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010583V#153F到底会有几层呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010584V#000F#1P这个嘛……\n',
            '我们之前只到过第二层。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010585V#000F这么高的塔，\n',
            '我想应该有五到六层左右吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010586V#010F#2P应该是五层，\n',
            '家里的资料是这样记载的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010587V#010F这里很久以前就有学者调查过，\n',
            '只不过后来被放置不理罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010588V#010F说起来，\n',
            '王国其它地方好像也有类似的塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0270010589V#140F#3P啊，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010590V#140F柏斯、卢安和蔡斯\n',
            '也建有同样建筑风格的塔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010591V#140F而且，\n',
            '好像是王国建国时期建造出来的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010592V#000F#1P啊～是吗。\n',
            '这座塔似乎很有历史价值嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0270010593V#141F#3P记录下这种价值就是我们来这的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010F, 0x0110, 400)
    ChrTurnDirection(0x0101, 0x0110, 400)
    ChrTurnDirection(0x0102, 0x0110, 400)

    ChrTalk(
        0x010F,
        (
            '#0270010594V#140F#3P朵洛希，\n',
            '先从低角度拍几张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0110, 0x010F, 400)

    ChrTalk(
        0x0110,
        (
            '#0280010595V#151F#4P好～的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0110, 2)
    CreateThread(0x0101, 0x01, 0x00, func_08_1292)
    CreateThread(0x0102, 0x01, 0x00, func_09_12AE)
    CreateThread(0x010F, 0x01, 0x00, func_0A_12CA)
    CreateThread(0x0110, 0x01, 0x00, func_0B_12E6)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x110, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x110, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x110, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 3000)
    ChrSetChipByIndex(0x0110, 3)

    ChrTalk(
        0x0110,
        (
            '#0280010596V#150F#4P好……我要拍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraSetDistance(2800, 1000)

    ChrTalk(
        0x0110,
        (
            '#0280010597V#150F#4P…………………………………………\n',
            '…………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010598V#004F（好，好厉害的气势……\n',
            '一拿起照相机，就像变了个人似的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010599V#010F（不愧是专业的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0110,
        (
            '#0280010600V#4P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010601V#4P……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010602V#4P……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x0110, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(2000)

    ChrTalk(
        0x0110,
        (
            '#0280010603V#4P呼～……Ｚｚｚ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x010F, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    OP_92(0x010F, 0x0110, 2000, 4000, 0x00)
    OP_92(0x010F, 0x0110, 1000, 5000, 0x00)
    OP_92(0x010F, 0x0110, 500, 6000, 0x00)
    ChrSetChipByIndex(0x0110, 2)
    PlaySE(125, 0x00, 0x64)
    ChrMoveTo(0x0110, 0, 0, -26700, 6000, 0x00)
    OP_63(0x0110)
    OP_62(0x0110, 0x00000000, 1900, 0x30, 0x32, 0x00000096, 0x00)
    PlaySE(48, 0x00, 0x64)
    Sleep(2000)

    OP_63(0x0110)
    Sleep(600)

    ChrTurnDirection(0x0110, 0x010F, 400)

    ChrTalk(
        0x0110,
        (
            '#0280010604V#152F#4P呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010605V#152F前辈，好疼啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0270010606V#144F我都和你说过多少次了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010607V#144F不要摆架势，\n',
            '照平时的样子去拍就行了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x010F, -3232, 0, -24431, 3000, 0x00)
    ChrTurnDirection(0x010F, 0x0110, 400)

    ChrTalk(
        0x0110,
        (
            '#0280010608V#151F#4P嘿嘿～\n',
            '果然还不太习惯拍照的方式啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010609V#151F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0110, -424, 0, -26391, 3000, 0x00)
    ChrSetChipByIndex(0x0110, 3)
    ChrSetDirection(0x0110, 0, 400)
    LoadEffect(0x00, 'map\\\\mp032_00.eff')

    ChrTalk(
        0x0110,
        (
            '#0280010610V#150F#4P哦哦，这个表情不错哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrMoveTo(0x0110, 758, 0, -26205, 3000, 0x00)

    ChrTalk(
        0x0110,
        (
            '#0280010611V#150F#4P真是性感啊。\n',
            '哇，太可爱了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrMoveTo(0x0110, -62, 0, -25625, 3000, 0x00)

    ChrTalk(
        0x0110,
        (
            '#0280010612V#151F#4P要照了，来喊『茄～子』㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    CreateThread(0x0110, 0x01, 0x00, func_0C_1302)
    OP_69(0x0102, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010613V#008F怎、怎么回事？\n',
            '又不是在拍人物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010614V#019F不过却有种奇妙的融合感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0270010615V#145F这家伙能看到景色的『表情』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010616V#145F她就是用这种白痴一样的做法，\n',
            '拍出很多让人叹为观止的照片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010617V#145F说起来，这也算是一种另类的天才吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010618V#501F呼……\n',
            '真是人不可貌相啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0110, 0xFF)
    Sleep(1000)

    ChrSetChipByIndex(0x0110, 65535)
    OP_92(0x0110, 0x0000, 1600, 3000, 0x00)
    ChrTurnDirection(0x0110, 0x010F, 400)
    ChrTurnDirection(0x010F, 0x0110, 400)

    ChrTalk(
        0x0110,
        (
            '#0280010619V#151F好了，让你们久等啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0270010620V#141F好，我们进去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010621V#141F目标是塔顶哦。\n',
            '拜托了，两位游击士新人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010622V#006F哼哼，交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010623V#006F不管出现什么样的魔兽，\n',
            '都不会让它碰你们一根手指的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010624V#010F进塔之后请不要离开我们身后啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_126B(): pass

    label('loc_126B')

    Return()

# id: 0x0005 offset: 0x126C
@scena.Code('func_05_126C')
def func_05_126C():
    OP_6C(0, 3000)

    Return()

# id: 0x0006 offset: 0x1276
@scena.Code('func_06_1276')
def func_06_1276():
    OP_67(0, 4500, -10000, 3000)

    Return()

# id: 0x0007 offset: 0x1288
@scena.Code('func_07_1288')
def func_07_1288():
    CameraSetDistance(6000, 3000)

    Return()

# id: 0x0008 offset: 0x1292
@scena.Code('func_08_1292')
def func_08_1292():
    ChrWalkTo(0x0101, -2478, 0, -22915, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0110, 400)

    Return()

# id: 0x0009 offset: 0x12AE
@scena.Code('func_09_12AE')
def func_09_12AE():
    ChrWalkTo(0x0102, -2610, 0, -23522, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0110, 400)

    Return()

# id: 0x000A offset: 0x12CA
@scena.Code('func_0A_12CA')
def func_0A_12CA():
    ChrWalkTo(0x010F, -3232, 0, -24431, 3000, 0x00)
    ChrTurnDirection(0x010F, 0x0110, 400)

    Return()

# id: 0x000B offset: 0x12E6
@scena.Code('func_0B_12E6')
def func_0B_12E6():
    ChrWalkTo(0x0110, -424, 0, -26391, 3000, 0x00)
    ChrSetDirection(0x0110, 0, 400)

    Return()

# id: 0x000C offset: 0x1302
@scena.Code('func_0C_1302')
def func_0C_1302():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1416',
    )

    ChrMoveTo(0x0110, -424, 0, -26391, 3000, 0x00)
    Sleep(2000)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrMoveTo(0x0110, 758, 0, -26205, 3000, 0x00)
    Sleep(1500)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    ChrMoveTo(0x0110, -62, 0, -25625, 3000, 0x00)
    Sleep(3000)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0110, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    Jump('func_0C_1302')

    def _loc_1416(): pass

    label('loc_1416')

    Return()

# id: 0x000D offset: 0x1417
@scena.Code('func_0D_1417')
def func_0D_1417():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 3, 0x23B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14B8',
    )

    EventBegin(0x00)
    ChrTurnDirection(0x0009, 0x0000, 400)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#0920010070V喂，这里是玛鲁加矿山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010071V无关人员不能进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.PushLong, 0x1E654),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_92(0x0000, 0x000D, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    ChrSetDirection(0x0009, 180, 0)
    OP_4B(0x0009, 255)

    Return()

    def _loc_14B8(): pass

    label('loc_14B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 3, 0x23B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 4, 0x23C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1876',
    )

    OP_4A(0x0009, 255)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0047, 4, 0x23C))
    OP_28(0x0003, 0x01, 0x0008)
    Fade(1000)
    ChrSetPos(0x0101, -166670, 30, 125190, 0)
    ChrSetPos(0x0102, -165340, 40, 125200, 0)
    CameraMove(-167300, 0, 128070, 2000)
    ChrTurnDirection(0x0009, 0x0101, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrWalkTo(0x0009, -166050, 0, 127040, 1000, 0x00)
    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#0920010072V#2P喂，这里是玛鲁加矿山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010073V#2P无关人员不能进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010074V#502F嘿嘿，我们是相关人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010075V#010F我们受洛连特的克劳斯市长委托，\n',
            '来这里收取七耀石的结晶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔出示市长的介绍信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0009,
        (
            '#0920010076V#2P哦，原来如此。\n',
            '这样就另当别论了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010077V#2P不好意思，\n',
            '你们直接进去找老大吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010078V#2P我还要留在这里值班。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010079V#505F等一下……老大……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010080V你还听不懂吗？\n',
            '我们是来找你们的矿长的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010081V#2P嘿嘿，我当然知道。\n',
            '矿长就是管我们这些矿工的加通老大嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010082V#2P七耀石矿脉就是他发现的。\n',
            '比起一日三餐，他更喜欢整天挖洞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010083V#2P今天他肯定也在地下矿坑里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010084V#010F明白了。\n',
            '那我们就进去找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, -167300, 0, 128100, 3000, 0x00)
    ChrSetDirection(0x0009, 180, 400)
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    def _loc_1876(): pass

    label('loc_1876')

    Return()

# id: 0x000E offset: 0x1877
@scena.Code('func_0E_1877')
def func_0E_1877():
    Return()

# id: 0x000F offset: 0x1878
@scena.Code('func_0F_1878')
def func_0F_1878():
    EventBegin(0x00)
    CameraMove(-166260, 20, 124370, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    ChrWalkTo(0x000A, -166330, -10, 122780, 5000, 0x00)
    ChrSetDirection(0x000A, 0, 400)

    ChrTalk(
        0x000A,
        (
            '#0990010257V真是失算啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010258V魔兽跑出来了，\n',
            '连游击士也出动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010259V唉，没办法……\n',
            '还是先回去如实报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)
    ChrWalkTo(0x000A, -166550, 20, 111740, 6000, 0x00)
    NewScene('ED6_DT01/C0100._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x198C
@scena.Code('func_10_198C')
def func_10_198C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 6, 0x21E)),
            Expr.Return,
        ),
        'loc_1A42',
    )

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrTurnDirection(0x0106, 0x0108, 0)

    ChrTalk(
        0x0108,
        (
            '#070F怎么了。\n',
            '现在要回城去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0106, 0)

    ChrTalk(
        0x0106,
        (
            '#050F不，还是算了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0000, 0, 0, -42800, 0)
    ChrSetPos(0x0001, 0, 0, -42800, 0)
    ChrSetPos(0x0002, 0, 0, -42800, 0)
    ChrSetPos(0x0003, 0, 0, -42800, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    MapSetFlags(0x00000001)
    EventEnd(0x00)

    Return()

    def _loc_1A42(): pass

    label('loc_1A42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A4B',
    )

    Return()

    def _loc_1A4B(): pass

    label('loc_1A4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 7, 0x217)),
            Expr.Return,
        ),
        'loc_1A53',
    )

    Return()

    def _loc_1A53(): pass

    label('loc_1A53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0044, 1, 0x221)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C5F',
    )

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_12(0x00009470, 0x00030D40, 0x00000000)

    @scena.Lambda('lambda_1A75')
    def lambda_1A75():
        CameraSetDistance(6000, 9500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1A75)

    @scena.Lambda('lambda_1A85')
    def lambda_1A85():
        OP_6C(0, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1A85)

    @scena.Lambda('lambda_1A95')
    def lambda_1A95():
        OP_67(0, 4000, -10000, 9500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_1A95)

    CameraMove(140, 5000, -10820, 6000)
    ChrSetPos(0x0101, 500, 100, -22600, 0)
    ChrSetPos(0x0102, -500, 100, -22600, 0)
    CreateThread(0x0102, 0x00, 0x00, func_11_1C60)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrWalkTo(0x0101, 500, 4000, -10440, 5000, 0x00)
    OP_A5(0x0003)
    WaitForThreadExit(0x0000, 0x0003)
    Fade(1000)
    OP_12(0x00009470, 0x000186A0, 0x00001F40)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2940, 0)
    OP_6C(315000, 0)
    CameraMove(140, 4000, -10820, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010000929V#002F虽然来到翡翠之塔了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000930V#002F可没在山路上遇到那两个孩子，\n',
            '也就是说……他们已经进去这里面了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000931V#012F看来可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000932V#012F我们进去吧。\n',
            '……必须赶快才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#0010000933V#002F嗯……是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_28(0x0001, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0044, 1, 0x221))

    def _loc_1C5F(): pass

    label('loc_1C5F')

    Return()

# id: 0x0011 offset: 0x1C60
@scena.Code('func_11_1C60')
def func_11_1C60():
    OP_A6(0x0003)
    Sleep(500)

    ChrWalkTo(0x00FE, -500, 4000, -11310, 5000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0012 offset: 0x1C80
@scena.Code('func_12_1C80')
def func_12_1C80():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0043, 6, 0x21E)),
            Expr.Return,
        ),
        'loc_1C92',
    )

    EventBegin(0x00)
    NewScene('ED6_DT01/C2100._SN', 1, 0, 0)
    IdleLoop()

    def _loc_1C92(): pass

    label('loc_1C92')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
