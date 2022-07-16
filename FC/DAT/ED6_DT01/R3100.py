import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '东方打扮的男人'),
    TXT(0x02, '蔡斯方向'),
    TXT(0x03, '亚尔摩村方向'),
    TXT(0x04, '沃尔费堡垒方向'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3100.x'
    header.mapIndex       = 1
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x16C0
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
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00054._CH', 'ED6_DT07/CH00054P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
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
        ('ED6_DT06/CH20139._CH', 'ED6_DT06/CH20139P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = -26180,
            z                   = 0,
            y                   = 75950,
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
            x                   = -27440,
            z                   = 0,
            y                   = -76050,
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
            x                   = 57120,
            z                   = 20,
            y                   = -11610,
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

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -31930,
            z           = -10,
            y           = 25570,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17900,
            z           = -100,
            y           = 29570,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17830,
            z           = -50,
            y           = 10270,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33160,
            z           = 80,
            y           = 9720,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33640,
            z           = -20,
            y           = -11610,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34150,
            z           = 10,
            y           = -34210,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17610,
            z           = 60,
            y           = -32390,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13750,
            z           = 20,
            y           = 4540,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 28640,
            z           = -50,
            y           = -14990,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 39490,
            z           = -40,
            y           = 9070,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 18010,
            z           = 0,
            y           = 13240,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19410,
            z           = -90,
            y           = 27970,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 20370,
            z           = 10,
            y           = 8119,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21540,
            z           = 50,
            y           = 3820,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -43300,
            z           = 80,
            y           = -22610,
            word_0C     = 0x00B4,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -25500,
            z           = 20,
            y           = 17440,
            word_0C     = 0x00B4,
            word_0E     = 0x0007,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7640,
            z           = 0,
            y           = 5540,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -31930,
            z           = -10,
            y           = 25570,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17900,
            z           = -100,
            y           = 29570,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17830,
            z           = -50,
            y           = 10270,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33160,
            z           = 80,
            y           = 9720,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -33640,
            z           = -20,
            y           = -11610,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34150,
            z           = 10,
            y           = -34210,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17610,
            z           = 60,
            y           = -32390,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13750,
            z           = 20,
            y           = 4540,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 28640,
            z           = -50,
            y           = -14990,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 39490,
            z           = -40,
            y           = 9070,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 18010,
            z           = 0,
            y           = 13240,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19410,
            z           = -90,
            y           = 27970,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 20370,
            z           = 10,
            y           = 8119,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21540,
            z           = 50,
            y           = 3820,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -43300,
            z           = 80,
            y           = -22610,
            word_0C     = 0x00B4,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -25500,
            z           = 20,
            y           = 17440,
            word_0C     = 0x00B4,
            word_0E     = 0x0007,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7640,
            z           = 0,
            y           = 5540,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x572
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -10960,
            y           = -1000,
            z           = -260,
            range       = -9090,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFD7CE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x592
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -31610,
            triggerZ            = 0,
            triggerY            = 41470,
            triggerRange        = 1500,
            actorX              = -31610,
            actorZ              = 1500,
            actorY              = 41470,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -15330,
            triggerZ            = 0,
            triggerY            = -13840,
            triggerRange        = 1500,
            actorX              = -15330,
            actorZ              = 1350,
            actorY              = -13840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12250,
            triggerZ            = 0,
            triggerY            = -9350,
            triggerRange        = 1500,
            actorX              = -12250,
            actorZ              = 1400,
            actorY              = -9350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3410,
            triggerZ            = -20,
            triggerY            = -11850,
            triggerRange        = 1000,
            actorX              = 3410,
            actorZ              = 1480,
            actorY              = -12510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -29130,
            triggerZ            = 90,
            triggerY            = -8189,
            triggerRange        = 1000,
            actorX              = -28780,
            actorZ              = 1590,
            actorY              = -8610,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x646
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x647
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -131000, -126000, 196653)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_671',
    )

    OP_B1('R3100_y')

    Jump('loc_67A')

    def _loc_671(): pass

    label('loc_671')

    OP_B1('R3100_n')

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6DE',
    )

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
    SetChrFlags(0x001C, 0x0080)

    Jump('loc_733')

    def _loc_6DE(): pass

    label('loc_6DE')

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
    SetChrFlags(0x002D, 0x0080)

    def _loc_733(): pass

    label('loc_733')

    If(
        (
            (Expr.Eval, "OP_40(0x0346)"),
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_748',
    )

    OP_1B(0x01, 0x00, 0x0002)

    def _loc_748(): pass

    label('loc_748')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 1, 0x599)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_75A',
    )

    OP_6F(0x0000, 0)

    Jump('loc_761')

    def _loc_75A(): pass

    label('loc_75A')

    OP_6F(0x0000, 60)

    def _loc_761(): pass

    label('loc_761')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 2, 0x59A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_773',
    )

    OP_6F(0x0001, 0)

    Jump('loc_77A')

    def _loc_773(): pass

    label('loc_773')

    OP_6F(0x0001, 60)

    def _loc_77A(): pass

    label('loc_77A')

    Return()

# id: 0x0002 offset: 0x77B
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_824',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180747V#010F艾丝蒂尔，\n',
            '先去把导力引擎送过去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180748V王先生他们肯定还在等着呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180749V#000F啊，对了。\n',
            '是从这里往西走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_908')

    def _loc_824(): pass

    label('loc_824')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020180750V#010F往这边走就到亚尔摩村了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180751V先去西边的平原\n',
            '把导力引擎送到王先生他们手里吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_908')

    def _loc_89A(): pass

    label('loc_89A')

    ChrTalk(
        0x0107,
        (
            '#0070180752V#060F（要先把导力引擎送过去才行……）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180753V#060F（运输车抛锚的地方\n',
            '　从这里往西走就到了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_908(): pass

    label('loc_908')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0003 offset: 0x924
@scena.Code('func_03_924')
def func_03_924():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 3, 0x53B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1325',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00AA, 0, 0x550))
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -22660, 0, -12250, 45)

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '#0080081312V哟？\n',
            '你们几个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-14850, -10, -5530, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(215000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -12590, -10, -5620, 270)
    SetChrPos(0x0107, -11250, 0, -6040, 270)
    SetChrPos(0x0102, -11730, 0, -3960, 270)
    SetChrPos(0x0106, -10690, 0, -4680, 270)

    @scena.Lambda('lambda_0A07')
    def lambda_0A07():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A07')

    DispatchAsync2(0x0101, 0x0003, lambda_0A07)

    @scena.Lambda('lambda_0A18')
    def lambda_0A18():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A18')

    DispatchAsync2(0x0102, 0x0003, lambda_0A18)

    @scena.Lambda('lambda_0A29')
    def lambda_0A29():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A29')

    DispatchAsync2(0x0107, 0x0003, lambda_0A29)

    @scena.Lambda('lambda_0A3A')
    def lambda_0A3A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A3A')

    DispatchAsync2(0x0106, 0x0003, lambda_0A3A)

    @scena.Lambda('lambda_0A4B')
    def lambda_0A4B():
        ChrWalkTo(0x00FE, -16250, 0, -5480, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A4B)

    OP_0D()
    WaitForThreadExit(0x0008, 0x0001)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081313V#004F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081314V#064F从亚尔摩回来时遇到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0080081315V#071F哈哈，\n',
            '那时真是谢谢你们指路啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081316V不过还能在街道遇到你们，\n',
            '我们还真是有缘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081317V#001F啊哈，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081318V#501F这么说来，\n',
            '大叔也是去亚尔摩村泡温泉的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0080081319V#075F话是没错……\n',
            '不过别叫我大叔啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081320V#073F对了，\n',
            '这位小哥之前好像没见过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081321V你脸色不太好啊，不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081322V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    @scena.Lambda('lambda_0C11')
    def lambda_0C11():
        CameraMove(-12080, 0, -4480, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C11)

    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)
    TerminateThread(0x0107, 0x03)
    TerminateThread(0x0106, 0x03)

    @scena.Lambda('lambda_0C39')
    def lambda_0C39():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0C39)

    @scena.Lambda('lambda_0C47')
    def lambda_0C47():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0C47)

    @scena.Lambda('lambda_0C55')
    def lambda_0C55():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_0C55)

    ChrTurnDirection(0x0101, 0x0106, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0106,
        (
            '#0050081323V#058F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(81)

    ChrTalk(
        0x0101,
        (
            '#0010081324V#2P#580F唔哇……脸色怎么会这样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081325V#065F阿、阿加特大哥哥……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081326V#058F吵死了……\n',
            '不是说了没事吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0106, 30, 0, 600, 3000)
    Fade(500)

    @scena.Lambda('lambda_0D6E')
    def lambda_0D6E():
        CameraSetDistance(2900, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0D6E)

    SetChrChipByIndex(0x0106, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050081327V#059F……呜………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(524, 0x00, 0x64)

    @scena.Lambda('lambda_0DB7')
    def lambda_0DB7():
        CameraSetDistance(2900, 500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0DB7)

    SetChrFlags(0x0106, 0x0002)
    SetChrChipByIndex(0x0106, 17)
    SetChrSubChip(0x0106, 0)
    SetChrPos(0x0106, -10570, 0, -4920, 91)
    SetChrDirection(0x0107, 0, 0)
    SetChrDirection(0x0101, 45, 0)
    SetChrDirection(0x0102, 180, 0)
    OP_0D()
    Sleep(500)

    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070081328V#069F呀……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081329V#580F#2P怎、怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081330V#016F……等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0102, 2)
    OP_0D()

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        ChrWalkTo(0x00FE, -13170, 0, -4490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E7E)

    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚用手拨开了阿加特的眼皮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0102, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020081331V#013F糟了……\n',
            '瞳孔怎么张得这么开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081332V那些黑衣人的导力弹里\n',
            '一定放了些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081333V#580F#2P什、什么……难道是毒！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0080081334V#072F唔，应该没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081335V出现瞳孔张开的症状，\n',
            '也许是中了植物性的神经毒药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0102, 65535)
    OP_0D()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020081336V#012F我也认为很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081337V虽然还不能肯定……\n',
            '但这样下去阿加特兄也许有生命危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081338V#069F怎、怎么会……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081339V#005F#2P总、总之要赶快\n',
            '把他送到有治疗设施的地方！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081340V提妲，\n',
            '这附近有能帮他治疗的地方吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081341V#068F中、中央工房……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081342V四楼有医务室！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0080081343V#072F事不宜迟……\n',
            '那就麻烦小姑娘带路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081344V我来背这个小哥好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1181')
    def lambda_1181():
        OP_69(0x0008, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1181)

    @scena.Lambda('lambda_118F')
    def lambda_118F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_118F)

    @scena.Lambda('lambda_119D')
    def lambda_119D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_119D)

    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010081345V#505F哎……可以吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0080081346V#070F#2P你看他这结实的块头。\n',
            '反正苦力的活儿就交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081347V而且……\n',
            '看来我们还是同行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081348V#004F同行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081349V#014F难道说，您也是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0080081350V#074F#2P还没自我介绍呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081351V#070F金·瓦赛克——\n',
            '隶属于共和国的游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081352V#070F请多指教。\n',
            '各位王国的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3118._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1325(): pass

    label('loc_1325')

    Return()

# id: 0x0004 offset: 0x1326
@scena.Code('func_04_1326')
def func_04_1326():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　蔡斯市\n',
            '南　亚尔摩村　　１６５塞尔矩\n',
            '　　沃尔费堡垒　２８０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x139D
@scena.Code('func_05_139D')
def func_05_139D():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　亚尔摩村　　１３０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x13EC
@scena.Code('func_06_13EC')
def func_06_13EC():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　蔡斯市\n',
            '东　沃尔费堡垒　２４５塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x1446
@scena.Code('func_07_1446')
def func_07_1446():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 1, 0x599)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1536',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_14BC',
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
    SetScenaFlags(ScenaFlag(0x00B3, 1, 0x599))

    Jump('loc_1533')

    def _loc_14BC(): pass

    label('loc_14BC')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_1533(): pass

    label('loc_1533')

    Jump('loc_156C')

    def _loc_1536(): pass

    label('loc_1536')

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
    WaitEffect(0x0F, 0x8D)
    def _loc_156C(): pass

    label('loc_156C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x157A
@scena.Code('func_08_157A')
def func_08_157A():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 2, 0x59A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_166A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_15F0',
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
    SetScenaFlags(ScenaFlag(0x00B3, 2, 0x59A))

    Jump('loc_1667')

    def _loc_15F0(): pass

    label('loc_15F0')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_1667(): pass

    label('loc_1667')

    Jump('loc_16A0')

    def _loc_166A(): pass

    label('loc_166A')

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
    WaitEffect(0x0F, 0x8E)
    def _loc_16A0(): pass

    label('loc_16A0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
