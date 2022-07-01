import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2700   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵尼克斯'),
    TXT(0x02, '士兵威尔斯'),
    TXT(0x03, '士兵库隆'),
    TXT(0x04, '梅尔茨'),
    TXT(0x05, '阿伊纳街道'),
    TXT(0x06, '卡鲁迪亚隧道'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2700.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2082
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 18400,
            z                   = 5000,
            y                   = 1400,
            direction           = 270,
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
            x                   = -18600,
            z                   = 0,
            y                   = 2300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 18400,
            z                   = 5000,
            y                   = 1400,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -22780,
            z                   = 0,
            y                   = 6880,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -62340,
            z                   = 0,
            y                   = -1100,
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
            x                   = 21320,
            z                   = 5000,
            y                   = 460,
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

# id: 0x10003 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x18A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x18A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 19830,
            triggerZ            = 5000,
            triggerY            = -50,
            triggerRange        = 800,
            actorX              = 19830,
            actorZ              = 6000,
            actorY              = -50,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -45890,
            triggerZ            = 0,
            triggerY            = 2240,
            triggerRange        = 1500,
            actorX              = -45890,
            actorZ              = 1700,
            actorY              = 2240,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3110,
            triggerZ            = 5000,
            triggerY            = 2490,
            triggerRange        = 1000,
            actorX              = 7850,
            actorZ              = -5000,
            actorY              = 9160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_21E',
    )

    SetChrPos(0x0008, 18400, 5000, 1400, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21B',
    )

    ClearChrFlags(0x000B, 0x0080)

    def _loc_21B(): pass

    label('loc_21B')

    Jump('loc_234')

    def _loc_21E(): pass

    label('loc_21E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_234',
    )

    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_234(): pass

    label('loc_234')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_240'),
        (-1, 'loc_254'),
    )

    def _loc_240(): pass

    label('loc_240')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 1, 0x1211)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_251',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0007)

    def _loc_251(): pass

    label('loc_251')

    Jump('loc_254')

    def _loc_254(): pass

    label('loc_254')

    Return()

# id: 0x0001 offset: 0x255
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDC5B0, 0xFFFE0C00, 0x0023004F)
    OP_E8(0xDC, 0x05, 0x00, 0x00)
    OP_1C(0x01, 0x00, 0x000C)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_289'),
        (0x00000065, 'loc_289'),
        (0x00000066, 'loc_291'),
        (0x00000067, 'loc_291'),
        (-1, 'loc_299'),
    )

    def _loc_289(): pass

    label('loc_289')

    OP_22(0x01CE, 0x01, 0x64)

    Jump('loc_299')

    def _loc_291(): pass

    label('loc_291')

    OP_22(0x01CA, 0x01, 0x64)

    Jump('loc_299')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AD',
    )

    OP_72(0x0002, 0x0010)
    OP_65(0x00, 0x0001)

    Jump('loc_2C4')

    def _loc_2AD(): pass

    label('loc_2AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_2C4',
    )

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 160)
    OP_64(0x00, 0x0001)

    def _loc_2C4(): pass

    label('loc_2C4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DC',
    )

    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 99)

    def _loc_2DC(): pass

    label('loc_2DC')

    Return()

# id: 0x0002 offset: 0x2DD
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

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_302',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_395')

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_395')

    def _loc_31B(): pass

    label('loc_31B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_334',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_395')

    def _loc_334(): pass

    label('loc_334')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_395')

    def _loc_34D(): pass

    label('loc_34D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_366',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_395')

    def _loc_366(): pass

    label('loc_366')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_395')

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_395',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_395')

    def _loc_3AA(): pass

    label('loc_3AA')

    Return()

# id: 0x0003 offset: 0x3AB
@scena.Code('func_03_3AB')
def func_03_3AB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_401',
    )

    ChrTalk(
        0x00FE,
        (
            '今天轮到我放哨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这么说来，到底是谁在下面\n',
            '办理通行手续呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_462')

    def _loc_401(): pass

    label('loc_401')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '尼克斯那家伙不能值勤，\n',
            '换我代替他放哨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，虽然不大明白…\n',
            '但这也是任务，没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_462(): pass

    label('loc_462')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x466
@scena.Code('func_04_466')
def func_04_466():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_521',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CE',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然扛着枪，\n',
            '但现在不能放子弹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想到就觉得不安，\n',
            '还是尽量不去想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_51E')

    def _loc_4CE(): pass

    label('loc_4CE')

    ChrTalk(
        0x00FE,
        (
            '虽然扛着枪，\n',
            '但现在不能放子弹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只靠枪和剑作战\n',
            '的演习都好久没做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51E(): pass

    label('loc_51E')

    Jump('loc_789')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_602',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A9',
    )

    ChrTalk(
        0x00FE,
        (
            '协会的游击士\n',
            '偶尔会来巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像在各地巡视，\n',
            '真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与我们巡逻的范围相比\n',
            '那可不是一个等级的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_5FF')

    def _loc_5A9(): pass

    label('loc_5A9')

    ChrTalk(
        0x00FE,
        (
            '这种时候我也明白\n',
            '巡视是很重要的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对方如此拼命\n',
            '自然这边也要精神振作起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FF(): pass

    label('loc_5FF')

    Jump('loc_789')

    def _loc_602(): pass

    label('loc_602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_698',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_64F',
    )

    ChrTalk(
        0x00FE,
        (
            '最近危险的魔兽\n',
            '也增加了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，好好\n',
            '休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_695')

    def _loc_64F(): pass

    label('loc_64F')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '哎呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然来到这种地方，\n',
            '是来消灭通缉魔兽的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_695(): pass

    label('loc_695')

    Jump('loc_789')

    def _loc_698(): pass

    label('loc_698')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_715',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_6D0',
    )

    ChrTalk(
        0x00FE,
        (
            '尼克斯那家伙好像\n',
            '真的看到了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_712')

    def _loc_6D0(): pass

    label('loc_6D0')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '尼克斯那家伙好像\n',
            '真的看到了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……还好我没看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_712(): pass

    label('loc_712')

    Jump('loc_789')

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_789',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_74A',
    )

    ChrTalk(
        0x00FE,
        (
            '近来游客也少,\n',
            '真是令人犯困啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_789')

    def _loc_74A(): pass

    label('loc_74A')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '呀，终于有人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '近来游客也少,\n',
            '真是令人犯困啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_789(): pass

    label('loc_789')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x78D
@scena.Code('func_05_78D')
def func_05_78D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_859',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_826',
    )

    ChrTalk(
        0x00FE,
        (
            '刚、刚才真令人难以置信，\n',
            '有人进了隧道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像有急事\n',
            '要返回蔡斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那小哥真勇敢啊。\n',
            '我要是女人真要喜欢上他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_853')

    def _loc_826(): pass

    label('loc_826')

    ChrTalk(
        0x00FE,
        (
            '刚、刚才真令人难以置信，\n',
            '有人进了隧道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_853(): pass

    label('loc_853')

    TalkEnd(0x00FE)

    Jump('loc_CF5')

    def _loc_859(): pass

    label('loc_859')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8C3',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '不妙啊……\n',
            '隧道一片漆黑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像随时会有魔兽跑出来似的。\n',
            '说、说实话，有点害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_CF5')

    def _loc_8C3(): pass

    label('loc_8C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 3, 0x1213)),
            Expr.Return,
        ),
        'loc_C66',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_9B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_938',
    )

    ChrTalk(
        0x00FE,
        (
            '配合条约签字仪式\n',
            '警备好像也强化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我明白是重要的仪式，\n',
            '不过跟我们没啥关系啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AF')

    def _loc_938(): pass

    label('loc_938')

    ChrTalk(
        0x00FE,
        (
            '配合互不侵犯条约的签字仪式\n',
            '关所的警备好像都强化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是王都周边倒还好说，\n',
            '不过我觉得这里好像没啥关系吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_9AF(): pass

    label('loc_9AF')

    Jump('loc_C60')

    def _loc_9B2(): pass

    label('loc_9B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_A43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_A02',
    )

    ChrTalk(
        0x00FE,
        (
            '那两个人相当着急呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，游击士\n',
            '好像都很忙，真够呛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A40')

    def _loc_A02(): pass

    label('loc_A02')

    ChrTalk(
        0x00FE,
        (
            '之前像是游击士\n',
            '的两个人来过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在隧道没碰到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A40(): pass

    label('loc_A40')

    Jump('loc_C60')

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_AEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_A9E',
    )

    ChrTalk(
        0x00FE,
        (
            '卡鲁迪亚丘陵周边\n',
            '地盘好像也还稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此地震什么的\n',
            '几乎没印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE7')

    def _loc_A9E(): pass

    label('loc_A9E')

    ChrTalk(
        0x00FE,
        (
            '好像在蔡斯地区\n',
            '发生地震了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔的地震\n',
            '好像很少见不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_AE7(): pass

    label('loc_AE7')

    Jump('loc_C60')

    def _loc_AEA(): pass

    label('loc_AEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_B5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B22',
    )

    ChrTalk(
        0x00FE,
        (
            '哈，难得来一趟。\n',
            '稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5C')

    def _loc_B22(): pass

    label('loc_B22')

    ChrTalk(
        0x00FE,
        (
            '呀，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然要过隧道\n',
            '又是什么工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_B5C(): pass

    label('loc_B5C')

    Jump('loc_C60')

    def _loc_B5F(): pass

    label('loc_B5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_C03',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BAF',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道会不会再出现，\n',
            '每晚都战战兢兢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快解决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C00')

    def _loc_BAF(): pass

    label('loc_BAF')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '哟，辛苦了。\n',
            '之后的调查怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不早点解决的话，\n',
            '永远都不能安心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C00(): pass

    label('loc_C00')

    Jump('loc_C60')

    def _loc_C03(): pass

    label('loc_C03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 2, 0x1212)),
            Expr.Return,
        ),
        'loc_C60',
    )

    ChrTalk(
        0x00FE,
        (
            '事到如今就算知道不是梦\n',
            '也够惹人生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，看到那个以后\n',
            '真是完全没好事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C60(): pass

    label('loc_C60')

    TalkEnd(0x0008)

    Jump('loc_CF5')

    def _loc_C66(): pass

    label('loc_C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 2, 0x1212)),
            Expr.Return,
        ),
        'loc_C74',
    )

    Call(0, 0x0008)

    Jump('loc_CF5')

    def _loc_C74(): pass

    label('loc_C74')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_CAA',
    )

    ChrTalk(
        0x00FE,
        (
            '隧道又暗又长呢。\n',
            '近来通过的人也少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF2')

    def _loc_CAA(): pass

    label('loc_CAA')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '这里是卡鲁迪亚隧道的入口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有通行准许证\n',
            '可不能再向前啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF2(): pass

    label('loc_CF2')

    TalkEnd(0x0008)

    def _loc_CF5(): pass

    label('loc_CF5')

    Return()

# id: 0x0006 offset: 0xCF6
@scena.Code('func_06_CF6')
def func_06_CF6():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D84',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是卢安支部所属\n',
            '梅尔茨准游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在到处\n',
            '巡视中！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然真是够累的，\n',
            '但这工作正适合我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_DDE')

    def _loc_D84(): pass

    label('loc_D84')

    ChrTalk(
        0x00FE,
        (
            '现在正在\n',
            '步行警戒中！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然真是够累的，\n',
            '但说到体力的话，我可是不会输给任何人的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DDE(): pass

    label('loc_DDE')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0xDE2
@scena.Code('func_07_DE2')
def func_07_DE2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DF3',
    )

    Call(0, 0x0009)

    def _loc_DF3(): pass

    label('loc_DF3')

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_4A(0x0008, 255)
    OP_6D(5900, 12000, 13400, 0)
    OP_6C(85000, 0)
    OP_6B(8000, 0)
    OP_12(0x00007D00, 0x0003D090, 0x00000000)
    SetChrPos(0x0101, -52500, 0, -1800, 90)
    SetChrPos(0x00F7, -52500, 0, -600, 90)
    OP_C8(0x0200, 0x0046, 'C_PLAC05._CH', 0x00, 0x07D0)
    ShowPlaceName('艾尔·雷登关所')
    FadeIn(2000, 0)
    OP_12(0x00007D00, 0x0001FBD0, 0x00002EE0)

    @scena.Lambda('lambda_0E91')
    def lambda_0E91():
        OP_6B(2800, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E91)

    @scena.Lambda('lambda_0EA1')
    def lambda_0EA1():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EA1)

    Sleep(3000)

    @scena.Lambda('lambda_0EB6')
    def lambda_0EB6():
        OP_6D(-50000, 0, -1500, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EB6)

    Sleep(8500)

    ChrTalk(
        0x0101,
        (
            '#0010201407V#1011F#6P艾尔·雷登关所……\n',
            '感觉好久没来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201408V#1016F这里有看到那个\n',
            '的士兵吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_10F1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201409V#051F#5P啊啊，嘉恩是这么说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201410V首先去找关所的队长\n',
            '问问看是谁吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201411V#1015F#6P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201412V#1007F哎～话说回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201413V这么漂亮的地方\n',
            '竟然会有那个出现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050201414V#552F#5P什么白影啊，那个什么的啊，\n',
            '真是不死心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201415V坦率地承认是幽灵不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201416V#1014F#6P啊～别管我啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201417V我在努力想办法\n',
            '让自己不去在意啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_128D')

    def _loc_10F1(): pass

    label('loc_10F1')

    ChrTalk(
        0x0103,
        (
            '#0030201418V#020F#5P嘉恩是这么说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201419V首先去找关所的队长\n',
            '问问看是谁吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201411V#1015F#6P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201412V#1007F哎～话说回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201413V这么漂亮的地方\n',
            '竟然会有那个出现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030201423V#027F#5P艾丝蒂尔……\n',
            '不能自欺欺人哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201424V什么白影啊那个的\n',
            '就承认是幽灵吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201425V#1014F#6P我听不见，我听不见！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201426V我绝对\n',
            '不承认那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_128D(): pass

    label('loc_128D')

    OP_A2(0x1211)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x1297
@scena.Code('func_08_1297')
def func_08_1297():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12B1',
    )

    Call(0, 0x0009)
    FadeIn(0, 0)

    def _loc_12B1(): pass

    label('loc_12B1')

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_4A(0x0008, 255)
    Fade(1000)
    SetChrPos(0x0101, 16230, 5000, 1730, 90)
    SetChrPos(0x00F7, 16120, 5000, 530, 45)
    OP_6B(2800, 0)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
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
            (Expr.GetChrWork, 0x8, 0x2),
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
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2820201455V哦，想进隧道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201456V稍等一下。\n',
            '我现在就开门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201457V#1016F#6P啊，不是。\n',
            '不是想通过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201458V#1000F我们\n',
            '是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201459V正在调查\n',
            '『白影』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2820201460V那难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201461V但、但是那个\n',
            '不只是我睡着了后做梦而已吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201462V#1002F#6P嗯，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201463V其实，除了你以外\n',
            '在卢安各地都有\n',
            '目击了白影的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1545',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201464V#051F你和这里的队长\n',
            '好像都不知道这事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201465V这可恶的白影可是惹了不少麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A1')

    def _loc_1545(): pass

    label('loc_1545')

    ChrTalk(
        0x0103,
        (
            '#0030201466V#020F你和队长\n',
            '好像都不知道这事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201467V据说白影搞出了不少乱子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A1(): pass

    label('loc_15A1')

    ChrTalk(
        0x0008,
        (
            '#2820201468V是，是这样吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201469V是吗～我放心了。\n',
            '作为梦来说也太真实了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2820201470V……唔。\n',
            '知道不是梦\n',
            '突然害怕起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201471V#1007F#6P……我明白你的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201472V#1008F嗯，这个暂且不管,\n',
            '那时的事情能告诉我们吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201473V尽量详细具体一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201474V啊啊，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201475V……３天前的半夜，\n',
            '我在放哨，和平常一样\n',
            '站在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201476V这里瀑布的声音很大吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201477V但是我习惯了这个节奏\n',
            '反而犯起困来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201478V刚刚吃了饭\n',
            '就换岗了,\n',
            '更加想睡了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201479V因此，为了赶走睡意\n',
            '就在这上面走来走去\n',
            '做步哨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201480V那时……\n',
            '我就看到了那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201481V#1002F#6P是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201482V那个\n',
            '是怎样的那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201483V白色的，轻飘飘的\n',
            '穿着古老的衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201484V还在瀑布正上方\n',
            '滴溜溜地跳着舞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201485V我打起了寒颤\n',
            '忍不住架起枪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201486V#1004F#6P咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201487V幽灵……\n',
            '难道你向它开枪了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201488V啊，啊啊……\n',
            '本想威吓射击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201489V但是好像没打中,\n',
            '还是在那里漂浮着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201490V然后突然飞向北方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201491V#1013F#6P啊…啊……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A71',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201492V#552F哼……\n',
            '搞得像真的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA9')

    def _loc_1A71(): pass

    label('loc_1A71')

    ChrTalk(
        0x0103,
        (
            '#0030201493V#025F哎呀呀……\n',
            '这搞不好真的是幽灵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA9(): pass

    label('loc_1AA9')

    ChrTalk(
        0x0008,
        (
            '#2820201494V然后，慌慌张张跑回里面\n',
            '把队长他们叫起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201495V『放哨时睡大觉是怎么回事！』\n',
            '『而且还乱开枪吗！』\n',
            '这样被狠训了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201496V唉……真是狼狈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201497V#1025F#6P真，真可怜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201498V#1016F不过当成是梦\n',
            '忘掉是最好的了，嗯嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201499V就算这么说\n',
            '也忘不掉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201500V……虽然不知道它\n',
            '为什么要出来晃悠，\n',
            '不过赶快想想办法啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201501V要是游击士，心灵的烦恼\n',
            '也能解决吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201502V#1007F#6P少、少来啦。\n',
            '我们又不是神父。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201503V#1015F不过确实……\n',
            '应该有什么出现的理由吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201504V想办法努力调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2820201505V啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    OP_A2(0x1213)
    OP_28(0x0082, 0x02, 0x0004)
    OP_28(0x0082, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x1D4F
@scena.Code('func_09_1D4F')
def func_09_1D4F():
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
        (0x00000000, 'loc_1DC9'),
        (0x00000001, 'loc_1DCF'),
        (-1, 'loc_1DD5'),
    )

    def _loc_1DC9(): pass

    label('loc_1DC9')

    OP_A2(0x1200)

    Jump('loc_1DD5')

    def _loc_1DCF(): pass

    label('loc_1DCF')

    OP_A2(0x1201)

    Jump('loc_1DD5')

    def _loc_1DD5(): pass

    label('loc_1DD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1DE3',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1DE7')

    def _loc_1DE3(): pass

    label('loc_1DE3')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1DE7(): pass

    label('loc_1DE7')

    Return()

# id: 0x000A offset: 0x1DE8
@scena.Code('func_0A_1DE8')
def func_0A_1DE8():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x1E32
@scena.Code('func_0B_1E32')
def func_0B_1E32():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　卢安市　１７５塞尔矩\n',
            '东　蔡斯市　４４８塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x1E96
@scena.Code('func_0C_1E96')
def func_0C_1E96():
    TalkBegin(0x00FF)
    Sleep(200)

    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x1EA2
@scena.Code('func_0D_1EA2')
def func_0D_1EA2():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1EDA')
    def lambda_1EDA():
        OP_6D(3950, 5000, 6930, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1EDA)

    @scena.Lambda('lambda_1EF2')
    def lambda_1EF2():
        OP_6B(3250, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1EF2)

    @scena.Lambda('lambda_1F02')
    def lambda_1F02():
        OP_6C(60000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_1F02)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2056',
    )

    OP_C0(0x0E, 0x0000001A, 0x00000CE4, 0x00001838, 0x00000D3E, 0x00000000, 0x00000C8A, 0xFFFFFC18, 0x00001A72)
    Fade(500)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    ClearChrFlags(0x0004, 0x0008)
    ClearChrFlags(0x0005, 0x0008)
    ClearChrFlags(0x0006, 0x0008)
    ClearChrFlags(0x0007, 0x0008)
    SetChrChipByIndex(0x0000, 65535)
    ClearChrFlags(0x0000, 0x0002)
    ClearChrFlags(0x0000, 0x0040)
    ClearChrFlags(0x0000, 0x0004)
    SetChrPos(0x0000, 4210, 5000, 2040, 0)
    SetChrPos(0x0001, 4210, 5000, 2040, 0)
    SetChrPos(0x0002, 4210, 5000, 2040, 0)
    SetChrPos(0x0003, 4210, 5000, 2040, 0)
    SetChrPos(0x0004, 4210, 5000, 2040, 0)
    SetChrPos(0x0005, 4210, 5000, 2040, 0)
    SetChrPos(0x0006, 4210, 5000, 2040, 0)
    SetChrPos(0x0007, 4210, 5000, 2040, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_2065')

    def _loc_2056(): pass

    label('loc_2056')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2065',
    )

    EventEnd(0x01)

    def _loc_2065(): pass

    label('loc_2065')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
