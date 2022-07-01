import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吸血蚊'),
    TXT(0x02, '猿羊'),
    TXT(0x03, '猿羊'),
    TXT(0x04, '猿羊'),
    TXT(0x05, '猿羊'),
    TXT(0x06, '猿羊'),
    TXT(0x07, '猿羊'),
    TXT(0x08, '蔡斯方向'),
    TXT(0x09, '亚尔摩村方向'),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
    TXT(0x0F, ''),
    TXT(0x10, ''),
    TXT(0x11, ''),
    TXT(0x12, ''),
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
    TXT(0x21, ''),
    TXT(0x22, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3101.x'
    header.mapIndex       = 1
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/R3101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xF14
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
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
        ('ED6_DT09/CH10080._CH', 'ED6_DT09/CH10080P._CP'),
        ('ED6_DT09/CH10081._CH', 'ED6_DT09/CH10081P._CP'),
        ('ED6_DT09/CH10120._CH', 'ED6_DT09/CH10120P._CP'),
        ('ED6_DT09/CH10121._CH', 'ED6_DT09/CH10121P._CP'),
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT09/CH10620._CH', 'ED6_DT09/CH10620P._CP'),
        ('ED6_DT09/CH10621._CH', 'ED6_DT09/CH10621P._CP'),
        ('ED6_DT09/CH10600._CH', 'ED6_DT09/CH10600P._CP'),
        ('ED6_DT09/CH10601._CH', 'ED6_DT09/CH10601P._CP'),
        ('ED6_DT09/CH10400._CH', 'ED6_DT09/CH10400P._CP'),
        ('ED6_DT09/CH10401._CH', 'ED6_DT09/CH10401P._CP'),
        ('ED6_DT29/CH12130._CH', 'ED6_DT29/CH12130P._CP'),
        ('ED6_DT29/CH12131._CH', 'ED6_DT29/CH12131P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT09/CH10144._CH', 'ED6_DT09/CH10144P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
        ('ED6_DT09/CH11154._CH', 'ED6_DT09/CH11154P._CP'),
        ('ED6_DT29/CH12070._CH', 'ED6_DT29/CH12070P._CP'),
        ('ED6_DT29/CH12071._CH', 'ED6_DT29/CH12071P._CP'),
        ('ED6_DT29/CH12074._CH', 'ED6_DT29/CH12074P._CP'),
    ]

# id: 0x10002 offset: 0x19A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -53000,
            z                   = -70,
            y                   = -1910,
            direction           = 94,
            word_0E             = 14,
            dword_10            = 917504,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 33300,
            z                   = 0,
            y                   = -32150,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 34470,
            z                   = 0,
            y                   = -30990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 33870,
            z                   = 0,
            y                   = -34110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 35470,
            z                   = 0,
            y                   = -33030,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 33840,
            z                   = 10,
            y                   = -30000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 33840,
            z                   = 10,
            y                   = -30000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -21960,
            z                   = 0,
            y                   = 68390,
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
            x                   = 68320,
            z                   = 0,
            y                   = -37930,
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

# id: 0x10003 offset: 0x2BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 31840,
            z           = -140,
            y           = -14910,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 20310,
            z           = 20,
            y           = 6500,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6650,
            z           = 10,
            y           = 6470,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7960,
            z           = -70,
            y           = 22900,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7300,
            z           = 80,
            y           = -13910,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8220,
            z           = 70,
            y           = -25600,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 18960,
            z           = 10,
            y           = -47120,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19200,
            z           = 50,
            y           = -40070,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -2840,
            z           = 20,
            y           = -43880,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23970,
            z           = -60,
            y           = -56200,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -47630,
            z           = 40,
            y           = -38230,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -41100,
            z           = 30,
            y           = -42080,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46340,
            z           = -10,
            y           = -47090,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39960,
            z           = -50,
            y           = -46350,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35370,
            z           = 60,
            y           = -38180,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39680,
            z           = -30,
            y           = -43880,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -31310,
            z           = -20,
            y           = -44150,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -37830,
            z           = -40,
            y           = -49270,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20630,
            z           = -50,
            y           = -21460,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6340,
            z           = -20,
            y           = 12260,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -9790,
            z           = 30,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -7920,
            z           = -70,
            y           = -27310,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22580,
            z           = 10,
            y           = 23060,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35830,
            z           = 30,
            y           = 26470,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x55A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -53000,
            y           = -1000,
            z           = -1910,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x57A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 36090,
            triggerZ            = -130,
            triggerY            = -4970,
            triggerRange        = 1000,
            actorX              = 36580,
            actorZ              = 1370,
            actorY              = -4390,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -43380,
            triggerZ            = -30,
            triggerY            = -54510,
            triggerRange        = 1000,
            actorX              = -43860,
            actorZ              = -30,
            actorY              = -54970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -21630,
            triggerZ            = -10,
            triggerY            = 8540,
            triggerRange        = 1000,
            actorX              = -21750,
            actorZ              = 1490,
            actorY              = 7880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20640,
            triggerZ            = -20,
            triggerY            = -6840,
            triggerRange        = 1000,
            actorX              = 17090,
            actorZ              = -600,
            actorY              = -7230,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x60A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_621',
    )

    OP_A3(0x10F0)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x29),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(1, 0x0001)

    def _loc_621(): pass

    label('loc_621')

    Return()

# id: 0x0001 offset: 0x622
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0048, 0xFFFE13D0, 0x0023002E)

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
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6EC',
    )

    If(
        (
            (Expr.GetChrWork, 0x104, 0x1C),
            (Expr.PushLong, 0x5B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6EC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6EC',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_69B',
    )

    OP_28(0x006E, 0x01, 0x0040)

    Jump('loc_6EC')

    def _loc_69B(): pass

    label('loc_69B')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B0',
    )

    OP_28(0x006E, 0x01, 0x0020)

    Jump('loc_6EC')

    def _loc_6B0(): pass

    label('loc_6B0')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C5',
    )

    OP_28(0x006E, 0x01, 0x0010)

    Jump('loc_6EC')

    def _loc_6C5(): pass

    label('loc_6C5')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DA',
    )

    OP_28(0x006E, 0x01, 0x0008)

    Jump('loc_6EC')

    def _loc_6DA(): pass

    label('loc_6DA')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6EC',
    )

    OP_28(0x006E, 0x01, 0x0004)

    def _loc_6EC(): pass

    label('loc_6EC')

    ExecExpressionWithValue(
        0x0017,
        0x24,
        (
            (Expr.PushLong, 0xBF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_715',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_727')

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x029F, 4, 0x14FC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_727',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_727(): pass

    label('loc_727')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 2, 0x1502)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_739',
    )

    OP_6F(0x0000, 0)

    Jump('loc_740')

    def _loc_739(): pass

    label('loc_739')

    OP_6F(0x0000, 60)

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 3, 0x1503)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_752',
    )

    OP_6F(0x0001, 0)

    Jump('loc_759')

    def _loc_752(): pass

    label('loc_752')

    OP_6F(0x0001, 60)

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 5, 0x1505)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_76B',
    )

    OP_6F(0x0002, 0)

    Jump('loc_772')

    def _loc_76B(): pass

    label('loc_76B')

    OP_6F(0x0002, 60)

    def _loc_772(): pass

    label('loc_772')

    OP_E0(0x01, 0xFC, 0x59, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x10, 0x2D, 0xFF, 0xFF)

    Return()

# id: 0x0002 offset: 0x781
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
        'loc_7A6',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_8E8')

    def _loc_7A6(): pass

    label('loc_7A6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BF',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_8E8')

    def _loc_7BF(): pass

    label('loc_7BF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D8',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_8E8')

    def _loc_7D8(): pass

    label('loc_7D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F1',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_8E8')

    def _loc_7F1(): pass

    label('loc_7F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80A',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_8E8')

    def _loc_80A(): pass

    label('loc_80A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_823',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_8E8')

    def _loc_823(): pass

    label('loc_823')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83C',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_8E8')

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_855',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_8E8')

    def _loc_855(): pass

    label('loc_855')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86E',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_8E8')

    def _loc_86E(): pass

    label('loc_86E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_887',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_8E8')

    def _loc_887(): pass

    label('loc_887')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A0',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_8E8')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B9',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_8E8')

    def _loc_8B9(): pass

    label('loc_8B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D2',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_8E8')

    def _loc_8D2(): pass

    label('loc_8D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E8',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_8E8(): pass

    label('loc_8E8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8FD',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_8E8')

    def _loc_8FD(): pass

    label('loc_8FD')

    Return()

# id: 0x0003 offset: 0x8FE
@scena.Code('func_03_8FE')
def func_03_8FE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x029F, 4, 0x14FC)),
            Expr.Return,
        ),
        'loc_906',
    )

    Return()

    def _loc_906(): pass

    label('loc_906')

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
        (0x00000001, 'loc_9EB'),
        (-1, 'loc_A0E'),
    )

    def _loc_9EB(): pass

    label('loc_9EB')

    Fade(500)
    OP_89(0x0000, -45180, -10, -2300, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_A0E(): pass

    label('loc_A0E')

    Battle(0x00000EE3, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -45180, -10, -2300, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_A47'),
        (0x00000001, 'loc_A4A'),
        (-1, 'loc_A4D'),
    )

    def _loc_A47(): pass

    label('loc_A47')

    EventEnd(0x00)

    Return()

    def _loc_A4A(): pass

    label('loc_A4A')

    OP_B4(0x00)

    Return()

    def _loc_A4D(): pass

    label('loc_A4D')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
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
    OP_A2(0x14FC)
    OP_28(0x00A7, 0x04, 0x10)
    OP_28(0x00A7, 0x04, 0x02)
    OP_28(0x00A7, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xAB9
@scena.Code('func_04_AB9')
def func_04_AB9():
    UnlockAchievement(0x02, 0xEC, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 2, 0x1502)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B96',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_B2D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1502)

    Jump('loc_B93')

    def _loc_B2D(): pass

    label('loc_B2D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
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

    def _loc_B93(): pass

    label('loc_B93')

    Jump('loc_BC7')

    def _loc_B96(): pass

    label('loc_B96')

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
    def _loc_BC7(): pass

    label('loc_BC7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xBD5
@scena.Code('func_05_BD5')
def func_05_BD5():
    UnlockAchievement(0x02, 0xED, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 3, 0x1503)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_C49',
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
    OP_A2(0x1503)

    Jump('loc_CAF')

    def _loc_C49(): pass

    label('loc_C49')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_CAF(): pass

    label('loc_CAF')

    Jump('loc_CE3')

    def _loc_CB2(): pass

    label('loc_CB2')

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
    def _loc_CE3(): pass

    label('loc_CE3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xCF1
@scena.Code('func_06_CF1')
def func_06_CF1():
    UnlockAchievement(0x02, 0xEE, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 5, 0x1505)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DCE',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['田螺'], 1)"),
            Expr.Return,
        ),
        'loc_D65',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['田螺']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1505)

    Jump('loc_DCB')

    def _loc_D65(): pass

    label('loc_D65')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['田螺']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['田螺']),
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

    def _loc_DCB(): pass

    label('loc_DCB')

    Jump('loc_DFF')

    def _loc_DCE(): pass

    label('loc_DCE')

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
    def _loc_DFF(): pass

    label('loc_DFF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xE0D
@scena.Code('func_07_E0D')
def func_07_E0D():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E45')
    def lambda_0E45():
        OP_6D(17340, -20, -7640, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0E45)

    @scena.Lambda('lambda_0E5D')
    def lambda_0E5D():
        OP_6B(3250, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0E5D)

    @scena.Lambda('lambda_0E6D')
    def lambda_0E6D():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0E6D)

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
        'loc_EF4',
    )

    OP_C0(0x0E, 0x00000023, 0x000050BE, 0xFFFFFFEC, 0xFFFFE566, 0x0000010E, 0x00004376, 0xFFFFFCE0, 0xFFFFE16A)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_F03')

    def _loc_EF4(): pass

    label('loc_EF4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F03',
    )

    EventEnd(0x01)

    def _loc_F03(): pass

    label('loc_F03')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
