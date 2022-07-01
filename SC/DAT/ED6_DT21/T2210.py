import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2210   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '弗洛拉'),
    TXT(0x02, '多米尼克'),
    TXT(0x03, '比古'),
    TXT(0x04, '王国军宪兵'),
    TXT(0x05, '达里奥'),
    TXT(0x06, '索雷诺'),
    TXT(0x07, '诺曼市长'),
    TXT(0x08, '秘书德尔斯'),
    TXT(0x09, '贝尔夫'),
    TXT(0x0A, '杯子'),
    TXT(0x0B, '杯子'),
    TXT(0x0C, '水壶'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2210.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x30E1
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
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 34540,
            z                   = 0,
            y                   = 27220,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -63810,
            z                   = 0,
            y                   = 34870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 33500,
            z                   = 0,
            y                   = 24400,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 2620,
            z                   = 0,
            y                   = 3200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 67820,
            z                   = -30,
            y                   = -5200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 800,
            z                   = 0,
            y                   = 2100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -64500,
            z                   = 0,
            y                   = 33170,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -7500,
            z                   = 0,
            y                   = 33230,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 36150,
            z                   = 0,
            y                   = 34260,
            direction           = 193,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 35510,
            z                   = 750,
            y                   = 27280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638400,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 35450,
            z                   = 750,
            y                   = 26890,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638400,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 35490,
            z                   = 750,
            y                   = 26520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703936,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x272
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x272
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x272
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -475,
            triggerZ            = 0,
            triggerY            = 3173,
            triggerRange        = 800,
            actorX              = -475,
            actorZ              = 800,
            actorY              = 3173,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -63800,
            triggerZ            = 0,
            triggerY            = 50790,
            triggerRange        = 900,
            actorX              = -63800,
            actorZ              = -300,
            actorY              = 50790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -62370,
            triggerZ            = 0,
            triggerY            = -43110,
            triggerRange        = 500,
            actorX              = -62370,
            actorZ              = 2000,
            actorY              = -43110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -59500,
            triggerZ            = 250,
            triggerY            = -36760,
            triggerRange        = 800,
            actorX              = -59500,
            actorZ              = 1250,
            actorY              = -36760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x302
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B8',
    )

    SetChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x000A, 33760, 0, 25890, 270)
    SetChrPos(0x0008, -4550, 0, -4059, 95)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_365',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0009, 67400, 0, 32619, 270)

    Jump('loc_3B5')

    def _loc_365(): pass

    label('loc_365')

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 4070, 0, 35300, 270)
    SetChrPos(0x0009, -1900, 0, 4450, 90)
    SetChrPos(0x000F, -61820, 0, 30050, 355)
    SetChrPos(0x0008, -2750, 0, 42770, 342)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_3B5(): pass

    label('loc_3B5')

    Jump('loc_401')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    SetChrPos(0x0008, 35530, 0, 34250, 180)

    Jump('loc_401')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_3DD',
    )

    Jump('loc_401')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3FA',
    )

    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)

    Jump('loc_401')

    def _loc_3FA(): pass

    label('loc_3FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_401',
    )

    def _loc_401(): pass

    label('loc_401')

    Return()

# id: 0x0001 offset: 0x402
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_42C',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)

    def _loc_42C(): pass

    label('loc_42C')

    OP_72(0x0010, 0x0010)
    OP_72(0x0010, 0x0008)
    OP_6F(0x0010, 360)

    Return()

# id: 0x0002 offset: 0x43E
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
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
        'loc_463',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_5A5')

    def _loc_463(): pass

    label('loc_463')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47C',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_5A5')

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_495',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_5A5')

    def _loc_495(): pass

    label('loc_495')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AE',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_5A5')

    def _loc_4AE(): pass

    label('loc_4AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C7',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_5A5')

    def _loc_4C7(): pass

    label('loc_4C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E0',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_5A5')

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F9',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_5A5')

    def _loc_4F9(): pass

    label('loc_4F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_512',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_5A5')

    def _loc_512(): pass

    label('loc_512')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_5A5')

    def _loc_52B(): pass

    label('loc_52B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_544',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_5A5')

    def _loc_544(): pass

    label('loc_544')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_5A5')

    def _loc_55D(): pass

    label('loc_55D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_576',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_5A5')

    def _loc_576(): pass

    label('loc_576')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_5A5')

    def _loc_58F(): pass

    label('loc_58F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A5',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5BA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5A5')

    def _loc_5BA(): pass

    label('loc_5BA')

    Return()

# id: 0x0003 offset: 0x5BB
@scena.Code('func_03_5BB')
def func_03_5BB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_635',
    )

    def _loc_5C2(): pass

    label('loc_5C2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_632',
    )

    OP_8E(0x00FE, -4500, 0, -5470, 1000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    OP_8C(0x00FE, 90, 400)
    Sleep(3500)

    OP_8E(0x00FE, -4500, 0, -3580, 1000, 0x00)
    OP_8C(0x00FE, 90, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(4500)

    Jump('loc_5C2')

    def _loc_632(): pass

    label('loc_632')

    Jump('loc_697')

    def _loc_635(): pass

    label('loc_635')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_63F(): pass

    label('loc_63F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_697',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_694',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_68A',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)

    def _loc_68A(): pass

    label('loc_68A')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_694(): pass

    label('loc_694')

    Jump('loc_63F')

    def _loc_697(): pass

    label('loc_697')

    Return()

# id: 0x0004 offset: 0x698
@scena.Code('func_04_698')
def func_04_698():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_763',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_6F6',
    )

    ChrTalk(
        0x00FE,
        (
            '伙食非常美味，\n',
            '不知不觉吃太多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样工作下去\n',
            '会不断长胖的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_760')

    def _loc_6F6(): pass

    label('loc_6F6')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '嗯～厨房\n',
            '飘来好香的味道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的厨师做的饭菜\n',
            '非常非常好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此我的皮带\n',
            '都紧起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_760(): pass

    label('loc_760')

    Jump('loc_997')

    def _loc_763(): pass

    label('loc_763')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_81C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_7B8',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然在自己家里\n',
            '养魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然还有人\n',
            '会去想这么可怕的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_819')

    def _loc_7B8(): pass

    label('loc_7B8')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '房间二楼的\n',
            '秘密魔兽饲养房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……看过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然还有人\n',
            '会去想这么可怕的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_819(): pass

    label('loc_819')

    Jump('loc_997')

    def _loc_81C(): pass

    label('loc_81C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_902',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_88B',
    )

    ChrTalk(
        0x00FE,
        (
            '对这等美术品出手的\n',
            '只可能是绝顶的笨蛋或者天才了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '普通的盗贼\n',
            '还是有自知之明的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8FF')

    def _loc_88B(): pass

    label('loc_88B')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '从这里的女佣\n',
            '那里听说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前不久这个烛台\n',
            '被偷走过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好厉害的家伙……不、不，\n',
            '竟然有这么坏的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8FF(): pass

    label('loc_8FF')

    Jump('loc_997')

    def _loc_902(): pass

    label('loc_902')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_997',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_948',
    )

    ChrTalk(
        0x00FE,
        (
            '所、所以不要\n',
            '在这附近转悠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也很紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_997')

    def _loc_948(): pass

    label('loc_948')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '这个烛台现在\n',
            '由王国军代为保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别太靠近。\n',
            '这可是相当贵重的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_997(): pass

    label('loc_997')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x99B
@scena.Code('func_05_99B')
def func_05_99B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_A74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A13',
    )

    ChrTalk(
        0x00FE,
        (
            '这是使用柴火的暖炉。\n',
            '最近的炊事都靠这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来是想要用火才做的，\n',
            '没想到会这么有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_A71')

    def _loc_A13(): pass

    label('loc_A13')

    ChrTalk(
        0x00FE,
        (
            '这是使用柴火的暖炉。\n',
            '最近的炊事都靠这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，适用范围\n',
            '稍微窄了点，也没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A71(): pass

    label('loc_A71')

    Jump('loc_DE6')

    def _loc_A74(): pass

    label('loc_A74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B02',
    )

    ChrTalk(
        0x00FE,
        (
            '管家达里奥\n',
            '回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多年服侍戴尔蒙家\n',
            '的同伴都在一起就心安多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么快就欠了雇佣我们的\n',
            '新市长的人情了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_B52')

    def _loc_B02(): pass

    label('loc_B02')

    ChrTalk(
        0x00FE,
        (
            '达里奥那家伙\n',
            '回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为服侍戴尔蒙家的同伴，\n',
            '他回来可让人心安多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B52(): pass

    label('loc_B52')

    Jump('loc_DE6')

    def _loc_B55(): pass

    label('loc_B55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_C0D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_BAC',
    )

    ChrTalk(
        0x00FE,
        (
            '好，差不多\n',
            '该准备午饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我为了士兵们\n',
            '加倍卖力的自信作品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C0A')

    def _loc_BAC(): pass

    label('loc_BAC')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '今天的伙食\n',
            '是加了橘子调味汁\n',
            '的照烧仔鸡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是我将东方的烹调法\n',
            '加以调整的自信作品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C0A(): pass

    label('loc_C0A')

    Jump('loc_DE6')

    def _loc_C0D(): pass

    label('loc_C0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_C6B',
    )

    ChrTalk(
        0x00FE,
        (
            '我也一直在担心\n',
            '达里奥那家伙的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长被逮捕之后\n',
            '他的情况确实很奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE6')

    def _loc_C6B(): pass

    label('loc_C6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D19',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_CBD',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们也不挑食，\n',
            '吃得都很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，也算做得值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D16')

    def _loc_CBD(): pass

    label('loc_CBD')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '我现在负责佣人和士兵们\n',
            '的伙食。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这房子也待了很久了。\n',
            '就让我效劳到最后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D16(): pass

    label('loc_D16')

    Jump('loc_DE6')

    def _loc_D19(): pass

    label('loc_D19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_DE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_D74',
    )

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '我一直在服侍戴尔蒙家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '家道没落了，\n',
            '还真是可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE6')

    def _loc_D74(): pass

    label('loc_D74')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长确实\n',
            '做了坏事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我和管家达里奥\n',
            '都服侍戴尔蒙家多年了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '家道没落了，\n',
            '实在是难过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE6(): pass

    label('loc_DE6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xDEA
@scena.Code('func_06_DEA')
def func_06_DEA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_E4B',
    )

    ChrTalk(
        0x00FE,
        (
            '没有了导力器的光，\n',
            '这个烛台也真可怜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就跟被导力文明所装点的\n',
            '我们一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DD')

    def _loc_E4B(): pass

    label('loc_E4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EDD',
    )

    ChrTalk(
        0x00FE,
        (
            '达里奥也完全\n',
            '恢复状态了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有段时间还形迹可疑，\n',
            '让人感觉诡异呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何，有个熟悉这里\n',
            '的人在真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_F29')

    def _loc_EDD(): pass

    label('loc_EDD')

    ChrTalk(
        0x00FE,
        (
            '达里奥也完全\n',
            '恢复状态了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有段时间还形迹可疑，\n',
            '让人感觉诡异呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F29(): pass

    label('loc_F29')

    Jump('loc_11DD')

    def _loc_F2C(): pass

    label('loc_F2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_FC6',
    )

    ChrTalk(
        0x00FE,
        (
            '根据市长选举的结果\n',
            '找工作的方针也要发生变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果诺曼获胜就找旅游相关职业，\n',
            '要是波尔多斯就去港口酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼哼，完美的再就业计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DD')

    def _loc_FC6(): pass

    label('loc_FC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_FF7',
    )

    ChrTalk(
        0x00FE,
        (
            '外面好像\n',
            '很吵闹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DD')

    def _loc_FF7(): pass

    label('loc_FF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1131',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1062',
    )

    ChrTalk(
        0x00FE,
        (
            '事件之后，管家达里奥\n',
            '好像变得很奇怪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长被逮捕\n',
            '似乎让他相当震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_112E')

    def _loc_1062(): pass

    label('loc_1062')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '最近，这里的旧管家\n',
            '达里奥好像都不见人影呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到底，那个人\n',
            '在市长被逮捕以后\n',
            '就变得有点奇怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『还有一个我！』什么的\n',
            '都说出来了，真是不太妙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '戴尔蒙市长被逮捕\n',
            '看来让他相当震惊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_112E(): pass

    label('loc_112E')

    Jump('loc_11DD')

    def _loc_1131(): pass

    label('loc_1131')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_11DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1194',
    )

    ChrTalk(
        0x00FE,
        (
            '军队管理期间还好，\n',
            '此后会变成怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁现在找到下一份工作\n',
            '会比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DD')

    def _loc_1194(): pass

    label('loc_1194')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '军队管理期间还好，\n',
            '此后会变成怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '佣人还是\n',
            '会被解雇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11DD(): pass

    label('loc_11DD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x11E1
@scena.Code('func_07_11E1')
def func_07_11E1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1236',
    )

    ChrTalk(
        0x00FE,
        (
            '除尘器也不能使用\n',
            '扫除可辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这栋房子\n',
            '竟然这么宽广啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1639')

    def _loc_1236(): pass

    label('loc_1236')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1340',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12E5',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎～\n',
            '欢迎光临市长官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们大家全部\n',
            '都被新市长雇佣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用，\n',
            '做家务虽然辛苦点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但大家一起努力\n',
            '一定能渡过难关的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_133D')

    def _loc_12E5(): pass

    label('loc_12E5')

    ChrTalk(
        0x00FE,
        (
            '我们大家全部\n',
            '都被新市长雇佣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '达里奥先生也回来了，\n',
            '这下一切都恢复原样了吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_133D(): pass

    label('loc_133D')

    Jump('loc_1639')

    def _loc_1340(): pass

    label('loc_1340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_13D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1386',
    )

    ChrTalk(
        0x00FE,
        (
            '我虽然想在这房子里\n',
            '工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是很难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13CD')

    def _loc_1386(): pass

    label('loc_1386')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '多米尼克已经\n',
            '在找下一份工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来\n',
            '我也着急起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13CD(): pass

    label('loc_13CD')

    Jump('loc_1639')

    def _loc_13D0(): pass

    label('loc_13D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_14AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_141A',
    )

    ChrTalk(
        0x00FE,
        (
            '最近一直没见着\n',
            '管家达里奥的身影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A7')

    def _loc_141A(): pass

    label('loc_141A')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '扫除的时候和多米尼克\n',
            '聊天来着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一直没见着\n',
            '管家达里奥的身影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事件之后\n',
            '情况就很奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '达里奥到底\n',
            '怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A7(): pass

    label('loc_14A7')

    Jump('loc_1639')

    def _loc_14AA(): pass

    label('loc_14AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_153D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_14F9',
    )

    ChrTalk(
        0x00FE,
        (
            '啦啦～啦⊙\n',
            '噜噜噜噜～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵先生们\n',
            '人都很好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_153A')

    def _loc_14F9(): pass

    label('loc_14F9')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '啦啦～啦⊙\n',
            '噜噜噜噜～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在准备\n',
            '给士兵们的茶呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_153A(): pass

    label('loc_153A')

    Jump('loc_1639')

    def _loc_153D(): pass

    label('loc_153D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1639',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_15A6',
    )

    ChrTalk(
        0x00FE,
        (
            '老爷被逮捕的时候\n',
            '还在想会变成怎样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来暂时还能和以前一样\n',
            '在这里生活下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1639')

    def _loc_15A6(): pass

    label('loc_15A6')

    OP_A2(0x0000)

    ChrTalk(
        0x00FE,
        (
            '现在，这栋房子\n',
            '由王国军管理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了维持宅邸的管理。\n',
            '我们佣人们\n',
            '也维持原样被雇佣了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，幸好军队的士兵们\n',
            '都是和善的好人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1639(): pass

    label('loc_1639')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x163D
@scena.Code('func_08_163D')
def func_08_163D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_174C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1705',
    )

    ChrTalk(
        0x00FE,
        (
            '如此非常时期\n',
            '竟然又发生事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这世道\n',
            '是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想来前市长的事件\n',
            '也是难以理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不，没什么好说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前市长的过失是事实。\n',
            '有罪就要认罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1749')

    def _loc_1705(): pass

    label('loc_1705')

    ChrTalk(
        0x00FE,
        (
            '如此非常时期\n',
            '竟然又发生事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底这世道\n',
            '是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1749(): pass

    label('loc_1749')

    Jump('loc_1858')

    def _loc_174C(): pass

    label('loc_174C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1858',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1804',
    )

    ChrTalk(
        0x00FE,
        (
            '我是在戴尔蒙家\n',
            '服侍多年的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '受新市长的委托，\n',
            '我作为这个市长官邸的管家\n',
            '重新回到这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我当作重获新生\n',
            '诚心诚意来服侍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '任何事都\n',
            '敬请吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1858')

    def _loc_1804(): pass

    label('loc_1804')

    ChrTalk(
        0x00FE,
        (
            '作为市长官邸的管家\n',
            '又回到宅邸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能和同伴们一起工作的幸福\n',
            '我要牢牢抓住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1858(): pass

    label('loc_1858')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x185C
@scena.Code('func_09_185C')
def func_09_185C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_194A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18F3',
    )

    ChrTalk(
        0x00FE,
        (
            '我面见了市长，\n',
            '请求对玛诺利亚紧急支持……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是卢安市\n',
            '好像情况也相当严峻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诺曼市长的严肃表情\n',
            '完全说明了这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1947')

    def _loc_18F3(): pass

    label('loc_18F3')

    ChrTalk(
        0x00FE,
        (
            '已经请求支持村子，\n',
            '但是卢安的状况也很严峻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诺曼市长\n',
            '看起来也相当疲劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1947(): pass

    label('loc_1947')

    Jump('loc_1A46')

    def _loc_194A(): pass

    label('loc_194A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A46',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19E6',
    )

    ChrTalk(
        0x00FE,
        (
            '作为玛诺利亚村的村长代理，\n',
            '我是来向卢安市长请愿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '需要尽早请求食品和燃料\n',
            '的支援啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，立刻去跟新市长\n',
            '打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1A46')

    def _loc_19E6(): pass

    label('loc_19E6')

    ChrTalk(
        0x00FE,
        (
            '作为玛诺利亚村的村长代理，\n',
            '我是来向卢安市长请愿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '需要尽早请求食品和燃料\n',
            '的支援啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A46(): pass

    label('loc_1A46')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1A4A
@scena.Code('func_0A_1A4A')
def func_0A_1A4A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1DC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 4, 0x20BC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C7D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1AB7',
    )

    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦哦，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚刚收到学院事件\n',
            '的报告呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AFD')

    def _loc_1AB7(): pass

    label('loc_1AB7')

    ChrTalk(
        0x00FE,
        (
            '哦哦……\n',
            '你们就是那些游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好收到学院事件\n',
            '的报告呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AFD(): pass

    label('loc_1AFD')

    ChrTalk(
        0x0101,
        (
            '#1011F哦～消息真灵通啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是嘉恩先生\n',
            '告知的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，从协会\n',
            '来了使者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，这么说来\n',
            '还没打招呼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1C03',
    )

    ChrTalk(
        0x00FE,
        (
            '和以前见面时相比\n',
            '我的立场也发生了变化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是这次就任新市长\n',
            '的诺曼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3A')

    def _loc_1C03(): pass

    label('loc_1C03')

    ChrTalk(
        0x00FE,
        (
            '我是这次就任新市长\n',
            '的诺曼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3A(): pass

    label('loc_1C3A')

    ChrTalk(
        0x0101,
        (
            '#1000F哪里哪里，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F恭喜您当选市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000B)

    Jump('loc_1DBF')

    def _loc_1C7D(): pass

    label('loc_1C7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1CBF',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也\n',
            '下定了决心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能尽快\n',
            '解决这个情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DBF')

    def _loc_1CBF(): pass

    label('loc_1CBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D44',
    )

    ChrTalk(
        0x00FE,
        (
            '关于学院的事件\n',
            '刚刚才收到报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '勤务员实在可怜，\n',
            '不过据说平安解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '代表市民，也让我\n',
            '重新表示感谢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_1DBF')

    def _loc_1D44(): pass

    label('loc_1D44')

    ChrTalk(
        0x00FE,
        (
            '关于学院的事件\n',
            '刚刚收到报告呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种非常时期的占据事件\n',
            '实在是令人难以置信的暴行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人们应该\n',
            '受到严惩才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DBF(): pass

    label('loc_1DBF')

    Jump('loc_20CC')

    def _loc_1DC2(): pass

    label('loc_1DC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_20CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 4, 0x20BC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2030',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1F72',
    )

    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦哦，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '选举中的酒店事件时\n',
            '承蒙关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊～那个事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，记得很～清楚哦。\n',
            '你的头还撞在门上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#1048F什么？那个事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是丢脸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，趁此机会\n',
            '请让我重新自我介绍一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和以前见面时相比\n',
            '我的立场也发生了变化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是就任新市长的诺曼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FED')

    def _loc_1F72(): pass

    label('loc_1F72')

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '你们是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是初次见面，\n',
            '请让我重新自我介绍一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是就任新市长的诺曼。\n',
            '以后也请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FED(): pass

    label('loc_1FED')

    ChrTalk(
        0x0101,
        (
            '#1000F哪里哪里，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F恭喜您当选市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000B)

    Jump('loc_20CC')

    def _loc_2030(): pass

    label('loc_2030')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_207E',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也\n',
            '下定了决心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '祈祷事件能尽快解决，\n',
            '期待诸位的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20CC')

    def _loc_207E(): pass

    label('loc_207E')

    ChrTalk(
        0x00FE,
        (
            '总之市民生活的稳定\n',
            '可以说是当前的课题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为此现在正在\n',
            '寻求各方援助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20CC(): pass

    label('loc_20CC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x20D0
@scena.Code('func_0B_20D0')
def func_0B_20D0():
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '唔，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，遗憾的是还不到\n',
            '沉浸在胜利中的时候……',
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
        'loc_215E',
    )

    ChrTalk(
        0x0106,
        (
            '#552F啊啊，正是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '您刚刚就任，也真是多灾多难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F0')

    def _loc_215E(): pass

    label('loc_215E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21A4',
    )

    ChrTalk(
        0x0103,
        (
            '#025F嗯嗯，我们明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '您刚刚就任就碰到这些事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F0')

    def _loc_21A4(): pass

    label('loc_21A4')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21F0',
    )

    ChrTalk(
        0x0108,
        (
            '#074F唔，实在让您伤脑筋了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '刚刚就任\n',
            '就碰到这些难题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F0(): pass

    label('loc_21F0')

    ChrTalk(
        0x00FE,
        (
            '说实话，\n',
            '真是无从下手啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当初的混乱虽然收拾了，\n',
            '但是导力器还是没恢复原状。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候只能努力\n',
            '支援市民的生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F但是，就现在而言\n',
            '这是最好的对策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '遗憾的是事态的解决\n',
            '可能还要花费一些时间。',
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
        'loc_2334',
    )

    ChrTalk(
        0x0108,
        (
            '#072F确实不是一朝一夕\n',
            '就能解决的事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为了防止长期延续\n',
            '需要更有效的对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0108, 400)

    Jump('loc_2407')

    def _loc_2334(): pass

    label('loc_2334')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23A1',
    )

    ChrTalk(
        0x0103,
        (
            '#022F是啊，这不是一朝一夕\n',
            '就能解决的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为了防止长期延续\n',
            '需要更有效的对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_2407')

    def _loc_23A1(): pass

    label('loc_23A1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2407',
    )

    ChrTalk(
        0x0106,
        (
            '#050F确实不是一天两天\n',
            '就能解决的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '考虑到事态的延续\n',
            '需要更有效的对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    def _loc_2407(): pass

    label('loc_2407')

    ChrTalk(
        0x00FE,
        (
            '唔，果然是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为新市长的首次工作来说\n',
            '略感负担沉重……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不负女神的期待，\n',
            '只有想办法努力克服了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '祈祷事件能尽快解决，\n',
            '期待诸位的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯……\n',
            '市长也要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F我们会尽力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)
    OP_A2(0x20BC)

    Return()

# id: 0x000C offset: 0x24EC
@scena.Code('func_0C_24EC')
def func_0C_24EC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_296B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 5, 0x20BD)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26EB',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那个……\n',
            '前几天承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊～还以为是谁呢，\n',
            '是宾馆事件的受害者吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……撞到的头已经不要紧了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托你的福已经完全好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，今天\n',
            '来市长官邸有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，其实也没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F请不用在意。\n',
            '只是来看看情况的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算是所谓的市内巡查吧？\n',
            '一直执行任务真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，有什么事的话\n',
            '请尽管开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我至少也算是\n',
            '市长秘书嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哦～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，到时候就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，请不必客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)
    OP_A2(0x20BD)

    Jump('loc_296B')

    def _loc_26EB(): pass

    label('loc_26EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2739',
    )

    ChrTalk(
        0x00FE,
        (
            '别看我这样，\n',
            '至少也是市长秘书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么事情\n',
            '请尽管吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_296B')

    def _loc_2739(): pass

    label('loc_2739')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_284B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27F4',
    )

    ChrTalk(
        0x00FE,
        (
            '关于学院的事件\n',
            '刚刚收到了报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说平安解决了，\n',
            '我和市长总算都放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正忙着做\n',
            '发放宣传的准备呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样得发出消息\n',
            '让大家感到安心才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2848')

    def _loc_27F4(): pass

    label('loc_27F4')

    ChrTalk(
        0x00FE,
        (
            '关于学院的事件\n',
            '刚刚收到了报告呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说平安解决了，\n',
            '我和市长总算都放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2848(): pass

    label('loc_2848')

    Jump('loc_296B')

    def _loc_284B(): pass

    label('loc_284B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2915',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，应付市民的意见\n',
            '总算告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '众多的市民一时间全涌过来，\n',
            '那时候这里也够辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，导力器的问题\n',
            '还没有解决的头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在光是支持市民生活\n',
            '就已经竭尽全力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_296B')

    def _loc_2915(): pass

    label('loc_2915')

    ChrTalk(
        0x00FE,
        (
            '导力器的问题\n',
            '还没有解决的头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在光是支持市民生活\n',
            '就已经竭尽全力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_296B(): pass

    label('loc_296B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x296F
@scena.Code('func_0D_296F')
def func_0D_296F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2FBC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 6, 0x20BE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D55',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A60',
    )

    ChrTurnDirection(0x00FE, 0x0106, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '咦，阿加特先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哦，好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看来还是\n',
            '很有精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，托你的福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老爸当了市长，\n',
            '我就来帮他的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种情况下，\n',
            '很多事都需要忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B57')

    def _loc_2A60(): pass

    label('loc_2A60')

    ChrTalk(
        0x00FE,
        (
            '咦，你们是……',
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
        'loc_2ABC',
    )

    ChrTalk(
        0x0101,
        (
            '#1000F啊，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，很有精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AE6')

    def _loc_2ABC(): pass

    label('loc_2ABC')

    ChrTalk(
        0x0101,
        (
            '#1000F啊，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎样？还好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AE6(): pass

    label('loc_2AE6')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈，托你的福还算好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老爸当了市长，\n',
            '我现在正在帮他的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种情况下，\n',
            '很多事都需要忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B57(): pass

    label('loc_2B57')

    ChrTalk(
        0x0101,
        (
            '#1011F哦～这可是\n',
            '正经的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，现在就和\n',
            '打工差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过着急也不是办法，\n',
            '我打算脚踏实地地努力看看。',
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
        'loc_2C51',
    )

    ChrTalk(
        0x0106,
        (
            '#051F有这觉悟就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……好好干哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '是，是。\n',
            '非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿加特先生也多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D4C')

    def _loc_2C51(): pass

    label('loc_2C51')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CDC',
    )

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，有这觉悟就\n',
            '一定没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，好好干哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯，我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '你们也多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D4C')

    def _loc_2CDC(): pass

    label('loc_2CDC')

    ChrTalk(
        0x0101,
        (
            '#1006F有这觉悟就\n',
            '一定没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，加油工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯，我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '你们也多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D4C(): pass

    label('loc_2D4C')

    OP_A2(0x000B)
    OP_A2(0x20BE)

    Jump('loc_2FBC')

    def _loc_2D55(): pass

    label('loc_2D55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2E0A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DC3',
    )

    ChrTalk(
        0x00FE,
        (
            '总之我打算\n',
            '脚踏实地的努力看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种非常时期，\n',
            '阿加特先生你们也要多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E07')

    def _loc_2DC3(): pass

    label('loc_2DC3')

    ChrTalk(
        0x00FE,
        (
            '总之我打算\n',
            '脚踏实地的努力看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '你们也要多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E07(): pass

    label('loc_2E07')

    Jump('loc_2FBC')

    def _loc_2E0A(): pass

    label('loc_2E0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2EF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E9A',
    )

    ChrTalk(
        0x00FE,
        (
            '学院的事件……\n',
            '从准游击士那里听说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候还发生人质事件，\n',
            '真是受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '犯人真是的，\n',
            '到底在想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_2EF6')

    def _loc_2E9A(): pass

    label('loc_2E9A')

    ChrTalk(
        0x00FE,
        (
            '这种时候还发生人质事件，\n',
            '真是受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都在齐心协力的时候，\n',
            '真是不能原谅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EF6(): pass

    label('loc_2EF6')

    Jump('loc_2FBC')

    def _loc_2EF9(): pass

    label('loc_2EF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F79',
    )

    ChrTalk(
        0x00FE,
        (
            '我老爸也因为各种事忙得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应付市民的意见、\n',
            '食品和医药品的确保……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是，要做的事\n',
            '多得堆成山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_2FBC')

    def _loc_2F79(): pass

    label('loc_2F79')

    ChrTalk(
        0x00FE,
        (
            '我老爸也因为各种事忙得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么这么喜欢\n',
            '当市长呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FBC(): pass

    label('loc_2FBC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2FC0
@scena.Code('func_0E_2FC0')
def func_0E_2FC0():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『苍耀之灯火』\n',
            '　被认为是初期导力艺术的\n',
            '　极致作品。\n',
            '　导力革命之后\n',
            '　由卢安市民\n',
            '　赠送给为城市发展\n',
            '　作出贡献的戴尔蒙家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x306D
@scena.Code('func_0F_306D')
def func_0F_306D():
    NewScene('ED6_DT21/T2210._SN', 123, 1, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x3077
@scena.Code('func_10_3077')
def func_10_3077():
    NewScene('ED6_DT21/T2210._SN', 121, 1, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x3081
@scena.Code('func_11_3081')
def func_11_3081():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有吊桥的控制装置。',
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
