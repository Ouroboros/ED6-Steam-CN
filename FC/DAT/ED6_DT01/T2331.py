import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2331_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2331   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雷克斯'),
    TXT(0x02, '卡拉'),
    TXT(0x03, '特蕾莎院长'),
    TXT(0x04, '达尼艾尔'),
    TXT(0x05, '玛丽'),
    TXT(0x06, '波利'),
    TXT(0x07, '克拉姆'),
    TXT(0x08, '戴尔蒙市长'),
    TXT(0x09, '秘书基尔巴特'),
    TXT(0x0A, '卡露娜'),
    TXT(0x0B, '阿尔宾'),
    TXT(0x0C, '蔡尔德'),
    TXT(0x0D, '卢希娅'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2331.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x60F6
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT06/CH20093._CH', 'ED6_DT06/CH20093P._CP'),
        ('ED6_DT06/CH20101._CH', 'ED6_DT06/CH20101P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -25500,
            z                   = 0,
            y                   = 43210,
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
            x                   = -37500,
            z                   = 0,
            y                   = 44500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -50190,
            z                   = 0,
            y                   = -1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -50850,
            z                   = 0,
            y                   = 180,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -50850,
            z                   = 0,
            y                   = 1400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -50570,
            z                   = 0,
            y                   = -2840,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -49420,
            z                   = 0,
            y                   = -2280,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
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
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -400,
            z                   = 0,
            y                   = 45400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -33200,
            z                   = 150,
            y                   = 41740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -32060,
            z                   = 150,
            y                   = 42960,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -23900,
            z                   = 0,
            y                   = -1170,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
    )

# id: 0x10003 offset: 0x2DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -37020,
            triggerZ            = 0,
            triggerY            = 42970,
            triggerRange        = 400,
            actorX              = -37500,
            actorZ              = 1500,
            actorY              = 44500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -26870,
            triggerZ            = 0,
            triggerY            = 42820,
            triggerRange        = 400,
            actorX              = -25500,
            actorZ              = 1500,
            actorY              = 43210,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x322
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_389',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -48350, 0, 150, 215)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -50850, 0, 180, 135)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -50570, 0, -2840, 0)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -49420, 0, -2280, 315)

    Jump('loc_59A')

    def _loc_389(): pass

    label('loc_389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_421',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0010)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0011, -53290, 0, 2040, 180)
    SetChrPos(0x000A, -53080, 0, -870, 180)
    SetChrPos(0x000B, -50850, 0, -230, 270)
    SetChrPos(0x000D, -50850, 0, -1430, 270)
    SetChrPos(0x000C, -52530, 0, -2420, 0)
    SetChrPos(0x000E, -50800, 0, 1470, 270)

    Jump('loc_59A')

    def _loc_421(): pass

    label('loc_421')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_506',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0010)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 15)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 15)
    SetChrPos(0x0011, -53000, 0, 2040, 90)
    SetChrPos(0x000A, -53000, 0, -870, 90)
    SetChrChipByIndex(0x000A, 13)
    SetChrChipByIndex(0x0011, 14)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x000A, 0xFF)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x0011, 0x0010)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x0011, 0x0002)
    SetChrFlags(0x000A, 0x0002)
    SetChrPos(0x000B, -50850, 0, -230, 270)
    SetChrPos(0x000D, -50850, 0, -1430, 270)
    SetChrPos(0x000C, -52530, 0, -2420, 0)
    SetChrPos(0x000E, -50800, 0, 1470, 270)
    ClearChrFlags(0x0014, 0x0080)

    Jump('loc_59A')

    def _loc_506(): pass

    label('loc_506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_51A',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0012, 0x0010)

    Jump('loc_59A')

    def _loc_51A(): pass

    label('loc_51A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_56B',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -48450, 0, -990, 270)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -49690, 0, -120, 90)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -47720, 0, 2100, 0)

    Jump('loc_59A')

    def _loc_56B(): pass

    label('loc_56B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_575',
    )

    Jump('loc_59A')

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_57F',
    )

    Jump('loc_59A')

    def _loc_57F(): pass

    label('loc_57F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_589',
    )

    Jump('loc_59A')

    def _loc_589(): pass

    label('loc_589')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_593',
    )

    Jump('loc_59A')

    def _loc_593(): pass

    label('loc_593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_59A',
    )

    def _loc_59A(): pass

    label('loc_59A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006B, 'loc_5A6'),
        (-1, 'loc_5CF'),
    )

    def _loc_5A6(): pass

    label('loc_5A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B9',
    )

    SetScenaFlags(ScenaFlag(0x0085, 0, 0x428))
    Event(0, 0x0010)

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CC',
    )

    SetScenaFlags(ScenaFlag(0x0086, 6, 0x436))
    Event(0, 0x0016)

    def _loc_5CC(): pass

    label('loc_5CC')

    Jump('loc_5CF')

    def _loc_5CF(): pass

    label('loc_5CF')

    Return()

# id: 0x0001 offset: 0x5D0
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x5D1
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5E6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_5E6(): pass

    label('loc_5E6')

    Return()

# id: 0x0003 offset: 0x5E7
@scena.Code('func_03_5E7')
def func_03_5E7():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x5EC
@scena.Code('func_04_5EC')
def func_04_5EC():
    TalkBegin(0x0008)
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
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_64A',
    )

    OP_0D()
    OP_A9(0x2A)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_64A(): pass

    label('loc_64A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65B',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_65B(): pass

    label('loc_65B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DAA',
    )

    EventBegin(0x00)
    OP_69(0x0008, 800)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 1, 0x401)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA6',
    )

    ChrTalk(
        0x0008,
        (
            '#1460040418V欢迎来到『白之木莲亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040419V啊，以前没见过你们。\n',
            '是来玛诺利亚村观光的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040420V#006F不是呢。\n',
            '其实我们正在去卢安市的途中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040421V#010F我们是从柏斯那边\n',
            '越过古罗尼山峰来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040422V越过古罗尼山峰！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040423V哈～没想到现在这个年代\n',
            '还会有人爬那座山峰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040424V你们平时有爬山的爱好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040425V#501F啊……\n',
            '也不算是啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040426V#501F总之，我们走了好久的山路，\n',
            '现在肚子饿得咕咕直叫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040427V#010F这里有什么特别推荐的料理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040428V料理的话……\n',
            '中午特别推荐的就肯定是便当了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040429V#004F便当？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040430V我们村里的风车屋前\n',
            '有个可以看到漂亮海景的瞭望台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040431V每到中午的时候，\n',
            '就有很多客人来这里买便当拿去那里吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040432V#001F啊～好像蛮有趣的嘛⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040433V光是听你这么介绍，\n',
            '我就已经觉得很好吃呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040434V#019F那么我们就买便当吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040435V#010F请问这里的便当有几种呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040436V今天有海鲜焗饭\n',
            '和熏火腿三明治两种。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040437V不管哪一个都非常值得品尝的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040438V#501F嗯～\n',
            '我要熏火腿三明治。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040439V#010F那我要海鲜焗饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040440V多谢惠顾。\n',
            '两款便当合计１２０米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B0C')

    def _loc_AA6(): pass

    label('loc_AA6')

    ChrTalk(
        0x0008,
        (
            '#1460040441V我们这里今天出售\n',
            '海鲜焗饭和熏火腿三明治\n',
            '两种便当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040442V一共是１２０米拉，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B0C(): pass

    label('loc_B0C')

    FadeOut(300, 0, 100)

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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【购买】\n'),
            TXT(0x01, '【还是算了】\n'),
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
        (0x00000000, 'loc_B73'),
        (0x00000001, 'loc_CF9'),
        (-1, 'loc_DA5'),
    )

    def _loc_B73(): pass

    label('loc_B73')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x78),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_CAC',
    )

    ExecExpressionWithVar(
        0x12,
        (
            (Expr.PushLong, 0x78),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '特制午餐盒饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x033C, 1)

    ChrTalk(
        0x0008,
        (
            '#1460040443V另外，作为今天的特别服务，\n',
            '随便当附送香草茶哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040444V这种茶也是本店的推荐饮品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040445V#001F啊～谢谢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040446V#010F那我们现在就去瞭望台吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040447V#006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0082, 3, 0x413))

    Jump('loc_CF6')

    def _loc_CAC(): pass

    label('loc_CAC')

    ChrTalk(
        0x0008,
        (
            '#1460040448V咦……\n',
            '好像没有足够的米拉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040449V攒够了钱再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0080, 1, 0x401))

    def _loc_CF6(): pass

    label('loc_CF6')

    Jump('loc_DA5')

    def _loc_CF9(): pass

    label('loc_CF9')

    ChrTalk(
        0x0008,
        (
            '#1460040450V那么，\n',
            '就在这里用餐怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1460040451V我们还供应很多别的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040452V#007F嗯～\n',
            '我还是想在室外吃便当呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040453V#008F不好意思，我们再考虑一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0080, 1, 0x401))

    Jump('loc_DA5')

    def _loc_DA5(): pass

    label('loc_DA5')

    EventEnd(0x01)

    Jump('loc_12AB')

    def _loc_DAA(): pass

    label('loc_DAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_E47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E17',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '袭击老师他们的犯人\n',
            '终于被抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望他们能够深刻反省，\n',
            '以偿还自己犯下的罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E44')

    def _loc_E17(): pass

    label('loc_E17')

    ChrTalk(
        0x0008,
        (
            '希望被捕的犯人能够深刻反省，\n',
            '好好赎罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E44(): pass

    label('loc_E44')

    Jump('loc_12AB')

    def _loc_E47(): pass

    label('loc_E47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_E7A',
    )

    ChrTalk(
        0x0008,
        (
            '外面已经很暗了。\n',
            '出去的时候要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AB')

    def _loc_E7A(): pass

    label('loc_E7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_F60',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F03',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '马上就要到学园祭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '孤儿院的孩子们\n',
            '好像也要到学院里去玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '能忘记以前的不快，\n',
            '玩得开心就最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F5D')

    def _loc_F03(): pass

    label('loc_F03')

    ChrTalk(
        0x0008,
        (
            '孤儿院的孩子们\n',
            '好像也要到学院里去玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '能忘记以前的不快，\n',
            '玩得开心就最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F5D(): pass

    label('loc_F5D')

    Jump('loc_12AB')

    def _loc_F60(): pass

    label('loc_F60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_FB3',
    )

    ChrTalk(
        0x0008,
        (
            '就在刚才，\n',
            '有个孤儿院的男孩子飞奔出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AB')

    def _loc_FB3(): pass

    label('loc_FB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_107B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1041',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '听说孤儿院\n',
            '被烧得精光？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我马上就去\n',
            '腾出房间给孩子们住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '小姑娘，如果可以的话，\n',
            '请你们鼓励一下那些孩子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1078')

    def _loc_1041(): pass

    label('loc_1041')

    ChrTalk(
        0x0008,
        (
            '小姑娘，如果可以的话，\n',
            '请你们鼓励一下那些孩子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1078(): pass

    label('loc_1078')

    Jump('loc_12AB')

    def _loc_107B(): pass

    label('loc_107B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_10BE',
    )

    ChrTalk(
        0x0008,
        (
            '今天的风很宜人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '沿着海岸散步\n',
            '感觉很舒服哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AB')

    def _loc_10BE(): pass

    label('loc_10BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_11E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1183',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '来这里的游客大多都是\n',
            '这里大部分的游客\n',
            '都是来赏花和观景的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还有就是\n',
            '会零零散散过来的登山客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前的人都是通过这里往来于柏斯和卢安的，\n',
            '所以说村里曾经非常热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E3')

    def _loc_1183(): pass

    label('loc_1183')

    ChrTalk(
        0x0008,
        (
            '从这里望向风车小屋，\n',
            '景色很美丽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个风车小屋和湛蓝的大海\n',
            '搭配起来很是诗情画意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E3(): pass

    label('loc_11E3')

    Jump('loc_12AB')

    def _loc_11E6(): pass

    label('loc_11E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_1271',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1251',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '哦，\n',
            '这不是刚才来过的小姑娘吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '男孩子？\n',
            '没有看到啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126E')

    def _loc_1251(): pass

    label('loc_1251')

    ChrTalk(
        0x0008,
        (
            '男孩子？\n',
            '没有看到啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126E(): pass

    label('loc_126E')

    Jump('loc_12AB')

    def _loc_1271(): pass

    label('loc_1271')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_12AB',
    )

    ChrTalk(
        0x0008,
        (
            '我们村里的风车屋前\n',
            '有一个瞭望台哦。（※假定）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AB(): pass

    label('loc_12AB')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x12AF
@scena.Code('func_05_12AF')
def func_05_12AF():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x12B4
@scena.Code('func_06_12B4')
def func_06_12B4():
    TalkBegin(0x0009)
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
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1310',
    )

    OP_0D()
    OP_A9(0x29)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_1310(): pass

    label('loc_1310')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1321',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_1321(): pass

    label('loc_1321')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1376',
    )

    ChrTalk(
        0x0009,
        (
            '听说犯人被抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '与其交给游击士协会，\n',
            '我们更想亲自来惩罚他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1851')

    def _loc_1376(): pass

    label('loc_1376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_13BF',
    )

    ChrTalk(
        0x0009,
        (
            '怎么会变成这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不可原谅……\n',
            '不可原谅这些犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1851')

    def _loc_13BF(): pass

    label('loc_13BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_146F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_142C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '孤儿院的老师和孩子们\n',
            '就由我们『白之木莲亭』\n',
            '来好好照顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '一人有难大家帮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_146C')

    def _loc_142C(): pass

    label('loc_142C')

    ChrTalk(
        0x0009,
        (
            '孤儿院的老师和孩子们\n',
            '就由我们『白之木莲亭』\n',
            '来好好照顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_146C(): pass

    label('loc_146C')

    Jump('loc_1851')

    def _loc_146F(): pass

    label('loc_146F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_14AC',
    )

    ChrTalk(
        0x0009,
        (
            '刚才克拉姆\n',
            '好像跑出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到底怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1851')

    def _loc_14AC(): pass

    label('loc_14AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_15E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15A2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '啊呀，那件制服是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '难道，\n',
            '你就是科洛丝吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，是的。\n',
            '我就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '孤儿院的孩子们\n',
            '急着想见你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他们应该都\n',
            '还在二楼的大房间里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你快点去见见他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，好、好的。\n',
            '真是麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15DF')

    def _loc_15A2(): pass

    label('loc_15A2')

    ChrTalk(
        0x0009,
        (
            '孤儿院的孩子们\n',
            '急着想见你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你快点去见见他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15DF(): pass

    label('loc_15DF')

    Jump('loc_1851')

    def _loc_15E2(): pass

    label('loc_15E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1680',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1648',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '好，接下来该洗衣服了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今天的天气很不错，\n',
            '晒床单的话应该很快就能干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167D')

    def _loc_1648(): pass

    label('loc_1648')

    ChrTalk(
        0x0009,
        (
            '今天的天气很不错，\n',
            '晒床单的话应该很快就能干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_167D(): pass

    label('loc_167D')

    Jump('loc_1851')

    def _loc_1680(): pass

    label('loc_1680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1745',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1702',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '今年的木莲之花\n',
            '也开始陆陆续续地盛开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里虽然不是什么起眼的村子，\n',
            '但是来赏木莲花的人\n',
            '却不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1742')

    def _loc_1702(): pass

    label('loc_1702')

    ChrTalk(
        0x0009,
        (
            '这里虽然不是什么起眼的村子，\n',
            '但是来赏木莲花的人\n',
            '却不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1742(): pass

    label('loc_1742')

    Jump('loc_1851')

    def _loc_1745(): pass

    label('loc_1745')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_179D',
    )

    ChrTalk(
        0x0009,
        (
            '男孩子？\n',
            '我没见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果是王立学院的女生，\n',
            '那刚才还见到过一个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1851')

    def _loc_179D(): pass

    label('loc_179D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1851',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1824',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '哟，两位客人你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果可以的话，\n',
            '请在我们这里享用午餐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '和丈夫一起经营旅馆，\n',
            '我也渐渐有了信心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1851')

    def _loc_1824(): pass

    label('loc_1824')

    ChrTalk(
        0x0009,
        (
            '如果可以的话，\n',
            '请在我们这里享用午餐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1851(): pass

    label('loc_1851')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1855
@scena.Code('func_07_1855')
def func_07_1855():
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '老师和孩子们\n',
            '由我们日夜轮流来守护。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就安心地\n',
            '去搜查犯人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x18A6
@scena.Code('func_08_18A6')
def func_08_18A6():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '虽然不知道能不能派上用场……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我们打算\n',
            '尽自己所能来帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0009 offset: 0x18F9
@scena.Code('func_09_18F9')
def func_09_18F9():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1B01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0390070175V#750F啊，是你们几个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390930010V我从旅馆的人那里听说了。\n',
            '你们已经把那些犯人抓住了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390070177V总是给你们添麻烦，\n',
            '我该怎么感谢你们才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F您、您这么说，\n',
            '我们会不好意思的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（嗯……现在还是不要\n',
            '　把实情说出来比较好啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070181V#010F……我们还要报告工作情况，\n',
            '所以现在要先回卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070182V犯人们如今在\n',
            '卡露娜小姐的严密监视之下，\n',
            '请你们放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0390070183V#750F嗯，真的非常感谢你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AFE')

    def _loc_1AB8(): pass

    label('loc_1AB8')

    ChrTalk(
        0x00FE,
        (
            '#0390070184V#750F最近我总是给你们添麻烦，\n',
            '我该怎么感谢你们才好呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AFE(): pass

    label('loc_1AFE')

    Jump('loc_1CD0')

    def _loc_1B01(): pass

    label('loc_1B01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1B29',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '特蕾莎院长安静地睡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1CD0')

    def _loc_1B29(): pass

    label('loc_1B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1BC4',
    )

    ChrTalk(
        0x00FE,
        (
            '#0390930008V#750F啊，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050989V这段时间真的帮了我们大忙啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390930009V我们也受到了玛诺利亚村村民的照顾，\n',
            '真是太感谢大家了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD0')

    def _loc_1BC4(): pass

    label('loc_1BC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1CD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C7C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0390930001V#750F我已经听玛丽说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050541V怎么会这样呢……\n',
            '那孩子竟然听到了那件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390930002V求求你们了。\n',
            '请一定要把克拉姆带回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390930003V我一会儿也会赶过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD0')

    def _loc_1C7C(): pass

    label('loc_1C7C')

    ChrTalk(
        0x00FE,
        (
            '#0390930004V#750F求求你们了。\n',
            '请一定要把克拉姆带回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390930005V我一会儿也会赶过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CD0(): pass

    label('loc_1CD0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1CD4
@scena.Code('func_0A_1CD4')
def func_0A_1CD4():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1D3E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0400070165V#770F啊，是姐姐你们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400070166V你们已经把那些家伙抓住了吧？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400070167V真厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D98')

    def _loc_1D3E(): pass

    label('loc_1D3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1D98',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0400061090V#773F约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400061091V我，一定要成为\n',
            '像哥哥一样强的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D98(): pass

    label('loc_1D98')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x1D9C
@scena.Code('func_0B_1D9C')
def func_0B_1D9C():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1DF6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410070173V清早的时候\n',
            '老师终于醒过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410070174V嘿嘿嘿，真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E82')

    def _loc_1DF6(): pass

    label('loc_1DF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1E58',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410061092V大家终于都\n',
            '稍微镇静下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410061093V接下来只要等\n',
            '老师醒过来就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E82')

    def _loc_1E58(): pass

    label('loc_1E58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1E82',
    )

    ChrTalk(
        0x00FE,
        (
            '大姐姐，\n',
            '克拉姆就拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E82(): pass

    label('loc_1E82')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x1E86
@scena.Code('func_0C_1E86')
def func_0C_1E86():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1EBC',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～一旦放心下来，\n',
            '肚子就觉得饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0A')

    def _loc_1EBC(): pass

    label('loc_1EBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1EDF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420061094V呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0A')

    def _loc_1EDF(): pass

    label('loc_1EDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1F0A',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420050546V克拉姆他\n',
            '突然怎么了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F0A(): pass

    label('loc_1F0A')

    TalkEnd(0x000B)

    Return()

# id: 0x000D offset: 0x1F0E
@scena.Code('func_0D_1F0E')
def func_0D_1F0E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1F3D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430070186V哇～\n',
            '老师醒过来了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FAB')

    def _loc_1F3D(): pass

    label('loc_1F3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1F6A',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430061095V老师……不会有事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FAB')

    def _loc_1F6A(): pass

    label('loc_1F6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1FAB',
    )

    ChrTalk(
        0x00FE,
        (
            '克拉姆他啊，\n',
            '在吃布丁的时候\n',
            '不知道又在想些什么事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FAB(): pass

    label('loc_1FAB')

    TalkEnd(0x000D)

    Return()

# id: 0x000E offset: 0x1FAF
@scena.Code('func_0E_1FAF')
def func_0E_1FAF():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2043',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320061361V在事情了结之前，\n',
            '这些属于特蕾莎院长的捐款\n',
            '就先由我来暂代保管吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320061362V这次我一定会保护好的，\n',
            '所以你们就安心出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2064')

    def _loc_2043(): pass

    label('loc_2043')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2064',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡露娜安静地睡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2064(): pass

    label('loc_2064')

    TalkEnd(0x0011)

    Return()

# id: 0x000F offset: 0x2068
@scena.Code('func_0F_2068')
def func_0F_2068():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '卢希娅一定要\n',
            '鼓励大家才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x2092
@scena.Code('func_10_2092')
def func_10_2092():
    EventBegin(0x00)
    CameraMove(-50180, 0, -790, 0)
    CameraSetDistance(2800, 0)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000A, -52390, 0, 510, 90)
    SetChrPos(0x000B, -50850, 0, 180, 315)
    SetChrPos(0x000D, -50850, 0, 1400, 225)
    SetChrPos(0x000C, -50570, 0, -2840, 45)
    SetChrPos(0x000E, -49420, 0, -2280, 225)
    SetChrPos(0x0101, -46270, 0, -1540, 270)
    SetChrPos(0x0102, -46100, 0, -760, 270)
    SetChrPos(0x0136, -47050, 0, -1030, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0136,
        (
            '#0060050290V#043F老师、孩子们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000E, 255)

    @scena.Lambda('lambda_2223')
    def lambda_2223():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2223)

    @scena.Lambda('lambda_2231')
    def lambda_2231():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2231)

    @scena.Lambda('lambda_223F')
    def lambda_223F():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_223F)

    @scena.Lambda('lambda_224D')
    def lambda_224D():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_224D)

    @scena.Lambda('lambda_225B')
    def lambda_225B():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_225B)

    Sleep(400)

    ChrTalk(
        0x000E,
        (
            '#0400050291V#774F啊，科洛丝姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410050292V姐姐来了啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22AD')
    def lambda_22AD():
        CameraMove(-50670, 0, -380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22AD)

    @scena.Lambda('lambda_22C5')
    def lambda_22C5():
        ChrMoveTo(0x00FE, -48730, 0, -370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_22C5)

    Sleep(100)

    @scena.Lambda('lambda_22E5')
    def lambda_22E5():
        ChrWalkTo(0x00FE, -49710, 0, 540, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_22E5)

    Sleep(100)

    @scena.Lambda('lambda_2305')
    def lambda_2305():
        ChrWalkTo(0x00FE, -49830, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2305)

    @scena.Lambda('lambda_2320')
    def lambda_2320():
        ChrWalkTo(0x00FE, -49200, 0, -1200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2320)

    Sleep(100)

    @scena.Lambda('lambda_2340')
    def lambda_2340():
        ChrWalkTo(0x00FE, -48350, 0, -1070, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2340)

    WaitForThreadExit(0x000E, 0x0002)
    ChrTurnDirection(0x000E, 0x0136, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050293V#042F#2P大家……\n',
            '都没受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0420050294V#1P嗯，没事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '嘿嘿。\n',
            '波利也没事～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050296V#048F#2P太好了……\n',
            '真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000A, 0x0004)
    ChrWalkTo(0x000A, -50870, 0, 180, 2000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0390050297V#750F呵呵……\n',
            '你能来真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050298V#751F艾丝蒂尔和约修亚\n',
            '也一起来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2465')
    def lambda_2465():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2465')

    DispatchAsync2(0x000A, 0x0001, lambda_2465)

    @scena.Lambda('lambda_2476')
    def lambda_2476():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_2476')

    DispatchAsync2(0x000B, 0x0001, lambda_2476)

    @scena.Lambda('lambda_2487')
    def lambda_2487():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_2487')

    DispatchAsync2(0x000D, 0x0001, lambda_2487)

    @scena.Lambda('lambda_2498')
    def lambda_2498():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_2498')

    DispatchAsync2(0x000C, 0x0001, lambda_2498)

    @scena.Lambda('lambda_24A9')
    def lambda_24A9():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_24A9')

    DispatchAsync2(0x000E, 0x0001, lambda_24A9)

    @scena.Lambda('lambda_24BA')
    def lambda_24BA():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_24BA')

    DispatchAsync2(0x0136, 0x0001, lambda_24BA)

    @scena.Lambda('lambda_24CB')
    def lambda_24CB():
        ChrWalkTo(0x00FE, -48860, 0, -2920, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_24CB)

    Sleep(500)

    @scena.Lambda('lambda_24EB')
    def lambda_24EB():
        ChrWalkTo(0x00FE, -48100, 0, -2570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_24EB)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_250B')
    def lambda_250B():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_250B)

    WaitForThreadExit(0x0102, 0x0002)

    @scena.Lambda('lambda_251E')
    def lambda_251E():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_251E)

    Sleep(500)

    TerminateThread(0x000A, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010050299V#000F嗯……\n',
            '有人通知了游击士协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050300V#010F我们是来调查的，\n',
            '顺便和科洛丝一起来看望你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050301V#750F是吗……\n',
            '谢谢你们的关心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050302V#772F#2P你说来调查……\n',
            '是来调查昨天的火灾吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050303V发现什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050304V#003F这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050305V#013F该怎么说好呢……',
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
            '艾丝蒂尔和约修亚\n',
            '为难地互相交换了一下眼神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrTurnDirection(0x0136, 0x0101, 400)
    OP_62(0x0136, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0136)
    TerminateThread(0x0136, 0xFF)
    ChrTurnDirection(0x0136, 0x000B, 400)
    Sleep(200)

    ChrTurnDirection(0x0136, 0x0102, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050306V#040F好了，孩子们。\n',
            '大家的肚子都饿了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050307V我还没有吃早饭呢，\n',
            '正准备到下面食堂吃点东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050308V#041F所以呢，\n',
            '今天就请大家吃点好东西好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2782')
    def lambda_2782():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_2782')

    DispatchAsync2(0x0101, 0x0001, lambda_2782)

    @scena.Lambda('lambda_2793')
    def lambda_2793():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_2793')

    DispatchAsync2(0x0102, 0x0001, lambda_2793)

    Sleep(50)

    @scena.Lambda('lambda_27A9')
    def lambda_27A9():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_27A9')

    DispatchAsync2(0x000A, 0x0001, lambda_27A9)

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    Sleep(50)

    @scena.Lambda('lambda_27CF')
    def lambda_27CF():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_27CF)

    @scena.Lambda('lambda_27DD')
    def lambda_27DD():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_27DD)

    Sleep(50)

    @scena.Lambda('lambda_27F0')
    def lambda_27F0():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_27F0)

    @scena.Lambda('lambda_27FE')
    def lambda_27FE():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_27FE)

    ChrTalk(
        0x000B,
        (
            '#0420050309V#1P哎？真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '波利要吃布丁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#773F#3P可、可是姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410050312V#1P…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000E, 400)

    ChrTalk(
        0x000C,
        (
            '#0410050313V#1P走吧，克拉姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000C, 400)

    ChrTalk(
        0x000E,
        (
            '#774F#4P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410050315V#1P别啰嗦了，\n',
            '快点过来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410050316V#1P科洛丝姐姐，\n',
            '我们快点下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050317V#048F呵呵，好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0136, 0x02, 0x00, 0x0011)
    CreateThread(0x000E, 0x02, 0x00, 0x0012)
    CreateThread(0x000C, 0x02, 0x00, 0x0013)
    CreateThread(0x000B, 0x02, 0x00, 0x0014)
    CreateThread(0x000D, 0x02, 0x00, 0x0015)

    @scena.Lambda('lambda_294B')
    def lambda_294B():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_294B)

    Sleep(600)

    @scena.Lambda('lambda_296B')
    def lambda_296B():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_296B)

    Sleep(50)

    @scena.Lambda('lambda_298B')
    def lambda_298B():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_298B)

    Sleep(200)

    @scena.Lambda('lambda_29AB')
    def lambda_29AB():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_29AB)

    Sleep(300)

    @scena.Lambda('lambda_29CB')
    def lambda_29CB():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_29CB)

    WaitForThreadExit(0x0136, 0x0001)
    SetChrFlags(0x0136, 0x0080)
    WaitForThreadExit(0x000E, 0x0001)
    SetChrFlags(0x000E, 0x0080)
    WaitForThreadExit(0x000C, 0x0001)
    SetChrFlags(0x000C, 0x0080)
    WaitForThreadExit(0x000B, 0x0001)
    SetChrFlags(0x000B, 0x0080)
    WaitForThreadExit(0x000D, 0x0001)
    SetChrFlags(0x000D, 0x0080)
    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x000A, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010050318V#007F呼……还好没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050319V调查的事还是不要\n',
            '让孩子们知道好一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F#4P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050321V#010F不过，那个叫玛丽的孩子\n',
            '似乎已经察觉到我们的意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050322V#751F呵呵，有这样懂事的孩子，\n',
            '我自己也觉得很欣慰啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0390050323V#750F对了，\n',
            '你们刚才说是来调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050324V想知道些什么，请随便问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 0)
    Sleep(100)

    ChrTurnDirection(0x0102, 0x000A, 0)

    ChrTalk(
        0x0102,
        (
            '#012F#4P多谢您的配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050326V#002F嗯，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0101, -49200, 0, -1200, 0)
    SetChrPos(0x0102, -50100, 0, -990, 45)
    SetChrPos(0x000A, -49670, 0, 200, 180)
    CameraMove(-50810, 0, 340, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020050327V首先，根据我们在火灾现场\n',
            '调查得到的结果来看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050328V这次火灾并不是意外， \n',
            '人为纵火的可能性极高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050329V#754F#2P是吗……果然啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050330V我也觉得着火的时候\n',
            '屋外的情况确实有点古怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050331V#012F我们想问问您……\n',
            '您觉得有什么可疑的人物吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050332V也就是说， \n',
            '谁会有做这种事的动机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050333V#757F#2P……我不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050334V我们几乎没有什么钱财，\n',
            '印象中也完全没和别人结怨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050335V#002F也就是说，\n',
            '犯人的动机既不是抢劫也不是报复吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050336V#012F这样的话，虽然很不愿相信，\n',
            '但有可能是纯粹的恶作剧犯罪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050337V事件发生前后，\n',
            '有什么不寻常的事情吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050338V比如说有没有\n',
            '陌生人在孤儿院附近晃荡……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050339V#756F#2P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050340V除了白天见到了你们之外，\n',
            '就没有什么特别的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050341V#757F……也应该跟那个人无关的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050342V#002F那个人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050343V#754F#2P在我们将要逃出\n',
            '被大火包围的屋子的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050344V天花板上的梁柱突然掉了下来，\n',
            '挡住了通往门口的路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050345V#750F但就在那个时候，\n',
            '有人打破了门，冲了进来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050346V那个人挪开了梁柱，\n',
            '把我和孩子们救了出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050347V#004F还、还有这么一回事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050348V那人是玛诺利亚的村民吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390930006V#756F#2P那个人把我们救出来之后，\n',
            '说去村子里叫人过来，\n',
            '连名字都没有留下就离开了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050350V我问了玛诺利亚的村民，\n',
            '不过似乎没人知道那个人是谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050351V#012F……这有点可疑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050352V半夜三更出现在孤儿院附近，\n',
            '怎么想也有点太过蹊跷了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050353V那是个什么样的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390930007V#750F#2P是个穿着象牙色外套，\n',
            '不到３０岁的青年男子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050355V而且，还有一头耀眼的银发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050356V#014F银发……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050357V#750F#2P嗯，虽然看样子还很年轻，\n',
            '但那深邃的眼神让人感到他饱经沧桑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050358V看起来不像是坏人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050359V#000F虽然感觉不是普通人，\n',
            '但他救了人这点的确是事实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050360V听起来不像是犯人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050361V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 300)

    ChrTalk(
        0x0101,
        (
            '#002F#4P约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050363V怎么了，为什么发起呆来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 200)

    ChrTalk(
        0x0102,
        (
            '#0020050364V#013F#1P没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050365V你们说得也对， \n',
            '也许是哪里过来的游击士也说不定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050366V#015F总之这个人的事\n',
            '还是先别下定论的好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F#4P啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(16, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0136,
        (
            '#0060050368V#1P……打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(15, 0x00, 0x64)
    Sleep(500)

    ChrTurnDirection(0x0136, 0x000A, 0)
    ClearChrFlags(0x0136, 0x0080)

    @scena.Lambda('lambda_3422')
    def lambda_3422():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3422)

    @scena.Lambda('lambda_3430')
    def lambda_3430():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3430)

    @scena.Lambda('lambda_343E')
    def lambda_343E():
        CameraMove(-49000, 0, -520, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_343E)

    @scena.Lambda('lambda_3456')
    def lambda_3456():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0136, 0x0003, lambda_3456)

    ChrWalkTo(0x0136, -47080, 0, -850, 2000, 0x00)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010050369V#000F啊，科洛丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050370V#010F那些孩子怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050371V#041F呵呵……\n',
            '大家都在下面吃蛋糕呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050372V#040F对了，老师。\n',
            '有两位客人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050373V#753F客人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000F, -44560, 0, -1000, 0)
    SetChrPos(0x0010, -44420, 0, -1440, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x000F, 0x000A, 0)

    NpcTalk(
        0x000F,
        '男性的声音',
        (
            '#0490050374V#1P打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0136, -47950, 0, -1840, 2000, 0x00)

    @scena.Lambda('lambda_35AD')
    def lambda_35AD():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_35AD')

    DispatchAsync2(0x0136, 0x0001, lambda_35AD)

    @scena.Lambda('lambda_35BE')
    def lambda_35BE():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_35BE')

    DispatchAsync2(0x0101, 0x0001, lambda_35BE)

    @scena.Lambda('lambda_35CF')
    def lambda_35CF():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_35CF')

    DispatchAsync2(0x0102, 0x0001, lambda_35CF)

    @scena.Lambda('lambda_35E0')
    def lambda_35E0():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_35E0')

    DispatchAsync2(0x000A, 0x0001, lambda_35E0)

    ClearChrFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_35F6')
    def lambda_35F6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_35F6)

    @scena.Lambda('lambda_3608')
    def lambda_3608():
        ChrWalkTo(0x00FE, -46810, 0, -650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3608)

    Sleep(500)

    ClearChrFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_362D')
    def lambda_362D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_362D)

    @scena.Lambda('lambda_363F')
    def lambda_363F():
        ChrWalkTo(0x00FE, -45610, 0, -1440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_363F)

    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010050375V#004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050376V#014F戴尔蒙市长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050377V#660F#2P啊，昨天碰到的\n',
            '两位游击士也在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050378V不愧是嘉恩，\n',
            '这么快就安排人手过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050379V#664F对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3713')
    def lambda_3713():
        ChrWalkTo(0x00FE, -48070, 0, 250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3713)

    Sleep(500)

    @scena.Lambda('lambda_3733')
    def lambda_3733():
        ChrWalkTo(0x00FE, -47210, 0, -920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3733)

    WaitForThreadExit(0x000F, 0x0001)
    ChrTurnDirection(0x000F, 0x000A, 400)
    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#0490050380V#660F#4P好久不见了，特蕾莎院长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050381V我刚刚接到报告，\n',
            '所以就急急忙忙赶了过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050382V不过，幸好你们都没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050383V#750F谢谢您，市长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050384V要您在百忙之中抽出时间过来，\n',
            '我真是感到过意不去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050385V#660F#4P没什么，这也是身为\n',
            '卢安市长所应尽的职责啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050386V#664F而且，虽然不知道是何人所为，\n',
            '总之这种行径绝不能饶恕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050387V竟然灭绝人性地把\n',
            '约瑟夫心爱的屋子给……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050388V#662F简直令人惋惜和气愤啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050389V#754F不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050390V只要孩子们得救了，\n',
            '我想他也会觉得欣慰吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050391V#757F唯一遗憾的是，\n',
            '他的遗物全都被烧毁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050392V#043F特蕾莎老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000F, 225, 300)

    ChrTalk(
        0x000F,
        (
            '#0490050393V#662F两位游击士，\n',
            '案件有眉目了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050394V#012F调查才刚开始，\n',
            '所以还不能下明确的结论……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050395V不过，经过初步的判断，\n',
            '也存在着恶作剧性质的犯罪可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050396V#664F是吗……\n',
            '真是令人遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050397V在这美丽的卢安，\n',
            '竟然也有如此丑恶的人存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0010, 315, 400)

    ChrTalk(
        0x0010,
        (
            '#0480050398V#673F市长，请恕我失礼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 400)

    ChrTalk(
        0x000F,
        (
            '#0490050399V#660F嗯，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480050400V#671F这次的火灾……\n',
            '该不会是他们几个做的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050401V#662F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050402V#004F等、等等！\n',
            '『他们几个』是指谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0010, 270, 300)

    ChrTalk(
        0x0010,
        (
            '#0480050403V#671F你们几位昨天不是也被他们缠上了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050404V就是聚集在卢安仓库那一带的\n',
            '那些地痞流氓啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050405V#002F是他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050406V#043F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050407V#012F恕我多言……\n',
            '为什么您会怀疑他们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480050408V#671F昨天的事也是这样……\n',
            '那帮家伙总是跟市长作对，\n',
            '整天惹是生非，唯恐天下不乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050409V甚至以给市长惹麻烦为乐。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480050410V#673F所以就对和市长\n',
            '交情很深的特蕾莎院长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050411V#665F基尔巴特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrDirection(0x0010, 315, 400)

    ChrTalk(
        0x0010,
        (
            '#0480050412V#676F是、是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050413V#663F不要光凭猜测就\n',
            '如此口无遮拦地妄下判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050414V这是重大的犯罪。\n',
            '绝不能冤枉任何人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0480050415V#676F十、十分抱歉。\n',
            '请恕我考虑不周……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#664F用不着你多嘴，\n',
            '这两位游击士也\n',
            '一定会把犯人缉捕归案的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000F, 225, 400)

    ChrTalk(
        0x000F,
        (
            '#0490050417V#660F我这样说没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050418V#006F嗯，包在我们身上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050419V#010F我们一定尽力而为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050420V#661F嗯，这回答真让人放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000A, 400)
    Sleep(500)

    SetChrDirection(0x0010, 270, 0)

    ChrTalk(
        0x000F,
        (
            '#0490050421V#660F#4P对了，特蕾莎院长……\n',
            '我有件事想和你谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050422V#753F什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050423V#660F#4P孤儿院现在毁了，\n',
            '从今以后你有什么打算？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050424V房子重建需要一段时间，\n',
            '而且需要花费的金钱也不少吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050425V#757F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050426V老实说，我也不知该如何是好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050427V我这里虽然有一点积蓄，\n',
            '但要重建孤儿院的话根本……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050428V#003F院长老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050429V#043F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050430V#664F#4P果然如此吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050431V#660F要不这样吧。\n',
            '你听听我个人的提议如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050432V#750F……是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050433V#660F#4P其实是这样的，\n',
            '格兰赛尔有我们戴尔蒙家的别墅。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050434V我平时只是偶尔去住一下，\n',
            '所以那里一直都是闲置着的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050435V可以的话，你就和孩子们\n',
            '搬到我那别墅住一段时间如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050436V#753F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050437V#660F#4P当然，院长你也不必\n',
            '为房租这类无关痛痒的事情和我客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050438V直到重建的事有眉目为止，\n',
            '随便你们在那里住多久都没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050439V#757F但、但这也太麻烦您了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050440V#661F#4P反正那屋子也没人住。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050441V你要是觉得过意不去……\n',
            '嗯，那不妨就帮我看管房子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050442V当然，我会付报酬的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050443V#756F市长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050444V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050445V#757F能让我考虑一下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050446V真的很感谢您的提议，\n',
            '不过实在发生了太多事情，\n',
            '所以我现在很难一下子给您答复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0490050447V#664F#4P这也难怪……\n',
            '你就先好好休息一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050448V#660F我们这就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490050449V如果你考虑好了，\n',
            '可以随时和我联系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050450V#750F好的……\n',
            '真的非常感谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 400)

    ChrTalk(
        0x000F,
        (
            '#0490050451V#660F基尔巴特，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 400)

    ChrTalk(
        0x0010,
        (
            '#0480050452V#670F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0010, -47080, 0, -1610, 2000, 0x00)
    SetChrDirection(0x0010, 0, 400)

    @scena.Lambda('lambda_44EA')
    def lambda_44EA():
        ChrWalkTo(0x00FE, -45280, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_44EA)

    WaitForThreadExit(0x000F, 0x0001)

    @scena.Lambda('lambda_450A')
    def lambda_450A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_450A)

    @scena.Lambda('lambda_451C')
    def lambda_451C():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_451C)

    Sleep(300)

    @scena.Lambda('lambda_453C')
    def lambda_453C():
        ChrWalkTo(0x00FE, -45280, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_453C)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_455C')
    def lambda_455C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_455C)

    @scena.Lambda('lambda_456E')
    def lambda_456E():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_456E)

    WaitForThreadExit(0x000F, 0x0001)
    SetChrFlags(0x000F, 0x0080)
    WaitForThreadExit(0x0010, 0x0001)
    SetChrFlags(0x0010, 0x0080)
    Sleep(500)

    @scena.Lambda('lambda_45A2')
    def lambda_45A2():
        CameraMove(-49600, 0, -480, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_45A2)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010050453V#008F哈～真是吃了一惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050454V原来除了梅贝尔市长之外，\n',
            '这个戴尔蒙市长也是这么大度的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050455V#010F是啊……\n',
            '真不愧是昔日的豪门贵族。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0136, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0136)

    @scena.Lambda('lambda_4670')
    def lambda_4670():
        CameraMove(-49200, 0, 70, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4670)

    TerminateThread(0x0136, 0xFF)
    ChrWalkTo(0x0136, -48300, 0, -100, 2000, 0x00)
    ChrTurnDirection(0x0136, 0x000A, 400)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_46B3')
    def lambda_46B3():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_46B3)

    @scena.Lambda('lambda_46C1')
    def lambda_46C1():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_46C1)

    ChrTurnDirection(0x000A, 0x0136, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050456V#049F老师，市长的提议，\n',
            '您打算怎么回应呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050457V#754F是啊……\n',
            '你又是怎么想的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050458V#049F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050459V#049F从常理来说，\n',
            '我觉得自然是应该接受的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050460V可是……\n',
            '你们要是去了王都的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050461V#043F不……没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050462V#750F呵呵，我知道你向来\n',
            '都是个很明白事理的孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050463V没事的，科洛丝。\n',
            '有什么心里话尽管说出来好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050464V#043F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050465V#049F要是你们去了王都，\n',
            '那块香草田就会没人打理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050466V而且……而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050467V#047F我总觉得老师和约瑟夫叔叔\n',
            '疼爱我照顾我的那段回忆\n',
            '也会随之消失掉似的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050468V对不起……\n',
            '我说了一些任性的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050469V#750F呵呵，其实我也有同样的感受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050470V在那里，充满了许多\n',
            '孩子们和我丈夫的珍贵回忆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050471V但是我觉得，\n',
            '和这些回忆相比起来，\n',
            '如何生存下去才是更加重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050472V#049F是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390050473V#750F嗯……\n',
            '这段时间我就会做出决定的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050474V你还是继续\n',
            '专心准备学园祭的事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050475V那些孩子也都\n',
            '很期待那天的到来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050476V#048F……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 300)

    ChrTalk(
        0x000A,
        (
            '#750F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050478V这么说虽然很不好意思……\n',
            '不过调查的事情，还是要拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 0)
    Sleep(100)

    ChrTurnDirection(0x0102, 0x000A, 0)

    ChrTalk(
        0x0102,
        (
            '#0020050479V#010F请放心交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050480V#006F我们一定会捉到犯人，\n',
            '绝对不会让他们逍遥法外的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x4B9C
@scena.Code('func_11_4B9C')
def func_11_4B9C():
    Sleep(1500)

    ChrSetRGBAMask(0x0136, 255, 255, 255, 0, 500)

    Return()

# id: 0x0012 offset: 0x4BAD
@scena.Code('func_12_4BAD')
def func_12_4BAD():
    Sleep(2000)

    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 500)

    Return()

# id: 0x0013 offset: 0x4BBE
@scena.Code('func_13_4BBE')
def func_13_4BBE():
    Sleep(2500)

    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 500)

    Return()

# id: 0x0014 offset: 0x4BCF
@scena.Code('func_14_4BCF')
def func_14_4BCF():
    Sleep(3000)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 500)

    Return()

# id: 0x0015 offset: 0x4BE0
@scena.Code('func_15_4BE0')
def func_15_4BE0():
    Sleep(3500)

    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 500)

    Return()

# id: 0x0016 offset: 0x4BF1
@scena.Code('func_16_4BF1')
def func_16_4BF1():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-50180, 0, -790, 0)
    FormationAddMember(0x05, 0xFF)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0009, -52430, 0, 480, 0)
    SetChrPos(0x000B, -50850, 0, -1230, 270)
    SetChrPos(0x000D, -51540, 0, -2430, 0)
    SetChrPos(0x000C, -52530, 0, -2420, 0)
    SetChrPos(0x000E, -50800, 0, 1470, 270)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrFlags(0x0106, 0x0080)
    SetChrPos(0x0101, -44330, 0, -1080, 270)
    SetChrPos(0x0102, -44330, 0, -1080, 270)
    SetChrPos(0x0105, -44330, 0, -1080, 270)
    SetChrPos(0x0106, -44330, 0, -1080, 270)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0106, 255, 255, 255, 0, 0)
    OP_4A(0x0009, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000E, 255)
    SetChrFlags(0x0106, 0x0080)
    FadeIn(1000, 0)
    CreateThread(0x0105, 0x01, 0x00, 0x0019)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 255, 500)
    CreateThread(0x0101, 0x01, 0x00, 0x0017)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 500)
    CreateThread(0x0102, 0x01, 0x00, 0x0018)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 255, 500)
    WaitForThreadExit(0x0011, 0x0001)
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_4DE0')
    def lambda_4DE0():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4DE0)

    @scena.Lambda('lambda_4DEE')
    def lambda_4DEE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4DEE)

    @scena.Lambda('lambda_4DFC')
    def lambda_4DFC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4DFC)

    @scena.Lambda('lambda_4E0A')
    def lambda_4E0A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4E0A)

    @scena.Lambda('lambda_4E18')
    def lambda_4E18():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4E18)

    ChrTalk(
        0x000E,
        (
            '#775F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哥哥姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061013V#043F孩子们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x00, 0x001A)
    CreateThread(0x000C, 0x01, 0x00, 0x001B)
    CreateThread(0x000E, 0x01, 0x00, 0x001C)
    CreateThread(0x000D, 0x01, 0x00, 0x001D)
    WaitForThreadExit(0x000B, 0x0001)
    CreateThread(0x0009, 0x01, 0x00, 0x001E)

    ChrTalk(
        0x000B,
        (
            '呜哇啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1P好可怕啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F太好了……\n',
            '大家都平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_4EE4')
    def lambda_4EE4():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4EE4')

    DispatchAsync2(0x0102, 0x0001, lambda_4EE4)

    ChrTalk(
        0x0102,
        (
            '#012F对不起。\n',
            '老师她们的状况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '放心吧。\n',
            '两人都没受什么伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '只是一直昏迷不醒，\n',
            '着实让人有些担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F……容我失礼一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_4F96')
    def lambda_4F96():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_4F96')

    DispatchAsync2(0x0101, 0x0001, lambda_4F96)

    @scena.Lambda('lambda_4FA7')
    def lambda_4FA7():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_4FA7')

    DispatchAsync2(0x0105, 0x0001, lambda_4FA7)

    @scena.Lambda('lambda_4FB8')
    def lambda_4FB8():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_4FB8')

    DispatchAsync2(0x000E, 0x0001, lambda_4FB8)

    @scena.Lambda('lambda_4FC9')
    def lambda_4FC9():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_4FC9')

    DispatchAsync2(0x000C, 0x0001, lambda_4FC9)

    @scena.Lambda('lambda_4FDA')
    def lambda_4FDA():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_4FDA')

    DispatchAsync2(0x0009, 0x0001, lambda_4FDA)

    ChrWalkTo(0x0102, -48420, 0, 90, 2000, 0x00)
    ChrWalkTo(0x0102, -49300, 0, 970, 2000, 0x00)

    @scena.Lambda('lambda_5013')
    def lambda_5013():
        CameraMove(-52260, 0, -520, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5013)

    ChrWalkTo(0x0102, -51050, 0, 550, 2000, 0x00)
    ChrWalkTo(0x0102, -53010, 0, 500, 2000, 0x00)
    SetChrDirection(0x0102, 0, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    SetChrDirection(0x0102, 180, 400)
    Sleep(1000)

    OP_63(0x0102)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020061021V#013F果然没错……\n',
            '看来是对她们施了催眠药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#004F催、催眠药？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061023V#012F嗯，还能闻到一点刺激性气味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061024V这是没有副作用的品种，\n',
            '所以我想应该可以放心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000C, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#505F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 90, 400)

    @scena.Lambda('lambda_5184')
    def lambda_5184():
        CameraMove(-50370, 0, -640, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5184)

    ChrWalkTo(0x0102, -50560, 0, 240, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#002F对了，克拉姆。\n',
            '可以告诉我们发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400061027V#773F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '我来说吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)

    @scena.Lambda('lambda_5230')
    def lambda_5230():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5230)

    @scena.Lambda('lambda_523E')
    def lambda_523E():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_523E)

    Sleep(50)

    @scena.Lambda('lambda_5251')
    def lambda_5251():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5251)

    @scena.Lambda('lambda_525F')
    def lambda_525F():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_525F)

    Sleep(50)

    @scena.Lambda('lambda_5272')
    def lambda_5272():
        ChrTurnDirection(0x00FE, 0x000C, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5272)

    @scena.Lambda('lambda_5280')
    def lambda_5280():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5280)

    Sleep(50)

    TerminateThread(0x000E, 0xFF)
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0410061029V#1P我们……\n',
            '和游击士姐姐一起\n',
            '在海道上走着走着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061030V#1P就在那时，\n',
            '突然出现了几个蒙面的怪人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061031V#1P游击士姐姐\n',
            '虽然想把他们赶走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061032V#1P但是我们很快就被\n',
            '那几个蒙面的怪人包围了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061033V#1P老师也为了保护我们，\n',
            '跟那帮怪人纠缠了起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061034V#1P……然后就……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061035V#003F好了好了，大家都吓坏了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400061036V#773F……那帮家伙……\n',
            '还把老师身上的信封给抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5452')
    def lambda_5452():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5452)

    Sleep(50)

    @scena.Lambda('lambda_5465')
    def lambda_5465():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5465)

    Sleep(50)

    @scena.Lambda('lambda_5478')
    def lambda_5478():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5478)

    Sleep(50)

    @scena.Lambda('lambda_548B')
    def lambda_548B():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_548B)

    Sleep(50)

    ChrTurnDirection(0x0102, 0x000E, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0400061037V#775F我……\n',
            '我想把信封抢回来的，\n',
            '但一下子就被他们踢倒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000E, 0xFF)
    ChrTurnDirection(0x000E, 0x0102, 300)

    ChrTalk(
        0x000E,
        (
            '#0400061038V#777F约修亚哥哥……\n',
            '我……没能保护好老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F#1P……没这回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061040V只要你们没事，\n',
            '老师就一定已经很高兴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061041V#012F所以……不要责备自己了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400061042V#777F但是……\n',
            '我……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#005F不可原谅……！\n',
            '到底是什么人干的好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#047F#2P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#042F#2P现在可以确定的是……\n',
            '那些蒙面人的犯案手段相当老练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060940005V连游击士都不是他们对手，\n',
            '甚至还被他们用催眠药弄晕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_56BB')
    def lambda_56BB():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_56BB)

    @scena.Lambda('lambda_56C9')
    def lambda_56C9():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_56C9)

    @scena.Lambda('lambda_56D7')
    def lambda_56D7():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_56D7)

    ChrTurnDirection(0x000E, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#004F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#042F#2P另外还有一点……\n',
            '我认为这是有计划的犯罪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061050V目标当然是\n',
            '老师身上的那大批捐款……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061051V纵火烧孤儿院\n',
            '恐怕同样是这些人的所为吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F#1P嗯，这种可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F科洛丝……\n',
            '看来你终于镇定下来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#043F#2P是的……\n',
            '因为再沮丧也于事无补。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061055V总之现在要尽快\n',
            '找到犯人的行踪才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0106, -44560, 0, -1160, 0)
    ChrTurnDirection(0x0106, 0x0105, 0)
    ClearChrFlags(0x0106, 0x0080)

    NpcTalk(
        0x0106,
        '青年的声音',
        (
            '#0050061056V#1P……我也有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrChipByIndex(0x0106, 15)

    @scena.Lambda('lambda_58D6')
    def lambda_58D6():
        CameraMove(-49600, 0, -620, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_58D6)

    ClearChrFlags(0x0106, 0x0080)

    @scena.Lambda('lambda_58F3')
    def lambda_58F3():
        ChrWalkTo(0x00FE, -47720, 0, -760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_58F3)

    @scena.Lambda('lambda_590E')
    def lambda_590E():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_590E)

    @scena.Lambda('lambda_591C')
    def lambda_591C():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_591C)

    @scena.Lambda('lambda_592A')
    def lambda_592A():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_592A)

    @scena.Lambda('lambda_5938')
    def lambda_5938():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5938)

    @scena.Lambda('lambda_5946')
    def lambda_5946():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5946)

    @scena.Lambda('lambda_5954')
    def lambda_5954():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5954)

    @scena.Lambda('lambda_5962')
    def lambda_5962():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5962)

    @scena.Lambda('lambda_5970')
    def lambda_5970():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5970)

    ChrSetRGBAMask(0x0106, 255, 255, 255, 255, 500)
    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#004F啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F阿加特兄……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061059V#051F事情我在协会听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061060V看来这次的情况\n',
            '还满棘手的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0005F别、别说得好像事不关己一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061062V连卡露娜姐姐都\n',
            '中了他们的暗算啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061063V#053F我知道……\n',
            '别大呼小叫的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061064V#050F卡露娜是一流的游击士。\n',
            '看来是帮相当危险的家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061065V把事情经过给我说一遍吧，\n',
            '说个大概就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061066V#012F好的……',
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
            '约修亚向阿加特说明了\n',
            '包括捐款被抢在内一系列事情的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0106,
        (
            '#053F嗯，这样啊……\n',
            '不过事情有点古怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F古怪？什么古怪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061069V#050F啊啊，其实是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061070V『渡鸦帮』的那帮蠢货\n',
            '已经离开了港口的仓库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F这、这就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061072V#005F果然是这帮家伙\n',
            '袭击特蕾莎院长他们吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F不，这还不好说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061074V我觉得以他们的力量\n',
            '根本不足以做卡露娜小姐的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F这倒也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061076V那帮家伙只会耍嘴皮子，\n',
            '根本就没什么真功夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061077V#057F我盯了他们一阵子，\n',
            '本来还以为他们变老实了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061078V谁知道那些蠢货\n',
            '今天突然不见了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061079V刚好又在这时候发生了这事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F先不说他们是不是犯人，\n',
            '但肯定跟这件事脱不了关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061081V#050F是啊……\n',
            '不过现在还不是研究这个的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061082V你们两个，跟我一起走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F什么呀，忽然冒出这一句……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061084V#002F到底要去哪里啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F你还真是迟钝。\n',
            '当然是去犯罪现场的海道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061086V先不管这件事\n',
            '是不是那帮蠢货干的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061087V#054F总之要尽量多搜集些线索，\n',
            '找到犯人的行踪！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F啊……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F明白了，我们跟你一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x5F40
@scena.Code('func_17_5F40')
def func_17_5F40():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -49040, 0, -1430, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 400)

    Return()

# id: 0x0018 offset: 0x5F61
@scena.Code('func_18_5F61')
def func_18_5F61():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -48370, 0, -700, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 400)

    Return()

# id: 0x0019 offset: 0x5F82
@scena.Code('func_19_5F82')
def func_19_5F82():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -49500, 0, -430, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 400)

    Return()

# id: 0x001A offset: 0x5FA3
@scena.Code('func_1A_5FA3')
def func_1A_5FA3():
    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -50110, 0, -750, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x001B offset: 0x5FD1
@scena.Code('func_1B_5FD1')
def func_1B_5FD1():
    Sleep(150)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -49270, 0, -2120, 3000, 0x00)
    SetChrDirection(0x00FE, 0, 400)

    Return()

# id: 0x001C offset: 0x6004
@scena.Code('func_1C_6004')
def func_1C_6004():
    Sleep(100)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -49390, 0, 270, 3000, 0x00)
    SetChrDirection(0x00FE, 180, 400)

    Return()

# id: 0x001D offset: 0x6037
@scena.Code('func_1D_6037')
def func_1D_6037():
    Sleep(50)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -49880, 0, -1360, 3000, 0x00)
    SetChrDirection(0x00FE, 45, 400)

    Return()

# id: 0x001E offset: 0x606A
@scena.Code('func_1E_606A')
def func_1E_606A():
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x0009, 0x0004)
    ChrWalkTo(0x0009, -50910, 0, 350, 2000, 0x00)
    ChrWalkTo(0x0009, -49590, 0, 1010, 2000, 0x00)
    ChrWalkTo(0x0009, -48330, 0, 860, 2000, 0x00)
    ChrTurnDirection(0x0009, 0x0102, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
