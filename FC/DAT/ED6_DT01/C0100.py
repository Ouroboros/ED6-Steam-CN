import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0100.x'
    header.mapIndex       = 14
    header.bgm            = 30
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
            dword_00        = 0x000061A8,
            dword_04        = 0x00000000,
            dword_08        = 0x00002328,
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
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 14,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x000061A8,
            dword_04        = 0x00000000,
            dword_08        = 0x00002328,
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
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 14,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10000._CH', 'ED6_DT09/CH10000P._CP'),
        ('ED6_DT09/CH10001._CH', 'ED6_DT09/CH10001P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT06/CH20034._CH', 'ED6_DT06/CH20034P._CP'),
    ]

# id: 0x10001 offset: 0x136
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '矿工迈尔德',
            x                   = 22500,
            z                   = 1000,
            y                   = 65840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '矿工兰古',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '见习矿工',
            x                   = 96890,
            z                   = 1000,
            y                   = 91220,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '矿工彭兹',
            x                   = 130850,
            z                   = 1000,
            y                   = 13900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '矿工提恩特',
            x                   = 126070,
            z                   = 500,
            y                   = 13270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '矿工皮尔姆',
            x                   = 83580,
            z                   = 1000,
            y                   = 33130,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '矿工海涅',
            x                   = 83760,
            z                   = 1000,
            y                   = 31300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '加通老大',
            x                   = 84600,
            z                   = 0,
            y                   = 14100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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

# id: 0x10002 offset: 0x316
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '嗜杀巨蟹',
            x           = 114000,
            z           = -500,
            y           = 80000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '嗜杀巨蟹',
            x           = 108000,
            z           = 0,
            y           = 54000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0058,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '嗜杀巨蟹',
            x           = 109000,
            z           = 0,
            y           = 35000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0056,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '嗜杀巨蟹',
            x           = 105000,
            z           = 0,
            y           = 16000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x81,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0057,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x386
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 104400,
            y           = -1000,
            z           = 68900,
            range       = 109400,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000FF14,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = 92200,
            y           = -1000,
            z           = 63230,
            range       = 4000,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = 90100,
            y           = -1000,
            z           = 72400,
            range       = 97800,
            dword_10    = 0x000003E8,
            dword_14    = 0x00010F4A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 123500,
            y           = -1000,
            z           = 27100,
            range       = 132000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00007E2B,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 126240,
            y           = -1000,
            z           = 15000,
            range       = 131400,
            dword_10    = 0x000007D0,
            dword_14    = 0x00002A94,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 92900,
            y           = -1000,
            z           = 33340,
            range       = 97970,
            dword_10    = 0x000003E8,
            dword_14    = 0x00005762,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 84730,
            y           = 1000,
            z           = 31370,
            range       = 88770,
            dword_10    = 0xFFFFFF9C,
            dword_14    = 0x00008444,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
    )

# id: 0x10004 offset: 0x466
@scena.ActorData('ActorData')
def ActorData():
    return (
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
            talkFunctionIndex   = 0x0021,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16000,
            triggerZ            = 1000,
            triggerY            = 32000,
            triggerRange        = 1500,
            actorX              = 16000,
            actorZ              = 1000,
            actorY              = 32000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 35000,
            triggerZ            = 1000,
            triggerY            = 59500,
            triggerRange        = 1500,
            actorX              = 35000,
            actorZ              = 1000,
            actorY              = 59500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 50500,
            triggerZ            = 1000,
            triggerY            = 50000,
            triggerRange        = 1500,
            actorX              = 50500,
            actorZ              = 1000,
            actorY              = 50000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
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
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 129000,
            triggerZ            = 500,
            triggerY            = 78200,
            triggerRange        = 600,
            actorX              = 129000,
            actorZ              = 500,
            actorY              = 78200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 104800,
            triggerZ            = 0,
            triggerY            = 39740,
            triggerRange        = 1000,
            actorX              = 104800,
            actorZ              = 1000,
            actorY              = 39740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x562
@scena.Code('Init')
def Init():
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0015, 0x0040)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_594'),
        (0x00000064, 'loc_59B'),
        (0x00000065, 'loc_59E'),
        (-1, 'loc_5A1'),
    )

    def _loc_594(): pass

    label('loc_594')

    Event(0, func_0F_2F85)

    Jump('loc_5A1')

    def _loc_59B(): pass

    label('loc_59B')

    Jump('loc_5A1')

    def _loc_59E(): pass

    label('loc_59E')

    Jump('loc_5A1')

    def _loc_5A1(): pass

    label('loc_5A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_5FD',
    )

    ChrSetPos(0x000F, 14160, 0, 12750, 225)
    ChrSetPos(0x000B, 39350, 0, 26280, 0)
    ChrSetPos(0x000C, 24110, -40, 15950, 0)
    ChrSetPos(0x000D, 10800, 0, 29530, 0)
    ChrSetPos(0x000E, 54240, 0, 53990, 0)

    def _loc_5FD(): pass

    label('loc_5FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_60E',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    def _loc_60E(): pass

    label('loc_60E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_61F',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)

    def _loc_61F(): pass

    label('loc_61F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Return()

# id: 0x0001 offset: 0x629
@scena.Code('func_01_629')
def func_01_629():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_63A',
    )

    OP_6F(0x0000, 0)

    Jump('loc_659')

    def _loc_63A(): pass

    label('loc_63A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_64B',
    )

    OP_6F(0x0000, 330)

    Jump('loc_659')

    def _loc_64B(): pass

    label('loc_64B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_659',
    )

    OP_6F(0x0000, 900)

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_66A',
    )

    OP_6F(0x0003, 25)

    Jump('loc_671')

    def _loc_66A(): pass

    label('loc_66A')

    OP_6F(0x0003, 0)

    def _loc_671(): pass

    label('loc_671')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6C6',
    )

    LoadEffect(0x00, 'map\\\\mp002_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 1000)

    def _loc_6C6(): pass

    label('loc_6C6')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x710
@scena.Code('func_02_710')
def func_02_710():
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
        'loc_735',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_877')

    def _loc_735(): pass

    label('loc_735')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_877')

    def _loc_74E(): pass

    label('loc_74E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_767',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_877')

    def _loc_767(): pass

    label('loc_767')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_780',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_877')

    def _loc_780(): pass

    label('loc_780')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_799',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_877')

    def _loc_799(): pass

    label('loc_799')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_877')

    def _loc_7B2(): pass

    label('loc_7B2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CB',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_877')

    def _loc_7CB(): pass

    label('loc_7CB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_877')

    def _loc_7E4(): pass

    label('loc_7E4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7FD',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_877')

    def _loc_7FD(): pass

    label('loc_7FD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_816',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_877')

    def _loc_816(): pass

    label('loc_816')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_877')

    def _loc_82F(): pass

    label('loc_82F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_848',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_877')

    def _loc_848(): pass

    label('loc_848')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_861',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_877')

    def _loc_861(): pass

    label('loc_861')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_877',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_877(): pass

    label('loc_877')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_88C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_877')

    def _loc_88C(): pass

    label('loc_88C')

    Return()

# id: 0x0003 offset: 0x88D
@scena.Code('func_03_88D')
def func_03_88D():
    Return()

# id: 0x0004 offset: 0x88E
@scena.Code('func_04_88E')
def func_04_88E():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000A,
        (
            '哇！吓我一跳～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦，找我们老大呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我想老大应该在\n',
            '过桥后更里面的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_935')

    def _loc_8F4(): pass

    label('loc_8F4')

    ChrTalk(
        0x000A,
        (
            '哦，找我们老大呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我想老大应该在\n',
            '过桥后更里面的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_935(): pass

    label('loc_935')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x939
@scena.Code('func_05_939')
def func_05_939():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_994',
    )

    ChrTalk(
        0x000B,
        (
            '我们把魔兽的巢穴\n',
            '用炸药来堵住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这下又能够继续工作，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACA')

    def _loc_994(): pass

    label('loc_994')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_9E5',
    )

    ChrTalk(
        0x000B,
        (
            '提恩特那家伙又不在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '准是又翘班了，\n',
            '溜到洛连特那里吃东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACA')

    def _loc_9E5(): pass

    label('loc_9E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_A41',
    )

    ChrTalk(
        0x000B,
        (
            '老大已经很久\n',
            '没回家好好休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '家人肯定在等着他回去吧。\n',
            '应该不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACA')

    def _loc_A41(): pass

    label('loc_A41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_A80',
    )

    ChrTalk(
        0x000B,
        (
            '我们暂时不能往下挖掘了，\n',
            '这里的工作也要暂停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACA')

    def _loc_A80(): pass

    label('loc_A80')

    ChrTalk(
        0x000B,
        (
            '提恩特那家伙\n',
            '好像又旷工翘班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '明明之前\n',
            '老大已经对他发过火了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ACA(): pass

    label('loc_ACA')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0xACE
@scena.Code('func_06_ACE')
def func_06_ACE():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_AF9',
    )

    ChrTalk(
        0x000C,
        (
            '我本来应该在洛连特的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C10')

    def _loc_AF9(): pass

    label('loc_AF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_B21',
    )

    ChrTalk(
        0x000C,
        (
            '我本来应该在洛连特的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C10')

    def _loc_B21(): pass

    label('loc_B21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_B77',
    )

    ChrTalk(
        0x000C,
        (
            '哈～好饿啊，\n',
            '已经达到极限了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '搞定这些活儿，\n',
            '我就去好好吃一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C10')

    def _loc_B77(): pass

    label('loc_B77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_BB6',
    )

    ChrTalk(
        0x000C,
        (
            '啊～好倒霉呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这下我的肚子\n',
            '真的是饿扁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C10')

    def _loc_BB6(): pass

    label('loc_BB6')

    ChrTalk(
        0x000C,
        (
            '唔，明明吃了很多了，\n',
            '可一会儿又开始饿了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '再旷一会儿工，\n',
            '到城里去吃些东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C10(): pass

    label('loc_C10')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0xC14
@scena.Code('func_07_C14')
def func_07_C14():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_C85',
    )

    ChrTalk(
        0x000D,
        (
            '呼呼，工作告一段落，\n',
            '要去教会祈祷一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '因为最近忙于工作，\n',
            '好久都没有去礼拜堂祈祷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DFE')

    def _loc_C85(): pass

    label('loc_C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_CBC',
    )

    ChrTalk(
        0x000D,
        (
            '老大果然打算用炸药\n',
            '来封住魔兽的巢穴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DFE')

    def _loc_CBC(): pass

    label('loc_CBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_D58',
    )

    ChrTalk(
        0x000D,
        (
            '崩塌之前我们\n',
            '在新的矿脉挖了很多东西，\n',
            '虽说现在矿山还有不少的储备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过不早点到下层\n',
            '看看情况的话，\n',
            '说不定那些挖出来的东西都没有了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DFE')

    def _loc_D58(): pass

    label('loc_D58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_DB0',
    )

    ChrTalk(
        0x000D,
        (
            '呼，\n',
            '我刚才还以为死定了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '回到镇里后一定\n',
            '要去礼拜堂向女神作祷告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DFE')

    def _loc_DB0(): pass

    label('loc_DB0')

    ChrTalk(
        0x000D,
        (
            '因为，\n',
            '我们能这么顺利地作业，\n',
            '也是受到女神的指引的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '要感谢女神呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DFE(): pass

    label('loc_DFE')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0xE02
@scena.Code('func_08_E02')
def func_08_E02():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_E77',
    )

    ChrTalk(
        0x000E,
        (
            '导力梯已经不能再用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然魔兽已经没有什么动静了，\n',
            '不过为了安全起见，\n',
            '还是要先看看情况才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA6')

    def _loc_E77(): pass

    label('loc_E77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_EE8',
    )

    ChrTalk(
        0x000E,
        (
            '巢穴被堵起来的话就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '必须得找人\n',
            '到下面一层去看看才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '让谁去做这样的事情好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA6')

    def _loc_EE8(): pass

    label('loc_EE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_F3D',
    )

    ChrTalk(
        0x000E,
        (
            '下层还有魔兽在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '得早点把它们收拾掉，\n',
            '或者把它们封锁起来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA6')

    def _loc_F3D(): pass

    label('loc_F3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_F81',
    )

    ChrTalk(
        0x000E,
        (
            '下面的楼层已经暂时被封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '因为魔兽很危险呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA6')

    def _loc_F81(): pass

    label('loc_F81')

    ChrTalk(
        0x000E,
        (
            '在找老大吗？\n',
            '他刚刚还在这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FA6(): pass

    label('loc_FA6')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0xFAA
@scena.Code('func_09_FAA')
def func_09_FAA():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_FD9',
    )

    ChrTalk(
        0x000F,
        (
            '现在应该在洛连特自己家里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2349')

    def _loc_FD9(): pass

    label('loc_FD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1041',
    )

    ChrTalk(
        0x000F,
        (
            '现在也唯有\n',
            '将魔兽的巢穴埋掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这并不是说放弃新矿脉。\n',
            '这次给游击士添了很多麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2349')

    def _loc_1041(): pass

    label('loc_1041')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_10C4',
    )

    ChrTalk(
        0x000F,
        (
            '崩塌的时候\n',
            '逃出来的新矿工\n',
            '好像再也没有回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '毕竟一来就遇到那样的事情。\n',
            '虽然有点遗憾，不过也不能勉强别人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2349')

    def _loc_10C4(): pass

    label('loc_10C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_1133',
    )

    ChrTalk(
        0x000F,
        (
            '这次真是不好意思。\n',
            '给你们添了这么多的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '不过真奇怪，\n',
            '那里的岩盘不应该\n',
            '那么脆弱的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2349')

    def _loc_1133(): pass

    label('loc_1133')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2349',
    )

    SetScenaFlags(ScenaFlag(0x0048, 2, 0x242))
    OP_28(0x0003, 0x01, 0x0040)
    OP_28(0x0003, 0x01, 0x0080)
    MapClearFlags(0x00000001)
    Fade(1000)
    EventBegin(0x00)
    FormationAddMember(0x32, 0xFF)
    ChrSetFlags(0x0133, 0x0080)
    ChrSetPos(0x0102, 85400, 0, 12650, 0)
    ChrSetPos(0x0101, 84250, 0, 12500, 0)
    OP_6C(315000, 0)
    ChrTurnDirection(0x000F, 0x0101, 0)
    ChrSetSubChip(0x000F, 0)
    CameraMove(84460, 0, 13210, 1000)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#0940010125V哎？小姑娘你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010126V#000F叔叔你就是矿长先生吗？\n',
            '太好了，终于找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010127V#010F我们是游击士协会的人，\n',
            '受克劳斯市长委托而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '把',
            (TxtCtl.SetColor, 0x2),
            '市长的介绍信',
            (TxtCtl.SetColor, 0x0),
            '交给了加通矿长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0321, 1)

    ChrTalk(
        0x000F,
        (
            '#0940010128V哦，原来如此。\n',
            '你们是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010129V小小年纪就当游击士可真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010130V#506F嘿嘿，过奖了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010131V#006F对了……结晶在什么地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010132V啊，稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010133V这毕竟是不能\n',
            '随便给别人看见的贵重物品嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010134V还是贴身保管比较安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '矿长从怀中取出大颗的结晶。',
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    PlaySE(128, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x000F, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010010135V#004F哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010136V#001F这么大的结晶，以前都没见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010137V#014F好厉害……\n',
            '像是从深处发出光芒一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010138V这个就是七耀石的其中一种，\n',
            '蕴含着风之力量的翠耀石结晶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010139V这么大块的结晶，\n',
            '作为宝石来讲有着很高的价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010140V你们一定要安全地送到市长那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010141V#002F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000F, 0x0101, 1000, 1000, 0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    ChrSetChipByIndex(0x0101, 8)
    StopEffect(0x00, 0x00)
    PlayEffect(0x00, 0x00, 0x0101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '七耀石的结晶',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0323, 1)
    ChrMoveTo(0x000F, 84600, 0, 14100, 1000, 0x00)
    CameraMove(84250, -500, 12500, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010010142V#008F哇～……真漂亮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010143V感觉就像捧着妖精一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    OP_69(0x0101, 1000)
    OP_6A(0x0101)
    MapSetFlags(0x00000001)
    OP_97(0x0101, 84250, 10750, -60000, 2000, 0x0001)

    @scena.Lambda('lambda_1755')
    def lambda_1755():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1755)

    OP_97(0x0101, 84250, 10750, -30000, 3000, 0x0001)
    OP_97(0x0101, 83500, 10750, -360000, 4000, 0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    CreateThread(0x0101, 0x01, 0x00, func_0A_234D)

    ChrTalk(
        0x0101,
        (
            '#0010010144V#001F啊哈，真有趣～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010145V#001F快看快看，约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    OP_6A(0x0000)
    MapClearFlags(0x00000001)
    CameraMove(84000, 0, 13440, 2000)

    ChrTalk(
        0x0102,
        (
            '#0020010146V#015F确实很漂亮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010147V#010F我劝你还是赶快停下来比较好。\n',
            '万一弄掉了就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010010148V#007F啧。\n',
            '真没劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 84250, 0, 12500, 1500, 0x00)
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0102, 0x0101, 0)
    Sleep(1000)

    StopEffect(0x00, 0x02)
    ChrSetChipByIndex(0x0101, 65535)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把结晶收在怀里。',
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010149V#006F这样就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010150V#006F那么，老大叔叔，\n',
            '我们会把它安全地送到市长那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010151V哦，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1100)

    ChrSetDirection(0x000F, 135, 400)

    ChrTalk(
        0x000F,
        (
            '#0940010152V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010153V#000F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010154V……奇怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010155V空气的流向好像有点不对劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010156V#004F空气的流向……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010157V#012F（这种感觉是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    CreateThread(0x0101, 0x01, 0x00, func_0D_23EC)
    PlaySE(133, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0940010158V哇！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010159V#504F呀啊～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 180, 400)
    ChrSetDirection(0x0101, 315, 400)
    ChrSetDirection(0x0101, 45, 400)
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010160V#012F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_24(0x0085, 0x5A)
    Sleep(200)

    OP_24(0x0085, 0x50)
    Sleep(200)

    OP_24(0x0085, 0x46)
    Sleep(200)

    OP_24(0x0085, 0x3C)
    Sleep(200)

    OP_24(0x0085, 0x32)
    Sleep(200)

    OP_24(0x0085, 0x28)
    Sleep(200)

    OP_24(0x0085, 0x1E)
    Sleep(200)

    OP_24(0x0085, 0x14)
    Sleep(200)

    OP_24(0x0085, 0x0A)
    Sleep(200)

    OP_23(0x0085)
    Sleep(200)

    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010161V#007F好、好像停下来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010162V#002F刚才不会是地震吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0940010163V不是……\n',
            '应该是坑道哪里发生了崩塌吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010164V是地基松软的地方受到了冲击吗？\n',
            '不赶快到现场确认情况的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0010, 92200, 0, 10100, 0)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetChipByIndex(0x0102, 7)
    ChrSetDirection(0x0102, 135, 800)

    ChrTalk(
        0x0102,
        (
            '#0020010165V#016F艾丝蒂尔，小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 800)

    ChrTalk(
        0x0101,
        (
            '#0010010166V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 6)

    @scena.Lambda('lambda_1D56')
    def lambda_1D56():
        CameraMove(91250, 0, 7500, 2600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D56)

    @scena.Lambda('lambda_1D6E')
    def lambda_1D6E():
        CameraSetDistance(2000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D6E)

    ChrWalkTo(0x0010, 88300, 0, 10500, 7000, 0x00)
    OP_92(0x0010, 0x0101, 2000, 10000, 0x00)
    TerminateThread(0x0101, 0xFF)
    Battle(0x00000384, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1DB7'),
        (-1, 'loc_1DBC'),
    )

    def _loc_1DB7(): pass

    label('loc_1DB7')

    OP_B4(0x00)

    Jump('loc_1DBC')

    def _loc_1DBC(): pass

    label('loc_1DBC')

    EventBegin(0x00)
    FadeIn(1000, 0)
    ChrSetFlags(0x0010, 0x0080)
    CameraSetDistance(2800, 0)
    CameraMove(84460, 0, 13210, 0)
    ChrSetPos(0x0101, 85400, 0, 12650, 0)
    ChrSetPos(0x0102, 86100, -500, 13380, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x000F, 0x0101, 0)
    ChrTurnDirection(0x0101, 0x000F, 0)
    ChrTurnDirection(0x0102, 0x000F, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010010167V#580F为、为什么会有魔兽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010168V矿长叔叔，这里也会出现魔兽吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010169V在这么深的地方出现还是头一次！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010170V魔兽对七耀石的光芒非常敏感，\n',
            '被吸引过来也不奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010171V以前也曾有一些魔兽闯进来，\n',
            '不过都只徘徊在入口附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010172V#012F难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010173V刚才的崩塌，\n',
            '把坑道的一部分和魔兽的巢穴连在了一起？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010174V#005F魔、魔兽的巢穴～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010175V不能排除这种可能性……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010176V这、这下糟了。\n',
            '要赶快通知弟兄们逃出去才行啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010177V#002F这种事情就交给我们吧！\n',
            '我们也来帮忙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010178V什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010179V#006F打倒魔兽对我们来说只是小事一桩。\n',
            '现在要分秒必争，就别考虑那么多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010180V抱歉……就拜托你们帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010181V#012F顺便问一下，\n',
            '这里的矿工一共有多少人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010182V在地下工作的……\n',
            '应该是四个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010183V#005F明白了，赶快去救他们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010184V麻烦你们了……\n',
            '啊，对了，必要的时候用这东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了２个',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(0x01F5, 2)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    LoadEffect(0x00, 'map\\\\mp002_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0011, 85530, 1000, 32350, 270)
    ChrSetPos(0x0012, 128360, 1000, 12900, 180)
    ChrSetPos(0x0013, 92200, 0, 63230, 225)
    ChrSetPos(0x0014, 92600, 0, 62100, 270)
    ChrSetPos(0x0015, 90800, 0, 63630, 180)
    ChrSetDirection(0x000A, 225, 0)
    ChrSetDirection(0x000B, 225, 0)
    ChrSetDirection(0x000D, 225, 0)
    ChrSetDirection(0x000D, 90, 0)
    ChrSetDirection(0x000E, 90, 0)
    ChrSetFlags(0x000F, 0x0040)

    @scena.Lambda('lambda_2329')
    def lambda_2329():
        OP_92(0x00FE, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2329)

    EventEnd(0x00)
    ChrClearFlags(0x0133, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0008)

    def _loc_2349(): pass

    label('loc_2349')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x234D
@scena.Code('func_0A_234D')
def func_0A_234D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_236C',
    )

    OP_97(0x0101, 83500, 10750, -90000, 4000, 0x0001)

    Jump('func_0A_234D')

    def _loc_236C(): pass

    label('loc_236C')

    OP_97(0x0101, 83500, 10750, -90000, 4000, 0x0001)
    OP_97(0x0101, 83500, 10750, -80000, 3000, 0x0001)
    OP_97(0x0101, 83500, 10750, -70000, 2000, 0x0001)
    OP_97(0x0101, 83500, 10750, -30000, 1000, 0x0001)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000B offset: 0x23D0
@scena.Code('func_0B_23D0')
def func_0B_23D0():
    CameraMove(91250, 0, 7500, 2600)

    Return()

# id: 0x000C offset: 0x23E2
@scena.Code('func_0C_23E2')
def func_0C_23E2():
    CameraSetDistance(200, 1500)

    Return()

# id: 0x000D offset: 0x23EC
@scena.Code('func_0D_23EC')
def func_0D_23EC():
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    def _loc_24B8(): pass

    label('loc_24B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_24E4',
    )

    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 400, 13440, 20)

    Jump('loc_24B8')

    def _loc_24E4(): pass

    label('loc_24E4')

    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 300, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 200, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)
    CameraMove(84000, 100, 13440, 20)
    CameraMove(84000, 0, 13440, 20)

    Return()

# id: 0x000E offset: 0x2804
@scena.Code('func_0E_2804')
def func_0E_2804():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_28BA',
    )

    ChrTalk(
        0x0008,
        (
            '老大自己到下层去\n',
            '用炸药把魔兽的巢穴给封住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们即使跟着他也不能帮上什么，\n',
            '说不定还会帮倒忙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不愧是加通老大啊。\n',
            '再也没有比他更有男子气概的矿工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F81')

    def _loc_28BA(): pass

    label('loc_28BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_2904',
    )

    ChrTalk(
        0x0008,
        (
            '呼呼，这里也已经采掘完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望下层的作业能早点重开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F81')

    def _loc_2904(): pass

    label('loc_2904')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 0, 0x250)),
            Expr.Return,
        ),
        'loc_2972',
    )

    ChrTalk(
        0x0008,
        (
            '好不容易找到了新的矿脉，\n',
            '没想到还没有挖了多久就崩塌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望能早点\n',
            '回到下层去作业就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F81')

    def _loc_2972(): pass

    label('loc_2972')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_29D0',
    )

    ChrTalk(
        0x0008,
        (
            '我听到脚下有地响的时候\n',
            '可真是吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '老大和大家都没事，\n',
            '实在是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F81')

    def _loc_29D0(): pass

    label('loc_29D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 6, 0x23E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D71',
    )

    EventBegin(0x00)
    OP_69(0x0008, 1000)
    SetScenaFlags(ScenaFlag(0x0047, 6, 0x23E))

    ChrTalk(
        0x0008,
        (
            '#0930010097V呀？你们……\n',
            '为什么会在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010098V是哪个矿工的熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010099V#000F不是呢。我们是受市长的委托，\n',
            '来这儿找矿长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010100V啊，是为了结晶的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010101V矿长应该在地下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010102V另一边尽头处有一部导力梯，\n',
            '可以通到地下去的。\n',
            '你们自己坐矿车到导力梯那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 0, 0x240)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C08',
    )

    ChrTalk(
        0x0101,
        (
            '#0010010103V#004F另一边的尽头？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010104V你们乘矿车过来的时候\n',
            '没看到有条岔路吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010105V导力梯就在\n',
            '那条岔路的终点处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010106V在矿车出发点有一个控制杆，\n',
            '把它推一下就可以切换终点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D6C')

    def _loc_2C08(): pass

    label('loc_2C08')

    SetScenaFlags(ScenaFlag(0x0047, 7, 0x23F))
    OP_28(0x0003, 0x01, 0x0020)

    ChrTalk(
        0x0101,
        (
            '#0010010107V#002F我们找到那部导力梯了，\n',
            '可是不知道怎么让它动起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010108V#002F你可以帮帮我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010109V是这样吗……\n',
            '对了，要有启动开关的钥匙才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010110V没办法，先借给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '借来了',
            (TxtCtl.SetColor, 0x2),
            '导力梯的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0322, 1)

    ChrTalk(
        0x0101,
        (
            '#0010010111V#001F谢谢矿工叔叔，\n',
            '用完之后就还你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D6C(): pass

    label('loc_2D6C')

    EventEnd(0x01)

    Jump('loc_2F81')

    def _loc_2D71(): pass

    label('loc_2D71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 7, 0x23F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 0, 0x240)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EA1',
    )

    EventBegin(0x00)
    OP_69(0x0008, 1000)
    SetScenaFlags(ScenaFlag(0x0047, 7, 0x23F))
    OP_28(0x0003, 0x01, 0x0020)

    ChrTalk(
        0x0008,
        (
            '#0930010112V啊？\n',
            '导力梯不能动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010113V是这样吗……\n',
            '要有启动开关的钥匙才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0930010114V没办法，先借给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '借来了',
            (TxtCtl.SetColor, 0x2),
            '导力梯的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0322, 1)

    ChrTalk(
        0x0101,
        (
            '#0010010115V#001F谢谢矿工叔叔，\n',
            '用完之后就还你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_2F81')

    def _loc_2EA1(): pass

    label('loc_2EA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 7, 0x23F)),
            Expr.Return,
        ),
        'loc_2EF4',
    )

    ChrTalk(
        0x0008,
        (
            '把钥匙插进开关里面，\n',
            '导力梯就可以用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '用完之后还给我就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F81')

    def _loc_2EF4(): pass

    label('loc_2EF4')

    ChrTalk(
        0x0008,
        (
            '你们乘矿车过来的时候\n',
            '没看到有条岔路吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '导力梯就在\n',
            '那条岔路的终点处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在矿车出发点有一个控制杆，\n',
            '把它推一下就可以切换终点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F81(): pass

    label('loc_2F81')

    TalkEnd(0x0008)

    Return()

# id: 0x000F offset: 0x2F85
@scena.Code('func_0F_2F85')
def func_0F_2F85():
    EventBegin(0x00)
    ChrSetPos(0x000F, 27100, -500, 13125, 180)
    ChrSetPos(0x0101, 26230, 0, 10530, 0)
    ChrSetPos(0x0102, 27600, 0, 10640, 0)
    ChrSetPos(0x000B, 39350, 0, 26280, 0)
    ChrSetPos(0x000C, 24110, -40, 15950, 0)
    ChrSetPos(0x000D, 10800, 0, 29530, 0)
    ChrSetPos(0x000E, 54240, 0, 53990, 0)
    RemoveItem(0x0322, 1)
    OP_4A(0x000F, 0)
    MapClearFlags(0x00000001)
    OP_69(0x0101, 0)

    ChrTalk(
        0x000F,
        (
            '#0940010260V这次真是不好意思。\n',
            '给你们添了这么多的麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010261V之后我会和协会进行联络，\n',
            '好好答谢你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010262V#000F哈哈，别客气啦。\n',
            '我们只是做了该做的事情而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010263V#000F这也算是一种修练吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010264V#010F对了……\n',
            '地下坑道打算怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010265V我们自己想办法处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010266V可以尝试用炸药\n',
            '把那个魔兽的巢穴封住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010267V不过，如果实在有困难，\n',
            '说不定还会请你们协会帮忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010268V#006F嗯，到时候就交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010269V#006F那么，\n',
            '我们就把结晶带回去给市长爷爷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010270V#010F艾丝蒂尔……\n',
            '没有把它弄丢吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010271V#007F你、你这什么意思啊？\n',
            '我才不会那么粗心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010272V#007F你看，在这儿呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010273V#007F…………………………\n',
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0102,
        (
            '#0020010274V#018F不、不会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010275V丢、丢了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    PlaySE(128, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x0101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetChipByIndex(0x0101, 8)
    ChrSetDirection(0x0101, 180, 500)
    ChrSetDirection(0x0101, 270, 500)
    ChrSetDirection(0x0101, 0, 500)
    ChrSetDirection(0x0101, 90, 500)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010276V#001F才不会呢⊙\n',
            '它还乖乖地藏在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010277V#001F好了，赶快把它送回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    StopEffect(0x00, 0x02)
    OP_84(0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020010278V#017F我说你真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0940010279V我的心脏差点受不了啊，小姑娘……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x00400000)
    OP_4B(0x000F, 0)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x350E
@scena.Code('func_10_350E')
def func_10_350E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 2, 0x24A)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 5, 0x24D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3660',
    )

    MapSetFlags(0x08000000)
    SetScenaFlags(ScenaFlag(0x0049, 2, 0x24A))
    SetScenaFlags(ScenaFlag(0x0049, 5, 0x24D))
    OP_62(0x0133, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetPos(0x000A, 90000, 0, 61740, 90)
    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrTurnDirection(0x0102, 0x000A, 0)
    ChrTurnDirection(0x0133, 0x000A, 0)
    EventBegin(0x00)

    ChrTalk(
        0x000A,
        (
            '#0990010215V嘿咿——！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010216V怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010217V救命啊～～～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 0, 0x248)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 5, 0x245)),
            Expr.Ez,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_360B',
    )

    Jump('loc_3659')

    def _loc_360B(): pass

    label('loc_360B')

    ChrTalk(
        0x0133,
        (
            '#0940010218V什么！\n',
            '还有其他人在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010219V#002F赶快去救他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3659(): pass

    label('loc_3659')

    EventEnd(0x01)
    MapClearFlags(0x08000000)

    def _loc_3660(): pass

    label('loc_3660')

    Return()

# id: 0x0011 offset: 0x3661
@scena.Code('func_11_3661')
def func_11_3661():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 3, 0x24B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AE9',
    )

    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x0013, 0)
    ChrTurnDirection(0x0001, 0x0013, 0)
    ChrTurnDirection(0x0002, 0x0013, 0)
    SetScenaFlags(ScenaFlag(0x0049, 3, 0x24B))
    ChrSetFlags(0x000A, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    ChrTurnDirection(0x0013, 0x0101, 800)
    CreateThread(0x0013, 0x01, 0x00, func_12_3AEA)
    ChrTurnDirection(0x0015, 0x0101, 800)
    CreateThread(0x0015, 0x01, 0x00, func_12_3AEA)
    ChrTurnDirection(0x0014, 0x0101, 800)
    CreateThread(0x0014, 0x01, 0x00, func_12_3AEA)
    OP_A6(0x0009)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0015, 0xFF)
    Battle(0x00000384, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_36DD'),
        (-1, 'loc_36E2'),
    )

    def _loc_36DD(): pass

    label('loc_36DD')

    OP_B4(0x00)

    Jump('loc_36E2')

    def _loc_36E2(): pass

    label('loc_36E2')

    EventBegin(0x00)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0008)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0008)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0008)
    ChrSetPos(0x0133, 91310, 0, 62810, 225)
    ChrSetPos(0x0102, 91630, 0, 64090, 225)
    ChrSetPos(0x0101, 92380, 0, 62140, 270)
    CameraMove(91000, 0, 62560, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x000A, 45, 0)
    TerminateThread(0x000A, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0990010220V得、得救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010221V#006F放心吧，已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010222V#006F只要有游击士出马，\n',
            '一两只魔兽算不了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0101, 600)

    ChrTalk(
        0x000A,
        (
            '#0990010223V游、游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010224V为什么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010225V哦？你好像是……\n',
            '昨天刚来的那个新人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010226V现在还用不着你来地下干活啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0133, 600)

    ChrTalk(
        0x000A,
        (
            '#0990010227V这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010228V我、我只是想\n',
            '见识一下前辈们的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010229V没想到那边的墙壁突然崩塌，\n',
            '从里面冲出了好多魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010230V果然是和魔兽的巢穴连在一起……\n',
            '和这位小哥推测的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010231V#012F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010232V那、那边真的很危险，\n',
            '有很多魔兽在里面游荡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0990010233V那、那我还是快点出去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x000A, 0x02, 0x00, func_14_3CAD)
    ChrWalkTo(0x000A, 95640, 0, 61500, 14000, 0x00)
    ChrWalkTo(0x000A, 109730, 0, 69700, 14000, 0x00)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010010234V#000F逃得真快……\n',
            '看样子吓得不轻呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010235V#010F……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    TerminateThread(0x000A, 0xFF)

    def _loc_3AE9(): pass

    label('loc_3AE9')

    Return()

# id: 0x0012 offset: 0x3AEA
@scena.Code('func_12_3AEA')
def func_12_3AEA():
    OP_92(0x00FE, 0x0000, 610, 5000, 0x00)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Return()

# id: 0x0013 offset: 0x3AFC
@scena.Code('func_13_3AFC')
def func_13_3AFC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            Expr.Return,
        ),
        'loc_3CAC',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C48',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrTurnDirection(0x0133, 0x0000, 400)

    ChrTalk(
        0x0133,
        (
            '#0940010185V我说你们两个想去哪儿？\n',
            '那边好像是魔兽的巢穴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0940010186V崩塌之后可能还存在危险性，\n',
            '我们还是不要靠近那边好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C06',
    )

    ChrTurnDirection(0x0101, 0x0133, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010187V#002F的确可能有危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010188V#012F嗯，我们回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C45')

    def _loc_3C06(): pass

    label('loc_3C06')

    @scena.Lambda('lambda_3C0C')
    def lambda_3C0C():
        ChrTurnDirection(0x0101, 0x0133, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C0C)

    ChrTurnDirection(0x0102, 0x0133, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010189V#012F是啊。\n',
            '我们回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C45(): pass

    label('loc_3C45')

    Jump('loc_3C91')

    def _loc_3C48(): pass

    label('loc_3C48')

    ChrTalk(
        0x0133,
        (
            '#0940010190V那边好像有魔兽的巢穴啊。\n',
            '我们还是不要靠近那边比较安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3C91(): pass

    label('loc_3C91')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3CAC(): pass

    label('loc_3CAC')

    Return()

# id: 0x0014 offset: 0x3CAD
@scena.Code('func_14_3CAD')
def func_14_3CAD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3CCF',
    )

    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    ChrTurnDirection(0x0002, 0x00FE, 0)
    Yield()

    Jump('func_14_3CAD')

    def _loc_3CCF(): pass

    label('loc_3CCF')

    Return()

# id: 0x0015 offset: 0x3CD0
@scena.Code('func_15_3CD0')
def func_15_3CD0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 4, 0x244)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E1D',
    )

    MapSetFlags(0x08000000)
    SetScenaFlags(ScenaFlag(0x0048, 4, 0x244))
    ChrSetPos(0x000B, 130840, 1000, 15040, 270)
    ChrSetPos(0x000C, 130850, 1000, 13860, 270)
    OP_62(0x0133, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x000B, 0)
    ChrTurnDirection(0x0102, 0x000B, 0)
    ChrTurnDirection(0x0133, 0x000B, 0)
    EventBegin(0x00)

    ChrTalk(
        0x000B,
        (
            '#0950010191V不、不要过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0950010192V不是我夸张，\n',
            '我身上的筋太多，一点也不好吃！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0960010193V我、我也很难吃的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0960010194V脂肪太多了，\n',
            '吃了肯定会有害健康！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    MapClearFlags(0x08000000)

    def _loc_3E1D(): pass

    label('loc_3E1D')

    Return()

# id: 0x0016 offset: 0x3E1E
@scena.Code('func_16_3E1E')
def func_16_3E1E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 5, 0x245)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40D7',
    )

    SetScenaFlags(ScenaFlag(0x0048, 5, 0x245))
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x0012, 0)
    ChrTurnDirection(0x0001, 0x0012, 0)
    ChrTurnDirection(0x0002, 0x0012, 0)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrTurnDirection(0x0012, 0x0101, 500)
    Sleep(200)

    OP_92(0x0012, 0x0000, 500, 7000, 0x00)
    Battle(0x00000384, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3E81'),
        (-1, 'loc_3E86'),
    )

    def _loc_3E81(): pass

    label('loc_3E81')

    OP_B4(0x00)

    Jump('loc_3E86')

    def _loc_3E86(): pass

    label('loc_3E86')

    EventBegin(0x00)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0012, 0x0008)
    ChrSetPos(0x0133, 129000, 1000, 12980, 45)
    ChrSetPos(0x0102, 126780, 1000, 11750, 45)
    ChrSetPos(0x0101, 127660, 1000, 11490, 45)
    CameraMove(128919, 1000, 12950, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    ChrTurnDirection(0x000B, 0x0101, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010195V#000F已经没事了，矿工叔叔们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0950010196V得、得救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0960010197V呼唉唉～\n',
            '还以为再也没机会吃饭了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010198V还说那么多废话干吗啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010199V都赶快给我逃出去！\n',
            '再这么磨蹭，是不是想被魔兽吃进肚子啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0950010200V知、知道了，老大！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x00, func_17_40D8)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0960010201V多谢救命之恩～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x000C, 0x02, 0x00, func_14_3CAD)
    ChrWalkTo(0x000C, 125870, 500, 12600, 6000, 0x00)
    ChrWalkTo(0x000C, 122500, 250, 16400, 7000, 0x00)
    ChrWalkTo(0x000C, 127100, 0, 25100, 8000, 0x00)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    EventEnd(0x00)
    TerminateThread(0x000C, 0xFF)

    def _loc_40D7(): pass

    label('loc_40D7')

    Return()

# id: 0x0017 offset: 0x40D8
@scena.Code('func_17_40D8')
def func_17_40D8():
    ChrWalkTo(0x000B, 125870, 500, 12600, 6000, 0x00)
    ChrWalkTo(0x000B, 122500, 250, 16400, 7000, 0x00)
    ChrWalkTo(0x000B, 127100, 0, 25100, 8000, 0x00)

    Return()

# id: 0x0018 offset: 0x4115
@scena.Code('func_18_4115')
def func_18_4115():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 7, 0x247)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4222',
    )

    MapSetFlags(0x08000000)
    SetScenaFlags(ScenaFlag(0x0048, 7, 0x247))
    OP_62(0x0133, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x000D, 0)
    ChrTurnDirection(0x0102, 0x000D, 0)
    ChrTurnDirection(0x0133, 0x000D, 0)
    EventBegin(0x00)

    ChrTalk(
        0x000D,
        (
            '#0970010202V啊啊，女神爱德丝……\n',
            '请来救救我们吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0980010203V笨、笨蛋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0980010204V有向神祈祷的工夫，\n',
            '还不如快点帮忙赶走这些东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    MapClearFlags(0x08000000)

    def _loc_4222(): pass

    label('loc_4222')

    Return()

# id: 0x0019 offset: 0x4223
@scena.Code('func_19_4223')
def func_19_4223():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 0, 0x248)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45CE',
    )

    SetScenaFlags(ScenaFlag(0x0049, 0, 0x248))
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x0011, 0)
    ChrTurnDirection(0x0001, 0x0011, 0)
    ChrTurnDirection(0x0002, 0x0011, 0)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrTurnDirection(0x0011, 0x0101, 500)
    Sleep(200)

    OP_92(0x0011, 0x0000, 500, 7000, 0x00)
    Battle(0x00000384, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_4286'),
        (-1, 'loc_428B'),
    )

    def _loc_4286(): pass

    label('loc_4286')

    OP_B4(0x00)

    Jump('loc_428B')

    def _loc_428B(): pass

    label('loc_428B')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0008)
    ChrSetPos(0x0133, 86770, -500, 30250, 315)
    ChrSetPos(0x0102, 87730, 0, 28260, 315)
    ChrSetPos(0x0101, 88160, 0, 29600, 315)
    CameraMove(84700, -290, 30790, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    ChrTurnDirection(0x000D, 0x0101, 0)
    ChrTurnDirection(0x000E, 0x0101, 0)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020010205V#010F没有受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0970010206V没、没事……\n',
            '多亏你们救了我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0970010207V啊啊，这一定就是爱德丝的引导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#0980010208V真是头脑简单的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0980010209V如果真的有女神引导，\n',
            '一开始就不会遇到这种事啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000D, 0x000E, 400)

    ChrTalk(
        0x000D,
        (
            '#0970010210V正、正是因为有你这种不虔诚的人，\n',
            '才会引起这样不幸的事故！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000E, 0x000D, 400)

    ChrTalk(
        0x000E,
        (
            '#0980010211V你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0133, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0133,
        (
            '#0940010212V现在是吵架的时候吗？\n',
            '都赶快给我离开这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0133, 600)
    ChrTurnDirection(0x000E, 0x0133, 600)

    ChrTalk(
        0x000D,
        (
            '#0970010213V是、是，老大！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0980010214V老大你们也要小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000E, 0x01, 0x00, func_1A_45CF)
    Sleep(500)

    CreateThread(0x000D, 0x02, 0x00, func_14_3CAD)
    ChrWalkTo(0x000D, 85500, 1000, 32700, 6000, 0x00)
    ChrWalkTo(0x000D, 98300, 0, 27100, 6000, 0x00)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0008)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0008)
    EventEnd(0x00)
    TerminateThread(0x000D, 0xFF)

    def _loc_45CE(): pass

    label('loc_45CE')

    Return()

# id: 0x001A offset: 0x45CF
@scena.Code('func_1A_45CF')
def func_1A_45CF():
    ChrWalkTo(0x000E, 85500, 1000, 32700, 6000, 0x00)
    ChrWalkTo(0x000E, 98300, 0, 27100, 6000, 0x00)

    Return()

# id: 0x001B offset: 0x45F8
@scena.Code('func_1B_45F8')
def func_1B_45F8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_4642',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力梯的开关被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x01)

    Jump('loc_4D7B')

    def _loc_4642(): pass

    label('loc_4642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 1, 0x241)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C6B',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 7, 0x23F)),
            Expr.Return,
        ),
        'loc_4899',
    )

    Fade(1000)
    ChrSetPos(0x0000, 53590, 50, 57020, 0)
    ChrSetPos(0x0001, 54570, 50, 57080, 0)
    CameraMove(53780, 50, 58370, 1000)
    SetScenaFlags(ScenaFlag(0x0048, 1, 0x241))

    ChrTalk(
        0x0102,
        (
            '#0020010121V#010F艾丝蒂尔。\n',
            '用刚才借的钥匙试试看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010122V#010F这次导力梯应该能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用了',
            (TxtCtl.SetColor, 0x5),
            '导力梯的钥匙',
            (TxtCtl.SetColor, 0x5),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(115, 0x00, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0102,
        (
            '#0020010123V#010F这样导力梯应该就可以动了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010124V#010F我们赶快下去吧？',
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
        0,
        (
            TXT(0x00, '【乘坐导力梯】\n'),
            TXT(0x01, '【不乘坐】\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47EE',
    )

    Sleep(300)

    EventEnd(0x00)

    Return()

    def _loc_47EE(): pass

    label('loc_47EE')

    Fade(1000)
    ChrSetPos(0x0000, 53590, 50, 57020, 0)
    ChrSetPos(0x0001, 54570, 50, 57080, 0)
    CameraMove(54090, 50, 57700, 1000)
    Sleep(120)

    PlaySE(102, 0x00, 0x64)
    OP_70(0x0001, 120)
    OP_73(0x0001)
    OP_6F(0x0001, 120)
    Fade(1000)
    CameraMove(129000, 0, 76700, 0)
    ChrSetPos(0x0000, 128580, 8000, 77050, 180)
    ChrSetPos(0x0001, 129560, 8000, 77060, 180)
    OP_6F(0x0002, 360)
    Sleep(120)

    OP_70(0x0002, 240)
    OP_73(0x0002)
    EventEnd(0x00)
    OP_6F(0x0002, 240)

    Return()

    def _loc_4899(): pass

    label('loc_4899')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 6, 0x23E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A6B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 0, 0x240)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A28',
    )

    Fade(1000)
    ChrSetPos(0x0101, 53800, 50, 57690, 0)
    ChrSetPos(0x0102, 54180, 50, 56280, 0)
    CameraMove(53780, 50, 58370, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010010087V#002F这个是导力梯吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010088V#002F怎么看起来不能动呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010089V#012F让我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_495F')
    def lambda_495F():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_495F')

    DispatchAsync2(0x0101, 0x0001, lambda_495F)

    ChrMoveTo(0x0101, 53390, 50, 57060, 2000, 0x00)
    ChrWalkTo(0x0102, 54070, 50, 57690, 2000, 0x00)
    Sleep(300)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0102)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010090V#012F虽然导力还通着，\n',
            '不过开关好像被锁上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010091V#012F问问这里的矿工比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    EventEnd(0x00)

    Jump('loc_4A68')

    def _loc_4A28(): pass

    label('loc_4A28')

    EventBegin(0x00)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力梯的开关被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x01)

    def _loc_4A68(): pass

    label('loc_4A68')

    Jump('loc_4C5F')

    def _loc_4A6B(): pass

    label('loc_4A6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 0, 0x240)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C1D',
    )

    Fade(1000)
    ChrSetPos(0x0101, 53800, 50, 57690, 0)
    ChrSetPos(0x0102, 54180, 50, 56280, 0)
    CameraMove(53780, 50, 58370, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010010092V#505F这个就是通到地下的导力梯吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010093V#505F不过好像不能动啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010094V#010F让我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_4B33')
    def lambda_4B33():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_4B33')

    DispatchAsync2(0x0101, 0x0001, lambda_4B33)

    ChrMoveTo(0x0101, 53390, 50, 57060, 2000, 0x00)
    ChrWalkTo(0x0102, 54070, 50, 57690, 2000, 0x00)
    Sleep(300)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0102)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010095V#015F虽然导力还通着，\n',
            '不过开关好像被锁上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010096V#010F去问问刚才的那个矿工吧。\n',
            '他可能知道开动这导力梯的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    EventEnd(0x00)

    Jump('loc_4C5F')

    def _loc_4C1D(): pass

    label('loc_4C1D')

    EventBegin(0x00)
    FadeOut(300, 0, 100)
    OP_0D()
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力梯的开关被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x01)

    def _loc_4C5F(): pass

    label('loc_4C5F')

    SetScenaFlags(ScenaFlag(0x0048, 0, 0x240))
    OP_28(0x0003, 0x01, 0x0010)

    Jump('loc_4D7B')

    def _loc_4C6B(): pass

    label('loc_4C6B')

    EventBegin(0x00)
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
            TXT(0x00, '【乘坐导力梯】\n'),
            TXT(0x01, '【不乘坐】\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CD0',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_4CD0(): pass

    label('loc_4CD0')

    Fade(1000)
    ChrSetPos(0x0000, 53590, 50, 57020, 0)
    ChrSetPos(0x0001, 54570, 50, 57080, 0)
    CameraMove(54090, 50, 57700, 1000)
    Sleep(120)

    PlaySE(102, 0x00, 0x64)
    OP_70(0x0001, 120)
    OP_73(0x0001)
    OP_6F(0x0001, 120)
    Fade(1000)
    CameraMove(129000, 0, 76700, 0)
    ChrSetPos(0x0000, 128580, 8000, 77050, 180)
    ChrSetPos(0x0001, 129560, 8000, 77060, 180)
    OP_6F(0x0002, 360)
    Sleep(120)

    OP_70(0x0002, 240)
    OP_73(0x0002)
    EventEnd(0x00)
    OP_6F(0x0002, 240)

    Return()

    def _loc_4D7B(): pass

    label('loc_4D7B')

    Return()

# id: 0x001C offset: 0x4D7C
@scena.Code('func_1C_4D7C')
def func_1C_4D7C():
    OP_92(0x0000, 0x0001, 0, 3000, 0x00)
    ChrTurnDirection(0x0000, 0x0001, 0)

    Return()

# id: 0x001D offset: 0x4D92
@scena.Code('func_1D_4D92')
def func_1D_4D92():
    EventBegin(0x00)
    MapSetFlags(0x08000000)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 0, 0x248)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 5, 0x245)),
            Expr.Ez,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E79',
    )

    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0016,
        0x01,
        (
            (Expr.GetChrWork, 0x2, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x02,
        (
            (Expr.GetChrWork, 0x2, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x03,
        (
            (Expr.GetChrWork, 0x2, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0016, 800)
    ChrTurnDirection(0x0000, 0x0002, 400)
    ChrTurnDirection(0x0001, 0x0002, 400)
    ChrTurnDirection(0x0002, 0x0000, 400)

    ChrTalk(
        0x0133,
        (
            '#0940010236V不好意思……\n',
            '好像还有兄弟在这里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010237V拜托你们再帮帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    MapClearFlags(0x08000000)

    Return()

    def _loc_4E79(): pass

    label('loc_4E79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 3, 0x24B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_506A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 5, 0x24D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FA1',
    )

    SetScenaFlags(ScenaFlag(0x0049, 5, 0x24D))
    ChrSetPos(0x000A, 90000, 0, 61740, 90)

    ChrTalk(
        0x000A,
        (
            '#0990010238V嘿咿——！\n',
            '怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrTurnDirection(0x0102, 0x000A, 0)
    ChrTurnDirection(0x0133, 0x000A, 0)

    ChrTalk(
        0x000A,
        (
            '#0990010239V救命啊～～～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0016,
        0x01,
        (
            (Expr.GetChrWork, 0x133, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x02,
        (
            (Expr.GetChrWork, 0x133, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x03,
        (
            (Expr.GetChrWork, 0x133, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0016, 800)

    ChrTalk(
        0x0133,
        (
            '#0940010240V什么！\n',
            '还有其他人在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010241V#002F赶快去救他吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5062')

    def _loc_4FA1(): pass

    label('loc_4FA1')

    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0016,
        0x01,
        (
            (Expr.GetChrWork, 0x133, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x02,
        (
            (Expr.GetChrWork, 0x133, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x03,
        (
            (Expr.GetChrWork, 0x133, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0016, 800)
    ChrTurnDirection(0x0101, 0x0133, 0)
    ChrTurnDirection(0x0102, 0x0133, 0)
    ChrTurnDirection(0x0133, 0x0101, 0)

    ChrTalk(
        0x0133,
        (
            '#0940010242V不好意思……\n',
            '无论怎样也要先找到他们再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010243V拜托你们再帮帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5062(): pass

    label('loc_5062')

    EventEnd(0x01)
    MapClearFlags(0x08000000)

    Return()

    def _loc_506A(): pass

    label('loc_506A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_517A',
    )

    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0016,
        0x01,
        (
            (Expr.GetChrWork, 0x133, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x02,
        (
            (Expr.GetChrWork, 0x133, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x03,
        (
            (Expr.GetChrWork, 0x133, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0016, 800)
    ChrTurnDirection(0x0101, 0x0133, 0)
    ChrTurnDirection(0x0102, 0x0133, 0)
    ChrTurnDirection(0x0133, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010010244V#000F老大叔叔，全部人都离开这里了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010245V啊啊……应该没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010246V#010F那好，\n',
            '我们也上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0133, 129070, 50, 76680, 0)

    Jump('loc_51E4')

    def _loc_517A(): pass

    label('loc_517A')

    EventBegin(0x00)
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
            TXT(0x00, '【乘坐导力梯】\n'),
            TXT(0x01, '【不乘坐】\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_51DF',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_51DF(): pass

    label('loc_51DF')

    Fade(1000)

    def _loc_51E4(): pass

    label('loc_51E4')

    ChrSetPos(0x0000, 128440, 50, 77690, 0)
    ChrSetPos(0x0001, 129410, 50, 77690, 0)
    CameraMove(129020, 50, 77590, 1000)
    Sleep(120)

    PlaySE(102, 0x00, 0x64)
    OP_70(0x0002, 360)
    OP_73(0x0002)
    OP_6F(0x0002, 360)
    Fade(1000)
    OP_6F(0x0001, 120)
    Sleep(120)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_533E',
    )

    ChrSetPos(0x000D, 51560, 0, 55100, 0)
    ChrSetPos(0x000E, 51880, 0, 53800, 0)
    ChrSetPos(0x0009, 53210, 0, 54100, 0)
    ChrSetPos(0x0008, 55190, 0, 54000, 0)
    ChrSetPos(0x000B, 55250, 0, 51960, 0)
    ChrSetPos(0x000C, 56100, 0, 52360, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000D, 0x0008)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000E, 0x0008)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000C, 0x0008)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000B, 0x0008)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0009, 0x0008)
    ChrClearFlags(0x0133, 0x0008)
    ChrClearFlags(0x0133, 0x0080)
    ChrClearFlags(0x0133, 0x0004)
    ChrSetBattleFlags(0x0133, 0x0020)
    OP_89(0x0133, 54000, 0, 56400, 180)
    ChrTurnDirection(0x000D, 0x0133, 0)
    ChrTurnDirection(0x000E, 0x0133, 0)
    ChrTurnDirection(0x000C, 0x0133, 0)
    ChrTurnDirection(0x000B, 0x0133, 0)
    ChrTurnDirection(0x0009, 0x0133, 0)
    ChrTurnDirection(0x0008, 0x0133, 0)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)

    def _loc_533E(): pass

    label('loc_533E')

    CameraMove(54110, 50, 57680, 0)
    ChrSetPos(0x0000, 53380, -6000, 57690, 180)
    ChrSetPos(0x0001, 54620, -6000, 57470, 180)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_6F(0x0001, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0048, 2, 0x242)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55CC',
    )

    @scena.Lambda('lambda_5394')
    def lambda_5394():
        CameraMove(54030, 0, 55920, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5394)

    ChrWalkTo(0x0133, 54300, 0, 55060, 4000, 0x00)
    SetScenaFlags(ScenaFlag(0x0049, 6, 0x24E))
    OP_28(0x0003, 0x01, 0x0100)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0930010247V老大，没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0950010248V哎哎～幸好平安无事呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0133, 0x0101, 400)

    ChrTalk(
        0x0133,
        (
            '#0940010249V多亏了小姑娘你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0133, 0x0009, 400)

    ChrTalk(
        0x0133,
        (
            '#0940010250V对了，弟兄们都在这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010251V没错，都在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010252V不过，刚才那个见习的新人\n',
            '慌慌忙忙地逃走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0920010253V看来真是受了很大的惊吓啊，那家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010254V是这样吗……\n',
            '可别为这种事受打击就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010255V总之，\n',
            '地下很可能还有魔兽残存着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0133,
        (
            '#0940010256V在未确认安全之前，\n',
            '这个导力梯暂时禁止使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    FormationDelMember(0x32, 0xFF)
    MapClearFlags(0x08000000)
    NewScene('ED6_DT01/R0303._SN', 3, 0, 0)
    IdleLoop()

    def _loc_55CC(): pass

    label('loc_55CC')

    MapClearFlags(0x00400000)
    EventEnd(0x00)
    MapClearFlags(0x08000000)

    Return()

# id: 0x001E offset: 0x55D9
@scena.Code('func_1E_55D9')
def func_1E_55D9():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 5, 0x23D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5667',
    )

    CameraMove(15980, 0, 32049, 1000)
    SetScenaFlags(ScenaFlag(0x0047, 5, 0x23D))

    ChrTalk(
        0x0101,
        (
            '#0010010085V#000F是矿车啊……\n',
            '这东西也是靠导力运转的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010086V#010F好像是。\n',
            '我们赶快坐上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5667(): pass

    label('loc_5667')

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
            TXT(0x00, '乘坐矿车\n'),
            TXT(0x01, '不乘坐\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56C0',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_56C0(): pass

    label('loc_56C0')

    MapSetFlags(0x00000001)
    Fade(500)
    ChrSetFlags(0x0001, 0x0008)
    ChrSetFlags(0x0002, 0x0008)
    ChrSetFlags(0x0003, 0x0008)
    ChrSetPos(0x0000, 15900, 400, 32299, 0)
    ChrSetPos(0x0001, 15900, 400, 32299, 0)
    ChrSetPos(0x0002, 15900, 400, 32299, 0)
    ChrSetPos(0x0003, 15900, 400, 32299, 0)
    Sleep(500)

    PlaySE(101, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57B7',
    )

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    OP_6F(0x0000, 0)
    OP_70(0x0000, 330)
    OP_73(0x0000)
    OP_6F(0x0000, 330)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0)
    ChrClearFlags(0x0001, 0x0008)
    ChrClearFlags(0x0002, 0x0008)
    ChrClearFlags(0x0003, 0x0008)
    ChrSetPos(0x0000, 34200, 100, 61400, 315)
    ChrSetPos(0x0001, 34200, 100, 61400, 315)
    ChrSetPos(0x0002, 34200, 100, 61400, 315)
    ChrSetPos(0x0003, 34200, 100, 61400, 315)

    Jump('loc_583C')

    def _loc_57B7(): pass

    label('loc_57B7')

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    OP_6F(0x0000, 500)
    OP_70(0x0000, 900)
    OP_73(0x0000)
    OP_6F(0x0000, 900)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0)
    ChrClearFlags(0x0001, 0x0008)
    ChrClearFlags(0x0002, 0x0008)
    ChrClearFlags(0x0003, 0x0008)
    ChrSetPos(0x0000, 50500, 0, 51900, 45)
    ChrSetPos(0x0001, 50500, 0, 51900, 45)
    ChrSetPos(0x0002, 50500, 0, 51900, 45)
    ChrSetPos(0x0003, 50500, 0, 51900, 45)

    def _loc_583C(): pass

    label('loc_583C')

    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0x5844
@scena.Code('func_1F_5844')
def func_1F_5844():
    EventBegin(0x00)
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
            TXT(0x00, '乘坐矿车\n'),
            TXT(0x01, '不乘坐\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_589F',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_589F(): pass

    label('loc_589F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    MapSetFlags(0x00000001)
    Fade(500)
    OP_69(0x0000, 0)
    ChrSetFlags(0x0001, 0x0008)
    ChrSetFlags(0x0002, 0x0008)
    ChrSetFlags(0x0003, 0x0008)
    ChrSetPos(0x0000, 34800, 400, 59200, 225)
    ChrSetPos(0x0001, 34800, 400, 59200, 225)
    ChrSetPos(0x0002, 34800, 400, 59200, 225)
    ChrSetPos(0x0003, 34800, 400, 59200, 225)
    Sleep(500)

    PlaySE(101, 0x00, 0x64)
    OP_6F(0x0000, 330)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_6F(0x0000, 0)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0)
    ChrClearFlags(0x0001, 0x0008)
    ChrClearFlags(0x0002, 0x0008)
    ChrClearFlags(0x0003, 0x0008)
    ChrSetPos(0x0000, 16000, 50, 29700, 180)
    ChrSetPos(0x0001, 16000, 50, 29700, 180)
    ChrSetPos(0x0002, 16000, 50, 29700, 180)
    ChrSetPos(0x0003, 16000, 50, 29700, 180)
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x0020 offset: 0x599A
@scena.Code('func_20_599A')
def func_20_599A():
    EventBegin(0x00)
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
            TXT(0x00, '乘坐矿车\n'),
            TXT(0x01, '不乘坐\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_59F5',
    )

    Sleep(300)

    EventEnd(0x01)

    Return()

    def _loc_59F5(): pass

    label('loc_59F5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    MapSetFlags(0x00000001)
    Fade(500)
    ChrSetFlags(0x0001, 0x0008)
    ChrSetFlags(0x0002, 0x0008)
    ChrSetFlags(0x0003, 0x0008)
    ChrSetPos(0x0000, 50200, 400, 49900, 270)
    ChrSetPos(0x0001, 50200, 400, 49900, 270)
    ChrSetPos(0x0002, 50200, 400, 49900, 270)
    ChrSetPos(0x0003, 50200, 400, 49900, 270)
    Sleep(500)

    PlaySE(101, 0x00, 0x64)
    OP_6F(0x0000, 900)
    OP_70(0x0000, 500)
    OP_73(0x0000)
    OP_6F(0x0000, 500)
    Sleep(500)

    Fade(500)
    OP_69(0x0000, 0)
    ChrSetPos(0x0000, 16000, 50, 29700, 180)
    ChrSetPos(0x0001, 16000, 50, 29700, 180)
    ChrSetPos(0x0002, 16000, 50, 29700, 180)
    ChrSetPos(0x0003, 16000, 50, 29700, 180)
    ChrClearFlags(0x0001, 0x0008)
    ChrClearFlags(0x0002, 0x0008)
    ChrClearFlags(0x0003, 0x0008)
    Sleep(300)

    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0x5AE9
@scena.Code('func_21_5AE9')
def func_21_5AE9():
    MapSetFlags(0x00000080)
    Sleep(30)

    PlaySE(100, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B17',
    )

    OP_70(0x0003, 25)
    OP_73(0x0003)
    OP_6F(0x0003, 25)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5B2B')

    def _loc_5B17(): pass

    label('loc_5B17')

    OP_70(0x0003, 0)
    OP_73(0x0003)
    OP_6F(0x0003, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5B2B(): pass

    label('loc_5B2B')

    OP_73(0x0003)
    MapClearFlags(0x00000080)

    Return()

# id: 0x0022 offset: 0x5B34
@scena.Code('func_22_5B34')
def func_22_5B34():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
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
            TXT(0x00, '在此休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D4D',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0033, 0)
    OP_70(0x0033, 50)
    OP_73(0x0033)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    ChrSetPos(0x0000, 106750, 0, 39530, 285)
    ChrSetPos(0x0001, 106750, 0, 39530, 285)
    ChrSetPos(0x0002, 106750, 0, 39530, 285)
    ChrSetPos(0x0003, 106750, 0, 39530, 285)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0033, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_5D4D(): pass

    label('loc_5D4D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D67',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_5D67(): pass

    label('loc_5D67')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
