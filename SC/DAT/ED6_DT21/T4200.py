import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵丹'),
    TXT(0x02, '士兵阿尔兹'),
    TXT(0x03, '王国军士兵'),
    TXT(0x04, '王国军士兵'),
    TXT(0x05, '王国军士兵'),
    TXT(0x06, '王国军士兵'),
    TXT(0x07, '王国军士兵'),
    TXT(0x08, '王国军士兵'),
    TXT(0x09, '王国军士兵'),
    TXT(0x0A, '王国军士兵'),
    TXT(0x0B, '王国军士兵'),
    TXT(0x0C, '王国军士兵'),
    TXT(0x0D, '王国军士兵'),
    TXT(0x0E, '王国军士兵'),
    TXT(0x0F, '王国军士兵'),
    TXT(0x10, '王国军士兵'),
    TXT(0x11, '王国军士兵'),
    TXT(0x12, '幻惑之铃露茜奥拉'),
    TXT(0x13, '瘦狼瓦鲁特'),
    TXT(0x14, '怪盗布卢布兰'),
    TXT(0x15, '歼灭天使玲'),
    TXT(0x16, '亡命装甲兵'),
    TXT(0x17, '亡命装甲兵'),
    TXT(0x18, '亡命装甲兵'),
    TXT(0x19, '瘦狼瓦鲁特的残像'),
    TXT(0x1A, '瘦狼瓦鲁特的残像'),
    TXT(0x1B, '游客'),
    TXT(0x1C, '游客'),
    TXT(0x1D, '游客'),
    TXT(0x1E, '游客'),
    TXT(0x1F, '游客'),
    TXT(0x20, '王都格兰赛尔·北街区'),
    TXT(0x21, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4200.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x63E1
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
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -790,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
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
            x                   = 950,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            npcIndex            = 0x0185,
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
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 6640,
            z                   = 0,
            y                   = 24120,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 470,
            z                   = 0,
            y                   = 2060,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 8130,
            z                   = 0,
            y                   = 11800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 6210,
            z                   = 0,
            y                   = 12000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -2970,
            z                   = 0,
            y                   = 12840,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = -22550,
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

# id: 0x10003 offset: 0x4E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x4E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4500,
            y           = -2000,
            z           = 37000,
            range       = 4200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00009470,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -5250,
            y           = -1000,
            z           = 28530,
            range       = 4870,
            dword_10    = 0x000007D0,
            dword_14    = 0x00007468,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000017,
        ),
    )

# id: 0x10005 offset: 0x522
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -11120,
            triggerZ            = 0,
            triggerY            = 19460,
            triggerRange        = 1000,
            actorX              = -15170,
            actorZ              = -2000,
            actorY              = 19020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x546
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_55B',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    Call(0, 0x0010)

    def _loc_55B(): pass

    label('loc_55B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_57B',
    )

    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)

    def _loc_57B(): pass

    label('loc_57B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_591',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0015)

    Jump('loc_611')

    def _loc_591(): pass

    label('loc_591')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5A5'),
        (0x00000065, 'loc_5DB'),
        (0x00000066, 'loc_5F6'),
        (-1, 'loc_611'),
    )

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C5',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000E)

    Jump('loc_5D8')

    def _loc_5C5(): pass

    label('loc_5C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D8',
    )

    OP_A2(0x1627)

    def _loc_5D8(): pass

    label('loc_5D8')

    Jump('loc_611')

    def _loc_5DB(): pass

    label('loc_5DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 4, 0x203C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F3',
    )

    SetMapFlags(0x10000000)
    OP_A3(0x203F)
    Event(0, 0x0011)

    def _loc_5F3(): pass

    label('loc_5F3')

    Jump('loc_611')

    def _loc_5F6(): pass

    label('loc_5F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 4, 0x203C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_60E',
    )

    SetMapFlags(0x10000000)
    OP_A2(0x203F)
    Event(0, 0x0011)

    def _loc_60E(): pass

    label('loc_60E')

    Jump('loc_611')

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 3, 0x1623)),
            Expr.Return,
        ),
        'loc_63A',
    )

    SetChrPos(0x0008, -2009, 0, 41980, 180)
    SetChrPos(0x0009, 2270, 0, 41980, 180)

    def _loc_63A(): pass

    label('loc_63A')

    Return()

# id: 0x0001 offset: 0x63B
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFE4A80, 0x00230060)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x550),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_662',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_662(): pass

    label('loc_662')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_682',
    )

    OP_B1('t4200_y')

    Jump('loc_68B')

    def _loc_682(): pass

    label('loc_682')

    OP_B1('t4200_n')

    def _loc_68B(): pass

    label('loc_68B')

    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_6E7',
    )

    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_71(0x0001, 0x0002)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 4, 0x203C)),
            Expr.Return,
        ),
        'loc_6D6',
    )

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 141)
    OP_72(0x0002, 0x0004)

    def _loc_6D6(): pass

    label('loc_6D6')

    OP_77(0xFF, 0xBD, 0xA7, 0x00, 0x00000000)
    Call(0, 0x000F)
    OP_64(0x00, 0x0001)

    def _loc_6E7(): pass

    label('loc_6E7')

    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 4, 0x203C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 5, 0x203D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_700',
    )

    Call(0, 0x0016)

    def _loc_700(): pass

    label('loc_700')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_711',
    )

    OP_6F(0x0000, 450)

    Jump('loc_794')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_75A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_729',
    )

    OP_6F(0x0000, 450)

    Jump('loc_730')

    def _loc_729(): pass

    label('loc_729')

    OP_6F(0x0000, 0)

    def _loc_730(): pass

    label('loc_730')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_73C'),
        (-1, 'loc_757'),
    )

    def _loc_73C(): pass

    label('loc_73C')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_757',
    )

    OP_6F(0x0000, 450)
    OP_A2(0x0002)

    Jump('loc_757')

    def _loc_757(): pass

    label('loc_757')

    Jump('loc_794')

    def _loc_75A(): pass

    label('loc_75A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Return,
        ),
        'loc_77C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_772',
    )

    OP_6F(0x0000, 0)

    Jump('loc_779')

    def _loc_772(): pass

    label('loc_772')

    OP_6F(0x0000, 450)

    def _loc_779(): pass

    label('loc_779')

    Jump('loc_794')

    def _loc_77C(): pass

    label('loc_77C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 3, 0x1623)),
            Expr.Return,
        ),
        'loc_78D',
    )

    OP_6F(0x0000, 450)

    Jump('loc_794')

    def _loc_78D(): pass

    label('loc_78D')

    OP_6F(0x0000, 0)

    def _loc_794(): pass

    label('loc_794')

    OP_22(0x01CC, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x79A
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
        'loc_7BF',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_901')

    def _loc_7BF(): pass

    label('loc_7BF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D8',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_901')

    def _loc_7D8(): pass

    label('loc_7D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F1',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_901')

    def _loc_7F1(): pass

    label('loc_7F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80A',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_901')

    def _loc_80A(): pass

    label('loc_80A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_823',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_901')

    def _loc_823(): pass

    label('loc_823')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83C',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_901')

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_855',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_901')

    def _loc_855(): pass

    label('loc_855')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_901')

    def _loc_86E(): pass

    label('loc_86E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_887',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_901')

    def _loc_887(): pass

    label('loc_887')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A0',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_901')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B9',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_901')

    def _loc_8B9(): pass

    label('loc_8B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D2',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_901')

    def _loc_8D2(): pass

    label('loc_8D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8EB',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_901')

    def _loc_8EB(): pass

    label('loc_8EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_901',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_901(): pass

    label('loc_901')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_916',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_901')

    def _loc_916(): pass

    label('loc_916')

    Return()

# id: 0x0003 offset: 0x917
@scena.Code('func_03_917')
def func_03_917():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_93A',
    )

    OP_8D(0x00FE, 2620, 2600, -590, 3530, 2000)

    Jump('func_03_917')

    def _loc_93A(): pass

    label('loc_93A')

    Return()

# id: 0x0004 offset: 0x93B
@scena.Code('func_04_93B')
def func_04_93B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_95E',
    )

    OP_8D(0x00FE, -1730, 10700, -4110, 14100, 2000)

    Jump('func_04_93B')

    def _loc_95E(): pass

    label('loc_95E')

    Return()

# id: 0x0005 offset: 0x95F
@scena.Code('func_05_95F')
def func_05_95F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_989',
    )

    ChrTalk(
        0x00FE,
        (
            '喔，是你们……\n',
            '请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1872')

    def _loc_989(): pass

    label('loc_989')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_C53',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_9B4',
    )

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF3')

    def _loc_9B4(): pass

    label('loc_9B4')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0105, 160, 0, 39870, 0)
    SetChrPos(0x0101, 80, 0, 38310, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9FE',
    )

    SetChrPos(0x0106, -740, 0, 36890, 0)

    Jump('loc_A0F')

    def _loc_9FE(): pass

    label('loc_9FE')

    SetChrPos(0x0103, -740, 0, 36890, 0)

    def _loc_A0F(): pass

    label('loc_A0F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A30',
    )

    SetChrPos(0x00F9, 710, 0, 37200, 0)

    Jump('loc_A41')

    def _loc_A30(): pass

    label('loc_A30')

    SetChrPos(0x00F8, 710, 0, 37200, 0)

    def _loc_A41(): pass

    label('loc_A41')

    OP_6D(1350, 0, 42100, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_8C(0x0008, 180, 0)
    SetChrSubChip(0x0008, 0)
    OP_8C(0x0009, 180, 0)
    SetChrSubChip(0x0009, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#5P公主殿下，您要进入城内吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P谨遵殿下之名！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 400)
    Sleep(500)

    OP_22(0x00D2, 0x00, 0x64)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 450)
    OP_70(0x0000, 0x000001C2)
    Sleep(6700)

    OP_8C(0x0009, 180, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1K#1P请进！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#1K#2P请进！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Fade(500)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 0, 0, 40470, 360)
    SetChrPos(0x0001, 0, 0, 40470, 360)
    SetChrPos(0x0002, 0, 0, 40470, 360)
    SetChrPos(0x0003, 0, 0, 40470, 360)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x0002)
    EventEnd(0x00)

    def _loc_BF3(): pass

    label('loc_BF3')

    Jump('loc_C50')

    def _loc_BF6(): pass

    label('loc_BF6')

    ChrTalk(
        0x00FE,
        (
            '终于抓到凯诺娜上尉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话女王陛下\n',
            '也能集中精力在条约的\n',
            '签字仪式上了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_C50(): pass

    label('loc_C50')

    Jump('loc_1872')

    def _loc_C53(): pass

    label('loc_C53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_E66',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 4, 0x164C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E28',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB0',
    )

    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '公主殿下有何吩咐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F丹先生，请问你\n',
            '有没有见过穿白色礼服的\n',
            '这么大的一个女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '穿白色礼服的女孩子……唔……\n',
            '不记得有这样的人进了城堡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才在王都前的广场巡逻时\n',
            '好像也没有看到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是吗……\n',
            '谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对、对不起。\n',
            '没能帮上您的忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不，我才是打扰了你的工作\n',
            '对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E22')

    def _loc_DB0(): pass

    label('loc_DB0')

    ChrTalk(
        0x00FE,
        (
            '你们在找穿白色\n',
            '礼服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……应该没有进入城堡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才在王都前的广场巡逻时\n',
            '好像也没有看到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E22(): pass

    label('loc_E22')

    OP_A2(0x164C)

    Jump('loc_E63')

    def _loc_E28(): pass

    label('loc_E28')

    ChrTalk(
        0x00FE,
        (
            '穿白色礼服的女孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我记得几天前\n',
            '好像见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_E63(): pass

    label('loc_E63')

    Jump('loc_1872')

    def _loc_E66(): pass

    label('loc_E66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EB3',
    )

    ChrTalk(
        0x00FE,
        (
            '公主殿下，您辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经是黄昏了，\n',
            '请您出去时小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1872')

    def _loc_EB3(): pass

    label('loc_EB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_EC9',
    )

    ChrTalk(
        0x00FE,
        (
            '请进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1872')

    def _loc_EC9(): pass

    label('loc_EC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1872',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 6, 0x166E)),
            (Expr.TestScenaFlags, ScenaFlag(0x02CE, 1, 0x1671)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F63',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F34',
    )

    ChrTurnDirection(0x0008, 0x0105, 0)

    ChrTalk(
        0x0008,
        (
            '#5P科洛蒂娅殿下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#5P如果需要进入城堡\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F60')

    def _loc_F34(): pass

    label('loc_F34')

    ChrTalk(
        0x0008,
        (
            '#5P需要进入城堡的话\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F60(): pass

    label('loc_F60')

    Jump('loc_1872')

    def _loc_F63(): pass

    label('loc_F63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 6, 0x166E)),
            Expr.Return,
        ),
        'loc_1241',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1210',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1093',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0009, 0x0105, 300)
    Sleep(700)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果需要进入城堡\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P好的，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 180, 300)
    OP_4B(0x0009, 255)
    OP_A2(0x1671)

    Jump('loc_120D')

    def _loc_1093(): pass

    label('loc_1093')

    ChrTalk(
        0x0008,
        (
            '#5P怎么了？\n',
            '#5P您是不是还是想进去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#048F#2P好久不见了。\n',
            '丹先生、阿尔兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0008, 0x0105, 300)
    ChrTurnDirection(0x0009, 0x0105, 300)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果需要进入城堡\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F#2P（不、不愧是科洛丝……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 180, 300)
    OP_4B(0x0009, 255)
    OP_A2(0x1671)

    def _loc_120D(): pass

    label('loc_120D')

    Jump('loc_123E')

    def _loc_1210(): pass

    label('loc_1210')

    ChrTalk(
        0x0008,
        (
            '#5P需要进入城堡的话，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_123E(): pass

    label('loc_123E')

    Jump('loc_1872')

    def _loc_1241(): pass

    label('loc_1241')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16CC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1435',
    )

    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0009, 0x0105, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 300)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x0008,
        (
            '咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 300)

    ChrTalk(
        0x0009,
        (
            '#5P那几位是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嘿嘿，好久不见了。',
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
        'loc_13C0',
    )

    ChrTalk(
        0x0108,
        (
            '#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C0(): pass

    label('loc_13C0')

    ChrTalk(
        0x0008,
        (
            '真让我吃惊。\n',
            '好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想进城堡的话，\n',
            '随时招呼我们一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 180, 300)
    OP_4B(0x0009, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)

    Jump('loc_16C9')

    def _loc_1435(): pass

    label('loc_1435')

    ChrTurnDirection(0x0009, 0x0000, 0)
    OP_4A(0x0009, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '哟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P你们是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嘿嘿，好久不见了。',
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
        'loc_14FF',
    )

    ChrTalk(
        0x0108,
        (
            '#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14FF(): pass

    label('loc_14FF')

    ChrTalk(
        0x0008,
        (
            '哈哈……\n',
            '今天有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果想见谁的话，\n',
            '我进去帮你们通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P或者说你们想\n',
            '进去参观？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F#2P不，不是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#048F#2P好久不见了。\n',
            '丹先生、阿尔兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 0)
    ChrTurnDirection(0x0009, 0x0105, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果需要进入城堡，\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P好的，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 180, 300)
    OP_4B(0x0009, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)
    def _loc_16C9(): pass

    label('loc_16C9')

    Jump('loc_1872')

    def _loc_16CC(): pass

    label('loc_16CC')

    ChrTurnDirection(0x0009, 0x0000, 0)
    OP_4A(0x0009, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '哟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P你们是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嘿嘿，好久不见了。',
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
        'loc_1796',
    )

    ChrTalk(
        0x0108,
        (
            '#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1796(): pass

    label('loc_1796')

    ChrTalk(
        0x0008,
        (
            '哈哈……\n',
            '今天有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果想见谁的话，\n',
            '我进去帮你们通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P或者说你们想\n',
            '进去参观？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F#2P不，今天\n',
            '只是路过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是吗，想进城堡的话，\n',
            '随时招呼我们一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F#2P嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 180, 300)
    OP_4B(0x0009, 255)
    OP_A2(0x166E)

    def _loc_1872(): pass

    label('loc_1872')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x1876
@scena.Code('func_06_1876')
def func_06_1876():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_18D1',
    )

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅殿下\n',
            '应该在城堡里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过她现在应该很忙，\n',
            '大概不能见你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259D')

    def _loc_18D1(): pass

    label('loc_18D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1B90',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_18FC',
    )

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B3B')

    def _loc_18FC(): pass

    label('loc_18FC')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0105, 160, 0, 39870, 0)
    SetChrPos(0x0101, 80, 0, 38310, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1946',
    )

    SetChrPos(0x0106, -740, 0, 36890, 0)

    Jump('loc_1957')

    def _loc_1946(): pass

    label('loc_1946')

    SetChrPos(0x0103, -740, 0, 36890, 0)

    def _loc_1957(): pass

    label('loc_1957')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1978',
    )

    SetChrPos(0x00F9, 710, 0, 37200, 0)

    Jump('loc_1989')

    def _loc_1978(): pass

    label('loc_1978')

    SetChrPos(0x00F8, 710, 0, 37200, 0)

    def _loc_1989(): pass

    label('loc_1989')

    OP_6D(1350, 0, 42100, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_8C(0x0008, 180, 0)
    SetChrSubChip(0x0008, 0)
    OP_8C(0x0009, 180, 0)
    SetChrSubChip(0x0009, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#5P公主殿下，您要进入城内吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P谨遵殿下之名！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 400)
    Sleep(500)

    OP_22(0x00D2, 0x00, 0x64)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 450)
    OP_70(0x0000, 0x000001C2)
    Sleep(6700)

    OP_8C(0x0009, 180, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1K#1P请进！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#1K#2P请进！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Fade(500)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 0, 0, 40470, 360)
    SetChrPos(0x0001, 0, 0, 40470, 360)
    SetChrPos(0x0002, 0, 0, 40470, 360)
    SetChrPos(0x0003, 0, 0, 40470, 360)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x0002)
    EventEnd(0x00)

    def _loc_1B3B(): pass

    label('loc_1B3B')

    Jump('loc_1B8D')

    def _loc_1B3E(): pass

    label('loc_1B3E')

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙们真把\n',
            '我们整得够呛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能抓到他们说实话让我松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1B8D(): pass

    label('loc_1B8D')

    Jump('loc_259D')

    def _loc_1B90(): pass

    label('loc_1B90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1BB7',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，今天也需要\n',
            '进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259D')

    def _loc_1BB7(): pass

    label('loc_1BB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BE2',
    )

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅殿下，\n',
            '欢迎您！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259D')

    def _loc_1BE2(): pass

    label('loc_1BE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1BF8',
    )

    ChrTalk(
        0x00FE,
        (
            '请进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259D')

    def _loc_1BF8(): pass

    label('loc_1BF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_259D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 6, 0x166E)),
            (Expr.TestScenaFlags, ScenaFlag(0x02CE, 1, 0x1671)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C94',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C65',
    )

    ChrTurnDirection(0x0009, 0x0105, 0)

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P如果需要进入城堡，\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C91')

    def _loc_1C65(): pass

    label('loc_1C65')

    ChrTalk(
        0x0009,
        (
            '#5P如果需要进入城堡，\n',
            '请随时命令我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C91(): pass

    label('loc_1C91')

    Jump('loc_259D')

    def _loc_1C94(): pass

    label('loc_1C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 6, 0x166E)),
            Expr.Return,
        ),
        'loc_1F7A',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F4B',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DC6',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0105, 300)
    Sleep(700)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果需要进入城堡，\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P好的，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 300)
    OP_4B(0x0008, 255)
    OP_A2(0x1671)

    Jump('loc_1F48')

    def _loc_1DC6(): pass

    label('loc_1DC6')

    ChrTalk(
        0x0009,
        (
            '#5P有何吩咐？\n',
            '#5P您还是有事要进城里吗......',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#048F#2P好久不见了。\n',
            '丹先生、阿尔兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0105, 300)
    ChrTurnDirection(0x0009, 0x0105, 300)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果需要进入城堡，\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F#2P（不、不愧是科洛丝……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 300)
    OP_4B(0x0008, 255)
    OP_A2(0x1671)

    def _loc_1F48(): pass

    label('loc_1F48')

    Jump('loc_1F77')

    def _loc_1F4B(): pass

    label('loc_1F4B')

    ChrTalk(
        0x0009,
        (
            '#5P如果需要进入城堡，\n',
            '请随时命令我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1F77(): pass

    label('loc_1F77')

    Jump('loc_259D')

    def _loc_1F7A(): pass

    label('loc_1F7A')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23F7',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2160',
    )

    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0105, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
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
            '咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P那几位是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嘿嘿，好久不见了。',
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
        'loc_20EB',
    )

    ChrTalk(
        0x0108,
        (
            '#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20EB(): pass

    label('loc_20EB')

    ChrTalk(
        0x0008,
        (
            '真让我吃惊。\n',
            '好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想进城堡的话，\n',
            '随时招呼我们一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 300)
    OP_4B(0x0008, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)

    Jump('loc_23F4')

    def _loc_2160(): pass

    label('loc_2160')

    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P你们是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嘿嘿，好久不见了。',
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
        'loc_222A',
    )

    ChrTalk(
        0x0108,
        (
            '#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_222A(): pass

    label('loc_222A')

    ChrTalk(
        0x0008,
        (
            '哈哈……\n',
            '今天有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果想见谁的话，\n',
            '我进去帮你们通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P或者说你们想\n',
            '进去参观？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F#2P不，不是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#048F#2P好久不见了。\n',
            '丹先生、阿尔兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 0)
    ChrTurnDirection(0x0009, 0x0105, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果需要进入城堡，\n',
            '请随时命令我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F#2P好的，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 300)
    OP_4B(0x0008, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)
    def _loc_23F4(): pass

    label('loc_23F4')

    Jump('loc_259D')

    def _loc_23F7(): pass

    label('loc_23F7')

    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P你们是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P嘿嘿，好久不见了。',
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
        'loc_24C1',
    )

    ChrTalk(
        0x0108,
        (
            '#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24C1(): pass

    label('loc_24C1')

    ChrTalk(
        0x0008,
        (
            '哈哈……\n',
            '今天有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果想见谁的话，\n',
            '我进去帮你们通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P或者说你们想\n',
            '进去参观？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F#2P不，今天\n',
            '只是路过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是吗，想进城堡的话，\n',
            '随时招呼我们一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F#2P嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 300)
    OP_4B(0x0008, 255)
    OP_A2(0x166E)

    def _loc_259D(): pass

    label('loc_259D')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x25A1
@scena.Code('func_07_25A1')
def func_07_25A1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_25AE',
    )

    Jump('loc_26EC')

    def _loc_25AE(): pass

    label('loc_25AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2602',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的余党之前\n',
            '终于被抓住了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女神有眼，\n',
            '不让他们再干坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26EC')

    def _loc_2602(): pass

    label('loc_2602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2643',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，\n',
            '瓦雷利亚湖真宽广……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像海一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26EC')

    def _loc_2643(): pass

    label('loc_2643')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2674',
    )

    ChrTalk(
        0x00FE,
        (
            '好久没这么\n',
            '悠闲地看夕阳了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26EC')

    def _loc_2674(): pass

    label('loc_2674')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_26C0',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，鱼儿也\n',
            '游得很开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～早知道应该\n',
            '带钓竿来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26EC')

    def _loc_26C0(): pass

    label('loc_26C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_26EC',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔，这附近\n',
            '好像很适合钓鱼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26EC(): pass

    label('loc_26EC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x26F0
@scena.Code('func_08_26F0')
def func_08_26F0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_26FD',
    )

    Jump('loc_28B3')

    def _loc_26FD(): pass

    label('loc_26FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2786',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部和亲卫队好像\n',
            '进行了战斗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好在我观光的时候\n',
            '发生了大事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望不要再像以前那样，\n',
            '连飞船也搭不了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B3')

    def _loc_2786(): pass

    label('loc_2786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_27D8',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道能不能见到\n',
            '科洛蒂娅公主……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还从来没见过\n',
            '公主殿下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B3')

    def _loc_27D8(): pass

    label('loc_27D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_282E',
    )

    ChrTalk(
        0x00FE,
        (
            '这座城门前的广场，\n',
            '给人的感觉真舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '景色也好，\n',
            '风也清爽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B3')

    def _loc_282E(): pass

    label('loc_282E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2860',
    )

    ChrTalk(
        0x00FE,
        (
            '我进城堡看过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的很不错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B3')

    def _loc_2860(): pass

    label('loc_2860')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_28B3',
    )

    ChrTalk(
        0x00FE,
        (
            '我是第一次近距离\n',
            '看到格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然和照片上的\n',
            '气势完全不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28B3(): pass

    label('loc_28B3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x28B7
@scena.Code('func_09_28B7')
def func_09_28B7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_28C4',
    )

    Jump('loc_29C0')

    def _loc_28C4(): pass

    label('loc_28C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_28F0',
    )

    ChrTalk(
        0x00FE,
        (
            '港口竟然发生了那样的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C0')

    def _loc_28F0(): pass

    label('loc_28F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2921',
    )

    ChrTalk(
        0x00FE,
        (
            '太棒了，我傍晚一定\n',
            '要去港口看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C0')

    def _loc_2921(): pass

    label('loc_2921')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2971',
    )

    ChrTalk(
        0x00FE,
        (
            '伫立在晚霞中的\n',
            '城堡可是很浪漫的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天去哪里\n',
            '参观呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C0')

    def _loc_2971(): pass

    label('loc_2971')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2998',
    )

    ChrTalk(
        0x00FE,
        (
            '这地方……\n',
            '风特别舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C0')

    def _loc_2998(): pass

    label('loc_2998')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_29C0',
    )

    ChrTalk(
        0x00FE,
        (
            '他难得旅行一次，\n',
            '特别兴奋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29C0(): pass

    label('loc_29C0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x29C4
@scena.Code('func_0A_29C4')
def func_0A_29C4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_29D1',
    )

    Jump('loc_2ABC')

    def _loc_29D1(): pass

    label('loc_29D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_29FA',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天我们俩去\n',
            '港口参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_29FA(): pass

    label('loc_29FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2A2D',
    )

    ChrTalk(
        0x00FE,
        (
            '今天要不要去大圣堂\n',
            '和格兰赛尔港呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_2A2D(): pass

    label('loc_2A2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A6C',
    )

    ChrTalk(
        0x00FE,
        (
            '王都的景点太多，\n',
            '好是好，不过也让人犹豫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_2A6C(): pass

    label('loc_2A6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2A90',
    )

    ChrTalk(
        0x00FE,
        (
            '那么接下来去哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_2A90(): pass

    label('loc_2A90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2ABC',
    )

    ChrTalk(
        0x00FE,
        (
            '哟！　你好。\n',
            '王都真是个好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ABC(): pass

    label('loc_2ABC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x2AC0
@scena.Code('func_0B_2AC0')
def func_0B_2AC0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2ACD',
    )

    Jump('loc_2CE0')

    def _loc_2ACD(): pass

    label('loc_2ACD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2B63',
    )

    ChrTalk(
        0x00FE,
        (
            '呀──────！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听我说听我说，昨天我见到\n',
            '急奔向港口的尤莉亚大人了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来情报部的人\n',
            '就被逮捕了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是被电到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CE0')

    def _loc_2B63(): pass

    label('loc_2B63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2BC1',
    )

    ChrTalk(
        0x00FE,
        (
            '要想见到尤莉亚大人，\n',
            '就只能去当她的女佣了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在没有在\n',
            '招聘女佣呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CE0')

    def _loc_2BC1(): pass

    label('loc_2BC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C38',
    )

    ChrTalk(
        0x00FE,
        (
            '我混在城里的游客中，\n',
            '还去了亲卫队的驻所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可还是没见到\n',
            '尤莉亚大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～她去\n',
            '哪里了啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CE0')

    def _loc_2C38(): pass

    label('loc_2C38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2CA0',
    )

    ChrTalk(
        0x00FE,
        (
            '我所崇拜的尤莉亚大人……\n',
            '到底怎样才能见到呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是以参观为名\n',
            '混进城堡内最好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CE0')

    def _loc_2CA0(): pass

    label('loc_2CA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2CE0',
    )

    ChrTalk(
        0x00FE,
        (
            '我是王室亲卫队的粉丝。\n',
            '当然最喜欢其中的尤莉亚大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CE0(): pass

    label('loc_2CE0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2CE4
@scena.Code('func_0C_2CE4')
def func_0C_2CE4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 3, 0x1623)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2CF1',
    )

    Return()

    def _loc_2CF1(): pass

    label('loc_2CF1')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CE, 1, 0x1671)),
            Expr.Return,
        ),
        'loc_2E8B',
    )

    Fade(1000)
    SetChrPos(0x0101, 530, 0, 37370, 357)
    SetChrPos(0x0105, -430, 0, 38470, 357)
    SetChrPos(0x0104, -1680, 0, 36350, 357)
    SetChrPos(0x0108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160250907V公主殿下，您好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250908V#5P您辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250909V#041F#2P丹先生和阿尔兹先生\n',
            '执行任务也辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250910V#542F这次我想带艾丝蒂尔\n',
            '她们进城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250894V可以放行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3510')

    def _loc_2E8B(): pass

    label('loc_2E8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 6, 0x166E)),
            Expr.Return,
        ),
        'loc_3177',
    )

    Fade(1000)
    SetChrPos(0x0101, 530, 0, 37370, 357)
    SetChrPos(0x0105, -430, 0, 36000, 357)
    SetChrPos(0x0104, -1680, 0, 36350, 357)
    SetChrPos(0x0108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160250912V哟，是你们啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160250886V如果想见谁的话，\n',
            '我进去帮你们通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250887V#5P或者说你们想\n',
            '进去参观？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250888V#1015F#2P嗯，我们这次是为了\n',
            '游击士的工作来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x0105, -430, 0, 38470, 2000, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060250889V#048F#2P好久不见了。\n',
            '丹先生、阿尔兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160250890V公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250891V#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250892V#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250893V#542F我想带艾丝蒂尔\n',
            '她们进去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250894V可以放行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3510')

    def _loc_3177(): pass

    label('loc_3177')

    Fade(1000)
    SetChrPos(0x0101, 530, 0, 37370, 357)
    SetChrPos(0x0105, -430, 0, 36000, 357)
    SetChrPos(0x0104, -1680, 0, 36350, 357)
    SetChrPos(0x0108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160250881V咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250882V#5P你们是……\n',
            '在武术大会上获得了冠军的……?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250883V#1006F#2P嘿嘿，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250884V#071F#2P上次真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160250885V哈哈……\n',
            '今天有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160250886V如果想见谁的话，\n',
            '我进去帮你们通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250887V#5P或者说你们想\n',
            '进去参观？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250888V#1015F#2P嗯，我们这次是为了\n',
            '游击士的工作来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x0105, -430, 0, 38470, 2000, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060250889V#048F#2P好久不见了。\n',
            '丹先生、阿尔兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160250890V公主殿下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250891V#5P科洛蒂娅殿下！\n',
            '我不知道您回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250892V#041F#2P呵呵，这次是因为\n',
            '有事，顺路过来看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250893V#542F我想带艾丝蒂尔\n',
            '她们进去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250894V可以放行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3510(): pass

    label('loc_3510')

    ChrTalk(
        0x0008,
        (
            '#2160250895V当然没问题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250896V#5P谨遵殿下之名！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250897V#1016F#2P（不、不愧是科洛丝……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250898V#031F（哟，科洛丝很得人心呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250899V#070F#2P（难怪公爵会闹别扭了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_35ED')
    def lambda_35ED():
        OP_6D(70, 750, 44190, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35ED)

    @scena.Lambda('lambda_3605')
    def lambda_3605():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3605)

    @scena.Lambda('lambda_3615')
    def lambda_3615():
        OP_6E(438, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_3615)

    OP_8E(0x0009, 110, 750, 44500, 2000, 0x00)
    OP_8C(0x0009, 0, 400)
    WaitForThreadExit(0x0105, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#2170250900V科洛丝殿下和\n',
            '艾丝蒂尔小姐一行入内！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170250901V开门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3692')
    def lambda_3692():
        OP_6D(70, 3450, 44190, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3692)

    @scena.Lambda('lambda_36AA')
    def lambda_36AA():
        OP_67(0, 7620, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_36AA)

    @scena.Lambda('lambda_36C2')
    def lambda_36C2():
        OP_8E(0x0008, -2300, 750, 44600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_36C2)

    OP_8E(0x0009, 2450, 750, 44600, 2000, 0x00)
    OP_8C(0x0009, 180, 400)
    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x0008, 180, 400)
    OP_22(0x00D2, 0x00, 0x64)
    Sleep(2000)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x000001C2)
    OP_73(0x0000)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#1K#1P请进！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#2170250903V#1K#2P请进！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0105,
        (
            '#0060250904V#048F#5P呵呵……\n',
            '各位辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3784')
    def lambda_3784():
        OP_6D(530, 0, 40500, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3784)

    @scena.Lambda('lambda_379C')
    def lambda_379C():
        OP_67(0, 6000, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_379C)

    Sleep(500)

    OP_8C(0x0105, 135, 400)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0105,
        (
            '#0060250905V#040F#5P艾丝蒂尔\n',
            '我们进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250906V#1008F#6P嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    Fade(500)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 0, 0, 40470, 360)
    SetChrPos(0x0001, 0, 0, 40470, 360)
    SetChrPos(0x0002, 0, 0, 40470, 360)
    SetChrPos(0x0003, 0, 0, 40470, 360)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_A2(0x1623)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x38BE
@scena.Code('func_0D_38BE')
def func_0D_38BE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Return,
        ),
        'loc_38C6',
    )

    Return()

    def _loc_38C6(): pass

    label('loc_38C6')

    OP_A2(0x1627)

    Return()

# id: 0x000E offset: 0x38CA
@scena.Code('func_0E_38CA')
def func_0E_38CA():
    EventBegin(0x00)
    SetChrPos(0x0101, -310, 750, 49090, 180)
    SetChrPos(0x0105, 720, 750, 48910, 180)
    SetChrPos(0x0104, 990, 750, 50200, 180)
    SetChrPos(0x0108, -540, 750, 50010, 180)
    OP_6D(120, 750, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_395C')
    def lambda_395C():
        OP_8E(0x00FE, -210, 750, 44090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_395C)

    Sleep(200)

    @scena.Lambda('lambda_397C')
    def lambda_397C():
        OP_8E(0x00FE, 620, 750, 43910, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_397C)

    Sleep(200)

    @scena.Lambda('lambda_399C')
    def lambda_399C():
        OP_8E(0x00FE, 990, 750, 45200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_399C)

    Sleep(200)

    @scena.Lambda('lambda_39BC')
    def lambda_39BC():
        OP_8E(0x00FE, -540, 750, 45010, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_39BC)

    WaitForThreadExit(0x0108, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A70',
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
            TXT(0x00, '【◇听说了奈尔不在】\n'),
            TXT(0x01, '【◇没听说奈尔不在】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_3A64'),
        (0x00000001, 'loc_3A6A'),
        (-1, 'loc_3A70'),
    )

    def _loc_3A64(): pass

    label('loc_3A64')

    OP_A2(0x1680)

    Jump('loc_3A70')

    def _loc_3A6A(): pass

    label('loc_3A6A')

    OP_A3(0x1680)

    Jump('loc_3A70')

    def _loc_3A70(): pass

    label('loc_3A70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 0, 0x1680)),
            Expr.Return,
        ),
        'loc_3B46',
    )

    ChrTalk(
        0x0104,
        (
            '#0040251233V#030F哟，已经傍晚了啊……\n',
            '时间过得真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251234V#040F奈尔先生也该……\n',
            '也回通讯社了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251235V#1011F#6P啊，也是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251236V#070F#5P好。\n',
            '我们去通讯社看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C16')

    def _loc_3B46(): pass

    label('loc_3B46')

    ChrTalk(
        0x0104,
        (
            '#0040251233V#030F哟，已经傍晚了啊……\n',
            '时间过得真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251238V#040F只剩下利贝尔\n',
            '通讯社还没去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251239V#1006F#6P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251240V#070F#5P时间也差不多了。\n',
            '快去拜访一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C16(): pass

    label('loc_3C16')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_6D(50, 750, 44240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -60, 750, 44250, 180)
    SetChrPos(0x0001, -60, 750, 44250, 180)
    SetChrPos(0x0002, -60, 750, 44250, 180)
    SetChrPos(0x0003, -60, 750, 44250, 180)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x1627)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x3CC4
@scena.Code('func_0F_3CC4')
def func_0F_3CC4():
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    LoadEffect(0x01, 'map\\\\mpfire2.eff')
    LoadEffect(0x02, 'map\\\\mpkaji0.eff')
    OP_22(0x0087, 0x01, 0x50)
    OP_22(0x00AE, 0x01, 0x50)
    PlayEffect(0x02, 0xFF, 0x00FF, -150, 250, 42190, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 4900, 3600, 4050, 0, 0, 0, 1100, 1100, 1100, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -100, 3300, -2001, 0, 0, 0, 1400, 1700, 1400, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -7410, 3800, 18520, 0, 0, 0, 1600, 1800, 1600, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 6100, 3500, 18170, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -460, 3000, -2230, 0, 0, 0, 2200, 2200, 2200, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 4970, 3000, 4050, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -7410, 3400, 18520, 0, 0, 0, 1700, 1700, 1700, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 6100, 3000, 18170, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0010 offset: 0x3EE4
@scena.Code('func_10_3EE4')
def func_10_3EE4():
    SetChrPos(0x000A, -2680, 0, 22070, 315)
    SetChrPos(0x000B, -2480, 0, 20750, 180)
    SetChrPos(0x000C, -1140, 0, 22210, 0)
    SetChrPos(0x000D, -410, 0, 21460, 90)
    SetChrPos(0x000E, 310, 0, 20760, 135)
    SetChrPos(0x000F, 2220, 0, 22250, 270)
    SetChrPos(0x0010, 2740, 0, 22270, 270)
    SetChrPos(0x0011, 4170, 0, 21930, 225)
    SetChrPos(0x0012, 4430, 0, 21030, 135)
    SetChrPos(0x0013, -1230, 0, 19640, 0)
    SetChrPos(0x0014, 400, 0, 19130, 270)
    SetChrPos(0x0015, -3570, 0, 19150, 0)
    SetChrPos(0x0016, -3030, 0, 21970, 270)
    SetChrPos(0x0017, 2740, 0, 19290, 0)
    SetChrPos(0x0018, -2190, 0, 18550, 135)
    ClearChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    ClearChrFlags(0x000D, 0x0001)
    ClearChrFlags(0x000E, 0x0001)
    ClearChrFlags(0x000F, 0x0001)
    ClearChrFlags(0x0010, 0x0001)
    ClearChrFlags(0x0011, 0x0001)
    ClearChrFlags(0x0012, 0x0001)
    ClearChrFlags(0x0013, 0x0001)
    ClearChrFlags(0x0014, 0x0001)
    ClearChrFlags(0x0015, 0x0001)
    ClearChrFlags(0x0016, 0x0001)
    ClearChrFlags(0x0017, 0x0001)
    ClearChrFlags(0x0018, 0x0001)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)

    Return()

# id: 0x0011 offset: 0x404D
@scena.Code('func_11_404D')
def func_11_404D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_D2(0x002701C8, 0x002701CD, 0x02)
    OP_D2(0x002701C6, 0x002701CB, 0x03)
    OP_D2(0x002701C9, 0x002701CE, 0x04)
    OP_D2(0x00260003, 0x00260008, 0x05)
    OP_D2(0x002601A7, 0x002601AC, 0x06)
    OP_D2(0x002600A0, 0x002600A5, 0x07)
    OP_D2(0x002601A7, 0x002601AC, 0x08)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    SetChrPos(0x001B, -290, 0, 28660, 0)
    SetChrPos(0x001C, -1380, 0, 26510, 0)
    SetChrPos(0x0019, -70, 0, 24500, 0)
    SetChrPos(0x001A, 1500, 0, 26000, 0)
    SetChrChipByIndex(0x0019, 2)
    SetChrChipByIndex(0x001A, 3)
    SetChrChipByIndex(0x001B, 4)
    SetChrChipByIndex(0x001C, 5)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    OP_6D(640, 0, 18960, 0)
    OP_67(0, 7320, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(33000, 0)
    OP_6E(332, 0)
    LoadEffect(0x03, 'scraft\\sc007_10.eff')
    LoadEffect(0x04, 'map\\mp002_00.eff')
    OP_C8(0x0200, 0x0046, 'C_PLAC00._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_41BF')
    def lambda_41BF():
        OP_8E(0x00FE, -370, 0, 41570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_41BF)

    @scena.Lambda('lambda_41DA')
    def lambda_41DA():
        OP_8E(0x00FE, -1660, 0, 40910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_41DA)

    @scena.Lambda('lambda_41F5')
    def lambda_41F5():
        OP_8E(0x00FE, -280, 0, 39930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_41F5)

    @scena.Lambda('lambda_4210')
    def lambda_4210():
        OP_8E(0x00FE, 1050, 0, 41050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_4210)

    @scena.Lambda('lambda_422B')
    def lambda_422B():
        OP_6D(1440, 750, 44680, 6500)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_422B)

    @scena.Lambda('lambda_4243')
    def lambda_4243():
        OP_67(0, 3770, -10000, 6500)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4243)

    @scena.Lambda('lambda_425B')
    def lambda_425B():
        OP_6B(2380, 6500)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_425B)

    @scena.Lambda('lambda_426B')
    def lambda_426B():
        OP_6E(507, 6500)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_426B)

    WaitForThreadExit(0x001A, 0x0001)
    SetChrChipByIndex(0x001A, 7)
    SetChrSubChip(0x001A, 0)
    WaitForThreadExit(0x0019, 0x0003)

    ChrTalk(
        0x001C,
        (
            '#0220380209V#264F#6P哎呀……\n',
            '城门给关起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0170380210V#230F#6P嗯，这座王都是旧式建筑，\n',
            '所以也可以用人力来开关城门。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380211V当然，肯定也要费不少力气吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0210380212V#244F#4P呵呵……\n',
            '真是辛苦他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x001C, 90, 400)
    Sleep(300)

    ChrTalk(
        0x001C,
        (
            '#0220380213V#261F#6P那怎么办？\n',
            '我还是把『帕蒂尔·玛蒂尔』叫来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x001A, 0x0020)
    OP_8C(0x001A, 270, 400)
    Sleep(300)

    ChrTalk(
        0x001A,
        (
            '#0200380214V#254F#2P喂喂。\n',
            '把那种大家伙叫来的话，\n',
            '咱们不就没的玩了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380215V#252F这里就交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x001B, 135, 400)
    OP_8C(0x0019, 45, 400)

    ChrTalk(
        0x001C,
        (
            '#0220380216V#267F#6P你要怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0200380217V#252F#2P哼哼……好好看着吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x001A, 0x0020)
    OP_8C(0x001A, 0, 400)

    @scena.Lambda('lambda_44B1')
    def lambda_44B1():
        OP_6D(1050, 750, 46640, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44B1)

    @scena.Lambda('lambda_44C9')
    def lambda_44C9():
        OP_6B(1950, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44C9)

    @scena.Lambda('lambda_44D9')
    def lambda_44D9():
        ChrTurnDirection(0x00FE, 0x001A, 400)
        Yield()

        Jump('lambda_44D9')

    DispatchAsync2(0x001B, 0x0002, lambda_44D9)

    @scena.Lambda('lambda_44EA')
    def lambda_44EA():
        ChrTurnDirection(0x00FE, 0x001A, 400)
        Yield()

        Jump('lambda_44EA')

    DispatchAsync2(0x001C, 0x0002, lambda_44EA)

    @scena.Lambda('lambda_44FB')
    def lambda_44FB():
        ChrTurnDirection(0x00FE, 0x001A, 400)
        Yield()

        Jump('lambda_44FB')

    DispatchAsync2(0x0019, 0x0002, lambda_44FB)

    ClearChrFlags(0x001A, 0x0020)
    SetChrChipByIndex(0x001A, 3)
    OP_8E(0x001A, 300, 750, 45020, 2000, 0x00)
    TerminateThread(0x001B, 0x02)
    TerminateThread(0x001C, 0x02)
    TerminateThread(0x0019, 0x02)
    OP_8C(0x001B, 0, 400)
    OP_8C(0x0019, 0, 400)
    OP_8C(0x001C, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(250)
    SetChrSubChip(0x001A, 0)
    SetChrChipByIndex(0x001A, 8)
    OP_0D()
    Sleep(500)

    OP_99(0x001A, 0x00, 0x02, 0x000007D0)
    OP_9F(0x0020, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    SetChrPos(0x0020, 300, 750, 45020, 0)
    SetChrChipByIndex(0x0020, 8)
    SetChrSubChip(0x0020, 2)
    ClearChrFlags(0x0020, 0x0080)
    SetChrFlags(0x0020, 0x0004)
    SetChrFlags(0x0020, 0x0020)
    SetChrFlags(0x0020, 0x0040)
    OP_9F(0x0021, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    SetChrPos(0x0021, 300, 750, 45020, 0)
    SetChrChipByIndex(0x0021, 8)
    SetChrSubChip(0x0021, 2)
    ClearChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0021, 0x0004)
    SetChrFlags(0x0021, 0x0020)
    SetChrFlags(0x0021, 0x0040)
    Sleep(500)

    @scena.Lambda('lambda_45E7')
    def lambda_45E7():
        OP_6B(1800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_45E7)

    PlayEffect(0x03, 0x00, 0x001A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(
        0x001A,
        (
            '#0200380218V#257F#6P#30A#100W喝啊啊啊啊啊啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_82(0x00, 0x02)
    Sleep(1500)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ClearMapFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_4689')
    def lambda_4689():
        OP_99(0x00FE, 0x02, 0x06, 0x000007D0)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_4689)

    @scena.Lambda('lambda_4699')
    def lambda_4699():
        OP_99(0x00FE, 0x02, 0x06, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4699)

    @scena.Lambda('lambda_46A9')
    def lambda_46A9():
        OP_99(0x00FE, 0x02, 0x06, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_46A9)

    CreateThread(0x0020, 0x00, 0x00, 0x0012)
    CreateThread(0x0021, 0x00, 0x00, 0x0013)
    OP_22(0x0088, 0x00, 0x64)
    OP_7C(0x0000012C, 0x00000064, 0x00000BB8, 0x0000012C)
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    Fade(500)
    Sleep(300)

    CreateThread(0x001A, 0x03, 0x00, 0x0014)
    SetChrPos(0x001A, 0, 750, 45050, 0)
    SetChrPos(0x0020, 0, 750, 45050, 0)
    SetChrPos(0x0021, 0, 750, 45050, 0)
    OP_6D(0, 3940, 46030, 0)
    OP_67(0, 3560, -10000, 0)
    OP_6B(1690, 0)
    OP_6C(0, 0)
    OP_6E(566, 0)

    @scena.Lambda('lambda_4771')
    def lambda_4771():
        OP_6B(1890, 4000)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_4771)

    Sleep(450)

    OP_22(0x013C, 0x00, 0x64)
    Sleep(1350)

    OP_22(0x00F6, 0x00, 0x64)
    PlayEffect(0x04, 0x01, 0x00FF, 0, 500, 43120, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    OP_82(0x01, 0x02)
    WaitForThreadExit(0x001A, 0x0000)
    WaitForThreadExit(0x001A, 0x0003)
    Sleep(500)

    Fade(500)
    OP_6D(1000, 750, 44760, 0)
    OP_67(0, 3770, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(33000, 0)
    OP_6E(507, 0)
    SetMapFlags(0x00000010)
    SetChrPos(0x001A, 410, 750, 45020, 0)
    SetChrPos(0x0020, 300, 750, 45020, 0)
    SetChrPos(0x0021, 300, 750, 45020, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x001C,
        (
            '#0220380219V#261F#6P哇……！\n',
            '好厉害呀！瓦鲁特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0210380220V#241F#6P这就是泰斗流的奥义……寸劲吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0170380221V#231F#6P呵呵……\n',
            '威力还是这么惊人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    SetChrSubChip(0x001A, 0)
    SetChrChipByIndex(0x001A, 7)
    SetChrFlags(0x001A, 0x0020)
    Sleep(300)

    OP_8C(0x001A, 225, 400)
    Sleep(300)

    ChrTalk(
        0x001A,
        (
            '#0200380222V#250F#5P嘿嘿……\n',
            '雕虫小技，不值一提啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380223V#252F好，让我再把这扇门也轰开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4210._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x49A9
@scena.Code('func_12_49A9')
def func_12_49A9():
    OP_91(0x00FE, 0, 0, -500, 2000, 0x00)
    OP_91(0x00FE, 0, 0, 500, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x49D7
@scena.Code('func_13_49D7')
def func_13_49D7():
    OP_91(0x00FE, 0, 0, 500, 2000, 0x00)
    OP_91(0x00FE, 0, 0, -500, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0x4A05
@scena.Code('func_14_4A05')
def func_14_4A05():
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0010)
    OP_72(0x0001, 0x0800)
    OP_B0(0x0001, 0x19)
    OP_6F(0x0001, 1)
    OP_70(0x0001, 0x00000019)
    OP_73(0x0001)
    Sleep(500)

    OP_B0(0x0001, 0x23)
    OP_6F(0x0001, 25)
    OP_70(0x0001, 0x0000003C)
    OP_73(0x0001)
    OP_B0(0x0001, 0x28)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x0000008C)
    OP_73(0x0001)

    Return()

# id: 0x0015 offset: 0x4A59
@scena.Code('func_15_4A59')
def func_15_4A59():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 7, 0x203F)),
            Expr.Return,
        ),
        'loc_4AE6',
    )

    OP_6D(4310, 0, -4910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 4310, 0, -4910, 0)
    SetChrPos(0x0001, 4310, 0, -4910, 0)
    SetChrPos(0x0002, 4310, 0, -4910, 0)
    SetChrPos(0x0003, 4310, 0, -4910, 0)

    Jump('loc_4B67')

    def _loc_4AE6(): pass

    label('loc_4AE6')

    OP_6D(-2630, 0, -4930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -2630, 0, -4930, 0)
    SetChrPos(0x0001, -2630, 0, -4930, 0)
    SetChrPos(0x0002, -2630, 0, -4930, 0)
    SetChrPos(0x0003, -2630, 0, -4930, 0)

    def _loc_4B67(): pass

    label('loc_4B67')

    OP_69(0x0000, 0x00000000)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0016 offset: 0x4B76
@scena.Code('func_16_4B76')
def func_16_4B76():
    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    OP_D2(0x00290188, 0x0029018C, 0x02)
    OP_D2(0x00270110, 0x00270120, 0x08)
    OP_D2(0x00270111, 0x00270121, 0x09)
    OP_D2(0x00270130, 0x00270140, 0x0A)
    OP_D2(0x00270131, 0x00270141, 0x0B)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_4BD5'),
        (0x00000005, 'loc_4BEC'),
        (0x00000006, 'loc_4C03'),
        (0x00000007, 'loc_4C1A'),
        (-1, 'loc_4C31'),
    )

    def _loc_4BD5(): pass

    label('loc_4BD5')

    OP_D2(0x000701D0, 0x000701DC, 0x0C)
    OP_D2(0x000701D1, 0x000701DD, 0x0D)

    Jump('loc_4C31')

    def _loc_4BEC(): pass

    label('loc_4BEC')

    OP_D2(0x00070218, 0x00070224, 0x0C)
    OP_D2(0x00070219, 0x00070225, 0x0D)

    Jump('loc_4C31')

    def _loc_4C03(): pass

    label('loc_4C03')

    OP_D2(0x00070230, 0x0007023C, 0x0C)
    OP_D2(0x00070231, 0x0007023D, 0x0D)

    Jump('loc_4C31')

    def _loc_4C1A(): pass

    label('loc_4C1A')

    OP_D2(0x00070248, 0x00070254, 0x0C)
    OP_D2(0x00070249, 0x00070255, 0x0D)

    Jump('loc_4C31')

    def _loc_4C31(): pass

    label('loc_4C31')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_4C4A'),
        (0x00000005, 'loc_4C61'),
        (0x00000006, 'loc_4C78'),
        (0x00000007, 'loc_4C8F'),
        (-1, 'loc_4CA6'),
    )

    def _loc_4C4A(): pass

    label('loc_4C4A')

    OP_D2(0x000701D0, 0x000701DC, 0x0E)
    OP_D2(0x000701D1, 0x000701DD, 0x0F)

    Jump('loc_4CA6')

    def _loc_4C61(): pass

    label('loc_4C61')

    OP_D2(0x00070218, 0x00070224, 0x0E)
    OP_D2(0x00070219, 0x00070225, 0x0F)

    Jump('loc_4CA6')

    def _loc_4C78(): pass

    label('loc_4C78')

    OP_D2(0x00070230, 0x0007023C, 0x0E)
    OP_D2(0x00070231, 0x0007023D, 0x0F)

    Jump('loc_4CA6')

    def _loc_4C8F(): pass

    label('loc_4C8F')

    OP_D2(0x00070248, 0x00070254, 0x0E)
    OP_D2(0x00070249, 0x00070255, 0x0F)

    Jump('loc_4CA6')

    def _loc_4CA6(): pass

    label('loc_4CA6')

    Return()

# id: 0x0017 offset: 0x4CA7
@scena.Code('func_17_4CA7')
def func_17_4CA7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 4, 0x203C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 5, 0x203D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4CB4',
    )

    Return()

    def _loc_4CB4(): pass

    label('loc_4CB4')

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
        'loc_4CD4',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)
    FadeIn(0, 0)

    def _loc_4CD4(): pass

    label('loc_4CD4')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D33',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_4D71')

    def _loc_4D33(): pass

    label('loc_4D33')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D5A',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_4D71')

    def _loc_4D5A(): pass

    label('loc_4D5A')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_4D71(): pass

    label('loc_4D71')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D9D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_4DDB')

    def _loc_4D9D(): pass

    label('loc_4D9D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DC4',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_4DDB')

    def _loc_4DC4(): pass

    label('loc_4DC4')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_4DDB(): pass

    label('loc_4DDB')

    Sleep(1000)

    @scena.Lambda('lambda_4DE6')
    def lambda_4DE6():
        OP_6D(2450, 750, 48690, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4DE6)

    @scena.Lambda('lambda_4DFE')
    def lambda_4DFE():
        OP_67(0, 6680, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4DFE)

    @scena.Lambda('lambda_4E16')
    def lambda_4E16():
        OP_6B(2570, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4E16)

    @scena.Lambda('lambda_4E26')
    def lambda_4E26():
        OP_6C(33000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4E26)

    OP_6E(403, 3000)
    Sleep(1000)

    Fade(500)
    OP_6D(490, 0, 35190, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(32000, 0)
    OP_6E(358, 0)
    SetChrPos(0x0101, -760, 0, 34260, 0)
    SetChrPos(0x0102, 620, 0, 34280, 0)
    SetChrPos(0x00F8, -1040, 0, 32729, 0)
    SetChrPos(0x00F9, 600, 0, 32930, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380264V#1020F#6P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380265V#1044F#4P这……\n',
            '大概是徒手破坏后的痕迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380266V#1042F恐怕是『瘦狼』的绝技……',
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
        'loc_4FA1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380267V#074F啊啊……\n',
            '是零距离吐劲的奥义“寸劲”。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FA1(): pass

    label('loc_4FA1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FD4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380268V#055F真、真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FD4(): pass

    label('loc_4FD4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5007',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380269V#065F呜、呜啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5007(): pass

    label('loc_5007')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_503E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380270V#025F好惊人的破坏力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_503E(): pass

    label('loc_503E')

    ChrTalk(
        0x0101,
        (
            '#0010380271V#1007F#6P怎么可能……\n',
            '这也太强了吧…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380272V#1005F……啊！\n',
            '现在可不是钦佩的时候！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380273V必须要赶快追上他们──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(200)

    OP_22(0x0077, 0x00, 0x64)
    OP_22(0x0135, 0x01, 0x32)
    Sleep(200)

    OP_24(0x0135, 0x3C)
    Sleep(200)

    OP_24(0x0135, 0x46)
    Sleep(200)

    OP_24(0x0135, 0x50)
    Sleep(200)

    OP_24(0x0135, 0x5A)
    Sleep(200)

    OP_24(0x0135, 0x64)

    ChrTalk(
        0x0102,
        (
            '#0020380274V#1046F#4P艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_5165')
    def lambda_5165():
        OP_96(0x00FE, 0x00000834, 0x00000000, 0x00008458, 0x000000C8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5165)

    Sleep(50)

    @scena.Lambda('lambda_5188')
    def lambda_5188():
        OP_96(0x00FE, 0xFFFFF7CC, 0x00000000, 0x00008458, 0x000000C8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5188)

    CreateThread(0x001D, 0x00, 0x00, 0x001A)

    @scena.Lambda('lambda_51AD')
    def lambda_51AD():
        OP_96(0x00FE, 0xFFFFFB50, 0x00000000, 0x00007724, 0x000000C8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_51AD)

    Sleep(50)

    CreateThread(0x001E, 0x00, 0x00, 0x001B)

    @scena.Lambda('lambda_51D7')
    def lambda_51D7():
        OP_96(0x00FE, 0x000004B0, 0x00000000, 0x00007724, 0x000000C8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_51D7)

    CreateThread(0x001F, 0x00, 0x00, 0x001C)
    SetChrPos(0x001D, 0, 12000, 38000, 180)
    SetChrPos(0x001E, 4000, 12000, 40000, 180)
    SetChrPos(0x001F, -4000, 12000, 40000, 180)
    SetChrChipByIndex(0x001D, 2)
    SetChrChipByIndex(0x001E, 2)
    SetChrChipByIndex(0x001F, 2)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    WaitForThreadExit(0x001D, 0x0000)
    WaitForThreadExit(0x001E, 0x0000)
    WaitForThreadExit(0x001F, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    Fade(500)
    ClearMapFlags(0x00000010)
    OP_6D(2190, 3130, 40810, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    SetChrPos(0x0101, -670, 0, 30300, 0)
    SetChrPos(0x0102, 950, 0, 30290, 0)
    SetChrPos(0x00F8, -990, 0, 28900, 0)
    SetChrPos(0x00F9, 1050, 0, 29020, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 8)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 10)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F8, 12)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 14)
    CreateThread(0x001D, 0x03, 0x00, 0x0019)
    CreateThread(0x001E, 0x03, 0x00, 0x0019)
    CreateThread(0x001F, 0x03, 0x00, 0x0019)

    @scena.Lambda('lambda_533D')
    def lambda_533D():
        OP_8F(0x00FE, 0, 2500, 38000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_533D)

    Sleep(200)

    @scena.Lambda('lambda_535D')
    def lambda_535D():
        OP_8F(0x00FE, 4000, 2500, 40000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_535D)

    Sleep(200)

    @scena.Lambda('lambda_537D')
    def lambda_537D():
        OP_8F(0x00FE, -4000, 2500, 40000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_537D)

    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_53A2')
    def lambda_53A2():
        OP_6D(2080, 0, 40810, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_53A2)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0101, 0x0002)
    OP_23(0x0077)
    Sleep(1000)

    @scena.Lambda('lambda_53D0')
    def lambda_53D0():
        OP_6D(2710, 0, 37470, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_53D0)

    @scena.Lambda('lambda_53E8')
    def lambda_53E8():
        OP_67(0, 4840, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53E8)

    @scena.Lambda('lambda_5400')
    def lambda_5400():
        OP_6B(3540, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5400)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010380275V#1005F#6P竟然出现在这里……！',
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
        'loc_5470',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380276V#054F毁掉它们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_54D1')

    def _loc_5470(): pass

    label('loc_5470')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54A2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380277V#076F击毁它们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_54D1')

    def _loc_54A2(): pass

    label('loc_54A2')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54D1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380278V#024F收拾它们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54D1(): pass

    label('loc_54D1')

    @scena.Lambda('lambda_54D7')
    def lambda_54D7():
        OP_6D(730, 0, 34730, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_54D7)

    @scena.Lambda('lambda_54EF')
    def lambda_54EF():
        OP_67(0, 5690, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_54EF)

    @scena.Lambda('lambda_5507')
    def lambda_5507():
        OP_6B(2580, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5507)

    @scena.Lambda('lambda_5517')
    def lambda_5517():
        OP_91(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_5517)

    @scena.Lambda('lambda_5532')
    def lambda_5532():
        OP_91(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0000, lambda_5532)

    @scena.Lambda('lambda_554D')
    def lambda_554D():
        OP_91(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0000, lambda_554D)

    @scena.Lambda('lambda_5568')
    def lambda_5568():
        OP_91(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5568)

    @scena.Lambda('lambda_5583')
    def lambda_5583():
        OP_91(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_5583)

    @scena.Lambda('lambda_559E')
    def lambda_559E():
        OP_91(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_559E)

    @scena.Lambda('lambda_55B9')
    def lambda_55B9():
        OP_91(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_55B9)

    Sleep(200)

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    TerminateThread(0x001D, 0x00)
    TerminateThread(0x001E, 0x00)
    TerminateThread(0x001F, 0x00)
    Battle(0x00000550, 0x00000000, 0x00, 0x0000, 0xFF)
    Call(0, 0x0018)

    Return()

# id: 0x0018 offset: 0x560D
@scena.Code('func_18_560D')
def func_18_560D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x001D, 0x00)
    TerminateThread(0x001E, 0x00)
    TerminateThread(0x001F, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    LoadEffect(0x01, 'map\\\\mpsibuk.eff')
    LoadEffect(0x00, 'battle\\\\btbomb00.eff')
    OP_D2(0x00290188, 0x0029018C, 0x02)
    SetChrPos(0x0101, -990, 0, 32820, 270)
    SetChrPos(0x0102, 450, 0, 32800, 90)
    SetChrPos(0x00F8, -1100, 0, 31260, 270)
    SetChrPos(0x00F9, 460, 0, 31240, 90)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 8)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 10)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F8, 12)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 14)
    OP_6D(1820, 0, 35140, 0)
    OP_67(0, 7170, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(44000, 0)
    OP_6E(399, 0)
    SetChrChipByIndex(0x001D, 2)
    SetChrChipByIndex(0x001E, 2)
    SetChrChipByIndex(0x001F, 2)
    CreateThread(0x001D, 0x03, 0x00, 0x0019)
    CreateThread(0x001E, 0x03, 0x00, 0x0019)
    CreateThread(0x001F, 0x03, 0x00, 0x0019)
    SetChrPos(0x001D, 6510, 1500, 36000, 270)
    SetChrPos(0x001E, 6700, 1200, 31600, 270)
    SetChrPos(0x001F, -5430, 1700, 34200, 90)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)

    @scena.Lambda('lambda_577E')
    def lambda_577E():
        OP_6D(40, 0, 32430, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_577E)

    @scena.Lambda('lambda_5796')
    def lambda_5796():
        OP_67(0, 6230, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5796)

    @scena.Lambda('lambda_57AE')
    def lambda_57AE():
        OP_6B(2800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_57AE)

    CreateThread(0x001D, 0x00, 0x00, 0x001D)
    CreateThread(0x001E, 0x00, 0x00, 0x001E)
    CreateThread(0x001F, 0x00, 0x00, 0x001F)
    FadeIn(1000, 0)
    WaitForThreadExit(0x001D, 0x0001)
    WaitForThreadExit(0x001E, 0x0001)
    WaitForThreadExit(0x001F, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Fade(500)
    OP_6D(-10, 0, 32470, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380279V#1005F#5P呼……\n',
            '这、这可不是开玩笑的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 225, 500)

    ChrTalk(
        0x0102,
        (
            '#0020380280V#1042F#5P没时间了……\n',
            '总之先要进去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x203D)
    Sleep(100)

    Fade(500)
    OP_6D(-480, 0, 33720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -480, 0, 33720, 0)
    SetChrPos(0x0001, -480, 0, 33720, 0)
    SetChrPos(0x0002, -480, 0, 33720, 0)
    SetChrPos(0x0003, -480, 0, 33720, 0)
    OP_0D()
    Call(0, 0x000F)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0019 offset: 0x5974
@scena.Code('func_19_5974')
def func_19_5974():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5989',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_19_5974')

    def _loc_5989(): pass

    label('loc_5989')

    Return()

# id: 0x001A offset: 0x598A
@scena.Code('func_1A_598A')
def func_1A_598A():
    PlayEffect(0x00, 0xFF, 0x00FF, 2200, 0, 36450, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 1030, 0, 34940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 80, 0, 33190, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -1300, 0, 31960, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -2130, 0, 30270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    Return()

# id: 0x001B offset: 0x5AC6
@scena.Code('func_1B_5AC6')
def func_1B_5AC6():
    PlayEffect(0x00, 0xFF, 0x00FF, -1840, 0, 36190, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -580, 0, 34220, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 330, 0, 32790, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 1800, 0, 31190, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 2680, 0, 30010, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    Return()

# id: 0x001C offset: 0x5C02
@scena.Code('func_1C_5C02')
def func_1C_5C02():
    PlayEffect(0x00, 0xFF, 0x00FF, -80, 0, 36860, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 30, 0, 34690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 60, 0, 32710, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 210, 0, 30920, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, 60, 0, 29140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x01F7, 0x00, 0x64)
    Sleep(100)

    Return()

# id: 0x001D offset: 0x5D3E
@scena.Code('func_1D_5D3E')
def func_1D_5D3E():
    TerminateThread(0x00FE, 0x03)
    SetChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_5D4D')
    def lambda_5D4D():
        OP_D1(254, 0, 90000, -45000, 500)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_5D4D)

    TerminateThread(0x00FE, 0x03)

    @scena.Lambda('lambda_5D6B')
    def lambda_5D6B():
        OP_8F(0x00FE, 6510, -4000, 36000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5D6B)

    PlayEffect(0x00, 0x00, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x00, 0x01, 0x00FE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x00, 0x00, 0x00FE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x00, 0x01, 0x00FE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_5E6E')
    def lambda_5E6E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5E6E)

    OP_22(0x00DC, 0x00, 0x64)
    PlayEffect(0x01, 0x00, 0x00FE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 2, 2, 2, 0)
    Sleep(200)

    SetChrFlags(0x00FE, 0x0080)
    OP_82(0x00, 0x02)

    Return()

# id: 0x001E offset: 0x5EC2
@scena.Code('func_1E_5EC2')
def func_1E_5EC2():
    Sleep(400)

    TerminateThread(0x00FE, 0x03)
    SetChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_5ED6')
    def lambda_5ED6():
        OP_D1(254, 0, 90000, -45000, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5ED6)

    TerminateThread(0x00FE, 0x03)

    @scena.Lambda('lambda_5EF4')
    def lambda_5EF4():
        OP_8F(0x00FE, 6700, -4000, 31600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5EF4)

    PlayEffect(0x00, 0x02, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x00, 0x03, 0x00FE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    Sleep(250)

    PlayEffect(0x00, 0x02, 0x00FE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(250)

    PlayEffect(0x00, 0x03, 0x00FE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0001)
    PlayEffect(0x01, 0x02, 0x00FE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 2, 2, 2, 0)
    SetChrFlags(0x00FE, 0x0080)
    OP_82(0x02, 0x02)

    Return()

# id: 0x001F offset: 0x602F
@scena.Code('func_1F_602F')
def func_1F_602F():
    Sleep(600)

    TerminateThread(0x00FE, 0x03)
    SetChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_6043')
    def lambda_6043():
        OP_D1(254, 0, 90000, -45000, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6043)

    TerminateThread(0x00FE, 0x03)

    @scena.Lambda('lambda_6061')
    def lambda_6061():
        OP_8F(0x00FE, -7000, -4000, 34200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_6061)

    PlayEffect(0x00, 0x04, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(250)

    PlayEffect(0x00, 0x05, 0x00FE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x00, 0x04, 0x00FE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(350)

    PlayEffect(0x00, 0x05, 0x00FE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_6164')
    def lambda_6164():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_6164)

    PlayEffect(0x01, 0x04, 0x00FE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 2, 2, 2, 0)
    Sleep(200)

    SetChrFlags(0x00FE, 0x0080)
    OP_82(0x04, 0x02)

    Return()

# id: 0x0020 offset: 0x61B3
@scena.Code('func_20_61B3')
def func_20_61B3():
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
        (0x00000000, 'loc_622D'),
        (0x00000001, 'loc_6233'),
        (-1, 'loc_6239'),
    )

    def _loc_622D(): pass

    label('loc_622D')

    OP_A2(0x1200)

    Jump('loc_6239')

    def _loc_6233(): pass

    label('loc_6233')

    OP_A2(0x1201)

    Jump('loc_6239')

    def _loc_6239(): pass

    label('loc_6239')

    Return()

# id: 0x0021 offset: 0x623A
@scena.Code('func_21_623A')
def func_21_623A():
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

# id: 0x0022 offset: 0x6293
@scena.Code('func_22_6293')
def func_22_6293():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_62CB')
    def lambda_62CB():
        OP_6D(-13180, -1000, 19320, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_62CB)

    @scena.Lambda('lambda_62E3')
    def lambda_62E3():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_62E3)

    @scena.Lambda('lambda_62F3')
    def lambda_62F3():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_62F3)

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
        'loc_638B',
    )

    OP_C0(0x0E, 0x0000002D, 0xFFFFD490, 0x00000000, 0x00004C4A, 0x0000010E, 0xFFFFC4BE, 0xFFFFF63C, 0x00004A4C)
    OP_6D(-9930, 0, 19230, 0)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_639A')

    def _loc_638B(): pass

    label('loc_638B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_639A',
    )

    EventEnd(0x01)

    def _loc_639A(): pass

    label('loc_639A')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
