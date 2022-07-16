import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '朵洛希'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '魔兽'),
    TXT(0x07, '东方打扮的男人'),
    TXT(0x08, '蔡斯方向'),
    TXT(0x09, '亚尔摩村方向'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3101.x'
    header.mapIndex       = 1
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2F92
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
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT09/CH10063._CH', 'ED6_DT09/CH10063P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00112._CH', 'ED6_DT07/CH00112P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
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

# id: 0x10002 offset: 0x172
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
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
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 31840,
            z           = -140,
            y           = -14910,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21310,
            z           = 20,
            y           = 1100,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6650,
            z           = 10,
            y           = 6470,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
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
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7300,
            z           = 80,
            y           = -13910,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
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
            word_0E     = 0x0015,
            byte_10     = 0x01,
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
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19200,
            z           = 50,
            y           = -40070,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -2840,
            z           = 20,
            y           = -43880,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23970,
            z           = -60,
            y           = -56200,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -47630,
            z           = 40,
            y           = -38230,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -41100,
            z           = 30,
            y           = -42080,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46340,
            z           = -10,
            y           = -47090,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39960,
            z           = -50,
            y           = -46350,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35370,
            z           = 60,
            y           = -38180,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39680,
            z           = -30,
            y           = -43880,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -31310,
            z           = -20,
            y           = -44150,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -37830,
            z           = -40,
            y           = -49270,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20630,
            z           = -50,
            y           = -21460,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0213,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6340,
            z           = -20,
            y           = 12260,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -9790,
            z           = 30,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -7920,
            z           = -70,
            y           = -27310,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22580,
            z           = 10,
            y           = 23060,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35830,
            z           = 30,
            y           = 26470,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 31840,
            z           = -140,
            y           = -14910,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0351,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21310,
            z           = 20,
            y           = 1100,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0351,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6650,
            z           = 10,
            y           = 6470,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7960,
            z           = -70,
            y           = 22900,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 7300,
            z           = 80,
            y           = -13910,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8220,
            z           = 70,
            y           = -25600,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 18960,
            z           = 10,
            y           = -47120,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 19200,
            z           = 50,
            y           = -40070,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -2840,
            z           = 20,
            y           = -43880,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23970,
            z           = -60,
            y           = -56200,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -47630,
            z           = 40,
            y           = -38230,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -41100,
            z           = 30,
            y           = -42080,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46340,
            z           = -10,
            y           = -47090,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39960,
            z           = -50,
            y           = -46350,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35370,
            z           = 60,
            y           = -38180,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -39680,
            z           = -30,
            y           = -43880,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -31310,
            z           = -20,
            y           = -44150,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -37830,
            z           = -40,
            y           = -49270,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20630,
            z           = -50,
            y           = -21460,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0353,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6340,
            z           = -20,
            y           = 12260,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -9790,
            z           = 30,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -7920,
            z           = -70,
            y           = -27310,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22580,
            z           = 10,
            y           = 23060,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35830,
            z           = 30,
            y           = 26470,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x7F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -47070,
            y           = -2000,
            z           = 850,
            range       = 5000,
            dword_10    = 0x00003A98,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -26870,
            y           = -1000,
            z           = 40570,
            range       = -17040,
            dword_10    = 0x000007D0,
            dword_14    = 0x000094DE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x832
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
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -43660,
            triggerZ            = -50,
            triggerY            = -54700,
            triggerRange        = 1000,
            actorX              = -44130,
            actorZ              = 1450,
            actorY              = -55170,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
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
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x89E
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_8AA'),
        (-1, 'loc_8C0'),
    )

    def _loc_8AA(): pass

    label('loc_8AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 1, 0x521)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8BD',
    )

    SetScenaFlags(ScenaFlag(0x00A4, 1, 0x521))
    Event(0, 0x0003)

    def _loc_8BD(): pass

    label('loc_8BD')

    Jump('loc_8C0')

    def _loc_8C0(): pass

    label('loc_8C0')

    Return()

# id: 0x0001 offset: 0x8C1
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -131000, -126000, 196654)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8EB',
    )

    OP_B1('R3101_y')

    Jump('loc_8F4')

    def _loc_8EB(): pass

    label('loc_8EB')

    OP_B1('R3101_n')

    def _loc_8F4(): pass

    label('loc_8F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_97B',
    )

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

    Jump('loc_9F3')

    def _loc_97B(): pass

    label('loc_97B')

    SetChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002B, 0x0080)
    SetChrFlags(0x002C, 0x0080)
    SetChrFlags(0x002D, 0x0080)
    SetChrFlags(0x002E, 0x0080)
    SetChrFlags(0x002F, 0x0080)
    SetChrFlags(0x0030, 0x0080)
    SetChrFlags(0x0031, 0x0080)
    SetChrFlags(0x0032, 0x0080)
    SetChrFlags(0x0033, 0x0080)
    SetChrFlags(0x0034, 0x0080)
    SetChrFlags(0x0035, 0x0080)
    SetChrFlags(0x0036, 0x0080)
    SetChrFlags(0x0037, 0x0080)
    SetChrFlags(0x0038, 0x0080)
    SetChrFlags(0x0039, 0x0080)
    SetChrFlags(0x003A, 0x0080)
    SetChrFlags(0x003B, 0x0080)
    SetChrFlags(0x003C, 0x0080)
    SetChrFlags(0x003D, 0x0080)
    SetChrFlags(0x003E, 0x0080)
    SetChrFlags(0x003F, 0x0080)
    SetChrFlags(0x0040, 0x0080)
    SetChrFlags(0x0041, 0x0080)

    def _loc_9F3(): pass

    label('loc_9F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 3, 0x59B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A05',
    )

    OP_6F(0x0000, 0)

    Jump('loc_A0C')

    def _loc_A05(): pass

    label('loc_A05')

    OP_6F(0x0000, 60)

    def _loc_A0C(): pass

    label('loc_A0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 4, 0x59C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A1E',
    )

    OP_6F(0x0002, 0)

    Jump('loc_A25')

    def _loc_A1E(): pass

    label('loc_A1E')

    OP_6F(0x0002, 60)

    def _loc_A25(): pass

    label('loc_A25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 5, 0x59D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A37',
    )

    OP_6F(0x0001, 0)

    Jump('loc_A3E')

    def _loc_A37(): pass

    label('loc_A37')

    OP_6F(0x0001, 60)

    def _loc_A3E(): pass

    label('loc_A3E')

    Return()

# id: 0x0002 offset: 0xA3F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A71',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A65',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_A6E')

    def _loc_A65(): pass

    label('loc_A65')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    def _loc_A6E(): pass

    label('loc_A6E')

    Jump('ReInit')

    def _loc_A71(): pass

    label('loc_A71')

    Return()

# id: 0x0003 offset: 0xA72
@scena.Code('func_03_A72')
def func_03_A72():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(47020, 0, -37820, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 46440, 0, -37370, 135)
    SetChrPos(0x0102, 47530, 0, -38220, 315)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080129V#002F对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080130V托兰特平原道那么大，\n',
            '我们要从哪里找起才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080131V#015F这个嘛……\n',
            '因为那个客人是要找景色漂亮的场所。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080132V#012F所以很有可能去了\n',
            '铺设了砖块的大路以外的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080133V#007F糟糕～……\n',
            '那不是更危险了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080134V#002F不管了！\n',
            '赶紧找到，然后带她回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0040, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xC13
@scena.Code('func_04_C13')
def func_04_C13():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1EFE',
    )

    SetScenaFlags(ScenaFlag(0x00A4, 2, 0x522))
    OP_28(0x0040, 0x01, 0x0100)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -46310, 110, 840, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0009, -47620, -30, -2150, 0)
    SetChrPos(0x000A, -45450, -50, -2620, 0)
    SetChrPos(0x000B, -44530, 40, -1070, 0)
    SetChrPos(0x000C, -42950, 40, 330, 0)
    SetChrPos(0x000D, -43940, 10, 2780, 0)
    ChrTurnDirection(0x0009, 0x0008, 0)
    ChrTurnDirection(0x000A, 0x0008, 0)
    ChrTurnDirection(0x000B, 0x0008, 0)
    ChrTurnDirection(0x000C, 0x0008, 0)
    ChrTurnDirection(0x000D, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x000B, 0)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)

    NpcTalk(
        0x0008,
        '女孩的声音',
        (
            '#0280080152V呜～哇……！\n',
            '讨厌讨厌，救命啦～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080153V#002F刚刚的声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080154V#012F嗯，很近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女孩的声音',
        (
            '#0280080155V女神啊～！\n',
            '爸爸，妈妈～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女孩的声音',
        (
            '#0280080156V奈尔前辈～！\n',
            '快来救救我呀～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010080157V#509F这、这好像是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080158V#012F果然不出我所料。\n',
            '……我们赶快上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    Sleep(100)

    Fade(1000)
    CameraMove(-46630, 80, 1280, 0)
    OP_6C(0, 0)
    OP_B7(0x000F, 0x01)
    FormationAddMember(0x0F, 0xFF)
    SetChrFlags(0x0110, 0x0008)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    OP_0D()
    OP_21()
    PlayBGM(81)
    Sleep(500)

    PlaySE(403, 0x00, 0x64)

    ChrTalk(
        0x000B,
        (
            '……嗷呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080160V#154F#1P各、各位狗大哥……\n',
            '我们稍微先商量一下行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080161V我、我可是\n',
            '一点儿也不好吃的哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080162V我每天睡１２个小时以上，\n',
            '吃的都是些蔬菜水果，\n',
            '而且皮肤也很光滑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080163V#153F……哎呀，我怎么反而\n',
            '说得自己又健康又美味的呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(403, 0x00, 0x64)

    ChrTalk(
        0x000B,
        (
            '嗷呜呜呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_100B')
    def lambda_100B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_100B')

    DispatchAsync2(0x0009, 0x0002, lambda_100B)

    @scena.Lambda('lambda_101C')
    def lambda_101C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_101C')

    DispatchAsync2(0x000A, 0x0001, lambda_101C)

    @scena.Lambda('lambda_102D')
    def lambda_102D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_102D')

    DispatchAsync2(0x000B, 0x0001, lambda_102D)

    @scena.Lambda('lambda_103E')
    def lambda_103E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_103E')

    DispatchAsync2(0x000C, 0x0001, lambda_103E)

    @scena.Lambda('lambda_104F')
    def lambda_104F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_104F')

    DispatchAsync2(0x000D, 0x0002, lambda_104F)

    @scena.Lambda('lambda_1060')
    def lambda_1060():
        CameraMove(-48670, -60, 3500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1060)

    SetChrChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_107D')
    def lambda_107D():
        ChrWalkTo(0x00FE, -45950, 100, 460, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_107D)

    Sleep(300)

    SetChrChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_10A2')
    def lambda_10A2():
        ChrMoveTo(0x00FE, -49790, 30, 320, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10A2)

    Sleep(100)

    SetChrChipByIndex(0x000D, 2)

    @scena.Lambda('lambda_10C7')
    def lambda_10C7():
        ChrMoveTo(0x00FE, -46480, -30, 4210, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_10C7)

    Sleep(200)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_10F9')
    def lambda_10F9():
        ChrMoveTo(0x0008, -49280, -70, 3340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_10F9)

    Sleep(500)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_111E')
    def lambda_111E():
        ChrWalkTo(0x00FE, -48040, 60, 150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_111E)

    Sleep(300)

    SetChrChipByIndex(0x000C, 2)

    @scena.Lambda('lambda_1143')
    def lambda_1143():
        ChrWalkTo(0x00FE, -45780, 0, 2640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1143)

    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 1)
    WaitForThreadExit(0x000D, 0x0001)
    SetChrChipByIndex(0x000D, 1)
    WaitForThreadExit(0x000B, 0x0002)
    SetChrChipByIndex(0x000B, 1)
    WaitForThreadExit(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 1)
    WaitForThreadExit(0x000C, 0x0002)
    SetChrChipByIndex(0x000C, 1)

    ChrTalk(
        0x0008,
        (
            '#0280080165V#152F#1P呜～呜。\n',
            '早知道会这样，\n',
            '就应该预支薪水大吃特吃的啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 8)
    SetChrChipByIndex(0x000C, 1)
    SetChrPos(0x0101, -44480, -70, -4400, 0)
    SetChrPos(0x0102, -40040, 10, -840, 0)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    Sleep(100)

    @scena.Lambda('lambda_1228')
    def lambda_1228():
        CameraMove(-47620, 30, 2760, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1228)

    SetChrChipByIndex(0x0101, 6)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_124A')
    def lambda_124A():
        OP_99(0x0101, 0x00, 0x0C, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_124A)

    @scena.Lambda('lambda_125A')
    def lambda_125A():
        ChrWalkTo(0x00FE, -45860, 50, -820, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_125A)

    @scena.Lambda('lambda_1275')
    def lambda_1275():
        ChrWalkTo(0x00FE, -45290, 90, 430, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1275)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1295')
    def lambda_1295():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_1295')

    DispatchAsync2(0x0101, 0x0002, lambda_1295)

    @scena.Lambda('lambda_12A6')
    def lambda_12A6():
        ChrJumpTo(0x00FE, -47620, -30, 2760, 500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12A6)

    Sleep(50)

    TerminateThread(0x000B, 0xFF)
    SetChrFlags(0x000B, 0x0020)
    SetChrFlags(0x000B, 0x1000)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 0)
    PlayEffect(0x08, 0xFF, 0x000B, 0, 2000, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1316')
    def lambda_1316():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 4000, 8000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1316)

    Sleep(50)

    @scena.Lambda('lambda_1339')
    def lambda_1339():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1339')

    DispatchAsync2(0x000C, 0x0002, lambda_1339)

    @scena.Lambda('lambda_134A')
    def lambda_134A():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_134A')

    DispatchAsync2(0x000D, 0x0002, lambda_134A)

    @scena.Lambda('lambda_135B')
    def lambda_135B():
        ChrMoveTo(0x00FE, -44410, 10, 2690, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_135B)

    @scena.Lambda('lambda_1376')
    def lambda_1376():
        ChrMoveTo(0x00FE, -46180, 0, 5460, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1376)

    SetChrChipByIndex(0x0102, 9)
    PlayEffect(0x12, 0xFF, 0x0102, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_13CB')
    def lambda_13CB():
        OP_99(0x0102, 0x00, 0x0C, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_13CB)

    @scena.Lambda('lambda_13DB')
    def lambda_13DB():
        ChrJumpTo(0x00FE, -48060, 50, 1440, 3000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_13DB)

    Sleep(350)

    PlaySE(501, 0x00, 0x64)
    PlayEffect(0x08, 0xFF, 0x000B, 0, 1000, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1438')
    def lambda_1438():
        ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1438)

    ChrMoveTo(0x000B, -46980, 100, 850, 15000, 0x00)

    @scena.Lambda('lambda_145E')
    def lambda_145E():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_145E')

    DispatchAsync2(0x0102, 0x0002, lambda_145E)

    @scena.Lambda('lambda_146F')
    def lambda_146F():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_146F')

    DispatchAsync2(0x0009, 0x0002, lambda_146F)

    @scena.Lambda('lambda_1480')
    def lambda_1480():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1480')

    DispatchAsync2(0x000A, 0x0002, lambda_1480)

    @scena.Lambda('lambda_1491')
    def lambda_1491():
        ChrMoveTo(0x00FE, -50240, 30, -580, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1491)

    @scena.Lambda('lambda_14AC')
    def lambda_14AC():
        ChrMoveTo(0x00FE, -47800, -20, -1160, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_14AC)

    ChrJumpToRelative(0x000B, -1000, 0, 0, 1000, 3000)
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#0280080166V#153F哈……\n',
            '你、你们是～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080167V#006F呼……\n',
            '果然不出所料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080168V#010F朵洛希小姐，\n',
            '已经不用担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080169V#155F…………………………\n',
            '……你们，是什么人来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080170V#007F……（晕倒）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080171V#018F……我们是游击士协会的\n',
            '艾丝蒂尔·布莱特和约修亚·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080172V#151F哦呵呵，开玩笑的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080173V小艾、小约。\n',
            '能在这里碰面，我们真是有缘呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080174V#509F真、真是受不了她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080175V#016F艾丝蒂尔，来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_16AF')
    def lambda_16AF():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_16AF)

    SetChrChipByIndex(0x000C, 2)

    @scena.Lambda('lambda_16CA')
    def lambda_16CA():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_16CA)

    Sleep(50)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_16EA')
    def lambda_16EA():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16EA)

    SetChrChipByIndex(0x000D, 2)

    @scena.Lambda('lambda_1705')
    def lambda_1705():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1705)

    Sleep(200)

    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    Battle(0x000003A5, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1747'),
        (-1, 'loc_174A'),
    )

    def _loc_1747(): pass

    label('loc_1747')

    OP_B4(0x00)

    Return()

    def _loc_174A(): pass

    label('loc_174A')

    EventBegin(0x00)
    CameraMove(-48280, -30, 2740, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0110, 0x0008)
    SetChrPos(0x0110, -51180, 0, 4520, 135)
    SetChrPos(0x0101, -47620, -30, 2760, 90)
    SetChrPos(0x0102, -48060, 50, 1440, 225)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080176V#006F呼……\n',
            '总算是收拾它们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)
    SetChrChipByIndex(0x0101, 65535)

    ChrTalk(
        0x0102,
        (
            '#0020080177V#012F艾丝蒂尔，你发现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080178V#002F嗯……\n',
            '是袭击山顶关所的魔兽吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080179V为什么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080180V#151F哇～厉害厉害。\n',
            '真不愧是游击士呢～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18C0')
    def lambda_18C0():
        ChrTurnDirection(0x00FE, 0x0110, 400)
        Yield()

        Jump('lambda_18C0')

    DispatchAsync2(0x0101, 0x0001, lambda_18C0)

    @scena.Lambda('lambda_18D1')
    def lambda_18D1():
        ChrTurnDirection(0x00FE, 0x0110, 400)
        Yield()

        Jump('lambda_18D1')

    DispatchAsync2(0x0102, 0x0001, lambda_18D1)

    @scena.Lambda('lambda_18E2')
    def lambda_18E2():
        CameraSetDistance(2690, 2300)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_18E2)

    ChrWalkTo(0x0110, -48890, -30, 2600, 3000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0110,
        (
            '#0280080181V#151F我们好久不见啦～～\n',
            '小艾，小约。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080182V真没想到会在\n',
            '这么特别的地方碰上你们～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080183V#155F啊～～\n',
            '难道这就是所谓命运的重逢吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080184V#007F是厄运吧，厄运……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080185V#010F对了，朵洛希小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080186V你就是那个\n',
            '住在亚尔摩旅馆的客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080187V#153F是啊……\n',
            '咦～小约你是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向朵洛希说明了\n',
            '亚尔摩旅馆的老板娘委托保护客人的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0110,
        (
            '#0280080188V#151F啊，是这样啊～\n',
            '你们还真是辛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080189V#007F什～么～呀，\n',
            '别说得好像事不关己似的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080190V#000F话说回来，\n',
            '你来街道外面到底想要干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080191V#151F嘻嘻嘻……\n',
            '这还不知道吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080192V哦呵呵呵，\n',
            '小艾的洞察力还是不够呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080193V#009F你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080194V#150F公布答案～我是来找\n',
            '用在这次特辑上的照片素材～的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080195V对了对了，\n',
            '还要顺便完成奈尔前辈给我的作业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080196V#010F原来如此，是为了工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080197V#007F就算是这样，\n',
            '也不用在这种地方找素材啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080198V啊啊，真是的～\n',
            '总觉得对你讲道理比战斗还要累人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080199V#154F你不要紧吧～小艾？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080200V别生气别生气，小艾是最乖的了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080201V#005F#3S害我们这么累还想逃避责任吗！\n',
            '别说得那么顺理成章的！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080202V#015F（还真是少见啊……\n',
            '竟然有人可以让艾丝蒂尔如此没辙。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080203V#010F好了，艾丝蒂尔。\n',
            '总之先回村子去吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080204V导力泵的修理\n',
            '也应该差不多结束了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080205V#007F唉唉……是、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080206V#509F听到了没有……\n',
            '朵洛希也要一起回去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080207V#154F咦～我还想拍照片呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080208V#001F#3S一·起·回·去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080209V#152F小艾……好吓人哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    EventEnd(0x00)

    def _loc_1EFE(): pass

    label('loc_1EFE')

    Return()

# id: 0x0005 offset: 0x1EFF
@scena.Code('func_05_1EFF')
def func_05_1EFF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 2, 0x52A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 1, 0x529)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27A2',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 2, 0x52A))
    EventBegin(0x00)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -21840, 0, 52760, 180)

    NpcTalk(
        0x000E,
        '男人的声音',
        (
            '#0080080632V哦哦，你们来得正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0107, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0110, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    Fade(1000)
    CameraMove(-22010, 0, 41300, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -21580, 0, 38890, 0)
    SetChrPos(0x0102, -22680, 0, 38930, 0)
    SetChrPos(0x0107, -21390, 0, 37530, 0)
    SetChrPos(0x0110, -22380, 0, 37650, 0)

    @scena.Lambda('lambda_202B')
    def lambda_202B():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_202B')

    DispatchAsync2(0x0101, 0x0002, lambda_202B)

    @scena.Lambda('lambda_203C')
    def lambda_203C():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_203C')

    DispatchAsync2(0x0102, 0x0002, lambda_203C)

    @scena.Lambda('lambda_204D')
    def lambda_204D():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_204D')

    DispatchAsync2(0x0107, 0x0002, lambda_204D)

    @scena.Lambda('lambda_205E')
    def lambda_205E():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_205E')

    DispatchAsync2(0x0110, 0x0002, lambda_205E)

    OP_0D()
    ChrWalkTo(0x000E, -22000, 0, 42280, 4000, 0x00)

    ChrTalk(
        0x000E,
        (
            '#0080080633V#070F哟，各位小姐，\n',
            '有样东西想请问一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080634V#004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080635V#064F哇，好高大的叔叔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080636V#153F哇哇～～熊、熊先生吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080080637V#074F熊……咳咳，也罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080638V#070F我不是什么坏人，\n',
            '只是想问个路而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080639V你们知道那个\n',
            '叫亚尔摩的温泉乡在哪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080640V#501F哦，你说亚尔摩村啊～\n',
            '那地方正好在我们刚刚走来的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080641V#010F嗯，再走一段路就到了。\n',
            '请从这里沿着大路一直向南走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080080642V#071F哦哦，是啊。\n',
            '多谢你们指路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0080080643V#073F哦？你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080644V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080645V#004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080080646V#073F嗯，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080647V你们难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080648V#010F我们有什么奇怪的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080080649V#070F啊，不好意思。\n',
            '没什么大不了的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080650V那么再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2374')
    def lambda_2374():
        OP_6C(0, 2500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2374)

    @scena.Lambda('lambda_2384')
    def lambda_2384():
        CameraMove(-22090, 0, 38340, 2500)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_2384)

    @scena.Lambda('lambda_239C')
    def lambda_239C():
        ChrWalkTo(0x00FE, -20180, 0, 40860, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_239C)

    WaitForThreadExit(0x000E, 0x0001)
    ChrWalkTo(0x000E, -20180, 0, 26000, 4000, 0x00)
    SetChrFlags(0x000E, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0110, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010080651V#505F总觉得有种外国人的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080652V#505F穿着东方风格的服装，\n',
            '刚才那大叔应该是从外国来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2452')
    def lambda_2452():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2452)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020080653V#010F蔡斯地区的东面是\n',
            '与卡尔瓦德共和国接壤的地方，\n',
            '那里有一座名为『沃尔费堡垒』的关所。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080654V说不定他就是从那边过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0110, 0, 600)
    SetChrDirection(0x0107, 0, 600)

    ChrTalk(
        0x0107,
        (
            '#0070080655V#060F嗯，我也觉得是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080656V毛婆婆也是东方人呢。\n',
            '反正蔡斯地区一直都住着\n',
            '很多从共和国那边过来的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080657V#501F啊，的确是啊。\n',
            '说起来雾香姐也是东方人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080658V#151F不过不过～\n',
            '那个熊先生真的好高大啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080659V吓了我一大跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080660V#067F呵呵……\n',
            '也真的很像熊那样魁梧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080661V#006F身材的确就像熊那样魁梧，\n',
            '不过，可没有熊那样简单哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080662V看得出他有着相当深厚的武术造诣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080663V#064F姐姐看得出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080664V#502F那当然啦～\n',
            '好歹我也是个武术家嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080665V那个大叔不仅身材高大，\n',
            '而且体格也经过了相当的锻炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080666V#010F是啊……\n',
            '走起路来沉稳有力，毫不拖泥带水。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080667V说不定和艾丝蒂尔说的一样，\n',
            '那位先生真的是位武术高人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_2B13')

    def _loc_27A2(): pass

    label('loc_27A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 3, 0x523)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B13',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A0C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2995',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28B3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010080135V#002F唔～找不到啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080136V我觉得不可能往再远的地方去了啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080137V#010F确实，根据时间来推算\n',
            '应该不会走得这么远。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080138V还是在附近的平原再仔细找找吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080139V#002F嗯，就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2992')

    def _loc_28B3(): pass

    label('loc_28B3')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080140V#002F喂，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080141V我觉得不可能往再远的地方去了啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080142V#010F确实，根据时间来推算\n',
            '应该不会走得这么远。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080143V还是在附近的平原再仔细找找吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080144V#002F嗯，就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2992(): pass

    label('loc_2992')

    Jump('loc_2A09')

    def _loc_2995(): pass

    label('loc_2995')

    @scena.Lambda('lambda_299B')
    def lambda_299B():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_299B)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080145V#010F根据时间来推算\n',
            '应该不会走得这么远。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080146V还是在附近的平原再仔细找找吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2A09(): pass

    label('loc_2A09')

    Jump('loc_2AF8')

    def _loc_2A0C(): pass

    label('loc_2A0C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A9C',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080147V#010F艾丝蒂尔，\n',
            '赶快回亚尔摩村吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080148V旅馆的人们肯定还在担心呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080149V#000F啊，说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AF8')

    def _loc_2A9C(): pass

    label('loc_2A9C')

    ChrTalk(
        0x0102,
        (
            '#0020080150V#010F这边是蔡斯啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080151V旅馆的人们肯定还在担心呢。\n',
            '还是赶快回亚尔摩村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AF8(): pass

    label('loc_2AF8')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_2B13(): pass

    label('loc_2B13')

    Return()

# id: 0x0006 offset: 0x2B14
@scena.Code('func_06_2B14')
def func_06_2B14():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 3, 0x59B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C04',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_2B8A',
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
    SetScenaFlags(ScenaFlag(0x00B3, 3, 0x59B))

    Jump('loc_2C01')

    def _loc_2B8A(): pass

    label('loc_2B8A')

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

    def _loc_2C01(): pass

    label('loc_2C01')

    Jump('loc_2C3A')

    def _loc_2C04(): pass

    label('loc_2C04')

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
    WaitEffect(0x0F, 0x8F)
    def _loc_2C3A(): pass

    label('loc_2C3A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x2C48
@scena.Code('func_07_2C48')
def func_07_2C48():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 4, 0x59C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D38',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_2CBE',
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
    SetScenaFlags(ScenaFlag(0x00B3, 4, 0x59C))

    Jump('loc_2D35')

    def _loc_2CBE(): pass

    label('loc_2CBE')

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

    def _loc_2D35(): pass

    label('loc_2D35')

    Jump('loc_2D6E')

    def _loc_2D38(): pass

    label('loc_2D38')

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
    WaitEffect(0x0F, 0x90)
    def _loc_2D6E(): pass

    label('loc_2D6E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x2D7C
@scena.Code('func_08_2D7C')
def func_08_2D7C():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 5, 0x59D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F3C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 6, 0x59E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E74',
    )

    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    SetChrPos(0x0011, -44130, 1500, -55170, 320)
    ChrTurnDirection(0x0011, 0x0000, 0)

    @scena.Lambda('lambda_2DCB')
    def lambda_2DCB():
        ChrMoveTo(0x00FE, -44130, 1000, -55170, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2DCB)

    @scena.Lambda('lambda_2DE6')
    def lambda_2DE6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2DE6)

    ClearChrFlags(0x0011, 0x0080)

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
        'loc_2E29',
    )

    Battle(0x00000356, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2E36')

    def _loc_2E29(): pass

    label('loc_2E29')

    Battle(0x00000216, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_2E36(): pass

    label('loc_2E36')

    SetChrFlags(0x0011, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E4F'),
        (0x00000002, 'loc_2E61'),
        (0x00000001, 'loc_2E71'),
        (-1, 'loc_2E74'),
    )

    def _loc_2E4F(): pass

    label('loc_2E4F')

    SetScenaFlags(ScenaFlag(0x00B3, 6, 0x59E))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_2E74')

    def _loc_2E61(): pass

    label('loc_2E61')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_2E71(): pass

    label('loc_2E71')

    OP_B4(0x00)

    Return()

    def _loc_2E74(): pass

    label('loc_2E74')

    If(
        (
            (Expr.Eval, "AddItem(0x026C, 1)"),
            Expr.Return,
        ),
        'loc_2EC8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '命中３',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B3, 5, 0x59D))

    Jump('loc_2F39')

    def _loc_2EC8(): pass

    label('loc_2EC8')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '命中３',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '命中３',
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

    def _loc_2F39(): pass

    label('loc_2F39')

    Jump('loc_2F72')

    def _loc_2F3C(): pass

    label('loc_2F3C')

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
    WaitEffect(0x0F, 0x91)
    def _loc_2F72(): pass

    label('loc_2F72')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
