import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1103   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1103.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1103_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT07/CH02380._CH', 'ED6_DT07/CH02380P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT26/CH20363._CH', 'ED6_DT26/CH20363P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT26/CH20243._CH', 'ED6_DT26/CH20243P._CP'),
        ('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP'),
    ]

# id: 0x10001 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '剑帝莱维',
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
            name                = '卢格兰老人',
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
            name                = '泊尔',
            x                   = 63800,
            z                   = 0,
            y                   = 43560,
            direction           = 321,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '市民',
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 49430,
            z                   = 0,
            y                   = 47820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古代龙',
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
            name                = '龙',
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
            name                = '卡洛',
            x                   = 29530,
            z                   = 0,
            y                   = 76910,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '刚茨',
            x                   = 37770,
            z                   = 0,
            y                   = 73470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '龙谷',
            x                   = 44080,
            z                   = 0,
            y                   = 76420,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '阿尔丹',
            x                   = 48620,
            z                   = 0,
            y                   = 81230,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '博尔德',
            x                   = 42290,
            z                   = 0,
            y                   = 44430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '特里诺',
            x                   = 44100,
            z                   = 0,
            y                   = 42920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '巴克',
            x                   = 61700,
            z                   = 0,
            y                   = 53800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '丽露露',
            x                   = 66890,
            z                   = 0,
            y                   = 49260,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '格蕾娅',
            x                   = 46080,
            z                   = 0,
            y                   = 42060,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '科尔娜',
            x                   = 68260,
            z                   = 0,
            y                   = 52310,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '雅哈多老人',
            x                   = 63060,
            z                   = 0,
            y                   = 49000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '雷塔',
            x                   = 41990,
            z                   = 0,
            y                   = 46350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '法娜',
            x                   = 37580,
            z                   = 0,
            y                   = 47610,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 46060,
            z                   = 0,
            y                   = 77320,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 72340,
            z                   = 0,
            y                   = 63740,
            direction           = 175,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 22580,
            z                   = 0,
            y                   = 48730,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 45370,
            z                   = 0,
            y                   = 78340,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '哈里',
            x                   = 30140,
            z                   = 0,
            y                   = 73750,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '米娜',
            x                   = 30140,
            z                   = 0,
            y                   = 72630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '奥维德',
            x                   = 49430,
            z                   = 0,
            y                   = 47820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '木匠',
            x                   = 44780,
            z                   = 4600,
            y                   = 51050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '木匠',
            x                   = 53490,
            z                   = 6420,
            y                   = 59900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '木匠',
            x                   = 56870,
            z                   = 4600,
            y                   = 53430,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '木匠',
            x                   = 41670,
            z                   = 4600,
            y                   = 68230,
            direction           = 314,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '木匠',
            x                   = 55760,
            z                   = 4600,
            y                   = 62760,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '青年管家',
            x                   = 66030,
            z                   = 0,
            y                   = 70470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '玛依森老人',
            x                   = 29410,
            z                   = 0,
            y                   = 56670,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '西柏斯街道方向',
            x                   = 4530,
            z                   = 0,
            y                   = 45190,
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
            name                = '东柏斯街道方向',
            x                   = 87650,
            z                   = 0,
            y                   = 60410,
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
            name                = '柏斯市·南街区',
            x                   = 47990,
            z                   = -3000,
            y                   = 29310,
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
            name                = '柏斯国际空港',
            x                   = 47940,
            z                   = 0,
            y                   = 93220,
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

# id: 0x10002 offset: 0x8E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x8E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 75900,
            y           = -1000,
            z           = 53900,
            range       = 76600,
            dword_10    = 0x000007D0,
            dword_14    = 0x00010554,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000033,
        ),
        ScenaEventData(
            x           = 17000,
            y           = -1000,
            z           = 50100,
            range       = 18000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00009D6C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000034,
        ),
        ScenaEventData(
            x           = 25200,
            y           = 0,
            z           = 57940,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000043,
        ),
        ScenaEventData(
            x           = 18880,
            y           = 0,
            z           = 76030,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000044,
        ),
        ScenaEventData(
            x           = 36200,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000045,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000046,
        ),
        ScenaEventData(
            x           = 38540,
            y           = 0,
            z           = 59990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000047,
        ),
        ScenaEventData(
            x           = 48040,
            y           = 100,
            z           = 69500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000047,
        ),
        ScenaEventData(
            x           = 57480,
            y           = 0,
            z           = 60010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000047,
        ),
        ScenaEventData(
            x           = 48010,
            y           = 0,
            z           = 50550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000047,
        ),
        ScenaEventData(
            x           = 67340,
            y           = -500,
            z           = 73070,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000048,
        ),
        ScenaEventData(
            x           = 72240,
            y           = 0,
            z           = 44910,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000049,
        ),
        ScenaEventData(
            x           = 47960,
            y           = 0,
            z           = 85570,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004A,
        ),
    )

# id: 0x10004 offset: 0xA82
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA82
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_AD4',
    )

    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0023, 40190, 0, 71770, 270)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003C, 0x0080)

    Jump('loc_C75')

    def _loc_AD4(): pass

    label('loc_AD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_B84',
    )

    ChrSetPos(0x001B, 47960, 0, 76090, 180)
    ChrSetPos(0x0025, 65480, 0, 69210, 225)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x0022, 29530, 0, 76910, 270)
    ChrSetPos(0x0033, 30140, 0, 73750, 135)
    ChrSetPos(0x0034, 30140, 0, 72630, 135)
    ChrSetPos(0x0024, 30060, 0, 66160, 90)
    ChrSetPos(0x002C, 65269, 0, 59980, 275)
    CreateThread(0x002C, 0x00, 0x06, func_02_DDB)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)

    Jump('loc_C75')

    def _loc_B84(): pass

    label('loc_B84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Return,
        ),
        'loc_BFA',
    )

    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x0022, 29530, 0, 76910, 270)
    ChrSetPos(0x0033, 30140, 0, 73750, 135)
    ChrSetPos(0x0034, 30140, 0, 72630, 135)
    ChrSetPos(0x0024, 30060, 0, 66160, 90)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)

    Jump('loc_C75')

    def _loc_BFA(): pass

    label('loc_BFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_C75',
    )

    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x002A, 0x0080)
    ChrSetFlags(0x002B, 0x0080)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetPos(0x002D, 66520, 0, 53320, 283)
    CreateThread(0x002D, 0x00, 0x06, func_02_DDB)
    ChrSetPos(0x002E, 67200, 0, 51980, 270)
    ChrSetFlags(0x002F, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    OP_4A(0x0036, 255)
    OP_4A(0x0037, 255)
    OP_4A(0x0038, 255)
    OP_4A(0x0039, 255)
    OP_4A(0x003A, 255)

    def _loc_C75(): pass

    label('loc_C75')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_C85',
    )

    ChrSetFlags(0x0035, 0x0080)

    def _loc_C85(): pass

    label('loc_C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_C9B',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_39_644C)

    Jump('loc_CEE')

    def _loc_C9B(): pass

    label('loc_C9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_CBA',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_3E_67FA)

    Jump('loc_CEE')

    def _loc_CBA(): pass

    label('loc_CBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_CD9',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_23_4F64)

    Jump('loc_CEE')

    def _loc_CD9(): pass

    label('loc_CD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CEE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_1F_39F6)

    def _loc_CEE(): pass

    label('loc_CEE')

    Return()

# id: 0x0001 offset: 0xCEF
@scena.Code('func_01_CEF')
def func_01_CEF():
    OP_16(0x02, 4000, -80000, -68000, 2293825)
    OP_72(0x0013, 0x0020)
    OP_72(0x0013, 0x0008)
    OP_71(0x0012, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Return,
        ),
        'loc_D1F',
    )

    OP_71(0x001F, 0x0004)

    Jump('loc_D68')

    def _loc_D1F(): pass

    label('loc_D1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D68',
    )

    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_71(0x0016, 0x0004)
    OP_71(0x0017, 0x0004)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x0020, 0x0004)

    def _loc_D68(): pass

    label('loc_D68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D83',
    )

    OP_72(0x0021, 0x0004)
    OP_72(0x0022, 0x0004)
    OP_72(0x0023, 0x0004)

    def _loc_D83(): pass

    label('loc_D83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Return,
        ),
        'loc_D8D',
    )

    Jump('loc_D9E')

    def _loc_D8D(): pass

    label('loc_D8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_D9E',
    )

    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)

    def _loc_D9E(): pass

    label('loc_D9E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DDA',
    )

    OP_72(0x000A, 0x0010)
    OP_72(0x000B, 0x0010)
    OP_72(0x000C, 0x0010)
    OP_72(0x000D, 0x0010)
    OP_6F(0x000A, 59)
    OP_6F(0x000B, 59)
    OP_6F(0x000C, 59)
    OP_6F(0x000D, 59)

    def _loc_DDA(): pass

    label('loc_DDA')

    Return()

# id: 0x0002 offset: 0xDDB
@scena.Code('func_02_DDB')
def func_02_DDB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EF7',
    )

    ChrWalkTo(0x00FE, 63060, 0, 72180, 2000, 0x00)
    ChrWalkTo(0x00FE, 62120, 0, 74260, 2000, 0x00)
    ChrWalkTo(0x00FE, 61300, 0, 74790, 2000, 0x00)
    ChrWalkTo(0x00FE, 35350, 0, 74790, 2000, 0x00)
    ChrWalkTo(0x00FE, 33690, 0, 73890, 2000, 0x00)
    ChrWalkTo(0x00FE, 32840, 0, 73270, 2000, 0x00)
    ChrWalkTo(0x00FE, 32840, 0, 60030, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 32840, 0, 48230, 2000, 0x00)
    ChrWalkTo(0x00FE, 33380, 0, 46100, 2000, 0x00)
    ChrWalkTo(0x00FE, 34280, 0, 45030, 2000, 0x00)
    ChrWalkTo(0x00FE, 60310, 0, 45030, 2000, 0x00)
    ChrWalkTo(0x00FE, 61730, 0, 45510, 2000, 0x00)
    ChrWalkTo(0x00FE, 63060, 0, 47220, 2000, 0x00)

    Jump('func_02_DDB')

    def _loc_EF7(): pass

    label('loc_EF7')

    Return()

# id: 0x0003 offset: 0xEF8
@scena.Code('func_03_EF8')
def func_03_EF8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F44',
    )

    ChrWalkTo(0x00FE, 61630, 0, 52250, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 61700, 0, 55270, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(3000)

    Jump('func_03_EF8')

    def _loc_F44(): pass

    label('loc_F44')

    Return()

# id: 0x0004 offset: 0xF45
@scena.Code('func_04_F45')
def func_04_F45():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F96',
    )

    Sleep(1500)

    ChrWalkTo(0x00FE, 42670, 0, 46350, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 41380, 0, 46350, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    Jump('func_04_F45')

    def _loc_F96(): pass

    label('loc_F96')

    Return()

# id: 0x0005 offset: 0xF97
@scena.Code('func_05_F97')
def func_05_F97():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1023',
    )

    ChrWalkTo(0x00FE, 39390, 4600, 57020, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 39640, 4600, 51120, 2000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 44850, 4600, 51120, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 39640, 4600, 51120, 2000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(3000)

    Jump('func_05_F97')

    def _loc_1023(): pass

    label('loc_1023')

    Return()

# id: 0x0006 offset: 0x1024
@scena.Code('func_06_1024')
def func_06_1024():
    TalkBegin(0x003C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1090',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '几天没见，\n',
            '工程有了很大的进展啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，在超市里\n',
            '边走边看古董真是一种乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1090(): pass

    label('loc_1090')

    TalkEnd(0x003C)

    Return()

# id: 0x0007 offset: 0x1094
@scena.Code('func_07_1094')
def func_07_1094():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_11C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1116',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军忙于消灭龙，\n',
            '城里的人们拼命为推进工程而努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，让我来认真努力地考虑一下\n',
            '今晚的菜单吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11BE')

    def _loc_1116(): pass

    label('loc_1116')

    ChrTalk(
        0x00FE,
        (
            '王国军忙于消灭龙，\n',
            '城里的人们拼命为推进工程而努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，让我来认真努力地考虑一下\n',
            '今晚的菜单吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是多无聊的工作，\n',
            '认真干的话其实都是很辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_11BE(): pass

    label('loc_11BE')

    Jump('loc_136C')

    def _loc_11C1(): pass

    label('loc_11C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_12A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_121B',
    )

    ChrTalk(
        0x00FE,
        (
            '超市的人们、\n',
            '好像正在宾馆里继续营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是对工作充满热情啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_129E')

    def _loc_121B(): pass

    label('loc_121B')

    ChrTalk(
        0x00FE,
        (
            '超市的人们、\n',
            '好像正在宾馆里继续营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们热心于工作真令人高兴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过托他们的福，\n',
            '我在料理制作上也不能偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_129E(): pass

    label('loc_129E')

    Jump('loc_136C')

    def _loc_12A1(): pass

    label('loc_12A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_136C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_12F8',
    )

    ChrTalk(
        0x00FE,
        (
            '没想超市\n',
            '居然会发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经没心情\n',
            '考虑什么菜单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136C')

    def _loc_12F8(): pass

    label('loc_12F8')

    ChrTalk(
        0x00FE,
        (
            '没想超市\n',
            '居然会发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经没心情\n',
            '考虑什么菜单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天只有面包和汤，\n',
            '如果有不满就别吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_136C(): pass

    label('loc_136C')

    TalkEnd(0x0022)

    Return()

# id: 0x0008 offset: 0x1370
@scena.Code('func_08_1370')
def func_08_1370():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1483',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_13D4',
    )

    ChrTalk(
        0x00FE,
        (
            '我也决定帮忙\n',
            '加入修复工程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望蛋糕铺的姐姐\n',
            '能早日回到过去待的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1480')

    def _loc_13D4(): pass

    label('loc_13D4')

    ChrTalk(
        0x00FE,
        (
            '我也决定帮忙\n',
            '加入修复工程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望蛋糕铺的姐姐\n',
            '能早日回到过去待的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果超市重新开始经营，\n',
            '未婚夫也会返回冰淇淋店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……没、没有什么别的用心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1480(): pass

    label('loc_1480')

    Jump('loc_1698')

    def _loc_1483(): pass

    label('loc_1483')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1599',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_14FA',
    )

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的姐姐\n',
            '是和未婚夫一起经营店铺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果超市重新开始经营，\n',
            '他们可能会分开工作一阵子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1596')

    def _loc_14FA(): pass

    label('loc_14FA')

    ChrTalk(
        0x00FE,
        (
            '呼，真想见见\n',
            '蛋糕店的姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她现在和未婚夫一起\n',
            '开店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果超市重新开始经营，\n',
            '他们可能会分开工作一阵子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我也去帮忙工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1596(): pass

    label('loc_1596')

    Jump('loc_1698')

    def _loc_1599(): pass

    label('loc_1599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1698',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1602',
    )

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的姐姐\n',
            '是和未婚夫一起经营店铺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说早知会有今天，\n',
            '但还是挺受打击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1698')

    def _loc_1602(): pass

    label('loc_1602')

    ChrTalk(
        0x00FE,
        (
            '我是听说了\n',
            '蛋糕店姐姐在酒馆避难才来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进去里面一看，姐姐她原来\n',
            '是和未婚夫一起经营店铺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说早知会有今天，\n',
            '但还是挺受打击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1698(): pass

    label('loc_1698')

    TalkEnd(0x0023)

    Return()

# id: 0x0009 offset: 0x169C
@scena.Code('func_09_169C')
def func_09_169C():
    TalkBegin(0x0024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1801',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1706',
    )

    ChrTalk(
        0x00FE,
        (
            '根据各地的传说，\n',
            '龙应该是理智而温和的生物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那又为何会\n',
            '来袭击果园呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17FE')

    def _loc_1706(): pass

    label('loc_1706')

    ChrTalk(
        0x00FE,
        (
            '外表特征看来\n',
            '倒确实是古代龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，情况好像有点奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传说中，龙被认为是\n',
            '理智而温厚的生物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然而，现实出现的龙\n',
            '却袭击了果园不是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然传说不是１００％的真实，\n',
            '但总会有一定的根据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相差这么远，\n',
            '不是很奇怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_17FE(): pass

    label('loc_17FE')

    Jump('loc_1949')

    def _loc_1801(): pass

    label('loc_1801')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1949',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_187A',
    )

    ChrTalk(
        0x00FE,
        (
            '那毫无疑问就是自太古时代就存在的\n',
            '幻之生物，古代龙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '镇、镇定～～\n',
            '首先从收集目击证言开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1949')

    def _loc_187A(): pass

    label('loc_187A')

    ChrTalk(
        0x00FE,
        (
            '刚、刚才那个看到了吗！？\n',
            '那毫无疑问就是古代龙啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从１２００年前的『大崩坏』以前开始\n',
            '就生存着的幻之生物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我主张其生存\n',
            '的学说果然是正确的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要、要赶快收集目击证言，\n',
            '画下草图才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1949(): pass

    label('loc_1949')

    TalkEnd(0x0024)

    Return()

# id: 0x000A offset: 0x194D
@scena.Code('func_0A_194D')
def func_0A_194D():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1A65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_19C5',
    )

    ChrTalk(
        0x00FE,
        (
            '我拍的龙的照片\n',
            '卖给利贝尔通讯社了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，下一期的利贝尔通讯…\n',
            '忍不住从现在就开始期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A62')

    def _loc_19C5(): pass

    label('loc_19C5')

    ChrTalk(
        0x00FE,
        (
            '那个怪物，看来\n',
            '似乎是古代龙这种生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说非常稀有，\n',
            '我的照片也被利贝尔通讯社\n',
            '买去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，下一期的利贝尔通讯…\n',
            '忍不住从现在就开始期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1A62(): pass

    label('loc_1A62')

    Jump('loc_1B79')

    def _loc_1A65(): pass

    label('loc_1A65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1B79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1AC6',
    )

    ChrTalk(
        0x00FE,
        (
            '我那时拍下了\n',
            '那头怪物的照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这个似乎\n',
            '是相当厉害的独家新闻吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B79')

    def _loc_1AC6(): pass

    label('loc_1AC6')

    ChrTalk(
        0x00FE,
        (
            '从、从飞船坪过来到这里，\n',
            '刚好碰上那个怪物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想、想都没想就用手中的照相机\n',
            '拍了一张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这个似乎\n',
            '是相当厉害的独家新闻吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定可以联系\n',
            '哪个杂志社卖掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1B79(): pass

    label('loc_1B79')

    TalkEnd(0x0025)

    Return()

# id: 0x000B offset: 0x1B7D
@scena.Code('func_0B_1B7D')
def func_0B_1B7D():
    TalkBegin(0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1C0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1BBE',
    )

    ChrTalk(
        0x00FE,
        (
            '超市在柏斯中心。\n',
            '要赶快研究对策才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C0A')

    def _loc_1BBE(): pass

    label('loc_1BBE')

    ChrTalk(
        0x00FE,
        (
            '究竟是什么事呢。\n',
            '超市竟然被袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……要赶快研究对策才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1C0A(): pass

    label('loc_1C0A')

    TalkEnd(0x0026)

    Return()

# id: 0x000C offset: 0x1C0E
@scena.Code('func_0C_1C0E')
def func_0C_1C0E():
    TalkBegin(0x0027)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1CA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1C6D',
    )

    ChrTalk(
        0x00FE,
        (
            '超市现在这个样子，\n',
            '柏斯的经济真是前途未卜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快想办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA3')

    def _loc_1C6D(): pass

    label('loc_1C6D')

    ChrTalk(
        0x00FE,
        (
            '怎、怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下简直\n',
            '像战争一样嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1CA3(): pass

    label('loc_1CA3')

    TalkEnd(0x0027)

    Return()

# id: 0x000D offset: 0x1CA7
@scena.Code('func_0D_1CA7')
def func_0D_1CA7():
    TalkBegin(0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1D79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1D08',
    )

    ChrTalk(
        0x00FE,
        (
            '工程进展很顺利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏大家齐心协力，\n',
            '看样子能比预想的更早恢复哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D76')

    def _loc_1D08(): pass

    label('loc_1D08')

    ChrTalk(
        0x00FE,
        (
            '工程进展很顺利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去似乎能比预想的\n',
            '更早重新开始营业哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这才是柏斯商人的实力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1D76(): pass

    label('loc_1D76')

    Jump('loc_1E40')

    def _loc_1D79(): pass

    label('loc_1D79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1E40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1DD2',
    )

    ChrTalk(
        0x00FE,
        (
            '超市的修复工程\n',
            '马上就开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然力量微薄，\n',
            '但我也来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E40')

    def _loc_1DD2(): pass

    label('loc_1DD2')

    ChrTalk(
        0x00FE,
        (
            '超市的修复工程\n',
            '马上就开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能一直给\n',
            '酒店的人添麻烦嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把店委托给同伴，\n',
            '我也来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1E40(): pass

    label('loc_1E40')

    TalkEnd(0x0028)

    Return()

# id: 0x000E offset: 0x1E44
@scena.Code('func_0E_1E44')
def func_0E_1E44():
    TalkBegin(0x0029)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1EBD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1E74',
    )

    ChrTalk(
        0x00FE,
        (
            '早点修好的话就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EBA')

    def _loc_1E74(): pass

    label('loc_1E74')

    ChrTalk(
        0x00FE,
        (
            '好不容易可以\n',
            '一个人来买东西了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早点修好的话就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_1EBA(): pass

    label('loc_1EBA')

    Jump('loc_1F50')

    def _loc_1EBD(): pass

    label('loc_1EBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1F50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1EF9',
    )

    ChrTalk(
        0x00FE,
        (
            '教区长说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙其实\n',
            '是很安分的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F50')

    def _loc_1EF9(): pass

    label('loc_1EF9')

    ChrTalk(
        0x00FE,
        (
            '教区长说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙其实\n',
            '是很安分的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，那为什么会\n',
            '做那么可怕的事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_1F50(): pass

    label('loc_1F50')

    TalkEnd(0x0029)

    Return()

# id: 0x000F offset: 0x1F54
@scena.Code('func_0F_1F54')
def func_0F_1F54():
    TalkBegin(0x002A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2033',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1FB2',
    )

    ChrTalk(
        0x00FE,
        (
            '各位市民\n',
            '都来帮工程的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此工程的进展\n',
            '似乎比预定中更快哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2030')

    def _loc_1FB2(): pass

    label('loc_1FB2')

    ChrTalk(
        0x00FE,
        (
            '各位市民\n',
            '都来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话我\n',
            '也想贡献自己的力量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但那样做的话只会拖后腿而已。\n',
            '这点我还是知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2030(): pass

    label('loc_2030')

    Jump('loc_2108')

    def _loc_2033(): pass

    label('loc_2033')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2108',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_208C',
    )

    ChrTalk(
        0x00FE,
        (
            '真令人惊讶。\n',
            '工程已经开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么时候\n',
            '准备得这么周全的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2108')

    def _loc_208C(): pass

    label('loc_208C')

    ChrTalk(
        0x00FE,
        (
            '早上开始就觉得很吵闹，\n',
            '于是过来看看情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真令人惊讶。\n',
            '工程已经开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么时候\n',
            '准备得这么周全的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_2108(): pass

    label('loc_2108')

    TalkEnd(0x002A)

    Return()

# id: 0x0010 offset: 0x210C
@scena.Code('func_10_210C')
def func_10_210C():
    TalkBegin(0x002B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2159',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，这样找\n',
            '竟然还没找到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那女孩\n',
            '真的在这城里吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_219B')

    def _loc_2159(): pass

    label('loc_2159')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_219B',
    )

    ChrTalk(
        0x00FE,
        (
            '去南街区之前\n',
            '再到这边找找……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，到底在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_219B(): pass

    label('loc_219B')

    TalkEnd(0x002B)

    Return()

# id: 0x0011 offset: 0x219F
@scena.Code('func_11_219F')
def func_11_219F():
    TalkBegin(0x002C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2263',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_21DE',
    )

    ChrTalk(
        0x00FE,
        (
            '现在城市的状况\n',
            '就像战争结束那时一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2260')

    def _loc_21DE(): pass

    label('loc_21DE')

    ChrTalk(
        0x00FE,
        (
            '唔，现在城市的样子\n',
            '就像战争结束那时一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候，为了修复\n',
            '在百日战役中荒废的城市，\n',
            '市民们也都是全体出动来帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_2260(): pass

    label('loc_2260')

    Jump('loc_2310')

    def _loc_2263(): pass

    label('loc_2263')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2310',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_22AD',
    )

    ChrTalk(
        0x00FE,
        (
            '工程好像已经开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '梅贝尔市长\n',
            '也很努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2310')

    def _loc_22AD(): pass

    label('loc_22AD')

    ChrTalk(
        0x00FE,
        (
            '唔，工程已经开始了啊。\n',
            '市长看来也在努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这方面的优秀能力\n',
            '可以说是继承自父亲的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_2310(): pass

    label('loc_2310')

    TalkEnd(0x002C)

    Return()

# id: 0x0012 offset: 0x2314
@scena.Code('func_12_2314')
def func_12_2314():
    TalkBegin(0x002D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_23E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_236F',
    )

    ChrTalk(
        0x00FE,
        (
            '梅贝尔市长来视察过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '百忙之中\n',
            '还一个人接一个人的鼓励大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DE')

    def _loc_236F(): pass

    label('loc_236F')

    ChrTalk(
        0x00FE,
        (
            '梅贝尔市长来视察过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '百忙之中\n',
            '还一个人接一个人的鼓励大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到她的样子\n',
            '突然就有了干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_23DE(): pass

    label('loc_23DE')

    Jump('loc_2522')

    def _loc_23E1(): pass

    label('loc_23E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_24A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_243A',
    )

    ChrTalk(
        0x00FE,
        (
            '和法娜一起\n',
            '在给工程帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然力量微薄，\n',
            '但也不能坐视不理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24A2')

    def _loc_243A(): pass

    label('loc_243A')

    ChrTalk(
        0x00FE,
        (
            '和法娜一起\n',
            '在给工程帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然力量微薄，\n',
            '但也不能坐视不理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，尽可能\n',
            '努力看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_24A2(): pass

    label('loc_24A2')

    Jump('loc_2522')

    def _loc_24A5(): pass

    label('loc_24A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2522',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_24D0',
    )

    ChrTalk(
        0x00FE,
        (
            '刚、刚才那个是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2522')

    def _loc_24D0(): pass

    label('loc_24D0')

    ChrTalk(
        0x00FE,
        (
            '刚、刚才那个是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那么大的魔兽，\n',
            '真是从来没见过也没听说过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_2522(): pass

    label('loc_2522')

    TalkEnd(0x002D)

    Return()

# id: 0x0013 offset: 0x2526
@scena.Code('func_13_2526')
def func_13_2526():
    TalkBegin(0x002E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_258A',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，市长小姐\n',
            '和我说话了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是为了得到赞扬\n',
            '才去做的，\n',
            '但还是很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2697')

    def _loc_258A(): pass

    label('loc_258A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_264C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_25D7',
    )

    ChrTalk(
        0x00FE,
        (
            '我们也来\n',
            '帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市封锁的话，\n',
            '也就不能打工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2649')

    def _loc_25D7(): pass

    label('loc_25D7')

    ChrTalk(
        0x00FE,
        (
            '我们也去帮忙\n',
            '加入修复工程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市封锁的话，\n',
            '也就不能打工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且有困难的时候\n',
            '就应该互相帮助嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_2649(): pass

    label('loc_2649')

    Jump('loc_2697')

    def _loc_264C(): pass

    label('loc_264C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2697',
    )

    ChrTalk(
        0x00FE,
        (
            '超，超市的顶棚\n',
            '给破坏得乱七八糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里面的人\n',
            '怎么样了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2697(): pass

    label('loc_2697')

    TalkEnd(0x002E)

    Return()

# id: 0x0014 offset: 0x269B
@scena.Code('func_14_269B')
def func_14_269B():
    TalkBegin(0x002F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2796',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_270F',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然遗憾，但是第一次\n',
            '捕获作战好像失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟能甩开舰队的追踪，\n',
            '真是不得了的飞行能力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2793')

    def _loc_270F(): pass

    label('loc_270F')

    ChrTalk(
        0x00FE,
        (
            '虽然遗憾，但是第一次\n',
            '捕获作战好像失败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来居然能\n',
            '甩开飞行舰队的追踪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能形容为\n',
            '超越人类智慧的力量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_2793(): pass

    label('loc_2793')

    Jump('loc_286A')

    def _loc_2796(): pass

    label('loc_2796')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_286A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_27F9',
    )

    ChrTalk(
        0x00FE,
        (
            '在古龙捕获作战成功之前，\n',
            '市街的警备由我们负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么问题\n',
            '就马上联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_286A')

    def _loc_27F9(): pass

    label('loc_27F9')

    ChrTalk(
        0x00FE,
        (
            '我们是国境师团的分遣队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在古龙捕获作战成功之前，\n',
            '负责柏斯市街的警备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么问题\n',
            '就马上联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    def _loc_286A(): pass

    label('loc_286A')

    TalkEnd(0x002F)

    Return()

# id: 0x0015 offset: 0x286E
@scena.Code('func_15_286E')
def func_15_286E():
    TalkBegin(0x0030)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_28D1',
    )

    ChrTalk(
        0x00FE,
        (
            '似乎连一般市民\n',
            '也参与修复工程了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个情况看来，\n',
            '超市很快就可以重开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29A4')

    def _loc_28D1(): pass

    label('loc_28D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_29A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_292C',
    )

    ChrTalk(
        0x00FE,
        (
            '面对那古代龙，\n',
            '我们可对抗不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能祈祷\n',
            '捕获作战能够成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29A4')

    def _loc_292C(): pass

    label('loc_292C')

    ChrTalk(
        0x00FE,
        (
            '我们的任务\n',
            '是让市民放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是警备，\n',
            '但对手可是那古代龙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再被袭击，\n',
            '我们的火力可无法对抗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    def _loc_29A4(): pass

    label('loc_29A4')

    TalkEnd(0x0030)

    Return()

# id: 0x0016 offset: 0x29A8
@scena.Code('func_16_29A8')
def func_16_29A8():
    TalkBegin(0x0031)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2A75',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_29FC',
    )

    ChrTalk(
        0x00FE,
        (
            '龙似乎逃进\n',
            '迷雾峡谷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道摩尔根将军\n',
            '有什么对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A72')

    def _loc_29FC(): pass

    label('loc_29FC')

    ChrTalk(
        0x00FE,
        (
            '龙似乎逃进\n',
            '迷雾峡谷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在山岳地带飞行本就危险，\n',
            '而且那里又起雾了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道摩尔根将军\n',
            '有什么对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    def _loc_2A72(): pass

    label('loc_2A72')

    Jump('loc_2B44')

    def _loc_2A75(): pass

    label('loc_2A75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2B44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_2AD0',
    )

    ChrTalk(
        0x00FE,
        (
            '拉文努村的\n',
            '果园似乎也遭殃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，果园……\n',
            '没理由袭击果园啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B44')

    def _loc_2AD0(): pass

    label('loc_2AD0')

    ChrTalk(
        0x00FE,
        (
            '拉文努村的\n',
            '果园似乎也遭殃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '派遣到那边的人\n',
            '说过情况非常严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，果园……\n',
            '没理由袭击果园啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    def _loc_2B44(): pass

    label('loc_2B44')

    TalkEnd(0x0031)

    Return()

# id: 0x0017 offset: 0x2B48
@scena.Code('func_17_2B48')
def func_17_2B48():
    TalkBegin(0x0032)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2C4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_2BA5',
    )

    ChrTalk(
        0x00FE,
        (
            '关于龙的捕获作战\n',
            '似乎帝国没有反对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是因为互不侵犯条约吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C49')

    def _loc_2BA5(): pass

    label('loc_2BA5')

    ChrTalk(
        0x00FE,
        (
            '本来还担心帝国方面\n',
            '会反对捕获作战……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过似乎并没反对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，柏斯地区\n',
            '可以说就在帝国隔壁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个有名的铁血宰相\n',
            '可不像是个会沉默的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    def _loc_2C49(): pass

    label('loc_2C49')

    Jump('loc_2D63')

    def _loc_2C4C(): pass

    label('loc_2C4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2D63',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_2CC5',
    )

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战可是需要军方\n',
            '大张旗鼓地出动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为作战地区是国境边沿，\n',
            '真担心会刺激到帝国军啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D63')

    def _loc_2CC5(): pass

    label('loc_2CC5')

    ChrTalk(
        0x00FE,
        (
            '龙的捕获作战可是需要军方\n',
            '大张旗鼓地出动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '附近有国境线，\n',
            '还是慎重行事为妙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说缔结了互不侵犯条约，\n',
            '但说实话，真是担心帝国军的反应啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    def _loc_2D63(): pass

    label('loc_2D63')

    TalkEnd(0x0032)

    Return()

# id: 0x0018 offset: 0x2D67
@scena.Code('func_18_2D67')
def func_18_2D67():
    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E5C',
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
        100,
        0,
        (
            TXT(0x00, '【◇完成过后篇一章【食材收集】委托】\n'),
            TXT(0x01, '【◇完成过前篇【寻找荧光菇】、【探索护卫】委托】\n'),
            TXT(0x02, '【◇没有完成】\n'),
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
        (0x00000000, 'loc_2E26'),
        (0x00000001, 'loc_2E38'),
        (0x00000002, 'loc_2E4A'),
        (-1, 'loc_2E5C'),
    )

    def _loc_2E26(): pass

    label('loc_2E26')

    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_2E5C')

    def _loc_2E38(): pass

    label('loc_2E38')

    OP_28(0x0065, 0x03, 0x10)
    OP_28(0x0005, 0x04, 0x10)
    OP_28(0x001F, 0x04, 0x10)

    Jump('loc_2E5C')

    def _loc_2E4A(): pass

    label('loc_2E4A')

    OP_28(0x0065, 0x03, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_2E5C')

    def _loc_2E5C(): pass

    label('loc_2E5C')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2E79',
    )

    Call(1, 0x0001)

    Return()

    def _loc_2E79(): pass

    label('loc_2E79')

    TalkBegin(0x0035)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2EF6',
    )

    ChrTalk(
        0x0035,
        (
            '超市的修复\n',
            '似乎还要一阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '唔～真令人着急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '定期船停航的这个时期，\n',
            '正是帮我的食材开拓市场的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3062')

    def _loc_2EF6(): pass

    label('loc_2EF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2F95',
    )

    ChrTalk(
        0x0035,
        (
            '呼，超市要\n',
            '暂时封闭啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '在本地商人的帮助下，总算\n',
            '和『安特洛丝餐厅』进行商谈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '……但是现在这样，我的远大计划\n',
            '不是要打水漂了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3062')

    def _loc_2F95(): pass

    label('loc_2F95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3062',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_2FF0',
    )

    ChrTalk(
        0x0035,
        (
            '正、正打算去超市\n',
            '开始营业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '这种时候没想到\n',
            '居然会被怪物袭击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3062')

    def _loc_2FF0(): pass

    label('loc_2FF0')

    ChrTalk(
        0x0035,
        (
            '正、正打算去超市\n',
            '开始营业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '这种时候没想到\n',
            '居然会被怪物袭击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '啊啊，女神啊！\n',
            '为什么要这样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    def _loc_3062(): pass

    label('loc_3062')

    TalkEnd(0x0035)

    Return()

# id: 0x0019 offset: 0x3066
@scena.Code('func_19_3066')
def func_19_3066():
    TalkBegin(0x0033)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3093',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_308C',
    )

    ChrTalk(
        0x00FE,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3090')

    def _loc_308C(): pass

    label('loc_308C')

    Call(0, 0x001B)

    def _loc_3090(): pass

    label('loc_3090')

    Jump('loc_3101')

    def _loc_3093(): pass

    label('loc_3093')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_30B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_30B2',
    )

    ChrTalk(
        0x00FE,
        (
            '失望……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30B6')

    def _loc_30B2(): pass

    label('loc_30B2')

    Call(0, 0x001B)

    def _loc_30B6(): pass

    label('loc_30B6')

    Jump('loc_3101')

    def _loc_30B9(): pass

    label('loc_30B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3101',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_30FD',
    )

    ChrTalk(
        0x00FE,
        (
            '确，确实避难\n',
            '是最安全的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（生气）……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3101')

    def _loc_30FD(): pass

    label('loc_30FD')

    Call(0, 0x001B)

    def _loc_3101(): pass

    label('loc_3101')

    TalkEnd(0x0033)
    ChrClearFlags(0x0034, 0x0010)

    Return()

# id: 0x001A offset: 0x310A
@scena.Code('func_1A_310A')
def func_1A_310A():
    TalkBegin(0x0034)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3170',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_3169',
    )

    ChrTalk(
        0x00FE,
        (
            '有目标是好，\n',
            '不过哈利缺乏具体的计划哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那不是目标，而是愿望啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_316D')

    def _loc_3169(): pass

    label('loc_3169')

    Call(0, 0x001B)

    def _loc_316D(): pass

    label('loc_316D')

    Jump('loc_31E5')

    def _loc_3170(): pass

    label('loc_3170')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_31AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_31A4',
    )

    ChrTalk(
        0x00FE,
        (
            '善意并不一定\n',
            '会产生好的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A8')

    def _loc_31A4(): pass

    label('loc_31A4')

    Call(0, 0x001B)

    def _loc_31A8(): pass

    label('loc_31A8')

    Jump('loc_31E5')

    def _loc_31AB(): pass

    label('loc_31AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_31E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_31E1',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，这份心意\n',
            '倒是令人感激……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31E5')

    def _loc_31E1(): pass

    label('loc_31E1')

    Call(0, 0x001B)

    def _loc_31E5(): pass

    label('loc_31E5')

    TalkEnd(0x0034)
    ChrClearFlags(0x0034, 0x0010)

    Return()

# id: 0x001B offset: 0x31EE
@scena.Code('func_1B_31EE')
def func_1B_31EE():
    OP_4A(0x0033, 255)
    OP_4A(0x0034, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_32BD',
    )

    ChrTalk(
        0x0033,
        (
            '市长好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '不只是市政的工作，\n',
            '做商人也是一流啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '啊～啊，我将来也想\n',
            '成为那样出色的人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '那么，就努力看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '首先从主日学校的考试\n',
            '拿满分开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3483')

    def _loc_32BD(): pass

    label('loc_32BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_33A2',
    )

    ChrClearFlags(0x0033, 0x0010)
    ChrClearFlags(0x0034, 0x0010)

    ChrTalk(
        0x0033,
        (
            '好厉害啊～\n',
            '工程已经开始了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '我也去\n',
            '帮点忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0034, 0x0033, 400)

    ChrTalk(
        0x0034,
        (
            '还是算了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '如果想帮忙工程，\n',
            '最好就是待在这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0033, 0x0034, 400)

    ChrTalk(
        0x0033,
        (
            '咦？为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '……就不会碍手碍脚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0033, 0x0010)
    ChrSetFlags(0x0034, 0x0010)

    Jump('loc_3483')

    def _loc_33A2(): pass

    label('loc_33A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3483',
    )

    ChrTalk(
        0x0033,
        (
            '米、米娜不要紧吗？\n',
            '有没有受伤？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '嗯嗯，不要紧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '放，放心！\n',
            '城市有我来保护！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '虽然你还算可靠……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '不过在保护城市之前，\n',
            '应该先保护我们自己的人身安全吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '……乖乖\n',
            '去避难所吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0033,
        (
            '是，是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3483(): pass

    label('loc_3483')

    OP_4B(0x0033, 255)
    OP_4B(0x0034, 255)
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    Return()

# id: 0x001C offset: 0x3492
@scena.Code('func_1C_3492')
def func_1C_3492():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_35CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_34FC',
    )

    ChrTalk(
        0x00FE,
        (
            '看来超市的修复工程\n',
            '好像非常顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说，剩下的问题\n',
            '就只有那条龙了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35CC')

    def _loc_34FC(): pass

    label('loc_34FC')

    ChrTalk(
        0x00FE,
        (
            '看来工程比预定\n',
            '进展更快呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说，剩下的问题\n',
            '只剩下龙的问题了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使建筑都修复了，\n',
            '但那种怪物在天空飞来飞去\n',
            '可会让人没心情买东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望王国军的计划，也能像\n',
            '工程这么顺利就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    def _loc_35CC(): pass

    label('loc_35CC')

    TalkEnd(0x000A)

    Return()

# id: 0x001D offset: 0x35D0
@scena.Code('func_1D_35D0')
def func_1D_35D0():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3978',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 5, 0x1A45)),
            Expr.Return,
        ),
        'loc_3650',
    )

    ChrTalk(
        0x001B,
        (
            '#0360310745V#610F总算勉强撑过最困难的时刻了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310746V接下来的目标就是\n',
            '修复超市和稳定市民生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3978')

    def _loc_3650(): pass

    label('loc_3650')

    ChrTalk(
        0x001B,
        (
            '#0360310747V#610F呀，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310748V#1011F啊，梅贝尔市长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310749V#1001F真是令人惊讶，\n',
            '工程竟然已经开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x001B,
        (
            '#0360310750V#611F嗯嗯，多亏市民们帮忙，\n',
            '所以开工比预期的早呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310751V给拉文努村的救援物资\n',
            '也平安送到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310752V这下总算是\n',
            '撑过最困难的时刻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310753V#1015F原来如此，告一段落了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310754V#1000F对了……\n',
            '莉拉的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0360310755V#618F很遗憾……\n',
            '从昨天开始就没有变化。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310756V只有静静等待\n',
            '药效发挥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310757V#1007F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0360310758V#615F但是，光是担心\n',
            '也解决不了任何问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310759V总之，现在身为市长\n',
            '必须履行自己的职责。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310760V#610F如果莉拉在这里……\n',
            '一定会这样说我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310761V#1006F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310762V我们也\n',
            '会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0360310763V#611F嗯嗯，期待\n',
            '你的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0348, 5, 0x1A45))

    def _loc_3978(): pass

    label('loc_3978')

    TalkEnd(0x001B)

    Return()

# id: 0x001E offset: 0x397C
@scena.Code('func_1E_397C')
def func_1E_397C():
    TalkBegin(0x003B)

    ChrTalk(
        0x00FE,
        (
            '嗯，看来药的效果\n',
            '可是发生了不少事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，看起来\n',
            '危险已经过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂时\n',
            '也好像没有避难的必要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x003B)

    Return()

# id: 0x001F offset: 0x39F6
@scena.Code('func_1F_39F6')
def func_1F_39F6():
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
        'loc_3A0D',
    )

    Call(0, 0x003F)
    Call(0, 0x0040)

    def _loc_3A0D(): pass

    label('loc_3A0D')

    Call(0, 0x0032)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x002E, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x002B, 0x0080)
    ChrSetFlags(0x002A, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    OP_4A(0x0036, 255)
    OP_4A(0x0037, 255)
    OP_4A(0x0038, 255)
    OP_4A(0x0039, 255)
    OP_4A(0x003A, 255)
    OP_71(0x0021, 0x0004)
    OP_71(0x0022, 0x0004)
    OP_71(0x0023, 0x0004)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetFlags(0x00FA, 0x0080)
    ChrSetFlags(0x00FB, 0x0080)
    ChrSetFlags(0x00FC, 0x0080)
    CameraMove(59000, 0, 77330, 0)
    OP_67(0, 8620, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(344000, 0)
    OP_6E(262, 0)
    OP_72(0x0012, 0x0004)
    OP_A1(0x0020, 0x0012)
    ChrSetPos(0x0020, 48600, 7100, 60940, 45)
    ChrSetPos(0x0021, 0, 0, 0, 45)
    OP_CF(0x0021, 0x12, 'Frame127_FireEmitter')
    LoadEffect(0x01, 'monster\\ms30703.eff')
    LoadEffect(0x02, 'monster\\ms30704.eff')
    MapClearFlags(0x00000010)
    FadeIn(1000, 0)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 59)
    OP_73(0x0001)
    Sleep(500)

    CreateThread(0x0106, 0x00, 0x00, func_25_5687)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010300844V#1020F#5P啊啊！？',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0106, 0x0000)
    CloseMessageWindow()
    Sleep(200)

    PlayBGM(46)
    Sleep(300)

    @scena.Lambda('lambda_3BD3')
    def lambda_3BD3():
        OP_6C(200000, 7000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3BD3)

    @scena.Lambda('lambda_3BE3')
    def lambda_3BE3():
        OP_6E(490, 7000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_3BE3)

    @scena.Lambda('lambda_3BF3')
    def lambda_3BF3():
        CameraMove(45280, 500, 51530, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3BF3)

    @scena.Lambda('lambda_3C0B')
    def lambda_3C0B():
        OP_67(0, 7000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3C0B)

    @scena.Lambda('lambda_3C23')
    def lambda_3C23():
        CameraSetDistance(5150, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3C23)

    Sleep(5500)

    OP_72(0x0012, 0x0020)
    OP_73(0x0012)
    OP_6F(0x0012, 55)
    OP_70(0x0012, 120)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(41420, 3160, 60230, 0)
    OP_67(0, 4650, -10000, 0)
    CameraSetDistance(3770, 0)
    OP_6C(223000, 0)
    OP_6E(490, 0)
    Sleep(500)

    PlaySE(287, 0x00, 0x64)
    OP_7C(600, 600, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0012)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0012, 0x0020)
    OP_6F(0x0012, 5)
    OP_70(0x0012, 55)

    @scena.Lambda('lambda_3CEE')
    def lambda_3CEE():
        CameraMove(49070, 4400, 60770, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3CEE)

    @scena.Lambda('lambda_3D06')
    def lambda_3D06():
        OP_67(0, 8760, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D06)

    @scena.Lambda('lambda_3D1E')
    def lambda_3D1E():
        CameraSetDistance(3870, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D1E)

    @scena.Lambda('lambda_3D2E')
    def lambda_3D2E():
        OP_6C(210000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D2E)

    OP_72(0x000A, 0x0800)
    OP_72(0x000B, 0x0800)
    OP_72(0x000C, 0x0800)
    OP_72(0x000D, 0x0800)
    OP_72(0x000A, 0x0010)
    OP_72(0x000B, 0x0010)
    OP_72(0x000C, 0x0010)
    OP_72(0x000D, 0x0010)
    OP_6F(0x000A, 0)
    OP_70(0x000A, 59)
    OP_6F(0x000B, 0)
    OP_70(0x000B, 59)
    OP_6F(0x000C, 0)
    OP_70(0x000C, 59)
    OP_6F(0x000D, 0)
    OP_70(0x000D, 59)
    OP_73(0x000D)
    Sleep(500)

    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x000B, 0x01, 0x00, func_2E_58FF)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x000C, 0x01, 0x00, func_2F_592F)
    Sleep(50)

    CreateThread(0x000D, 0x01, 0x00, func_30_5987)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x000E, 0x01, 0x00, func_31_59B7)
    Sleep(400)

    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x000F, 0x01, 0x00, func_2E_58FF)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0010, 0x01, 0x00, func_2F_592F)
    Sleep(50)

    CreateThread(0x0011, 0x01, 0x00, func_30_5987)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0012, 0x01, 0x00, func_31_59B7)
    Sleep(400)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0013, 0x01, 0x00, func_2E_58FF)
    Sleep(50)

    OP_62(0x0014, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0014, 0x01, 0x00, func_2F_592F)
    Sleep(50)

    CreateThread(0x0015, 0x01, 0x00, func_30_5987)
    Sleep(50)

    OP_62(0x0016, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0016, 0x01, 0x00, func_31_59B7)
    Sleep(400)

    OP_62(0x0017, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0017, 0x01, 0x00, func_2E_58FF)
    Sleep(50)

    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0018, 0x01, 0x00, func_2F_592F)
    Sleep(50)

    CreateThread(0x0019, 0x01, 0x00, func_30_5987)
    Sleep(50)

    OP_62(0x001A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x001A, 0x01, 0x00, func_31_59B7)
    Sleep(3500)

    OP_63(0x000B)
    OP_63(0x000C)
    OP_63(0x000D)
    OP_63(0x000E)
    OP_63(0x000F)
    OP_63(0x0010)
    OP_63(0x0011)
    OP_63(0x0012)
    OP_63(0x0013)
    OP_63(0x0014)
    OP_63(0x0015)
    OP_63(0x0016)
    OP_63(0x0017)
    OP_63(0x0018)
    OP_63(0x0019)
    OP_63(0x001A)
    Fade(500)
    CameraMove(58270, 0, 78850, 0)
    OP_67(0, 6790, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(344000, 0)
    OP_6E(283, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300845V#1020F#5P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300846V#065F#5P啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030300847V#023F#5P怎么这么大……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080300848V#077F#2P这是……龙吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060300849V#043F#2P是……是古代龙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300850V传说自古\n',
            '栖息在利贝尔\n',
            '某处的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040300851V#032F#5P哎呀呀，吓死人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300852V#057F#5P难不成……\n',
            '这也是『结社』搞的鬼吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 54630, 4600, 69030, 45)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0140300853V#2P……嗯，那也不必否认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0008, 255, 255, 255, 255, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(20)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(40)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(30)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(20)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_4268')
    def lambda_4268():
        CameraMove(53140, 0, 73070, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4268)

    @scena.Lambda('lambda_4280')
    def lambda_4280():
        OP_67(0, 6620, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4280)

    @scena.Lambda('lambda_4298')
    def lambda_4298():
        CameraSetDistance(2150, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4298)

    @scena.Lambda('lambda_42A8')
    def lambda_42A8():
        OP_6C(264000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_42A8)

    @scena.Lambda('lambda_42B8')
    def lambda_42B8():
        OP_6E(588, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_42B8)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010300854V#1020F#2P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300855V#052F#2P你是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030300856V#024F#2P特务部队队长、\n',
            '洛伦斯·博格少尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '银发的青年',
        (
            '#0140300857V#121F呵呵，那只不过是假名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x00, 0, 0, 512, 512, 100, 0, 768, 512, 0, 0, 512, 512, 0x00FFFFFF, 0x00, 'C_VIS191._CH')
    OP_C6(0x00, 0x00, 125000, 0, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('银发的青年')

    Talk(
        (
            '#0140300858V#124F执行者ＮＯ．Ⅱ。\n',
            '『剑帝』莱恩哈特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140300859V以后，就这么称呼我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(250)

    Sleep(500)

    OP_C6(0x00, 0x06, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010300860V#1020F#2P『剑帝』……莱恩哈特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040300861V#035F#2P原来如此……\n',
            '莱恩哈特（ＬＥＯＮＨＡＲＤＴ）就是『狮子的果敢』的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300862V#030F那么说，莱维（狮子）\n',
            '就是你的爱称吧。',
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
            '#0010261088V#1005F#2P你，你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060300864V#043F#2P你就是莱维……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140300865V#124F……虽然我并不喜欢，\n',
            '但在同伴间这样称呼我的人倒是不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140300866V#123F算了，那就随便你们\n',
            '怎么叫都好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300867V#057F#2P……真是小看人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(287, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_4680')
    def lambda_4680():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4680)

    @scena.Lambda('lambda_468E')
    def lambda_468E():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_468E)

    @scena.Lambda('lambda_469C')
    def lambda_469C():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_469C)

    Sleep(100)

    @scena.Lambda('lambda_46AF')
    def lambda_46AF():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_46AF)

    @scena.Lambda('lambda_46BD')
    def lambda_46BD():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_46BD)

    Sleep(100)

    @scena.Lambda('lambda_46D0')
    def lambda_46D0():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_46D0)

    @scena.Lambda('lambda_46DE')
    def lambda_46DE():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_46DE)

    Sleep(100)

    @scena.Lambda('lambda_46F1')
    def lambda_46F1():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00FC, 0x0001, lambda_46F1)

    @scena.Lambda('lambda_46FF')
    def lambda_46FF():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_46FF)

    Sleep(100)

    Fade(500)
    ChrSetPos(0x0020, 48600, 7100, 60940, 0)
    CameraMove(31950, 0, 69570, 0)
    OP_67(0, 6310, -10000, 0)
    CameraSetDistance(3330, 0)
    OP_6C(251000, 0)
    OP_6E(490, 0)
    OP_72(0x0012, 0x0020)
    OP_6F(0x0012, 55)
    OP_70(0x0012, 115)
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    PlayEffect(0x01, 0x00, 0x0021, 0, 0, 0, 0, -45, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(289, 0x00, 0x64)
    OP_73(0x0012)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0012, 0x0020)
    OP_6F(0x0012, 5)
    OP_70(0x0012, 55)
    Sleep(1500)

    Fade(500)
    OP_71(0x0012, 0x0004)
    ChrSetPos(0x0020, 48600, 7100, 60940, 45)
    CameraMove(57430, 0, 76950, 0)
    OP_67(0, 8390, -10000, 0)
    CameraSetDistance(2940, 0)
    OP_6C(11000, 0)
    OP_6E(291, 0)
    ChrSetDirection(0x0008, 225, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300868V#1020F#2P啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030300869V#523F#5P打算烧了城市吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140300870V#124F#5P……真是的。\n',
            '让我多费工夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetChipByIndex(0x0008, 33)
    ChrSetSubChip(0x0008, 1)
    OP_0D()
    Sleep(200)

    ChrClearFlags(0x0008, 0x0001)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)
    ChrSetSubChip(0x0008, 2)
    PlaySE(163, 0x00, 0x64)
    ChrSetDirection(0x0008, 270, 0)

    @scena.Lambda('lambda_490E')
    def lambda_490E():
        ChrJumpTo(0x00FE, 48430, 15100, 65620, 11000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_490E)

    Sleep(200)

    Fade(100)
    OP_72(0x0012, 0x0004)
    CameraMove(56240, 18870, 65550, 0)
    OP_67(0, 8780, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(270000, 0)
    OP_6E(312, 0)
    WaitForThreadExit(0x0008, 0x0003)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0008, 1)
    ChrClearFlags(0x0008, 0x0004)
    OP_CF(0x0008, 0x12, 'Frame141_back_Null1')
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetDirection(0x0008, 90, 0)
    Sleep(500)

    ChrSetChipByIndex(0x0008, 34)
    ChrSetSubChip(0x0008, 0)
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_49D7')
    def lambda_49D7():
        OP_67(0, 8740, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_49D7)

    @scena.Lambda('lambda_49EF')
    def lambda_49EF():
        CameraSetDistance(2500, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_49EF)

    @scena.Lambda('lambda_49FF')
    def lambda_49FF():
        OP_6E(442, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_49FF)

    @scena.Lambda('lambda_4A0F')
    def lambda_4A0F():
        CameraMove(52240, 18870, 65550, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_4A0F)

    @scena.Lambda('lambda_4A27')
    def lambda_4A27():
        ChrSetDirection(0x00FE, 315, 80)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_4A27)

    OP_72(0x0012, 0x0020)
    OP_6F(0x0012, 116)
    OP_70(0x0012, 145)
    OP_73(0x0012)
    OP_B0(0x0012, 0x05)
    OP_71(0x0012, 0x0020)
    OP_6F(0x0012, 145)
    OP_70(0x0012, 158)
    Sleep(200)

    CreateThread(0x0020, 0x03, 0x00, func_20_4D7C)
    Sleep(500)

    CreateThread(0x0020, 0x01, 0x00, func_21_4D93)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050300871V#055F#5P给、给我停下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140300872V#122F#6P……这次的实验\n',
            '稍微有点不合常理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140300873V说实话，并不是你们\n',
            '能够应付的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140300874V#125F把事情交给王国军，\n',
            '然后待在一边乖乖看着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_4B5F')
    def lambda_4B5F():
        CameraMove(48240, 18870, 69550, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_4B5F)

    @scena.Lambda('lambda_4B77')
    def lambda_4B77():
        OP_67(0, 10000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4B77)

    @scena.Lambda('lambda_4B8F')
    def lambda_4B8F():
        CameraSetDistance(4010, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_4B8F)

    @scena.Lambda('lambda_4B9F')
    def lambda_4B9F():
        OP_6C(270000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_4B9F)

    @scena.Lambda('lambda_4BAF')
    def lambda_4BAF():
        OP_6E(395, 4000)

        ExitThread()

    DispatchAsync(0x0020, 0x0003, lambda_4BAF)

    @scena.Lambda('lambda_4BBF')
    def lambda_4BBF():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4BBF')

    DispatchAsync2(0x0101, 0x0001, lambda_4BBF)

    @scena.Lambda('lambda_4BD0')
    def lambda_4BD0():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4BD0')

    DispatchAsync2(0x0106, 0x0001, lambda_4BD0)

    @scena.Lambda('lambda_4BE1')
    def lambda_4BE1():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4BE1')

    DispatchAsync2(0x00F8, 0x0001, lambda_4BE1)

    @scena.Lambda('lambda_4BF2')
    def lambda_4BF2():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4BF2')

    DispatchAsync2(0x00F9, 0x0001, lambda_4BF2)

    @scena.Lambda('lambda_4C03')
    def lambda_4C03():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4C03')

    DispatchAsync2(0x00FA, 0x0001, lambda_4C03)

    @scena.Lambda('lambda_4C14')
    def lambda_4C14():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4C14')

    DispatchAsync2(0x00FB, 0x0001, lambda_4C14)

    @scena.Lambda('lambda_4C25')
    def lambda_4C25():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4C25')

    DispatchAsync2(0x00FC, 0x0001, lambda_4C25)

    @scena.Lambda('lambda_4C36')
    def lambda_4C36():
        ChrTurnDirection(0x00FE, 0x0020, 0)
        Yield()

        Jump('lambda_4C36')

    DispatchAsync2(0x0009, 0x0001, lambda_4C36)

    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 0)
    OP_72(0x0012, 0x0020)
    OP_73(0x0012)
    OP_B0(0x0012, 0x14)
    OP_6F(0x0012, 145)
    OP_70(0x0012, 170)
    PlaySE(136, 0x00, 0x64)
    OP_7C(0, 400, 5000, 1500)
    PlayEffect(0x02, 0x00, 0x0020, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0x01, 0x0020, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0012, 0x0020)
    OP_B0(0x0012, 0x19)
    OP_6F(0x0012, 170)
    OP_70(0x0012, 190)
    PlayEffect(0x02, 0x02, 0x0020, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0020, 0x01)
    CreateThread(0x0020, 0x00, 0x00, func_22_4DDA)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(2500)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x4D7C
@scena.Code('func_20_4D7C')
def func_20_4D7C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4D92',
    )

    PlaySE(288, 0x00, 0x64)
    Sleep(2700)

    Jump('func_20_4D7C')

    def _loc_4D92(): pass

    label('loc_4D92')

    Return()

# id: 0x0021 offset: 0x4D93
@scena.Code('func_21_4D93')
def func_21_4D93():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4DD9',
    )

    PlayEffect(0x02, 0xFF, 0x0020, 0, -6000, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(2700)

    Jump('func_21_4D93')

    def _loc_4DD9(): pass

    label('loc_4DD9')

    Return()

# id: 0x0022 offset: 0x4DDA
@scena.Code('func_22_4DDA')
def func_22_4DDA():
    PlaySE(288, 0x00, 0x64)

    @scena.Lambda('lambda_4DE5')
    def lambda_4DE5():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4DE5)

    Sleep(200)

    PlayEffect(0x02, 0x00, 0x0020, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4E3A')
    def lambda_4E3A():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4E3A)

    Sleep(200)

    PlayEffect(0x02, 0x01, 0x0020, 0, -2000, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlaySE(288, 0x00, 0x64)

    @scena.Lambda('lambda_4E94')
    def lambda_4E94():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4E94)

    Sleep(200)

    PlayEffect(0x02, 0x01, 0x0020, 0, -4000, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_4EE9')
    def lambda_4EE9():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4EE9)

    Sleep(200)

    @scena.Lambda('lambda_4F09')
    def lambda_4F09():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4F09)

    Sleep(200)

    PlaySE(288, 0x00, 0x64)

    @scena.Lambda('lambda_4F2E')
    def lambda_4F2E():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 32000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4F2E)

    Sleep(300)

    @scena.Lambda('lambda_4F4E')
    def lambda_4F4E():
        ChrMoveTo(0x00FE, -25690, 35000, 110610, 64000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4F4E)

    Return()

# id: 0x0023 offset: 0x4F64
@scena.Code('func_23_4F64')
def func_23_4F64():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(58650, 0, 78150, 0)
    OP_67(0, 6790, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(344000, 0)
    OP_6E(283, 0)
    OP_71(0x0021, 0x0004)
    OP_71(0x0022, 0x0004)
    OP_71(0x0023, 0x0004)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x00FA, 0x01)
    TerminateThread(0x00FB, 0x01)
    TerminateThread(0x00FC, 0x01)
    TerminateThread(0x0009, 0x01)
    ChrSetPos(0x0101, 59570, 0, 76570, 315)
    ChrSetPos(0x0106, 58320, 0, 76730, 315)
    ChrSetPos(0x0107, 57360, 0, 77470, 315)
    ChrSetPos(0x0103, 58660, 0, 77700, 315)
    ChrSetPos(0x0104, 58080, 0, 78840, 315)
    ChrSetPos(0x0105, 60210, 0, 77350, 315)
    ChrSetPos(0x0108, 59500, 0, 78870, 315)
    ChrSetPos(0x0009, 59050, 500, 79890, 315)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x002C, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0035, 0x0080)
    ChrSetFlags(0x002F, 0x0080)
    ChrSetFlags(0x0030, 0x0080)
    ChrSetFlags(0x0031, 0x0080)
    ChrSetFlags(0x0032, 0x0080)
    ChrSetFlags(0x002E, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x002B, 0x0080)
    ChrSetFlags(0x002A, 0x0080)
    ChrSetFlags(0x0029, 0x0080)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0027, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    OP_4A(0x0036, 255)
    OP_4A(0x0037, 255)
    OP_4A(0x0038, 255)
    OP_4A(0x0039, 255)
    OP_4A(0x003A, 255)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 59)
    OP_72(0x000C, 0x0010)
    OP_6F(0x000C, 59)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300875V#1005F#6P怎、怎么办……\n',
            '这样下去会被他逃掉的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300876V#053F#5P……我现在\n',
            '去追踪那个大家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300877V#057F你们在军方到来之前\n',
            '先确认受害状况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_51BD')
    def lambda_51BD():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_51BD)

    Sleep(10)

    @scena.Lambda('lambda_51D0')
    def lambda_51D0():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_51D0)

    Sleep(20)

    @scena.Lambda('lambda_51E3')
    def lambda_51E3():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_51E3)

    Sleep(10)

    @scena.Lambda('lambda_51F6')
    def lambda_51F6():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_51F6)

    Sleep(30)

    @scena.Lambda('lambda_5209')
    def lambda_5209():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_5209)

    Sleep(10)

    @scena.Lambda('lambda_521C')
    def lambda_521C():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x00FC, 0x0001, lambda_521C)

    Sleep(20)

    @scena.Lambda('lambda_522F')
    def lambda_522F():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_522F)

    Sleep(400)

    @scena.Lambda('lambda_5242')
    def lambda_5242():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_5242')

    DispatchAsync2(0x0101, 0x0001, lambda_5242)

    @scena.Lambda('lambda_5253')
    def lambda_5253():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_5253')

    DispatchAsync2(0x00F8, 0x0001, lambda_5253)

    @scena.Lambda('lambda_5264')
    def lambda_5264():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_5264')

    DispatchAsync2(0x00F9, 0x0001, lambda_5264)

    @scena.Lambda('lambda_5275')
    def lambda_5275():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_5275')

    DispatchAsync2(0x00FA, 0x0001, lambda_5275)

    @scena.Lambda('lambda_5286')
    def lambda_5286():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_5286')

    DispatchAsync2(0x00FB, 0x0001, lambda_5286)

    @scena.Lambda('lambda_5297')
    def lambda_5297():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_5297')

    DispatchAsync2(0x00FC, 0x0001, lambda_5297)

    @scena.Lambda('lambda_52A8')
    def lambda_52A8():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_52A8')

    DispatchAsync2(0x0009, 0x0001, lambda_52A8)

    ChrTalk(
        0x0101,
        (
            '#0010211688V#1020F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030300879V#023F#2P阿加特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300880V#054F#5P稍后联络！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5324')
    def lambda_5324():
        OP_6C(302000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5324)

    @scena.Lambda('lambda_5334')
    def lambda_5334():
        CameraMove(55320, 0, 76560, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5334)

    @scena.Lambda('lambda_534C')
    def lambda_534C():
        ChrWalkTo(0x00FE, 38120, 0, 73830, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_534C)

    Sleep(2000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    TerminateThread(0x00FA, 0x01)
    TerminateThread(0x00FB, 0x01)
    TerminateThread(0x00FC, 0x01)
    TerminateThread(0x0009, 0x01)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070300881V#065F#5P阿加特哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300882V#1020F#6P等、等等！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 49540, 0, 70870, 0)
    ChrClearFlags(0x000A, 0x0080)

    ChrTalk(
        0x000A,
        (
            '#3520300883V#4P是、是你们！\n',
            '还好找到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5425')
    def lambda_5425():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5425)

    @scena.Lambda('lambda_5433')
    def lambda_5433():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5433)

    @scena.Lambda('lambda_5441')
    def lambda_5441():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5441)

    @scena.Lambda('lambda_544F')
    def lambda_544F():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_544F)

    @scena.Lambda('lambda_545D')
    def lambda_545D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_545D)

    @scena.Lambda('lambda_546B')
    def lambda_546B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00FC, 0x0001, lambda_546B)

    @scena.Lambda('lambda_5479')
    def lambda_5479():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5479)

    @scena.Lambda('lambda_5487')
    def lambda_5487():
        OP_6C(270000, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5487)

    @scena.Lambda('lambda_5497')
    def lambda_5497():
        CameraMove(54350, 0, 74950, 1800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5497)

    @scena.Lambda('lambda_54AF')
    def lambda_54AF():
        ChrWalkTo(0x00FE, 53810, 0, 74210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_54AF)

    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    WaitForThreadExit(0x000A, 0x0001)
    OP_4A(0x000A, 255)

    @scena.Lambda('lambda_54E5')
    def lambda_54E5():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_54E5)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#3520300884V#5P拜托了，来帮帮我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3520300885V#5P有人被压在瓦砾下面\n',
            '还没有逃出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0108,
        (
            '#0080300886V#072F#2P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300887V#1005F#2P你、你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x07, 0xFF)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1123._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0024 offset: 0x55CB
@scena.Code('func_24_55CB')
def func_24_55CB():
    @scena.Lambda('lambda_55D1')
    def lambda_55D1():
        ChrMoveTo(0x00FE, 50790, 0, 74910, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_55D1)

    Sleep(300)

    @scena.Lambda('lambda_55F1')
    def lambda_55F1():
        ChrMoveTo(0x00FE, 50890, 0, 75910, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_55F1)

    Sleep(100)

    @scena.Lambda('lambda_5611')
    def lambda_5611():
        ChrMoveTo(0x00FE, 52100, 0, 75100, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_5611)

    Sleep(100)

    @scena.Lambda('lambda_5631')
    def lambda_5631():
        ChrMoveTo(0x00FE, 51720, 0, 73740, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5631)

    Sleep(100)

    @scena.Lambda('lambda_5651')
    def lambda_5651():
        ChrMoveTo(0x00FE, 53030, 0, 73140, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5651)

    Sleep(100)

    @scena.Lambda('lambda_5671')
    def lambda_5671():
        ChrMoveTo(0x00FE, 59640, 0, 78210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_5671)

    Return()

# id: 0x0025 offset: 0x5687
@scena.Code('func_25_5687')
def func_25_5687():
    CreateThread(0x0106, 0x01, 0x00, func_27_5729)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x00, func_26_56E3)
    Sleep(400)

    CreateThread(0x0107, 0x01, 0x00, func_28_576F)
    Sleep(400)

    CreateThread(0x0103, 0x01, 0x00, func_29_57B5)
    Sleep(400)

    CreateThread(0x0105, 0x01, 0x00, func_2B_5841)
    Sleep(400)

    CreateThread(0x0104, 0x01, 0x00, func_2A_57FB)
    Sleep(400)

    CreateThread(0x0108, 0x01, 0x00, func_2C_5887)
    Sleep(400)

    CreateThread(0x0009, 0x01, 0x00, func_2D_58CD)

    Return()

# id: 0x0026 offset: 0x56E3
@scena.Code('func_26_56E3')
def func_26_56E3():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 59570, 0, 76570, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0027 offset: 0x5729
@scena.Code('func_27_5729')
def func_27_5729():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 58320, 0, 76730, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0028 offset: 0x576F
@scena.Code('func_28_576F')
def func_28_576F():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 57360, 0, 77470, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0029 offset: 0x57B5
@scena.Code('func_29_57B5')
def func_29_57B5():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 58660, 0, 77700, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x002A offset: 0x57FB
@scena.Code('func_2A_57FB')
def func_2A_57FB():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 58080, 0, 78840, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x002B offset: 0x5841
@scena.Code('func_2B_5841')
def func_2B_5841():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 60210, 0, 77350, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x002C offset: 0x5887
@scena.Code('func_2C_5887')
def func_2C_5887():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59060, 470, 79530, 5000, 0x00)
    ChrWalkTo(0x00FE, 59500, 0, 78870, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x002D offset: 0x58CD
@scena.Code('func_2D_58CD')
def func_2D_58CD():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59050, 500, 79890, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x002E offset: 0x58FF
@scena.Code('func_2E_58FF')
def func_2E_58FF():
    ChrSetPos(0x00FE, 54510, 0, 60010, 90)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 72590, 0, 60010, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002F offset: 0x592F
@scena.Code('func_2F_592F')
def func_2F_592F():
    ChrSetPos(0x00FE, 41460, 0, 59990, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 32580, 0, 59990, 5000, 0x00)
    ChrWalkTo(0x00FE, 32710, 0, 43760, 5000, 0x00)
    ChrWalkTo(0x00FE, 17140, 0, 42870, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0030 offset: 0x5987
@scena.Code('func_30_5987')
def func_30_5987():
    ChrSetPos(0x00FE, 48010, 0, 53480, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 48570, -3000, 17410, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0031 offset: 0x59B7
@scena.Code('func_31_59B7')
def func_31_59B7():
    ChrSetPos(0x00FE, 48040, 0, 66510, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 47990, 3000, 91080, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0032 offset: 0x59E7
@scena.Code('func_32_59E7')
def func_32_59E7():
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
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5A20',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_5A20(): pass

    label('loc_5A20')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5A6D',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A55',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_5A6D')

    def _loc_5A55(): pass

    label('loc_5A55')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_5A6D(): pass

    label('loc_5A6D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5AE2',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AA2',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_5AE2')

    def _loc_5AA2(): pass

    label('loc_5AA2')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5ACA',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_5AE2')

    def _loc_5ACA(): pass

    label('loc_5ACA')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_5AE2(): pass

    label('loc_5AE2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B2F',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B17',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_5B2F')

    def _loc_5B17(): pass

    label('loc_5B17')

    FormationAddMember(ChrTable['科洛丝'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_5B2F(): pass

    label('loc_5B2F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5B54',
    )

    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_5B54(): pass

    label('loc_5B54')

    Return()

# id: 0x0033 offset: 0x5B55
@scena.Code('func_33_5B55')
def func_33_5B55():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C72',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BD6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300975V#074F现在已经\n',
            '没空乱逛了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300976V#070F在街上买过东西之后\n',
            '就去国际空港吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C54')

    def _loc_5BD6(): pass

    label('loc_5BD6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BEC',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_5BF3')

    def _loc_5BEC(): pass

    label('loc_5BEC')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_5BF3(): pass

    label('loc_5BF3')

    ChrTalk(
        0x0103,
        (
            '#0030300977V#020F现在已经\n',
            '没时间闲逛了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300978V在街上买完东西以后\n',
            '就去国际空港吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C54(): pass

    label('loc_5C54')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_6160')

    def _loc_5C72(): pass

    label('loc_5C72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 6, 0x1A16)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5EE1',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_5CA0'),
        (0x00000002, 'loc_5CF6'),
        (0x00000004, 'loc_5D54'),
        (0x00000003, 'loc_5DAE'),
        (0x00000006, 'loc_5E0C'),
        (0x00000007, 'loc_5E6C'),
        (-1, 'loc_5EC3'),
    )

    def _loc_5CA0(): pass

    label('loc_5CA0')

    ChrTalk(
        0x0101,
        (
            '#0010300979V#1002F不是这条路啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300980V准备完毕之后\n',
            '马上回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5CF6(): pass

    label('loc_5CF6')

    ChrTalk(
        0x0103,
        (
            '#0030300981V#022F现在没时间\n',
            '绕远路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300982V准备结束之后\n',
            '就赶快回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5D54(): pass

    label('loc_5D54')

    ChrTalk(
        0x0105,
        (
            '#0060300983V#042F现在没空\n',
            '绕远路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300984V准备结束之后\n',
            '赶快回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5DAE(): pass

    label('loc_5DAE')

    ChrTalk(
        0x0104,
        (
            '#0040300985V#032F现在不是闲逛\n',
            '的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300986V准备完毕之后\n',
            '赶快回拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5E0C(): pass

    label('loc_5E0C')

    ChrTalk(
        0x0107,
        (
            '#0070300987V#062F……别再\n',
            '磨磨蹭蹭的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300988V准备好之后\n',
            '赶快追上阿加特哥哥吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5E6C(): pass

    label('loc_5E6C')

    ChrTalk(
        0x0108,
        (
            '#0080300989V#072F已经没时间乱逛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300990V准备好之后\n',
            '赶快回拉文努村吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5EC3(): pass

    label('loc_5EC3')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_6160')

    def _loc_5EE1(): pass

    label('loc_5EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6160',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_5F0F'),
        (0x00000002, 'loc_5F67'),
        (0x00000004, 'loc_5FC0'),
        (0x00000003, 'loc_6019'),
        (0x00000006, 'loc_606E'),
        (0x00000007, 'loc_60F2'),
        (-1, 'loc_6145'),
    )

    def _loc_5F0F(): pass

    label('loc_5F0F')

    ChrTalk(
        0x0101,
        (
            '#0010300991V#1002F现在必须要\n',
            '赶快到拉文努村…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300992V从西边的出口出去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6145')

    def _loc_5F67(): pass

    label('loc_5F67')

    ChrTalk(
        0x0103,
        (
            '#0030300993V#022F要去拉文努村的话，\n',
            '得从西边的出口出去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300994V快一点吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6145')

    def _loc_5FC0(): pass

    label('loc_5FC0')

    ChrTalk(
        0x0105,
        (
            '#0060300995V#042F拉文努村\n',
            '位于柏斯的西北方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300996V从西边的出口出去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6145')

    def _loc_6019(): pass

    label('loc_6019')

    ChrTalk(
        0x0104,
        (
            '#0040300997V#032F拉文努村\n',
            '是在西北方向呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300998V从西边的出口出去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6145')

    def _loc_606E(): pass

    label('loc_606E')

    ChrTalk(
        0x0107,
        (
            '#0070300999V#065F啊啊……\n',
            '要去拉文努村的话，\n',
            '应该从西边的出口出去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301000V#062F我们必须要早点\n',
            '追上阿加特哥哥……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6145')

    def _loc_60F2(): pass

    label('loc_60F2')

    ChrTalk(
        0x0108,
        (
            '#0080301001V#072F去拉文努村的话、\n',
            '要从西边出去，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080301002V赶快行动吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6145')

    def _loc_6145(): pass

    label('loc_6145')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6160(): pass

    label('loc_6160')

    Return()

# id: 0x0034 offset: 0x6161
@scena.Code('func_34_6161')
def func_34_6161():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_627B',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61E2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300975V#074F现在已经\n',
            '没空乱逛了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300976V#070F在街上买过东西之后\n',
            '就去国际空港吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6260')

    def _loc_61E2(): pass

    label('loc_61E2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61F8',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_61FF')

    def _loc_61F8(): pass

    label('loc_61F8')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_61FF(): pass

    label('loc_61FF')

    ChrTalk(
        0x0103,
        (
            '#0030300977V#020F现在已经\n',
            '没时间闲逛了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300978V在街上买完东西以后\n',
            '就去国际空港吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6260(): pass

    label('loc_6260')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_627B(): pass

    label('loc_627B')

    Return()

# id: 0x0035 offset: 0x627C
@scena.Code('func_35_627C')
def func_35_627C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_6284',
    )

    Return()

    def _loc_6284(): pass

    label('loc_6284')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_62D4',
    )

    EventBegin(0x02)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '◆禁止进入用障壁的代替品',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_62D4(): pass

    label('loc_62D4')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0036 offset: 0x62F0
@scena.Code('func_36_62F0')
def func_36_62F0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_62F8',
    )

    Return()

    def _loc_62F8(): pass

    label('loc_62F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_6348',
    )

    EventBegin(0x02)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '◆禁止进入用障壁的代替品',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_6348(): pass

    label('loc_6348')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0037 offset: 0x6364
@scena.Code('func_37_6364')
def func_37_6364():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_636C',
    )

    Return()

    def _loc_636C(): pass

    label('loc_636C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_63BC',
    )

    EventBegin(0x02)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '◆禁止进入用障壁的代替品',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_63BC(): pass

    label('loc_63BC')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0038 offset: 0x63D8
@scena.Code('func_38_63D8')
def func_38_63D8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_63E0',
    )

    Return()

    def _loc_63E0(): pass

    label('loc_63E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_6430',
    )

    EventBegin(0x02)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '◆禁止进入用障壁的代替品',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_6430(): pass

    label('loc_6430')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0039 offset: 0x644C
@scena.Code('func_39_644C')
def func_39_644C():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    OP_E5(0x2A, 0x00, 0x00)
    CameraMove(47330, 400, 59690, 0)
    OP_67(0, 14540, -10000, 0)
    CameraSetDistance(2840, 0)
    OP_6C(314000, 0)
    OP_6E(556, 0)
    OP_71(0x000C, 0x0004)
    OP_71(0x0023, 0x0004)
    ChrSetPos(0x001B, 45230, 0, 74390, 90)
    ChrSetPos(0x000B, 47000, 0, 73840, 270)
    ChrSetPos(0x000C, 46950, 0, 74750, 270)
    ChrSetPos(0x000D, 46540, 0, 72950, 315)
    ChrSetPos(0x001D, 46630, 0, 75700, 225)
    ChrSetPos(0x001C, 48040, 0, 71510, 90)
    ChrSetPos(0x000F, 49220, 0, 71700, 90)
    ChrSetPos(0x0011, 49940, 0, 72980, 135)
    ChrSetPos(0x001E, 51670, 0, 72890, 90)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    OP_E5(0x1B, 0x00, 0x00)
    OP_E5(0x0B, 0x00, 0x00)
    OP_E5(0x0C, 0x00, 0x00)
    OP_E5(0x0D, 0x00, 0x00)
    OP_E5(0x0F, 0x00, 0x00)
    OP_E5(0x11, 0x00, 0x00)
    OP_E5(0x1C, 0x00, 0x00)
    OP_E5(0x1D, 0x00, 0x00)
    OP_E5(0x1E, 0x00, 0x00)
    PlaySE(450, 0x00, 0x64)
    CreateThread(0x001B, 0x01, 0x00, func_3A_66BF)
    CreateThread(0x001E, 0x01, 0x00, func_3B_673F)

    @scena.Lambda('lambda_65AC')
    def lambda_65AC():
        OP_6C(213000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_65AC)

    FadeIn(2000, 0)
    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    @scena.Lambda('lambda_65D4')
    def lambda_65D4():
        CameraMove(46830, 400, 72760, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_65D4)

    @scena.Lambda('lambda_65EC')
    def lambda_65EC():
        OP_67(0, 9760, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_65EC)

    @scena.Lambda('lambda_6604')
    def lambda_6604():
        CameraSetDistance(2800, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6604)

    @scena.Lambda('lambda_6614')
    def lambda_6614():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_6614)

    ChrWalkTo(0x001C, 48040, 300, 69500, 2000, 0x00)
    OP_72(0x000C, 0x0010)
    OP_6F(0x000C, 0)
    OP_70(0x000C, 59)
    OP_73(0x000C)
    ChrTurnDirection(0x001C, 0x000F, 400)
    Sleep(1000)

    CreateThread(0x000F, 0x01, 0x00, func_3C_677C)
    Sleep(800)

    CreateThread(0x0011, 0x01, 0x00, func_3D_67BB)
    Sleep(2000)

    ChrSetDirection(0x001C, 180, 400)

    @scena.Lambda('lambda_6679')
    def lambda_6679():
        ChrWalkTo(0x00FE, 48040, 500, 66510, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_6679)

    WaitForThreadExit(0x001C, 0x0001)
    ChrSetFlags(0x001C, 0x0080)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_E5(0x2A, 0x00, 0x01)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x003A offset: 0x66BF
@scena.Code('func_3A_66BF')
def func_3A_66BF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_673E',
    )

    OP_62(0x001B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1500)

    OP_62(0x001D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(100)

    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(100)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(100)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1500)

    Jump('func_3A_66BF')

    def _loc_673E(): pass

    label('loc_673E')

    Return()

# id: 0x003B offset: 0x673F
@scena.Code('func_3B_673F')
def func_3B_673F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_677B',
    )

    ChrSetDirection(0x00FE, 0, 300)
    Sleep(1000)

    ChrSetDirection(0x00FE, 270, 300)
    Sleep(1000)

    ChrSetDirection(0x00FE, 0, 300)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 300)
    Sleep(1000)

    Jump('func_3B_673F')

    def _loc_677B(): pass

    label('loc_677B')

    Return()

# id: 0x003C offset: 0x677C
@scena.Code('func_3C_677C')
def func_3C_677C():
    Sleep(500)

    ChrTurnDirection(0x00FE, 0x001C, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 48040, 300, 69500, 2000, 0x00)
    ChrWalkTo(0x00FE, 48040, 500, 66510, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x003D offset: 0x67BB
@scena.Code('func_3D_67BB')
def func_3D_67BB():
    Sleep(500)

    ChrTurnDirection(0x00FE, 0x001C, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 48640, 0, 72260, 2000, 0x00)
    ChrWalkTo(0x00FE, 48040, 500, 66510, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x003E offset: 0x67FA
@scena.Code('func_3E_67FA')
def func_3E_67FA():
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
        'loc_6811',
    )

    Call(0, 0x003F)
    Call(0, 0x0042)

    def _loc_6811(): pass

    label('loc_6811')

    ChrSetStatus(0x00FF, 0xFE, 0)
    CameraMove(48700, 0, 83750, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 47650, 1500, 87720, 180)
    ChrSetPos(0x0106, 49120, 1500, 87720, 180)
    ChrSetPos(0x0107, 49200, 2500, 89250, 180)
    ChrSetPos(0x00F9, 47650, 2500, 89250, 180)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_68A6')
    def lambda_68A6():
        ChrWalkTo(0x00FE, 47650, 0, 82720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_68A6)

    Sleep(70)

    @scena.Lambda('lambda_68C6')
    def lambda_68C6():
        ChrWalkTo(0x00FE, 49120, 0, 82720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_68C6)

    Sleep(80)

    @scena.Lambda('lambda_68E6')
    def lambda_68E6():
        ChrWalkTo(0x00FE, 47650, 0, 84250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_68E6)

    Sleep(70)

    @scena.Lambda('lambda_6906')
    def lambda_6906():
        ChrWalkTo(0x00FE, 49200, 0, 84250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_6906)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_6926')
    def lambda_6926():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6926)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_6939')
    def lambda_6939():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_6939)

    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_694C')
    def lambda_694C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_694C)

    WaitForThreadExit(0x0107, 0x0001)
    ChrSetDirection(0x0107, 225, 400)
    Sleep(300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A05',
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
            TXT(0x00, '【◇在后篇见过维姆拉】\n'),
            TXT(0x01, '【◇在后篇没见过维姆拉】\n'),
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
        (0x00000000, 'loc_69F9'),
        (0x00000001, 'loc_69FF'),
        (-1, 'loc_6A05'),
    )

    def _loc_69F9(): pass

    label('loc_69F9')

    SetScenaFlags(ScenaFlag(0x0350, 0, 0x1A80))

    Jump('loc_6A05')

    def _loc_69FF(): pass

    label('loc_69FF')

    ClearScenaFlags(ScenaFlag(0x0350, 0, 0x1A80))

    Jump('loc_6A05')

    def _loc_6A05(): pass

    label('loc_6A05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 0, 0x1A80)),
            Expr.Return,
        ),
        'loc_6A9A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310809V#1006F#6P好了，去找\n',
            '迷雾峡谷的维姆拉先生对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310810V#053F#2P啊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310811V#552F话说回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0096, 0x01, 0x0004)
    OP_28(0x0096, 0x01, 0x0008)

    Jump('loc_6B44')

    def _loc_6A9A(): pass

    label('loc_6A9A')

    ChrTalk(
        0x0101,
        (
            '#0010310812V#1006F#6P好了，去找\n',
            '要去拜访叫做维姆拉的人对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310813V#053F#2P啊啊、应该住在\n',
            '峡谷东侧的山中小屋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310811V#552F话说回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0096, 0x01, 0x0010)
    OP_28(0x0096, 0x01, 0x0020)

    def _loc_6B44(): pass

    label('loc_6B44')

    ChrTurnDirection(0x0106, 0x0107, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050310815V#555F……果然\n',
            '打算跟着来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070310816V#061F嘿嘿，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310817V#560F振动装置要是出故障了\n',
            '就可以当场修理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070310818V如果是遇到会飞行的敌人，\n',
            '导力炮也会有用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310819V#053F呼……真没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310820V#051F不要太乱来，\n',
            '免得拖我后腿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310821V#067F好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CCB',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_6CFF')

    def _loc_6CCB(): pass

    label('loc_6CCB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CED',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_6CFF')

    def _loc_6CED(): pass

    label('loc_6CED')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_6CFF(): pass

    label('loc_6CFF')

    Sleep(1500)

    ChrSetDirection(0x0106, 270, 400)
    Sleep(100)

    ChrTurnDirection(0x0107, 0x0101, 400)
    Sleep(300)

    OP_62(0x0106, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070310822V#560F#5P什、什么、姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    OP_63(0x00F9)

    ChrTalk(
        0x0106,
        (
            '#0050310823V#555F#2P……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310824V#1028F#6P呀～怎么说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310825V觉得你们好像\n',
            '比以前更要好了呢。',
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
        'loc_6E48',
    )

    ChrTalk(
        0x0103,
        (
            '#0030310826V#027F#1P呵呵，看来\n',
            '发生什么好事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F1B')

    def _loc_6E48(): pass

    label('loc_6E48')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E90',
    )

    ChrTalk(
        0x0105,
        (
            '#0060310827V#048F#1P嘻……\n',
            '好像发生什么好事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F1B')

    def _loc_6E90(): pass

    label('loc_6E90')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6ED6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040310828V#037F#1P呼，看来\n',
            '发生什么好事了呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F1B')

    def _loc_6ED6(): pass

    label('loc_6ED6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F1B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080310829V#071F#1P哈哈，看来\n',
            '发生什么好事了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F1B(): pass

    label('loc_6F1B')

    ChrTalk(
        0x0107,
        (
            '#0070310830V#065F#5P啊啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050310831V#055F#2P说、说什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310832V#1001F#6P啊哈哈，别着急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310833V#1006F不过……心情似乎\n',
            '已经调整好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310834V#051F#2P……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310835V不会再一个人穷追猛打，\n',
            '做那种自杀式行为了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050310836V我可不想再被那个小不点\n',
            '一脸凶凶地教训了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310837V#562F啊……\n',
            '阿加特哥哥真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310838V#1012F#6P呵呵……是吗是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310839V#1018F好～那么\n',
            '立刻去迷雾峡谷吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070310840V#061F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310841V#051F#2P噢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0095, 0x01, 0x0040)
    OP_28(0x0095, 0x01, 0x0080)
    OP_28(0x0095, 0x01, 0x0100)
    OP_28(0x0096, 0x04, 0x02)
    OP_28(0x0096, 0x04, 0x08)
    OP_28(0x0096, 0x01, 0x0001)
    OP_28(0x0096, 0x01, 0x0002)
    OP_20(0x000003E8)
    OP_21()
    EventEnd(0x00)
    PlayBGM(11)

    Return()

# id: 0x003F offset: 0x716A
@scena.Code('func_3F_716A')
def func_3F_716A():
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
        (0x00000000, 'loc_71E7'),
        (0x00000001, 'loc_71ED'),
        (-1, 'loc_71F3'),
    )

    def _loc_71E7(): pass

    label('loc_71E7')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_71F3')

    def _loc_71ED(): pass

    label('loc_71ED')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_71F3')

    def _loc_71F3(): pass

    label('loc_71F3')

    Return()

# id: 0x0040 offset: 0x71F4
@scena.Code('func_40_71F4')
def func_40_71F4():
    MapClearFlags(0x00000001)
    CameraMove(97010, 0, 95840, 0)
    FadeIn(0, 0)
    Sleep(100)

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

# id: 0x0041 offset: 0x724F
@scena.Code('func_41_724F')
def func_41_724F():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
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

# id: 0x0042 offset: 0x72AC
@scena.Code('func_42_72AC')
def func_42_72AC():
    MapClearFlags(0x00000001)
    CameraMove(97010, 0, 95840, 0)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
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

# id: 0x0043 offset: 0x7305
@scena.Code('func_43_7305')
def func_43_7305():
    OP_13(0x002A)

    Return()

# id: 0x0044 offset: 0x7309
@scena.Code('func_44_7309')
def func_44_7309():
    OP_13(0x0026)

    Return()

# id: 0x0045 offset: 0x730D
@scena.Code('func_45_730D')
def func_45_730D():
    OP_13(0x0025)

    Return()

# id: 0x0046 offset: 0x7311
@scena.Code('func_46_7311')
def func_46_7311():
    OP_13(0x0020)

    Return()

# id: 0x0047 offset: 0x7315
@scena.Code('func_47_7315')
def func_47_7315():
    OP_13(0x0028)

    Return()

# id: 0x0048 offset: 0x7319
@scena.Code('func_48_7319')
def func_48_7319():
    OP_13(0x002B)

    Return()

# id: 0x0049 offset: 0x731D
@scena.Code('func_49_731D')
def func_49_731D():
    OP_13(0x0021)

    Return()

# id: 0x004A offset: 0x7321
@scena.Code('func_4A_7321')
def func_4A_7321():
    OP_13(0x0027)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
