import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4103   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵'),
    TXT(0x02, '士兵'),
    TXT(0x03, '士兵'),
    TXT(0x04, '士兵'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '士兵'),
    TXT(0x09, '阿鲁姆'),
    TXT(0x0A, '艾娅莉'),
    TXT(0x0B, '托伊'),
    TXT(0x0C, '马丁'),
    TXT(0x0D, '玛丽安'),
    TXT(0x0E, '海伦娜'),
    TXT(0x0F, '诺雅尔'),
    TXT(0x10, '维基奥'),
    TXT(0x11, '巴鲁托'),
    TXT(0x12, '士兵'),
    TXT(0x13, '士兵'),
    TXT(0x14, '士兵'),
    TXT(0x15, '士兵'),
    TXT(0x16, '特务兵'),
    TXT(0x17, '特务兵'),
    TXT(0x18, '特务兵'),
    TXT(0x19, '米亚尔'),
    TXT(0x1A, '戈万'),
    TXT(0x1B, '修女艾伦'),
    TXT(0x1C, '观光客'),
    TXT(0x1D, '观光客'),
    TXT(0x1E, '观光客'),
    TXT(0x1F, '观光客'),
    TXT(0x20, '观光客'),
    TXT(0x21, '观光客'),
    TXT(0x22, '观光客'),
    TXT(0x23, '观光客'),
    TXT(0x24, '观光客'),
    TXT(0x25, '观光客'),
    TXT(0x26, '观光客'),
    TXT(0x27, '观光客'),
    TXT(0x28, '王都格兰赛尔·西街区'),
    TXT(0x29, '格兰赛尔城'),
    TXT(0x2A, '王都格兰赛尔·东街区'),
    TXT(0x2B, '王都格兰赛尔·南街区'),
    TXT(0x2C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4103.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x430B
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
            dword_08        = 0x000101D0,
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
    ]

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -2980,
            z                   = 0,
            y                   = 68330,
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
            x                   = 3120,
            z                   = 0,
            y                   = 68420,
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
            x                   = -32570,
            z                   = 0,
            y                   = 50050,
            direction           = 90,
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
            x                   = -9530,
            z                   = 250,
            y                   = 32240,
            direction           = 90,
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
            x                   = 9480,
            z                   = 250,
            y                   = 37480,
            direction           = 270,
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
            x                   = 560,
            z                   = 0,
            y                   = 39030,
            direction           = 225,
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
            x                   = -370,
            z                   = 0,
            y                   = 38160,
            direction           = 45,
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
            x                   = 3800,
            z                   = 0,
            y                   = 65780,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x002D,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 6490,
            z                   = 0,
            y                   = 43840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -2950,
            z                   = 0,
            y                   = 63820,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -7440,
            z                   = 0,
            y                   = 49400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -6340,
            z                   = 0,
            y                   = 52120,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 6490,
            z                   = 0,
            y                   = 43840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -2950,
            z                   = 0,
            y                   = 63820,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 3660,
            z                   = 0,
            y                   = 64440,
            direction           = 356,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -7400,
            z                   = 250,
            y                   = 59390,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 4750,
            z                   = 0,
            y                   = 10320,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -710,
            z                   = 0,
            y                   = 68870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -5260,
            z                   = 0,
            y                   = 66960,
            direction           = 131,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = -5940,
            z                   = 0,
            y                   = 65580,
            direction           = 30,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = -8140,
            z                   = 250,
            y                   = 56080,
            direction           = 219,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = -10060,
            z                   = 250,
            y                   = 56020,
            direction           = 149,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = -9190,
            z                   = 250,
            y                   = 54240,
            direction           = 9,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 7480,
            z                   = 250,
            y                   = 59730,
            direction           = 267,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            x                   = 9690,
            z                   = 250,
            y                   = 50490,
            direction           = 281,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            x                   = 7050,
            z                   = 250,
            y                   = 50520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = 9510,
            z                   = 0,
            y                   = 44040,
            direction           = 96,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            x                   = 8700,
            z                   = 0,
            y                   = 44910,
            direction           = 108,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            x                   = 7190,
            z                   = 250,
            y                   = 38180,
            direction           = 258,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            x                   = -7530,
            z                   = 250,
            y                   = 44220,
            direction           = 37,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            x                   = -40080,
            z                   = 0,
            y                   = 17660,
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
            x                   = 100,
            z                   = 0,
            y                   = 104130,
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
            x                   = 40430,
            z                   = 0,
            y                   = 64060,
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
            x                   = 20,
            z                   = 0,
            y                   = -3500,
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

# id: 0x10003 offset: 0x6D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x6D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 18520,
            y           = 0,
            z           = 44050,
            range       = 1500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000030,
        ),
    )

# id: 0x10005 offset: 0x6F2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x6F2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_70E',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x002B)
    OP_B1('t4103_n')

    def _loc_70E(): pass

    label('loc_70E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006E, 'loc_71A'),
        (-1, 'loc_730'),
    )

    def _loc_71A(): pass

    label('loc_71A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 4, 0x62C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_72D',
    )

    SetScenaFlags(ScenaFlag(0x00C5, 4, 0x62C))
    Event(0, 0x002F)

    def _loc_72D(): pass

    label('loc_72D')

    Jump('loc_730')

    def _loc_730(): pass

    label('loc_730')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7F4',
    )

    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, -7310, 250, 28970, 270)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, -9190, 250, 29720, 90)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -9190, 250, 28210, 90)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    SetChrFlags(0x0023, 0x0010)
    ClearChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0024, 0x0010)
    ClearChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0025, 0x0010)
    ClearChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0026, 0x0010)
    ClearChrFlags(0x0027, 0x0080)
    SetChrFlags(0x0027, 0x0010)
    ClearChrFlags(0x0028, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)
    SetChrFlags(0x002A, 0x0010)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    SetChrFlags(0x002C, 0x0010)
    ClearChrFlags(0x002D, 0x0080)
    ClearChrFlags(0x002E, 0x0080)

    Jump('loc_93B')

    def _loc_7F4(): pass

    label('loc_7F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_848',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0010, 0x0010)
    SetChrPos(0x0010, -3840, 0, 67340, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0010)
    SetChrPos(0x0011, -2760, 0, 67340, 0)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0021, 0x0080)

    Jump('loc_93B')

    def _loc_848(): pass

    label('loc_848')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_897',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -3820, 0, 66400, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -2760, 0, 66400, 0)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x0021, 0x0080)

    Jump('loc_93B')

    def _loc_897(): pass

    label('loc_897')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_8B5',
    )

    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)

    Jump('loc_93B')

    def _loc_8B5(): pass

    label('loc_8B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_8D3',
    )

    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)

    Jump('loc_93B')

    def _loc_8D3(): pass

    label('loc_8D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_8F1',
    )

    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)

    Jump('loc_93B')

    def _loc_8F1(): pass

    label('loc_8F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_911',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 3080, 0, 67910, 0)

    Jump('loc_93B')

    def _loc_911(): pass

    label('loc_911')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_920',
    )

    ClearChrFlags(0x0022, 0x0080)

    Jump('loc_93B')

    def _loc_920(): pass

    label('loc_920')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_92A',
    )

    Jump('loc_93B')

    def _loc_92A(): pass

    label('loc_92A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_934',
    )

    Jump('loc_93B')

    def _loc_934(): pass

    label('loc_934')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_93B',
    )

    def _loc_93B(): pass

    label('loc_93B')

    Return()

# id: 0x0001 offset: 0x93C
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -138000, -78000, 196702)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_981',
    )

    OP_B1('t4103_y')

    Jump('loc_98A')

    def _loc_981(): pass

    label('loc_981')

    OP_B1('t4103_n')

    def _loc_98A(): pass

    label('loc_98A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9CC',
    )

    OP_72(0x0006, 0x0008)
    OP_72(0x0006, 0x0020)
    OP_72(0x0006, 0x0002)
    OP_6F(0x0006, 0)
    OP_72(0x0002, 0x0010)
    OP_72(0x0005, 0x0008)
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0002)
    OP_6F(0x0005, 0)
    OP_72(0x0003, 0x0010)

    def _loc_9CC(): pass

    label('loc_9CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A38',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    CreateThread(0x0008, 0x01, 0x00, 0x002E)
    CreateThread(0x0009, 0x01, 0x00, 0x002E)
    CreateThread(0x000A, 0x01, 0x00, 0x002E)
    CreateThread(0x000B, 0x01, 0x00, 0x002E)
    CreateThread(0x000C, 0x01, 0x00, 0x002E)
    CreateThread(0x000D, 0x01, 0x00, 0x002E)
    CreateThread(0x000E, 0x01, 0x00, 0x002E)
    CreateThread(0x000F, 0x01, 0x00, 0x002E)

    def _loc_A38(): pass

    label('loc_A38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_B14',
    )

    OP_72(0x0007, 0x0004)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)
    SetMapFlags(0x00000800)
    OP_1B(0x07, 0x00, 0x0002)
    OP_1B(0x06, 0x00, 0x0002)
    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -40, 250, 54930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 90, 0, 39630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 90, 250, 20100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_B14(): pass

    label('loc_B14')

    Return()

# id: 0x0002 offset: 0xB15
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x00000800)
    ClearMapFlags(0x02000000)
    OP_1B(0x07, 0x00, 0xFFFF)
    OP_1B(0x06, 0x00, 0xFFFF)

    Return()

# id: 0x0003 offset: 0xB2A
@scena.Code('func_03_B2A')
def func_03_B2A():
    ExecExpressionWithReg(
        0x0003,
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
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_C91')

    def _loc_B4F(): pass

    label('loc_B4F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B68',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_C91')

    def _loc_B68(): pass

    label('loc_B68')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B81',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_C91')

    def _loc_B81(): pass

    label('loc_B81')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B9A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_C91')

    def _loc_B9A(): pass

    label('loc_B9A')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB3',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_C91')

    def _loc_BB3(): pass

    label('loc_BB3')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BCC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_C91')

    def _loc_BCC(): pass

    label('loc_BCC')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_C91')

    def _loc_BE5(): pass

    label('loc_BE5')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_C91')

    def _loc_BFE(): pass

    label('loc_BFE')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C17',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_C91')

    def _loc_C17(): pass

    label('loc_C17')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C30',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_C91')

    def _loc_C30(): pass

    label('loc_C30')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C49',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_C91')

    def _loc_C49(): pass

    label('loc_C49')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C62',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_C91')

    def _loc_C62(): pass

    label('loc_C62')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_C91')

    def _loc_C7B(): pass

    label('loc_C7B')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C91',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_C91(): pass

    label('loc_C91')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CA6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_C91')

    def _loc_CA6(): pass

    label('loc_CA6')

    Return()

# id: 0x0004 offset: 0xCA7
@scena.Code('func_04_CA7')
def func_04_CA7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CEC',
    )

    SetChrPos(0x00FE, 31870, 0, 62980, 270)
    ChrWalkTo(0x00FE, 3180, 0, 62980, 2000, 0x00)
    ChrWalkTo(0x00FE, 3180, 0, 16590, 2000, 0x00)

    Jump('func_04_CA7')

    def _loc_CEC(): pass

    label('loc_CEC')

    Return()

# id: 0x0005 offset: 0xCED
@scena.Code('func_05_CED')
def func_05_CED():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EFD',
    )

    SetChrPos(0x00FE, -40860, 0, 28340, 0)
    ChrWalkTo(0x00FE, -40860, 0, 47840, 9000, 0x00)
    ChrWalkTo(0x00FE, -40370, 0, 50210, 9000, 0x00)
    ChrWalkTo(0x00FE, -23750, 0, 50680, 9000, 0x00)
    SetChrDirection(0x00FE, 0, 800)
    Sleep(300)

    ChrWalkTo(0x00FE, -23750, 250, 59870, 9000, 0x00)
    ChrWalkTo(0x00FE, -24760, 250, 61940, 9000, 0x00)
    SetChrDirection(0x00FE, 0, 800)
    Sleep(400)

    ChrWalkTo(0x00FE, -23750, 250, 59870, 9000, 0x00)
    ChrWalkTo(0x00FE, -23750, 0, 50680, 9000, 0x00)
    ChrWalkTo(0x00FE, -6540, 0, 50680, 9000, 0x00)
    OP_62(0x0017, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrWalkTo(0x00FE, -4900, 0, 52950, 9000, 0x00)
    ChrWalkTo(0x00FE, -4900, 0, 62070, 9000, 0x00)
    ChrWalkTo(0x00FE, -3730, 0, 64900, 9000, 0x00)
    ChrWalkTo(0x00FE, 39820, 0, 64900, 9000, 0x00)
    Sleep(2000)

    SetChrPos(0x00FE, 39650, 0, 62210, 90)
    ChrWalkTo(0x00FE, 26530, 0, 62210, 9000, 0x00)
    ChrWalkTo(0x00FE, 22200, 250, 58890, 9000, 0x00)
    ChrWalkTo(0x00FE, 10910, 250, 58890, 9000, 0x00)
    ChrWalkTo(0x00FE, 8840, 250, 56320, 9000, 0x00)
    ChrWalkTo(0x00FE, 8840, 250, 49200, 9000, 0x00)
    ChrWalkTo(0x00FE, 11240, 250, 46800, 9000, 0x00)
    ChrWalkTo(0x00FE, 16430, 250, 46800, 9000, 0x00)
    Sleep(400)

    ChrWalkTo(0x00FE, 7920, 250, 36370, 9000, 0x00)
    ChrWalkTo(0x00FE, 7920, 250, 7940, 9000, 0x00)
    Sleep(2000)

    Jump('func_05_CED')

    def _loc_EFD(): pass

    label('loc_EFD')

    Return()

# id: 0x0006 offset: 0xEFE
@scena.Code('func_06_EFE')
def func_06_EFE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F57',
    )

    SetChrPos(0x00FE, -4340, 0, 16160, 0)
    ChrWalkTo(0x00FE, -4340, 0, 48500, 2500, 0x00)
    ChrWalkTo(0x00FE, -38810, 0, 48500, 2500, 0x00)
    ChrWalkTo(0x00FE, -38810, 0, 27480, 2500, 0x00)

    Jump('func_06_EFE')

    def _loc_F57(): pass

    label('loc_F57')

    Return()

# id: 0x0007 offset: 0xF58
@scena.Code('func_07_F58')
def func_07_F58():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FE4',
    )

    ChrWalkTo(0x00FE, 6490, 0, 47450, 2500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 6490, 0, 43840, 2500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 6490, 0, 40410, 2500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 6490, 0, 43840, 2500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    Jump('func_07_F58')

    def _loc_FE4(): pass

    label('loc_FE4')

    Return()

# id: 0x0008 offset: 0xFE5
@scena.Code('func_08_FE5')
def func_08_FE5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_107B',
    )

    ChrWalkTo(0x00FE, -2950, 0, 49920, 2500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -2950, 0, 21800, 2500, 0x00)
    Sleep(2000)

    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -2950, 0, 49920, 2500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -2950, 0, 63820, 2500, 0x00)
    Sleep(2000)

    SetChrDirection(0x00FE, 90, 400)
    Sleep(2000)

    Jump('func_08_FE5')

    def _loc_107B(): pass

    label('loc_107B')

    Return()

# id: 0x0009 offset: 0x107C
@scena.Code('func_09_107C')
def func_09_107C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1182',
    )

    ChrWalkTo(0x00FE, -22900, 0, 49400, 2500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -22900, 0, 49400, 2500, 0x00)
    ChrWalkTo(0x00FE, -39450, 0, 48100, 2500, 0x00)
    ChrWalkTo(0x00FE, -39750, 0, 46660, 2500, 0x00)
    ChrWalkTo(0x00FE, -39750, 0, 38290, 2500, 0x00)
    Sleep(2000)

    ChrWalkTo(0x00FE, -39750, 0, 46660, 2500, 0x00)
    ChrWalkTo(0x00FE, -39060, 0, 49640, 2500, 0x00)
    ChrWalkTo(0x00FE, -22900, 0, 49400, 2500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, -7440, 0, 49400, 2500, 0x00)
    Sleep(2000)

    SetChrDirection(0x00FE, 0, 400)
    Sleep(2000)

    SetChrDirection(0x00FE, 180, 400)
    Sleep(2000)

    SetChrDirection(0x00FE, 90, 400)
    Sleep(2000)

    Jump('func_09_107C')

    def _loc_1182(): pass

    label('loc_1182')

    Return()

# id: 0x000A offset: 0x1183
@scena.Code('func_0A_1183')
def func_0A_1183():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11A6',
    )

    OP_8D(0x00FE, -7060, 65710, 5760, 62220, 3000)

    Jump('func_0A_1183')

    def _loc_11A6(): pass

    label('loc_11A6')

    Return()

# id: 0x000B offset: 0x11A7
@scena.Code('func_0B_11A7')
def func_0B_11A7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11E7',
    )

    ChrWalkTo(0x00FE, 4550, 0, 61060, 2800, 0x00)
    Sleep(3000)

    SetChrDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 4750, 0, 10320, 2800, 0x00)

    Jump('func_0B_11A7')

    def _loc_11E7(): pass

    label('loc_11E7')

    Return()

# id: 0x000C offset: 0x11E8
@scena.Code('func_0C_11E8')
def func_0C_11E8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 6, 0x67E)),
            Expr.Return,
        ),
        'loc_125E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0100101482V我、我是个路痴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100101483V对格兰赛尔的大街\n',
            '还不是很熟悉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101484V#010F……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13CF')

    def _loc_125E(): pass

    label('loc_125E')

    SetScenaFlags(ScenaFlag(0x00CF, 6, 0x67E))

    ChrTalk(
        0x00FE,
        (
            '#0100101485V啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101486V#001F啊，是修女艾伦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101487V#014F怎么了？\n',
            '在这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0022, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0100101488V这、这……我出来办点事情，\n',
            '结果却迷了路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101489V#010F如果可以的话，\n',
            '让我们送您回大圣堂好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100101490V啊，\n',
            '士兵刚才已经告诉我怎么走了，\n',
            '已经没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101491V#000F这样啊，那你路上小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0100101492V嗯，谢谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13CF(): pass

    label('loc_13CF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x13D3
@scena.Code('func_0D_13D3')
def func_0D_13D3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1403',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '心情好久没有这么爽快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C8')

    def _loc_1403(): pass

    label('loc_1403')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1473',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要去\n',
            '西街区的咖啡厅\n',
            '喝杯咖啡解解困呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '士兵们从早忙到晚，真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C8')

    def _loc_1473(): pass

    label('loc_1473')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_157B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_14D8',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的警戒\n',
            '怎么变得这么严了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过是闲逛了一会儿，\n',
            '就被士兵盘问了好几次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1578')

    def _loc_14D8(): pass

    label('loc_14D8')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '呼～决赛那天好热闹啊。\n',
            '昨天不知不觉就喝多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一觉睡到大天亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '街上的警戒\n',
            '怎么变得这么严了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过是闲逛了一会儿，\n',
            '就被士兵盘问了好几次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1578(): pass

    label('loc_1578')

    Jump('loc_15C8')

    def _loc_157B(): pass

    label('loc_157B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1585',
    )

    Jump('loc_15C8')

    def _loc_1585(): pass

    label('loc_1585')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_158F',
    )

    Jump('loc_15C8')

    def _loc_158F(): pass

    label('loc_158F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1599',
    )

    Jump('loc_15C8')

    def _loc_1599(): pass

    label('loc_1599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_15A3',
    )

    Jump('loc_15C8')

    def _loc_15A3(): pass

    label('loc_15A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_15AD',
    )

    Jump('loc_15C8')

    def _loc_15AD(): pass

    label('loc_15AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_15B7',
    )

    Jump('loc_15C8')

    def _loc_15B7(): pass

    label('loc_15B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_15C1',
    )

    Jump('loc_15C8')

    def _loc_15C1(): pass

    label('loc_15C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_15C8',
    )

    def _loc_15C8(): pass

    label('loc_15C8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x15CC
@scena.Code('func_0E_15CC')
def func_0E_15CC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '在武术大会里大显身手的游击士\n',
            '成功阻止了这次政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～真是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1620
@scena.Code('func_0F_1620')
def func_0F_1620():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_165B',
    )

    ChrTalk(
        0x00FE,
        (
            '不要光在街上\n',
            '站着不动，\n',
            '请到处走走看看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188A')

    def _loc_165B(): pass

    label('loc_165B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1665',
    )

    Jump('loc_188A')

    def _loc_1665(): pass

    label('loc_1665')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_16BD',
    )

    ChrTalk(
        0x00FE,
        (
            '很快就要到诞辰庆典了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前\n',
            '一定要千方百计将\n',
            '恐怖分子们抓住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188A')

    def _loc_16BD(): pass

    label('loc_16BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_16F7',
    )

    ChrTalk(
        0x00FE,
        (
            '决赛好像结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是哪一方获胜了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188A')

    def _loc_16F7(): pass

    label('loc_16F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_17CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_175C',
    )

    ChrTalk(
        0x00FE,
        (
            '我不太喜欢\n',
            '特务部队那些家伙，\n',
            '所以我决定支持你们游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要告诉别人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17CB')

    def _loc_175C(): pass

    label('loc_175C')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '今天是决赛日啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不太喜欢\n',
            '特务部队那些家伙，\n',
            '所以我决定支持你们游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要告诉别人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17CB(): pass

    label('loc_17CB')

    Jump('loc_188A')

    def _loc_17CE(): pass

    label('loc_17CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_185B',
    )

    ChrTalk(
        0x00FE,
        (
            '难得大家都沉浸在节日的气氛当中，\n',
            '给你们泼冷水真是很抱歉，\n',
            '但是上面命令我们必须加强警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须得到\n',
            '广大市民的配合才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188A')

    def _loc_185B(): pass

    label('loc_185B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1865',
    )

    Jump('loc_188A')

    def _loc_1865(): pass

    label('loc_1865')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_186F',
    )

    Jump('loc_188A')

    def _loc_186F(): pass

    label('loc_186F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1879',
    )

    Jump('loc_188A')

    def _loc_1879(): pass

    label('loc_1879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1883',
    )

    Jump('loc_188A')

    def _loc_1883(): pass

    label('loc_1883')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_188A',
    )

    def _loc_188A(): pass

    label('loc_188A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x188E
@scena.Code('func_10_188E')
def func_10_188E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_18E2',
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
            '因为警备是轮流执行的，\n',
            '所以我也要在街道上巡逻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A42')

    def _loc_18E2(): pass

    label('loc_18E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_18EC',
    )

    Jump('loc_1A42')

    def _loc_18EC(): pass

    label('loc_18EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_191F',
    )

    ChrTalk(
        0x00FE,
        (
            '如果有什么异常情况，\n',
            '请马上告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A42')

    def _loc_191F(): pass

    label('loc_191F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_197D',
    )

    ChrTalk(
        0x00FE,
        (
            '据说亲卫队是恐怖分子，\n',
            '这是真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '悄悄告诉你们，\n',
            '我也不相信这件事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A42')

    def _loc_197D(): pass

    label('loc_197D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_19DA',
    )

    ChrTalk(
        0x00FE,
        (
            '就算找到了亲卫队，\n',
            '一旦动手我们也未必有胜算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他们的强大是出了名的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A42')

    def _loc_19DA(): pass

    label('loc_19DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1A13',
    )

    ChrTalk(
        0x00FE,
        (
            '如果看见有像亲卫队的人，\n',
            '请马上过来报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A42')

    def _loc_1A13(): pass

    label('loc_1A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1A1D',
    )

    Jump('loc_1A42')

    def _loc_1A1D(): pass

    label('loc_1A1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1A27',
    )

    Jump('loc_1A42')

    def _loc_1A27(): pass

    label('loc_1A27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1A31',
    )

    Jump('loc_1A42')

    def _loc_1A31(): pass

    label('loc_1A31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A3B',
    )

    Jump('loc_1A42')

    def _loc_1A3B(): pass

    label('loc_1A3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1A42',
    )

    def _loc_1A42(): pass

    label('loc_1A42')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1A46
@scena.Code('func_11_1A46')
def func_11_1A46():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1ABE',
    )

    ChrTalk(
        0x00FE,
        (
            '结果，\n',
            '亲卫队的队员言而有信地\n',
            '成功守护了女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……他们是王国军的榜样，\n',
            '再次向他们表示敬意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1ABE(): pass

    label('loc_1ABE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1AC8',
    )

    Jump('loc_1C1E')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1B61',
    )

    ChrTalk(
        0x00FE,
        (
            '就算到现在我还是无法相信\n',
            '亲卫队的人就是恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为他们在军队中位置特殊，\n',
            '所以才会惹来那么多非议吧，\n',
            '但我还是觉得他们很厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1B61(): pass

    label('loc_1B61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1BA2',
    )

    ChrTalk(
        0x00FE,
        (
            '这里没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '差不多该是换班的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1BA2(): pass

    label('loc_1BA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1BC6',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉，我们现在很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1BC6(): pass

    label('loc_1BC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1BEF',
    )

    ChrTalk(
        0x00FE,
        (
            '很抱歉，\n',
            '请不要妨碍巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C1E')

    def _loc_1BEF(): pass

    label('loc_1BEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1BF9',
    )

    Jump('loc_1C1E')

    def _loc_1BF9(): pass

    label('loc_1BF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1C03',
    )

    Jump('loc_1C1E')

    def _loc_1C03(): pass

    label('loc_1C03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1C0D',
    )

    Jump('loc_1C1E')

    def _loc_1C0D(): pass

    label('loc_1C0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1C17',
    )

    Jump('loc_1C1E')

    def _loc_1C17(): pass

    label('loc_1C17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1C1E',
    )

    def _loc_1C1E(): pass

    label('loc_1C1E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1C22
@scena.Code('func_12_1C22')
def func_12_1C22():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1C87',
    )

    ChrTalk(
        0x00FE,
        (
            '那位理查德上校\n',
            '是政变的策划人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不敢相信更加不愿去相信，\n',
            '我真的很尊敬他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DDA')

    def _loc_1C87(): pass

    label('loc_1C87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1C91',
    )

    Jump('loc_1DDA')

    def _loc_1C91(): pass

    label('loc_1C91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1CDE',
    )

    ChrTalk(
        0x00FE,
        (
            '不要妨碍警备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果让恐怖分子\n',
            '混入诞辰庆典就不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DDA')

    def _loc_1CDE(): pass

    label('loc_1CDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1D25',
    )

    ChrTalk(
        0x00FE,
        (
            '那个特务部队\n',
            '在决赛中竟然输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士干得不赖呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DDA')

    def _loc_1D25(): pass

    label('loc_1D25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1D6E',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真是个很厉害的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也是这么认为的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DDA')

    def _loc_1D6E(): pass

    label('loc_1D6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1DAB',
    )

    ChrTalk(
        0x00FE,
        (
            '如果干了什么可疑的事，\n',
            '就算是游击士也要逮捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DDA')

    def _loc_1DAB(): pass

    label('loc_1DAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1DB5',
    )

    Jump('loc_1DDA')

    def _loc_1DB5(): pass

    label('loc_1DB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1DBF',
    )

    Jump('loc_1DDA')

    def _loc_1DBF(): pass

    label('loc_1DBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1DC9',
    )

    Jump('loc_1DDA')

    def _loc_1DC9(): pass

    label('loc_1DC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1DD3',
    )

    Jump('loc_1DDA')

    def _loc_1DD3(): pass

    label('loc_1DD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1DDA',
    )

    def _loc_1DDA(): pass

    label('loc_1DDA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1DDE
@scena.Code('func_13_1DDE')
def func_13_1DDE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '这边的情况没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x1E04
@scena.Code('func_14_1E04')
def func_14_1E04():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '让开让开！\n',
            '别妨碍执行公务！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x1E2C
@scena.Code('func_15_1E2C')
def func_15_1E2C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '王都的守卫\n',
            '现在由我们特务兵来担当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也好，如果原来那些家伙还在，\n',
            '只会拖我们后腿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x1E8F
@scena.Code('func_16_1E8F')
def func_16_1E8F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1EF8',
    )

    ChrTalk(
        0x00FE,
        (
            '终于看到好久不见的\n',
            '女王陛下的身影了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来所有的担心和顾虑\n',
            '就都一扫而空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_1EF8(): pass

    label('loc_1EF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1F66',
    )

    ChrTalk(
        0x00FE,
        (
            '平常的那些士兵们\n',
            '都匆匆忙忙地撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '守卫王城的人\n',
            '变成了黑衣士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有些不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_1F66(): pass

    label('loc_1F66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2090',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1FE0',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会结束了，\n',
            '离女王陛下的生日\n',
            '也已经没有几天了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可还是得不到关于\n',
            '陛下病情的详细情况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208D')

    def _loc_1FE0(): pass

    label('loc_1FE0')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '武术大会结束了，\n',
            '离女王陛下的生日已经很近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我们还是不知道\n',
            '陛下病情的详细情况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，本来让那个杜南公爵\n',
            '担任女王陛下的代理\n',
            '我就觉得很不可思议了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_208D(): pass

    label('loc_208D')

    Jump('loc_25AA')

    def _loc_2090(): pass

    label('loc_2090')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_20BD',
    )

    ChrTalk(
        0x00FE,
        (
            '已经到傍晚了。\n',
            '要快点回家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_20BD(): pass

    label('loc_20BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_210B',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会\n',
            '今天到了决赛日啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少今天\n',
            '还是要去现场看看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_210B(): pass

    label('loc_210B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2161',
    )

    ChrTalk(
        0x00FE,
        (
            '常常可以看见\n',
            '穿黑衣服的士兵\n',
            '在王城中出入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们到底是什么人啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_2161(): pass

    label('loc_2161')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_226B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_21CE',
    )

    ChrTalk(
        0x00FE,
        (
            '王城的城门前面\n',
            '不是有个很大的广场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典当天可以从那里\n',
            '一睹女王陛下的风采。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2268')

    def _loc_21CE(): pass

    label('loc_21CE')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '王城的城门前面\n',
            '不是有个很大的广场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典当天可以从那里\n',
            '一睹女王陛下的风采。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，照现在这样下去的话，\n',
            '今年的诞辰庆典会怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2268(): pass

    label('loc_2268')

    Jump('loc_25AA')

    def _loc_226B(): pass

    label('loc_226B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_23CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2313',
    )

    ChrTalk(
        0x00FE,
        (
            '站在王城的空中庭园，\n',
            '从瓦雷利亚湖吹面而来的清爽凉风\n',
            '和空中庭园里植被的清香让人神清气爽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在不能进去了，\n',
            '不过无论如何我还是要推荐一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CB')

    def _loc_2313(): pass

    label('loc_2313')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '以前是可以到王城的空中庭园\n',
            '去进行参观游览的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从瓦雷利亚湖吹面而来的清爽凉风\n',
            '和空中庭园里植被的清香让人神清气爽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在不能进去了，\n',
            '不过无论如何我还是要推荐一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23CB(): pass

    label('loc_23CB')

    Jump('loc_25AA')

    def _loc_23CE(): pass

    label('loc_23CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2445',
    )

    ChrTalk(
        0x00FE,
        (
            '不久前还是\n',
            '只要通过申请\n',
            '就可以进王城参观的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是因为女王陛下身体欠佳，\n',
            '所以参观的事情基本无望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AA')

    def _loc_2445(): pass

    label('loc_2445')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2536',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_248E',
    )

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王\n',
            '是利贝尔的骄傲，\n',
            '而杜南公爵则是耻辱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2533')

    def _loc_248E(): pass

    label('loc_248E')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '之前，\n',
            '那个杜南公爵又在城门外耍无赖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，就算是女王陛下身体欠佳，\n',
            '也不该找那种代理人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王\n',
            '是利贝尔的骄傲，\n',
            '而杜南公爵则是耻辱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2533(): pass

    label('loc_2533')

    Jump('loc_25AA')

    def _loc_2536(): pass

    label('loc_2536')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_25AA',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会虽然开始了，\n',
            '但这周围的观光客好像\n',
            '比平时还要少了一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是因为王城\n',
            '禁止对外开放的缘故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25AA(): pass

    label('loc_25AA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x25AE
@scena.Code('func_17_25AE')
def func_17_25AE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2609',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典并不意味着\n',
            '是邮递员的休息日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反而是服务行业\n',
            '最忙的时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_2609(): pass

    label('loc_2609')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_266B',
    )

    ChrTalk(
        0x00FE,
        (
            '空港被军队给封锁了，\n',
            '已经不能进入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等这个货物邮递完毕后\n',
            '就没有其他任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_266B(): pass

    label('loc_266B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_26AE',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '空港来了好多士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底发生了什么事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_26AE(): pass

    label('loc_26AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2707',
    )

    ChrTalk(
        0x00FE,
        (
            '下次的《利贝尔通讯》\n',
            '好像会出武术大会特辑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从现在开始就很期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_2707(): pass

    label('loc_2707')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2777',
    )

    ChrTalk(
        0x00FE,
        (
            '最近王都大大小小的角落\n',
            '都有一大群士兵在巡逻，\n',
            '搞得我工作也不顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是一群给人添麻烦的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_2777(): pass

    label('loc_2777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_27BD',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，下面要把东西送到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经傍晚了，必须快点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_27BD(): pass

    label('loc_27BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2800',
    )

    ChrTalk(
        0x00FE,
        (
            '那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将这些货物送完之后，\n',
            '就回空港休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_2800(): pass

    label('loc_2800')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_284F',
    )

    ChrTalk(
        0x00FE,
        (
            '有时候收信人的地址\n',
            '写得不工整导致看不清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很麻烦呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_284F(): pass

    label('loc_284F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_28C5',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，如果不是因为工作的话，\n',
            '我肯定已经去观看武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '邮递员的工作很多，\n',
            '哪有什么休息的时间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_28C5(): pass

    label('loc_28C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_294A',
    )

    ChrTalk(
        0x00FE,
        (
            '我回空港去取邮寄的物品时，\n',
            '却发现王家飞艇『埃尔赛尤号』\n',
            '被士兵给包围了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟发生了什么事……\n',
            '感觉不是很太平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_294A(): pass

    label('loc_294A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_29B0',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，接下来要送的东西是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，王都实在是太大了，\n',
            '对于我们这些邮递员来说真是灾难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29B0(): pass

    label('loc_29B0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x29B4
@scena.Code('func_18_29B4')
def func_18_29B4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2AB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2A1B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然接下来会很辛苦，\n',
            '但是现在卡西乌斯上校回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我们就一定要努力了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB1')

    def _loc_2A1B(): pass

    label('loc_2A1B')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀～～～\n',
            '跟预想的一样，\n',
            '我被安排了像山一样多的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然接下来会很辛苦，\n',
            '但是现在卡西乌斯上校回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我们就一定要努力了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AB1(): pass

    label('loc_2AB1')

    Jump('loc_32B2')

    def _loc_2AB4(): pass

    label('loc_2AB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2B3C',
    )

    ChrTalk(
        0x00FE,
        (
            '没有任何公告的情况下\n',
            '王都守卫队突然撤离，\n',
            '特务部队却出现了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么想，\n',
            '都觉得是王城里\n',
            '发生了什么可怕的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B2')

    def _loc_2B3C(): pass

    label('loc_2B3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2BA4',
    )

    ChrTalk(
        0x00FE,
        (
            '总觉得最近在街上\n',
            '老是能看到特务兵的身影……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即便如此，\n',
            '还是没能抓到亲卫队的那些人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B2')

    def _loc_2BA4(): pass

    label('loc_2BA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2CCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2C27',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙们\n',
            '经常用很蛮横的态度\n',
            '来打听情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '同样是为利贝尔王国\n',
            '服务的工作人员，\n',
            '他们对我们很不友好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CCB')

    def _loc_2C27(): pass

    label('loc_2C27')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙们\n',
            '经常用很蛮横的态度\n',
            '来打听情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '同样是为利贝尔王国\n',
            '服务的工作人员，\n',
            '他们对我们很不友好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是凯诺娜上尉，\n',
            '对她抱反感的人有不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CCB(): pass

    label('loc_2CCB')

    Jump('loc_32B2')

    def _loc_2CCE(): pass

    label('loc_2CCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2E03',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2D45',
    )

    ChrTalk(
        0x00FE,
        (
            '传说中的『埃尔赛尤号』\n',
            '也被军队接管起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是那个理查德上校，\n',
            '这样做也会让人不愉快的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E00')

    def _loc_2D45(): pass

    label('loc_2D45')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '传说中的『埃尔赛尤号』\n',
            '也被军队接管起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然那艘飞艇的成员\n',
            '和亲卫队的人有交往，\n',
            '不过不管怎么说，那可是王家的飞艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是那个理查德上校，\n',
            '这样做也会让人不愉快的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E00(): pass

    label('loc_2E00')

    Jump('loc_32B2')

    def _loc_2E03(): pass

    label('loc_2E03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2F23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2E82',
    )

    ChrTalk(
        0x00FE,
        (
            '就算是理查德上校，\n',
            '搜捕起亲卫队来\n',
            '也着实非常的辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部初来乍到，\n',
            '一时间很难得到\n',
            '市民们的配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F20')

    def _loc_2E82(): pass

    label('loc_2E82')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '就算是理查德上校，\n',
            '搜捕起亲卫队来\n',
            '也着实非常的辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为亲卫队一直都\n',
            '相当受王都市民的欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部初来乍到，\n',
            '一时间很难得到\n',
            '市民们的配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F20(): pass

    label('loc_2F20')

    Jump('loc_32B2')

    def _loc_2F23(): pass

    label('loc_2F23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3018',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2F64',
    )

    ChrTalk(
        0x00FE,
        (
            '我们文官当中\n',
            '好像也有很多人\n',
            '同情亲卫队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3015')

    def _loc_2F64(): pass

    label('loc_2F64')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '我们文官当中\n',
            '好像也有很多人\n',
            '同情亲卫队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怖事件发生的时候，\n',
            '他们应该在艾尔贝离宫那边\n',
            '进行演习吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他们有不在场证明，\n',
            '但没想到陛下\n',
            '还是下了逮捕令呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3015(): pass

    label('loc_3015')

    Jump('loc_32B2')

    def _loc_3018(): pass

    label('loc_3018')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_313A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3098',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，我在休假的时候\n',
            '还看到情报部的士兵\n',
            '押送着亲卫队的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤莉亚·舒华兹中尉\n',
            '现在到底怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3137')

    def _loc_3098(): pass

    label('loc_3098')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '对了，我在休假的时候\n',
            '还看到情报部的士兵\n',
            '押送着亲卫队的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是把王城剩下的\n',
            '亲卫队成员都逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤莉亚·舒华兹中尉\n',
            '现在到底怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3137(): pass

    label('loc_3137')

    Jump('loc_32B2')

    def _loc_313A(): pass

    label('loc_313A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_319C',
    )

    ChrTalk(
        0x00FE,
        (
            '突然间可以休假了，\n',
            '还真是有些不太习惯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于王城的公务\n',
            '反而有些放心不下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B2')

    def _loc_319C(): pass

    label('loc_319C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3217',
    )

    ChrTalk(
        0x00FE,
        (
            '最近一段时间，\n',
            '理查德上校时常在王城出入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身体欠佳的女王陛下\n',
            '一定很信任他，\n',
            '才把他从要塞那里叫了回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32B2')

    def _loc_3217(): pass

    label('loc_3217')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_32B2',
    )

    ChrTalk(
        0x00FE,
        (
            '我本来是在王城里工作的，\n',
            '几天前，代替女王行使政权的公爵\n',
            '突然宣布让我们休假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是因为女王陛下身体欠佳\n',
            '而暂时不进行政务，\n',
            '休息一段时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32B2(): pass

    label('loc_32B2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x32B6
@scena.Code('func_19_32B6')
def func_19_32B6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_32EA',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '接下来就开始点名吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_334B')

    def _loc_32EA(): pass

    label('loc_32EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_32F4',
    )

    Jump('loc_334B')

    def _loc_32F4(): pass

    label('loc_32F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_32FE',
    )

    Jump('loc_334B')

    def _loc_32FE(): pass

    label('loc_32FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3308',
    )

    Jump('loc_334B')

    def _loc_3308(): pass

    label('loc_3308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3312',
    )

    Jump('loc_334B')

    def _loc_3312(): pass

    label('loc_3312')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_331C',
    )

    Jump('loc_334B')

    def _loc_331C(): pass

    label('loc_331C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3326',
    )

    Jump('loc_334B')

    def _loc_3326(): pass

    label('loc_3326')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3330',
    )

    Jump('loc_334B')

    def _loc_3330(): pass

    label('loc_3330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_333A',
    )

    Jump('loc_334B')

    def _loc_333A(): pass

    label('loc_333A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3344',
    )

    Jump('loc_334B')

    def _loc_3344(): pass

    label('loc_3344')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_334B',
    )

    def _loc_334B(): pass

    label('loc_334B')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x334F
@scena.Code('func_1A_334F')
def func_1A_334F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3392',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我的老公又是状态极佳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是没办法啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33F3')

    def _loc_3392(): pass

    label('loc_3392')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_339C',
    )

    Jump('loc_33F3')

    def _loc_339C(): pass

    label('loc_339C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_33A6',
    )

    Jump('loc_33F3')

    def _loc_33A6(): pass

    label('loc_33A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_33B0',
    )

    Jump('loc_33F3')

    def _loc_33B0(): pass

    label('loc_33B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_33BA',
    )

    Jump('loc_33F3')

    def _loc_33BA(): pass

    label('loc_33BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_33C4',
    )

    Jump('loc_33F3')

    def _loc_33C4(): pass

    label('loc_33C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_33CE',
    )

    Jump('loc_33F3')

    def _loc_33CE(): pass

    label('loc_33CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_33D8',
    )

    Jump('loc_33F3')

    def _loc_33D8(): pass

    label('loc_33D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_33E2',
    )

    Jump('loc_33F3')

    def _loc_33E2(): pass

    label('loc_33E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_33EC',
    )

    Jump('loc_33F3')

    def _loc_33EC(): pass

    label('loc_33EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_33F3',
    )

    def _loc_33F3(): pass

    label('loc_33F3')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x33F7
@scena.Code('func_1B_33F7')
def func_1B_33F7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3437',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '爸爸他究竟要点过多少次名才罢休嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3498')

    def _loc_3437(): pass

    label('loc_3437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3441',
    )

    Jump('loc_3498')

    def _loc_3441(): pass

    label('loc_3441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_344B',
    )

    Jump('loc_3498')

    def _loc_344B(): pass

    label('loc_344B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3455',
    )

    Jump('loc_3498')

    def _loc_3455(): pass

    label('loc_3455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_345F',
    )

    Jump('loc_3498')

    def _loc_345F(): pass

    label('loc_345F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3469',
    )

    Jump('loc_3498')

    def _loc_3469(): pass

    label('loc_3469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3473',
    )

    Jump('loc_3498')

    def _loc_3473(): pass

    label('loc_3473')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_347D',
    )

    Jump('loc_3498')

    def _loc_347D(): pass

    label('loc_347D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3487',
    )

    Jump('loc_3498')

    def _loc_3487(): pass

    label('loc_3487')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3491',
    )

    Jump('loc_3498')

    def _loc_3491(): pass

    label('loc_3491')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3498',
    )

    def _loc_3498(): pass

    label('loc_3498')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x349C
@scena.Code('func_1C_349C')
def func_1C_349C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_34C7',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀～好想进城去看看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3527')

    def _loc_34C7(): pass

    label('loc_34C7')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x00FE,
        (
            '咦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里就是格兰赛尔城吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………咦～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们约好\n',
            '在哪里见面呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3527(): pass

    label('loc_3527')

    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x352B
@scena.Code('func_1D_352B')
def func_1D_352B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_35D8',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才本打算在这里求婚的，\n',
            '这时，城门突然打开了，\n',
            '然后亲卫队和游击士冲了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我以为是来阻止我求婚的，\n',
            '吓了我一大跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果我还是\n',
            '没能向她求成婚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36DD')

    def _loc_35D8(): pass

    label('loc_35D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_362D',
    )

    ChrTalk(
        0x00FE,
        (
            '艾娅莉，请听我说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天对于我们俩来说，\n',
            '是个特别有意义的日子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36DD')

    def _loc_362D(): pass

    label('loc_362D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3690',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说转遍了\n',
            '街上的各个地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但能够最好表达\n',
            '感情的地方果然\n',
            '还是王城前面啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36DD')

    def _loc_3690(): pass

    label('loc_3690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_369A',
    )

    Jump('loc_36DD')

    def _loc_369A(): pass

    label('loc_369A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_36A4',
    )

    Jump('loc_36DD')

    def _loc_36A4(): pass

    label('loc_36A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_36AE',
    )

    Jump('loc_36DD')

    def _loc_36AE(): pass

    label('loc_36AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_36B8',
    )

    Jump('loc_36DD')

    def _loc_36B8(): pass

    label('loc_36B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_36C2',
    )

    Jump('loc_36DD')

    def _loc_36C2(): pass

    label('loc_36C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_36CC',
    )

    Jump('loc_36DD')

    def _loc_36CC(): pass

    label('loc_36CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_36D6',
    )

    Jump('loc_36DD')

    def _loc_36D6(): pass

    label('loc_36D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_36DD',
    )

    def _loc_36DD(): pass

    label('loc_36DD')

    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x36E1
@scena.Code('func_1E_36E1')
def func_1E_36E1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_37AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_374B',
    )

    ChrTalk(
        0x00FE,
        (
            '没有想到会\n',
            '遇到这样的麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我们俩这趟旅程的\n',
            '最高潮从现在才开始哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37A8')

    def _loc_374B(): pass

    label('loc_374B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '女王陛下和公主殿下，\n',
            '她们都好有气质啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候的骚乱\n',
            '原来是件不得了的大事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37A8(): pass

    label('loc_37A8')

    Jump('loc_393D')

    def _loc_37AB(): pass

    label('loc_37AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_380F',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，阿鲁姆……\n',
            '这一刻终于到来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我那强烈的心跳声……\n',
            '被他听到了该怎么办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_393D')

    def _loc_380F(): pass

    label('loc_380F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_38F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3875',
    )

    ChrTalk(
        0x00FE,
        (
            '今天他好像\n',
            '在想什么事情，\n',
            '可又不告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，太坏了。\n',
            '我可要撒娇了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38ED')

    def _loc_3875(): pass

    label('loc_3875')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵，他呀，\n',
            '今天总是在自言自语。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像在想什么事情，\n',
            '可又不告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，太坏了。\n',
            '我可要撒娇了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38ED(): pass

    label('loc_38ED')

    Jump('loc_393D')

    def _loc_38F0(): pass

    label('loc_38F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_38FA',
    )

    Jump('loc_393D')

    def _loc_38FA(): pass

    label('loc_38FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3904',
    )

    Jump('loc_393D')

    def _loc_3904(): pass

    label('loc_3904')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_390E',
    )

    Jump('loc_393D')

    def _loc_390E(): pass

    label('loc_390E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3918',
    )

    Jump('loc_393D')

    def _loc_3918(): pass

    label('loc_3918')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3922',
    )

    Jump('loc_393D')

    def _loc_3922(): pass

    label('loc_3922')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_392C',
    )

    Jump('loc_393D')

    def _loc_392C(): pass

    label('loc_392C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3936',
    )

    Jump('loc_393D')

    def _loc_3936(): pass

    label('loc_3936')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_393D',
    )

    def _loc_393D(): pass

    label('loc_393D')

    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x3941
@scena.Code('func_1F_3941')
def func_1F_3941():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我的钱包应该不会被偷去的，\n',
            '因为我把它放在腰包里面了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀？\n',
            '怎么不见了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x39A2
@scena.Code('func_20_39A2')
def func_20_39A2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '爸爸，我要喝果汁嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x39C3
@scena.Code('func_21_39C3')
def func_21_39C3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '对呀对呀，就在那边的拐角……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看到了一个和科洛蒂娅公主\n',
            '长得很相似的女孩哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道真的是她本人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x3A3B
@scena.Code('func_22_3A3B')
def func_22_3A3B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，夫人真是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公主殿下刚才\n',
            '还在王城的阳台上面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果说是换了着装到外面来，\n',
            '是不是也太快了一点呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x3ABA
@scena.Code('func_23_3ABA')
def func_23_3ABA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '是呀，肯定是看错了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且从那里走过的女孩\n',
            '穿的还是学校的校服呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x3B0E
@scena.Code('func_24_3B0E')
def func_24_3B0E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '果然如此，\n',
            '既壮丽又富有历史气息，\n',
            '这些街道真是两者兼备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且给人以安定的感觉……\n',
            '果然和共和国的城市不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x3B8E
@scena.Code('func_25_3B8E')
def func_25_3B8E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊，又来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是因为这样，\n',
            '所以我讨厌和爸爸一起来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x3BDA
@scena.Code('func_26_3BDA')
def func_26_3BDA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '准～备，咔嚓！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我们不打算在这里住宿，\n',
            '所以要趁现在多照一些照片作为纪念才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x3C3C
@scena.Code('func_27_3C3C')
def func_27_3C3C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我的女儿女婿为了给我们庆祝六十大寿，\n',
            '特地用王都旅行作为祝寿的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然是她俩的好意，我们就来了，\n',
            '正好也碰上女王陛下的诞辰庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，哪怕只有一次机会，\n',
            '能来王都游览一下也很不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x3D0A
@scena.Code('func_28_3D0A')
def func_28_3D0A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，我说老伴儿啊，\n',
            '就在这个旅馆里面住下如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是异常华丽的建筑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x3D62
@scena.Code('func_29_3D62')
def func_29_3D62():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '好不容易来王都一趟，\n',
            '一定要到处去逛逛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x3D9B
@scena.Code('func_2A_3D9B')
def func_2A_3D9B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '这附近是什么地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有地图所以迷路了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0x3DDF
@scena.Code('func_2B_3DDF')
def func_2B_3DDF():
    EventBegin(0x00)
    CameraMove(2190, 0, 46270, 0)
    OP_67(0, 29260, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_12(0x00009C40, 0x0003D090, 0x00000000)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_3E43')
    def lambda_3E43():
        OP_6C(90000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E43)

    Sleep(1000)

    @scena.Lambda('lambda_3E58')
    def lambda_3E58():
        CameraMove(10350, 3620, 43920, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E58)

    @scena.Lambda('lambda_3E70')
    def lambda_3E70():
        OP_67(0, 3740, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3E70)

    OP_12(0x00009C40, 0x000249F0, 0x00002710)
    Sleep(10000)

    ClearMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002C offset: 0x3EA6
@scena.Code('func_2C_3EA6')
def func_2C_3EA6():
    Return()

# id: 0x002D offset: 0x3EA7
@scena.Code('func_2D_3EA7')
def func_2D_3EA7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F03',
    )

    ChrWalkTo(0x00FE, 3800, 0, 40510, 3000, 0x00)
    ChrWalkTo(0x00FE, -2970, 0, 40510, 3000, 0x00)
    ChrWalkTo(0x00FE, -2970, 0, 65560, 3000, 0x00)
    ChrWalkTo(0x00FE, 3800, 0, 65780, 3000, 0x00)

    Jump('func_2D_3EA7')

    def _loc_3F03(): pass

    label('loc_3F03')

    Return()

# id: 0x002E offset: 0x3F04
@scena.Code('func_2E_3F04')
def func_2E_3F04():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4153',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3F37',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_3F37(): pass

    label('loc_3F37')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3F5D',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_3F5D(): pass

    label('loc_3F5D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3F83',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_3F83(): pass

    label('loc_3F83')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3FAA',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_3FAA(): pass

    label('loc_3FAA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3FD0',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_3FD0(): pass

    label('loc_3FD0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3FF6',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_3FF6(): pass

    label('loc_3FF6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_401B',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_401B(): pass

    label('loc_401B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4040',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4054')

    def _loc_4040(): pass

    label('loc_4040')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4054(): pass

    label('loc_4054')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xDAC),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xDAC),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xDAC),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xDAC),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4150',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    OP_69(0x00FE, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4141',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（糟了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（被发现了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4141(): pass

    label('loc_4141')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_4150(): pass

    label('loc_4150')

    Jump('func_2E_3F04')

    def _loc_4153(): pass

    label('loc_4153')

    Return()

# id: 0x002F offset: 0x4154
@scena.Code('func_2F_4154')
def func_2F_4154():
    EventBegin(0x00)
    CameraMove(17700, 510, 43970, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6E(262, 0)
    OP_6C(90000, 0)
    SetChrPos(0x0101, 17540, 510, 44210, 270)
    SetChrPos(0x0102, 17540, 510, 43360, 270)

    ChrTalk(
        0x0101,
        (
            '#000F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_41CE')
    def lambda_41CE():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_41CE)

    CameraMove(4010, 0, 38720, 3000)
    SetChrPos(0x0101, 13280, 250, 49870, 225)
    SetChrPos(0x0102, 14070, 250, 49980, 225)
    Sleep(1000)

    CameraMove(13610, 250, 50130, 3000)

    ChrTalk(
        0x0102,
        (
            '#010F（已经在巡逻了呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（我们要想办法不被他们发现，\n',
            '　然后找一条安全的路线到达大圣堂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（嗯，我知道了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0030 offset: 0x42A5
@scena.Code('func_30_42A5')
def func_30_42A5():
    OP_13(0x00B4)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
