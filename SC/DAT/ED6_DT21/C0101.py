import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '矿工兰古'),
    TXT(0x02, '矿工提恩特'),
    TXT(0x03, '矿工皮尔姆'),
    TXT(0x04, '矿工海涅'),
    TXT(0x05, '矿工彭兹'),
    TXT(0x06, '加通老大'),
    TXT(0x07, '利吉'),
    TXT(0x08, '螃蟹老大'),
    TXT(0x09, '螃蟹'),
    TXT(0x0A, '螃蟹'),
    TXT(0x0B, '螃蟹'),
    TXT(0x0C, '螃蟹'),
    TXT(0x0D, '螃蟹'),
    TXT(0x0E, '螃蟹'),
    TXT(0x0F, '螃蟹'),
    TXT(0x10, '螃蟹'),
    TXT(0x11, '螃蟹'),
    TXT(0x12, '螃蟹'),
    TXT(0x13, '螃蟹'),
    TXT(0x14, '螃蟹'),
    TXT(0x15, '目标用照相机'),
    TXT(0x16, ''),
    TXT(0x17, ''),
    TXT(0x18, ''),
    TXT(0x19, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0101.x'
    header.mapIndex       = 1
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xBE7E
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
        ('ED6_DT29/CH12920._CH', 'ED6_DT29/CH12920P._CP'),
        ('ED6_DT29/CH12921._CH', 'ED6_DT29/CH12921P._CP'),
        ('ED6_DT09/CH10000._CH', 'ED6_DT09/CH10000P._CP'),
        ('ED6_DT09/CH10001._CH', 'ED6_DT09/CH10001P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH00490._CH', 'ED6_DT07/CH00490P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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

# id: 0x10003 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 125180,
            z           = 0,
            y           = 20140,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 112970,
            z           = -210,
            y           = 81150,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 104360,
            z           = 0,
            y           = 53370,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x3D6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 90600,
            y           = -1000,
            z           = 68100,
            range       = 97100,
            dword_10    = 0x000003E8,
            dword_14    = 0x00010EB4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000022,
        ),
        ScenaEventData(
            x           = 125000,
            y           = -1000,
            z           = 24700,
            range       = 134000,
            dword_10    = 0x000003E8,
            dword_14    = 0x000065F4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = 106480,
            y           = -1000,
            z           = 31780,
            range       = 104940,
            dword_10    = 0x000003E8,
            dword_14    = 0x00005E60,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 98500,
            y           = -1000,
            z           = 3100,
            range       = 99500,
            dword_10    = 0x000003E8,
            dword_14    = 0x00003BC4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000020,
        ),
    )

# id: 0x10005 offset: 0x456
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 54000,
            triggerZ            = 500,
            triggerY            = 58200,
            triggerRange        = 600,
            actorX              = 54000,
            actorZ              = 500,
            actorY              = 58200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14000,
            triggerZ            = 1000,
            triggerY            = 31800,
            triggerRange        = 1000,
            actorX              = 14000,
            actorZ              = 1000,
            actorY              = 31800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x49E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_507',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrPos(0x000D, 24270, -200, 15450, 315)
    SetChrPos(0x0009, 12850, 0, 12900, 140)
    SetChrPos(0x000C, 10170, 0, 29510, 315)
    SetChrPos(0x000A, 36510, 0, 25540, 270)
    SetChrPos(0x000B, 36500, -130, 23470, 270)

    Jump('loc_652')

    def _loc_507(): pass

    label('loc_507')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Return,
        ),
        'loc_652',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 0, 0x2088)),
            Expr.Return,
        ),
        'loc_617',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 132100, 0, 74120, 225)
    SetChrPos(0x0009, 132170, 0, 72480, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            Expr.Return,
        ),
        'loc_57C',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000A, 131940, 0, 69900, 315)
    SetChrPos(0x000B, 130930, 0, 68610, 45)
    SetChrFlags(0x001D, 0x0080)

    Jump('loc_5A8')

    def _loc_57C(): pass

    label('loc_57C')

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000A, 130610, 1000, 14190, 180)
    SetChrPos(0x000B, 130610, 1000, 12770, 0)

    def _loc_5A8(): pass

    label('loc_5A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Return,
        ),
        'loc_5C8',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 124780, 0, 74190, 180)

    Jump('loc_5DE')

    def _loc_5C8(): pass

    label('loc_5C8')

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 96530, -70, 29250, 0)

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Return,
        ),
        'loc_5FE',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 126540, 0, 75140, 180)

    Jump('loc_614')

    def _loc_5FE(): pass

    label('loc_5FE')

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 86190, -500, 13450, 0)

    def _loc_614(): pass

    label('loc_614')

    Jump('loc_652')

    def _loc_617(): pass

    label('loc_617')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 7, 0x2087)),
            Expr.Return,
        ),
        'loc_637',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 51720, 0, 55230, 180)

    Jump('loc_652')

    def _loc_637(): pass

    label('loc_637')

    SetChrFlags(0x0008, 0x0010)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 53910, 0, 53890, 0)

    def _loc_652(): pass

    label('loc_652')

    Return()

# id: 0x0001 offset: 0x653
@scena.Code('Init')
def Init():
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Return,
        ),
        'loc_675',
    )

    OP_6F(0x0000, 75)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 7, 0x2087)),
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 0, 0x2088)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_675',
    )

    OP_65(0x00, 0x0001)

    def _loc_675(): pass

    label('loc_675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_814',
    )

    OP_D2(0x0026006E, 0x00260073, 0x07)
    OP_D2(0x0026006E, 0x00260073, 0x08)
    OP_D2(0x0026006E, 0x00260073, 0x09)
    OP_D2(0x00270110, 0x00270120, 0x0A)
    OP_D2(0x00270111, 0x00270121, 0x0B)
    OP_D2(0x00270130, 0x00270140, 0x0C)
    OP_D2(0x00270131, 0x00270141, 0x0D)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_6DC'),
        (0x00000005, 'loc_6F3'),
        (0x00000006, 'loc_70A'),
        (0x00000007, 'loc_721'),
        (-1, 'loc_738'),
    )

    def _loc_6DC(): pass

    label('loc_6DC')

    OP_D2(0x000701D0, 0x000701DC, 0x0E)
    OP_D2(0x000701D1, 0x000701DD, 0x0F)

    Jump('loc_738')

    def _loc_6F3(): pass

    label('loc_6F3')

    OP_D2(0x00070218, 0x00070224, 0x0E)
    OP_D2(0x00070219, 0x00070225, 0x0F)

    Jump('loc_738')

    def _loc_70A(): pass

    label('loc_70A')

    OP_D2(0x00070230, 0x0007023C, 0x0E)
    OP_D2(0x00070231, 0x0007023D, 0x0F)

    Jump('loc_738')

    def _loc_721(): pass

    label('loc_721')

    OP_D2(0x00070248, 0x00070254, 0x0E)
    OP_D2(0x00070249, 0x00070255, 0x0F)

    Jump('loc_738')

    def _loc_738(): pass

    label('loc_738')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_751'),
        (0x00000005, 'loc_768'),
        (0x00000006, 'loc_77F'),
        (0x00000007, 'loc_796'),
        (-1, 'loc_7AD'),
    )

    def _loc_751(): pass

    label('loc_751')

    OP_D2(0x000701D0, 0x000701DC, 0x10)
    OP_D2(0x000701D1, 0x000701DD, 0x11)

    Jump('loc_7AD')

    def _loc_768(): pass

    label('loc_768')

    OP_D2(0x00070218, 0x00070224, 0x10)
    OP_D2(0x00070219, 0x00070225, 0x11)

    Jump('loc_7AD')

    def _loc_77F(): pass

    label('loc_77F')

    OP_D2(0x00070230, 0x0007023C, 0x10)
    OP_D2(0x00070231, 0x0007023D, 0x11)

    Jump('loc_7AD')

    def _loc_796(): pass

    label('loc_796')

    OP_D2(0x00070248, 0x00070254, 0x10)
    OP_D2(0x00070249, 0x00070255, 0x11)

    Jump('loc_7AD')

    def _loc_7AD(): pass

    label('loc_7AD')

    LoadEffect(0x00, 'map\\\\mp002_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 1000)
    OP_D2(0x0029039C, 0x002903A0, 0x12)
    OP_D2(0x0029039D, 0x002903A1, 0x13)
    OP_D2(0x002903A2, 0x002903A3, 0x14)

    def _loc_814(): pass

    label('loc_814')

    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
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
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)
    OP_71(0x0020, 0x0004)
    OP_71(0x0021, 0x0004)
    OP_71(0x0022, 0x0004)
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)
    OP_71(0x0027, 0x0004)
    OP_71(0x0028, 0x0004)
    OP_71(0x0029, 0x0004)
    OP_71(0x002A, 0x0004)
    OP_71(0x002B, 0x0004)
    OP_71(0x002C, 0x0004)
    OP_71(0x002D, 0x0004)
    OP_71(0x002E, 0x0004)
    OP_71(0x002F, 0x0004)
    OP_71(0x0030, 0x0004)
    OP_71(0x0031, 0x0004)
    OP_71(0x0032, 0x0004)
    OP_79(0x04, 0x0002)
    OP_79(0x05, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_79(0x09, 0x0002)
    OP_79(0x0A, 0x0002)
    OP_79(0x0B, 0x0002)
    OP_79(0x0C, 0x0002)
    OP_79(0x0D, 0x0002)
    OP_79(0x0E, 0x0002)
    OP_79(0x0F, 0x0002)
    OP_79(0x10, 0x0002)
    OP_79(0x11, 0x0002)
    OP_79(0x12, 0x0002)
    OP_79(0x13, 0x0002)
    OP_79(0x14, 0x0002)
    OP_79(0x15, 0x0002)
    OP_79(0x16, 0x0002)
    OP_79(0x17, 0x0002)
    OP_79(0x18, 0x0002)
    OP_79(0x19, 0x0002)
    OP_79(0x1A, 0x0002)
    OP_79(0x1B, 0x0002)
    OP_79(0x1C, 0x0002)
    OP_79(0x1D, 0x0002)
    OP_79(0x1E, 0x0002)
    OP_79(0x1F, 0x0002)
    OP_79(0x20, 0x0002)
    OP_79(0x21, 0x0002)
    OP_79(0x22, 0x0002)
    OP_79(0x23, 0x0002)
    OP_79(0x24, 0x0002)
    OP_79(0x25, 0x0002)
    OP_79(0x26, 0x0002)
    OP_79(0x27, 0x0002)
    OP_79(0x28, 0x0002)
    OP_79(0x29, 0x0002)
    OP_79(0x2A, 0x0002)
    OP_79(0x2B, 0x0002)
    OP_79(0x2C, 0x0002)
    OP_79(0x2D, 0x0002)
    OP_79(0x2E, 0x0002)
    OP_79(0x2F, 0x0002)
    OP_79(0x30, 0x0002)
    OP_79(0x31, 0x0002)
    OP_79(0x32, 0x0002)
    OP_7B()
    OP_77(0x96, 0x96, 0x96, 0x00, 0x00000000)
    OP_D7(0x01, 20000, 0)

    Return()

# id: 0x0002 offset: 0x9CE
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
        'loc_9F3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_B35')

    def _loc_9F3(): pass

    label('loc_9F3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A0C',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_B35')

    def _loc_A0C(): pass

    label('loc_A0C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A25',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_B35')

    def _loc_A25(): pass

    label('loc_A25')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A3E',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_B35')

    def _loc_A3E(): pass

    label('loc_A3E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A57',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_B35')

    def _loc_A57(): pass

    label('loc_A57')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A70',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_B35')

    def _loc_A70(): pass

    label('loc_A70')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A89',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_B35')

    def _loc_A89(): pass

    label('loc_A89')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AA2',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_B35')

    def _loc_AA2(): pass

    label('loc_AA2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ABB',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_B35')

    def _loc_ABB(): pass

    label('loc_ABB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD4',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_B35')

    def _loc_AD4(): pass

    label('loc_AD4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AED',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_B35')

    def _loc_AED(): pass

    label('loc_AED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B06',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_B35')

    def _loc_B06(): pass

    label('loc_B06')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_B35')

    def _loc_B1F(): pass

    label('loc_B1F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B35',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_B35(): pass

    label('loc_B35')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B4A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_B35')

    def _loc_B4A(): pass

    label('loc_B4A')

    Return()

# id: 0x0003 offset: 0xB4B
@scena.Code('func_03_B4B')
def func_03_B4B():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 0, 0x2088)),
            Expr.Return,
        ),
        'loc_C6A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BAF',
    )

    ChrTalk(
        0x00FE,
        (
            '大家平安\n',
            '我就放心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士朋友要是\n',
            '也能早点被找到就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C67')

    def _loc_BAF(): pass

    label('loc_BAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C0F',
    )

    ChrTalk(
        0x00FE,
        (
            '还应该有矿工同伴\n',
            '隐藏在坑道里面才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请你们想办法\n',
            '把他们救出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C67')

    def _loc_C0F(): pass

    label('loc_C0F')

    ChrTalk(
        0x00FE,
        (
            '我、我和提恩特\n',
            '会乖乖待在这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那么游击士朋友。\n',
            '老大他们就拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C67(): pass

    label('loc_C67')

    Jump('loc_CCB')

    def _loc_C6A(): pass

    label('loc_C6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 7, 0x2087)),
            Expr.Return,
        ),
        'loc_CC6',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉，请想办法帮我\n',
            '确认一下坑道的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老大他们一定也\n',
            '在等待着救援呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_CC6(): pass

    label('loc_CC6')

    Call(0, 0x0009)

    Return()

    def _loc_CCB(): pass

    label('loc_CCB')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xCCF
@scena.Code('func_04_CCF')
def func_04_CCF():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_DAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D55',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正准备要回去吃饭的时候\n',
            '工作都已经开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵……\n',
            '肚子一饿就使不出力气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_DA7')

    def _loc_D55(): pass

    label('loc_D55')

    ChrTalk(
        0x00FE,
        (
            '我准备回去吃饭的时候\n',
            '工作已经开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵……\n',
            '肚子饿得使不出力气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DA7(): pass

    label('loc_DA7')

    Jump('loc_DE3')

    def _loc_DAA(): pass

    label('loc_DAA')

    ChrTalk(
        0x00FE,
        (
            '快、快点帮助大家\n',
            '从这里逃离吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（发抖）……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_DE3(): pass

    label('loc_DE3')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xDE7
@scena.Code('func_05_DE7')
def func_05_DE7():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_EE0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E8D',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，各位游击士。\n',
            '又给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的事情也\n',
            '一定是女神的旨意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得一定是女神\n',
            '想通过那起事故\n',
            '向我们传递什么讯息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_EDD')

    def _loc_E8D(): pass

    label('loc_E8D')

    ChrTalk(
        0x00FE,
        (
            '那起事故也一定是\n',
            '女神的旨意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也打算要为了\n',
            '理解启示而重新读圣典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EDD(): pass

    label('loc_EDD')

    Jump('loc_F1C')

    def _loc_EE0(): pass

    label('loc_EE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            Expr.Return,
        ),
        'loc_F17',
    )

    ChrTalk(
        0x00FE,
        (
            '女神啊……\n',
            '请拯救我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1C')

    def _loc_F17(): pass

    label('loc_F17')

    Call(0, 0x0012)

    Return()

    def _loc_F1C(): pass

    label('loc_F1C')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0xF20
@scena.Code('func_06_F20')
def func_06_F20():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1033',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FE2',
    )

    ChrTalk(
        0x00FE,
        (
            '皮尔姆那家伙还是\n',
            '把一切都归咎于女神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，你以为是谁\n',
            '救了你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再发生事故，\n',
            '我看那家伙就不必去救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不那么做的话\n',
            '那个笨蛋一辈子也不会清醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_1030')

    def _loc_FE2(): pass

    label('loc_FE2')

    ChrTalk(
        0x00FE,
        (
            '皮尔姆那家伙还是\n',
            '把一切都归咎于女神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，你以为是谁\n',
            '救了你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1030(): pass

    label('loc_1030')

    Jump('loc_1087')

    def _loc_1033(): pass

    label('loc_1033')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            Expr.Return,
        ),
        'loc_1082',
    )

    ChrTalk(
        0x00FE,
        (
            '皮尔姆那家伙又在祈祷了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，事到如今\n',
            '懒得再对他说教了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1087')

    def _loc_1082(): pass

    label('loc_1082')

    Call(0, 0x0012)

    Return()

    def _loc_1087(): pass

    label('loc_1087')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x108B
@scena.Code('func_07_108B')
def func_07_108B():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_11A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1158',
    )

    ChrTalk(
        0x00FE,
        (
            '提恩特那家伙，\n',
            '似乎又在偷懒的样子，\n',
            '所以我已经向老大告状了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，谁叫他发生事故时\n',
            '一个人逃跑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那家伙当时\n',
            '动作可真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作时也能那样\n',
            '干脆利落就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_11A2')

    def _loc_1158(): pass

    label('loc_1158')

    ChrTalk(
        0x00FE,
        (
            '遇到事故时的提恩特\n',
            '动作可真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作时也能那样\n',
            '干脆利落就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A2(): pass

    label('loc_11A2')

    Jump('loc_11C4')

    def _loc_11A5(): pass

    label('loc_11A5')

    ChrTalk(
        0x00FE,
        (
            '呼～呼～\n',
            '真、真是可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_11C4(): pass

    label('loc_11C4')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x11C8
@scena.Code('func_08_11C8')
def func_08_11C8():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_12E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1280',
    )

    ChrTalk(
        0x000D,
        (
            '喔，是各位游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '托你们的福\n',
            '已经可以重新开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然升降机\n',
            '依然还是不能动，\n',
            '不过现在发牢骚也没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '总之先从可以进行的地方\n',
            '开始开采吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_12E1')

    def _loc_1280(): pass

    label('loc_1280')

    ChrTalk(
        0x000D,
        (
            '虽然升降机\n',
            '依然还是不能动，\n',
            '不过现在发牢骚也没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '真想要小姐你们\n',
            '使用过的那个装置啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12E1(): pass

    label('loc_12E1')

    Jump('loc_137A')

    def _loc_12E4(): pass

    label('loc_12E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1343',
    )

    ChrTalk(
        0x000D,
        (
            '游击士小哥\n',
            '可能还在现场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '他在那里直到最后\n',
            '还在为我们争取\n',
            '逃跑的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_137A')

    def _loc_1343(): pass

    label('loc_1343')

    ChrTalk(
        0x000D,
        (
            '游击士小哥\n',
            '可能还在现场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '真希望他能没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137A(): pass

    label('loc_137A')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x137E
@scena.Code('func_09_137E')
def func_09_137E():
    EventBegin(0x00)
    Fade(500)
    OP_6D(54410, 60, 52800, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 54510, 150, 52380, 0)
    SetChrPos(0x0102, 53460, 160, 52670, 0)
    SetChrPos(0x00F8, 54510, 150, 51180, 0)
    SetChrPos(0x00F9, 53460, 160, 51470, 0)
    OP_4A(0x0008, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0920350602V唔唔～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350603V这可麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350604V#1015F请问，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0920350605V哦，原来是\n',
            '游击士姐姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350606V上次多亏你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350607V#1016F啊哈哈，真是怀念啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350608V#1040F是来搬运七耀石时\n',
            '碰上塌方的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350609V#1035F确实很怀念，\n',
            '不过现在不是闲聊过去的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350610V#1004F啊，对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350611V嗯，其实是升降机\n',
            '不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350612V没办法和在坑道的\n',
            '老大他们交接班。',
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
        'loc_1638',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350613V#022F之前坑道里\n',
            '在施工吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B7')

    def _loc_1638(): pass

    label('loc_1638')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1679',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350614V#072F听说之前坑道里\n',
            '在施工吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B7')

    def _loc_1679(): pass

    label('loc_1679')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16B7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350615V#050F好像之前坑道里\n',
            '在施工吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16B7(): pass

    label('loc_16B7')

    ChrTalk(
        0x0008,
        (
            '#0920350616V嗯，是为了填补\n',
            '那次塌方造成的坑洞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350617V虽然骨架已经弄好，\n',
            '但稳固地基的工作还没完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350618V#1002F那次塌方所造成的坑洞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350619V#1042F嗯，是我们上次来的时候发现的\n',
            '那个魔兽巢穴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350620V嗯，就是那个坑洞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350621V虽然老大他们后来马上\n',
            '利用爆破将它填埋起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350622V不管怎么说也是与魔兽的巢穴\n',
            '相连的危险场所啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350623V所以就准备\n',
            '再好好地施工一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350624V#1042F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350625V所以就邀请利吉先生\n',
            '过来警戒了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350626V#1015F不过在那个工程的\n',
            '关键时刻却发生了导力停止现象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350627V#1003F……希望没出什么事就好。',
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
        'loc_1998',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350628V#057F很麻烦呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350629V现在只能到下面\n',
            '确认一下情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A63')

    def _loc_1998(): pass

    label('loc_1998')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19F9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350630V#072F喔，有股危险的感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350631V现在应该尽早\n',
            '下去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A63')

    def _loc_19F9(): pass

    label('loc_19F9')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A63',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350632V#022F我有一种不祥的预感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350633V现在只能到下面\n',
            '去确认一下情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A63(): pass

    label('loc_1A63')

    ChrTalk(
        0x0008,
        (
            '#0920350634V啊，当然希望\n',
            '你们这么做……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350635V但是，你们准备\n',
            '如何到下面去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350636V最重要的是\n',
            '升降机动不了了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010350637V#1019F唔、唔……\n',
            '说来也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350638V#1043F因为那也是用\n',
            '导力器驱动的机械嘛。',
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
        'loc_1BBF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350639V#064F请、请问……\n',
            '有没有其它办法可以下去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3C')

    def _loc_1BBF(): pass

    label('loc_1BBF')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BFF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350640V#023F有没有其它手段可以下去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3C')

    def _loc_1BFF(): pass

    label('loc_1BFF')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C3C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350641V#072F有没有其它可以下去的路？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3C(): pass

    label('loc_1C3C')

    ChrTalk(
        0x0008,
        (
            '#0920350642V你在说什么呢。\n',
            '有的话我早就用了。',
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
        'loc_1CA8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350643V#562F啊……\n',
            '是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D0B')

    def _loc_1CA8(): pass

    label('loc_1CA8')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CDC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350644V#025F嗯，也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D0B')

    def _loc_1CDC(): pass

    label('loc_1CDC')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D0B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350645V#073F啊，也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D0B(): pass

    label('loc_1D0B')

    ChrTalk(
        0x0101,
        (
            '#0010350646V#1002F可就算这样\n',
            '也不能放弃。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350647V因为现在矿工还在\n',
            '地下等着我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350648V#1043F是啊。\n',
            '得想想办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350649V不好意思，请你们想想办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350650V老大他们一定也在\n',
            '等待着我们救援呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0008, 52430, 0, 55250, 2000, 0x00)
    OP_8C(0x0008, 180, 400)
    OP_4B(0x0008, 255)
    OP_65(0x00, 0x0001)
    ClearChrFlags(0x0008, 0x0010)
    OP_A2(0x2087)
    OP_28(0x00BF, 0x04, 0x02)
    OP_28(0x00BF, 0x04, 0x08)
    OP_28(0x00BF, 0x01, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x1E35
@scena.Code('func_0A_1E35')
def func_0A_1E35():
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '按了开关没反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(500)
    OP_6D(54080, 0, 55500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F2F',
    )

    OP_D2(0x00070065, 0x0007006D, 0x07)
    SetChrPos(0x0101, 54510, 0, 54700, 0)
    SetChrPos(0x0107, 53490, 0, 54670, 0)
    SetChrPos(0x0102, 54620, 0, 53520, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F1B',
    )

    SetChrPos(0x00F9, 53390, 0, 53520, 0)

    Jump('loc_1F2C')

    def _loc_1F1B(): pass

    label('loc_1F1B')

    SetChrPos(0x00F8, 53390, 0, 53520, 0)

    def _loc_1F2C(): pass

    label('loc_1F2C')

    Jump('loc_1F73')

    def _loc_1F2F(): pass

    label('loc_1F2F')

    SetChrPos(0x0101, 54510, 0, 54700, 0)
    SetChrPos(0x0102, 53490, 0, 54670, 0)
    SetChrPos(0x00F8, 54620, 0, 53520, 0)
    SetChrPos(0x00F9, 53390, 0, 53520, 0)
    def _loc_1F73(): pass

    label('loc_1F73')

    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010350651V#1026F#2P果然启动不了……',
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
        'loc_201B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350652V#022F升降机开关的\n',
            '控制钥匙也插在上面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350653V不会动是因为受了\n',
            '导力停止现象的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_211A')

    def _loc_201B(): pass

    label('loc_201B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2097',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350654V#050F升降机开关的\n',
            '控制钥匙也插在上面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350655V不运作是因为受了\n',
            '导力停止现象的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_211A')

    def _loc_2097(): pass

    label('loc_2097')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_211A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350656V#072F升降机开关的\n',
            '控制钥匙也插在上面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350657V这么说动不了是因为受了\n',
            '导力停止现象的影响了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_211A(): pass

    label('loc_211A')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36E8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350658V#062F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_215C')
    def lambda_215C():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_215C')

    DispatchAsync2(0x0101, 0x0001, lambda_215C)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010350659V#1002F#2P嗯……？\n',
            '提妲，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070350660V#060F#1P嗯、嗯……\n',
            '我稍微想了一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070350661V#060F#1P那个，这部升降机是\n',
            '驱动部件内置型的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)

    @scena.Lambda('lambda_222E')
    def lambda_222E():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_222E')

    DispatchAsync2(0x0008, 0x0001, lambda_222E)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0920350662V哎…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350663V啊，啊啊……\n',
            '没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070350664V#064F#1P啊，果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22A7')
    def lambda_22A7():
        OP_6D(54090, 50, 56090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22A7)

    @scena.Lambda('lambda_22BF')
    def lambda_22BF():
        OP_6C(31000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_22BF)

    OP_8E(0x0107, 53820, 50, 57680, 2000, 0x00)
    OP_8C(0x0107, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070350665V#062F#5P嗯，控制钥匙的\n',
            '插孔在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    SetChrChipByIndex(0x0107, 7)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070350666V#062F#5P……驱动导力器\n',
            '正好在这附近吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350667V要是按照标准的设计，\n',
            '我想大概是在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2443',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2402',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_2440')

    def _loc_2402(): pass

    label('loc_2402')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2429',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_2440')

    def _loc_2429(): pass

    label('loc_2429')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_2440(): pass

    label('loc_2440')

    Jump('loc_24A8')

    def _loc_2443(): pass

    label('loc_2443')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_246A',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_24A8')

    def _loc_246A(): pass

    label('loc_246A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2491',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_24A8')

    def _loc_2491(): pass

    label('loc_2491')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_24A8(): pass

    label('loc_24A8')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010350668V#1016F#2P唔、唔……',
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
        'loc_2507',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350669V#551F真是的，又来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2507(): pass

    label('loc_2507')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2560',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350670V#071F哈哈，一看到机械\n',
            '眼神就马上变了，\n',
            '不愧是博士的孙女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2560(): pass

    label('loc_2560')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25AA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350671V#021F呵呵，这副认真的样子\n',
            '不是挺可爱的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25AA(): pass

    label('loc_25AA')

    ChrTalk(
        0x0008,
        (
            '#0920350672V#3P好、好像是个异常\n',
            '熟悉机械的小鬼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0107, 65535)
    OP_0D()
    OP_8C(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070350673V#060F#5P嗯……\n',
            '好像有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350674V#1011F#2P有办法……',
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
        'loc_268B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350675V#023F难道说你能让\n',
            '这升降机动起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_270B')

    def _loc_268B(): pass

    label('loc_268B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350676V#052F……难道说你能让它动起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_270B')

    def _loc_26CD(): pass

    label('loc_26CD')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_270B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350677V#073F哟，莫非\n',
            '你能让它动起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_270B(): pass

    label('loc_270B')

    ChrTalk(
        0x0107,
        (
            '#0070350678V#060F#5P……嗯，大概能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350679V如果使用那个零力场发生器的话，\n',
            '一定能动起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350680V#1004F#2P咦，用发生器？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070350681V#560F#5P嗯，让发生器\n',
            '尽可能地靠近驱动部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350682V顺利的话应该能暂时使\n',
            '停止现象的效果无效。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350683V#1044F原来如此……\n',
            '还有这一招啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350684V#1040F赶快试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.Eval, "OP_40(0x0151, 0x00)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2882',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_2882(): pass

    label('loc_2882')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_289A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_289A(): pass

    label('loc_289A')

    If(
        (
            (Expr.Eval, "OP_D5(0x00, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28B2',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_28B2(): pass

    label('loc_28B2')

    If(
        (
            (Expr.Eval, "OP_D5(0x00, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28CA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_28CA(): pass

    label('loc_28CA')

    If(
        (
            (Expr.Eval, "OP_D5(0x01, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28E2',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_28E2(): pass

    label('loc_28E2')

    If(
        (
            (Expr.Eval, "OP_D5(0x01, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28FA',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_28FA(): pass

    label('loc_28FA')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2938',
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2920',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_2920(): pass

    label('loc_2920')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2938',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_2938(): pass

    label('loc_2938')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2976',
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_295E',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_295E(): pass

    label('loc_295E')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2976',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_2976(): pass

    label('loc_2976')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29B4',
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_299C',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_299C(): pass

    label('loc_299C')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29B4',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_29B4(): pass

    label('loc_29B4')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_29FB',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350685V#560F#5P嗯、嗯！\n',
            '试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBF')

    def _loc_29FB(): pass

    label('loc_29FB')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x00, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "OP_D5(0x00, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2B00',
    )

    ChrTalk(
        0x0101,
        (
            '#0010350686V#1006F#2P这样的话\n',
            '首先需要有发生器呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350687V嗯，先借一个给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070350688V#560F#5P嗯……\n',
            '谢谢姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350689V那么试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBF')

    def _loc_2B00(): pass

    label('loc_2B00')

    If(
        (
            (Expr.Eval, "OP_D5(0x01, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x01, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2C24',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350690V#560F#5P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350691V#1015F这样的话\n',
            '首先需要有发生器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350692V#1040F那就把我的借你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070350693V#560F#5P嗯……\n',
            '谢谢哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350689V那么试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBF')

    def _loc_2C24(): pass

    label('loc_2C24')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D57',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350690V#560F#5P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350691V#1015F#2P这样的话\n',
            '首先需要有发生器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030350697V#020F那就把我的借你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070350698V#560F#5P嗯……\n',
            '谢谢雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350699V那么试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBF')

    def _loc_2D57(): pass

    label('loc_2D57')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E93',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350690V#560F#5P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350691V#1015F#2P这样的话\n',
            '首先需要有发生器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050350702V#051F那就先把\n',
            '我的借给你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070350703V#560F#5P嗯……\n',
            '谢谢阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350699V那么试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBF')

    def _loc_2E93(): pass

    label('loc_2E93')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FBF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350690V#560F#5P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350691V#1015F#2P这样的话\n',
            '首先需要有发生器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080350707V#070F把我的借你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070350708V#560F#5P嗯……\n',
            '谢谢金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350689V那么试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FBF(): pass

    label('loc_2FBF')

    WaitForThreadExit(0x0101, 0x0002)
    OP_8C(0x0107, 0, 400)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲将零力场发生器\n',
            '按在了升降机的操作盘上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    LoadEffect(0x01, 'map\\\\mp007_00.eff')
    PlayEffect(0x01, 0x00, 0x00FF, 54000, 800, 58200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0090, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0920350710V哇、哇！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350711V#1020F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350712V这、这道亮光……',
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
        'loc_312A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350713V#023F和福音一样的光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A3')

    def _loc_312A(): pass

    label('loc_312A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_316A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350714V#052F和那个福音一样的光呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A3')

    def _loc_316A(): pass

    label('loc_316A')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31A3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350715V#072F和福音一样的光啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31A3(): pass

    label('loc_31A3')

    ChrTalk(
        0x0102,
        (
            '#0020350716V#1042F……似乎正在发生干涉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070350658V#062F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_82(0x00, 0x02)
    OP_23(0x0090)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0920350718V消、消失了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070350719V#561F呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350720V这样一来\n',
            '大概就行了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000005)
    OP_73(0x0001)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32DC',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_331A')

    def _loc_32DC(): pass

    label('loc_32DC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3303',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_331A')

    def _loc_3303(): pass

    label('loc_3303')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_331A(): pass

    label('loc_331A')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3346',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3384')

    def _loc_3346(): pass

    label('loc_3346')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_336D',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3384')

    def _loc_336D(): pass

    label('loc_336D')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_3384(): pass

    label('loc_3384')

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    ChrTalk(
        0x0107,
        (
            '#0070350721V#065F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350722V#1004F#2P动、动了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350723V#1042F内部导力器的\n',
            '导力好象恢复了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350724V赶快上升降机吧。\n',
            '要下去就趁现在。',
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
        'loc_347D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350725V#525F呵呵，干得不错嘛㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34E6')

    def _loc_347D(): pass

    label('loc_347D')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34BD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350726V#051F嘿嘿，是小不点的功劳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34E6')

    def _loc_34BD(): pass

    label('loc_34BD')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34E6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350727V#072F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34E6(): pass

    label('loc_34E6')

    @scena.Lambda('lambda_34EC')
    def lambda_34EC():
        OP_6D(54080, 50, 56970, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34EC)

    @scena.Lambda('lambda_3504')
    def lambda_3504():
        OP_8E(0x00FE, 54510, 0, 57700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3504)

    Sleep(100)

    @scena.Lambda('lambda_3524')
    def lambda_3524():
        OP_8E(0x00FE, 54620, 0, 56520, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3524)

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3562',
    )

    OP_8E(0x00F9, 53390, 0, 56520, 5000, 0x00)

    Jump('loc_3576')

    def _loc_3562(): pass

    label('loc_3562')

    OP_8E(0x00F8, 53390, 0, 56520, 5000, 0x00)

    def _loc_3576(): pass

    label('loc_3576')

    ChrTalk(
        0x0008,
        (
            '#0920350728V#2A我、我也跟着去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_35A1')
    def lambda_35A1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_35A1')

    DispatchAsync2(0x0102, 0x0001, lambda_35A1)

    Sleep(100)

    @scena.Lambda('lambda_35B7')
    def lambda_35B7():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_35B7')

    DispatchAsync2(0x0101, 0x0001, lambda_35B7)

    Sleep(100)

    @scena.Lambda('lambda_35CD')
    def lambda_35CD():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_35CD')

    DispatchAsync2(0x00F8, 0x0001, lambda_35CD)

    @scena.Lambda('lambda_35DE')
    def lambda_35DE():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_35DE')

    DispatchAsync2(0x00F9, 0x0001, lambda_35DE)

    ChrTalk(
        0x0102,
        (
            '#0020350729V#1046F#2A快点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_3615')
    def lambda_3615():
        OP_8E(0x00FE, 53850, 50, 55360, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3615)

    @scena.Lambda('lambda_3630')
    def lambda_3630():
        OP_8F(0x00FE, 54620, 0, 56820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3630)

    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3675',
    )

    @scena.Lambda('lambda_365D')
    def lambda_365D():
        OP_8F(0x00FE, 53390, 0, 56820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_365D)

    Jump('loc_3690')

    def _loc_3675(): pass

    label('loc_3675')

    @scena.Lambda('lambda_367B')
    def lambda_367B():
        OP_8F(0x00FE, 53390, 0, 56820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_367B)

    def _loc_3690(): pass

    label('loc_3690')

    WaitForThreadExit(0x0008, 0x0001)
    OP_8E(0x0008, 53850, 0, 56360, 5000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_8C(0x0107, 0, 800)

    ChrTalk(
        0x0107,
        (
            '#0070350730V#062F那、那就去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4600')

    def _loc_36E8(): pass

    label('loc_36E8')

    ChrTalk(
        0x0102,
        (
            '#0020350731V#1043F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_371D')
    def lambda_371D():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_371D')

    DispatchAsync2(0x0101, 0x0001, lambda_371D)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010350732V#1002F#2P约修亚，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350733V#1040F#1P嗯，我注意到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350734V一点事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350735V#1011F#2P注意到什么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350736V#1040F#1P这升降机是\n',
            '驱动部件内置型的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)

    @scena.Lambda('lambda_3818')
    def lambda_3818():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_3818')

    DispatchAsync2(0x0008, 0x0001, lambda_3818)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0920350737V哎…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350738V啊，啊啊……\n',
            '没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350739V#1035F#1P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3892')
    def lambda_3892():
        OP_6D(54090, 50, 56090, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3892)

    @scena.Lambda('lambda_38AA')
    def lambda_38AA():
        OP_6C(31000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38AA)

    OP_8E(0x0102, 53820, 50, 57680, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020350740V#1043F#5P控制钥匙的插孔在这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350741V……就是说，用来驱动的\n',
            '导力器就在它下面吗？',
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
        'loc_3975',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350742V#052F想到什么好办法了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39F7')

    def _loc_3975(): pass

    label('loc_3975')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39BE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350743V#027F呵呵，莫非你想到什么\n',
            '好办法了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39F7')

    def _loc_39BE(): pass

    label('loc_39BE')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39F7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350744V#073F想到什么好办法了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39F7(): pass

    label('loc_39F7')

    OP_8C(0x0102, 180, 400)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.Eval, "OP_40(0x0151, 0x00)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x00, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A20',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3A20(): pass

    label('loc_3A20')

    If(
        (
            (Expr.Eval, "OP_D5(0x00, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A38',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3A38(): pass

    label('loc_3A38')

    If(
        (
            (Expr.Eval, "OP_D5(0x01, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A50',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3A50(): pass

    label('loc_3A50')

    If(
        (
            (Expr.Eval, "OP_D5(0x01, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A68',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3A68(): pass

    label('loc_3A68')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AA6',
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A8E',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3A8E(): pass

    label('loc_3A8E')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AA6',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3AA6(): pass

    label('loc_3AA6')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AE4',
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3ACC',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3ACC(): pass

    label('loc_3ACC')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AE4',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3AE4(): pass

    label('loc_3AE4')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B22',
    )

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B0A',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3B0A(): pass

    label('loc_3B0A')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B22',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_3B22(): pass

    label('loc_3B22')

    If(
        (
            (Expr.Eval, "OP_D5(0x01, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x01, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3BB5',
    )

    ChrTalk(
        0x0102,
        (
            '#0020350745V#1043F#1P还不能确定……\n',
            '不过我觉得有必要试一试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350746V如果使用零力场发生器的话\n',
            '可能会有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFD')

    def _loc_3BB5(): pass

    label('loc_3BB5')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x00, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "OP_D5(0x00, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3CE9',
    )

    ChrTalk(
        0x0102,
        (
            '#0020350745V#1043F#1P还不能确定……\n',
            '不过我觉得有必要试一试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350748V#1040F艾丝蒂尔。\n',
            '能不能把你的零力场发生器借给我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350749V#1011F#2P发生器？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350750V#1015F嗯、嗯，这倒没问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_3EFD')

    def _loc_3CE9(): pass

    label('loc_3CE9')

    ChrTalk(
        0x0102,
        (
            '#0020350751V#1040F#1P不过我觉得有必要试一试',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350752V#1040F#1P不好意思，\n',
            '能不能把你的零力场发生器借给我？',
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
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DB8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350753V#020F#6P零力场发生器\n',
            '我倒是有一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E97')

    def _loc_3DB8(): pass

    label('loc_3DB8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E29',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350754V#051F#6P老爷爷给的那东西吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350755V我倒是有一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E97')

    def _loc_3E29(): pass

    label('loc_3E29')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E97',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350756V#070F#6P博士给的那个装置啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350757V我正好有一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E97(): pass

    label('loc_3E97')

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['零力场发生器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020350758V#1040F请借我用一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EFD(): pass

    label('loc_3EFD')

    ChrTalk(
        0x0101,
        (
            '#0010350759V#1002F#2P那你准备用这个\n',
            '发生器做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350760V#1040F#1P你很快就会知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 0, 400)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚把零力场发生器\n',
            '按在升降机的操作盘上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    LoadEffect(0x01, 'map\\\\mp007_00.eff')
    PlayEffect(0x01, 0x00, 0x00FF, 54000, 800, 58200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0090, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0920350710V哇、哇！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350711V#1020F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350712V这、这道亮光……',
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
        'loc_40C8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350713V#023F和福音一样的光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4141')

    def _loc_40C8(): pass

    label('loc_40C8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4108',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350714V#052F和那个福音一样的光呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4141')

    def _loc_4108(): pass

    label('loc_4108')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4141',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350715V#072F和福音一样的光啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4141(): pass

    label('loc_4141')

    ChrTalk(
        0x0102,
        (
            '#0020350767V#1042F没关系……\n',
            '只是导力波在进行干涉而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350768V如果我的想法正确，\n',
            '这样一来导力就能暂时恢复了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_82(0x00, 0x02)
    OP_23(0x0090)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0920350718V消、消失了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350770V#1042F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000005)
    OP_73(0x0001)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4287',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_42C5')

    def _loc_4287(): pass

    label('loc_4287')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42AE',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_42C5')

    def _loc_42AE(): pass

    label('loc_42AE')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_42C5(): pass

    label('loc_42C5')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42F1',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_432F')

    def _loc_42F1(): pass

    label('loc_42F1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4318',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_432F')

    def _loc_4318(): pass

    label('loc_4318')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_432F(): pass

    label('loc_432F')

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010350722V#1004F#2P动、动了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350772V#1042F好……导力恢复了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 180, 800)

    ChrTalk(
        0x0102,
        (
            '#0020350773V#1046F赶快上升降机吧！\n',
            '要下去就趁现在。',
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
        'loc_4411',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350725V#525F呵呵，干得不错嘛㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4466')

    def _loc_4411(): pass

    label('loc_4411')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_443D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350775V#051F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4466')

    def _loc_443D(): pass

    label('loc_443D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4466',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350727V#072F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4466(): pass

    label('loc_4466')

    @scena.Lambda('lambda_446C')
    def lambda_446C():
        OP_6D(54080, 50, 56970, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_446C)

    @scena.Lambda('lambda_4484')
    def lambda_4484():
        OP_8E(0x00FE, 54510, 0, 57700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4484)

    Sleep(100)

    @scena.Lambda('lambda_44A4')
    def lambda_44A4():
        OP_8E(0x00FE, 54620, 0, 56520, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_44A4)

    Sleep(100)

    OP_8E(0x00F9, 53390, 0, 56520, 5000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0920350728V#2A我、我也跟着去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_44FD')
    def lambda_44FD():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_44FD')

    DispatchAsync2(0x0101, 0x0001, lambda_44FD)

    Sleep(100)

    @scena.Lambda('lambda_4513')
    def lambda_4513():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4513')

    DispatchAsync2(0x00F8, 0x0001, lambda_4513)

    @scena.Lambda('lambda_4524')
    def lambda_4524():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4524')

    DispatchAsync2(0x00F9, 0x0001, lambda_4524)

    ChrTalk(
        0x0101,
        (
            '#0010350778V#1005F#2P#2A大叔冲刺！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_4562')
    def lambda_4562():
        OP_8E(0x00FE, 53850, 50, 55360, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4562)

    @scena.Lambda('lambda_457D')
    def lambda_457D():
        OP_8F(0x00FE, 54620, 0, 56820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_457D)

    Sleep(200)

    @scena.Lambda('lambda_459D')
    def lambda_459D():
        OP_8F(0x00FE, 53390, 0, 56820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0002, lambda_459D)

    WaitForThreadExit(0x0008, 0x0001)
    OP_8E(0x0008, 53850, 0, 56360, 5000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_8C(0x0102, 0, 800)

    ChrTalk(
        0x0102,
        (
            '#0020350779V#1046F开始下降！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4600(): pass

    label('loc_4600')

    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x4605
@scena.Code('func_0B_4605')
def func_0B_4605():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 5)
    OP_70(0x0001, 0x0000000F)
    OP_73(0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010350780V#1004F#2A#5P哇哇！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 15)
    OP_70(0x0001, 0x00000019)
    OP_73(0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010350781V#1004F#2A#5P哇、哇、哇、哇……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 25)
    OP_70(0x0001, 0x00000023)
    OP_73(0x0001)
    Sleep(200)

    OP_0D()
    OP_6D(129000, 0, 76700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6F(0x0002, 360)
    OP_6F(0x0002, 280)
    Yield()
    SetChrBattleFlags(0x0008, 0x0020)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47B3',
    )

    OP_89(0x0101, 129600, 15000, 77700, 180)
    OP_89(0x0107, 128919, 15000, 77680, 0)
    OP_89(0x0102, 129720, 15000, 76820, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_479F',
    )

    OP_89(0x00F9, 128320, 15000, 76820, 180)

    Jump('loc_47B0')

    def _loc_479F(): pass

    label('loc_479F')

    OP_89(0x00F8, 128320, 15000, 76820, 180)

    def _loc_47B0(): pass

    label('loc_47B0')

    Jump('loc_47F7')

    def _loc_47B3(): pass

    label('loc_47B3')

    OP_89(0x0101, 129600, 15000, 77700, 180)
    OP_89(0x0102, 128919, 15000, 77680, 0)
    OP_89(0x00F8, 129720, 15000, 76820, 180)
    OP_89(0x00F9, 128320, 15000, 76820, 180)
    def _loc_47F7(): pass

    label('loc_47F7')

    OP_89(0x0008, 128949, 15000, 76360, 180)
    LoadEffect(0x01, 'Craft\\\\cr162_02.eff')
    LoadEffect(0x02, 'Craft\\\\cr162_00.eff')
    LoadEffect(0x03, 'Craft\\\\cr161_00.eff')
    LoadEffect(0x04, 'scraft\\\\sc000_11.eff')
    OP_D2(0x00090003, 0x00090007, 0x07)
    OP_D2(0x00270130, 0x00270140, 0x08)
    OP_D2(0x00270139, 0x00270149, 0x09)
    FadeIn(1000, 0)
    Sleep(400)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0002, 280)
    OP_70(0x0002, 0x0000010E)
    OP_73(0x0002)
    Sleep(400)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0002, 270)
    OP_70(0x0002, 0x00000104)
    OP_73(0x0002)
    Sleep(400)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0002, 260)
    OP_70(0x0002, 0x000000FA)
    OP_73(0x0002)
    Sleep(400)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0002, 250)
    OP_70(0x0002, 0x000000F0)
    OP_73(0x0002)
    OP_23(0x0068)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020350782V#1035F呼……',
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
        'loc_4995',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350783V#025F啊，差点咬到舌头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4995(): pass

    label('loc_4995')

    ChrTalk(
        0x0101,
        (
            '#0010350784V#1019F为、为什么晃得\n',
            '这么厉害啊……',
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
        'loc_4A15',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350785V#067F嘿嘿，因为导力器的\n',
            '输出完全不够……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B07')

    def _loc_4A15(): pass

    label('loc_4A15')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A85',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350786V#070F大概是因为导力器的\n',
            '导力不充足吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350787V总之先下去\n',
            '确认一下状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B07')

    def _loc_4A85(): pass

    label('loc_4A85')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B07',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350788V#552F导力器的马力\n',
            '好象不够……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350789V#053F反正现在情况这么紧急，\n',
            '就别抱怨升降机舒不舒服了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B07(): pass

    label('loc_4B07')

    @scena.Lambda('lambda_4B0D')
    def lambda_4B0D():
        OP_6D(129479, 150, 73430, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4B0D)

    @scena.Lambda('lambda_4B25')
    def lambda_4B25():
        OP_8E(0x00FE, 129000, 60, 72120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4B25)

    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BEF',
    )

    @scena.Lambda('lambda_4B53')
    def lambda_4B53():
        OP_8E(0x00FE, 129550, 0, 74500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4B53)

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B98',
    )

    @scena.Lambda('lambda_4B80')
    def lambda_4B80():
        OP_8E(0x00FE, 128530, 0, 74500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4B80)

    Jump('loc_4BB3')

    def _loc_4B98(): pass

    label('loc_4B98')

    @scena.Lambda('lambda_4B9E')
    def lambda_4B9E():
        OP_8E(0x00FE, 128530, 0, 74500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4B9E)

    def _loc_4BB3(): pass

    label('loc_4BB3')

    Sleep(100)

    @scena.Lambda('lambda_4BBE')
    def lambda_4BBE():
        OP_8E(0x00FE, 129550, 0, 75500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4BBE)

    Sleep(50)

    OP_8E(0x0107, 128530, 0, 75500, 2000, 0x00)

    Jump('loc_4C63')

    def _loc_4BEF(): pass

    label('loc_4BEF')

    @scena.Lambda('lambda_4BF5')
    def lambda_4BF5():
        OP_8E(0x00FE, 129550, 0, 74500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4BF5)

    Sleep(100)

    @scena.Lambda('lambda_4C15')
    def lambda_4C15():
        OP_8E(0x00FE, 128530, 0, 74500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4C15)

    Sleep(100)

    @scena.Lambda('lambda_4C35')
    def lambda_4C35():
        OP_8E(0x00FE, 129550, 0, 75500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C35)

    Sleep(50)

    OP_8E(0x0102, 128530, 0, 75500, 2000, 0x00)
    def _loc_4C63(): pass

    label('loc_4C63')

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_8C(0x0008, 45, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0920350790V噢，还有\n',
            '灯光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 270, 400)

    @scena.Lambda('lambda_4CC5')
    def lambda_4CC5():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4CC5')

    DispatchAsync2(0x0101, 0x0001, lambda_4CC5)

    @scena.Lambda('lambda_4CD6')
    def lambda_4CD6():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4CD6')

    DispatchAsync2(0x0102, 0x0001, lambda_4CD6)

    @scena.Lambda('lambda_4CE7')
    def lambda_4CE7():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4CE7')

    DispatchAsync2(0x00F8, 0x0001, lambda_4CE7)

    @scena.Lambda('lambda_4CF8')
    def lambda_4CF8():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4CF8')

    DispatchAsync2(0x00F9, 0x0001, lambda_4CF8)

    @scena.Lambda('lambda_4D09')
    def lambda_4D09():
        OP_6D(127060, 0, 73010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4D09)

    OP_8E(0x0008, 125240, 0, 72000, 2000, 0x00)
    OP_8C(0x0008, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0920350791V……坑道那边好安静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350792V说不定是我们\n',
            '多虑了……',
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
            '#0920350793V……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350794V#1044F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350795V啊，好像有人过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350796V哟，我还以为是谁呢。\n',
            '那不是提恩特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350797V喂～提恩特！\n',
            '你在那儿干吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0040)
    SetChrPos(0x0009, 120370, 0, 67550, 90)

    @scena.Lambda('lambda_4E8D')
    def lambda_4E8D():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4E8D')

    DispatchAsync2(0x0008, 0x0001, lambda_4E8D)

    @scena.Lambda('lambda_4E9E')
    def lambda_4E9E():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4E9E')

    DispatchAsync2(0x0101, 0x0001, lambda_4E9E)

    @scena.Lambda('lambda_4EAF')
    def lambda_4EAF():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4EAF')

    DispatchAsync2(0x0102, 0x0001, lambda_4EAF)

    @scena.Lambda('lambda_4EC0')
    def lambda_4EC0():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4EC0')

    DispatchAsync2(0x00F8, 0x0001, lambda_4EC0)

    @scena.Lambda('lambda_4ED1')
    def lambda_4ED1():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_4ED1')

    DispatchAsync2(0x00F9, 0x0001, lambda_4ED1)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x0009, 125780, 0, 71170, 6000, 0x00)

    @scena.Lambda('lambda_4F08')
    def lambda_4F08():
        OP_6D(129380, 60, 72150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F08)

    OP_8E(0x0009, 132010, 0, 71320, 6000, 0x00)
    OP_8C(0x0009, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0920350798V喂、喂……\n',
            '你着急什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350799V后、后面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350800V……啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350801V我、我都说了在后面！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0010, 121610, 0, 69620, 45)
    SetChrPos(0x0011, 118640, 0, 68820, 45)
    SetChrPos(0x0012, 118570, 0, 67630, 45)
    SetChrPos(0x0013, 119440, 0, 66840, 45)
    SetChrPos(0x0014, 120720, 0, 67050, 45)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    OP_59()
    Fade(1000)
    OP_6D(121150, 0, 69600, 0)
    OP_6C(270000, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0008, 0x01)
    SetChrPos(0x0008, 123930, 0, 71340, 0)
    ChrTurnDirection(0x0008, 0x0009, 0)
    OP_0D()

    @scena.Lambda('lambda_50C8')
    def lambda_50C8():
        OP_94(0x01, 0x00FE, 0x000A, 0x0000047E, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_50C8)

    Sleep(100)

    @scena.Lambda('lambda_50E3')
    def lambda_50E3():
        OP_94(0x01, 0x00FE, 0x000A, 0x0000047E, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_50E3)

    @scena.Lambda('lambda_50F9')
    def lambda_50F9():
        OP_94(0x01, 0x00FE, 0x000A, 0x0000047E, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_50F9)

    Sleep(100)

    @scena.Lambda('lambda_5114')
    def lambda_5114():
        OP_94(0x01, 0x00FE, 0x000A, 0x0000047E, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_5114)

    @scena.Lambda('lambda_512A')
    def lambda_512A():
        OP_94(0x01, 0x00FE, 0x000A, 0x0000047E, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_512A)

    @scena.Lambda('lambda_5140')
    def lambda_5140():
        OP_94(0x01, 0x00FE, 0x000A, 0x0000047E, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_5140)

    OP_8C(0x0008, 235, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_95(0x0008, 0x00000000, 0x00000000, 0x00000000, 0x00000320, 0x00002EE0)
    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_51A2')
    def lambda_51A2():
        OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_51A2)

    ChrTalk(
        0x0008,
        (
            '#0920350802V哇、哇哇！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrChipByIndex(0x0102, 9)
    SetChrSubChip(0x0102, 3)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(500)

    SetChrPos(0x0102, 123030, 3000, 70820, 235)
    PlayEffect(0x01, 0x00, 0x0102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_9F(0x0102, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000064)
    OP_22(0x00D5, 0x00, 0x64)
    OP_83(0x00, 0x02)
    CreateThread(0x0102, 0x01, 0x00, 0x000C)
    Sleep(300)

    PlayEffect(0x03, 0xFF, 0x0010, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x04, 0xFF, 0x0010, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_4A(0x0010, 0)
    SetChrChipByIndex(0x0010, 7)
    SetChrFlags(0x0010, 0x0020)
    SetChrFlags(0x0010, 0x0040)

    @scena.Lambda('lambda_52D6')
    def lambda_52D6():
        OP_9E(0x00FE, 0x0000000A, 0x00000000, 0x000003E8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_52D6)

    OP_8F(0x0010, 121260, 0, 69190, 7000, 0x00)
    SetChrChipByIndex(0x0010, 2)
    ClearChrFlags(0x0010, 0x0020)
    OP_4B(0x0010, 0)
    OP_96(0x0102, 0x0001E168, 0x00000000, 0x0001149A, 0x000001F4, 0x00001388)
    SetChrFlags(0x0008, 0x0040)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x0008, 127580, 0, 75220, 4000, 0x00)

    @scena.Lambda('lambda_5354')
    def lambda_5354():
        OP_8E(0x00FE, 129789, 0, 75200, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5354)

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)

    @scena.Lambda('lambda_537E')
    def lambda_537E():
        OP_6D(122730, 0, 70630, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_537E)

    CreateThread(0x0101, 0x01, 0x00, 0x000D)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, 0x000E)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, 0x000F)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    ClearChrFlags(0x0008, 0x0040)
    ClearChrFlags(0x0009, 0x0040)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53FA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350803V#057F切，还真的有魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53FA(): pass

    label('loc_53FA')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5432',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350804V#065F啊……\n',
            '这、这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5432(): pass

    label('loc_5432')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5471',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350805V#070F哈哈，好热烈的欢迎仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5471(): pass

    label('loc_5471')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54C1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350806V#025F唔，是甲壳魔兽啊……\n',
            '这些家伙又硬又难对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54C1(): pass

    label('loc_54C1')

    ChrTalk(
        0x0101,
        (
            '#0010350807V#1002F#2P不会吧，莫非那魔兽的巢穴……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350808V#1042F#1P大概吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350809V不过看来是\n',
            '没有时间考虑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0010, 3)

    @scena.Lambda('lambda_5553')
    def lambda_5553():
        OP_94(0x01, 0x00FE, 0x0000, 0x000006A4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5553)

    Sleep(30)

    SetChrChipByIndex(0x0011, 3)
    SetChrChipByIndex(0x0014, 3)

    @scena.Lambda('lambda_5578')
    def lambda_5578():
        OP_94(0x01, 0x00FE, 0x0000, 0x000006A4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5578)

    @scena.Lambda('lambda_558E')
    def lambda_558E():
        OP_94(0x01, 0x00FE, 0x0000, 0x000006A4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_558E)

    Sleep(30)

    SetChrChipByIndex(0x0012, 3)
    SetChrChipByIndex(0x0013, 3)

    @scena.Lambda('lambda_55B3')
    def lambda_55B3():
        OP_94(0x01, 0x00FE, 0x0000, 0x000006A4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_55B3)

    @scena.Lambda('lambda_55C9')
    def lambda_55C9():
        OP_94(0x01, 0x00FE, 0x0000, 0x000006A4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_55C9)

    WaitForThreadExit(0x0010, 0x0001)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    Battle(0x00000057, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_561B'),
        (-1, 'loc_5620'),
    )

    def _loc_561B(): pass

    label('loc_561B')

    OP_B4(0x00)

    Jump('loc_5620')

    def _loc_5620(): pass

    label('loc_5620')

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    Call(0, 0x0010)

    Return()

# id: 0x000C offset: 0x563E
@scena.Code('func_0C_563E')
def func_0C_563E():
    OP_99(0x00FE, 0x03, 0x0B, 0x000007D0)
    SetChrChipByIndex(0x00FE, 12)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x000D offset: 0x5652
@scena.Code('func_0D_5652')
def func_0D_5652():
    SetChrPos(0x00FE, 126140, 0, 74760, 225)
    OP_8E(0x00FE, 123110, 0, 71990, 5000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x000E offset: 0x567F
@scena.Code('func_0E_567F')
def func_0E_567F():
    SetChrPos(0x00FE, 128370, 0, 74230, 225)
    OP_8E(0x00FE, 124530, 0, 70380, 5000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x000F offset: 0x56AC
@scena.Code('func_0F_56AC')
def func_0F_56AC():
    SetChrPos(0x00FE, 128690, 0, 75630, 225)
    OP_8E(0x00FE, 124680, 0, 71610, 5000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x0010 offset: 0x56D9
@scena.Code('func_10_56D9')
def func_10_56D9():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    OP_6D(123290, 0, 71580, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 123110, 0, 71990, 225)
    SetChrPos(0x0102, 123240, 0, 70810, 225)
    SetChrPos(0x00F8, 124530, 0, 70380, 225)
    SetChrPos(0x00F9, 124680, 0, 71610, 225)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    SetChrPos(0x0008, 132100, 0, 74120, 225)
    SetChrPos(0x0009, 132170, 0, 72480, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010350810V#1002F总算是击退了……',
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
        'loc_5828',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350811V#025F呼，想不到这么难对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58A7')

    def _loc_5828(): pass

    label('loc_5828')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5864',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350812V#050F比我想象中的要厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58A7')

    def _loc_5864(): pass

    label('loc_5864')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58A7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350813V#075F呼，对这种魔兽可不能掉以轻心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58A7(): pass

    label('loc_58A7')

    ChrTalk(
        0x0102,
        (
            '#0020350814V#1035F嗯，是不能大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350815V#5P喂、喂……游击士朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350816V#5P我、我能出来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
    OP_22(0x00D5, 0x00, 0x64)
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350817V#1011F啊，嗯，没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x0009, 131020, 0, 71030, 270)
    SetChrPos(0x0008, 130449, 220, 72720, 270)

    @scena.Lambda('lambda_5985')
    def lambda_5985():
        OP_6D(124320, 0, 71010, 1500)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5985)

    @scena.Lambda('lambda_599D')
    def lambda_599D():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_599D)

    @scena.Lambda('lambda_59AD')
    def lambda_59AD():
        OP_8E(0x00FE, 126090, 0, 71090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_59AD)

    @scena.Lambda('lambda_59C8')
    def lambda_59C8():
        OP_8E(0x00FE, 126130, 0, 72200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_59C8)

    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)

    @scena.Lambda('lambda_59ED')
    def lambda_59ED():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_59ED)

    @scena.Lambda('lambda_59FB')
    def lambda_59FB():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_59FB)

    Sleep(100)

    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_5A13')
    def lambda_5A13():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5A13)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0960350818V呼～谢谢，总算得救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350819V多亏了你们，\n',
            '我又能活着回家吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0920350820V#2P喂，笨蛋。\n',
            '还在说这种悠闲的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350821V#2P老大他们怎么样了？\n',
            '先告诉我们这件事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350822V#1002F嗯，总之现在\n',
            '首先要掌握情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350823V#1042F#1P是发生事故了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350824V嗯、嗯……是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350825V在昨天的施工中，驱赶魔兽的\n',
            '导力灯不亮了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350826V无可奈何之下，只能暂停施工\n',
            '在这里待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350827V然后今天早上现场就\n',
            '出现了大群魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350828V啊……我、我差点\n',
            '就被吃掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350829V#1002F你等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350830V应该有一个从协会\n',
            '过来的游击士在这里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350831V啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350832V那位小哥为我们逃跑\n',
            '争取了时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350833V不过，最后那个人也\n',
            '被、被魔兽群包围了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D8B',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_5DC9')

    def _loc_5D8B(): pass

    label('loc_5D8B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DB2',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_5DC9')

    def _loc_5DB2(): pass

    label('loc_5DB2')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_5DC9(): pass

    label('loc_5DC9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DF0',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_5E2E')

    def _loc_5DF0(): pass

    label('loc_5DF0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E17',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_5E2E')

    def _loc_5E17(): pass

    label('loc_5E17')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_5E2E(): pass

    label('loc_5E2E')

    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010350834V#1020F！！',
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
        'loc_5E86',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350835V#065F怎、怎么会……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E86(): pass

    label('loc_5E86')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EB9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350836V#023F难道利吉他！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EB9(): pass

    label('loc_5EB9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EF6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350837V#072F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EF6(): pass

    label('loc_5EF6')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F25',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350838V#057F麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F25(): pass

    label('loc_5F25')

    ChrTalk(
        0x0102,
        (
            '#0020350839V#1042F……要立即采取行动了呢。',
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
        'loc_5FBD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350840V#022F总之现在首先\n',
            '要营救矿工们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350841V等完成之后\n',
            '再去救利吉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6096')

    def _loc_5FBD(): pass

    label('loc_5FBD')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_602B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350842V#072F呼，总之我们\n',
            '先快点去救矿工们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350843V等完成之后\n',
            '再去救游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6096')

    def _loc_602B(): pass

    label('loc_602B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6096',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350844V#057F总之营救矿工\n',
            '必须要摆在第一位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350845V等完成之后\n',
            '再去救游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6096(): pass

    label('loc_6096')

    ChrTalk(
        0x0101,
        (
            '#0010350846V#1003F……嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350847V虽然很担心，不过\n',
            '这也是我们的使命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350848V我、我因为肚子饿\n',
            '就飞跑出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350849V老大他们一定还\n',
            '躲在什么地方。',
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
        'loc_618B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350850V#072F这里一共有多少人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61F4')

    def _loc_618B(): pass

    label('loc_618B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_61C1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350851V#052F一共有多少人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61F4')

    def _loc_61C1(): pass

    label('loc_61C1')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_61F4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350852V#022F一共有多少人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_61F4(): pass

    label('loc_61F4')

    OP_8C(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0920350853V#2P应该还有４个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0920350854V#2P算上游击士兄弟的话\n',
            '还有５个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350855V#1002F明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350856V马上开始搜索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350857V#1042F嗯，要赶快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0960350858V快、快点回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    SetChrPos(0x0008, 132100, 0, 74120, 225)
    SetChrPos(0x0009, 132170, 0, 72480, 270)
    OP_6D(123230, 0, 71000, 0)
    SetChrPos(0x0000, 123230, 0, 71000, 270)
    SetChrPos(0x0001, 123230, 0, 71000, 270)
    SetChrPos(0x0002, 123230, 0, 71000, 270)
    SetChrPos(0x0003, 123230, 0, 71000, 270)
    FadeIn(1000, 0)
    OP_0D()
    OP_A2(0x2088)
    OP_28(0x00BF, 0x01, 0x0002)
    OP_28(0x00BF, 0x01, 0x0004)
    OP_28(0x00BF, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x6389
@scena.Code('func_11_6389')
def func_11_6389():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 0, 0x2088)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 1, 0x2089)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6396',
    )

    Return()

    def _loc_6396(): pass

    label('loc_6396')

    EventBegin(0x00)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    SetChrPos(0x000A, 130610, 1000, 14190, 180)
    SetChrPos(0x000B, 130610, 1000, 12770, 0)

    @scena.Lambda('lambda_63C8')
    def lambda_63C8():
        OP_6D(130580, 1000, 13440, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_63C8)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0970350859V#1S啊，女神爱德丝啊……\n',
            '请伸出援手拯救我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0980350860V#1S嘘，安静！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0980350861V#1S你在嘀咕些什么啊。\n',
            '魔兽会跑过来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0970350862V#1S是吗？上回塌方的时候\n',
            '也是像这样子祈祷才得救的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0970350863V#1S你也多少要保留一点\n',
            '信仰心如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    OP_4B(0x000A, 255)
    OP_4B(0x000B, 255)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x2089)
    EventEnd(0x01)

    Return()

# id: 0x0012 offset: 0x650E
@scena.Code('func_12_650E')
def func_12_650E():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(130139, 1000, 12840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    SetChrFlags(0x001E, 0x0080)
    FormationAddMember(ChrTable['矿工皮尔姆'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['矿工海涅'], 0xFF, 0xFF)
    SetChrFlags(0x0149, 0x0080)
    SetChrFlags(0x014A, 0x0080)
    SetChrPos(0x0101, 129190, 1000, 12210, 90)
    SetChrPos(0x0102, 128000, 1000, 11480, 90)
    SetChrPos(0x00F8, 129220, 1000, 13440, 90)
    SetChrPos(0x00F9, 127720, 1000, 13010, 90)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_8C(0x000A, 270, 0)
    OP_8C(0x000B, 270, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0980350864V你、你们是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350865V#1042F#2P我们是游击士协会的人。\n',
            '是来营救各位的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350866V#1002F两位有没有受伤？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0980350867V嗯、嗯……起码现在还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0970350868V啊，女神啊……',
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
        'loc_6709',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350869V#072F有坚定的信仰是好事情，\n',
            '不过要感谢还为时尚早。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350870V现在要尽快\n',
            '逃出这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67C5')

    def _loc_6709(): pass

    label('loc_6709')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_676E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350871V#050F喂喂，要感谢女神\n',
            '还为时尚早。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350872V现在要先离开此地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67C5')

    def _loc_676E(): pass

    label('loc_676E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_67C5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350873V#022F现在祈祷还早了点哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350874V首先要逃出这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_67C5(): pass

    label('loc_67C5')

    OP_59()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_8C(0x0102, 315, 400)
    SetChrChipByIndex(0x0102, 12)
    SetChrSubChip(0x0102, 0)
    OP_22(0x00D5, 0x00, 0x64)

    ChrTalk(
        0x0102,
        (
            '#0020350875V#1042F#2P确实……\n',
            '稍微早了一点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0010, 0x0040)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0012, 0x0040)

    @scena.Lambda('lambda_683C')
    def lambda_683C():
        OP_6D(127130, 1000, 12140, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_683C)

    CreateThread(0x0010, 0x01, 0x00, 0x0013)
    Sleep(200)

    @scena.Lambda('lambda_6860')
    def lambda_6860():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_6860')

    DispatchAsync2(0x0101, 0x0001, lambda_6860)

    @scena.Lambda('lambda_6871')
    def lambda_6871():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_6871')

    DispatchAsync2(0x0102, 0x0001, lambda_6871)

    @scena.Lambda('lambda_6882')
    def lambda_6882():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_6882')

    DispatchAsync2(0x00F8, 0x0001, lambda_6882)

    @scena.Lambda('lambda_6893')
    def lambda_6893():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_6893')

    DispatchAsync2(0x00F9, 0x0001, lambda_6893)

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    OP_22(0x00D5, 0x00, 0x64)
    Sleep(100)

    OP_22(0x00D5, 0x00, 0x64)
    Sleep(200)

    CreateThread(0x0011, 0x01, 0x00, 0x0014)
    Sleep(400)

    CreateThread(0x0012, 0x01, 0x00, 0x0015)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0012, 0x0001)
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_690A')
    def lambda_690A():
        OP_94(0x01, 0x00FE, 0x00BE, 0x000000C8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_690A)

    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_6937')
    def lambda_6937():
        OP_94(0x01, 0x00FE, 0x00AA, 0x000000C8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_6937)

    ChrTalk(
        0x000B,
        (
            '#0980350876V哇、哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0970350877V女神啊，请大发慈悲！',
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
        'loc_69C1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350878V#024F过来了！小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A2C')

    def _loc_69C1(): pass

    label('loc_69C1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_69F7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350879V#054F过来了！小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A2C')

    def _loc_69F7(): pass

    label('loc_69F7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A2C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350880V#076F当心！它们来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A2C(): pass

    label('loc_6A2C')

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    SetChrChipByIndex(0x0010, 3)

    @scena.Lambda('lambda_6A47')
    def lambda_6A47():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6A47)

    Sleep(30)

    SetChrChipByIndex(0x0011, 3)

    @scena.Lambda('lambda_6A67')
    def lambda_6A67():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6A67)

    Sleep(30)

    SetChrChipByIndex(0x0012, 3)

    @scena.Lambda('lambda_6A87')
    def lambda_6A87():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6A87)

    WaitForThreadExit(0x0010, 0x0001)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    Battle(0x00000ED8, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_6AC1'),
        (-1, 'loc_6AC6'),
    )

    def _loc_6AC1(): pass

    label('loc_6AC1')

    OP_B4(0x00)

    Jump('loc_6AC6')

    def _loc_6AC6(): pass

    label('loc_6AC6')

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    FormationDelMember(0x48, 0xFF)
    FormationDelMember(0x49, 0xFF)
    EventBegin(0x00)
    OP_6D(128650, 1000, 12260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, 130610, 1000, 12770, 270)
    SetChrPos(0x000A, 130610, 1000, 14190, 270)
    SetChrPos(0x0101, 129190, 1000, 12210, 270)
    SetChrPos(0x0102, 128000, 1000, 11480, 270)
    SetChrPos(0x00F8, 129220, 1000, 13440, 270)
    SetChrPos(0x00F9, 127720, 1000, 13010, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010350881V#1006F好！击退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0980350882V吓死我了……\n',
            '啊，女神啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0970350883V冷、冷汗都冒出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6C0E')
    def lambda_6C0E():
        OP_8C(0x0102, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6C0E)

    @scena.Lambda('lambda_6C1C')
    def lambda_6C1C():
        OP_8C(0x00F8, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_6C1C)

    Sleep(200)

    @scena.Lambda('lambda_6C2F')
    def lambda_6C2F():
        OP_8C(0x0101, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6C2F)

    @scena.Lambda('lambda_6C3D')
    def lambda_6C3D():
        OP_8C(0x00F9, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_6C3D)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020350884V#1042F请立即到\n',
            '升降机前避难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350885V由于附近可能会有魔兽，\n',
            '麻烦请迅速行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0980350886V哦、哦！明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0970350887V也愿女神\n',
            '保佑你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x001D, 0x0080)

    @scena.Lambda('lambda_6D00')
    def lambda_6D00():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_6D00')

    DispatchAsync2(0x0102, 0x0001, lambda_6D00)

    @scena.Lambda('lambda_6D11')
    def lambda_6D11():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_6D11')

    DispatchAsync2(0x0101, 0x0001, lambda_6D11)

    @scena.Lambda('lambda_6D22')
    def lambda_6D22():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_6D22')

    DispatchAsync2(0x00F8, 0x0001, lambda_6D22)

    @scena.Lambda('lambda_6D33')
    def lambda_6D33():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_6D33')

    DispatchAsync2(0x00F9, 0x0001, lambda_6D33)

    @scena.Lambda('lambda_6D44')
    def lambda_6D44():
        OP_6D(126940, 1000, 12790, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_6D44)

    CreateThread(0x000B, 0x01, 0x00, 0x0016)
    Sleep(200)

    CreateThread(0x000A, 0x01, 0x00, 0x0017)
    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    OP_A2(0x208A)
    OP_28(0x00BF, 0x01, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E4E',
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
            TXT(0x00, '【◇3组都已经救出的情况下】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        (0x00000000, 'loc_6DFB'),
        (-1, 'loc_6E4E'),
    )

    def _loc_6DFB(): pass

    label('loc_6DFB')

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0x000A, 131940, 0, 69900, 315)
    SetChrPos(0x000B, 130930, 0, 68610, 45)
    SetChrPos(0x000C, 124780, 0, 74190, 180)
    SetChrPos(0x000D, 126540, 0, 75140, 180)

    Jump('loc_6E4E')

    def _loc_6E4E(): pass

    label('loc_6E4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6EEC',
    )

    OP_A2(0x0000)

    ExecExpressionWithValue(
        0x001C,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    @scena.Lambda('lambda_6EAA')
    def lambda_6EAA():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6EAA)

    @scena.Lambda('lambda_6EB8')
    def lambda_6EB8():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_6EB8)

    Sleep(150)

    @scena.Lambda('lambda_6ECB')
    def lambda_6ECB():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6ECB)

    @scena.Lambda('lambda_6ED9')
    def lambda_6ED9():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_6ED9)

    OP_69(0x001C, 0x000007D0)
    Call(0, 0x0021)

    def _loc_6EEC(): pass

    label('loc_6EEC')

    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x6EEF
@scena.Code('func_13_6EEF')
def func_13_6EEF():
    SetChrPos(0x00FE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0x00FE, 3)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 122980, 0, 19990, 5000, 0x00)
    OP_8E(0x00FE, 122980, 500, 15170, 5000, 0x00)
    OP_8E(0x00FE, 125640, 500, 10850, 5000, 0x00)
    OP_8C(0x0010, 90, 400)
    SetChrChipByIndex(0x0010, 2)
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0014 offset: 0x6F5A
@scena.Code('func_14_6F5A')
def func_14_6F5A():
    SetChrPos(0x00FE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0x00FE, 3)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 122980, 0, 19990, 5000, 0x00)
    OP_8E(0x00FE, 122980, 500, 15170, 5000, 0x00)
    OP_8E(0x00FE, 124700, 500, 11980, 5000, 0x00)
    OP_8C(0x0011, 90, 400)
    SetChrChipByIndex(0x0011, 2)
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0015 offset: 0x6FC5
@scena.Code('func_15_6FC5')
def func_15_6FC5():
    SetChrPos(0x00FE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0x00FE, 3)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 122980, 0, 19990, 5000, 0x00)
    OP_8E(0x00FE, 122980, 500, 15170, 5000, 0x00)
    OP_8E(0x00FE, 124000, 500, 13040, 5000, 0x00)
    OP_8C(0x0012, 90, 400)
    SetChrChipByIndex(0x00FE, 2)
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0016 offset: 0x7030
@scena.Code('func_16_7030')
def func_16_7030():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrFlags(0x00FE, 0x0040)
    OP_8E(0x00FE, 128979, 1000, 10900, 5000, 0x00)
    OP_8E(0x00FE, 126210, 500, 10900, 5000, 0x00)
    OP_8E(0x00FE, 122720, 500, 14390, 5000, 0x00)
    OP_8E(0x00FE, 122630, -360, 18180, 5000, 0x00)
    ClearChrFlags(0x00FE, 0x0040)
    SetChrPos(0x000B, 130930, 0, 68610, 45)
    OP_4B(0x000B, 255)

    Return()

# id: 0x0017 offset: 0x70B2
@scena.Code('func_17_70B2')
def func_17_70B2():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrFlags(0x00FE, 0x0040)
    OP_8E(0x00FE, 130610, 1000, 12770, 5000, 0x00)
    OP_8E(0x00FE, 128979, 1000, 10900, 5000, 0x00)
    OP_8E(0x00FE, 126210, 500, 10900, 5000, 0x00)
    OP_8E(0x00FE, 122720, 500, 14390, 5000, 0x00)
    OP_8E(0x00FE, 122630, -360, 18180, 5000, 0x00)
    ClearChrFlags(0x00FE, 0x0040)
    SetChrPos(0x000A, 131940, 0, 69900, 315)
    OP_4B(0x000A, 255)

    Return()

# id: 0x0018 offset: 0x7148
@scena.Code('func_18_7148')
def func_18_7148():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 0, 0x2088)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7155',
    )

    Return()

    def _loc_7155(): pass

    label('loc_7155')

    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x000C, 255)
    SetChrPos(0x000C, 91290, 0, 30810, 129)
    SetChrFlags(0x000C, 0x0040)
    OP_6C(0, 0)
    ChrTurnDirection(0x0000, 0x000C, 0)
    ChrTurnDirection(0x0001, 0x000C, 0)
    ChrTurnDirection(0x0002, 0x000C, 0)
    ChrTurnDirection(0x0003, 0x000C, 0)
    OP_0D()

    @scena.Lambda('lambda_71A2')
    def lambda_71A2():
        OP_6D(94990, -500, 28960, 2500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_71A2)

    OP_8E(0x000C, 93270, -240, 29310, 1000, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    FormationAddMember(ChrTable['矿工彭兹'], 0xFF, 0xFF)

    ChrTalk(
        0x000C,
        (
            '#0950350888V可、可恶～提恩特那家伙\n',
            '竟然一个人逃跑，太狡猾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350889V只、只剩下我一个人\n',
            '岂不是太过寂寞了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_8C(0x000C, 270, 400)
    SetChrChipByIndex(0x0010, 3)
    SetChrChipByIndex(0x0012, 3)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0010, 87360, -450, 30190, 181)
    SetChrPos(0x0012, 86520, -380, 28480, 180)
    SetChrPos(0x0011, 99570, 0, 24640, 315)
    SetChrPos(0x0013, 100440, 0, 25840, 315)

    @scena.Lambda('lambda_72E2')
    def lambda_72E2():
        OP_6D(93440, -330, 29110, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_72E2)

    @scena.Lambda('lambda_72FA')
    def lambda_72FA():
        OP_92(0x0010, 0x000C, 0x00000BB8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_72FA)

    @scena.Lambda('lambda_730F')
    def lambda_730F():
        OP_92(0x0012, 0x000C, 0x00000DAC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_730F)

    WaitForThreadExit(0x0010, 0x0001)
    SetChrChipByIndex(0x0010, 2)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    WaitForThreadExit(0x0012, 0x0001)
    SetChrChipByIndex(0x0012, 2)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000C,
        (
            '#0950350890V啊……不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8C(0x000C, 90, 400)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrChipByIndex(0x0011, 3)
    SetChrChipByIndex(0x0013, 3)

    @scena.Lambda('lambda_7398')
    def lambda_7398():
        OP_8E(0x00FE, 97030, 0, 28560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_7398)

    @scena.Lambda('lambda_73B3')
    def lambda_73B3():
        OP_8E(0x00FE, 95620, -330, 28430, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_73B3)

    OP_94(0x01, 0x000C, 0x0000, 0x000001F4, 0x000007D0, 0x00)
    ChrTurnDirection(0x000C, 0x0011, 0)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_95(0x000C, 0x00000000, 0x00000000, 0x00000000, 0x00000320, 0x00002EE0)
    OP_94(0x01, 0x000C, 0x00B4, 0x000001F4, 0x00001388, 0x00)
    WaitForThreadExit(0x0011, 0x0001)
    SetChrChipByIndex(0x0011, 2)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    WaitForThreadExit(0x0013, 0x0001)
    SetChrChipByIndex(0x0013, 2)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)

    ChrTalk(
        0x000C,
        (
            '#0950350891V啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0010, 90, 0)
    OP_8C(0x0012, 90, 0)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0013, 0x01)
    SetChrChipByIndex(0x0010, 3)
    SetChrChipByIndex(0x0011, 3)
    SetChrChipByIndex(0x0012, 3)
    SetChrChipByIndex(0x0013, 3)

    @scena.Lambda('lambda_748F')
    def lambda_748F():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_748F')

    DispatchAsync2(0x0010, 0x0002, lambda_748F)

    @scena.Lambda('lambda_74A0')
    def lambda_74A0():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_74A0')

    DispatchAsync2(0x0011, 0x0002, lambda_74A0)

    @scena.Lambda('lambda_74B1')
    def lambda_74B1():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_74B1')

    DispatchAsync2(0x0013, 0x0002, lambda_74B1)

    @scena.Lambda('lambda_74C2')
    def lambda_74C2():
        OP_6D(93850, -230, 29940, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_74C2)

    @scena.Lambda('lambda_74DA')
    def lambda_74DA():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_74DA)

    @scena.Lambda('lambda_74F0')
    def lambda_74F0():
        OP_92(0x00FE, 0x000C, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_74F0)

    Sleep(120)

    CreateThread(0x0012, 0x01, 0x00, 0x001D)
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8F(0x000C, 93600, -210, 29780, 1000, 0x00)
    OP_8C(0x000C, 225, 400)
    OP_8F(0x000C, 94950, -240, 30620, 1000, 0x00)

    ChrTalk(
        0x000C,
        (
            '#0950350892V不、不好！！\n',
            '难道是走投无路了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350893V哇～有、有人吗～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_75AB')
    def lambda_75AB():
        OP_6D(96410, -130, 28390, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_75AB)

    @scena.Lambda('lambda_75C3')
    def lambda_75C3():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_75C3)

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    CreateThread(0x0102, 0x01, 0x00, 0x001A)
    Sleep(200)

    CreateThread(0x0101, 0x01, 0x00, 0x0019)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x001C)
    Sleep(200)

    CreateThread(0x00F8, 0x01, 0x00, 0x001B)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    ChrTurnDirection(0x000C, 0x0101, 800)

    ChrTalk(
        0x000C,
        (
            '#0950350894V你、你们是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350895V#1006F#2P这种事待会儿再说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350896V#1042F#1P我们马上来救你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Battle(0x00000ED9, 0x00300018, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_76C2'),
        (-1, 'loc_76C7'),
    )

    def _loc_76C2(): pass

    label('loc_76C2')

    OP_B4(0x00)

    Jump('loc_76C7')

    def _loc_76C7(): pass

    label('loc_76C7')

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    EventBegin(0x00)
    FormationDelMember(0x4A, 0xFF)
    OP_6D(95530, -350, 29670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 95990, -230, 28580, 180)
    SetChrPos(0x0102, 94980, -500, 28580, 180)
    SetChrPos(0x00F8, 96920, 0, 28930, 90)
    SetChrPos(0x00F9, 93800, -470, 28930, 225)
    OP_8C(0x000C, 180, 0)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrPos(0x000C, 95240, -270, 30370, 180)
    ClearChrFlags(0x000C, 0x0040)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0950350897V呼～呼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350898V啊～～我还以为自己要死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350899V#1007F呼，真不容易……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350900V#1043F真是千钧一发啊。',
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
        'loc_7888',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350901V#561F还、还好赶上了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_790D')

    def _loc_7888(): pass

    label('loc_7888')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_78C9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350902V#073F呼……\n',
            '真的是只差一步呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_790D')

    def _loc_78C9(): pass

    label('loc_78C9')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_790D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350903V#027F真是的……\n',
            '真是让人捏一把汗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_790D(): pass

    label('loc_790D')

    ChrTalk(
        0x000C,
        (
            '#0950350904V那个，莫非你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350905V是在上次塌方事故中\n',
            '救了我们的游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_7984')
    def lambda_7984():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_7984')

    DispatchAsync2(0x0101, 0x0001, lambda_7984)

    @scena.Lambda('lambda_7995')
    def lambda_7995():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_7995')

    DispatchAsync2(0x0102, 0x0001, lambda_7995)

    Sleep(200)

    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)

    @scena.Lambda('lambda_79BF')
    def lambda_79BF():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_79BF')

    DispatchAsync2(0x00F8, 0x0001, lambda_79BF)

    @scena.Lambda('lambda_79D0')
    def lambda_79D0():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_79D0')

    DispatchAsync2(0x00F9, 0x0001, lambda_79D0)

    ChrTalk(
        0x0101,
        (
            '#0010350906V#1006F嗯，答对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350907V#1040F不过那时候我们\n',
            '还是准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350908V那～那就是说你们已经\n',
            '顺利成为正游击士了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350909V嗯，这么说来，看上去\n',
            '是有了点正游击士的风格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350910V#1008F嘿嘿，真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350911V#1007F……什么啊，现在\n',
            '可不是开玩笑的场合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350912V啊……\n',
            '是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350913V那接下来我应该\n',
            '怎么做才好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350914V#1042F请立即到\n',
            '升降机前避难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350915V尽快离开，\n',
            '不要让魔兽发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350916V嗯、嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0950350917V那么，\n',
            '你们也要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7C0E')
    def lambda_7C0E():
        OP_6D(97510, 0, 28150, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_7C0E)

    @scena.Lambda('lambda_7C26')
    def lambda_7C26():
        OP_8F(0x00FE, 96830, -10, 27890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_7C26)

    @scena.Lambda('lambda_7C41')
    def lambda_7C41():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_7C41')

    DispatchAsync2(0x0101, 0x0001, lambda_7C41)

    OP_8E(0x000C, 99420, 0, 26990, 4000, 0x00)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_8E(0x000C, 108600, 0, 27380, 4000, 0x00)
    TerminateThread(0x0101, 0x01)
    SetChrPos(0x000C, 124780, 0, 74190, 180)
    OP_4B(0x000C, 255)
    OP_A2(0x208B)
    OP_28(0x00BF, 0x01, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D69',
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
            TXT(0x00, '【◇3组都已经救出的情况下】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        (0x00000000, 'loc_7D16'),
        (-1, 'loc_7D69'),
    )

    def _loc_7D16(): pass

    label('loc_7D16')

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0x000A, 131940, 0, 69900, 315)
    SetChrPos(0x000B, 130930, 0, 68610, 45)
    SetChrPos(0x000C, 124780, 0, 74190, 180)
    SetChrPos(0x000D, 126540, 0, 75140, 180)

    Jump('loc_7D69')

    def _loc_7D69(): pass

    label('loc_7D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7E06',
    )

    OP_A2(0x0001)
    Fade(500)
    OP_6D(95210, -440, 28870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(22000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 95750, -310, 28080, 315)
    SetChrPos(0x0102, 94440, -500, 28540, 45)
    SetChrPos(0x00F8, 96210, -160, 29110, 225)
    SetChrPos(0x00F9, 94950, -500, 29820, 135)
    OP_0D()
    Call(0, 0x0021)

    def _loc_7E06(): pass

    label('loc_7E06')

    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x7E09
@scena.Code('func_19_7E09')
def func_19_7E09():
    SetChrPos(0x00FE, 106130, 0, 27510, 45)
    OP_8E(0x00FE, 99570, 0, 27040, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x001A offset: 0x7E36
@scena.Code('func_1A_7E36')
def func_1A_7E36():
    SetChrPos(0x00FE, 106130, 0, 27510, 45)
    OP_8E(0x00FE, 98740, 0, 26320, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x001B offset: 0x7E63
@scena.Code('func_1B_7E63')
def func_1B_7E63():
    SetChrPos(0x00FE, 106130, 0, 27510, 45)
    OP_8E(0x00FE, 100770, 0, 26530, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x001C offset: 0x7E90
@scena.Code('func_1C_7E90')
def func_1C_7E90():
    SetChrPos(0x00FE, 106130, 0, 27510, 45)
    OP_8E(0x00FE, 99520, 0, 25280, 5000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x001D offset: 0x7EBD
@scena.Code('func_1D_7EBD')
def func_1D_7EBD():
    OP_8E(0x00FE, 93210, -330, 28890, 2000, 0x00)
    ChrTurnDirection(0x0012, 0x000C, 400)

    Return()

# id: 0x001E offset: 0x7ED9
@scena.Code('func_1E_7ED9')
def func_1E_7ED9():
    OP_8E(0x00F8, 95850, -260, 29730, 2000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x001F offset: 0x7EF5
@scena.Code('func_1F_7EF5')
def func_1F_7EF5():
    OP_8E(0x00F9, 94400, -320, 30080, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0020 offset: 0x7F11
@scena.Code('func_20_7F11')
def func_20_7F11():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 0, 0x2088)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7F1E',
    )

    Return()

    def _loc_7F1E(): pass

    label('loc_7F1E')

    EventBegin(0x00)
    Fade(500)
    OP_4A(0x000D, 255)
    SetChrPos(0x000D, 83170, -500, 10620, 90)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0010, 86220, -500, 12400, 270)
    SetChrPos(0x0011, 87000, -500, 11330, 270)
    SetChrPos(0x0012, 86950, -500, 9870, 270)
    SetChrPos(0x0013, 86220, -500, 8710, 270)
    SetChrChipByIndex(0x0010, 2)
    SetChrChipByIndex(0x0011, 2)
    SetChrChipByIndex(0x0012, 2)
    SetChrChipByIndex(0x0013, 2)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_800C',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_804A')

    def _loc_800C(): pass

    label('loc_800C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8033',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_804A')

    def _loc_8033(): pass

    label('loc_8033')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_804A(): pass

    label('loc_804A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8071',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_80AF')

    def _loc_8071(): pass

    label('loc_8071')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8098',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_80AF')

    def _loc_8098(): pass

    label('loc_8098')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_80AF(): pass

    label('loc_80AF')

    ChrTurnDirection(0x0000, 0x000D, 0)
    ChrTurnDirection(0x0001, 0x000D, 0)
    ChrTurnDirection(0x0002, 0x000D, 0)
    ChrTurnDirection(0x0003, 0x000D, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010350204V#1020F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350919V#1044F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)

    @scena.Lambda('lambda_811E')
    def lambda_811E():
        OP_6D(83130, -340, 10670, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_811E)

    OP_6C(315000, 0)
    OP_0D()
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_8163')
    def lambda_8163():
        OP_94(0x00, 0x00FE, 0x0000, 0x000002BC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_8163)

    Sleep(120)

    @scena.Lambda('lambda_817E')
    def lambda_817E():
        OP_94(0x00, 0x00FE, 0x0000, 0x000002BC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_817E)

    Sleep(100)

    @scena.Lambda('lambda_8199')
    def lambda_8199():
        OP_94(0x00, 0x00FE, 0x0000, 0x000002BC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_8199)

    Sleep(150)

    OP_94(0x00, 0x0013, 0x0000, 0x000002BC, 0x000003E8, 0x00)
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_81D5')
    def lambda_81D5():
        OP_91(0x00FE, -500, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_81D5)

    Sleep(150)

    Sleep(50)

    @scena.Lambda('lambda_81FA')
    def lambda_81FA():
        OP_94(0x00, 0x00FE, 0x0000, 0x000002BC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_81FA)

    Sleep(100)

    @scena.Lambda('lambda_8215')
    def lambda_8215():
        OP_94(0x00, 0x00FE, 0x0000, 0x000002BC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_8215)

    Sleep(100)

    @scena.Lambda('lambda_8230')
    def lambda_8230():
        OP_94(0x00, 0x00FE, 0x0000, 0x000002BC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_8230)

    Sleep(120)

    OP_94(0x00, 0x0013, 0x0000, 0x000002BC, 0x000003E8, 0x00)
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_826C')
    def lambda_826C():
        OP_91(0x00FE, -500, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_826C)

    Sleep(200)

    @scena.Lambda('lambda_828C')
    def lambda_828C():
        OP_94(0x00, 0x00FE, 0x0000, 0x000004B0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_828C)

    Sleep(100)

    @scena.Lambda('lambda_82A7')
    def lambda_82A7():
        OP_94(0x00, 0x00FE, 0x0000, 0x000004B0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_82A7)

    Sleep(120)

    @scena.Lambda('lambda_82C2')
    def lambda_82C2():
        OP_94(0x00, 0x00FE, 0x0000, 0x000004B0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_82C2)

    Sleep(100)

    @scena.Lambda('lambda_82DD')
    def lambda_82DD():
        OP_94(0x00, 0x00FE, 0x0000, 0x000004B0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_82DD)

    Sleep(200)

    @scena.Lambda('lambda_82F8')
    def lambda_82F8():
        OP_91(0x00FE, -500, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_82F8)

    WaitForThreadExit(0x000D, 0x0001)
    OP_4A(0x000D, 255)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0012, 0x0001)
    WaitForThreadExit(0x0013, 0x0001)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#0940350920V混、混帐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350921V把魔兽引向这边的\n',
            '做法是很好啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 45, 400)
    Sleep(400)

    OP_8C(0x000D, 135, 400)
    Sleep(400)

    OP_8C(0x000D, 90, 400)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0940350922V嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350923V……不过这看起来\n',
            '做得有些过头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350924V阿妮娅、芙莉莎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350925V不好意思……\n',
            '看来我已经不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350926V老大！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    FormationAddMember(ChrTable['加通老大'], 0xFF, 0xFF)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrPos(0x0101, 94580, -350, 10790, 5000)
    SetChrPos(0x0102, 94510, -390, 9750, 5000)
    SetChrPos(0x00F8, 95840, -240, 10950, 5000)
    SetChrPos(0x00F9, 95640, -410, 9340, 5000)

    @scena.Lambda('lambda_84F2')
    def lambda_84F2():
        OP_6D(84450, -500, 10830, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_84F2)

    @scena.Lambda('lambda_850A')
    def lambda_850A():
        OP_8E(0x00FE, 87580, -350, 10790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_850A)

    Sleep(300)

    @scena.Lambda('lambda_852A')
    def lambda_852A():
        OP_8E(0x00FE, 87510, -390, 9750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_852A)

    Sleep(200)

    @scena.Lambda('lambda_854A')
    def lambda_854A():
        OP_8E(0x00FE, 89340, -240, 10950, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_854A)

    Sleep(40)

    OP_8E(0x00F9, 89140, -410, 9340, 5000, 0x00)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000D,
        (
            '#0940350927V你、你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350928V#1005F#2P别放弃！\n',
            '我们一定会救你的！',
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
        'loc_863C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350929V#076F用保守战术的话时间来不及了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350930V一口气杀出一条血路来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8701')

    def _loc_863C(): pass

    label('loc_863C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_869C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350931V#054F没时间小心翼翼的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350932V现在只能一口气突入了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8701')

    def _loc_869C(): pass

    label('loc_869C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8701',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350933V#024F用保守战术的话时间来不及了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350934V大家做好觉悟后突入吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8701(): pass

    label('loc_8701')

    ChrTalk(
        0x0102,
        (
            '#0020350935V#1046F#3P是！',
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
        'loc_8751',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350936V#062F明、明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8751(): pass

    label('loc_8751')

    @scena.Lambda('lambda_8757')
    def lambda_8757():
        OP_90(0x00FE, -1500, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8757)

    @scena.Lambda('lambda_8772')
    def lambda_8772():
        OP_90(0x00FE, -1500, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8772)

    @scena.Lambda('lambda_878D')
    def lambda_878D():
        OP_90(0x00FE, -1500, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_878D)

    @scena.Lambda('lambda_87A8')
    def lambda_87A8():
        OP_90(0x00FE, -1400, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_87A8)

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    Battle(0x00000EDA, 0x00300018, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    EventBegin(0x00)
    FormationDelMember(0x32, 0xFF)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    OP_6D(82190, -500, 10990, 0)
    OP_67(0, 8109, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 84100, -500, 10790, 90)
    SetChrPos(0x0102, 84110, -410, 9850, 90)
    SetChrPos(0x00F8, 83380, -470, 11670, 90)
    SetChrPos(0x00F9, 83620, -180, 8820, 90)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010350937V#1007F呼，总算……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350938V#1043F……似乎解决了呢。',
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
        'loc_8947',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350939V#561F呼、呼……\n',
            '我的心跳得好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8947(): pass

    label('loc_8947')

    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)

    @scena.Lambda('lambda_8961')
    def lambda_8961():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_8961')

    DispatchAsync2(0x00F8, 0x0001, lambda_8961)

    @scena.Lambda('lambda_8972')
    def lambda_8972():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_8972')

    DispatchAsync2(0x00F9, 0x0001, lambda_8972)

    Sleep(200)

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_899C')
    def lambda_899C():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_899C')

    DispatchAsync2(0x0101, 0x0001, lambda_899C)

    @scena.Lambda('lambda_89AD')
    def lambda_89AD():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_89AD')

    DispatchAsync2(0x0102, 0x0001, lambda_89AD)

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89F7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350940V#020F老大，你没受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A5E')

    def _loc_89F7(): pass

    label('loc_89F7')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A2F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350941V#051F大叔，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A5E')

    def _loc_8A2F(): pass

    label('loc_8A2F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A5E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350942V#070F没受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A5E(): pass

    label('loc_8A5E')

    ChrTalk(
        0x000D,
        (
            '#0940350943V嗯、嗯……\n',
            '只是擦伤而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350944V不过真多亏你们\n',
            '跑来救我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350945V有机会的话也希望偶尔在\n',
            '事故之外的场合下见见你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350946V#1016F哈哈，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350947V不知为什么，每次来矿山\n',
            '都会遇到紧急情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350948V#1048F呼，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350949V#1035F不过，等下次\n',
            '有机会再聊吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350950V现在必须先要请你\n',
            '尽快去避难……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350951V哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350952V#1002F提恩特先生他们在\n',
            '升降机前面等着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350953V请你先到\n',
            '那里避难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350954V好，就这么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8C76')
    def lambda_8C76():
        OP_6D(84620, -500, 10450, 1500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_8C76)

    OP_8E(0x000D, 82300, -270, 11970, 3000, 0x00)
    OP_8E(0x000D, 83180, -440, 12650, 3000, 0x00)
    OP_8E(0x000D, 86360, -500, 12400, 3000, 0x00)
    OP_8E(0x000D, 88130, -500, 10050, 3000, 0x00)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    ChrTurnDirection(0x000D, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0940350955V……对了，得告诉你们几个，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350956V从支部过来负责\n',
            '警戒的游击士小哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350957V那家伙已经去避难了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350958V#1026F#2P啊，你是说利吉先生吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350959V#1043F#3P不，很遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350960V我们也还\n',
            '没看到他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0940350961V果然是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0940350962V如果找不到的话\n',
            '你们就去施工现场看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0940350963V那位小哥直到最后\n',
            '都在那里为大家争取逃跑的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350964V#1002F#2P……嗯，明白了。',
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
        'loc_8F00',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350965V#072F好，我们会参考你的意见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F79')

    def _loc_8F00(): pass

    label('loc_8F00')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F3E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350966V#050F我们会参考你的意见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8F79')

    def _loc_8F3E(): pass

    label('loc_8F3E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F79',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350967V#022F我们会参考你的意见的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F79(): pass

    label('loc_8F79')

    @scena.Lambda('lambda_8F7F')
    def lambda_8F7F():
        OP_6D(90550, -420, 10520, 1500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_8F7F)

    OP_8E(0x000D, 101910, 0, 11210, 3000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    SetChrPos(0x000D, 126540, 0, 75140, 180)
    OP_4B(0x000D, 255)
    OP_A2(0x208C)
    OP_28(0x00BF, 0x01, 0x0040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_909A',
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
            TXT(0x00, '【◇3组都已经救出的情况下】\n'),
            TXT(0x01, '【◇不变更】\n'),
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
        (0x00000000, 'loc_9047'),
        (-1, 'loc_909A'),
    )

    def _loc_9047(): pass

    label('loc_9047')

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0x000A, 131940, 0, 69900, 315)
    SetChrPos(0x000B, 130930, 0, 68610, 45)
    SetChrPos(0x000C, 124780, 0, 74190, 180)
    SetChrPos(0x000D, 126540, 0, 75140, 180)

    Jump('loc_909A')

    def _loc_909A(): pass

    label('loc_909A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 2, 0x208A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 3, 0x208B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 4, 0x208C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9137',
    )

    OP_A2(0x0002)
    Fade(500)
    OP_6D(82850, -460, 10740, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 83690, -500, 10780, 270)
    SetChrPos(0x0102, 82740, -440, 11720, 180)
    SetChrPos(0x00F8, 82930, -430, 9940, 0)
    SetChrPos(0x00F9, 82130, -280, 10740, 90)
    OP_0D()
    Call(0, 0x0021)

    def _loc_9137(): pass

    label('loc_9137')

    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0x913A
@scena.Code('func_21_913A')
def func_21_913A():
    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010350968V#1002F那么……现在人都到齐了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350969V#1040F嗯，矿工们应该\n',
            '已经全部营救完毕了。',
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
        'loc_9224',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350970V#026F就是说，接下来\n',
            '只剩要去救利吉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350971V#522F很遗憾，目前为止还\n',
            '没看到过他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9326')

    def _loc_9224(): pass

    label('loc_9224')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_929D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350972V#552F就是说，接下来是利吉啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350973V在目前为止调查过的地方\n',
            '好象都没见到过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9326')

    def _loc_929D(): pass

    label('loc_929D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9326',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350974V#072F就是说，接下来只剩那个\n',
            '叫做利吉的游击士了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350975V很遗憾，在迄今为止的搜索中\n',
            '都没发现他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9326(): pass

    label('loc_9326')

    ChrTalk(
        0x0101,
        (
            '#0010350976V#1002F我记得老大\n',
            '叫我们去施工现场看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350977V他说利吉先生\n',
            '一个人留在那里……',
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
        'loc_9403',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350978V#050F现在没时间多想了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350979V在一切为时已晚之前，\n',
            '赶快去那个什么施工现场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9498')

    def _loc_9403(): pass

    label('loc_9403')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_944F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350981V#072F快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350982V有可能会来不及的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9498')

    def _loc_944F(): pass

    label('loc_944F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9498',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350984V#022F快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350985V有可能会来不及的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9498(): pass

    label('loc_9498')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9581',
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
            TXT(0x00, '【◇最后救出的是皮尔姆、海涅的情况下】\n'),
            TXT(0x01, '【◇最后救出的是彭兹的情况下】\n'),
            TXT(0x02, '【◇最后救出的是加通的情况下】\n'),
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
        (0x00000000, 'loc_955D'),
        (0x00000001, 'loc_9569'),
        (0x00000002, 'loc_9575'),
        (-1, 'loc_9581'),
    )

    def _loc_955D(): pass

    label('loc_955D')

    OP_A2(0x0000)
    OP_A3(0x0001)
    OP_A3(0x0002)

    Jump('loc_9581')

    def _loc_9569(): pass

    label('loc_9569')

    OP_A3(0x0000)
    OP_A2(0x0001)
    OP_A3(0x0002)

    Jump('loc_9581')

    def _loc_9575(): pass

    label('loc_9575')

    OP_A3(0x0000)
    OP_A3(0x0001)
    OP_A2(0x0002)

    Jump('loc_9581')

    def _loc_9581(): pass

    label('loc_9581')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_95C3',
    )

    OP_A3(0x0000)

    ChrTalk(
        0x0102,
        (
            '#0020350980V#1042F塌方的现场\n',
            '应该是在西北方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9644')

    def _loc_95C3(): pass

    label('loc_95C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_9605',
    )

    OP_A3(0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020350983V#1042F塌方的现场\n',
            '应该是在西北方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9644')

    def _loc_9605(): pass

    label('loc_9605')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_9644',
    )

    OP_A3(0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020350983V#1042F塌方的现场\n',
            '应该是在西北方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9644(): pass

    label('loc_9644')

    ChrTalk(
        0x0101,
        (
            '#0010350987V#1002F好！走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x208D)
    OP_28(0x00BF, 0x01, 0x0080)
    OP_28(0x00BF, 0x01, 0x0100)

    Return()

# id: 0x0022 offset: 0x9676
@scena.Code('func_22_9676')
def func_22_9676():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 5, 0x208D)),
            Expr.Return,
        ),
        'loc_9A87',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 6, 0x208E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98A0',
    )

    Fade(500)
    OP_6D(93490, -500, 66260, 0)
    SetChrPos(0x0101, 93950, -260, 66700, 0)
    SetChrPos(0x0102, 93090, -480, 66700, 0)
    SetChrPos(0x00F8, 94220, -230, 65500, 0)
    SetChrPos(0x00F9, 92880, -350, 65500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010350988V#1002F前面就是魔兽的巢穴……',
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
        'loc_976A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350989V#057F真不得了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350990V到处都充满了魔兽的气味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983C')

    def _loc_976A(): pass

    label('loc_976A')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_97CC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350991V#523F真是好讨厌的地方啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350992V到处都充满了魔兽的气味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_983C')

    def _loc_97CC(): pass

    label('loc_97CC')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_983C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350993V#072F嗯，简直是死亡之地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350994V光是站在这里就能感受到\n',
            '强烈的魔兽的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_983C(): pass

    label('loc_983C')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350995V#1042F进去之后就\n',
            '无法回头了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350996V艾丝蒂尔。\n',
            '装备都确认好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_995A')

    def _loc_98A0(): pass

    label('loc_98A0')

    Fade(500)
    OP_6D(93490, -500, 66260, 0)
    SetChrPos(0x0101, 93950, -260, 66700, 0)
    SetChrPos(0x0102, 93090, -480, 66700, 0)
    SetChrPos(0x00F8, 94220, -230, 65500, 0)
    SetChrPos(0x00F9, 92880, -350, 65500, 0)
    OP_0D()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350997V#1042F艾丝蒂尔。\n',
            '装备都确认好了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350998V进去之后就\n',
            '无法回头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_995A(): pass

    label('loc_995A')

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
            TXT(0x00, '【突入】\n'),
            TXT(0x01, '【还没准备好】\n'),
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
        (0x00000000, 'loc_99B9'),
        (0x00000001, 'loc_99C0'),
        (-1, 'loc_9A84'),
    )

    def _loc_99B9(): pass

    label('loc_99B9')

    Call(0, 0x0023)

    Jump('loc_9A84')

    def _loc_99C0(): pass

    label('loc_99C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0411, 6, 0x208E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9A50',
    )

    OP_A2(0x208E)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350999V#1015F应该是没问题的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351000V不过我想再\n',
            '仔细确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351001V#1040F明白，就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A7F')

    def _loc_9A50(): pass

    label('loc_9A50')

    ChrTalk(
        0x0102,
        (
            '#0020351002V#1040F明白，好好准备\n',
            '一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A7F(): pass

    label('loc_9A7F')

    EventEnd(0x00)

    Jump('loc_9A84')

    def _loc_9A84(): pass

    label('loc_9A84')

    Jump('loc_9BCF')

    def _loc_9A87(): pass

    label('loc_9A87')

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9B51',
    )

    ChrTalk(
        0x0101,
        (
            '#0010351003V#1025F啊……\n',
            '这里是魔兽的巢穴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351004V#1042F在进入这里之前\n',
            '首先要营救矿工们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020351005V还没确认全体人员是否平安哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340419V#1002F嗯，我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_9BB4')

    def _loc_9B51(): pass

    label('loc_9B51')

    ChrTalk(
        0x0101,
        (
            '#0010351007V#1002F这里是魔兽的巢穴呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351008V在进入这里之前\n',
            '要先确认矿工们是否平安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9BB4(): pass

    label('loc_9BB4')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_9BCF(): pass

    label('loc_9BCF')

    Return()

# id: 0x0023 offset: 0x9BD0
@scena.Code('func_23_9BD0')
def func_23_9BD0():
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010351009V#1006F嗯……准备ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351010V#1042F好，那我们走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)
    OP_8C(0x0102, 0, 400)

    @scena.Lambda('lambda_9C42')
    def lambda_9C42():
        OP_6D(95620, 0, 73830, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9C42)

    @scena.Lambda('lambda_9C5A')
    def lambda_9C5A():
        OP_8E(0x00FE, 95950, -350, 75420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9C5A)

    Sleep(200)

    @scena.Lambda('lambda_9C7A')
    def lambda_9C7A():
        OP_8E(0x00FE, 95950, -350, 75420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9C7A)

    Sleep(200)

    @scena.Lambda('lambda_9C9A')
    def lambda_9C9A():
        OP_8E(0x00FE, 95950, -350, 75420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9C9A)

    Sleep(200)

    @scena.Lambda('lambda_9CBA')
    def lambda_9CBA():
        OP_8E(0x00FE, 95950, -350, 75420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_9CBA)

    Sleep(400)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x0101, 0x02)
    SetChrPos(0x0101, 185820, -450, 52650, 0)
    SetChrPos(0x0102, 185820, -450, 52650, 0)
    SetChrPos(0x00F8, 185820, -450, 52650, 0)
    SetChrPos(0x00F9, 185820, -450, 52650, 0)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0010, 189500, -250, 70370, 180)
    SetChrPos(0x0011, 190500, -250, 69540, 225)
    SetChrPos(0x0012, 190400, -130, 68040, 315)
    SetChrPos(0x0013, 188000, -250, 70370, 180)
    SetChrPos(0x0014, 187000, -250, 69540, 135)
    SetChrPos(0x0015, 186900, -130, 68040, 45)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0015, 0xFF)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    SetChrPos(0x0016, 188680, 0, 73010, 202)
    SetChrPos(0x0017, 185450, 0, 71540, 139)
    SetChrPos(0x0019, 191630, 0, 71750, 239)
    SetChrPos(0x001A, 193000, -130, 68420, 270)
    SetChrPos(0x001B, 184070, 0, 68530, 103)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    OP_D2(0x00090002, 0x00090006, 0x07)
    OP_D2(0x0007051D, 0x00070524, 0x04)
    OP_D2(0x0007051E, 0x00070525, 0x05)
    SetChrChipByIndex(0x000E, 5)
    SetChrSubChip(0x000E, 3)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 188800, -250, 68950, 0)
    LoadEffect(0x01, 'scraft\\\\sc000_11.eff')
    LoadEffect(0x02, 'map\\\\mp023_00.eff')
    LoadEffect(0x03, 'monster\\\\msc0550.eff')
    OP_26(287)
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    SetChrChipByIndex(0x00F8, 14)
    SetChrChipByIndex(0x00F9, 16)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x0010, 2)
    SetChrChipByIndex(0x0011, 2)
    SetChrChipByIndex(0x0012, 2)
    SetChrChipByIndex(0x0013, 2)
    SetChrChipByIndex(0x0014, 2)
    SetChrChipByIndex(0x0015, 2)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    CreateThread(0x0015, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x0016, 2)
    SetChrChipByIndex(0x0017, 2)
    SetChrChipByIndex(0x0018, 2)
    SetChrChipByIndex(0x0019, 2)
    SetChrChipByIndex(0x001A, 2)
    SetChrChipByIndex(0x001B, 2)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    CreateThread(0x0018, 0x00, 0x00, 0x0002)
    CreateThread(0x0019, 0x00, 0x00, 0x0002)
    CreateThread(0x001A, 0x00, 0x00, 0x0002)
    CreateThread(0x001B, 0x00, 0x00, 0x0002)
    OP_20(0x000003E8)
    Sleep(1000)

    OP_21()
    OP_1D(0x56)
    Sleep(1000)

    OP_6D(199700, 110, 73850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(107000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_9FE9')
    def lambda_9FE9():
        OP_6D(188900, -250, 69050, 5000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_9FE9)

    @scena.Lambda('lambda_A001')
    def lambda_A001():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_A001)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x000D, 0x0001)

    ChrTalk(
        0x000E,
        (
            '#3350351011V#4P呜、呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A041')
    def lambda_A041():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x000003E8, 0x000007D0)
        Yield()

        Jump('lambda_A041')

    DispatchAsync2(0x000E, 0x0001, lambda_A041)

    OP_99(0x000E, 0x03, 0x00, 0x00000258)
    TerminateThread(0x000E, 0x01)
    SetChrChipByIndex(0x000E, 6)
    CreateThread(0x0013, 0x01, 0x00, 0x0024)
    Sleep(200)

    CreateThread(0x0010, 0x01, 0x00, 0x0025)
    Sleep(500)

    @scena.Lambda('lambda_A088')
    def lambda_A088():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_A088)

    @scena.Lambda('lambda_A096')
    def lambda_A096():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_A096)

    @scena.Lambda('lambda_A0A4')
    def lambda_A0A4():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_A0A4)

    @scena.Lambda('lambda_A0B2')
    def lambda_A0B2():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_A0B2)

    Sleep(200)

    @scena.Lambda('lambda_A0C5')
    def lambda_A0C5():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_A0C5')

    DispatchAsync2(0x0016, 0x0001, lambda_A0C5)

    @scena.Lambda('lambda_A0D6')
    def lambda_A0D6():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_A0D6')

    DispatchAsync2(0x0017, 0x0001, lambda_A0D6)

    @scena.Lambda('lambda_A0E7')
    def lambda_A0E7():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_A0E7')

    DispatchAsync2(0x0018, 0x0001, lambda_A0E7)

    @scena.Lambda('lambda_A0F8')
    def lambda_A0F8():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_A0F8')

    DispatchAsync2(0x0019, 0x0001, lambda_A0F8)

    @scena.Lambda('lambda_A109')
    def lambda_A109():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_A109')

    DispatchAsync2(0x001A, 0x0001, lambda_A109)

    @scena.Lambda('lambda_A11A')
    def lambda_A11A():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_A11A')

    DispatchAsync2(0x001B, 0x0001, lambda_A11A)

    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    TerminateThread(0x0016, 0x01)
    TerminateThread(0x0017, 0x01)
    TerminateThread(0x0018, 0x01)
    TerminateThread(0x0019, 0x01)
    TerminateThread(0x001A, 0x01)
    TerminateThread(0x001B, 0x01)

    ChrTalk(
        0x000E,
        (
            '#3350351012V啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A167')
    def lambda_A167():
        OP_9E(0x00FE, 0x00000032, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_A167')

    DispatchAsync2(0x000E, 0x0001, lambda_A167)

    Sleep(200)

    OP_99(0x000E, 0x03, 0x00, 0x0000012C)
    Sleep(200)

    TerminateThread(0x000E, 0x01)
    SetChrChipByIndex(0x000E, 6)

    ChrTalk(
        0x000E,
        (
            '#3350351013V呜、呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351014V#5P利吉先生！',
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
        'loc_A205',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351015V#1P利吉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A224')

    def _loc_A205(): pass

    label('loc_A205')

    ChrTalk(
        0x0102,
        (
            '#0020351016V#1P你没事吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A224(): pass

    label('loc_A224')

    TerminateThread(0x000E, 0x03)
    CreateThread(0x0101, 0x01, 0x00, 0x0027)
    CreateThread(0x0101, 0x02, 0x00, 0x002B)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x0028)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0029)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x002A)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A35B',
    )

    ChrTalk(
        0x000E,
        (
            '#3350351017V那、那个……\n',
            '艾丝蒂尔和雪拉前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3350351018V你、你们怎么会……\n',
            '来这里……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030351019V#524F利吉，你已经做得很好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030351020V你战斗得非常出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351021V#1042F接下来的事情就\n',
            '交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A411')

    def _loc_A35B(): pass

    label('loc_A35B')

    ChrTalk(
        0x000E,
        (
            '#3350351022V那、那个……\n',
            '艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3350351018V你、你们怎么会……\n',
            '来这里……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351024V#1006F当然是来帮你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351025V#1042F接下来就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A411(): pass

    label('loc_A411')

    ChrTalk(
        0x000E,
        (
            '#3350351026V是、是吗……太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#3350351027V不、不过，你们要小心。\n',
            '敌人不只是眼前这些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x000E, 5)
    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x000E, 0x00, 0x03, 0x000003E8)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4F4',
    )

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080351028V#072F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080351029V#076F不好，先后退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5C2')

    def _loc_A4F4(): pass

    label('loc_A4F4')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A55F',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050351030V#052F嗯……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050351031V#054F喂，先后退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5C2')

    def _loc_A55F(): pass

    label('loc_A55F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A5C2',
    )

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030351032V#022F……！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030351033V大家先后退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A5C2(): pass

    label('loc_A5C2')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_A5D1')
    def lambda_A5D1():
        OP_6D(188840, 720, 70020, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_A5D1)

    @scena.Lambda('lambda_A5E9')
    def lambda_A5E9():
        OP_67(0, 3720, -10000, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_A5E9)

    @scena.Lambda('lambda_A601')
    def lambda_A601():
        OP_6B(2780, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_A601)

    @scena.Lambda('lambda_A611')
    def lambda_A611():
        OP_6C(5000, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_A611)

    @scena.Lambda('lambda_A621')
    def lambda_A621():
        OP_96(0x00FE, 0x0002E568, 0x00000000, 0x0000F15E, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_A621)

    OP_22(0x00A3, 0x00, 0x64)
    Sleep(10)

    @scena.Lambda('lambda_A649')
    def lambda_A649():
        OP_96(0x00FE, 0x0002D9A6, 0xFFFFFF7E, 0x0000F262, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_A649)

    Sleep(100)

    @scena.Lambda('lambda_A66C')
    def lambda_A66C():
        OP_96(0x00FE, 0x0002E22A, 0xFFFFFF88, 0x0000F636, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A66C)

    OP_22(0x00A3, 0x00, 0x64)
    Sleep(10)

    @scena.Lambda('lambda_A694')
    def lambda_A694():
        OP_96(0x00FE, 0x0002DDC0, 0xFFFFFF06, 0x0000F690, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A694)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrPos(0x001C, 188800, -250, 68950, 0)

    @scena.Lambda('lambda_A6C8')
    def lambda_A6C8():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_A6C8)

    @scena.Lambda('lambda_A6D6')
    def lambda_A6D6():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_A6D6)

    @scena.Lambda('lambda_A6E4')
    def lambda_A6E4():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_A6E4)

    @scena.Lambda('lambda_A6F2')
    def lambda_A6F2():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_A6F2)

    @scena.Lambda('lambda_A700')
    def lambda_A700():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0003, lambda_A700)

    @scena.Lambda('lambda_A70E')
    def lambda_A70E():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0003, lambda_A70E)

    @scena.Lambda('lambda_A71C')
    def lambda_A71C():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0003, lambda_A71C)

    @scena.Lambda('lambda_A72A')
    def lambda_A72A():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0003, lambda_A72A)

    @scena.Lambda('lambda_A738')
    def lambda_A738():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0003, lambda_A738)

    @scena.Lambda('lambda_A746')
    def lambda_A746():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_A746)

    @scena.Lambda('lambda_A754')
    def lambda_A754():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_A754)

    @scena.Lambda('lambda_A762')
    def lambda_A762():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_A762)

    Sleep(600)

    SetChrFlags(0x0010, 0x0010)
    SetChrFlags(0x0011, 0x0010)
    SetChrFlags(0x0012, 0x0010)
    SetChrFlags(0x0013, 0x0010)
    SetChrFlags(0x0014, 0x0010)
    SetChrFlags(0x0015, 0x0010)
    SetChrFlags(0x0010, 0x0040)
    SetChrFlags(0x0011, 0x0040)
    SetChrFlags(0x0012, 0x0040)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0014, 0x0040)
    SetChrFlags(0x0015, 0x0040)

    @scena.Lambda('lambda_A7B1')
    def lambda_A7B1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_A7B1)

    @scena.Lambda('lambda_A7C7')
    def lambda_A7C7():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_A7C7)

    @scena.Lambda('lambda_A7DD')
    def lambda_A7DD():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_A7DD)

    @scena.Lambda('lambda_A7F3')
    def lambda_A7F3():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_A7F3)

    @scena.Lambda('lambda_A809')
    def lambda_A809():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_A809)

    @scena.Lambda('lambda_A81F')
    def lambda_A81F():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_A81F)

    @scena.Lambda('lambda_A835')
    def lambda_A835():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_A835)

    @scena.Lambda('lambda_A84B')
    def lambda_A84B():
        OP_8F(0x00FE, 185590, 0, 72190, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_A84B)

    @scena.Lambda('lambda_A866')
    def lambda_A866():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_A866)

    @scena.Lambda('lambda_A87C')
    def lambda_A87C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_A87C)

    @scena.Lambda('lambda_A892')
    def lambda_A892():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_A892)

    @scena.Lambda('lambda_A8A8')
    def lambda_A8A8():
        OP_8F(0x00FE, 184100, 0, 68710, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_A8A8)

    Sleep(100)

    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x000F, 0x0020)

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000F, 20)
    SetChrSubChip(0x000F, 0)
    SetChrPos(0x000F, 188800, 10000, 68950, 185)
    OP_8F(0x000F, 188800, -350, 68950, 20000, 0x00)

    @scena.Lambda('lambda_A91C')
    def lambda_A91C():
        OP_9E(0x00FE, 0x00000028, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_A91C)

    OP_22(0x0088, 0x00, 0x64)
    OP_7C(0x00000000, 0x000007D0, 0x00002710, 0x00000064)

    @scena.Lambda('lambda_A94C')
    def lambda_A94C():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_A94C)

    @scena.Lambda('lambda_A96A')
    def lambda_A96A():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_A96A)

    @scena.Lambda('lambda_A988')
    def lambda_A988():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_A988)

    @scena.Lambda('lambda_A9A6')
    def lambda_A9A6():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_A9A6)

    @scena.Lambda('lambda_A9C4')
    def lambda_A9C4():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_A9C4)

    @scena.Lambda('lambda_A9E2')
    def lambda_A9E2():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x00000190, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_A9E2)

    @scena.Lambda('lambda_AA00')
    def lambda_AA00():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_AA00)

    @scena.Lambda('lambda_AA1E')
    def lambda_AA1E():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x000000C8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_AA1E)

    @scena.Lambda('lambda_AA3C')
    def lambda_AA3C():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_AA3C)

    @scena.Lambda('lambda_AA5A')
    def lambda_AA5A():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x000000C8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_AA5A)

    @scena.Lambda('lambda_AA78')
    def lambda_AA78():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_AA78)

    @scena.Lambda('lambda_AA96')
    def lambda_AA96():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0x00000000, 0x000000C8, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_AA96)

    Sleep(100)

    PlayEffect(0x02, 0x00, 0x00FF, 187810, -250, 68250, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    OP_82(0x00, 0x02)

    @scena.Lambda('lambda_AAF6')
    def lambda_AAF6():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_AAF6)

    @scena.Lambda('lambda_AB04')
    def lambda_AB04():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_AB04)

    @scena.Lambda('lambda_AB12')
    def lambda_AB12():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_AB12)

    @scena.Lambda('lambda_AB20')
    def lambda_AB20():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_AB20)

    @scena.Lambda('lambda_AB2E')
    def lambda_AB2E():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0003, lambda_AB2E)

    @scena.Lambda('lambda_AB3C')
    def lambda_AB3C():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0003, lambda_AB3C)

    @scena.Lambda('lambda_AB4A')
    def lambda_AB4A():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0003, lambda_AB4A)

    @scena.Lambda('lambda_AB58')
    def lambda_AB58():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0003, lambda_AB58)

    @scena.Lambda('lambda_AB66')
    def lambda_AB66():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0003, lambda_AB66)

    @scena.Lambda('lambda_AB74')
    def lambda_AB74():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_AB74)

    @scena.Lambda('lambda_AB82')
    def lambda_AB82():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_AB82)

    @scena.Lambda('lambda_AB90')
    def lambda_AB90():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_AB90)

    Sleep(1400)

    Fade(100)
    SetChrChipByIndex(0x000F, 18)
    SetChrSubChip(0x000F, 5)
    OP_99(0x000F, 0x05, 0x01, 0x000005DC)
    OP_22(0x011F, 0x00, 0x64)

    @scena.Lambda('lambda_ABC0')
    def lambda_ABC0():
        OP_6D(188840, -250, 68280, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_ABC0)

    @scena.Lambda('lambda_ABD8')
    def lambda_ABD8():
        OP_6B(3180, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_ABD8)

    @scena.Lambda('lambda_ABE8')
    def lambda_ABE8():
        OP_67(0, 4100, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_ABE8)

    OP_7C(0x0000012C, 0x00000000, 0x00001770, 0x000003E8)
    Sleep(1000)

    OP_7C(0x000000C8, 0x00000000, 0x00001194, 0x000003E8)
    Sleep(1000)

    OP_7C(0x00000064, 0x00000000, 0x00000BB8, 0x000003E8)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000F, 18)
    SetChrSubChip(0x000F, 0)
    Sleep(50)

    SetChrChipByIndex(0x000F, 0)
    SetChrSubChip(0x000F, 0)

    @scena.Lambda('lambda_AC64')
    def lambda_AC64():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_AC64')

    DispatchAsync2(0x000F, 0x0000, lambda_AC64)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACA3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351034V#065F#6P啊、哎呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ACA3(): pass

    label('loc_ACA3')

    ChrTalk(
        0x0101,
        (
            '#0010351035V#1005F#6P那、那是什么！',
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
        'loc_AD00',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351036V#550F#6P我怎么知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD00(): pass

    label('loc_AD00')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD40',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351037V#023F#6P这家伙是这个巢穴的主人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD40(): pass

    label('loc_AD40')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AD7C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351038V#070F#6P哈哈，这还真是吓人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD7C(): pass

    label('loc_AD7C')

    ChrTalk(
        0x0102,
        (
            '#0020351039V#1043F#6P先不管它的来历……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020351040V可以肯定的是我们不受它的欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351041V#1020F#6P！？',
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
        'loc_AE33',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351042V#024F#6P艾丝蒂尔，敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEA4')

    def _loc_AE33(): pass

    label('loc_AE33')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE6C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351043V#076F#6P喂，敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEA4')

    def _loc_AE6C(): pass

    label('loc_AE6C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEA4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351044V#054F#6P小心，敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AEA4(): pass

    label('loc_AEA4')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000F, 0x00)
    SetChrChipByIndex(0x000F, 0)
    SetChrSubChip(0x000F, 1)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_AEC6')
    def lambda_AEC6():
        OP_96(0x000F, 0x0002DFC8, 0xFFFFFF06, 0x0000FC80, 0x000005DC, 0x00001B58)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_AEC6)

    @scena.Lambda('lambda_AEE4')
    def lambda_AEE4():
        OP_99(0x00FE, 0x01, 0x03, 0x000005DC)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_AEE4)

    @scena.Lambda('lambda_AEF4')
    def lambda_AEF4():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_AEF4)

    @scena.Lambda('lambda_AF09')
    def lambda_AF09():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_AF09)

    @scena.Lambda('lambda_AF1E')
    def lambda_AF1E():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AF1E)

    @scena.Lambda('lambda_AF33')
    def lambda_AF33():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_AF33)

    @scena.Lambda('lambda_AF48')
    def lambda_AF48():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_AF48)

    @scena.Lambda('lambda_AF5D')
    def lambda_AF5D():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_AF5D)

    @scena.Lambda('lambda_AF72')
    def lambda_AF72():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_AF72)

    @scena.Lambda('lambda_AF87')
    def lambda_AF87():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_AF87)

    @scena.Lambda('lambda_AF9C')
    def lambda_AF9C():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_AF9C)

    @scena.Lambda('lambda_AFB1')
    def lambda_AFB1():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_AFB1)

    @scena.Lambda('lambda_AFC6')
    def lambda_AFC6():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_AFC6)

    @scena.Lambda('lambda_AFDB')
    def lambda_AFDB():
        OP_92(0x00FE, 0x000E, 0x000003E8, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_AFDB)

    Sleep(300)

    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x000E, 0xFF)
    Battle(0x00000EDB, 0x00000000, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_B059'),
        (-1, 'loc_B05E'),
    )

    def _loc_B059(): pass

    label('loc_B059')

    OP_B4(0x00)

    Jump('loc_B05E')

    def _loc_B05E(): pass

    label('loc_B05E')

    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_6D(189040, -250, 72180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_D2(0x0007051E, 0x00070525, 0x05)
    SetChrPos(0x0101, 188750, -150, 63910, 0)
    SetChrPos(0x0102, 187450, -250, 64030, 0)
    SetChrPos(0x00F8, 189850, 0, 63000, 0)
    SetChrPos(0x00F9, 186360, -140, 63140, 0)
    SetChrChipByIndex(0x000E, 5)
    SetChrSubChip(0x000E, 3)
    SetChrPos(0x000E, 187650, 0, 60830, 0)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0015, 0xFF)
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)

    @scena.Lambda('lambda_B18B')
    def lambda_B18B():
        OP_6D(189040, -250, 65180, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_B18B)

    FadeIn(1000, 0)
    WaitForThreadExit(0x000E, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010351045V#1021F#3P干、干掉了……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351046V#1042F#3P嗯……总算。',
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
        'loc_B23D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351047V#561F呼……\n',
            '终、终于结束了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B23D(): pass

    label('loc_B23D')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B29F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351048V#026F魔兽的气息也已经没有了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030351049V好像分出胜负了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B362')

    def _loc_B29F(): pass

    label('loc_B29F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B303',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351050V#070F周围已经没魔兽的气息了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080351051V似乎平安地解决了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B362')

    def _loc_B303(): pass

    label('loc_B303')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B362',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351052V#050F魔兽的气息也已经没有了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050351053V看来胜负已见分晓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B362(): pass

    label('loc_B362')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    OP_22(0x00D5, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351054V#1004F#3P对、对了！\n',
            '利吉先生他！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B3CE')
    def lambda_B3CE():
        OP_6D(188340, 0, 61600, 1500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_B3CE)

    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F8, 0)

    @scena.Lambda('lambda_B3F0')
    def lambda_B3F0():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_B3F0)

    Sleep(50)

    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)

    @scena.Lambda('lambda_B40D')
    def lambda_B40D():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B40D)

    Sleep(50)

    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F9, 0)

    @scena.Lambda('lambda_B42A')
    def lambda_B42A():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_B42A)

    Sleep(700)

    WaitForThreadExit(0x000E, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B48B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351055V#027F没事的……\n',
            '只是因为用尽力气而晕过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4C2')

    def _loc_B48B(): pass

    label('loc_B48B')

    ChrTalk(
        0x0102,
        (
            '#0020351056V#1040F看来是\n',
            '因为用尽力气而晕过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4C2(): pass

    label('loc_B4C2')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B507',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351057V#065F不过，得赶快\n',
            '把他带回城里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5D6')

    def _loc_B507(): pass

    label('loc_B507')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B572',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351058V#070F总之先把他带回城里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080351059V说不定\n',
            '哪里受了内伤也是有可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5D6')

    def _loc_B572(): pass

    label('loc_B572')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5D6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351060V#552F赶快把他带回城里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050351061V总之现在要\n',
            '让他躺在床上休养。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B5D6(): pass

    label('loc_B5D6')

    ChrTalk(
        0x0101,
        (
            '#0010351062V#1000F嗯，说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351063V#1040F那就和矿工们会合后\n',
            '返回地面上吧。',
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
        'loc_B667',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351064V#020F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6CA')

    def _loc_B667(): pass

    label('loc_B667')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B699',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351065V#051F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6CA')

    def _loc_B699(): pass

    label('loc_B699')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6CA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351066V#070F好，回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B6CA(): pass

    label('loc_B6CA')

    FadeOut(2000, 0, -1)
    OP_0D()
    EventBegin(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '因导力停止现象引发的\n',
            '玛鲁加矿山危机\n',
            '就这样顺利平息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(53610, 0, 51680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D2(0x0007051E, 0x00070525, 0x07)
    OP_D2(0x00070109, 0x0007010D, 0x08)
    SetChrChipByIndex(0x000D, 8)
    SetChrPos(0x000A, 53220, 0, 52940, 0)
    SetChrPos(0x000B, 51880, 0, 53800, 0)
    SetChrPos(0x0008, 53210, 0, 54100, 90)
    SetChrPos(0x000D, 55190, 0, 54000, 180)
    SetChrPos(0x000C, 55250, 0, 51960, 0)
    SetChrPos(0x0009, 56100, 0, 52360, 0)
    ChrTurnDirection(0x000C, 0x0009, 0)
    ChrTurnDirection(0x0009, 0x000C, 0)
    ChrTurnDirection(0x000B, 0x000A, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)
    SetChrChipByIndex(0x000E, 7)
    SetChrSubChip(0x000E, 3)
    ClearChrFlags(0x000E, 0x0080)
    SetChrBattleFlags(0x000E, 0x0020)
    OP_6F(0x0001, 55)
    Yield()
    OP_89(0x0101, 54600, -4530, 57510, 180)
    OP_89(0x0102, 53690, -4530, 57700, 0)
    OP_89(0x00F8, 54620, -4530, 56530, 180)
    OP_89(0x00F9, 53370, -4530, 57200, 180)
    OP_89(0x000E, 53400, -4530, 56550, 180)
    FadeIn(2000, 0)
    Sleep(2000)

    CreateThread(0x000D, 0x01, 0x00, 0x002C)
    OP_6D(54140, 0, 54820, 2000)
    Sleep(200)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 65)
    OP_70(0x0001, 0x00000037)
    OP_73(0x0001)
    Sleep(500)

    Sleep(200)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 55)
    OP_70(0x0001, 0x0000002D)
    OP_73(0x0001)
    Sleep(500)

    Sleep(200)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 45)
    OP_70(0x0001, 0x00000023)
    OP_73(0x0001)
    Sleep(500)

    Sleep(200)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 25)
    OP_70(0x0001, 0x0000000F)
    OP_73(0x0001)
    Sleep(500)

    Sleep(200)

    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x0000012C)
    OP_6F(0x0001, 15)
    OP_70(0x0001, 0x00000000)
    OP_73(0x0001)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_63(0x000A)
    OP_63(0x000B)
    OP_63(0x0008)
    OP_63(0x000D)
    OP_63(0x000C)
    OP_63(0x0009)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '与矿工们互相庆祝了平安无事\n',
            '并到达地面之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '为了送利吉先生回城镇，\n',
            '我们和前去汇报事件经过的矿山长一起\n',
            '结伴前往洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0024 offset: 0xBAB2
@scena.Code('func_24_BAB2')
def func_24_BAB2():
    SetChrChipByIndex(0x00FE, 7)

    @scena.Lambda('lambda_BABD')
    def lambda_BABD():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_BABD)

    @scena.Lambda('lambda_BACD')
    def lambda_BACD():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_BACD)

    Sleep(500)

    PlayEffect(0x01, 0xFF, 0x000E, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_BB22')
    def lambda_BB22():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_BB22)

    SetChrChipByIndex(0x00FE, 2)

    Return()

# id: 0x0025 offset: 0xBB38
@scena.Code('func_25_BB38')
def func_25_BB38():
    SetChrChipByIndex(0x00FE, 7)

    @scena.Lambda('lambda_BB43')
    def lambda_BB43():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_BB43)

    @scena.Lambda('lambda_BB53')
    def lambda_BB53():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_BB53)

    Sleep(500)

    PlayEffect(0x01, 0xFF, 0x000E, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x000E, 0x01, 0x00, 0x0026)
    WaitForThreadExit(0x00FE, 0x0002)

    @scena.Lambda('lambda_BBAF')
    def lambda_BBAF():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_BBAF)

    SetChrChipByIndex(0x00FE, 2)

    Return()

# id: 0x0026 offset: 0xBBC5
@scena.Code('func_26_BBC5')
def func_26_BBC5():
    OP_6A(0x000E)
    SetChrChipByIndex(0x000E, 4)
    SetChrPos(0x001C, 188900, -250, 69050, 0)
    OP_96(0x00FE, 0x0002DD02, 0x00000000, 0x0000ED9E, 0x000001F4, 0x00001388)
    OP_9E(0x00FE, 0x00000096, 0x00000000, 0x00000190, 0x00000FA0)
    SetChrChipByIndex(0x000E, 5)
    SetChrSubChip(0x00FE, 3)
    OP_6A(0x00FF)

    Return()

# id: 0x0027 offset: 0xBC16
@scena.Code('func_27_BC16')
def func_27_BC16():
    OP_8E(0x00FE, 185490, 60, 60360, 5000, 0x00)
    OP_8E(0x00FE, 188970, -120, 64030, 5000, 0x00)
    OP_22(0x00D5, 0x00, 0x64)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0028 offset: 0xBC4B
@scena.Code('func_28_BC4B')
def func_28_BC4B():
    OP_8E(0x00FE, 185490, 60, 60360, 5000, 0x00)
    OP_8E(0x00FE, 187840, -250, 64120, 5000, 0x00)
    OP_22(0x00D5, 0x00, 0x64)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0029 offset: 0xBC80
@scena.Code('func_29_BC80')
def func_29_BC80():
    OP_8E(0x00FE, 185490, 60, 60360, 5000, 0x00)
    OP_8E(0x00FE, 189500, 0, 62790, 5000, 0x00)
    OP_22(0x00D5, 0x00, 0x64)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x002A offset: 0xBCB5
@scena.Code('func_2A_BCB5')
def func_2A_BCB5():
    OP_8E(0x00FE, 185490, 60, 60360, 5000, 0x00)
    OP_8E(0x00FE, 186790, -130, 63050, 5000, 0x00)
    OP_22(0x00D5, 0x00, 0x64)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x002B offset: 0xBCEA
@scena.Code('func_2B_BCEA')
def func_2B_BCEA():
    OP_6D(187810, -40, 61790, 1500)
    OP_6D(188510, -100, 63310, 2000)

    Return()

# id: 0x002C offset: 0xBD0D
@scena.Code('func_2C_BD0D')
def func_2C_BD0D():
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    OP_4A(0x000D, 0)
    OP_8C(0x000D, 0, 400)
    Sleep(400)

    @scena.Lambda('lambda_BD3A')
    def lambda_BD3A():
        OP_8C(0x000A, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_BD3A)

    @scena.Lambda('lambda_BD48')
    def lambda_BD48():
        OP_8C(0x000B, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_BD48)

    Sleep(400)

    @scena.Lambda('lambda_BD5B')
    def lambda_BD5B():
        OP_8C(0x0008, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_BD5B)

    @scena.Lambda('lambda_BD69')
    def lambda_BD69():
        OP_8C(0x000C, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_BD69)

    Sleep(400)

    @scena.Lambda('lambda_BD7C')
    def lambda_BD7C():
        OP_8C(0x0009, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_BD7C)

    Return()

# id: 0x002D offset: 0xBD85
@scena.Code('func_2D_BD85')
def func_2D_BD85():
    SetMapFlags(0x00000080)
    Sleep(30)

    OP_22(0x0064, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BDB3',
    )

    OP_70(0x0003, 0x00000019)
    OP_73(0x0003)
    OP_6F(0x0003, 25)
    OP_A2(0x0009)

    Jump('loc_BDC7')

    def _loc_BDB3(): pass

    label('loc_BDB3')

    OP_70(0x0003, 0x00000000)
    OP_73(0x0003)
    OP_6F(0x0003, 0)
    OP_A3(0x0009)

    def _loc_BDC7(): pass

    label('loc_BDC7')

    OP_73(0x0003)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '动了控制杆也没有反应。\n',
            '看来是导力断绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ClearMapFlags(0x00000080)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
