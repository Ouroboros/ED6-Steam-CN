import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '王国军士官'),
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
    TXT(0x0E, '士兵'),
    TXT(0x0F, '士兵'),
    TXT(0x10, '士兵'),
    TXT(0x11, '亡命守护者'),
    TXT(0x12, '亡命守护者'),
    TXT(0x13, '亡命守护者'),
    TXT(0x14, '亡命守护者'),
    TXT(0x15, '亡命守护者'),
    TXT(0x16, '亡命守护者'),
    TXT(0x17, '目标'),
    TXT(0x18, '目标'),
    TXT(0x19, '目标'),
    TXT(0x1A, '目标'),
    TXT(0x1B, '目标'),
    TXT(0x1C, '目标'),
    TXT(0x1D, '蔡斯方向'),
    TXT(0x1E, '亚尔摩村方向'),
    TXT(0x1F, '沃尔费堡垒方向'),
    TXT(0x20, ''),
    TXT(0x21, ''),
    TXT(0x22, ''),
    TXT(0x23, ''),
    TXT(0x24, ''),
    TXT(0x25, ''),
    TXT(0x26, ''),
    TXT(0x27, ''),
    TXT(0x28, ''),
    TXT(0x29, ''),
    TXT(0x2A, ''),
    TXT(0x2B, ''),
    TXT(0x2C, ''),
    TXT(0x2D, ''),
    TXT(0x2E, ''),
    TXT(0x2F, ''),
    TXT(0x30, ''),
    TXT(0x31, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3100.x'
    header.mapIndex       = 1
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C4C
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
        ('ED6_DT09/CH11210._CH', 'ED6_DT09/CH11210P._CP'),
        ('ED6_DT09/CH11211._CH', 'ED6_DT09/CH11211P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT07/CH00336._CH', 'ED6_DT07/CH00336P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT29/CH12323._CH', 'ED6_DT29/CH12323P._CP'),
    ]

# id: 0x10002 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 19,
            chipIndex           = 19,
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
            dword_10            = 19,
            chipIndex           = 19,
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
            dword_10            = 19,
            chipIndex           = 19,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            npcIndex            = 0x0080,
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
            npcIndex            = 0x0080,
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
            npcIndex            = 0x0080,
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
            npcIndex            = 0x0080,
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
            npcIndex            = 0x0080,
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
            npcIndex            = 0x0080,
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

# id: 0x10003 offset: 0x55A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -31930,
            z           = -10,
            y           = 25570,
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
            x           = -17900,
            z           = -100,
            y           = 29570,
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
            x           = -17830,
            z           = -50,
            y           = 10270,
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
            x           = -33160,
            z           = 80,
            y           = 9720,
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
            x           = -33640,
            z           = -20,
            y           = -11610,
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
            x           = -34150,
            z           = 10,
            y           = -34210,
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
            x           = -17610,
            z           = 60,
            y           = -32390,
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
            x           = 13750,
            z           = 20,
            y           = 4540,
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
            x           = 28640,
            z           = -50,
            y           = -14990,
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
            x           = 39490,
            z           = -40,
            y           = 9070,
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
            x           = 28310,
            z           = 0,
            y           = 15860,
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
            x           = 19410,
            z           = -90,
            y           = 27970,
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
            x           = 20370,
            z           = 10,
            y           = 8119,
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
            x           = 21540,
            z           = 50,
            y           = 3820,
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
            x           = -43300,
            z           = 80,
            y           = -22610,
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
            x           = -25500,
            z           = 20,
            y           = 17440,
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
            x           = 7640,
            z           = 0,
            y           = 5540,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x736
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x736
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
            talkFunctionIndex   = 0x0014,
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
            talkFunctionIndex   = 0x0015,
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
            talkFunctionIndex   = 0x0016,
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
            talkFunctionIndex   = 0x0002,
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
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x7EA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_808',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0004)

    def _loc_808(): pass

    label('loc_808')

    Return()

# id: 0x0001 offset: 0x809
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0048, 0xFFFE13D0, 0x0023002D)

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
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_836',
    )

    OP_10(0x02, 0x00)
    OP_10(0x03, 0x01)

    def _loc_836(): pass

    label('loc_836')

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
        'loc_8E5',
    )

    If(
        (
            (Expr.GetChrWork, 0x104, 0x1C),
            (Expr.PushLong, 0x5B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E5',
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
        'loc_894',
    )

    OP_28(0x006E, 0x01, 0x0040)

    Jump('loc_8E5')

    def _loc_894(): pass

    label('loc_894')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A9',
    )

    OP_28(0x006E, 0x01, 0x0020)

    Jump('loc_8E5')

    def _loc_8A9(): pass

    label('loc_8A9')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8BE',
    )

    OP_28(0x006E, 0x01, 0x0010)

    Jump('loc_8E5')

    def _loc_8BE(): pass

    label('loc_8BE')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D3',
    )

    OP_28(0x006E, 0x01, 0x0008)

    Jump('loc_8E5')

    def _loc_8D3(): pass

    label('loc_8D3')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E5',
    )

    OP_28(0x006E, 0x01, 0x0004)

    def _loc_8E5(): pass

    label('loc_8E5')

    ExecExpressionWithValue(
        0x0031,
        0x24,
        (
            (Expr.PushLong, 0xBF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 0, 0x1500)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_902',
    )

    OP_6F(0x0000, 0)

    Jump('loc_909')

    def _loc_902(): pass

    label('loc_902')

    OP_6F(0x0000, 60)

    def _loc_909(): pass

    label('loc_909')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 1, 0x1501)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_91B',
    )

    OP_6F(0x0001, 0)

    Jump('loc_922')

    def _loc_91B(): pass

    label('loc_91B')

    OP_6F(0x0001, 60)

    def _loc_922(): pass

    label('loc_922')

    Return()

# id: 0x0002 offset: 0x923
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xEA, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 0, 0x1500)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A00',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['雨太公'], 1)"),
            Expr.Return,
        ),
        'loc_997',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['雨太公']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1500)

    Jump('loc_9FD')

    def _loc_997(): pass

    label('loc_997')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['雨太公']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['雨太公']),
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

    def _loc_9FD(): pass

    label('loc_9FD')

    Jump('loc_A31')

    def _loc_A00(): pass

    label('loc_A00')

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
    def _loc_A31(): pass

    label('loc_A31')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0xA3F
@scena.Code('func_03_A3F')
def func_03_A3F():
    UnlockAchievement(0x02, 0xEB, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 1, 0x1501)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B1C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蚯蚓'], 1)"),
            Expr.Return,
        ),
        'loc_AB3',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['蚯蚓']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1501)

    Jump('loc_B19')

    def _loc_AB3(): pass

    label('loc_AB3')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['蚯蚓']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['蚯蚓']),
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

    def _loc_B19(): pass

    label('loc_B19')

    Jump('loc_B4D')

    def _loc_B1C(): pass

    label('loc_B1C')

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
    def _loc_B4D(): pass

    label('loc_B4D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0xB5B
@scena.Code('func_04_B5B')
def func_04_B5B():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_6D(-27360, 10, 29020, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(322000, 0)
    OP_6E(345, 0)
    SetChrPos(0x0008, -29200, -70, 33610, 180)
    SetChrPos(0x0009, -24560, 0, 32650, 180)
    SetChrPos(0x000A, -23210, -40, 32509, 180)
    SetChrPos(0x000B, -23790, 0, 34420, 180)
    SetChrPos(0x000C, -30940, 10, 33050, 180)
    SetChrPos(0x000D, -30670, 70, 34610, 180)
    SetChrPos(0x000E, -32119, -10, 34350, 180)
    SetChrPos(0x000F, -21940, -20, 29970, 180)
    SetChrPos(0x0010, -20480, -20, 29690, 180)
    SetChrPos(0x0011, -21000, -10, 30930, 180)
    SetChrPos(0x0012, -37550, -70, 30440, 180)
    SetChrPos(0x0013, -38850, -170, 32369, 180)
    SetChrPos(0x0014, -37340, -100, 32500, 180)
    SetChrPos(0x0015, -27000, 400, 33740, 180)
    SetChrPos(0x0016, -34420, 400, 31580, 180)
    SetChrPos(0x0017, -22100, 400, 26090, 180)
    SetChrPos(0x0018, -28080, 0, -50520, 0)
    SetChrPos(0x0019, -24880, 0, -51600, 0)
    SetChrPos(0x001A, -28240, 10, -55120, 0)
    SetChrPos(0x001B, -25980, 0, -55110, 0)
    SetChrPos(0x001C, -26210, 0, -58780, 0)
    SetChrPos(0x001D, -25980, 0, -62040, 0)
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
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0015, 0x0004)
    SetChrFlags(0x0016, 0x0004)
    SetChrFlags(0x0017, 0x0004)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    SetChrFlags(0x0018, 0x0004)
    SetChrFlags(0x0019, 0x0004)
    SetChrFlags(0x001A, 0x0004)
    SetChrFlags(0x001B, 0x0004)
    SetChrFlags(0x001C, 0x0004)
    SetChrFlags(0x001D, 0x0004)
    SetChrFlags(0x0018, 0x0800)
    SetChrFlags(0x0019, 0x0800)
    SetChrFlags(0x001A, 0x0800)
    SetChrFlags(0x001B, 0x0800)
    SetChrFlags(0x001C, 0x0800)
    SetChrFlags(0x001D, 0x0800)
    LoadEffect(0x00, 'battle\\\\btgun60.eff')
    LoadEffect(0x01, 'map\\\\mp019_00.eff')
    LoadEffect(0x02, 'Scraft\\\\sc008_04.eff')
    LoadEffect(0x03, 'battle\\\\btbomb00.eff')
    LoadEffect(0x04, 'Scraft\\\\sc003_12.eff')
    OP_C8(0x0200, 0x0046, 'C_PLAC19._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    CreateThread(0x0008, 0x03, 0x00, 0x0005)
    Sleep(2000)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2440340956V……好象来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2440340957V榴弹炮，准备射击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlayEffect(0x02, 0x00, 0x00FF, -26480, 1250, 30810, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x01, 0x00FF, -33230, 1250, 28840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0x02, 0x00FF, -21710, 1250, 23210, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Fade(500)
    OP_6D(-25880, 0, -49340, 0)
    OP_67(0, 4130, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(146000, 0)
    OP_6E(290, 0)
    SetChrChipByIndex(0x0018, 24)
    SetChrChipByIndex(0x0019, 24)
    SetChrChipByIndex(0x001A, 24)
    SetChrChipByIndex(0x001B, 24)
    SetChrChipByIndex(0x001C, 24)
    SetChrChipByIndex(0x001D, 24)

    @scena.Lambda('lambda_0FED')
    def lambda_0FED():
        OP_6D(-26900, 0, -47350, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0FED)

    @scena.Lambda('lambda_1005')
    def lambda_1005():
        OP_67(0, 5390, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1005)

    @scena.Lambda('lambda_101D')
    def lambda_101D():
        OP_6B(3280, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_101D)

    @scena.Lambda('lambda_102D')
    def lambda_102D():
        OP_6C(123000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_102D)

    @scena.Lambda('lambda_103D')
    def lambda_103D():
        OP_6E(340, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_103D)

    @scena.Lambda('lambda_104D')
    def lambda_104D():
        OP_90(0x00FE, 1000, 0, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_104D)

    @scena.Lambda('lambda_1068')
    def lambda_1068():
        OP_90(0x00FE, 1000, 0, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1068)

    @scena.Lambda('lambda_1083')
    def lambda_1083():
        OP_90(0x00FE, 1000, 0, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1083)

    @scena.Lambda('lambda_109E')
    def lambda_109E():
        OP_90(0x00FE, 1000, 0, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_109E)

    @scena.Lambda('lambda_10B9')
    def lambda_10B9():
        OP_90(0x00FE, 1000, 0, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_10B9)

    @scena.Lambda('lambda_10D4')
    def lambda_10D4():
        OP_90(0x00FE, 1000, 0, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_10D4)

    Sleep(4000)

    Fade(500)
    OP_6D(-27360, 10, 29020, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(322000, 0)
    OP_6E(345, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2440340958V#3S射击！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x000C)
    Sleep(100)

    CreateThread(0x0101, 0x02, 0x00, 0x000D)
    Sleep(100)

    CreateThread(0x0101, 0x03, 0x00, 0x000E)
    Sleep(3000)

    CreateThread(0x0102, 0x01, 0x00, 0x000F)
    Fade(500)
    OP_6D(-25630, 0, -32509, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(156000, 0)
    OP_6E(329, 0)
    SetChrPos(0x001E, -25500, 0, -26000, 0)
    SetChrPos(0x001F, -29500, 0, -26000, 0)
    SetChrPos(0x0020, -22000, 0, -31000, 0)
    SetChrPos(0x0021, -34000, 0, -31000, 0)
    SetChrPos(0x0022, -20000, 0, -37000, 0)
    SetChrPos(0x0023, -36000, 0, -37000, 0)
    SetChrPos(0x0018, -29080, 0, -36000, 0)
    SetChrPos(0x0019, -25780, 0, -37590, 0)
    SetChrPos(0x001A, -27930, 0, -41140, 0)
    SetChrPos(0x001B, -24760, 0, -42840, 0)
    SetChrPos(0x001C, -27700, 0, -45820, 0)
    SetChrPos(0x001D, -24460, 0, -47690, 0)
    CreateThread(0x0018, 0x01, 0x00, 0x0006)
    CreateThread(0x0019, 0x01, 0x00, 0x0007)
    CreateThread(0x001A, 0x01, 0x00, 0x0008)
    CreateThread(0x001B, 0x01, 0x00, 0x0009)
    CreateThread(0x001C, 0x01, 0x00, 0x000A)
    CreateThread(0x001D, 0x01, 0x00, 0x000B)

    @scena.Lambda('lambda_12C6')
    def lambda_12C6():
        OP_6D(-25630, 0, -32509, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_12C6)

    @scena.Lambda('lambda_12DE')
    def lambda_12DE():
        OP_67(0, 4600, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12DE)

    @scena.Lambda('lambda_12F6')
    def lambda_12F6():
        OP_6B(4000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12F6)

    @scena.Lambda('lambda_1306')
    def lambda_1306():
        OP_6C(168000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1306)

    @scena.Lambda('lambda_1316')
    def lambda_1316():
        OP_6E(347, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1316)

    Sleep(9000)

    Fade(500)
    OP_6D(-27360, 10, 29020, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(322000, 0)
    OP_6E(345, 0)
    OP_0D()
    OP_A2(0x0000)

    ChrTalk(
        0x0008,
        (
            '#2440340959V停止射击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 21)
    OP_0D()
    Sleep(300)

    SetChrSubChip(0x0008, 1)
    Sleep(200)

    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2440340960V全体突入！\n',
            '一只也不能让它们接近城市！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('士兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2440340961V#5S是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    CreateThread(0x0009, 0x01, 0x00, 0x0010)
    Sleep(10)

    CreateThread(0x000C, 0x01, 0x00, 0x0011)
    Sleep(10)

    CreateThread(0x000F, 0x01, 0x00, 0x0012)
    Sleep(10)

    CreateThread(0x0012, 0x01, 0x00, 0x0013)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, 0x0010)
    Sleep(10)

    CreateThread(0x000D, 0x01, 0x00, 0x0011)
    Sleep(10)

    CreateThread(0x0010, 0x01, 0x00, 0x0012)
    Sleep(10)

    CreateThread(0x0013, 0x01, 0x00, 0x0013)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, 0x0010)
    Sleep(10)

    CreateThread(0x000E, 0x01, 0x00, 0x0011)
    Sleep(10)

    CreateThread(0x0011, 0x01, 0x00, 0x0012)
    Sleep(10)

    CreateThread(0x0014, 0x01, 0x00, 0x0013)
    Sleep(1000)

    OP_A2(0x0002)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    SetMapFlags(0x02000000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T3120._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x14E8
@scena.Code('func_05_14E8')
def func_05_14E8():
    Sleep(150)

    OP_22(0x013A, 0x00, 0x1E)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x23)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x28)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x2D)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x32)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x37)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x3C)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x41)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x46)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x4B)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    def _loc_15A1(): pass

    label('loc_15A1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_15C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_15B4',
    )

    Jump('loc_15C9')

    def _loc_15B4(): pass

    label('loc_15B4')

    OP_22(0x013A, 0x00, 0x50)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    Jump('loc_15A1')

    def _loc_15C9(): pass

    label('loc_15C9')

    OP_22(0x013A, 0x00, 0x46)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x3C)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x32)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x28)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x1E)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    OP_22(0x013A, 0x00, 0x14)
    Sleep(200)

    OP_23(0x013A)
    Sleep(180)

    Return()

# id: 0x0006 offset: 0x1636
@scena.Code('func_06_1636')
def func_06_1636():
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 1500, 0, 7500, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 3000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 4000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 15000, 2000, 0x00)

    Return()

# id: 0x0007 offset: 0x1758
@scena.Code('func_07_1758')
def func_07_1758():
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 1500, 0, 6000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 4000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 500, 0, 3000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 0, 0, 15000, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0x187A
@scena.Code('func_08_187A')
def func_08_187A():
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 500, 0, 7000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 3000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 4000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 500, 0, 15000, 2000, 0x00)

    Return()

# id: 0x0009 offset: 0x199C
@scena.Code('func_09_199C')
def func_09_199C():
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 500, 0, 5000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -1000, 0, 3000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 500, 0, 4000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 0, 0, 15000, 2000, 0x00)

    Return()

# id: 0x000A offset: 0x1ABE
@scena.Code('func_0A_1ABE')
def func_0A_1ABE():
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 0, 0, 6000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -1000, 0, 2000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 500, 0, 3000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 15000, 2000, 0x00)

    Return()

# id: 0x000B offset: 0x1BE0
@scena.Code('func_0B_1BE0')
def func_0B_1BE0():
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 0, 0, 5000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 0, 200, 200, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -1000, 0, 3000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, -500, 0, 2000, 2000, 0x00)
    PlayEffect(0x03, 0xFF, 0x00FE, 100, 400, 0, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x00FE, 25)
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 24)
    OP_90(0x00FE, 0, 0, 15000, 2000, 0x00)

    Return()

# id: 0x000C offset: 0x1D02
@scena.Code('func_0C_1D02')
def func_0C_1D02():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D81',
    )

    PlayEffect(0x00, 0xFF, 0x00FF, -26480, 1250, 30810, 180, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x04, 0xFF, 0x00FF, -26480, 1000, 30810, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    Jump('func_0C_1D02')

    def _loc_1D81(): pass

    label('loc_1D81')

    Return()

# id: 0x000D offset: 0x1D82
@scena.Code('func_0D_1D82')
def func_0D_1D82():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E01',
    )

    PlayEffect(0x00, 0xFF, 0x00FF, -33230, 1250, 28840, 180, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x04, 0xFF, 0x00FF, -33230, 1000, 28840, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(700)

    Jump('func_0D_1D82')

    def _loc_1E01(): pass

    label('loc_1E01')

    Return()

# id: 0x000E offset: 0x1E02
@scena.Code('func_0E_1E02')
def func_0E_1E02():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E81',
    )

    PlayEffect(0x00, 0xFF, 0x00FF, -21710, 1250, 23210, 180, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x04, 0xFF, 0x00FF, -21710, 1000, 23210, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(900)

    Jump('func_0E_1E02')

    def _loc_1E81(): pass

    label('loc_1E81')

    Return()

# id: 0x000F offset: 0x1E82
@scena.Code('func_0F_1E82')
def func_0F_1E82():
    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001C, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001F, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001E, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0019, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0018, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001F, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -26480, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001D, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0019, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001E, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001F, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0022, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001B, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, -33230, 16000, -14800, 0, 0, 0, 1000, 1000, 1000, 0x001E, 0, 0, 0, 0)

    Return()

# id: 0x0010 offset: 0x2A46
@scena.Code('func_10_2A46')
def func_10_2A46():
    SetChrChipByIndex(0x00FE, 23)
    OP_8E(0x00FE, -25720, 0, 25760, 6000, 0x00)
    OP_90(0x00FE, 0, 0, -30000, 6000, 0x00)

    Return()

# id: 0x0011 offset: 0x2A74
@scena.Code('func_11_2A74')
def func_11_2A74():
    SetChrChipByIndex(0x00FE, 23)
    OP_8E(0x00FE, -27310, 10, 25660, 6000, 0x00)
    OP_90(0x00FE, 0, 0, -30000, 6000, 0x00)

    Return()

# id: 0x0012 offset: 0x2AA2
@scena.Code('func_12_2AA2')
def func_12_2AA2():
    SetChrChipByIndex(0x00FE, 23)
    OP_8E(0x00FE, -24020, -20, 28830, 6000, 0x00)
    OP_90(0x00FE, 0, 0, -30000, 6000, 0x00)

    Return()

# id: 0x0013 offset: 0x2AD0
@scena.Code('func_13_2AD0')
def func_13_2AD0():
    SetChrChipByIndex(0x00FE, 23)
    OP_8E(0x00FE, -29350, -50, 19330, 6000, 0x00)
    OP_90(0x00FE, 0, 0, -30000, 6000, 0x00)

    Return()

# id: 0x0014 offset: 0x2AFE
@scena.Code('func_14_2AFE')
def func_14_2AFE():
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

# id: 0x0015 offset: 0x2B75
@scena.Code('func_15_2B75')
def func_15_2B75():
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

# id: 0x0016 offset: 0x2BC4
@scena.Code('func_16_2BC4')
def func_16_2BC4():
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
