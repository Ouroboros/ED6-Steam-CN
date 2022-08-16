import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
    header.importTable    = ['ED6_DT21/T4101._SN', 'ED6_DT21/T4101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT26/CH20304._CH', 'ED6_DT26/CH20304P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH03060._CH', 'ED6_DT27/CH03060P._CP'),
    ]

# id: 0x10001 offset: 0x162
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵达克特',
            x                   = 71040,
            z                   = 0,
            y                   = -9000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '士兵贝尔坎',
            x                   = 74970,
            z                   = 0,
            y                   = 71250,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '娜碧',
            x                   = 100180,
            z                   = 250,
            y                   = 33080,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '米亚尔',
            x                   = 52990,
            z                   = 250,
            y                   = 46290,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '戈万',
            x                   = 52990,
            z                   = 250,
            y                   = 44530,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '帕菲',
            x                   = 39700,
            z                   = 1250,
            y                   = 46260,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '娜娜',
            x                   = 39700,
            z                   = 1250,
            y                   = 47860,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 70490,
            z                   = 250,
            y                   = 6990,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 71500,
            z                   = 750,
            y                   = 7870,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '索露贝',
            x                   = 37580,
            z                   = 1250,
            y                   = 49800,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '卡拉莉丝',
            x                   = 48810,
            z                   = 250,
            y                   = 49340,
            direction           = 227,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '尼莫',
            x                   = 49630,
            z                   = 0,
            y                   = 61870,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '吉米',
            x                   = 50410,
            z                   = 0,
            y                   = 81110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '拉奥尼',
            x                   = 81160,
            z                   = 0,
            y                   = -2940,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '梅夏',
            x                   = 69020,
            z                   = 250,
            y                   = 4960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '维尔娜婆婆',
            x                   = 63010,
            z                   = 0,
            y                   = 62930,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 93700,
            z                   = 0,
            y                   = 32900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 53830,
            z                   = 250,
            y                   = 24100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 54040,
            z                   = 250,
            y                   = 8750,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '玲',
            x                   = 42240,
            z                   = 1250,
            y                   = 51400,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 41280,
            z                   = 1250,
            y                   = 52380,
            direction           = 146,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 45300,
            z                   = 250,
            y                   = 76500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 45300,
            z                   = 250,
            y                   = 77950,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '贝利',
            x                   = 69930,
            z                   = 250,
            y                   = 67560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '旅行者',
            x                   = 49030,
            z                   = 0,
            y                   = -3820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 73950,
            z                   = 250,
            y                   = 44280,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 47630,
            z                   = 250,
            y                   = 29460,
            direction           = 257,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 124170,
            z                   = -3500,
            y                   = 72870,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '莉西娅',
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
            name                = '格斯塔夫维修长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '菲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '运输车',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯诺娜',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            name                = '强化猎兵',
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
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '装甲猎豹',
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
            name                = '装甲猎豹',
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
            name                = '奈尔',
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
            name                = '朵洛希',
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
    )

# id: 0x10002 offset: 0xA62
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA62
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 42000,
            y           = -2000,
            z           = 71500,
            range       = 59000,
            dword_10    = 0x000007D0,
            dword_14    = 0x000122A0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 109720,
            y           = 1000,
            z           = 32980,
            range       = 2000,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000024,
        ),
        ScenaEventData(
            x           = 76740,
            y           = 1000,
            z           = 23010,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 69950,
            y           = 1000,
            z           = 14290,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 63260,
            y           = 1000,
            z           = 22960,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 69910,
            y           = 1000,
            z           = 31710,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 42920,
            y           = 0,
            z           = 81110,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000026,
        ),
        ScenaEventData(
            x           = 70940,
            y           = 0,
            z           = -9490,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000027,
        ),
        ScenaEventData(
            x           = 75010,
            y           = 0,
            z           = 71300,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000028,
        ),
    )

# id: 0x10004 offset: 0xB82
@scena.ActorData('ActorData')
def ActorData():
    return (
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
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
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
            talkFunctionIndex   = 0x0023,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xBCA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 7, 0x161F)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C08',
    )

    ChrSetPos(0x0009, 77220, 250, 71250, 180)
    ChrSetPos(0x0013, 47790, 250, 48080, 37)
    ChrSetFlags(0x0013, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C08',
    )

    ChrClearFlags(0x0013, 0x0010)

    def _loc_C08(): pass

    label('loc_C08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 3, 0x161B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C24',
    )

    ChrSetPos(0x0008, 68770, 250, -9000, 0)

    def _loc_C24(): pass

    label('loc_C24')

    CreateThread(0x0019, 0x02, 0x00, func_09_181F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C53',
    )

    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)

    Jump('loc_E74')

    def _loc_C53(): pass

    label('loc_C53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_CB5',
    )

    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0012, 0x0010)
    ChrSetPos(0x0013, 47790, 250, 48080, 37)
    ChrSetPos(0x001D, 47840, 250, 78050, 2)
    ChrSetPos(0x001E, 47840, 250, 79500, 180)
    ChrSetPos(0x0022, 42990, 1250, 52970, 29)
    ChrSetFlags(0x001D, 0x0010)

    Jump('loc_E74')

    def _loc_CB5(): pass

    label('loc_CB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_D19',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetPos(0x0013, 49630, 0, 61870, 45)
    ChrSetPos(0x001D, 53310, 250, 72710, 324)
    ChrSetPos(0x001E, 53180, 250, 74370, 320)
    ChrSetPos(0x001F, 60880, 250, 67010, 180)
    ChrSetPos(0x0022, 53110, 250, 8150, 273)

    Jump('loc_E74')

    def _loc_D19(): pass

    label('loc_D19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DB3',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetPos(0x0013, 49630, 0, 61870, 45)
    ChrSetPos(0x001D, 53140, 250, 23270, 180)
    ChrSetPos(0x001E, 53500, 250, 22190, 315)
    ChrSetPos(0x001F, 71900, 250, 60850, 9)
    ChrSetPos(0x0022, 56200, 250, 26240, 252)
    ChrSetPos(0x0023, 124210, -3500, 70990, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB0',
    )

    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001B, 0x0080)

    def _loc_DB0(): pass

    label('loc_DB0')

    Jump('loc_E74')

    def _loc_DB3(): pass

    label('loc_DB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_E21',
    )

    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetPos(0x0013, 47790, 250, 48080, 37)
    ChrSetPos(0x001D, 93990, 0, 34340, 180)
    ChrSetPos(0x001E, 93990, 0, 32670, 0)
    ChrSetPos(0x0022, 39640, 1250, 51520, 221)
    ChrSetPos(0x0023, 124210, -3500, 70990, 270)

    Jump('loc_E74')

    def _loc_E21(): pass

    label('loc_E21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_E74',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x001D, 107750, 1250, 32920, 93)
    ChrSetPos(0x001E, 109710, 1650, 31920, 75)
    ChrSetPos(0x0023, 124210, -3500, 70990, 270)

    def _loc_E74(): pass

    label('loc_E74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_E8A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_0F_3968)

    Jump('loc_F46')

    def _loc_E8A(): pass

    label('loc_E8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_EA0',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_14_4107)

    Jump('loc_F46')

    def _loc_EA0(): pass

    label('loc_EA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_F22',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_77(0xFF, 0xBD, 0xA7, 0x00, 0x00000000)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    Event(1, 0x001D)

    Jump('loc_F46')

    def _loc_F22(): pass

    label('loc_F22')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_F2E'),
        (-1, 'loc_F46'),
    )

    def _loc_F2E(): pass

    label('loc_F2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 2, 0x1622)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F43',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0E_2CE0)

    def _loc_F43(): pass

    label('loc_F43')

    Jump('loc_F46')

    def _loc_F46(): pass

    label('loc_F46')

    Return()

# id: 0x0001 offset: 0xF47
@scena.Code('func_01_F47')
def func_01_F47():
    OP_16(0x02, 4000, -46000, -90000, 2293852)

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
        'loc_F79',
    )

    OP_B1('t4101_y')

    Jump('loc_F82')

    def _loc_F79(): pass

    label('loc_F79')

    OP_B1('t4101_n')

    def _loc_F82(): pass

    label('loc_F82')

    OP_71(0x0011, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F9C',
    )

    OP_10(0x0C, 0x01)
    OP_10(0x0B, 0x00)

    Jump('loc_FB2')

    def _loc_F9C(): pass

    label('loc_F9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_FAC',
    )

    OP_10(0x0C, 0x00)
    OP_10(0x0B, 0x01)

    Jump('loc_FB2')

    def _loc_FAC(): pass

    label('loc_FAC')

    OP_10(0x0B, 0x00)
    OP_10(0x0C, 0x01)

    def _loc_FB2(): pass

    label('loc_FB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FC6',
    )

    OP_71(0x0009, 0x0010)
    OP_1C(0x09, 0x00, 0x0029)

    Jump('loc_102C')

    def _loc_FC6(): pass

    label('loc_FC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1013',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_FE1',
    )

    OP_71(0x0009, 0x0010)
    OP_1C(0x09, 0x00, 0x0029)

    Jump('loc_FE6')

    def _loc_FE1(): pass

    label('loc_FE1')

    OP_72(0x0009, 0x0010)

    def _loc_FE6(): pass

    label('loc_FE6')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_FF2'),
        (-1, 'loc_1010'),
    )

    def _loc_FF2(): pass

    label('loc_FF2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1010',
    )

    OP_71(0x0009, 0x0010)
    OP_1C(0x09, 0x00, 0x0029)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1010')

    def _loc_1010(): pass

    label('loc_1010')

    Jump('loc_102C')

    def _loc_1013(): pass

    label('loc_1013')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 7, 0x161F)),
            Expr.Return,
        ),
        'loc_1027',
    )

    OP_71(0x0009, 0x0010)
    OP_1C(0x09, 0x00, 0x0029)

    Jump('loc_102C')

    def _loc_1027(): pass

    label('loc_1027')

    OP_72(0x0009, 0x0010)

    def _loc_102C(): pass

    label('loc_102C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1040',
    )

    OP_71(0x000A, 0x0010)
    OP_1C(0x0A, 0x00, 0x0029)

    Jump('loc_10A6')

    def _loc_1040(): pass

    label('loc_1040')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_108D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_105B',
    )

    OP_71(0x000A, 0x0010)
    OP_1C(0x0A, 0x00, 0x0029)

    Jump('loc_1060')

    def _loc_105B(): pass

    label('loc_105B')

    OP_72(0x000A, 0x0010)

    def _loc_1060(): pass

    label('loc_1060')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_106C'),
        (-1, 'loc_108A'),
    )

    def _loc_106C(): pass

    label('loc_106C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_108A',
    )

    OP_71(0x000A, 0x0010)
    OP_1C(0x0A, 0x00, 0x0029)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_108A')

    def _loc_108A(): pass

    label('loc_108A')

    Jump('loc_10A6')

    def _loc_108D(): pass

    label('loc_108D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 3, 0x161B)),
            Expr.Return,
        ),
        'loc_10A1',
    )

    OP_71(0x000A, 0x0010)
    OP_1C(0x0A, 0x00, 0x0029)

    Jump('loc_10A6')

    def _loc_10A1(): pass

    label('loc_10A1')

    OP_72(0x000A, 0x0010)

    def _loc_10A6(): pass

    label('loc_10A6')

    OP_72(0x0005, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0007, 0x0010)
    OP_72(0x0008, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0040)"),
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10FE',
    )

    OP_71(0x0005, 0x0010)
    OP_71(0x0006, 0x0010)
    OP_71(0x0007, 0x0010)
    OP_71(0x0008, 0x0010)
    OP_1C(0x05, 0x01, 0x004A)
    OP_1C(0x06, 0x01, 0x0049)
    OP_1C(0x07, 0x01, 0x0049)
    OP_1C(0x08, 0x01, 0x004B)

    def _loc_10FE(): pass

    label('loc_10FE')

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x0100)"),
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_112D',
    )

    OP_71(0x0005, 0x0010)
    OP_71(0x0006, 0x0010)
    OP_71(0x0007, 0x0010)
    OP_71(0x0008, 0x0010)

    def _loc_112D(): pass

    label('loc_112D')

    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_113E',
    )

    OP_72(0x000B, 0x0010)

    def _loc_113E(): pass

    label('loc_113E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_117A',
    )

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 59)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 59)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 59)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 59)

    def _loc_117A(): pass

    label('loc_117A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1268',
    )

    LoadChip('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP', 0)
    LoadChip('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP', 1)
    LoadChip('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP', 2)
    LoadChip('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP', 3)
    LoadChip('ED6_DT26/CH20304._CH', 'ED6_DT26/CH20304P._CP', 4)
    LoadChip('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP', 5)
    LoadChip('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP', 6)
    LoadChip('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP', 7)
    LoadChip('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP', 8)
    LoadChip('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP', 9)
    LoadChip('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP', 10)
    LoadChip('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP', 11)
    LoadChip('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP', 12)
    LoadChip('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP', 13)
    LoadChip('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP', 14)
    LoadChip('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP', 15)
    LoadChip('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP', 16)
    LoadChip('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP', 17)
    LoadChip('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP', 18)
    LoadChip('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP', 19)
    LoadChip('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP', 20)
    LoadChip('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP', 21)
    LoadChip('ED6_DT27/CH03060._CH', 'ED6_DT27/CH03060P._CP', 22)

    def _loc_1268(): pass

    label('loc_1268')

    Return()

# id: 0x0002 offset: 0x1269
@scena.Code('func_02_1269')
def func_02_1269():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_128C',
    )

    OP_8D(0x00FE, 102900, 37500, 97550, 28500, 2000)

    Jump('func_02_1269')

    def _loc_128C(): pass

    label('loc_128C')

    Return()

# id: 0x0003 offset: 0x128D
@scena.Code('func_03_128D')
def func_03_128D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1379',
    )

    ChrWalkTo(0x00FE, 52470, 0, -2940, 2500, 0x00)
    ChrWalkTo(0x00FE, 50290, 0, 140, 2500, 0x00)
    ChrWalkTo(0x00FE, 50290, 0, 62250, 2500, 0x00)
    ChrWalkTo(0x00FE, 53220, 0, 65700, 2500, 0x00)
    ChrWalkTo(0x00FE, 88770, 0, 64700, 2500, 0x00)
    ChrWalkTo(0x00FE, 90900, 0, 64390, 2500, 0x00)
    ChrWalkTo(0x00FE, 91360, 0, 33390, 2500, 0x00)
    ChrSetDirection(0x0015, 90, 400)
    Sleep(4000)

    ChrWalkTo(0x00FE, 91360, 0, 32390, 2500, 0x00)
    ChrSetDirection(0x0015, 90, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 90450, 0, 1230, 2500, 0x00)
    ChrWalkTo(0x00FE, 88850, 0, -1860, 2500, 0x00)

    Jump('func_03_128D')

    def _loc_1379(): pass

    label('loc_1379')

    Return()

# id: 0x0004 offset: 0x137A
@scena.Code('func_04_137A')
def func_04_137A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1426',
    )

    ChrWalkTo(0x00FE, 52890, 0, 62930, 2000, 0x00)
    ChrWalkTo(0x00FE, 51980, 0, 62040, 2000, 0x00)
    ChrWalkTo(0x00FE, 51980, 0, 2070, 2000, 0x00)
    ChrWalkTo(0x00FE, 52970, 0, 830, 2000, 0x00)
    ChrWalkTo(0x00FE, 87440, 0, 830, 2000, 0x00)
    ChrWalkTo(0x00FE, 88280, 0, 1720, 2000, 0x00)
    ChrWalkTo(0x00FE, 88280, 0, 61270, 2000, 0x00)
    ChrWalkTo(0x00FE, 87410, 40, 62930, 2000, 0x00)

    Jump('func_04_137A')

    def _loc_1426(): pass

    label('loc_1426')

    Return()

# id: 0x0005 offset: 0x1427
@scena.Code('func_05_1427')
def func_05_1427():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_155F',
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
    ChrWalkTo(0x00FE, 72040, 1250, 11710, 2500, 0x00)
    ChrWalkTo(0x00FE, 68840, 1250, 10030, 2500, 0x00)
    ChrWalkTo(0x00FE, 68840, 250, 5830, 2500, 0x00)

    Jump('func_05_1427')

    def _loc_155F(): pass

    label('loc_155F')

    Return()

# id: 0x0006 offset: 0x1560
@scena.Code('func_06_1560')
def func_06_1560():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1604',
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

    Jump('func_06_1560')

    def _loc_1604(): pass

    label('loc_1604')

    Return()

# id: 0x0007 offset: 0x1605
@scena.Code('func_07_1605')
def func_07_1605():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1709',
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

    Jump('func_07_1605')

    def _loc_1709(): pass

    label('loc_1709')

    Return()

# id: 0x0008 offset: 0x170A
@scena.Code('func_08_170A')
def func_08_170A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_181E',
    )

    ChrWalkTo(0x00FE, 54000, 250, 4230, 2500, 0x00)
    ChrSetDirection(0x00FE, 225, 400)
    Sleep(1500)

    Call(0, 0x000A)
    ChrWalkTo(0x00FE, 85860, 250, 4230, 2500, 0x00)
    ChrSetDirection(0x00FE, 135, 400)
    Sleep(1500)

    Call(0, 0x000A)
    ChrWalkTo(0x00FE, 85060, 250, 59050, 2500, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(1500)

    Call(0, 0x000A)
    ChrWalkTo(0x00FE, 69510, 250, 59050, 2500, 0x00)
    ChrWalkTo(0x00FE, 69510, 1250, 53930, 2500, 0x00)
    ChrWalkTo(0x00FE, 61050, 1250, 53930, 2500, 0x00)
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(1500)

    Call(0, 0x000A)
    ChrWalkTo(0x00FE, 61050, 1250, 47180, 2500, 0x00)
    ChrWalkTo(0x00FE, 55030, 250, 47180, 2500, 0x00)
    ChrWalkTo(0x00FE, 55030, 250, 25990, 2500, 0x00)
    ChrWalkTo(0x00FE, 53830, 250, 24100, 2500, 0x00)

    Jump('func_08_170A')

    def _loc_181E(): pass

    label('loc_181E')

    Return()

# id: 0x0009 offset: 0x181F
@scena.Code('func_09_181F')
def func_09_181F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_187F',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x4B0),
            Expr.Add,
            (Expr.GetChrWork, 0x1A, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x4B0),
            Expr.Sub,
            (Expr.GetChrWork, 0x1A, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Add,
            (Expr.GetChrWork, 0x1A, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x4B0),
            Expr.Sub,
            (Expr.GetChrWork, 0x1A, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1873',
    )

    OP_4B(0x00FE, 0)

    Jump('loc_1877')

    def _loc_1873(): pass

    label('loc_1873')

    OP_4A(0x00FE, 0)

    def _loc_1877(): pass

    label('loc_1877')

    Sleep(100)

    Jump('func_09_181F')

    def _loc_187F(): pass

    label('loc_187F')

    Return()

# id: 0x000A offset: 0x1880
@scena.Code('func_0A_1880')
def func_0A_1880():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_18DA',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x2328),
            Expr.Add,
            (Expr.GetChrWork, 0x19, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x2328),
            Expr.Sub,
            (Expr.GetChrWork, 0x19, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x2328),
            Expr.Add,
            (Expr.GetChrWork, 0x19, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x2328),
            Expr.Sub,
            (Expr.GetChrWork, 0x19, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18D2',
    )

    Sleep(100)

    Return()

    def _loc_18D2(): pass

    label('loc_18D2')

    Sleep(100)

    Jump('func_0A_1880')

    def _loc_18DA(): pass

    label('loc_18DA')

    Return()

# id: 0x000B offset: 0x18DB
@scena.Code('func_0B_18DB')
def func_0B_18DB():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0108, 70950, 0, -6900, 180)
    ChrSetPos(0x0101, 71720, 0, -5910, 180)
    ChrSetPos(0x0105, 70350, 0, -5760, 180)
    ChrSetPos(0x0104, 70950, 0, -4800, 180)
    CameraMove(71730, 0, -7500, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x0008, 0, 0)
    ChrSetSubChip(0x0008, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 4, 0x166C)),
            Expr.Return,
        ),
        'loc_1A14',
    )

    ChrTalk(
        0x0008,
        (
            '#2220250480V啊，金先生。\n',
            '辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2220250481V请问有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250482V#070F#6P嗯，我有事要找\n',
            '爱尔莎大使商量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250483V她现在在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B09')

    def _loc_1A14(): pass

    label('loc_1A14')

    ChrTalk(
        0x0108,
        (
            '#0080250484V#071F#6P哟，兄弟，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250485V咦？\n',
            '这不是金先生吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250486V你又来利贝尔\n',
            '玩了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250487V#070F#6P哈哈，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250488V来打个招呼，顺便有事要找\n',
            '爱尔莎大使商量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250483V她现在在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B09(): pass

    label('loc_1B09')

    ChrTalk(
        0x0008,
        (
            '#2220250490V她没有外出，\n',
            '应该在的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250491V对了，那边的各位呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250492V#070F#6P是我在协会的工作伙伴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250493V正准备介绍给\n',
            '我们的大使呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250494V嘿嘿，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250495V反正只要是金先生的\n',
            '朋友，放行也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    PlaySE(115, 0x00, 0x64)
    Sleep(500)

    OP_6F(0x000A, 0)
    OP_70(0x000A, 60)
    Sleep(1000)

    ChrWalkTo(0x0008, 68770, 250, -9000, 3000, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2220250496V请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250497V啊，因为大使馆的领域内\n',
            '拥有治外法权，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2220250498V言行举止请\n',
            '谨慎一些哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250499V#1006F#5P听见没，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250500V#034F唉，你们真不信任我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 71150, 0, -6670, 180)
    ChrSetPos(0x0001, 71150, 0, -6670, 180)
    ChrSetPos(0x0002, 71150, 0, -6670, 180)
    ChrSetPos(0x0003, 71150, 0, -6670, 180)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x02C3, 3, 0x161B))
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x1DB7
@scena.Code('func_0C_1DB7')
def func_0C_1DB7():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0104, 75060, 0, 69850, 0)
    ChrSetPos(0x0101, 74090, 0, 68370, 0)
    ChrSetPos(0x0105, 75800, 0, 68680, 0)
    ChrSetPos(0x0108, 74770, 0, 67260, 0)
    CameraMove(75780, 0, 70890, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x0009, 180, 0)
    ChrSetSubChip(0x0009, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 5, 0x166D)),
            Expr.Return,
        ),
        'loc_1EDB',
    )

    ChrTalk(
        0x0009,
        (
            '#3190250665V#5P哎呀，奥利维尔先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250666V#035F#6P呵呵，你工作辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250667V#030F我想进去，\n',
            '请问能不能放行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2149')

    def _loc_1EDB(): pass

    label('loc_1EDB')

    ChrTalk(
        0x0104,
        (
            '#0040250635V#031F#6P哟，士兵朋友。\n',
            '你还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#3190250636V#5P奥、奥利维尔先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250637V#5P你之前都在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250638V#033F#6P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250639V#5P不是怎么不怎么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250640V#5P你去亚尔摩后就\n',
            '就行踪不明了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250641V#5P穆拉先生可生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250642V#035F#6P呼……\n',
            '这个男人还是那么可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250643V#1007F#6P对了，奥利维尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250644V#1019F难道你没告诉\n',
            '大使馆你和我们\n',
            '在一起行动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250645V#031F#6P哈哈哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250646V寻求爱的彷徨旅途\n',
            '是注定要隐忍的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250647V#030F先不说这些……\n',
            '能不能让我进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2149(): pass

    label('loc_2149')

    ChrTalk(
        0x0009,
        (
            '#3190250648V#5P这倒没问题……\n',
            '请问那边的几位是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250649V#1006F#6P我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250650V有点事想问问\n',
            '这里的大使先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250651V所以就让这个得意忘形的大赖皮蛋\n',
            '来介绍我们认识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250652V#5P原来是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250653V#5P身份也确认了，\n',
            '应该能放行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250654V#5P不过不巧的是达维尔大使\n',
            '和穆拉先生一同外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250655V#033F#6P哎呀，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 180, 400)

    ChrTalk(
        0x0104,
        (
            '#0040250656V#030F#5P怎么办？艾丝蒂尔。\n',
            '要在里面等吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250657V#1015F#6P嗯…虽然那样也可以……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250658V#1006F但我们并没有太多的时间，\n',
            '还是先去别的地方转转吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250659V#040F#2P那么，我们先去拜访\n',
            '共和国大使馆吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250660V同样也在东街区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250661V#070F是啊。\n',
            '回来也方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250662V#1006F#6P那就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250663V士兵先生。\n',
            '我们一会儿再回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250664V#5P嗯，恭候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    ChrSetDirection(0x0009, 180, 0)
    CameraMove(74860, 0, 68920, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 74860, 0, 68920, 0)
    ChrSetPos(0x0001, 74860, 0, 68920, 0)
    ChrSetPos(0x0002, 74860, 0, 68920, 0)
    ChrSetPos(0x0003, 74860, 0, 68920, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x02C3, 6, 0x161E))
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x2524
@scena.Code('func_0D_2524')
def func_0D_2524():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0104, 75060, 0, 69850, 0)
    ChrSetPos(0x0101, 74090, 0, 68370, 0)
    ChrSetPos(0x0105, 75800, 0, 68680, 0)
    ChrSetPos(0x0108, 74770, 0, 67260, 0)
    CameraMove(75780, 0, 70890, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x0009, 180, 0)
    ChrSetSubChip(0x0009, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_266B',
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
        0,
        (
            TXT(0x00, '【◇第一次和贝尔坎说话的情况下】\n'),
            TXT(0x01, '【◇已经和贝尔坎说过话的情况下】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_265F'),
        (0x00000001, 'loc_2665'),
        (-1, 'loc_266B'),
    )

    def _loc_265F(): pass

    label('loc_265F')

    ClearScenaFlags(ScenaFlag(0x02C3, 6, 0x161E))

    Jump('loc_266B')

    def _loc_2665(): pass

    label('loc_2665')

    SetScenaFlags(ScenaFlag(0x02C3, 6, 0x161E))

    Jump('loc_266B')

    def _loc_266B(): pass

    label('loc_266B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 6, 0x161E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 5, 0x166D)),
            Expr.Return,
        ),
        'loc_2702',
    )

    ChrTalk(
        0x0009,
        (
            '#3190250665V#5P哎呀，奥利维尔先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250666V#035F#6P呵呵，你工作辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250667V#030F我想进去，\n',
            '请问能不能放行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2970')

    def _loc_2702(): pass

    label('loc_2702')

    ChrTalk(
        0x0104,
        (
            '#0040250635V#031F#6P哟，士兵朋友。\n',
            '你还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#3190250636V#5P奥、奥利维尔先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250637V#5P你之前都在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250638V#033F#6P咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250639V#5P不是怎么不怎么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250640V#5P你去亚尔摩后就\n',
            '就行踪不明了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250641V#5P穆拉先生可生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250642V#035F#6P呼……\n',
            '这个男人还是那么可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250643V#1007F#6P对了，奥利维尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250644V#1019F难道你没告诉\n',
            '大使馆你和我们\n',
            '在一起行动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250645V#031F#6P哈哈哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250646V寻求爱的彷徨旅途\n',
            '是注定要隐忍的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250647V#030F先不说这些……\n',
            '能不能让我进去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2970(): pass

    label('loc_2970')

    ChrTalk(
        0x0009,
        (
            '#3190250648V#5P这倒没问题……\n',
            '请问那边的几位是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250649V#1006F#6P我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250650V有点事想问问\n',
            '这里的大使先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250651V所以就让这个得意忘形的大赖皮蛋\n',
            '来介绍我们认识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250652V#5P原来是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250686V#5P身份也确认了，\n',
            '看来可以让你们进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7C')

    def _loc_2AA1(): pass

    label('loc_2AA1')

    ChrTalk(
        0x0009,
        (
            '#3190250687V#5P啊，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250688V#5P就在刚才达维尔大使和\n',
            '穆拉先生已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250689V#031F#6P呵呵，看来我们来得是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250690V#1011F#6P那么，能不能放行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250691V#5P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2B7C(): pass

    label('loc_2B7C')

    ChrSetDirection(0x0009, 0, 400)
    PlaySE(115, 0x00, 0x64)
    Sleep(500)

    OP_6F(0x0009, 0)
    OP_70(0x0009, 60)
    Sleep(1000)

    ChrWalkTo(0x0009, 77220, 250, 71250, 3000, 0x00)
    ChrSetDirection(0x0009, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#3190250692V#5P请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3190250693V#5P因为大使馆的领域内\n',
            '有治外法权，\n',
            '所以请小心一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230422V#1006F#6P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    ChrSetDirection(0x0009, 180, 0)
    CameraMove(74870, 0, 68640, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 74870, 0, 68640, 0)
    ChrSetPos(0x0001, 74870, 0, 68640, 0)
    ChrSetPos(0x0002, 74870, 0, 68640, 0)
    ChrSetPos(0x0003, 74870, 0, 68640, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x02C3, 7, 0x161F))
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x2CE0
@scena.Code('func_0E_2CE0')
def func_0E_2CE0():
    EventBegin(0x00)
    OP_4A(0x0015, 255)
    OP_4A(0x0017, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E55',
    )

    FadeOut(0, 0, -1)

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
            TXT(0x00, '【◇还没去过城里的各处目标（听说了奈尔不在）】\n'),
            TXT(0x01, '【◇还没去过城里的各处目标（没听说奈尔不在）】\n'),
            TXT(0x02, '【◇去过城里的各处目标（听说了奈尔不在）】\n'),
            TXT(0x03, '【◇去过城里的各处目标（没听说奈尔不在）】\n'),
            TXT(0x04, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_2E01'),
        (0x00000001, 'loc_2E16'),
        (0x00000002, 'loc_2E2B'),
        (0x00000003, 'loc_2E40'),
        (-1, 'loc_2E55'),
    )

    def _loc_2E01(): pass

    label('loc_2E01')

    ClearScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    ClearScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    ClearScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    ClearScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    ClearScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02D0, 0, 0x1680))

    Jump('loc_2E55')

    def _loc_2E16(): pass

    label('loc_2E16')

    ClearScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    ClearScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    ClearScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    ClearScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    ClearScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    ClearScenaFlags(ScenaFlag(0x02D0, 0, 0x1680))

    Jump('loc_2E55')

    def _loc_2E2B(): pass

    label('loc_2E2B')

    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    SetScenaFlags(ScenaFlag(0x02D0, 0, 0x1680))

    Jump('loc_2E55')

    def _loc_2E40(): pass

    label('loc_2E40')

    SetScenaFlags(ScenaFlag(0x02C4, 3, 0x1623))
    SetScenaFlags(ScenaFlag(0x02C4, 4, 0x1624))
    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C4, 7, 0x1627))
    ClearScenaFlags(ScenaFlag(0x02D0, 0, 0x1680))

    Jump('loc_2E55')

    def _loc_2E55(): pass

    label('loc_2E55')

    ChrSetPos(0x0104, 75810, 0, 65960, 0)
    ChrSetPos(0x0101, 74720, 0, 65970, 0)
    ChrSetPos(0x0105, 76080, 0, 64650, 0)
    ChrSetPos(0x0108, 74790, 0, 64580, 9)
    ChrSetPos(0x0130, 75150, 0, 67480, 180)
    CameraMove(74330, 0, 66970, 0)
    OP_67(0, 6020, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(308000, 0)
    OP_6E(262, 0)
    OP_6F(0x0009, 60)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010250838V#1006F#1P穆拉先生，谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250839V多亏你的帮忙，我们从大使先生\n',
            '那里听到了很多事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0130,
        (
            '#0110250840V#277F#2P哪里……\n',
            '没什么大不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250841V而且这本来也是三个国家的问题，\n',
            '我当然要配合你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250842V#070F#1P哈哈，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250843V#542F#6P要是能有办法\n',
            '解决就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250844V#032F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250845V#1004F#5P啊……\n',
            '怎么了，奥利维尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 270, 400)

    ChrTalk(
        0x0104,
        (
            '#0040250846V#030F不……想了点事情而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250847V和恐吓事件无关，\n',
            '不用介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250848V#1015F#5P嗯、嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0130,
        (
            '#0110250849V#270F#2P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250850V#272F奥利维尔，留在王都的期间，\n',
            '你会住在大使馆吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 0, 400)

    ChrTalk(
        0x0104,
        (
            '#0040250851V#031F呵呵，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250852V就像平时一样，躺在你的\n',
            '床上做着甜美的梦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250853V#1004F#5P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250854V#044F#6P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0130, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0130,
        (
            '#0110250855V#274F#2P……小姐们会信以为真的，\n',
            '别开这种无聊的玩笑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250856V再开过分的玩笑我就用席子\n',
            '把你卷起来扔到地板上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040250857V#037F讨厌，难道\n',
            '这就是所谓的捆绑游戏……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0130,
        (
            '#0110250858V#276F#2P如果你希望的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250859V我还可以把你像\n',
            '结草虫一样吊在窗口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040250860V#034F对不起。\n',
            '我太得意忘形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250861V#1016F#1P嗯，不愧从小到大的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250862V#071F#1P哈哈，不管嘴上说什么，\n',
            '脾气还是很合拍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0130,
        (
            '#0110250863V#272F#2P请不要说得\n',
            '这么别扭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250864V#277F算了……\n',
            '我就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110250865V请你们努力调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250866V#1006F#1P嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0130, 0, 400)

    @scena.Lambda('lambda_34FA')
    def lambda_34FA():
        CameraMove(74890, 0, 70490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_34FA)

    @scena.Lambda('lambda_3512')
    def lambda_3512():
        ChrWalkTo(0x0130, 74380, 0, 77210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0130, 0x0001, lambda_3512)

    Sleep(4000)

    OP_4A(0x0009, 255)
    ChrSetDirection(0x0009, 270, 400)
    ChrWalkTo(0x0009, 74970, 0, 71250, 2000, 0x00)
    ChrSetDirection(0x0009, 0, 400)
    PlaySE(110, 0x00, 0x64)
    OP_71(0x0009, 0x0010)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)
    Sleep(1500)

    ChrWalkTo(0x0009, 77220, 250, 71250, 2000, 0x00)
    ChrSetDirection(0x0009, 180, 400)
    OP_4B(0x0009, 255)

    @scena.Lambda('lambda_3594')
    def lambda_3594():
        CameraMove(74740, 0, 65560, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3594)

    @scena.Lambda('lambda_35AC')
    def lambda_35AC():
        ChrSetDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35AC)

    ChrSetDirection(0x0009, 180, 400)
    ChrSetDirection(0x0104, 180, 400)
    WaitForThreadExit(0x0101, 0x0002)
    ChrSetFlags(0x0130, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3710',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 0, 0x1680)),
            Expr.Return,
        ),
        'loc_366D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250867V#1006F#5P好了……\n',
            '还没到傍晚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250868V先去格兰赛尔城，\n',
            '然后再去利贝尔通讯社吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250869V#040F#6P嗯，就这么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_370D')

    def _loc_366D(): pass

    label('loc_366D')

    ChrTalk(
        0x0101,
        (
            '#0010250870V#1006F#5P两个大使馆都解决了，\n',
            '剩下的就是城堡和利贝尔通讯社了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250871V要是能有线索就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250872V#040F是啊……\n',
            '总之去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_370D(): pass

    label('loc_370D')

    Jump('loc_38B8')

    def _loc_3710(): pass

    label('loc_3710')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 0, 0x1680)),
            Expr.Return,
        ),
        'loc_37E6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040250873V#030F#2P不过已经傍晚了呢……\n',
            '时间过得真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250874V#040F#6P可能奈尔先生\n',
            '也回通讯社了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250875V#1011F#5P嗯，也对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250876V#070F#3P好。\n',
            '我们去通讯社看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38B8')

    def _loc_37E6(): pass

    label('loc_37E6')

    ChrTalk(
        0x0104,
        (
            '#0040250877V#030F#2P不过已经傍晚了呢……\n',
            '时间过得真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250878V#040F#6P就只剩下\n',
            '利贝尔通讯社没去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250879V#1006F#5P嗯，对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250880V#070F#3P时间也差不多了。\n',
            '快去拜访一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38B8(): pass

    label('loc_38B8')

    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x2F, 0xFF)
    CameraMove(74890, 0, 65620, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 74890, 0, 65620, 180)
    ChrSetPos(0x0001, 74890, 0, 65620, 180)
    ChrSetPos(0x0002, 74890, 0, 65620, 180)
    ChrSetPos(0x0003, 74890, 0, 65620, 180)
    Sleep(500)

    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x02C4, 2, 0x1622))
    OP_71(0x0009, 0x0010)
    EventEnd(0x00)
    OP_4B(0x0015, 255)
    OP_4B(0x0017, 255)

    Return()

# id: 0x000F offset: 0x3968
@scena.Code('func_0F_3968')
def func_0F_3968():
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
        'loc_3989',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)

    def _loc_3989(): pass

    label('loc_3989')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_39A1'),
        (0x0000006A, 'loc_3A25'),
        (0x0000006B, 'loc_3AA9'),
        (0x0000006C, 'loc_3B2D'),
        (-1, 'loc_3BB1'),
    )

    def _loc_39A1(): pass

    label('loc_39A1')

    ChrSetPos(0x0101, 69080, 1250, 35450, 315)
    ChrSetPos(0x0107, 71080, 1250, 35550, 45)
    ChrSetPos(0x00F7, 69580, 1250, 33780, 225)
    ChrSetPos(0x00F9, 70630, 1250, 33820, 135)
    CameraMove(70020, 1250, 34440, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    Jump('loc_3BB1')

    def _loc_3A25(): pass

    label('loc_3A25')

    ChrSetPos(0x0101, 81200, 1250, 24440, 45)
    ChrSetPos(0x0107, 81200, 1250, 22600, 135)
    ChrSetPos(0x00F7, 79390, 1250, 24250, 225)
    ChrSetPos(0x00F9, 79200, 1250, 22670, 315)
    CameraMove(79940, 1250, 23610, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(303000, 0)
    OP_6E(262, 0)

    Jump('loc_3BB1')

    def _loc_3AA9(): pass

    label('loc_3AA9')

    ChrSetPos(0x0101, 71120, 1250, 10530, 135)
    ChrSetPos(0x0107, 69070, 1250, 10520, 225)
    ChrSetPos(0x00F7, 71070, 1250, 12090, 315)
    ChrSetPos(0x00F9, 69540, 1250, 12070, 45)
    CameraMove(70260, 1250, 11450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_3BB1')

    def _loc_3B2D(): pass

    label('loc_3B2D')

    ChrSetPos(0x0101, 59140, 1250, 22220, 225)
    ChrSetPos(0x0107, 59260, 1250, 24340, 315)
    ChrSetPos(0x00F7, 61220, 1250, 22110, 135)
    ChrSetPos(0x00F9, 61090, 1250, 23790, 45)
    CameraMove(59990, 1250, 23630, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)

    Jump('loc_3BB1')

    def _loc_3BB1(): pass

    label('loc_3BB1')

    ChrSetFlags(0x0016, 0x0080)
    OP_4A(0x0016, 255)
    ChrSetPos(0x0016, 62410, 250, 5400, 270)
    CreateThread(0x0101, 0x01, 0x00, func_10_3E33)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, func_13_4052)
    Sleep(300)

    CreateThread(0x00F7, 0x01, 0x00, func_12_3F9D)
    Sleep(100)

    CreateThread(0x0107, 0x01, 0x00, func_11_3EE8)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    ChrTurnDirection(0x0101, 0x00F7, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260615V#1007F嗯……\n',
            '跟丢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_3C53')
    def lambda_3C53():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3C53)

    Sleep(100)

    @scena.Lambda('lambda_3C66')
    def lambda_3C66():
        ChrTurnDirection(0x00FE, 0x00F9, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3C66)

    Sleep(100)

    @scena.Lambda('lambda_3C79')
    def lambda_3C79():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3C79)

    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3CBE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260616V#555F真是的，\n',
            '这么鬼灵精……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CEB')

    def _loc_3CBE(): pass

    label('loc_3CBE')

    ChrTalk(
        0x0103,
        (
            '#0030260617V#524F嗯，这孩子真像只小猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CEB(): pass

    label('loc_3CEB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D39',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260618V#070F你们昨天是一起\n',
            '逛过这间\n',
            '百货商店的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D7A')

    def _loc_3D39(): pass

    label('loc_3D39')

    ChrTalk(
        0x0105,
        (
            '#0060260619V#542F我记得她和\n',
            '提妲一起逛过\n',
            '这间百货商店的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D7A(): pass

    label('loc_3D7A')

    ChrTalk(
        0x0107,
        (
            '#0070260620V#063F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260621V#561F说不定是去了\n',
            '别的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260622V#1006F没关系，应该还\n',
            '没跑得太远吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260623V以东街区为中心搜索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C5, 6, 0x162E))
    OP_28(0x008C, 0x01, 0x0004)
    EventEnd(0x00)
    ChrClearFlags(0x0016, 0x0080)
    OP_4B(0x0016, 255)

    Return()

# id: 0x0010 offset: 0x3E33
@scena.Code('func_10_3E33')
def func_10_3E33():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_3E4B'),
        (0x0000006A, 'loc_3E72'),
        (0x0000006B, 'loc_3E99'),
        (0x0000006C, 'loc_3EC0'),
        (-1, 'loc_3EE7'),
    )

    def _loc_3E4B(): pass

    label('loc_3E4B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E6F',
    )

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    Jump('loc_3E4B')

    def _loc_3E6F(): pass

    label('loc_3E6F')

    Jump('loc_3EE7')

    def _loc_3E72(): pass

    label('loc_3E72')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E96',
    )

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    Jump('loc_3E72')

    def _loc_3E96(): pass

    label('loc_3E96')

    Jump('loc_3EE7')

    def _loc_3E99(): pass

    label('loc_3E99')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EBD',
    )

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    Jump('loc_3E99')

    def _loc_3EBD(): pass

    label('loc_3EBD')

    Jump('loc_3EE7')

    def _loc_3EC0(): pass

    label('loc_3EC0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3EE4',
    )

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    Jump('loc_3EC0')

    def _loc_3EE4(): pass

    label('loc_3EE4')

    Jump('loc_3EE7')

    def _loc_3EE7(): pass

    label('loc_3EE7')

    Return()

# id: 0x0011 offset: 0x3EE8
@scena.Code('func_11_3EE8')
def func_11_3EE8():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_3F00'),
        (0x0000006A, 'loc_3F27'),
        (0x0000006B, 'loc_3F4E'),
        (0x0000006C, 'loc_3F75'),
        (-1, 'loc_3F9C'),
    )

    def _loc_3F00(): pass

    label('loc_3F00')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F24',
    )

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    Jump('loc_3F00')

    def _loc_3F24(): pass

    label('loc_3F24')

    Jump('loc_3F9C')

    def _loc_3F27(): pass

    label('loc_3F27')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F4B',
    )

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    Jump('loc_3F27')

    def _loc_3F4B(): pass

    label('loc_3F4B')

    Jump('loc_3F9C')

    def _loc_3F4E(): pass

    label('loc_3F4E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F72',
    )

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    Jump('loc_3F4E')

    def _loc_3F72(): pass

    label('loc_3F72')

    Jump('loc_3F9C')

    def _loc_3F75(): pass

    label('loc_3F75')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F99',
    )

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    Jump('loc_3F75')

    def _loc_3F99(): pass

    label('loc_3F99')

    Jump('loc_3F9C')

    def _loc_3F9C(): pass

    label('loc_3F9C')

    Return()

# id: 0x0012 offset: 0x3F9D
@scena.Code('func_12_3F9D')
def func_12_3F9D():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_3FB5'),
        (0x0000006A, 'loc_3FDC'),
        (0x0000006B, 'loc_4003'),
        (0x0000006C, 'loc_402A'),
        (-1, 'loc_4051'),
    )

    def _loc_3FB5(): pass

    label('loc_3FB5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3FD9',
    )

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    Jump('loc_3FB5')

    def _loc_3FD9(): pass

    label('loc_3FD9')

    Jump('loc_4051')

    def _loc_3FDC(): pass

    label('loc_3FDC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4000',
    )

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    Jump('loc_3FDC')

    def _loc_4000(): pass

    label('loc_4000')

    Jump('loc_4051')

    def _loc_4003(): pass

    label('loc_4003')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4027',
    )

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    Jump('loc_4003')

    def _loc_4027(): pass

    label('loc_4027')

    Jump('loc_4051')

    def _loc_402A(): pass

    label('loc_402A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_404E',
    )

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    Jump('loc_402A')

    def _loc_404E(): pass

    label('loc_404E')

    Jump('loc_4051')

    def _loc_4051(): pass

    label('loc_4051')

    Return()

# id: 0x0013 offset: 0x4052
@scena.Code('func_13_4052')
def func_13_4052():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_406A'),
        (0x0000006A, 'loc_4091'),
        (0x0000006B, 'loc_40B8'),
        (0x0000006C, 'loc_40DF'),
        (-1, 'loc_4106'),
    )

    def _loc_406A(): pass

    label('loc_406A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_408E',
    )

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    Jump('loc_406A')

    def _loc_408E(): pass

    label('loc_408E')

    Jump('loc_4106')

    def _loc_4091(): pass

    label('loc_4091')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_40B5',
    )

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(2000)

    Jump('loc_4091')

    def _loc_40B5(): pass

    label('loc_40B5')

    Jump('loc_4106')

    def _loc_40B8(): pass

    label('loc_40B8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_40DC',
    )

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(2000)

    Jump('loc_40B8')

    def _loc_40DC(): pass

    label('loc_40DC')

    Jump('loc_4106')

    def _loc_40DF(): pass

    label('loc_40DF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4103',
    )

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(2000)

    Jump('loc_40DF')

    def _loc_4103(): pass

    label('loc_4103')

    Jump('loc_4106')

    def _loc_4106(): pass

    label('loc_4106')

    Return()

# id: 0x0014 offset: 0x4107
@scena.Code('func_14_4107')
def func_14_4107():
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
        'loc_411E',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)

    def _loc_411E(): pass

    label('loc_411E')

    ChrSetPos(0x0101, 45720, 250, 79960, 180)
    ChrSetPos(0x0107, 45460, 250, 81610, 360)
    ChrSetPos(0x00F7, 44130, 250, 80220, 180)
    ChrSetPos(0x00F9, 44120, 250, 81630, 360)
    CameraMove(43920, 500, 81110, 0)
    OP_67(0, 7630, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    CreateThread(0x0101, 0x01, 0x00, func_15_486F)
    Sleep(300)

    CreateThread(0x00F9, 0x01, 0x00, func_16_4894)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_15_486F)
    Sleep(300)

    CreateThread(0x0107, 0x01, 0x00, func_16_4894)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260648V#1007F#6P又、又不在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6F(0x0004, 0)
    OP_70(0x0004, 59)
    Sleep(1000)

    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 41000, 750, 81110, 90)
    ChrWalkTo(0x0024, 42920, 500, 81110, 2000, 0x00)

    ChrTalk(
        0x0024,
        (
            '#3200260649V#5P对、对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_4271')
    def lambda_4271():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4271)

    Sleep(50)

    @scena.Lambda('lambda_4284')
    def lambda_4284():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4284)

    Sleep(50)

    @scena.Lambda('lambda_4297')
    def lambda_4297():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_4297)

    Sleep(50)

    @scena.Lambda('lambda_42AA')
    def lambda_42AA():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_42AA)

    Sleep(300)

    ChrTalk(
        0x0024,
        (
            '#3200260650V#5P我虽然想留住\n',
            '她的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260651V#1016F#6P不，没事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260652V#1015F倒是你有没有\n',
            '跟她交谈过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#3200260653V#5P嗯，嗯……\n',
            '她跟我说的话很不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#3200260654V#5P她说『你知道哪儿有\n',
            '没有颜色的鱼吗？』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260655V#6P#1004F咦……？',
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
        'loc_4537',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260656V#074F呼，这话真有深意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080260657V说不定是\n',
            '解谜的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_442C')
    def lambda_442C():
        ChrSetDirection(0x0107, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_442C)

    @scena.Lambda('lambda_443A')
    def lambda_443A():
        ChrSetDirection(0x00F7, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_443A)

    ChrSetDirection(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260658V#1020F#6P解、解谜！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0108, 135, 400)

    ChrTalk(
        0x0108,
        (
            '#0080260659V#070F#5P就是说她让我们\n',
            '通过解谜来找到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260660V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260661V那么她刚才也是\n',
            '故意逃避我们的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080260662V#071F#5P嗯，应该是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46A3')

    def _loc_4537(): pass

    label('loc_4537')

    ChrTalk(
        0x0105,
        (
            '#0060260663V#047F这话真有深意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060260664V也许这是\n',
            '解谜的线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4587')
    def lambda_4587():
        ChrSetDirection(0x0107, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4587)

    @scena.Lambda('lambda_4595')
    def lambda_4595():
        ChrSetDirection(0x00F7, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_4595)

    ChrSetDirection(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260658V#1020F#6P解、解谜！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 135, 400)

    ChrTalk(
        0x0105,
        (
            '#0060260666V#542F#5P就是说她有可能\n',
            '是希望我们通过\n',
            '解谜来找到她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260660V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260661V那么她刚才也是\n',
            '故意逃避我们的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060260669V#045F#5P唔……\n',
            '应该是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46A3(): pass

    label('loc_46A3')

    ChrTalk(
        0x0101,
        (
            '#0010260670V#1019F#6P好、好一个玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260671V既然她要玩这手，\n',
            '我们也不会输！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 90, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4743',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260672V#551F#5P我说啊……\n',
            '现在问题不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_477A')

    def _loc_4743(): pass

    label('loc_4743')

    ChrTalk(
        0x0103,
        (
            '#0030260673V#025F#5P我说啊……\n',
            '现在问题不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_477A(): pass

    label('loc_477A')

    ChrSetDirection(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070260674V#067F#2P总、总之……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260675V线索就是『你知道哪儿有\n',
            '没有颜色的鱼吗？』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260676V#1006F#6P嗯，在这个提示的基础上\n',
            '我们要追查到那孩子去了哪儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#3200260677V#5P加、加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0024, 0x01, 0x00, func_17_48B9)
    SetScenaFlags(ScenaFlag(0x02C6, 1, 0x1631))
    OP_28(0x008C, 0x01, 0x0010)
    OP_28(0x008C, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x486F
@scena.Code('func_15_486F')
def func_15_486F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4893',
    )

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(2000)

    Jump('func_15_486F')

    def _loc_4893(): pass

    label('loc_4893')

    Return()

# id: 0x0016 offset: 0x4894
@scena.Code('func_16_4894')
def func_16_4894():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_48B8',
    )

    ChrSetDirection(0x00FE, 360, 400)
    Sleep(2000)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(2000)

    Jump('func_16_4894')

    def _loc_48B8(): pass

    label('loc_48B8')

    Return()

# id: 0x0017 offset: 0x48B9
@scena.Code('func_17_48B9')
def func_17_48B9():
    ChrSetDirection(0x0024, 270, 400)
    ChrWalkTo(0x0024, 41000, 750, 81110, 2000, 0x00)
    ChrSetFlags(0x0024, 0x0080)
    OP_72(0x0004, 0x0800)
    OP_6F(0x0004, 59)
    OP_70(0x0004, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_71(0x0004, 0x0800)

    Return()

# id: 0x0018 offset: 0x48FA
@scena.Code('func_18_48FA')
def func_18_48FA():
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
        'loc_491A',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)
    FadeIn(0, 0)

    def _loc_491A(): pass

    label('loc_491A')

    Fade(1000)
    ChrSetPos(0x0107, 38700, 1250, 50460, 270)
    ChrSetPos(0x0101, 38820, 1250, 49280, 270)
    ChrSetPos(0x00F7, 38450, 1250, 48150, 315)
    ChrSetPos(0x00F9, 40210, 1250, 49430, 270)
    CameraMove(37890, 1250, 50340, 0)
    OP_67(0, 10000, -10000, 0)
    OP_67(0, 7130, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x0011, 90, 0)
    ChrSetSubChip(0x0011, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260710V#1006F『没人管就会消失的点心』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260714V原来是这个啊。',
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
        'loc_4A5D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260715V#070F嗯，确实，没人管的话\n',
            '就会化掉并消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A97')

    def _loc_4A5D(): pass

    label('loc_4A5D')

    ChrTalk(
        0x0105,
        (
            '#0060260716V#542F确实，没人管的话\n',
            '就会化掉并消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A97(): pass

    label('loc_4A97')

    ChrTalk(
        0x0011,
        (
            '#3210260717V#5P哎呀，这不是昨天的小妹妹么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3210260718V#5P刚才你的朋友\n',
            '还来买了冰淇淋哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3210260719V#5P今天你们没在一起啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260720V#067F果然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260721V#560F请问，那孩子\n',
            '有说什么神秘兮兮的话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3210260722V#5P神秘兮兮？\n',
            '让我想想',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3210260723V#5P她倒是乐呵呵地说\n',
            '『我和姐姐她们\n',
            '约好在空港见面的』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260724V#1015F姐姐她们就是\n',
            '在说我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260725V#1007F呼～谜题终于结束了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)
    Sleep(300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4C96',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260726V#051F不过还真是被她\n',
            '牵着鼻子走了一圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CD0')

    def _loc_4C96(): pass

    label('loc_4C96')

    ChrTalk(
        0x0103,
        (
            '#0030260727V#021F呵呵，还真是被她\n',
            '牵着鼻子走了一圈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CD0(): pass

    label('loc_4CD0')

    ChrTalk(
        0x0101,
        (
            '#0010260728V#1019F真是的……\n',
            '害我这么担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260729V找到她以后\n',
            '要好好地说教一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070260730V#065F#2P姐、姐姐。\n',
            '请不要对她发太大的脾气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260731V#063F小玲一定是因为\n',
            '很寂寞才这样做的吧',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260732V我们老是在说\n',
            '工作的事……',
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
        'loc_4E04',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260733V#070F嗯……\n',
            '也有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E30')

    def _loc_4E04(): pass

    label('loc_4E04')

    ChrTalk(
        0x0105,
        (
            '#0060260734V#045F嗯……\n',
            '有可能是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E30(): pass

    label('loc_4E30')

    ChrTalk(
        0x0101,
        (
            '#0010260735V#1007F唔……我无可辩驳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260736V#1006F好了，总之我们\n',
            '先去空港接她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C6, 4, 0x1634))
    OP_28(0x008C, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x4E99
@scena.Code('func_19_4E99')
def func_19_4E99():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 4, 0x1634)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4EA6',
    )

    Return()

    def _loc_4EA6(): pass

    label('loc_4EA6')

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
        'loc_4EC6',
    )

    Call(0, 0x0020)
    Call(0, 0x0021)
    FadeIn(0, 0)

    def _loc_4EC6(): pass

    label('loc_4EC6')

    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0026, 0x0001)
    ChrClearFlags(0x0027, 0x0080)
    ChrSetFlags(0x0027, 0x0008)
    ChrSetFlags(0x0027, 0x0040)
    ChrSetPos(0x0025, 50460, 0, 85300, 180)
    ChrSetPos(0x0027, 50900, 100, 87500, 180)
    OP_A1(0x0027, 0x0011)
    OP_72(0x0011, 0x0004)
    OP_71(0x0011, 0x0040)
    OP_71(0x0011, 0x0020)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 50)
    Yield()
    ChrSetBattleFlags(0x0026, 0x0020)
    OP_89(0x0026, 50900, 350, 87200, 270)
    Fade(1000)
    ChrSetPos(0x0101, 47230, 250, 72940, 0)
    ChrSetPos(0x0107, 46120, 250, 72830, 0)
    ChrSetPos(0x00F7, 47390, 250, 71550, 0)
    ChrSetPos(0x00F9, 46230, 250, 71360, 0)
    CameraMove(47050, 250, 72580, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260737V#1004F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4FEF')
    def lambda_4FEF():
        CameraMove(49820, 0, 82670, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4FEF)

    @scena.Lambda('lambda_5007')
    def lambda_5007():
        OP_67(0, 8200, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5007)

    @scena.Lambda('lambda_501F')
    def lambda_501F():
        CameraSetDistance(1960, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_501F)

    @scena.Lambda('lambda_502F')
    def lambda_502F():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_502F)

    @scena.Lambda('lambda_503F')
    def lambda_503F():
        OP_6E(419, 3000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_503F)

    Sleep(1000)

    @scena.Lambda('lambda_5054')
    def lambda_5054():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_5054)

    Sleep(300)

    @scena.Lambda('lambda_5074')
    def lambda_5074():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_5074)

    PlaySE(207, 0x01, 0x64)
    CreateThread(0x0027, 0x02, 0x00, func_1E_62AE)
    WaitForThreadExit(0x0027, 0x0001)
    OP_72(0x0011, 0x0020)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 50)
    OP_24(0x00CF, 0x50)
    WaitForThreadExit(0x0107, 0x0002)

    ChrTalk(
        0x0025,
        (
            '#0560260738V#692F#5P哟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_50DA')
    def lambda_50DA():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_50DA')

    DispatchAsync2(0x0025, 0x0002, lambda_50DA)

    CreateThread(0x0101, 0x00, 0x00, func_1A_623E)
    Sleep(300)

    CreateThread(0x0107, 0x00, 0x00, func_1B_625A)
    CreateThread(0x00F7, 0x00, 0x00, func_1C_6276)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_1D_6292)
    WaitForThreadExit(0x00F9, 0x0000)
    TerminateThread(0x0025, 0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51CA',
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
        0,
        (
            TXT(0x00, '【◇在第２章见到了格斯塔夫维修长】\n'),
            TXT(0x01, '【◇没在第２章见到格斯塔夫维修长】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_51BE'),
        (0x00000001, 'loc_51C4'),
        (-1, 'loc_51CA'),
    )

    def _loc_51BE(): pass

    label('loc_51BE')

    SetScenaFlags(ScenaFlag(0x0290, 3, 0x1483))

    Jump('loc_51CA')

    def _loc_51C4(): pass

    label('loc_51C4')

    ClearScenaFlags(ScenaFlag(0x0290, 3, 0x1483))

    Jump('loc_51CA')

    def _loc_51CA(): pass

    label('loc_51CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 3, 0x1483)),
            Expr.Return,
        ),
        'loc_533A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070260739V#064F维修长先生，还有菲小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#1980260740V#5P咦，这不是提妲么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#0560260741V#693F#2P你好啊，小提妲！\n',
            '艾丝蒂尔你们都在啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_52D2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010260742V#1001F你好～维修长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260743V#051F怎么了？\n',
            '难得能在这里见到你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5337')

    def _loc_52D2(): pass

    label('loc_52D2')

    ChrTalk(
        0x0101,
        (
            '#0010260744V#1001F你好～维修长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260745V#1006F不过这是怎么了？\n',
            '难得能在这里见到你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5337(): pass

    label('loc_5337')

    Jump('loc_5468')

    def _loc_533A(): pass

    label('loc_533A')

    ChrTalk(
        0x0107,
        (
            '#0070260739V#064F维修长先生，还有菲小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#1980260740V#5P咦，这不是提妲么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#0560260748V#693F#2P你好啊，小提妲！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260749V#691F还有……\n',
            '好久不见了啊，艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260750V#1001F啊、嗯！\n',
            '维修长你们看起来也挺精神的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260745V#1006F不过这是怎么了？\n',
            '难得能在这里见到你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5468(): pass

    label('loc_5468')

    ChrTalk(
        0x0025,
        (
            '#0560260752V#691F#2P嘿嘿，我们是运送\n',
            '这个来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0025, 315, 400)

    @scena.Lambda('lambda_54AA')
    def lambda_54AA():
        CameraMove(49350, 250, 84910, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_54AA)

    Sleep(300)

    @scena.Lambda('lambda_54C7')
    def lambda_54C7():
        ChrWalkTo(0x00FE, 48880, 250, 86500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_54C7)

    Sleep(800)

    @scena.Lambda('lambda_54E7')
    def lambda_54E7():
        ChrWalkTo(0x00FE, 48810, 250, 85060, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_54E7)

    Sleep(200)

    @scena.Lambda('lambda_5507')
    def lambda_5507():
        ChrWalkTo(0x00FE, 48760, 250, 83460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5507)

    Sleep(200)

    @scena.Lambda('lambda_5527')
    def lambda_5527():
        ChrWalkTo(0x00FE, 48120, 250, 81710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5527)

    Sleep(500)

    WaitForThreadExit(0x0107, 0x0001)
    ChrSetDirection(0x0107, 45, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 45, 400)
    ChrSetSubChip(0x0026, 2)
    WaitForThreadExit(0x00F7, 0x0001)
    ChrSetDirection(0x00F7, 45, 400)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010260753V#1004F#6P哇～这是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260754V#064F#3P那个那个，莫非……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#0560260755V#691F#4P这就是埃尔赛尤的新引擎，\n',
            '『ＸＧ－０２』的样品？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260756V虽说是样品，不过\n',
            '性能几乎和实机一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260757V#1008F#6P哟～就是这个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260758V#560F#3P哇～真不敢相信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260759V设计得这么紧凑，竟然\n',
            '还能提供那么强劲的马力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260760V设计也兼备了功能性和可爱度……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260761V#067F啊～好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260762V#1016F#6P等等等等，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_57AB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260763V#551F#6P啊……\n',
            '又～进入忘我状态了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_57E3')

    def _loc_57AB(): pass

    label('loc_57AB')

    ChrTalk(
        0x0103,
        (
            '#0030260764V#021F#6P呵呵……看来她已经沉醉其中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_57E3(): pass

    label('loc_57E3')

    ChrSetDirection(0x00F9, 45, 400)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_586C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260765V#070F#6P不过，这既然是运来\n',
            '王都的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080260766V就代表它是要提供给\n',
            '共和国和帝国的样本？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58D2')

    def _loc_586C(): pass

    label('loc_586C')

    ChrTalk(
        0x0105,
        (
            '#0060260767V#040F#6P这既然是运来\n',
            '王都的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060260768V就代表它是要赠送给\n',
            '共和国和帝国的样本？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58D2(): pass

    label('loc_58D2')

    ChrSetDirection(0x0025, 225, 400)

    ChrTalk(
        0x0025,
        (
            '#0560260769V#691F#2P哟，你知道的还真不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260770V在埃尔赛尤上装配的\n',
            '作业终于完成了，\n',
            '所以就送来这边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    ChrSetDirection(0x00F7, 135, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BC9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060260771V#048F#6P是吗……\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#0560260772V#692F#2P啊、啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260773V请问，小姐你是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060260774V#047F#6P抱歉，这么晚才做自我介绍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060260775V#040F我是\n',
            '科洛蒂娅·冯·奥赛雷丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#0560260776V#692F#2P奥赛雷丝……\n',
            '难道是王室的……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260777V#1006F#5P嗯，她是女王陛下的孙女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060260778V#048F#6P埃尔赛尤应该算是\n',
            '王室所有的船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060260779V所以我要代替陛下\n',
            '向你们表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0025, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0025,
        (
            '#0560260780V#692F#2P不、不胜荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260781V#1016F#5P哈哈，突然听到这些\n',
            '你们会相当吃惊吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260782V#1006F话说回来，这引擎\n',
            '要送去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C1D')

    def _loc_5BC9(): pass

    label('loc_5BC9')

    ChrTalk(
        0x0101,
        (
            '#0010260783V#1006F#5P是吗，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260784V话说回来，这引擎\n',
            '要送去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C1D(): pass

    label('loc_5C1D')

    ChrTurnDirection(0x0025, 0x0101, 400)

    ChrTalk(
        0x0025,
        (
            '#0560260785V#691F#4P哦，要送往港口的仓库街。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260786V听说要由那边保管到\n',
            '条约的签字仪式进行的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260787V#1011F#5P哦？这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 135, 400)

    ChrTalk(
        0x0107,
        (
            '#0070260788V#560F#1P请问，维修长你们\n',
            '什么时候回蔡斯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#0560260789V#691F#4P嗯，运送完这东西\n',
            '就立刻出发。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260790V小提妲。\n',
            '要乖乖的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260791V#061F#1P啊，嗯。\n',
            '维修长你们也要保重！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5E41',
    )

    ChrTalk(
        0x0025,
        (
            '#0560260792V#691F#4P艾丝蒂尔……\n',
            '还有那个叫阿加特的，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560260793V小提妲就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260794V#1006F#5P嗯，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260795V#051F#5P好了，别担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EA1')

    def _loc_5E41(): pass

    label('loc_5E41')

    ChrTalk(
        0x0025,
        (
            '#0560260796V#691F#4P艾丝蒂尔。\n',
            '小提妲就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260794V#1006F#5P嗯，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EA1(): pass

    label('loc_5EA1')

    ChrTalk(
        0x0026,
        (
            '#1980260798V#2P再见，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    CameraMove(50680, 250, 83000, 0)
    OP_67(0, 9530, -10000, 0)
    CameraSetDistance(1780, 0)
    OP_6C(315000, 0)
    OP_6E(419, 0)
    OP_0D()
    OP_24(0x00CF, 0x64)

    @scena.Lambda('lambda_5F15')
    def lambda_5F15():
        ChrTurnDirection(0x00FE, 0x0025, 0)
        Yield()

        Jump('lambda_5F15')

    DispatchAsync2(0x0101, 0x0001, lambda_5F15)

    @scena.Lambda('lambda_5F26')
    def lambda_5F26():
        ChrTurnDirection(0x00FE, 0x0025, 0)
        Yield()

        Jump('lambda_5F26')

    DispatchAsync2(0x0107, 0x0001, lambda_5F26)

    @scena.Lambda('lambda_5F37')
    def lambda_5F37():
        ChrTurnDirection(0x00FE, 0x0025, 0)
        Yield()

        Jump('lambda_5F37')

    DispatchAsync2(0x00F7, 0x0001, lambda_5F37)

    @scena.Lambda('lambda_5F48')
    def lambda_5F48():
        ChrTurnDirection(0x00FE, 0x0025, 0)
        Yield()

        Jump('lambda_5F48')

    DispatchAsync2(0x00F9, 0x0001, lambda_5F48)

    ChrSetSubChip(0x0026, 0)

    @scena.Lambda('lambda_5F5E')
    def lambda_5F5E():
        ChrMoveToRelative(0x00FE, 0, 0, -20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_5F5E)

    Sleep(300)

    @scena.Lambda('lambda_5F7E')
    def lambda_5F7E():
        CameraMove(50680, 250, 79000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5F7E)

    @scena.Lambda('lambda_5F96')
    def lambda_5F96():
        ChrMoveToRelative(0x00FE, 0, 0, -20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_5F96)

    CreateThread(0x0027, 0x02, 0x00, func_1F_62F2)
    WaitForThreadExit(0x0027, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    OP_71(0x0011, 0x0004)
    CameraMove(48760, 250, 84990, 2000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260799V#1008F#5P啊～那就是\n',
            '埃尔赛尤用的引擎吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260800V虽然不太明白，\n',
            '不过看上去是很厉害的机器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260801V#560F嗯……\n',
            '真让人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260802V#061F我好想将来也能造出\n',
            '那么了不起的机器来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6169',
    )

    ChrSetDirection(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050260803V#551F#6P真拿你没办法……\n',
            '你在机械方面真是一根筋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260804V#051F不过有目标也是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260805V#067F嘿嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6197')

    def _loc_6169(): pass

    label('loc_6169')

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260806V#1017F#6P呵呵，也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6197(): pass

    label('loc_6197')

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(48450, 250, 85560, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 48450, 250, 85560, 180)
    ChrSetPos(0x0001, 48450, 250, 85560, 180)
    ChrSetPos(0x0002, 48450, 250, 85560, 180)
    ChrSetPos(0x0003, 48450, 250, 85560, 180)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x02C6, 5, 0x1635))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0x623E
@scena.Code('func_1A_623E')
def func_1A_623E():
    ChrWalkTo(0x00FE, 48360, 250, 81590, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x001B offset: 0x625A
@scena.Code('func_1B_625A')
def func_1B_625A():
    ChrWalkTo(0x00FE, 47380, 250, 80900, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x001C offset: 0x6276
@scena.Code('func_1C_6276')
def func_1C_6276():
    ChrWalkTo(0x00FE, 48630, 250, 80290, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x001D offset: 0x6292
@scena.Code('func_1D_6292')
def func_1D_6292():
    ChrWalkTo(0x00FE, 47650, 250, 79480, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x001E offset: 0x62AE
@scena.Code('func_1E_62AE')
def func_1E_62AE():
    OP_24(0x00CF, 0x41)
    Sleep(100)

    OP_24(0x00CF, 0x46)
    Sleep(100)

    OP_24(0x00CF, 0x4B)
    Sleep(100)

    OP_24(0x00CF, 0x50)
    Sleep(100)

    OP_24(0x00CF, 0x55)
    Sleep(100)

    OP_24(0x00CF, 0x5A)
    Sleep(100)

    OP_24(0x00CF, 0x5F)
    Sleep(100)

    OP_24(0x00CF, 0x64)

    Return()

# id: 0x001F offset: 0x62F2
@scena.Code('func_1F_62F2')
def func_1F_62F2():
    Sleep(6500)

    OP_24(0x00CF, 0x5F)
    Sleep(500)

    OP_24(0x00CF, 0x5A)
    Sleep(500)

    OP_24(0x00CF, 0x55)
    Sleep(500)

    OP_24(0x00CF, 0x50)
    Sleep(500)

    OP_24(0x00CF, 0x4B)
    Sleep(500)

    OP_24(0x00CF, 0x46)
    Sleep(500)

    OP_24(0x00CF, 0x41)
    Sleep(500)

    OP_23(0x00CF)

    Return()

# id: 0x0020 offset: 0x633A
@scena.Code('func_20_633A')
def func_20_633A():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_63B7'),
        (0x00000001, 'loc_63BD'),
        (-1, 'loc_63C3'),
    )

    def _loc_63B7(): pass

    label('loc_63B7')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_63C3')

    def _loc_63BD(): pass

    label('loc_63BD')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_63C3')

    def _loc_63C3(): pass

    label('loc_63C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_63D1',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_63D5')

    def _loc_63D1(): pass

    label('loc_63D1')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_63D5(): pass

    label('loc_63D5')

    Return()

# id: 0x0021 offset: 0x63D6
@scena.Code('func_21_63D6')
def func_21_63D6():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    CameraMove(22110, 0, 124540, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_6426',
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

    Jump('loc_6440')

    def _loc_6426(): pass

    label('loc_6426')

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

    def _loc_6440(): pass

    label('loc_6440')

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

# id: 0x0022 offset: 0x6460
@scena.Code('func_22_6460')
def func_22_6460():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力式时钟２号机\n',
            '　七耀历１１６３年·由蔡斯技术工房制造',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0023 offset: 0x64C2
@scena.Code('func_23_64C2')
def func_23_64C2():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0024 offset: 0x6508
@scena.Code('func_24_6508')
def func_24_6508():
    OP_13(0x00BA)

    Return()

# id: 0x0025 offset: 0x650C
@scena.Code('func_25_650C')
def func_25_650C():
    OP_13(0x00B1)

    Return()

# id: 0x0026 offset: 0x6510
@scena.Code('func_26_6510')
def func_26_6510():
    OP_13(0x00BB)

    Return()

# id: 0x0027 offset: 0x6514
@scena.Code('func_27_6514')
def func_27_6514():
    OP_13(0x00BC)

    Return()

# id: 0x0028 offset: 0x6518
@scena.Code('func_28_6518')
def func_28_6518():
    OP_13(0x00BD)

    Return()

# id: 0x0029 offset: 0x651C
@scena.Code('func_29_651C')
def func_29_651C():
    TalkBegin(0x00FF)
    Sleep(500)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
