import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵切斯利'),
    TXT(0x02, '黛米'),
    TXT(0x03, '士兵儒勒'),
    TXT(0x04, '士兵埃克托尔'),
    TXT(0x05, '安敦'),
    TXT(0x06, '利库斯'),
    TXT(0x07, '利塔街道方向'),
    TXT(0x08, '庭园大道方向'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3401.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1A56
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
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
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 20790,
            z                   = 11750,
            y                   = 6470,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 10500,
            z                   = 0,
            y                   = -3140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 10500,
            z                   = 0,
            y                   = 3140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 14160,
            z                   = 13750,
            y                   = 1650,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 16520,
            z                   = 11750,
            y                   = -540,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -37360,
            z                   = 0,
            y                   = 960,
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
            x                   = 83520,
            z                   = 0,
            y                   = 630,
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
    )

# id: 0x10003 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -25540,
            y           = -1000,
            z           = -4310,
            range       = -27840,
            dword_10    = 0x00001388,
            dword_14    = 0x00001F90,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000011,
        ),
    )

# id: 0x10005 offset: 0x1F2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 15150,
            triggerZ            = 11750,
            triggerY            = 1650,
            triggerRange        = 400,
            actorX              = 14160,
            actorZ              = 15250,
            actorY              = 1650,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x216
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_230',
    )

    ClearChrFlags(0x000B, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, 0x0007)
    OP_64(0x00, 0x0001)

    Jump('loc_2CD')

    def _loc_230(): pass

    label('loc_230')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_24B',
    )

    SetChrPos(0x0008, 18040, 11750, -4680, 225)

    Jump('loc_2CD')

    def _loc_24B(): pass

    label('loc_24B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_260',
    )

    CreateThread(0x0008, 0x00, 0x00, 0x0007)
    OP_64(0x00, 0x0001)

    Jump('loc_2CD')

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_2B7',
    )

    SetChrPos(0x0008, 18300, 11750, -10110, 225)
    CreateThread(0x0008, 0x00, 0x00, 0x0003)
    SetChrPos(0x000C, 14830, 11750, 6510, 90)
    SetChrPos(0x000D, 16120, 11750, 4840, 315)
    ClearChrFlags(0x000C, 0x0004)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    OP_64(0x00, 0x0001)

    Jump('loc_2CD')

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2CD',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_341',
    )

    SetChrPos(0x000C, 14830, 11750, 6510, 90)
    SetChrPos(0x000D, 16120, 11750, 4840, 315)
    ClearChrFlags(0x000C, 0x0004)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, 18300, 11750, -10110, 225)
    CreateThread(0x0008, 0x00, 0x00, 0x0003)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)
    OP_A2(0x1413)
    SetMapFlags(0x10000000)
    Event(0, 0x000E)

    def _loc_341(): pass

    label('loc_341')

    Return()

# id: 0x0001 offset: 0x342
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE65D8, 0xFFFE0C00, 0x00230056)
    OP_1C(0x02, 0x00, 0x0012)
    OP_1C(0x03, 0x00, 0x0012)
    OP_1C(0x04, 0x00, 0x0012)
    OP_6F(0x0000, 160)
    OP_6F(0x0001, 160)
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_395',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_395(): pass

    label('loc_395')

    Return()

# id: 0x0002 offset: 0x396
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_3C7'),
        (0x00000001, 'loc_3D3'),
        (0x00000002, 'loc_3DF'),
        (0x00000003, 'loc_3EB'),
        (0x00000004, 'loc_3F7'),
        (0x00000005, 'loc_403'),
        (0x00000006, 'loc_40F'),
        (-1, 'loc_41B'),
    )

    def _loc_3C7(): pass

    label('loc_3C7')

    OP_99(0x00FE, 0x00, 0x07, 0x000005AA)

    Jump('loc_427')

    def _loc_3D3(): pass

    label('loc_3D3')

    OP_99(0x00FE, 0x00, 0x07, 0x0000060E)

    Jump('loc_427')

    def _loc_3DF(): pass

    label('loc_3DF')

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('loc_427')

    def _loc_3EB(): pass

    label('loc_3EB')

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('loc_427')

    def _loc_3F7(): pass

    label('loc_3F7')

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_427')

    def _loc_403(): pass

    label('loc_403')

    OP_99(0x00FE, 0x00, 0x07, 0x00000546)

    Jump('loc_427')

    def _loc_40F(): pass

    label('loc_40F')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_427')

    def _loc_41B(): pass

    label('loc_41B')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_427')

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_43C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_427')

    def _loc_43C(): pass

    label('loc_43C')

    Return()

# id: 0x0003 offset: 0x43D
@scena.Code('func_03_43D')
def func_03_43D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_460',
    )

    OP_8D(0x00FE, 20420, -7160, 16050, -13610, 2000)

    Jump('func_03_43D')

    def _loc_460(): pass

    label('loc_460')

    Return()

# id: 0x0004 offset: 0x461
@scena.Code('func_04_461')
def func_04_461():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_484',
    )

    OP_8D(0x00FE, 15300, 14530, 19530, 9890, 2000)

    Jump('func_04_461')

    def _loc_484(): pass

    label('loc_484')

    Return()

# id: 0x0005 offset: 0x485
@scena.Code('func_05_485')
def func_05_485():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A8',
    )

    OP_8D(0x00FE, 15160, 2490, 19190, -2240, 2000)

    Jump('func_05_485')

    def _loc_4A8(): pass

    label('loc_4A8')

    Return()

# id: 0x0006 offset: 0x4A9
@scena.Code('func_06_4A9')
def func_06_4A9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4CC',
    )

    OP_8D(0x00FE, 30170, 1730, 27910, -3560, 2000)

    Jump('func_06_4A9')

    def _loc_4CC(): pass

    label('loc_4CC')

    Return()

# id: 0x0007 offset: 0x4CD
@scena.Code('func_07_4CD')
def func_07_4CD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4F0',
    )

    OP_8D(0x00FE, 23750, 7410, 18380, -2820, 2000)

    Jump('func_07_4CD')

    def _loc_4F0(): pass

    label('loc_4F0')

    Return()

# id: 0x0008 offset: 0x4F1
@scena.Code('func_08_4F1')
def func_08_4F1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 4, 0x1414)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_502',
    )

    Call(0, 0x000F)

    Return()

    def _loc_502(): pass

    label('loc_502')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_5F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_58B',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校给人的\n',
            '印象更像是文官，\n',
            '不过实际上战斗力也十分了得哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是在魔法方面\n',
            '可是王国军中少数精锐之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EE')

    def _loc_58B(): pass

    label('loc_58B')

    ChrTalk(
        0x00FE,
        (
            '对签字仪式进行警戒的\n',
            '好像是雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且又是希德中校指挥，\n',
            '可以说是万无一失了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_5EE(): pass

    label('loc_5EE')

    Jump('loc_8CC')

    def _loc_5F1(): pass

    label('loc_5F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_70A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_67F',
    )

    ChrTalk(
        0x00FE,
        (
            '塔顶开始闪光是在\n',
            '诞辰庆典之后的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知何时起开始向天\n',
            '升起柱子一样的光线来了',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来就一直能看到\n',
            '塔顶上又光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_707')

    def _loc_67F(): pass

    label('loc_67F')

    ChrTalk(
        0x00FE,
        (
            '从这里能看到托兰特\n',
            '平原的『红莲之塔』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一直能看到\n',
            '塔顶有光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我向队长也报告过了，\n',
            '不过还是很在意那是什么光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_707(): pass

    label('loc_707')

    Jump('loc_8CC')

    def _loc_70A(): pass

    label('loc_70A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_76E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，真没办法……\n',
            '好不容易搞定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然地震很罕见，\n',
            '不过还是希望不要有第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CC')

    def _loc_76E(): pass

    label('loc_76E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_7C6',
    )

    ChrTalk(
        0x00FE,
        (
            '叫黛米的女孩子\n',
            '听说见过那个怪家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她在食堂工作，\n',
            '要不你们去问问？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CC')

    def _loc_7C6(): pass

    label('loc_7C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_809',
    )

    ChrTalk(
        0x00FE,
        (
            '你们看看这副样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能在晚饭之前\n',
            '整理好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CC')

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_8CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_859',
    )

    ChrTalk(
        0x0008,
        (
            '爬城墙可是很危险的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '得好好提醒一下\n',
            '那个年轻人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CC')

    def _loc_859(): pass

    label('loc_859')

    ChrTalk(
        0x0008,
        (
            '爬城墙可不正常。\n',
            '真是的，要是掉下来怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦！？　难、难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你、你没在想什么\n',
            '搞怪的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_8CC(): pass

    label('loc_8CC')

    TalkEnd(0x0008)

    Return()

# id: 0x0009 offset: 0x8D0
@scena.Code('func_09_8D0')
def func_09_8D0():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_908',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到圣海姆门。\n',
            '有事的话请进来说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF5')

    def _loc_908(): pass

    label('loc_908')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_99D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_954',
    )

    ChrTalk(
        0x00FE,
        (
            '埃克托尔去帮忙以后\n',
            '就没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是先吃饭了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99A')

    def _loc_954(): pass

    label('loc_954')

    ChrTalk(
        0x00FE,
        (
            '地震的善后\n',
            '总算是结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过埃克托尔那家伙还没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_99A(): pass

    label('loc_99A')

    Jump('loc_AF5')

    def _loc_99D(): pass

    label('loc_99D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_A33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_9F6',
    )

    ChrTalk(
        0x00FE,
        (
            '门内的大伙儿\n',
            '都在努力收拾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的搭档埃克托尔\n',
            '也急忙去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A30')

    def _loc_9F6(): pass

    label('loc_9F6')

    ChrTalk(
        0x00FE,
        (
            '刚才摇得挺厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没像这样\n',
            '感觉到危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_A30(): pass

    label('loc_A30')

    Jump('loc_AF5')

    def _loc_A33(): pass

    label('loc_A33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_AF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A6F',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎来到圣海姆门！\n',
            '也欢迎你们来旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF5')

    def _loc_A6F(): pass

    label('loc_A6F')

    ChrTalk(
        0x000A,
        (
            '欢迎来到圣海姆门！\n',
            '也欢迎你们来旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这里是名叫『亚宁堡』的\n',
            '古代长城的一部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '作为旅游名胜，\n',
            '来参观的人也很多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_AF5(): pass

    label('loc_AF5')

    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0xAF9
@scena.Code('func_0A_AF9')
def func_0A_AF9():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_BA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_B5D',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来很快就有\n',
            '条约的签字仪式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，队长又要在那儿\n',
            '嚷嚷强化警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B9E')

    def _loc_B5D(): pass

    label('loc_B5D')

    ChrTalk(
        0x00FE,
        (
            '地震好像也\n',
            '平息下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅客和我们都总算\n',
            '能放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_B9E(): pass

    label('loc_B9E')

    Jump('loc_C1E')

    def _loc_BA1(): pass

    label('loc_BA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_C1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_BE0',
    )

    ChrTalk(
        0x000B,
        (
            '没事情也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你们可以随意出入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1E')

    def _loc_BE0(): pass

    label('loc_BE0')

    ChrTalk(
        0x000B,
        (
            '哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果有什么事情\n',
            '就和里面的队长说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_C1E(): pass

    label('loc_C1E')

    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0xC22
@scena.Code('func_0B_C22')
def func_0B_C22():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0xC27
@scena.Code('func_0C_C27')
def func_0C_C27():
    UnlockAchievement(0x01, 0x0A, 0x00, 0x00)
    SetChrName('安敦')
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_CBB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_C77',
    )

    ChrTalk(
        0x00FE,
        (
            '差、差点就\n',
            '差点没命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～真吓人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB8')

    def _loc_C77(): pass

    label('loc_C77')

    ChrTalk(
        0x00FE,
        (
            '呼～呼……\n',
            '啊～真吓人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差、差点就\n',
            '差点没命了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_CB8(): pass

    label('loc_CB8')

    Jump('loc_D33')

    def _loc_CBB(): pass

    label('loc_CBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_D33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CF2',
    )

    ChrTalk(
        0x000C,
        (
            '再见──！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我的青春──！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D33')

    def _loc_CF2(): pass

    label('loc_CF2')

    ChrTalk(
        0x000C,
        (
            '诞辰庆典──！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我最讨厌了───！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哇──！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_D33(): pass

    label('loc_D33')

    TalkEnd(0x000C)

    Return()

# id: 0x000D offset: 0xD37
@scena.Code('func_0D_D37')
def func_0D_D37():
    SetChrName('利库斯')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_D56',
    )

    ClearChrFlags(0x000D, 0x0010)

    Jump('loc_D5B')

    def _loc_D56(): pass

    label('loc_D56')

    SetChrFlags(0x000D, 0x0010)

    def _loc_D5B(): pass

    label('loc_D5B')

    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_E76',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_DB9',
    )

    ChrTalk(
        0x00FE,
        (
            '这家伙地震的时候\n',
            '正好在爬城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被震感吓着了，\n',
            '差点就掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E73')

    def _loc_DB9(): pass

    label('loc_DB9')

    ChrTalk(
        0x00FE,
        (
            '这家伙地震的时候\n',
            '正好在爬城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被震感吓着了，\n',
            '差点就掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x000C, 400)

    ChrTalk(
        0x00FE,
        (
            '如果地震再稍微大一点，\n',
            '说不定真的就掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这一点上来说，安敦，\n',
            '可以说你算是走运的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_E73(): pass

    label('loc_E73')

    Jump('loc_F75')

    def _loc_E76(): pass

    label('loc_E76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_F75',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F22',
    )

    ChrTalk(
        0x000D,
        (
            '我的搭档安敦在诞辰庆典的时候\n',
            '向仰慕的女性告白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过残酷的现实是他被\n',
            '彻底地拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '再次来到这里也算\n',
            '他好像为了断却这个念想就去爬城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F75')

    def _loc_F22(): pass

    label('loc_F22')

    ChrTalk(
        0x000D,
        (
            '安敦…\n',
            '那边是蔡斯的方向啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果你恨诞辰庆典的话\n',
            '至少要面向王都吼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_F75(): pass

    label('loc_F75')

    TalkEnd(0x000D)

    Return()

# id: 0x000E offset: 0xF79
@scena.Code('func_0E_F79')
def func_0E_F79():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F8C',
    )

    Call(0, 0x0010)

    def _loc_F8C(): pass

    label('loc_F8C')

    OP_6D(29440, 0, 4420, 0)
    OP_67(0, 9960, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    OP_12(0x000088B8, 0x00061A80, 0x00000000)
    OP_C8(0x0200, 0x0046, 'C_PLAC09._CH', 0x01, 0x07D0)
    ShowPlaceName('圣海姆门')
    FadeIn(2000, 0)
    OP_6C(45000, 6000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T3411._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x101F
@scena.Code('func_0F_101F')
def func_0F_101F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1039',
    )

    Call(0, 0x0010)
    FadeIn(0, 0)

    def _loc_1039(): pass

    label('loc_1039')

    EventBegin(0x00)
    OP_4A(0x0008, 255)
    Fade(1000)
    SetChrPos(0x0101, 18120, 11750, -11850, 270)
    SetChrPos(0x00F7, 18420, 11750, -13130, 270)
    SetChrPos(0x0105, 19340, 11750, -11430, 270)
    SetChrPos(0x0104, 19610, 11750, -12770, 270)
    SetChrPos(0x0008, 16800, 11750, -12550, 90)
    OP_6D(17660, 11750, -12360, 0)
    OP_67(0, 7800, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(310000, 0)
    OP_6E(423, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#3090221084V#5P咦……你们是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221085V#1006F你就是切斯利先生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_118D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221086V#051F#6P我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221087V关于刚才的地震\n',
            '我们有事想问你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11EA')

    def _loc_118D(): pass

    label('loc_118D')

    ChrTalk(
        0x0103,
        (
            '#0030221088V#020F#6P我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221089V关于刚才的地震\n',
            '我们有事想问你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11EA(): pass

    label('loc_11EA')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行询问了关于他\n',
            '所看到的可疑人物的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#3090221090V#5P哦，昨天的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221091V#5P不，我怎么也不觉得\n',
            '那和地震有什么关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221092V#5P我在这里看到了一个\n',
            '个子非常高、戴着墨镜的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221093V#1002F果然如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060221094V#047F在沃尔费堡垒也有人\n',
            '看到了戴墨镜的男性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221095V#043F那个人到底做了什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221096V#5P不，他上到这里\n',
            '眺望了一会儿景色之后\n',
            '就下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221097V#5P我因为没见过戴墨镜的人，\n',
            '所以就注意了他一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221098V#5P他也没跟我打招呼，\n',
            '我也没主动跟他打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221099V#1007F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221100V#1015F还有没有人\n',
            '见过那个戴墨镜的男人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221101V#5P这一点倒是很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221102V#5P因为我觉得那个人太古怪了，\n',
            '就把他当作晚饭时的话题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221103V#5P不过其他人都说\n',
            '没见过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221104V#5P只有在食堂工作的\n',
            '叫黛米的女孩子好像见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040221105V#032F#7P唔，这个关卡和沃尔费堡垒\n',
            '不同，通行的人也很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221106V可是目击者却\n',
            '只有两个人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221107V#035F让人感觉有点不自然呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_167E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221108V#053F#6P慎重起见，也去跟\n',
            '那个女孩子打听一下吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221109V#050F是食堂的黛米吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E8')

    def _loc_167E(): pass

    label('loc_167E')

    ChrTalk(
        0x0103,
        (
            '#0030221110V#026F#6P慎重起见，也去跟\n',
            '那个女孩子打听一下吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221111V#020F在食堂工作的黛米是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16E8(): pass

    label('loc_16E8')

    ChrTalk(
        0x0101,
        (
            '#0010221112V#1006F谢谢，你提供的内容很重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221113V#5P能帮上你们就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3090221114V#5P要努力调查哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(18730, 11750, -12190, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 18730, 11750, -12190, 90)
    SetChrPos(0x0001, 18730, 11750, -12190, 90)
    SetChrPos(0x0002, 18730, 11750, -12190, 90)
    SetChrPos(0x0003, 18730, 11750, -12190, 90)
    OP_4B(0x0008, 255)
    OP_A2(0x1415)
    OP_28(0x0086, 0x01, 0x0008)
    OP_28(0x0086, 0x01, 0x0010)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0010 offset: 0x1817
@scena.Code('func_10_1817')
def func_10_1817():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1891'),
        (0x00000001, 'loc_1897'),
        (-1, 'loc_189D'),
    )

    def _loc_1891(): pass

    label('loc_1891')

    OP_A2(0x1200)

    Jump('loc_189D')

    def _loc_1897(): pass

    label('loc_1897')

    OP_A2(0x1201)

    Jump('loc_189D')

    def _loc_189D(): pass

    label('loc_189D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_18AB',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_18AF')

    def _loc_18AB(): pass

    label('loc_18AB')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_18AF(): pass

    label('loc_18AF')

    Return()

# id: 0x0011 offset: 0x18B0
@scena.Code('func_11_18B0')
def func_11_18B0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A23',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_191F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010221014V#1002F……这里的调查\n',
            '还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250473V赶快\n',
            '去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A03')

    def _loc_191F(): pass

    label('loc_191F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1996',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_193C',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_1943')

    def _loc_193C(): pass

    label('loc_193C')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_1943(): pass

    label('loc_1943')

    ChrTalk(
        0x0106,
        (
            '#0050221016V#050F这里的调查\n',
            '还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221017V我们赶快去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A03')

    def _loc_1996(): pass

    label('loc_1996')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19AC',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_19B3')

    def _loc_19AC(): pass

    label('loc_19AC')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_19B3(): pass

    label('loc_19B3')

    ChrTalk(
        0x0103,
        (
            '#0030221018V#020F这里的调查\n',
            '还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221019V我们赶快去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A03(): pass

    label('loc_1A03')

    OP_90(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_1A23(): pass

    label('loc_1A23')

    Return()

# id: 0x0012 offset: 0x1A24
@scena.Code('func_12_1A24')
def func_12_1A24():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
