import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4101.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4101._SN', 'ED6_DT01/T4101_1._SN', 'ED6_DT01/T4101_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02190._CH', 'ED6_DT07/CH02190P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT06/CH20101._CH', 'ED6_DT06/CH20101P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT06/CH20101._CH', 'ED6_DT06/CH20101P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT06/CH20090._CH', 'ED6_DT06/CH20090P._CP'),
        ('ED6_DT06/CH20091._CH', 'ED6_DT06/CH20091P._CP'),
        ('ED6_DT06/CH20147._CH', 'ED6_DT06/CH20147P._CP'),
        ('ED6_DT06/CH20099._CH', 'ED6_DT06/CH20099P._CP'),
        ('ED6_DT06/CH20103._CH', 'ED6_DT06/CH20103P._CP'),
        ('ED6_DT06/CH20107._CH', 'ED6_DT06/CH20107P._CP'),
        ('ED6_DT06/CH20108._CH', 'ED6_DT06/CH20108P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
    ]

# id: 0x10001 offset: 0x21A
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
            name                = '穆拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '莉珐',
            x                   = 109490,
            z                   = 1450,
            y                   = 23040,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            name                = '接待员',
            x                   = 109630,
            z                   = 1500,
            y                   = 33010,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '迪恩',
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
            name                = '雷斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 70000,
            z                   = 250,
            y                   = 69110,
            direction           = 18,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 79960,
            z                   = 250,
            y                   = 69120,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 76080,
            z                   = 250,
            y                   = -7320,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 65990,
            z                   = 250,
            y                   = -7150,
            direction           = 360,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 44730,
            z                   = 250,
            y                   = 46870,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 44900,
            z                   = 250,
            y                   = 28910,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0012,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0013,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0014,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0015,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0016,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0017,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0018,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0019,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001A,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x001B,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉尔夫',
            x                   = 107860,
            z                   = 1250,
            y                   = 32850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '士兵贝尔坎',
            x                   = 74970,
            z                   = 0,
            y                   = 69190,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '士兵达克特',
            x                   = 71040,
            z                   = 0,
            y                   = -6930,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '娜碧',
            x                   = 105230,
            z                   = 1250,
            y                   = 36670,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '米亚尔',
            x                   = 101110,
            z                   = 250,
            y                   = 31490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '戈万',
            x                   = 104590,
            z                   = 1000,
            y                   = 29040,
            direction           = 24,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '帕菲',
            x                   = 99900,
            z                   = 250,
            y                   = 35240,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '娜娜',
            x                   = 101180,
            z                   = 250,
            y                   = 36470,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 70490,
            z                   = 250,
            y                   = 6990,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 71500,
            z                   = 750,
            y                   = 7870,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '索露贝',
            x                   = 37580,
            z                   = 1250,
            y                   = 49800,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '卡拉',
            x                   = 40270,
            z                   = 1250,
            y                   = 51990,
            direction           = 91,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '卢希娅',
            x                   = 40960,
            z                   = 1250,
            y                   = 50060,
            direction           = 169,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '卡拉莉丝',
            x                   = 36250,
            z                   = 1250,
            y                   = 42940,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '尼莫',
            x                   = 38980,
            z                   = 1250,
            y                   = 41620,
            direction           = 254,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '拉奥尼',
            x                   = 81160,
            z                   = 0,
            y                   = -2940,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '梅夏',
            x                   = 69020,
            z                   = 250,
            y                   = 4960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '维尔娜婆婆',
            x                   = 63010,
            z                   = 0,
            y                   = 62930,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 93700,
            z                   = 0,
            y                   = 32900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 47210,
            z                   = 250,
            y                   = 4820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 54000,
            z                   = 250,
            y                   = 10090,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 93700,
            z                   = 0,
            y                   = 32900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 47210,
            z                   = 250,
            y                   = 4820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 54000,
            z                   = 250,
            y                   = 10090,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48190,
            z                   = 250,
            y                   = 52050,
            direction           = 111,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48120,
            z                   = 250,
            y                   = 51230,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48030,
            z                   = 250,
            y                   = 47650,
            direction           = 248,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48730,
            z                   = 250,
            y                   = 44340,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48460,
            z                   = 250,
            y                   = 45120,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 53030,
            z                   = 250,
            y                   = 48510,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 53030,
            z                   = 250,
            y                   = 47600,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 40260,
            z                   = 1250,
            y                   = 49220,
            direction           = 226,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 41010,
            z                   = 1250,
            y                   = 49820,
            direction           = 206,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 44130,
            z                   = 250,
            y                   = 67000,
            direction           = 185,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 47760,
            z                   = 250,
            y                   = 74930,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48690,
            z                   = 250,
            y                   = 75760,
            direction           = 293,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 56730,
            z                   = 250,
            y                   = 24550,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 55820,
            z                   = 250,
            y                   = 23780,
            direction           = 36,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 58580,
            z                   = 1250,
            y                   = 24420,
            direction           = 276,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 53090,
            z                   = 250,
            y                   = 21320,
            direction           = 269,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48730,
            z                   = 250,
            y                   = 35180,
            direction           = 136,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 68250,
            z                   = 0,
            y                   = 1870,
            direction           = 35,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 69310,
            z                   = 250,
            y                   = 3150,
            direction           = 211,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002E,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 72270,
            z                   = 0,
            y                   = 2150,
            direction           = 142,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x002F,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 70950,
            z                   = 0,
            y                   = -1170,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0030,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 51120,
            z                   = 0,
            y                   = 1090,
            direction           = 214,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0031,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 56190,
            z                   = 250,
            y                   = 6020,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0032,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 61700,
            z                   = 250,
            y                   = 3050,
            direction           = 189,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0033,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48860,
            z                   = 250,
            y                   = 8420,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0034,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 49200,
            z                   = 250,
            y                   = 9460,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0035,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 48880,
            z                   = 250,
            y                   = 15620,
            direction           = 63,
            word_0E             = 0,
            dword_10            = 36,
            chipIndex           = 36,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0036,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 69950,
            z                   = 250,
            y                   = 60930,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0037,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 59720,
            z                   = 250,
            y                   = 66950,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0038,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 60800,
            z                   = 250,
            y                   = 66950,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0039,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 51510,
            z                   = 0,
            y                   = 67330,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x003A,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = 17760,
            z                   = 0,
            y                   = 63880,
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
            name                = '王都格兰赛尔·南街区',
            x                   = 29270,
            z                   = 0,
            y                   = -950,
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
            name                = '王都格兰赛尔·空港',
            x                   = 51010,
            z                   = 0,
            y                   = 102170,
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
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xC9A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xC9A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 73540,
            y           = -1000,
            z           = 49000,
            range       = 66420,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000A028,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = 37600,
            y           = -1000,
            z           = 49280,
            range       = 5000,
            dword_10    = 0x00001388,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 109720,
            y           = 1000,
            z           = 32980,
            range       = 2000,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002A,
        ),
        ScenaEventData(
            x           = 76740,
            y           = 1000,
            z           = 23010,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 69950,
            y           = 1000,
            z           = 14290,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 63260,
            y           = 1000,
            z           = 22960,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 69910,
            y           = 1000,
            z           = 31710,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 42920,
            y           = 0,
            z           = 81110,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002C,
        ),
        ScenaEventData(
            x           = 70940,
            y           = 0,
            z           = -9490,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002D,
        ),
        ScenaEventData(
            x           = 75010,
            y           = 0,
            z           = 71300,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002E,
        ),
    )

# id: 0x10004 offset: 0xDDA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 124880,
            triggerZ            = -3500,
            triggerY            = 70940,
            triggerRange        = 800,
            actorX              = 124880,
            actorZ              = -2500,
            actorY              = 70940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75060,
            triggerZ            = 0,
            triggerY            = 71950,
            triggerRange        = 800,
            actorX              = 75060,
            actorZ              = 1000,
            actorY              = 71950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0027,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 70950,
            triggerZ            = 0,
            triggerY            = -9930,
            triggerRange        = 800,
            actorX              = 70950,
            actorZ              = 1000,
            actorY              = -9930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0028,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 108180,
            triggerZ            = 1250,
            triggerY            = 23100,
            triggerRange        = 800,
            actorX              = 109490,
            actorZ              = 2950,
            actorY              = 23040,
            flags               = 0x007E,
            talkScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72040,
            triggerZ            = 250,
            triggerY            = 44930,
            triggerRange        = 3000,
            actorX              = 74100,
            actorZ              = 750,
            actorY              = 45100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 68020,
            triggerZ            = 250,
            triggerY            = 44970,
            triggerRange        = 3000,
            actorX              = 66070,
            actorZ              = 750,
            actorY              = 45100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 38820,
            triggerZ            = 1250,
            triggerY            = 36920,
            triggerRange        = 800,
            actorX              = 38820,
            actorZ              = 2250,
            actorY              = 36920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xED6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_EF2',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0D_2271)

    def _loc_EF2(): pass

    label('loc_EF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_F05',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0F_2437)

    def _loc_F05(): pass

    label('loc_F05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_F13',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_10_3522)

    def _loc_F13(): pass

    label('loc_F13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_F21',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_1C_4057)

    def _loc_F21(): pass

    label('loc_F21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Return,
        ),
        'loc_F2F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    Event(0, func_1E_4C9F)

    def _loc_F2F(): pass

    label('loc_F2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Return,
        ),
        'loc_F42',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    Event(0, func_1F_63FF)

    def _loc_F42(): pass

    label('loc_F42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Return,
        ),
        'loc_F5E',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    Event(0, func_20_66D3)

    def _loc_F5E(): pass

    label('loc_F5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Return,
        ),
        'loc_F77',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_23_9615)

    def _loc_F77(): pass

    label('loc_F77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1104',
    )

    ChrSetFlags(0x002B, 0x0010)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetPos(0x0024, 37580, 1250, 48810, 279)
    ChrSetPos(0x0027, 38460, 1250, 48810, 90)
    ChrSetPos(0x0028, 39430, 1250, 48810, 270)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002E, 36280, 1250, 42890, 45)
    ChrSetPos(0x002C, 37150, 1250, 43970, 225)
    ChrSetPos(0x002D, 40850, 1250, 45260, 0)
    ChrSetPos(0x002F, 40050, 1250, 45290, 0)
    ChrSetFlags(0x002D, 0x0010)
    ChrSetFlags(0x002F, 0x0010)
    CreateThread(0x002D, 0x00, 0x00, func_02_178A)
    CreateThread(0x002F, 0x00, 0x00, func_02_178A)
    CreateThread(0x0031, 0x00, 0x00, func_07_1C50)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    CreateThread(0x0035, 0x00, 0x00, func_0C_21E4)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrSetFlags(0x003C, 0x0010)
    ChrClearFlags(0x003D, 0x0080)
    ChrSetFlags(0x003D, 0x0010)
    ChrClearFlags(0x003E, 0x0080)
    ChrClearFlags(0x003F, 0x0080)
    ChrClearFlags(0x0040, 0x0080)
    ChrClearFlags(0x0041, 0x0080)
    ChrClearFlags(0x0042, 0x0080)
    ChrClearFlags(0x0043, 0x0080)
    ChrClearFlags(0x0044, 0x0080)
    ChrClearFlags(0x0045, 0x0080)
    ChrClearFlags(0x0046, 0x0080)
    ChrClearFlags(0x0047, 0x0080)
    ChrClearFlags(0x0048, 0x0080)
    ChrClearFlags(0x0049, 0x0080)
    ChrClearFlags(0x004A, 0x0080)
    ChrSetFlags(0x004A, 0x0010)
    ChrClearFlags(0x004B, 0x0080)
    ChrSetFlags(0x004B, 0x0010)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrClearFlags(0x004E, 0x0080)
    ChrClearFlags(0x004F, 0x0080)
    ChrSetFlags(0x004F, 0x0010)
    ChrClearFlags(0x0050, 0x0080)
    ChrClearFlags(0x0051, 0x0080)
    ChrClearFlags(0x0052, 0x0080)
    ChrClearFlags(0x0053, 0x0080)
    ChrClearFlags(0x0054, 0x0080)
    ChrClearFlags(0x0055, 0x0080)
    ChrSetFlags(0x0055, 0x0010)
    ChrClearFlags(0x0056, 0x0080)
    ChrSetFlags(0x0056, 0x0010)
    ChrClearFlags(0x0057, 0x0080)

    Jump('loc_146B')

    def _loc_1104(): pass

    label('loc_1104')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_11A8',
    )

    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetPos(0x0024, 48500, 250, 41910, 90)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002E, 36280, 1250, 42890, 45)
    ChrSetPos(0x002C, 37150, 1250, 43970, 225)
    ChrSetFlags(0x002E, 0x0010)
    ChrSetFlags(0x002C, 0x0010)
    ChrSetPos(0x002D, 40150, 1250, 48060, 180)
    ChrSetPos(0x002F, 40150, 1250, 46580, 0)
    CreateThread(0x002D, 0x00, 0x00, func_02_178A)
    CreateThread(0x002F, 0x00, 0x00, func_02_178A)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)

    Jump('loc_146B')

    def _loc_11A8(): pass

    label('loc_11A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1262',
    )

    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetPos(0x0024, 53110, 250, 44970, 270)
    ChrSetPos(0x0025, 53210, 250, 25020, 270)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002E, 36280, 1250, 42890, 45)
    ChrSetPos(0x002C, 37150, 1250, 43970, 225)
    ChrSetFlags(0x002E, 0x0010)
    ChrSetFlags(0x002C, 0x0010)
    ChrSetPos(0x002D, 40150, 1250, 48060, 180)
    ChrSetPos(0x002F, 40150, 1250, 46580, 0)
    ChrSetFlags(0x002D, 0x0010)
    ChrSetFlags(0x002F, 0x0010)
    CreateThread(0x002D, 0x00, 0x00, func_02_178A)
    CreateThread(0x002F, 0x00, 0x00, func_02_178A)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)

    Jump('loc_146B')

    def _loc_1262(): pass

    label('loc_1262')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1306',
    )

    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetPos(0x0024, 48500, 250, 41910, 90)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002E, 36280, 1250, 42890, 45)
    ChrSetPos(0x002C, 37150, 1250, 43970, 225)
    ChrSetPos(0x002D, 40150, 1250, 48060, 180)
    ChrSetPos(0x002F, 40150, 1250, 46580, 0)
    ChrSetFlags(0x002D, 0x0010)
    ChrSetFlags(0x002F, 0x0010)
    CreateThread(0x002D, 0x00, 0x00, func_02_178A)
    CreateThread(0x002F, 0x00, 0x00, func_02_178A)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)

    Jump('loc_146B')

    def _loc_1306(): pass

    label('loc_1306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1357',
    )

    ChrSetPos(0x002C, 40920, 1250, 52020, 190)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002F, 38410, 1250, 45900, 45)
    ChrSetFlags(0x002F, 0x0010)
    CreateThread(0x002F, 0x00, 0x00, func_02_178A)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)

    Jump('loc_146B')

    def _loc_1357(): pass

    label('loc_1357')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_13CA',
    )

    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrSetPos(0x0028, 72000, 250, 44380, 0)
    ChrSetPos(0x0027, 72000, 250, 45900, 180)
    ChrSetPos(0x0024, 48500, 250, 41910, 90)
    ChrSetPos(0x0026, 99020, 250, 30860, 270)
    ChrSetPos(0x0025, 100930, 250, 35130, 315)

    Jump('loc_146B')

    def _loc_13CA(): pass

    label('loc_13CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_13D4',
    )

    Jump('loc_146B')

    def _loc_13D4(): pass

    label('loc_13D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1450',
    )

    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, 39000, 1250, 49410, 270)
    CreateThread(0x001F, 0x00, 0x00, func_02_178A)
    ChrSetPos(0x0028, 72000, 250, 44380, 0)
    ChrSetPos(0x0027, 72000, 250, 45900, 180)
    ChrSetPos(0x0024, 40440, 1250, 49390, 270)
    ChrSetPos(0x0026, 99020, 250, 30860, 270)
    ChrSetPos(0x0025, 100930, 250, 35130, 315)

    Jump('loc_146B')

    def _loc_1450(): pass

    label('loc_1450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_145A',
    )

    Jump('loc_146B')

    def _loc_145A(): pass

    label('loc_145A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1464',
    )

    Jump('loc_146B')

    def _loc_1464(): pass

    label('loc_1464')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_146B',
    )

    def _loc_146B(): pass

    label('loc_146B')

    Return()

# id: 0x0001 offset: 0x146C
@scena.Code('func_01_146C')
def func_01_146C():
    OP_16(0x02, 4000, -46000, -90000, 196700)

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
        'loc_14B1',
    )

    OP_B1('t4101_y')

    Jump('loc_14D0')

    def _loc_14B1(): pass

    label('loc_14B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Return,
        ),
        'loc_14C7',
    )

    OP_B1('t4101_y')
    ClearScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))

    Jump('loc_14D0')

    def _loc_14C7(): pass

    label('loc_14C7')

    OP_B1('t4101_n')

    def _loc_14D0(): pass

    label('loc_14D0')

    OP_72(0x000E, 0x0020)
    OP_72(0x000F, 0x0020)
    OP_6F(0x000E, 118)
    OP_6F(0x000F, 118)
    OP_72(0x0005, 0x0010)
    OP_72(0x0008, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0007, 0x0010)
    OP_72(0x0009, 0x0010)
    OP_72(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1544',
    )

    OP_1B(0x0A, 0x02, 0x0002)
    OP_6F(0x0006, 60)
    OP_6F(0x0007, 60)
    ChrClearFlags(0x000B, 0x0080)

    Jump('loc_1549')

    def _loc_1544(): pass

    label('loc_1544')

    ChrSetFlags(0x000B, 0x0080)

    def _loc_1549(): pass

    label('loc_1549')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 0, 0x630)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1562',
    )

    OP_72(0x000B, 0x0010)
    OP_65(0x00, 0x0001)

    def _loc_1562(): pass

    label('loc_1562')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1575',
    )

    OP_1B(0x09, 0x00, 0x0026)

    def _loc_1575(): pass

    label('loc_1575')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_159F',
    )

    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x000B, 0x0010)
    OP_72(0x0004, 0x0010)

    def _loc_159F(): pass

    label('loc_159F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1675',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    CreateThread(0x000F, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0010, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0011, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0012, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0013, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0014, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0015, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0016, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0017, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0018, 0x01, 0x00, func_11_3A24)
    CreateThread(0x0019, 0x01, 0x00, func_11_3A24)
    CreateThread(0x001A, 0x01, 0x00, func_11_3A24)
    CreateThread(0x001B, 0x01, 0x00, func_11_3A24)
    CreateThread(0x001C, 0x01, 0x00, func_11_3A24)
    CreateThread(0x001D, 0x01, 0x00, func_11_3A24)
    CreateThread(0x001E, 0x01, 0x00, func_11_3A24)

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1675(): pass

    label('loc_1675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_1681',
    )

    OP_72(0x0010, 0x0004)

    def _loc_1681(): pass

    label('loc_1681')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1781',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0x04, 0x00FF, 45590, 250, 45800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 55330, 250, 22770, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 70130, 250, 6410, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 86040, 250, 22980, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_1789')

    def _loc_1781(): pass

    label('loc_1781')

    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)

    def _loc_1789(): pass

    label('loc_1789')

    Return()

# id: 0x0002 offset: 0x178A
@scena.Code('func_02_178A')
def func_02_178A():
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
        0x0005,
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
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17BA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_18FC')

    def _loc_17BA(): pass

    label('loc_17BA')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17D3',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_18FC')

    def _loc_17D3(): pass

    label('loc_17D3')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17EC',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_18FC')

    def _loc_17EC(): pass

    label('loc_17EC')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1805',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_18FC')

    def _loc_1805(): pass

    label('loc_1805')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_181E',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_18FC')

    def _loc_181E(): pass

    label('loc_181E')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1837',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_18FC')

    def _loc_1837(): pass

    label('loc_1837')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1850',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_18FC')

    def _loc_1850(): pass

    label('loc_1850')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1869',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_18FC')

    def _loc_1869(): pass

    label('loc_1869')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1882',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_18FC')

    def _loc_1882(): pass

    label('loc_1882')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_189B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_18FC')

    def _loc_189B(): pass

    label('loc_189B')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18B4',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_18FC')

    def _loc_18B4(): pass

    label('loc_18B4')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18CD',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_18FC')

    def _loc_18CD(): pass

    label('loc_18CD')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18E6',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_18FC')

    def _loc_18E6(): pass

    label('loc_18E6')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18FC',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_18FC(): pass

    label('loc_18FC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1911',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_18FC')

    def _loc_1911(): pass

    label('loc_1911')

    Return()

# id: 0x0003 offset: 0x1912
@scena.Code('func_03_1912')
def func_03_1912():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1935',
    )

    OP_8D(0x00FE, 39320, 51160, 42580, 48520, 3000)

    Jump('func_03_1912')

    def _loc_1935(): pass

    label('loc_1935')

    Return()

# id: 0x0004 offset: 0x1936
@scena.Code('func_04_1936')
def func_04_1936():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1959',
    )

    OP_8D(0x00FE, 37230, 39170, 41090, 44360, 4000)

    Jump('func_04_1936')

    def _loc_1959(): pass

    label('loc_1959')

    Return()

# id: 0x0005 offset: 0x195A
@scena.Code('func_05_195A')
def func_05_195A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1A46',
    )

    ChrWalkTo(0x00FE, 52470, 0, -2940, 2500, 0x00)
    ChrWalkTo(0x00FE, 50290, 0, 140, 2500, 0x00)
    ChrWalkTo(0x00FE, 50290, 0, 62250, 2500, 0x00)
    ChrWalkTo(0x00FE, 53220, 0, 65700, 2500, 0x00)
    ChrWalkTo(0x00FE, 88770, 0, 64700, 2500, 0x00)
    ChrWalkTo(0x00FE, 90900, 0, 64390, 2500, 0x00)
    ChrWalkTo(0x00FE, 91360, 0, 33390, 2500, 0x00)
    ChrSetDirection(0x0030, 90, 400)
    Sleep(4000)

    ChrWalkTo(0x00FE, 91360, 0, 32390, 2500, 0x00)
    ChrSetDirection(0x0030, 90, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 90450, 0, 1230, 2500, 0x00)
    ChrWalkTo(0x00FE, 88850, 0, -1860, 2500, 0x00)

    Jump('func_05_195A')

    def _loc_1A46(): pass

    label('loc_1A46')

    Return()

# id: 0x0006 offset: 0x1A47
@scena.Code('func_06_1A47')
def func_06_1A47():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1C4F',
    )

    ChrWalkTo(0x00FE, 55020, 250, 4960, 2500, 0x00)
    ChrWalkTo(0x00FE, 55020, 250, 23020, 2500, 0x00)
    ChrWalkTo(0x00FE, 59950, 1250, 23020, 2500, 0x00)
    ChrWalkTo(0x00FE, 59950, 1250, 33970, 2500, 0x00)
    ChrWalkTo(0x00FE, 64090, 1250, 36040, 2500, 0x00)
    ChrWalkTo(0x00FE, 67880, 1250, 36040, 2500, 0x00)
    ChrWalkTo(0x00FE, 69960, 1250, 38000, 2500, 0x00)
    ChrWalkTo(0x00FE, 70090, 1250, 51890, 2500, 0x00)
    ChrWalkTo(0x00FE, 78010, 1250, 51890, 2500, 0x00)
    ChrWalkTo(0x00FE, 78010, 1250, 47670, 2500, 0x00)
    ChrWalkTo(0x00FE, 80080, 1250, 44020, 2500, 0x00)
    ChrWalkTo(0x00FE, 80080, 1250, 11710, 2500, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B71',
    )

    OP_62(0x0031, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(500)

    ChrSetDirection(0x0031, 225, 400)
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    OP_4A(0x0031, 255)

    def _loc_1B71(): pass

    label('loc_1B71')

    ChrWalkTo(0x00FE, 72040, 1250, 11710, 2500, 0x00)
    ChrWalkTo(0x00FE, 68840, 1250, 10030, 2500, 0x00)
    ChrSetDirection(0x0031, 180, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C33',
    )

    ChrTurnDirection(0x0029, 0x0031, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1BD8',
    )

    OP_62(0x0029, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_1C27')

    def _loc_1BD8(): pass

    label('loc_1BD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1C01',
    )

    OP_62(0x0029, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_1C27')

    def _loc_1C01(): pass

    label('loc_1C01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1C27',
    )

    OP_62(0x0029, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_1C27(): pass

    label('loc_1C27')

    Sleep(500)

    ChrSetDirection(0x0029, 180, 400)

    def _loc_1C33(): pass

    label('loc_1C33')

    Sleep(1500)

    ChrWalkTo(0x00FE, 68840, 250, 5830, 2500, 0x00)

    Jump('func_06_1A47')

    def _loc_1C4F(): pass

    label('loc_1C4F')

    Return()

# id: 0x0007 offset: 0x1C50
@scena.Code('func_07_1C50')
def func_07_1C50():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D2F',
    )

    ChrWalkTo(0x00FE, 55020, 250, 4960, 2500, 0x00)
    ChrWalkTo(0x00FE, 55020, 250, 59020, 2500, 0x00)
    ChrWalkTo(0x00FE, 85030, 250, 59020, 2500, 0x00)
    ChrWalkTo(0x00FE, 85030, 250, 23000, 2500, 0x00)
    ChrWalkTo(0x00FE, 80140, 1250, 23000, 2500, 0x00)
    ChrWalkTo(0x00FE, 80080, 1250, 11710, 2500, 0x00)
    ChrWalkTo(0x00FE, 72040, 1250, 11710, 2500, 0x00)
    ChrWalkTo(0x00FE, 68840, 1250, 10030, 2500, 0x00)
    ChrSetDirection(0x0031, 0, 400)
    ChrTurnDirection(0x0029, 0x0031, 400)
    Sleep(500)

    ChrSetDirection(0x0029, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 68840, 250, 5830, 2500, 0x00)

    Jump('func_07_1C50')

    def _loc_1D2F(): pass

    label('loc_1D2F')

    Return()

# id: 0x0008 offset: 0x1D30
@scena.Code('func_08_1D30')
def func_08_1D30():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1DDC',
    )

    ChrWalkTo(0x00FE, 52890, 0, 62930, 2000, 0x00)
    ChrWalkTo(0x00FE, 51980, 0, 62040, 2000, 0x00)
    ChrWalkTo(0x00FE, 51980, 0, 2070, 2000, 0x00)
    ChrWalkTo(0x00FE, 52970, 0, 830, 2000, 0x00)
    ChrWalkTo(0x00FE, 87440, 0, 830, 2000, 0x00)
    ChrWalkTo(0x00FE, 88280, 0, 1720, 2000, 0x00)
    ChrWalkTo(0x00FE, 88280, 0, 61270, 2000, 0x00)
    ChrWalkTo(0x00FE, 87410, 40, 62930, 2000, 0x00)

    Jump('func_08_1D30')

    def _loc_1DDC(): pass

    label('loc_1DDC')

    Return()

# id: 0x0009 offset: 0x1DDD
@scena.Code('func_09_1DDD')
def func_09_1DDD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1E81',
    )

    ChrWalkTo(0x00FE, 93700, 0, 40380, 2500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 93700, 0, 32900, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 93700, 0, 25070, 2500, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 93700, 0, 32900, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    Jump('func_09_1DDD')

    def _loc_1E81(): pass

    label('loc_1E81')

    Return()

# id: 0x000A offset: 0x1E82
@scena.Code('func_0A_1E82')
def func_0A_1E82():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_20DE',
    )

    ChrWalkTo(0x00FE, 47210, 250, 58890, 2500, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 43020, 250, 59890, 2500, 0x00)
    ChrWalkTo(0x00FE, 43020, 250, 68950, 2500, 0x00)
    ChrWalkTo(0x00FE, 47030, 250, 68950, 2500, 0x00)
    ChrSetDirection(0x00FE, 135, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 47030, 250, 81070, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 54910, 250, 81070, 2500, 0x00)
    ChrWalkTo(0x00FE, 54910, 250, 68830, 2500, 0x00)
    ChrWalkTo(0x00FE, 72630, 250, 68830, 2500, 0x00)
    ChrWalkTo(0x00FE, 75010, 0, 67100, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 87700, 250, 67100, 2500, 0x00)
    ChrWalkTo(0x00FE, 89260, 250, 68240, 2500, 0x00)
    ChrWalkTo(0x00FE, 94020, 250, 68050, 2500, 0x00)
    ChrWalkTo(0x00FE, 94020, 250, 44680, 2500, 0x00)
    ChrWalkTo(0x00FE, 97850, 250, 44680, 2500, 0x00)
    ChrWalkTo(0x00FE, 97850, 250, 21480, 2500, 0x00)
    ChrWalkTo(0x00FE, 94010, 250, 21480, 2500, 0x00)
    ChrWalkTo(0x00FE, 94010, 250, 5180, 2500, 0x00)
    ChrWalkTo(0x00FE, 91030, 0, 2950, 2500, 0x00)
    ChrWalkTo(0x00FE, 91030, 0, -3010, 2500, 0x00)
    ChrWalkTo(0x00FE, 72790, 0, -3010, 2500, 0x00)
    ChrWalkTo(0x00FE, 71040, 0, -4620, 2500, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 69480, 0, -3010, 2500, 0x00)
    ChrWalkTo(0x00FE, 46540, 0, -3010, 2500, 0x00)
    ChrWalkTo(0x00FE, 43510, 0, -900, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 43320, 250, 4930, 2500, 0x00)
    ChrWalkTo(0x00FE, 47850, 250, 5020, 2500, 0x00)

    Jump('func_0A_1E82')

    def _loc_20DE(): pass

    label('loc_20DE')

    Return()

# id: 0x000B offset: 0x20DF
@scena.Code('func_0B_20DF')
def func_0B_20DF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_21E3',
    )

    ChrWalkTo(0x00FE, 54000, 250, 4230, 2500, 0x00)
    ChrSetDirection(0x00FE, 225, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 85860, 250, 4230, 2500, 0x00)
    ChrSetDirection(0x00FE, 135, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 85060, 250, 59050, 2500, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 69510, 250, 59050, 2500, 0x00)
    ChrWalkTo(0x00FE, 69510, 1250, 53930, 2500, 0x00)
    ChrWalkTo(0x00FE, 61050, 1250, 53930, 2500, 0x00)
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 61050, 1250, 47180, 2500, 0x00)
    ChrWalkTo(0x00FE, 55030, 250, 47180, 2500, 0x00)
    ChrWalkTo(0x00FE, 55030, 250, 25990, 2500, 0x00)
    ChrWalkTo(0x00FE, 53830, 250, 24100, 2500, 0x00)

    Jump('func_0B_20DF')

    def _loc_21E3(): pass

    label('loc_21E3')

    Return()

# id: 0x000C offset: 0x21E4
@scena.Code('func_0C_21E4')
def func_0C_21E4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2270',
    )

    ChrWalkTo(0x00FE, 53700, 250, 3890, 2500, 0x00)
    ChrSetDirection(0x00FE, 225, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 86060, 250, 3890, 2500, 0x00)
    ChrSetDirection(0x00FE, 135, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 86060, 250, 60110, 2500, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, 53830, 250, 60110, 2500, 0x00)
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(1500)

    Jump('func_0C_21E4')

    def _loc_2270(): pass

    label('loc_2270')

    Return()

# id: 0x000D offset: 0x2271
@scena.Code('func_0D_2271')
def func_0D_2271():
    EventBegin(0x00)
    ChrSetPos(0x0008, 66340, 6500, -8490, 0)
    ChrClearFlags(0x0008, 0x0080)
    CameraMove(69990, 250, 45010, 0)
    OP_67(0, 13780, -10000, 0)
    CameraSetDistance(1890, 0)
    OP_6C(315000, 0)
    OP_6E(576, 0)
    OP_77(0xB4, 0xB4, 0xB4, 0x00, 0x00000000)
    LoadEffect(0x00, 'map\\\\mp014_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 69990, 250, 45010, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 74960, 1650, 71540, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0001, 0x02, 0x00, func_0E_23D3)

    @scena.Lambda('lambda_235A')
    def lambda_235A():
        OP_6C(0, 11000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_235A)

    Sleep(3000)

    @scena.Lambda('lambda_236F')
    def lambda_236F():
        CameraMove(74960, 1650, 71540, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_236F)

    @scena.Lambda('lambda_2387')
    def lambda_2387():
        OP_67(0, 8880, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2387)

    @scena.Lambda('lambda_239F')
    def lambda_239F():
        CameraSetDistance(3490, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_239F)

    @scena.Lambda('lambda_23AF')
    def lambda_23AF():
        OP_6E(262, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_23AF)

    Sleep(6000)

    OP_13(0x00BD)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4112._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x23D3
@scena.Code('func_0E_23D3')
def func_0E_23D3():
    Sleep(700)

    OP_24(0x01C9, 0x28)
    Sleep(300)

    OP_24(0x01C9, 0x32)
    Sleep(300)

    OP_24(0x01C9, 0x3C)
    Sleep(300)

    OP_24(0x01C9, 0x41)
    Sleep(300)

    OP_24(0x01C9, 0x46)
    Sleep(300)

    OP_24(0x01C9, 0x4B)
    Sleep(300)

    OP_24(0x01C9, 0x50)
    Sleep(300)

    OP_24(0x01C9, 0x55)
    Sleep(300)

    OP_24(0x01C9, 0x5A)
    Sleep(300)

    OP_24(0x01C9, 0x5F)
    Sleep(300)

    OP_24(0x01C9, 0x64)

    Return()

# id: 0x000F offset: 0x2437
@scena.Code('func_0F_2437')
def func_0F_2437():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(110500, 8440, 40040, 0)
    OP_67(0, 5160, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(69000, 0)
    OP_6E(446, 0)
    ChrSetPos(0x0101, 108200, 1250, 33360, 0)
    ChrSetPos(0x0102, 108300, 1250, 31990, 0)
    ChrSetPos(0x0108, 106150, 1250, 33250, 0)
    ChrSetPos(0x0104, 106480, 1250, 31500, 0)
    ChrTurnDirection(0x0101, 0x0108, 0)
    ChrTurnDirection(0x0102, 0x0108, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0108, 0x0101, 0)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_2508')
    def lambda_2508():
        CameraMove(108600, 1250, 33560, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2508)

    @scena.Lambda('lambda_2520')
    def lambda_2520():
        OP_6E(333, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2520)

    @scena.Lambda('lambda_2530')
    def lambda_2530():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2530)

    Sleep(5000)

    ChrTalk(
        0x0108,
        (
            '#0080110327V#070F这样……\n',
            '我们就顺利地进入第二轮了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110328V虽然不知道能走多远，\n',
            '不过明天也能继续保持这种气势就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110329V#006F#5P那当然了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110330V#007F不过从今天各队的战果来看，\n',
            '剩下的都是强敌啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110331V协会的前辈、空贼团，\n',
            '还有情报部的那些家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110332V#015F#2P是啊……\n',
            '不做好充足的准备不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110333V#031F没什么，不用担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110334V恋爱的力量是不会停止的。\n',
            '不管什么障碍也能够突破的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110335V#509F#5P我根本听不懂你在说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110336V#070F今天我们要好好地养精蓄锐，\n',
            '为明天的半决赛做好准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110337V我现在就去酒廊吃饭，\n',
            '你们三个打算怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110338V#035F呵呵……\n',
            '本人很荣幸和你一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110339V#012F#2P（我们最好先向协会报告一下吧。）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110340V（说不定会得到和委托有关的情报。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110341V#004F#5P（啊，也是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)
    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110342V#506F#5P不好意思，金先生。\n',
            '我们两个就不跟你们去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110343V#070F那么，今天就此分别吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110344V明天早上，我们还是在酒店集合。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110345V#031FAu revoir.\n',
            '可爱的小猫咪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_298A')
    def lambda_298A():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_298A')

    DispatchAsync2(0x0102, 0x0001, lambda_298A)

    ChrSetDirection(0x0108, 270, 400)

    @scena.Lambda('lambda_29A2')
    def lambda_29A2():
        ChrWalkTo(0x00FE, 91230, 0, 33850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_29A2)

    ChrSetDirection(0x0104, 270, 400)

    @scena.Lambda('lambda_29C4')
    def lambda_29C4():
        ChrWalkTo(0x00FE, 91230, 0, 31850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_29C4)

    Sleep(3000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110346V#006F#5P那么……我们去协会吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110347V#013F#2P……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110348V还有……\n',
            '去哪里收集情报呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110349V#004F#5P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000C, 98320, 250, 32830, 90)
    ChrSetPos(0x000D, 97140, 250, 33540, 90)
    ChrSetPos(0x000E, 96950, 250, 32180, 90)

    NpcTalk(
        0x000C,
        '青年的声音',
        (
            '#0450110350V#2P嘿嘿～\n',
            '干嘛呆呆地站在那里啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B19')
    def lambda_2B19():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B19)

    @scena.Lambda('lambda_2B27')
    def lambda_2B27():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2B27)

    CameraMove(103750, 1250, 32810, 2000)

    @scena.Lambda('lambda_2B46')
    def lambda_2B46():
        ChrWalkTo(0x00FE, 105880, 1250, 32780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2B46)

    Sleep(200)

    @scena.Lambda('lambda_2B66')
    def lambda_2B66():
        ChrWalkTo(0x00FE, 105260, 1250, 33630, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2B66)

    Sleep(200)

    @scena.Lambda('lambda_2B86')
    def lambda_2B86():
        ChrWalkTo(0x00FE, 105430, 1250, 31690, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2B86)

    CameraMove(107020, 1250, 33610, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010110351V#000F啊，是你们……\n',
            '今天的比赛真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110352V哼……\n',
            '可不要得意忘形哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110353V这次是因为时间不够，\n',
            '锻炼不够充分而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110354V下次再战的时候，我们一定会赢的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110355V哎～还要打吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110356V#001F啊哈哈，可以啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110357V如果还有机会的话，\n',
            '什么时候交手都可以哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110358V#014F等一下，艾丝蒂尔……\n',
            '这么轻易就答应下来，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110359V#006F哎呀哎呀～有什么不好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110360V而且他们如果认真修行的话，\n',
            '就没有空闲去做坏事了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110361V哼……\n',
            '真是不知天高地厚的小鬼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110362V给你们这个吧，\n',
            '拿好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000C, 0x0101, 1200, 3000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '地下水路的钥匙Ａ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x036D, 1)
    OP_94(0x01, 0x000C, 0x00B4, 0x00000320, 0x00000BB8, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010110363V#505F这、这是什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110364V#014F好像是把很古老的钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110365V这个钥匙可以打开\n',
            '西街区的那个栅栏门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110366V从那里能通往地下水路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110367V我们偶然得到了那把钥匙，\n',
            '就每天去那里探险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110368V里面盘踞着很强的魔兽，\n',
            '是个不错的修行场所呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110369V#004F哎，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110370V可、可不要搞错哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110371V你们赢得了胜利是你们的实力。\n',
            '如果你们轻易输给别人，我们会很不甘心的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110372V听好了……一定要拿冠军哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110373V除此之外是绝不允许的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110374V那么，告辞了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 270, 400)

    @scena.Lambda('lambda_30D8')
    def lambda_30D8():
        ChrWalkTo(0x00FE, 91230, 0, 31850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_30D8)

    ChrSetDirection(0x000E, 270, 400)

    @scena.Lambda('lambda_30FA')
    def lambda_30FA():
        ChrWalkTo(0x00FE, 91230, 0, 31850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_30FA)

    ChrSetDirection(0x000C, 270, 400)

    @scena.Lambda('lambda_311C')
    def lambda_311C():
        ChrWalkTo(0x00FE, 91230, 0, 31850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_311C)

    Sleep(3000)

    @scena.Lambda('lambda_313C')
    def lambda_313C():
        CameraMove(109230, 1250, 33610, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_313C)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110375V#505F#5P哎～刚才难道是……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110376V#010F嗯，好像是在鼓励我们呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110377V是让我们去那个地下水路锻炼，\n',
            '为接下来的比赛做准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110378V#008F#5P果、果然是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110379V嗯……\n',
            '他们果然是洗心革面了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110380V#019F哈哈……\n',
            '说不定是被你的大肚量所感染了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110381V真是意外啊，\n',
            '艾丝蒂尔很适合当他们的头儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110382V#509F#5P大肚量……头儿……\n',
            '真是让人高兴不起来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110383V#007F不过算了，\n',
            '我们就满怀感激地收下他们的好意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110384V#010F不过，今天已经这么晚了，\n',
            '我们就不要去地下水路了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110385V明天早上比赛之前\n',
            '去试试身手反而会比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110386V#006F#5P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110387V那么，我们就去协会\n',
            '向艾南哥哥报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x00C3, 6, 0x61E))
    OP_28(0x0047, 0x01, 0x0040)
    OP_28(0x0047, 0x01, 0x0080)
    OP_28(0x0047, 0x01, 0x0100)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetPos(0x0104, 107840, 1250, 25920, 0)
    ChrSetPos(0x0108, 107840, 1250, 25920, 0)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x03, 0xFF)
    ChrSetPos(0x0101, 106440, 1250, 32490, 270)
    ChrSetPos(0x0102, 106440, 1250, 32490, 270)
    CameraMove(106440, 1250, 32490, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x3522
@scena.Code('func_10_3522')
def func_10_3522():
    EventBegin(0x00)
    CameraMove(110500, 8440, 40040, 0)
    OP_67(0, 5160, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(69000, 0)
    OP_6E(446, 0)
    ChrSetPos(0x0101, 108200, 1250, 33360, 0)
    ChrSetPos(0x0102, 108300, 1250, 31990, 0)
    ChrSetPos(0x0108, 106150, 1250, 33250, 0)
    ChrSetPos(0x0104, 106480, 1250, 31500, 0)
    ChrTurnDirection(0x0101, 0x0108, 0)
    ChrTurnDirection(0x0102, 0x0108, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0108, 0x0101, 0)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_35F3')
    def lambda_35F3():
        CameraMove(108600, 1250, 33560, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35F3)

    @scena.Lambda('lambda_360B')
    def lambda_360B():
        OP_6E(333, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_360B)

    @scena.Lambda('lambda_361B')
    def lambda_361B():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_361B)

    Sleep(5000)

    ChrTalk(
        0x0101,
        (
            '#0010110923V#007F#5P呼……\n',
            '不管怎么说，今天也赢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110924V#006F明天总算要进行决赛了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110925V#070F要为即将到来的激烈战斗做准备，\n',
            '必须得养精蓄锐才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110926V#071F所以……\n',
            '今晚也去酒馆吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110927V#031F呵呵，好主意。\n',
            '我也和你一起去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110928V#509F#5P怎么觉得有点不对劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110929V#010F#2P我们两个还有别的事，\n',
            '所以今晚也不跟你们去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110930V#070F哦，那么就再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110931V明天早上我还在酒店前台等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110932V#035F晚安，我的两个小甜心㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_383B')
    def lambda_383B():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_383B')

    DispatchAsync2(0x0102, 0x0001, lambda_383B)

    ChrSetDirection(0x0108, 270, 400)

    @scena.Lambda('lambda_3853')
    def lambda_3853():
        ChrWalkTo(0x00FE, 91230, 0, 33850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3853)

    ChrSetDirection(0x0104, 270, 400)

    @scena.Lambda('lambda_3875')
    def lambda_3875():
        ChrWalkTo(0x00FE, 91230, 0, 31850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3875)

    Sleep(3000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110933V#006F#5P那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110934V奈尔一定在等着，\n',
            '我们赶快去杂志社吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110935V#010F#2P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110936V如果能知道关于\n',
            '情报部成员的一些事情就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_28(0x0048, 0x01, 0x0020)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetPos(0x0104, 107450, 1250, 31370, 0)
    ChrSetPos(0x0108, 107450, 1250, 31370, 0)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x03, 0xFF)
    ChrSetPos(0x0101, 106440, 1250, 32490, 270)
    ChrSetPos(0x0102, 106440, 1250, 32490, 270)
    CameraMove(106440, 1250, 32490, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x3A24
@scena.Code('func_11_3A24')
def func_11_3A24():
    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C82',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3A57',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xBB8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3A57(): pass

    label('loc_3A57')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3A7D',
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

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3A7D(): pass

    label('loc_3A7D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3AA3',
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

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3AA3(): pass

    label('loc_3AA3')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3ACA',
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

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3ACA(): pass

    label('loc_3ACA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3AF0',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3AF0(): pass

    label('loc_3AF0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3B16',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3B16(): pass

    label('loc_3B16')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3B3B',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3B3B(): pass

    label('loc_3B3B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3B60',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3B74')

    def _loc_3B60(): pass

    label('loc_3B60')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3B74(): pass

    label('loc_3B74')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C7F',
    )

    ExecExpressionWithReg(
        0x0001,
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
        'loc_3C70',
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

    def _loc_3C70(): pass

    label('loc_3C70')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_3C7F(): pass

    label('loc_3C7F')

    Jump('func_11_3A24')

    def _loc_3C82(): pass

    label('loc_3C82')

    Return()

# id: 0x0012 offset: 0x3C83
@scena.Code('func_12_3C83')
def func_12_3C83():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D18',
    )

    ChrSetPos(0x00FE, 48010, 250, 59980, 270)
    ChrWalkTo(0x00FE, 35200, 250, 59980, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 59980, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 4310, 3000, 0x00)
    ChrWalkTo(0x00FE, 42030, 250, 4310, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 4310, 3000, 0x00)
    ChrWalkTo(0x00FE, 48010, 250, 59980, 3000, 0x00)

    Jump('func_12_3C83')

    def _loc_3D18(): pass

    label('loc_3D18')

    Return()

# id: 0x0013 offset: 0x3D19
@scena.Code('func_13_3D19')
def func_13_3D19():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D5E',
    )

    ChrSetPos(0x00FE, 39910, 0, 63710, 270)
    ChrWalkTo(0x00FE, 89750, 0, 63710, 3000, 0x00)
    ChrWalkTo(0x00FE, 39910, 0, 63710, 3000, 0x00)

    Jump('func_13_3D19')

    def _loc_3D5E(): pass

    label('loc_3D5E')

    Return()

# id: 0x0014 offset: 0x3D5F
@scena.Code('func_14_3D5F')
def func_14_3D5F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3DA4',
    )

    ChrSetPos(0x00FE, 50960, 0, 16800, 0)
    ChrWalkTo(0x00FE, 50960, 0, 59090, 3000, 0x00)
    ChrWalkTo(0x00FE, 50960, 0, 16800, 3000, 0x00)

    Jump('func_14_3D5F')

    def _loc_3DA4(): pass

    label('loc_3DA4')

    Return()

# id: 0x0015 offset: 0x3DA5
@scena.Code('func_15_3DA5')
def func_15_3DA5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E12',
    )

    ChrSetPos(0x00FE, 55970, 250, 6050, 0)
    ChrWalkTo(0x00FE, 55970, 250, 58080, 3000, 0x00)
    ChrWalkTo(0x00FE, 84170, 250, 58080, 3000, 0x00)
    ChrWalkTo(0x00FE, 84170, 250, 5990, 3000, 0x00)
    ChrWalkTo(0x00FE, 55970, 250, 6050, 3000, 0x00)

    Jump('func_15_3DA5')

    def _loc_3E12(): pass

    label('loc_3E12')

    Return()

# id: 0x0016 offset: 0x3E13
@scena.Code('func_16_3E13')
def func_16_3E13():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E80',
    )

    ChrSetPos(0x00FE, 53970, 250, 3940, 90)
    ChrWalkTo(0x00FE, 86060, 250, 3940, 3000, 0x00)
    ChrWalkTo(0x00FE, 86060, 250, 59960, 3000, 0x00)
    ChrWalkTo(0x00FE, 53920, 250, 59960, 3000, 0x00)
    ChrWalkTo(0x00FE, 53970, 250, 3940, 3000, 0x00)

    Jump('func_16_3E13')

    def _loc_3E80(): pass

    label('loc_3E80')

    Return()

# id: 0x0017 offset: 0x3E81
@scena.Code('func_17_3E81')
def func_17_3E81():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EC6',
    )

    ChrSetPos(0x00FE, 54120, 250, 67800, 270)
    ChrWalkTo(0x00FE, 95480, 250, 67800, 3000, 0x00)
    ChrWalkTo(0x00FE, 54120, 250, 67800, 3000, 0x00)

    Jump('func_17_3E81')

    def _loc_3EC6(): pass

    label('loc_3EC6')

    Return()

# id: 0x0018 offset: 0x3EC7
@scena.Code('func_18_3EC7')
def func_18_3EC7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F0C',
    )

    ChrSetPos(0x00FE, 95540, 250, -5740, 90)
    ChrWalkTo(0x00FE, 42710, 250, -5740, 3000, 0x00)
    ChrWalkTo(0x00FE, 95540, 250, -5740, 3000, 0x00)

    Jump('func_18_3EC7')

    def _loc_3F0C(): pass

    label('loc_3F0C')

    Return()

# id: 0x0019 offset: 0x3F0D
@scena.Code('func_19_3F0D')
def func_19_3F0D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F7A',
    )

    ChrSetPos(0x00FE, 42960, 0, -1020, 90)
    ChrWalkTo(0x00FE, 89990, 0, -1020, 3000, 0x00)
    ChrWalkTo(0x00FE, 89990, 0, 58750, 3000, 0x00)
    ChrWalkTo(0x00FE, 89990, 0, -1020, 3000, 0x00)
    ChrWalkTo(0x00FE, 42960, 0, -1020, 3000, 0x00)

    Jump('func_19_3F0D')

    def _loc_3F7A(): pass

    label('loc_3F7A')

    Return()

# id: 0x001A offset: 0x3F7B
@scena.Code('func_1A_3F7B')
def func_1A_3F7B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3FE8',
    )

    ChrSetPos(0x00FE, 61020, 1250, 53050, 180)
    ChrWalkTo(0x00FE, 61020, 1250, 37000, 3000, 0x00)
    ChrWalkTo(0x00FE, 79040, 1250, 37000, 3000, 0x00)
    ChrWalkTo(0x00FE, 79040, 1250, 52810, 3000, 0x00)
    ChrWalkTo(0x00FE, 61020, 1250, 53050, 3000, 0x00)

    Jump('func_1A_3F7B')

    def _loc_3FE8(): pass

    label('loc_3FE8')

    Return()

# id: 0x001B offset: 0x3FE9
@scena.Code('func_1B_3FE9')
def func_1B_3FE9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4056',
    )

    ChrSetPos(0x00FE, 77980, 1250, 52000, 180)
    ChrWalkTo(0x00FE, 77980, 1250, 37980, 3000, 0x00)
    ChrWalkTo(0x00FE, 62050, 1250, 37980, 3000, 0x00)
    ChrWalkTo(0x00FE, 62050, 1250, 51960, 3000, 0x00)
    ChrWalkTo(0x00FE, 77980, 1250, 52000, 3000, 0x00)

    Jump('func_1B_3FE9')

    def _loc_4056(): pass

    label('loc_4056')

    Return()

# id: 0x001C offset: 0x4057
@scena.Code('func_1C_4057')
def func_1C_4057():
    EventBegin(0x00)
    CameraMove(69830, 1250, 37910, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(1750, 0)
    OP_6C(224000, 0)
    OP_6E(508, 0)
    ChrSetPos(0x0101, 68870, 1250, 37520, 0)
    ChrSetPos(0x0102, 70330, 1250, 37670, 0)

    @scena.Lambda('lambda_40BE')
    def lambda_40BE():
        ChrWalkTo(0x00FE, 69470, 250, 44600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_40BE)

    Sleep(300)

    @scena.Lambda('lambda_40DE')
    def lambda_40DE():
        ChrWalkTo(0x00FE, 69360, 250, 43310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_40DE)

    CameraMove(68880, 250, 42980, 3000)

    ChrTalk(
        0x0101,
        (
            '呼……\n',
            '躲避着巡逻的士兵，\n',
            '没想到来到这种地方了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111405V看起来，\n',
            '这边好像已经没有士兵了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F嗯……没有人的气息了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111407V夜间的巡逻\n',
            '也差不多该结束了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111408V我们稍微休息一下就回旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000FＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_420A')
    def lambda_420A():
        ChrWalkTo(0x00FE, 66420, 250, 44610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_420A)

    Sleep(400)

    @scena.Lambda('lambda_422A')
    def lambda_422A():
        ChrWalkTo(0x00FE, 66430, 250, 45490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_422A)

    @scena.Lambda('lambda_4245')
    def lambda_4245():
        OP_67(0, 5940, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4245)

    CameraMove(66840, 250, 45270, 3000)

    ChrTalk(
        0x0101,
        (
            '#000F啊～发生了这么多事，\n',
            '脑子还处于不清醒状态呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈……确实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没想到在大圣堂\n',
            '等着我们的人是中尉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111414V刚开始约修亚以为\n',
            '送信的不是尤莉亚小姐吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F………那是……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111417V…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，算我没说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111420V犯规了犯规了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是最初的约定之一嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在约修亚愿意自己说出来之前，\n',
            '不能问我们相遇前的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然我一直在注意，\n',
            '不过还是不小心忘记了呢～。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111425V艾丝蒂尔，我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我，和你一起旅行，\n',
            '觉得自己稍微变坚强了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F在同一片天空下生活的\n',
            '各种各样的人，各种各样的人生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '无数交织在一起的思念的轨迹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '每当感受到这些，\n',
            '就似乎找回了自己丢失的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这种感觉……真美好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F大概这是错觉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111434V尽管如此，我也……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我也要感谢\n',
            '和你一起生活的这些日子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111436V和这片天空，和父亲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '当然还有艾丝蒂尔……你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F所以……我们约定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111440V如果这次的事情能够结束，\n',
            '父亲平安地回来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我就告诉你和你相遇之前的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真、真的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111443V#010F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111444V和这星空做个约定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……好，决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 66950, 250, 44770, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F该怎么说呢……\n',
            '沉重的心情一扫而光呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111449V全部结束之后，\n',
            '我也有话想对约修亚说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哎……啊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111451V难道是那个烦恼的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F对对，就是那个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嘿嘿……\n',
            '我已经做好准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F准备……\n',
            '是很让人烦恼的事情吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么现在说出来也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不～行！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '说那种话，\n',
            '果然还是要时机的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯～虽然现在\n',
            '这个气氛相当的好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F为了这个，\n',
            '明天的比赛一定不能输……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看我用少女的力量，\n',
            '把那些特务兵们打飞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F打飞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呼……啊哈哈哈……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你……果然……\n',
            '……不愧是父亲的女儿啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么啊，这样说真是失礼呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111468V我跟那样的不良中年\n',
            '到底有那点像啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '明天的比赛，\n',
            '我也有取胜的信心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x4A69
@scena.Code('func_1D_4A69')
def func_1D_4A69():
    If(
        (
            (Expr.Eval, "OP_40(0x036E)"),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4AC8',
    )

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Jump('loc_4C9E')

    def _loc_4AC8(): pass

    label('loc_4AC8')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C37',
    )

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 0, 0x630)),
            Expr.Return,
        ),
        'loc_4BA4',
    )

    ChrTalk(
        0x0102,
        (
            '#0020110434V#010F今天已经很晚了，\n',
            '就不要到地下水路去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110435V明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C31')

    def _loc_4BA4(): pass

    label('loc_4BA4')

    ChrTalk(
        0x0102,
        (
            '#0020110945V#010F看起来这里就是\n',
            '艾南先生所说的地下水路的入口了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C31(): pass

    label('loc_4C31')

    TalkEnd(0x00FF)

    Jump('loc_4C9E')

    def _loc_4C37(): pass

    label('loc_4C37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 0, 0x630)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C9E',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(115, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '地下水路的钥匙Ｂ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x00C6, 0, 0x630))
    OP_64(0x00, 0x0001)
    OP_71(0x000B, 0x0010)
    TalkEnd(0x00FF)

    def _loc_4C9E(): pass

    label('loc_4C9E')

    Return()

# id: 0x001E offset: 0x4C9F
@scena.Code('func_1E_4C9F')
def func_1E_4C9F():
    EventBegin(0x00)
    CameraMove(110500, 8440, 40040, 0)
    OP_67(0, 5160, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(69000, 0)
    OP_6E(446, 0)
    ChrSetPos(0x0101, 108200, 1250, 33060, 0)
    ChrSetPos(0x0102, 108300, 1250, 31690, 0)
    ChrSetPos(0x0108, 106860, 1250, 33260, 0)
    ChrSetPos(0x0104, 106480, 1250, 31500, 0)
    ChrTurnDirection(0x0101, 0x0108, 0)
    ChrTurnDirection(0x0102, 0x0108, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0108, 0x0101, 0)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    OP_4A(0x0034, 255)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_4D79')
    def lambda_4D79():
        CameraMove(108600, 1250, 33260, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D79)

    @scena.Lambda('lambda_4D91')
    def lambda_4D91():
        OP_6E(333, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4D91)

    @scena.Lambda('lambda_4DA1')
    def lambda_4DA1():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4DA1)

    Sleep(5000)

    ChrTalk(
        0x0101,
        (
            '#0010111846V#001F#5P哈啊～该怎么说呢。\n',
            '真是激烈的战斗啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111847V那个洛伦斯少尉比想象中还要厉害呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111848V#010F#2P嗯……终于赢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111849V到现在我还不敢相信呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111850V#074F……真不爽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111851V#004F#5P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111852V#070F不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111853V说起来，晚宴就是今天晚上吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111854V因为会进行到很晚，\n',
            '好像也为我们准备了房间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111855V#030F哎呀哎呀，真是王家典范的服务啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111856V虽然能和各位社会名流同席，\n',
            '但是总觉得有点拘谨啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111857V不过可以享受到利贝尔的宫廷料理，\n',
            '我这就赏面应邀参加一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111858V#035F呼～现在只是想象一下，\n',
            '口水也就要流出来了呢～啧啧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111859V#509F#5P出来了，出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111860V#019F#2P呵呵，一听奥利维尔这些话，\n',
            '好像感觉自己什么压力都没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111861V#031F哈·哈·哈。\n',
            '那么我们赶快去吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111862V到盛情邀请我们的爱与希望的天堂去！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    TerminateThread(0x0108, 0xFF)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 98000, 250, 32890, 90)

    NpcTalk(
        0x0009,
        '男性的声音',
        (
            '#0110111863V#2P……就这样走吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5194')
    def lambda_5194():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5194)

    @scena.Lambda('lambda_51A2')
    def lambda_51A2():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_51A2)

    @scena.Lambda('lambda_51B0')
    def lambda_51B0():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_51B0)

    @scena.Lambda('lambda_51BE')
    def lambda_51BE():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_51BE)

    CameraMove(103750, 1250, 32810, 1500)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040111864V#033F啊，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_521C')
    def lambda_521C():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_521C')

    DispatchAsync2(0x0101, 0x0002, lambda_521C)

    @scena.Lambda('lambda_522D')
    def lambda_522D():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_522D')

    DispatchAsync2(0x0102, 0x0002, lambda_522D)

    @scena.Lambda('lambda_523E')
    def lambda_523E():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_523E')

    DispatchAsync2(0x0104, 0x0002, lambda_523E)

    @scena.Lambda('lambda_524F')
    def lambda_524F():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_524F')

    DispatchAsync2(0x0108, 0x0002, lambda_524F)

    @scena.Lambda('lambda_5260')
    def lambda_5260():
        ChrWalkTo(0x00FE, 105180, 1250, 32000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5260)

    CameraMove(107020, 1250, 33310, 3000)
    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0104, 400)

    ChrTalk(
        0x0009,
        (
            '#0110111865V#274F你这人啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111866V我还以为你每天不打招呼就出去\n',
            '是去干什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111867V没想到你根本没考虑到自己的立场\n',
            '就去参加什么武术大会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111868V#031F真、真讨厌啊，穆拉君。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111869V不要做出那样恐怖的表情嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111870V微笑才能招福嘛。\n',
            '笑一个，笑一个～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0110111871V#271F#3S谁做出恐怖的表情了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111872V#004F（那个制服，难道是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111873V#012F（嗯……\n',
            '　是埃雷波尼亚帝国的军服……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111874V#070F（嗯……\n',
            '　看起来是个很能干的小哥嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111875V#270F……初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111876V我的名字叫穆拉。\n',
            '是前一段时间来上任的\n',
            '埃雷波尼亚帝国大使馆的武官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111877V我和这个超级大赖皮蛋……\n',
            '唉……算是很久以前认识的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0104, 0xFF)
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040111878V#031F就是所谓的『青梅竹马』啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111879V呵呵，平时总是一幅严肃的面孔，\n',
            '没想到还有这样可爱的地方嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111880V#274F#3S快·给·我·闭·嘴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111881V#034F是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#0110111882V#272F咳，失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111883V#270F看起来……\n',
            '这个大赖皮蛋给你们添了很多麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111884V我代表帝国大使馆向你们道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111885V#008F啊，没什么……\n',
            '也没有什么麻烦啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111886V在比赛中，奥利维尔的枪法和魔法\n',
            '给予了我们很大的帮忙呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111887V#014F我说，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111888V参加武术大会的事情，\n',
            '你一直瞒着大使馆的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111889V#031F哈·哈·哈。\n',
            '我没有故意隐瞒啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111890V只是没有告诉他们罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111891V#271F#3S这不是隐瞒又是什么！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x0009,
        (
            '#0110111892V#272F算了……\n',
            '过去的事情再说也没用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111893V赶快回大使馆去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111894V#033F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111895V#036F请、请等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111896V我们正要去王城应邀出席一场\n',
            '美妙豪华的晚宴呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111897V#270F正因为是美妙豪华的晚宴，\n',
            '所以让你去了我就更加难办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111898V这段时间，\n',
            '你还是给我老老实实地呆在大使馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111899V#033F………………真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111900V#272F我从不开玩笑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0104,
        (
            '#0040111901V#036F这、这简直是杀人啦～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111902V我全心全意地为晚宴努力到如此地步……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111903V#506F确、确实……\n',
            '这样不是有点可怜吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111904V#070F只是出席晚宴，\n',
            '不会有什么问题的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111905V#010F有什么原因吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040111906V#031F你们，说得太好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111907V啊啊……\n',
            '『伙伴』是多么美妙的词语……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111908V比起某个寡情薄幸的青梅竹马来说\n',
            '简直就是温暖太多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111909V#272F……你们好像还不了解事情的严重程度。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111910V#270F仔细想象一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111911V利贝尔王家主办的晚宴，\n',
            '各地的有权有势的人士齐聚一堂……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111912V在那里，有个弄不清楚自己立场的\n',
            '旁若无人的我行我素的大赖皮蛋在捣乱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111913V如果被人知道他是帝国人的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111914V#505F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100672V#013F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111916V#074F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111917V#033F等、等一下各位。\n',
            '为什么都突然沉默了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111918V#007F……不好意思，奥利维尔。\n',
            '你那位朋友的担心也很有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111919V#018F没错，如果在王城的晚宴中\n',
            '也像平常那样胡作非为的话就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111920V#075F嗯……\n',
            '说不定会发展成国际问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111921V#036F哇，这样就叛变了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111922V#270F百日战役结束后的第十个年头……\n',
            '……这是个非常微妙的时间啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110111923V忍耐一下吧，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)

    @scena.Lambda('lambda_5F10')
    def lambda_5F10():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_5F10')

    DispatchAsync2(0x0104, 0x0002, lambda_5F10)

    ChrWalkTo(0x0009, 106100, 1250, 32060, 2000, 0x00)
    ChrTurnDirection(0x0009, 0x0104, 400)
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0104,
        (
            '#0040111924V#031F稍、稍微等一下嘛～\n',
            '穆拉先生～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111925V隐瞒了真相的事情，我道歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110111926V#272F说什么也没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5FD1')
    def lambda_5FD1():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_5FD1')

    DispatchAsync2(0x0101, 0x0002, lambda_5FD1)

    @scena.Lambda('lambda_5FE2')
    def lambda_5FE2():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_5FE2')

    DispatchAsync2(0x0102, 0x0002, lambda_5FE2)

    @scena.Lambda('lambda_5FF3')
    def lambda_5FF3():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_5FF3')

    DispatchAsync2(0x0104, 0x0002, lambda_5FF3)

    @scena.Lambda('lambda_6004')
    def lambda_6004():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_6004')

    DispatchAsync2(0x0108, 0x0002, lambda_6004)

    TerminateThread(0x0104, 0xFF)
    ChrSetDirection(0x0009, 270, 400)

    @scena.Lambda('lambda_6020')
    def lambda_6020():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_6020)

    Sleep(200)

    ChrSetChipByIndex(0x0104, 37)
    ChrSetSubChip(0x0104, 0)
    ChrSetFlags(0x0104, 0x0020)

    @scena.Lambda('lambda_6042')
    def lambda_6042():
        CameraMove(107020, 1250, 33610, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6042)

    @scena.Lambda('lambda_605A')
    def lambda_605A():
        ChrMoveTo(0x00FE, 96000, 250, 31500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_605A)

    @scena.Lambda('lambda_6075')
    def lambda_6075():
        ChrWalkTo(0x00FE, 96000, 250, 32060, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6075)

    ChrTalk(
        0x0104,
        (
            '#0040111927V#25A#2P我的晚宴～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2400)

    ChrTalk(
        0x0104,
        (
            '#0040111928V#30A#2P我的宫廷料理～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(3100)

    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    CameraMove(108020, 1250, 33310, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010111929V#506F#5P哎……这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111930V#015F#2P虽然表面上有点可怜……\n',
            '不过他应该想到最后还是这样的，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111931V#071F哈哈，算了算了。\n',
            '正所谓『塞翁失马焉知非福』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111932V我们连他的那份也一起享受算了～！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111933V#007F#5P嗯……没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111934V#006F那么，我们就打起精神，\n',
            '马上向格兰赛尔城出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    AddItem(0x0371, 1)
    OP_28(0x0049, 0x01, 0x0040)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x0104, 106850, 1250, 30720, 0)
    FormationDelMember(0x03, 0xFF)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetPos(0x0024, 48500, 250, 41910, 90)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002E, 36280, 1250, 42890, 45)
    ChrSetPos(0x002C, 37150, 1250, 43970, 225)
    ChrSetPos(0x002D, 40150, 1250, 48060, 180)
    ChrSetPos(0x002F, 40150, 1250, 46580, 0)
    ChrSetFlags(0x002D, 0x0010)
    ChrSetFlags(0x002F, 0x0010)
    CreateThread(0x002D, 0x00, 0x00, func_02_178A)
    CreateThread(0x002F, 0x00, 0x00, func_02_178A)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    OP_4B(0x0034, 255)
    ChrSetPos(0x0101, 106440, 1250, 32490, 270)
    ChrSetPos(0x0102, 106440, 1250, 32490, 270)
    ChrSetPos(0x0108, 106440, 1250, 32490, 270)
    CameraMove(106440, 1250, 32490, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x001F offset: 0x63FF
@scena.Code('func_1F_63FF')
def func_1F_63FF():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(72150, 250, 45780, 0)
    OP_6C(45000, 0)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, 72830, 250, 45190, 270)
    ChrSetPos(0x0101, 71410, 250, 45750, 125)
    ChrSetPos(0x0102, 71380, 250, 44240, 45)
    ChrSetPos(0x0108, 70360, 250, 45070, 90)
    OP_4A(0x0031, 255)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x001F,
        (
            '#0120130138V#814F………………啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130139V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130140V#012F刚才所说的句句属实，绝非戏言。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130141V这是一个非常重要的任务，\n',
            '需要亚妮拉丝小姐你的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0120130142V#819F……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130143V抱歉，我头脑有一些混乱了，\n',
            '不太能把握现在的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130144V#812F虽然不太明白，\n',
            '但大家是不是要在协会集合呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130145V#006F嗯，没错。\n',
            '可以向艾南哥哥询问详细的情况哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0120130146V我知道了……！\n',
            '我先去那里等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6652')
    def lambda_6652():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_6652')

    DispatchAsync2(0x0101, 0x0001, lambda_6652)

    @scena.Lambda('lambda_6663')
    def lambda_6663():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_6663')

    DispatchAsync2(0x0102, 0x0001, lambda_6663)

    @scena.Lambda('lambda_6674')
    def lambda_6674():
        ChrTurnDirection(0x00FE, 0x001F, 0)
        Yield()

        Jump('lambda_6674')

    DispatchAsync2(0x0108, 0x0001, lambda_6674)

    ChrWalkTo(0x001F, 71220, 250, 41420, 4000, 0x00)
    ChrWalkTo(0x001F, 70990, 1250, 37850, 4000, 0x00)
    ChrWalkTo(0x001F, 61490, 1250, 37980, 4000, 0x00)
    ChrSetFlags(0x001F, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    OP_4B(0x0031, 255)
    EventEnd(0x00)

    Return()

# id: 0x0020 offset: 0x66D3
@scena.Code('func_20_66D3')
def func_20_66D3():
    EventBegin(0x00)
    OP_6F(0x000E, 118)
    OP_6F(0x000F, 120)
    CameraMove(44210, 5550, 35490, 0)
    OP_67(0, 9330, -10000, 0)
    OP_6C(294000, 0)
    OP_6E(212, 0)
    CameraSetDistance(4490, 0)

    @scena.Lambda('lambda_6726')
    def lambda_6726():
        CameraMove(37610, 5550, 36790, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6726)

    @scena.Lambda('lambda_673E')
    def lambda_673E():
        OP_67(0, 5170, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_673E)

    @scena.Lambda('lambda_6756')
    def lambda_6756():
        OP_6C(270000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6756)

    @scena.Lambda('lambda_6766')
    def lambda_6766():
        OP_6E(149, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6766)

    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x002E, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    Sleep(9000)

    OP_6F(0x000E, 118)
    OP_6F(0x000F, 120)
    OP_70(0x000E, 120)
    OP_70(0x000F, 120)
    PlaySE(130, 0x00, 0x64)
    Sleep(1000)

    PlaySE(182, 0x00, 0x64)
    Sleep(2500)

    PlaySE(182, 0x00, 0x64)
    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4102._SN', 100, 1, 0)
    IdleLoop()

    Return()

# id: 0x0021 offset: 0x67D5
@scena.Code('func_21_67D5')
def func_21_67D5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 5, 0x66D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_684E',
    )

    EventBegin(0x00)
    Fade(1500)
    ChrSetPos(0x0101, 68590, 250, 45300, 270)
    ChrSetPos(0x0102, 69280, 250, 44330, 270)
    CameraMove(68980, 250, 44840, 1500)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020140933V#010F这里就是休息处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Call(0, 0x0022)

    def _loc_684E(): pass

    label('loc_684E')

    Return()

# id: 0x0022 offset: 0x684F
@scena.Code('func_22_684F')
def func_22_684F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 5, 0x66D)),
            Expr.Return,
        ),
        'loc_6858',
    )

    EventBegin(0x00)

    def _loc_6858(): pass

    label('loc_6858')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 4, 0x6EC)),
            Expr.Return,
        ),
        'loc_6869',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_6869(): pass

    label('loc_6869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 5, 0x6ED)),
            Expr.Return,
        ),
        'loc_687A',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_687A(): pass

    label('loc_687A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 6, 0x6EE)),
            Expr.Return,
        ),
        'loc_688B',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_688B(): pass

    label('loc_688B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 7, 0x6EF)),
            Expr.Return,
        ),
        'loc_689C',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_689C(): pass

    label('loc_689C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 0, 0x6F0)),
            Expr.Return,
        ),
        'loc_68AD',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_68AD(): pass

    label('loc_68AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 1, 0x6F1)),
            Expr.Return,
        ),
        'loc_68BE',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_68BE(): pass

    label('loc_68BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 2, 0x6F2)),
            Expr.Return,
        ),
        'loc_68CF',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_68CF(): pass

    label('loc_68CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 3, 0x6F3)),
            Expr.Return,
        ),
        'loc_68E0',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_68E0(): pass

    label('loc_68E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 4, 0x6F4)),
            Expr.Return,
        ),
        'loc_68F1',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_68F1(): pass

    label('loc_68F1')

    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_694C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020140934V#014F我们还有很多地方都没逛呢，\n',
            '现在就要休息了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69D2')

    def _loc_694C(): pass

    label('loc_694C')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_699C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020140935V#010F还没有逛过所有地方呢，\n',
            '现在就要休息了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69D2')

    def _loc_699C(): pass

    label('loc_699C')

    ChrTalk(
        0x0102,
        (
            '#0020140936V#019F已经有点累了呢。\n',
            '现在就休息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69D2(): pass

    label('loc_69D2')

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【继续参观诞辰庆典】\n'),
            TXT(0x01, '【已经累了，休息一下】\n'),
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
        (0x00000000, 'loc_6A4F'),
        (0x00000001, 'loc_6B17'),
        (-1, 'loc_9614'),
    )

    def _loc_6A4F(): pass

    label('loc_6A4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 5, 0x66D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B0D',
    )

    SetScenaFlags(ScenaFlag(0x00CD, 5, 0x66D))
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140937V#505F嗯，\n',
            '还想再看看别的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140938V#010F那么，把王都转遍了之后\n',
            '我们再回到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140939V#006F嗯，就坐在那边的长椅上休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_6B0F')

    def _loc_6B0D(): pass

    label('loc_6B0D')

    EventEnd(0x01)

    def _loc_6B0F(): pass

    label('loc_6B0F')

    MapSetFlags(0x02000000)

    Jump('loc_9614')

    def _loc_6B17(): pass

    label('loc_6B17')

    SetScenaFlags(ScenaFlag(0x00CD, 7, 0x66F))
    OP_28(0x0055, 0x04, 0x40)
    StopEffect(0x04, 0x00)
    Fade(1000)
    CameraMove(70100, 250, 42490, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6C(225000, 0)
    ChrSetPos(0x0101, 70660, 250, 42400, 0)
    ChrSetPos(0x0102, 69570, 250, 42530, 0)
    MapClearFlags(0x00000800)

    @scena.Lambda('lambda_6B7F')
    def lambda_6B7F():
        OP_67(0, 5350, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6B7F)

    @scena.Lambda('lambda_6B97')
    def lambda_6B97():
        OP_6C(135000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6B97)

    @scena.Lambda('lambda_6BA7')
    def lambda_6BA7():
        CameraMove(73240, 250, 45110, 3500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6BA7)

    @scena.Lambda('lambda_6BBF')
    def lambda_6BBF():
        CameraSetDistance(2800, 3500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_6BBF)

    @scena.Lambda('lambda_6BCF')
    def lambda_6BCF():
        ChrWalkTo(0x00FE, 73240, 250, 44890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6BCF)

    Sleep(400)

    @scena.Lambda('lambda_6BEF')
    def lambda_6BEF():
        ChrWalkTo(0x00FE, 73240, 250, 45860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6BEF)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetChipByIndex(0x0101, 38)

    @scena.Lambda('lambda_6C20')
    def lambda_6C20():
        ChrJumpTo(0x00FE, 73750, 450, 44890, 700, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6C20)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 270, 400)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0102, 39)

    @scena.Lambda('lambda_6C54')
    def lambda_6C54():
        ChrJumpTo(0x00FE, 73750, 450, 45860, 700, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6C54)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010140940V#007F哈啊……\n',
            '到处逛还真是累呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 1)

    ChrTalk(
        0x0102,
        (
            '#0020140941V#010F就在这里稍微休息一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140942V真是难得的安逸时刻……\n',
            '王都也没有发生其他骚动的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    ChrTalk(
        0x0101,
        (
            '#0010140943V#004F约修亚你真是的……\n',
            '难道还在担心那件事吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140944V#006F今天就把所有的事情都扔给老爸吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140945V谁让他迟到了，\n',
            '多做点工作也是理所应当的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140946V#019F哈哈，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140947V#010F不管怎么说这也是他的职责啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140948V#007F呼，真是没办法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140949V#501F话说回来……\n',
            '我们已经是正游击士了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140950V#010F嗯，以后就可以在\n',
            '不受支部监督的情况下自由行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140951V而且人手不足的支部会发来支援请求，\n',
            '乘坐定期船的机会也会变多。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140952V#019F相应地，我们所要承担的责任也增加了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140953V#006F嗯，不管怎么说，\n',
            '我们俩都会继续努力下去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140954V而且这次连政变都成功阻止了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140955V#001F哈哈，老爸再也不会说\n',
            '『约修亚不在的话很让人担心』\n',
            '这类又讨厌又没根据的话了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140956V#019F哈哈……\n',
            '我想父亲他应该不会再说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140957V#010F不过，我以后也想继续和你在一起。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140958V#004F……哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140959V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010140960V#005F#3S哎哎哎哎哎哎哎哎！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140961V#014F啊，这样让你很为难吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140962V#503F不是，该说是为难呢还是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140963V在一起……\n',
            '那个……是指什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140964V#010F那个啊，因为我们互相了解对方的脾气，\n',
            '而且也知道各自的习惯和爱好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140965V所以我觉得，\n',
            '我们俩以后继续搭档也很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140966V#008F啊……是指游击士的工作啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140967V#506F什么嘛，我还以为是告白呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140968V#014F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    @scena.Lambda('lambda_72CA')
    def lambda_72CA():
        OP_6E(251, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_72CA)

    Sleep(250)

    ChrTalk(
        0x0101,
        (
            '#0010140969V#504F#3S哇啊啊啊啊啊啊！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140970V#3S我什么都没说！快给我忘掉！#2S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140971V#014F艾丝蒂尔，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_7373')
    def lambda_7373():
        OP_67(0, 7000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7373)

    @scena.Lambda('lambda_738B')
    def lambda_738B():
        OP_6C(115000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_738B)

    @scena.Lambda('lambda_739B')
    def lambda_739B():
        CameraSetDistance(3000, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_739B)

    Sleep(500)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)

    @scena.Lambda('lambda_73BA')
    def lambda_73BA():
        ChrJumpTo(0x00FE, 73000, 250, 44890, 700, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_73BA)

    WaitForThreadExit(0x0101, 0x0001)
    ChrWalkTo(0x0101, 72500, 250, 44890, 2000, 0x00)
    ChrSetSubChip(0x0102, 0)
    WaitForThreadExit(0x0101, 0x0003)
    ChrTurnDirection(0x0101, 0x0102, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 6, 0x66E)),
            Expr.Return,
        ),
        'loc_749F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140972V#008F不、不过今天还真是热啊！？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140973V#008F热的时候吃冰淇淋是最好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140974V#504F之前说好我要请客的！\n',
            '在这等我一会儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_752A')

    def _loc_749F(): pass

    label('loc_749F')

    ChrTalk(
        0x0101,
        (
            '#0010140972V#008F不、不过\n',
            '今天还真是热啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140973V#008F热的时候吃冰淇淋是最好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140977V#504F我请客，\n',
            '在这等我一会儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_752A(): pass

    label('loc_752A')

    ChrClearFlags(0x0101, 0x0004)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetFlags(0x0101, 0x0040)

    @scena.Lambda('lambda_754C')
    def lambda_754C():
        CameraMove(73240, 250, 46110, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_754C)

    @scena.Lambda('lambda_7564')
    def lambda_7564():
        ChrWalkTo(0x00FE, 70300, 250, 60700, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7564)

    ChrSetSubChip(0x0102, 2)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020140978V#014F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020140979V#017F#5P艾丝蒂尔……\n',
            '卖冰淇淋的地方不是那边啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140980V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140981V#014F难道……刚才……艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140982V#013F不……\n',
            '……应该不可能吧………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0020, 71640, 1250, 37000, 0)

    NpcTalk(
        0x0020,
        '男性的声音',
        (
            '#0150140983V#3P哎呀……\n',
            '年轻人还真是令人羡慕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_76F2')
    def lambda_76F2():
        OP_6C(153000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_76F2)

    @scena.Lambda('lambda_7702')
    def lambda_7702():
        CameraMove(71700, 1250, 39000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7702)

    @scena.Lambda('lambda_771A')
    def lambda_771A():
        OP_67(0, 5170, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_771A)

    @scena.Lambda('lambda_7732')
    def lambda_7732():
        OP_6E(251, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7732)

    @scena.Lambda('lambda_7742')
    def lambda_7742():
        CameraSetDistance(3340, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7742)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 1)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    @scena.Lambda('lambda_776B')
    def lambda_776B():
        ChrWalkTo(0x00FE, 71900, 250, 41950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_776B)

    Sleep(200)

    @scena.Lambda('lambda_778B')
    def lambda_778B():
        CameraMove(72850, 250, 43180, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_778B)

    @scena.Lambda('lambda_77A3')
    def lambda_77A3():
        OP_67(0, 7230, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_77A3)

    @scena.Lambda('lambda_77BB')
    def lambda_77BB():
        OP_6E(262, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_77BB)

    @scena.Lambda('lambda_77CB')
    def lambda_77CB():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_77CB)

    @scena.Lambda('lambda_77DB')
    def lambda_77DB():
        OP_6C(135000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_77DB)

    WaitForThreadExit(0x0020, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020140984V#014F亚鲁瓦教授……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150140985V#130F哎呀，真是好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150140986V最近发生了不少事情，\n',
            '不过，最后能恢复和平真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150140987V人类这种生物，\n',
            '还是最适合过着平安无事的生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140988V#012F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150140989V#131F哎，怎么了？\n',
            '你的脸色看起来不太好哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150140990V好不容易才当上了正游击士，\n',
            '不是应该高兴点才对吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150140991V#132F对了，我也送你点什么礼物吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150140992V虽然不是什么很值钱的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlayBGM(33)

    @scena.Lambda('lambda_79CF')
    def lambda_79CF():
        OP_6E(276, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_79CF)

    ChrTalk(
        0x0102,
        (
            '#0020140993V#013F第一次在洛连特见到你的时候……\n',
            '我就开始感到很不对劲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140994V虽说现在有些习惯了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140995V但是，每当你出现之时，\n',
            '我的身体都会不由得感到颤抖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150140996V#132F哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140997V#013F而且……各地所发生的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140998V那些记忆被操纵的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140999V凡是有事情发生的地方，\n',
            '你都会以调查为由出现在那里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141000V而且……\n',
            '出现的时间也未免太巧了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141001V#132F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141002V#015F决定性的证据……\n',
            '就是克鲁茨先生的反应……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141003V被抹去记忆的克鲁茨先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141004V在竞技场的观众席上，\n',
            '他也无故地突然感觉不舒服……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141005V而那时……\n',
            '你也在同一个地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141001V#132F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7CAA')
    def lambda_7CAA():
        CameraMove(72320, 250, 43180, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_7CAA)

    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_7CCC')
    def lambda_7CCC():
        ChrJumpTo(0x00FE, 73040, 250, 45860, 500, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7CCC)

    WaitForThreadExit(0x0102, 0x0001)
    ChrWalkTo(0x0102, 72200, 250, 45860, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0020, 400)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020141007V#015F亚鲁瓦教授……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141008V#012F是你干的……没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141009V#136F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141010V被操纵了记忆和认知之后还能\n',
            '察觉到这种地步，真是不简单啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141011V不愧是我制造出来的杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141012V#014F……哎……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141013V#134F那么，我就来解开暗示吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0020, 29)
    ChrSetSubChip(0x0020, 0)

    @scena.Lambda('lambda_7E47')
    def lambda_7E47():
        CameraSetDistance(2600, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7E47)

    ChrWalkTo(0x0020, 71900, 250, 43000, 1000, 0x00)
    ChrSetChipByIndex(0x0020, 30)
    ChrSetSubChip(0x0020, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrSetSubChip(0x0020, 1)
    Sleep(100)

    OP_20(0x00000000)
    PlaySE(188, 0x00, 0x64)
    ChrSetSubChip(0x0020, 2)
    OP_AD('ED6_DT04/C_VIS036._CH', 0x0000, 0x0000, 0x000007D0)
    Sleep(500)

    OP_AD('ED6_DT04/C_VIS028._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(300)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    OP_AD('ED6_DT04/C_VIS029._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(300)

    OP_AD('ED6_DT04/C_VIS030._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(300)

    OP_AD('ED6_DT04/C_VIS031._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(300)

    OP_AD('ED6_DT04/C_VIS032._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(300)

    OP_AD('ED6_DT04/C_VIS037._CH', 0x0000, 0x0000, 0x000003E8)
    Sleep(400)

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x5DC0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000004)
    CreateThread(0x0102, 0x03, 0x00, func_24_A279)
    OP_AE(0x000001F4)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020141014V#514F………………啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0102, 30, 0, 400, 3000)

    @scena.Lambda('lambda_7F95')
    def lambda_7F95():
        OP_6C(153000, 100000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7F95)

    @scena.Lambda('lambda_7FA5')
    def lambda_7FA5():
        OP_67(0, 6900, -10000, 100000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7FA5)

    PlayBGM(90)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020141015V#514F你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141016V……你是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '？？？',
        (
            '#0150141017V#133F哼哼……\n',
            '看来你终于想起我是谁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141018V想起了那个把你那七零八落的心\n',
            '重新组合并修复完整的我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141019V想起了那个赐予虚无的人偶以灵魂的我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141020V#510F拥有能够扭曲和操纵对方的\n',
            '记忆和认知的特殊能力……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141021V七人组『蛇之使徒』其中的一员！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141022V『白面』怀斯曼……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 9)

    @scena.Lambda('lambda_8152')
    def lambda_8152():
        CameraSetDistance(2800, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8152)

    @scena.Lambda('lambda_8162')
    def lambda_8162():
        CameraMove(72010, 650, 45100, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_8162)

    PlaySE(501, 0x00, 0x64)
    ChrJumpTo(0x0102, 72200, 250, 47000, 700, 8000)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141023V#134F嘿嘿……\n',
            '我刚才不是说了『真是好久不见了』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141024V『执行者』No.XIII。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141025V『漆黑之牙』——\n',
            '约修亚·阿斯特雷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141026V#510F是、是你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141027V是你在背后操纵这次的事件！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141028V果然……\n',
            '那个洛伦斯少尉真的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141029V#134F猜得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141030V我并没有消除他的记忆，\n',
            '所以他很快就察觉到你的真实身份。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141031V哈哈，他也应该感到很高兴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141032V#516F你……你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141033V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141034V#510F……是来了结我的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141035V#134F哼哼……\n',
            '没必要摆出这副架势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141036V计划的第一阶段已经顺利完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141037V我只是稍微有点空闲，\n',
            '顺道过来和你叙一下旧而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141038V#510F第一阶段……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141039V是指那个地下遗迹的封印吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141040V#134F阻塞通往『环』之路的『门』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141041V将其开启，就是计划的第一阶段。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141042V#136F哼哼……\n',
            '要想再次关上已经是不可能的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141043V#510F果然……\n',
            '总觉得事情还没那么容易结束……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141044V#515F『辉之环』到底是什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141045V『结社』……\n',
            '你到底有什么企图！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141046V#134F如果想知道的话，\n',
            '不如考虑一下重返『结社』吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141047V是你的话，应该很快就能重操旧业的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141048V虽然意识上稍微有点迟钝，\n',
            '不过治疗一下就能立刻恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141049V#516F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141050V#133F嘿嘿，不要摆出\n',
            '那么一副狰狞可怕的表情嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141051V我知道……我知道\n',
            '你现在有两位很重要的家人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141052V令人尊敬的父亲，\n',
            '还有那个值得自己全心守护的女孩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141053V就算『他』现在站在你面前，\n',
            '你也不会舍得离开那两个人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141054V#013F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141055V#136F所以，我今天才来找你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141056V作为协助完成计划的谢礼，\n',
            '我现在让你正式脱离『结社』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141057V#134F……祝贺你，约修亚。\n',
            '你已经从『结社』解放出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141058V这五年来，真的辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141059V#014F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141060V#514F………………哎………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141061V#137F什么呀，真是没意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141062V还以为你听了之后会表现得很高兴……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141063V#136F唔，难道是感情的那部分结构\n',
            '至今仍存在着缺陷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141064V#590F我……协助计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141065V……哈哈……说什么……\n',
            '你在说什么傻话呀……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141066V#134F啊啊，抱歉。\n',
            '还忘了跟你说明一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141067V你真正的任务不是暗杀，而是谍报。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141068V#014F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141069V#134F一个被『结社』丢弃的孩子，\n',
            '受到别人的同情和无微不至的照顾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141070V而这个孩子不但没有感恩图报，\n',
            '还定期向结社的联络员传达各种报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141071V包括游击士协会的动向……\n',
            '以及卡西乌斯·布莱特的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141072V#514F#4S！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141073V#136F当然，你所做过的这些事，\n',
            '你本人并不会留有丝毫印象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141074V因为我对你施加了暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141075V#518F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141076V#135FＳ级游击士——卡西乌斯·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141077V毫无疑问，\n',
            '这个人是本次计划的最大障碍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141078V假如他当时还在利贝尔，\n',
            '上校的政变必定很快就会被识破和阻止。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141079V#136F为了分析他的性格和行动方式，\n',
            '并将他在毫不知情的情况下引到国外……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141080V你的情报真的是立了大功哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 31)
    ChrSetSubChip(0x0102, 0)

    @scena.Lambda('lambda_8DFA')
    def lambda_8DFA():
        OP_99(0x0102, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8DFA)

    OP_9E(0x0102, 30, 0, 800, 3000)

    ChrTalk(
        0x0102,
        (
            '#0020141081V#517F…………骗……人……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141082V#134F所以……我再次对你表示感谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141083V这五年来，真是辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8EAE')
    def lambda_8EAE():
        OP_99(0x0102, 0x02, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8EAE)

    OP_9E(0x0102, 30, 0, 1200, 3000)

    ChrTalk(
        0x0102,
        (
            '#0020141084V#517F#3S骗人，你在骗人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    @scena.Lambda('lambda_8F00')
    def lambda_8F00():
        OP_99(0x0102, 0x03, 0x06, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8F00)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020141085V#519F#5S这不是真的啊啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_8F5A')
    def lambda_8F5A():
        OP_99(0x0102, 0x06, 0x0C, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8F5A)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020141086V#517F#50W……我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141087V和艾丝蒂尔一起度过的……\n',
            '………这些日子……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141088V#133F嘿嘿……\n',
            '为什么要变得这么难过啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141089V装作什么都不知道，\n',
            '继续和家人幸福地生活在一起不就行了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141090V只要你不说，他们永远也不会知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141091V#517F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141092V#134F不过嘛……\n',
            '仔细想想这也真是残酷的对比。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141093V布莱特家的父女实在是太过完美了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141094V对于你这样的怪物来说，\n',
            '他们所绽放出的光芒是不是太过刺眼了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141095V#518F…………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141096V#134F虽然你能过着人类的正常生活，\n',
            '不过，本质上还是和普通人不一样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141097V这种在任何时候都能想到合理手段，\n',
            '并用以成功完成任务的思考模式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141098V这种能够独自与大部队抗衡的\n',
            '被强化至极限的肉体和反射神经。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141099V我所造出来的最强人类兵器，\n',
            '那就是你——『漆黑之牙』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141100V#518F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141101V#134F这样的你，\n',
            '终究还是不可能和普通人类交往的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141102V就算今后仍然和他们生活在一起，\n',
            '这样的你，也不可能感到幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141100V#518F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141104V#136F所以，要是觉得难受的话，\n',
            '什么时候回来都可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141105V由伟大的主人所统率的魂之结社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141106V#138F我们『噬身之蛇』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0020, 29)
    ChrSetSubChip(0x0020, 0)
    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_9470')
    def lambda_9470():
        CameraMove(72320, 250, 46180, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_9470)

    ChrWalkTo(0x0020, 70330, 250, 46920, 2000, 0x00)

    @scena.Lambda('lambda_949C')
    def lambda_949C():
        OP_6C(134000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_949C)

    @scena.Lambda('lambda_94AC')
    def lambda_94AC():
        ChrWalkTo(0x00FE, 70240, 250, 57660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_94AC)

    Sleep(6000)

    OP_20(0x000007D0)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0020, 0x0001)

    @scena.Lambda('lambda_94DB')
    def lambda_94DB():
        CameraSetDistance(2300, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_94DB)

    OP_21()
    PlayBGM(83)
    Sleep(2000)

    ChrTalk(
        0x0102,
        (
            '#0020141107V#517F#5P#40W……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141108V这是……惩罚吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141109V……姐姐……莱维………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141110V…………我是……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141111V………………………………\n',
            '………………我是………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()

    ExecExpressionWithValue(
        0x0102,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000004)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 1)
    IdleLoop()

    Jump('loc_9614')

    def _loc_9614(): pass

    label('loc_9614')

    Return()

# id: 0x0023 offset: 0x9615
@scena.Code('func_23_9615')
def func_23_9615():
    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0020, 0xFF)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetChipByIndex(0x0101, 32)
    ChrSetPos(0x0101, 42010, 1250, 46960, 102)
    ChrSetPos(0x0020, 58940, 1250, 47080, 263)
    OP_7E(600, -800, -900, 80, 0)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x0039, 0x0080)
    ChrSetFlags(0x003A, 0x0080)
    ChrSetFlags(0x003B, 0x0080)
    ChrSetFlags(0x003C, 0x0080)
    ChrSetFlags(0x003D, 0x0080)
    ChrSetFlags(0x003E, 0x0080)
    ChrSetFlags(0x003F, 0x0080)
    ChrSetFlags(0x0040, 0x0080)
    ChrSetFlags(0x0041, 0x0080)
    ChrSetFlags(0x0042, 0x0080)
    ChrSetFlags(0x0043, 0x0080)
    ChrSetFlags(0x0044, 0x0080)
    ChrSetFlags(0x0045, 0x0080)
    ChrSetFlags(0x0046, 0x0080)
    ChrSetFlags(0x0047, 0x0080)
    ChrSetFlags(0x0048, 0x0080)
    ChrSetFlags(0x0049, 0x0080)
    ChrSetFlags(0x004A, 0x0080)
    ChrSetFlags(0x004B, 0x0080)
    ChrSetFlags(0x004C, 0x0080)
    ChrSetFlags(0x004D, 0x0080)
    ChrSetFlags(0x004E, 0x0080)
    ChrSetFlags(0x004F, 0x0080)
    ChrSetFlags(0x0050, 0x0080)
    ChrSetFlags(0x0051, 0x0080)
    ChrSetFlags(0x0052, 0x0080)
    ChrSetFlags(0x0053, 0x0080)
    ChrSetFlags(0x0054, 0x0080)
    ChrSetFlags(0x0055, 0x0080)
    ChrSetFlags(0x0056, 0x0080)
    ChrSetFlags(0x0057, 0x0080)
    CameraMove(49840, 0, 46640, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    ChrWalkTo(0x0101, 48630, 250, 46920, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010141112V#007F哈啊……\n',
            '竟然等了这么长时间啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141113V天色都已经快黑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141114V#503F约修亚……\n',
            '刚才是怎么想的呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141115V唔～……\n',
            '一想起来脸还会发热呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0020,
        '男性的声音',
        (
            '#0150141116V#1P哦，是艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_9885')
    def lambda_9885():
        ChrTurnDirection(0x00FE, 0x0020, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9885)

    @scena.Lambda('lambda_9893')
    def lambda_9893():
        CameraMove(51060, 0, 46780, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9893)

    @scena.Lambda('lambda_98AB')
    def lambda_98AB():
        ChrWalkTo(0x00FE, 51800, 0, 46980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_98AB)

    Sleep(2000)

    ChrWalkTo(0x0101, 50200, 0, 46980, 2000, 0x00)
    ChrSetFlags(0x0101, 0x1000)
    WaitForThreadExit(0x0020, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010141117V#004F咦，亚鲁瓦教授。\n',
            '在这种地方遇见你真是难得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141118V#130F#4P哈哈，也许吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141119V对了，刚才我也见到约修亚了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141120V还有，在此恭喜一下。\n',
            '听说你们终于成为了正游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141121V#008F嘿嘿……还好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141122V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141123V#131F#4P……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141124V#006F教授你……\n',
            '和平时看起来感觉不太一样啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141125V总觉得你的样子好像特别的高兴。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0150141126V#132F#4P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141127V#130F哈哈，被你看穿了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141128V其实也不是什么特别高兴的事，\n',
            '只是考古学的研究取得了进展而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141129V所以有点喜出望外了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141130V#501F哎～那不是很好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141131V#004F啊……对不起！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141132V冰淇淋快融化了，我得赶快走了！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141133V#001F那么，回头见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9BFA')
    def lambda_9BFA():
        CameraMove(53990, 250, 46840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9BFA)

    @scena.Lambda('lambda_9C12')
    def lambda_9C12():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_9C12')

    DispatchAsync2(0x0020, 0x0001, lambda_9C12)

    ChrWalkTo(0x0101, 51420, 0, 47930, 4000, 0x00)
    ChrWalkTo(0x0101, 60120, 1250, 48000, 4000, 0x00)
    ChrWalkTo(0x0101, 62900, 1250, 51420, 4000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    NpcTalk(
        0x0020,
        '怀斯曼',
        (
            '#0150141134V#136F哼哼，原来如此。\n',
            '卡西乌斯·布莱特的女儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150141135V#134F让我感到越来越有趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    StopEffect(0x04, 0x00)
    CameraMove(67120, 250, 45170, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 65535)
    ChrClearFlags(0x0102, 0x0002)
    ChrSetPos(0x0102, 67120, 250, 45170, 270)
    ChrSetPos(0x0101, 68100, 1250, 54590, 180)

    @scena.Lambda('lambda_9D5C')
    def lambda_9D5C():
        CameraMove(67810, 250, 44960, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9D5C)

    ChrWalkTo(0x0101, 68930, 250, 45010, 4000, 0x00)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010141136V#506F不好意思，我回来晚了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141137V人太多了，好不容易才买到呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020141138V#010F是吗，真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141139V那么我就不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 68380, 250, 44900, 2000, 0x00)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetChipByIndex(0x0101, 33)
    OP_99(0x0101, 0x00, 0x02, 1500)
    Sleep(500)

    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetChipByIndex(0x0101, 34)
    ChrSetChipByIndex(0x0102, 35)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrMoveTo(0x0102, 67500, 250, 44960, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010141140V#008F……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141141V#503F那个，刚才的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141142V#019F啊啊，刚才真抱歉。\n',
            '那种说话方式让你误会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141143V我刚才所说的那些话，\n',
            '的确好像是那种很差劲的告白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141144V#503F哎……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141145V倒也不是什么很差劲的啦……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141146V#010F不过，仔细想想的话，\n',
            '其实也不用这么着急地下结论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141147V既然已经成为了正游击士，\n',
            '当然可以各自发展去做自己想做的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141148V说不定……\n',
            '现在应该考虑一下大家的未来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141149V#008F确、确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141150V#503F（如果结婚的话，就会生小孩呢……）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141151V#504F（……哎呀！我想到哪里去了啊！）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141152V#019F那么，都已经傍晚了，\n',
            '我们吃完冰淇淋就回城去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141153V父亲和大家都在等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141154V#004F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141155V#002F……约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141156V#014F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020141157V是不是想谈关于未来的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141158V#509F不、不是啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141159V#582F总之赶快回城里去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4204._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0024 offset: 0xA279
@scena.Code('func_24_A279')
def func_24_A279():
    OP_77(0x64, 0x64, 0x64, 0x00, 0x00001770)

    Return()

# id: 0x0025 offset: 0xA283
@scena.Code('func_25_A283')
def func_25_A283():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 6, 0x66E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_A290',
    )

    Return()

    def _loc_A290(): pass

    label('loc_A290')

    SetScenaFlags(ScenaFlag(0x00CD, 6, 0x66E))
    EventBegin(0x00)
    CameraMove(37600, 1250, 49080, 2000)
    ChrTurnDirectionByPos(0x0101, 37090, 49010, 400)
    ChrTurnDirectionByPos(0x0102, 37090, 49010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140916V#004F哇啊……\n',
            '好多人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140917V#010F因为今天特别热嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140918V冰淇淋店生意红火也是情理之中的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140919V#007F唔～一看到这样的场景，\n',
            '我就更想吃了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x005B,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x005B,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x005B,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_A3F2')
    def lambda_A3F2():
        OP_69(0x005B, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A3F2)

    ChrTurnDirection(0x0101, 0x0102, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010140920V#501F啊，对了……\n',
            '那个时候的约定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140921V#014F约定……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140922V#507F在王城里面穿女佣服的时候，\n',
            '约修亚，你不是在那里闹别扭吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140923V那时我就答应要请你吃冰淇淋的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140924V#017F你怎么偏偏想起了那件无聊的事情……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140925V#018F我刚才还以为是在那个小公园\n',
            '互相约定的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140926V#503F啊……哦。\n',
            '那、那个我当然还记得啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140927V可是在白天我实在平静不下来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100489V#014F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010140929V#509F总、总而言之等逛了一圈之后，\n',
            '就到百货店后面的小公园去休息！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140930V那时我就请你吃冰淇淋！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140931V这样就ＯＫ了吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140932V#010FＯ、ＯＫ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0026 offset: 0xA6B4
@scena.Code('func_26_A6B4')
def func_26_A6B4():
    EventBegin(0x02)

    ChrTalk(
        0x0102,
        (
            '#0020110945V#010F看起来这里就是\n',
            '艾南先生所说的地下水路的入口。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0027 offset: 0xA75D
@scena.Code('func_27_A75D')
def func_27_A75D():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0028 offset: 0xA7B1
@scena.Code('func_28_A7B1')
def func_28_A7B1():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0029 offset: 0xA805
@scena.Code('func_29_A805')
def func_29_A805():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '《导力时钟第２号》\n',
            '　七耀历１１６３年·蔡斯技术工房制造',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x002A offset: 0xA867
@scena.Code('func_2A_A867')
def func_2A_A867():
    OP_13(0x00BA)

    Return()

# id: 0x002B offset: 0xA86B
@scena.Code('func_2B_A86B')
def func_2B_A86B():
    OP_13(0x00B1)

    Return()

# id: 0x002C offset: 0xA86F
@scena.Code('func_2C_A86F')
def func_2C_A86F():
    OP_13(0x00BB)

    Return()

# id: 0x002D offset: 0xA873
@scena.Code('func_2D_A873')
def func_2D_A873():
    OP_13(0x00BC)

    Return()

# id: 0x002E offset: 0xA877
@scena.Code('func_2E_A877')
def func_2E_A877():
    OP_13(0x00BD)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
