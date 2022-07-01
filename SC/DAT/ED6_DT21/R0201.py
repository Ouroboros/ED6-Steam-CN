import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '阿斯顿队长'),
    TXT(0x02, '士兵'),
    TXT(0x03, '士兵'),
    TXT(0x04, '士兵'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '士兵'),
    TXT(0x09, '士兵'),
    TXT(0x0A, '士兵'),
    TXT(0x0B, '士兵'),
    TXT(0x0C, '士兵'),
    TXT(0x0D, '士兵'),
    TXT(0x0E, '雾调整'),
    TXT(0x0F, '洛连特方向'),
    TXT(0x10, '威尔特桥·关所方向'),
    TXT(0x11, '帕赛尔农场方向'),
    TXT(0x12, '窃魂兽'),
    TXT(0x13, ''),
    TXT(0x14, ''),
    TXT(0x15, ''),
    TXT(0x16, ''),
    TXT(0x17, ''),
    TXT(0x18, ''),
    TXT(0x19, ''),
    TXT(0x1A, ''),
    TXT(0x1B, ''),
    TXT(0x1C, ''),
    TXT(0x1D, ''),
    TXT(0x1E, ''),
    TXT(0x1F, ''),
    TXT(0x20, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0201.x'
    header.mapIndex       = 22
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3145
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
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10180._CH', 'ED6_DT09/CH10180P._CP'),
        ('ED6_DT09/CH10181._CH', 'ED6_DT09/CH10181P._CP'),
        ('ED6_DT09/CH10260._CH', 'ED6_DT09/CH10260P._CP'),
        ('ED6_DT09/CH10261._CH', 'ED6_DT09/CH10261P._CP'),
        ('ED6_DT09/CH10210._CH', 'ED6_DT09/CH10210P._CP'),
        ('ED6_DT09/CH10211._CH', 'ED6_DT09/CH10211P._CP'),
        ('ED6_DT29/CH12090._CH', 'ED6_DT29/CH12090P._CP'),
        ('ED6_DT29/CH12091._CH', 'ED6_DT29/CH12091P._CP'),
        ('ED6_DT29/CH12130._CH', 'ED6_DT29/CH12130P._CP'),
        ('ED6_DT29/CH12131._CH', 'ED6_DT29/CH12131P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT29/CH12400._CH', 'ED6_DT29/CH12400P._CP'),
        ('ED6_DT29/CH12401._CH', 'ED6_DT29/CH12401P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            x                   = -131580,
            z                   = 0,
            y                   = -18130,
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
            x                   = -224350,
            z                   = 20,
            y                   = -16180,
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
            x                   = -184980,
            z                   = 0,
            y                   = -81290,
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
            x                   = -186100,
            z                   = 40,
            y                   = -22120,
            direction           = 213,
            word_0E             = 14,
            dword_10            = 917504,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x36A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -160000,
            z           = 200,
            y           = -2000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -161000,
            z           = 0,
            y           = -21000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -155000,
            z           = 0,
            y           = -44000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -178000,
            z           = 500,
            y           = -29000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -190000,
            z           = 0,
            y           = -39000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -205000,
            z           = 200,
            y           = -55000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -193000,
            z           = 200,
            y           = -2000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -207000,
            z           = 200,
            y           = -6000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -198000,
            z           = 300,
            y           = -47000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180000,
            z           = -500,
            y           = -58000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -159000,
            z           = 200,
            y           = -59000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180000,
            z           = 0,
            y           = -5000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -172000,
            z           = 200,
            y           = -43000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0079,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x4D6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -186100,
            y           = -1040,
            z           = -22120,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x4F6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -176080,
            triggerZ            = 50,
            triggerY            = 11940,
            triggerRange        = 1000,
            actorX              = -176140,
            actorZ              = 1050,
            actorY              = 12680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -211720,
            triggerZ            = 20,
            triggerY            = -56010,
            triggerRange        = 1000,
            actorX              = -211660,
            actorZ              = 20,
            actorY              = -56570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -145080,
            triggerZ            = 40,
            triggerY            = -50920,
            triggerRange        = 1000,
            actorX              = -144640,
            actorZ              = 40,
            actorY              = -51360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -179550,
            triggerZ            = 0,
            triggerY            = -15360,
            triggerRange        = 1500,
            actorX              = -179550,
            actorZ              = 1500,
            actorY              = -15360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x586
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A0',
    )

    Event(0, 0x000A)

    Jump('loc_5B6')

    def _loc_5A0(): pass

    label('loc_5A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5B2',
    )

    Event(0, 0x0009)

    Jump('loc_5B6')

    def _loc_5B2(): pass

    label('loc_5B2')

    Event(0, 0x0008)

    def _loc_5B6(): pass

    label('loc_5B6')

    Jump('loc_5C9')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C9',
    )

    Event(0, 0x000B)

    def _loc_5C9(): pass

    label('loc_5C9')

    Return()

# id: 0x0001 offset: 0x5CA
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFB54B0, 0xFFFD8730, 0x0023000C)

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 2, 0x1922)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F7',
    )

    OP_6F(0x0000, 0)

    Jump('loc_5FE')

    def _loc_5F7(): pass

    label('loc_5F7')

    OP_6F(0x0000, 60)

    def _loc_5FE(): pass

    label('loc_5FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 3, 0x1923)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_610',
    )

    OP_6F(0x0001, 0)

    Jump('loc_617')

    def _loc_610(): pass

    label('loc_610')

    OP_6F(0x0001, 60)

    def _loc_617(): pass

    label('loc_617')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 4, 0x1924)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_629',
    )

    OP_6F(0x0002, 0)

    Jump('loc_630')

    def _loc_629(): pass

    label('loc_629')

    OP_6F(0x0002, 60)

    def _loc_630(): pass

    label('loc_630')

    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_720',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_66A',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)
    OP_C4(0x00, 0x00000004)

    Jump('loc_720')

    def _loc_66A(): pass

    label('loc_66A')

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x00013880, 0x00000000)
    CreateThread(0x0015, 0x00, 0x00, 0x0003)

    def _loc_720(): pass

    label('loc_720')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_73E',
    )

    SetChrFlags(0x0019, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_750')

    def _loc_73E(): pass

    label('loc_73E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x031F, 5, 0x18FD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_750',
    )

    ClearChrFlags(0x0019, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_750(): pass

    label('loc_750')

    ExecExpressionWithValue(
        0x0019,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0021,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0022,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0023,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0024,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x7EB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_800',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_800(): pass

    label('loc_800')

    Return()

# id: 0x0003 offset: 0x801
@scena.Code('func_03_801')
def func_03_801():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_898',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x22AB0),
            Expr.Neg,
            (Expr.PushValueByIndex, 0x65),
            Expr.Sub,
            (Expr.PushLong, 0xA),
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_835',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_84A')

    def _loc_835(): pass

    label('loc_835')

    If(
        (
            (Expr.PushValueByIndex, 0x37),
            (Expr.PushLong, 0x7D00),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_84A',
    )

    ExecExpressionWithVar(
        0x37,
        (
            (Expr.PushLong, 0x7D00),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_84A(): pass

    label('loc_84A')

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x22AB0),
            Expr.Neg,
            (Expr.PushValueByIndex, 0x65),
            Expr.Sub,
            (Expr.PushLong, 0xA),
            Expr.Mul,
            (Expr.PushLong, 0x13880),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x13880),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_87B',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_890')

    def _loc_87B(): pass

    label('loc_87B')

    If(
        (
            (Expr.PushValueByIndex, 0x38),
            (Expr.PushLong, 0x222E0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_890',
    )

    ExecExpressionWithVar(
        0x38,
        (
            (Expr.PushLong, 0x222E0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_890(): pass

    label('loc_890')

    Sleep(10)

    Jump('func_03_801')

    def _loc_898(): pass

    label('loc_898')

    Return()

# id: 0x0004 offset: 0x899
@scena.Code('func_04_899')
def func_04_899():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x031F, 5, 0x18FD)),
            Expr.Return,
        ),
        'loc_8A1',
    )

    Return()

    def _loc_8A1(): pass

    label('loc_8A1')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_986'),
        (-1, 'loc_9A9'),
    )

    def _loc_986(): pass

    label('loc_986')

    Fade(500)
    OP_89(0x0000, -191670, 190, -27970, 45)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_9A9(): pass

    label('loc_9A9')

    Battle(0x00000EEB, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -191670, 190, -27970, 45)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_9E2'),
        (0x00000001, 'loc_9E5'),
        (-1, 'loc_9E8'),
    )

    def _loc_9E2(): pass

    label('loc_9E2')

    EventEnd(0x00)

    Return()

    def _loc_9E5(): pass

    label('loc_9E5')

    OP_B4(0x00)

    Return()

    def _loc_9E8(): pass

    label('loc_9E8')

    EventBegin(0x01)
    SetChrFlags(0x0019, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x18FD)
    OP_28(0x00AF, 0x04, 0x10)
    OP_28(0x00AF, 0x04, 0x02)
    OP_28(0x00AF, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0xA54
@scena.Code('func_05_A54')
def func_05_A54():
    UnlockAchievement(0x02, 0xC2, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 2, 0x1922)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B31',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['轰雷剑'], 1)"),
            Expr.Return,
        ),
        'loc_AC8',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['轰雷剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1922)

    Jump('loc_B2E')

    def _loc_AC8(): pass

    label('loc_AC8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['轰雷剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['轰雷剑']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_B2E(): pass

    label('loc_B2E')

    Jump('loc_B62')

    def _loc_B31(): pass

    label('loc_B31')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_B62(): pass

    label('loc_B62')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xB70
@scena.Code('func_06_B70')
def func_06_B70():
    UnlockAchievement(0x02, 0xC3, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 3, 0x1923)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C4D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_BE4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1923)

    Jump('loc_C4A')

    def _loc_BE4(): pass

    label('loc_BE4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_C4A(): pass

    label('loc_C4A')

    Jump('loc_C7E')

    def _loc_C4D(): pass

    label('loc_C4D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_C7E(): pass

    label('loc_C7E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xC8C
@scena.Code('func_07_C8C')
def func_07_C8C():
    UnlockAchievement(0x02, 0xC4, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0324, 4, 0x1924)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D69',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_D00',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1924)

    Jump('loc_D66')

    def _loc_D00(): pass

    label('loc_D00')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_D66(): pass

    label('loc_D66')

    Jump('loc_D9A')

    def _loc_D69(): pass

    label('loc_D69')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_D9A(): pass

    label('loc_D9A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xDA8
@scena.Code('func_08_DA8')
def func_08_DA8():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DD2',
    )

    Call(0, 0x0027)
    FadeIn(0, 0)
    Call(0, 0x0028)

    def _loc_DD2(): pass

    label('loc_DD2')

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -134560, 0, -17700, 270)
    SetChrPos(0x0103, -134560, 0, -18700, 270)
    SetChrPos(0x00F8, -133560, 0, -17450, 270)
    SetChrPos(0x00F9, -133560, 0, -18950, 270)

    @scena.Lambda('lambda_0E59')
    def lambda_0E59():
        OP_90(0x00FE, -7000, 0, 0, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E59)

    Sleep(100)

    @scena.Lambda('lambda_0E79')
    def lambda_0E79():
        OP_90(0x00FE, -7000, 0, 0, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0E79)

    Sleep(200)

    @scena.Lambda('lambda_0E99')
    def lambda_0E99():
        OP_90(0x00FE, -6500, 0, 0, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0E99)

    Sleep(100)

    @scena.Lambda('lambda_0EB9')
    def lambda_0EB9():
        OP_90(0x00FE, -6500, 0, 0, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0EB9)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010281161V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F04')
    def lambda_0F04():
        OP_8E(0x00FE, -147560, 0, -17700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F04)

    Sleep(100)

    @scena.Lambda('lambda_0F24')
    def lambda_0F24():
        OP_8E(0x00FE, -147610, 0, -18850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0F24)

    Sleep(200)

    @scena.Lambda('lambda_0F44')
    def lambda_0F44():
        OP_8E(0x00FE, -145740, 0, -17340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F44)

    Sleep(100)

    @scena.Lambda('lambda_0F64')
    def lambda_0F64():
        OP_8E(0x00FE, -145870, 0, -18620, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0F64)

    @scena.Lambda('lambda_0F7F')
    def lambda_0F7F():
        OP_6D(-146390, 0, -17590, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F7F)

    @scena.Lambda('lambda_0F97')
    def lambda_0F97():
        OP_6B(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F97)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0103, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_8C(0x0101, 295, 400)
    Sleep(50)

    OP_8C(0x0103, 270, 400)
    Sleep(30)

    OP_8C(0x00F8, 270, 400)
    Sleep(50)

    OP_8C(0x00F9, 240, 400)
    Sleep(400)

    OP_8C(0x0101, 270, 400)
    Sleep(50)

    OP_8C(0x0103, 295, 400)
    Sleep(30)

    OP_8C(0x00F8, 240, 400)
    Sleep(50)

    OP_8C(0x00F9, 270, 400)
    Sleep(400)

    OP_8C(0x0101, 240, 400)
    Sleep(50)

    OP_8C(0x0103, 240, 400)
    Sleep(30)

    OP_8C(0x00F8, 270, 400)
    Sleep(50)

    OP_8C(0x00F9, 295, 400)
    Sleep(400)

    OP_8C(0x0101, 270, 400)
    Sleep(50)

    OP_8C(0x0103, 295, 400)
    Sleep(30)

    OP_8C(0x00F8, 295, 400)
    Sleep(50)

    OP_8C(0x00F9, 240, 400)
    Sleep(400)

    OP_8C(0x0101, 90, 400)
    Sleep(50)

    OP_8C(0x0103, 90, 400)
    Sleep(30)

    OP_8C(0x00F8, 270, 400)
    Sleep(50)

    OP_8C(0x00F9, 270, 400)
    Sleep(400)

    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10EA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281162V#560F哇……\n',
            '一下子就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E3')

    def _loc_10EA(): pass

    label('loc_10EA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1128',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281163V#051F嘿……\n',
            '突然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E3')

    def _loc_1128(): pass

    label('loc_1128')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1168',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281164V#030F嗯……\n',
            '一下子就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E3')

    def _loc_1168(): pass

    label('loc_1168')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281165V#048F呵呵……\n',
            '忽然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E3')

    def _loc_11A8(): pass

    label('loc_11A8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11E3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281166V#070F呼……\n',
            '突然就明朗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E3(): pass

    label('loc_11E3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_122B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281167V#061F雾的覆盖范围\n',
            '似乎就到这里为止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1348')

    def _loc_122B(): pass

    label('loc_122B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1273',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281168V#051F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1348')

    def _loc_1273(): pass

    label('loc_1273')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12BB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281169V#030F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1348')

    def _loc_12BB(): pass

    label('loc_12BB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1303',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281170V#048F雾的覆盖范围\n',
            '似乎就到这里为止呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1348')

    def _loc_1303(): pass

    label('loc_1303')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1348',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281171V#070F雾的覆盖范围\n',
            '似乎就到这里为止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1348(): pass

    label('loc_1348')

    ChrTalk(
        0x0103,
        (
            '#0030281172V#026F米尔西街道，从洛连特出发\n',
            '大约８０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281173V#022F浓雾中有魔兽在游荡，\n',
            '情况相当危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281174V#1015F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281175V调查完其它地方后，\n',
            '必须赶快向爱娜姐报告才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x180F)
    OP_28(0x008F, 0x02, 0x0010)
    OP_28(0x008F, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x143A
@scena.Code('func_09_143A')
def func_09_143A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1464',
    )

    Call(0, 0x0027)
    FadeIn(0, 0)
    Call(0, 0x0028)

    def _loc_1464(): pass

    label('loc_1464')

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -137560, 0, -17700, 270)
    SetChrPos(0x0103, -137560, 0, -18700, 270)
    SetChrPos(0x00F8, -136560, 0, -17450, 270)
    SetChrPos(0x00F9, -136560, 0, -18950, 270)

    @scena.Lambda('lambda_14EB')
    def lambda_14EB():
        OP_8E(0x00FE, -147560, 0, -17700, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14EB)

    Sleep(100)

    @scena.Lambda('lambda_150B')
    def lambda_150B():
        OP_8E(0x00FE, -147610, 0, -18850, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_150B)

    Sleep(200)

    @scena.Lambda('lambda_152B')
    def lambda_152B():
        OP_8E(0x00FE, -145740, 0, -17340, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_152B)

    Sleep(100)

    @scena.Lambda('lambda_154B')
    def lambda_154B():
        OP_8E(0x00FE, -145870, 0, -18620, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_154B)

    @scena.Lambda('lambda_1566')
    def lambda_1566():
        OP_6D(-146390, 0, -17590, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1566)

    @scena.Lambda('lambda_157E')
    def lambda_157E():
        OP_6B(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_157E)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15D3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281176V#061F嘿嘿，已经晴了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16BA')

    def _loc_15D3(): pass

    label('loc_15D3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_160A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281177V#051F嘿，已经晴了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16BA')

    def _loc_160A(): pass

    label('loc_160A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1645',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281178V#030F嗯，好像已经晴了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16BA')

    def _loc_1645(): pass

    label('loc_1645')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1680',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281179V#048F……似乎已经晴了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16BA')

    def _loc_1680(): pass

    label('loc_1680')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16BA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281180V#070F嗯……已经没有雾了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16BA(): pass

    label('loc_16BA')

    ChrTalk(
        0x0103,
        (
            '#0030281172V#026F米尔西街道，距离洛连特\n',
            '大约８０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281173V#022F浓雾中有魔兽在游荡，\n',
            '情况相当危险呢。',
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
        'loc_17D4',
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
            TXT(0x00, '【◇调查过玛鲁加山道】\n'),
            TXT(0x01, '【◇调查过艾利兹街道】\n'),
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
        (0x00000000, 'loc_17C2'),
        (0x00000001, 'loc_17CB'),
        (-1, 'loc_17D4'),
    )

    def _loc_17C2(): pass

    label('loc_17C2')

    OP_A3(0x180E)
    OP_A2(0x1810)

    Jump('loc_17D4')

    def _loc_17CB(): pass

    label('loc_17CB')

    OP_A2(0x180E)
    OP_A3(0x1810)

    Jump('loc_17D4')

    def _loc_17D4(): pass

    label('loc_17D4')

    ChrTurnDirection(0x0101, 0x0103, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Return,
        ),
        'loc_1846',
    )

    ChrTalk(
        0x0101,
        (
            '#0010281183V#1006F#5P嗯……\n',
            '就向爱娜姐报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281184V接下来，只剩下\n',
            '艾利兹街道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A7')

    def _loc_1846(): pass

    label('loc_1846')

    ChrTalk(
        0x0101,
        (
            '#0010281183V#1006F#5P嗯……\n',
            '就向爱娜姐报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281186V接下来，只剩下\n',
            '玛鲁加山道了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A7(): pass

    label('loc_18A7')

    OP_A2(0x180F)
    OP_28(0x008F, 0x02, 0x0010)
    OP_28(0x008F, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x18B9
@scena.Code('func_0A_18B9')
def func_0A_18B9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18E3',
    )

    Call(0, 0x0027)
    FadeIn(0, 0)
    Call(0, 0x0028)

    def _loc_18E3(): pass

    label('loc_18E3')

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -137560, 0, -17700, 270)
    SetChrPos(0x0103, -137560, 0, -18700, 270)
    SetChrPos(0x00F8, -136560, 0, -17450, 270)
    SetChrPos(0x00F9, -136560, 0, -18950, 270)

    @scena.Lambda('lambda_196A')
    def lambda_196A():
        OP_8E(0x00FE, -147560, 0, -17700, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_196A)

    Sleep(100)

    @scena.Lambda('lambda_198A')
    def lambda_198A():
        OP_8E(0x00FE, -147610, 0, -18850, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_198A)

    Sleep(200)

    @scena.Lambda('lambda_19AA')
    def lambda_19AA():
        OP_8E(0x00FE, -145740, 0, -17340, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_19AA)

    Sleep(100)

    @scena.Lambda('lambda_19CA')
    def lambda_19CA():
        OP_8E(0x00FE, -145870, 0, -18620, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_19CA)

    @scena.Lambda('lambda_19E5')
    def lambda_19E5():
        OP_6D(-146390, 0, -17590, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_19E5)

    @scena.Lambda('lambda_19FD')
    def lambda_19FD():
        OP_6B(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_19FD)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A52',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281176V#061F嘿嘿，已经晴了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B39')

    def _loc_1A52(): pass

    label('loc_1A52')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A89',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281177V#051F嘿，已经晴了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B39')

    def _loc_1A89(): pass

    label('loc_1A89')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AC4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281178V#030F嗯，好像已经晴了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B39')

    def _loc_1AC4(): pass

    label('loc_1AC4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AFF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281179V#048F……似乎已经晴了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B39')

    def _loc_1AFF(): pass

    label('loc_1AFF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B39',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281180V#070F嗯……已经没有雾了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B39(): pass

    label('loc_1B39')

    ChrTalk(
        0x0103,
        (
            '#0030281172V#026F米尔西街道，从洛连特出发\n',
            '大约８０塞尔矩的地点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281173V#022F浓雾中有魔兽在游荡，\n',
            '情况相当危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281194V#1015F#5P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281195V这样的话，三个地方\n',
            '都调查过了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281196V#1006F#5P我们应该回协会\n',
            '向爱娜姐报告了吧？',
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
        'loc_1CDA',
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
            TXT(0x00, '【◇没去过布莱特家】\n'),
            TXT(0x01, '【◇去过布莱特家】\n'),
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
        (0x00000000, 'loc_1CCE'),
        (0x00000001, 'loc_1CD4'),
        (-1, 'loc_1CDA'),
    )

    def _loc_1CCE(): pass

    label('loc_1CCE')

    OP_A3(0x180D)

    Jump('loc_1CDA')

    def _loc_1CD4(): pass

    label('loc_1CD4')

    OP_A2(0x180D)

    Jump('loc_1CDA')

    def _loc_1CDA(): pass

    label('loc_1CDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DB0',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281197V#023F那样也好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281198V不过，好像还没\n',
            '回家看看呢吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281199V#1004F#5P啊……都给忘了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281200V#1008F回协会报告之前\n',
            '先回去看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008F, 0x02, 0x0010)
    OP_28(0x008F, 0x01, 0x0020)
    OP_28(0x008F, 0x01, 0x0800)
    OP_28(0x008F, 0x01, 0x1000)

    Jump('loc_1DF7')

    def _loc_1DB0(): pass

    label('loc_1DB0')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030281201V#021F哎哎。\n',
            '那样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008F, 0x02, 0x0010)
    OP_28(0x008F, 0x01, 0x0020)
    OP_28(0x008F, 0x01, 0x0200)
    OP_28(0x008F, 0x01, 0x0400)

    def _loc_1DF7(): pass

    label('loc_1DF7')

    OP_A2(0x180F)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x1DFD
@scena.Code('func_0B_1DFD')
def func_0B_1DFD():
    EventBegin(0x00)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001C, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001E, 0x0080)
    SetChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrPos(0x0101, -141380, 0, -19300, 270)
    SetChrPos(0x0103, -141280, 0, -17970, 270)
    SetChrPos(0x0107, -139730, 50, -17680, 270)
    SetChrPos(0x0105, -139950, 20, -19100, 270)
    OP_6D(-142040, 0, -19080, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010290521V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, -159130, 0, -15030, 135)
    SetChrPos(0x0009, -161380, 10, -15080, 135)
    SetChrPos(0x000A, -159660, 20, -13430, 135)
    SetChrPos(0x000B, -162790, -10, -14750, 90)
    SetChrPos(0x000C, -161600, -10, -12770, 90)
    SetChrPos(0x000D, -164800, 10, -14940, 90)
    SetChrPos(0x000E, -164010, -10, -12600, 90)
    SetChrPos(0x000F, -166820, 0, -15120, 90)
    SetChrPos(0x0010, -165800, 20, -12760, 90)
    SetChrPos(0x0011, -168710, 0, -15170, 90)
    SetChrPos(0x0012, -167690, 0, -12810, 90)
    SetChrPos(0x0013, -171010, -20, -15140, 90)
    SetChrPos(0x0014, -170070, 0, -12990, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)

    @scena.Lambda('lambda_2012')
    def lambda_2012():
        OP_6D(-161370, 10, -15120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2012)

    @scena.Lambda('lambda_202A')
    def lambda_202A():
        OP_67(0, 9470, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_202A)

    Sleep(1200)

    CreateThread(0x0008, 0x00, 0x00, 0x000C)
    Sleep(300)

    CreateThread(0x0009, 0x00, 0x00, 0x000D)
    CreateThread(0x000A, 0x00, 0x00, 0x000E)
    CreateThread(0x000B, 0x00, 0x00, 0x000F)
    CreateThread(0x000C, 0x00, 0x00, 0x0010)
    CreateThread(0x000D, 0x00, 0x00, 0x0011)
    CreateThread(0x000E, 0x00, 0x00, 0x0012)
    CreateThread(0x000F, 0x00, 0x00, 0x0013)
    CreateThread(0x0010, 0x00, 0x00, 0x0014)
    CreateThread(0x0011, 0x00, 0x00, 0x0015)
    CreateThread(0x0012, 0x00, 0x00, 0x0016)
    CreateThread(0x0013, 0x00, 0x00, 0x0017)
    CreateThread(0x0014, 0x00, 0x00, 0x0018)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_20B6')
    def lambda_20B6():
        OP_6D(-153200, 0, -18030, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_20B6)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#1130290522V#5P呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#1130290523V#6P……各位，停止前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0101, -143870, 0, -17360, 270)
    SetChrPos(0x0103, -143760, 0, -16219, 270)
    SetChrPos(0x0107, -142530, 0, -16120, 270)
    SetChrPos(0x0105, -142450, 0, -17250, 270)

    @scena.Lambda('lambda_216E')
    def lambda_216E():
        OP_8E(0x00FE, -151990, 0, -18040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_216E)

    Sleep(100)

    @scena.Lambda('lambda_218E')
    def lambda_218E():
        OP_8E(0x00FE, -151910, 0, -16680, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_218E)

    Sleep(100)

    @scena.Lambda('lambda_21AE')
    def lambda_21AE():
        OP_8E(0x00FE, -150610, 0, -17880, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_21AE)

    Sleep(100)

    @scena.Lambda('lambda_21CE')
    def lambda_21CE():
        OP_8E(0x00FE, -150560, 0, -16520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_21CE)

    OP_8C(0x0008, 90, 400)
    WaitForThreadExit(0x0107, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_228A',
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
            TXT(0x00, '【◇没有和阿斯顿再会过】\n'),
            TXT(0x01, '【◇和阿斯顿再会过】\n'),
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
        (0x00000000, 'loc_227E'),
        (0x00000001, 'loc_2284'),
        (-1, 'loc_228A'),
    )

    def _loc_227E(): pass

    label('loc_227E')

    OP_A3(0x1887)

    Jump('loc_228A')

    def _loc_2284(): pass

    label('loc_2284')

    OP_A2(0x1887)

    Jump('loc_228A')

    def _loc_228A(): pass

    label('loc_228A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 7, 0x1887)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_233B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290524V#1011F#6P阿斯顿先生，好久不见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290525V#5P好久不见了，艾丝蒂尔。\n',
            '连雪拉扎德也在一起啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290526V#5P难道是正在处理协会的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CD')

    def _loc_233B(): pass

    label('loc_233B')

    ChrTalk(
        0x0101,
        (
            '#0010290527V#1011F#6P……阿斯顿先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290528V#5P艾丝蒂尔。\n',
            '连雪拉扎德也在一起啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290526V#5P难道是正在处理协会的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23CD(): pass

    label('loc_23CD')

    ChrTalk(
        0x0101,
        (
            '#0010290530V#1025F#6P嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290531V莫非要前往洛连特\n',
            '进行警备的部队是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290532V#5P嗯！就是我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290533V#5P我们和哈肯大门的增援\n',
            '要一起前去守卫洛连特市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290534V#1017F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290535V#021F那真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290536V#5P哪里，保护市民\n',
            '也是王国军的义务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290537V#5P洛连特的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290538V#1015F#6P嗯，雾还是很浓，\n',
            '不过昨天的昏睡事件……',
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
            '#0010290539V#1020F#6P啊、那个、阿斯顿先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290540V#5P……啊，你是想说鲁克吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290541V#5P他只是睡着了而已，\n',
            '并没有生命危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290542V#5P不用那么担心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280758V#1026F#6P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290544V#5P我们现在的当务之急是\n',
            '去执行自己的责任和义务，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290545V#5P也只有那样才能让\n',
            '鲁克他们早日清醒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290546V#1025F#6P阿斯顿先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290547V#026F嗯，说的没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290548V#020F阿斯顿队长，\n',
            '城镇那边就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290549V#5P没问题，交给我就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#1130290550V#6P马上就到洛连特了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130290551V#6P到达之后\n',
            '马上进入警备状态！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrName('士兵们')
    SetMessageWindowPos(350, 80, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2440290552V#4S是！长官！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x0008, 90, 400)
    Sleep(200)

    CreateThread(0x0101, 0x03, 0x00, 0x0019)
    WaitForThreadExit(0x0101, 0x0003)
    CreateThread(0x0008, 0x00, 0x00, 0x001A)

    @scena.Lambda('lambda_2879')
    def lambda_2879():
        OP_6D(-147740, 0, -17850, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2879)

    CreateThread(0x0009, 0x00, 0x00, 0x001B)
    CreateThread(0x000A, 0x00, 0x00, 0x001C)
    CreateThread(0x000B, 0x00, 0x00, 0x001D)
    CreateThread(0x000C, 0x00, 0x00, 0x001E)
    CreateThread(0x000D, 0x00, 0x00, 0x001F)
    CreateThread(0x000E, 0x00, 0x00, 0x0020)
    CreateThread(0x000F, 0x00, 0x00, 0x0021)
    CreateThread(0x0010, 0x00, 0x00, 0x0022)
    CreateThread(0x0011, 0x00, 0x00, 0x0023)
    CreateThread(0x0012, 0x00, 0x00, 0x0024)
    CreateThread(0x0013, 0x00, 0x00, 0x0025)
    CreateThread(0x0014, 0x00, 0x00, 0x0026)
    WaitForThreadExit(0x0014, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x0105, 0x01)

    @scena.Lambda('lambda_28FA')
    def lambda_28FA():
        OP_6D(-150960, 10, -15560, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28FA)

    Sleep(1000)

    @scena.Lambda('lambda_2917')
    def lambda_2917():
        OP_8C(0x0101, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2917)

    Sleep(50)

    @scena.Lambda('lambda_292A')
    def lambda_292A():
        OP_8C(0x0105, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_292A)

    Sleep(50)

    @scena.Lambda('lambda_293D')
    def lambda_293D():
        OP_8C(0x0103, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_293D)

    Sleep(50)

    OP_8C(0x0107, 215, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070290553V#063F刚才那位队长\n',
            '难道就是那昏睡的男孩的…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290554V#1007F嗯……他就是鲁克的父亲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290555V#1003F他心里肯定\n',
            '很担心的，可是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290556V#043F#6P真是个……坚强的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290557V#026F是啊……\n',
            '所以我们也要加油才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290558V#020F马上去帕赛尔农场吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    OP_A2(0x181F)
    OP_28(0x0091, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x2AC8
@scena.Code('func_0C_2AC8')
def func_0C_2AC8():
    OP_8E(0x00FE, -155890, 0, -17520, 2000, 0x00)
    OP_8E(0x00FE, -153490, 0, -17780, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000D offset: 0x2AF8
@scena.Code('func_0D_2AF8')
def func_0D_2AF8():
    OP_8E(0x00FE, -158080, 0, -18310, 2000, 0x00)
    OP_8E(0x00FE, -155450, -10, -18480, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000E offset: 0x2B28
@scena.Code('func_0E_2B28')
def func_0E_2B28():
    OP_8E(0x00FE, -156660, 0, -16530, 2000, 0x00)
    OP_8E(0x00FE, -155160, 0, -16750, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000F offset: 0x2B58
@scena.Code('func_0F_2B58')
def func_0F_2B58():
    OP_8E(0x00FE, -158480, 0, -18410, 2000, 0x00)
    OP_8E(0x00FE, -157320, -10, -18560, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0010 offset: 0x2B88
@scena.Code('func_10_2B88')
def func_10_2B88():
    OP_8E(0x00FE, -156820, 0, -16600, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0011 offset: 0x2BA4
@scena.Code('func_11_2BA4')
def func_11_2BA4():
    OP_8E(0x00FE, -162180, -10, -14600, 2000, 0x00)
    OP_8E(0x00FE, -158810, 0, -17810, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0012 offset: 0x2BD4
@scena.Code('func_12_2BD4')
def func_12_2BD4():
    OP_8E(0x00FE, -161150, 20, -12930, 2000, 0x00)
    OP_8E(0x00FE, -158150, 0, -15840, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0013 offset: 0x2C04
@scena.Code('func_13_2C04')
def func_13_2C04():
    OP_8E(0x00FE, -162180, -10, -14600, 2000, 0x00)
    OP_8E(0x00FE, -160030, 0, -16740, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0014 offset: 0x2C34
@scena.Code('func_14_2C34')
def func_14_2C34():
    OP_8E(0x00FE, -161150, 20, -12930, 2000, 0x00)
    OP_8E(0x00FE, -159160, 0, -14810, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0015 offset: 0x2C64
@scena.Code('func_15_2C64')
def func_15_2C64():
    OP_8E(0x00FE, -162180, -10, -14600, 2000, 0x00)
    OP_8E(0x00FE, -161020, 0, -15800, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0016 offset: 0x2C94
@scena.Code('func_16_2C94')
def func_16_2C94():
    OP_8E(0x00FE, -161150, 20, -12930, 2000, 0x00)
    OP_8E(0x00FE, -160080, 20, -13710, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0017 offset: 0x2CC4
@scena.Code('func_17_2CC4')
def func_17_2CC4():
    OP_8E(0x00FE, -162230, -10, -14630, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0018 offset: 0x2CE0
@scena.Code('func_18_2CE0')
def func_18_2CE0():
    OP_8E(0x00FE, -161360, 10, -12690, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0019 offset: 0x2CFC
@scena.Code('func_19_2CFC')
def func_19_2CFC():
    @scena.Lambda('lambda_2D02')
    def lambda_2D02():
        OP_8E(0x00FE, -151240, 40, -14620, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2D02)

    Sleep(50)

    @scena.Lambda('lambda_2D22')
    def lambda_2D22():
        OP_8E(0x00FE, -149900, 20, -14500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2D22)

    Sleep(200)

    @scena.Lambda('lambda_2D42')
    def lambda_2D42():
        OP_8E(0x00FE, -151210, 10, -15690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D42)

    Sleep(50)

    @scena.Lambda('lambda_2D62')
    def lambda_2D62():
        OP_8E(0x00FE, -149900, 10, -15590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2D62)

    WaitForThreadExit(0x0103, 0x0001)

    @scena.Lambda('lambda_2D82')
    def lambda_2D82():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2D82')

    DispatchAsync2(0x0103, 0x0001, lambda_2D82)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_2D98')
    def lambda_2D98():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2D98')

    DispatchAsync2(0x0107, 0x0001, lambda_2D98)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2DAE')
    def lambda_2DAE():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2DAE')

    DispatchAsync2(0x0101, 0x0001, lambda_2DAE)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_2DC4')
    def lambda_2DC4():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2DC4')

    DispatchAsync2(0x0105, 0x0001, lambda_2DC4)

    Return()

# id: 0x001A offset: 0x2DD0
@scena.Code('func_1A_2DD0')
def func_1A_2DD0():
    OP_8E(0x00FE, -130500, 20, -18200, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x2DEA
@scena.Code('func_1B_2DEA')
def func_1B_2DEA():
    OP_8E(0x00FE, -131580, 30, -18770, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0x2E04
@scena.Code('func_1C_2E04')
def func_1C_2E04():
    OP_8E(0x00FE, -131300, 20, -17110, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001D offset: 0x2E1E
@scena.Code('func_1D_2E1E')
def func_1D_2E1E():
    OP_8E(0x00FE, -133080, 40, -18640, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001E offset: 0x2E38
@scena.Code('func_1E_2E38')
def func_1E_2E38():
    OP_8E(0x00FE, -132850, 20, -17060, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001F offset: 0x2E52
@scena.Code('func_1F_2E52')
def func_1F_2E52():
    OP_8E(0x00FE, -157270, -10, -18670, 3000, 0x00)
    OP_8E(0x00FE, -133080, 40, -18640, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0020 offset: 0x2E80
@scena.Code('func_20_2E80')
def func_20_2E80():
    OP_8E(0x00FE, -157090, 0, -16790, 3000, 0x00)
    OP_8E(0x00FE, -132850, 20, -17060, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0021 offset: 0x2EAE
@scena.Code('func_21_2EAE')
def func_21_2EAE():
    OP_8E(0x00FE, -157270, -10, -18670, 3000, 0x00)
    OP_8E(0x00FE, -133080, 40, -18640, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0022 offset: 0x2EDC
@scena.Code('func_22_2EDC')
def func_22_2EDC():
    OP_8E(0x00FE, -157090, 0, -16790, 3000, 0x00)
    OP_8E(0x00FE, -132850, 20, -17060, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0023 offset: 0x2F0A
@scena.Code('func_23_2F0A')
def func_23_2F0A():
    OP_8E(0x00FE, -157270, -10, -18670, 3000, 0x00)
    OP_8E(0x00FE, -133080, 40, -18640, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0024 offset: 0x2F38
@scena.Code('func_24_2F38')
def func_24_2F38():
    OP_8E(0x00FE, -157090, 0, -16790, 3000, 0x00)
    OP_8E(0x00FE, -132850, 20, -17060, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0025 offset: 0x2F66
@scena.Code('func_25_2F66')
def func_25_2F66():
    OP_8E(0x00FE, -157270, -10, -18670, 3000, 0x00)
    OP_8E(0x00FE, -133080, 40, -18640, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0026 offset: 0x2F94
@scena.Code('func_26_2F94')
def func_26_2F94():
    OP_8E(0x00FE, -157090, 0, -16790, 3000, 0x00)
    OP_8E(0x00FE, -132850, 20, -17060, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0027 offset: 0x2FC2
@scena.Code('func_27_2FC2')
def func_27_2FC2():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_303F'),
        (0x00000001, 'loc_3045'),
        (-1, 'loc_304B'),
    )

    def _loc_303F(): pass

    label('loc_303F')

    OP_A2(0x1200)

    Jump('loc_304B')

    def _loc_3045(): pass

    label('loc_3045')

    OP_A2(0x1201)

    Jump('loc_304B')

    def _loc_304B(): pass

    label('loc_304B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3059',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_305D')

    def _loc_3059(): pass

    label('loc_3059')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_305D(): pass

    label('loc_305D')

    Return()

# id: 0x0028 offset: 0x305E
@scena.Code('func_28_305E')
def func_28_305E():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
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

# id: 0x0029 offset: 0x30B0
@scena.Code('func_29_30B0')
def func_29_30B0():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　帕赛尔农场',
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
