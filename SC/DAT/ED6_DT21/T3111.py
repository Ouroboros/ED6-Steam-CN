import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3111.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '埃里克',
            x                   = 8650,
            z                   = 0,
            y                   = -1430,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '海泽尔',
            x                   = 0,
            z                   = 0,
            y                   = 6130,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '伊格尔',
            x                   = 7720,
            z                   = 0,
            y                   = 4160,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '佛莱迪',
            x                   = 8830,
            z                   = 0,
            y                   = 3050,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '米拉诺',
            x                   = -6250,
            z                   = 100,
            y                   = -4650,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0135,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '西蒙',
            x                   = -4600,
            z                   = 0,
            y                   = -3500,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '菲',
            x                   = -113390,
            z                   = -4000,
            y                   = -111160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '普罗梅笛',
            x                   = -10070,
            z                   = 0,
            y                   = -200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '诺蒂亚',
            x                   = -10070,
            z                   = 0,
            y                   = -1720,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '鲁迪',
            x                   = -121060,
            z                   = -4000,
            y                   = -111070,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '看板',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 14,
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
            name                = '临时',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 14,
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
            name                = '大叔',
            x                   = -225250,
            z                   = 0,
            y                   = 17330,
            direction           = 160,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = -108560,
            z                   = 0,
            y                   = -105400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
    )

# id: 0x10002 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 50,
            triggerZ            = 0,
            triggerY            = 3900,
            triggerRange        = 400,
            actorX              = 0,
            actorZ              = 1500,
            actorY              = 6130,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6900,
            triggerZ            = 0,
            triggerY            = -1410,
            triggerRange        = 400,
            actorX              = 8650,
            actorZ              = 1500,
            actorY              = -1430,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -200120,
            triggerZ            = 0,
            triggerY            = 118010,
            triggerRange        = 1200,
            actorX              = -200120,
            actorZ              = 1500,
            actorY              = 118010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -121030,
            triggerZ            = -4000,
            triggerY            = -99900,
            triggerRange        = 800,
            actorX              = -121030,
            actorZ              = -3000,
            actorY              = -99900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x37A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BA',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_3B7',
    )

    ChrClearFlags(0x0016, 0x0080)

    def _loc_3B7(): pass

    label('loc_3B7')

    Jump('loc_3FD')

    def _loc_3BA(): pass

    label('loc_3BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3DF',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -113390, -4000, -111160, 0)

    Jump('loc_3FD')

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_3E9',
    )

    Jump('loc_3FD')

    def _loc_3E9(): pass

    label('loc_3E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3FD',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_3FD')

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_429',
    )

    ChrSetPos(0x000E, -116160, -4000, -113310, 90)

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 7, 0x2037)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45D',
    )

    MapSetFlags(0x10000000)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_44F'),
        (0x00000067, 'loc_456'),
        (-1, 'loc_45D'),
    )

    def _loc_44F(): pass

    label('loc_44F')

    Event(0, func_12_6463)

    Jump('loc_45D')

    def _loc_456(): pass

    label('loc_456')

    Event(0, func_17_6B5B)

    Jump('loc_45D')

    def _loc_45D(): pass

    label('loc_45D')

    Return()

# id: 0x0001 offset: 0x45E
@scena.Code('func_01_45E')
def func_01_45E():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_558',
    )

    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0003, 0)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0001, 29)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0002, 29)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0004, 29)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0005, 29)
    OP_72(0x0005, 0x0010)
    OP_6F(0x0007, 29)
    OP_72(0x0007, 0x0010)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_71(0x0016, 0x0004)
    OP_71(0x0017, 0x0004)
    OP_71(0x0018, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_7A(0x3D, 0x0002)
    OP_7A(0x3E, 0x0002)
    OP_7A(0x3F, 0x0002)
    OP_7B()
    OP_72(0x001A, 0x0004)
    OP_72(0x001B, 0x0004)
    OP_72(0x001C, 0x0004)
    OP_72(0x001D, 0x0004)
    OP_72(0x001E, 0x0004)
    OP_72(0x001F, 0x0004)
    OP_76(0x00FF, 0x00000016, 0x0000, 0, 0, 0, 0x00, 0x00)
    OP_10(0x01, 0x00)
    OP_10(0x06, 0x00)

    Jump('loc_56E')

    def _loc_558(): pass

    label('loc_558')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_562',
    )

    Jump('loc_56E')

    def _loc_562(): pass

    label('loc_562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_56E',
    )

    def _loc_56E(): pass

    label('loc_56E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_57E'),
        (0x0000006D, 'loc_57E'),
        (-1, 'loc_5B7'),
    )

    def _loc_57E(): pass

    label('loc_57E')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A3',
    )

    OP_75(0xFF, 0x00000016, 0x05)

    Jump('loc_5B4')

    def _loc_5A3(): pass

    label('loc_5A3')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B4',
    )

    PlaySE(160, 0x01, 0x64)

    def _loc_5B4(): pass

    label('loc_5B4')

    Jump('loc_5BD')

    def _loc_5B7(): pass

    label('loc_5B7')

    OP_23(0x00A0)

    Jump('loc_5BD')

    def _loc_5BD(): pass

    label('loc_5BD')

    Return()

# id: 0x0002 offset: 0x5BE
@scena.Code('func_02_5BE')
def func_02_5BE():
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x5C6
@scena.Code('func_03_5C6')
def func_03_5C6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6BF',
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
            TXT(0x01, '工作取消\n'),
            TXT(0x02, '改造·换钱\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_650',
    )

    Call(1, 0x0008)

    Jump('loc_683')

    def _loc_650(): pass

    label('loc_650')

    Call(1, 0x0009)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_668',
    )

    Call(1, 0x000C)

    Jump('loc_683')

    def _loc_668(): pass

    label('loc_668')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_683',
    )

    Call(1, 0x000B)

    def _loc_683(): pass

    label('loc_683')

    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

    def _loc_68A(): pass

    label('loc_68A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A2',
    )

    Call(1, 0x000A)
    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

    def _loc_6A2(): pass

    label('loc_6A2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B8',
    )

    OP_A9(0x96)
    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

    def _loc_6B8(): pass

    label('loc_6B8')

    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

    def _loc_6BF(): pass

    label('loc_6BF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_711',
    )

    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FA',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_6F1',
    )

    OP_A9(0x9F)

    Jump('loc_6F3')

    def _loc_6F1(): pass

    label('loc_6F1')

    OP_A9(0x96)

    def _loc_6F3(): pass

    label('loc_6F3')

    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

    def _loc_6FA(): pass

    label('loc_6FA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_70E',
    )

    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

    def _loc_70E(): pass

    label('loc_70E')

    Jump('loc_11CF')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11CF',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 6700, 0, -1700, 90)
    ChrSetPos(0x0102, 6500, 0, -900, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_778',
    )

    ChrSetPos(0x00F9, 5500, 0, -1300, 90)
    ChrSetPos(0x00F8, 5300, 0, -400, 90)

    Jump('loc_79A')

    def _loc_778(): pass

    label('loc_778')

    ChrSetPos(0x00F8, 5500, 0, -1300, 90)
    ChrSetPos(0x00F9, 5300, 0, -400, 90)

    def _loc_79A(): pass

    label('loc_79A')

    ChrSetDirection(0x0008, 270, 0)
    CameraMove(7160, 0, -820, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '真是不好意思，\n',
            '工房现在停业中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '加工用的器材\n',
            '现在都无法运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_869',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，那个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们带了好东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎，究竟是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CDA')

    def _loc_869(): pass

    label('loc_869')

    ChrTalk(
        0x0101,
        (
            '#1026F#4P啊，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯……不过正伤脑筋啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结晶回路的合成和结晶孔的强化\n',
            '都完全不能进行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_912',
    )

    ChrTalk(
        0x0103,
        (
            '#025F嗯嗯，难得的发生器\n',
            '真是暴殄天物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99F')

    def _loc_912(): pass

    label('loc_912')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_951',
    )

    ChrTalk(
        0x0108,
        (
            '#072F唔，难得的发生器\n',
            '也只能暴殄天物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_99F')

    def _loc_951(): pass

    label('loc_951')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_99F',
    )

    ChrTalk(
        0x0106,
        (
            '#552F啊啊，难得使用发生器\n',
            '能使用魔法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是暴殄天物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_99F(): pass

    label('loc_99F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F4',
    )

    ChrTalk(
        0x0107,
        (
            '#064F啊，不过姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果只是一小会儿，\n',
            '或许能用也说不定哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A42')

    def _loc_9F4(): pass

    label('loc_9F4')

    ChrTalk(
        0x0102,
        (
            '#1043F#1P确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F不过，如果只是一小会儿\n',
            '或许能用也说不定哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A42(): pass

    label('loc_A42')

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AB1',
    )

    @scena.Lambda('lambda_0A72')
    def lambda_0A72():
        ChrTurnDirection(0x0000, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A72)

    Sleep(120)

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        ChrTurnDirection(0x0001, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0A85)

    @scena.Lambda('lambda_0A93')
    def lambda_0A93():
        ChrTurnDirection(0x0002, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0A93)

    Sleep(120)

    @scena.Lambda('lambda_0AA6')
    def lambda_0AA6():
        ChrTurnDirection(0x0003, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0AA6)

    Jump('loc_AB8')

    def _loc_AB1(): pass

    label('loc_AB1')

    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_AB8(): pass

    label('loc_AB8')

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#1004F#4P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B15',
    )

    ChrTalk(
        0x0106,
        (
            '#052F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B70')

    def _loc_B15(): pass

    label('loc_B15')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B43',
    )

    ChrTalk(
        0x0103,
        (
            '#023F能让工房运作起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B70')

    def _loc_B43(): pass

    label('loc_B43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B70',
    )

    ChrTalk(
        0x0108,
        (
            '#073F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B70(): pass

    label('loc_B70')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BB2',
    )

    ChrTalk(
        0x0107,
        (
            '#060F是，是，大概……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '用那个发生器的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF8')

    def _loc_BB2(): pass

    label('loc_BB2')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P是，恐怕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果使用那个发生器\n',
            '应该能在短时间内复原。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF8(): pass

    label('loc_BF8')

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，原来如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C56',
    )

    ChrTalk(
        0x0008,
        (
            '那个，提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个发生器是什么东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C84')

    def _loc_C56(): pass

    label('loc_C56')

    ChrTalk(
        0x0008,
        (
            '那个，诸位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个发生器是什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C84(): pass

    label('loc_C84')

    @scena.Lambda('lambda_0C8A')
    def lambda_0C8A():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C8A)

    Sleep(120)

    @scena.Lambda('lambda_0C9D')
    def lambda_0C9D():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0C9D)

    @scena.Lambda('lambda_0CAB')
    def lambda_0CAB():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0CAB)

    Sleep(120)

    @scena.Lambda('lambda_0CBE')
    def lambda_0CBE():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0CBE)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    def _loc_CDA(): pass

    label('loc_CDA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D08',
    )

    ChrTalk(
        0x0107,
        (
            '#560F嗯、其实是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D29')

    def _loc_D08(): pass

    label('loc_D08')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那个，是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D29(): pass

    label('loc_D29')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了使用『零力场发生器』\n',
            '可暂时恢复工房机能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '啊啊！拉赛尔博士\n',
            '最新发明的发生器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请一定拿来试试看啊，\n',
            '能不能马上借我用用？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F#4P啊、嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E96',
    )

    ChrTalk(
        0x0107,
        (
            '#560F那么～埃里克先生。\n',
            '可以帮我一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，没问题，不过我手脚比较笨，\n',
            '还要请你多指教了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED7')

    def _loc_E96(): pass

    label('loc_E96')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P发生器的设置\n',
            '交给你可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然。\n',
            '稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ED7(): pass

    label('loc_ED7')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    PlaySE(157, 0x00, 0x64)
    ChrSetDirection(0x0008, 270, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用『零力场发生器』将工房机能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetPos(0x0008, 9890, 0, 2600, 180)

    @scena.Lambda('lambda_0F43')
    def lambda_0F43():
        ChrWalkTo(0x0008, 9890, 0, -130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F43)

    @scena.Lambda('lambda_0F5E')
    def lambda_0F5E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0F5E')

    DispatchAsync2(0x0000, 0x0001, lambda_0F5E)

    @scena.Lambda('lambda_0F6F')
    def lambda_0F6F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0F6F')

    DispatchAsync2(0x0001, 0x0001, lambda_0F6F)

    @scena.Lambda('lambda_0F80')
    def lambda_0F80():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0F80')

    DispatchAsync2(0x0002, 0x0001, lambda_0F80)

    @scena.Lambda('lambda_0F91')
    def lambda_0F91():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0F91')

    DispatchAsync2(0x0003, 0x0001, lambda_0F91)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0008, 0x0001)
    ChrWalkTo(0x0008, 8650, 0, -1430, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    OP_0D()
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)

    ChrTalk(
        0x0008,
        (
            '嗯，器材确实是\n',
            '可以运转了，不过…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从原理上来看的话，\n',
            '应该只是一时性的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1076',
    )

    ChrTalk(
        0x0107,
        (
            '#063F嗯，确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F过一阵子就应该\n',
            '恢复原状了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B4')

    def _loc_1076(): pass

    label('loc_1076')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '经过一段时间后\n',
            '就会再次停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10B4(): pass

    label('loc_10B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_10CE',
    )

    Jump('loc_1102')

    def _loc_10CE(): pass

    label('loc_10CE')

    ChrTalk(
        0x0101,
        (
            '#1007F#4P是、是吗……\n',
            '看来是个应急型的装置啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1102(): pass

    label('loc_1102')

    ChrTalk(
        0x0008,
        (
            '原来如此，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不管怎样，趁现在可以\n',
            '好好利用一下工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x9F)
    OP_56(0x00)
    OP_0D()
    Sleep(30)

    ChrTalk(
        0x0008,
        (
            '使用这种方法的话，\n',
            '随时都可以使用工房哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟是博士辛苦发明出来的东西，\n',
            '我们要好好利用才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041C, 4, 0x20E4))
    EventEnd(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_11CF(): pass

    label('loc_11CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_12AD',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1228',
    )

    ChrTalk(
        0x0008,
        (
            '各位，今天真是谢谢了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以后再有什么事情的话\n',
            '还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AA')

    def _loc_1228(): pass

    label('loc_1228')

    ChrTalk(
        0x0008,
        (
            '今天虽然很遗憾，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟是我的失误，\n',
            '只能靠自己的力量来试着解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果以后再有什么事情的话\n',
            '还请多多关照了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AA(): pass

    label('loc_12AA')

    Jump('loc_1AB8')

    def _loc_12AD(): pass

    label('loc_12AD')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12E8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_12E1',
    )

    Call(1, 0x0006)

    Jump('loc_12E5')

    def _loc_12E1(): pass

    label('loc_12E1')

    Call(1, 0x0005)

    def _loc_12E5(): pass

    label('loc_12E5')

    Jump('loc_1AB8')

    def _loc_12E8(): pass

    label('loc_12E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_13A5',
    )

    ChrTalk(
        0x0008,
        (
            '如果零导力发生器可以量产的话\n',
            '也许就可以平息这次的混乱了吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过这样复杂的高端装置，\n',
            '要想量产化实在是太困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过如果是拉赛尔博士的话，\n',
            '也没准可以创造出奇迹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB8')

    def _loc_13A5(): pass

    label('loc_13A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1444',
    )

    ChrTalk(
        0x0008,
        (
            '哈～总之全靠大家，\n',
            '这里又可以开始工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看过那发生器的效果之后\n',
            '我又变得干劲十足了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '能将人类从危机中拯救的\n',
            '果然还是只有导力技术啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB8')

    def _loc_1444(): pass

    label('loc_1444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1600',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1511',
    )

    ChrTalk(
        0x0008,
        (
            '中央工房的工房长\n',
            '在这里的地位就相当于市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然有些人对安全宣言抱有怀疑，\n',
            '但从行政方面考虑，这也是最正确的办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_150E',
    )

    ChrTalk(
        0x0008,
        (
            '……那个暂且不说了，\n',
            '现在最重要的是我的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_150E(): pass

    label('loc_150E')

    Jump('loc_15FD')

    def _loc_1511(): pass

    label('loc_1511')

    ChrTalk(
        0x0008,
        (
            '啊，大家听说了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '玛多克工房长已经发表了\n',
            '有关地震的安全宣言呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '既然是有科学根据的发言，\n',
            '我们也就可以放心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '工房长那么说的话，\n',
            '大家就可以安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15FA',
    )

    ChrTalk(
        0x0008,
        (
            '……那个暂且不说了，\n',
            '现在最重要的是我的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15FA(): pass

    label('loc_15FA')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_15FD(): pass

    label('loc_15FD')

    Jump('loc_1AB8')

    def _loc_1600(): pass

    label('loc_1600')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_17D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_16B4',
    )

    ChrTalk(
        0x0008,
        (
            '听传闻说，新来的女实习生\n',
            '是以前某个知名人士\n',
            '的孙女呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '同、同样是实习生，\n',
            '我也绝对不会输给她的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16B1',
    )

    ChrTalk(
        0x0008,
        (
            '呼～还是先考虑自己的工作\n',
            '该怎么办吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16B1(): pass

    label('loc_16B1')

    Jump('loc_17D5')

    def _loc_16B4(): pass

    label('loc_16B4')

    ChrTalk(
        0x0008,
        (
            '呀，各位。\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，有个见习职员已经\n',
            '过来了，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说那个新来的小姑娘\n',
            '是以前某个知名人士\n',
            '的孙女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样看的话，虽然是个普通女孩，\n',
            '但肯定会有过人之处吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '同、同样是实习生，\n',
            '我也绝不能输给她的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D2',
    )

    ChrTalk(
        0x0008,
        (
            '呼～还是先考虑自己的工作\n',
            '该怎么办吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D2(): pass

    label('loc_17D2')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_17D5(): pass

    label('loc_17D5')

    Jump('loc_1AB8')

    def _loc_17D8(): pass

    label('loc_17D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_193A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1881',
    )

    ChrTalk(
        0x0008,
        (
            '新型导力器能普及，\n',
            '中央工房实在功不可没。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在也有洛连特的人\n',
            '来这里进行研修呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_187E',
    )

    ChrTalk(
        0x0008,
        (
            '……那个暂且不说了，\n',
            '现在最重要的是我的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_187E(): pass

    label('loc_187E')

    Jump('loc_1937')

    def _loc_1881(): pass

    label('loc_1881')

    ChrTalk(
        0x0008,
        (
            '呀，各位。\n',
            '上次真是多谢你们了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '新型的导力器\n',
            '用得习惯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之，努力去习惯吧，\n',
            '多试试它的各种新功能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1934',
    )

    ChrTalk(
        0x0008,
        (
            '……那个暂且不说了，\n',
            '现在最重要的是我的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1934(): pass

    label('loc_1934')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_1937(): pass

    label('loc_1937')

    Jump('loc_1AB8')

    def _loc_193A(): pass

    label('loc_193A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_19F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1988',
    )

    ChrTalk(
        0x0008,
        (
            '很久没有在工作中\n',
            '遇到失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，该怎么做呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F5')

    def _loc_1988(): pass

    label('loc_1988')

    ChrTalk(
        0x0008,
        (
            '地震没有造成重大损害\n',
            '虽然很好，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很不幸的是，\n',
            '我这里却发生了故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，真是认命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_19F5(): pass

    label('loc_19F5')

    Jump('loc_1AB8')

    def _loc_19F8(): pass

    label('loc_19F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1AB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1A6B',
    )

    ChrTalk(
        0x0008,
        (
            '已经检查过部件了，\n',
            '似乎没有因为地震而受到损坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈～那么小的震动，\n',
            '我就知道不会有事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB8')

    def _loc_1A6B(): pass

    label('loc_1A6B')

    ChrTalk(
        0x0008,
        (
            '欢迎光临中央工房\n',
            '的维修窗口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要是有什么需要帮忙的\n',
            '请尽管说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1AB8(): pass

    label('loc_1AB8')

    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1ABF
@scena.Code('func_04_1ABF')
def func_04_1ABF():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x1AC4
@scena.Code('func_05_1AC4')
def func_05_1AC4():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1EF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 4, 0x20CC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D0C',
    )

    ChrTalk(
        0x0009,
        (
            '啊，是各位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F海泽尔小姐，你还好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么回事，好像\n',
            '这里好像很昏暗啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '啊，至少有油灯，\n',
            '还不要紧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过大部分的研究工作\n',
            '都被迫中止了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果没有导力，\n',
            '任何实验器材也都无法运转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BE1',
    )

    ChrTalk(
        0x0107,
        (
            '#561F啊……是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BFB')

    def _loc_1BE1(): pass

    label('loc_1BE1')

    ChrTalk(
        0x0101,
        (
            '#1007F啊……确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BFB(): pass

    label('loc_1BFB')

    ChrTalk(
        0x0102,
        (
            '#1043F情况似乎比预想中的\n',
            '还要严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '但我觉得现在这种时候，\n',
            '中央工房更要发挥自己的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了早日重新恢复研究工作，\n',
            '大家都在拼命努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，如果有什么我可以帮忙的\n',
            '请尽管说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '各位，谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '像现在这种时候，\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    SetScenaFlags(ScenaFlag(0x0419, 4, 0x20CC))

    Jump('loc_1EEE')

    def _loc_1D0C(): pass

    label('loc_1D0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D6E',
    )

    ChrTalk(
        0x0009,
        (
            '中央工房更要发挥\n',
            '自己的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了让研究工作重新展开，\n',
            '我们也要努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EEE')

    def _loc_1D6E(): pass

    label('loc_1D6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1E9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E3B',
    )

    ChrTalk(
        0x0009,
        (
            '在这里的屋顶上\n',
            '可以清楚地看见浮游物体哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '刚才还有一名带着孩子的绅士\n',
            '来这里参观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '在这种时候竟然还有兴致\n',
            '特意来参观……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呵呵呵，好奇心旺盛\n',
            '是这里市民们的特点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1E97')

    def _loc_1E3B(): pass

    label('loc_1E3B')

    ChrTalk(
        0x0009,
        (
            '在这里的屋顶上\n',
            '可以清楚地看见浮游物体哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '刚才还有一名绅士带着孩子\n',
            '来这里参观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E97(): pass

    label('loc_1E97')

    Jump('loc_1EEE')

    def _loc_1E9A(): pass

    label('loc_1E9A')

    ChrTalk(
        0x0009,
        (
            '中央工房更要发挥\n',
            '自己的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了让研究工作重新展开，\n',
            '我们也要努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EEE(): pass

    label('loc_1EEE')

    Jump('loc_287C')

    def _loc_1EF1(): pass

    label('loc_1EF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2148',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 7, 0x163F)),
            Expr.Return,
        ),
        'loc_1F2D',
    )

    ChrTalk(
        0x0009,
        (
            '提妲\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，请小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2145')

    def _loc_1F2D(): pass

    label('loc_1F2D')

    ChrTalk(
        0x0009,
        (
            '哎呀，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我听说了哦！\n',
            '你们要离开蔡斯了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，这次是要去王都呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '听说王国军那边\n',
            '发来委托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '呼～还真是忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '工作虽然重要，但请各位\n',
            '还是要注意身体啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '年轻人可不能太勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F哈哈，谢谢啦。\n',
            '我们会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20A8',
    )

    ChrTalk(
        0x0009,
        (
            '那么，提妲\n',
            '就拜托大家照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '提妲，\n',
            '你也不要太乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F是的，我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20C7')

    def _loc_20A8(): pass

    label('loc_20A8')

    ChrTalk(
        0x0009,
        (
            '提妲也\n',
            '就拜托大家照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C7(): pass

    label('loc_20C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_20E8',
    )

    ChrTalk(
        0x0106,
        (
            '#050F嗯，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2101')

    def _loc_20E8(): pass

    label('loc_20E8')

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2101(): pass

    label('loc_2101')

    ChrTalk(
        0x0101,
        (
            '#1011F那么先这样，海泽尔小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，到王都\n',
            '也要小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C7, 7, 0x163F))

    def _loc_2145(): pass

    label('loc_2145')

    Jump('loc_287C')

    def _loc_2148(): pass

    label('loc_2148')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 1, 0x1429)),
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2394',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2248',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_21C5',
    )

    ChrTalk(
        0x0009,
        (
            '亚尔摩村那边\n',
            '已经联系过了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '玛多克工房长已经\n',
            '把事情经过说明了，\n',
            '他们一定会协助你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2245')

    def _loc_21C5(): pass

    label('loc_21C5')

    ChrTalk(
        0x0009,
        (
            '亚尔摩村那边\n',
            '已经联系过了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '玛多克工房长已经\n',
            '把事情经过说明了，\n',
            '他们一定会协助你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，请大家多小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2245(): pass

    label('loc_2245')

    Jump('loc_2391')

    def _loc_2248(): pass

    label('loc_2248')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_229A',
    )

    ChrTalk(
        0x0009,
        (
            '拉赛尔博士\n',
            '在５层的演算室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请乘坐\n',
            '左边的电梯上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2391')

    def _loc_229A(): pass

    label('loc_229A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_22F0',
    )

    ChrTalk(
        0x0009,
        (
            '拉赛尔博士刚才\n',
            '风风火火就赶回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看来是又想起\n',
            '什么新实验了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2391')

    def _loc_22F0(): pass

    label('loc_22F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2332',
    )

    ChrTalk(
        0x0009,
        (
            '拉赛尔博士\n',
            '好像去协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '大概是去\n',
            '等你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2391')

    def _loc_2332(): pass

    label('loc_2332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2391',
    )

    ChrTalk(
        0x0009,
        (
            '现在还没有接到地震\n',
            '的受灾报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '市区这边应该没出什么事，\n',
            '总算是可以放心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2391(): pass

    label('loc_2391')

    Jump('loc_287C')

    def _loc_2394(): pass

    label('loc_2394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2446',
    )

    ChrTurnDirection(0x0009, 0x0101, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F啊，海泽尔小姐。\n',
            '好久不见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊！好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)

    ChrTalk(
        0x0009,
        (
            '二位都还和从前一样，\n',
            '真是太好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24C7')

    def _loc_2446(): pass

    label('loc_2446')

    ChrTurnDirection(0x0009, 0x0101, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊～还以为是谁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F啊，海泽尔小姐。\n',
            '好久不见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '还和从前一样，真是太好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24C7(): pass

    label('loc_24C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_25AC',
    )

    ChrTalk(
        0x0009,
        (
            '对了，拉赛尔博士\n',
            '在演算室等着你们呢，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他让我在你们回来之后\n',
            '通知你们一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '演算室就在５层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请乘坐\n',
            '左边的电梯上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F谢谢啦，是５层吗，\n',
            '那么这就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2879')

    def _loc_25AC(): pass

    label('loc_25AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_26C3',
    )

    ChrTalk(
        0x0009,
        (
            '不过、原来如此……\n',
            '果然是如此吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F哎，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '嗯～雾香小姐\n',
            '说过要请求支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我就知道来的\n',
            '会是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，在蔡斯的期间\n',
            '请继续关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，加油工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，海泽尔小姐也是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2879')

    def _loc_26C3(): pass

    label('loc_26C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2769',
    )

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '对了，拉赛尔博士\n',
            '好像是去协会了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '似乎是要在那里\n',
            '等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F谢啦，那就赶快\n',
            '去协会看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '工作要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2879')

    def _loc_2769(): pass

    label('loc_2769')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2879',
    )

    ChrTalk(
        0x0009,
        (
            '不过、原来如此……\n',
            '果然是如此吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F哎，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '嗯～雾香小姐\n',
            '说过要请求支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我就知道来的\n',
            '会是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊，是这样呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，在蔡斯的期间\n',
            '请继续关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，加油工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，海泽尔也是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2879(): pass

    label('loc_2879')

    SetScenaFlags(ScenaFlag(0x0285, 1, 0x1429))
    def _loc_287C(): pass

    label('loc_287C')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x2880
@scena.Code('func_06_2880')
def func_06_2880():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_299A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_28EE',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，工房船似乎顺利\n',
            '出发了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来『埃尔赛尤』终于\n',
            '可以拥有自己的双翼了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2997')

    def _loc_28EE(): pass

    label('loc_28EE')

    ChrTalk(
        0x00FE,
        (
            '呼，工房船似乎顺利\n',
            '出发了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来『埃尔赛尤』终于\n',
            '可以拥有自己的双翼了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新型引擎的开发\n',
            '比预想的要迟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』大概\n',
            '早就迫不及待了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2997(): pass

    label('loc_2997')

    Jump('loc_2C98')

    def _loc_299A(): pass

    label('loc_299A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2A97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2A01',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，我也要准备修理一下\n',
            '城里的时钟了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些什么新型引擎\n',
            '实在是搞不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A94')

    def _loc_2A01(): pass

    label('loc_2A01')

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』的工事\n',
            '好像已经开始准备了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这次没有我什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这老家伙现在只剩下理论了，\n',
            '还是那些现役的小子更能派上用场啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2A94(): pass

    label('loc_2A94')

    Jump('loc_2C98')

    def _loc_2A97(): pass

    label('loc_2A97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2B6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2AEB',
    )

    ChrTalk(
        0x00FE,
        (
            '特意来学习新型导力器\n',
            '的基础理论……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这才是像样的职业人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B6C')

    def _loc_2AEB(): pass

    label('loc_2AEB')

    ChrTalk(
        0x00FE,
        (
            '那小子不但是我的弟子，\n',
            '更是一名合格的职业人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特意从洛连特过来\n',
            '进行新型导力技术的研修。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，不愧是我的弟子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2B6C(): pass

    label('loc_2B6C')

    Jump('loc_2C98')

    def _loc_2B6F(): pass

    label('loc_2B6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2C98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2BFA',
    )

    ChrTalk(
        0x00FE,
        (
            '最近的年轻研究员们\n',
            '太不争气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候\n',
            '就算周围着火\n',
            '也都会继续研究的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拉赛尔那家伙\n',
            '实在是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C98')

    def _loc_2BFA(): pass

    label('loc_2BFA')

    ChrTalk(
        0x00FE,
        (
            '真是一群没用的小子，\n',
            '一点地震就给吓成那副德性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候\n',
            '就算周围着火\n',
            '也都会继续研究的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看看拉赛尔吧，\n',
            '他的头发都快被研究\n',
            '累得掉光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2C98(): pass

    label('loc_2C98')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x2C9C
@scena.Code('func_07_2C9C')
def func_07_2C9C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 2, 0x142A)),
            Expr.Return,
        ),
        'loc_30A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_305E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2E1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2D11',
    )

    ChrTalk(
        0x00FE,
        (
            '我准备再过一阵子\n',
            '就回洛连特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次再来我店时\n',
            '会让你好好看看我的成果！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E1A')

    def _loc_2D11(): pass

    label('loc_2D11')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '对了，艾丝蒂尔你\n',
            '准备什么时候回洛连特呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F接下来我们要先去王都，\n',
            '回洛连特大概还要过一阵子了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F佛莱迪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近就要回去了，\n',
            '研修已经快结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次再来我的店时\n',
            '会让你好好看看我的成果！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F哈哈，那真是不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2E1A(): pass

    label('loc_2E1A')

    Jump('loc_305B')

    def _loc_2E1D(): pass

    label('loc_2E1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2E8F',
    )

    ChrTalk(
        0x00FE,
        (
            '新型的战术导力器\n',
            '增加了１个结晶孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然性能因此而大大提升了，\n',
            '但结晶回路的组合却也更麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_305B')

    def _loc_2E8F(): pass

    label('loc_2E8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2FFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2F25',
    )

    ChrTalk(
        0x00FE,
        (
            '我从父亲那里学到了\n',
            '七耀石的加工技术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '向伊格尔老师学习到了\n',
            '结晶回路的理论知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些东西都是我人生中\n',
            '最宝贵的财富。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF7')

    def _loc_2F25(): pass

    label('loc_2F25')

    ChrTalk(
        0x00FE,
        (
            '伊格尔先生是我\n',
            '以前的老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也算是有缘，这次的研修\n',
            '又要麻烦他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从父亲那里学到了\n',
            '七耀石的加工技术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '向伊格尔老师学习到了\n',
            '结晶回路的理论知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些东西都是我人生中\n',
            '最宝贵的财富。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2FF7(): pass

    label('loc_2FF7')

    Jump('loc_305B')

    def _loc_2FFA(): pass

    label('loc_2FFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_305B',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国是很少\n',
            '发生地震的哦，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论是在洛连特还是蔡斯，\n',
            '以前好像都从没发生过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_305B(): pass

    label('loc_305B')

    Jump('loc_30A4')

    def _loc_305E(): pass

    label('loc_305E')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '做的好像很不错，\n',
            '今天真是放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，工作加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_30A4(): pass

    label('loc_30A4')

    Jump('loc_36BB')

    def _loc_30A7(): pass

    label('loc_30A7')

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊、那个……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3102',
    )

    ChrTalk(
        0x00FE,
        (
            '这不是艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_312D')

    def _loc_3102(): pass

    label('loc_3102')

    ChrTalk(
        0x00FE,
        (
            '艾、艾丝蒂尔！\n',
            '而且连雪拉扎德也在？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_312D(): pass

    label('loc_312D')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F佛莱迪！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为、为什么佛莱迪\n',
            '会在这里呀？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_31E7',
    )

    ChrTalk(
        0x0106,
        (
            '#052F熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，你应该在\n',
            '洛连特的工房才是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1004F店里没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Jump('loc_3225')

    def _loc_31E7(): pass

    label('loc_31E7')

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，世界还真是小啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '洛连特的店不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    def _loc_3225(): pass

    label('loc_3225')

    ChrTalk(
        0x00FE,
        (
            '啊，把工房交给爸爸以后，\n',
            '我就来中央工房研修了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能在这里学到最新的\n',
            '导力技术知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F嘿～还有这样的研修啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F说起来的话，佛莱迪\n',
            '好像以前也在这里学习过吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯～年轻的时候曾经在这里\n',
            '学习过基础知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～其实现在学习的一样也是\n',
            '新型的基础知识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_347D',
    )

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '约修亚没和你在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F啊、啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F发生了一点事情呢，\n',
            '现在我们暂时分别行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，那可真遗憾。\n',
            '我还挺想约修亚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，今天能遇到艾丝蒂尔\n',
            '就已经很高兴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以在这里给你爸爸\n',
            '买些礼物哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那么，加油工作吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，佛莱迪\n',
            '也加油研修吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36B5')

    def _loc_347D(): pass

    label('loc_347D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_3580',
    )

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '你们看起来好像很忙啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F啊、嗯！有些\n',
            '很紧急的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3503',
    )

    ChrTalk(
        0x0106,
        (
            '#050F就是那样啦，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不好意思，先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3530')

    def _loc_3503(): pass

    label('loc_3503')

    ChrTalk(
        0x0103,
        (
            '#020F就是那样了哦，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '抱歉，我们先走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3530(): pass

    label('loc_3530')

    ChrTurnDirection(0x00FE, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '啊～这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，工作加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，努力研修吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36B5')

    def _loc_3580(): pass

    label('loc_3580')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_36B5',
    )

    ChrTalk(
        0x00FE,
        (
            '不过…\n',
            '约修亚没和你在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F啊、啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F发生了一点事情呢，\n',
            '现在我们暂时分别行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，那可真遗憾。\n',
            '我还挺想约修亚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，今天能遇到艾丝蒂尔\n',
            '就已经很高兴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以在这里给你爸爸\n',
            '买些礼物哦，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那么，加油工作吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，佛莱迪\n',
            '也加油研修吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36B5(): pass

    label('loc_36B5')

    SetScenaFlags(ScenaFlag(0x0285, 2, 0x142A))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    def _loc_36BB(): pass

    label('loc_36BB')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x36BF
@scena.Code('func_08_36BF')
def func_08_36BF():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_37D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_372B',
    )

    ChrTalk(
        0x00FE,
        (
            '那个引擎的贩卖权，\n',
            '要想办法争取来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是得到的话，\n',
            '比交给国家要有效率多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37D6')

    def _loc_372B(): pass

    label('loc_372B')

    ChrTalk(
        0x00FE,
        (
            '听说新型的引擎\n',
            '也是这里制造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个引擎的贩卖权，\n',
            '要想办法争取来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是得到的话，\n',
            '比交给国家要有效率多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但税金会增加，\n',
            '而且推广也会更迅速。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_37D6(): pass

    label('loc_37D6')

    Jump('loc_3A40')

    def _loc_37D9(): pass

    label('loc_37D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_38B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_383B',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的研究室\n',
            '创造过很多\n',
            '惊世的发明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有时间的话\n',
            '真想去参观一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38AF')

    def _loc_383B(): pass

    label('loc_383B')

    ChrTalk(
        0x00FE,
        (
            '这里也许还有很多\n',
            '惊世的发明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有时间的话\n',
            '真想去参观一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定有很多没有公布于世\n',
            '的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_38AF(): pass

    label('loc_38AF')

    Jump('loc_3A40')

    def _loc_38B2(): pass

    label('loc_38B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3991',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_390E',
    )

    ChrTalk(
        0x00FE,
        (
            '在商业世界中信用是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在看见真东西之前，\n',
            '一定要保证信用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_398E')

    def _loc_390E(): pass

    label('loc_390E')

    ChrTalk(
        0x00FE,
        (
            '相机和家庭用品\n',
            '该怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问题是导力器都是现货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西蒙，地下工厂\n',
            '的库存怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要亲自去\n',
            '确认才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_398E(): pass

    label('loc_398E')

    Jump('loc_3A40')

    def _loc_3991(): pass

    label('loc_3991')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_3A40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_39F4',
    )

    ChrTalk(
        0x00FE,
        (
            '不过、这次的地震。\n',
            '倒是没有波及到柏斯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果震过来的话\n',
            '一定会吓死人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A40')

    def _loc_39F4(): pass

    label('loc_39F4')

    ChrTalk(
        0x00FE,
        (
            '西蒙如果感觉到地震的话，\n',
            '从他的脚部就可以看出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '冷静，冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_3A40(): pass

    label('loc_3A40')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x3A44
@scena.Code('func_09_3A44')
def func_09_3A44():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3B34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3AB4',
    )

    ChrTalk(
        0x00FE,
        (
            '因为王国的外交政策，\n',
            '钱也比以前难赚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是米拉诺小姐……\n',
            '想法都和别人不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B31')

    def _loc_3AB4(): pass

    label('loc_3AB4')

    ChrTalk(
        0x00FE,
        (
            '新、新型引擎的贩卖权……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为王国的外交政策，\n',
            '钱也比以前难赚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是米拉诺小姐……\n',
            '想法都和别人不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3B31(): pass

    label('loc_3B31')

    Jump('loc_3D01')

    def _loc_3B34(): pass

    label('loc_3B34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_3BA4',
    )

    ChrTalk(
        0x00FE,
        (
            '好、好像参观的时候\n',
            '需要办相关手续呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为中央工房的被袭事件，\n',
            '现在的标准比以前严格了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D01')

    def _loc_3BA4(): pass

    label('loc_3BA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3C7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3C01',
    )

    ChrTalk(
        0x00FE,
        (
            '真想早点去\n',
            '看看地下工厂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能办理许可证的话\n',
            '我马上就会去办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C7B')

    def _loc_3C01(): pass

    label('loc_3C01')

    ChrTalk(
        0x00FE,
        (
            '是、是的，导力器\n',
            '的库存已经确认完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想早点去\n',
            '看看地下工厂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯、在得到许可之前\n',
            '看来要稍等一阵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3C7B(): pass

    label('loc_3C7B')

    Jump('loc_3D01')

    def _loc_3C7E(): pass

    label('loc_3C7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_3D01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3CB4',
    )

    ChrTalk(
        0x00FE,
        (
            '总、总觉得脚底下\n',
            '好像有些摇晃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D01')

    def _loc_3CB4(): pass

    label('loc_3CB4')

    ChrTalk(
        0x00FE,
        (
            '总、总觉得脚底下\n',
            '好像有些摇晃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没、没问题，\n',
            '马上就可以冷静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3D01(): pass

    label('loc_3D01')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x3D05
@scena.Code('func_0A_3D05')
def func_0A_3D05():
    TalkBegin(0x000E)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D1D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_3D1D(): pass

    label('loc_3D1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DA3',
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
        100,
        0,
        (
            TXT(0x00, '【◇【爱的使者】高评价完成】\n'),
            TXT(0x01, '【◇【爱的使者】没有高评价完成】\n'),
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
        (0x00000000, 'loc_3D97'),
        (0x00000001, 'loc_3D9D'),
        (-1, 'loc_3DA3'),
    )

    def _loc_3D97(): pass

    label('loc_3D97')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_3DA3')

    def _loc_3D9D(): pass

    label('loc_3D9D')

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_3DA3')

    def _loc_3DA3(): pass

    label('loc_3DA3')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DC5',
    )

    Call(1, 0x0000)

    Jump('loc_4755')

    def _loc_3DC5(): pass

    label('loc_3DC5')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x2000)"),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3E29',
    )

    ChrTalk(
        0x00FE,
        (
            '今后可能也还会有事情\n',
            '要拜托各位的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么～工作请加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FE1')

    def _loc_3E29(): pass

    label('loc_3E29')

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
            '协会的招牌板竟然会在这里，\n',
            '真是吓了我一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F多谢协助啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '全亏了菲小姐的帮忙\n',
            '才能发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈，那种小事\n',
            '不必客气啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，盗走招牌板的小偷\n',
            '实在是很可怕啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抓到他了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F现在想抓到他太难了…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过呢，总有一天\n',
            '一定会抓到他的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，就是要有这种信心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后可能也还会有事情\n',
            '拜托你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F哈哈，多谢鼓励，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '努力工作吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～你们也是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    OP_28(0x006C, 0x01, 0x2000)

    def _loc_3FE1(): pass

    label('loc_3FE1')

    Jump('loc_4755')

    def _loc_3FE4(): pass

    label('loc_3FE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 3, 0x142B)),
            Expr.Return,
        ),
        'loc_449D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4386',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_40D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4058',
    )

    ChrTalk(
        0x00FE,
        (
            '我也要乘坐工房船\n',
            '前往雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在那里进行『埃尔赛尤』\n',
            '的改装工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40D6')

    def _loc_4058(): pass

    label('loc_4058')

    ChrTalk(
        0x00FE,
        (
            '那么，差不多该\n',
            '要赶快去飞船坪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要乘坐工房船\n',
            '前往雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在那里进行『埃尔赛尤』\n',
            '的改装工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_40D6(): pass

    label('loc_40D6')

    Jump('loc_4383')

    def _loc_40D9(): pass

    label('loc_40D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_433F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_41FE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4145',
    )

    ChrTalk(
        0x00FE,
        (
            '好不容易才和布拉姆\n',
            '重归于好，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近实在太忙，\n',
            '连约会的时间也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41FB')

    def _loc_4145(): pass

    label('loc_4145')

    ChrTalk(
        0x00FE,
        (
            '只是忙倒不算什么，\n',
            '可连休假都没有实在太痛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易才和布拉姆重归于好，\n',
            '现在却连在一起约会的时间都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等『埃尔赛尤』的工作结束之后\n',
            '一定要申请休个长假……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_41FB(): pass

    label('loc_41FB')

    Jump('loc_433C')

    def _loc_41FE(): pass

    label('loc_41FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4286',
    )

    ChrTalk(
        0x00FE,
        (
            '只是忙的话倒也无所谓，\n',
            '可连休假都没有实在太痛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但要是偶尔可以像诞辰庆典时那样\n',
            '再和鲁迪一起去哪里玩玩就好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_433C')

    def _loc_4286(): pass

    label('loc_4286')

    ChrTalk(
        0x00FE,
        (
            '只是忙的话倒也无所谓，\n',
            '可连休假都没有实在太痛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等『埃尔赛尤』的工作结束之后\n',
            '真想有几天休假啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但要是偶尔可以像诞辰庆典时那样\n',
            '再和鲁迪一起去哪里玩玩就好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_433C(): pass

    label('loc_433C')

    Jump('loc_4383')

    def _loc_433F(): pass

    label('loc_433F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_4383',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的地下工厂\n',
            '似乎没有受到地震的影响',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天线很正常，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4383(): pass

    label('loc_4383')

    Jump('loc_449A')

    def _loc_4386(): pass

    label('loc_4386')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_43C1',
    )

    ChrTalk(
        0x00FE,
        (
            '不是很着急吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、大家都\n',
            '加油工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449A')

    def _loc_43C1(): pass

    label('loc_43C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4437',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然还是和以前一样忙得要死，\n',
            '但也只有这样才会有充实的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，说实话，\n',
            '我也希望偶尔可以歇一歇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449A')

    def _loc_4437(): pass

    label('loc_4437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_449A',
    )

    ChrTalk(
        0x00FE,
        (
            '即便是这样\n',
            '地震还真是少见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工厂虽然没有什么异常情况，\n',
            '但上层的各位还是很担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_449A(): pass

    label('loc_449A')

    Jump('loc_4755')

    def _loc_449D(): pass

    label('loc_449D')

    ChrTalk(
        0x00FE,
        (
            '哎呀，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久不见，最近还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1018F啊，菲小姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '菲小姐最近怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈，我还是和以前一样\n',
            '每天忙得要死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_457E',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏你们\n',
            '我和布拉姆重新和好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，感觉还算是很充实啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45AD')

    def _loc_457E(): pass

    label('loc_457E')

    ChrTalk(
        0x00FE,
        (
            '这里的输出也很顺利，\n',
            '地下工厂没有休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45AD(): pass

    label('loc_45AD')

    ChrTalk(
        0x00FE,
        (
            '你们也在\n',
            '这里工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_4677',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，是啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯，现在有些\n',
            '比较紧急的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '打扰你们真不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，抱歉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F那我就先走啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_474F')

    def _loc_4677(): pass

    label('loc_4677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_474F',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，是啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '暂时会待在蔡斯，\n',
            '有需要帮忙的话不用客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那多谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么需要的话\n',
            '和协会联络就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我还要工作，\n',
            '先去忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F噢，在工作吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F嗯，菲小姐，再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_474F(): pass

    label('loc_474F')

    SetScenaFlags(ScenaFlag(0x0285, 3, 0x142B))
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_4755(): pass

    label('loc_4755')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x4759
@scena.Code('func_0B_4759')
def func_0B_4759():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_47EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_47E6',
    )

    ChrTalk(
        0x00FE,
        (
            '总之过去是没发生过\n',
            '这种地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说，这次的地震\n',
            '应该有特殊的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比如未知的火山开始活动\n',
            '等等原因……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47EA')

    def _loc_47E6(): pass

    label('loc_47E6')

    Call(0, 0x000D)

    def _loc_47EA(): pass

    label('loc_47EA')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0x47EE
@scena.Code('func_0C_47EE')
def func_0C_47EE():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_483D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_4839',
    )

    ChrTalk(
        0x00FE,
        (
            '特殊的原因吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里特殊？\n',
            '是否可以解说一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_483D')

    def _loc_4839(): pass

    label('loc_4839')

    Call(0, 0x000D)

    def _loc_483D(): pass

    label('loc_483D')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0x4841
@scena.Code('func_0D_4841')
def func_0D_4841():
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)

    ChrTalk(
        0x0010,
        (
            '之前和利贝尔通讯的人\n',
            '进行过联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '震源已经\n',
            '确定了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '没，还没有查明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '说实话，这次的地震\n',
            '相当奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '即使是我们这些科学家\n',
            '也难以探明其原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Return()

# id: 0x000E offset: 0x48FE
@scena.Code('func_0E_48FE')
def func_0E_48FE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4E96',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_491A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_491A(): pass

    label('loc_491A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49A0',
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
        100,
        0,
        (
            TXT(0x00, '【◇【爱的使者】高评价完成】\n'),
            TXT(0x01, '【◇【爱的使者】没有高评价完成】\n'),
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
        (0x00000000, 'loc_4994'),
        (0x00000001, 'loc_499A'),
        (-1, 'loc_49A0'),
    )

    def _loc_4994(): pass

    label('loc_4994')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_49A0')

    def _loc_499A(): pass

    label('loc_499A')

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_49A0')

    def _loc_49A0(): pass

    label('loc_49A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_4A6D',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A13',
    )

    ChrTalk(
        0x00FE,
        (
            '地下工厂\n',
            '还没有恢复的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是完全自动化的，\n',
            '导力器无法运作的话\n',
            '就什么都做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_4A67')

    def _loc_4A13(): pass

    label('loc_4A13')

    ChrTalk(
        0x00FE,
        (
            '地下工厂\n',
            '还没有恢复的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，毕竟是靠导力驱动的设施，\n',
            '这也是当然的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A67(): pass

    label('loc_4A67')

    TalkEnd(0x00FE)

    Jump('loc_4E93')

    def _loc_4A6D(): pass

    label('loc_4A6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Return,
        ),
        'loc_4C94',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '汽油到手了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我连一次都没有\n',
            '去过温泉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4B7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B23',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然听说那里的热水\n',
            '泡起来很舒服，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，亚尔摩的温泉\n',
            '也不能治愈失恋的创伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_4B79')

    def _loc_4B23(): pass

    label('loc_4B23')

    ChrTalk(
        0x00FE,
        (
            '我还一次\n',
            '都没有去过温泉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，作为伤心旅行的场所，\n',
            '也许那里再适合不过了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B79(): pass

    label('loc_4B79')

    Jump('loc_4C8E')

    def _loc_4B7C(): pass

    label('loc_4B7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C2F',
    )

    ChrTalk(
        0x00FE,
        (
            '不如等菲前辈回来之后\n',
            '试着约她一起去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那可是露天的温泉浴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……嘿、嘿嘿嘿嘿㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1019F（目、目的太明显了吧～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_4C8E')

    def _loc_4C2F(): pass

    label('loc_4C2F')

    ChrTalk(
        0x00FE,
        (
            '不如等菲前辈回来之后\n',
            '试着约她一起去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那可是露天的温泉浴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿……㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C8E(): pass

    label('loc_4C8E')

    TalkEnd(0x00FE)

    Jump('loc_4E93')

    def _loc_4C94(): pass

    label('loc_4C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 2, 0x200A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 0, 0x2010)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CA5',
    )

    Call(0, 0x0011)

    Return()

    def _loc_4CA5(): pass

    label('loc_4CA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 2, 0x200A)),
            Expr.Return,
        ),
        'loc_4D8E',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D38',
    )

    ChrTalk(
        0x00FE,
        (
            '要去卢安的话\n',
            '卡鲁迪亚隧道是条近路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过隧道现在一团漆黑，\n',
            '非常危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要想从那里通行的话\n',
            '一定要非常小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_4D88')

    def _loc_4D38(): pass

    label('loc_4D38')

    ChrTalk(
        0x00FE,
        (
            '不过隧道现在一团漆黑，\n',
            '非常危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要想从那里通行的话\n',
            '一定要非常小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D88(): pass

    label('loc_4D88')

    TalkEnd(0x00FE)

    Jump('loc_4E93')

    def _loc_4D8E(): pass

    label('loc_4D8E')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E3A',
    )

    ChrTalk(
        0x00FE,
        (
            '菲前辈和博士一起\n',
            '去什么地方办事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是王国军的邀请，\n',
            '不过看起来好像慌慌张张的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说老实话，这种时候没有前辈在身边…\n',
            '心里还真是不踏实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    Jump('loc_4E90')

    def _loc_4E3A(): pass

    label('loc_4E3A')

    ChrTalk(
        0x00FE,
        (
            '菲前辈和博士一起\n',
            '去什么地方办事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候前辈不在旁边\n',
            '真是很不踏实啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E90(): pass

    label('loc_4E90')

    TalkEnd(0x00FE)
    def _loc_4E93(): pass

    label('loc_4E93')

    Jump('loc_51DC')

    def _loc_4E96(): pass

    label('loc_4E96')

    TalkBegin(0x0011)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EAE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_4EAE(): pass

    label('loc_4EAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F34',
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
        100,
        0,
        (
            TXT(0x00, '【◇【爱的使者】高评价完成】\n'),
            TXT(0x01, '【◇【爱的使者】没有高评价完成】\n'),
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
        (0x00000000, 'loc_4F28'),
        (0x00000001, 'loc_4F2E'),
        (-1, 'loc_4F34'),
    )

    def _loc_4F28(): pass

    label('loc_4F28')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_4F34')

    def _loc_4F2E(): pass

    label('loc_4F2E')

    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_4F34')

    def _loc_4F34(): pass

    label('loc_4F34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_506B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_4FA5',
    )

    ChrTalk(
        0x00FE,
        (
            '菲前辈乘坐工房的飞船\n',
            '去雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了装配『埃尔赛尤』的引擎，\n',
            '要在那边进行作业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5068')

    def _loc_4FA5(): pass

    label('loc_4FA5')

    ChrTalk(
        0x00FE,
        (
            '菲前辈乘坐工房的飞船\n',
            '去雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了装配『埃尔赛尤』的引擎，\n',
            '要在那边进行作业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了～前辈不在的时候\n',
            '我就要一个人努力工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在新的邂逅来临之前，\n',
            '工作就是我的恋人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    def _loc_5068(): pass

    label('loc_5068')

    Jump('loc_51D9')

    def _loc_506B(): pass

    label('loc_506B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_5102',
    )

    ChrTalk(
        0x00FE,
        (
            '菲前辈乘坐工房的飞船\n',
            '去雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜，我正准备向前辈提出\n',
            '正式交往的请求呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶的『埃尔赛尤』……\n',
            '竟敢把我和前辈拆散～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51D9')

    def _loc_5102(): pass

    label('loc_5102')

    ChrTalk(
        0x00FE,
        (
            '菲前辈乘坐工房的飞船\n',
            '去雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了装配『埃尔赛尤』的引擎，\n',
            '前辈要去要塞进行作业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但我今天本来还要\n',
            '向前辈提出正式交往的请求呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可、可恶的『埃尔赛尤』……\n',
            '竟敢把我和前辈拆散～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    def _loc_51D9(): pass

    label('loc_51D9')

    TalkEnd(0x0011)
    def _loc_51DC(): pass

    label('loc_51DC')

    Return()

# id: 0x000F offset: 0x51DD
@scena.Code('func_0F_51DD')
def func_0F_51DD():
    Return()

# id: 0x0010 offset: 0x51DE
@scena.Code('func_10_51DE')
def func_10_51DE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5323',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_5323',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52BD',
    )

    ChrTalk(
        0x00FE,
        (
            '街道的灯已经全部熄灭了，\n',
            '现在哪条路也都很难走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是卡鲁迪亚隧道\n',
            '普通人连出行都成了问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是要去卢安的话\n',
            '也只能走那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，呼……\n',
            '要是有护卫委托的话该怎么办呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Jump('loc_5323')

    def _loc_52BD(): pass

    label('loc_52BD')

    ChrTalk(
        0x00FE,
        (
            '卡鲁迪亚隧道一片漆黑\n',
            '普通人连出行都成了问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，呼……\n',
            '要是有护卫委托的话该怎么办呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5323(): pass

    label('loc_5323')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x5327
@scena.Code('func_11_5327')
def func_11_5327():
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
        'loc_534C',
    )

    Call(0, 0x001C)
    Call(0, 0x001D)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_534C(): pass

    label('loc_534C')

    Fade(1000)
    CameraMove(-119860, -4000, -108560, 0)
    OP_67(0, 5480, -10000, 0)
    CameraSetDistance(3070, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    ChrSetPos(0x0101, -121590, -4000, -109860, 180)
    ChrSetPos(0x0102, -120550, -4000, -109740, 180)
    ChrSetPos(0x00F8, -121640, -4000, -108680, 180)
    ChrSetPos(0x00F9, -120310, -4000, -108480, 180)
    OP_4A(0x0011, 255)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54B4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370534V#560F#5P那个…鲁迪哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0011, 0, 400)

    ChrTalk(
        0x0011,
        (
            '#2090370535V#4P啊～这不是提妲吗，\n',
            '艾丝蒂尔也在一起啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2090370536V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370537V#1025F#5P嗯，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_556C')

    def _loc_54B4(): pass

    label('loc_54B4')

    ChrTalk(
        0x0101,
        (
            '#0010370538V#1025F#5P那个…鲁迪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0011, 0, 400)

    ChrTalk(
        0x0011,
        (
            '#2090370539V#4P啊～这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2090370536V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370541V#1040F#5P是的，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_556C(): pass

    label('loc_556C')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向鲁迪说明了水泵装置的事情，\n',
            '并请求将这里储备的汽油分一些来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0011,
        (
            '#2090370542V#4P啊～那可真不得了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2090370543V亚尔摩温泉我也经常去的，\n',
            '很想帮你们，可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2090370544V真不好意思，\n',
            '这里储备的汽油也用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56C8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370545V#063F#5P这、这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370546V#1007F#5P这可麻烦了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_571E')

    def _loc_56C8(): pass

    label('loc_56C8')

    ChrTalk(
        0x0101,
        (
            '#0010370547V#1026F#5P竟、竟然会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370548V#1043F#5P这可麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_571E(): pass

    label('loc_571E')

    ChrSetPos(0x0012, -114100, 0, -100940, 270)
    ChrClearFlags(0x0012, 0x0080)

    NpcTalk(
        0x0012,
        '男性的声音',
        (
            '#0550370549V#6P……谁在那里说话啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_578F',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_57CD')

    def _loc_578F(): pass

    label('loc_578F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57B6',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_57CD')

    def _loc_57B6(): pass

    label('loc_57B6')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_57CD(): pass

    label('loc_57CD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57F4',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5832')

    def _loc_57F4(): pass

    label('loc_57F4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_581B',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5832')

    def _loc_581B(): pass

    label('loc_581B')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5832(): pass

    label('loc_5832')

    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_588C')
    def lambda_588C():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_588C')

    DispatchAsync2(0x00F8, 0x0001, lambda_588C)

    Sleep(50)

    @scena.Lambda('lambda_58A2')
    def lambda_58A2():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_58A2')

    DispatchAsync2(0x00F9, 0x0001, lambda_58A2)

    Sleep(60)

    @scena.Lambda('lambda_58B8')
    def lambda_58B8():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_58B8')

    DispatchAsync2(0x0101, 0x0001, lambda_58B8)

    Sleep(50)

    @scena.Lambda('lambda_58CE')
    def lambda_58CE():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_58CE')

    DispatchAsync2(0x0102, 0x0001, lambda_58CE)

    Sleep(60)

    @scena.Lambda('lambda_58E4')
    def lambda_58E4():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_58E4')

    DispatchAsync2(0x0011, 0x0001, lambda_58E4)

    @scena.Lambda('lambda_58F5')
    def lambda_58F5():
        CameraMove(-119650, -4000, -107120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_58F5)

    @scena.Lambda('lambda_590D')
    def lambda_590D():
        OP_67(0, 6350, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_590D)

    @scena.Lambda('lambda_5925')
    def lambda_5925():
        OP_6E(286, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5925)

    ChrSetPos(0x0012, -117860, -2000, -100950, 0)
    ChrWalkTo(0x0012, -118040, -4000, -106030, 2000, 0x00)
    ChrSetDirection(0x0012, 225, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A47',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370550V#560F#6P啊，工房长伯伯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0550370551V#802F#5P是提妲啊……\n',
            '艾丝蒂尔也在一起啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370552V#803F听到地下有人说话，\n',
            '我还在想是谁呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370553V#800F又发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B01')

    def _loc_5A47(): pass

    label('loc_5A47')

    ChrTalk(
        0x0101,
        (
            '#0010370554V#1004F#6P啊～工房长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0550370555V#802F#5P啊，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370552V#803F听到地下有人说话，\n',
            '我还在想是谁呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370553V#800F又发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B01(): pass

    label('loc_5B01')

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, -121550, -4000, -108680, 0)
    ChrSetPos(0x0102, -120310, -4000, -108480, 0)
    ChrSetPos(0x00F8, -121700, -4000, -109860, 0)
    ChrSetPos(0x00F9, -120300, -4000, -109740, 0)
    ChrSetPos(0x0012, -120720, -4000, -107000, 180)
    Sleep(2000)

    TerminateThread(0x0011, 0x01)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0550370558V#803F#5P原来如此，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370559V#806F说起汽油的话…\n',
            '我记得１个月前还从\n',
            '共和国订购过的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370560V#1004F#6P真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370561V#1042F#4P１个月之前的话……\n',
            '那现在应该已经送到了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2090370562V#4P可、可是工房长…\n',
            '我这里并没有收到那种东西啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0550370563V#803F#5P啊，等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370564V#802F我想起来了，因为并不是太急用的\n',
            '东西，所以是用的海上寄送。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D6D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370565V#070F#6P那就是说没有用飞船送，\n',
            '而是使用了普通的海船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E4C')

    def _loc_5D6D(): pass

    label('loc_5D6D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5DDF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370566V#052F#6P海上寄送的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370567V那就是不使用飞船，\n',
            '而使用普通的海船是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E4C')

    def _loc_5DDF(): pass

    label('loc_5DDF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E4C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370568V#023F#6P海运的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370569V那就是不使用飞船，\n',
            '那就是使用普通的海船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E4C(): pass

    label('loc_5E4C')

    ChrTalk(
        0x0012,
        (
            '#0550370570V#803F#5P嗯，正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370571V#806F所以据我推算，\n',
            '应该才刚刚送到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370572V#800F嗯，也许现在\n',
            '正在卢安\n',
            '卸货吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370573V#1042F#4P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370574V因为导力停止现象，\n',
            '连运输业也受了不小的影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370575V#1006F#6P这么说的话，只要去\n',
            '卢安的码头应该就可以拿到了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0550370576V#800F#5P嗯，应该没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370577V#803F啊，大家稍等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '玛多克工房长拿出纸和笔，\n',
            '写了一封书信，并签上了自己的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrWalkTo(0x0012, -121370, -4000, -107690, 2000, 0x00)
    ChrSetDirection(0x0012, 180, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['工房长的介绍信']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['工房长的介绍信'], 1)
    ChrMoveTo(0x0012, -120720, -4000, -107000, 2000, 0x00)

    ChrTalk(
        0x0012,
        (
            '#0550370578V#800F#5P把这封介绍信交给卢安码头\n',
            '的负责人就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370579V如果汽油已经送到的话，\n',
            '看到我的信他就会给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370580V#1006F#6P谢谢您了，工房长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_619E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370581V#067F#6P嘿嘿……\n',
            '真是谢谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_619E(): pass

    label('loc_619E')

    ChrTalk(
        0x0102,
        (
            '#0020370582V#1054F#4P真不好意思，麻烦您了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0550370583V#801F#5P什么话嘛，我虽然没博士去得勤，\n',
            '但也算是温泉的常客了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370584V身为蔡斯地区的代表，\n',
            '这种事也是我的义务啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370585V#800F好了……\n',
            '我要先回办公室去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370586V还有一大堆文件\n',
            '都没有处理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370587V#1015F#6P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6321',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370588V#063F#6P那个……\n',
            '请您别太勉强啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6353')

    def _loc_6321(): pass

    label('loc_6321')

    ChrTalk(
        0x0102,
        (
            '#0020370589V#1043F#4P……请别太\n',
            '勉强自己啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6353(): pass

    label('loc_6353')

    ChrTalk(
        0x0012,
        (
            '#0550370590V#801F#5P哈哈，等你们把水泵修好以后\n',
            '我也会去泡温泉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370591V那就先失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0402, 0, 0x2010))
    OP_28(0x00C2, 0x01, 0x0200)
    OP_28(0x00C2, 0x01, 0x0400)

    @scena.Lambda('lambda_63CB')
    def lambda_63CB():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_63CB')

    DispatchAsync2(0x00F8, 0x0001, lambda_63CB)

    @scena.Lambda('lambda_63DC')
    def lambda_63DC():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_63DC')

    DispatchAsync2(0x00F9, 0x0001, lambda_63DC)

    @scena.Lambda('lambda_63ED')
    def lambda_63ED():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_63ED')

    DispatchAsync2(0x0101, 0x0001, lambda_63ED)

    @scena.Lambda('lambda_63FE')
    def lambda_63FE():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_63FE')

    DispatchAsync2(0x0102, 0x0001, lambda_63FE)

    @scena.Lambda('lambda_640F')
    def lambda_640F():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_640F')

    DispatchAsync2(0x0011, 0x0001, lambda_640F)

    ChrWalkTo(0x0012, -118040, -4000, -106030, 2000, 0x00)
    ChrWalkTo(0x0012, -117860, -2000, -100950, 2000, 0x00)
    ChrSetFlags(0x0012, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0011, 0x01)
    OP_4B(0x0011, 255)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x6463
@scena.Code('func_12_6463')
def func_12_6463():
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
        'loc_647A',
    )

    Call(0, 0x001C)
    Call(0, 0x001D)

    def _loc_647A(): pass

    label('loc_647A')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(-200, 0, 6140, 0)
    OP_67(0, 7400, -10000, 0)
    CameraSetDistance(2490, 0)
    OP_6C(45000, 0)
    OP_6E(350, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_64DB')
    def lambda_64DB():
        CameraMove(620, 0, -7820, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_64DB)

    @scena.Lambda('lambda_64F3')
    def lambda_64F3():
        OP_6E(285, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_64F3)

    Sleep(2000)

    CreateThread(0x0101, 0x01, 0x00, func_13_6943)
    Sleep(100)

    CreateThread(0x0102, 0x01, 0x00, func_14_69A2)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_15_6A01)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, func_16_6AAE)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010370033V#1004F#6P呜哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65DA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370034V#052F#4P这是……\n',
            '这比想象中还要漆黑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370035V虽然已经安装上了油灯，\n',
            '可还是没起什么作用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_676A')

    def _loc_65DA(): pass

    label('loc_65DA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6663',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370036V#023F#4P这是……\n',
            '比预想中还要黑暗啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370037V虽然已经安装上了油灯，\n',
            '虽然做了些补救措施，可还是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_676A')

    def _loc_6663(): pass

    label('loc_6663')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_676A',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66F7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370038V#073F#4P这是……\n',
            '比想象中还要黑暗啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370039V虽然已经安装上了油灯，\n',
            '虽然做了一些应急措施，但…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_676A')

    def _loc_66F7(): pass

    label('loc_66F7')

    ChrTalk(
        0x0108,
        (
            '#0080370040V#073F这是……\n',
            '比想象中还要黑暗啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370039V虽然已经安装上了油灯，\n',
            '虽然做了一些应急措施，但…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_676A(): pass

    label('loc_676A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_67B2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370042V#063F#4P工房的各位\n',
            '不知道是否还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6893')

    def _loc_67B2(): pass

    label('loc_67B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6846',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_680B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370043V#072F#4P像现在这种状况\n',
            '确实没办法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6843')

    def _loc_680B(): pass

    label('loc_680B')

    ChrTalk(
        0x0108,
        (
            '#0080370044V#072F像现在这种状况\n',
            '确实没办法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6843(): pass

    label('loc_6843')

    Jump('loc_6893')

    def _loc_6846(): pass

    label('loc_6846')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6893',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370045V#522F#4P现在这种状况的话\n',
            '根本就没办法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6893(): pass

    label('loc_6893')

    ChrTalk(
        0x0101,
        (
            '#0010370046V#1015F#6P而且……不用说，\n',
            '电梯肯定也不能使用了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370047V#1035F#4P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370048V#1043F要想去其他楼层的话\n',
            '就只能走紧急通路那里的楼梯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0406, 7, 0x2037))
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x6943
@scena.Code('func_13_6943')
def func_13_6943():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -760, 0, -11540, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_696A')
    def lambda_696A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_696A)

    ChrWalkTo(0x00FE, -490, 0, -7870, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x0014 offset: 0x69A2
@scena.Code('func_14_69A2')
def func_14_69A2():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 320, 0, -11560, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_69C9')
    def lambda_69C9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_69C9)

    ChrWalkTo(0x00FE, 500, 0, -7970, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x0015 offset: 0x6A01
@scena.Code('func_15_6A01')
def func_15_6A01():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -760, 0, -11540, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6A28')
    def lambda_6A28():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6A28)

    ChrWalkTo(0x00FE, -1020, 0, -9310, 2000, 0x00)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A6F',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_6AAD')

    def _loc_6A6F(): pass

    label('loc_6A6F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A96',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_6AAD')

    def _loc_6A96(): pass

    label('loc_6A96')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_6AAD(): pass

    label('loc_6AAD')

    Return()

# id: 0x0016 offset: 0x6AAE
@scena.Code('func_16_6AAE')
def func_16_6AAE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 320, 0, -11560, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6AD5')
    def lambda_6AD5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6AD5)

    ChrWalkTo(0x00FE, 330, 0, -9400, 2000, 0x00)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B1C',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_6B5A')

    def _loc_6B1C(): pass

    label('loc_6B1C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B43',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_6B5A')

    def _loc_6B43(): pass

    label('loc_6B43')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_6B5A(): pass

    label('loc_6B5A')

    Return()

# id: 0x0017 offset: 0x6B5B
@scena.Code('func_17_6B5B')
def func_17_6B5B():
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
        'loc_6B72',
    )

    Call(0, 0x001C)
    Call(0, 0x001D)

    def _loc_6B72(): pass

    label('loc_6B72')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(-200970, 0, 17180, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(335, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_6BD3')
    def lambda_6BD3():
        CameraMove(-225780, 0, 16880, 4500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6BD3)

    @scena.Lambda('lambda_6BEB')
    def lambda_6BEB():
        OP_67(0, 6990, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6BEB)

    @scena.Lambda('lambda_6C03')
    def lambda_6C03():
        CameraSetDistance(2520, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6C03)

    Sleep(2000)

    CreateThread(0x0101, 0x01, 0x00, func_18_6EC5)
    Sleep(600)

    CreateThread(0x0102, 0x01, 0x00, func_19_6F2B)
    Sleep(600)

    CreateThread(0x00F8, 0x01, 0x00, func_1A_6F91)
    Sleep(600)

    CreateThread(0x00F9, 0x01, 0x00, func_1B_7059)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010370049V#1004F#4P哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6CA9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370050V#052F#6P这是…\n',
            '比想象中还要黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D34')

    def _loc_6CA9(): pass

    label('loc_6CA9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6CEF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370051V#023F#6P这……\n',
            '比预想中还要黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D34')

    def _loc_6CEF(): pass

    label('loc_6CEF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D34',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370052V#073F#6P这个……\n',
            '比想象中还要黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D34(): pass

    label('loc_6D34')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6D7E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370042V#063F#6P工房中的各位\n',
            '不知道是否还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E15')

    def _loc_6D7E(): pass

    label('loc_6D7E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6DCC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370054V#075F#6P像现在这样的状况\n',
            '确实没办法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E15')

    def _loc_6DCC(): pass

    label('loc_6DCC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E15',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370045V#522F#6P这种状况的话\n',
            '根本就没办法工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E15(): pass

    label('loc_6E15')

    ChrTalk(
        0x0101,
        (
            '#0010370056V#1015F#4P而且……不用说，\n',
            '电梯肯定也不能使用了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370057V#1035F#6P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370048V#1043F要想去其他楼层的话\n',
            '就只能走紧急通路那里的楼梯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0406, 7, 0x2037))
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x6EC5
@scena.Code('func_18_6EC5')
def func_18_6EC5():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -230500, -250, 15940, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6EEC')
    def lambda_6EEC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_6EEC)

    ChrWalkTo(0x00FE, -225560, 0, 15330, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x0019 offset: 0x6F2B
@scena.Code('func_19_6F2B')
def func_19_6F2B():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -230500, -250, 15940, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6F52')
    def lambda_6F52():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_6F52)

    ChrWalkTo(0x00FE, -225570, 0, 16379, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Return()

# id: 0x001A offset: 0x6F91
@scena.Code('func_1A_6F91')
def func_1A_6F91():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -230500, -250, 15940, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6FB8')
    def lambda_6FB8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_6FB8)

    ChrWalkTo(0x00FE, -228210, 0, 15950, 2000, 0x00)
    ChrWalkTo(0x00FE, -226740, 0, 15070, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_701A',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7058')

    def _loc_701A(): pass

    label('loc_701A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7041',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7058')

    def _loc_7041(): pass

    label('loc_7041')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_7058(): pass

    label('loc_7058')

    Return()

# id: 0x001B offset: 0x7059
@scena.Code('func_1B_7059')
def func_1B_7059():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -230000, -250, 15940, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_7080')
    def lambda_7080():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0000, lambda_7080)

    ChrWalkTo(0x00FE, -228210, 0, 15950, 2000, 0x00)
    ChrWalkTo(0x00FE, -226900, 0, 16420, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70E2',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7120')

    def _loc_70E2(): pass

    label('loc_70E2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7109',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7120')

    def _loc_7109(): pass

    label('loc_7109')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_7120(): pass

    label('loc_7120')

    Return()

# id: 0x001C offset: 0x7121
@scena.Code('func_1C_7121')
def func_1C_7121():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_719B'),
        (0x00000001, 'loc_71A1'),
        (-1, 'loc_71A7'),
    )

    def _loc_719B(): pass

    label('loc_719B')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_71A7')

    def _loc_71A1(): pass

    label('loc_71A1')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_71A7')

    def _loc_71A7(): pass

    label('loc_71A7')

    Return()

# id: 0x001D offset: 0x71A8
@scena.Code('func_1D_71A8')
def func_1D_71A8():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x001E offset: 0x7201
@scena.Code('func_1E_7201')
def func_1E_7201():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '左·中央工房电梯\n',
            '右·地下导力器工厂',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001F offset: 0x7257
@scena.Code('func_1F_7257')
def func_1F_7257():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
