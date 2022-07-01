import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2120   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '嘉恩'),
    TXT(0x02, '索姆茨'),
    TXT(0x03, '爱珐'),
    TXT(0x04, '欧尼尔'),
    TXT(0x05, '奈尔'),
    TXT(0x06, '朵洛希'),
    TXT(0x07, '普莱米奥'),
    TXT(0x08, '梅尔茨'),
    TXT(0x09, '目标用照相机'),
    TXT(0x0A, '雪拉扎德'),
    TXT(0x0B, '阿加特'),
    TXT(0x0C, '提妲'),
    TXT(0x0D, '金'),
    TXT(0x0E, '森特'),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2120.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T2120._SN', 'ED6_DT21/T2120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xCCE7
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
        ('ED6_DT07/CH02400._CH', 'ED6_DT07/CH02400P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -5700,
            z                   = 0,
            y                   = 45100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -30000,
            z                   = 0,
            y                   = 4910,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            x                   = 1200,
            z                   = 0,
            y                   = 5000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 29900,
            z                   = 0,
            y                   = 4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -36400,
            z                   = 0,
            y                   = 41430,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
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
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1310,
            y           = 0,
            z           = 38500,
            range       = 1450,
            dword_10    = 0x000007D0,
            dword_14    = 0x00009B46,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
    )

# id: 0x10005 offset: 0x2F2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1070,
            triggerZ            = 0,
            triggerY            = 43260,
            triggerRange        = 1400,
            actorX              = 1070,
            actorZ              = 2000,
            actorY              = 43260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30020,
            triggerZ            = 0,
            triggerY            = 3590,
            triggerRange        = 400,
            actorX              = -30000,
            actorZ              = 1500,
            actorY              = 4910,
            flags               = 0x007E,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1020,
            triggerZ            = 0,
            triggerY            = 3000,
            triggerRange        = 400,
            actorX              = 1200,
            actorZ              = 1500,
            actorY              = 5000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 29980,
            triggerZ            = 0,
            triggerY            = 3310,
            triggerRange        = 400,
            actorX              = 29900,
            actorZ              = 1500,
            actorY              = 4500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4420,
            triggerZ            = 0,
            triggerY            = 45090,
            triggerRange        = 600,
            actorX              = -5700,
            actorZ              = 1500,
            actorY              = 45100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3A6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B0',
    )

    Jump('loc_3CA')

    def _loc_3B0(): pass

    label('loc_3B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3CA',
    )

    ClearChrFlags(0x000F, 0x0080)

    def _loc_3CA(): pass

    label('loc_3CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3EC',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -2790, 0, 41750, 0)

    def _loc_3EC(): pass

    label('loc_3EC')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B5',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_42E',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0004)
    SetChrChipByIndex(0x0011, 8)
    SetChrPos(0x0011, -33790, 250, 46120, 180)

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_45B',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0012, 0x0004)
    SetChrChipByIndex(0x0012, 9)
    SetChrPos(0x0012, -31990, 250, 46120, 180)

    def _loc_45B(): pass

    label('loc_45B')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_488',
    )

    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0013, 0x0004)
    SetChrChipByIndex(0x0013, 10)
    SetChrPos(0x0013, -33850, 250, 43760, 0)

    def _loc_488(): pass

    label('loc_488')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4B5',
    )

    ClearChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0014, 0x0004)
    SetChrChipByIndex(0x0014, 11)
    SetChrPos(0x0014, -31980, 250, 43650, 0)

    def _loc_4B5(): pass

    label('loc_4B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_4CB',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0011)

    Jump('loc_54B')

    def _loc_4CB(): pass

    label('loc_4CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_4E1',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x0012)

    Jump('loc_54B')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_4F7',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 0x0007)

    Jump('loc_54B')

    def _loc_4F7(): pass

    label('loc_4F7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_503'),
        (-1, 'loc_54B'),
    )

    def _loc_503(): pass

    label('loc_503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_51B',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0013)

    Jump('loc_548')

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 3, 0x1213)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_537',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000C)

    Jump('loc_548')

    def _loc_537(): pass

    label('loc_537')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_548',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    def _loc_548(): pass

    label('loc_548')

    Jump('loc_54B')

    def _loc_54B(): pass

    label('loc_54B')

    Return()

# id: 0x0001 offset: 0x54C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 1, 0x1241)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_565',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_565(): pass

    label('loc_565')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57B',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)

    def _loc_57B(): pass

    label('loc_57B')

    Return()

# id: 0x0002 offset: 0x57C
@scena.Code('ReInit')
def ReInit():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x581
@scena.Code('func_03_581')
def func_03_581():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_B23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 5, 0x20B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B20',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360092V#650F呀，辛苦了。\n',
            '学院刚刚发生的事真是不得了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360093V不过，不愧是你们啊，\n',
            '顺利解决了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360094V#1001F嘿嘿，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360095V这也多亏嘉恩哥哥\n',
            '联络及时啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360099V#1040F嗯嗯，也多亏卡露娜他们\n',
            '的突袭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500360096V#650F哈哈，这是我的工作嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360097V不管怎样，没有出大事\n',
            '就算放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360098V#655F但是这个导力停止现象\n',
            '还没有完全解决，\n',
            '所以还不能完全放下心来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360100V#072F而且，结社的人\n',
            '也不知道还会做出什么事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080360101V此后行事\n',
            '也不能松懈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89C')

    def _loc_7B1(): pass

    label('loc_7B1')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_825',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360102V#022F而且，结社的人\n',
            '也不知道还会做出什么事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360103V此后也要\n',
            '谨慎行事为妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89C')

    def _loc_825(): pass

    label('loc_825')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360104V#050F而且，结社的人\n',
            '也不知道还会做出什么事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360105V嗯，此后也要\n',
            '谨慎行事才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89C(): pass

    label('loc_89C')

    ChrTalk(
        0x0101,
        (
            '#0010360106V#1002F确实如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Return,
        ),
        'loc_8D0',
    )

    OP_A2(0x0008)

    Jump('loc_8D3')

    def _loc_8D0(): pass

    label('loc_8D0')

    OP_A3(0x0008)

    def _loc_8D3(): pass

    label('loc_8D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98D',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇地方任务未报告（QF_REPORT不成立）】\n'),
            TXT(0x01, '【◇在其他支部报告完毕（QF_REPORT成立）】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_981'),
        (0x00000001, 'loc_987'),
        (-1, 'loc_98D'),
    )

    def _loc_981(): pass

    label('loc_981')

    OP_A3(0x0008)

    Jump('loc_98D')

    def _loc_987(): pass

    label('loc_987')

    OP_A2(0x0008)

    Jump('loc_98D')

    def _loc_98D(): pass

    label('loc_98D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A99',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360107V#652F嗯，此后也要小心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360108V#650F啊，对了对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360109V学院事件的事，\n',
            '核定已经完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360110V想领取报酬的时候\n',
            '要重新报告一下哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360111V#1000F啊，嗯。\n',
            '谢谢嘉恩哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360112V#1040F那么，先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B19')

    def _loc_A99(): pass

    label('loc_A99')

    ChrTalk(
        0x0008,
        (
            '#0500360113V#652F嗯，此后也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360111V#1000F啊，嗯。\n',
            '谢谢嘉恩哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360112V#1040F那么，先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B19(): pass

    label('loc_B19')

    OP_A2(0x20B5)
    TalkEnd(0x0008)

    Return()

    def _loc_B20(): pass

    label('loc_B20')

    Jump('loc_BB0')

    def _loc_B23(): pass

    label('loc_B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BB0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 4, 0x20B4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BB0',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360116V#650F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360117V想找其他支部的\n',
            '伙伴时就跟我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360118V我会跟他们联络\n',
            '让他们过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20B4)

    def _loc_BB0(): pass

    label('loc_BB0')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C14',
    )

    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '呼叫同伴\n'),
            TXT(0x03, '离开\n'),
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
    FadeIn(300, 0)

    Jump('loc_C18')

    def _loc_C14(): pass

    label('loc_C14')

    Call(6, 0x0005)

    def _loc_C18(): pass

    label('loc_C18')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D7E',
    )

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CAA',
    )

    OP_28(0x00C3, 0x04, 0x20)
    OP_A9(0x67)

    ChrTalk(
        0x0008,
        (
            '#0500360119V#650F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360120V完成了什么任务的话\n',
            '再来报告哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D78')

    def _loc_CAA(): pass

    label('loc_CAA')

    If(
        (
            (Expr.Eval, "OP_A9(0x67)"),
            Expr.Return,
        ),
        'loc_D17',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360121V#650F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360122V完成了什么任务的话\n',
            '再来报告哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D78')

    def _loc_D17(): pass

    label('loc_D17')

    ChrTalk(
        0x0008,
        (
            '#0500360123V#650F现在好像\n',
            '没有可以报告的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360124V完成了什么任务的话\n',
            '再来报告哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D78(): pass

    label('loc_D78')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_D7E(): pass

    label('loc_D7E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E49',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E45',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360125V#650F要找同伴过来吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360126V明白了，那么\n',
            '我马上联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '联络各支部，\n',
            '集合了待命人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()

    def _loc_E45(): pass

    label('loc_E45')

    TalkEnd(0x0008)

    Return()

    def _loc_E49(): pass

    label('loc_E49')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E5A',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_E5A(): pass

    label('loc_E5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_EE4',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360127V#650F学院刚刚发生的事真是不得了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360128V此后结社的人\n',
            '可能还会谋划什么事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360129V请多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1666')

    def _loc_EE4(): pass

    label('loc_EE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1142',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 2, 0x2002)),
            Expr.Return,
        ),
        'loc_1031',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FAD',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360130V#650F王都支部来了联络，\n',
            '但似乎不是马上要你们去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360131V要是以后路过王都附近的话，\n',
            '顺便过去一趟就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360132V嗯，到时候\n',
            '去艾南那里\n',
            '一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_102E')

    def _loc_FAD(): pass

    label('loc_FAD')

    ChrTalk(
        0x0008,
        (
            '#0500360130V#650F王都支部来了联络，\n',
            '但似乎不是马上要你们去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360134V要是以后路过王都附近的话，\n',
            '顺便过去一趟就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_102E(): pass

    label('loc_102E')

    Jump('loc_113F')

    def _loc_1031(): pass

    label('loc_1031')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10D8',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360087V#650F对了，检查一下\n',
            '公告板上的工作好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360136V还有，如果能去确认一下\n',
            '近郊居民的情况就再好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360137V那么，就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_113F')

    def _loc_10D8(): pass

    label('loc_10D8')

    ChrTalk(
        0x0008,
        (
            '#0500360138V#650F就麻烦你们检查一下\n',
            '公告板还有去近郊巡视吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360139V现在要做的\n',
            '也就这些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_113F(): pass

    label('loc_113F')

    Jump('loc_1666')

    def _loc_1142(): pass

    label('loc_1142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1298',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_11DE',
    )

    ChrTalk(
        0x0008,
        (
            '#0500220079V#650F到了蔡斯\n',
            '先拜访一下拉赛尔博士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500220080V有关新『福音』的事\n',
            '最好借助博士的智慧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500220081V那么，多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1295')

    def _loc_11DE(): pass

    label('loc_11DE')

    OP_A2(0x0002)

    ChrTalk(
        0x0008,
        (
            '#0500220079V#650F到了蔡斯\n',
            '先拜访一下拉赛尔博士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500220080V有关新『福音』的事\n',
            '最好借助博士的智慧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500220084V这边就由梅尔茨\n',
            '暂时撑着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500220081V那么，多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1295(): pass

    label('loc_1295')

    Jump('loc_1666')

    def _loc_1298(): pass

    label('loc_1298')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_134A',
    )

    ChrTalk(
        0x0008,
        (
            '#0500200923V#650F要去王立学院就从城北门出去，\n',
            '梅威海道向东拐后一直走就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200924V记得学院祭的时候\n',
            '去帮过忙吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200925V那么，调查\n',
            '就麻烦你们处理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1666')

    def _loc_134A(): pass

    label('loc_134A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_13BD',
    )

    ChrTalk(
        0x0008,
        (
            '#0500200921V#652F不好意思，\n',
            '桥上的骚动就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200922V支持者之间要是打起来，\n',
            '可就不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1666')

    def _loc_13BD(): pass

    label('loc_13BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1536',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1435',
    )

    ChrTalk(
        0x0008,
        (
            '#0500200908V#650F３处情报都确认后\n',
            '就到这里来报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200909V然后再研究\n',
            '收集的情报看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1533')

    def _loc_1435(): pass

    label('loc_1435')

    OP_A2(0x0002)

    ChrTalk(
        0x0008,
        (
            '#0500200910V#650F呀，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200911V目击情报的\n',
            '确认结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200912V#1000F没，正在进行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200908V#650F３处情报都确认后\n',
            '就到这里来报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200909V然后再研究\n',
            '收集的情报看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200915V#1006FＯＫ，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1533(): pass

    label('loc_1533')

    Jump('loc_1666')

    def _loc_1536(): pass

    label('loc_1536')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1666',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_15C6',
    )

    ChrTalk(
        0x0008,
        (
            '#0500200916V#650F首先去确认３处目击情报，\n',
            '然后总结起来再过来报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200917V不是很紧急的工作，\n',
            '稍微推迟点也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1666')

    def _loc_15C6(): pass

    label('loc_15C6')

    OP_A2(0x0002)

    ChrTalk(
        0x0008,
        (
            '#0500200916V#650F首先去确认３处目击情报，\n',
            '然后总结起来再过来报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200919V不是很紧急的工作，\n',
            '稍微推迟点也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200920V那么，就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1666(): pass

    label('loc_1666')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x166A
@scena.Code('func_04_166A')
def func_04_166A():
    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '诺曼的支持者和\n',
            '波尔多斯的支持者\n',
            '在大桥争吵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这样下去会打起来的。\n',
            '快想办法调停吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0005 offset: 0x16D0
@scena.Code('func_05_16D0')
def func_05_16D0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1904',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1801',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1768',
    )

    ChrTalk(
        0x00FE,
        (
            '之前因为工作去了仓库区，\n',
            '结果被问了好多奇怪的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '准游击士必要的资格啦、\n',
            '招募的方法啦等等的问了好多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FE')

    def _loc_1768(): pass

    label('loc_1768')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '之前因为工作去了仓库区，\n',
            '碰到个问个不停的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '准游击士必要的资格啦、\n',
            '招募的方法啦等等的问了好多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话，这些事\n',
            '去问嘉恩不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17FE(): pass

    label('loc_17FE')

    Jump('loc_1901')

    def _loc_1801(): pass

    label('loc_1801')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1871',
    )

    ChrTalk(
        0x00FE,
        (
            '之前都是靠体力和毅力\n',
            '撑过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来游击士还是\n',
            '需要才智和教养的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是吸取教训了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1901')

    def _loc_1871(): pass

    label('loc_1871')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '之前代替卡露娜小姐\n',
            '当过主日学校的讲师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是完全不行啊！\n',
            '必须从协会规章开始从头学起！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连修女也看不下去了，\n',
            '实在是太丢人了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1901(): pass

    label('loc_1901')

    Jump('loc_1A4C')

    def _loc_1904(): pass

    label('loc_1904')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1A4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1953',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔！\n',
            '恭喜你晋升！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要努力不输给你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A4C')

    def _loc_1953(): pass

    label('loc_1953')

    OP_A2(0x0003)
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久不见了！\n',
            '我是支部所属的梅尔茨准游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恭喜你晋升！\n',
            '我也会加油的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡露娜前辈也不在，\n',
            '说实话真是很辛苦很辛苦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1A24',
    )

    ChrTurnDirection(0x00FE, 0x0106, 0)

    ChrTalk(
        0x00FE,
        (
            '阿加特前辈\n',
            '也请多多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A4C')

    def _loc_1A24(): pass

    label('loc_1A24')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德前辈\n',
            '也请多多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A4C(): pass

    label('loc_1A4C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1A50
@scena.Code('func_06_1A50')
def func_06_1A50():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x05,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0011)
    ClearChrFlags(0x0011, 0x0010)
    ChrTurnDirection(0x0011, 0x0000, 0)

    ExecExpressionWithValue(
        0x0011,
        0x04,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x04,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x11, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x05,
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x11, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1AE0',
    )

    Jump('loc_1B22')

    def _loc_1AE0(): pass

    label('loc_1AE0')

    If(
        (
            (Expr.GetChrWork, 0x11, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1AFC',
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B22')

    def _loc_1AFC(): pass

    label('loc_1AFC')

    If(
        (
            (Expr.GetChrWork, 0x11, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1B18',
    )

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B22')

    def _loc_1B18(): pass

    label('loc_1B18')

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.GetChrWork, 0x11, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B22(): pass

    label('loc_1B22')

    ExecExpressionWithValue(
        0x0011,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0011, 0x0010)

    ChrTalk(
        0x0011,
        (
            '#0030360140V#020F哎呀，有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1BC7'),
        (-1, 'loc_1C00'),
    )

    def _loc_1BC7(): pass

    label('loc_1BC7')

    ChrTalk(
        0x0011,
        (
            '#0030360141V#020F嗯～是吗～？\n',
            '要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000A)

    Jump('loc_1C67')

    def _loc_1C00(): pass

    label('loc_1C00')

    ChrTalk(
        0x0011,
        (
            '#0030360142V#026F难得来卢安\n',
            '待在这里也没意思呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360143V#027F偷偷去娱乐场\n',
            '看看如何呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C67')

    def _loc_1C67(): pass

    label('loc_1C67')

    SetChrSubChip(0x0011, 0)
    TalkEnd(0x0011)

    Return()

# id: 0x0007 offset: 0x1C70
@scena.Code('func_07_1C70')
def func_07_1C70():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x12, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x05,
        (
            (Expr.GetChrWork, 0x12, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0012)
    ClearChrFlags(0x0012, 0x0010)
    ChrTurnDirection(0x0012, 0x0000, 0)

    ExecExpressionWithValue(
        0x0012,
        0x04,
        (
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x04,
        (
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x12, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x05,
        (
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x12, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D00',
    )

    Jump('loc_1D42')

    def _loc_1D00(): pass

    label('loc_1D00')

    If(
        (
            (Expr.GetChrWork, 0x12, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1D1C',
    )

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D42')

    def _loc_1D1C(): pass

    label('loc_1D1C')

    If(
        (
            (Expr.GetChrWork, 0x12, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1D38',
    )

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D42')

    def _loc_1D38(): pass

    label('loc_1D38')

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.GetChrWork, 0x12, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1D42(): pass

    label('loc_1D42')

    ExecExpressionWithValue(
        0x0012,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0012, 0x0010)

    ChrTalk(
        0x0012,
        (
            '#0050360144V#050F哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1DE3'),
        (-1, 'loc_1E0F'),
    )

    def _loc_1DE3(): pass

    label('loc_1DE3')

    ChrTalk(
        0x0012,
        (
            '#0050360145V#052F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000A)

    Jump('loc_1E69')

    def _loc_1E0F(): pass

    label('loc_1E0F')

    ChrTalk(
        0x0012,
        (
            '#0050360146V#050F是吗……\n',
            '算了，随你高兴吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360147V我就在这里\n',
            '休息休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E69')

    def _loc_1E69(): pass

    label('loc_1E69')

    SetChrSubChip(0x0012, 0)
    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x1E72
@scena.Code('func_08_1E72')
def func_08_1E72():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x13, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x05,
        (
            (Expr.GetChrWork, 0x13, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0013)
    ClearChrFlags(0x0013, 0x0010)
    ChrTurnDirection(0x0013, 0x0000, 0)

    ExecExpressionWithValue(
        0x0013,
        0x04,
        (
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x04,
        (
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x13, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x05,
        (
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x13, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1F02',
    )

    Jump('loc_1F44')

    def _loc_1F02(): pass

    label('loc_1F02')

    If(
        (
            (Expr.GetChrWork, 0x13, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F1E',
    )

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F44')

    def _loc_1F1E(): pass

    label('loc_1F1E')

    If(
        (
            (Expr.GetChrWork, 0x13, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1F3A',
    )

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F44')

    def _loc_1F3A(): pass

    label('loc_1F3A')

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.GetChrWork, 0x13, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F44(): pass

    label('loc_1F44')

    ExecExpressionWithValue(
        0x0013,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0013, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FBF',
    )

    ChrTalk(
        0x0013,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2041')

    def _loc_1FBF(): pass

    label('loc_1FBF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1FFA',
    )

    ChrTalk(
        0x0013,
        (
            '#0070370814V#060F啊，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2041')

    def _loc_1FFA(): pass

    label('loc_1FFA')

    ChrTalk(
        0x0013,
        (
            '#0070271311V#060F啊，姐姐是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2041(): pass

    label('loc_2041')

    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_209A'),
        (-1, 'loc_2121'),
    )

    def _loc_209A(): pass

    label('loc_209A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_20E8',
    )

    ChrTalk(
        0x0013,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_211A')

    def _loc_20E8(): pass

    label('loc_20E8')

    ChrTalk(
        0x0013,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_211A(): pass

    label('loc_211A')

    Call(0, 0x000A)

    Jump('loc_21FE')

    def _loc_2121(): pass

    label('loc_2121')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_219A',
    )

    ChrTalk(
        0x0013,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271320V#060F我就在这里等，\n',
            '有什么事就来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21FB')

    def _loc_219A(): pass

    label('loc_219A')

    ChrTalk(
        0x0013,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271322V#060F我会在这里等的，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21FB(): pass

    label('loc_21FB')

    Jump('loc_21FE')

    def _loc_21FE(): pass

    label('loc_21FE')

    SetChrSubChip(0x0013, 0)
    TalkEnd(0x0013)

    Return()

# id: 0x0009 offset: 0x2207
@scena.Code('func_09_2207')
def func_09_2207():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x14, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x05,
        (
            (Expr.GetChrWork, 0x14, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0014)
    ClearChrFlags(0x0014, 0x0010)
    ChrTurnDirection(0x0014, 0x0000, 0)

    ExecExpressionWithValue(
        0x0014,
        0x04,
        (
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x04,
        (
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x14, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x05,
        (
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x14, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2297',
    )

    Jump('loc_22D9')

    def _loc_2297(): pass

    label('loc_2297')

    If(
        (
            (Expr.GetChrWork, 0x14, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_22B3',
    )

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22D9')

    def _loc_22B3(): pass

    label('loc_22B3')

    If(
        (
            (Expr.GetChrWork, 0x14, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_22CF',
    )

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22D9')

    def _loc_22CF(): pass

    label('loc_22CF')

    ExecExpressionWithValue(
        0x0014,
        0x08,
        (
            (Expr.GetChrWork, 0x14, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_22D9(): pass

    label('loc_22D9')

    ExecExpressionWithValue(
        0x0014,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0014, 0x0010)

    ChrTalk(
        0x0014,
        (
            '#0080370823V#070F噢，有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_237A'),
        (-1, 'loc_23A6'),
    )

    def _loc_237A(): pass

    label('loc_237A')

    ChrTalk(
        0x0014,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000A)

    Jump('loc_2403')

    def _loc_23A6(): pass

    label('loc_23A6')

    ChrTalk(
        0x0014,
        (
            '#0080370825V#070F怎么，不调整了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370826V唔，还想着能去\n',
            '参观卢安呢，可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2403')

    def _loc_2403(): pass

    label('loc_2403')

    SetChrSubChip(0x0014, 0)
    TalkEnd(0x0014)

    Return()

# id: 0x000A offset: 0x240C
@scena.Code('func_0A_240C')
def func_0A_240C():
    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    OP_A3(0x0007)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_24A9',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0004)
    SetChrChipByIndex(0x0011, 8)
    SetChrPos(0x0011, -33790, 250, 46120, 180)

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_248E',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_248E(): pass

    label('loc_248E')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24A9',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_24A9(): pass

    label('loc_24A9')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_250C',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0012, 0x0004)
    SetChrChipByIndex(0x0012, 9)
    SetChrPos(0x0012, -31990, 250, 46120, 180)

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24F1',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_24F1(): pass

    label('loc_24F1')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_250C',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_250C(): pass

    label('loc_250C')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_256F',
    )

    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0013, 0x0004)
    SetChrChipByIndex(0x0013, 10)
    SetChrPos(0x0013, -33850, 250, 43760, 0)

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2554',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_2554(): pass

    label('loc_2554')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_256F',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_256F(): pass

    label('loc_256F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_25D2',
    )

    ClearChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0014, 0x0004)
    SetChrChipByIndex(0x0014, 11)
    SetChrPos(0x0014, -31980, 250, 43650, 0)

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25B7',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_25B7(): pass

    label('loc_25B7')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25D2',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0007)

    def _loc_25D2(): pass

    label('loc_25D2')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_264F',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※要待命的成员\n',
            '　装备着『零力场发生器』。\n',
            '　将其回收加入队伍的携带品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_264F(): pass

    label('loc_264F')

    Return()

# id: 0x000B offset: 0x2650
@scena.Code('func_0B_2650')
def func_0B_2650():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2661',
    )

    Call(0, 0x001D)

    def _loc_2661(): pass

    label('loc_2661')

    FadeOut(0, 0, -1)
    EventBegin(0x00)
    SetChrPos(0x0101, -3540, 0, 45230, 0)
    SetChrPos(0x00F7, -3540, 0, 43990, 0)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x00F7, 0x0008, 400)
    OP_4A(0x0008, 255)
    OP_6D(-650, 0, 40270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_26E4')
    def lambda_26E4():
        OP_6D(-4590, 0, 45190, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_26E4)

    @scena.Lambda('lambda_26FC')
    def lambda_26FC():
        OP_67(0, 7240, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_26FC)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3D05',
    )

    ChrTalk(
        0x0008,
        (
            '#0500200724V#650F#5P呀～！\n',
            '你们来的正是时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200725V因为卡露娜不在，\n',
            '公告板的工作都堆积着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200726V#651F马上精神抖擞、活力充沛地\n',
            '去工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200727V#1016F#4P啊，啊哈哈……\n',
            '还是这么有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200728V#053F公告板的工作\n',
            '是打算慢慢整理完成的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200729V#050F有没有其它紧急的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200730V#650F#5P这个，虽然工作都堆积着，\n',
            '但没有什么紧急的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200731V市长选举的管理是在军队的管辖之内……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200732V城市也正忙于市长选举，\n',
            '游客也不多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200733V#1015F#4P哎呀～原来市长选举\n',
            '那么热闹啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200734V有谁出来参选啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200735V#650F#5P推进旅游业的诺曼和\n',
            '呼吁维持港湾业的波尔多斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200736V虽说只是卢安市长，\n',
            '但其权限可是波及到全卢安地区的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200737V所以玛诺利亚村的居民也会投票，\n',
            '宣传媒体也相当关注。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200738V#651F这必然会成为左右\n',
            '卢安地区未来的重要选举啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200739V#1006F#4P啊～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200740V我还未成年，不是居住民，\n',
            '所以没有选举权……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200741V不过作为那个事件的相关人士，\n',
            '还是挺在意其发展动向呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200742V#651F#5P这方面\n',
            '利贝尔通讯有出特刊，\n',
            '推荐看看哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200743V#653F啊……这么说来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200744V#652F的确有一件事\n',
            '想让你们调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200745V#1004F#4P想调查的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200746V#654F#5P嗯～怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200747V要怎么说明才好呢～？\n',
            '实在是很困难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200748V#555F怎么？\n',
            '真是不干脆啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200749V就像平时一样厚着脸皮\n',
            '一口气全说出来不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200750V#651F#5P啊哈哈，好过分的话哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200751V#652F那我就说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200752V希望你们调查一下『亡灵』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x0106)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0500200753V#654F#5P唉，我就知道\n',
            '你们会摆出那种表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200754V所以才不想说的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200755V#1016F#4P……啊，不，嗯。\n',
            '只是一下没明白过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200756V#1011F到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200757V#652F嗯……\n',
            '最近１～２周呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200758V协会收到了好几起\n',
            '关于『夜晚看见了白影』的报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200759V而且是从卢安各地发来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200760V#1015F#4P夜晚看见了白影……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010200761V#1020F#3S#4P然然然，然后呢！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200762V#053F原来如此，然后就说是『亡灵』吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200763V#050F要说是错觉，\n',
            '但各地都出现就比较奇怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200764V#652F#5P嗯，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200765V完成公告板上的工作以外附带\n',
            '打听一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200766V#1008F#4P啊，但是，那个，是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200767V#1013F也不是那么容易的事，\n',
            '就让我们考虑考虑吧，嗯～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 0)
    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0106)
    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0500200768V#653F#5P艾丝蒂尔、难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 600)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0008, 600)
    Sleep(400)

    ChrTurnDirection(0x0101, 0x0106, 600)

    ChrTalk(
        0x0101,
        (
            '#0010200769V#1008F#2P咦，讨厌，不是啦！？　\n',
            '完全没有那种事哦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200770V小孩子看到我都会吓得不敢哭，这样的艾丝蒂尔\n',
            '竟然会怕幽灵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 500)

    ChrTalk(
        0x0101,
        (
            '#0010200771V#1007F#4P……对不起。\n',
            '是有点害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200772V#651F#5P啊哈哈。\n',
            '好像不是有点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200773V#650F不过，也没有造成什么实际伤害，\n',
            '这事就当没提过吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200774V#053F不……我们接受了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200775V#057F……别忘了。\n',
            '我们的任务是调查『结社』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200776V就算稍微有些奇怪的征兆，\n',
            '也该调查验证是否与『结社』有关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200777V我说的没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200778V#1026F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200779V#053F人都有弱点的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200780V偶尔示弱一下也没什么不好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200781V#057F但是，可别什么都不做\n',
            '就夹着尾巴逃跑哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200782V#1003F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200783V#654F#5P哎呀哎呀。\n',
            '是不是太严格了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200784V#1010F#2P……不。\n',
            '阿加特说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200785V#1002F我确实怕幽灵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200786V但是和约修亚消失比起来\n',
            '就一点也不可怕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0500200787V#653F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200788V#051F嗯，这不是挺明白的吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200789V#1006F#4P嘉恩哥哥，这个调查，\n',
            '能交给我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200790V#651F#5P你这么说就求之不得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200791V#652F已经收集了一些证言，\n',
            '不过出现了３个新的目击者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200792V首先是在艾尔·雷登的\n',
            '关所工作的一名士兵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200793V据说在夜巡时看到了幽灵，\n',
            '当场吓得腰都直不起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200794V#1007F#4P呜哎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200795V#655F#5P第二个好像是渡鸦帮的\n',
            '成员之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200796V#650F这个有阿加特在\n',
            '就很容易打听了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200797V#051F嗯，要是敢拒绝\n',
            '就用武力撬开他的嘴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200798V#1007F#2P这就免了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200799V#1025F武术大会时对战过，\n',
            '好像很有洗心革面的样子哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200800V#552F哼……谁知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200801V#654F#5P好了好了，就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0500200802V#650F#5P而最后的目击者……\n',
            '是玛西亚孤儿院的孩子们。',
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
            '#0010200803V#1004F#4P咦……\n',
            '孤儿院的孩子们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200804V#650F#5P啊啊，特蕾莎院长\n',
            '代替他们联络我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200805V顺带一提玛西亚孤儿院\n',
            '前几天刚刚重建好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200806V出于特蕾莎院长的希望，\n',
            '据说大体和以前样式相同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200807V#1017F#4P是吗……太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200808V正打算去和院长老师还有孩子们\n',
            '打个招呼呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200809V顺便表示祝贺\n',
            '就去问问看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200810V#651F#5P拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200811V#650F不过我刚才说了，这个调查并不紧急，\n',
            '推迟点也完全没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200812V公告板上还有其他工作，\n',
            '就先检查一下那边好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3AD4')
    def lambda_3AD4():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3AD4)

    @scena.Lambda('lambda_3AE2')
    def lambda_3AE2():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3AE2)

    OP_6D(-720, 0, 45530, 1500)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※能够自由接受的工作记载在公告板上。\n',
            '　接近公告板会有！记号出现，\n',
            '　右击显示工作列表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※单击列表显示的各工作名，\n',
            '　能确认工作的详细内容。\n',
            '　确认了的内容会自动登记在手册上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    @scena.Lambda('lambda_3BD0')
    def lambda_3BD0():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3BD0)

    @scena.Lambda('lambda_3BDE')
    def lambda_3BDE():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3BDE)

    OP_6D(-4590, 0, 45190, 1500)

    ChrTalk(
        0x0008,
        (
            '#0500200813V#650F#5P确认了３件目击情报就\n',
            '再返回这里总结报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200814V一起研究一下搜集的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200815V#1006F#4P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200816V不过，渡鸦帮在仓库区，\n',
            '先去那里看看可能比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200817V#051F那么在出城之前\n',
            '就先去港口仓库看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5252')

    def _loc_3D05(): pass

    label('loc_3D05')

    ChrTalk(
        0x0008,
        (
            '#0500200724V#650F#5P呀～！\n',
            '你们来的正是时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200725V因为卡露娜不在，\n',
            '公告板的工作都堆积着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200726V#651F马上精神抖擞、活力充沛地\n',
            '去工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200727V#1016F#4P啊，啊哈哈……\n',
            '还是这么有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200822V#021F呵呵，心情可以理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200823V#020F那么请赶快介绍紧急的工作\n',
            '给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200730V#650F#5P这个，虽然工作都堆积着，\n',
            '但没有什么紧急的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200731V市长选举的管理是在军队的管辖之内……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200732V城市也正忙于市长选举，\n',
            '游客也不多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200733V#1015F#4P哎呀～原来市长选举\n',
            '那么热闹啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200734V有谁出来参选啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200735V#650F#5P推进旅游业的诺曼和\n',
            '呼吁维持港湾业的波尔多斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200736V虽说只是卢安市长，\n',
            '但其权限可是波及到全卢安地区的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200737V所以玛诺利亚村的居民也会投票，\n',
            '宣传媒体也相当关注。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200738V#651F这必然会成为左右\n',
            '卢安地区未来的重要选举啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200739V#1006F#4P啊～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200740V我还未成年，不是居住民，\n',
            '所以没有选举权……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200741V不过作为那个事件的相关人士，\n',
            '还是挺在意其发展动向呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200742V#651F#5P这方面\n',
            '利贝尔通讯有出特刊，\n',
            '推荐看看哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200743V#653F啊……这么说来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200744V#652F的确有一件事\n',
            '想让你们调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200745V#1004F#4P想调查的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200840V#655F#5P嗯～怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200747V要怎么说明才好呢～？\n',
            '实在是很困难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200842V#027F哎呀，真稀奇。\n',
            '嘉恩居然会犹豫啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200843V平时不总是一下子就\n',
            '给我们派一堆工作的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200844V#654F#5P雪拉，别这么说嘛～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200751V#652F那我就说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200752V希望你们调查一下『亡灵』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x0103)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0500200753V#654F#5P唉，我就知道\n',
            '你们会摆出那种表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200754V所以才不想说的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200755V#1016F#4P……啊，不，嗯。\n',
            '只是一下没明白过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200756V#1011F到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200757V#652F#5P嗯……\n',
            '最近１～２周呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200758V协会收到了好几起\n',
            '关于『夜晚看见了白影』的报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200759V而且是从卢安各地发来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200760V#1015F#4P夜晚看见了白影……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010200761V#1020F#3S#4P然然然，然后呢！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200856V#026F原来如此，所以才说是『亡灵』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200857V#020F如果说是恶作剧的话，\n',
            '但各地都出现就不符合逻辑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200764V#652F#5P嗯，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200765V完成公告板上的工作以外附带\n',
            '打听一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200766V#1008F#4P啊，但是，那个，是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200767V#1013F也不是那么容易的事，\n',
            '就让我们考虑考虑吧，嗯～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0103)
    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0500200768V#653F#5P艾丝蒂尔，难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 600)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0008, 600)
    Sleep(400)

    ChrTurnDirection(0x0101, 0x0103, 600)

    ChrTalk(
        0x0101,
        (
            '#0010200769V#1008F#2P咦，讨厌，不是啦！？　\n',
            '完全没有那种事哦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200770V小孩子看到我都会吓得不敢哭，这样的艾丝蒂尔\n',
            '竟然会怕幽灵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200771V#1007F#4P……对不起。\n',
            '是有点害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200772V#651F#5P啊哈哈。\n',
            '好像不是有点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200773V#650F不过，也没有造成什么实际伤害，\n',
            '这事就当没提过吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200868V#026F等等，嘉恩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200869V#020F艾丝蒂尔……\n',
            '这件事，就接受下来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200870V#021F没问题，没问题。\n',
            '有姐姐在嘛㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200871V#020F而且，调查这种事\n',
            '对我们的任务也很有价值哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200872V#1026F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200873V#026F巡回利贝尔各地\n',
            '调查『结社』的动向……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200874V这正是要我们找出\n',
            '不可见威胁的根源所在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200875V#027F这和『亡灵』\n',
            '不是很像吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200876V#1004F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200877V#1011F是吗……\n',
            '这么一说确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200878V#1007F对不起，雪拉姐。\n',
            '说了些这么孩子气的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200789V#1006F#4P嘉恩哥哥，这个调查\n',
            '能交给我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200790V#651F#5P你这么说就求之不得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200881V#652F已经收集了一些证言，\n',
            '不过出现了３个新的目击者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200882V首先是在艾尔·雷登\n',
            '关所工作的一名士兵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200793V据说在夜巡时看到了幽灵，\n',
            '当场吓得腰都直不起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200794V#1007F#4P呼哎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200885V#655F#5P第二个好像是渡鸦帮的\n',
            '成员之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200886V#022F渡鸦帮……\n',
            '是卢安的不良少年集团吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200887V#522F嗯，希望能老老实实\n',
            '配合调查就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200888V#1025F#2P嗯～我想没问题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200889V武术大会的时候对战过，\n',
            '好像很有洗心革面的样子哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200890V#023F哎呀。\n',
            '有这样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200891V#651F#5P嗯，他们的确有些自己的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0500200802V#650F#5P而最后的目击者……\n',
            '是玛西亚孤儿院的孩子们。',
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
            '#0010200803V#1004F#4P咦……\n',
            '孤儿院的孩子们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200804V#650F#5P啊啊，特蕾莎院长\n',
            '代替他们联络我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200805V顺带一提玛西亚孤儿院\n',
            '前几天刚刚重建好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200806V出于特蕾莎院长的希望，\n',
            '据说大体和以前样式相同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200807V#1017F#4P是吗……太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200808V正打算去和院长老师还有孩子们\n',
            '打个招呼呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200809V顺便表示祝贺\n',
            '就去问问看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500200810V#651F#5P拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200811V#650F不过我刚才说了，这个调查并不紧急，\n',
            '所以推迟点也完全没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200812V公告板上还有其他工作，\n',
            '就先检查一下那边好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5024')
    def lambda_5024():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5024)

    @scena.Lambda('lambda_5032')
    def lambda_5032():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5032)

    OP_6D(-720, 0, 45530, 1500)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※能够自由接受的工作记载在公告板上。\n',
            '　接近公告板会有！记号出现，\n',
            '　右击显示工作列表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※单击列表显示的各工作名，\n',
            '　能确认工作的详细内容。\n',
            '　确认了的内容会自动登记在手册上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    @scena.Lambda('lambda_5120')
    def lambda_5120():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5120)

    @scena.Lambda('lambda_512E')
    def lambda_512E():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_512E)

    OP_6D(-4590, 0, 45190, 1500)

    ChrTalk(
        0x0008,
        (
            '#0500200813V#650F#5P确认了３件目击情报之后\n',
            '再返回这里总结报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500200814V一起研究一下搜集的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200815V#1006F#4P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200816V不过，渡鸦帮在仓库区，\n',
            '先去那里看看可能比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200907V#020F那么，出城之前\n',
            '先去港口仓库看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5252(): pass

    label('loc_5252')

    OP_A2(0x1206)
    OP_28(0x0081, 0x01, 0x0080)
    OP_28(0x0081, 0x04, 0x10)
    OP_28(0x0081, 0x04, 0x20)
    OP_28(0x0082, 0x04, 0x02)
    OP_28(0x0082, 0x04, 0x08)
    OP_28(0x0082, 0x01, 0x0001)
    OP_28(0x0082, 0x01, 0x0002)
    OP_28(0x0082, 0x01, 0x0010)
    OP_28(0x0082, 0x01, 0x0080)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x528E
@scena.Code('func_0C_528E')
def func_0C_528E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_529F',
    )

    Call(0, 0x001D)

    def _loc_529F(): pass

    label('loc_529F')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0101, 180, -500, 37430, 45)
    SetChrPos(0x00F7, 180, -500, 37430, 45)
    SetChrPos(0x000C, -3540, 0, 45230, 275)
    SetChrPos(0x000D, -2540, 0, 46000, 275)
    SetChrPos(0x000E, 530, 0, 38440, 0)
    OP_4A(0x000E, 255)
    OP_4A(0x0008, 255)
    OP_6D(-520, 0, 40270, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x00F7, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_5375')
    def lambda_5375():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5375)

    @scena.Lambda('lambda_5387')
    def lambda_5387():
        OP_8E(0x00FE, -620, 0, 39710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5387)

    Sleep(500)

    @scena.Lambda('lambda_53A7')
    def lambda_53A7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_53A7)

    @scena.Lambda('lambda_53B9')
    def lambda_53B9():
        OP_8E(0x00FE, 550, 0, 39220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_53B9)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x00F7, 0x0000)
    ChrTurnDirection(0x0101, 0x000C, 400)
    ChrTurnDirection(0x00F7, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210433V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5434')
    def lambda_5434():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5434')

    DispatchAsync2(0x000C, 0x0001, lambda_5434)

    Sleep(200)

    @scena.Lambda('lambda_544A')
    def lambda_544A():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_544A')

    DispatchAsync2(0x000D, 0x0001, lambda_544A)

    Sleep(100)

    @scena.Lambda('lambda_5460')
    def lambda_5460():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_5460')

    DispatchAsync2(0x0008, 0x0001, lambda_5460)

    ChrTalk(
        0x000C,
        (
            '#0270210434V#141F#6P噢，回来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280210435V#151F#4P小艾！\n',
            '你回来啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x000D)

    @scena.Lambda('lambda_54CD')
    def lambda_54CD():
        OP_6D(-3940, 0, 45120, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_54CD)

    @scena.Lambda('lambda_54E5')
    def lambda_54E5():
        OP_67(0, 6260, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_54E5)

    CreateThread(0x00F7, 0x01, 0x00, 0x000E)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x0008, 0x01)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010210436V#1008F#6P奈尔、朵洛希！\n',
            '你们怎么会在卢安？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270210437V#141F#5P这个嘛，当然是为了采访\n',
            '热门话题市长选举而来的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210438V对了，听说还发生了奇怪的事件，\n',
            '所以就来协会问问情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210439V#1017F#6P奇怪的事件……\n',
            '是那个『白影』的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0008,
        (
            '#0500210440V#654F其实，在你们调查期间，\n',
            '市街发生了另外的目击事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210441V市民之间的不安\n',
            '也在逐渐蔓延。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_56DE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210442V#050F#6P是吗……\n',
            '事情渐渐闹大了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5713')

    def _loc_56DE(): pass

    label('loc_56DE')

    ChrTalk(
        0x0103,
        (
            '#0030210443V#022F#6P哎呀……\n',
            '越发变得严重了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5713(): pass

    label('loc_5713')

    ChrTalk(
        0x0008,
        (
            '#0500210444V#652F并且，可以断定的是……\n',
            '这位小姐拍的照片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210445V我想这是相当\n',
            '有价值的情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210446V#1015F#6P照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210447V#1020F#6P不、不不、不会吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5837',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210448V#052F#6P所谓的灵异照片？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5863')

    def _loc_5837(): pass

    label('loc_5837')

    ChrTalk(
        0x0103,
        (
            '#0030210449V#023F#6P所谓的灵异照片吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5863(): pass

    label('loc_5863')

    ChrTalk(
        0x000D,
        (
            '#0280210450V#150F#2P嗯～大概是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210451V在酒店拍摄夜景的时候\n',
            '偶然拍下来的，\n',
            '我还搞不太清楚呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210452V先看看吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD(0x00240090, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010210453V#1020F………………………（咕噜）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_59A1',
    )

    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName('阿加特')

    Talk(
        (
            '#0050210454V#552F……什么～？\n',
            '这样可以确定这次事件的真实性了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_59F4')

    def _loc_59A1(): pass

    label('loc_59A1')

    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            '#0030210455V#025F……唉。\n',
            '这样可以确定这次事件的真实性了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_59F4(): pass

    label('loc_59F4')

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010210456V#1016F啊、啊哈哈……\n',
            '要下结论也太早了点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210457V也可能是导力照相机\n',
            '出毛病了也不一定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName('朵洛希')

    Talk(
        (
            '#0280210458V#150F嗯～故障～？\n',
            '不可能是故障哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210459V#151F这是从中央工房买的最新机种，\n',
            '维护得也很仔细呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010210460V#1019F不是真的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName('朵洛希')

    Talk(
        (
            '#0280210461V#154F小艾、好可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0500210462V#654F嗯，也就是说\n',
            '事件变得\n',
            '很真实化了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210463V#652F这件事就算和媒体\n',
            '配合应该也没什么坏处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210464V现在就赶快把各地\n',
            '调查的情况报告了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210465V#1015F#6P嗯、嗯……\n',
            '３个地方都调查过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000E, 200, -500, 37500, 0)

    NpcTalk(
        0x000E,
        '青年的声音',
        (
            '#1760210466V#2P不、不好了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_5D1F')
    def lambda_5D1F():
        ChrTurnDirection(0x0101, 0x000E, 400)
        Yield()

        Jump('lambda_5D1F')

    DispatchAsync2(0x0101, 0x0001, lambda_5D1F)

    @scena.Lambda('lambda_5D30')
    def lambda_5D30():
        ChrTurnDirection(0x00F7, 0x000E, 400)
        Yield()

        Jump('lambda_5D30')

    DispatchAsync2(0x00F7, 0x0001, lambda_5D30)

    @scena.Lambda('lambda_5D41')
    def lambda_5D41():
        ChrTurnDirection(0x000C, 0x000E, 400)
        Yield()

        Jump('lambda_5D41')

    DispatchAsync2(0x000C, 0x0001, lambda_5D41)

    @scena.Lambda('lambda_5D52')
    def lambda_5D52():
        ChrTurnDirection(0x000D, 0x000E, 400)
        Yield()

        Jump('lambda_5D52')

    DispatchAsync2(0x000D, 0x0001, lambda_5D52)

    @scena.Lambda('lambda_5D63')
    def lambda_5D63():
        ChrTurnDirection(0x0008, 0x000E, 400)
        Yield()

        Jump('lambda_5D63')

    DispatchAsync2(0x0008, 0x0001, lambda_5D63)

    @scena.Lambda('lambda_5D74')
    def lambda_5D74():
        OP_6D(-3020, 0, 43600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5D74)

    @scena.Lambda('lambda_5D8C')
    def lambda_5D8C():
        OP_67(0, 6260, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5D8C)

    Sleep(500)

    OP_9F(0x000E, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_5DB9')
    def lambda_5DB9():
        OP_8E(0x00FE, 0, 0, 39190, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_5DB9)

    @scena.Lambda('lambda_5DD4')
    def lambda_5DD4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5DD4)

    WaitForThreadExit(0x000E, 0x0000)

    @scena.Lambda('lambda_5DEB')
    def lambda_5DEB():
        OP_8E(0x00FE, -2790, 0, 41750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_5DEB)

    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    ChrTurnDirection(0x000E, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x0008, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010210467V#1004F#5P怎、怎么了！\n',
            '那么慌张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5E93',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210468V#054F#2P有抢劫吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EBF')

    def _loc_5E93(): pass

    label('loc_5E93')

    ChrTalk(
        0x0103,
        (
            '#0030210469V#024F#2P难道出现了魔兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EBF(): pass

    label('loc_5EBF')

    ChrTalk(
        0x000E,
        (
            '#1760210470V#6P不、不是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1760210471V#6P诺曼先生的支持者\n',
            '波尔多斯的支持者\n',
            '吵起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#1760210472V#6P现在正在伦格兰德大桥\n',
            '相互对峙中！',
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
            '#0010210473V#1005F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5FF5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210474V#057F#2P说到诺曼和波尔多斯，\n',
            '两人都是市长选举的候选人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6040')

    def _loc_5FF5(): pass

    label('loc_5FF5')

    ChrTalk(
        0x0103,
        (
            '#0030210475V#022F#2P说到诺曼和波尔多斯，\n',
            '两人都是市长选举的候选人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6040(): pass

    label('loc_6040')

    ChrTalk(
        0x000C,
        (
            '#0270210476V#141F#5P喔喔。\n',
            '这可是相当不错的新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 90, 400)

    ChrTalk(
        0x000C,
        (
            '#0270210477V#144F#5P朵洛希、快走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280210478V#151F#2P是，前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 600)
    ChrTurnDirection(0x0101, 0x000C, 600)
    ChrTurnDirection(0x00F7, 0x000C, 600)

    ChrTalk(
        0x000D,
        (
            '#0280210479V#150F#2P小艾，回头见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_610F')
    def lambda_610F():
        OP_6D(-1770, 0, 42260, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_610F)

    @scena.Lambda('lambda_6127')
    def lambda_6127():
        OP_67(0, 6260, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6127)

    ChrTurnDirection(0x000C, 0x0101, 600)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x000C, 0x01, 0x00, 0x000F)

    @scena.Lambda('lambda_615F')
    def lambda_615F():
        OP_91(0x00FE, -500, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_615F)

    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_6191')
    def lambda_6191():
        OP_91(0x00FE, 300, 0, 300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_6191)

    @scena.Lambda('lambda_61AC')
    def lambda_61AC():
        ChrTurnDirection(0x0101, 0x000C, 0)
        Yield()

        Jump('lambda_61AC')

    DispatchAsync2(0x0101, 0x0002, lambda_61AC)

    @scena.Lambda('lambda_61BD')
    def lambda_61BD():
        ChrTurnDirection(0x00F7, 0x000C, 0)
        Yield()

        Jump('lambda_61BD')

    DispatchAsync2(0x00F7, 0x0002, lambda_61BD)

    CreateThread(0x000D, 0x01, 0x00, 0x0010)
    WaitForThreadExit(0x000D, 0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x00F7, 0x02)

    @scena.Lambda('lambda_61E2')
    def lambda_61E2():
        OP_6D(-3750, 0, 44170, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_61E2)

    @scena.Lambda('lambda_61FA')
    def lambda_61FA():
        OP_67(0, 6260, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_61FA)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010210480V#1019F#5P好、好快啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    @scena.Lambda('lambda_624C')
    def lambda_624C():
        OP_8F(0x00FE, -2340, 0, 43760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_624C)

    WaitForThreadExit(0x00F7, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_62C5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210481V#057F#4P以防万一我们也去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210482V万一要打起来\n',
            '得赶快调停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6316')

    def _loc_62C5(): pass

    label('loc_62C5')

    ChrTalk(
        0x0103,
        (
            '#0030210483V#022F#4P我们也去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210484V万一要打起来\n',
            '得插手调停才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6316(): pass

    label('loc_6316')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210485V#1002F#5P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500210486V#652F#5P抱歉。\n',
            '就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 105, 400)
    OP_4B(0x0008, 255)
    OP_4B(0x000E, 255)
    CreateThread(0x000E, 0x00, 0x06, 0x0002)
    OP_A2(0x121C)
    OP_28(0x0082, 0x01, 0x0800)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x638D
@scena.Code('func_0D_638D')
def func_0D_638D():
    OP_8E(0x00FE, -3020, 0, 43600, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000D, 400)

    Return()

# id: 0x000E offset: 0x63A9
@scena.Code('func_0E_63A9')
def func_0E_63A9():
    Sleep(500)

    OP_8E(0x00FE, -1840, 0, 43600, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000C, 400)

    Return()

# id: 0x000F offset: 0x63CA
@scena.Code('func_0F_63CA')
def func_0F_63CA():
    OP_8F(0x00FE, -20, -500, 38350, 5000, 0x00)

    @scena.Lambda('lambda_63E4')
    def lambda_63E4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_63E4)

    OP_8F(0x00FE, 90, -500, 37500, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0010 offset: 0x640A
@scena.Code('func_10_640A')
def func_10_640A():
    Sleep(500)

    OP_8C(0x00FE, 180, 0)
    OP_8F(0x00FE, -2500, 0, 44340, 5000, 0x00)
    OP_8F(0x00FE, -20, -500, 38350, 5000, 0x00)

    @scena.Lambda('lambda_6444')
    def lambda_6444():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6444)

    OP_8F(0x00FE, 90, -500, 37500, 5000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0011 offset: 0x646A
@scena.Code('func_11_646A')
def func_11_646A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_647B',
    )

    Call(0, 0x001D)

    def _loc_647B(): pass

    label('loc_647B')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    OP_4A(0x0008, 255)
    SetChrPos(0x0101, -3540, 0, 45030, 90)
    SetChrPos(0x00F7, -3550, 0, 46010, 125)
    SetChrPos(0x0104, -2090, 0, 45270, 268)
    SetChrPos(0x000C, -3440, 0, 43970, 44)
    SetChrPos(0x000D, -2380, 0, 44040, 10)
    OP_6D(460, 0, 37310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    @scena.Lambda('lambda_6537')
    def lambda_6537():
        OP_6D(-3150, 0, 45370, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6537)

    @scena.Lambda('lambda_654F')
    def lambda_654F():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_654F)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0104,
        (
            '#0040210582V#034F多么薄情啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210583V面对久别重逢\n',
            '的命运对象，\n',
            '这样的行为实在太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6669',
    )

    ChrTalk(
        0x0101,
        (
            '#0010210584V#1007F#5P什么命运的对象啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210585V#1019F那，奥利维尔\n',
            '怎么会在卢安啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210586V不是在\n',
            '亚尔摩的温泉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_66FE')

    def _loc_6669(): pass

    label('loc_6669')

    ChrTalk(
        0x0101,
        (
            '#0010210584V#1007F#5P什么命运的对象啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210588V#1019F那，奥利维尔\n',
            '怎么会在卢安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210589V#020F#5P记得是在亚尔摩温泉\n',
            '才对啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66FE(): pass

    label('loc_66FE')

    ChrTalk(
        0x0104,
        (
            '#0040210590V#030F呵，其实穆拉\n',
            '给红叶亭发来了联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210591V特地告诉我\n',
            '艾丝蒂尔你回来了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210592V#031F我想必须要来见你才行，\n',
            '就拼了命赶过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210593V#1007F#5P好、好意我心领了，\n',
            '说实话还真没有高兴的感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210594V#1017F不过，诞辰庆典之后\n',
            '就再没见过面呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210595V谢谢，奥利维尔。\n',
            '能再见到你真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210596V#033F是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210597V#032F唔～艾丝蒂尔\n',
            '一坦率好像浑身不对劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040210598V#037F不多多挖苦我的话，\n',
            '嗯……会欲求不满的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210599V#1014F#5P#3S不要红着脸\n',
            '再说这种轻浮的话！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210600V#1019F#5P唉……算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210601V#1007F#6P嘉恩哥哥。\n',
            '这是政变事件的时候\n',
            '帮助过我们的奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210602V从埃雷波尼亚来的演奏家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0500210603V#650F啊……\n',
            '真是厉害的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210604V既然如此，\n',
            '就让他一起听报告\n',
            '也没关系吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6BAB',
    )

    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210605V#552F#2P本来正要把他当成是\n',
            '外部人员赶出去的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210606V想想他也不会乖乖出去的，\n',
            '那就不用理他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210607V#031F哈哈哈。\n',
            '不愧是阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210608V关于我的事\n',
            '非常了解呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0104, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210609V#055F#5P完全是\n',
            '两回事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210610V那个时候只是一起作战过，\n',
            '没怎么说过话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6CA6')

    def _loc_6BAB(): pass

    label('loc_6BAB')

    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210611V#020F#2P嗯，算了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210612V反正就算不让他听，\n',
            '他也死缠烂打跟着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210613V#031F哈哈哈。\n',
            '不愧是雪拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210608V关于我的事\n',
            '非常了解呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210615V#027F#5P背景是不大清楚，\n',
            '性格方面还算大概了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CA6(): pass

    label('loc_6CA6')

    ChrTalk(
        0x0101,
        (
            '#0010210616V#1019F#6P……嗯，随他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500210617V#651FＯＫ。\n',
            '这样也比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 0, 300)

    ChrTalk(
        0x000C,
        (
            '#0270210618V#142F怎样都好，\n',
            '赶快说来听听吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210619V我们可是在等着\n',
            '收集市长选举的消息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    @scena.Lambda('lambda_6D76')
    def lambda_6D76():
        ChrTurnDirection(0x00F7, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_6D76)

    @scena.Lambda('lambda_6D84')
    def lambda_6D84():
        ChrTurnDirection(0x0008, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6D84)

    @scena.Lambda('lambda_6D92')
    def lambda_6D92():
        ChrTurnDirection(0x0104, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_6D92)

    @scena.Lambda('lambda_6DA0')
    def lambda_6DA0():
        ChrTurnDirection(0x000D, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6DA0)

    ChrTalk(
        0x0101,
        (
            '#0010210620V#1007F#5P是是，知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210621V#1002F那么就按照询问的顺序\n',
            '报告目击情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '除了报告各地的目击情报之外\n',
            '还说明了凯文神父的见解。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0008,
        (
            '#0500210622V#650F原来如此……\n',
            '收集得很具体呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210623V至少已经调查到\n',
            '足够多的情报了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210624V#1015F#5P嗯～是吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270210625V#141F不过，刚才骚动时民众说的\n',
            '为了妨碍市长选举对手阵营\n',
            '而搞的恶作剧应该是不可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210626V且不说诺曼的儿子，\n',
            '威胁孤儿院和关所的士兵\n',
            '想不出有什么用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_700A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210627V#050F#2P亡灵确实在天上飞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210628V这应该不是一般人\n',
            '能简单做到的技巧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7069')

    def _loc_700A(): pass

    label('loc_700A')

    ChrTalk(
        0x0103,
        (
            '#0030210629V#022F#2P亡灵确实在天上飞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210630V这应该不是一般人\n',
            '能简单做到的技巧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7069(): pass

    label('loc_7069')

    OP_62(0x000D, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0280210631V#151F#6P那么果然\n',
            '是货真价实的幽灵吗～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210632V可能是被戴上面具，\n',
            '在被幽禁中疯了的\n',
            '太古贵族之类～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210633V经过数百年来到现代，\n',
            '化为怨灵苏醒了～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210634V#1019F#5P那、那么恐怖的事\n',
            '不要说得那么开心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210635V#1015F再说、所谓幽灵\n',
            '好像都是被人或者地方所束缚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210636V这好象有所不同吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040210637V#035F……不。\n',
            '这可难说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0104, 500)

    @scena.Lambda('lambda_724D')
    def lambda_724D():
        ChrTurnDirection(0x00F7, 0x0104, 500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_724D)

    @scena.Lambda('lambda_725B')
    def lambda_725B():
        ChrTurnDirection(0x0008, 0x0104, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_725B)

    @scena.Lambda('lambda_7269')
    def lambda_7269():
        ChrTurnDirection(0x000C, 0x0104, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_7269)

    @scena.Lambda('lambda_7277')
    def lambda_7277():
        ChrTurnDirection(0x000D, 0x0104, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_7277)

    ChrTalk(
        0x0101,
        (
            '#0010210638V#1004F#5P怎、怎么了，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_72E2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210639V#052F#5P想到什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_730A')

    def _loc_72E2(): pass

    label('loc_72E2')

    ChrTalk(
        0x0103,
        (
            '#0030210640V#023F#5P想到什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_730A(): pass

    label('loc_730A')

    ChrTalk(
        0x0104,
        (
            '#0040210641V#030F不，是不是幽灵\n',
            '我也无法判断……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210642V不过听了艾丝蒂尔的报告，\n',
            '觉得有几个地方值得注意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210643V对于那个白影，它不被人和地方\n',
            '所束缚这样的说法，\n',
            '我稍微有点疑问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500210644V#650F哎呀，真了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210645V#651F我也正在考虑\n',
            '同一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210646V#031F呵呵，果然是吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210647V#030F作为旅行者，我最近\n',
            '经常仔细观察王国地图……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210648V首先请关注\n',
            '卢安地区吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS133._CH')
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS200._CH')
    OP_C5(0x02, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS201._CH')
    OP_C5(0x03, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS202._CH')
    OP_C5(0x04, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS203._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1000, 0)
    Sleep(1500)

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040210649V#032F那么……\n',
            '关于艾丝蒂尔等人调查的\n',
            '３处目击地点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210650V是这里，这里，和这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010210651V#1015F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210652V卢安南街区和\n',
            '艾尔·雷登关所，\n',
            '还有玛西亚孤儿院。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210653V是啊，这３处怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040210654V#035F这３处的证言\n',
            '有着一条很明显不同的信息，\n',
            '而事实就会从这信息中浮现出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210655V#030F艾丝蒂尔。\n',
            '你觉得这个不同的信息是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010210656V#1002F３个证言\n',
            '明显不同的信息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210657V#1004F那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '３处证言中有明显不同的地方是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【白影出现的时间】\n'),
            TXT(0x01, '【白影离去的方向】\n'),
            TXT(0x02, '【白影采取的行动】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_78A7'),
        (0x00000001, 'loc_7A26'),
        (0x00000002, 'loc_7A7C'),
        (-1, 'loc_7C17'),
    )

    def _loc_78A7(): pass

    label('loc_78A7')

    OP_2B(0x0082, 0x0001)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040210658V#030F嗯，孤儿院的孩子\n',
            '说是在晚饭后看见的幽灵，\n',
            '而其它两人都是半夜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210659V每个证言说的都是夜晚，\n',
            '可以说其实是差不多的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010210660V#1007F嗯～是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 50, -1, -1)
    SetChrName('嘉恩')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0500210661V#651F那么我来\n',
            '回答吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210662V#650F就是幽灵离去的方向吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010210663V#1004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_7C17')

    def _loc_7A26(): pass

    label('loc_7A26')

    OP_2B(0x0082, 0x0003)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010210664V#1018F明白了！\n',
            '也就是白影离去的方向吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_7C17')

    def _loc_7A7C(): pass

    label('loc_7A7C')

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040210665V#030F不，３处证言\n',
            '重合的部分很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210666V对孤儿院的孩子打了招呼\n',
            '可称作例外……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210667V不过除此以外，转着圈跳着舞\n',
            '向天空飞去这些\n',
            '都是相当相似的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010210660V#1007F嗯～是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 50, -1, -1)
    SetChrName('嘉恩')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0500210661V#651F那么我来\n',
            '回答吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210662V#650F就是幽灵离去的方向吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010210663V#1004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_7C17')

    def _loc_7C17(): pass

    label('loc_7C17')

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040210672V#031F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210673V#030F南街区不良少年的证言\n',
            '是白影消失在『东北』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040210674V#030F艾尔·雷登士兵的证言\n',
            '是白影消失在『北』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040210675V#035F而孤儿院孩子的证言\n',
            '是白影消失在『东』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010210676V#1004F#4S啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7E20',
    )

    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName('阿加特')

    Talk(
        (
            '#0050210677V#051F呵，是那样的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_7E5A')

    def _loc_7E20(): pass

    label('loc_7E20')

    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            '#0030210678V#020F的确很隐蔽啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_7E5A(): pass

    label('loc_7E5A')

    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName('奈尔')

    Talk(
        (
            '#0270210679V#141F原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210680V就是说幽灵离去的地方\n',
            '可以确定了，是吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040210681V#031F呵呵～就是那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210682V#030F『杰尼丝王立学院』……\n',
            '好像就在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 0, 0)
    OP_C6(0x04, 0x03, 16777215, 1000, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010210683V#1001F#5P奥利维尔……\n',
            '你真够机灵的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210684V#1006F既然如此，幽灵也好、\n',
            '什么也好都无所谓了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210685V赶紧去调查吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_80B8',
    )

    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210686V#051F#2P呼……\n',
            '嘉恩，你没疑问吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_80F8')

    def _loc_80B8(): pass

    label('loc_80B8')

    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210687V#020F#2P嘉恩。\n',
            '我们要去学院，没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_80F8(): pass

    label('loc_80F8')

    ChrTalk(
        0x0008,
        (
            '#0500210688V#650F啊啊，请认真调查，\n',
            '最好能成功解决问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000C, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0500210689V#650F利贝尔通讯的同志\n',
            '现在打算怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8180')
    def lambda_8180():
        ChrTurnDirection(0x0101, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8180)

    @scena.Lambda('lambda_818E')
    def lambda_818E():
        ChrTurnDirection(0x00F7, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_818E)

    @scena.Lambda('lambda_819C')
    def lambda_819C():
        ChrTurnDirection(0x0104, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_819C)

    @scena.Lambda('lambda_81AA')
    def lambda_81AA():
        ChrTurnDirection(0x000D, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_81AA)

    ChrTalk(
        0x000C,
        (
            '#0270210690V#145F这个嘛，关键的市长选举\n',
            '还得去采访……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000D, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0270210691V#141F#5P好吧，朵洛希。\n',
            '这个事就交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280210692V#151F#6P好～明白了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210693V我一定会努力\n',
            '拍出好的灵异照片的～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270210694V#144F#5P不是！\n',
            '是要你去了解事件的真相。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210695V跟艾丝蒂尔他们去\n',
            '做幽灵事件的采访!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280210696V#153F#6P啊，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210697V#151F虽然还不大明白啦～\n',
            '但我一定尽心尽力～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210698V#1019F#2P我、我说。\n',
            '别说得那么轻松好不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0500210699V#651F好了好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210700V你们也提供了照片，\n',
            '就算礼尚往来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8420',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210701V#552F#2P呼……没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8453')

    def _loc_8420(): pass

    label('loc_8420')

    ChrTalk(
        0x0103,
        (
            '#0030210702V#021F#2P嗯，就这点小事\n',
            '没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8453(): pass

    label('loc_8453')

    ChrTalk(
        0x0101,
        (
            '#0010210703V#1007F#2P嗯～感觉紧张感\n',
            '越来越淡了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210704V#1017F不过，这样倒也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#0270210705V#141F就这样了，\n',
            '事件的调查就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210706V我接着去采访\n',
            '两位候选人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 135, 400)

    @scena.Lambda('lambda_8520')
    def lambda_8520():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_8520')

    DispatchAsync2(0x0101, 0x0001, lambda_8520)

    @scena.Lambda('lambda_8531')
    def lambda_8531():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_8531')

    DispatchAsync2(0x00F7, 0x0001, lambda_8531)

    @scena.Lambda('lambda_8542')
    def lambda_8542():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_8542')

    DispatchAsync2(0x0104, 0x0001, lambda_8542)

    @scena.Lambda('lambda_8553')
    def lambda_8553():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_8553')

    DispatchAsync2(0x000D, 0x0001, lambda_8553)

    @scena.Lambda('lambda_8564')
    def lambda_8564():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_8564')

    DispatchAsync2(0x0008, 0x0001, lambda_8564)

    @scena.Lambda('lambda_8575')
    def lambda_8575():
        OP_8E(0x00FE, -1250, 0, 41210, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_8575)

    Sleep(700)

    @scena.Lambda('lambda_8595')
    def lambda_8595():
        OP_8E(0x00FE, -1250, 0, 41210, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_8595)

    @scena.Lambda('lambda_85B0')
    def lambda_85B0():
        OP_6D(-2280, 0, 44400, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_85B0)

    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0270210707V#143F……\n',
            '对了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0270210708V#140F……关于约修亚，\n',
            '我从你父亲那儿听说了一些事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210709V谜之组织的确令人在意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210710V如果有相关信息\n',
            '我会马上联络协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210711V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270210712V#144F所以呢……\n',
            '好了，你加油吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210713V那、那我走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 135, 600)

    @scena.Lambda('lambda_8714')
    def lambda_8714():
        OP_6D(-1770, 0, 42260, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8714)

    @scena.Lambda('lambda_872C')
    def lambda_872C():
        OP_8E(0x00FE, 150, 0, 39450, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_872C)

    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_874C')
    def lambda_874C():
        OP_8E(0x00FE, 410, -500, 37140, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_874C)

    Sleep(200)

    @scena.Lambda('lambda_876C')
    def lambda_876C():
        OP_9F(0x000C, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_876C)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x000C, 0x0001)
    Sleep(500)

    OP_6D(-3790, 0, 46180, 1500)
    SetChrFlags(0x000C, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x00F7, 0xFF)
    TerminateThread(0x0104, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010210714V#1025F#5P奈尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280210715V#151F#5P啊哈哈。\n',
            '前辈还害羞呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0280210716V#150F#6P前辈好像听了卡西乌斯先生的话之后\n',
            '相当震惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210717V不知道自己能帮什么忙，\n',
            '他好像一直很烦恼呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210718V#1008F#5P这、这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210719V#1016F真是的……\n',
            '该说他是不坦率呢还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280210720V#150F#6P这么说我也一样，\n',
            '如果在采访中发现值得注意的消息\n',
            '也会马上联络协会的～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210721V#151F所以小艾。\n',
            '要·加·油·哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210722V#1012F#5P嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210723V#1018F那么……\n',
            '去王立学院吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '#0500210724V#650F王立学院那边\n',
            '我会去联络的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500210725V那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_A2(0x10F0)
    OP_A2(0x121D)
    NewScene('ED6_DT21/T2100._SN', 109, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x8A41
@scena.Code('func_12_8A41')
def func_12_8A41():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8A52',
    )

    Call(0, 0x001D)

    def _loc_8A52(): pass

    label('loc_8A52')

    EventBegin(0x00)
    OP_1D(0x0C)
    SetChrPos(0x0101, -3540, 0, 46000, 270)
    SetChrPos(0x00F7, -2470, 0, 45400, 270)
    SetChrPos(0x0104, -2720, 0, 44400, 270)
    SetChrPos(0x0105, -3540, 0, 43930, 315)
    OP_6D(-4410, 0, 45930, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()
    OP_28(0x0084, 0x01, 0x0040)
    OP_28(0x0084, 0x01, 0x0080)
    OP_28(0x0084, 0x01, 0x0100)
    OP_28(0x0084, 0x01, 0x0200)

    ChrTalk(
        0x0008,
        (
            '#0500211805V#652F#5P是吗……辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211806V#655F『噬身之蛇』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211807V听卡西乌斯先生说起的时候，\n',
            '说实话，还半信半疑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211808V#652F总而言之，\n',
            '先给你们这次调查的报酬吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211809V虽然没想到\n',
            '会变成这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0082, 0x04, 0x10)
    OP_AF(0x67, 0x0082)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x0083, 0x04, 0x10)
    OP_28(0x0083, 0x04, 0x20)
    OP_28(0x0084, 0x04, 0x10)
    OP_28(0x0084, 0x04, 0x20)

    ChrTalk(
        0x0008,
        (
            '#0500211810V#652F调查结果\n',
            '我马上向王国军报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211811V军队那边也相当\n',
            '需要情报呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8D03',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211812V#050F啊啊，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211813V考虑到那个投影装置，\n',
            '那个组织肯定不简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211814V而且居然连『福音』\n',
            '都拿出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D98')

    def _loc_8D03(): pass

    label('loc_8D03')

    ChrTalk(
        0x0103,
        (
            '#0030211815V#022F嗯嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211816V考虑到那个投影装置，\n',
            '那个组织肯定具有相当大的规模。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211817V而且居然连『福音』\n',
            '都拿出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D98(): pass

    label('loc_8D98')

    ChrTalk(
        0x0104,
        (
            '#0040211818V#030F看来结社的目的\n',
            '似乎是使用新『福音』\n',
            '做实验呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211819V幽灵骚动，似乎只是\n',
            '凭兴趣的实验结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211820V#1002F#2P怪盗布卢布兰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211821V那个家伙，称呼自己\n',
            '为『执行者』对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500211822V#652F#5P恐怕他是『结社』\n',
            '精英吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211823V根据推察，那个洛伦斯少尉\n',
            '应该也和他立场相似吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211824V#1003F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211825V#043F#6P艾丝蒂尔，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010211826V#1007F#5P嗯，我知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211827V#1003F『漆黑之牙』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211828V那天，约修亚是这样\n',
            '称呼自己的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211829V#1025F大概约修亚也是\n',
            '那种『执行者』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_90B4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211830V#053F原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211831V和那个混帐怪盗同等级的话，\n',
            '那家伙的专业技术也能理解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211832V#552F搞不好是隐藏实力\n',
            '伪装了自己也不一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9161')

    def _loc_90B4(): pass

    label('loc_90B4')

    ChrTalk(
        0x0103,
        (
            '#0030211833V#025F第一次见面的时候\n',
            '就觉得他不一般……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211834V没想到小小年纪，竟然\n',
            '和那怪盗男同等级……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211835V#522F或许那孩子，是隐藏了\n',
            '自己的实力也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9161(): pass

    label('loc_9161')

    ChrTalk(
        0x0101,
        (
            '#0010211836V#1003F#5P嗯……可能吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211837V#1002F#2P……对了，嘉恩哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500211838V#653F#5P怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211839V#1002F#2P那个怪盗男说\n',
            '结社的计划才刚刚开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211840V大概还会在利贝尔各地\n',
            '做各种事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211841V其它的地方支部\n',
            '没发来什么情报吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500211842V#654F#5P嗯……\n',
            '现在没有特别的情报呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211843V#652F不过，艾丝蒂尔说得对，\n',
            '结社在各地开始暗中活动\n',
            '的可能性极高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211844V幽灵骚动也告一段落了，\n',
            '你们转移到其它地区比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_939B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211845V#051F啊啊。\n',
            '我也正在考虑这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211846V哪个支部比较缺人手？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_93EB')

    def _loc_939B(): pass

    label('loc_939B')

    ChrTalk(
        0x0103,
        (
            '#0030211847V#020F是啊。\n',
            '我也是这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211848V哪个支部比较缺人手？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_93EB(): pass

    label('loc_93EB')

    ChrTalk(
        0x0008,
        (
            '#0500211849V#650F#5P稍微缺乏人手的话\n',
            '应该是蔡斯支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211850V原本应该在蔡斯的冈多夫\n',
            '好像去了王都那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211851V看上去很吃力的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211852V#1006F#2P那么，我们\n',
            '最好去帮忙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211853V不过，卢安支部不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500211854V#651F#5P其实，柏斯支部的斯丁克\n',
            '数日后会来这边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211855V之前就让梅尔茨一个人\n',
            '想办法撑着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211856V#650F对了，到了蔡斯\n',
            '最好去找一下拉赛尔博士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211857V有关新『福音』的事\n',
            '最好借助博士的智慧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211858V#1006F#2P嗯，确实是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211859V也想见见提妲了，\n',
            '就立刻出发去中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211860V#031F那么准备好之后\n',
            '就马上去飞船坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040211861V#030F嘉恩先生。\n',
            '麻烦你安排４张船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500211862V#653F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211863V#1019F#5P干嘛突然\n',
            '做这种厚脸皮的总结性发言啊……',
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
            '#0010211864V#1004F#5P……啊，４张？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9830',
    )

    ChrTalk(
        0x0104,
        (
            '#0040211865V#035F呵，艾丝蒂尔和阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211866V#030F然后是我和\n',
            '公主殿下的份，这还用说吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211867V#1005F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0104, 400)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050211868V#552F#2P就觉得是这样……\n',
            '以后还打算跟着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_990D')

    def _loc_9830(): pass

    label('loc_9830')

    ChrTalk(
        0x0104,
        (
            '#0040211869V#035F呵，艾丝蒂尔和雪拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211866V#030F然后是我和\n',
            '公主殿下的份，这还用说吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211871V#1005F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030211872V#020F#2P就觉得是这样……\n',
            '以后还打算跟着来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_990D(): pass

    label('loc_990D')

    ChrTurnDirection(0x0104, 0x00F7, 400)

    ChrTalk(
        0x0104,
        (
            '#0040211873V#031F寻找约修亚\n',
            '是我作为爱之猎人的使命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211874V并且还遇上了一个好对手，\n',
            '同行的理由应该很充分了吧？',
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
            '#0010211875V#1019F#5P你、你那些\n',
            '乱七八糟的理由先不提了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211876V怎么连科洛丝\n',
            '都一起卷进来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211877V#542F#6P不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211878V其实我也有\n',
            '同样的请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211879V#1004F#5P咦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211880V#047F#6P在利贝尔暗中活跃的\n',
            '神秘组织『结社』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211881V身为拥有王位继承权的人\n',
            '不能置之不理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211882V#043F而且更重要的是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211883V我想帮助\n',
            '艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211884V#1008F#5P科洛丝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211885V但、但是\n',
            '学院的课程怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211886V#542F#6P其实今天早上，我向科林兹校长\n',
            '递交了休学申请。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211887V考试的成绩没有问题了，\n',
            '晋级需要的学分也够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211888V#041F和乔儿、汉斯也商量过，\n',
            '他们说『你就去吧』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211889V#1016F#5P什、什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9E7C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211890V#051F#2P哎呀哎呀。\n',
            '真是位做事干脆的公主啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211891V#540F#6P对、对不起……\n',
            '先斩后奏确实不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211892V#043F那个……不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211893V#1008F#5P呵呵……\n',
            '怎么可能不行嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211894V#1018F既然如此，\n',
            '就不客气地劳你帮忙喽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211895V#1006F#5P阿加特也没意见吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050211896V#051F#2P嗯，好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211897V无论是魔法还是那只隼，\n',
            '公主在可真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211898V#045F#6P太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211899V#048F谢谢你们。\n',
            '艾丝蒂尔，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A077')

    def _loc_9E7C(): pass

    label('loc_9E7C')

    ChrTalk(
        0x0103,
        (
            '#0030211900V#027F#2P呵呵。\n',
            '真不愧是公主殿下，做事如此干脆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211891V#540F#6P对、对不起……\n',
            '先斩后奏确实不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211892V#043F那个……不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211903V#1016F#5P呵呵……\n',
            '怎么可能不行嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211894V#1018F既然如此，\n',
            '就不客气地劳你帮忙喽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211905V#1006F#5P雪拉姐也没意见吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030211906V#021F#2P嗯嗯，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211907V无论是魔法还是那只隼，\n',
            '公主殿下在可真是帮大忙了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211898V#045F#6P太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211909V#048F谢谢你们。\n',
            '艾丝蒂尔，雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A077(): pass

    label('loc_A077')

    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211910V#1017F#5P嘿嘿，怎么说都是\n',
            '是红骑士和苍骑士的关系嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211911V齐心协力，去寻找\n',
            '失踪的公主吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211912V#542F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211913V#041F好，说得对呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211914V#035F呼，那我就是\n',
            '打算强行夺走黑发公主的\n',
            '邻国王子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211915V#1005F#5P不要随便增加角色！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500211916V#651F#5P啊哈哈……\n',
            '你们意见相符就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211917V#650F不过这样的话\n',
            '我就把两人当作\n',
            '『协力人员』来处理比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500211918V这样的话，协会\n',
            '在经费方面也好计算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    @scena.Lambda('lambda_A271')
    def lambda_A271():
        ChrTurnDirection(0x00F7, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_A271)

    @scena.Lambda('lambda_A27F')
    def lambda_A27F():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A27F)

    ChrTalk(
        0x0105,
        (
            '#0060211919V#040F#6P好的，那么就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211920V#031F我会诚心诚意，满怀爱心的\n',
            '来协力你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(ItemTable['后门的钥匙'], 1)
    RemoveItem(ItemTable['旧钥匙'], 1)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_AD(0x002400AE, 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_A2(0x1241)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x123),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x0E, 0x00, 0x00, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A390',
    )

    ShowSaveMenu()

    def _loc_A390(): pass

    label('loc_A390')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_20(0x00000BB8)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_21()
    OP_A3(0x1241)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    NewScene('ED6_DT21/T2105._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0xA3C9
@scena.Code('func_13_A3C9')
def func_13_A3C9():
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
        'loc_A3E0',
    )

    Call(0, 0x001D)
    Call(0, 0x001E)

    def _loc_A3E0(): pass

    label('loc_A3E0')

    OP_4A(0x0008, 255)
    OP_6D(-5760, 0, 45080, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    OP_8C(0x0008, 135, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360001V#650F#5P呀，有什么困扰的事吗──',
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
            '#0500360002V#653F#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0101, -550, 0, 39990, 315)
    SetChrPos(0x0102, 80, 0, 40550, 315)
    SetChrPos(0x00F8, 180, 0, 39140, 315)
    SetChrPos(0x00F9, 840, 0, 39800, 315)

    @scena.Lambda('lambda_A4F8')
    def lambda_A4F8():
        OP_6D(-5300, 0, 46380, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A4F8)

    @scena.Lambda('lambda_A510')
    def lambda_A510():
        OP_67(0, 5620, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A510)

    @scena.Lambda('lambda_A528')
    def lambda_A528():
        OP_6E(310, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_A528)

    @scena.Lambda('lambda_A538')
    def lambda_A538():
        OP_6B(2600, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_A538)

    @scena.Lambda('lambda_A548')
    def lambda_A548():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_A548')

    DispatchAsync2(0x0008, 0x0002, lambda_A548)

    CreateThread(0x0102, 0x01, 0x00, 0x0015)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x0014)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x0017)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0016)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    TerminateThread(0x0008, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010360003V#1006F#6P你好，嘉恩哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360004V#1035F……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500360005V#653F#5P艾丝蒂尔……\n',
            '还有约修亚……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360006V#656F是吗……\n',
            '大家都平安无事就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360007V你们去『塔』的时候\n',
            '发生了那个现象，\n',
            '真是令人担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360008V#1016F#6P啊哈哈……\n',
            '让你担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A726',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360009V#021F我们这里还好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360010V#524F但是卢安这边\n',
            '似乎状况相当严峻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A783')

    def _loc_A726(): pass

    label('loc_A726')

    ChrTalk(
        0x0102,
        (
            '#0020360011V#1040F我们这里还算好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360012V#1043F但是卢安地区的\n',
            '状况好像很严峻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A783(): pass

    label('loc_A783')

    ChrTalk(
        0x0008,
        (
            '#0500360013V#654F#5P啊啊……\n',
            '真是相当混乱的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360014V那个贝壳样的巨大物体\n',
            '一在湖上面出现，\n',
            '全部的导力器就不能动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360015V#652F就算是新市长诺曼，\n',
            '终究也是难以应付啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360016V说实话，要是没有渡鸦帮成员\n',
            '和七耀教会的人的话，\n',
            '市内必然已经陷入恐慌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A93C',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇知道渡鸦帮改邪归正的事】\n'),
            TXT(0x01, '【◇不知道渡鸦帮改邪归正的事】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_A930'),
        (0x00000001, 'loc_A936'),
        (-1, 'loc_A93C'),
    )

    def _loc_A930(): pass

    label('loc_A930')

    OP_A2(0x2080)

    Jump('loc_A93C')

    def _loc_A936(): pass

    label('loc_A936')

    OP_A3(0x2080)

    Jump('loc_A93C')

    def _loc_A93C(): pass

    label('loc_A93C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 0, 0x2080)),
            Expr.Return,
        ),
        'loc_AA2B',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A9D8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360017V#1008F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360018V渡鸦帮的成员\n',
            '似乎真的很努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360019V#051F嘿……\n',
            '稍微对他们有点改观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AA28')

    def _loc_A9D8(): pass

    label('loc_A9D8')

    ChrTalk(
        0x0101,
        (
            '#0010360017V#1008F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360018V渡鸦帮的成员\n',
            '似乎真的很努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AA28(): pass

    label('loc_AA28')

    Jump('loc_AC08')

    def _loc_AA2B(): pass

    label('loc_AA2B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA91',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360022V#1019F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360023V#055F渡鸦帮的人～？\n',
            '……你说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AADB')

    def _loc_AA91(): pass

    label('loc_AA91')

    ChrTalk(
        0x0101,
        (
            '#0010360024V#1004F#6P咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360025V#1015F渡鸦帮的成员\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AADB(): pass

    label('loc_AADB')

    ChrTalk(
        0x0008,
        (
            '#0500360026V#650F#5P导力停止现象发生之后，\n',
            '快要发生恐慌的时候\n',
            '是他们带头帮忙阻止了混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360027V#651F现在也举全帮之力\n',
            '协助协会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2080)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABD4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360028V#555F真的假的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360029V#1006F#6P是吗……\n',
            '终于有干劲了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AC08')

    def _loc_ABD4(): pass

    label('loc_ABD4')

    ChrTalk(
        0x0101,
        (
            '#0010360029V#1006F#6P是吗……\n',
            '终于有干劲了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC08(): pass

    label('loc_AC08')

    ChrTalk(
        0x0008,
        (
            '#0500360031V#654F#5P还有一件更麻烦的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360032V#652F真是巧合，偏偏\n',
            '是在吊桥抬起的时候\n',
            '发生了那个非常事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360033V结果现在只能靠手划的小船\n',
            '在街区间往返了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AD82',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇从南街区来的】\n'),
            TXT(0x01, '【◇从北街区来的&看到了小船】\n'),
            TXT(0x02, '【◇从北街区来的&没看到小船】\n'),
            TXT(0x03, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_AD67'),
        (0x00000001, 'loc_AD70'),
        (0x00000002, 'loc_AD79'),
        (-1, 'loc_AD82'),
    )

    def _loc_AD67(): pass

    label('loc_AD67')

    OP_A2(0x2035)
    OP_A2(0x2036)

    Jump('loc_AD82')

    def _loc_AD70(): pass

    label('loc_AD70')

    OP_A2(0x2035)
    OP_A3(0x2036)

    Jump('loc_AD82')

    def _loc_AD79(): pass

    label('loc_AD79')

    OP_A3(0x2035)
    OP_A3(0x2036)

    Jump('loc_AD82')

    def _loc_AD82(): pass

    label('loc_AD82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Return,
        ),
        'loc_ADF7',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360034V#1015F#6P嗯，我们\n',
            '也是乘那个过来这边的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360035V#1007F等待的时间\n',
            '可真是够长的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9F')

    def _loc_ADF7(): pass

    label('loc_ADF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 5, 0x2035)),
            Expr.Return,
        ),
        'loc_AE5D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360036V#1015F#6P嗯，来这里之前\n',
            '看到了小船的渡口……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360037V好像要等很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9F')

    def _loc_AE5D(): pass

    label('loc_AE5D')

    ChrTalk(
        0x0101,
        (
            '#0010360038V#1015F#6P这样啊……\n',
            '的确没有除此以外的方法了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE9F(): pass

    label('loc_AE9F')

    ChrTalk(
        0x0008,
        (
            '#0500360039V#652F#5P不过，总不能\n',
            '一直保持这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360040V很想和各地的支部以及王国军配合\n',
            '确定相应的对策……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360041V#654F但通信器也不能用，\n',
            '联络无法进行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360042V#1006F#6P放心吧，嘉恩哥哥！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360043V我们带好东西\n',
            '来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500360044V#653F#5P好东西……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360045V#1040F是的，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人向嘉恩说明了\n',
            '『浮游都市』出现的缘由，以及\n',
            '关于『零力场发生器』的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0500360046V#652F#5P是吗……\n',
            '那个巨大的物体\n',
            '果然是『结社』干的好事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360047V#650F不过，通信器能够使用\n',
            '可真是帮大忙了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360048V#651F赶快进行设置吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B240',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360049V#560F好，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0009)
    SetChrPos(0x0107, -6250, 0, 46860, 270)
    ChrTurnDirection(0x0008, 0x0107, 0)
    ChrTurnDirection(0x0101, 0x0107, 0)
    ChrTurnDirection(0x0102, 0x0107, 0)
    ChrTurnDirection(0x00F8, 0x0107, 0)
    ChrTurnDirection(0x00F9, 0x0107, 0)
    OP_6D(-6670, 0, 46850, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(315000, 0)
    OP_6E(321, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070360050V#061F……嗯，这样就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_B36A')

    def _loc_B240(): pass

    label('loc_B240')

    ChrTalk(
        0x0102,
        (
            '#0020360051V#1040F好的，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x0009)
    SetChrPos(0x0102, -6250, 0, 46860, 270)
    ChrTurnDirection(0x0008, 0x0102, 0)
    ChrTurnDirection(0x0101, 0x0102, 0)
    ChrTurnDirection(0x00F8, 0x0102, 0)
    ChrTurnDirection(0x00F9, 0x0102, 0)
    OP_6D(-6670, 0, 46850, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(315000, 0)
    OP_6E(321, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360052V#1035F……这样就设置完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_B36A(): pass

    label('loc_B36A')

    Sleep(500)

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_22(0x0083, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0500360053V#653F#6P喔喔～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B490',
    )

    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070360054V#560F#2P这下这个通信器\n',
            '应该能够使用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350438V不过，如果对方的通讯器没修好\n',
            '还是不能发送的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B50E')

    def _loc_B490(): pass

    label('loc_B490')

    OP_8C(0x0102, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020360056V#1040F#2P这下通信器\n',
            '能够使用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350440V但这必须是在对方的通讯器\n',
            '也已经修好，可以使用的前提下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B50E(): pass

    label('loc_B50E')

    ChrTalk(
        0x0008,
        (
            '#0500360058V#656F#6P呀～话说回来真是帮大忙了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360059V这个状况下，能恢复联络\n',
            '真是太好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360060V#651F真想给拉赛尔博士和你们\n',
            '感谢之吻啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B62B',
    )

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070360061V#067F啊，啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360062V#1016F#6P啊哈哈……\n',
            '心领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B660')

    def _loc_B62B(): pass

    label('loc_B62B')

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360062V#1016F#6P啊哈哈……\n',
            '心领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B660(): pass

    label('loc_B660')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B6FE',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇恢复全部的通讯器】\n'),
            TXT(0x01, '【◇只恢复这里的通讯器】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B6EC'),
        (0x00000001, 'loc_B6F5'),
        (-1, 'loc_B6FE'),
    )

    def _loc_B6EC(): pass

    label('loc_B6EC')

    OP_A2(0x2003)
    OP_A2(0x2005)

    Jump('loc_B6FE')

    def _loc_B6F5(): pass

    label('loc_B6F5')

    OP_A3(0x2003)
    OP_A3(0x2005)

    Jump('loc_B6FE')

    def _loc_B6FE(): pass

    label('loc_B6FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BAC7',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B7BD',
    )

    ChrTurnDirection(0x0108, 0x0008, 400)

    @scena.Lambda('lambda_B724')
    def lambda_B724():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B724)

    Sleep(100)

    @scena.Lambda('lambda_B737')
    def lambda_B737():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B737)

    ChrTalk(
        0x0108,
        (
            '#0080350448V#070F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350449V那么，配合各地的状况\n',
            '进行执行任务的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B922')

    def _loc_B7BD(): pass

    label('loc_B7BD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B871',
    )

    ChrTurnDirection(0x0103, 0x0008, 400)

    @scena.Lambda('lambda_B7D8')
    def lambda_B7D8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B7D8)

    Sleep(100)

    @scena.Lambda('lambda_B7EB')
    def lambda_B7EB():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B7EB)

    ChrTalk(
        0x0103,
        (
            '#0030350450V#020F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350451V那么，结合各地的状况\n',
            '一起进行任务的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B922')

    def _loc_B871(): pass

    label('loc_B871')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B922',
    )

    ChrTurnDirection(0x0106, 0x0008, 400)

    @scena.Lambda('lambda_B88C')
    def lambda_B88C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B88C)

    Sleep(100)

    @scena.Lambda('lambda_B89F')
    def lambda_B89F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B89F)

    ChrTalk(
        0x0106,
        (
            '#0050350452V#051F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350453V那么，结合各地的状况\n',
            '一起进行任务的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B922(): pass

    label('loc_B922')

    OP_59()
    OP_28(0x009B, 0x04, 0x10)
    OP_AF(0x67, 0x009B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x009B, 0x01, 0x0100)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B9A9',
    )

    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360070V#651F#5P呀～真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360071V这下终于\n',
            '可以迅速应对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA03')

    def _loc_B9A9(): pass

    label('loc_B9A9')

    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360072V#651F#5P各位，真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360073V这下终于\n',
            '可以迅速应对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA03(): pass

    label('loc_BA03')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA45',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350458V#070F还有其它什么事要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BAC4')

    def _loc_BA45(): pass

    label('loc_BA45')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA8B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350459V#020F是否还有其它什么事要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BAC4')

    def _loc_BA8B(): pass

    label('loc_BA8B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BAC4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350460V#051F还有什么要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BAC4(): pass

    label('loc_BAC4')

    Jump('loc_BCC7')

    def _loc_BAC7(): pass

    label('loc_BAC7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BB72',
    )

    ChrTurnDirection(0x0108, 0x0008, 400)

    @scena.Lambda('lambda_BAE2')
    def lambda_BAE2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BAE2)

    Sleep(100)

    @scena.Lambda('lambda_BAF5')
    def lambda_BAF5():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BAF5)

    ChrTalk(
        0x0108,
        (
            '#0080350461V#070F#4P嗯，准备继续去把\n',
            '其它协会的通讯器也修好，\n',
            '不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350462V这边还有什么要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCC7')

    def _loc_BB72(): pass

    label('loc_BB72')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BC1D',
    )

    ChrTurnDirection(0x0103, 0x0008, 400)

    @scena.Lambda('lambda_BB8D')
    def lambda_BB8D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BB8D)

    Sleep(100)

    @scena.Lambda('lambda_BBA0')
    def lambda_BBA0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BBA0)

    ChrTalk(
        0x0103,
        (
            '#0030350465V#020F#4P嗯，准备继续去把\n',
            '其它协会的通讯器也修好，\n',
            '不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350466V这边还有要帮忙的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCC7')

    def _loc_BC1D(): pass

    label('loc_BC1D')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BCC7',
    )

    ChrTurnDirection(0x0106, 0x0008, 400)

    @scena.Lambda('lambda_BC38')
    def lambda_BC38():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BC38)

    Sleep(100)

    @scena.Lambda('lambda_BC4B')
    def lambda_BC4B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BC4B)

    ChrTalk(
        0x0106,
        (
            '#0050350463V#051F#4P嗯，准备继续去把\n',
            '其它协会的通讯器也修好，\n',
            '不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350464V这边没有要帮忙的事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCC7(): pass

    label('loc_BCC7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD93',
    )

    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360083V#655F#5P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360084V#650F有空的话请\n',
            '检查一下留言板上的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360085V另外，可以的话，请去确认一下\n',
            '卢安近郊中有市民居住的场所，\n',
            '那就帮了大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE52')

    def _loc_BD93(): pass

    label('loc_BD93')

    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360086V#655F#5P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360087V#650F有空的话请\n',
            '检查一下留言板上的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360088V另外，可以的话，请去确认一下\n',
            '卢安近郊中有市民居住的场所，\n',
            '那就算是帮了大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE52(): pass

    label('loc_BE52')

    ChrTalk(
        0x0101,
        (
            '#0010360089V#1015F#6P的确，在这种状况下\n',
            '也有必要进行巡逻的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360090V#1040F尽量小心地\n',
            '四处转转吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500360091V#651F#5P啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※因为通讯器已经修好了，可以呼叫在其他支部待命的同伴，\n',
            '  将他们召集来卢安支部。\n',
            '　想呼叫的时候请在接待处选择『呼叫同伴』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_4B(0x0008, 255)
    OP_A2(0x2001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BF9C',
    )

    OP_A2(0x2091)

    Jump('loc_BF9F')

    def _loc_BF9C(): pass

    label('loc_BF9C')

    OP_A3(0x2091)

    def _loc_BF9F(): pass

    label('loc_BF9F')

    OP_28(0x009B, 0x02, 0x0004)
    OP_28(0x009B, 0x01, 0x0008)
    OP_6D(-2150, 0, 43020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -2150, 0, 43020, 135)
    SetChrPos(0x0001, -2150, 0, 43020, 135)
    SetChrPos(0x0002, -2150, 0, 43020, 135)
    SetChrPos(0x0003, -2150, 0, 43020, 135)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0xC03D
@scena.Code('func_14_C03D')
def func_14_C03D():
    OP_8E(0x00FE, -3540, 0, 44200, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0015 offset: 0xC059
@scena.Code('func_15_C059')
def func_15_C059():
    OP_8E(0x00FE, -3540, 0, 45300, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0016 offset: 0xC075
@scena.Code('func_16_C075')
def func_16_C075():
    OP_8E(0x00FE, -2400, 0, 44200, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0017 offset: 0xC091
@scena.Code('func_17_C091')
def func_17_C091():
    OP_8E(0x00FE, -1930, 0, 43660, 2500, 0x00)
    OP_8E(0x00FE, -2400, 0, 45300, 2500, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0018 offset: 0xC0C1
@scena.Code('func_18_C0C1')
def func_18_C0C1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 2, 0x2002)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 4, 0x2004)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 6, 0x2006)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C0DB',
    )

    Return()

    def _loc_C0DB(): pass

    label('loc_C0DB')

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
        'loc_C0FB',
    )

    Call(0, 0x001D)
    Call(0, 0x001E)
    FadeIn(0, 0)

    def _loc_C0FB(): pass

    label('loc_C0FB')

    OP_22(0x00C3, 0x01, 0x64)
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0101,
        (
            '#0010260612V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C185')
    def lambda_C185():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_C185)

    @scena.Lambda('lambda_C193')
    def lambda_C193():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_C193)

    Sleep(100)

    @scena.Lambda('lambda_C1A6')
    def lambda_C1A6():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_C1A6)

    OP_8C(0x0003, 315, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360149V#653F#6P喔，这么快就\n',
            '来联络了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(-6390, 0, 46350, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(315000, 0)
    OP_6E(313, 0)
    SetChrPos(0x0101, -550, 0, 39990, 315)
    SetChrPos(0x0102, 80, 0, 40550, 315)
    SetChrPos(0x00F8, 180, 0, 39140, 315)
    SetChrPos(0x00F9, 840, 0, 39800, 315)
    OP_8E(0x0008, -6250, 0, 46860, 2000, 0x00)
    OP_8C(0x0008, 270, 400)
    Sleep(700)

    OP_23(0x00C3)
    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x00, 0x00)
    PlayEffect(0x01, 0x01, 0x00FF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0001)
    CreateThread(0x0102, 0x01, 0x00, 0x0015)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x0014)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x0017)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0016)

    ChrTalk(
        0x0008,
        (
            '#0500360150V#652F#4P是，这里是游击士协会\n',
            '卢安支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360151V#650F……啊啊，是你啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360152V#651F呀～这边也\n',
            '正想联络你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360153V啊，就在刚才\n',
            '通信器修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360154V#653F……艾丝蒂尔他们吗？\n',
            '他们现在就在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_C402')
    def lambda_C402():
        OP_6D(-5690, 0, 46380, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C402)

    @scena.Lambda('lambda_C41A')
    def lambda_C41A():
        OP_67(0, 6020, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C41A)

    OP_6E(330, 1200)

    ChrTalk(
        0x0101,
        (
            '#0010360155V#1004F#6P（找我们的……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360156V#1044F（好像有话要说呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500360157V#652F#4P……嗯……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360158V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360159V#650F啊啊，明白了。\n',
            '我会转达给他们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360160V关于这边的状况\n',
            '整理好了再联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360161V#651F……啊啊，彼此都加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C5BB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360162V#052F#4P嘉恩。\n',
            '是哪里来的联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5F1')

    def _loc_C5BB(): pass

    label('loc_C5BB')

    ChrTalk(
        0x0101,
        (
            '#0010360163V#1015F#6P嘉恩哥哥。\n',
            '是哪里来的联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5F1(): pass

    label('loc_C5F1')

    OP_8E(0x0008, -5700, 0, 45100, 2000, 0x00)
    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0500360164V#650F#5P是王都支部的艾南。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360165V好像是女王陛下\n',
            '有话要对你们说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360166V让我转告你们，等到\n',
            '路过格兰赛尔时，\n',
            '能不能来王城一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360167V#1004F#6P女王陛下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C71E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350505V#052F#4P这真令人吃惊……\n',
            '到底有什么事呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7BD')

    def _loc_C71E(): pass

    label('loc_C71E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C770',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350507V#023F#4P这真令人吃惊呢……\n',
            '究竟有什么事情呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7BD')

    def _loc_C770(): pass

    label('loc_C770')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C7BD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350506V#073F#4P这真令人吃惊啊。\n',
            '究竟有什么事情呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7BD(): pass

    label('loc_C7BD')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_C82E',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360171V#656F#5P虽然没仔细问……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360172V但好像是通信\n',
            '难以传达的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C891')

    def _loc_C82E(): pass

    label('loc_C82E')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C891',
    )

    ChrTalk(
        0x0008,
        (
            '#0500360173V#656F#5P虽然没仔细问……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360174V但好像是通信\n',
            '难以传达的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C891(): pass

    label('loc_C891')

    ChrTalk(
        0x0101,
        (
            '#0010360175V#1015F#6P不能在通讯中传达……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350513V#1026F是吗，导力通讯\n',
            '存在被人监听的危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360177V#1042F看来是有什么\n',
            '比较机密的话要说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0500360178V#650F#5P不过，好像没说一定\n',
            '要马上过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0500360134V就等路过王都的时候，\n',
            '顺便过去就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360180V#1006F#6P这样啊……知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA06',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360181V#051F#4P有空就去一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA30')

    def _loc_CA06(): pass

    label('loc_CA06')

    ChrTalk(
        0x0102,
        (
            '#0020360182V#1040F有空就去一趟看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA30(): pass

    label('loc_CA30')

    OP_A2(0x2002)
    OP_28(0x009B, 0x01, 0x0200)
    OP_28(0x009B, 0x01, 0x0400)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)
    OP_6D(-2150, 0, 43020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -2150, 0, 43020, 135)
    SetChrPos(0x0001, -2150, 0, 43020, 135)
    SetChrPos(0x0002, -2150, 0, 43020, 135)
    SetChrPos(0x0003, -2150, 0, 43020, 135)
    OP_69(0x0000, 0x00000000)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0xCAF7
@scena.Code('func_19_CAF7')
def func_19_CAF7():
    OP_8E(0x00FE, -3540, 0, 44590, 2000, 0x00)

    @scena.Lambda('lambda_CB11')
    def lambda_CB11():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_CB11')

    DispatchAsync2(0x00FE, 0x0002, lambda_CB11)

    Return()

# id: 0x001A offset: 0xCB1D
@scena.Code('func_1A_CB1D')
def func_1A_CB1D():
    OP_8E(0x00FE, -3540, 0, 45310, 2000, 0x00)

    @scena.Lambda('lambda_CB37')
    def lambda_CB37():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_CB37')

    DispatchAsync2(0x00FE, 0x0002, lambda_CB37)

    Return()

# id: 0x001B offset: 0xCB43
@scena.Code('func_1B_CB43')
def func_1B_CB43():
    OP_8E(0x00FE, -3550, 0, 43830, 2000, 0x00)

    @scena.Lambda('lambda_CB5D')
    def lambda_CB5D():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_CB5D')

    DispatchAsync2(0x00FE, 0x0002, lambda_CB5D)

    Return()

# id: 0x001C offset: 0xCB69
@scena.Code('func_1C_CB69')
def func_1C_CB69():
    OP_8E(0x00FE, -1930, 0, 43660, 2000, 0x00)
    OP_8E(0x00FE, -2850, 0, 46040, 2000, 0x00)
    OP_8E(0x00FE, -3540, 0, 46050, 2000, 0x00)

    @scena.Lambda('lambda_CBAB')
    def lambda_CBAB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_CBAB')

    DispatchAsync2(0x00FE, 0x0002, lambda_CBAB)

    Return()

# id: 0x001D offset: 0xCBB7
@scena.Code('func_1D_CBB7')
def func_1D_CBB7():
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
        (0x00000000, 'loc_CC31'),
        (0x00000001, 'loc_CC37'),
        (-1, 'loc_CC3D'),
    )

    def _loc_CC31(): pass

    label('loc_CC31')

    OP_A2(0x1200)

    Jump('loc_CC3D')

    def _loc_CC37(): pass

    label('loc_CC37')

    OP_A2(0x1201)

    Jump('loc_CC3D')

    def _loc_CC3D(): pass

    label('loc_CC3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_CC4B',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_CC4F')

    def _loc_CC4B(): pass

    label('loc_CC4B')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_CC4F(): pass

    label('loc_CC4F')

    Return()

# id: 0x001E offset: 0xCC50
@scena.Code('func_1E_CC50')
def func_1E_CC50():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
