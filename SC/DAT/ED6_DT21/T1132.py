import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1132   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '巴雷里奥'),
    TXT(0x02, '蒂娜'),
    TXT(0x03, '达维尔大使'),
    TXT(0x04, '杰拉尔德'),
    TXT(0x05, '杰拉尔德'),
    TXT(0x06, '巴克雷书记官'),
    TXT(0x07, '巴克'),
    TXT(0x08, '德拉多'),
    TXT(0x09, '普蕾沙'),
    TXT(0x0A, '波波'),
    TXT(0x0B, '思潘斯老人'),
    TXT(0x0C, '米蕾婆婆'),
    TXT(0x0D, '里布罗'),
    TXT(0x0E, '艾米'),
    TXT(0x0F, '哈尔德'),
    TXT(0x10, '罗亚'),
    TXT(0x11, '提克'),
    TXT(0x12, '莫莉'),
    TXT(0x13, '赛希莉亚号乘客'),
    TXT(0x14, '赛希莉亚号乘客'),
    TXT(0x15, '赛希莉亚号乘客'),
    TXT(0x16, '赛希莉亚号乘客'),
    TXT(0x17, '目标用照相机'),
    TXT(0x18, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1132.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x000C
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1132_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x45B9
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
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT27/CH03710._CH', 'ED6_DT27/CH03710P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4500,
            z                   = 0,
            y                   = 190600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -49910,
            z                   = 0,
            y                   = 118350,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -122680,
            z                   = 0,
            y                   = 179240,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -126260,
            z                   = 0,
            y                   = 138000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -127460,
            z                   = 0,
            y                   = 181340,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -123490,
            z                   = 0,
            y                   = 178400,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -85120,
            z                   = 0,
            y                   = 121590,
            direction           = 130,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -86580,
            z                   = 0,
            y                   = 119500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -45690,
            z                   = 0,
            y                   = 152320,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -48210,
            z                   = 0,
            y                   = 155300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -49050,
            z                   = 0,
            y                   = 120240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -85770,
            z                   = 0,
            y                   = 152520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -85280,
            z                   = 0,
            y                   = 153820,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 4530,
            z                   = 0,
            y                   = 182260,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 6470,
            z                   = 0,
            y                   = 191180,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -45610,
            z                   = 0,
            y                   = 153280,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -88500,
            z                   = 0,
            y                   = 122920,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -84260,
            z                   = 0,
            y                   = 119710,
            direction           = 291,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -49680,
            z                   = 0,
            y                   = 119810,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -86090,
            z                   = 0,
            y                   = 151630,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -82340,
            z                   = 0,
            y                   = 158280,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = -47150,
            z                   = 0,
            y                   = 152620,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
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
    )

# id: 0x10003 offset: 0x40A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x40A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -126260,
            y           = 0,
            z           = 138000,
            range       = 1000,
            dword_10    = 0x00000514,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000000,
        ),
    )

# id: 0x10005 offset: 0x42A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 6598,
            triggerZ            = 0,
            triggerY            = 190158,
            triggerRange        = 700,
            actorX              = 4500,
            actorZ              = 1500,
            actorY              = 190662,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3130,
            triggerZ            = 0,
            triggerY            = 192000,
            triggerRange        = 800,
            actorX              = 3130,
            actorZ              = 1000,
            actorY              = 192000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x472
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_48C',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)
    Event(1, 0x000A)

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4F0',
    )

    OP_B2(0x00, 0x00, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrPos(0x0009, -124920, 0, 178920, 0)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0018, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D9',
    )

    ClearChrFlags(0x0019, 0x0080)

    Jump('loc_4ED')

    def _loc_4D9(): pass

    label('loc_4D9')

    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)

    def _loc_4ED(): pass

    label('loc_4ED')

    Jump('loc_600')

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_51F',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrPos(0x0009, -126520, 0, 181820, 90)

    Jump('loc_600')

    def _loc_51F(): pass

    label('loc_51F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_578',
    )

    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0009, -42800, 0, 152070, 270)
    SetChrPos(0x0016, -128430, 0, 128900, 270)

    Jump('loc_600')

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_5C0',
    )

    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0009, -130180, 0, 130460, 270)

    Jump('loc_600')

    def _loc_5C0(): pass

    label('loc_5C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_600',
    )

    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0009, -130180, 0, 130460, 270)

    def _loc_600(): pass

    label('loc_600')

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_623',
    )

    SetChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    def _loc_623(): pass

    label('loc_623')

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_667',
    )

    SetChrPos(0x000A, -123450, 0, 178760, 270)
    SetChrPos(0x000D, -122420, 0, 179380, 270)
    SetChrPos(0x000C, -128500, 0, 178640, 90)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)

    def _loc_667(): pass

    label('loc_667')

    Return()

# id: 0x0001 offset: 0x668
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 2, 0x1A12)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_67A',
    )

    OP_10(0x01, 0x00)
    OP_10(0x0E, 0x01)

    def _loc_67A(): pass

    label('loc_67A')

    Return()

# id: 0x0002 offset: 0x67B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_69E',
    )

    OP_8D(0x00FE, 3860, 184520, 5490, 181970, 1500)

    Jump('ReInit')

    def _loc_69E(): pass

    label('loc_69E')

    Return()

# id: 0x0003 offset: 0x69F
@scena.Code('func_03_69F')
def func_03_69F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6EB',
    )

    OP_8E(0x00FE, -122680, 0, 180920, 1500, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, -122680, 0, 179240, 1500, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)

    Jump('func_03_69F')

    def _loc_6EB(): pass

    label('loc_6EB')

    Return()

# id: 0x0004 offset: 0x6EC
@scena.Code('func_04_6EC')
def func_04_6EC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_70F',
    )

    OP_8D(0x00FE, -127570, 177960, -122660, 179600, 1000)

    Jump('func_04_6EC')

    def _loc_70F(): pass

    label('loc_70F')

    Return()

# id: 0x0005 offset: 0x710
@scena.Code('func_05_710')
def func_05_710():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_733',
    )

    OP_8D(0x00FE, -51430, 121490, -47820, 118410, 1500)

    Jump('func_05_710')

    def _loc_733(): pass

    label('loc_733')

    Return()

# id: 0x0006 offset: 0x734
@scena.Code('func_06_734')
def func_06_734():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_757',
    )

    OP_8D(0x00FE, -84580, 120430, -82970, 119500, 1500)

    Jump('func_06_734')

    def _loc_757(): pass

    label('loc_757')

    Return()

# id: 0x0007 offset: 0x758
@scena.Code('func_07_758')
def func_07_758():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x75D
@scena.Code('func_08_75D')
def func_08_75D():
    TalkBegin(0x0008)
    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_777',
    )

    OP_A9(0x35)
    TalkEnd(0x0008)

    Return()

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_788',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_788(): pass

    label('loc_788')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_879',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_822',
    )

    ChrTalk(
        0x0008,
        (
            '定期船的恢复航行，\n',
            '到底要等到什么时候呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本酒店也有\n',
            '等待出发的客人在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对从事旅游业的人们来说\n',
            '真是个头痛的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_876')

    def _loc_822(): pass

    label('loc_822')

    ChrTalk(
        0x0008,
        (
            '定期船的恢复\n',
            '会是什么时候呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对从事旅游业的人们来说\n',
            '真是个头痛的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_876(): pass

    label('loc_876')

    Jump('loc_DF4')

    def _loc_879(): pass

    label('loc_879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_953',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_90F',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎。\n',
            '欢迎光临富莱登酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '导力器虽然无法工作，\n',
            '但本酒店依然照常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们深知会给您带来不便，\n',
            '但还请多多原谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_950')

    def _loc_90F(): pass

    label('loc_90F')

    ChrTalk(
        0x0008,
        (
            '导力器虽然无法工作，\n',
            '但本酒店依然照常营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请多担待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_950(): pass

    label('loc_950')

    Jump('loc_DF4')

    def _loc_953(): pass

    label('loc_953')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_A3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9BE',
    )

    ChrTalk(
        0x0008,
        (
            '超市的修复工程\n',
            '给大家添了不少麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天和平时一样正常营业。\n',
            '请大家多多惠顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3C')

    def _loc_9BE(): pass

    label('loc_9BE')

    ChrTalk(
        0x0008,
        (
            '欢迎。\n',
            '欢迎光临富莱登酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '超市的修复工程\n',
            '给大家添了不少麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天和平时一样正常营业。\n',
            '请大家多多惠顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A3C(): pass

    label('loc_A3C')

    Jump('loc_DF4')

    def _loc_A3F(): pass

    label('loc_A3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_B2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AAA',
    )

    ChrTalk(
        0x0008,
        (
            '看来超市的修复工程\n',
            '进行的很顺利嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，\n',
            '很快就要和这迷你百货市场说再见了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2C')

    def _loc_AAA(): pass

    label('loc_AAA')

    ChrTalk(
        0x0008,
        (
            '看来超市的修复工程\n',
            '进行的很顺利嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，\n',
            '很快就要和这迷你百货市场说再见了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想到这里，\n',
            '感觉稍稍有点寂寞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_B2C(): pass

    label('loc_B2C')

    Jump('loc_DF4')

    def _loc_B2F(): pass

    label('loc_B2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_C3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BC1',
    )

    ChrTalk(
        0x0008,
        (
            '现在，\n',
            '本酒店开放为商人们的临时店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '非常时期的团结以及互相协助\n',
            '正是我们柏斯商人的美德啊。\n',
            '我很乐意为大家效犬马之劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C37')

    def _loc_BC1(): pass

    label('loc_BC1')

    ChrTalk(
        0x0008,
        (
            '欢迎。\n',
            '欢迎光临富莱登酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在，\n',
            '本酒店开放为商人们的临时店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么回事，\n',
            '有点百货超市的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_C37(): pass

    label('loc_C37')

    Jump('loc_DF4')

    def _loc_C3A(): pass

    label('loc_C3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_D08',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C6A',
    )

    ChrTalk(
        0x0008,
        (
            '唉哟哟……\n',
            '出大事儿了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D05')

    def _loc_C6A(): pass

    label('loc_C6A')

    ChrTalk(
        0x0008,
        (
            '唉哟哟……\n',
            '唉哟哟，出大事情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '遵从梅贝尔市长的请求，\n',
            '本酒店会将客房开放，\n',
            '用于保护商人们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是那个怪物要是再来的话\n',
            '该怎么办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_D05(): pass

    label('loc_D05')

    Jump('loc_DF4')

    def _loc_D08(): pass

    label('loc_D08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_DF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D65',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎。\n',
            '欢迎光临富莱登酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '帝国大使大人\n',
            '目前正在本酒店下榻暂住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF4')

    def _loc_D65(): pass

    label('loc_D65')

    ChrTalk(
        0x0008,
        (
            '欢迎。\n',
            '欢迎光临富莱登酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '帝国大使大人\n',
            '目前正在本酒店下榻暂住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '出于安全的考虑，\n',
            '我们深知会给您带来不便，\n',
            '还请务必多包涵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_DF4(): pass

    label('loc_DF4')

    TalkEnd(0x0008)

    Return()

# id: 0x0009 offset: 0xDF8
@scena.Code('func_09_DF8')
def func_09_DF8():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_F31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EDC',
    )

    ChrTalk(
        0x00FE,
        (
            '酒店里现在住的客人是\n',
            '因为定期船停航才住下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '虽然觉得客人们挺可怜的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但突然间被增加工作量的\n',
            '我才更可怜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来以为超市的销售量可以\n',
            '有所上升的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，真是灾难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_F2E')

    def _loc_EDC(): pass

    label('loc_EDC')

    ChrTalk(
        0x00FE,
        (
            '定期船的客人\n',
            '虽然觉得挺可怜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是突然间被增加工作量的\n',
            '我才更可怜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F2E(): pass

    label('loc_F2E')

    Jump('loc_14B2')

    def _loc_F31(): pass

    label('loc_F31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1022',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FBD',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～真是的……\n',
            '太费时间了，真没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果扫地不用吸尘器，\n',
            '还是会很麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就好像煎蛋\n',
            '不用锅子一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_101F')

    def _loc_FBD(): pass

    label('loc_FBD')

    ChrTalk(
        0x00FE,
        (
            '如果扫地不用吸尘器，\n',
            '还是会很麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，老板那家伙总说我……\n',
            '倒是让他自己来试试看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_101F(): pass

    label('loc_101F')

    Jump('loc_14B2')

    def _loc_1022(): pass

    label('loc_1022')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1118',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1085',
    )

    ChrTalk(
        0x00FE,
        (
            '那个帝国大使什么的，\n',
            '总算是回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是摆着一副臭架子，\n',
            '感觉好讨厌哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1115')

    def _loc_1085(): pass

    label('loc_1085')

    ChrTalk(
        0x00FE,
        (
            '那个帝国大使什么的，\n',
            '可算回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是摆着一副臭架子，\n',
            '感觉好讨厌哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然商人先生回去了挺遗憾的，\n',
            '但那个人走了可真叫人高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1115(): pass

    label('loc_1115')

    Jump('loc_14B2')

    def _loc_1118(): pass

    label('loc_1118')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_11FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_118B',
    )

    ChrTalk(
        0x00FE,
        (
            '这位商人先生\n',
            '做的是碟子和小商品的生意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上班时还可以买东西，\n',
            '真是梦一般的职场环境啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11F7')

    def _loc_118B(): pass

    label('loc_118B')

    ChrTalk(
        0x00FE,
        (
            '这位商人先生\n',
            '做的是碟子和小商品的生意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚好我正在\n',
            '寻找茶杯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等等有时间\n',
            '再来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_11F7(): pass

    label('loc_11F7')

    Jump('loc_14B2')

    def _loc_11FA(): pass

    label('loc_11FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1308',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_126D',
    )

    ChrTalk(
        0x00FE,
        (
            '短时间内，我们酒店\n',
            '会成为商人们的临时住所呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作能够变轻松的话，\n',
            '不管是什么我都欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1305')

    def _loc_126D(): pass

    label('loc_126D')

    ChrTalk(
        0x00FE,
        (
            '短时间内，我们酒店\n',
            '会成为商人们的临时住所呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也就是说，负责客房的人\n',
            '可以不用工作了是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去看看就知道，\n',
            '几乎都处在开店休业状态嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1305(): pass

    label('loc_1305')

    Jump('loc_14B2')

    def _loc_1308(): pass

    label('loc_1308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_13F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1376',
    )

    ChrTalk(
        0x00FE,
        (
            '总，总觉得商人们好像\n',
            '在往客房里搬运货物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里会被梅贝尔市长收购\n',
            '变成超市2号店吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13ED')

    def _loc_1376(): pass

    label('loc_1376')

    ChrTalk(
        0x00FE,
        (
            '总，总觉得商人们好像\n',
            '在往客房里搬运货物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，难道说！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里会被梅贝尔市长收购\n',
            '变成超市２号店之类？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_13ED(): pass

    label('loc_13ED')

    Jump('loc_14B2')

    def _loc_13F0(): pass

    label('loc_13F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_14B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_144D',
    )

    ChrTalk(
        0x00FE,
        (
            '住在２楼的人\n',
            '好像颇有来头呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '好像一直待在房间里不出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B2')

    def _loc_144D(): pass

    label('loc_144D')

    ChrTalk(
        0x00FE,
        (
            '住在２楼的人\n',
            '好像颇有来头呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '好像一直待在房间里不出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底在做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_14B2(): pass

    label('loc_14B2')

    TalkEnd(0x0009)

    Return()

# id: 0x000A offset: 0x14B6
@scena.Code('func_0A_14B6')
def func_0A_14B6():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1564',
    )

    ChrTalk(
        0x000A,
        (
            '#0670480526V#1100F对我来说只要把\n',
            '勋章取回来就足够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480527V『怪盗Ｂ』的逮捕\n',
            '是国家及协会全体考虑的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480528V我觉得\n',
            '你们没有必要太担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19BA')

    def _loc_1564(): pass

    label('loc_1564')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1673',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_15EE',
    )

    ChrTalk(
        0x000A,
        (
            '#0670480529V#1100F我最后决定\n',
            '乘坐王国军警备艇回王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480530V嗯，对待帝国大使，\n',
            '这样的安排是理所当然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1670')

    def _loc_15EE(): pass

    label('loc_15EE')

    ChrTalk(
        0x000A,
        (
            '#0670480531V#1100F计划将乘坐王国军的警备艇\n',
            '于不久后返回王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480532V无论如何都要在这之前把勋章找回来！\n',
            '一定要找回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1670(): pass

    label('loc_1670')

    Jump('loc_19BA')

    def _loc_1673(): pass

    label('loc_1673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1795',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1701',
    )

    ChrTalk(
        0x000A,
        (
            '#0670480533V#1100F定期船停航了，\n',
            '就算想回王都也没有办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480534V我，我可是帝国大使！\n',
            '敢挡我去路，胆子可不小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1792')

    def _loc_1701(): pass

    label('loc_1701')

    ChrTalk(
        0x000A,
        (
            '#0670480535V#1100F勋章是陛下赏赐予\n',
            '本家族荣誉的象征……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480536V但是，我差不多\n',
            '该回王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480537V无论如何\n',
            '都要在这之前找回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1792(): pass

    label('loc_1792')

    Jump('loc_19BA')

    def _loc_1795(): pass

    label('loc_1795')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_18B8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1837',
    )

    ChrTalk(
        0x000A,
        (
            '#0670480538V#1100F即使我打算恢复视察，\n',
            '可是超市现在那副样子也没办法继续……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480539V唔，预定的行程终于结束了。\n',
            '应该是时候回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18B5')

    def _loc_1837(): pass

    label('loc_1837')

    ChrTalk(
        0x000A,
        (
            '#0670480540V#1100F那勋章是皇帝陛下赏赐的，\n',
            '是本家族荣誉的象征……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480541V难道超市也被牵连到了……\n',
            '真是没有想到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18B5(): pass

    label('loc_18B5')

    Jump('loc_19BA')

    def _loc_18B8(): pass

    label('loc_18B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_19BA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_195B',
    )

    ChrTalk(
        0x000A,
        (
            '#0670480542V#1100F我觉得是时候恢复\n',
            '对这座城市的视察了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480543V听说柏斯超市里有\n',
            '很多我国的商人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480544V首先\n',
            '得从那里开始啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19BA')

    def _loc_195B(): pass

    label('loc_195B')

    ChrTalk(
        0x000A,
        (
            '#0670480545V#1100F那个勋章\n',
            '是殿下赏赐给我家的荣誉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670480546V无论如何都要找回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19BA(): pass

    label('loc_19BA')

    TalkEnd(0x000A)

    Return()

# id: 0x000B offset: 0x19BE
@scena.Code('func_0B_19BE')
def func_0B_19BE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1ABF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1A7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1A25',
    )

    ChrTalk(
        0x00FE,
        (
            '非常感谢各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '勋章完好无损的找回来了，\n',
            '这样就可以放心回国了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A79')

    def _loc_1A25(): pass

    label('loc_1A25')

    ChrTalk(
        0x00FE,
        (
            '在王国军的协助下，\n',
            '能够回王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大使大人非常感谢\n',
            '王国方面所表示的诚意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A79(): pass

    label('loc_1A79')

    Jump('loc_1ABC')

    def _loc_1A7C(): pass

    label('loc_1A7C')

    ChrTalk(
        0x00FE,
        (
            '王国军为了大使\n',
            '出动了飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在船到达前\n',
            '能找到勋章吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1ABC(): pass

    label('loc_1ABC')

    Jump('loc_1D81')

    def _loc_1ABF(): pass

    label('loc_1ABF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1BB2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1B72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B32',
    )

    ChrTalk(
        0x00FE,
        (
            '非常感谢各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，超市\n',
            '暂时休业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '若是能在日程内\n',
            '完成视察就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B6F')

    def _loc_1B32(): pass

    label('loc_1B32')

    ChrTalk(
        0x00FE,
        (
            '帝国的人当中，\n',
            '好像没有人负伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不幸中的大幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B6F(): pass

    label('loc_1B6F')

    Jump('loc_1BAF')

    def _loc_1B72(): pass

    label('loc_1B72')

    ChrTalk(
        0x00FE,
        (
            '能找到勋章吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要……\n',
            '能在回王都前找到就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1BAF(): pass

    label('loc_1BAF')

    Jump('loc_1D81')

    def _loc_1BB2(): pass

    label('loc_1BB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1CAE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1C63',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1C08',
    )

    ChrTalk(
        0x00FE,
        (
            '非常感谢各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '超市遭受破坏的程度如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2B')

    def _loc_1C08(): pass

    label('loc_1C08')

    ChrTalk(
        0x00FE,
        (
            '超市遭受的破坏，\n',
            '的程度如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C2B(): pass

    label('loc_1C2B')

    ChrTalk(
        0x00FE,
        (
            '难道会影响到视察行程的安排，\n',
            '说不定会取消行程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CAB')

    def _loc_1C63(): pass

    label('loc_1C63')

    ChrTalk(
        0x00FE,
        (
            '超市遭受的破坏，\n',
            '的程度如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '受伤人员中\n',
            '可能也有我国的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1CAB(): pass

    label('loc_1CAB')

    Jump('loc_1D81')

    def _loc_1CAE(): pass

    label('loc_1CAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1D81',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '象征功劳的勋章……\n',
            '衷心祝贺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这枚勋章是授予那些\n',
            '为帝国做出过贡献的人们的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '授予外国人，\n',
            '可是非常罕见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D81')

    def _loc_1D3D(): pass

    label('loc_1D3D')

    ChrTalk(
        0x00FE,
        (
            '各位，务必\n',
            '就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去\n',
            '视察肯定无法恢复了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D81(): pass

    label('loc_1D81')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1D85
@scena.Code('func_0C_1D85')
def func_0C_1D85():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1E9B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1E1A',
    )

    ChrTalk(
        0x00FE,
        (
            '大使已经预定好了返回王都的时间。\n',
            '很快就要起程了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次事件能圆满解决真是多亏你们的帮忙。\n',
            '非常感谢你们，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E98')

    def _loc_1E1A(): pass

    label('loc_1E1A')

    ChrTalk(
        0x00FE,
        (
            '调查的情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大使已经预定好了返回王都的时间。\n',
            '很快就要起程了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调查所剩的时间已经不多了。\n',
            '请多加努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E98(): pass

    label('loc_1E98')

    Jump('loc_21B9')

    def _loc_1E9B(): pass

    label('loc_1E9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1FAD',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1F34',
    )

    ChrTalk(
        0x00FE,
        (
            '由于王国处于警戒状态，\n',
            '我们正在考虑返回王都的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于王国军的戒严，\n',
            '定期船又无法使用，\n',
            '我们唯有竭尽全力寻找其他的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FAA')

    def _loc_1F34(): pass

    label('loc_1F34')

    ChrTalk(
        0x00FE,
        (
            '各位，调查有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于王国处于警戒状态，\n',
            '我们正在寻找返回王都的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '离开大使馆太长时间\n',
            '可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FAA(): pass

    label('loc_1FAA')

    Jump('loc_21B9')

    def _loc_1FAD(): pass

    label('loc_1FAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_20EB',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2005',
    )

    ChrTalk(
        0x00FE,
        (
            '按照行程，\n',
            '正要恢复视察……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到却出了那种事……\n',
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E8')

    def _loc_2005(): pass

    label('loc_2005')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2075',
    )

    ChrTalk(
        0x00FE,
        (
            '光是勋章被盗事件就够\n',
            '我们忙的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然接二连三的出事\n',
            '俗话说屋漏偏逢连夜雨，就是这样的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20E8')

    def _loc_2075(): pass

    label('loc_2075')

    ChrTalk(
        0x00FE,
        (
            '光是勋章被盗事件就够\n',
            '我们忙的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再加上超市那件事\n',
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '俗话说屋漏偏逢连夜雨，就是这样的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_20E8(): pass

    label('loc_20E8')

    Jump('loc_21B9')

    def _loc_20EB(): pass

    label('loc_20EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_21B9',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2169',
    )

    ChrTalk(
        0x00FE,
        (
            '各位游击士，\n',
            '大使也计划不久后恢复视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前真是承蒙你们的照顾。\n',
            '衷心对各位这次的协助表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B9')

    def _loc_2169(): pass

    label('loc_2169')

    ChrTalk(
        0x00FE,
        (
            '为了我帝国的荣誉，\n',
            '请各位一定要发挥实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '务必请将大使的勋章\n',
            '找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21B9(): pass

    label('loc_21B9')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x21BD
@scena.Code('func_0D_21BD')
def func_0D_21BD():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2423',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 2, 0x1A42)),
            Expr.Return,
        ),
        'loc_2252',
    )

    ChrTalk(
        0x00FE,
        (
            '打算暂时借用这里\n',
            '继续营业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '货源虽然不足，\n',
            '但是我还是会一如既往继续努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要什么的话，\n',
            '就和那边的伙计说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2423')

    def _loc_2252(): pass

    label('loc_2252')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢。\n',
            '危难时多亏有你们相救啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F哪里，在非常时期这是应该做的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '超市里面的人\n',
            '全部都成功逃出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，暂时是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在小姐的安排下\n',
            '暂时在这里营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '商店全部关闭的话，\n',
            '会给市民的生活带来麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F不愧是梅贝尔市长。\n',
            '这种时候的反应真迅速。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F虽然很不容易但加油。\n',
            '有什么事我们也会帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '噢，就算是为了小姐也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要什么的话，\n',
            '就和那边的伙计说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A42)

    def _loc_2423(): pass

    label('loc_2423')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x2427
@scena.Code('func_0E_2427')
def func_0E_2427():
    Call(0, 0x000F)

    Return()

# id: 0x000F offset: 0x242C
@scena.Code('func_0F_242C')
def func_0F_242C():
    TalkBegin(0x000F)
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
        'loc_248A',
    )

    OP_0D()
    OP_A9(0x50)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_248A(): pass

    label('loc_248A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_249B',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_249B(): pass

    label('loc_249B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_25AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2504',
    )

    ChrTalk(
        0x00FE,
        (
            '由于军队的作战，\n',
            '定期船一直停航中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是无可奈何的事，\n',
            '但是库存也快没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_2504(): pass

    label('loc_2504')

    ChrTalk(
        0x00FE,
        (
            '由于军队的作战，\n',
            '定期船一直停航中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是无可奈何的事，\n',
            '但是库存也快没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，大家都是一样辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算无视利益，\n',
            '也会维持现在的价格的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_25AA(): pass

    label('loc_25AA')

    Jump('loc_27C7')

    def _loc_25AD(): pass

    label('loc_25AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_26BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_261C',
    )

    ChrTalk(
        0x00FE,
        (
            '超市的修复工程\n',
            '今早开始动工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是天才般的梅贝尔市长。\n',
            '处理事情的手腕的确英明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26B8')

    def _loc_261C(): pass

    label('loc_261C')

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市修复工程，\n',
            '好像今早开始动工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '巴克那家伙\n',
            '听到消息就飞奔过去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对那家伙在这种时候的干劲，\n',
            '说真的，我很羡慕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_26B8(): pass

    label('loc_26B8')

    Jump('loc_27C7')

    def _loc_26BB(): pass

    label('loc_26BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_27C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2701',
    )

    ChrTalk(
        0x00FE,
        (
            '还没冷静下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '超市今后会怎样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C7')

    def _loc_2701(): pass

    label('loc_2701')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2781',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '不过总觉得无法安心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我们设法让店铺继续营业下去……\n',
            '但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '超市今后会怎样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_27C7')

    def _loc_2781(): pass

    label('loc_2781')

    ChrTalk(
        0x00FE,
        (
            '呀，刚才真多亏你们帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '莉拉没事就真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_27C7(): pass

    label('loc_27C7')

    TalkEnd(0x000F)

    Return()

# id: 0x0010 offset: 0x27CB
@scena.Code('func_10_27CB')
def func_10_27CB():
    TalkBegin(0x0010)
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
        'loc_2829',
    )

    OP_0D()
    OP_A9(0x40)
    OP_56(0x00)
    TalkEnd(0x0010)

    Return()

    def _loc_2829(): pass

    label('loc_2829')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_283A',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_283A(): pass

    label('loc_283A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_294C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_28B1',
    )

    ChrTalk(
        0x00FE,
        (
            '说起我老公，\n',
            '他还在担心村子的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望他能多为家里着想，\n',
            '就算是担心村子的几分之一都行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2949')

    def _loc_28B1(): pass

    label('loc_28B1')

    ChrTalk(
        0x00FE,
        (
            '我丈夫真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都到这地步了，\n',
            '还在为村里的事担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村人们又不是小孩子，\n',
            '总会自己想办法的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来就不是\n',
            '该轮到他操心的事儿嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2949(): pass

    label('loc_2949')

    Jump('loc_2A97')

    def _loc_294C(): pass

    label('loc_294C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2A20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_29A5',
    )

    ChrTalk(
        0x00FE,
        (
            '拉文努村的\n',
            '那位先生来了噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候，有男人在\n',
            '可真帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1D')

    def _loc_29A5(): pass

    label('loc_29A5')

    ChrTalk(
        0x00FE,
        (
            '拉文努村的\n',
            '那位先生来了噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候，有男人在\n',
            '可真帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有一肚子话想说，\n',
            '还是暂时忍了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2A1D(): pass

    label('loc_2A1D')

    Jump('loc_2A97')

    def _loc_2A20(): pass

    label('loc_2A20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2A97',
    )

    ChrTalk(
        0x00FE,
        (
            '但我到现在还是不相信\n',
            '会有龙出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在故乡拉文努村\n',
            '过去也有着这样的传说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但没想到居然会是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A97(): pass

    label('loc_2A97')

    TalkEnd(0x0010)

    Return()

# id: 0x0011 offset: 0x2A9B
@scena.Code('func_11_2A9B')
def func_11_2A9B():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2AF2',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈虽然跟我\n',
            '抱怨了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过爸爸能来，\n',
            '她果然还是很开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CA2')

    def _loc_2AF2(): pass

    label('loc_2AF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2BE7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2B53',
    )

    ChrTalk(
        0x00FE,
        (
            '好像拉文努村也\n',
            '出现龙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没有人受伤，\n',
            '但是果树园却被烧毁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BE4')

    def _loc_2B53(): pass

    label('loc_2B53')

    ChrTalk(
        0x00FE,
        (
            '好像听说拉文努村也\n',
            '出现了龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没有人受伤，\n',
            '但是果树园却被烧毁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我很庆幸\n',
            '爸爸他没有受伤。\n',
            '但是感觉有点笑不太出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2BE4(): pass

    label('loc_2BE4')

    Jump('loc_2CA2')

    def _loc_2BE7(): pass

    label('loc_2BE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2CA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2C3F',
    )

    ChrTalk(
        0x00FE,
        (
            '龙朝着爸爸所在的村子的方向\n',
            '飞走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿不要出什么事才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CA2')

    def _loc_2C3F(): pass

    label('loc_2C3F')

    ChrTalk(
        0x00FE,
        (
            '龙好像朝\n',
            '西北方飞去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那方向就是\n',
            '爸爸所在的拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿不要出什么事才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2CA2(): pass

    label('loc_2CA2')

    TalkEnd(0x0011)

    Return()

# id: 0x0012 offset: 0x2CA6
@scena.Code('func_12_2CA6')
def func_12_2CA6():
    TalkBegin(0x0012)
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
        'loc_2D04',
    )

    OP_0D()
    OP_A9(0x3C)
    OP_56(0x00)
    TalkEnd(0x0012)

    Return()

    def _loc_2D04(): pass

    label('loc_2D04')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D15',
    )

    TalkEnd(0x0012)

    Return()

    def _loc_2D15(): pass

    label('loc_2D15')

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2D22',
    )

    OP_A2(0x000A)

    def _loc_2D22(): pass

    label('loc_2D22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D98',
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
            TXT(0x00, '【◇前编QST017通关】\n'),
            TXT(0x01, '【◇前编QST017没有通关】\n'),
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
        (0x00000000, 'loc_2D8C'),
        (0x00000001, 'loc_2D92'),
        (-1, 'loc_2D98'),
    )

    def _loc_2D8C(): pass

    label('loc_2D8C')

    OP_A2(0x000A)

    Jump('loc_2D98')

    def _loc_2D92(): pass

    label('loc_2D92')

    OP_A3(0x000A)

    Jump('loc_2D98')

    def _loc_2D98(): pass

    label('loc_2D98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 0, 0x1A40)),
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2FAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2E02',
    )

    ChrTalk(
        0x00FE,
        (
            '看来超市的修复工程\n',
            '进展很顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像很久都没有听到\n',
            '好消息了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F57')

    def _loc_2E02(): pass

    label('loc_2E02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2E4C',
    )

    ChrTalk(
        0x00FE,
        (
            '超市的修复工作\n',
            '好像开始了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能\n',
            '早日恢复就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F57')

    def _loc_2E4C(): pass

    label('loc_2E4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2F57',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2EC1',
    )

    ChrTalk(
        0x00FE,
        (
            '目前我们的计划是\n',
            '借用这里的场地来维持买卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大家都不知道\n',
            '超市什么时候才能恢复营运啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F57')

    def _loc_2EC1(): pass

    label('loc_2EC1')

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，总之\n',
            '把做买卖的道具都带出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目前我们的计划是\n',
            '借用这里的场地来维持买卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大家都不知道\n',
            '超市什么时候才能恢复营运啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_2F57(): pass

    label('loc_2F57')

    Jump('loc_2FAC')

    def _loc_2F5A(): pass

    label('loc_2F5A')

    ChrTalk(
        0x00FE,
        (
            '这药代表了我\n',
            '支持你们的心意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这药的效果很不错，\n',
            '我想应该能够派上用场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2FAC(): pass

    label('loc_2FAC')

    Jump('loc_32C2')

    def _loc_2FAF(): pass

    label('loc_2FAF')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，各位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '曾经帮我寻找药草的\n',
            '游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F好象……\n',
            '的确有这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F老爷爷\n',
            '现在还在这里做买卖？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是的，目前这段时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这时候药店关门的话，\n',
            '大家会很为难的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_313C',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嘿，我们也正需要您的药品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F因为我们马上\n',
            '准备去做一件麻烦的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '麻烦的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是关于龙的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，是的，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31D8')

    def _loc_313C(): pass

    label('loc_313C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_31D8',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嘿，我们也正需要您的药品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F因为我们马上\n',
            '准备出城调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调查？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是关于之前龙的那件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F嗯，是与之相关的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31D8(): pass

    label('loc_31D8')

    ChrTalk(
        0x00FE,
        (
            '这样的话，\n',
            '让我也来帮你们一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['还魂粉'], 1)

    ChrTalk(
        0x00FE,
        (
            '这是效果很不错的药，\n',
            '我想肯定能帮到你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '期待你们工作顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F谢谢爷爷。\n',
            '我们会好好使用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A40)
    OP_A2(0x0008)
    def _loc_32C2(): pass

    label('loc_32C2')

    TalkEnd(0x0012)

    Return()

# id: 0x0013 offset: 0x32C6
@scena.Code('func_13_32C6')
def func_13_32C6():
    TalkBegin(0x0013)
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
        'loc_3330',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3328',
    )

    OP_A9(0x44)

    Jump('loc_332A')

    def _loc_3328(): pass

    label('loc_3328')

    OP_A9(0x42)

    def _loc_332A(): pass

    label('loc_332A')

    OP_56(0x00)
    TalkEnd(0x0013)

    Return()

    def _loc_3330(): pass

    label('loc_3330')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3341',
    )

    TalkEnd(0x0013)

    Return()

    def _loc_3341(): pass

    label('loc_3341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_342D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_33A0',
    )

    ChrTalk(
        0x00FE,
        (
            '由于军队的戒严，\n',
            '定期船还在停航中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，商品的货源\n',
            '将更加紧张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342A')

    def _loc_33A0(): pass

    label('loc_33A0')

    ChrTalk(
        0x00FE,
        (
            '由于军队的戒严，\n',
            '定期船还在停开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，为了抓住龙\n',
            '这么做还是有必要的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都做到这地步了，\n',
            '真希望能够百分之一百成功啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_342A(): pass

    label('loc_342A')

    Jump('loc_36E5')

    def _loc_342D(): pass

    label('loc_342D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_351B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3494',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军好像\n',
            '正在做抓捕龙的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还记得……\n',
            '小时候老师说龙是神圣的生物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3518')

    def _loc_3494(): pass

    label('loc_3494')

    ChrTalk(
        0x00FE,
        (
            '王国军好像\n',
            '正在做抓捕龙的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还记得……\n',
            '小时候老师说龙是神圣的生物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如去抓捕它的话，\n',
            '是不是会遭天遣呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3518(): pass

    label('loc_3518')

    Jump('loc_36E5')

    def _loc_351B(): pass

    label('loc_351B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_36E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_35D1',
    )

    ChrTalk(
        0x00FE,
        (
            '那时候有一瞬间，我眼前浮现出\n',
            '战争的景象了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过呢，我们的超市\n',
            '就算化成了灰烬也还是会再建起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是龙来了还是炸弹投下来了，\n',
            '我们都会让它复活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36E5')

    def _loc_35D1(): pass

    label('loc_35D1')

    ChrTalk(
        0x00FE,
        (
            '瓦砾掉下来的时候，\n',
            '我又想起了那时战争的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候也是天花板燃烧着往下塌，\n',
            '大家一个劲的逃命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过呢，不能忘记的是，\n',
            '即便如此也能重新建起超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要我们永不放弃，\n',
            '不管遇到怎样的挫折都能够再次站立起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战争对我来说，\n',
            '是一个不可磨灭的记忆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_36E5(): pass

    label('loc_36E5')

    TalkEnd(0x0013)

    Return()

# id: 0x0014 offset: 0x36E9
@scena.Code('func_14_36E9')
def func_14_36E9():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3804',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_375F',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军抓捕龙的作战之中，\n',
            '好像『埃尔赛尤』也参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '计划的真好，\n',
            '真希望能顺利赶走龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3801')

    def _loc_375F(): pass

    label('loc_375F')

    ChrTalk(
        0x00FE,
        (
            '王国军抓捕龙的作战之中，\n',
            '好像『埃尔赛尤』也参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是女王陛下发表的声明，\n',
            '王国军给人一种全力出击的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么到最后，\n',
            '那次作战成功了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3801(): pass

    label('loc_3801')

    Jump('loc_3A04')

    def _loc_3804(): pass

    label('loc_3804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3917',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3871',
    )

    ChrTalk(
        0x00FE,
        (
            '现在借用了酒店的房间\n',
            '可以继续营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯商人的那种互相帮助\n',
            '的精神可真令人钦佩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3914')

    def _loc_3871(): pass

    label('loc_3871')

    ChrTalk(
        0x00FE,
        (
            '在梅贝尔市长的安排下，\n',
            '现在借用了酒店的房间\n',
            '可以继续营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯商人的那种互相帮助\n',
            '的精神可真令人钦佩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为有这样的基础\n',
            '才能从战争中恢复啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3914(): pass

    label('loc_3914')

    Jump('loc_3A04')

    def _loc_3917(): pass

    label('loc_3917')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3A04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3978',
    )

    ChrTalk(
        0x00FE,
        (
            '米蕾婆婆跑回去拿商品，\n',
            '可真让人着急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '婆婆真不愧是超市\n',
            '里的风云人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A04')

    def _loc_3978(): pass

    label('loc_3978')

    ChrTalk(
        0x00FE,
        (
            '我，我们……\n',
            '总算是……平安逃出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米蕾婆婆在半路上\n',
            '又跑回去拿商品可真让人着急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从战火中过来的人\n',
            '的胆识果然了得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3A04(): pass

    label('loc_3A04')

    TalkEnd(0x0014)

    Return()

# id: 0x0015 offset: 0x3A08
@scena.Code('func_15_3A08')
def func_15_3A08():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3B00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3A74',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船明明停航了，\n',
            '但蔬菜的价格却没有上涨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真奇怪啊……\n',
            '还以为一定会涨价呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AFD')

    def _loc_3A74(): pass

    label('loc_3A74')

    ChrTalk(
        0x00FE,
        (
            '我是来逛\n',
            '蔬果店的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船明明停航了，\n',
            '但蔬菜的价格却没有上涨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真奇怪啊……\n',
            '原本以为一定会涨价，\n',
            '结果提早买了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_3AFD(): pass

    label('loc_3AFD')

    Jump('loc_3CC9')

    def _loc_3B00(): pass

    label('loc_3B00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3C02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3B6F',
    )

    ChrTalk(
        0x00FE,
        (
            '就算稍微贵一点，\n',
            '好象也是现在买比较划算吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，买没打折的东西\n',
            '总有种失败感呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BFF')

    def _loc_3B6F(): pass

    label('loc_3B6F')

    ChrTalk(
        0x00FE,
        (
            '听说了吗？定期船好像\n',
            '还没恢复航行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是说，蔬菜的价格\n',
            '渐渐会开始上涨是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算稍微贵一点，\n',
            '好象也是现在买比较划算吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_3BFF(): pass

    label('loc_3BFF')

    Jump('loc_3CC9')

    def _loc_3C02(): pass

    label('loc_3C02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3CC9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_3C56',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯嗯……\n',
            '商人们好像在避难的地方做买卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CC9')

    def _loc_3C56(): pass

    label('loc_3C56')

    ChrTalk(
        0x00FE,
        (
            '嗯嗯……\n',
            '商人们好像在避难的地方做买卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还没决定晚饭要吃什么呢。\n',
            '吃什么好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_3CC9(): pass

    label('loc_3CC9')

    TalkEnd(0x0015)

    Return()

# id: 0x0016 offset: 0x3CCD
@scena.Code('func_16_3CCD')
def func_16_3CCD():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3DC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_3D37',
    )

    ChrTalk(
        0x0016,
        (
            '定期船停航了，\n',
            '每一家店铺都很繁忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '果然……\n',
            '还没有到开商业洽谈会的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DC3')

    def _loc_3D37(): pass

    label('loc_3D37')

    ChrTalk(
        0x0016,
        (
            '定期船停航了，\n',
            '每一家店铺都很繁忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '果然……\n',
            '还没有到开商业洽谈会的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '直到超市恢复营业前，\n',
            '除了等没有别的可做了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_3DC3(): pass

    label('loc_3DC3')

    Jump('loc_3E91')

    def _loc_3DC6(): pass

    label('loc_3DC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3E91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_3E19',
    )

    ChrTalk(
        0x0016,
        (
            '超市的店铺\n',
            '好像暂时在这里营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '那么，\n',
            '周围先转一圈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E91')

    def _loc_3E19(): pass

    label('loc_3E19')

    ChrTalk(
        0x0016,
        (
            '超市的店铺\n',
            '好像暂时在这里营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '那么，\n',
            '周围先转一圈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '可能营业方面有点吃紧，\n',
            '但是还是想去打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_3E91(): pass

    label('loc_3E91')

    TalkEnd(0x0016)

    Return()

# id: 0x0017 offset: 0x3E95
@scena.Code('func_17_3E95')
def func_17_3E95():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3F85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_3EEA',
    )

    ChrTalk(
        0x00FE,
        (
            '我很担心拉文努村啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '贝斯卡和库赖\n',
            '能和睦相处就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F82')

    def _loc_3EEA(): pass

    label('loc_3EEA')

    ChrTalk(
        0x00FE,
        (
            '虽然匆匆忙忙\n',
            '离开拉文努村来到了这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但果然还是担心村子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '贝斯卡和库赖\n',
            '能和睦相处就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟他们两个\n',
            '一直坚持到现在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    def _loc_3F82(): pass

    label('loc_3F82')

    Jump('loc_4014')

    def _loc_3F85(): pass

    label('loc_3F85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_4014',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_3FC1',
    )

    ChrTalk(
        0x00FE,
        (
            '老婆和孩子没有受伤，\n',
            '我总算松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4014')

    def _loc_3FC1(): pass

    label('loc_3FC1')

    ChrTalk(
        0x00FE,
        (
            '这里的超市\n',
            '好像被破坏了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之老婆和孩子没有受伤，\n',
            '我总算松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    def _loc_4014(): pass

    label('loc_4014')

    TalkEnd(0x0017)

    Return()

# id: 0x0018 offset: 0x4018
@scena.Code('func_18_4018')
def func_18_4018():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_40BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4088',
    )

    ChrTalk(
        0x00FE,
        (
            '糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钱包差不多\n',
            '快空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然手上有回去的船票，\n',
            '但船不来也没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    Jump('loc_40B7')

    def _loc_4088(): pass

    label('loc_4088')

    ChrTalk(
        0x00FE,
        (
            '糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钱包差不多\n',
            '快要光溜溜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40B7(): pass

    label('loc_40B7')

    Jump('loc_4184')

    def _loc_40BA(): pass

    label('loc_40BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4184',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4138',
    )

    ChrTalk(
        0x00FE,
        (
            '我是来柏斯参观\n',
            '哈肯大门的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到在旅行的目的地\n',
            '会遇到这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之希望\n',
            '能早日恢复啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    Jump('loc_4184')

    def _loc_4138(): pass

    label('loc_4138')

    ChrTalk(
        0x00FE,
        (
            '没想到在旅行的目的地\n',
            '会出这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望定期船能\n',
            '早日恢复航行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4184(): pass

    label('loc_4184')

    TalkEnd(0x0018)

    Return()

# id: 0x0019 offset: 0x4188
@scena.Code('func_19_4188')
def func_19_4188():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4214',
    )

    ChrTalk(
        0x00FE,
        (
            '我的导力照相机也\n',
            '无法使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易有机会\n',
            '能拍到哈肯大门的威容……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔，好想快点\n',
            '看到冲洗出来的照片啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    Jump('loc_425A')

    def _loc_4214(): pass

    label('loc_4214')

    ChrTalk(
        0x00FE,
        (
            '我的导力照相机也\n',
            '无法使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在没办法冲洗\n',
            '真让人着急啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_425A(): pass

    label('loc_425A')

    TalkEnd(0x0019)

    Return()

# id: 0x001A offset: 0x425E
@scena.Code('func_1A_425E')
def func_1A_425E():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4308',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然安排的很仓促，\n',
            '但还是很不错的酒店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '并且住宿费全由\n',
            '飞船公社承担……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '觉得有种因祸得福的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过现在\n',
            '可不是高兴的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    Jump('loc_4362')

    def _loc_4308(): pass

    label('loc_4308')

    ChrTalk(
        0x00FE,
        (
            '虽然安排的很仓促，\n',
            '但还是很不错的酒店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞船公社的服务还是\n',
            '十分令人满意的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4362(): pass

    label('loc_4362')

    TalkEnd(0x001A)

    Return()

# id: 0x001B offset: 0x4366
@scena.Code('func_1B_4366')
def func_1B_4366():
    TalkBegin(0x001B)

    ChrTalk(
        0x00FE,
        (
            '能这么快住进酒店，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我跟女儿\n',
            '都很累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001B)

    Return()

# id: 0x001C offset: 0x43AB
@scena.Code('func_1C_43AB')
def func_1C_43AB():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43F0',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的澡堂\n',
            '很不错哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是公主\n',
            '用的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0014)

    Jump('loc_440B')

    def _loc_43F0(): pass

    label('loc_43F0')

    ChrTalk(
        0x00FE,
        (
            '这里的澡堂\n',
            '很不错哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_440B(): pass

    label('loc_440B')

    TalkEnd(0x001C)

    Return()

# id: 0x001D offset: 0x440F
@scena.Code('func_1D_440F')
def func_1D_440F():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44AD',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然很感谢能\n',
            '为我们准备房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这也就是说，定期船要停航\n',
            '很长一段时间是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也罢，这也是没有办法的。\n',
            '先去洗个澡放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    Jump('loc_4501')

    def _loc_44AD(): pass

    label('loc_44AD')

    ChrTalk(
        0x00FE,
        (
            '看来定期船要\n',
            '停航很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也罢，这也是没有办法的。\n',
            '先去洗个澡放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4501(): pass

    label('loc_4501')

    TalkEnd(0x001D)

    Return()

# id: 0x001E offset: 0x4505
@scena.Code('func_1E_4505')
def func_1E_4505():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　工作人员室　　　　　　　\n',
            '          ※无关人员请勿入内',
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
