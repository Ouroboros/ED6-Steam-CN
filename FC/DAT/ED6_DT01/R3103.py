import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3103   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '蔡斯方向'),
    TXT(0x02, '沃尔费堡垒方向'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3103.x'
    header.mapIndex       = 1
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xD1B
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
            word_3A         = 144,
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
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -53110,
            z                   = 0,
            y                   = -14880,
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
            x                   = 22050,
            z                   = -10,
            y                   = 35970,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -30730,
            z           = -20,
            y           = 28880,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -27870,
            z           = 80,
            y           = 46700,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14660,
            z           = -80,
            y           = 32810,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24060,
            z           = 70,
            y           = -7910,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -10150,
            z           = 10,
            y           = -20920,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13270,
            z           = -30,
            y           = -23320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15990,
            z           = -10,
            y           = 1090,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 31250,
            z           = 30,
            y           = -6140,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 39280,
            z           = 20,
            y           = -27110,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 23510,
            z           = 40,
            y           = -36040,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x021B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 10940,
            z           = 10,
            y           = -46410,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x021B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -10090,
            z           = 10,
            y           = -39590,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -25680,
            z           = -40,
            y           = -25220,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -29830,
            z           = -90,
            y           = -39580,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -30430,
            z           = -80,
            y           = -45390,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -21410,
            z           = -50,
            y           = -50290,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22480,
            z           = 30,
            y           = -37550,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -30730,
            z           = -20,
            y           = 28880,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -27870,
            z           = 80,
            y           = 46700,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14660,
            z           = -80,
            y           = 32810,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24060,
            z           = 70,
            y           = -7910,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -10150,
            z           = 10,
            y           = -20920,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13270,
            z           = -30,
            y           = -23320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15990,
            z           = -10,
            y           = 1090,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 31250,
            z           = 30,
            y           = -6140,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 39280,
            z           = 20,
            y           = -27110,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 23510,
            z           = 40,
            y           = -36040,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x035B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 10940,
            z           = 10,
            y           = -46410,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x035B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -10090,
            z           = 10,
            y           = -39590,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -25680,
            z           = -40,
            y           = -25220,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -29830,
            z           = -90,
            y           = -39580,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -30430,
            z           = -80,
            y           = -45390,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -21410,
            z           = -50,
            y           = -50290,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22480,
            z           = 30,
            y           = -37550,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x532
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x532
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -17270,
            triggerZ            = 0,
            triggerY            = 42460,
            triggerRange        = 1400,
            actorX              = -17270,
            actorZ              = 0,
            actorY              = 42460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17230,
            triggerZ            = 10,
            triggerY            = -7630,
            triggerRange        = 1000,
            actorX              = 17890,
            actorZ              = 10,
            actorY              = -7630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12960,
            triggerZ            = -20,
            triggerY            = 45920,
            triggerRange        = 1000,
            actorX              = -12550,
            actorZ              = -20,
            actorY              = 46450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -24020,
            triggerZ            = -10,
            triggerY            = -43750,
            triggerRange        = 1000,
            actorX              = -24580,
            actorZ              = -10,
            actorY              = -43380,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5C2
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x5C3
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -131000, -126000, 196656)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5ED',
    )

    OP_B1('R3103_y')

    Jump('loc_5F6')

    def _loc_5ED(): pass

    label('loc_5ED')

    OP_B1('R3103_n')

    def _loc_5F6(): pass

    label('loc_5F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_65A',
    )

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
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

    Jump('loc_6AF')

    def _loc_65A(): pass

    label('loc_65A')

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
    SetChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)

    def _loc_6AF(): pass

    label('loc_6AF')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002F, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6CF',
    )

    OP_65(0x00, 0x0001)

    def _loc_6CF(): pass

    label('loc_6CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 2, 0x5A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E1',
    )

    OP_6F(0x0000, 0)

    Jump('loc_6E8')

    def _loc_6E1(): pass

    label('loc_6E1')

    OP_6F(0x0000, 60)

    def _loc_6E8(): pass

    label('loc_6E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 4, 0x5A4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FA',
    )

    OP_6F(0x0001, 0)

    Jump('loc_701')

    def _loc_6FA(): pass

    label('loc_6FA')

    OP_6F(0x0001, 60)

    def _loc_701(): pass

    label('loc_701')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 1, 0x5A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_713',
    )

    OP_6F(0x0002, 0)

    Jump('loc_71A')

    def _loc_713(): pass

    label('loc_713')

    OP_6F(0x0002, 60)

    def _loc_71A(): pass

    label('loc_71A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_726'),
        (-1, 'loc_733'),
    )

    def _loc_726(): pass

    label('loc_726')

    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)

    Jump('loc_733')

    def _loc_733(): pass

    label('loc_733')

    Return()

# id: 0x0002 offset: 0x734
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_749',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_749(): pass

    label('loc_749')

    Return()

# id: 0x0003 offset: 0x74A
@scena.Code('func_03_74A')
def func_03_74A():
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '发现了一个油纸包。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '里面放着',
            (TxtCtl.SetColor, 0x2),
            '哈茨少年冒险记·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0344, 1)
    OP_64(0x00, 0x0001)
    OP_28(0x002F, 0x01, 0x0008)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x7CB
@scena.Code('func_04_7CB')
def func_04_7CB():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 2, 0x5A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_997',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 3, 0x5A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C3',
    )

    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    SetChrPos(0x000A, -12550, 1500, 46450, 320)
    ChrTurnDirection(0x000A, 0x0000, 0)

    @scena.Lambda('lambda_081A')
    def lambda_081A():
        ChrMoveTo(0x00FE, -12550, 1000, 46450, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_081A)

    @scena.Lambda('lambda_0835')
    def lambda_0835():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0835)

    ClearChrFlags(0x000A, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_878',
    )

    Battle(0x00000357, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_885')

    def _loc_878(): pass

    label('loc_878')

    Battle(0x00000217, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_885(): pass

    label('loc_885')

    SetChrFlags(0x000A, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_89E'),
        (0x00000002, 'loc_8B0'),
        (0x00000001, 'loc_8C0'),
        (-1, 'loc_8C3'),
    )

    def _loc_89E(): pass

    label('loc_89E')

    SetScenaFlags(ScenaFlag(0x00B4, 3, 0x5A3))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_8C3')

    def _loc_8B0(): pass

    label('loc_8B0')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_8C0(): pass

    label('loc_8C0')

    OP_B4(0x00)

    Return()

    def _loc_8C3(): pass

    label('loc_8C3')

    If(
        (
            (Expr.Eval, "AddItem(0x0142, 1)"),
            Expr.Return,
        ),
        'loc_91B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '苍耀石护符',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B4, 2, 0x5A2))

    Jump('loc_994')

    def _loc_91B(): pass

    label('loc_91B')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '苍耀石护符',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '苍耀石护符',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_994(): pass

    label('loc_994')

    Jump('loc_9CD')

    def _loc_997(): pass

    label('loc_997')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x93)
    def _loc_9CD(): pass

    label('loc_9CD')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x9DB
@scena.Code('func_05_9DB')
def func_05_9DB():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 4, 0x5A4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B95',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 5, 0x5A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AD3',
    )

    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    SetChrPos(0x000A, -24580, 1500, -43380, 320)
    ChrTurnDirection(0x000A, 0x0000, 0)

    @scena.Lambda('lambda_0A2A')
    def lambda_0A2A():
        ChrMoveTo(0x00FE, -24580, 1000, -43380, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A2A)

    @scena.Lambda('lambda_0A45')
    def lambda_0A45():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0A45)

    ClearChrFlags(0x000A, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A88',
    )

    Battle(0x00000357, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_A95')

    def _loc_A88(): pass

    label('loc_A88')

    Battle(0x00000217, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_A95(): pass

    label('loc_A95')

    SetChrFlags(0x000A, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_AAE'),
        (0x00000002, 'loc_AC0'),
        (0x00000001, 'loc_AD0'),
        (-1, 'loc_AD3'),
    )

    def _loc_AAE(): pass

    label('loc_AAE')

    SetScenaFlags(ScenaFlag(0x00B4, 5, 0x5A5))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_AD3')

    def _loc_AC0(): pass

    label('loc_AC0')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_AD0(): pass

    label('loc_AD0')

    OP_B4(0x00)

    Return()

    def _loc_AD3(): pass

    label('loc_AD3')

    If(
        (
            (Expr.Eval, "AddItem(0x014F, 1)"),
            Expr.Return,
        ),
        'loc_B25',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '长桶',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B4, 4, 0x5A4))

    Jump('loc_B92')

    def _loc_B25(): pass

    label('loc_B25')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '长桶',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '长桶',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_B92(): pass

    label('loc_B92')

    Jump('loc_BCB')

    def _loc_B95(): pass

    label('loc_B95')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x94)
    def _loc_BCB(): pass

    label('loc_BCB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xBD9
@scena.Code('func_06_BD9')
def func_06_BD9():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 1, 0x5A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CC9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_C4F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B4, 1, 0x5A1))

    Jump('loc_CC6')

    def _loc_C4F(): pass

    label('loc_C4F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_CC6(): pass

    label('loc_CC6')

    Jump('loc_CFF')

    def _loc_CC9(): pass

    label('loc_CC9')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x95)
    def _loc_CFF(): pass

    label('loc_CFF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
