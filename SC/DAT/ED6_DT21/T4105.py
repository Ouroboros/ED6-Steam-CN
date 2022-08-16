import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4105   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4105.x'
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
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
    ]

# id: 0x10001 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '菲丝',
            x                   = 58770,
            z                   = 250,
            y                   = 137000,
            direction           = 281,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '卡鲁尼洛',
            x                   = 83950,
            z                   = 1500,
            y                   = 142840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '蒂法露',
            x                   = 82520,
            z                   = 1500,
            y                   = 142760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '修理员佩顿',
            x                   = 72500,
            z                   = -10000,
            y                   = 163540,
            direction           = 76,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 68650,
            z                   = 250,
            y                   = 147890,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 55860,
            z                   = 250,
            y                   = 134560,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 54740,
            z                   = 250,
            y                   = 134560,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '基蒂',
            x                   = 56060,
            z                   = 250,
            y                   = 145340,
            direction           = 169,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '尼莫',
            x                   = 64980,
            z                   = 250,
            y                   = 147870,
            direction           = 92,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '卡拉莉丝',
            x                   = 66300,
            z                   = 250,
            y                   = 147820,
            direction           = 253,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '村中的老年男性',
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
            name                = '村中的老年女性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '村中的中年男性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '村中的中年女性',
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
            name                = '村中的青年男性',
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
            name                = '村中的青年女性',
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
            name                = '飞船乘客',
            x                   = 53780,
            z                   = 250,
            y                   = 136340,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 62390,
            z                   = 0,
            y                   = 144850,
            direction           = 246,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 60950,
            z                   = 0,
            y                   = 143420,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 53110,
            z                   = 250,
            y                   = 145310,
            direction           = 322,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 62500,
            z                   = -3000,
            y                   = 170810,
            direction           = 101,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 57230,
            z                   = 250,
            y                   = 138300,
            direction           = 134,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 66300,
            z                   = 250,
            y                   = 147820,
            direction           = 253,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '飞船乘客',
            x                   = 64980,
            z                   = 250,
            y                   = 147870,
            direction           = 92,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '提妲',
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
            name                = '金',
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
            name                = '穆拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '格雷特纳号的影子',
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
            name                = '格雷特纳号',
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
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '地名用假人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·东街区',
            x                   = 51050,
            z                   = 0,
            y                   = 83440,
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

# id: 0x10002 offset: 0x6A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x6A2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 48500,
            y           = -200,
            z           = 94500,
            range       = 53500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00017318,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000027,
        ),
    )

# id: 0x10004 offset: 0x6C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 56800,
            triggerZ            = 250,
            triggerY            = 136940,
            triggerRange        = 800,
            actorX              = 58770,
            actorZ              = 1750,
            actorY              = 137000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53710,
            triggerZ            = 250,
            triggerY            = 137720,
            triggerRange        = 800,
            actorX              = 53710,
            actorZ              = 2450,
            actorY              = 137720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71160,
            triggerZ            = -10000,
            triggerY            = 151550,
            triggerRange        = 800,
            actorX              = 71160,
            actorZ              = -8500,
            actorY              = 151550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x72E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_75B',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x0009, 0x0010)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)

    Jump('loc_806')

    def _loc_75B(): pass

    label('loc_75B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 2, 0x1202)),
            Expr.Return,
        ),
        'loc_7DC',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetFlags(0x0011, 0x0010)
    ChrSetFlags(0x0019, 0x0010)
    ChrSetFlags(0x001A, 0x0010)
    ChrSetFlags(0x001C, 0x0010)
    ChrSetPos(0x0009, 61450, -3000, 162010, 6)
    ChrSetPos(0x000A, 61450, -3000, 163810, 180)

    Jump('loc_806')

    def _loc_7DC(): pass

    label('loc_7DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7F8',
    )

    MapClearFlags(0x00000010)
    MapSetFlags(0x10000000)
    Event(0, func_26_3E9C)

    Jump('loc_806')

    def _loc_7F8(): pass

    label('loc_7F8')

    MapClearFlags(0x00000010)
    MapSetFlags(0x10000000)
    Event(0, func_21_3460)

    def _loc_806(): pass

    label('loc_806')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x811
@scena.Code('func_01_811')
def func_01_811():
    OP_16(0x02, 4000, -43000, 29000, 2293855)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_836',
    )

    OP_B1('T4105_1')

    Jump('loc_869')

    def _loc_836(): pass

    label('loc_836')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 4, 0x1204)),
            Expr.Return,
        ),
        'loc_849',
    )

    OP_B1('T4105_2')

    Jump('loc_869')

    def _loc_849(): pass

    label('loc_849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_860',
    )

    OP_B1('T4105_1')

    Jump('loc_869')

    def _loc_860(): pass

    label('loc_860')

    OP_B1('T4105_3')

    def _loc_869(): pass

    label('loc_869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 3, 0x1683)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_882',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_882(): pass

    label('loc_882')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_89B',
    )

    OP_71(0x0005, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)

    Jump('loc_8B1')

    def _loc_89B(): pass

    label('loc_89B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 2, 0x1202)),
            Expr.Return,
        ),
        'loc_8B1',
    )

    OP_71(0x0005, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)

    def _loc_8B1(): pass

    label('loc_8B1')

    OP_E5(0x0B, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8CF',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8D9')

    def _loc_8CF(): pass

    label('loc_8CF')

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8D9(): pass

    label('loc_8D9')

    Return()

# id: 0x0002 offset: 0x8DA
@scena.Code('func_02_8DA')
def func_02_8DA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8EF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_8DA')

    def _loc_8EF(): pass

    label('loc_8EF')

    Return()

# id: 0x0003 offset: 0x8F0
@scena.Code('func_03_8F0')
def func_03_8F0():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x8F5
@scena.Code('func_04_8F5')
def func_04_8F5():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_906',
    )

    Call(0, 0x0016)

    Jump('loc_1112')

    def _loc_906(): pass

    label('loc_906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_922',
    )

    ChrTalk(
        0x0008,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1112')

    def _loc_922(): pass

    label('loc_922')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 4, 0x1204)),
            Expr.Return,
        ),
        'loc_10E7',
    )

    EventBegin(0x00)
    Fade(1000)
    MapClearFlags(0x00000001)
    CameraMove(57940, 250, 137110, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 56920, 250, 136300, 85)
    ChrSetPos(0x00F7, 56810, 250, 137100, 79)
    ChrTurnDirection(0x0008, 0x00F7, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2790200563V欢迎光临。\n',
            '要搭乘定期船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790200564V搭乘时需要\n',
            '办理登船手续，\n',
            '所以到时请把票给我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A90',
    )

    ChrTurnDirection(0x0106, 0x0101, 500)
    ChrTurnDirection(0x0101, 0x0106, 500)

    ChrTalk(
        0x0106,
        (
            '#0050200565V#050F#5P如果办好了手续，那在船到之前\n',
            '在这里等着就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200566V不需要买什么东西了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF9')

    def _loc_A90(): pass

    label('loc_A90')

    ChrTurnDirection(0x0103, 0x0101, 500)
    ChrTurnDirection(0x0101, 0x0103, 500)

    ChrTalk(
        0x0103,
        (
            '#0030200567V#020F#5P办完手续后可以\n',
            '在这里等船来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200568V不需要买什么东西了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF9(): pass

    label('loc_AF9')

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
            TXT(0x00, '【还有点事】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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
    OP_0D()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B5F'),
        (0x00000001, 'loc_BBD'),
        (-1, 'loc_10E4'),
    )

    def _loc_B5F(): pass

    label('loc_B5F')

    ChrTurnDirection(0x00F7, 0x0008, 500)
    ChrSetDirection(0x0101, 85, 500)

    ChrTalk(
        0x0008,
        (
            '#2790200569V明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790200570V那么，在需要搭乘时\n',
            '请再来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_10E4')

    def _loc_BBD(): pass

    label('loc_BBD')

    ChrTurnDirection(0x00F7, 0x0008, 500)
    ChrSetDirection(0x0101, 85, 500)

    ChrTalk(
        0x0008,
        (
            '#2790200569V明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790200572V那么请在这张单子上\n',
            '签个字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200573V#1011F啊，好的好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C72',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200574V#6P#053F…………（刷刷写字声）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA2')

    def _loc_C72(): pass

    label('loc_C72')

    ChrTalk(
        0x0103,
        (
            '#0030200575V#6P#027F呼呼哼哼⊙(刷刷写字声)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA2(): pass

    label('loc_CA2')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人办完了乘船手续。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    RemoveItem(ItemTable['船票'], 2)

    ChrTalk(
        0x0008,
        (
            '#2790200576V好，可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790200577V那么在定期船到达之前\n',
            '请在飞船坪内等候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200578V#1000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x00F7, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_DC0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200579V#051F#5P那么在船到来之前\n',
            '到长椅上坐会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF9')

    def _loc_DC0(): pass

    label('loc_DC0')

    ChrTalk(
        0x0103,
        (
            '#0030200580V#021F#5P那么我们就坐在\n',
            '长椅上等船来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF9(): pass

    label('loc_DF9')

    OP_DB()
    FadeOut(2000, 0, -1)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    OP_0D()
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_71(0x0009, 0x0004)
    MapClearFlags(0x00000010)
    PlaySE(226, 0x00, 0x64)
    PlaySE(117, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    MapClearFlags(0x00000010)
    Yield()
    OP_89(0x0101, 83040, 1500, 143200, 4)
    OP_89(0x00F7, 83180, 1700, 141880, 192)
    CameraMove(83210, 1700, 140260, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0EB0')
    def lambda_0EB0():
        ChrWalkTo(0x00F7, 82620, 1500, 133740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0EB0)

    @scena.Lambda('lambda_0ECB')
    def lambda_0ECB():
        ChrWalkTo(0x0101, 82620, 1500, 133740, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0ECB)

    @scena.Lambda('lambda_0EE6')
    def lambda_0EE6():
        CameraMove(82850, 1700, 135080, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EE6)

    Sleep(4000)

    MapClearFlags(0x00000001)
    Fade(1000)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x00F7, 0x0008)
    CameraMove(87540, 1500, 134660, 0)
    OP_67(0, 12280, -10000, 0)
    CameraSetDistance(6180, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0028, 0x0004)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0029, 0x0004)
    ChrSetFlags(0x0029, 0x0040)
    OP_A1(0x0028, 0x000B)
    OP_A1(0x0029, 0x000A)
    OP_72(0x000B, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x0009, 0x0004)
    ChrSetPos(0x0028, 87000, -5300, 131150, 90)
    ChrSetPos(0x0029, 87000, -5300, 131150, 90)
    Yield()
    OP_0D()
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 100)
    Sleep(3000)

    OP_6F(0x000A, 2)
    OP_70(0x000A, 100)
    PlaySE(118, 0x00, 0x64)
    OP_73(0x000A)
    OP_23(0x0075)
    PlaySE(119, 0x00, 0x64)
    OP_6F(0x000A, 100)
    OP_6F(0x000B, 100)
    OP_70(0x000A, 200)
    OP_70(0x000B, 200)
    OP_73(0x000B)
    OP_6F(0x000A, 200)
    OP_6F(0x000B, 200)
    OP_70(0x000A, 300)
    OP_70(0x000B, 300)

    @scena.Lambda('lambda_1016')
    def lambda_1016():
        ChrMoveTo(0x00FE, 100000, 500, 131110, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_1016)

    @scena.Lambda('lambda_1031')
    def lambda_1031():
        ChrMoveTo(0x00FE, 100000, 500, 131110, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_1031)

    WaitForThreadExit(0x0029, 0x0001)
    Fade(1000)
    CameraMove(108820, 1500, 134250, 0)
    OP_67(0, 9790, -10000, 0)
    CameraSetDistance(7800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_1093')
    def lambda_1093():
        ChrMoveTo(0x00FE, 148750, 1500, 131110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0003, lambda_1093)

    @scena.Lambda('lambda_10AE')
    def lambda_10AE():
        ChrMoveTo(0x00FE, 148750, 1500, 131110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0003, lambda_10AE)

    Sleep(4000)

    FadeOut(2000, 0, -1)
    WaitForThreadExit(0x0029, 0x0003)
    OP_DC()
    NewScene('ED6_DT21/E0000._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_10E4')

    def _loc_10E4(): pass

    label('loc_10E4')

    Jump('loc_1112')

    def _loc_10E7(): pass

    label('loc_10E7')

    ChrTalk(
        0x0008,
        (
            '需要购买船票的客人请去\n',
            '那边的建筑物～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1112(): pass

    label('loc_1112')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1116
@scena.Code('func_05_1116')
def func_05_1116():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1181',
    )

    ChrTalk(
        0x00FE,
        (
            '唔、嗯……\n',
            '机械部分无任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力压的调整也完成了……\n',
            '这、这下，全部都结束了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A6')

    def _loc_1181(): pass

    label('loc_1181')

    ChrTalk(
        0x00FE,
        (
            '唔、嗯……\n',
            '……下一班定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A6(): pass

    label('loc_11A6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x11AA
@scena.Code('func_06_11AA')
def func_06_11AA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1225',
    )

    ChrTalk(
        0x00FE,
        (
            '最后的总检查\n',
            '是维修主任您的工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，不要对我这么客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '为什么每次都变成这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1270')

    def _loc_1225(): pass

    label('loc_1225')

    ChrTalk(
        0x00FE,
        (
            '真让人着急……\n',
            '赛希莉亚号刚刚才飞走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来是林德号、林德号！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1270(): pass

    label('loc_1270')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1274
@scena.Code('func_07_1274')
def func_07_1274():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_133B',
    )

    ChrTalk(
        0x00FE,
        (
            '不得了不得了，\n',
            '新引擎的性能真令人吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过看来还需要不断通过\n',
            '飞行实验来收集数据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要最大限度地发挥动力\n',
            '就必须考虑机体的协调性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想过一阵就\n',
            '去请教请教拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1369')

    def _loc_133B(): pass

    label('loc_133B')

    ChrTalk(
        0x00FE,
        (
            '快了，快了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要新型引擎完成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1369(): pass

    label('loc_1369')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x136D
@scena.Code('func_08_136D')
def func_08_136D():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1374
@scena.Code('func_09_1374')
def func_09_1374():
    UnlockAchievement(0x01, 0x000D, 0x00)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_13C9',
    )

    ChrTalk(
        0x00FE,
        (
            '果然男人还是要\n',
            '自己来开拓道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以呢，\n',
            '该是旅行的时候了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C9(): pass

    label('loc_13C9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x13CD
@scena.Code('func_0A_13CD')
def func_0A_13CD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1400',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈，和安敦在一起\n',
            '真不会感到无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1400(): pass

    label('loc_1400')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1404
@scena.Code('func_0B_1404')
def func_0B_1404():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1454',
    )

    ChrTalk(
        0x00FE,
        (
            '我终于找到了\n',
            '自己想做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以为了学习，\n',
            '我准备去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1454(): pass

    label('loc_1454')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1458
@scena.Code('func_0C_1458')
def func_0C_1458():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呵呵，你要\n',
            '好好看家哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x147C
@scena.Code('func_0D_147C')
def func_0D_147C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '妈妈，你放心吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1499
@scena.Code('func_0E_1499')
def func_0E_1499():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我是第一次一个人\n',
            '坐飞船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什、什么啊，\n',
            '我可没有紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x14E2
@scena.Code('func_0F_14E2')
def func_0F_14E2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '爷～爷，我\n',
            '想坐那～边的飞～船！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x150E
@scena.Code('func_10_150E')
def func_10_150E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '听、听话，那可是\n',
            '女王陛下的飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能乘坐的话，\n',
            '我倒也想坐坐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1561
@scena.Code('func_11_1561')
def func_11_1561():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 3, 0x1203)),
            Expr.Return,
        ),
        'loc_15B9',
    )

    ChrTalk(
        0x00FE,
        (
            '怎、怎么了……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才出来的那两个人\n',
            '表情恐怖的互相瞪着对方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15F8')

    def _loc_15B9(): pass

    label('loc_15B9')

    ChrTalk(
        0x00FE,
        (
            '呼……这就是\n',
            '飞船公社的总公司啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相当不错的建筑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15F8(): pass

    label('loc_15F8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x15FC
@scena.Code('func_12_15FC')
def func_12_15FC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哟，这就是埃尔赛尤啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好漂亮的飞船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1635
@scena.Code('func_13_1635')
def func_13_1635():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '搭下一班飞船\n',
            '几点能到蔡斯呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x165F
@scena.Code('func_14_165F')
def func_14_165F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '听着，你\n',
            '一定要乖乖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x1683
@scena.Code('func_15_1683')
def func_15_1683():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯，一言为定～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x16A0
@scena.Code('func_16_16A0')
def func_16_16A0():
    EventBegin(0x00)

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16CA',
    )

    Call(0, 0x0028)
    Call(0, 0x002A)
    FadeIn(0, 0)

    def _loc_16CA(): pass

    label('loc_16CA')

    Fade(1000)
    CameraMove(57660, 250, 137100, 0)
    OP_67(0, 8420, -10000, 0)
    CameraSetDistance(2690, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 56940, 250, 136330, 90)
    ChrSetPos(0x00F7, 56900, 250, 137490, 90)
    ChrSetPos(0x00F8, 55560, 250, 135910, 90)
    ChrSetPos(0x00F9, 55480, 250, 137370, 90)
    ChrSetDirection(0x0008, 276, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 6, 0x163E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C6',
    )

    SetScenaFlags(ScenaFlag(0x02C7, 6, 0x163E))

    ChrTalk(
        0x0008,
        (
            '#2790271202V欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790271203V你们是去柏斯的\n',
            '游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271204V#1011F啊，嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790271205V艾南先生已经\n',
            '替你们付过旅费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2790271206V要办理搭乘手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 180, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18B2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050271207V#050F#5P如果办好了手续，那在船到之前\n',
            '在这里等着就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271208V我们已经在格兰赛尔\n',
            '没有事留下了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1930')

    def _loc_18B2(): pass

    label('loc_18B2')

    ChrTalk(
        0x0103,
        (
            '#0030271209V#020F#5P如果办好了手续，那在船到之前\n',
            '在这里等着就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271210V在格兰赛尔\n',
            '已经没有什么还需要做的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1930(): pass

    label('loc_1930')

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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19C3',
    )

    ChrTalk(
        0x0008,
        (
            '#2790271211V那么请在方便的时候\n',
            '再来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_19C3(): pass

    label('loc_19C3')

    Jump('loc_1A86')

    def _loc_19C6(): pass

    label('loc_19C6')

    ChrTalk(
        0x0008,
        (
            '#2790271212V哎呀……\n',
            '要办理搭乘手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A86',
    )

    ChrTalk(
        0x0008,
        (
            '#2790271211V那么请在方便的时候\n',
            '再来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_1A86(): pass

    label('loc_1A86')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B36',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    EventBegin(0x00)
    CameraMove(56610, 250, 137000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 56610, 250, 137000, 90)
    ChrSetPos(0x0001, 56610, 250, 137000, 90)
    ChrSetPos(0x0002, 56610, 250, 137000, 90)
    ChrSetPos(0x0003, 56610, 250, 137000, 90)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_1B36(): pass

    label('loc_1B36')

    OP_E9(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xCA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BE6',
    )

    ExecExpressionWithVar(
        0xCA,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    EventBegin(0x00)
    CameraMove(56610, 250, 137000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 56610, 250, 137000, 90)
    ChrSetPos(0x0001, 56610, 250, 137000, 90)
    ChrSetPos(0x0002, 56610, 250, 137000, 90)
    ChrSetPos(0x0003, 56610, 250, 137000, 90)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_1BE6(): pass

    label('loc_1BE6')

    ChrTalk(
        0x0008,
        (
            '#2790200569V明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#2790271215V那么，我和协会联系一下，\n',
            '请其他人也来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行人办理完乘船手续之后\n',
            '就在原地等待飞船起飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    Call(0, 0x001F)
    CameraMove(87590, 1500, 142760, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 91000, 1500, 143280, 270)
    ChrSetPos(0x0103, 91860, 1500, 142720, 270)
    ChrSetPos(0x0106, 91910, 1500, 143800, 270)
    ChrSetPos(0x0105, 93140, 1500, 142720, 270)
    ChrSetPos(0x0107, 92990, 1500, 143800, 270)
    ChrSetPos(0x0108, 94220, 1500, 142720, 270)
    ChrSetPos(0x0104, 94240, 1500, 143800, 270)
    ChrSetPos(0x0012, 82860, 1500, 143460, 180)
    ChrSetPos(0x0013, 84050, 1500, 143590, 270)
    ChrSetPos(0x0014, 86810, 1500, 143690, 270)
    ChrSetPos(0x0015, 88180, 1500, 143410, 270)
    ChrSetPos(0x0016, 85280, 1500, 143380, 270)
    ChrSetPos(0x0017, 89440, 1500, 143050, 270)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_6F(0x000A, 60)
    OP_6F(0x0005, 100)
    PlaySE(226, 0x00, 0x64)
    PlaySE(117, 0x01, 0x5A)
    Sleep(3000)

    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    Sleep(1000)

    OP_71(0x0009, 0x0004)
    FadeIn(2000, 0)
    OP_0D()
    PlaySE(118, 0x00, 0x46)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 1)
    Sleep(1500)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 200)
    OP_73(0x0005)
    CreateThread(0x0012, 0x01, 0x00, func_17_305E)
    Sleep(500)

    CreateThread(0x0013, 0x01, 0x00, func_17_305E)
    Sleep(800)

    CreateThread(0x0016, 0x01, 0x00, func_17_305E)
    Sleep(600)

    CreateThread(0x0014, 0x01, 0x00, func_17_305E)
    Sleep(100)

    CreateThread(0x0015, 0x01, 0x00, func_17_305E)
    Sleep(500)

    CreateThread(0x0017, 0x01, 0x00, func_17_305E)
    Sleep(500)

    @scena.Lambda('lambda_1ECF')
    def lambda_1ECF():
        ChrWalkTo(0x00FE, 83300, 1500, 143280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ECF)

    Sleep(500)

    @scena.Lambda('lambda_1EEF')
    def lambda_1EEF():
        CameraMove(83300, 1500, 143110, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EEF)

    @scena.Lambda('lambda_1F07')
    def lambda_1F07():
        ChrWalkTo(0x00FE, 85140, 1500, 142720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1F07)

    Sleep(200)

    @scena.Lambda('lambda_1F27')
    def lambda_1F27():
        ChrWalkTo(0x00FE, 85230, 1500, 143800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1F27)

    Sleep(100)

    @scena.Lambda('lambda_1F47')
    def lambda_1F47():
        ChrWalkTo(0x00FE, 86240, 1500, 143800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1F47)

    Sleep(100)

    @scena.Lambda('lambda_1F67')
    def lambda_1F67():
        ChrWalkTo(0x00FE, 86290, 1500, 142720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1F67)

    Sleep(100)

    @scena.Lambda('lambda_1F87')
    def lambda_1F87():
        ChrWalkTo(0x00FE, 87410, 1500, 143800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_1F87)

    Sleep(100)

    @scena.Lambda('lambda_1FA7')
    def lambda_1FA7():
        ChrWalkTo(0x00FE, 87450, 1500, 142720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1FA7)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 180, 400)
    ChrSetPos(0x0026, 73360, 1500, 142950, 90)
    ChrSetPos(0x0027, 73360, 1500, 143830, 90)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)

    NpcTalk(
        0x0026,
        '男人的声音',
        (
            '#0270271216V#1P赶上了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_20F3')
    def lambda_20F3():
        CameraMove(81000, 1500, 142960, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20F3)

    @scena.Lambda('lambda_210B')
    def lambda_210B():
        OP_67(0, 7210, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_210B)

    @scena.Lambda('lambda_2123')
    def lambda_2123():
        OP_6C(225000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2123)

    @scena.Lambda('lambda_2133')
    def lambda_2133():
        CameraSetDistance(2270, 3000)

        ExitThread()

    DispatchAsync(0x0026, 0x0002, lambda_2133)

    @scena.Lambda('lambda_2143')
    def lambda_2143():
        OP_6E(362, 3000)

        ExitThread()

    DispatchAsync(0x0026, 0x0003, lambda_2143)

    @scena.Lambda('lambda_2153')
    def lambda_2153():
        ChrWalkTo(0x00FE, 79350, 1500, 142950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_2153)

    Sleep(500)

    @scena.Lambda('lambda_2173')
    def lambda_2173():
        ChrWalkTo(0x00FE, 78820, 1500, 143830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_2173)

    WaitForThreadExit(0x0026, 0x0001)
    WaitForThreadExit(0x0026, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010271217V#1004F#6P咦，奈尔……\n',
            '朵洛希也在？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0280271218V#154F#4P小艾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0270271219V#145F#5P呼～我去了协会，\n',
            '听说已经出发了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271220V#140F我就急着追来了，\n',
            '还好赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271221V#1015F#6P咦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271222V关于昨晚的事件\n',
            '我们应该聊过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0270271223V#142F#5P不……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0026, 135, 400)
    Sleep(500)

    ChrTurnDirection(0x0026, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0026,
        (
            '#0270271224V#140F#5P我有点私人的事情\n',
            '要跟你说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271225V起飞之前\n',
            '能跟我们待一会儿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271226V#1004F#6P我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010271227V#1015F#5P那么，雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030271228V#027F没关系。\n',
            '你们聊吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271229V我们就先进去\n',
            '帮你找座位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271230V#1006F#5P嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060271231V#040F#5P祝你们愉快。\n',
            '奈尔先生，朵洛希小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070271232V#061F#5P再见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2474')
    def lambda_2474():
        ChrWalkTo(0x00FE, 81230, 1500, 143280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2474)

    @scena.Lambda('lambda_248F')
    def lambda_248F():
        CameraMove(79800, 1500, 143330, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_248F)

    @scena.Lambda('lambda_24A7')
    def lambda_24A7():
        CameraSetDistance(2100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_24A7)

    CreateThread(0x0103, 0x01, 0x00, func_18_30A5)
    Sleep(800)

    CreateThread(0x0106, 0x01, 0x00, func_19_30EC)
    Sleep(300)

    CreateThread(0x0107, 0x01, 0x00, func_1A_3133)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_1B_317A)
    Sleep(300)

    CreateThread(0x0108, 0x01, 0x00, func_1C_31C1)
    Sleep(500)

    CreateThread(0x0104, 0x01, 0x00, func_1D_3208)
    Sleep(4000)

    ChrTalk(
        0x0101,
        (
            '#0010271233V#1011F#6P没太多时间了，\n',
            '有什么话赶紧说吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271234V#1019F#5P咦，奥利维尔为什么\n',
            '还留在这里不走？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040271235V#035F呵呵，你就把我\n',
            '当作路边的\n',
            '小石子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040271236V#030F好了，快开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271237V#1007F#5P这个男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0270271238V#142F真是颗自说自话的\n',
            '小石子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0103, 0x0080)
    ChrSetPos(0x0103, 83210, 1500, 134330, 0)
    ChrWalkTo(0x0103, 82860, 1700, 141440, 4000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#0030271239V#027F#5P我还在想怎么突然找不到你了，\n',
            '果然在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0103, 0x0104, 500, 3000, 0x00)

    ChrTalk(
        0x0104,
        (
            '#0040271240V#036F等、等等，雪拉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030271241V#021F#5P好了好了，我们\n',
            '快去自己的座位吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 180, 400)

    @scena.Lambda('lambda_273D')
    def lambda_273D():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_273D')

    DispatchAsync2(0x0101, 0x0001, lambda_273D)

    @scena.Lambda('lambda_274E')
    def lambda_274E():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_274E')

    DispatchAsync2(0x0026, 0x0001, lambda_274E)

    @scena.Lambda('lambda_275F')
    def lambda_275F():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_275F')

    DispatchAsync2(0x0027, 0x0001, lambda_275F)

    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    @scena.Lambda('lambda_2782')
    def lambda_2782():
        ChrWalkTo(0x00FE, 82860, 1500, 130550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2782)

    Sleep(100)

    @scena.Lambda('lambda_27A2')
    def lambda_27A2():
        ChrSetDirection(0x0104, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_27A2)

    @scena.Lambda('lambda_27B0')
    def lambda_27B0():
        ChrMoveTo(0x00FE, 82860, 1500, 130550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_27B0)

    ChrSetFlags(0x0104, 0x0020)
    ChrSetFlags(0x0104, 0x0002)
    ChrSetChipByIndex(0x0104, 20)
    ChrSetSubChip(0x0104, 5)
    CameraMove(80980, 1500, 139850, 2000)
    WaitForThreadExit(0x0103, 0x0001)
    ChrSetFlags(0x0103, 0x0080)
    WaitForThreadExit(0x0104, 0x0001)
    ChrSetFlags(0x0104, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0026, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0026, 0x01)
    TerminateThread(0x0027, 0x01)
    CameraMove(79960, 1500, 143070, 1500)
    ChrTurnDirection(0x0026, 0x0101, 400)

    ChrTalk(
        0x0026,
        (
            '#0270271242V#142F#5P怎么说呢，\n',
            '那位老兄还真是一成不变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0026, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271243V#1016F#6P哈哈，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0280271244V#154F#4P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0027, 400)

    ChrTalk(
        0x0101,
        (
            '#0010271245V#1015F#6P朵洛希。\n',
            '你好像无精打采的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271246V我记得你去柏斯\n',
            '地区采访了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0027, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0027,
        (
            '#0280271247V#154F嗯、嗯……\n',
            '是今早回来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280271248V我、我说～小艾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271249V#1006F#6P啊，我想起来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271250V我记得你们去了\n',
            '迷雾峡谷的空贼老巢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271251V听说那里现在是军队的\n',
            '飞行训练基地……',
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
            '#0010271252V#1004F#6P咦，这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0270271253V#140F#5P你终于注意到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271254V那就是昨晚被空贼团的\n',
            '余党袭击的基地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271255V空贼艇被夺时\n',
            '这家伙正好在场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271256V#1002F#6P这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271257V#1011F那你们是特地\n',
            '来提供消息的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271258V#1001F嘿嘿，你还挺聪明的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0270271259V#145F#5P嗯，虽然确实可以\n',
            '说是提供消息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271260V#1004F#6P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0026,
        (
            '#0270271261V#142F#5P算了。\n',
            '朵洛希，把东西拿出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0280271262V#154F好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    ChrWalkTo(0x0027, 80490, 1500, 143290, 1500, 0x00)
    Sleep(500)

    ChrTalk(
        0x0027,
        (
            '#0280271263V#155F#2P我说啊～小艾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280271264V你可别太\n',
            '往坏处想哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280271265V照片是不一定会\n',
            '反映所有的真实情况的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271266V#1008F#6P怎、怎么了啊？\n',
            '表情这么凝重……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#0280271267V#154F#2P这……\n',
            '就是我昨天拍的照片～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 21)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔从朵洛希那里拿到一张照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['约修亚的照片'], 1)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_AD('ED6_DT24/C_VIS122._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    SetMessageWindowPos(100, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010271268V#1015F#6P这是……\n',
            '空贼艇和那个男人婆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271269V那么，这边的人是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190016V………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010271271V#1004F#3S咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetPos(0x0027, 79680, 1500, 144000, 90)
    OP_AE(0x000001F4)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0026,
        (
            '#0270271272V#142F#5P……现在我们还不准备\n',
            '将这张照片提供给王国军。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271273V当然也不会刊登。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270271274V应该怎么做\n',
            '由你来判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0026, 0x03, 0x00, func_1E_3224)
    FadeOut(2000, 0, -1)
    OP_0D()
    Call(0, 0x0020)
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS153._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_28(0x00A9, 0x04, 0x40)
    OP_28(0x00AA, 0x04, 0x40)
    OP_28(0x00AB, 0x04, 0x40)
    OP_28(0x00AC, 0x04, 0x40)
    SetScenaFlags(ScenaFlag(0x02D0, 3, 0x1683))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x125),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x10, 0x0000, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3025',
    )

    ShowSaveMenu()

    def _loc_3025(): pass

    label('loc_3025')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    ClearScenaFlags(ScenaFlag(0x02D0, 3, 0x1683))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x02D0, 3, 0x1683))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x305E
@scena.Code('func_17_305E')
def func_17_305E():
    ChrWalkTo(0x00FE, 82860, 1500, 143460, 2000, 0x00)
    ChrWalkTo(0x00FE, 82860, 1500, 133740, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 82860, 1500, 130550, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0018 offset: 0x30A5
@scena.Code('func_18_30A5')
def func_18_30A5():
    ChrWalkTo(0x00FE, 82860, 1500, 143460, 2000, 0x00)
    ChrWalkTo(0x00FE, 82860, 1500, 133740, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 82860, 1500, 130550, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0019 offset: 0x30EC
@scena.Code('func_19_30EC')
def func_19_30EC():
    ChrWalkTo(0x00FE, 82860, 1500, 143460, 2000, 0x00)
    ChrWalkTo(0x00FE, 82860, 1500, 133740, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 82860, 1500, 130550, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001A offset: 0x3133
@scena.Code('func_1A_3133')
def func_1A_3133():
    ChrWalkTo(0x00FE, 82860, 1500, 143460, 2000, 0x00)
    ChrWalkTo(0x00FE, 82860, 1500, 133740, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 82860, 1500, 130550, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x317A
@scena.Code('func_1B_317A')
def func_1B_317A():
    ChrWalkTo(0x00FE, 82860, 1500, 143460, 2000, 0x00)
    ChrWalkTo(0x00FE, 82860, 1500, 133740, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 82860, 1500, 130550, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0x31C1
@scena.Code('func_1C_31C1')
def func_1C_31C1():
    ChrWalkTo(0x00FE, 82860, 1500, 143460, 2000, 0x00)
    ChrWalkTo(0x00FE, 82860, 1500, 133740, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, 82860, 1500, 130550, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001D offset: 0x3208
@scena.Code('func_1D_3208')
def func_1D_3208():
    ChrWalkTo(0x00FE, 82930, 1500, 144220, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001E offset: 0x3224
@scena.Code('func_1E_3224')
def func_1E_3224():
    Sleep(600)

    OP_24(0x0075, 0x50)
    Sleep(300)

    OP_24(0x0075, 0x46)
    Sleep(300)

    OP_24(0x0075, 0x3C)
    Sleep(300)

    OP_24(0x0075, 0x32)
    Sleep(300)

    OP_24(0x0075, 0x28)
    Sleep(300)

    OP_24(0x0075, 0x1E)
    Sleep(300)

    OP_24(0x0075, 0x14)
    Sleep(300)

    OP_23(0x0075)

    Return()

# id: 0x001F offset: 0x326C
@scena.Code('func_1F_326C')
def func_1F_326C():
    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
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

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_32A5',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_32A5(): pass

    label('loc_32A5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_32CA',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_32CA(): pass

    label('loc_32CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3317',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32FF',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_3317')

    def _loc_32FF(): pass

    label('loc_32FF')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_3317(): pass

    label('loc_3317')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_338C',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_334C',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_338C')

    def _loc_334C(): pass

    label('loc_334C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3374',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_338C')

    def _loc_3374(): pass

    label('loc_3374')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_338C(): pass

    label('loc_338C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_33D9',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C1',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_33D9')

    def _loc_33C1(): pass

    label('loc_33C1')

    FormationAddMember(ChrTable['科洛丝'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_33D9(): pass

    label('loc_33D9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_33FE',
    )

    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_33FE(): pass

    label('loc_33FE')

    Return()

# id: 0x0020 offset: 0x33FF
@scena.Code('func_20_33FF')
def func_20_33FF():
    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_340F',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_340F(): pass

    label('loc_340F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_341F',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_341F(): pass

    label('loc_341F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_342F',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_342F(): pass

    label('loc_342F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_343F',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_343F(): pass

    label('loc_343F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_344F',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_344F(): pass

    label('loc_344F')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_345F',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_345F(): pass

    label('loc_345F')

    Return()

# id: 0x0021 offset: 0x3460
@scena.Code('func_21_3460')
def func_21_3460():
    MapClearFlags(0x00000001)
    MapClearFlags(0x00000080)
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_DB()
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0009, 0x0004)
    MapClearFlags(0x00000010)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    CameraMove(83480, 1500, 131810, 0)
    OP_67(0, 15200, -10000, 0)
    CameraSetDistance(7000, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    OP_6F(0x0005, 100)
    OP_6F(0x000A, 410)
    ChrSetFlags(0x0028, 0x0004)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0029, 0x0004)
    ChrSetFlags(0x0029, 0x0040)
    OP_A1(0x0028, 0x000B)
    OP_A1(0x0029, 0x000A)
    OP_72(0x000B, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_6F(0x000A, 390)
    OP_70(0x000A, 300)
    FadeIn(3000, 0)
    ChrSetPos(0x0028, 87000, -5100, 130500, 90)
    ChrSetPos(0x0029, 87000, 5500, 130500, 90)

    @scena.Lambda('lambda_3565')
    def lambda_3565():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3565)

    @scena.Lambda('lambda_3575')
    def lambda_3575():
        OP_67(0, 11200, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3575)

    @scena.Lambda('lambda_358D')
    def lambda_358D():
        CameraSetDistance(3500, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_358D)

    CreateThread(0x002D, 0x00, 0x00, func_2B_66AC)

    @scena.Lambda('lambda_35A4')
    def lambda_35A4():
        ChrMoveTo(0x00FE, 87000, -5650, 130500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0002, lambda_35A4)

    WaitForThreadExit(0x0029, 0x0002)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    Sleep(100)

    OP_72(0x000A, 0x0020)
    PlaySE(118, 0x00, 0x64)
    OP_6F(0x000A, 80)
    OP_70(0x000A, 1)
    Sleep(2700)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 0)
    Sleep(3000)

    PlaySE(6, 0x00, 0x64)
    OP_6F(0x000A, 411)
    OP_70(0x000A, 450)
    OP_73(0x000A)
    Sleep(300)

    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x010A, 0x0020)
    ChrSetBattleFlags(0x0012, 0x0020)
    ChrSetBattleFlags(0x0013, 0x0020)
    ChrSetBattleFlags(0x0014, 0x0020)
    ChrSetBattleFlags(0x0015, 0x0020)
    ChrSetBattleFlags(0x0016, 0x0020)
    Yield()
    OP_89(0x0012, 86970, 1700, 130570, 189)
    OP_89(0x0013, 89160, 1500, 133510, 189)
    OP_89(0x0014, 86970, 1700, 130570, 189)
    OP_89(0x0015, 86970, 1700, 130570, 189)
    OP_89(0x0016, 89160, 1500, 133510, 189)
    OP_89(0x0101, 86970, 1700, 130570, 189)
    OP_89(0x010A, 86970, 1700, 130570, 189)
    CreateThread(0x0012, 0x01, 0x00, func_23_3D7F)
    Sleep(1000)

    CreateThread(0x0013, 0x01, 0x00, func_22_3D2A)
    Sleep(2000)

    CreateThread(0x0014, 0x01, 0x00, func_23_3D7F)
    Sleep(1000)

    CreateThread(0x0015, 0x01, 0x00, func_23_3D7F)
    Sleep(1000)

    CreateThread(0x0016, 0x01, 0x00, func_22_3D2A)
    Sleep(2000)

    CreateThread(0x010A, 0x01, 0x00, func_24_3DE8)
    Sleep(800)

    CreateThread(0x0101, 0x01, 0x00, func_25_3E4C)
    Sleep(4000)

    Fade(1000)
    CameraMove(82440, 1500, 142990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    WaitForThreadExit(0x010A, 0x0001)
    OP_DC()
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120200058V#819F呼～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200059V在飞船上呆了大半天的，\n',
            '果真是累人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200060V#810F赶紧去向协会报到和\n',
            '汇报完成训练的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200061V#1015F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200062V#814F艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200063V#1025F#5P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200064V对了。\n',
            '还要和艾南先生打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200065V#810F那个……莫非。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200066V艾丝蒂尔你在紧张？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200067V#1007F#5P嗯、嗯，不知道为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200068V#1026F在参加训练之前\n',
            '从没这种感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200069V想到今后就要\n',
            '以正游击士的身份工作了，\n',
            '总觉得平静不下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200070V#810F是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200071V#1314F这大概……\n',
            '就是所谓的兴奋难耐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200072V#1004F#5P兴、兴奋难耐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200073V#816F艾丝蒂尔，你在这\n',
            '一个月的训练中变强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200074V不仅是力量，\n',
            '我觉得应该还包括知识、\n',
            '谨慎度和判断力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200075V#817F揭开神秘组织的阴谋、\n',
            '带回约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200076V#816F你大概是预先感知\n',
            '到了这些事的困难程度吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200077V#1004F#5P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200078V#1000F嗯。\n',
            '被你这么一说，我也觉得可能是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200079V#1007F唉……我真是个傻瓜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200080V就好像不知道自己要登的山\n',
            '有多高的登山员一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200081V#1314F你不想登了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200082V#1006F#5P当然不是！\n',
            '相反，比之前更有干劲了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200083V不管是多高的山，到头来\n',
            '还是只能一步一步向上登。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200084V#1018F就算是爬，我也要\n',
            '爬到山顶！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200085V#811F呵呵，这就对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200086V#1310F那么赶快\n',
            '回协会报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200087V#1006F#5P嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(1500, 0)
    OP_0D()
    NewScene('ED6_DT21/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0022 offset: 0x3D2A
@scena.Code('func_22_3D2A')
def func_22_3D2A():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 83000, 1700, 133170, 2000, 0x00)
    ChrSetDirection(0x00FE, 11, 1000)
    ChrWalkTo(0x00FE, 83050, 1600, 143060, 2000, 0x00)
    ChrSetDirection(0x00FE, 278, 1000)
    ChrWalkTo(0x00FE, 69850, 1600, 143060, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0023 offset: 0x3D7F
@scena.Code('func_23_3D7F')
def func_23_3D7F():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 84280, 1700, 130410, 2000, 0x00)
    ChrWalkTo(0x00FE, 82610, 1700, 132890, 2000, 0x00)
    ChrSetDirection(0x00FE, 11, 1000)
    ChrWalkTo(0x00FE, 83050, 1600, 143060, 2000, 0x00)
    ChrSetDirection(0x00FE, 278, 1000)
    ChrWalkTo(0x00FE, 69850, 1600, 143060, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0024 offset: 0x3DE8
@scena.Code('func_24_3DE8')
def func_24_3DE8():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 84250, 1600, 131020, 2000, 0x00)
    ChrWalkTo(0x00FE, 82950, 1500, 133500, 2000, 0x00)
    ChrSetDirection(0x00FE, 11, 1000)
    ChrWalkTo(0x00FE, 83050, 1600, 143060, 2000, 0x00)
    ChrWalkTo(0x00FE, 81550, 1500, 143060, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 500)

    Return()

# id: 0x0025 offset: 0x3E4C
@scena.Code('func_25_3E4C')
def func_25_3E4C():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 84000, 1600, 131020, 2000, 0x00)
    ChrWalkTo(0x00FE, 82950, 1500, 133500, 2000, 0x00)
    ChrSetDirection(0x00FE, 11, 1000)
    ChrWalkTo(0x00FE, 83050, 1600, 143060, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 500)

    Return()

# id: 0x0026 offset: 0x3E9C
@scena.Code('func_26_3E9C')
def func_26_3E9C():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    PlaySE(117, 0x00, 0x64)
    OP_71(0x0009, 0x0004)
    MapClearFlags(0x00000010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3EC8',
    )

    Call(0, 0x0028)

    def _loc_3EC8(): pass

    label('loc_3EC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3EDA',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xF8, 0xFF)

    Jump('loc_3EE2')

    def _loc_3EDA(): pass

    label('loc_3EDA')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)

    def _loc_3EE2(): pass

    label('loc_3EE2')

    CameraMove(83200, 1500, 143040, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 83490, 1700, 143700, 180)
    ChrSetPos(0x00F7, 82560, 1700, 143700, 180)
    ChrSetPos(0x00F8, 83490, 1700, 142100, 360)
    ChrSetPos(0x010A, 82560, 1700, 142100, 360)
    ChrSetPos(0x0017, 81620, 1500, 115180, 360)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x10A, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x10A, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x10A, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6C(135000, 0)
    FadeIn(2000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4489',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200257V#053F那我们就\n',
            '先行一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200258V#050F……喂，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200259V#1011F#6P嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200260V#050F有时候勉强打起精神\n',
            '也许是一种必要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200261V不过你是一个女人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200262V偶尔也应该依赖一下别人，\n',
            '吐露下自己的苦衷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200263V#1026F#6P咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200264V#1002F什、什么啊！\n',
            '因为我是女人你就瞧不起我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200265V#053F不，我没这个意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200266V#552F只不过男人是一种愚蠢的动物，\n',
            '总会不自觉地意气用事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200267V我，还有大叔都这样……\n',
            '约修亚大概也一样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200268V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200269V#051F愚蠢的意气用事，\n',
            '只有这一点死也治不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200270V所以，你作为女人，\n',
            '没必要和我们逞强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200271V有时也可以依靠一下别人，\n',
            '按照自己的方式生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200272V#1017F#6P阿加特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200273V嗯，我会记在心里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0106, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200274V#027F呵呵，想不到你也会\n',
            '说出这么体贴人的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0106, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200275V#1310F没错没错。\n',
            '我都有点吃惊了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200276V#811F想不到阿加特前辈\n',
            '也会对女孩子温柔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0103, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200277V#054F喂，你这是什么意思啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200278V#1315F哈哈，开玩笑的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0103, 400)

    @scena.Lambda('lambda_442F')
    def lambda_442F():
        ChrTurnDirection(0x0106, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_442F)

    Sleep(100)

    @scena.Lambda('lambda_4442')
    def lambda_4442():
        ChrTurnDirection(0x0103, 0x010A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4442)

    Sleep(300)

    ChrTalk(
        0x010A,
        (
            '#0120200279V#1314F……艾丝蒂尔。\n',
            '要暂时离别了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_482B')

    def _loc_4489(): pass

    label('loc_4489')

    ChrTalk(
        0x0103,
        (
            '#0030200280V#021F那我们就\n',
            '先行一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200281V#020F艾丝蒂尔……\n',
            '你难得回来一次，\n',
            '却不能多聊聊，真是遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200282V#1016F#6P嗯……我也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200283V#1011F不过爱娜小姐那边似乎也很麻烦，\n',
            '没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200284V替我向洛连特的各位问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200285V#020F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200286V艾丝蒂尔。\n',
            '我知道你已经没问题了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200287V不过还是别太着急了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200288V#1026F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200289V#026F塔罗牌显示\n',
            '你和约修亚的关系\n',
            '并没有断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200290V#020F所以啦，不必担心。\n',
            '要相信你和约修亚之间的羁绊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200291V那样的话，你就一定能找到自己的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200292V#1017F#6P嗯…明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200293V谢谢，雪拉姐。\n',
            '你的话给我很多勇气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200294V#1003F我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200295V#021F好了好了，别一副这样的表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200296V#027F你已经是正游击士了吧？\n',
            '要挺起胸膛前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200297V#1017F#6P……嗯，我知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200298V#1314F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200299V艾丝蒂尔。\n',
            '要暂时离别了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_482B(): pass

    label('loc_482B')

    ChrTalk(
        0x0101,
        (
            '#0010200300V#1017F#6P亚妮拉丝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200301V真的谢谢你陪我\n',
            '一起训练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200302V其实是雪拉姐拜托你\n',
            '陪我一起的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_48CF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200303V#023F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48EF')

    def _loc_48CF(): pass

    label('loc_48CF')

    ChrTalk(
        0x0103,
        (
            '#0030200304V#023F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48EF(): pass

    label('loc_48EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4904',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)
    ChrTurnDirection(0x0106, 0x0103, 400)

    def _loc_4904(): pass

    label('loc_4904')

    ChrTalk(
        0x010A,
        (
            '#0120200305V#1315F嘿嘿，看来是穿帮了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200306V#810F嗯，如果有个\n',
            '不太了解约修亚的人在你\n',
            '身边的话，有助于你整理情绪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200307V雪拉前辈就是这么说着拜托我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200308V#1001F#6P嘿嘿，我就知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0103, 0x010A, 800)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4A3A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200309V#024F等、等等……\n',
            '你怎么都给说出来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A75')

    def _loc_4A3A(): pass

    label('loc_4A3A')

    ChrTalk(
        0x0103,
        (
            '#0030200310V#024F#6P等、等等……\n',
            '你怎么都给说出来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A75(): pass

    label('loc_4A75')

    ChrTurnDirection(0x010A, 0x0103, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200311V#819F好了啦，这也没什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4ABE',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)
    ChrTurnDirection(0x010A, 0x0106, 400)

    def _loc_4ABE(): pass

    label('loc_4ABE')

    Sleep(400)

    ChrTalk(
        0x010A,
        (
            '#0120200312V#816F……不过，不仅如此，\n',
            '我自己也确实得到了锻炼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200313V与艾丝蒂尔一起训练\n',
            '我真是受益匪浅。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200314V#811F所以我也要谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200315V#1017F#6P亚妮拉丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200316V#1316F另、另外，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200317V我接下来要说的话\n',
            '你可能会感觉有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200318V#1011F#6P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200319V#1314F虽然我认为我们已经是朋友了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200320V不过我想让自己和艾丝蒂尔的\n',
            '关系再进一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200321V#1011F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010200322V#1004F#6P#4S哎哎！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4D0B',
    )

    ChrTurnDirection(0x0103, 0x010A, 400)

    def _loc_4D0B(): pass

    label('loc_4D0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4D4D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200323V#023F等、等等……\n',
            '你怎么突然这么说！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D88')

    def _loc_4D4D(): pass

    label('loc_4D4D')

    ChrTalk(
        0x0103,
        (
            '#0030200324V#023F#6P等、等等……\n',
            '你怎么突然这么说！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D88(): pass

    label('loc_4D88')

    ChrTurnDirection(0x010A, 0x0103, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200325V#812F前辈，请不要阻止我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200326V我可是认真的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4E43',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200327V#025F认、认真……（晕眩中）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200328V#552F#6P（真是的，在想什么啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EA4')

    def _loc_4E43(): pass

    label('loc_4E43')

    ChrTalk(
        0x0103,
        (
            '#0030200329V#025F#6P认、认真……（晕眩中）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200330V#552F（真是的，在想什么啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EA4(): pass

    label('loc_4EA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4EB5',
    )

    ChrTurnDirection(0x010A, 0x0103, 400)

    Jump('loc_4EC3')

    def _loc_4EB5(): pass

    label('loc_4EB5')

    ChrTurnDirection(0x010A, 0x0106, 400)
    ChrTurnDirection(0x0103, 0x0106, 400)

    def _loc_4EC3(): pass

    label('loc_4EC3')

    ChrTalk(
        0x010A,
        (
            '#0120200331V#1311F那个，我虽然比艾丝蒂尔\n',
            '年长两岁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200332V不过应该算是\n',
            '同辈的游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200333V#1314F而且这种事\n',
            '年龄也不是问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200334V所以……你觉得怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200335V#1008F#6P那、那个……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200336V#1013F我、我虽然很高兴，\n',
            '不过还是感觉有点那个～吃惊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200337V而且我还有约修亚，\n',
            '不管从哪方面说也都不太方便吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200338V#814F约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200339V我和艾丝蒂尔成为\n',
            '竞争对手，\n',
            '有什么不方便的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0103)
    OP_63(0x0106)

    ChrTalk(
        0x0101,
        (
            '#0010200340V#1004F#6P……………………\n',
            '…………竞争对手？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200341V#811F嗯嗯。\n',
            '#816F年龄接近、武艺相当。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200342V我想彼此要是能\n',
            '互相切磋和勉励就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200343V#1316F是不是……给你添麻烦了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200344V#1016F#6P啊、啊哈哈……\n',
            '原来是这个意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5256',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200345V#025F唉……\n',
            '还是一样地让人摸不着头脑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200346V真没想到是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52B3')

    def _loc_5256(): pass

    label('loc_5256')

    ChrTalk(
        0x0103,
        (
            '#0030200347V#025F#6P唉……\n',
            '还是一样地让人摸不着头脑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200346V真没想到是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52B3(): pass

    label('loc_52B3')

    ChrTalk(
        0x010A,
        (
            '#0120200349V#814F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200350V#1012F#6P嗯……\n',
            '不过，如果是这样的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200351V#1006F不成器的艾丝蒂尔·布莱特，\n',
            '虽然初出茅庐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200352V#1018F不过还是非常愿意\n',
            '把亚妮拉丝当作竞争对手!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200353V#811F太好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200354V#1310F总之就是看哪一方先赶上\n',
            '前辈们的竞争⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200355V#1006F#6P正合我意！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200356V我绝对不会输！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_54C9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200357V#027F呵呵……真拿你们没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200358V看来我们也\n',
            '不能松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200359V#051F#6P嘿嘿，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200360V没有比初生的牛犊\n',
            '更可怕的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_556C')

    def _loc_54C9(): pass

    label('loc_54C9')

    ChrTalk(
        0x0103,
        (
            '#0030200361V#027F#6P呵呵……真拿你们没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200358V看来我们也\n',
            '不能松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200363V#051F嘿嘿，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200360V没有比初生的牛犊\n',
            '更可怕的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_556C(): pass

    label('loc_556C')

    Sleep(500)

    PlaySE(166, 0x00, 0x64)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880200365V前往洛连特的定期飞船\n',
            '『赛希莉亚号』即将升空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0880200366V需要乘坐的旅客请立即登船。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetFlags(0x010A, 0x0040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_588C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200367V#052F哟，时间已经到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5638')
    def lambda_5638():
        CameraMove(82810, 1580, 137840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5638)

    @scena.Lambda('lambda_5650')
    def lambda_5650():
        OP_67(0, 6980, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5650)

    @scena.Lambda('lambda_5668')
    def lambda_5668():
        CameraSetDistance(3130, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5668)

    ChrSetDirection(0x0106, 180, 400)

    @scena.Lambda('lambda_567F')
    def lambda_567F():
        ChrWalkTo(0x0106, 82740, 1700, 139050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_567F)

    Sleep(500)

    ChrSetDirection(0x010A, 180, 400)

    @scena.Lambda('lambda_56A6')
    def lambda_56A6():
        ChrWalkTo(0x010A, 82830, 1500, 135070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_56A6)

    @scena.Lambda('lambda_56C1')
    def lambda_56C1():
        ChrWalkTo(0x0101, 83490, 1500, 142800, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_56C1)

    Sleep(200)

    @scena.Lambda('lambda_56E1')
    def lambda_56E1():
        ChrWalkTo(0x0103, 82560, 1500, 142800, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_56E1)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_5701')
    def lambda_5701():
        ChrWalkTo(0x0106, 83650, 1550, 133380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_5701)

    Sleep(1000)

    @scena.Lambda('lambda_5721')
    def lambda_5721():
        ChrWalkTo(0x0106, 83400, 1550, 134000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_5721)

    @scena.Lambda('lambda_573C')
    def lambda_573C():
        ChrWalkTo(0x010A, 82570, 1550, 133940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_573C)

    WaitForThreadExit(0x0106, 0x0001)
    ChrTurnDirection(0x0106, 0x0101, 500)
    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_5768')
    def lambda_5768():
        ChrWalkTo(0x010A, 82500, 1550, 133500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_5768)

    WaitForThreadExit(0x010A, 0x0001)
    ChrTurnDirection(0x010A, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050200368V#051F#6P那么再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200369V我们彼此如果有什么新动向，\n',
            '都要通过协会支部\n',
            '进行联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200370V#020F#2P嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200371V#1018F#1P再见！\n',
            '阿加特、亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200372V#811F#4P嗯！\n',
            '艾丝蒂尔你们也要保重！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B1C')

    def _loc_588C(): pass

    label('loc_588C')

    ChrTalk(
        0x0103,
        (
            '#0030200373V#023F哎呀，时间已经到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_58BF')
    def lambda_58BF():
        CameraMove(82810, 1580, 137840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58BF)

    @scena.Lambda('lambda_58D7')
    def lambda_58D7():
        OP_67(0, 6980, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_58D7)

    @scena.Lambda('lambda_58EF')
    def lambda_58EF():
        CameraSetDistance(3130, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_58EF)

    ChrSetDirection(0x0103, 180, 400)

    @scena.Lambda('lambda_5906')
    def lambda_5906():
        ChrWalkTo(0x0103, 82740, 1700, 139050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5906)

    Sleep(500)

    ChrSetDirection(0x010A, 180, 400)

    @scena.Lambda('lambda_592D')
    def lambda_592D():
        ChrWalkTo(0x010A, 82830, 1500, 135070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_592D)

    @scena.Lambda('lambda_5948')
    def lambda_5948():
        ChrWalkTo(0x0101, 83490, 1500, 142800, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5948)

    Sleep(200)

    @scena.Lambda('lambda_5968')
    def lambda_5968():
        ChrWalkTo(0x0106, 82560, 1500, 142800, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_5968)

    WaitForThreadExit(0x0106, 0x0001)

    @scena.Lambda('lambda_5988')
    def lambda_5988():
        ChrWalkTo(0x0103, 83650, 1550, 133380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5988)

    Sleep(1000)

    @scena.Lambda('lambda_59A8')
    def lambda_59A8():
        ChrWalkTo(0x0103, 83400, 1550, 134000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_59A8)

    @scena.Lambda('lambda_59C3')
    def lambda_59C3():
        ChrWalkTo(0x010A, 82570, 1550, 133940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_59C3)

    WaitForThreadExit(0x0103, 0x0001)
    ChrTurnDirection(0x0103, 0x0101, 500)
    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_59EF')
    def lambda_59EF():
        ChrWalkTo(0x010A, 82500, 1550, 133500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_59EF)

    WaitForThreadExit(0x010A, 0x0001)
    ChrTurnDirection(0x010A, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030200374V#020F#6P那么要跟你们两个说再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200375V我们彼此如果有什么新动向，\n',
            '都要通过协会支部\n',
            '进行联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200376V#051F#2P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200377V#1018F#1P再见！\n',
            '雪拉姐、亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200372V#811F#4P嗯！\n',
            '艾丝蒂尔你们也要保重！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B1C(): pass

    label('loc_5B1C')

    Sleep(100)

    Fade(1000)
    ChrSetFlags(0x010A, 0x0008)
    ChrSetFlags(0x00F8, 0x0008)
    CameraMove(82160, 1700, 131180, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3430, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0028, 0x0004)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0029, 0x0004)
    ChrSetFlags(0x0029, 0x0040)
    OP_A1(0x0028, 0x000B)
    OP_A1(0x0029, 0x000A)
    OP_72(0x000B, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x0028, 87000, -5200, 130500, 90)
    ChrSetPos(0x0029, 87000, -5200, 130500, 90)
    OP_0D()
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 100)
    Sleep(3000)

    OP_6F(0x000A, 2)
    OP_70(0x000A, 100)
    PlaySE(118, 0x00, 0x64)
    OP_73(0x000A)
    ChrSetDirection(0x0101, 145, 0)
    ChrSetDirection(0x00F7, 145, 0)
    OP_23(0x0075)
    PlaySE(119, 0x00, 0x64)
    OP_6F(0x000A, 100)
    OP_6F(0x000B, 100)
    OP_70(0x000A, 200)
    OP_70(0x000B, 200)
    OP_73(0x000B)
    OP_6F(0x000A, 200)
    OP_6F(0x000B, 200)
    OP_70(0x000A, 300)
    OP_70(0x000B, 300)

    @scena.Lambda('lambda_5C3D')
    def lambda_5C3D():
        ChrMoveTo(0x00FE, 100000, 500, 131110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0001, lambda_5C3D)

    @scena.Lambda('lambda_5C58')
    def lambda_5C58():
        ChrMoveTo(0x00FE, 100000, 500, 131110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_5C58)

    Sleep(1000)

    Fade(1000)
    CameraMove(91460, 1500, 134290, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(6440, 0)
    OP_6C(146000, 0)
    OP_6E(262, 0)
    WaitForThreadExit(0x0029, 0x0001)
    Fade(1000)
    CameraMove(108820, 1500, 134250, 0)
    CameraSetDistance(7800, 0)
    OP_67(0, 9790, -10000, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_5D01')
    def lambda_5D01():
        ChrMoveTo(0x00FE, 148750, 1500, 131110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0028, 0x0003, lambda_5D01)

    @scena.Lambda('lambda_5D1C')
    def lambda_5D1C():
        ChrMoveTo(0x00FE, 148750, 1500, 131110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0029, 0x0003, lambda_5D1C)

    Sleep(4000)

    FadeOut(2000, 0, -1)
    WaitForThreadExit(0x0029, 0x0003)
    OP_0D()
    OP_23(0x0077)
    OP_72(0x0009, 0x0004)
    Sleep(1000)

    ChrSetPos(0x0101, 83630, 1500, 142960, 270)
    ChrSetPos(0x00F7, 82000, 1500, 142960, 90)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x2, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x2, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x2, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    FadeIn(1500, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5F88',
    )

    ChrTalk(
        0x0101,
        (
            '#0010200379V#1011F#5P那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200380V我们办好登船手续，\n',
            '然后等待去卢安的船着陆吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200381V#026F是啊，反方向的船\n',
            '也快来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200382V#020F隔了一个月没来，\n',
            '要不先回王都买点东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200383V#1016F#5P啊，不用了不用了。\n',
            '在卢安也能买东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200384V#1006F赶紧办理登船手续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200385V#021F呵呵，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200386V#020F船票在飞船公社的\n',
            '等候厅就能够买到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200387V#1006F#5P嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_620E')

    def _loc_5F88(): pass

    label('loc_5F88')

    ChrTalk(
        0x0101,
        (
            '#0010200388V#1000F#5P那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200380V我们办好登船手续，\n',
            '然后等去卢安的船吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200390V#051F对了，反方向的\n',
            '定期船也快到达了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200391V不过你离开都一个月了，\n',
            '想不想买点东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200392V#1011F#5P嗯～确实\n',
            '想去逛逛百货商店什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200393V阿加特你怎么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200394V#051F我无所谓的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200395V打扮什么的\n',
            '是女人的需要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200396V你来决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200397V#1016F#5P这样啊……嘿嘿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200398V#1015F嗯，这样啊。\n',
            '在卢安也能买东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200384V#1006F赶紧办理登船手续吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200400V#051F是吗？明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200401V船票在飞船公社的\n',
            '等候厅能够买到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200387V#1006F#5P嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_620E(): pass

    label('loc_620E')

    Sleep(100)

    SetScenaFlags(ScenaFlag(0x0240, 2, 0x1202))
    OP_28(0x0081, 0x04, 0x02)
    OP_28(0x0081, 0x04, 0x08)
    OP_28(0x0081, 0x01, 0x0040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_6242',
    )

    OP_28(0x0081, 0x01, 0x0008)
    OP_28(0x0081, 0x01, 0x0010)
    OP_28(0x0081, 0x01, 0x0020)

    Jump('loc_625B')

    def _loc_6242(): pass

    label('loc_6242')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_625B',
    )

    OP_28(0x0081, 0x01, 0x0001)
    OP_28(0x0081, 0x01, 0x0002)
    OP_28(0x0081, 0x01, 0x0004)

    def _loc_625B(): pass

    label('loc_625B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_626B',
    )

    FormationDelMember(0x09, 0xFF)
    FormationDelMember(0x05, 0xFF)

    Jump('loc_6271')

    def _loc_626B(): pass

    label('loc_626B')

    FormationDelMember(0x09, 0xFF)
    FormationDelMember(0x02, 0xFF)

    def _loc_6271(): pass

    label('loc_6271')

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetFlags(0x0011, 0x0010)
    ChrSetFlags(0x0019, 0x0010)
    ChrSetFlags(0x001A, 0x0010)
    ChrSetFlags(0x001C, 0x0010)
    ChrSetPos(0x0009, 61450, -3000, 162010, 6)
    ChrSetPos(0x000A, 61450, -3000, 163810, 180)
    EventEnd(0x00)
    MapSetFlags(0x00000001)
    MapClearFlags(0x00000080)

    Return()

# id: 0x0027 offset: 0x62FF
@scena.Code('func_27_62FF')
def func_27_62FF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 2, 0x1202)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 5, 0x1205)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6526',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 4, 0x1204)),
            Expr.Return,
        ),
        'loc_63E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6381',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200403V#050F怎么了？你要去城里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200404V乘船手续可以在\n',
            '公社外的柜台处办理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63E0')

    def _loc_6381(): pass

    label('loc_6381')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200408V#020F咦？你要去城里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200409V乘船手续可以在\n',
            '公社外的柜台处办理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63E0(): pass

    label('loc_63E0')

    Jump('loc_650B')

    def _loc_63E3(): pass

    label('loc_63E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_647C',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200405V#052F怎么？还是\n',
            '想在城里买东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200406V#1016F啊，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200407V#1006F赶快去等候厅\n',
            '买票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_650B')

    def _loc_647C(): pass

    label('loc_647C')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200410V#023F咦？你还是\n',
            '想在城里买东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200406V#1016F啊，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200407V#1006F赶快去等候厅\n',
            '买票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_650B(): pass

    label('loc_650B')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6526(): pass

    label('loc_6526')

    Return()

# id: 0x0028 offset: 0x6527
@scena.Code('func_28_6527')
def func_28_6527():
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
        (0x00000000, 'loc_65A1'),
        (0x00000001, 'loc_65A7'),
        (-1, 'loc_65AD'),
    )

    def _loc_65A1(): pass

    label('loc_65A1')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_65AD')

    def _loc_65A7(): pass

    label('loc_65A7')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_65AD')

    def _loc_65AD(): pass

    label('loc_65AD')

    Return()

# id: 0x0029 offset: 0x65AE
@scena.Code('func_29_65AE')
def func_29_65AE():
    MapClearFlags(0x00000001)
    CameraMove(12790, 0, 144090, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_65ED',
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

    Jump('loc_6607')

    def _loc_65ED(): pass

    label('loc_65ED')

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

    def _loc_6607(): pass

    label('loc_6607')

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

# id: 0x002A offset: 0x6627
@scena.Code('func_2A_6627')
def func_2A_6627():
    MapClearFlags(0x00000001)
    CameraMove(12790, 0, 144090, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_666C',
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

    Jump('loc_668C')

    def _loc_666C(): pass

    label('loc_666C')

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

    def _loc_668C(): pass

    label('loc_668C')

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

# id: 0x002B offset: 0x66AC
@scena.Code('func_2B_66AC')
def func_2B_66AC():
    Sleep(2000)

    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x00, 0x03E8)
    ShowPlaceName('王都格兰赛尔')

    Return()

# id: 0x002C offset: 0x66D5
@scena.Code('func_2C_66D5')
def func_2C_66D5():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船飞船坪\n',
            '≡　前往洛连特市\n',
            '≡　前往蔡斯市\n',
            '≡　去卡尔瓦德共和国',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　『利贝尔飞船公社』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002D offset: 0x6782
@scena.Code('func_2D_6782')
def func_2D_6782():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '   『利贝尔飞船公社』　',
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
