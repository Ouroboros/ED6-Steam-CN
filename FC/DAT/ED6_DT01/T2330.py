import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2330_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2330   ._SN')

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
    header.mapModel       = 'T2330.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7276
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
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
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
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_32C',
    )

    Jump('loc_591')

    def _loc_32C(): pass

    label('loc_32C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_393',
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

    Jump('loc_591')

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_42B',
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

    Jump('loc_591')

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_502',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0010)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
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

    Jump('loc_591')

    def _loc_502(): pass

    label('loc_502')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_511',
    )

    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_591')

    def _loc_511(): pass

    label('loc_511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_562',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -48450, 0, -990, 270)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -49210, 0, -2360, 315)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -47720, 0, 2100, 0)

    Jump('loc_591')

    def _loc_562(): pass

    label('loc_562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_56C',
    )

    Jump('loc_591')

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_576',
    )

    Jump('loc_591')

    def _loc_576(): pass

    label('loc_576')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_580',
    )

    Jump('loc_591')

    def _loc_580(): pass

    label('loc_580')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_58A',
    )

    Jump('loc_591')

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_591',
    )

    def _loc_591(): pass

    label('loc_591')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006B, 'loc_59D'),
        (-1, 'loc_5C6'),
    )

    def _loc_59D(): pass

    label('loc_59D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B0',
    )

    SetScenaFlags(ScenaFlag(0x0085, 0, 0x428))
    Event(0, 0x0010)

    def _loc_5B0(): pass

    label('loc_5B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C3',
    )

    SetScenaFlags(ScenaFlag(0x0086, 6, 0x436))
    Event(0, 0x0016)

    def _loc_5C3(): pass

    label('loc_5C3')

    Jump('loc_5C6')

    def _loc_5C6(): pass

    label('loc_5C6')

    Return()

# id: 0x0001 offset: 0x5C7
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F7',
    )

    OP_B1('t2330_y')
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 15)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 15)

    Jump('loc_600')

    def _loc_5F7(): pass

    label('loc_5F7')

    OP_B1('t2330_n')

    def _loc_600(): pass

    label('loc_600')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_610',
    )

    OP_64(0x00, 0x0001)

    def _loc_610(): pass

    label('loc_610')

    Return()

# id: 0x0002 offset: 0x611
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_626',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_626(): pass

    label('loc_626')

    Return()

# id: 0x0003 offset: 0x627
@scena.Code('func_03_627')
def func_03_627():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x62C
@scena.Code('func_04_62C')
def func_04_62C():
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
            TXT(0x02, '欢迎品尝「硬壳杂菜烩饭」500米拉\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AA',
    )

    OP_0D()
    OP_A9(0x2A)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_6AA(): pass

    label('loc_6AA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x1F4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_777',
    )

    SubMira(500)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '硬壳杂菜烩饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFD, 450)
    SetChrStatus(0x0001, 0xFD, 450)
    SetChrStatus(0x0002, 0xFD, 450)
    SetChrStatus(0x0003, 0xFD, 450)
    SetChrStatus(0x0004, 0xFD, 450)
    SetChrStatus(0x0005, 0xFD, 450)
    SetChrStatus(0x0006, 0xFD, 450)
    SetChrStatus(0x0007, 0xFD, 450)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_769',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0001)"),
            Expr.Return,
        ),
        'loc_73F',
    )

    Jump('loc_769')

    def _loc_73F(): pass

    label('loc_73F')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '硬壳杂菜烩饭',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_769(): pass

    label('loc_769')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_79D')

    def _loc_777(): pass

    label('loc_777')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_79D(): pass

    label('loc_79D')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0008)

    Return()

    def _loc_7AC(): pass

    label('loc_7AC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BD',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_7BD(): pass

    label('loc_7BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F16',
    )

    EventBegin(0x00)
    OP_69(0x0008, 800)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 1, 0x401)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C08',
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

    Jump('loc_C6E')

    def _loc_C08(): pass

    label('loc_C08')

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

    def _loc_C6E(): pass

    label('loc_C6E')

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
        (0x00000000, 'loc_CD5'),
        (0x00000001, 'loc_E65'),
        (-1, 'loc_F11'),
    )

    def _loc_CD5(): pass

    label('loc_CD5')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x78),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_E18',
    )

    ExecExpressionWithVar(
        0x12,
        (
            (Expr.PushLong, 0x78),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    PlaySE(20, 0x00, 0x64)
    Sleep(1000)

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

    Jump('loc_E62')

    def _loc_E18(): pass

    label('loc_E18')

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

    def _loc_E62(): pass

    label('loc_E62')

    Jump('loc_F11')

    def _loc_E65(): pass

    label('loc_E65')

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

    Jump('loc_F11')

    def _loc_F11(): pass

    label('loc_F11')

    EventEnd(0x01)

    Jump('loc_1616')

    def _loc_F16(): pass

    label('loc_F16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_FFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FAA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '当时我看到的犯人\n',
            '果然是市长的秘书啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说起来，\n',
            '市长他们竟然犯下那样的罪行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哼，\n',
            '他们要用往后的人生来赎罪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FFC')

    def _loc_FAA(): pass

    label('loc_FAA')

    ChrTalk(
        0x0008,
        (
            '说起来，\n',
            '市长他们竟然犯下那样的罪行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哼，\n',
            '他们要用往后的人生来赎罪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FFC(): pass

    label('loc_FFC')

    Jump('loc_1616')

    def _loc_FFF(): pass

    label('loc_FFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_10E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1095',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我好像在哪里\n',
            '看到过其中的一个犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '难道说，就是之前\n',
            '到这里来过的戴尔蒙市长的秘书？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……不会的。\n',
            '应该不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10E1')

    def _loc_1095(): pass

    label('loc_1095')

    ChrTalk(
        0x0008,
        (
            '其中一个犯人\n',
            '感觉有点像市长的秘书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……不会的。\n',
            '应该不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10E1(): pass

    label('loc_10E1')

    Jump('loc_1616')

    def _loc_10E4(): pass

    label('loc_10E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1193',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1155',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '老师她们\n',
            '在这里的二楼休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '纵火事件也好，这回的事情也罢，\n',
            '孩子们真是太可怜了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1190')

    def _loc_1155(): pass

    label('loc_1155')

    ChrTalk(
        0x0008,
        (
            '纵火事件也好，这回的事情也罢，\n',
            '孩子们真是太可怜了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1190(): pass

    label('loc_1190')

    Jump('loc_1616')

    def _loc_1193(): pass

    label('loc_1193')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1279',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_121C',
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

    Jump('loc_1276')

    def _loc_121C(): pass

    label('loc_121C')

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

    def _loc_1276(): pass

    label('loc_1276')

    Jump('loc_1616')

    def _loc_1279(): pass

    label('loc_1279')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_12CC',
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

    Jump('loc_1616')

    def _loc_12CC(): pass

    label('loc_12CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_1396',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_135C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '听说，\n',
            '孤儿院被烧得精光？',
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

    Jump('loc_1393')

    def _loc_135C(): pass

    label('loc_135C')

    ChrTalk(
        0x0008,
        (
            '小姑娘，如果可以的话，\n',
            '请你们鼓励一下那些孩子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1393(): pass

    label('loc_1393')

    Jump('loc_1616')

    def _loc_1396(): pass

    label('loc_1396')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_13D9',
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

    Jump('loc_1616')

    def _loc_13D9(): pass

    label('loc_13D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_14F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_149D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '这里的游客大多都是\n',
            '来观赏木莲之花和海岸美景的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '偶尔也会有一些\n',
            '像那两个人一样的登山客来……',
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

    Jump('loc_14F5')

    def _loc_149D(): pass

    label('loc_149D')

    ChrTalk(
        0x0008,
        (
            '从风车小屋望出去，\n',
            '景色很美丽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个风车小屋和湛蓝的大海\n',
            '搭配起来很漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F5(): pass

    label('loc_14F5')

    Jump('loc_1616')

    def _loc_14F8(): pass

    label('loc_14F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_159B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_156F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '哦，\n',
            '这不是刚才来过的小姑娘吗。',
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
            '啊？男孩子吗？\n',
            '他没有到这家店来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1598')

    def _loc_156F(): pass

    label('loc_156F')

    ChrTalk(
        0x0008,
        (
            '啊？男孩子吗？\n',
            '他没有到这家店来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1598(): pass

    label('loc_1598')

    Jump('loc_1616')

    def _loc_159B(): pass

    label('loc_159B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1616',
    )

    ChrTalk(
        0x0008,
        (
            '我们村里的风车小屋前\n',
            '有个可以看到漂亮海景的瞭望台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '每到中午的时候，\n',
            '就有很多客人来这里买便当拿去那里吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1616(): pass

    label('loc_1616')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x161A
@scena.Code('func_05_161A')
def func_05_161A():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x161F
@scena.Code('func_06_161F')
def func_06_161F():
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
        'loc_167B',
    )

    OP_0D()
    OP_A9(0x29)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_167B(): pass

    label('loc_167B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_168C',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_168C(): pass

    label('loc_168C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_16E7',
    )

    ChrTalk(
        0x0009,
        (
            '在孤儿院重建之前，\n',
            '各位就先住在这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里变得热闹起来，我也很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BFA')

    def _loc_16E7(): pass

    label('loc_16E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1758',
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

    ChrTalk(
        0x0009,
        (
            '可能会用石头砸他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BFA')

    def _loc_1758(): pass

    label('loc_1758')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_17A3',
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
            '做坏事也要有个限度啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BFA')

    def _loc_17A3(): pass

    label('loc_17A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1853',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1810',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '孤儿院的孩子们和老师\n',
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

    Jump('loc_1850')

    def _loc_1810(): pass

    label('loc_1810')

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

    def _loc_1850(): pass

    label('loc_1850')

    Jump('loc_1BFA')

    def _loc_1853(): pass

    label('loc_1853')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1894',
    )

    ChrTalk(
        0x0009,
        (
            '刚才克拉姆\n',
            '急急忙忙跑出去了……',
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

    Jump('loc_1BFA')

    def _loc_1894(): pass

    label('loc_1894')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_19DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1995',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x0009, 0x0136, 0)

    ChrTalk(
        0x0009,
        (
            '啊，王立学院的校服……',
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
        0x0136,
        (
            '#044F嗯，是的。\n',
            '我就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '孤儿院的孩子们\n',
            '都急着想见你呢。',
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
        0x0136,
        (
            '#043F嗯，好、好的。\n',
            '真是麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19DB')

    def _loc_1995(): pass

    label('loc_1995')

    ChrTurnDirection(0x0009, 0x0136, 0)

    ChrTalk(
        0x0009,
        (
            '孤儿院的孩子们\n',
            '都急着想见你呢。',
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

    def _loc_19DB(): pass

    label('loc_19DB')

    Jump('loc_1BFA')

    def _loc_19DE(): pass

    label('loc_19DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1A7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A44',
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

    Jump('loc_1A79')

    def _loc_1A44(): pass

    label('loc_1A44')

    ChrTalk(
        0x0009,
        (
            '今天的天气很不错，\n',
            '晒床单的话应该很快就能干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A79(): pass

    label('loc_1A79')

    Jump('loc_1BFA')

    def _loc_1A7C(): pass

    label('loc_1A7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1AEE',
    )

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
            '但是来赏花的人却不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BFA')

    def _loc_1AEE(): pass

    label('loc_1AEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_1B46',
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

    Jump('loc_1BFA')

    def _loc_1B46(): pass

    label('loc_1B46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1BFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BCD',
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

    Jump('loc_1BFA')

    def _loc_1BCD(): pass

    label('loc_1BCD')

    ChrTalk(
        0x0009,
        (
            '如果可以的话，\n',
            '请在我们这里享用午餐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BFA(): pass

    label('loc_1BFA')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1BFE
@scena.Code('func_07_1BFE')
def func_07_1BFE():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1C42',
    )

    ChrTalk(
        0x00FE,
        (
            '好，再去登山吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '古罗尼的山峰\n',
            '在呼唤着我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D5')

    def _loc_1C42(): pass

    label('loc_1C42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1CAB',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '听说犯人被抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想把他们带到山里，\n',
            '把他们那些扭曲丑陋的性格\n',
            '给纠正回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D5')

    def _loc_1CAB(): pass

    label('loc_1CAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_1D9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D3C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '那些孩子们\n',
            '这次又被强盗袭击了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '可恶，这是怎么回事啊！\n',
            '怎么会发生这种残酷的事情！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9C')

    def _loc_1D3C(): pass

    label('loc_1D3C')

    ChrTalk(
        0x00FE,
        (
            '那些孩子们\n',
            '这次又被强盗袭击了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶，这是怎么回事啊！\n',
            '怎么会发生这种残酷的事情！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9C(): pass

    label('loc_1D9C')

    Jump('loc_21D5')

    def _loc_1D9F(): pass

    label('loc_1D9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1EB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E60',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '今天天气不错，\n',
            '应该能够登上山顶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '我还是有点担心孤儿院的孩子们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还想再照顾一下\n',
            '那些孩子们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我可能帮不上什么忙，\n',
            '但是我也不能坐视不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EB4')

    def _loc_1E60(): pass

    label('loc_1E60')

    ChrTalk(
        0x00FE,
        (
            '今天天气不错，\n',
            '应该能够登上山顶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '我还是有点担心孤儿院的孩子们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EB4(): pass

    label('loc_1EB4')

    Jump('loc_21D5')

    def _loc_1EB7(): pass

    label('loc_1EB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1F17',
    )

    ChrTalk(
        0x00FE,
        (
            '附近的孤儿院被纵火烧毁了，\n',
            '是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然有人能\n',
            '做出这么伤天害理的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D5')

    def _loc_1F17(): pass

    label('loc_1F17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_1F5A',
    )

    ChrTalk(
        0x00FE,
        (
            '我听到二楼\n',
            '传出孩子们的哭声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D5')

    def _loc_1F5A(): pass

    label('loc_1F5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_205A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FF9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '山真好呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一大早起来呼吸到清爽的空气，\n',
            '感觉真的很舒服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直就像切身感受到\n',
            '山间气氛的瞬间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～好想快点去登山啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2057')

    def _loc_1FF9(): pass

    label('loc_1FF9')

    ChrTalk(
        0x00FE,
        (
            '一大早起来呼吸到清爽的空气，\n',
            '感觉真的很舒服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直就像切身感受到\n',
            '山间气氛的瞬间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2057(): pass

    label('loc_2057')

    Jump('loc_21D5')

    def _loc_205A(): pass

    label('loc_205A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_2130',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2100',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊～我好想快点去登山啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你问我为什么要去登山？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真是个愚蠢的问题……\n',
            '因为那里有山啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F那个……\n',
            '我什么也没有问啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_212D')

    def _loc_2100(): pass

    label('loc_2100')

    ChrTalk(
        0x00FE,
        (
            '你问我为什么要去登山？\n',
            '因为那里有山啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_212D(): pass

    label('loc_212D')

    Jump('loc_21D5')

    def _loc_2130(): pass

    label('loc_2130')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_2183',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯？\n',
            '你们在找一个戴帽子的男孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好像没有看见过这样的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D5')

    def _loc_2183(): pass

    label('loc_2183')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_21D5',
    )

    ChrTalk(
        0x00FE,
        (
            '我们是登山爱好者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了登上古罗尼连峰，\n',
            '我们才留在了玛诺利亚村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21D5(): pass

    label('loc_21D5')

    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x21D9
@scena.Code('func_08_21D9')
def func_08_21D9():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_223C',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，南坡面的雪有点融化，\n',
            '可能会很危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是重新考虑一下\n',
            '登山路线比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C4')

    def _loc_223C(): pass

    label('loc_223C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_22B6',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '听说那些犯人终于被抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我的同伴\n',
            '也可以稍微放心些了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的心情也一下子爽快了许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C4')

    def _loc_22B6(): pass

    label('loc_22B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2318',
    )

    ChrTalk(
        0x00FE,
        (
            '难不成，\n',
            '抢劫犯和纵火犯是同一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种行为太没有人性了。\n',
            '真让人怒火中烧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C4')

    def _loc_2318(): pass

    label('loc_2318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2374',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '登山的机会以后还是会有的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于阿尔宾说的那番话，\n',
            '我也没有异议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C4')

    def _loc_2374(): pass

    label('loc_2374')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_23DF',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，天气很不错，\n',
            '不久之后就可以\n',
            '向古罗尼连峰挑战了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来我们这么等着\n',
            '还是有价值的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C4')

    def _loc_23DF(): pass

    label('loc_23DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_240C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '看来发生了什么大事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C4')

    def _loc_240C(): pass

    label('loc_240C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_258C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2527',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '古罗尼连峰就像半岛一样，\n',
            '向瓦雷利亚湖中突起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为标高相当高，\n',
            '要登山必须装备得非常完善才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据天气和季节不同，\n',
            '必须要慎重考虑，\n',
            '选择路线也是非常重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我们应该等到\n',
            '山里的天气恢复了再行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这里很晴朗，\n',
            '但山里天气好像很糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2589')

    def _loc_2527(): pass

    label('loc_2527')

    ChrTalk(
        0x00FE,
        (
            '要登古罗尼连蜂\n',
            '必须要有完善的装备和心理准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我们只能等到\n',
            '山里的天气恢复了再行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2589(): pass

    label('loc_2589')

    Jump('loc_27C4')

    def _loc_258C(): pass

    label('loc_258C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_266C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2613',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '已经购买了充足的干粮，\n',
            '装备也准备齐全了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上一次由于气候恶劣只能作罢，\n',
            '这次我一定要踏遍这连绵的山峦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2669')

    def _loc_2613(): pass

    label('loc_2613')

    ChrTalk(
        0x00FE,
        (
            '众所周知，山里面是很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的伙伴阿尔宾\n',
            '如果能学得\n',
            '更加慎重点就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2669(): pass

    label('loc_2669')

    Jump('loc_27C4')

    def _loc_266C(): pass

    label('loc_266C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_273E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2710',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '男孩子啊……\n',
            '长什么样子的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F唔，戴着帽子的，\n',
            '样子很淘气任性的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '非常抱歉，我没有看到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273B')

    def _loc_2710(): pass

    label('loc_2710')

    ChrTalk(
        0x00FE,
        (
            '男孩子啊……\n',
            '非常抱歉，我没有看到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_273B(): pass

    label('loc_273B')

    Jump('loc_27C4')

    def _loc_273E(): pass

    label('loc_273E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_27C4',
    )

    ChrTalk(
        0x00FE,
        (
            '我们就是所谓的登山家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玛诺利亚村一直被认为是\n',
            '古罗尼连峰的登山入口……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们要在这里做好准备，向这座山发起挑战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27C4(): pass

    label('loc_27C4')

    TalkEnd(0x0013)

    Return()

# id: 0x0009 offset: 0x27C8
@scena.Code('func_09_27C8')
def func_09_27C8():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_27D5',
    )

    Jump('loc_2C44')

    def _loc_27D5(): pass

    label('loc_27D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_29F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29B0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0390070175V#750F啊，是你们几个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390070176V我从旅馆的人那里听说了。\n',
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
            '#0010070178V#008F您、您这么说，\n',
            '我们会不好意思的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070179V#008F而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070180V#503F（嗯……现在还是不要\n',
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

    Jump('loc_29F6')

    def _loc_29B0(): pass

    label('loc_29B0')

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

    def _loc_29F6(): pass

    label('loc_29F6')

    Jump('loc_2C44')

    def _loc_29F9(): pass

    label('loc_29F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2A21',
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

    Jump('loc_2C44')

    def _loc_2A21(): pass

    label('loc_2A21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2B30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AD7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0390050988V#750F哎呀，是你们几个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050989V这段时间真的帮了我们大忙啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050990V玛诺利亚村的村民\n',
            '也对我们非常好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050991V#751F真的要感谢大家才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B2D')

    def _loc_2AD7(): pass

    label('loc_2AD7')

    ChrTalk(
        0x00FE,
        (
            '#0390050992V#750F这段时间真的帮了我们大忙啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050993V#751F真的要感谢大家才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B2D(): pass

    label('loc_2B2D')

    Jump('loc_2C44')

    def _loc_2B30(): pass

    label('loc_2B30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2C44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BD4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0390050540V#756F……我已经听玛丽说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050541V怎么会这样呢……\n',
            '那孩子竟然听到了那件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050542V#752F求求你们了。\n',
            '请一定要把克拉姆带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C44')

    def _loc_2BD4(): pass

    label('loc_2BD4')

    ChrTalk(
        0x00FE,
        (
            '#0390050543V#756F怎么会这样呢……\n',
            '那孩子竟然听到了那件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050544V#752F求求你们了。\n',
            '请一定要把克拉姆带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C44(): pass

    label('loc_2C44')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x2C48
@scena.Code('func_0A_2C48')
def func_0A_2C48():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2C55',
    )

    Jump('loc_2D08')

    def _loc_2C55(): pass

    label('loc_2C55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_2CBC',
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

    Jump('loc_2D08')

    def _loc_2CBC(): pass

    label('loc_2CBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2D08',
    )

    ChrTalk(
        0x00FE,
        (
            '#770F约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400061091V我，一定要成为\n',
            '像哥哥一样强的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D08(): pass

    label('loc_2D08')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x2D0C
@scena.Code('func_0B_2D0C')
def func_0B_2D0C():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2D19',
    )

    Jump('loc_2E02')

    def _loc_2D19(): pass

    label('loc_2D19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_2D70',
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

    Jump('loc_2E02')

    def _loc_2D70(): pass

    label('loc_2D70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2DD2',
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

    Jump('loc_2E02')

    def _loc_2DD2(): pass

    label('loc_2DD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2E02',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410050545V大姐姐，克拉姆就拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E02(): pass

    label('loc_2E02')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x2E06
@scena.Code('func_0C_2E06')
def func_0C_2E06():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2E13',
    )

    Jump('loc_2E9B')

    def _loc_2E13(): pass

    label('loc_2E13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_2E4D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420070185V哈～一旦放心下来，\n',
            '肚子就觉得饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E9B')

    def _loc_2E4D(): pass

    label('loc_2E4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2E70',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420061094V呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E9B')

    def _loc_2E70(): pass

    label('loc_2E70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2E9B',
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

    def _loc_2E9B(): pass

    label('loc_2E9B')

    TalkEnd(0x000B)

    Return()

# id: 0x000D offset: 0x2E9F
@scena.Code('func_0D_2E9F')
def func_0D_2E9F():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2EAC',
    )

    Jump('loc_2F4D')

    def _loc_2EAC(): pass

    label('loc_2EAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_2ED8',
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

    Jump('loc_2F4D')

    def _loc_2ED8(): pass

    label('loc_2ED8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_2F05',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430061095V老师……不会有事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F4D')

    def _loc_2F05(): pass

    label('loc_2F05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2F4D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430050547V克拉姆他啊，\n',
            '在吃布丁的时候\n',
            '不知道又在想些什么事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F4D(): pass

    label('loc_2F4D')

    TalkEnd(0x000D)

    Return()

# id: 0x000E offset: 0x2F51
@scena.Code('func_0E_2F51')
def func_0E_2F51():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2FE5',
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

    Jump('loc_3006')

    def _loc_2FE5(): pass

    label('loc_2FE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_3006',
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

    def _loc_3006(): pass

    label('loc_3006')

    TalkEnd(0x0011)

    Return()

# id: 0x000F offset: 0x300A
@scena.Code('func_0F_300A')
def func_0F_300A():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_3082',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_306C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '孤儿院的大家\n',
            '都一边哭一边跑回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事？\n',
            '是谁欺负他们了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3082')

    def _loc_306C(): pass

    label('loc_306C')

    ChrTalk(
        0x00FE,
        (
            '是谁欺负他们了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3082(): pass

    label('loc_3082')

    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x3086
@scena.Code('func_10_3086')
def func_10_3086():
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

    @scena.Lambda('lambda_3217')
    def lambda_3217():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3217)

    @scena.Lambda('lambda_3225')
    def lambda_3225():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3225)

    @scena.Lambda('lambda_3233')
    def lambda_3233():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3233)

    @scena.Lambda('lambda_3241')
    def lambda_3241():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3241)

    @scena.Lambda('lambda_324F')
    def lambda_324F():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_324F)

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

    @scena.Lambda('lambda_32A1')
    def lambda_32A1():
        CameraMove(-50670, 0, -380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32A1)

    @scena.Lambda('lambda_32B9')
    def lambda_32B9():
        ChrMoveTo(0x00FE, -48730, 0, -370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_32B9)

    Sleep(100)

    @scena.Lambda('lambda_32D9')
    def lambda_32D9():
        ChrWalkTo(0x00FE, -49710, 0, 540, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_32D9)

    Sleep(100)

    @scena.Lambda('lambda_32F9')
    def lambda_32F9():
        ChrWalkTo(0x00FE, -49830, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_32F9)

    @scena.Lambda('lambda_3314')
    def lambda_3314():
        ChrWalkTo(0x00FE, -49200, 0, -1200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_3314)

    Sleep(100)

    @scena.Lambda('lambda_3334')
    def lambda_3334():
        ChrWalkTo(0x00FE, -48350, 0, -1070, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3334)

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
            '#0430050295V嘿嘿。\n',
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

    @scena.Lambda('lambda_3460')
    def lambda_3460():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_3460')

    DispatchAsync2(0x000A, 0x0001, lambda_3460)

    @scena.Lambda('lambda_3471')
    def lambda_3471():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3471')

    DispatchAsync2(0x000B, 0x0001, lambda_3471)

    @scena.Lambda('lambda_3482')
    def lambda_3482():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3482')

    DispatchAsync2(0x000D, 0x0001, lambda_3482)

    @scena.Lambda('lambda_3493')
    def lambda_3493():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3493')

    DispatchAsync2(0x000C, 0x0001, lambda_3493)

    @scena.Lambda('lambda_34A4')
    def lambda_34A4():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_34A4')

    DispatchAsync2(0x000E, 0x0001, lambda_34A4)

    @scena.Lambda('lambda_34B5')
    def lambda_34B5():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_34B5')

    DispatchAsync2(0x0136, 0x0001, lambda_34B5)

    @scena.Lambda('lambda_34C6')
    def lambda_34C6():
        ChrWalkTo(0x00FE, -48860, 0, -2920, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_34C6)

    Sleep(500)

    @scena.Lambda('lambda_34E6')
    def lambda_34E6():
        ChrWalkTo(0x00FE, -48100, 0, -2570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_34E6)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_3506')
    def lambda_3506():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3506)

    WaitForThreadExit(0x0102, 0x0002)

    @scena.Lambda('lambda_3519')
    def lambda_3519():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3519)

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

    @scena.Lambda('lambda_377D')
    def lambda_377D():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_377D')

    DispatchAsync2(0x0101, 0x0001, lambda_377D)

    @scena.Lambda('lambda_378E')
    def lambda_378E():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_378E')

    DispatchAsync2(0x0102, 0x0001, lambda_378E)

    Sleep(50)

    @scena.Lambda('lambda_37A4')
    def lambda_37A4():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_37A4')

    DispatchAsync2(0x000A, 0x0001, lambda_37A4)

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    Sleep(50)

    @scena.Lambda('lambda_37CA')
    def lambda_37CA():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_37CA)

    @scena.Lambda('lambda_37D8')
    def lambda_37D8():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_37D8)

    Sleep(50)

    @scena.Lambda('lambda_37EB')
    def lambda_37EB():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_37EB)

    @scena.Lambda('lambda_37F9')
    def lambda_37F9():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_37F9)

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
            '#0430050310V波利要吃布丁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400050311V#773F#3P可、可是姐姐……',
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
            '#0400050314V#774F#4P哎？',
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

    @scena.Lambda('lambda_395B')
    def lambda_395B():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_395B)

    Sleep(600)

    @scena.Lambda('lambda_397B')
    def lambda_397B():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_397B)

    Sleep(50)

    @scena.Lambda('lambda_399B')
    def lambda_399B():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_399B)

    Sleep(200)

    @scena.Lambda('lambda_39BB')
    def lambda_39BB():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_39BB)

    Sleep(300)

    @scena.Lambda('lambda_39DB')
    def lambda_39DB():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_39DB)

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
            '#0020050320V#015F#4P是啊。',
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
            '#0020050325V#012F#4P多谢您的配合。',
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
            '#0390050349V#756F#2P那个人把我们救出来之后，\n',
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
            '#0390050354V#750F#2P是个穿着象牙色外套，\n',
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
            '#0010050362V#002F#4P约修亚？',
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
            '#0010050367V#002F#4P啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0136,
        (
            '#0060050368V#1P……打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrTurnDirection(0x0136, 0x000A, 0)
    ClearChrFlags(0x0136, 0x0080)

    @scena.Lambda('lambda_444E')
    def lambda_444E():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_444E)

    @scena.Lambda('lambda_445C')
    def lambda_445C():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_445C)

    @scena.Lambda('lambda_446A')
    def lambda_446A():
        CameraMove(-49000, 0, -520, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_446A)

    @scena.Lambda('lambda_4482')
    def lambda_4482():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0136, 0x0003, lambda_4482)

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

    @scena.Lambda('lambda_45D9')
    def lambda_45D9():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_45D9')

    DispatchAsync2(0x0136, 0x0001, lambda_45D9)

    @scena.Lambda('lambda_45EA')
    def lambda_45EA():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_45EA')

    DispatchAsync2(0x0101, 0x0001, lambda_45EA)

    @scena.Lambda('lambda_45FB')
    def lambda_45FB():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_45FB')

    DispatchAsync2(0x0102, 0x0001, lambda_45FB)

    @scena.Lambda('lambda_460C')
    def lambda_460C():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_460C')

    DispatchAsync2(0x000A, 0x0001, lambda_460C)

    ClearChrFlags(0x000F, 0x0080)

    @scena.Lambda('lambda_4622')
    def lambda_4622():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_4622)

    @scena.Lambda('lambda_4634')
    def lambda_4634():
        ChrWalkTo(0x00FE, -46810, 0, -650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4634)

    Sleep(500)

    ClearChrFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_4659')
    def lambda_4659():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_4659)

    @scena.Lambda('lambda_466B')
    def lambda_466B():
        ChrWalkTo(0x00FE, -45610, 0, -1440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_466B)

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

    @scena.Lambda('lambda_473F')
    def lambda_473F():
        ChrWalkTo(0x00FE, -48070, 0, 250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_473F)

    Sleep(500)

    @scena.Lambda('lambda_475F')
    def lambda_475F():
        ChrWalkTo(0x00FE, -47210, 0, -920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_475F)

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
            '#0490050416V#664F用不着你多嘴，\n',
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

    @scena.Lambda('lambda_551D')
    def lambda_551D():
        ChrWalkTo(0x00FE, -45280, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_551D)

    WaitForThreadExit(0x000F, 0x0001)

    @scena.Lambda('lambda_553D')
    def lambda_553D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_553D)

    @scena.Lambda('lambda_554F')
    def lambda_554F():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_554F)

    Sleep(300)

    @scena.Lambda('lambda_556F')
    def lambda_556F():
        ChrWalkTo(0x00FE, -45280, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_556F)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_558F')
    def lambda_558F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_558F)

    @scena.Lambda('lambda_55A1')
    def lambda_55A1():
        ChrWalkTo(0x00FE, -44560, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_55A1)

    WaitForThreadExit(0x000F, 0x0001)
    SetChrFlags(0x000F, 0x0080)
    WaitForThreadExit(0x0010, 0x0001)
    SetChrFlags(0x0010, 0x0080)
    Sleep(500)

    PlaySE(7, 0x00, 0x64)

    @scena.Lambda('lambda_55DA')
    def lambda_55DA():
        CameraMove(-49600, 0, -480, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_55DA)

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

    @scena.Lambda('lambda_56A8')
    def lambda_56A8():
        CameraMove(-49200, 0, 70, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_56A8)

    TerminateThread(0x0136, 0xFF)
    ChrWalkTo(0x0136, -48300, 0, -100, 2000, 0x00)
    ChrTurnDirection(0x0136, 0x000A, 400)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_56EB')
    def lambda_56EB():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_56EB)

    @scena.Lambda('lambda_56F9')
    def lambda_56F9():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_56F9)

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
            '#0390050477V#750F艾丝蒂尔、约修亚。',
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
    OP_28(0x003B, 0x01, 0x0080)
    OP_28(0x003B, 0x01, 0x0100)
    OP_28(0x003B, 0x01, 0x0200)
    OP_28(0x003B, 0x01, 0x0400)
    OP_28(0x003C, 0x04, 0x02)
    OP_28(0x003C, 0x04, 0x04)
    OP_28(0x003C, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x5C03
@scena.Code('func_11_5C03')
def func_11_5C03():
    Sleep(1000)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrSetRGBAMask(0x0136, 255, 255, 255, 0, 500)

    Return()

# id: 0x0012 offset: 0x5C1E
@scena.Code('func_12_5C1E')
def func_12_5C1E():
    Sleep(2000)

    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 500)

    Return()

# id: 0x0013 offset: 0x5C2F
@scena.Code('func_13_5C2F')
def func_13_5C2F():
    Sleep(2500)

    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 500)

    Return()

# id: 0x0014 offset: 0x5C40
@scena.Code('func_14_5C40')
def func_14_5C40():
    Sleep(3000)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 500)

    Return()

# id: 0x0015 offset: 0x5C51
@scena.Code('func_15_5C51')
def func_15_5C51():
    Sleep(3500)

    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 500)
    PlaySE(7, 0x00, 0x64)

    Return()

# id: 0x0016 offset: 0x5C67
@scena.Code('func_16_5C67')
def func_16_5C67():
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
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0008)
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

    @scena.Lambda('lambda_5E60')
    def lambda_5E60():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5E60)

    @scena.Lambda('lambda_5E6E')
    def lambda_5E6E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5E6E)

    @scena.Lambda('lambda_5E7C')
    def lambda_5E7C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5E7C)

    @scena.Lambda('lambda_5E8A')
    def lambda_5E8A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5E8A)

    @scena.Lambda('lambda_5E98')
    def lambda_5E98():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5E98)

    ChrTalk(
        0x000E,
        (
            '#0400061011V#775F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061012V哥哥姐姐……',
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
            '#0420061014V呜哇啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0430061015V#5P好可怕啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061016V#008F太好了……\n',
            '大家都平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_5F87')
    def lambda_5F87():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_5F87')

    DispatchAsync2(0x0102, 0x0001, lambda_5F87)

    ChrTalk(
        0x0102,
        (
            '#0020061017V#012F对不起。\n',
            '老师她们的状况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1660061018V放心吧。\n',
            '两人都没受什么伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1660061019V只是一直昏迷不醒，\n',
            '着实让人有些担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061020V#015F……容我失礼一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_6055')
    def lambda_6055():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6055')

    DispatchAsync2(0x0101, 0x0001, lambda_6055)

    @scena.Lambda('lambda_6066')
    def lambda_6066():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6066')

    DispatchAsync2(0x0105, 0x0001, lambda_6066)

    @scena.Lambda('lambda_6077')
    def lambda_6077():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6077')

    DispatchAsync2(0x000E, 0x0001, lambda_6077)

    @scena.Lambda('lambda_6088')
    def lambda_6088():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6088')

    DispatchAsync2(0x000C, 0x0001, lambda_6088)

    @scena.Lambda('lambda_6099')
    def lambda_6099():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6099')

    DispatchAsync2(0x0009, 0x0001, lambda_6099)

    ChrWalkTo(0x0102, -48420, 0, 90, 2000, 0x00)
    ChrWalkTo(0x0102, -49300, 0, 970, 2000, 0x00)

    @scena.Lambda('lambda_60D2')
    def lambda_60D2():
        CameraMove(-52260, 0, -520, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_60D2)

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
            '#0010061022V#580F催、催眠药？',
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
            '#0010061025V#505F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 90, 400)

    @scena.Lambda('lambda_6251')
    def lambda_6251():
        CameraMove(-50370, 0, -640, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6251)

    ChrWalkTo(0x0102, -50560, 0, 240, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061026V#002F对了，克拉姆。\n',
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
            '#0410061028V我来说吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)

    @scena.Lambda('lambda_630B')
    def lambda_630B():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_630B)

    @scena.Lambda('lambda_6319')
    def lambda_6319():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6319)

    Sleep(50)

    @scena.Lambda('lambda_632C')
    def lambda_632C():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_632C)

    @scena.Lambda('lambda_633A')
    def lambda_633A():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_633A)

    Sleep(50)

    @scena.Lambda('lambda_634D')
    def lambda_634D():
        ChrTurnDirection(0x00FE, 0x000C, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_634D)

    @scena.Lambda('lambda_635B')
    def lambda_635B():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_635B)

    Sleep(50)

    TerminateThread(0x000E, 0xFF)
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0410061029V#3P我们……\n',
            '和游击士姐姐一起\n',
            '在海道上走着走着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061030V#3P就在那时，\n',
            '突然出现了几个蒙面的怪人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061031V#3P游击士姐姐\n',
            '虽然想把他们赶走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061032V#3P但是我们很快就被\n',
            '那几个蒙面的怪人包围了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061033V#3P老师也为了保护我们，\n',
            '跟那帮怪人纠缠了起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410061034V#3P……然后就……呜……',
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

    @scena.Lambda('lambda_652D')
    def lambda_652D():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_652D)

    Sleep(50)

    @scena.Lambda('lambda_6540')
    def lambda_6540():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6540)

    Sleep(50)

    @scena.Lambda('lambda_6553')
    def lambda_6553():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6553)

    Sleep(50)

    @scena.Lambda('lambda_6566')
    def lambda_6566():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6566)

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
            '#0020061039V#015F#5P……没这回事。',
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
            '#0410061043V呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061044V#005F不可原谅……！\n',
            '到底是什么人干的好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061045V#047F#2P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061046V#042F#2P现在可以确定的是……\n',
            '那些蒙面人的犯案手段相当老练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061047V连游击士都不是他们对手，\n',
            '甚至还被他们用催眠药弄晕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_67B9')
    def lambda_67B9():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_67B9)

    @scena.Lambda('lambda_67C7')
    def lambda_67C7():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_67C7)

    @scena.Lambda('lambda_67D5')
    def lambda_67D5():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_67D5)

    ChrTurnDirection(0x000E, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061048V#004F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061049V#042F#2P另外还有一点……\n',
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
            '#0020061052V#012F#1P嗯，这种可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061053V#006F科洛丝……\n',
            '看来你终于镇定下来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061054V#043F#2P是的……\n',
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

    PlaySE(6, 0x00, 0x64)
    SetChrChipByIndex(0x0106, 15)

    @scena.Lambda('lambda_69FC')
    def lambda_69FC():
        CameraMove(-49600, 0, -620, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_69FC)

    ClearChrFlags(0x0106, 0x0080)

    @scena.Lambda('lambda_6A19')
    def lambda_6A19():
        ChrWalkTo(0x00FE, -47720, 0, -760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_6A19)

    @scena.Lambda('lambda_6A34')
    def lambda_6A34():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6A34)

    @scena.Lambda('lambda_6A42')
    def lambda_6A42():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6A42)

    @scena.Lambda('lambda_6A50')
    def lambda_6A50():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6A50)

    @scena.Lambda('lambda_6A5E')
    def lambda_6A5E():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6A5E)

    @scena.Lambda('lambda_6A6C')
    def lambda_6A6C():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_6A6C)

    @scena.Lambda('lambda_6A7A')
    def lambda_6A7A():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6A7A)

    @scena.Lambda('lambda_6A88')
    def lambda_6A88():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6A88)

    @scena.Lambda('lambda_6A96')
    def lambda_6A96():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6A96)

    ChrSetRGBAMask(0x0106, 255, 255, 255, 255, 500)
    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010061057V#004F啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061058V#014F阿加特兄……',
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
            '#0010061061V#005F别、别说得好像事不关己一样！',
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
            '#0050061067V#552F嗯，这样啊……\n',
            '不过事情有点古怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061068V#505F古怪？什么古怪？',
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
            '#0010061071V#580F这、这就是说……',
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
            '#0020061073V#012F不，这还不好说。',
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
            '#0010061075V#007F这倒也是……',
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
            '#0020061080V#012F先不说他们是不是犯人，\n',
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
            '#0010061083V#004F什么呀，忽然冒出这一句……',
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
            '#0050061085V#551F你还真是迟钝。\n',
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
            '#0010061088V#004F啊……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061089V#012F明白了，我们跟你一起去。',
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

# id: 0x0017 offset: 0x70C0
@scena.Code('func_17_70C0')
def func_17_70C0():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -49040, 0, -1430, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 400)

    Return()

# id: 0x0018 offset: 0x70E1
@scena.Code('func_18_70E1')
def func_18_70E1():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -48370, 0, -700, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 400)

    Return()

# id: 0x0019 offset: 0x7102
@scena.Code('func_19_7102')
def func_19_7102():
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -49500, 0, -430, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 400)

    Return()

# id: 0x001A offset: 0x7123
@scena.Code('func_1A_7123')
def func_1A_7123():
    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -50110, 0, -750, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x001B offset: 0x7151
@scena.Code('func_1B_7151')
def func_1B_7151():
    Sleep(150)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -49270, 0, -2120, 3000, 0x00)
    SetChrDirection(0x00FE, 0, 400)

    Return()

# id: 0x001C offset: 0x7184
@scena.Code('func_1C_7184')
def func_1C_7184():
    Sleep(100)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -49390, 0, 270, 3000, 0x00)
    SetChrDirection(0x00FE, 180, 400)

    Return()

# id: 0x001D offset: 0x71B7
@scena.Code('func_1D_71B7')
def func_1D_71B7():
    Sleep(50)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, -49880, 0, -1360, 3000, 0x00)
    SetChrDirection(0x00FE, 45, 400)

    Return()

# id: 0x001E offset: 0x71EA
@scena.Code('func_1E_71EA')
def func_1E_71EA():
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
