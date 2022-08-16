import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4100.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP'),
        ('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP'),
        ('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP'),
        ('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
    ]

# id: 0x10001 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奥利维尔',
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
            name                = '玲',
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾南',
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
            name                = '亡命守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亡命守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亡命装甲兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '嘉瑟',
            x                   = -5720,
            z                   = 0,
            y                   = -36280,
            direction           = 281,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '诺娜',
            x                   = 5550,
            z                   = 0,
            y                   = -54380,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '蒂库',
            x                   = -840,
            z                   = 0,
            y                   = -50090,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '拉尔斯',
            x                   = 710,
            z                   = 0,
            y                   = -50090,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '托伊',
            x                   = -90,
            z                   = 0,
            y                   = -51500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '伯登',
            x                   = 5760,
            z                   = 0,
            y                   = -46060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '拉塔娜',
            x                   = -2070,
            z                   = 0,
            y                   = -5120,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '托朗老人',
            x                   = 3520,
            z                   = 0,
            y                   = 10640,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 4760,
            z                   = 0,
            y                   = -39600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -4540,
            z                   = 0,
            y                   = -29870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '塔巴莎',
            x                   = -9390,
            z                   = 250,
            y                   = -6510,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '萨米',
            x                   = 8060,
            z                   = 250,
            y                   = 5500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '吉恩',
            x                   = 8060,
            z                   = 250,
            y                   = 4120,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '迪克斯',
            x                   = 5990,
            z                   = 0,
            y                   = -7440,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = 10,
            z                   = 250,
            y                   = 36990,
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
            name                = '庭园大道方向',
            x                   = -50,
            z                   = 0,
            y                   = -90220,
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
            name                = '王都格兰赛尔·东街区',
            x                   = 54990,
            z                   = 0,
            y                   = -1130,
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
            name                = '王都格兰赛尔·西街区',
            x                   = -44420,
            z                   = 0,
            y                   = -19990,
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

# id: 0x10002 offset: 0x6FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -430,
            z           = 0,
            y           = -39050,
            word_0C     = 0x00B4,
            word_0E     = 0x0012,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0549,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -17930,
            z           = 0,
            y           = -20130,
            word_0C     = 0x00B4,
            word_0E     = 0x0014,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x054A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -5660,
            z           = 0,
            y           = -1440,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0547,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 21340,
            z           = 0,
            y           = -230,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0546,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -13570,
            z           = 250,
            y           = -51100,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0548,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x786
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -5000,
            y           = -2000,
            z           = -65600,
            range       = 5000,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF0344,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000035,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -25000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003D,
        ),
        ScenaEventData(
            x           = -10280,
            y           = 0,
            z           = -11040,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003E,
        ),
        ScenaEventData(
            x           = -14940,
            y           = 0,
            z           = -15750,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003E,
        ),
        ScenaEventData(
            x           = -10290,
            y           = 0,
            z           = -30020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003F,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -13010,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000040,
        ),
        ScenaEventData(
            x           = 15900,
            y           = 0,
            z           = 6330,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000041,
        ),
    )

# id: 0x10004 offset: 0x866
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9620,
            triggerZ            = 500,
            triggerY            = -25020,
            triggerRange        = 800,
            actorX              = 9620,
            actorZ              = 1500,
            actorY              = -25020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23690,
            triggerZ            = 500,
            triggerY            = -7620,
            triggerRange        = 800,
            actorX              = 23690,
            actorZ              = 1500,
            actorY              = -7620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16040,
            triggerZ            = 500,
            triggerY            = 6640,
            triggerRange        = 800,
            actorX              = 16040,
            actorZ              = 1500,
            actorY              = 6640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12480,
            triggerZ            = 500,
            triggerY            = -2460,
            triggerRange        = 800,
            actorX              = -12480,
            actorZ              = 1500,
            actorY              = -2460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10640,
            triggerZ            = 500,
            triggerY            = -11060,
            triggerRange        = 800,
            actorX              = -10640,
            actorZ              = 1500,
            actorY              = -11060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14870,
            triggerZ            = 500,
            triggerY            = -15350,
            triggerRange        = 800,
            actorX              = -14870,
            actorZ              = 1500,
            actorY              = -15350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -10680,
            triggerZ            = 500,
            triggerY            = -29970,
            triggerRange        = 800,
            actorX              = -10680,
            actorZ              = 1500,
            actorY              = -29970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30,
            triggerZ            = 300,
            triggerY            = -43060,
            triggerRange        = 800,
            actorX              = -30,
            actorZ              = 4300,
            actorY              = -46060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x986
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_9D0',
    )

    Call(0, 0x0028)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x002E, 0x0080)
    ChrSetFlags(0x002F, 0x0080)

    Jump('loc_A5A')

    def _loc_9D0(): pass

    label('loc_9D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_9E4',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)

    Jump('loc_A5A')

    def _loc_9E4(): pass

    label('loc_9E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_9F8',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)

    Jump('loc_A5A')

    def _loc_9F8(): pass

    label('loc_9F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_A0C',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)

    Jump('loc_A5A')

    def _loc_A0C(): pass

    label('loc_A0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_A20',
    )

    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)

    Jump('loc_A5A')

    def _loc_A20(): pass

    label('loc_A20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A2E',
    )

    Jump('loc_A5A')

    def _loc_A2E(): pass

    label('loc_A2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_A38',
    )

    Jump('loc_A5A')

    def _loc_A38(): pass

    label('loc_A38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_A42',
    )

    Jump('loc_A5A')

    def _loc_A42(): pass

    label('loc_A42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_A5A',
    )

    ChrSetPos(0x0026, 16000, 250, 4030, 0)

    def _loc_A5A(): pass

    label('loc_A5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A81',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_1E_4BB3)

    def _loc_A81(): pass

    label('loc_A81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_A9A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x02C3, 2, 0x161A))
    Event(0, func_18_4368)

    Jump('loc_B2D')

    def _loc_A9A(): pass

    label('loc_A9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_AB3',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x02C5, 5, 0x162D))
    Event(0, func_19_46AC)

    Jump('loc_B2D')

    def _loc_AB3(): pass

    label('loc_AB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_AC9',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_1F_4BBF)

    Jump('loc_B2D')

    def _loc_AC9(): pass

    label('loc_AC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_AE8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(0, func_27_5FED)

    Jump('loc_B2D')

    def _loc_AE8(): pass

    label('loc_AE8')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_AF4'),
        (-1, 'loc_B2D'),
    )

    def _loc_AF4(): pass

    label('loc_AF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B15',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_2A_6B34)

    Jump('loc_B2A')

    def _loc_B15(): pass

    label('loc_B15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 0, 0x1618)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 1, 0x1619)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B2A',
    )

    MapSetFlags(0x10000000)
    Event(0, func_17_3EC1)

    def _loc_B2A(): pass

    label('loc_B2A')

    Jump('loc_B2D')

    def _loc_B2D(): pass

    label('loc_B2D')

    Return()

# id: 0x0001 offset: 0xB2E
@scena.Code('func_01_B2E')
def func_01_B2E():
    OP_16(0x02, 4000, -128000, -148000, 2293851)

    ExecExpressionWithValue(
        0x0035,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        'loc_B6B',
    )

    OP_B1('t4100_y')

    Jump('loc_B74')

    def _loc_B6B(): pass

    label('loc_B6B')

    OP_B1('t4100_n')

    def _loc_B74(): pass

    label('loc_B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_BC6',
    )

    OP_72(0x0000, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x0004, 0x0010)
    OP_72(0x0005, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0010, 0x0010)
    OP_1B(0x09, 0x00, 0x0030)
    OP_1B(0x0A, 0x00, 0x002F)
    OP_77(0xFF, 0xBD, 0xA7, 0x00, 0x00000000)
    Call(0, 0x0029)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    Jump('loc_BE4')

    def _loc_BC6(): pass

    label('loc_BC6')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_B5(0x00)

    def _loc_BE4(): pass

    label('loc_BE4')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x54F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BF9(): pass

    label('loc_BF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C26',
    )

    OP_1B(0x09, 0x00, 0x003B)
    OP_1B(0x0A, 0x00, 0x003A)
    OP_1B(0x0B, 0x00, 0x0037)
    OP_1B(0x0C, 0x00, 0x0038)
    OP_1B(0x0D, 0x00, 0x0037)
    OP_1B(0x0E, 0x00, 0x0039)

    Jump('loc_C53')

    def _loc_C26(): pass

    label('loc_C26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C53',
    )

    OP_1B(0x09, 0x00, 0x003B)
    OP_1B(0x0A, 0x00, 0x003A)
    OP_1B(0x0B, 0x00, 0x0037)
    OP_1B(0x0C, 0x00, 0x0038)
    OP_1B(0x0D, 0x00, 0x0037)
    OP_1B(0x0E, 0x00, 0x0039)

    Jump('loc_C53')

    def _loc_C53(): pass

    label('loc_C53')

    OP_64(0x07, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C77',
    )

    OP_65(0x07, 0x0001)

    def _loc_C77(): pass

    label('loc_C77')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C92',
    )

    StopEffect(0x84, 0x00)
    StopEffect(0x88, 0x00)
    StopEffect(0x89, 0x00)
    StopEffect(0x8A, 0x00)

    Jump('loc_CAE')

    def _loc_C92(): pass

    label('loc_C92')

    OP_25(0x01CB, 50, 0, -46480, 2000, 15000, 0x64, 0x00000000)

    def _loc_CAE(): pass

    label('loc_CAE')

    Return()

# id: 0x0002 offset: 0xCAF
@scena.Code('func_02_CAF')
def func_02_CAF():
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
        'loc_CD4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_E16')

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CED',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_E16')

    def _loc_CED(): pass

    label('loc_CED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D06',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_E16')

    def _loc_D06(): pass

    label('loc_D06')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_E16')

    def _loc_D1F(): pass

    label('loc_D1F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D38',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_E16')

    def _loc_D38(): pass

    label('loc_D38')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D51',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_E16')

    def _loc_D51(): pass

    label('loc_D51')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D6A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_E16')

    def _loc_D6A(): pass

    label('loc_D6A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D83',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_E16')

    def _loc_D83(): pass

    label('loc_D83')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D9C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_E16')

    def _loc_D9C(): pass

    label('loc_D9C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DB5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_E16')

    def _loc_DB5(): pass

    label('loc_DB5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DCE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_E16')

    def _loc_DCE(): pass

    label('loc_DCE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DE7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_E16')

    def _loc_DE7(): pass

    label('loc_DE7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E00',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_E16')

    def _loc_E00(): pass

    label('loc_E00')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E16',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_E16(): pass

    label('loc_E16')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E2B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_E16')

    def _loc_E2B(): pass

    label('loc_E2B')

    Return()

# id: 0x0003 offset: 0xE2C
@scena.Code('func_03_E2C')
def func_03_E2C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E4F',
    )

    OP_8D(0x00FE, 3700, -42040, 10110, -50100, 2000)

    Jump('func_03_E2C')

    def _loc_E4F(): pass

    label('loc_E4F')

    Return()

# id: 0x0004 offset: 0xE50
@scena.Code('func_04_E50')
def func_04_E50():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EAC',
    )

    ChrWalkTo(0x00FE, -2070, 0, -37340, 2300, 0x00)
    ChrWalkTo(0x00FE, 2510, 0, -37340, 2300, 0x00)
    ChrWalkTo(0x00FE, 2510, 0, 8550, 2300, 0x00)
    ChrWalkTo(0x00FE, -2070, 0, 8550, 2300, 0x00)

    Jump('func_04_E50')

    def _loc_EAC(): pass

    label('loc_EAC')

    Return()

# id: 0x0005 offset: 0xEAD
@scena.Code('func_05_EAD')
def func_05_EAD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F39',
    )

    ChrWalkTo(0x00FE, 3520, 0, -39630, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -3430, 0, -39630, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -3430, 0, 10640, 2000, 0x00)
    ChrWalkTo(0x00FE, 3520, 0, 10640, 2000, 0x00)

    Jump('func_05_EAD')

    def _loc_F39(): pass

    label('loc_F39')

    Return()

# id: 0x0006 offset: 0xF3A
@scena.Code('func_06_F3A')
def func_06_F3A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FA8',
    )

    ChrWalkTo(0x00FE, 4760, 0, -39600, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 4760, 0, -1190, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    Jump('func_06_F3A')

    def _loc_FA8(): pass

    label('loc_FA8')

    Return()

# id: 0x0007 offset: 0xFA9
@scena.Code('func_07_FA9')
def func_07_FA9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1017',
    )

    ChrWalkTo(0x00FE, -4540, 0, -20540, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -4430, 0, -39600, 2500, 0x00)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    Jump('func_07_FA9')

    def _loc_1017(): pass

    label('loc_1017')

    Return()

# id: 0x0008 offset: 0x1018
@scena.Code('func_08_1018')
def func_08_1018():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_103B',
    )

    OP_8D(0x00FE, -9540, -8220, -7490, -4270, 2000)

    Jump('func_08_1018')

    def _loc_103B(): pass

    label('loc_103B')

    Return()

# id: 0x0009 offset: 0x103C
@scena.Code('func_09_103C')
def func_09_103C():
    TalkBegin(0x00FE)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1056',
    )

    OP_A9(0xD6)
    TalkEnd(0x00FE)

    Return()

    def _loc_1056(): pass

    label('loc_1056')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1067',
    )

    TalkEnd(0x00FE)

    Return()

    def _loc_1067(): pass

    label('loc_1067')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1071',
    )

    Jump('loc_14E9')

    def _loc_1071(): pass

    label('loc_1071')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1110',
    )

    ChrTalk(
        0x00FE,
        (
            '我刚在试验像以前一样\n',
            '用火力来做爆米花，失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，我这个人一直不走运，\n',
            '对麻烦已经习以为常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不久就会恢复了，\n',
            '现在就努力克服吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_1110(): pass

    label('loc_1110')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_11A6',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天我去进货，\n',
            '以令人惊讶的价格\n',
            '买到了爆米花的原料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '机器虽然坏了，\n',
            '不过说不定也是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像牧师大人说的那样，\n',
            '应该向前看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_11A6(): pass

    label('loc_11A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1250',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_121C',
    )

    ChrTalk(
        0x00FE,
        (
            '制作爆米花的\n',
            '机器坏了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是神说你今天\n',
            '别卖东西了，\n',
            '去进货吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_124D')

    def _loc_121C(): pass

    label('loc_121C')

    ChrTalk(
        0x00FE,
        (
            '一定要向前看，\n',
            '向前看向前看……重复重复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_124D(): pass

    label('loc_124D')

    Jump('loc_14E9')

    def _loc_1250(): pass

    label('loc_1250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1283',
    )

    ChrTalk(
        0x00FE,
        (
            '咦？　奇怪……\n',
            '机器好像有问题了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_1283(): pass

    label('loc_1283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1343',
    )

    ChrTalk(
        0x00FE,
        (
            '我在教会倾诉了\n',
            '自己遭遇的不幸是如何的多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利瓦尔牧师非常\n',
            '亲切的听了我说的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说就算遭遇挫折，\n',
            '还是要尽可能地\n',
            '向前看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，赶快从明天\n',
            '开始实践～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_13A6')

    def _loc_1343(): pass

    label('loc_1343')

    ChrTalk(
        0x00FE,
        (
            '我在七耀教会倾诉了\n',
            '自己遭遇的不幸是如何的多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说就算遭遇挫折，\n',
            '还是要尽可能地\n',
            '向前看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13A6(): pass

    label('loc_13A6')

    Jump('loc_14E9')

    def _loc_13A9(): pass

    label('loc_13A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_141A',
    )

    ChrTalk(
        0x00FE,
        (
            '咳，今天把钓鱼用的钱\n',
            '忘在家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给客人们\n',
            '添麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的人生果然\n',
            '是要持续遇到麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_141A(): pass

    label('loc_141A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_149F',
    )

    ChrTalk(
        0x00FE,
        (
            '……我的人生从来就是\n',
            '麻烦不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典时也因为摊子坏了，\n',
            '没法提高销售额。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是要在七耀教会\n',
            '除一下魔呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_149F(): pass

    label('loc_149F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_14E9',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，欢迎来到王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁着休息，要不要\n',
            '吃点爆米花？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14E9(): pass

    label('loc_14E9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x14ED
@scena.Code('func_0A_14ED')
def func_0A_14ED():
    TalkBegin(0x00FE)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1507',
    )

    OP_A9(0xD5)
    TalkEnd(0x00FE)

    Return()

    def _loc_1507(): pass

    label('loc_1507')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1518',
    )

    TalkEnd(0x00FE)

    Return()

    def _loc_1518(): pass

    label('loc_1518')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1522',
    )

    Jump('loc_1840')

    def _loc_1522(): pass

    label('loc_1522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_158D',
    )

    ChrTalk(
        0x00FE,
        (
            '我打算租的\n',
            '西街区的空房\n',
            '似乎有人住进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像要开店的样子，\n',
            '不过是个挺可疑的大叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_158D(): pass

    label('loc_158D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_164E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_161C',
    )

    ChrTalk(
        0x00FE,
        (
            '西街区的空房似乎\n',
            '有人先签了合同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点不甘心，不过那边\n',
            '昨天好象还发生了案件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来和我无缘，算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_164B')

    def _loc_161C(): pass

    label('loc_161C')

    ChrTalk(
        0x00FE,
        (
            '不过，那处空房……\n',
            '到底是什么人租下了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_164B(): pass

    label('loc_164B')

    Jump('loc_1840')

    def _loc_164E(): pass

    label('loc_164E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1686',
    )

    ChrTalk(
        0x00FE,
        (
            '你们怎么东张西望的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是在找人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_1686(): pass

    label('loc_1686')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_16D4',
    )

    ChrTalk(
        0x00FE,
        (
            '以前西街区就有\n',
            '一处空房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我存的钱可能\n',
            '够把那里租下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_16D4(): pass

    label('loc_16D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1730',
    )

    ChrTalk(
        0x00FE,
        (
            '我从诞辰庆典前就\n',
            '开始存钱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是不是该认真\n',
            '考虑一下过单身生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_1730(): pass

    label('loc_1730')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1763',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '要不要来份美味的薄煎饼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_1763(): pass

    label('loc_1763')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_17E1',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才王国军的大人物\n',
            '从这儿过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然穿着军服，\n',
            '不过看起来是个很随和的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给人一种温柔老爸的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_17E1(): pass

    label('loc_17E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1840',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是利贝尔的中枢，\n',
            '王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然发生过政变，\n',
            '不过现在已经完全复原了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1840(): pass

    label('loc_1840')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1844
@scena.Code('func_0B_1844')
def func_0B_1844():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1851',
    )

    Jump('loc_1EBA')

    def _loc_1851(): pass

    label('loc_1851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_189E',
    )

    ChrTalk(
        0x00FE,
        (
            '……真是的，太不方便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚上漆黑一片的，\n',
            '厕所也不能上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBA')

    def _loc_189E(): pass

    label('loc_189E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_18ED',
    )

    ChrTalk(
        0x00FE,
        (
            '好像昨天亲卫队在港口\n',
            '和巨大的坦克发生了战斗哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真了不得！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBA')

    def _loc_18ED(): pass

    label('loc_18ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1976',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 7, 0x164F)),
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 0, 0x1650)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1939',
    )

    ChrTalk(
        0x00FE,
        (
            '那、那个……今天穿白衣服的\n',
            '趾高气扬的女人不在吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1973')

    def _loc_1939(): pass

    label('loc_1939')

    ChrTalk(
        0x00FE,
        (
            '唉，就没什么有意思的事吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天实在是太无聊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1973(): pass

    label('loc_1973')

    Jump('loc_1EBA')

    def _loc_1976(): pass

    label('loc_1976')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1BD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 7, 0x164F)),
            Expr.Return,
        ),
        'loc_19D5',
    )

    ChrTurnDirection(0x0024, 0x012F, 400)

    ChrTalk(
        0x00FE,
        (
            '你、你好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#260F你是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我们上次不是说过话啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BCE')

    def _loc_19D5(): pass

    label('loc_19D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 0, 0x1650)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B71',
    )

    ChrTurnDirection(0x0024, 0x012F, 0)

    ChrTalk(
        0x00FE,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂、喂，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说穿白衣服的那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#264F……你莫非是在说玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对、对，你，\n',
            '还没过来跟我打招呼吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#264F咦，玲为什么非要\n',
            '跟你打招呼呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来、来到这个城市的人\n',
            '都得跟我打招呼，\n',
            '这是规矩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#267F是嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#263F不过我不愿意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你、你说什么～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#263F因为爸爸说过绅士\n',
            '是会先主动\n',
            '上前打招呼的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#260F玲不想和不懂礼貌的\n',
            '人交朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CA, 0, 0x1650))

    Jump('loc_1BCE')

    def _loc_1B71(): pass

    label('loc_1B71')

    ChrTurnDirection(0x012F, 0x00FE, 0)

    ChrTalk(
        0x012F,
        (
            '#260F (盯)……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0024, 0x012F, 400)

    ChrTalk(
        0x00FE,
        (
            '什、什么嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天就放过你吧。\n',
            '你、你可以走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BCE(): pass

    label('loc_1BCE')

    Jump('loc_1EBA')

    def _loc_1BD1(): pass

    label('loc_1BD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C16',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～我肚子饿了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再不回去的话\n',
            '会被老妈揍的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBA')

    def _loc_1C16(): pass

    label('loc_1C16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1C6B',
    )

    ChrTalk(
        0x00FE,
        (
            '名为互不侵犯条约的良药吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，\n',
            '都不像是会顺利进行的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBA')

    def _loc_1C6B(): pass

    label('loc_1C6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1E72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 7, 0x164F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E15',
    )

    ChrTurnDirection(0x0024, 0x012F, 0)

    ChrTalk(
        0x00FE,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂、喂，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说穿白衣服的那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0024, 400)

    ChrTalk(
        0x012F,
        (
            '#264F……你莫非是在说玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对、对，你，\n',
            '还没过来跟我打招呼吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#264F咦，玲为什么非要\n',
            '跟你打招呼呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来、来到这个城市的人\n',
            '都得跟我打招呼，\n',
            '这是规矩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#267F是嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#263F不过我不愿意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你、你说什么～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#263F因为爸爸说过绅士\n',
            '是会先主动\n',
            '上前打招呼的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#260F玲不想和不懂礼貌的\n',
            '人交朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C9, 7, 0x164F))

    Jump('loc_1E6F')

    def _loc_1E15(): pass

    label('loc_1E15')

    ChrTurnDirection(0x012F, 0x0024, 400)

    ChrTalk(
        0x012F,
        (
            '#260F切……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0024, 0x012F, 400)

    ChrTalk(
        0x00FE,
        (
            '什、什么嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天就放过你吧。\n',
            '你、你可以走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E6F(): pass

    label('loc_1E6F')

    Jump('loc_1EBA')

    def _loc_1E72(): pass

    label('loc_1E72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1EBA',
    )

    ChrTalk(
        0x00FE,
        (
            '……真是的。\n',
            '托伊那家伙又迟到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想早点去港口玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EBA(): pass

    label('loc_1EBA')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1EBE
@scena.Code('func_0C_1EBE')
def func_0C_1EBE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1ECB',
    )

    Jump('loc_2129')

    def _loc_1ECB(): pass

    label('loc_1ECB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F26',
    )

    ChrTalk(
        0x00FE,
        (
            '蒂库胆子小，平时应该是\n',
            '不敢一个人上厕所的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是在问有没有什么改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2129')

    def _loc_1F26(): pass

    label('loc_1F26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1F6B',
    )

    ChrTalk(
        0x00FE,
        (
            '听说有几个情报部的人\n',
            '被抓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是一件大事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2129')

    def _loc_1F6B(): pass

    label('loc_1F6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1FB3',
    )

    ChrTalk(
        0x00FE,
        (
            '我也喜欢这种\n',
            '悠闲的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忧虑太多的话\n',
            '人会变老的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2129')

    def _loc_1FB3(): pass

    label('loc_1FB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1FEA',
    )

    ChrTalk(
        0x00FE,
        (
            '蒂库心跳加快的\n',
            '可能性是……９６·７％。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2129')

    def _loc_1FEA(): pass

    label('loc_1FEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2010',
    )

    ChrTalk(
        0x00FE,
        (
            '今天该要结束了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2129')

    def _loc_2010(): pass

    label('loc_2010')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2039',
    )

    ChrTalk(
        0x00FE,
        (
            '你们两个……\n',
            '我有点害羞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2129')

    def _loc_2039(): pass

    label('loc_2039')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_20D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 7, 0x164F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2078',
    )

    ChrTalk(
        0x00FE,
        (
            '不出我的意料，托伊\n',
            '果然是在途中耽搁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D3')

    def _loc_2078(): pass

    label('loc_2078')

    ChrTalk(
        0x00FE,
        (
            '呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蒂库一见钟情后\n',
            '以失恋告终的概率……９９．７％。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是笨拙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20D3(): pass

    label('loc_20D3')

    Jump('loc_2129')

    def _loc_20D6(): pass

    label('loc_20D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2129',
    )

    ChrTalk(
        0x00FE,
        (
            '托伊比预计时间\n',
            '迟到的概率……８３％。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '途中耽搁的习惯\n',
            '还是照旧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2129(): pass

    label('loc_2129')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x212D
@scena.Code('func_0D_212D')
def func_0D_212D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_213A',
    )

    Jump('loc_234B')

    def _loc_213A(): pass

    label('loc_213A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2181',
    )

    ChrTalk(
        0x00FE,
        (
            '夜晚漆黑一片的，\n',
            '可以看见很多星星。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是很漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_2181(): pass

    label('loc_2181')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_21D6',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天港口那边传来了很响的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '灯也突然暗了，\n',
            '到底发生了什么呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_21D6(): pass

    label('loc_21D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2225',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～好想吃冰淇淋啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们知道吗，\n',
            '东街区的冰淇淋很好吃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_2225(): pass

    label('loc_2225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_226B',
    )

    ChrTalk(
        0x00FE,
        (
            '蒂库虽然平时\n',
            '趾高气扬的，不过跟女孩子\n',
            '说话时就会紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_226B(): pass

    label('loc_226B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2298',
    )

    ChrTalk(
        0x00FE,
        (
            '肚子饿了啊～\n',
            '我得回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_2298(): pass

    label('loc_2298')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_22C7',
    )

    ChrTalk(
        0x00FE,
        (
            '我可不想吃药，\n',
            '想吃好吃的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_22C7(): pass

    label('loc_22C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_22F6',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿……\n',
            '又比约定的时间晚点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234B')

    def _loc_22F6(): pass

    label('loc_22F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_234B',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～\n',
            '好香啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……咦？\n',
            '我有没有跟什么人有约？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～让我想想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_234B(): pass

    label('loc_234B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x234F
@scena.Code('func_0E_234F')
def func_0E_234F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_235C',
    )

    Jump('loc_2B27')

    def _loc_235C(): pass

    label('loc_235C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_23FC',
    )

    ChrTalk(
        0x00FE,
        (
            '在工房当修理师的\n',
            '多姆确实是个可信赖的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果他说这不是故障，\n',
            '那应该是没问题的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是塞森说的，\n',
            '我倒是会怀疑他\n',
            '是不是想买新的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B27')

    def _loc_23FC(): pass

    label('loc_23FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2494',
    )

    ChrTalk(
        0x00FE,
        (
            '原情报部的凯诺娜上尉\n',
            '是不是真的举兵谋反了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '港湾设施好像被导力坦克\n',
            '破坏得一塌糊涂了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望没有对互不侵犯条约产生太大的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B27')

    def _loc_2494(): pass

    label('loc_2494')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_25B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_256B',
    )

    ChrTalk(
        0x00FE,
        (
            '杜南公爵和科洛蒂娅公主……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王准备\n',
            '传位给哪一个呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我个人觉得科洛蒂娅\n',
            '公主比较好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我不太了解\n',
            '科洛蒂娅公主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2565',
    )

    ChrTalk(
        0x0105,
        (
            '#042F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2565(): pass

    label('loc_2565')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_25AD')

    def _loc_256B(): pass

    label('loc_256B')

    ChrTalk(
        0x00FE,
        (
            '其实我不太了解\n',
            '科洛蒂娅公主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多只知道\n',
            '她是个美人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_25AD(): pass

    label('loc_25AD')

    Jump('loc_2B27')

    def _loc_25B0(): pass

    label('loc_25B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_267F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2634',
    )

    ChrTalk(
        0x00FE,
        (
            '有不少市民希望\n',
            '理查德上校复职呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也说明他的\n',
            '言行是有足够魅力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来我有点\n',
            '寂寞的心情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_267C')

    def _loc_2634(): pass

    label('loc_2634')

    ChrTalk(
        0x00FE,
        (
            '有不少市民希望\n',
            '理查德上校复职呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来我有点\n',
            '寂寞的心情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_267C(): pass

    label('loc_267C')

    Jump('loc_2B27')

    def _loc_267F(): pass

    label('loc_267F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26ED',
    )

    ChrTalk(
        0x00FE,
        (
            '西街区的利贝尔通讯社\n',
            '总是亮着灯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定很忙吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市民都称呼西街区\n',
            '为不夜城的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B27')

    def _loc_26ED(): pass

    label('loc_26ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2886',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27DA',
    )

    ChrTalk(
        0x00FE,
        (
            '你们要问路就问我\n',
            '这个地道的格兰赛尔人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '共和国大使馆在东街区的南侧，\n',
            '帝国大使馆在东街区的北侧哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王住的格兰赛尔城\n',
            '在北街区的最北头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯社在西街区的南侧，\n',
            '在狭窄的胡同里，可别看漏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_2883')

    def _loc_27DA(): pass

    label('loc_27DA')

    ChrTalk(
        0x00FE,
        (
            '共和国大使馆在东街区的南侧，\n',
            '帝国大使馆在东街区的北侧哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王住的格兰赛尔城\n',
            '在北街区的最北头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯社在西街区的南侧，\n',
            '在狭窄的胡同里，可别看漏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2883(): pass

    label('loc_2883')

    Jump('loc_2B27')

    def _loc_2886(): pass

    label('loc_2886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2982',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_291F',
    )

    ChrTalk(
        0x00FE,
        (
            '在格兰赛尔设有\n',
            '下水道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在街上的很多地方\n',
            '都有管理用的入口，\n',
            '可以从那里进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说里面全是魔兽，\n',
            '还是不要进去为好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_297F')

    def _loc_291F(): pass

    label('loc_291F')

    ChrTalk(
        0x00FE,
        (
            '下水道里净是魔兽，\n',
            '还是不要进去为好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也只有承办了剿灭魔兽任务的\n',
            '游击士才有资格进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_297F(): pass

    label('loc_297F')

    Jump('loc_2B27')

    def _loc_2982(): pass

    label('loc_2982')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2B27',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AD7',
    )

    ChrTalk(
        0x00FE,
        (
            '南街区这边有协会\n',
            '和种种店铺鳞次栉比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '北街区有王国最大的宾馆。\n',
            '再往北就是格兰赛尔城了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西街区以大圣堂\n',
            '和利贝尔通讯社\n',
            '而为人们所知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而东街区\n',
            '则林立着各国大使馆、格兰竞技场\n',
            '和百货商店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，我忘了一件要紧事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西街区的对面\n',
            '有港口和仓库街。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是发生政变时\n',
            '被封锁而无法进入的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_2B27')

    def _loc_2AD7(): pass

    label('loc_2AD7')

    ChrTalk(
        0x00FE,
        (
            '西街区的对面\n',
            '有港口和仓库街。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是发生政变时\n',
            '被封锁而无法进入的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B27(): pass

    label('loc_2B27')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2B2B
@scena.Code('func_0F_2B2B')
def func_0F_2B2B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_2B38',
    )

    Jump('loc_3009')

    def _loc_2B38(): pass

    label('loc_2B38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2B90',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，想不到阳光是\n',
            '这么明亮和温暖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夜晚又暗又冷，\n',
            '令人越发不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2B90(): pass

    label('loc_2B90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2C24',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校的副官\n',
            '好象再次谋划了叛变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就觉得那张狐狸脸\n',
            '肯定没打什么好主意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我能理解\n',
            '她拼命想要帮助\n',
            '上校的心情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2C24(): pass

    label('loc_2C24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2C60',
    )

    ChrTalk(
        0x00FE,
        (
            '……穿白衣服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，我没看见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2C60(): pass

    label('loc_2C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2D02',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才我看见杜南公爵了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我怀疑自己是不是看错了，\n',
            '不过他那个发型不可能认错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听说他在离宫诚惶诚恐地过日子，\n',
            '不过看来是回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2D02(): pass

    label('loc_2D02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D6E',
    )

    ChrTalk(
        0x00FE,
        (
            '我相信理查德上校\n',
            '是有苦衷的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我完全无法\n',
            '原谅杜南公爵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不这么认为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2D6E(): pass

    label('loc_2D6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2DC3',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国大使和共和国大使……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两个人我都见过，\n',
            '都各自有着不好的毛病。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2DC3(): pass

    label('loc_2DC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2EC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E69',
    )

    ChrTalk(
        0x00FE,
        (
            '条约的签字仪式近了，\n',
            '王国军好象要对街道进行警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……理查德上校现在\n',
            '在哪里？又在干吗呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在仍然相信上校的\n',
            '政变是事出有因的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2EBF')

    def _loc_2E69(): pass

    label('loc_2E69')

    ChrTalk(
        0x00FE,
        (
            '理查德上校现在\n',
            '在哪里？又在干吗呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在仍然相信上校的\n',
            '政变是事出有因的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EBF(): pass

    label('loc_2EBF')

    Jump('loc_3009')

    def _loc_2EC2(): pass

    label('loc_2EC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3009',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FA1',
    )

    ChrTalk(
        0x00FE,
        (
            '想去艾尔贝离宫的话就从那边的\n',
            '正门出去，然后从庭园大道往南走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '走到有指示牌的三叉路后\n',
            '向格鲁纳门方向前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再一次到三叉路时\n',
            '向南走就是艾尔贝离宫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好好看指示牌的话\n',
            '应该不会迷路的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_3009')

    def _loc_2FA1(): pass

    label('loc_2FA1')

    ChrTalk(
        0x00FE,
        (
            '想去艾尔贝离宫的话就从那里的\n',
            '正门出去，然后从庭园大道往南走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '道旁有指示牌，\n',
            '应该不会迷路的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3009(): pass

    label('loc_3009')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x300D
@scena.Code('func_10_300D')
def func_10_300D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_301A',
    )

    Jump('loc_33B5')

    def _loc_301A(): pass

    label('loc_301A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_308D',
    )

    ChrTalk(
        0x00FE,
        (
            '年轻人因为从小\n',
            '生活在导力器环境下，\n',
            '好像很惊慌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那里的钓公师团的\n',
            '家伙们好像很镇定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_308D(): pass

    label('loc_308D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_30FB',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校的部下们\n',
            '好像发动了叛乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在女王脚下惹麻烦，真是一帮\n',
            '直到最后也不太平的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_30FB(): pass

    label('loc_30FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3155',
    )

    ChrTalk(
        0x00FE,
        (
            '好像卢安市长选举的\n',
            '结果出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '过一会儿去买利贝尔通讯的\n',
            '最新一期吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_3155(): pass

    label('loc_3155')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_3200',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约本身\n',
            '虽然大家心里都想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真正能付诸实施的也只有\n',
            '像艾莉茜雅女王这样的人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王是利贝尔国民的骄傲……\n',
            '那个理查德被抓真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_3200(): pass

    label('loc_3200')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3252',
    )

    ChrTalk(
        0x00FE,
        (
            '我早晨和傍晚\n',
            '必定出来散步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天的散步\n',
            '正是我健康的秘诀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_3252(): pass

    label('loc_3252')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_32A8',
    )

    ChrTalk(
        0x00FE,
        (
            '听说艾莉茜雅女王得病的时候\n',
            '我还真吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真是无礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_32A8(): pass

    label('loc_32A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3352',
    )

    ChrTalk(
        0x00FE,
        (
            '前不久在王城前看到了\n',
            '传说中的卡西乌斯准将。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然比摩尔根将军年轻，\n',
            '不过我觉得他是一个\n',
            '稳重、有威严的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可为什么百日战役的\n',
            '英雄去当游击士了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33B5')

    def _loc_3352(): pass

    label('loc_3352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_33B5',
    )

    ChrTalk(
        0x00FE,
        (
            '前一阵子在那边的酒馆\n',
            '里有个钢琴家,\n',
            '演奏很了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然人怪怪的，\n',
            '不过是真有水平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33B5(): pass

    label('loc_33B5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x33B9
@scena.Code('func_11_33B9')
def func_11_33B9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_33C6',
    )

    Jump('loc_3532')

    def _loc_33C6(): pass

    label('loc_33C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3412',
    )

    ChrTalk(
        0x00FE,
        (
            '王都总算是\n',
            '恢复平静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是拜女王陛下\n',
            '发布公告所赐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3532')

    def _loc_3412(): pass

    label('loc_3412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3443',
    )

    ChrTalk(
        0x00FE,
        (
            '想不到凯诺娜上尉\n',
            '会潜伏在王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3532')

    def _loc_3443(): pass

    label('loc_3443')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_34BC',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军里也有很多\n',
            '支持理查德的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他犯了决\n',
            '不能犯的错误。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '触犯军规的军人\n',
            '受到处罚是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3532')

    def _loc_34BC(): pass

    label('loc_34BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_3509',
    )

    ChrTalk(
        0x00FE,
        (
            '签字仪式的日子近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在希德中校的指挥下\n',
            '王都将进行警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3532')

    def _loc_3509(): pass

    label('loc_3509')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3517',
    )

    Jump('loc_3532')

    def _loc_3517(): pass

    label('loc_3517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3521',
    )

    Jump('loc_3532')

    def _loc_3521(): pass

    label('loc_3521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_352B',
    )

    Jump('loc_3532')

    def _loc_352B(): pass

    label('loc_352B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3532',
    )

    def _loc_3532(): pass

    label('loc_3532')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x3536
@scena.Code('func_12_3536')
def func_12_3536():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_3543',
    )

    Jump('loc_371E')

    def _loc_3543(): pass

    label('loc_3543')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3589',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然这么做，\n',
            '不过到关键时刻不能开枪\n',
            '还是令人不安啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_371E')

    def _loc_3589(): pass

    label('loc_3589')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_364E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_360C',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军全力搜索过了，\n',
            '不过还是没找到巨大机器人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种东西竟然也出现了，\n',
            '利贝尔接下来会变得怎样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_364B')

    def _loc_360C(): pass

    label('loc_360C')

    ChrTalk(
        0x00FE,
        (
            '不，王国军\n',
            '有那位卡西乌斯准将在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他一定有办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_364B(): pass

    label('loc_364B')

    Jump('loc_371E')

    def _loc_364E(): pass

    label('loc_364E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3691',
    )

    ChrTalk(
        0x00FE,
        (
            '没有异常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望签字仪式之前\n',
            '什么也不要发生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_371E')

    def _loc_3691(): pass

    label('loc_3691')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_36F5',
    )

    ChrTalk(
        0x00FE,
        (
            '如果你们看见可疑的人\n',
            '请一定要毫不犹豫地举报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为有可能有人\n',
            '欲图干扰签字仪式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_371E')

    def _loc_36F5(): pass

    label('loc_36F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3703',
    )

    Jump('loc_371E')

    def _loc_3703(): pass

    label('loc_3703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_370D',
    )

    Jump('loc_371E')

    def _loc_370D(): pass

    label('loc_370D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3717',
    )

    Jump('loc_371E')

    def _loc_3717(): pass

    label('loc_3717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_371E',
    )

    def _loc_371E(): pass

    label('loc_371E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3722
@scena.Code('func_13_3722')
def func_13_3722():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_372F',
    )

    Jump('loc_38DE')

    def _loc_372F(): pass

    label('loc_372F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_377B',
    )

    ChrTalk(
        0x00FE,
        (
            '有没有办法让\n',
            '导力炉能用呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有炉子的话\n',
            '做菜很麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_377B(): pass

    label('loc_377B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_37A6',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部一定想\n',
            '妨碍签字仪式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_37A6(): pass

    label('loc_37A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_37CA',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们也真不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_37CA(): pass

    label('loc_37CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_37F4',
    )

    ChrTalk(
        0x00FE,
        (
            '好，今天一整天也要努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_37F4(): pass

    label('loc_37F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_381A',
    )

    ChrTalk(
        0x00FE,
        (
            '得回去准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_381A(): pass

    label('loc_381A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3872',
    )

    ChrTalk(
        0x00FE,
        (
            '（哈欠）……我要不要\n',
            '回家去睡个午觉呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么吃了午饭\n',
            '就犯困了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_3872(): pass

    label('loc_3872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3899',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的天气\n',
            '也很爽朗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38DE')

    def _loc_3899(): pass

    label('loc_3899')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_38DE',
    )

    ChrTalk(
        0x00FE,
        (
            '你好。\n',
            '今天也是个好天气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天气好的话\n',
            '心情也会开朗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38DE(): pass

    label('loc_38DE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x38E2
@scena.Code('func_14_38E2')
def func_14_38E2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_38EF',
    )

    Jump('loc_3A7B')

    def _loc_38EF(): pass

    label('loc_38EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_393A',
    )

    ChrTalk(
        0x00FE,
        (
            '那个飞天贝壳\n',
            '好像从港口也能看见哦',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要现在就去看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_393A(): pass

    label('loc_393A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3981',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说昨天情报部和特务兵\n',
            '出现在港口了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_3981(): pass

    label('loc_3981')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_39AE',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安的市长\n',
            '好像已经确定了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_39AE(): pass

    label('loc_39AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_39E9',
    )

    ChrTalk(
        0x00FE,
        (
            '今天天气也不错，\n',
            '要不要去艾尔贝离宫看看呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_39E9(): pass

    label('loc_39E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A22',
    )

    ChrTalk(
        0x00FE,
        (
            '到底是吃鱼还是吃肉，\n',
            '这可是个问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_3A22(): pass

    label('loc_3A22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3A40',
    )

    ChrTalk(
        0x00FE,
        (
            '晚饭吃什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_3A40(): pass

    label('loc_3A40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3A5E',
    )

    ChrTalk(
        0x00FE,
        (
            '今天去哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7B')

    def _loc_3A5E(): pass

    label('loc_3A5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3A7B',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～快饿死了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A7B(): pass

    label('loc_3A7B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x3A7F
@scena.Code('func_15_3A7F')
def func_15_3A7F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_3A8C',
    )

    Jump('loc_3C55')

    def _loc_3A8C(): pass

    label('loc_3A8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3AB5',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～现在实在\n',
            '没那种心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3AB5(): pass

    label('loc_3AB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3B03',
    )

    ChrTalk(
        0x00FE,
        (
            '特务兵就是\n',
            '情报部的实战部队哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明白？\n',
            '就是说是一回事儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3B03(): pass

    label('loc_3B03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3B32',
    )

    ChrTalk(
        0x00FE,
        (
            '……他总是有点微秒的\n',
            '愣头愣脑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3B32(): pass

    label('loc_3B32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_3B65',
    )

    ChrTalk(
        0x00FE,
        (
            '……不知道吗？\n',
            '离宫现在禁止进入哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3B65(): pass

    label('loc_3B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BA8',
    )

    ChrTalk(
        0x00FE,
        (
            '你一天中有半天的时间\n',
            '都在为吃饭的事情而烦恼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3BA8(): pass

    label('loc_3BA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3BF3',
    )

    ChrTalk(
        0x00FE,
        (
            '你不是刚吃了午饭吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肚子饱饱的，\n',
            '现在什么都不想考虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3BF3(): pass

    label('loc_3BF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3C31',
    )

    ChrTalk(
        0x00FE,
        (
            '不一定非要\n',
            '去什么地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得\n',
            '悠闲一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C55')

    def _loc_3C31(): pass

    label('loc_3C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3C55',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，那么\n',
            '赶紧吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C55(): pass

    label('loc_3C55')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x3C59
@scena.Code('func_16_3C59')
def func_16_3C59():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_3C66',
    )

    Jump('loc_3EBD')

    def _loc_3C66(): pass

    label('loc_3C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3CC4',
    )

    ChrTalk(
        0x00FE,
        (
            '完全看不到\n',
            '游客的影子了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这也是没办法的事，\n',
            '不过还是令人感到萧瑟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3CC4(): pass

    label('loc_3CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_3D34',
    )

    ChrTalk(
        0x00FE,
        (
            '昨晚在西街区好像有\n',
            '一阵子不能使用导力器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系，只要让多姆调查\n',
            '一下马上就能知道原因啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3D34(): pass

    label('loc_3D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_3D6D',
    )

    ChrTalk(
        0x00FE,
        (
            '工房的塞森\n',
            '确实有一套。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3D6D(): pass

    label('loc_3D6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_3DBB',
    )

    ChrTalk(
        0x00FE,
        (
            '昨晚到很晚工房的\n',
            '３楼都有灯光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是多姆\n',
            '在通宵修理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3DBB(): pass

    label('loc_3DBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DEC',
    )

    ChrTalk(
        0x00FE,
        (
            '那就定在日落之前\n',
            '回家好不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3DEC(): pass

    label('loc_3DEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_3E40',
    )

    ChrTalk(
        0x00FE,
        (
            '工房的多姆好像和\n',
            '老板塞森大吵了一架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们以前就\n',
            '相处得不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3E40(): pass

    label('loc_3E40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_3E8F',
    )

    ChrTalk(
        0x00FE,
        (
            '工房的多姆,本事\n',
            '确实是一流的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像就没有\n',
            '他不会修的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3E8F(): pass

    label('loc_3E8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_3EBD',
    )

    ChrTalk(
        0x00FE,
        (
            '这座城市的工房\n',
            '有个亲切的修理师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EBD(): pass

    label('loc_3EBD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x3EC1
@scena.Code('func_17_3EC1')
def func_17_3EC1():
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
        'loc_3EDC',
    )

    Call(0, 0x0031)
    Call(0, 0x0032)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)

    def _loc_3EDC(): pass

    label('loc_3EDC')

    ChrSetPos(0x0101, 1530, 0, -62500, 180)
    ChrSetPos(0x012F, 150, 0, -63240, 90)
    ChrSetPos(0x00F7, 2900, 0, -63290, 270)
    ChrSetPos(0x00F8, 2150, 0, -64519, 0)
    ChrSetPos(0x00F9, 1100, 0, -64430, 0)
    CameraMove(1530, 0, -62500, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(31000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010250103V#1006F#5P好了……\n',
            '我们赶快会协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250104V关于玲的事\n',
            '必须和艾南先生商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4094',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250105V#552F这是不错，不过军队的\n',
            '负责人也快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250106V你没忘记吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250107V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050250108V#053F真是的，拿你没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4138')

    def _loc_4094(): pass

    label('loc_4094')

    ChrTalk(
        0x0103,
        (
            '#0030250109V#027F这是不错，不过军队的\n',
            '负责人也快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250110V你不会忘了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250111V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030250112V#025F呼，真拿你没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4138(): pass

    label('loc_4138')

    ChrTalk(
        0x012F,
        (
            '#0220250113V#264F#6P咦？怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250114V记得你们是要把玲\n',
            '带去那个什么协会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42DF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040250115V#031F呵呵，小小姐。\n',
            '请赐我您的手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250116V就让这个不肖的\n',
            '奥利维尔来护送您吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250117V#263F#6P你的好意我心领了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250118V玲希望姐姐\n',
            '来带路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250119V#036F唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 231, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250120V#1016F#5P啊哈哈……\n',
            '抱歉，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250121V#1006F那么小玲，\n',
            '我们去游击士协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_433C')

    def _loc_42DF(): pass

    label('loc_42DF')

    ChrSetDirection(0x0101, 231, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250122V#1006F#5P啊，嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250123V那么小玲。\n',
            '我们去游击士协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_433C(): pass

    label('loc_433C')

    ChrTalk(
        0x012F,
        (
            '#0220250124V#261F#6P嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C3, 1, 0x1619))
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x4368
@scena.Code('func_18_4368')
def func_18_4368():
    EventBegin(0x00)
    OP_4A(0x0028, 255)
    OP_4A(0x0029, 255)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x2E, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['金'], 0xF9, 0xFF)
    ChrSetPos(0x0101, 5050, 0, -11050, 180)
    ChrSetPos(0x0108, 6200, 0, -12130, 270)
    ChrSetPos(0x0104, 4000, 0, -12230, 90)
    ChrSetPos(0x0105, 5130, 0, -13310, 360)
    CameraMove(5100, 0, -12050, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010250354V#1011F#5P那么……\n',
            '开始打听情况吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250355V嗯……从哪儿开始呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250356V#070F算了，从哪儿开始都一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250357V如果是卡尔瓦德大使馆的话\n',
            '我是可以自由出入的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250358V我应该能马上\n',
            '把你们介绍给大使的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250359V#030F#6P我就负责埃雷波尼亚大使馆了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250360V只要跟门卫士兵传达，\n',
            '他们会郑重地领我们进去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250361V#040F有我在的话可以\n',
            '直接进入格兰赛尔城。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250362V可能和祖母商量一下\n',
            '是最好的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250363V#1006F#5P利贝尔通讯社\n',
            '也没什么问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250364V好，我们就\n',
            '一个个地来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008A, 0x04, 0x02)
    OP_28(0x008A, 0x04, 0x08)
    OP_28(0x008A, 0x01, 0x0001)
    OP_28(0x008A, 0x01, 0x0002)
    OP_28(0x008B, 0x04, 0x02)
    OP_28(0x008B, 0x04, 0x08)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4676',
    )

    OP_28(0x008B, 0x01, 0x0002)

    Jump('loc_4683')

    def _loc_4676(): pass

    label('loc_4676')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4683',
    )

    OP_28(0x008B, 0x01, 0x0001)

    def _loc_4683(): pass

    label('loc_4683')

    OP_28(0x008B, 0x01, 0x0004)
    OP_28(0x008B, 0x01, 0x0008)
    OP_28(0x008B, 0x01, 0x0020)
    OP_28(0x008B, 0x01, 0x0080)
    OP_28(0x008B, 0x01, 0x1000)
    EventEnd(0x00)
    OP_4B(0x0028, 255)
    OP_4B(0x0029, 255)

    Return()

# id: 0x0019 offset: 0x46AC
@scena.Code('func_19_46AC')
def func_19_46AC():
    EventBegin(0x00)
    OP_4A(0x0028, 255)
    OP_4A(0x0029, 255)
    OP_4A(0x002A, 255)
    OP_4A(0x002B, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_46D3',
    )

    Call(0, 0x0031)
    Call(0, 0x0033)

    def _loc_46D3(): pass

    label('loc_46D3')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(9240, 410, -13010, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    OP_0D()
    OP_6F(0x0001, 0)
    OP_70(0x0001, 59)
    OP_73(0x0001)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_1A_4AA8)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_1B_4ADA)
    Sleep(800)

    CreateThread(0x0107, 0x01, 0x00, func_1C_4B0C)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_1D_4B3E)
    Sleep(2000)

    @scena.Lambda('lambda_477A')
    def lambda_477A():
        CameraMove(4550, 0, -13010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_477A)

    OP_6C(32000, 3000)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010260585V#1011F#6P那么……\n',
            '关于那孩子去的地方，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260586V#1006F#5P提妲，你有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260587V#561F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260588V#060F我们昨天在东街区\n',
            '逛了很多地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260589V她有可能在其中的某个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260590V#1004F#5P逛了很多地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260591V#560F嗯，首先是在\n',
            '百货商店买东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260592V然后去了历史资料馆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260593V#061F最后在时钟台附近\n',
            '吃了冰淇淋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260594V#1016F#5P原来如此，是不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260595V#1006F提妲你也挺\n',
            '悠然自得的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260596V#067F嘿嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49F5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260597V#070F首先调查一下\n',
            '那一带吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A23')

    def _loc_49F5(): pass

    label('loc_49F5')

    ChrTalk(
        0x0105,
        (
            '#0060260598V#048F首先调查一下\n',
            '那一带吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A23(): pass

    label('loc_4A23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4A5C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260599V#051F#5P嗯。\n',
            '赶紧把她领回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A85')

    def _loc_4A5C(): pass

    label('loc_4A5C')

    ChrTalk(
        0x0103,
        (
            '#0030260600V#020F#5P嗯。\n',
            '去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A85(): pass

    label('loc_4A85')

    OP_28(0x008C, 0x04, 0x02)
    OP_28(0x008C, 0x04, 0x08)
    OP_28(0x008C, 0x01, 0x0001)
    EventEnd(0x00)
    OP_4B(0x0028, 255)
    OP_4B(0x0029, 255)
    OP_4B(0x002A, 255)
    OP_4B(0x002B, 255)

    Return()

# id: 0x001A offset: 0x4AA8
@scena.Code('func_1A_4AA8')
def func_1A_4AA8():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)
    ChrWalkTo(0x00FE, 3550, 0, -13010, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x001B offset: 0x4ADA
@scena.Code('func_1B_4ADA')
def func_1B_4ADA():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)
    ChrWalkTo(0x00FE, 4340, 0, -12060, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x001C offset: 0x4B0C
@scena.Code('func_1C_4B0C')
def func_1C_4B0C():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)
    ChrWalkTo(0x00FE, 4430, 0, -13960, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x001D offset: 0x4B3E
@scena.Code('func_1D_4B3E')
def func_1D_4B3E():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 11480, 750, -13010, 270)
    ChrWalkTo(0x00FE, 9240, 410, -13010, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    OP_72(0x0001, 0x0800)
    OP_6F(0x0001, 59)
    OP_70(0x0001, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0001)
    OP_71(0x0001, 0x0800)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 5280, 0, -13010, 2000, 0x00)

    Return()

# id: 0x001E offset: 0x4BB3
@scena.Code('func_1E_4BB3')
def func_1E_4BB3():
    EventBegin(0x00)
    NewScene('ED6_DT21/T4150._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x4BBF
@scena.Code('func_1F_4BBF')
def func_1F_4BBF():
    EventBegin(0x00)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x002A, 0x0080)
    ChrSetFlags(0x002B, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    LoadChip('ED6_DT26/CH20415._CH', 'ED6_DT26/CH20415P._CP', 22)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C20',
    )

    Call(0, 0x0031)
    Call(0, 0x0033)
    FadeIn(0, 0)

    def _loc_4C20(): pass

    label('loc_4C20')

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x00F7, 4670, 0, -3450, 180)
    ChrSetPos(0x0008, 3420, 0, -3270, 180)
    ChrSetPos(0x00F9, 4650, 0, -1250, 180)
    ChrSetPos(0x0107, 3640, 0, -1760, 180)
    ChrSetPos(0x0101, 4890, 0, 8950, 180)
    ChrSetPos(0x0009, 3730, 0, 10070, 180)
    CameraMove(5110, 0, 330, 0)
    OP_67(0, 7760, -10000, 0)
    CameraSetDistance(2410, 0)
    OP_6C(45000, 0)
    OP_6E(320, 0)
    CreateThread(0x00F7, 0x01, 0x00, func_21_5EA5)
    CreateThread(0x0008, 0x01, 0x00, func_22_5EE9)
    CreateThread(0x00F9, 0x01, 0x00, func_23_5F2D)
    CreateThread(0x0107, 0x01, 0x00, func_24_5F5D)
    CreateThread(0x0101, 0x01, 0x00, func_25_5F8D)
    CreateThread(0x0009, 0x01, 0x00, func_26_5FBD)

    @scena.Lambda('lambda_4CFD')
    def lambda_4CFD():
        CameraMove(8590, 250, -13060, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4CFD)

    FadeIn(2000, 0)
    WaitForThreadExit(0x00F7, 0x0001)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 59)
    OP_73(0x0001)
    CreateThread(0x00F7, 0x01, 0x00, func_20_5E80)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_20_5E80)
    Sleep(300)

    CreateThread(0x00F9, 0x01, 0x00, func_20_5E80)
    Sleep(300)

    CreateThread(0x0107, 0x01, 0x00, func_20_5E80)
    WaitForThreadExit(0x0107, 0x0001)
    Sleep(300)

    OP_72(0x0001, 0x0800)
    OP_6F(0x0001, 59)
    OP_70(0x0001, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)

    @scena.Lambda('lambda_4D89')
    def lambda_4D89():
        ChrWalkTo(0x00FE, 9540, 500, -13110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D89)

    @scena.Lambda('lambda_4DA4')
    def lambda_4DA4():
        ChrWalkTo(0x00FE, 6990, 250, -13160, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4DA4)

    WaitForThreadExit(0x0009, 0x0001)
    OP_71(0x0001, 0x0800)
    ChrSetDirection(0x0009, 90, 0)

    ChrTalk(
        0x0009,
        (
            '#0220260882V#267F#6P我说，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    ChrWalkTo(0x0101, 8590, 250, -13060, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010260883V#1006F#2P嗯？怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260884V我已经不生气了，\n',
            '你可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260885V#261F#6P呵呵，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260886V#265F首先，就算艾丝蒂尔生气\n',
            '也一点都不可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260887V#1019F#2P唔……你这小鬼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260888V#1015F那么是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260889V#267F#6P我说啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260890V其实我有东西\n',
            '要交给艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260891V#1004F#2P东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260892V#267F#6P嗯。\n',
            '你可别吓一跳哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    ChrMoveTo(0x0009, 7950, 250, -13090, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '玲给了艾丝蒂尔一封信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrMoveTo(0x0009, 6990, 250, -13160, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010260893V#1004F咦#2P……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260894V这是什么？给我的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260895V#260F#6P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260896V#1015F#2P谁给你的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260897V#263F#6P呵呵，你读过\n',
            '就明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260898V#1011F#2P是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadChip('ED6_DT26/CH20415._CH', 'ED6_DT26/CH20415P._CP', 22)
    Sleep(200)

    Fade(250)
    ChrSetChipByIndex(0x0101, 22)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(200)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔拆开了信封。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AD('ED6_DT24/C_VIS128._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    TalkSetChrName('')
    SetMessageWindowPos(-1, 300, -1, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0020260899V致艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260900V我迷惑了很久，\n',
            '不过还是有话必须\n',
            '要跟你说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260901V像那样离开了你，\n',
            '我这种要求可能是太过分了。\n',
            '不过能不能让我们单独见面？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020260902V今天傍晚我在格鲁纳门一侧的\n',
            '亚宁堡上等你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1500)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260903V#1004F#2P………………………\n',
            '…………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(91)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0220260904V#265F#6P呵呵，看来你明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260905V玲也是听了你的话\n',
            '以后才恍然大悟的⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010260906V#1020F#2P这、这是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260907V谁给你的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260908V#260F#6P一个黑发、琥珀色\n',
            '眼睛的帅哥哥给我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260909V我在空港的等候厅等\n',
            '艾丝蒂尔你们的时候，\n',
            '他让我把这个交给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260910V#1025F#2P……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260911V#261F#6P那个人就是艾丝蒂尔\n',
            '你说的约修亚哥哥吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260912V#1025F#2P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260913V笔迹也很像，\n',
            '嗯，应该没错的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260914V#1015F傍晚在格鲁纳门一侧的\n',
            '亚宁堡上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260915V#1020F傍晚……\n',
            '不是快到了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6F(0x0001, 0)
    OP_70(0x0001, 59)
    OP_73(0x0001)
    ChrClearFlags(0x00F7, 0x0080)

    @scena.Lambda('lambda_5556')
    def lambda_5556():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_5556)

    @scena.Lambda('lambda_5568')
    def lambda_5568():
        ChrWalkTo(0x00FE, 9500, 410, -13010, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5568)

    WaitForThreadExit(0x00F7, 0x0001)
    OP_72(0x0001, 0x0800)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 59)
    OP_70(0x0001, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0001)
    OP_71(0x0001, 0x0800)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5A0C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260916V#052F喂，你在干吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260917V艾南好像要\n',
            '介绍各地的情况哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260918V#1026F#6P阿加特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260919V我应该……怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260920V#055F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260921V喂、喂，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔默默地把信给阿加特看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0106,
        (
            '#0050260922V#052F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260923V#050F这是……约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260924V#1026F#6P嗯……看来是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260925V玲说她是从一个很像\n',
            '约修亚的人那里收到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050211830V#053F原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260927V#051F好啊，去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211050V#1004F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260929V#051F别磨蹭了，快去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260930V我会和其他人说\n',
            '个合适的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260931V#1025F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260932V#1001F谢谢你，阿加特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 600)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010260933V#1018F#2P还有玲……\n',
            '谢谢你告诉我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260934V#264F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 600)

    @scena.Lambda('lambda_58FA')
    def lambda_58FA():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_58FA')

    DispatchAsync2(0x0009, 0x0001, lambda_58FA)

    @scena.Lambda('lambda_590B')
    def lambda_590B():
        ChrWalkTo(0x00FE, 8230, 250, -30110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_590B)

    Sleep(500)

    @scena.Lambda('lambda_592B')
    def lambda_592B():
        CameraMove(8540, 250, -16640, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_592B)

    ChrWalkTo(0x00F7, 8590, 250, -13060, 2000, 0x00)
    ChrSetDirection(0x00F7, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    CameraMove(8189, 250, -12990, 2000)

    ChrTalk(
        0x0009,
        (
            '#0220260935V#268F#6P她走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260936V#267F那么想见\n',
            '那个人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260937V#051F#5P嗯……应该是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260938V嘿嘿，该怎么\n',
            '糊弄其他人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E5E')

    def _loc_5A0C(): pass

    label('loc_5A0C')

    ChrTalk(
        0x0103,
        (
            '#0030260939V#020F艾丝蒂尔，你在干吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260940V艾南好像要向我们\n',
            '介绍各地的情况哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260941V#1026F#6P雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260919V我应该……怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260943V#023F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260944V#022F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔默默地把信给雪拉扎德看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0103,
        (
            '#0030260945V#022F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260946V……是约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260924V#1026F#6P嗯……看来是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260925V玲说她是从一个很像\n',
            '约修亚的人那里收到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260949V#026F是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260950V#524F好啊，去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211050V#1004F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260952V#027F我会帮你搪塞\n',
            '其他人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260953V我知道你想去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260931V#1025F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260955V#1001F谢谢雪拉姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 600)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010260933V#1018F#2P还有玲……\n',
            '谢谢你告诉我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0220260934V#264F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 600)

    @scena.Lambda('lambda_5D5D')
    def lambda_5D5D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_5D5D')

    DispatchAsync2(0x0009, 0x0001, lambda_5D5D)

    @scena.Lambda('lambda_5D6E')
    def lambda_5D6E():
        ChrWalkTo(0x00FE, 8230, 250, -30110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5D6E)

    @scena.Lambda('lambda_5D89')
    def lambda_5D89():
        CameraMove(8540, 250, -16640, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5D89)

    ChrWalkTo(0x00F7, 8590, 250, -13060, 2000, 0x00)
    ChrSetDirection(0x00F7, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    CameraMove(8189, 250, -12990, 2000)

    ChrTalk(
        0x0009,
        (
            '#0220260935V#268F#6P她走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260936V#267F那么想见\n',
            '那个人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260960V#524F#5P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260961V那是那孩子旅行的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E5E(): pass

    label('loc_5E5E')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x5E80
@scena.Code('func_20_5E80')
def func_20_5E80():
    ChrWalkTo(0x00FE, 11500, 750, -12770, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0021 offset: 0x5EA5
@scena.Code('func_21_5EA5')
def func_21_5EA5():
    ChrWalkTo(0x00FE, 4860, 0, -9430, 2000, 0x00)
    ChrWalkTo(0x00FE, 7870, 250, -12670, 2000, 0x00)
    ChrWalkTo(0x00FE, 9670, 500, -12900, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0022 offset: 0x5EE9
@scena.Code('func_22_5EE9')
def func_22_5EE9():
    ChrWalkTo(0x00FE, 3510, 0, -9770, 2000, 0x00)
    ChrWalkTo(0x00FE, 6840, 250, -13550, 2000, 0x00)
    ChrWalkTo(0x00FE, 8650, 250, -13530, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0023 offset: 0x5F2D
@scena.Code('func_23_5F2D')
def func_23_5F2D():
    ChrWalkTo(0x00FE, 4860, 0, -9430, 2000, 0x00)
    ChrWalkTo(0x00FE, 7770, 250, -12780, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0024 offset: 0x5F5D
@scena.Code('func_24_5F5D')
def func_24_5F5D():
    ChrWalkTo(0x00FE, 3510, 0, -9770, 2000, 0x00)
    ChrWalkTo(0x00FE, 7390, 250, -13910, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0025 offset: 0x5F8D
@scena.Code('func_25_5F8D')
def func_25_5F8D():
    ChrWalkTo(0x00FE, 4860, 0, -9430, 2000, 0x00)
    ChrWalkTo(0x00FE, 5660, 0, -12220, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0026 offset: 0x5FBD
@scena.Code('func_26_5FBD')
def func_26_5FBD():
    ChrWalkTo(0x00FE, 3510, 0, -9770, 2000, 0x00)
    ChrWalkTo(0x00FE, 5130, 0, -13240, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0027 offset: 0x5FED
@scena.Code('func_27_5FED')
def func_27_5FED():
    EventBegin(0x00)
    OP_4A(0x0028, 255)
    OP_4A(0x0029, 255)
    OP_4A(0x002A, 255)
    OP_4A(0x002B, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6010',
    )

    Call(0, 0x0031)

    def _loc_6010(): pass

    label('loc_6010')

    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    CameraMove(106730, -1920, 53920, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_60C1',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_60E1')

    def _loc_60C1(): pass

    label('loc_60C1')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_60E1(): pass

    label('loc_60E1')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(9240, 410, -13010, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x0001, 0x0010)
    PlayBGM(14)
    FadeIn(2000, 0)
    OP_0D()
    OP_6F(0x0001, 0)
    OP_70(0x0001, 59)
    OP_73(0x0001)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_1A_4AA8)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_1B_4ADA)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_1C_4B0C)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_1D_4B3E)
    Sleep(2000)

    @scena.Lambda('lambda_61A2')
    def lambda_61A2():
        CameraMove(4550, 0, -13010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_61A2)

    OP_6C(32000, 3000)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010271194V#1011F#6P那么……\n',
            '接下来是柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240115V准备完毕后\n',
            '就马上去飞船坪吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6291',
    )

    ChrTalk(
        0x0106,
        (
            '#0050271196V#051F#5P反正空贼事件\n',
            '王国军应该正在搜查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271197V也不紧急，\n',
            '没必要马上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62F5')

    def _loc_6291(): pass

    label('loc_6291')

    ChrTalk(
        0x0103,
        (
            '#0030271198V#020F#5P反正空贼事件\n',
            '王国军应该正在搜查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271199V也不紧急，\n',
            '没必要马上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62F5(): pass

    label('loc_62F5')

    ChrTalk(
        0x0101,
        (
            '#0010271200V#1006F#6P这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271201V就是说解决了剩下的\n',
            '工作后再去不迟喽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_71(0x0001, 0x0010)
    SetScenaFlags(ScenaFlag(0x02C7, 5, 0x163D))
    OP_28(0x008E, 0x01, 0x0010)
    OP_28(0x008E, 0x01, 0x0020)
    OP_28(0x008E, 0x01, 0x0040)
    OP_28(0x008E, 0x01, 0x0080)
    OP_28(0x008E, 0x01, 0x0100)
    EventEnd(0x00)
    OP_4B(0x0028, 255)
    OP_4B(0x0029, 255)
    OP_4B(0x002A, 255)
    OP_4B(0x002B, 255)

    Return()

# id: 0x0028 offset: 0x6384
@scena.Code('func_28_6384')
def func_28_6384():
    ChrSetPos(0x000A, 4360, 0, -46020, 45)
    ChrSetPos(0x000B, 8590, 250, 4630, 135)
    ChrSetPos(0x000C, -20020, 0, -18430, 45)
    ChrSetPos(0x000D, -1290, 0, -27300, 225)
    ChrSetPos(0x000E, -9520, 250, -34120, 135)
    ChrSetPos(0x000F, -5550, 0, 10730, 45)
    ChrSetPos(0x0010, -2220, 0, -52660, 135)
    ChrSetPos(0x0011, 8320, 0, -54670, 135)
    ChrSetPos(0x0012, -6330, 0, -43560, 45)
    ChrSetPos(0x0013, -4470, 0, -43980, 315)
    ChrSetPos(0x0014, 7400, 250, -24080, 135)
    ChrSetPos(0x0015, -7630, 250, -23890, 180)
    ChrSetPos(0x0016, 1760, 0, 3810, 180)
    ChrSetPos(0x0017, 80, 0, -5910, 315)
    ChrSetPos(0x0018, 10730, 0, -660, 270)
    ChrSetPos(0x0019, -10270, 250, -2340, 90)
    ChrSetPos(0x001A, -12400, 0, -18460, 90)
    ChrSetPos(0x001B, 7690, 0, -41750, 180)
    ChrSetPos(0x001C, 3030, 0, -21550, 180)
    ChrSetPos(0x001D, -3210, 0, -13780, 180)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000B, 0x0020)
    ChrSetFlags(0x000C, 0x0020)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetFlags(0x000E, 0x0020)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0012, 0x0020)
    ChrSetFlags(0x0013, 0x0020)
    ChrSetFlags(0x0014, 0x0020)
    ChrSetFlags(0x0015, 0x0020)
    ChrSetFlags(0x0016, 0x0020)
    ChrSetFlags(0x0017, 0x0020)
    ChrSetFlags(0x0018, 0x0020)
    ChrSetFlags(0x0019, 0x0020)
    ChrSetFlags(0x001A, 0x0020)
    ChrSetFlags(0x001B, 0x0020)
    ChrSetFlags(0x001C, 0x0020)
    ChrSetFlags(0x001D, 0x0020)
    ChrClearFlags(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrClearFlags(0x0011, 0x0001)
    ChrClearFlags(0x0012, 0x0001)
    ChrClearFlags(0x0013, 0x0001)
    ChrClearFlags(0x0014, 0x0001)
    ChrClearFlags(0x0015, 0x0001)
    ChrClearFlags(0x0016, 0x0001)
    ChrClearFlags(0x0017, 0x0001)
    ChrClearFlags(0x0018, 0x0001)
    ChrClearFlags(0x0019, 0x0001)
    ChrClearFlags(0x001A, 0x0001)
    ChrClearFlags(0x001B, 0x0001)
    ChrClearFlags(0x001C, 0x0001)
    ChrClearFlags(0x001D, 0x0001)

    Return()

# id: 0x0029 offset: 0x65C4
@scena.Code('func_29_65C4')
def func_29_65C4():
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    LoadEffect(0x01, 'map\\\\mpfire2.eff')
    LoadEffect(0x02, 'map\\\\mpkaji0.eff')
    PlaySE(135, 0x01, 0x50)
    PlaySE(174, 0x01, 0x50)
    PlayEffect(0x02, 0xFF, 0x00FF, -40, 250, -19800, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 6610, 1800, -55210, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 250, 4400, -9460, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -6990, 1800, -36580, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -10790, 5400, -31940, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -12500, 5400, -3340, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 12600, 4800, -33570, 0, 0, 0, 1100, 1100, 1100, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 300, 3900, -2500, 0, 0, 0, 1500, 1800, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -740, 3210, -30070, 0, 0, 0, 1600, 1700, 1400, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 12400, 1900, -37980, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -15780, 7900, -15450, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 10800, 4800, 9940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 31290, 5000, -7600, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 6400, 1200, -55200, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 12720, 4600, -33670, 0, 0, 0, 1700, 1700, 1700, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 12400, 1700, -38000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -1000, 2700, -29750, 0, 0, 0, 2200, 2200, 2200, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -15780, 7600, -15200, 0, 0, 0, 1800, 1800, 1800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 1000, 2400, -2390, 0, 0, 0, 2500, 2500, 2500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 31290, 4500, -7600, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 340, 4000, -9320, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -6720, 1500, -36580, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -10840, 4800, -32049, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -12750, 5200, -3340, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 10800, 4700, 9940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x002A offset: 0x6B34
@scena.Code('func_2A_6B34')
def func_2A_6B34():
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
        'loc_6B5E',
    )

    Call(0, 0x0031)
    Call(0, 0x0034)
    FadeIn(0, 0)

    def _loc_6B5E(): pass

    label('loc_6B5E')

    LoadChip('ED6_DT07/CH02580._CH', 'ED6_DT07/CH02580P._CP', 22)
    LoadChip('ED6_DT29/CH12322._CH', 'ED6_DT29/CH12322P._CP', 23)
    LoadChip('ED6_DT29/CH12322._CH', 'ED6_DT29/CH12322P._CP', 24)
    LoadChip('ED6_DT29/CH12322._CH', 'ED6_DT29/CH12322P._CP', 25)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 27)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 28)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_6BB3'),
        (0x00000005, 'loc_6BC0'),
        (0x00000006, 'loc_6BCD'),
        (0x00000007, 'loc_6BDA'),
        (-1, 'loc_6BE7'),
    )

    def _loc_6BB3(): pass

    label('loc_6BB3')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 29)

    Jump('loc_6BE7')

    def _loc_6BC0(): pass

    label('loc_6BC0')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 29)

    Jump('loc_6BE7')

    def _loc_6BCD(): pass

    label('loc_6BCD')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 29)

    Jump('loc_6BE7')

    def _loc_6BDA(): pass

    label('loc_6BDA')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 29)

    Jump('loc_6BE7')

    def _loc_6BE7(): pass

    label('loc_6BE7')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_6C00'),
        (0x00000005, 'loc_6C0D'),
        (0x00000006, 'loc_6C1A'),
        (0x00000007, 'loc_6C27'),
        (-1, 'loc_6C34'),
    )

    def _loc_6C00(): pass

    label('loc_6C00')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 30)

    Jump('loc_6C34')

    def _loc_6C0D(): pass

    label('loc_6C0D')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 30)

    Jump('loc_6C34')

    def _loc_6C1A(): pass

    label('loc_6C1A')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 30)

    Jump('loc_6C34')

    def _loc_6C27(): pass

    label('loc_6C27')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 30)

    Jump('loc_6C34')

    def _loc_6C34(): pass

    label('loc_6C34')

    ChrSetChipByIndex(0x001E, 22)
    ChrSetPos(0x0101, 630, 0, -62820, 0)
    ChrSetPos(0x0102, 1830, 0, -62880, 0)
    ChrSetPos(0x00F8, 270, 0, -64190, 0)
    ChrSetPos(0x00F9, 1700, 0, -64349, 0)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)
    CameraMove(780, 250, 3690, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3370, 0)
    OP_6C(22000, 0)
    OP_6E(435, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x00, 0x03E8)
    ShowPlaceName('王都格兰赛尔')
    FadeIn(1000, 0)

    @scena.Lambda('lambda_6D05')
    def lambda_6D05():
        CameraMove(1690, 0, -62710, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6D05)

    @scena.Lambda('lambda_6D1D')
    def lambda_6D1D():
        OP_67(0, 8670, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6D1D)

    @scena.Lambda('lambda_6D35')
    def lambda_6D35():
        CameraSetDistance(1940, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6D35)

    @scena.Lambda('lambda_6D45')
    def lambda_6D45():
        OP_6C(33000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6D45)

    OP_6E(389, 9000)

    ChrTalk(
        0x0101,
        (
            '#0010380133V#1020F#5P真、真过分……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6DB9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380134V#065F#6P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6DB9(): pass

    label('loc_6DB9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6DF1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380135V#523F#6P真是触目惊心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6DF1(): pass

    label('loc_6DF1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E25',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380136V#077F#6P太惨烈了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E25(): pass

    label('loc_6E25')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E57',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380137V#057F#6P可恶……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E57(): pass

    label('loc_6E57')

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 28)

    ChrTalk(
        0x0102,
        (
            '#0020380138V#1046F#4P……敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetFlags(0x001F, 0x0004)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetChipByIndex(0x001F, 20)
    ChrSetChipByIndex(0x0020, 20)
    ChrSetPos(0x001F, -3390, 1000, -51000, 180)
    ChrSetPos(0x0020, 2660, 1000, -51000, 180)

    @scena.Lambda('lambda_6EF1')
    def lambda_6EF1():
        CameraMove(2080, 0, -60800, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6EF1)

    @scena.Lambda('lambda_6F09')
    def lambda_6F09():
        OP_67(0, 7000, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F09)

    @scena.Lambda('lambda_6F21')
    def lambda_6F21():
        CameraSetDistance(1800, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6F21)

    @scena.Lambda('lambda_6F31')
    def lambda_6F31():
        OP_6E(389, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6F31)

    ChrSetChipByIndex(0x001F, 21)
    CreateThread(0x001F, 0x03, 0x00, func_2B_6FF2)

    @scena.Lambda('lambda_6F4D')
    def lambda_6F4D():
        ChrMoveTo(0x00FE, 0, 500, -60500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_6F4D)

    Sleep(200)

    ChrSetChipByIndex(0x0020, 21)

    @scena.Lambda('lambda_6F72')
    def lambda_6F72():
        ChrMoveTo(0x00FE, 2830, 500, -60000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_6F72)

    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 27)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 29)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 30)
    WaitForThreadExit(0x001F, 0x0001)
    WaitForThreadExit(0x0020, 0x0001)
    TerminateThread(0x001F, 0x03)
    OP_23(0x013A)
    WaitForThreadExit(0x0101, 0x0000)
    CreateThread(0x001F, 0x00, 0x00, func_2C_7020)
    Sleep(100)

    CreateThread(0x0020, 0x00, 0x00, func_2C_7020)
    WaitForThreadExit(0x001F, 0x0000)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)
    Battle(0x0000054F, 0x00000000, 0x00, 0x0000, 0xFF)
    Call(0, 0x002D)

    Return()

# id: 0x002B offset: 0x6FF2
@scena.Code('func_2B_6FF2')
def func_2B_6FF2():
    PlaySE(314, 0x00, 0x64)
    Sleep(300)

    PlaySE(314, 0x00, 0x64)
    Sleep(300)

    PlaySE(314, 0x00, 0x64)
    Sleep(300)

    PlaySE(314, 0x00, 0x64)
    Sleep(300)

    PlaySE(314, 0x00, 0x64)

    Return()

# id: 0x002C offset: 0x7020
@scena.Code('func_2C_7020')
def func_2C_7020():
    ChrSetChipByIndex(0x00FE, 23)
    OP_99(0x00FE, 0x00, 0x02, 1500)
    OP_9E(0x00FE, 15, 0, 300, 3000)
    OP_99(0x00FE, 0x03, 0x04, 2500)

    Return()

# id: 0x002D offset: 0x704B
@scena.Code('func_2D_704B')
def func_2D_704B():
    EventBegin(0x00)
    LoadChip('ED6_DT07/CH02580._CH', 'ED6_DT07/CH02580P._CP', 22)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 27)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 28)
    TerminateThread(0x001F, 0x01)
    TerminateThread(0x0020, 0x01)
    TerminateThread(0x0021, 0x01)
    CameraMove(30, 0, -56130, 0)
    OP_67(0, 7860, -10000, 0)
    CameraSetDistance(2260, 0)
    OP_6C(359000, 0)
    OP_6E(371, 0)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    ChrSetPos(0x0101, -490, 0, -62350, 0)
    ChrSetPos(0x0102, 790, 0, -62340, 0)
    ChrSetPos(0x00F8, -870, 0, -64030, 0)
    ChrSetPos(0x00F9, 1170, 0, -64250, 0)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x0036, 0x0080)
    ChrSetFlags(0x0037, 0x0080)
    ChrSetFlags(0x0038, 0x0080)

    @scena.Lambda('lambda_714E')
    def lambda_714E():
        CameraMove(70, 0, -61320, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_714E)

    @scena.Lambda('lambda_7166')
    def lambda_7166():
        CameraSetDistance(1990, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7166)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010380139V#1022F#5P哎呀……\n',
            '怎、怎么办……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380140V#1005F在这种情况下\n',
            '应该做什么才好呢……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x001E, 4920, 0, -49670, 225)
    ChrClearFlags(0x001E, 0x0080)

    NpcTalk(
        0x001E,
        '青年的声音',
        (
            '#0590380141V#6P──各位！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7288',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_72C6')

    def _loc_7288(): pass

    label('loc_7288')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72AF',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_72C6')

    def _loc_72AF(): pass

    label('loc_72AF')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_72C6(): pass

    label('loc_72C6')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72F2',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7330')

    def _loc_72F2(): pass

    label('loc_72F2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7319',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7330')

    def _loc_7319(): pass

    label('loc_7319')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_7330(): pass

    label('loc_7330')

    Sleep(1000)

    @scena.Lambda('lambda_733B')
    def lambda_733B():
        CameraMove(700, 0, -60230, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_733B)

    @scena.Lambda('lambda_7353')
    def lambda_7353():
        OP_67(0, 5480, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7353)

    @scena.Lambda('lambda_736B')
    def lambda_736B():
        CameraSetDistance(2720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_736B)

    @scena.Lambda('lambda_737B')
    def lambda_737B():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_737B)

    @scena.Lambda('lambda_738B')
    def lambda_738B():
        OP_6E(289, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_738B)

    @scena.Lambda('lambda_739B')
    def lambda_739B():
        ChrWalkTo(0x00FE, 1900, 0, -59530, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_739B)

    @scena.Lambda('lambda_73B6')
    def lambda_73B6():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_73B6')

    DispatchAsync2(0x0101, 0x0001, lambda_73B6)

    Sleep(50)

    @scena.Lambda('lambda_73CC')
    def lambda_73CC():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_73CC')

    DispatchAsync2(0x0102, 0x0001, lambda_73CC)

    Sleep(50)

    @scena.Lambda('lambda_73E2')
    def lambda_73E2():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_73E2')

    DispatchAsync2(0x00F8, 0x0001, lambda_73E2)

    Sleep(50)

    @scena.Lambda('lambda_73F8')
    def lambda_73F8():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_73F8')

    DispatchAsync2(0x00F9, 0x0001, lambda_73F8)

    WaitForThreadExit(0x001E, 0x0001)
    ChrSetDirection(0x001E, 225, 400)
    TerminateThread(0x0102, 0x01)
    ChrSetDirection(0x0102, 45, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010380142V#1004F#6P艾南先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0590380143V#762F#2P你们来得正好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590380144V是为了女王陛下的\n',
            '事来王都的吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380145V#1042F#6P嗯……现在的情况是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0590380146V#764F#2P现在军队的守备队\n',
            '正在东街区和西街区作战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590380147V形势很严峻，\n',
            '不过现在也只有交给他们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590380148V#762F各位请去追击\n',
            '前往城堡的执行者们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380149V#1020F#6P可、可是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75D6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380150V#022F#6P市区要不要紧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7645')

    def _loc_75D6(): pass

    label('loc_75D6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_760F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380151V#072F#6P市区要不要紧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7645')

    def _loc_760F(): pass

    label('loc_760F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7645',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380152V#057F#6P市区要不要紧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7645(): pass

    label('loc_7645')

    ChrTalk(
        0x001E,
        (
            '#0590380153V#762F#2P这附近的人\n',
            '已经去协会避难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590380154V在其他的街区也有\n',
            '军队在引导人们避难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380155V#1007F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380156V#1002F……那么，虽然很抱歉，\n',
            '但我们要抓紧时间赶去王都了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0590380157V#764F#2P嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590380158V#760F对了……\n',
            '不嫌弃的话，请把这个拿去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_93(0x001E, 0x0102, 1000, 3000, 0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(ItemTable['还魂粉'], 4)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrMoveTo(0x001E, 1900, 0, -59530, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020380159V#1040F#6P那我们就愧领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0590380160V#762F#2P祝你们旗开得胜……\n',
            '请一定要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_784B')
    def lambda_784B():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_784B')

    DispatchAsync2(0x0102, 0x0001, lambda_784B)

    ChrSetDirection(0x001E, 0, 600)
    ChrWalkTo(0x001E, 4460, 0, -51270, 5000, 0x00)
    ChrSetFlags(0x001E, 0x0080)
    Fade(500)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    CameraMove(1560, 0, -61910, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 1560, 0, -61910, 0)
    ChrSetPos(0x0001, 1560, 0, -61910, 0)
    ChrSetPos(0x0002, 1560, 0, -61910, 0)
    ChrSetPos(0x0003, 1560, 0, -61910, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0407, 3, 0x203B))
    OP_28(0x009C, 0x01, 0x0010)
    OP_28(0x009C, 0x01, 0x0020)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x002E offset: 0x793D
@scena.Code('func_2E_793D')
def func_2E_793D():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapSetFlags(0x02000000)

    Return()

# id: 0x002F offset: 0x7976
@scena.Code('func_2F_7976')
def func_2F_7976():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_797F',
    )

    Return()

    def _loc_797F(): pass

    label('loc_797F')

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_799F',
    )

    Call(0, 0x0031)
    Call(0, 0x0034)
    FadeIn(0, 0)

    def _loc_799F(): pass

    label('loc_799F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东街区断断续续地\n',
            '传来枪声和剑戟的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A56',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380161V#1002F（看来是军队在\n',
            '和猎兵作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380162V(我们得赶快\n',
            '赶往城堡！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C5B')

    def _loc_7A56(): pass

    label('loc_7A56')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7ABD',
    )

    ChrTalk(
        0x0102,
        (
            '#0020380163V#1042F（这边布置了\n',
            '军队……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380164V(就交给他们吧，我们去城堡。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C5B')

    def _loc_7ABD(): pass

    label('loc_7ABD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B21',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380165V#022F（这边应该\n',
            '有军队在作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030380166V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C5B')

    def _loc_7B21(): pass

    label('loc_7B21')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7B98',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380167V#062F（军队的失败们看来\n',
            '正在结社的人作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070380168V(我们得赶快\n',
            '赶往城堡……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C5B')

    def _loc_7B98(): pass

    label('loc_7B98')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C00',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380169V#057F（看来军队住在\n',
            '和猎兵们作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050380170V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C5B')

    def _loc_7C00(): pass

    label('loc_7C00')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C5B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380171V#072F（这边有军队\n',
            '在守护……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250453V(我们赶紧去王城吧)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C5B(): pass

    label('loc_7C5B')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0030 offset: 0x7C7C
@scena.Code('func_30_7C7C')
def func_30_7C7C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C85',
    )

    Return()

    def _loc_7C85(): pass

    label('loc_7C85')

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7CA5',
    )

    Call(0, 0x0031)
    Call(0, 0x0034)
    FadeIn(0, 0)

    def _loc_7CA5(): pass

    label('loc_7CA5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西街区断断续续地\n',
            '传来枪声和剑戟的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D5C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010380161V#1002F（看来是军队在\n',
            '和猎兵作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380162V(我们得赶快\n',
            '赶往城堡！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F64')

    def _loc_7D5C(): pass

    label('loc_7D5C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DC3',
    )

    ChrTalk(
        0x0102,
        (
            '#0020380163V#1042F（这边布置了\n',
            '军队……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380164V(就交给他们吧，我们去城堡。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F64')

    def _loc_7DC3(): pass

    label('loc_7DC3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E27',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380165V#022F（这边应该\n',
            '有军队在作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030380166V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F64')

    def _loc_7E27(): pass

    label('loc_7E27')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7EA1',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380167V#062F（军队的士兵们看来\n',
            '正在和结社的人作战……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070380168V(我们得赶快\n',
            '赶往城堡……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F64')

    def _loc_7EA1(): pass

    label('loc_7EA1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F09',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380169V#057F（看来军队正在\n',
            '和猎兵们作战……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050380170V(我们还是去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F64')

    def _loc_7F09(): pass

    label('loc_7F09')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F64',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380171V#072F（这边有军队\n',
            '在守护……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250453V(我们赶紧去王城吧)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F64(): pass

    label('loc_7F64')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0031 offset: 0x7F85
@scena.Code('func_31_7F85')
def func_31_7F85():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_7FFF'),
        (0x00000001, 'loc_8005'),
        (-1, 'loc_800B'),
    )

    def _loc_7FFF(): pass

    label('loc_7FFF')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_800B')

    def _loc_8005(): pass

    label('loc_8005')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_800B')

    def _loc_800B(): pass

    label('loc_800B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8019',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_801D')

    def _loc_8019(): pass

    label('loc_8019')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_801D(): pass

    label('loc_801D')

    Return()

# id: 0x0032 offset: 0x801E
@scena.Code('func_32_801E')
def func_32_801E():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8061',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_807F')

    def _loc_8061(): pass

    label('loc_8061')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_807F(): pass

    label('loc_807F')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0033 offset: 0x809F
@scena.Code('func_33_809F')
def func_33_809F():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_80DE',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_80F8')

    def _loc_80DE(): pass

    label('loc_80DE')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_80F8(): pass

    label('loc_80F8')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0034 offset: 0x8118
@scena.Code('func_34_8118')
def func_34_8118():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0035 offset: 0x8171
@scena.Code('func_35_8171')
def func_35_8171():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_83E9',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_81D9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250442V#1002F（现在不能\n',
            '离开王都……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250443V(得赶紧赶往城堡！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_83C6')

    def _loc_81D9(): pass

    label('loc_81D9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_823E',
    )

    ChrTalk(
        0x0102,
        (
            '#0020250444V#1042F（现在不能\n',
            '离开王都……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020250445V(得分秒必争地赶往城堡。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_83C6')

    def _loc_823E(): pass

    label('loc_823E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_829A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030250446V#022F（现在时间\n',
            '十分宝贵……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250447V(赶紧去城堡吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_83C6')

    def _loc_829A(): pass

    label('loc_829A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8305',
    )

    ChrTalk(
        0x0107,
        (
            '#0070250448V#065F（啊……这边是出口哦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250449V#062F（总之现在\n',
            '赶往城堡……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_83C6')

    def _loc_8305(): pass

    label('loc_8305')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8369',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250450V#050F（没时间在这里\n',
            '磨磨蹭蹭的了……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250451V(得赶紧去城堡。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_83C6')

    def _loc_8369(): pass

    label('loc_8369')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83C6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080250452V#072F（没时间在这里\n',
            '担搁了……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250453V(我们赶紧去王城吧)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_83C6(): pass

    label('loc_83C6')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Jump('loc_89DE')

    def _loc_83E9(): pass

    label('loc_83E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 6, 0x162E)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8469',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0101, 0x0000, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250454V#1006F玲应该还在城里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250455V那么\n',
            '一定要把她找出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_89DE')

    def _loc_8469(): pass

    label('loc_8469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8706',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0000, 0x0001, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84E9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250456V#1006F她一个人出城\n',
            '总是不可能的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250457V首先从东街区\n',
            '附近开始找。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E8')

    def _loc_84E9(): pass

    label('loc_84E9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_854F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030250458V#020F无法想象她会\n',
            '一个人出城。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250459V总之先搜索\n',
            '东街区附近吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E8')

    def _loc_854F(): pass

    label('loc_854F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85BF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070250460V#060F小玲应该还没\n',
            '出城吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250461V首先从她昨天去过的\n',
            '东街区附近开始找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E8')

    def _loc_85BF(): pass

    label('loc_85BF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_861F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250462V#050F她总不至于\n',
            '出城吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250463V首先从东街区\n',
            '附近开始找。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E8')

    def _loc_861F(): pass

    label('loc_861F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8683',
    )

    ChrTalk(
        0x0108,
        (
            '#0080250464V#070F她应该不会\n',
            '出城吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250465V总之先从东街区\n',
            '附近开始找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E8')

    def _loc_8683(): pass

    label('loc_8683')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86E8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060250466V#040F我觉得她还不至于\n',
            '一个人出城。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250467V总之从东街区\n',
            '开始找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86E8(): pass

    label('loc_86E8')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_89DE')

    def _loc_8706(): pass

    label('loc_8706')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8842',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_875C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250468V#1000F已经，差不多时间了。\n',
            '该回协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8824')

    def _loc_875C(): pass

    label('loc_875C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_879D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040250469V#030F太阳都要下山了。\n',
            '回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8824')

    def _loc_879D(): pass

    label('loc_879D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87DC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080250470V#070F已经挺玩了。\n',
            '赶紧回协会吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8824')

    def _loc_87DC(): pass

    label('loc_87DC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8824',
    )

    ChrTalk(
        0x0105,
        (
            '#0060250471V#040F太阳都要下山了。\n',
            '差不多该回协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8824(): pass

    label('loc_8824')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_89DE')

    def _loc_8842(): pass

    label('loc_8842')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_89DE',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88A4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250472V#1000F没必要出城。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250473V赶快\n',
            '去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89C3')

    def _loc_88A4(): pass

    label('loc_88A4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8907',
    )

    ChrTalk(
        0x0104,
        (
            '#0040250474V#030F恐吓信的调查\n',
            '看来还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250475V我们快去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89C3')

    def _loc_8907(): pass

    label('loc_8907')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8965',
    )

    ChrTalk(
        0x0108,
        (
            '#0080250476V#070F就算出去\n',
            '也找不到罪犯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250477V赶快打听\n',
            '好情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89C3')

    def _loc_8965(): pass

    label('loc_8965')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89C3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060250478V#040F恐吓信的调查\n',
            '还没结束呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250479V赶快回去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89C3(): pass

    label('loc_89C3')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_89DE(): pass

    label('loc_89DE')

    Return()

# id: 0x0036 offset: 0x89DF
@scena.Code('func_36_89DF')
def func_36_89DF():
    Call(0, 0x003C)
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0037 offset: 0x89FF
@scena.Code('func_37_89FF')
def func_37_89FF():
    Call(0, 0x003C)
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0038 offset: 0x8A1F
@scena.Code('func_38_8A1F')
def func_38_8A1F():
    Call(0, 0x003C)
    OP_59()

    @scena.Lambda('lambda_8A2A')
    def lambda_8A2A():
        CameraMove(-3370, 0, 9000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_8A2A)

    Fade(1000)
    ChrSetPos(0x0000, -3370, 0, 12430, 180)
    ChrSetPos(0x0001, -3370, 0, 12430, 180)
    ChrSetPos(0x0002, -3370, 0, 12430, 180)
    ChrSetPos(0x0003, -3370, 0, 12430, 180)
    ChrSetPos(0x012F, -3370, 0, 12430, 180)
    OP_0D()
    ChrSetDirection(0x0000, 180, 0)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0039 offset: 0x8AA6
@scena.Code('func_39_8AA6')
def func_39_8AA6():
    Call(0, 0x003C)
    OP_59()

    @scena.Lambda('lambda_8AB1')
    def lambda_8AB1():
        CameraMove(3370, 0, 9000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_8AB1)

    Fade(1000)
    ChrSetPos(0x0000, 3370, 0, 12430, 180)
    ChrSetPos(0x0001, 3370, 0, 12430, 180)
    ChrSetPos(0x0002, 3370, 0, 12430, 180)
    ChrSetPos(0x0003, 3370, 0, 12430, 180)
    ChrSetPos(0x012F, 3370, 0, 12430, 180)
    OP_0D()
    ChrSetDirection(0x0000, 180, 0)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x003A offset: 0x8B2D
@scena.Code('func_3A_8B2D')
def func_3A_8B2D():
    Call(0, 0x003C)
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x003B offset: 0x8B4D
@scena.Code('func_3B_8B4D')
def func_3B_8B4D():
    Call(0, 0x003C)
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x003C offset: 0x8B6D
@scena.Code('func_3C_8B6D')
def func_3C_8B6D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8D90',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8C41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8BE5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B9F',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_8BA6')

    def _loc_8B9F(): pass

    label('loc_8B9F')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_8BA6(): pass

    label('loc_8BA6')

    ChrTalk(
        0x0106,
        (
            '#0050250125V#050F……得赶快确认消息。\n',
            '径直返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C3E')

    def _loc_8BE5(): pass

    label('loc_8BE5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8BFB',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_8C02')

    def _loc_8BFB(): pass

    label('loc_8BFB')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_8C02(): pass

    label('loc_8C02')

    ChrTalk(
        0x0103,
        (
            '#0030250126V#020F……得赶快确认消息。\n',
            '径直返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8C3E(): pass

    label('loc_8C3E')

    Jump('loc_8D8D')

    def _loc_8C41(): pass

    label('loc_8C41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8CA4',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C5E',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_8C65')

    def _loc_8C5E(): pass

    label('loc_8C5E')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_8C65(): pass

    label('loc_8C65')

    ChrTalk(
        0x0106,
        (
            '#0050250125V#050F……得赶快确认消息。\n',
            '径直返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CFD')

    def _loc_8CA4(): pass

    label('loc_8CA4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8CBA',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_8CC1')

    def _loc_8CBA(): pass

    label('loc_8CBA')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_8CC1(): pass

    label('loc_8CC1')

    ChrTalk(
        0x0103,
        (
            '#0030250126V#020F……得赶快确认消息。\n',
            '径直返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8CFD(): pass

    label('loc_8CFD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D35',
    )

    ChrTurnDirection(0x0000, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250129V#1000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D67')

    def _loc_8D35(): pass

    label('loc_8D35')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D67',
    )

    ChrTurnDirection(0x0000, 0x00F7, 400)

    ChrTalk(
        0x0107,
        (
            '#0070250130V#060F嗯，是啊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D67(): pass

    label('loc_8D67')

    ChrTalk(
        0x012F,
        (
            '#0220250131V#268F啊，好无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_8D8D(): pass

    label('loc_8D8D')

    Jump('loc_90C5')

    def _loc_8D90(): pass

    label('loc_8D90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90C5',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8DF5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080250132V#070F军队的负责人\n',
            '快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250133V赶紧回协会吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90C5')

    def _loc_8DF5(): pass

    label('loc_8DF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8EDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8E6D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E19',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_8E20')

    def _loc_8E19(): pass

    label('loc_8E19')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_8E20(): pass

    label('loc_8E20')

    ChrTalk(
        0x0106,
        (
            '#0050250134V#050F军队的负责人\n',
            '快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250135V赶快回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EDA')

    def _loc_8E6D(): pass

    label('loc_8E6D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E83',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_8E8A')

    def _loc_8E83(): pass

    label('loc_8E83')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_8E8A(): pass

    label('loc_8E8A')

    ChrTalk(
        0x0103,
        (
            '#0030250136V#020F军队的负责人\n',
            '也快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250137V我们赶快会协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8EDA(): pass

    label('loc_8EDA')

    Jump('loc_90C5')

    def _loc_8EDD(): pass

    label('loc_8EDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8F4E',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8EFA',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_8F01')

    def _loc_8EFA(): pass

    label('loc_8EFA')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_8F01(): pass

    label('loc_8F01')

    ChrTalk(
        0x0106,
        (
            '#0050250134V#050F军队的负责人\n',
            '快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250135V赶快回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8FBB')

    def _loc_8F4E(): pass

    label('loc_8F4E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F64',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_8F6B')

    def _loc_8F64(): pass

    label('loc_8F64')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_8F6B(): pass

    label('loc_8F6B')

    ChrTalk(
        0x0103,
        (
            '#0030250136V#020F军队的负责人\n',
            '也快要来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250137V我们赶快会协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8FBB(): pass

    label('loc_8FBB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FF5',
    )

    ChrTurnDirection(0x0000, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250142V#1011F哎呀，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_909B')

    def _loc_8FF5(): pass

    label('loc_8FF5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_902C',
    )

    ChrTurnDirection(0x0000, 0x00F7, 400)

    ChrTalk(
        0x0104,
        (
            '#0040250143V#030F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_909B')

    def _loc_902C(): pass

    label('loc_902C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9069',
    )

    ChrTurnDirection(0x0000, 0x00F7, 400)

    ChrTalk(
        0x0105,
        (
            '#0060250144V#040F嗯嗯，是的是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_909B')

    def _loc_9069(): pass

    label('loc_9069')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_909B',
    )

    ChrTurnDirection(0x0000, 0x00F7, 400)

    ChrTalk(
        0x0107,
        (
            '#0070250130V#060F嗯，是啊',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_909B(): pass

    label('loc_909B')

    ChrTalk(
        0x012F,
        (
            '#0220250146V#264F咦？不是这边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_90C5(): pass

    label('loc_90C5')

    Return()

# id: 0x003D offset: 0x90C6
@scena.Code('func_3D_90C6')
def func_3D_90C6():
    OP_13(0x00B9)

    Return()

# id: 0x003E offset: 0x90CA
@scena.Code('func_3E_90CA')
def func_3E_90CA():
    OP_13(0x00B0)

    Return()

# id: 0x003F offset: 0x90CE
@scena.Code('func_3F_90CE')
def func_3F_90CE():
    OP_13(0x00B2)

    Return()

# id: 0x0040 offset: 0x90D2
@scena.Code('func_40_90D2')
def func_40_90D2():
    OP_13(0x00AE)

    Return()

# id: 0x0041 offset: 0x90D6
@scena.Code('func_41_90D6')
def func_41_90D6():
    OP_13(0x00B3)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
