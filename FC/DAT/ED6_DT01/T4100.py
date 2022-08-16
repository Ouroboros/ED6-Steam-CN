import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
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
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00001450,
            dword_04        = 0x00000000,
            dword_08        = 0x000003E8,
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
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
    ]

# id: 0x10001 offset: 0x1CA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奥利维尔',
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
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
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0036,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0037,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0038,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0039,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x003A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x003B,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
            x                   = 4500,
            z                   = 0,
            y                   = -63100,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '比尔爷爷',
            x                   = 7810,
            z                   = 0,
            y                   = -1510,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '伊鲁妮婆婆',
            x                   = 7800,
            z                   = 0,
            y                   = -530,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '嘉瑟',
            x                   = -5720,
            z                   = 0,
            y                   = -36280,
            direction           = 281,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '芬尼尔',
            x                   = -5830,
            z                   = 0,
            y                   = -55640,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '诺娜',
            x                   = 5550,
            z                   = 0,
            y                   = -54380,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '阿鲁姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '艾娅莉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '蒂库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '拉尔斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '托伊',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '伯登',
            x                   = 5760,
            z                   = 0,
            y                   = -46060,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '拉塔娜',
            x                   = -2070,
            z                   = 0,
            y                   = -5120,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '托朗老人',
            x                   = 3520,
            z                   = 0,
            y                   = 10640,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 6280,
            z                   = 0,
            y                   = 2180,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -6430,
            z                   = 0,
            y                   = -22020,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 4760,
            z                   = 0,
            y                   = -39600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -4540,
            z                   = 0,
            y                   = -29870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 6280,
            z                   = 0,
            y                   = 2180,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 4760,
            z                   = 0,
            y                   = -39600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = -4540,
            z                   = 0,
            y                   = -29870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -6250,
            z                   = 0,
            y                   = -870,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -6250,
            z                   = 0,
            y                   = -1920,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -8540,
            z                   = 250,
            y                   = 6040,
            direction           = 172,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -8540,
            z                   = 250,
            y                   = 4630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -5690,
            z                   = 0,
            y                   = -7580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 13060,
            z                   = 250,
            y                   = 4130,
            direction           = 51,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 7390,
            z                   = 250,
            y                   = -15350,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 7390,
            z                   = 250,
            y                   = -17380,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = '米拉诺',
            x                   = -7510,
            z                   = 250,
            y                   = -16200,
            direction           = 99,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = '西蒙',
            x                   = -8330,
            z                   = 250,
            y                   = -14940,
            direction           = 138,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 8300,
            z                   = 250,
            y                   = 3500,
            direction           = 170,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 7330,
            z                   = 250,
            y                   = -27330,
            direction           = 37,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -7120,
            z                   = 250,
            y                   = -30460,
            direction           = 102,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 7170,
            z                   = 250,
            y                   = -10430,
            direction           = 272,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = -80,
            z                   = 0,
            y                   = -49760,
            direction           = 160,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = -990,
            z                   = 0,
            y                   = -50700,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002D,
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

# id: 0x10002 offset: 0x80A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x80A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 5270,
            y           = -1000,
            z           = -67700,
            range       = -6090,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF0182,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000047,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -25000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000049,
        ),
        ScenaEventData(
            x           = -10280,
            y           = 0,
            z           = -11040,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004A,
        ),
        ScenaEventData(
            x           = -14940,
            y           = 0,
            z           = -15750,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004A,
        ),
        ScenaEventData(
            x           = -10290,
            y           = 0,
            z           = -30020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004B,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -13010,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004C,
        ),
        ScenaEventData(
            x           = 15900,
            y           = 0,
            z           = 6330,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004D,
        ),
    )

# id: 0x10004 offset: 0x8EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x8EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_8FD',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_31_6281)

    def _loc_8FD(): pass

    label('loc_8FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_90E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    OP_26(125)
    Event(0, func_33_6BB0)

    def _loc_90E(): pass

    label('loc_90E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_91C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_3C_7718)

    def _loc_91C(): pass

    label('loc_91C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_92F',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_3D_7A8E)

    def _loc_92F(): pass

    label('loc_92F')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_93F'),
        (0x00000067, 'loc_955'),
        (-1, 'loc_96B'),
    )

    def _loc_93F(): pass

    label('loc_93F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 7, 0x607)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_952',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 0, 0x608))
    Event(0, func_2F_5760)

    def _loc_952(): pass

    label('loc_952')

    Jump('loc_96B')

    def _loc_955(): pass

    label('loc_955')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_968',
    )

    SetScenaFlags(ScenaFlag(0x00C5, 1, 0x629))
    Event(0, func_34_6DE5)

    def _loc_968(): pass

    label('loc_968')

    Jump('loc_96B')

    def _loc_96B(): pass

    label('loc_96B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_A25',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -4270, 0, -46090, 273)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -5960, 0, -47010, 44)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -5960, 0, -45200, 140)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0033, 0x0080)

    Jump('loc_E18')

    def _loc_A25(): pass

    label('loc_A25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_A80',
    )

    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)

    Jump('loc_E18')

    def _loc_A80(): pass

    label('loc_A80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_AE0',
    )

    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)

    Jump('loc_E18')

    def _loc_AE0(): pass

    label('loc_AE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_B6C',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -3830, 0, -46790, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -3810, 0, -44860, 180)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)

    Jump('loc_E18')

    def _loc_B6C(): pass

    label('loc_B6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_B8A',
    )

    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)

    Jump('loc_E18')

    def _loc_B8A(): pass

    label('loc_B8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_BFB',
    )

    ChrSetPos(0x0014, -5720, 0, -37010, 257)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)

    Jump('loc_E18')

    def _loc_BFB(): pass

    label('loc_BFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_C31',
    )

    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 270)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 90)

    Jump('loc_E18')

    def _loc_C31(): pass

    label('loc_C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_CA9',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, 5340, 0, -37270, 84)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, 5410, 0, -37950, 90)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)

    Jump('loc_E18')

    def _loc_CA9(): pass

    label('loc_CA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_D2B',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, 5340, 0, -37270, 84)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, 5410, 0, -37950, 90)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 270)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 90)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -5300, 0, -38930, 315)
    ChrSetFlags(0x001B, 0x0010)

    Jump('loc_E18')

    def _loc_D2B(): pass

    label('loc_D2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_DA3',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -3830, 0, -46790, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -3810, 0, -44860, 180)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)

    Jump('loc_E18')

    def _loc_DA3(): pass

    label('loc_DA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_E18',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -3830, 0, -46790, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -3810, 0, -44860, 180)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, 1120, 0, -52220, 315)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -1040, 0, -52280, 45)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, 10, 0, -50410, 180)

    def _loc_E18(): pass

    label('loc_E18')

    Return()

# id: 0x0001 offset: 0xE19
@scena.Code('func_01_E19')
def func_01_E19():
    OP_16(0x02, 4000, -128000, -148000, 196699)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 1, 0x611)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E3C',
    )

    OP_1C(0x10, 0x00, 0x0030)

    def _loc_E3C(): pass

    label('loc_E3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E50',
    )

    OP_1B(0x03, 0x00, 0x002E)

    Jump('loc_E73')

    def _loc_E50(): pass

    label('loc_E50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_E63',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_E73')

    def _loc_E63(): pass

    label('loc_E63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_E73',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E73(): pass

    label('loc_E73')

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
        'loc_EA6',
    )

    OP_B1('t4100_y')

    Jump('loc_EAF')

    def _loc_EA6(): pass

    label('loc_EA6')

    OP_B1('t4100_n')

    def _loc_EAF(): pass

    label('loc_EAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 1, 0x609)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EBF',
    )

    OP_1B(0x00, 0x00, 0x003F)

    Jump('loc_F5C')

    def _loc_EBF(): pass

    label('loc_EBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_ED8',
    )

    OP_1B(0x00, 0x00, 0x0032)

    Jump('loc_F5C')

    def _loc_ED8(): pass

    label('loc_ED8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 7, 0x61F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EEC',
    )

    OP_1B(0x00, 0x00, 0x0040)

    Jump('loc_F5C')

    def _loc_EEC(): pass

    label('loc_EEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 7, 0x61F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 0, 0x620)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F00',
    )

    OP_1B(0x00, 0x00, 0x0041)

    Jump('loc_F5C')

    def _loc_F00(): pass

    label('loc_F00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F14',
    )

    OP_1B(0x00, 0x00, 0x0042)

    Jump('loc_F5C')

    def _loc_F14(): pass

    label('loc_F14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F28',
    )

    OP_1B(0x00, 0x00, 0x0043)

    Jump('loc_F5C')

    def _loc_F28(): pass

    label('loc_F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F3C',
    )

    OP_1B(0x00, 0x00, 0x0044)

    Jump('loc_F5C')

    def _loc_F3C(): pass

    label('loc_F3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F50',
    )

    OP_1B(0x00, 0x00, 0x0045)

    Jump('loc_F5C')

    def _loc_F50(): pass

    label('loc_F50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_F5C',
    )

    OP_1B(0x00, 0x00, 0x0046)

    def _loc_F5C(): pass

    label('loc_F5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F86',
    )

    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0004, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0010, 0x0010)

    def _loc_F86(): pass

    label('loc_F86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FE4',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    CreateThread(0x000B, 0x01, 0x00, func_35_729D)
    CreateThread(0x000C, 0x01, 0x00, func_35_729D)
    CreateThread(0x000D, 0x01, 0x00, func_35_729D)
    CreateThread(0x000E, 0x01, 0x00, func_35_729D)
    CreateThread(0x000F, 0x01, 0x00, func_35_729D)
    CreateThread(0x0010, 0x01, 0x00, func_35_729D)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FE4(): pass

    label('loc_FE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_10D8',
    )

    OP_72(0x0019, 0x0004)
    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -70, 0, -46310, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -70, 250, -24300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -70, 0, -5700, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -70, 0, 8590, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_10D8(): pass

    label('loc_10D8')

    OP_25(0x01CB, 50, 0, -46480, 2000, 15000, 0x64, 0x00000000)

    Return()

# id: 0x0002 offset: 0x10F5
@scena.Code('func_02_10F5')
def func_02_10F5():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        'loc_1125',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_1267')

    def _loc_1125(): pass

    label('loc_1125')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_113E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_1267')

    def _loc_113E(): pass

    label('loc_113E')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1157',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_1267')

    def _loc_1157(): pass

    label('loc_1157')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1170',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_1267')

    def _loc_1170(): pass

    label('loc_1170')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1189',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_1267')

    def _loc_1189(): pass

    label('loc_1189')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_1267')

    def _loc_11A2(): pass

    label('loc_11A2')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11BB',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_1267')

    def _loc_11BB(): pass

    label('loc_11BB')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_1267')

    def _loc_11D4(): pass

    label('loc_11D4')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11ED',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_1267')

    def _loc_11ED(): pass

    label('loc_11ED')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1206',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_1267')

    def _loc_1206(): pass

    label('loc_1206')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_121F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_1267')

    def _loc_121F(): pass

    label('loc_121F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1238',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_1267')

    def _loc_1238(): pass

    label('loc_1238')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1251',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_1267')

    def _loc_1251(): pass

    label('loc_1251')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1267',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_1267(): pass

    label('loc_1267')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_127C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_1267')

    def _loc_127C(): pass

    label('loc_127C')

    Return()

# id: 0x0003 offset: 0x127D
@scena.Code('func_03_127D')
def func_03_127D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12A0',
    )

    OP_8D(0x00FE, 3700, -42040, 10110, -50100, 2000)

    Jump('func_03_127D')

    def _loc_12A0(): pass

    label('loc_12A0')

    Return()

# id: 0x0004 offset: 0x12A1
@scena.Code('func_04_12A1')
def func_04_12A1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12FD',
    )

    ChrWalkTo(0x00FE, -2070, 0, -37340, 2300, 0x00)
    ChrWalkTo(0x00FE, 2510, 0, -37340, 2300, 0x00)
    ChrWalkTo(0x00FE, 2510, 0, 8550, 2300, 0x00)
    ChrWalkTo(0x00FE, -2070, 0, 8550, 2300, 0x00)

    Jump('func_04_12A1')

    def _loc_12FD(): pass

    label('loc_12FD')

    Return()

# id: 0x0005 offset: 0x12FE
@scena.Code('func_05_12FE')
def func_05_12FE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_138A',
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

    Jump('func_05_12FE')

    def _loc_138A(): pass

    label('loc_138A')

    Return()

# id: 0x0006 offset: 0x138B
@scena.Code('func_06_138B')
def func_06_138B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_13AE',
    )

    OP_8D(0x00FE, 7470, -10200, 1790, -22030, 3000)

    Jump('func_06_138B')

    def _loc_13AE(): pass

    label('loc_13AE')

    Return()

# id: 0x0007 offset: 0x13AF
@scena.Code('func_07_13AF')
def func_07_13AF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_141D',
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

    Jump('func_07_13AF')

    def _loc_141D(): pass

    label('loc_141D')

    Return()

# id: 0x0008 offset: 0x141E
@scena.Code('func_08_141E')
def func_08_141E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_148C',
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

    Jump('func_08_141E')

    def _loc_148C(): pass

    label('loc_148C')

    Return()

# id: 0x0009 offset: 0x148D
@scena.Code('func_09_148D')
def func_09_148D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '亲卫队那群家伙竟敢\n',
            '反抗理查德上校，不可饶恕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x14C7
@scena.Code('func_0A_14C7')
def func_0A_14C7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '干嘛，你这家伙是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不想挨揍的话\n',
            '就乖乖地回协会去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1513
@scena.Code('func_0B_1513')
def func_0B_1513():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '王城已经完全封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生了什么事吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x154C
@scena.Code('func_0C_154C')
def func_0C_154C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_15EA',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，你们是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '街道的警备就交给我们了，\n',
            '今天你们就好好享受庆典带来的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变的时候\n',
            '我们没能做什么，\n',
            '现在我们会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1712')

    def _loc_15EA(): pass

    label('loc_15EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_15F4',
    )

    Jump('loc_1712')

    def _loc_15F4(): pass

    label('loc_15F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1623',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天起空港\n',
            '好像被完全封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1712')

    def _loc_1623(): pass

    label('loc_1623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1675',
    )

    ChrTalk(
        0x00FE,
        (
            '随着天色变晚，\n',
            '巡逻也加紧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果发现可疑的人\n',
            '请马上告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1712')

    def _loc_1675(): pass

    label('loc_1675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1697',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，没有任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1712')

    def _loc_1697(): pass

    label('loc_1697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_16E3',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '街上加强了警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是为了\n',
            '保证大家的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1712')

    def _loc_16E3(): pass

    label('loc_16E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_16ED',
    )

    Jump('loc_1712')

    def _loc_16ED(): pass

    label('loc_16ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_16F7',
    )

    Jump('loc_1712')

    def _loc_16F7(): pass

    label('loc_16F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1701',
    )

    Jump('loc_1712')

    def _loc_1701(): pass

    label('loc_1701')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_170B',
    )

    Jump('loc_1712')

    def _loc_170B(): pass

    label('loc_170B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1712',
    )

    def _loc_1712(): pass

    label('loc_1712')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1716
@scena.Code('func_0D_1716')
def func_0D_1716():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_177F',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也想留在王都\n',
            '为女王陛下而战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是假传的命令把我们从王都撤走了，\n',
            '真是可恶啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CB')

    def _loc_177F(): pass

    label('loc_177F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1789',
    )

    Jump('loc_18CB')

    def _loc_1789(): pass

    label('loc_1789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_17D0',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典\n',
            '会怎么样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下的病情很让人担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CB')

    def _loc_17D0(): pass

    label('loc_17D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1836',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会结束以后，\n',
            '我心里的石头也落地了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，不能放松，\n',
            '必须要继续保持警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CB')

    def _loc_1836(): pass

    label('loc_1836')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1865',
    )

    ChrTalk(
        0x00FE,
        (
            '希望武术大会\n',
            '能圆满顺利地闭幕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CB')

    def _loc_1865(): pass

    label('loc_1865')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_189C',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会正在进行，\n',
            '千万不能太放松警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CB')

    def _loc_189C(): pass

    label('loc_189C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_18A6',
    )

    Jump('loc_18CB')

    def _loc_18A6(): pass

    label('loc_18A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_18B0',
    )

    Jump('loc_18CB')

    def _loc_18B0(): pass

    label('loc_18B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_18BA',
    )

    Jump('loc_18CB')

    def _loc_18BA(): pass

    label('loc_18BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_18C4',
    )

    Jump('loc_18CB')

    def _loc_18C4(): pass

    label('loc_18C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_18CB',
    )

    def _loc_18CB(): pass

    label('loc_18CB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x18CF
@scena.Code('func_0E_18CF')
def func_0E_18CF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1953',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校是这起政变的发动者，\n',
            '对此至今我都无法相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许你们不知道，\n',
            '亲卫队那些家伙\n',
            '真的是干了不少坏事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5A')

    def _loc_1953(): pass

    label('loc_1953')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_195D',
    )

    Jump('loc_1A5A')

    def _loc_195D(): pass

    label('loc_195D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1991',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士协会\n',
            '应该没有窝藏\n',
            '恐怖分子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5A')

    def _loc_1991(): pass

    label('loc_1991')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_19C2',
    )

    ChrTalk(
        0x00FE,
        (
            '如果发现亲卫队的人，\n',
            '请立刻通报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5A')

    def _loc_19C2(): pass

    label('loc_19C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_19E8',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么了，不许妨碍我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5A')

    def _loc_19E8(): pass

    label('loc_19E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1A2B',
    )

    ChrTalk(
        0x00FE,
        (
            '你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不要做出什么\n',
            '奇怪的举动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5A')

    def _loc_1A2B(): pass

    label('loc_1A2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1A35',
    )

    Jump('loc_1A5A')

    def _loc_1A35(): pass

    label('loc_1A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1A3F',
    )

    Jump('loc_1A5A')

    def _loc_1A3F(): pass

    label('loc_1A3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1A49',
    )

    Jump('loc_1A5A')

    def _loc_1A49(): pass

    label('loc_1A49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A53',
    )

    Jump('loc_1A5A')

    def _loc_1A53(): pass

    label('loc_1A53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1A5A',
    )

    def _loc_1A5A(): pass

    label('loc_1A5A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1A5E
@scena.Code('func_0F_1A5E')
def func_0F_1A5E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1AB2',
    )

    ChrTalk(
        0x00FE,
        (
            '王都还存在着\n',
            '特务部队余党的可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要做好戒备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC5')

    def _loc_1AB2(): pass

    label('loc_1AB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1ABC',
    )

    Jump('loc_1BC5')

    def _loc_1ABC(): pass

    label('loc_1ABC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1B0D',
    )

    ChrTalk(
        0x00FE,
        (
            '特务部队那些人明明是新来的，\n',
            '还一副了不起的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '气死人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC5')

    def _loc_1B0D(): pass

    label('loc_1B0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1B40',
    )

    ChrTalk(
        0x00FE,
        (
            '那些恐怖分子……\n',
            '到底躲在哪儿呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC5')

    def _loc_1B40(): pass

    label('loc_1B40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1B69',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我也想去看总决赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC5')

    def _loc_1B69(): pass

    label('loc_1B69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1B96',
    )

    ChrTalk(
        0x00FE,
        (
            '看见可疑的人\n',
            '要马上过来报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC5')

    def _loc_1B96(): pass

    label('loc_1B96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1BA0',
    )

    Jump('loc_1BC5')

    def _loc_1BA0(): pass

    label('loc_1BA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1BAA',
    )

    Jump('loc_1BC5')

    def _loc_1BAA(): pass

    label('loc_1BAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1BB4',
    )

    Jump('loc_1BC5')

    def _loc_1BB4(): pass

    label('loc_1BB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1BBE',
    )

    Jump('loc_1BC5')

    def _loc_1BBE(): pass

    label('loc_1BBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1BC5',
    )

    def _loc_1BC5(): pass

    label('loc_1BC5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1BC9
@scena.Code('func_10_1BC9')
def func_10_1BC9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1CE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1C50',
    )

    ChrTalk(
        0x00FE,
        (
            '那位理查德上校\n',
            '是政变的发动者啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前我在城外见过他，\n',
            '从他的目光里真的可以看出\n',
            '他是为了王国着想的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CE0')

    def _loc_1C50(): pass

    label('loc_1C50')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '那位理查德上校\n',
            '是政变的发动者啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前我在城外见过他，\n',
            '从他的目光里真的可以看出\n',
            '他是为了王国着想的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那难道也是演技吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CE0(): pass

    label('loc_1CE0')

    Jump('loc_220E')

    def _loc_1CE3(): pass

    label('loc_1CE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1D52',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队的那些人\n',
            '要是突然改变主意\n',
            '来进攻王城怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望不要给艾莉茜雅女王\n',
            '造成什么威胁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1D52(): pass

    label('loc_1D52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1DB6',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下的病情\n',
            '到底怎么样了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目前一点新消息都没有，\n',
            '我担心得夜夜都睡不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1DB6(): pass

    label('loc_1DB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1DFC',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会\n',
            '平安地结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典\n',
            '又会怎么样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1DFC(): pass

    label('loc_1DFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1E52',
    )

    ChrTalk(
        0x00FE,
        (
            '每日散步\n',
            '就是我健康的秘诀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天天气很好啊，\n',
            '而且还吹着清爽的风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1E52(): pass

    label('loc_1E52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1EB4',
    )

    ChrTalk(
        0x00FE,
        (
            '谈到理查德上校啊，\n',
            '他确实是个很优秀的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他才是真正\n',
            '为利贝尔王国着想的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1EB4(): pass

    label('loc_1EB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F1B',
    )

    ChrTalk(
        0x00FE,
        (
            '我虽然也很\n',
            '喜欢武术大会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但听说女王陛下病了，\n',
            '就没有心情兴高采烈地\n',
            '去看比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1F1B(): pass

    label('loc_1F1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1F78',
    )

    ChrTalk(
        0x00FE,
        (
            '像这种亲卫队被\n',
            '王国军追捕的事情\n',
            '是前所未闻的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总感觉\n',
            '会发生什么大事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_220E')

    def _loc_1F78(): pass

    label('loc_1F78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_20BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1FFA',
    )

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫没有举行仪式的时候\n',
            '是对市民们开放的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在好像是作为\n',
            '王国军对付恐怖分子的\n',
            '总部来使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20BA')

    def _loc_1FFA(): pass

    label('loc_1FFA')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫没有举行仪式的时候\n',
            '是对市民们开放的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这几年里，\n',
            '要说王家用到离宫的时候，\n',
            '也就只有外国的重要人物来访时了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在好像是作为\n',
            '王国军对付恐怖分子的\n',
            '总部来使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20BA(): pass

    label('loc_20BA')

    Jump('loc_220E')

    def _loc_20BD(): pass

    label('loc_20BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_21AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2121',
    )

    ChrTalk(
        0x00FE,
        (
            '本来打算去艾尔贝离宫散步的，\n',
            '不过现在那里不让一般人接近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21AA')

    def _loc_2121(): pass

    label('loc_2121')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '天气不错，我本来打算到\n',
            '艾尔贝离宫去好好散散步的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是最近王国军贴出了公告，\n',
            '现在那里不让一般人接近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21AA(): pass

    label('loc_21AA')

    Jump('loc_220E')

    def _loc_21AD(): pass

    label('loc_21AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_220E',
    )

    ChrTalk(
        0x00FE,
        (
            '这条大道是\n',
            '格兰赛尔的繁华大街啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这大道中央散步，\n',
            '已经成了我每天必做之事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_220E(): pass

    label('loc_220E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2212
@scena.Code('func_11_2212')
def func_11_2212():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2324',
    )

    If(
        (
            (Expr.PushLong, 0xB),
            Expr.Return,
        ),
        'loc_2298',
    )

    ChrTalk(
        0x00FE,
        (
            '那位理查德上校\n',
            '是政变主谋的说法，\n',
            '我怎么也无法相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是真的，\n',
            '肯定也是因为有\n',
            '比山高比海深的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2321')

    def _loc_2298(): pass

    label('loc_2298')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '那位理查德上校\n',
            '是政变主谋的说法，\n',
            '我怎么也无法相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是真的，\n',
            '肯定也是因为有\n',
            '比山高比海深的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，肯定是这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2321(): pass

    label('loc_2321')

    Jump('loc_28CE')

    def _loc_2324(): pass

    label('loc_2324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2398',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵的数量增加了不少，\n',
            '却也不发表一下声明，真让人担忧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来想外出的，\n',
            '现在看来还是回家为好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CE')

    def _loc_2398(): pass

    label('loc_2398')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2405',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '武术大会历来都是\n',
            '诞辰庆典的开胃菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，女王陛下生病了，\n',
            '诞辰庆典会怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CE')

    def _loc_2405(): pass

    label('loc_2405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2458',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的人都在谈论武术大会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像这次优胜者\n',
            '出乎大家的预料哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CE')

    def _loc_2458(): pass

    label('loc_2458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2497',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是决赛哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要去竞技场\n',
            '好好看一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CE')

    def _loc_2497(): pass

    label('loc_2497')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_251A',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校身后\n',
            '总是跟着一个狐媚的副官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她那蔑视别人的眼神\n',
            '真让人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么那样的人\n',
            '会跟在上校身边呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CE')

    def _loc_251A(): pass

    label('loc_251A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2628',
    )

    If(
        (
            (Expr.PushLong, 0xB),
            Expr.Return,
        ),
        'loc_258D',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校以前也是\n',
            '从武术大会里脱颖而出的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使得一手变幻莫测的剑术，\n',
            '相当的强悍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2625')

    def _loc_258D(): pass

    label('loc_258D')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '理查德上校以前也是\n',
            '从武术大会里脱颖而出的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使得一手变幻莫测的剑术，\n',
            '相当的强悍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说好像是从一位\n',
            '相当厉害的剑术老师那里学来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2625(): pass

    label('loc_2625')

    Jump('loc_28CE')

    def _loc_2628(): pass

    label('loc_2628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2730',
    )

    If(
        (
            (Expr.PushLong, 0xB),
            Expr.Return,
        ),
        'loc_269B',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真的是一个很酷的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从在柏斯逮捕空贼以来，\n',
            '我已经完全为上校而着迷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272D')

    def _loc_269B(): pass

    label('loc_269B')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真的是一个很酷的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '长得又帅，头脑又好，\n',
            '简直是完美的男人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从在柏斯逮捕空贼以来，\n',
            '我已经完全为上校而着迷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_272D(): pass

    label('loc_272D')

    Jump('loc_28CE')

    def _loc_2730(): pass

    label('loc_2730')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2829',
    )

    If(
        (
            (Expr.PushLong, 0xB),
            Expr.Return,
        ),
        'loc_278F',
    )

    ChrTalk(
        0x00FE,
        (
            '我很讨厌那个公爵\n',
            '做女王的代理人什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下，\n',
            '请早日康复吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2826')

    def _loc_278F(): pass

    label('loc_278F')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我很讨厌那个公爵\n',
            '做女王的代理人什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然最近他的一些发言\n',
            '还算说得过去，\n',
            '不过我还是觉得那副打扮很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下，\n',
            '请早日康复吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2826(): pass

    label('loc_2826')

    Jump('loc_28CE')

    def _loc_2829(): pass

    label('loc_2829')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_286F',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有一个\n',
            '非常高大的壮汉走了过去，\n',
            '好像是大会的选手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CE')

    def _loc_286F(): pass

    label('loc_286F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_28CE',
    )

    ChrTalk(
        0x00FE,
        (
            '因为武术大会要开始了，\n',
            '所以东街区现在热闹的不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '预选赛\n',
            '很快就要开始了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28CE(): pass

    label('loc_28CE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x28D2
@scena.Code('func_12_28D2')
def func_12_28D2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2927',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '已经被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他竟然是个坏人，\n',
            '我怎么看不出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2927(): pass

    label('loc_2927')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2961',
    )

    ChrTalk(
        0x00FE,
        (
            '那些士兵好可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉不是很太平啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2961(): pass

    label('loc_2961')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_29B9',
    )

    ChrTalk(
        0x00FE,
        (
            '这条大街旁边的树\n',
            '是科洛蒂娅公主\n',
            '降生的时候种植的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是光阴似箭啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_29B9(): pass

    label('loc_29B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2A2E',
    )

    ChrTalk(
        0x00FE,
        (
            '大会的优胜者\n',
            '能参加城里的晚宴啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我对那个\n',
            '主办者公爵没好印象，\n',
            '但肯定是个很华丽的宴会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2A2E(): pass

    label('loc_2A2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2A71',
    )

    ChrTalk(
        0x00FE,
        (
            '因为今天是总决赛的日子，\n',
            '所以有很多人很早就出门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2A71(): pass

    label('loc_2A71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2B53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2AD4',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '常常能看见身穿黑色铠甲的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就是传闻中\n',
            '王国军的反恐精英吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B50')

    def _loc_2AD4(): pass

    label('loc_2AD4')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '常常能看见身穿黑色铠甲的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好就是从\n',
            '女王病倒的时候开始呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就是传闻中\n',
            '王国军的反恐精英吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B50(): pass

    label('loc_2B50')

    Jump('loc_2F7E')

    def _loc_2B53(): pass

    label('loc_2B53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2BBC',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '喜欢武术大会的人\n',
            '一大早就会到会场去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了占到好位置，\n',
            '好像还有人彻夜排队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2BBC(): pass

    label('loc_2BBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2C39',
    )

    ChrTalk(
        0x00FE,
        (
            '在格兰赛尔的市民中，\n',
            '理查德上校的人气\n',
            '可以说是直线上升。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，作为一个男人而言，\n',
            '他是个既帅又厉害的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2C39(): pass

    label('loc_2C39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2CFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2C91',
    )

    ChrTalk(
        0x00FE,
        (
            '这个格兰赛尔的\n',
            '地下水路经过了一番整修。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样还真是方便多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CFC')

    def _loc_2C91(): pass

    label('loc_2C91')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '这个格兰赛尔的\n',
            '地下水路经过了一番整修。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看，\n',
            '大街上到处都是排水口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样还真是方便多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CFC(): pass

    label('loc_2CFC')

    Jump('loc_2F7E')

    def _loc_2CFF(): pass

    label('loc_2CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2D6A',
    )

    ChrTalk(
        0x00FE,
        (
            '这个喷水的雕像\n',
            '是只白隼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它是利贝尔的国鸟，\n',
            '国旗上有它的图案，\n',
            '王家的徽章上也有它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2D6A(): pass

    label('loc_2D6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2F7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2E40',
    )

    ChrTalk(
        0x00FE,
        (
            '这个城市一共分为\n',
            '四个主要区域哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个南街区有游击士协会和商店，\n',
            '北街区有王国最大的酒店，\n',
            '往北直走就是格兰赛尔城了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西街区有大圣堂和出版社，\n',
            '东街区则有各国大使馆、\n',
            '竞技场和百货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7E')

    def _loc_2E40(): pass

    label('loc_2E40')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '哟，是第一次来到格兰赛尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个城市一共分为\n',
            '四个主要区域哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是南街区，有游击士协会\n',
            '以及鳞次栉比的各种商店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '北街区有王国最大的酒店，\n',
            '往北直走就是格兰赛尔城了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '西街区有大圣堂和\n',
            '利贝尔通讯社，\n',
            '是众人皆知的公共设施之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后是东街区，\n',
            '有着各国大使馆和竞技场，\n',
            '还有大型的百货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F7E(): pass

    label('loc_2F7E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x2F82
@scena.Code('func_13_2F82')
def func_13_2F82():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2FA7',
    )

    ChrTalk(
        0x00FE,
        (
            '庆典真的很好玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_2FA7(): pass

    label('loc_2FA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2FC3',
    )

    ChrTalk(
        0x00FE,
        (
            '坏蛋来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_2FC3(): pass

    label('loc_2FC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2FE5',
    )

    ChrTalk(
        0x00FE,
        (
            '呜呜～肚子好饿啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_2FE5(): pass

    label('loc_2FE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_302C',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，比赛结束的时候\n',
            '只有那个红头盔没有气喘吁吁的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_302C(): pass

    label('loc_302C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3036',
    )

    Jump('loc_313B')

    def _loc_3036(): pass

    label('loc_3036')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_307F',
    )

    ChrTalk(
        0x00FE,
        (
            '我想明天游击士的\n',
            '那个小组会取胜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是直觉而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_307F(): pass

    label('loc_307F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3089',
    )

    Jump('loc_313B')

    def _loc_3089(): pass

    label('loc_3089')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_30CB',
    )

    ChrTalk(
        0x00FE,
        (
            '一个人就那么强，\n',
            '四个人在一起的话\n',
            '不就是最强了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_30CB(): pass

    label('loc_30CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_30EF',
    )

    ChrTalk(
        0x00FE,
        (
            '哇啊～好像很好吃呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_30EF(): pass

    label('loc_30EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3111',
    )

    ChrTalk(
        0x00FE,
        (
            '实在是酷得不得了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_313B')

    def _loc_3111(): pass

    label('loc_3111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_313B',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '门票掉到哪里去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_313B(): pass

    label('loc_313B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x313F
@scena.Code('func_14_313F')
def func_14_313F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_31AA',
    )

    ChrTalk(
        0x00FE,
        (
            '蒂库他对美女毫无抵抗力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据我统计，\n',
            '他只要一看到美女，\n',
            '有９５％的概率都会一见钟情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_31AA(): pass

    label('loc_31AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_31E9',
    )

    ChrTalk(
        0x00FE,
        (
            '奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们不觉得\n',
            '那些士兵有些慌乱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_31E9(): pass

    label('loc_31E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_321A',
    )

    ChrTalk(
        0x00FE,
        (
            '今年的诞辰庆典\n',
            '能照原计划举办吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_321A(): pass

    label('loc_321A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3256',
    )

    ChrTalk(
        0x00FE,
        (
            '好精彩的比赛呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直可以称为『激斗』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_3256(): pass

    label('loc_3256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3260',
    )

    Jump('loc_33DA')

    def _loc_3260(): pass

    label('loc_3260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_32B1',
    )

    ChrTalk(
        0x00FE,
        (
            '我对游击士之间的比赛\n',
            '很有兴趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为平时看不到这样的场面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_32B1(): pass

    label('loc_32B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_32E2',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '托伊他确实是一个路痴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_32E2(): pass

    label('loc_32E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3344',
    )

    ChrTalk(
        0x00FE,
        (
            '托伊发表的意见\n',
            '有时没有根据，\n',
            '但却能够抓住问题的核心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这次会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_3344(): pass

    label('loc_3344')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_337D',
    )

    ChrTalk(
        0x00FE,
        (
            '托伊他趁我不留神的时候\n',
            '一下就跑得不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_337D(): pass

    label('loc_337D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_33AE',
    )

    ChrTalk(
        0x00FE,
        (
            '问题是只靠一个人\n',
            '究竟能走多远……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33DA')

    def _loc_33AE(): pass

    label('loc_33AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_33DA',
    )

    ChrTalk(
        0x00FE,
        (
            '如果不快点的话\n',
            '就找不到座位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33DA(): pass

    label('loc_33DA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x33DE
@scena.Code('func_15_33DE')
def func_15_33DE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3424',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～\n',
            '科洛蒂娅公主既温柔又漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好心动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_3424(): pass

    label('loc_3424')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3455',
    )

    ChrTalk(
        0x00FE,
        (
            '大街上怎么全是士兵\n',
            '在跑来跑去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_3455(): pass

    label('loc_3455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3488',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会也结束了，\n',
            '今天玩什么好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_3488(): pass

    label('loc_3488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_34B9',
    )

    ChrTalk(
        0x00FE,
        (
            '我还以为戴红头盔的\n',
            '那个人会赢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_34B9(): pass

    label('loc_34B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_34C3',
    )

    Jump('loc_36EF')

    def _loc_34C3(): pass

    label('loc_34C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3525',
    )

    ChrTalk(
        0x00FE,
        (
            '红头盔的那家伙和空贼的比赛\n',
            '很有魄力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然今年的冠军\n',
            '还是会被王国军夺得吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_3525(): pass

    label('loc_3525')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3554',
    )

    ChrTalk(
        0x00FE,
        (
            '喂喂，\n',
            '托伊那家伙今天迟到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_3554(): pass

    label('loc_3554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3640',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_35BF',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多能看出来\n',
            '各个组的实力水平了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个叫做金的选手\n',
            '也请了另外三个人来助拳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_363D')

    def _loc_35BF(): pass

    label('loc_35BF')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '那个戴红头盔的人\n',
            '相当强嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多能看出来\n',
            '各个组的实力水平了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个叫做金的选手\n',
            '也请了另外三个人来助拳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_363D(): pass

    label('loc_363D')

    Jump('loc_36EF')

    def _loc_3640(): pass

    label('loc_3640')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3690',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '为什么他总是这样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想早点去竞技场\n',
            '占个好座位啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_3690(): pass

    label('loc_3690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_36CC',
    )

    ChrTalk(
        0x00FE,
        (
            '那个共和国的人好强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '单打独斗就获胜了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36EF')

    def _loc_36CC(): pass

    label('loc_36CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_36EF',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，托伊那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36EF(): pass

    label('loc_36EF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x36F3
@scena.Code('func_16_36F3')
def func_16_36F3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3700',
    )

    Jump('loc_3995')

    def _loc_3700(): pass

    label('loc_3700')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_370A',
    )

    Jump('loc_3995')

    def _loc_370A(): pass

    label('loc_370A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_37EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3770',
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

    Jump('loc_37E8')

    def _loc_3770(): pass

    label('loc_3770')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

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

    def _loc_37E8(): pass

    label('loc_37E8')

    Jump('loc_3995')

    def _loc_37EB(): pass

    label('loc_37EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_380F',
    )

    ChrTalk(
        0x00FE,
        (
            '嘻嘻，他真是热情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3995')

    def _loc_380F(): pass

    label('loc_380F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3847',
    )

    ChrTalk(
        0x00FE,
        (
            '哇，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难以置信地好吃啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3995')

    def _loc_3847(): pass

    label('loc_3847')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3851',
    )

    Jump('loc_3995')

    def _loc_3851(): pass

    label('loc_3851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_385B',
    )

    Jump('loc_3995')

    def _loc_385B(): pass

    label('loc_385B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_38C4',
    )

    ChrTalk(
        0x00FE,
        (
            '他呀，\n',
            '那时一直都在盯着我的脸看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0018, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '讨厌，真让人家害羞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3995')

    def _loc_38C4(): pass

    label('loc_38C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3932',
    )

    ChrTalk(
        0x00FE,
        (
            '今天一整天\n',
            '又和他一起渡过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0018, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '到格兰赛尔来旅行\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3995')

    def _loc_3932(): pass

    label('loc_3932')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_396D',
    )

    ChrTalk(
        0x00FE,
        (
            '他啊，在看比赛的时候\n',
            '也紧紧地握住我的手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3995')

    def _loc_396D(): pass

    label('loc_396D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3995',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '好想到王城里去看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3995(): pass

    label('loc_3995')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x3999
@scena.Code('func_17_3999')
def func_17_3999():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_39A6',
    )

    Jump('loc_3D53')

    def _loc_39A6(): pass

    label('loc_39A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_39B0',
    )

    Jump('loc_3D53')

    def _loc_39B0(): pass

    label('loc_39B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3A13',
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
            '感情的地方果然还是\n',
            '王城前面啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D53')

    def _loc_3A13(): pass

    label('loc_3A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3B0E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3A51',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '这世上还有比这更加美丽的东西吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B0B')

    def _loc_3A51(): pass

    label('loc_3A51')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '在火红的黄昏中屹立着\n',
            '美丽的王都和格兰赛尔城……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且，\n',
            '还有映出那样美景的你的双眸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '这世上还有比这更加美丽的东西吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，绝对没有！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有就是没有！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B0B(): pass

    label('loc_3B0B')

    Jump('loc_3D53')

    def _loc_3B0E(): pass

    label('loc_3B0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3B36',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～不愧是王室御用店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D53')

    def _loc_3B36(): pass

    label('loc_3B36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3B40',
    )

    Jump('loc_3D53')

    def _loc_3B40(): pass

    label('loc_3B40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3B4A',
    )

    Jump('loc_3D53')

    def _loc_3B4A(): pass

    label('loc_3B4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3BB6',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，看比赛的过程中\n',
            '不自觉地侧过脸去凝视她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟有多少魅力呢，\n',
            '她的美丽难道也是罪过吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D53')

    def _loc_3BB6(): pass

    label('loc_3BB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3BFE',
    )

    ChrTalk(
        0x00FE,
        (
            '好～的，\n',
            '今天也要和她一起度过\n',
            '比这个糖果还要甜美的时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D53')

    def _loc_3BFE(): pass

    label('loc_3BFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3CF6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3C67',
    )

    ChrTalk(
        0x00FE,
        (
            '竞技场正在被\n',
            '鼎沸的热情所包围着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不辜负这股热情，\n',
            '我俩也要热恋起来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF3')

    def _loc_3C67(): pass

    label('loc_3C67')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '既然不能进入王城，\n',
            '那就先去看看武术大会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竞技场正在被\n',
            '鼎沸的热情所包围着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不辜负这股热情，\n',
            '我俩也要热恋起来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CF3(): pass

    label('loc_3CF3')

    Jump('loc_3D53')

    def _loc_3CF6(): pass

    label('loc_3CF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3D53',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，怎么会这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和心肝宝贝儿\n',
            '一起到王都来旅行，\n',
            '可现在竟然不能进入王城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D53(): pass

    label('loc_3D53')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x3D57
@scena.Code('func_18_3D57')
def func_18_3D57():
    TalkBegin(0x0016)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0004)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB5',
    )

    OP_0D()
    OP_A9(0x72)
    OP_56(0x00)
    TalkEnd(0x0016)

    Return()

    def _loc_3DB5(): pass

    label('loc_3DB5')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DC6',
    )

    TalkEnd(0x0016)

    Return()

    def _loc_3DC6(): pass

    label('loc_3DC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3DF4',
    )

    ChrTalk(
        0x0016,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '请慢慢挑选！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_3DF4(): pass

    label('loc_3DF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3E4B',
    )

    ChrTalk(
        0x0016,
        (
            '与之前在这里的士兵不同，\n',
            '新来的是一些黑衣士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '发生什么事了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_3E4B(): pass

    label('loc_3E4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3EE3',
    )

    ChrTalk(
        0x0016,
        (
            '武术大会结束以后，\n',
            '街道上也安静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '随着女王陛下的诞辰庆典临近，\n',
            '街上应该又会热闹起来的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '不过今年的情况究竟会如何呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_3EE3(): pass

    label('loc_3EE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3F3D',
    )

    ChrTalk(
        0x0016,
        (
            '唔～\n',
            '至少想去看看决赛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '不过为了能独立生活，\n',
            '就必须得努力工作才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_3F3D(): pass

    label('loc_3F3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3F85',
    )

    ChrTalk(
        0x0016,
        (
            '欢迎光临，\n',
            '我这里的草莓薄饼非常好吃哦，\n',
            '向你们强烈推荐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_3F85(): pass

    label('loc_3F85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3FDB',
    )

    ChrTalk(
        0x0016,
        (
            '在这个时期打工\n',
            '会得到更高的工钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '但代价就是\n',
            '不能去看武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_3FDB(): pass

    label('loc_3FDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_400C',
    )

    ChrTalk(
        0x0016,
        (
            '欢迎光临！\n',
            '本店的薄饼十分美味哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_400C(): pass

    label('loc_400C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4037',
    )

    ChrTalk(
        0x0016,
        (
            '啊～啊，\n',
            '就不能多卖一些吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_4037(): pass

    label('loc_4037')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4073',
    )

    ChrTalk(
        0x0016,
        (
            '那边的哥哥姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '来一些美味的薄饼如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_4073(): pass

    label('loc_4073')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_40E2',
    )

    ChrTalk(
        0x0016,
        (
            '我为了独立生活，\n',
            '所以就在这里打工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '西街区有一间\n',
            '正在出售的空的房子，\n',
            '我准备把那里买下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4113')

    def _loc_40E2(): pass

    label('loc_40E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4113',
    )

    ChrTalk(
        0x0016,
        (
            '欢迎～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '来尝尝吧，很好吃的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4113(): pass

    label('loc_4113')

    TalkEnd(0x0016)

    Return()

# id: 0x0019 offset: 0x4117
@scena.Code('func_19_4117')
def func_19_4117():
    TalkBegin(0x0015)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0004)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4175',
    )

    OP_0D()
    OP_A9(0x71)
    OP_56(0x00)
    TalkEnd(0x0015)

    Return()

    def _loc_4175(): pass

    label('loc_4175')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4186',
    )

    TalkEnd(0x0015)

    Return()

    def _loc_4186(): pass

    label('loc_4186')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4202',
    )

    ChrTalk(
        0x0015,
        (
            '东街区的冰淇淋小店\n',
            '很受欢迎呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我虽然去侦察过，\n',
            '可排的队太长了，没能买到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '好～的，我绝对不能输！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_4202(): pass

    label('loc_4202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_425E',
    )

    ChrTalk(
        0x0015,
        (
            '那些黑衣士兵们\n',
            '也是属于王国军的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '他们很有压迫感，\n',
            '我都有些害怕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_425E(): pass

    label('loc_425E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_42DC',
    )

    ChrTalk(
        0x0015,
        (
            '在诞辰庆典之前，\n',
            '我打算一直在格兰赛尔摆摊子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '不过，女王陛下的病无法痊愈的话，\n',
            '诞辰庆典恐怕就要中止了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_42DC(): pass

    label('loc_42DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4322',
    )

    ChrTalk(
        0x0015,
        (
            '呼，\n',
            '今天天气也很好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '柏斯地区\n',
            '也应该很晴朗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_4322(): pass

    label('loc_4322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4398',
    )

    ChrTalk(
        0x0015,
        (
            '昨天从傍晚开始，\n',
            '大街上的士兵就增多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '虽然我是个奉公守法的市民，\n',
            '不过看到这种场面也有点紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_4398(): pass

    label('loc_4398')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_43DD',
    )

    ChrTalk(
        0x0015,
        (
            '您好，欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '好吃的冰淇淋，\n',
            '来品尝一个好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_43DD(): pass

    label('loc_43DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4437',
    )

    ChrTalk(
        0x0015,
        (
            '大赛从第一天开始\n',
            '就非常热闹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '竞技场里传来的欢呼声\n',
            '连这里都能听见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_4437(): pass

    label('loc_4437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4490',
    )

    ChrTalk(
        0x0015,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '在为大会加油而疲惫的时候，\n',
            '难道不想要来点甘甜的东西吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_4490(): pass

    label('loc_4490')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_44EE',
    )

    ChrTalk(
        0x0015,
        (
            '我原以为柏斯\n',
            '就算很大的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '不愧是王都啊，\n',
            '光是街上行人的数量就这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_44EE(): pass

    label('loc_44EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4558',
    )

    ChrTalk(
        0x0015,
        (
            '我平时是在\n',
            '柏斯做生意的，\n',
            '这次出差到了王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我为了做好买卖\n',
            '而到各个地方\n',
            '去寻找机遇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_458F')

    def _loc_4558(): pass

    label('loc_4558')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_458F',
    )

    ChrTalk(
        0x0015,
        (
            '您好，欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '来一个冰淇淋怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_458F(): pass

    label('loc_458F')

    TalkEnd(0x0015)

    Return()

# id: 0x001A offset: 0x4593
@scena.Code('func_1A_4593')
def func_1A_4593():
    TalkBegin(0x0014)
    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_45A3',
    )

    Jump('loc_4613')

    def _loc_45A3(): pass

    label('loc_45A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_45B0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4613')

    def _loc_45B0(): pass

    label('loc_45B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_45BA',
    )

    Jump('loc_4613')

    def _loc_45BA(): pass

    label('loc_45BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_45C7',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4613')

    def _loc_45C7(): pass

    label('loc_45C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_45D4',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4613')

    def _loc_45D4(): pass

    label('loc_45D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_45DE',
    )

    Jump('loc_4613')

    def _loc_45DE(): pass

    label('loc_45DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_45E8',
    )

    Jump('loc_4613')

    def _loc_45E8(): pass

    label('loc_45E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_45F5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4613')

    def _loc_45F5(): pass

    label('loc_45F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4602',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4613')

    def _loc_4602(): pass

    label('loc_4602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_460C',
    )

    Jump('loc_4613')

    def _loc_460C(): pass

    label('loc_460C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4613',
    )

    def _loc_4613(): pass

    label('loc_4613')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_4686',
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    MenuEnd(0x0004)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4675',
    )

    OP_0D()
    OP_A9(0x73)
    OP_56(0x00)
    TalkEnd(0x0014)

    Return()

    def _loc_4675(): pass

    label('loc_4675')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4686',
    )

    TalkEnd(0x0014)

    Return()

    def _loc_4686(): pass

    label('loc_4686')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_476A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_46E7',
    )

    ChrTalk(
        0x0014,
        (
            '飞艇停运了，\n',
            '商品也就送不过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '这回的这个麻烦事\n',
            '就不能怪在我头上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4767')

    def _loc_46E7(): pass

    label('loc_46E7')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0014,
        (
            '呼，飞艇停运了，\n',
            '商品也就送不过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '真让人着急啊，\n',
            '为什么总是这么巧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '这回的这个麻烦事\n',
            '就不能怪在我头上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4767(): pass

    label('loc_4767')

    Jump('loc_4B73')

    def _loc_476A(): pass

    label('loc_476A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_47AF',
    )

    ChrTalk(
        0x0014,
        (
            '怎么那么多士兵啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '啊！\n',
            '又、又有什么麻烦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_47AF(): pass

    label('loc_47AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_47D4',
    )

    ChrTalk(
        0x0014,
        (
            '天哪～！\n',
            '轮胎爆胎啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_47D4(): pass

    label('loc_47D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_48A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4833',
    )

    ChrTalk(
        0x0014,
        (
            '没有麻烦\n',
            '反而让我有些失望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '我的人生似乎就是\n',
            '与麻烦形影不离的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48A1')

    def _loc_4833(): pass

    label('loc_4833')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0014,
        (
            '今天没有\n',
            '出现什么麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '不过这反而\n',
            '让人有些失望呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '我的人生似乎就是\n',
            '与麻烦形影不离的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48A1(): pass

    label('loc_48A1')

    Jump('loc_4B73')

    def _loc_48A4(): pass

    label('loc_48A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_48D1',
    )

    ChrTalk(
        0x0014,
        (
            '呼，\n',
            '今天要是没有麻烦就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_48D1(): pass

    label('loc_48D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_49C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_492C',
    )

    ChrTalk(
        0x0014,
        (
            '货物拿不出来，\n',
            '今日的销售额为零。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '呜呜，\n',
            '我怎么总是这么倒霉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49C5')

    def _loc_492C(): pass

    label('loc_492C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0014,
        (
            '因为一直在\n',
            '修理货箱的缘故，\n',
            '所以今天很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '货物拿不出来，\n',
            '今日的销售额为零。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '呜呜，\n',
            '我怎么总是这么倒霉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49C5(): pass

    label('loc_49C5')

    Jump('loc_4B73')

    def _loc_49C8(): pass

    label('loc_49C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4A38',
    )

    ChrTalk(
        0x0014,
        (
            '这、这回箱子坏了，\n',
            '彻底打不开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '呜呜，\n',
            '我怎么总是这么倒霉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_4A38(): pass

    label('loc_4A38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4A88',
    )

    ChrTalk(
        0x0014,
        (
            '比赛的前后\n',
            '是顾客最多的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '比赛开始时\n',
            '就可以松一口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_4A88(): pass

    label('loc_4A88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4AB7',
    )

    ChrTalk(
        0x0014,
        (
            '呼，\n',
            '总算是把现金出纳机修好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_4AB7(): pass

    label('loc_4AB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4B31',
    )

    ChrTalk(
        0x0014,
        (
            '好不容易等到武术大会，\n',
            '正是客人多的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '呜呜，\n',
            '我怎么总是这么倒霉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B73')

    def _loc_4B31(): pass

    label('loc_4B31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4B73',
    )

    ChrTalk(
        0x0014,
        (
            '唔～糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '现金出纳机坏掉了。\n',
            '怎么办好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B73(): pass

    label('loc_4B73')

    TalkEnd(0x0014)

    Return()

# id: 0x001B offset: 0x4B77
@scena.Code('func_1B_4B77')
def func_1B_4B77():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，可喜可贺可喜可贺！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下万岁，公主殿下万岁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x4BBE
@scena.Code('func_1C_4BBE')
def func_1C_4BBE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '当我看到科洛蒂娅公主的身影时，\n',
            '一下就感觉到利贝尔王国的未来\n',
            '将是平稳安泰的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x4C19
@scena.Code('func_1D_4C19')
def func_1D_4C19():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4C26',
    )

    Jump('loc_4EF2')

    def _loc_4C26(): pass

    label('loc_4C26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4C30',
    )

    Jump('loc_4EF2')

    def _loc_4C30(): pass

    label('loc_4C30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4C3A',
    )

    Jump('loc_4EF2')

    def _loc_4C3A(): pass

    label('loc_4C3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4C44',
    )

    Jump('loc_4EF2')

    def _loc_4C44(): pass

    label('loc_4C44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4C4E',
    )

    Jump('loc_4EF2')

    def _loc_4C4E(): pass

    label('loc_4C4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4C58',
    )

    Jump('loc_4EF2')

    def _loc_4C58(): pass

    label('loc_4C58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4C62',
    )

    Jump('loc_4EF2')

    def _loc_4C62(): pass

    label('loc_4C62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4C6C',
    )

    Jump('loc_4EF2')

    def _loc_4C6C(): pass

    label('loc_4C6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4EE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_4CF5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330141613V#840F虽然参加了武术大会，\n',
            '但游击士的任务\n',
            '并不能因此而怠慢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141608V我正要去处理\n',
            '一些简单的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EDE')

    def _loc_4CF5(): pass

    label('loc_4CF5')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0330141603V#840F哦……是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141604V#501F啊，克鲁茨大哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141605V#010F怎么了？\n',
            '在这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330141606V#840F我现在正要去\n',
            '剿灭通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141607V虽然参加了武术大会，\n',
            '但游击士的任务\n',
            '并不能因此而怠慢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141608V我正要去处理\n',
            '一些简单的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141609V#008F啊～不愧是前辈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330141610V#841F哈哈，\n',
            '就算是稍微热热身吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141611V对了，\n',
            '如果我们在比赛中相遇了，\n',
            '还请你们手下留情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141612V#010F彼此彼此，\n',
            '请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EDE(): pass

    label('loc_4EDE')

    Jump('loc_4EF2')

    def _loc_4EE1(): pass

    label('loc_4EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4EEB',
    )

    Jump('loc_4EF2')

    def _loc_4EEB(): pass

    label('loc_4EEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4EF2',
    )

    def _loc_4EF2(): pass

    label('loc_4EF2')

    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x4EF6
@scena.Code('func_1E_4EF6')
def func_1E_4EF6():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我们是借诞辰庆典的机会\n',
            '来王都参观游览的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x4F2C
@scena.Code('func_1F_4F2C')
def func_1F_4F2C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '接下来去哪儿好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说大圣堂也是个好去处，\n',
            '但我又想去看看长城『亚宁堡』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x4F88
@scena.Code('func_20_4F88')
def func_20_4F88():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '是老妈带我\n',
            '到王都来的，\n',
            '这里的街道真宽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x4FBF
@scena.Code('func_21_4FBF')
def func_21_4FBF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我已经累得不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是到处都没有\n',
            '可以休息的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去酒廊里又要花钱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x501F
@scena.Code('func_22_501F')
def func_22_501F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '当听说发生了政变时，\n',
            '我吓了一大跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过看着街道这么热闹的样子，\n',
            '怎么也无法想象发生过那样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x5092
@scena.Code('func_23_5092')
def func_23_5092():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '肚子好饿呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易来了王都一趟，\n',
            '想要到一些有名的餐馆去，\n',
            '不知道这家如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像每家餐馆都很不错，\n',
            '简直让我眼花缭乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x5124
@scena.Code('func_24_5124')
def func_24_5124():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这里是很热闹，\n',
            '但东街区的人更多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x5152
@scena.Code('func_25_5152')
def func_25_5152():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我找不到路了，\n',
            '要去游击士协会问问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x5182
@scena.Code('func_26_5182')
def func_26_5182():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈～不愧是诞辰庆典，\n',
            '好热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典时期\n',
            '就应该到这里来做生意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x51D7
@scena.Code('func_27_51D7')
def func_27_51D7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '传说中\n',
            '最好吃的那个冰淇淋店\n',
            '在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x520A
@scena.Code('func_28_520A')
def func_28_520A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '那个商店是卖什么的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x522D
@scena.Code('func_29_522D')
def func_29_522D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '各种事件相继发生，\n',
            '能够回归和平的日子真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了女王陛下，\n',
            '我以后也要好好加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x5292
@scena.Code('func_2A_5292')
def func_2A_5292():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '终于看到好久不见的女王陛下，\n',
            '我已经很满足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有这么好的一位女王陛下，\n',
            '却还要发动什么政变，\n',
            '不知道那些人是怎么想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0x5318
@scena.Code('func_2B_5318')
def func_2B_5318():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '因为飞艇停航的缘故，\n',
            '我来到格兰赛尔时\n',
            '已经耽误很长时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002C offset: 0x535F
@scena.Code('func_2C_535F')
def func_2C_535F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 0, 0x6E8)),
            Expr.Return,
        ),
        'loc_53D5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0360140890V#611F呵呵，正游击士的徽章\n',
            '和你们二人很相配呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140891V#008F啊……嗯，谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56B6')

    def _loc_53D5(): pass

    label('loc_53D5')

    SetScenaFlags(ScenaFlag(0x00DD, 0, 0x6E8))

    ChrTalk(
        0x00FE,
        (
            '#0360140879V#617F……呵呵，晚宴之后\n',
            '就知道想要很快回去是不可能的了，\n',
            '只有在这里多滞留一会儿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140880V#001F啊哈，\n',
            '各位市长是要进行一些商议对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360140881V#610F嗯，科林兹校长的提案是\n',
            '召开一个临时王国会议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360140882V#612F由于政变的混乱，\n',
            '这次的事件给市民带来的影响绝对不能小视。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360140883V因此现在各个地区保持联系合作是必要的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140884V#501F啊～\n',
            '看来市长姐姐又要变得越来越忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360140885V#610F呵呵，\n',
            '至少今天可以不受拘束地放松一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360140886V这就准备散步到大圣堂去做礼拜呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140887V#505F说起来，我们第一次见面时\n',
            '市长姐姐就逃掉了礼拜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360140888V#617F嗯，\n',
            '所以这次我更要好好地祷告了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360140889V看来到大圣堂还得把至今为止偷的懒\n',
            '一起做个忏悔才行呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56B6(): pass

    label('loc_56B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x002D offset: 0x56BA
@scena.Code('func_2D_56BA')
def func_2D_56BA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0370140894V#620F就算连日参加会议，\n',
            '和小姐平常的工作量相比也轻松了许多。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370140895V看来想要让小姐休息，\n',
            '还是离开柏斯最好……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002E offset: 0x574C
@scena.Code('func_2E_574C')
def func_2E_574C():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1B(0x03, 0x00, 0xFFFF)

    Return()

# id: 0x002F offset: 0x5760
@scena.Code('func_2F_5760')
def func_2F_5760():
    EventBegin(0x00)
    ChrSetPos(0x001C, 5760, 0, -46060, 270)
    CreateThread(0x001C, 0x00, 0x00, func_02_10F5)
    CameraMove(600, 250, 1950, 0)
    OP_67(0, 17690, -10000, 0)
    CameraSetDistance(2530, 0)
    OP_6C(315000, 0)
    OP_6E(571, 0)
    ChrSetPos(0x0101, -100, 0, -56250, 0)
    ChrSetPos(0x0102, -1060, 0, -58160, 0)
    ChrSetPos(0x010E, 890, 0, -58220, 0)

    @scena.Lambda('lambda_57F0')
    def lambda_57F0():
        CameraMove(-270, 1500, -57160, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_57F0)

    Sleep(2000)

    @scena.Lambda('lambda_580D')
    def lambda_580D():
        CameraSetDistance(3000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_580D)

    @scena.Lambda('lambda_581D')
    def lambda_581D():
        OP_67(0, 4000, -10000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_581D)

    @scena.Lambda('lambda_5835')
    def lambda_5835():
        OP_6C(8000, 11000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5835)

    @scena.Lambda('lambda_5845')
    def lambda_5845():
        OP_6E(273, 9000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5845)

    Sleep(11000)

    ChrTalk(
        0x0101,
        (
            '#0010100579V#001F#5P哇～～\n',
            '好大的城市啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100580V以前和老爸一起来的时候，\n',
            '就有这么大吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100581V#010F当然了，这是王国最大的城市嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100582V这条大街的最前方，\n',
            '就是女王陛下所居住的格兰赛尔城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100583V还有七耀教会的大圣堂、王立竞技场，\n',
            '以及各国的大使馆之类的设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100584V#501F#5P哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100585V不过约修亚，你还真是了解啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100586V以前也来过这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100587V#015F嗯……\n',
            '也是小时候的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100588V#130F真的是……\n',
            '这城市无论何时看起来都是这么美丽呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100589V不过单从规模上来说，\n',
            '帝国和共和国的首都比这里要更大一些。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100590V不过这个格兰赛尔，\n',
            '可是有着其他地方比不上的舒适感呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5B0C')
    def lambda_5B0C():
        ChrTurnDirection(0x00FE, 0x010E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5B0C)

    ChrTurnDirection(0x0101, 0x010E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100591V#506F#5P嘿嘿，真是高兴啊。\n',
            '能听到外国的朋友这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100592V#501F对了……\n',
            '教授，你接下来打算怎么样呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100593V日常生活的费用有着落吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0101, 400)

    ChrTalk(
        0x010E,
        (
            '#0150100594V#130F哈哈，其实是有保障的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100595V我会暂时寄住在一个叫\n',
            '『历史资料馆』的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100596V#004F#5P哎，还有这样的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100597V#010F是个展示发掘出来的文物\n',
            '和美术品之类的博物馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100598V#130F对，作为那里的名誉会员，\n',
            '我可以在那里借住一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100599V艾丝蒂尔、约修亚，\n',
            '如果方便的话你们也过来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100600V#007F#5P唔……说到博物馆，\n',
            '就有一种很严肃的气氛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100601V#509F是不是要说『既然来了，就学习吧』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100602V#132F呵呵，如果你真的愿意的话，\n',
            '我也可以认真地教教你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100603V#130F……开玩笑的。\n',
            '去那里只要参观一下展示品，\n',
            '就已经会感到很开心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100604V那么，我就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5E65')
    def lambda_5E65():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_5E65')

    DispatchAsync2(0x0101, 0x0001, lambda_5E65)

    @scena.Lambda('lambda_5E76')
    def lambda_5E76():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_5E76')

    DispatchAsync2(0x0102, 0x0001, lambda_5E76)

    ChrSetDirection(0x010E, 45, 400)
    ChrWalkTo(0x010E, 4059, 0, -54820, 4000, 0x00)

    @scena.Lambda('lambda_5EA2')
    def lambda_5EA2():
        ChrWalkTo(0x00FE, 4950, 0, -35100, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_5EA2)

    @scena.Lambda('lambda_5EBD')
    def lambda_5EBD():
        CameraSetDistance(2800, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5EBD)

    @scena.Lambda('lambda_5ECD')
    def lambda_5ECD():
        CameraMove(-780, 0, -56940, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5ECD)

    @scena.Lambda('lambda_5EE5')
    def lambda_5EE5():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5EE5)

    @scena.Lambda('lambda_5EFD')
    def lambda_5EFD():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5EFD)

    @scena.Lambda('lambda_5F0D')
    def lambda_5F0D():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x010E, 0x0003, lambda_5F0D)

    Sleep(3000)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010100605V#506F#5P哈～该怎么说呢，\n',
            '还是老样子，是个乐天派的人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100606V#006F不过说到名誉会员，\n',
            '他应该是个相当有名的学者吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100607V#015F嗯，说不定就是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100608V#010F那么，我们先去拜访一下\n',
            '游击士协会格兰赛尔支部吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100609V要办理转属手续……\n',
            '而且要完成博士交待的委托，\n',
            '也要先和协会商量一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrSetDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100610V#505F#5P嗯，没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100611V仔细想想，\n',
            '该怎么和女王陛下会面呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100612V#007F肯定不会是去城里就能见到\n',
            '那样简单容易吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0054, 0x03, 0x02)
    OP_28(0x0054, 0x03, 0x04)
    OP_28(0x0045, 0x04, 0x02)
    OP_28(0x0045, 0x04, 0x04)
    OP_28(0x0045, 0x01, 0x0001)
    OP_28(0x0045, 0x01, 0x0002)
    OP_28(0x0045, 0x01, 0x0004)
    OP_28(0x0045, 0x01, 0x0008)
    OP_28(0x0045, 0x01, 0x0010)
    OP_28(0x0045, 0x01, 0x0020)
    OP_28(0x0045, 0x01, 0x0040)
    FormationDelMember(0x0D, 0xFF)
    EventEnd(0x00)
    CreateThread(0x001C, 0x00, 0x00, func_03_127D)

    Return()

# id: 0x0030 offset: 0x615E
@scena.Code('func_30_615E')
def func_30_615E():
    EventBegin(0x00)
    OP_20(0x000005DC)
    ChrSetDirection(0x0000, 0, 0)
    ChrTurnDirection(0x0001, 0x0000, 0)
    CameraMove(16030, 500, 7220, 1000)
    OP_21()
    PlayBGM(72)
    OP_1F(0x4B, 0x000000C8)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010101256V#004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101257V这是……钢琴声？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101258V#014F嗯，不像是放唱片的。\n',
            '应该是有人在里面弹钢琴吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101259V这个旋律，\n',
            '好像觉得在哪里听过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101260V#509F有点不好的预感呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0031 offset: 0x6281
@scena.Code('func_31_6281')
def func_31_6281():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(16020, 250, 7280, 0)
    OP_6C(315000, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetPos(0x0102, 15830, 740, 8470, 0)
    ChrSetPos(0x0101, 15830, 740, 8470, 0)
    ChrSetPos(0x0008, 15830, 740, 8470, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_72(0x0010, 0x0010)
    OP_70(0x0010, 60)
    OP_73(0x0010)
    OP_6F(0x0010, 60)

    @scena.Lambda('lambda_6305')
    def lambda_6305():
        ChrWalkTo(0x00FE, 15230, 250, 3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6305)

    Sleep(400)

    @scena.Lambda('lambda_6325')
    def lambda_6325():
        ChrWalkTo(0x00FE, 16480, 250, 3690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6325)

    Sleep(500)

    @scena.Lambda('lambda_6345')
    def lambda_6345():
        ChrWalkTo(0x00FE, 16030, 250, 5370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_6345)

    CameraMove(16100, 250, 4400, 2000)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101317V#509F我说，为什么你又这么\n',
            '理所当然地跟了出来啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101318V#035F哈·哈·哈。\n',
            '别说如此无情的话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101319V旅行要结伴才会愉快的，\n',
            '而且我也可以帮忙找人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101320V#030F还是说……\n',
            '……我妨碍到你们两个了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010101321V#580F什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101322V#031F哎呀哎呀。\n',
            '真是天真啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101323V刚刚意识到自己心中爱情花蕾的存在，\n',
            '却又害怕它绽放的少女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101324V#037F……嘻嘻，感觉不错啊，\n',
            '让我都有一些春心萌动了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101325V#503F…………呜………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101326V#014F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101327V你说的是什么意思啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101328V#031F嘻嘻，那就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrSetChipByIndex(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010101329V#08A#005F#3S嘿呀！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_666A')
    def lambda_666A():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_666A)

    PlaySE(500, 0x00, 0x64)
    OP_99(0x0101, 0x00, 0x07, 2500)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x1000)
    PlaySE(125, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 2)

    ChrTalk(
        0x0008,
        (
            '#0040101330V#038F#15A啊～～……！#10A',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_66E9')
    def lambda_66E9():
        ChrMoveTo(0x00FE, 15830, 740, 8470, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_66E9)

    OP_99(0x0101, 0x07, 0x0C, 2500)
    Sleep(300)

    PlaySE(151, 0x00, 0x64)
    Sleep(700)

    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0101, 0x1000)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#2710101331V哇哇，怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#2720101332V这位客人，请振作一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '老人的声音',
        (
            '#2730101333V不行了……\n',
            '已经翻白眼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101334V#018F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101335V不知道你在生什么气，\n',
            '不过这么做好像也太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    TerminateThread(0x0101, 0xFF)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0008, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101336V#509F……我已经避开了要害，\n',
            '只是把他打飞而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101337V不会受很重的伤的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101338V嘻嘻嘻……\n',
            '艾丝蒂尔君……真害羞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020101339V#019F……看起来的确是没什么事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_69B9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010101340V#582F好啦，接着去找人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101344V别磨磨蹭蹭的了，\n',
            '赶快去大使馆看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A17')

    def _loc_69B9(): pass

    label('loc_69B9')

    ChrTalk(
        0x0101,
        (
            '#0010101340V#582F好啦，接着去找人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101341V别磨磨蹭蹭的了，\n',
            '赶快去周游道看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A17(): pass

    label('loc_6A17')

    ChrTalk(
        0x0102,
        (
            '#0020101342V#017F（……为什么\n',
            '　要把气撒在我身上？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0032 offset: 0x6A54
@scena.Code('func_32_6A54')
def func_32_6A54():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6ADB',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101218V#010F艾丝蒂尔，还不知道\n',
            '金先生到底去了哪里呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101219V我们去东街区的\n',
            '卡尔瓦德大使馆问问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BAB')

    def _loc_6ADB(): pass

    label('loc_6ADB')

    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101220V#000F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101221V不是说金大哥\n',
            '时常在酒廊喝酒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101222V#010F啊，艾南先生\n',
            '确实这么说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101223V为了慎重起见，去周游道之前\n',
            '先到酒廊看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BAB(): pass

    label('loc_6BAB')

    Call(0, 0x0048)

    Return()

# id: 0x0033 offset: 0x6BB0
@scena.Code('func_33_6BB0')
def func_33_6BB0():
    EventBegin(0x00)
    CameraMove(16020, 250, 7280, 0)
    FormationDelMember(0x07, 0xFF)
    ChrSetPos(0x0101, 15830, 740, 8470, 0)
    ChrSetPos(0x0102, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x0010, 60)
    OP_73(0x0010)

    @scena.Lambda('lambda_6BF9')
    def lambda_6BF9():
        ChrWalkTo(0x00FE, 15230, 250, 3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6BF9)

    Sleep(400)

    @scena.Lambda('lambda_6C19')
    def lambda_6C19():
        ChrWalkTo(0x00FE, 16480, 250, 3690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6C19)

    CameraMove(16100, 250, 4400, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0102, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#000F呼～……\n',
            '肚子已经鼓鼓的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那两个人，都已经吃了那么多，\n',
            '还在不停地狼吞虎咽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101584V他们还真是合得来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F金先生是那样的体格，\n',
            '奥利维尔先生又很能吃嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101586V只要不影响到明天的比赛\n',
            '就没什么关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，确实他们两个\n',
            '都不用让人担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101588V#010F那么，\n',
            '我们也该去北街区的旅馆了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101589V艾南先生一定\n',
            '已经给我们订好房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0034 offset: 0x6DE5
@scena.Code('func_34_6DE5')
def func_34_6DE5():
    EventBegin(0x00)
    ChrSetPos(0x0101, 8940, 250, -12710, 270)
    ChrSetPos(0x0102, 8980, 250, -13870, 270)
    ChrSetPos(0x0009, 1930, 0, -4430, 0)
    ChrSetPos(0x000A, 1040, 0, -5320, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    CameraMove(9320, 440, -13270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    ChrTalk(
        0x0101,
        (
            '#000F哇……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111132V#010F我们还是\n',
            '赶快回旅馆去比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '喂，那边的人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6EE2')
    def lambda_6EE2():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6EE2)

    @scena.Lambda('lambda_6EF0')
    def lambda_6EF0():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6EF0)

    @scena.Lambda('lambda_6EFE')
    def lambda_6EFE():
        ChrWalkTo(0x00FE, 7030, 250, -10460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6EFE)

    Sleep(300)

    @scena.Lambda('lambda_6F1E')
    def lambda_6F1E():
        ChrWalkTo(0x00FE, 5920, 0, -11500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6F1E)

    CameraMove(7460, 250, -12150, 3000)

    ChrTalk(
        0x0101,
        (
            '#000F哎……\n',
            '士兵先生，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们是巡逻人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '作为恐怖活动的对策之一\n',
            '从今天开始，夜间的巡视\n',
            '要进行强化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因此，晚上９点之后请尽量\n',
            '控制行动，不要外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们也赶快回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F晚上９点……\n',
            '是不是早了点呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这是上面的决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然很抱歉，还是请你们服从命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对了……\n',
            '你们住在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111143V#010F我们住在北街区的\n',
            '罗恩鲍姆酒店。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111144V在武术大会期间\n',
            '都会住在那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '武术大会期间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '等一下，你们的脸\n',
            '好像在哪里见过的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这两个孩子，不是进入\n',
            '武术大会决赛的选手吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你这样一说，还真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，士兵先生，\n',
            '你们也去看比赛了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，是借着做警卫的时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '特别是今天白热化的比赛\n',
            '让我感到很兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '明天就是决赛了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们送你们回旅馆，\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111156V#010F明白了。\n',
            '谢谢你们的好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0035 offset: 0x729D
@scena.Code('func_35_729D')
def func_35_729D():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_74FB',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_72D0',
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
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_73ED')

    def _loc_72D0(): pass

    label('loc_72D0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_72F6',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_73ED')

    def _loc_72F6(): pass

    label('loc_72F6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_731C',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
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

    Jump('loc_73ED')

    def _loc_731C(): pass

    label('loc_731C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7343',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_73ED')

    def _loc_7343(): pass

    label('loc_7343')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7369',
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
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_73ED')

    def _loc_7369(): pass

    label('loc_7369')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_738F',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_73ED')

    def _loc_738F(): pass

    label('loc_738F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_73B4',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
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

    Jump('loc_73ED')

    def _loc_73B4(): pass

    label('loc_73B4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_73D9',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_73ED')

    def _loc_73D9(): pass

    label('loc_73D9')

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
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_73ED(): pass

    label('loc_73ED')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_74F8',
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
        'loc_74E9',
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

    def _loc_74E9(): pass

    label('loc_74E9')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_74F8(): pass

    label('loc_74F8')

    Jump('func_35_729D')

    def _loc_74FB(): pass

    label('loc_74FB')

    Return()

# id: 0x0036 offset: 0x74FC
@scena.Code('func_36_74FC')
def func_36_74FC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7569',
    )

    ChrSetPos(0x00FE, -29750, 250, -16079, 270)
    ChrWalkTo(0x00FE, -8010, 250, -16079, 3000, 0x00)
    ChrWalkTo(0x00FE, -8010, 250, 12010, 3000, 0x00)
    ChrWalkTo(0x00FE, -8010, 250, -16079, 3000, 0x00)
    ChrWalkTo(0x00FE, -29750, 250, -16079, 3000, 0x00)

    Jump('func_36_74FC')

    def _loc_7569(): pass

    label('loc_7569')

    Return()

# id: 0x0037 offset: 0x756A
@scena.Code('func_37_756A')
def func_37_756A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_75D7',
    )

    ChrSetPos(0x00FE, -29910, 250, -23870, 270)
    ChrWalkTo(0x00FE, -8440, 250, -23870, 3000, 0x00)
    ChrWalkTo(0x00FE, -8660, 250, -33400, 3000, 0x00)
    ChrWalkTo(0x00FE, -8440, 250, -23870, 3000, 0x00)
    ChrWalkTo(0x00FE, -29910, 250, -23870, 3000, 0x00)

    Jump('func_37_756A')

    def _loc_75D7(): pass

    label('loc_75D7')

    Return()

# id: 0x0038 offset: 0x75D8
@scena.Code('func_38_75D8')
def func_38_75D8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_761D',
    )

    ChrSetPos(0x00FE, -6720, 0, -19860, 270)
    ChrWalkTo(0x00FE, -31200, 0, -19860, 3000, 0x00)
    ChrWalkTo(0x00FE, -6720, 0, -19860, 3000, 0x00)

    Jump('func_38_75D8')

    def _loc_761D(): pass

    label('loc_761D')

    Return()

# id: 0x0039 offset: 0x761E
@scena.Code('func_39_761E')
def func_39_761E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7663',
    )

    ChrSetPos(0x00FE, 3810, 0, 10100, 180)
    ChrWalkTo(0x00FE, 3810, 0, -35560, 3000, 0x00)
    ChrWalkTo(0x00FE, 3810, 0, 10100, 3000, 0x00)

    Jump('func_39_761E')

    def _loc_7663(): pass

    label('loc_7663')

    Return()

# id: 0x003A offset: 0x7664
@scena.Code('func_3A_7664')
def func_3A_7664():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_76A9',
    )

    ChrSetPos(0x00FE, -3690, 0, -34890, 180)
    ChrWalkTo(0x00FE, -3690, 0, 9690, 3000, 0x00)
    ChrWalkTo(0x00FE, -3690, 0, -34890, 3000, 0x00)

    Jump('func_3A_7664')

    def _loc_76A9(): pass

    label('loc_76A9')

    Return()

# id: 0x003B offset: 0x76AA
@scena.Code('func_3B_76AA')
def func_3B_76AA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7717',
    )

    ChrSetPos(0x00FE, -1740, 0, -6830, 180)
    ChrWalkTo(0x00FE, -1740, 0, -20710, 3000, 0x00)
    ChrWalkTo(0x00FE, 2040, 0, -20890, 3000, 0x00)
    ChrWalkTo(0x00FE, 2040, 0, -6990, 3000, 0x00)
    ChrWalkTo(0x00FE, -1740, 0, -6830, 3000, 0x00)

    Jump('func_3B_76AA')

    def _loc_7717(): pass

    label('loc_7717')

    Return()

# id: 0x003C offset: 0x7718
@scena.Code('func_3C_7718')
def func_3C_7718():
    EventBegin(0x00)
    FormationDelMember(0x00, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x001C, -4970, 0, -57100, 270)
    OP_4A(0x001C, 255)
    CameraMove(-220, 250, -32150, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0104, -870, 0, -62440, 0)
    ChrSetPos(0x0102, -80, 0, -61370, 0)
    ChrSetPos(0x0108, 630, 0, -62400, 0)
    FadeIn(2000, 0)
    CameraMove(170, 0, -59880, 7000)
    Fade(1000)
    CameraMove(-80, 0, -62140, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020131001V#012F……不是一般的士兵在巡逻了，\n',
            '全部都已经换成特务兵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131002V#072F离宫被攻陷之后，\n',
            '敌人也开始豁出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131003V不过这种气氛感觉还是太夸张了一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131004V#035F#5P很好，此刻我就用鲁特琴来\n',
            '缓和一下这里的紧张气氛吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7918')
    def lambda_7918():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_7918)

    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131005V#017F如果你做了那么引人注目的事情，\n',
            '那个人一定又会飞奔而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131006V#010F我记得他是叫穆拉对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040131007V#036F#5P是、是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131008V你们两个千万不要接近帝国大使馆啊！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131009V#070F哈哈哈，我们才没有那份闲心\n',
            '跑去大使馆那里呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131010V准备完毕之后就进地下水路里去吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x001C, 255)

    Return()

# id: 0x003D offset: 0x7A8E
@scena.Code('func_3D_7A8E')
def func_3D_7A8E():
    EventBegin(0x00)
    FadeIn(2000, 0)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetChipByIndex(0x0011, 29)

    ExecExpressionWithValue(
        0x0011,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0027,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0028,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0029,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002D,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002E,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x0011, -4100, 0, -48960, 0)
    ChrSetPos(0x0013, -4010, 0, -39700, 0)
    ChrSetPos(0x0014, -2770, 0, -39710, 0)
    ChrSetPos(0x0015, -4520, 0, -30260, 0)
    ChrSetPos(0x0016, -18010, 250, -16550, 0)
    ChrSetPos(0x0017, -1760, 0, -25440, 0)
    ChrSetPos(0x0018, -4560, 0, -18230, 0)
    ChrSetPos(0x001C, -8670, 250, -15130, 0)
    ChrSetPos(0x001D, -7730, 250, -16070, 0)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrSetPos(0x001E, -4930, 0, -48010, 0)
    ChrSetPos(0x0026, 8840, 250, -36590, 0)
    ChrSetPos(0x0027, 7970, 250, -30700, 0)
    ChrSetPos(0x0028, 8039, 250, -34920, 0)
    ChrSetPos(0x0029, 5020, 0, -32530, 0)
    ChrSetPos(0x002C, 17670, 0, 1260, 270)
    ChrSetPos(0x002D, 17680, 0, -70, 270)
    ChrSetPos(0x002E, 1540, 0, -21430, 0)
    ChrSetPos(0x002A, 2700, 0, -20310, 0)
    ChrSetPos(0x002B, 1640, 0, -19200, 0)
    ChrSetPos(0x0012, 8390, 0, -38030, 0)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    CameraSetDistance(1800, 0)
    OP_6C(0, 0)
    OP_6E(580, 0)

    @scena.Lambda('lambda_7E5C')
    def lambda_7E5C():
        CameraMove(50, 0, 5920, 14000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7E5C)

    @scena.Lambda('lambda_7E74')
    def lambda_7E74():
        OP_6C(320000, 16000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_7E74)

    @scena.Lambda('lambda_7E84')
    def lambda_7E84():
        OP_67(0, 14750, -10000, 16000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_7E84)

    @scena.Lambda('lambda_7E9C')
    def lambda_7E9C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_7E9C)

    Sleep(20)

    @scena.Lambda('lambda_7EBC')
    def lambda_7EBC():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0000, lambda_7EBC)

    Sleep(20)

    @scena.Lambda('lambda_7EDC')
    def lambda_7EDC():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0000, lambda_7EDC)

    Sleep(20)

    @scena.Lambda('lambda_7EFC')
    def lambda_7EFC():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1700, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0000, lambda_7EFC)

    Sleep(20)

    @scena.Lambda('lambda_7F1C')
    def lambda_7F1C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2300, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0000, lambda_7F1C)

    Sleep(20)

    Sleep(20)

    @scena.Lambda('lambda_7F41')
    def lambda_7F41():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_7F41)

    Sleep(20)

    @scena.Lambda('lambda_7F61')
    def lambda_7F61():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2900, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_7F61)

    Sleep(20)

    @scena.Lambda('lambda_7F81')
    def lambda_7F81():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_7F81)

    Sleep(20)

    @scena.Lambda('lambda_7FA1')
    def lambda_7FA1():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2200, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_7FA1)

    @scena.Lambda('lambda_7FBC')
    def lambda_7FBC():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0000, lambda_7FBC)

    Sleep(20)

    @scena.Lambda('lambda_7FDC')
    def lambda_7FDC():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0000, lambda_7FDC)

    Sleep(20)

    @scena.Lambda('lambda_7FFC')
    def lambda_7FFC():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0000, lambda_7FFC)

    Sleep(20)

    @scena.Lambda('lambda_801C')
    def lambda_801C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0000, lambda_801C)

    Sleep(20)

    @scena.Lambda('lambda_803C')
    def lambda_803C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0000, lambda_803C)

    Sleep(20)

    @scena.Lambda('lambda_805C')
    def lambda_805C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x002A, 0x0000, lambda_805C)

    Sleep(20)

    @scena.Lambda('lambda_807C')
    def lambda_807C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0000, lambda_807C)

    Sleep(20)

    @scena.Lambda('lambda_809C')
    def lambda_809C():
        ChrMoveToRelative(0x00FE, 0, 0, 50000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x002E, 0x0000, lambda_809C)

    Sleep(1000)

    @scena.Lambda('lambda_80BC')
    def lambda_80BC():
        ChrWalkTo(0x00FE, -7530, 250, -16290, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0000, lambda_80BC)

    Sleep(1700)

    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x001A, 0x0040)
    ChrSetPos(0x001B, 4090, 0, -66400, 0)
    ChrSetPos(0x0019, 4090, 0, -68100, 0)
    ChrSetPos(0x001A, 4090, 0, -69800, 0)
    CreateThread(0x001B, 0x00, 0x00, func_3E_81A3)
    Sleep(100)

    CreateThread(0x0019, 0x00, 0x00, func_3E_81A3)
    Sleep(100)

    CreateThread(0x001A, 0x00, 0x00, func_3E_81A3)
    Sleep(20)

    @scena.Lambda('lambda_8151')
    def lambda_8151():
        ChrWalkTo(0x00FE, 5890, 0, 1540, 1350, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0000, lambda_8151)

    @scena.Lambda('lambda_816C')
    def lambda_816C():
        ChrWalkTo(0x00FE, 5470, 0, 410, 1340, 0x00)

        ExitThread()

    DispatchAsync(0x002D, 0x0000, lambda_816C)

    Sleep(7000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x003E offset: 0x81A3
@scena.Code('func_3E_81A3')
def func_3E_81A3():
    ChrWalkTo(0x00FE, 4900, 0, -42140, 10000, 0x00)
    ChrWalkTo(0x00FE, 2270, 0, -23460, 10000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    OP_97(0x00FE, 0, -23460, -90000, 9400, 0x0001)
    OP_97(0x00FE, 0, -18160, 90000, 9400, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -2450, 0, -8080, 10000, 0x00)
    ChrWalkTo(0x00FE, 780, 0, -4760, 10000, 0x00)
    ChrSetFlags(0x00FE, 0x0002)

    @scena.Lambda('lambda_8232')
    def lambda_8232():
        OP_99(0x00FE, 0x00, 0x07, 1800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_8232)

    ChrJumpTo(0x00FE, 4080, 0, -3430, 2500, 2000)
    ChrClearFlags(0x00FE, 0x0002)
    ChrWalkTo(0x00FE, 5680, 0, 33510, 10000, 0x00)

    Return()

# id: 0x003F offset: 0x826D
@scena.Code('func_3F_826D')
def func_3F_826D():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8319',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020100613V#010F还是先去协会支部打声招呼吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100614V要先办理转属手续……\n',
            '而且还有博士的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100615V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8386')

    def _loc_8319(): pass

    label('loc_8319')

    ChrTalk(
        0x0102,
        (
            '#0020100616V#010F还是先去协会支部打声招呼吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100614V要先办理转属手续……\n',
            '而且还有博士的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8386(): pass

    label('loc_8386')

    Call(0, 0x0048)

    Return()

# id: 0x0040 offset: 0x838B
@scena.Code('func_40_838B')
def func_40_838B():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8422',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020110442V#010F赶快回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110443V再磨磨蹭蹭的天就要黑了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110444V#006F嗯，现在就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8474')

    def _loc_8422(): pass

    label('loc_8422')

    ChrTalk(
        0x0102,
        (
            '#0020110442V#010F赶快回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110443V再磨磨蹭蹭的天就要黑了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8474(): pass

    label('loc_8474')

    Call(0, 0x0048)

    Return()

# id: 0x0041 offset: 0x8479
@scena.Code('func_41_8479')
def func_41_8479():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8521',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020110447V#010F已经很晚了，\n',
            '我们回酒店去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110448V该休息的时候就是要好好休息。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110449V#000F酒店在北街区对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8584')

    def _loc_8521(): pass

    label('loc_8521')

    ChrTalk(
        0x0102,
        (
            '#0020110450V#010F已经很晚了，\n',
            '我们回酒店去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110451V明天还有比赛，\n',
            '我们最好早点休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8584(): pass

    label('loc_8584')

    Call(0, 0x0048)

    Return()

# id: 0x0042 offset: 0x8589
@scena.Code('func_42_8589')
def func_42_8589():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86BD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8631',
    )

    ChrTalk(
        0x0102,
        (
            '#0020110937V#010F我想奈尔先生正在等我们吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110938V去西街区的通讯社看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110939V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86BA')

    def _loc_8631(): pass

    label('loc_8631')

    ChrTalk(
        0x0102,
        (
            '#0020110940V#010F艾丝蒂尔，那边是城门哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110941V奈尔先生的通讯社应该在西街区吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110942V#006F哦～呵呵，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86BA(): pass

    label('loc_86BA')

    Jump('loc_8721')

    def _loc_86BD(): pass

    label('loc_86BD')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110943V#010F我想奈尔先生正在等我们吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110938V去西街区的通讯社看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8721(): pass

    label('loc_8721')

    Call(0, 0x0048)

    Return()

# id: 0x0043 offset: 0x8726
@scena.Code('func_43_8726')
def func_43_8726():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87CF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020111069V#010F总之我们先回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111070V最好把奈尔的调查结果也告诉艾南先生。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110444V#006F嗯，现在就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8833')

    def _loc_87CF(): pass

    label('loc_87CF')

    ChrTalk(
        0x0102,
        (
            '#0020111069V#010F总之我们先回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111070V最好把奈尔的调查结果也告诉艾南先生。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8833(): pass

    label('loc_8833')

    Call(0, 0x0048)

    Return()

# id: 0x0044 offset: 0x8838
@scena.Code('func_44_8838')
def func_44_8838():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88BA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080111935V#070F呼，已经傍晚了。\n',
            '我们尽量不要外出了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111936V今天就别修行了，\n',
            '赶快去城里参加晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8930')

    def _loc_88BA(): pass

    label('loc_88BA')

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111937V#070F喂喂，\n',
            '难道你们还打算外出吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111938V就算是再热衷于修炼，\n',
            '现在还是快去参加晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8930(): pass

    label('loc_8930')

    Call(0, 0x0048)

    Return()

# id: 0x0045 offset: 0x8935
@scena.Code('func_45_8935')
def func_45_8935():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_89A0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080131011V#070F现在没空去街道外面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131012V做好准备后就向地下水路进发吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A01')

    def _loc_89A0(): pass

    label('loc_89A0')

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080131013V#070F现在没空去街道外面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131014V做好准备后就向地下水路进发吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A01(): pass

    label('loc_8A01')

    Call(0, 0x0048)

    Return()

# id: 0x0046 offset: 0x8A06
@scena.Code('func_46_8A06')
def func_46_8A06():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B1A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140901V#501F啊，这边是城外……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140902V#000F我说，\n',
            '我们还是在城里再散散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140909V#010F嗯，好啊。\n',
            '还有很多地方没看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140910V如果觉得累了，\n',
            '就去东街区那个小公园休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140911V#001F嗯，好吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BF4')

    def _loc_8B1A(): pass

    label('loc_8B1A')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140912V#000F我说，\n',
            '我们还是在城里再散散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140909V#010F嗯，好啊。\n',
            '还有很多地方没看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140910V如果觉得累了，\n',
            '就去东街区那个小公园休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140911V#001F嗯，好吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BF4(): pass

    label('loc_8BF4')

    Call(0, 0x0048)

    Return()

# id: 0x0047 offset: 0x8BF9
@scena.Code('func_47_8BF9')
def func_47_8BF9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 4, 0x62C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8CF7',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8CA1',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111296V#012F艾丝蒂尔，\n',
            '已经快到指定的时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111297V我们赶快去大圣堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111298V#002F嗯……明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF3')

    def _loc_8CA1(): pass

    label('loc_8CA1')

    ChrTalk(
        0x0102,
        (
            '#0020111299V#012F已经快到指定的时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111297V我们赶快去大圣堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8CF3(): pass

    label('loc_8CF3')

    Call(0, 0x0048)

    def _loc_8CF7(): pass

    label('loc_8CF7')

    Return()

# id: 0x0048 offset: 0x8CF8
@scena.Code('func_48_8CF8')
def func_48_8CF8():
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0049 offset: 0x8D14
@scena.Code('func_49_8D14')
def func_49_8D14():
    OP_13(0x00B9)

    Return()

# id: 0x004A offset: 0x8D18
@scena.Code('func_4A_8D18')
def func_4A_8D18():
    OP_13(0x00B0)

    Return()

# id: 0x004B offset: 0x8D1C
@scena.Code('func_4B_8D1C')
def func_4B_8D1C():
    OP_13(0x00B2)

    Return()

# id: 0x004C offset: 0x8D20
@scena.Code('func_4C_8D20')
def func_4C_8D20():
    OP_13(0x00AE)

    Return()

# id: 0x004D offset: 0x8D24
@scena.Code('func_4D_8D24')
def func_4D_8D24():
    OP_13(0x00B3)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
