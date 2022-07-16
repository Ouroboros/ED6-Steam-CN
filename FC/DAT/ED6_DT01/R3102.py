import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '王'),
    TXT(0x02, '布鲁诺'),
    TXT(0x03, '装甲兔'),
    TXT(0x04, '装甲兔'),
    TXT(0x05, '装甲兔'),
    TXT(0x06, '装甲兔'),
    TXT(0x07, '装甲兔'),
    TXT(0x08, '装甲兔'),
    TXT(0x09, '车'),
    TXT(0x0A, '装甲兔'),
    TXT(0x0B, '装甲兔'),
    TXT(0x0C, '装甲兔'),
    TXT(0x0D, '装甲兔'),
    TXT(0x0E, ''),
    TXT(0x0F, ''),
    TXT(0x10, '蔡斯方向'),
    TXT(0x11, '沃尔费堡垒方向'),
    TXT(0x12, '红莲之塔方向'),
    TXT(0x13, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3102.x'
    header.mapIndex       = 144
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/R3102._SN', 'ED6_DT01/R3102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1516
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
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT09/CH10123._CH', 'ED6_DT09/CH10123P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00490._CH', 'ED6_DT07/CH00490P._CP'),
        ('ED6_DT07/CH00491._CH', 'ED6_DT07/CH00491P._CP'),
        ('ED6_DT09/CH10120._CH', 'ED6_DT09/CH10120P._CP'),
        ('ED6_DT09/CH10121._CH', 'ED6_DT09/CH10121P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00492._CH', 'ED6_DT07/CH00492P._CP'),
        ('ED6_DT07/CH00494._CH', 'ED6_DT07/CH00494P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT06/CH20119._CH', 'ED6_DT06/CH20119P._CP'),
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
        ('ED6_DT07/CH00000._CH', 'ED6_DT09/CH10080P._CP'),
        ('ED6_DT07/CH00000._CH', 'ED6_DT09/CH10081P._CP'),
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
        ('ED6_DT09/CH11240._CH', 'ED6_DT09/CH11240P._CP'),
        ('ED6_DT09/CH11241._CH', 'ED6_DT09/CH11241P._CP'),
    ]

# id: 0x10002 offset: 0x1A2
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -27260,
            z                   = 20,
            y                   = -22270,
            direction           = 357,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -74130,
            z                   = 0,
            y                   = 3100,
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
            x                   = 64319,
            z                   = 10,
            y                   = -52920,
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
            x                   = 10040,
            z                   = -130,
            y                   = 67800,
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

# id: 0x10003 offset: 0x3E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -36940,
            z           = -10,
            y           = 10890,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28070,
            z           = 80,
            y           = 10280,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17490,
            z           = 0,
            y           = -1540,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 4150,
            z           = -60,
            y           = 15540,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x021B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 32970,
            z           = -30,
            y           = 25660,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 26690,
            z           = 50,
            y           = 5570,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13500,
            z           = -20,
            y           = -4890,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34620,
            z           = -50,
            y           = -10530,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37440,
            z           = -50,
            y           = -24530,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0212,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15930,
            z           = 0,
            y           = -38970,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0211,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35920,
            z           = -20,
            y           = -35400,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -29740,
            z           = -110,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19490,
            z           = 0,
            y           = -17710,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12390,
            z           = 50,
            y           = -16010,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x021B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5230,
            z           = 0,
            y           = -27150,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 11730,
            z           = -30,
            y           = 7970,
            word_0C     = 0x0000,
            word_0E     = 0x001D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x05E0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -36940,
            z           = -10,
            y           = 10890,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28070,
            z           = 80,
            y           = 10280,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17490,
            z           = 0,
            y           = -1540,
            word_0C     = 0x00B4,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 4150,
            z           = -60,
            y           = 15540,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x035B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 32970,
            z           = -30,
            y           = 25660,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 26690,
            z           = 50,
            y           = 5570,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13500,
            z           = -20,
            y           = -4890,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0351,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34620,
            z           = -50,
            y           = -10530,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0351,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37440,
            z           = -50,
            y           = -24530,
            word_0C     = 0x00B4,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0352,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15930,
            z           = 0,
            y           = -38970,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0351,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35920,
            z           = -20,
            y           = -35400,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -29740,
            z           = -110,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19490,
            z           = 0,
            y           = -17710,
            word_0C     = 0x00B4,
            word_0E     = 0x0019,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12390,
            z           = 50,
            y           = -16010,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x035B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5230,
            z           = 0,
            y           = -27150,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x034D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 11730,
            z           = -30,
            y           = 7970,
            word_0C     = 0x0000,
            word_0E     = 0x001D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x05E1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x762
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -27260,
            y           = -1000,
            z           = -22270,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10005 offset: 0x782
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 13630,
            triggerZ            = 0,
            triggerY            = 35620,
            triggerRange        = 1500,
            actorX              = 13630,
            actorZ              = 1200,
            actorY              = 35620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3130,
            triggerZ            = 30,
            triggerY            = -11320,
            triggerRange        = 1000,
            actorX              = -3130,
            actorZ              = 30,
            actorY              = -10750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x7CA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_7D4',
    )

    Jump('loc_86C')

    def _loc_7D4(): pass

    label('loc_7D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_7DE',
    )

    Jump('loc_86C')

    def _loc_7DE(): pass

    label('loc_7DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_7E8',
    )

    Jump('loc_86C')

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_7F2',
    )

    Jump('loc_86C')

    def _loc_7F2(): pass

    label('loc_7F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_7FC',
    )

    Jump('loc_86C')

    def _loc_7FC(): pass

    label('loc_7FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_806',
    )

    Jump('loc_86C')

    def _loc_806(): pass

    label('loc_806')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_847',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_844',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -19060, -10, -40450, 145)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -17490, 10, -39610, 182)

    def _loc_844(): pass

    label('loc_844')

    Jump('loc_86C')

    def _loc_847(): pass

    label('loc_847')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_851',
    )

    Jump('loc_86C')

    def _loc_851(): pass

    label('loc_851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_85B',
    )

    Jump('loc_86C')

    def _loc_85B(): pass

    label('loc_85B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_865',
    )

    Jump('loc_86C')

    def _loc_865(): pass

    label('loc_865')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_86C',
    )

    def _loc_86C(): pass

    label('loc_86C')

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x879
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -131000, -126000, 196655)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8A3',
    )

    OP_B1('R3102_y')

    Jump('loc_8AC')

    def _loc_8A3(): pass

    label('loc_8A3')

    OP_B1('R3102_n')

    def _loc_8AC(): pass

    label('loc_8AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90B',
    )

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

    Jump('loc_95B')

    def _loc_90B(): pass

    label('loc_90B')

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

    def _loc_95B(): pass

    label('loc_95B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_96C',
    )

    OP_1B(0x03, 0x00, 0x0006)

    def _loc_96C(): pass

    label('loc_96C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_983',
    )

    Jump('loc_988')

    def _loc_983(): pass

    label('loc_983')

    OP_71(0x0000, 0x0004)

    def _loc_988(): pass

    label('loc_988')

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            (Expr.Eval, "OP_29(0x0032, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0032, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B9, 1, 0x5C9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9B6',
    )

    ClearChrFlags(0x0016, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_9B6(): pass

    label('loc_9B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 0, 0x5A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9C8',
    )

    OP_6F(0x0001, 0)

    Jump('loc_9CF')

    def _loc_9C8(): pass

    label('loc_9C8')

    OP_6F(0x0001, 60)

    def _loc_9CF(): pass

    label('loc_9CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9E0',
    )

    OP_1B(0x01, 0x00, 0x0005)

    def _loc_9E0(): pass

    label('loc_9E0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9F7',
    )

    SetChrFlags(0x0029, 0x0080)
    SetChrFlags(0x0039, 0x0080)

    def _loc_9F7(): pass

    label('loc_9F7')

    Return()

# id: 0x0002 offset: 0x9F8
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A1D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_AB0')

    def _loc_A1D(): pass

    label('loc_A1D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A36',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_AB0')

    def _loc_A36(): pass

    label('loc_A36')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A4F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_AB0')

    def _loc_A4F(): pass

    label('loc_A4F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A68',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_AB0')

    def _loc_A68(): pass

    label('loc_A68')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A81',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_AB0')

    def _loc_A81(): pass

    label('loc_A81')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A9A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_AB0')

    def _loc_A9A(): pass

    label('loc_A9A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AB0',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_AB0(): pass

    label('loc_AB0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AC5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_AB0')

    def _loc_AC5(): pass

    label('loc_AC5')

    Return()

# id: 0x0003 offset: 0xAC6
@scena.Code('func_03_AC6')
def func_03_AC6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_B99',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0346)"),
            (Expr.Eval, "OP_29(0x0028, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AEB',
    )

    Call(1, 0x0003)

    Jump('loc_B99')

    def _loc_AEB(): pass

    label('loc_AEB')

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x01, 0x0001)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AFE',
    )

    Call(1, 0x0002)

    Jump('loc_B99')

    def _loc_AFE(): pass

    label('loc_AFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B49',
    )

    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '#2060180703V怎么样，布鲁诺先生？\n',
            '是不是相当麻烦啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B96')

    def _loc_B49(): pass

    label('loc_B49')

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#2060180704V我们要留在这里\n',
            '继续努力试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2060180705V你们也要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B96(): pass

    label('loc_B96')

    TalkEnd(0x00FE)

    def _loc_B99(): pass

    label('loc_B99')

    Return()

# id: 0x0004 offset: 0xB9A
@scena.Code('func_04_B9A')
def func_04_B9A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_F2C',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0346)"),
            (Expr.Eval, "OP_29(0x0028, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0029, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BBF',
    )

    Call(1, 0x0003)

    Jump('loc_F2C')

    def _loc_BBF(): pass

    label('loc_BBF')

    If(
        (
            (Expr.Eval, "OP_29(0x0028, 0x01, 0x0001)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BD2',
    )

    Call(1, 0x0002)

    Jump('loc_F2C')

    def _loc_BD2(): pass

    label('loc_BD2')

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_C49',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#2070180714V呼，果然还是要\n',
            '亲自去把零件给取回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180719V也罢，自己的事情\n',
            '还是只有靠自己来做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2C')

    def _loc_C49(): pass

    label('loc_C49')

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_E36',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_28(0x0029, 0x01, 0x4000)

    ChrTalk(
        0x00FE,
        (
            '#2070180710V哦，怎么样了。\n',
            '和普罗梅笛先生取得联系了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180711V#000F唔～嗯，是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔告诉了他们\n',
            '普罗梅笛已经不是运输车的管理员的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010180712V#000F……就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180713V怎么会这样。\n',
            '既然这样，真是抱歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180714V呼，果然还是要\n',
            '亲自去把零件给取回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180715V唉，\n',
            '给你们俩添了不少麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180716V也罢，自己的事情\n',
            '还是只有靠自己来做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180717V那就再见了，\n',
            '到亚尔摩的路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2C')

    def _loc_E36(): pass

    label('loc_E36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_EB5',
    )

    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    ClearChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '#2070180706V唔～唔，除了引擎故障，\n',
            '实在想不出什么别的原因啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180707V只好再全部\n',
            '重新检查一下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F29')

    def _loc_EB5(): pass

    label('loc_EB5')

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#2070180644V如果你们有空的话，\n',
            '请帮忙联络一下普罗梅笛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2070180645V他应该一直都在中央工房\n',
            '三楼的设计室里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F29(): pass

    label('loc_F29')

    TalkEnd(0x00FE)

    def _loc_F2C(): pass

    label('loc_F2C')

    Return()

# id: 0x0005 offset: 0xF2D
@scena.Code('func_05_F2D')
def func_05_F2D():
    OP_20(0x000005DC)
    OP_1B(0x01, 0x00, 0xFFFF)

    Return()

# id: 0x0006 offset: 0xF38
@scena.Code('func_06_F38')
def func_06_F38():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F8D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050090551V#050F……方向走反了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090552V总之现在还是回蔡斯吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD8')

    def _loc_F8D(): pass

    label('loc_F8D')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090553V#050F喂，方向走反了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090554V总之现在赶快回蔡斯吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FD8(): pass

    label('loc_FD8')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0007 offset: 0xFF4
@scena.Code('func_07_FF4')
def func_07_FF4():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　红莲之塔\n',
            '※魔兽较多，请注意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x1048
@scena.Code('func_08_1048')
def func_08_1048():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 7, 0x59F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_120E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B4, 0, 0x5A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1140',
    )

    ChrSetRGBAMask(0x0015, 255, 255, 255, 0, 0)
    SetChrPos(0x0015, -3130, 1500, -10750, 320)
    ChrTurnDirection(0x0015, 0x0000, 0)

    @scena.Lambda('lambda_1097')
    def lambda_1097():
        ChrMoveTo(0x00FE, -3130, 1000, -10750, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1097)

    @scena.Lambda('lambda_10B2')
    def lambda_10B2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_10B2)

    ClearChrFlags(0x0015, 0x0080)

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
        'loc_10F5',
    )

    Battle(0x00000357, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1102')

    def _loc_10F5(): pass

    label('loc_10F5')

    Battle(0x00000217, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_1102(): pass

    label('loc_1102')

    SetChrFlags(0x0015, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_111B'),
        (0x00000002, 'loc_112D'),
        (0x00000001, 'loc_113D'),
        (-1, 'loc_1140'),
    )

    def _loc_111B(): pass

    label('loc_111B')

    SetScenaFlags(ScenaFlag(0x00B4, 0, 0x5A0))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_1140')

    def _loc_112D(): pass

    label('loc_112D')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_113D(): pass

    label('loc_113D')

    OP_B4(0x00)

    Return()

    def _loc_1140(): pass

    label('loc_1140')

    If(
        (
            (Expr.Eval, "AddItem(0x0130, 1)"),
            Expr.Return,
        ),
        'loc_1196',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '黑色手镯',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B3, 7, 0x59F))

    Jump('loc_120B')

    def _loc_1196(): pass

    label('loc_1196')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '黑色手镯',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '黑色手镯',
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

    def _loc_120B(): pass

    label('loc_120B')

    Jump('loc_1244')

    def _loc_120E(): pass

    label('loc_120E')

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
    WaitEffect(0x0F, 0x92)
    def _loc_1244(): pass

    label('loc_1244')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x1252
@scena.Code('func_09_1252')
def func_09_1252():
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

    MenuEnd(0x0001)

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
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000001, 'loc_1337'),
        (-1, 'loc_13D1'),
    )

    def _loc_1337(): pass

    label('loc_1337')

    Fade(1000)
    SetChrPos(0x0000, -26250, -10, -14890, 192)
    SetChrPos(0x0001, -26250, -10, -14890, 192)
    SetChrPos(0x0002, -26250, -10, -14890, 192)
    SetChrPos(0x0003, -26250, -10, -14890, 192)
    SetChrPos(0x0004, -26250, -10, -14890, 192)
    SetChrPos(0x0005, -26250, -10, -14890, 192)
    SetChrPos(0x0006, -26250, -10, -14890, 192)
    SetChrPos(0x0007, -26250, -10, -14890, 192)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_13D1(): pass

    label('loc_13D1')

    Battle(0x000003FE, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrPos(0x0000, -26250, -10, -14890, 192)
    SetChrPos(0x0001, -26250, -10, -14890, 192)
    SetChrPos(0x0002, -26250, -10, -14890, 192)
    SetChrPos(0x0003, -26250, -10, -14890, 192)
    SetChrPos(0x0004, -26250, -10, -14890, 192)
    SetChrPos(0x0005, -26250, -10, -14890, 192)
    SetChrPos(0x0006, -26250, -10, -14890, 192)
    SetChrPos(0x0007, -26250, -10, -14890, 192)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_147F'),
        (0x00000001, 'loc_1482'),
        (-1, 'loc_1485'),
    )

    def _loc_147F(): pass

    label('loc_147F')

    EventEnd(0x00)

    Return()

    def _loc_1482(): pass

    label('loc_1482')

    OP_B4(0x00)

    Return()

    def _loc_1485(): pass

    label('loc_1485')

    EventBegin(0x01)
    SetChrFlags(0x0016, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '成功消灭了托兰特平原道中被通缉的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0032, 0x04, 0x10)
    OP_28(0x0032, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x00B9, 1, 0x5C9))
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
