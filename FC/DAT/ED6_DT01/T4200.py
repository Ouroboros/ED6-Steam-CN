import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4200.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00401._CH', 'ED6_DT07/CH00401P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00391._CH', 'ED6_DT07/CH00391P._CP'),
        ('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP'),
        ('ED6_DT06/CH20114._CH', 'ED6_DT06/CH20114P._CP'),
        ('ED6_DT06/CH20116._CH', 'ED6_DT06/CH20116P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT06/CH20155._CH', 'ED6_DT06/CH20155P._CP'),
        ('ED6_DT06/CH20156._CH', 'ED6_DT06/CH20156P._CP'),
        ('ED6_DT06/CH20123._CH', 'ED6_DT06/CH20123P._CP'),
        ('ED6_DT06/CH20124._CH', 'ED6_DT06/CH20124P._CP'),
        ('ED6_DT06/CH20125._CH', 'ED6_DT06/CH20125P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10001 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵丹',
            x                   = -790,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '士兵阿尔兹',
            x                   = 950,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
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
            name                = '管家菲利普',
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
            name                = '特务兵',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '特务兵',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '卡露娜',
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
            name                = '亚妮拉丝',
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
            name                = '库拉茨',
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
            name                = '克鲁茨',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '卡西乌斯',
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
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2660,
            z                   = 0,
            y                   = 27180,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65550,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1310,
            z                   = 0,
            y                   = 26540,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131085,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -240,
            z                   = 0,
            y                   = 27230,
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
            name                = '观众',
            x                   = 480,
            z                   = 0,
            y                   = 26860,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393230,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1600,
            z                   = 0,
            y                   = 26120,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65549,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2350,
            z                   = 0,
            y                   = 27390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393230,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3680,
            z                   = 0,
            y                   = 26400,
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
            name                = '观众',
            x                   = -2140,
            z                   = 0,
            y                   = 25650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458765,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -520,
            z                   = 0,
            y                   = 25640,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262158,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 950,
            z                   = 0,
            y                   = 25560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393230,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3100,
            z                   = 0,
            y                   = 25890,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327694,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2260,
            z                   = 0,
            y                   = 24940,
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
            name                = '观众',
            x                   = -10,
            z                   = 0,
            y                   = 24790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131085,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1370,
            z                   = 0,
            y                   = 24770,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262157,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3170,
            z                   = 0,
            y                   = 24640,
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
            name                = '观众',
            x                   = 3830,
            z                   = 0,
            y                   = 26870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262159,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -4590,
            z                   = 0,
            y                   = 25090,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327695,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2070,
            z                   = 0,
            y                   = 24370,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65549,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1570,
            z                   = 0,
            y                   = 24240,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131085,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3520,
            z                   = 0,
            y                   = 24060,
            direction           = 3,
            word_0E             = 0,
            dword_10            = 393229,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1000,
            z                   = 0,
            y                   = 23340,
            direction           = 343,
            word_0E             = 0,
            dword_10            = 262157,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2820,
            z                   = 0,
            y                   = 22600,
            direction           = 13,
            word_0E             = 0,
            dword_10            = 196622,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -4730,
            z                   = 0,
            y                   = 22830,
            direction           = 353,
            word_0E             = 0,
            dword_10            = 262157,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -670,
            z                   = 0,
            y                   = 21410,
            direction           = 12,
            word_0E             = 0,
            dword_10            = 327693,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1120,
            z                   = 0,
            y                   = 23290,
            direction           = 2,
            word_0E             = 0,
            dword_10            = 327694,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2340,
            z                   = 0,
            y                   = 22560,
            direction           = 359,
            word_0E             = 0,
            dword_10            = 65550,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 4380,
            z                   = 0,
            y                   = 25570,
            direction           = 10,
            word_0E             = 0,
            dword_10            = 262158,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1240,
            z                   = 0,
            y                   = 21910,
            direction           = 357,
            word_0E             = 0,
            dword_10            = 393230,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2670,
            z                   = 0,
            y                   = 21140,
            direction           = 358,
            word_0E             = 0,
            dword_10            = 458766,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3700,
            z                   = 0,
            y                   = 21580,
            direction           = 1,
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
            name                = '观众',
            x                   = -6810,
            z                   = 0,
            y                   = 23940,
            direction           = 46,
            word_0E             = 0,
            dword_10            = 393229,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -5270,
            z                   = 0,
            y                   = 24130,
            direction           = 36,
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
            name                = '观众',
            x                   = -1790,
            z                   = 0,
            y                   = 22220,
            direction           = 21,
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
            name                = '观众',
            x                   = 310,
            z                   = 0,
            y                   = 22190,
            direction           = 13,
            word_0E             = 0,
            dword_10            = 196623,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3970,
            z                   = 0,
            y                   = 22250,
            direction           = 349,
            word_0E             = 0,
            dword_10            = 131087,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿鲁姆',
            x                   = -1370,
            z                   = 0,
            y                   = 10340,
            direction           = 352,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '艾娅莉',
            x                   = -2340,
            z                   = 0,
            y                   = 9870,
            direction           = 10,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -3590,
            z                   = 0,
            y                   = 14380,
            direction           = 54,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = -2690,
            z                   = 0,
            y                   = 13710,
            direction           = 353,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 4310,
            z                   = 0,
            y                   = 13350,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '游客',
            x                   = 4960,
            z                   = 0,
            y                   = 3770,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = 0,
            z                   = 0,
            y                   = -22550,
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

# id: 0x10002 offset: 0x93A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x93A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -5630,
            y           = -1000,
            z           = 30090,
            range       = 6050,
            dword_10    = 0x000003E8,
            dword_14    = 0x000069BE,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
    )

# id: 0x10004 offset: 0x95A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x95A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_976',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0F_4646)

    def _loc_976(): pass

    label('loc_976')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_984',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_10_4B1E)

    def _loc_984(): pass

    label('loc_984')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_992',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_11_4F38)

    def _loc_992(): pass

    label('loc_992')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_9A2'),
        (0x00000065, 'loc_9A2'),
        (-1, 'loc_9B8'),
    )

    def _loc_9A2(): pass

    label('loc_9A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 1, 0x609)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9B5',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 3, 0x60B))
    Event(0, func_0D_1B7F)

    def _loc_9B5(): pass

    label('loc_9B5')

    Jump('loc_9B8')

    def _loc_9B8(): pass

    label('loc_9B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_9E0',
    )

    ChrClearFlags(0x0040, 0x0080)
    ChrClearFlags(0x0041, 0x0080)
    ChrClearFlags(0x0042, 0x0080)
    ChrClearFlags(0x0043, 0x0080)
    ChrClearFlags(0x0044, 0x0080)
    ChrClearFlags(0x0045, 0x0080)

    Jump('loc_A77')

    def _loc_9E0(): pass

    label('loc_9E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_A20',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000C, -790, 0, 41980, 180)
    ChrSetPos(0x000D, 950, 0, 41980, 180)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    Jump('loc_A77')

    def _loc_A20(): pass

    label('loc_A20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_A2A',
    )

    Jump('loc_A77')

    def _loc_A2A(): pass

    label('loc_A2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_A34',
    )

    Jump('loc_A77')

    def _loc_A34(): pass

    label('loc_A34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_A3E',
    )

    Jump('loc_A77')

    def _loc_A3E(): pass

    label('loc_A3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_A48',
    )

    Jump('loc_A77')

    def _loc_A48(): pass

    label('loc_A48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_A52',
    )

    Jump('loc_A77')

    def _loc_A52(): pass

    label('loc_A52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_A5C',
    )

    Jump('loc_A77')

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_A66',
    )

    Jump('loc_A77')

    def _loc_A66(): pass

    label('loc_A66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_A70',
    )

    Jump('loc_A77')

    def _loc_A70(): pass

    label('loc_A70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_A77',
    )

    def _loc_A77(): pass

    label('loc_A77')

    Return()

# id: 0x0001 offset: 0xA78
@scena.Code('func_01_A78')
def func_01_A78():
    OP_16(0x02, 4000, -128000, -112000, 196704)

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
        'loc_ABD',
    )

    OP_B1('t4200_y')

    Jump('loc_AC6')

    def _loc_ABD(): pass

    label('loc_ABD')

    OP_B1('t4200_n')

    def _loc_AC6(): pass

    label('loc_AC6')

    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_AE3',
    )

    OP_6F(0x0000, 450)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)

    def _loc_AE3(): pass

    label('loc_AE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AF8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_AF8(): pass

    label('loc_AF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_B7D',
    )

    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -770, 750, 23720, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -520, 750, 42700, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_B7D(): pass

    label('loc_B7D')

    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0xB83
@scena.Code('func_02_B83')
def func_02_B83():
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
        'loc_BA8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_CEA')

    def _loc_BA8(): pass

    label('loc_BA8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC1',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_CEA')

    def _loc_BC1(): pass

    label('loc_BC1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDA',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_CEA')

    def _loc_BDA(): pass

    label('loc_BDA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF3',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_CEA')

    def _loc_BF3(): pass

    label('loc_BF3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_CEA')

    def _loc_C0C(): pass

    label('loc_C0C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C25',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_CEA')

    def _loc_C25(): pass

    label('loc_C25')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C3E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_CEA')

    def _loc_C3E(): pass

    label('loc_C3E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C57',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_CEA')

    def _loc_C57(): pass

    label('loc_C57')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C70',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_CEA')

    def _loc_C70(): pass

    label('loc_C70')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C89',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_CEA')

    def _loc_C89(): pass

    label('loc_C89')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_CEA')

    def _loc_CA2(): pass

    label('loc_CA2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_CEA')

    def _loc_CBB(): pass

    label('loc_CBB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CD4',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_CEA')

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CEA',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_CEA(): pass

    label('loc_CEA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CFF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_CEA')

    def _loc_CFF(): pass

    label('loc_CFF')

    Return()

# id: 0x0003 offset: 0xD00
@scena.Code('func_03_D00')
def func_03_D00():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔城完全封锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上面下了命令，\n',
            '无论是谁也不能通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xD4A
@scena.Code('func_04_D4A')
def func_04_D4A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '你们是在武术大会\n',
            '取得优胜的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚宴已经结束了。\n',
            '快回游击士协会去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xDA7
@scena.Code('func_05_DA7')
def func_05_DA7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_EC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E26',
    )

    ChrTalk(
        0x00FE,
        (
            '尤莉亚中尉是恐怖分子的说法\n',
            '让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而理查德上校\n',
            '是政变的主谋这一点\n',
            '同样让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC3')

    def _loc_E26(): pass

    label('loc_E26')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '尤莉亚中尉是恐怖分子的说法\n',
            '让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而理查德上校\n',
            '是政变的主谋这一点\n',
            '同样让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么优秀的一个人，\n',
            '怎么会做出这种事来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC3(): pass

    label('loc_EC3')

    Jump('loc_1385')

    def _loc_EC6(): pass

    label('loc_EC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_ED0',
    )

    Jump('loc_1385')

    def _loc_ED0(): pass

    label('loc_ED0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_EFD',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，\n',
            '在王城里面好好参观了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_EFD(): pass

    label('loc_EFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_F5B',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到\n',
            '女王陛下的格兰赛尔城！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们从这里进去，\n',
            '就会有接待人员前来迎接。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_F5B(): pass

    label('loc_F5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_FC5',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '不知道尤莉亚中尉现在怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天向中尉打招呼\n',
            '可是我日常工作当中的一大乐趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_FC5(): pass

    label('loc_FC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1056',
    )

    ChrTalk(
        0x00FE,
        (
            '我们从今晚开始\n',
            '必须在市内巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为恐怖分子还未抓到，\n',
            '所以必须严加防范。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么特务部队的工作\n',
            '要由我们正规军来善后啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_1056(): pass

    label('loc_1056')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_10C5',
    )

    ChrTalk(
        0x00FE,
        (
            '特务部队的那群人\n',
            '在大会中连续获胜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起去参加比赛，\n',
            '我倒希望他们\n',
            '快点去搜捕亲卫队的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_10C5(): pass

    label('loc_10C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_11CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1143',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下生病后，\n',
            '就几乎很少能在城外\n',
            '看见理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来情报部的本部\n',
            '好像也要暂时转移到王城里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11C7')

    def _loc_1143(): pass

    label('loc_1143')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '好像非常忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下生病后，\n',
            '几乎很少能在城外看见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来情报部的本部\n',
            '好像也要暂时转移到王城里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11C7(): pass

    label('loc_11C7')

    Jump('loc_1385')

    def _loc_11CA(): pass

    label('loc_11CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1274',
    )

    ChrTalk(
        0x00FE,
        (
            '说起理查德上校，\n',
            '我当然是很尊敬他啦。\n',
            '可是那些情报部的黑衣家伙们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我承认他们有实力，\n',
            '可他们给人的感觉很不舒服，\n',
            '在军队里面关于他们的流言也不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_1274(): pass

    label('loc_1274')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_12DF',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '的确是个优秀的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为在王国军中颇具人气，\n',
            '有许多人都慕名\n',
            '转到情报部去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_12DF(): pass

    label('loc_12DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1385',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            Expr.Return,
        ),
        'loc_134A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不能进城参观，\n',
            '也不要这么灰心丧气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔的大街上\n',
            '还有很多观光胜地呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1385')

    def _loc_134A(): pass

    label('loc_134A')

    ChrTalk(
        0x00FE,
        (
            '请你们站住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，\n',
            '王城现在禁止无关人等进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1385(): pass

    label('loc_1385')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1389
@scena.Code('func_06_1389')
def func_06_1389():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1409',
    )

    ChrTalk(
        0x00FE,
        (
            '这次政变竟然是由\n',
            '城内的情报部发起的，\n',
            '的确让我感到震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过庆典总算能够平安无事地进行，\n',
            '真的是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_1409(): pass

    label('loc_1409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1413',
    )

    Jump('loc_1933')

    def _loc_1413(): pass

    label('loc_1413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1480',
    )

    ChrTalk(
        0x00FE,
        (
            '你们好啊，\n',
            '晚宴怎么样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '宫廷料理什么的，\n',
            '我只在执行警卫时见过，\n',
            '从来都没机会品尝过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_1480(): pass

    label('loc_1480')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_14AA',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，祝各位晚上玩得愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_14AA(): pass

    label('loc_14AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_150E',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '宫廷料理的材料都已经运到城内来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概那就是\n',
            '用来烹制今晚晚宴的食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_150E(): pass

    label('loc_150E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_15F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1577',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '全城的警戒都加强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这项工作似乎是由\n',
            '上校的副官凯诺娜上尉负责的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15F1')

    def _loc_1577(): pass

    label('loc_1577')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '全城的警戒都加强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这项工作似乎是由\n',
            '上校的副官凯诺娜上尉负责的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '果然相当忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15F1(): pass

    label('loc_15F1')

    Jump('loc_1933')

    def _loc_15F4(): pass

    label('loc_15F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1669',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '关于女王陛下病情的详细情况，\n',
            '我们也不太了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '的确感觉有些不安呢，\n',
            '也不知道到底会怎么样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_1669(): pass

    label('loc_1669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_16C9',
    )

    ChrTalk(
        0x00FE,
        (
            '大会正式赛第一回合\n',
            '好像已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '代表王国警备队出场的\n',
            '那些人怎么样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_16C9(): pass

    label('loc_16C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_17C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1734',
    )

    ChrTalk(
        0x00FE,
        (
            '杜南公爵\n',
            '就算在王城里也很招人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校不在的话，\n',
            '不知道会变成什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17C0')

    def _loc_1734(): pass

    label('loc_1734')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '杜南公爵\n',
            '就算在王城里也很招人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为无论是谁，\n',
            '都只看到过他在吃、睡、玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校不在的话，\n',
            '不知道会变成什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17C0(): pass

    label('loc_17C0')

    Jump('loc_1933')

    def _loc_17C3(): pass

    label('loc_17C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_18CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1840',
    )

    ChrTalk(
        0x00FE,
        (
            '因为今年的武术大会是团体战，\n',
            '比赛场次比以往减少了一些呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正式赛和预选赛不一样，\n',
            '是在下午进行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18CC')

    def _loc_1840(): pass

    label('loc_1840')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '武术大会的预选赛\n',
            '好像已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今年因为是团体战，\n',
            '比赛场次比以往减少了一些呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正式赛和预选赛不一样，\n',
            '是在下午进行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18CC(): pass

    label('loc_18CC')

    Jump('loc_1933')

    def _loc_18CF(): pass

    label('loc_18CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1933',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            Expr.Return,
        ),
        'loc_191B',
    )

    ChrTalk(
        0x00FE,
        (
            '好不容易来一次王都，\n',
            '就请舒舒服服地享受观光的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1933')

    def _loc_191B(): pass

    label('loc_191B')

    ChrTalk(
        0x00FE,
        (
            '现在不能进城参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1933(): pass

    label('loc_1933')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1937
@scena.Code('func_07_1937')
def func_07_1937():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '刚才我正打算\n',
            '在王城前向她求婚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
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
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x19EA
@scena.Code('func_08_19EA')
def func_08_19EA():
    TalkBegin(0x00FE)

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
            '不过，我们俩这趟旅程的最高潮\n',
            '从现在才开始哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1A47
@scena.Code('func_09_1A47')
def func_09_1A47():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '没想到呢，\n',
            '今年也能和孙子一起\n',
            '一睹女王陛下的风采。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，太好了太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1AA0
@scena.Code('func_0A_1AA0')
def func_0A_1AA0():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '公主殿下真的好漂亮哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我只能用『哇啊～』来形容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1AE5
@scena.Code('func_0B_1AE5')
def func_0B_1AE5():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '女王陛下生病的事\n',
            '只是谣言吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了……\n',
            '我对此事一直很担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1B36
@scena.Code('func_0C_1B36')
def func_0C_1B36():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我也要去街区那边\n',
            '好好逛一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这会儿那里\n',
            '肯定非常热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1B7F
@scena.Code('func_0D_1B7F')
def func_0D_1B7F():
    EventBegin(0x00)
    OP_12(0x000186A0, 0x0002BF20, 0x000003E8)
    OP_6C(30000, 0)

    @scena.Lambda('lambda_1B9D')
    def lambda_1B9D():
        CameraMove(-930, 750, 44710, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B9D)

    @scena.Lambda('lambda_1BB5')
    def lambda_1BB5():
        OP_67(0, 4250, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BB5)

    @scena.Lambda('lambda_1BCD')
    def lambda_1BCD():
        CameraSetDistance(11000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1BCD)

    @scena.Lambda('lambda_1BDD')
    def lambda_1BDD():
        OP_6C(0, 15000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1BDD)

    Sleep(12000)

    ChrSetPos(0x0101, -910, 0, 8880, 0)
    ChrSetPos(0x0102, 1000, 0, 10110, 0)

    @scena.Lambda('lambda_1C14')
    def lambda_1C14():
        CameraMove(-290, 0, 32350, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1C14)

    @scena.Lambda('lambda_1C2C')
    def lambda_1C2C():
        CameraSetDistance(7180, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C2C)

    @scena.Lambda('lambda_1C3C')
    def lambda_1C3C():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C3C)

    @scena.Lambda('lambda_1C4C')
    def lambda_1C4C():
        ChrWalkTo(0x00FE, -670, 0, 18440, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C4C)

    @scena.Lambda('lambda_1C67')
    def lambda_1C67():
        ChrWalkTo(0x00FE, 600, 0, 18440, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1C67)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010100752V#001F哇～……\n',
            '这就是格兰赛尔城啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100753V女王住的地方，\n',
            '果然是又气派又漂亮呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020100754V#010F嗯……\n',
            '看起来不仅是漂亮，\n',
            '而且也十分的坚固呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100755V那个巨大的城门就是很好的例子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100756V#505F确实……\n',
            '不可能那么简单就能进得去呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100757V总之……\n',
            '只能先向那边的士兵打听一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100758V#010F我们先暗中调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100759V#015F……就像刚从乡下来，\n',
            '想进王城参观那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100760V想借此机会拜见女王，\n',
            '哪怕看一眼也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100761V#010F——这种设定不错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100762V#007F还是老样子，摆出一幅若无其事的表情，\n',
            '立刻就能说出想法来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100763V老是让人家吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100764V#019F这句话我就当成是夸奖收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F58')
    def lambda_1F58():
        CameraMove(0, 250, 42590, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F58)

    @scena.Lambda('lambda_1F70')
    def lambda_1F70():
        CameraSetDistance(5100, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F70)

    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0009, 400)
    WaitForThreadExit(0x0101, 0x0002)
    ChrSetPos(0x0101, -850, 0, 25330, 0)
    ChrSetPos(0x0102, 1090, 0, 22700, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010100765V喂～你们好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_1FF7')
    def lambda_1FF7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1FF7')

    DispatchAsync2(0x0008, 0x0001, lambda_1FF7)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_201F')
    def lambda_201F():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_201F')

    DispatchAsync2(0x0009, 0x0001, lambda_201F)

    @scena.Lambda('lambda_2030')
    def lambda_2030():
        ChrWalkTo(0x00FE, 600, 0, 37520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2030)

    @scena.Lambda('lambda_204B')
    def lambda_204B():
        ChrWalkTo(0x00FE, -670, 0, 37520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_204B)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160100766V#1P哦，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100767V#2P欢迎来到格兰赛尔城。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020100768V#010F我们是刚从洛连特来到王都观光的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100769V借此机会，\n',
            '想进城里面参观一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100770V#1P啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100771V#1P两位游客，很抱歉。\n',
            '格兰赛尔城是禁止无关人员入内的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100772V#2P由于恐怖分子骚乱，\n',
            '现在的检查更为严格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100773V#2P不过，抓到了恐怖分子之后，\n',
            '应该就允许大家参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100774V#007F是这样啊……真可惜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100775V唉，难道见女王陛下一面的梦想\n',
            '还是没办法实现吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100776V#1P对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100777V#1P诞辰庆典那天，\n',
            '女王会照例在王城的露台上对市民致意，\n',
            '我想应该会有见面的机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100778V#2P不过最近，\n',
            '陛下的身体状况不是很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100779V#2P例行的致意还会不会有呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100780V#580F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100781V#012F请问……\n',
            '女王陛下生病了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100782V#2P是啊……\n',
            '大概是因为操劳过度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100783V#2P而且，因为自己十分信赖的亲卫队\n',
            '被当成恐怖事件的嫌疑犯这件事，\n',
            '也受了相当大的打击吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100784V#2P最近都没有出现在谒见室，\n',
            '应该是在女王宫静养吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100785V#002F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100786V#1P真是的，亲卫队那些家伙，\n',
            '对陛下的信赖反倒恩将仇报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100787V#1P平常我就不喜欢\n',
            '这些所谓的精英。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2170100788V#2P可、可是，\n',
            '尤莉亚中尉平时不是很亲切的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 800)

    ChrTalk(
        0x0009,
        (
            '#2170100789V#2P对我们这些普通的士兵，\n',
            '也亲自教授剑术和行事方法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100790V#2P说她是恐怖分子，\n',
            '我有点不太相信呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2160100791V#1P这、这是肯定的啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100792V#1P可能因为部下的胡作非为而感到责任重大，\n',
            '所以才就这样突然失踪的啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100793V#1P啊啊……\n',
            '尤莉亚小姐真是可怜啊……',
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
            '#0010100794V#509F（看起来，这些人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100795V（只是因为尤莉亚小姐的关系，\n',
            '　在嫉妒其他的队员呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100796V#019F（嗯，的确是这样……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2160100797V#1P咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100798V#1P总之，就是这个原因，\n',
            '格兰赛尔城禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2170100799V#2P抱歉，请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100800V#007F唉，这样的话，\n',
            '也只好暂时打消这个念头了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100801V#013F不过，我还是有点担心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100802V女王陛下的健康暂且不论，\n',
            '政务方面不用管理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100803V#2P嗯……\n',
            '这个担心很有道理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100804V#2P虽然这样，\n',
            '还是有名义上的代理人的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100805V#505F名义上的代理人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100806V#1P哈哈。\n',
            '顾名思义，只是『名义上的』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100807V#1P那一位大人和政务\n',
            '还真是八竿子打不着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2170100808V#2P喂喂，说话要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100809V#2P不过确实，\n',
            '我也觉得公主更为适合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2160100810V#1P看，你不也是这样想的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(210, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000A, -270, 750, 48420, 180)
    ChrSetPos(0x000B, 550, 750, 49230, 180)

    ChrTalk(
        0x0101,
        (
            '#0010100811V#004F什、什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000B, 400)
    ChrTurnDirection(0x0009, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#2160100812V#1P哦，好像出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B88')
    def lambda_2B88():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B88)

    @scena.Lambda('lambda_2BA0')
    def lambda_2BA0():
        CameraSetDistance(3800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2BA0)

    @scena.Lambda('lambda_2BB0')
    def lambda_2BB0():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2BB0)

    Sleep(100)

    ChrTurnDirection(0x0008, 0x0009, 400)

    @scena.Lambda('lambda_2BCC')
    def lambda_2BCC():
        ChrMoveTo(0x00FE, -2320, 0, 41990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2BCC)

    ChrTurnDirection(0x0009, 0x0008, 400)

    @scena.Lambda('lambda_2BEE')
    def lambda_2BEE():
        ChrMoveTo(0x00FE, 2320, 0, 42150, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2BEE)

    CameraMove(-10, 750, 48050, 3000)

    @scena.Lambda('lambda_2C1A')
    def lambda_2C1A():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2C1A')

    DispatchAsync2(0x0101, 0x0001, lambda_2C1A)

    @scena.Lambda('lambda_2C2B')
    def lambda_2C2B():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2C2B')

    DispatchAsync2(0x0102, 0x0001, lambda_2C2B)

    ChrSetPos(0x0101, -2130, 0, 39490, 0)
    ChrSetPos(0x0102, -2130, 0, 37840, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 450)
    OP_73(0x0000)

    @scena.Lambda('lambda_2C6F')
    def lambda_2C6F():
        ChrWalkTo(0x00FE, -260, 750, 44590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2C6F)

    Sleep(500)

    @scena.Lambda('lambda_2C8F')
    def lambda_2C8F():
        ChrWalkTo(0x00FE, 630, 750, 45200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2C8F)

    CameraMove(0, 750, 44920, 2000)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000A,
        (
            '#0640100813V#222F哼，这叫什么事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100814V现在预选赛不是已经开始了吗！？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#0640100815V#224F菲利普！\n',
            '都是因为你没有叫我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#0660100816V#722F实在是抱歉，公爵大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100817V不过，这也是因为\n',
            '公爵大人不注意生活规律啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100818V这几天连续大摆宴席，\n',
            '又是吃又是唱地大闹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100819V啤酒和油炸食品放在一起大量地吃，\n',
            '还彻夜地看漫画杂志一直到早上……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100820V总是这样，\n',
            '睡过头也是理所当然的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0640100821V#225F闭嘴，菲利普！\n',
            '你的这些话我已经听够了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100822V作为下任国王的我，\n',
            '有权力想干什么就干什么！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100823V#224F哎呀，时间紧迫！\n',
            '赶快去王立竞技场才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)

    @scena.Lambda('lambda_2F44')
    def lambda_2F44():
        ChrWalkTo(0x00FE, -270, 0, 28020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2F44)

    Sleep(500)

    @scena.Lambda('lambda_2F64')
    def lambda_2F64():
        ChrWalkTo(0x00FE, 1070, 0, 27640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2F64)

    OP_6F(0x0000, 450)
    OP_70(0x0000, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    CameraMove(-30, 0, 40870, 5000)

    @scena.Lambda('lambda_2FC2')
    def lambda_2FC2():
        ChrMoveTo(0x00FE, -790, 0, 41980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2FC2)

    @scena.Lambda('lambda_2FDD')
    def lambda_2FDD():
        ChrMoveTo(0x00FE, 950, 0, 41980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2FDD)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 180, 400)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetDirection(0x0009, 180, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_63(0x0101)
    OP_63(0x0102)
    Sleep(400)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100824V#509F……哎…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, -1320, 0, 38630, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100825V#014F#6P……我说，难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0009, 0x0101, 400)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2160100826V#5P我知道，不用再说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100827V#5P刚才那位就是陛下的代理人，\n',
            '现在主理政务的杜南公爵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100828V#007F我……\n',
            '我的头开始疼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100829V#2P总、总之不用担心。\n',
            '有个可靠的人在辅佐，所以没问题的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170100830V#2P多亏了那个人，\n',
            '至今还没出什么大乱子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_31DD')
    def lambda_31DD():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_31DD)

    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100831V#012F#6P可靠的辅佐人……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100832V#5P嘿嘿，那个人就是\n',
            '王国军情报部的理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100833V#5P可以说，他代替放荡的杜南公爵，\n',
            '一手处理王国的政务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100834V#009F（果、果然……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100835V#012F#6P（比想象中还要更加深入地\n',
            '　控制了国家的核心呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100836V#5P不过，虽然不能进城参观，\n',
            '也不要这么灰心丧气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160100837V#5P王都格兰赛尔还有\n',
            '很多观光胜地呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#2170100838V#2P好不容易来一次王都，\n',
            '就请慢慢地享受观光的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100839V#008F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100840V#019F#6P感谢你们的好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0008, -790, 0, 41980, 180)
    ChrSetPos(0x0009, 950, 0, 41980, 180)
    CreateThread(0x0008, 0x00, 0x00, func_02_B83)
    CreateThread(0x0009, 0x00, 0x00, func_02_B83)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    CameraMove(-170, 0, 24540, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_12(0x00000000, 0x00000000, 0x00000001)
    ChrSetPos(0x0102, 660, 0, 34050, 18)
    ChrSetPos(0x0101, -860, 0, 33870, 45)

    @scena.Lambda('lambda_34F1')
    def lambda_34F1():
        ChrWalkTo(0x00FE, -860, 0, 25150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34F1)

    Sleep(300)

    @scena.Lambda('lambda_3511')
    def lambda_3511():
        ChrWalkTo(0x00FE, 660, 0, 24840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3511)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_353B')
    def lambda_353B():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_353B)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_354E')
    def lambda_354E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_354E)

    ChrTalk(
        0x0101,
        (
            '#0010100841V#006F#3P嗯……\n',
            '比想象中收获更大呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100842V#007F而且，那个胖子公爵\n',
            '竟然是女王陛下的代理人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100843V#013F实际掌权的，是理查德上校吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100844V而且……\n',
            '自己的阴谋周围的人都浑然不觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100845V#012F操纵情报的手段还真是高明啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100846V#007F#3P真是的，约修亚。\n',
            '这可不是称赞敌人的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100847V#006F对了对了，\n',
            '那个公爵好像去看武术大会了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100848V我们也去看看如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100849V#015F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100850V#010F调查一下公爵的行动，\n',
            '也许会有什么收获也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100851V#001F#3P那么就决定了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100852V#505F#3P嗯……\n',
            '王立竞技场是在哪个方向呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100853V#010F我记得应该是在东街区吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100854V先回到大街上然后往东走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0045, 0x01, 0x0200)
    OP_28(0x0045, 0x01, 0x0400)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x3837
@scena.Code('func_0E_3837')
def func_0E_3837():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3844',
    )

    Return()

    def _loc_3844(): pass

    label('loc_3844')

    EventBegin(0x00)

    @scena.Lambda('lambda_384C')
    def lambda_384C():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_384C)

    @scena.Lambda('lambda_385A')
    def lambda_385A():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_385A)

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080120001V#073F哦，现在就进城去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120002V晚宴结束之后要在城里的客房过夜，\n',
            '明天才能回到街上来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【进入格兰赛尔城】\n'),
            TXT(0x01, '【等一会儿再来】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_394F'),
        (0x00000001, 'loc_3A14'),
        (-1, 'loc_3A5D'),
    )

    def _loc_394F(): pass

    label('loc_394F')

    ChrTalk(
        0x0108,
        (
            '#0080120004V#070F那么就把请帖给那边的门卫看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120005V#008F嗯～\n',
            '总觉得很紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120006V#019F没错，像这样被招待进王城的体验，\n',
            '对我们这些普通百姓来说还真是难得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A5D')

    def _loc_3A14(): pass

    label('loc_3A14')

    ChrTalk(
        0x0108,
        (
            '#0080120003V#070F知道了，一会儿再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_3A5D(): pass

    label('loc_3A5D')

    @scena.Lambda('lambda_3A63')
    def lambda_3A63():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A63)

    @scena.Lambda('lambda_3A71')
    def lambda_3A71():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3A71)

    @scena.Lambda('lambda_3A7F')
    def lambda_3A7F():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3A7F)

    @scena.Lambda('lambda_3A8D')
    def lambda_3A8D():
        OP_67(0, 5220, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3A8D)

    @scena.Lambda('lambda_3AA5')
    def lambda_3AA5():
        OP_6E(287, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3AA5)

    CameraMove(110, 0, 41220, 3000)
    ChrSetPos(0x0101, -620, 0, 32729, 0)
    ChrSetPos(0x0102, 920, 0, 32590, 0)
    ChrSetPos(0x0108, 90, 0, 32000, 0)

    @scena.Lambda('lambda_3AF9')
    def lambda_3AF9():
        ChrWalkTo(0x00FE, -770, 0, 39810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3AF9)

    Sleep(300)

    @scena.Lambda('lambda_3B19')
    def lambda_3B19():
        ChrWalkTo(0x00FE, 1250, 0, 39890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3B19)

    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160120007V#1P这里是女王陛下\n',
            '居住的格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120008V如果没有事情的话，\n',
            '就请离开这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120009V哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010120010V#006F晚上好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020120011V#010F#4P那天麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120012V怎么，原来是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120013V你们还呆在王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120014V#001F嗯，稍微有点事情。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120015V#010F#4P今天是因为受到正式邀请才来这里的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160120016V正式的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120017V邀请……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120018V#1P……是公爵亲自给我们的请帖。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D99')
    def lambda_3D99():
        ChrWalkTo(0x00FE, 300, 0, 39010, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3D99)

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#2160120019V哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120020V巨、巨人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0108,
        (
            '#0080120021V#070F#4P给，这就是请帖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0108, 360, 0, 41430, 2000, 0x00)
    RemoveItem(0x0371, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '晚宴请帖',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrMoveTo(0x0108, 300, 0, 40600, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#2160120022V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120023V『金·瓦赛克等四人\n',
            '　在武术大会获得优胜，\n',
            '　特此邀请参加晚宴……』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120024V这样啊……\n',
            '你们是武术大会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120025V我记得，\n',
            '获得优胜的是来自东方的\n',
            '武术家所率领的小组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120026V难道……\n',
            '你们就是那个小组的成员？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120027V#502F嘿嘿，其实就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120028V#010F#4P只不过是帮了点微不足道的小忙而已。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120029V原来如此，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120030V……你们的事情\n',
            '我从女官长那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120031V不过，好像少一个人啊。\n',
            '那一位怎么没有来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120032V#070F#4P因为有点私事，\n',
            '所以没办法来参加了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120033V出席的只有我们而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120034V是吗，那真是遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120035V算了……\n',
            '现在就让你们进城吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_41BC')
    def lambda_41BC():
        CameraMove(70, 750, 44190, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_41BC)

    @scena.Lambda('lambda_41D4')
    def lambda_41D4():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41D4)

    @scena.Lambda('lambda_41E4')
    def lambda_41E4():
        OP_6E(438, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_41E4)

    ChrWalkTo(0x0009, 110, 750, 44500, 2000, 0x00)
    ChrSetDirection(0x0009, 0, 400)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#2170120036V武术大会的优胜者，\n',
            '金选手等三人前来光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120037V开门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4267')
    def lambda_4267():
        CameraMove(70, 3450, 44190, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4267)

    @scena.Lambda('lambda_427F')
    def lambda_427F():
        OP_67(0, 7620, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_427F)

    @scena.Lambda('lambda_4297')
    def lambda_4297():
        ChrWalkTo(0x0008, -2300, 750, 44600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4297)

    ChrWalkTo(0x0009, 2450, 750, 44600, 2000, 0x00)
    ChrSetDirection(0x0009, 180, 400)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 180, 400)
    PlaySE(210, 0x00, 0x64)
    Sleep(2000)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 450)
    OP_73(0x0000)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010120038V#004F哇啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120039V和哈肯大门一样，\n',
            '这个城门也非常的有魄力啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120040V#010F而且，只有王城才能建造得如此坚固。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120041V#1P这是不可能被攻陷的城堡呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120042V#1P建国以来，\n',
            '虽然亚宁堡没有被外敌突破过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120043V#1P但因为贵族的叛乱，\n',
            '王都数次被卷入战火之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120044V#2P那个时候，多亏了这座城堡，\n',
            '王家才得以击退反叛军的进攻，\n',
            '保护了王族成员和避难的人民……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120045V#2P有很多这种故事流传下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120046V#501F哎～有这样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120047V#070F嗯，有悠久历史的国家\n',
            '总会有种种古代的传奇故事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120048V#1P好了，请进吧！\n',
            '欢迎来到女王陛下的格兰赛尔城！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120049V#1P进去之后，\n',
            '就会有接待人员迎接你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120050V#2P祝你们晚上过得愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_45E8')
    def lambda_45E8():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_45E8)

    Sleep(100)

    @scena.Lambda('lambda_4603')
    def lambda_4603():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4603)

    Sleep(100)

    @scena.Lambda('lambda_461E')
    def lambda_461E():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_461E)

    SetScenaFlags(ScenaFlag(0x00C7, 0, 0x638))
    FadeOut(2000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/T4250._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x4646
@scena.Code('func_0F_4646')
def func_0F_4646():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    CameraMove(70, -1900, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    ChrSetPos(0x000C, -790, 0, 41980, 180)
    ChrSetPos(0x000D, 950, 0, 41980, 180)
    PlaySE(210, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_46DF')
    def lambda_46DF():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_46DF)

    Sleep(200)

    @scena.Lambda('lambda_46F2')
    def lambda_46F2():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_46F2)

    CameraMove(70, 2550, 45150, 2000)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 450)

    ChrTalk(
        0x000C,
        (
            '#2620131152V怎、怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2630131153V奇怪了啊……\n',
            '不是说已经完全封闭了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_47AD')
    def lambda_47AD():
        ChrSetDirection(0x00FE, 180, 800)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_47AD)

    Sleep(100)

    @scena.Lambda('lambda_47C0')
    def lambda_47C0():
        ChrSetDirection(0x00FE, 180, 800)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_47C0)

    CameraMove(70, -1900, 45200, 1000)

    ChrTalk(
        0x000C,
        (
            '#2620131154V#1P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2630131155V#2P怎么会！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-1030, 0, 9000, 0)
    OP_67(0, 9340, -13360, 0)
    CameraSetDistance(1000, 0)
    OP_6C(135000, 0)
    OP_6E(747, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0012, 1730, 0, -280, 0)
    ChrSetPos(0x0013, 1730, 0, -2790, 180)
    ChrSetPos(0x0014, 1730, 0, -5480, 180)
    ChrSetPos(0x0015, 1730, 0, -8070, 180)
    ChrSetPos(0x0016, 1730, 0, -10050, 180)
    ChrSetPos(0x000E, 3230, 0, -4350, 0)
    ChrSetPos(0x0010, 3230, 0, -1480, 0)
    ChrSetPos(0x0017, -1770, 0, -380, 260)
    ChrSetPos(0x0018, -1770, 0, -2970, 180)
    ChrSetPos(0x0019, -1770, 0, -5140, 180)
    ChrSetPos(0x001A, -1770, 0, -7650, 180)
    ChrSetPos(0x000F, -3240, 0, -1470, 360)
    ChrSetPos(0x0011, -3240, 0, -4130, 360)

    @scena.Lambda('lambda_4980')
    def lambda_4980():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4980)

    @scena.Lambda('lambda_499B')
    def lambda_499B():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_499B)

    @scena.Lambda('lambda_49B6')
    def lambda_49B6():
        ChrWalkTo(0x00FE, -250, 0, 98520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_49B6)

    @scena.Lambda('lambda_49D1')
    def lambda_49D1():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_49D1)

    @scena.Lambda('lambda_49EC')
    def lambda_49EC():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_49EC)

    @scena.Lambda('lambda_4A07')
    def lambda_4A07():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A07)

    @scena.Lambda('lambda_4A22')
    def lambda_4A22():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4A22)

    @scena.Lambda('lambda_4A3D')
    def lambda_4A3D():
        ChrWalkTo(0x00FE, -250, 0, 98520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_4A3D)

    @scena.Lambda('lambda_4A58')
    def lambda_4A58():
        ChrWalkTo(0x00FE, -250, 0, 98520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_4A58)

    @scena.Lambda('lambda_4A73')
    def lambda_4A73():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_4A73)

    @scena.Lambda('lambda_4A8E')
    def lambda_4A8E():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_4A8E)

    @scena.Lambda('lambda_4AA9')
    def lambda_4AA9():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4AA9)

    @scena.Lambda('lambda_4AC4')
    def lambda_4AC4():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_4AC4)

    @scena.Lambda('lambda_4ADF')
    def lambda_4ADF():
        CameraMove(-390, 0, 29050, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4ADF)

    @scena.Lambda('lambda_4AF7')
    def lambda_4AF7():
        OP_6C(44000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4AF7)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x4B1E
@scena.Code('func_10_4B1E')
def func_10_4B1E():
    EventBegin(0x00)
    FadeIn(2000, 0)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
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
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)
    ChrClearFlags(0x003E, 0x0080)
    ChrClearFlags(0x003F, 0x0080)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(50, 4200, 30840, 0)
    OP_67(0, 6310, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(61000, 0)
    OP_6E(391, 0)

    @scena.Lambda('lambda_4C39')
    def lambda_4C39():
        CameraMove(50, 100, 30840, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_4C39)

    @scena.Lambda('lambda_4C51')
    def lambda_4C51():
        OP_6C(50000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4C51)

    Sleep(5000)

    OP_62(0x001D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x001E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x001F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0020, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0021, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0022, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0023, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0024, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0025, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0026, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0027, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0028, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0029, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x002A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x002B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x002C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x002D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x002E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x002F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0030, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0031, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0032, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0033, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0034, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0036, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0037, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0038, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0039, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x003A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x003B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x003C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x003D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x003E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x003F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_4EE1')
    def lambda_4EE1():
        CameraMove(20, 13000, 44770, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_4EE1)

    @scena.Lambda('lambda_4EF9')
    def lambda_4EF9():
        OP_67(0, 3640, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4EF9)

    @scena.Lambda('lambda_4F11')
    def lambda_4F11():
        OP_6C(0, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4F11)

    Sleep(2500)

    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x4F38
@scena.Code('func_11_4F38')
def func_11_4F38():
    EventBegin(0x00)
    OP_6F(0x0000, 450)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetPos(0x001C, 3420, 0, -7500, 0)
    ChrSetPos(0x001B, 2600, 0, -6950, 0)
    ChrSetPos(0x0101, 3420, 0, -8400, 0)
    ChrSetPos(0x0102, 4150, 0, -7140, 0)
    ChrSetChipByIndex(0x0102, 11)
    ChrSetChipByIndex(0x001B, 12)
    ChrClearFlags(0x001B, 0x0080)
    MapSetFlags(0x00000001)
    OP_69(0x001C, 0)
    OP_6A(0x001C)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_4FE8')
    def lambda_4FE8():
        OP_6C(135000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4FE8)

    @scena.Lambda('lambda_4FF8')
    def lambda_4FF8():
        ChrMoveToRelativeAsync(0x00FE, -3470, 0, 38000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_4FF8)

    CreateThread(0x0101, 0x01, 0x00, func_12_61A2)
    CreateThread(0x0102, 0x01, 0x00, func_13_61B7)
    CreateThread(0x001B, 0x01, 0x00, func_14_61DD)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010140558V#007F老爸也真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140559V就不能陪我们一起参加诞辰庆典吗，\n',
            '至少一起参观一下王都也好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140560V#080F抱歉，我还有紧急的军事会议要出席。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140561V虽然理查德被逮捕了，\n',
            '但是逃亡中的特务兵还有很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140562V凯诺娜上尉也不知道什么时候\n',
            '从那个地下遗迹中失踪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140563V而且，参加武术大会的空贼团\n',
            '也趁混乱的时候逃走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140564V为了不让诞辰庆典发生任何骚动，\n',
            '我们还得加强警备工作才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140565V#509F真是的……\n',
            '那些臭味相投的顽固家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140566V#019F确实，无论哪一伙人，\n',
            '都不像是会就此善罢甘休的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140567V#082F总之，警备方面可以放心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140568V问题是，在那个地下遗迹里发生的事情，\n',
            '到底隐含着什么含义呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140569V理查德解开的那个封印，\n',
            '到底会产生什么样的影响呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140570V『辉之环』是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140571V这些事情必须要弄清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140572V#505F嗯……确实是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140573V而且，和上校战斗的时候，\n',
            '我们发现他的记忆好像有些混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140574V#085F嗯，和克鲁茨一样，\n',
            '有些重要的事情想不起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140575V#082F虽然如此，\n',
            '我在审讯他时还是弄清楚了一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140576V就是那个黑色导力器的来历。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130663V#580F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140578V#012F查到制造它的人了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140579V#082F不……仅仅是一些线索。\n',
            '只是知道是谁将这东西带到了情报部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140580V那个人就是情报部特务部队队长\n',
            '洛伦斯·博格少尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121285V#005F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140582V#014F是、是那个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140583V#085F在被招入情报部的时候，\n',
            '他把那个东西交给了理查德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140584V而且，理查德的政变计划，\n',
            '大概也是从那个时候开始的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140585V#082F总之，有必要调查清楚\n',
            '那个洛伦斯少尉的真实身份。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140586V#003F原来是这样啊……\n',
            '虽然不知道他的真正目的是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140587V#006F说起来，那次的战斗还真不可思议，\n',
            '我和雪拉姐她们看见他的样子了呢。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140588V如果有需要的话，\n',
            '我可以画一张肖像画给你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140589V#080F啊，那到时候就拜托了。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140590V#081F虽然对你的绘画水平不敢抱有期望……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140591V不过，既然还有其他人见过，\n',
            '拜托雪拉扎德或者陛下帮忙也可以嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140592V#009F哼，你这是什么意思！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    Fade(1000)
    ChrSetChipByIndex(0x001B, 10)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x001B, 0)
    ChrTurnDirection(0x0102, 0x0101, 0)
    ChrTurnDirection(0x001B, 0x0101, 0)
    OP_6C(0, 0)
    CameraSetDistance(2600, 0)
    MapClearFlags(0x00000001)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020140593V#014F#2P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140594V洛伦斯少尉的脸，你看见过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140595V#501F哎，我没告诉过你吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140596V在女王宫露台上交手的时候，\n',
            '那个少尉把自己的头盔摘掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140597V看样子大概是２５岁左右吧，\n',
            '一头银灰色的头发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140598V#514F#2P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140599V#007F而且女王当时说他的眼神深邃，\n',
            '给人的感觉好像经历过巨大的苦难一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140600V#003F该怎么说呢……表面看来非常冷漠， \n',
            '却从内心深处散发出炽热的情感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140601V而且，逃走的时候还对女王说\n',
            '『您并没有怜悯我的资格』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140602V#013F#2P『您并没有怜悯我的资格』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140603V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140604V#505F约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140605V#080F唉，我说你这孩子，\n',
            '从以前开始就总是顾虑得太多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140606V后面的事情交给我们处理就行了，\n',
            '你和艾丝蒂尔还是尽情享受诞辰庆典吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x001B, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110319V#014F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140608V#010F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140609V#001F是啊是啊。\n',
            '我们一定要玩个痛快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x001B, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010140610V#006F对了，\n',
            '我们今天晚上要在城里住吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001B, 0x0101, 400)

    ChrTalk(
        0x001B,
        (
            '#0160140611V#080F对，女王陛下安排了\n',
            '王城右翼的两间客房给我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140612V我和约修亚在右边，\n',
            '艾丝蒂尔和雪拉扎德在左边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140613V#004F啊……\n',
            '我和雪拉姐住一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140614V#084F难道还有更好的组合吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140615V那么，我和艾丝蒂尔，\n',
            '约修亚和雪拉扎德，这样安排好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140616V#081F你可以尽情向老爸撒娇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140617V#509F……真、真讨厌～\n',
            '还是和雪拉姐一起比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140618V#081F哇哈哈，真是害羞啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140619V#080F那么，晚上再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x001B, 0, 400)

    @scena.Lambda('lambda_5E4F')
    def lambda_5E4F():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_5E4F')

    DispatchAsync2(0x0101, 0x0001, lambda_5E4F)

    @scena.Lambda('lambda_5E60')
    def lambda_5E60():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_5E60')

    DispatchAsync2(0x0102, 0x0001, lambda_5E60)

    CreateThread(0x001B, 0x01, 0x00, func_15_6203)
    Sleep(5000)

    ChrSetFlags(0x001B, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140620V#010F#2P反正已经好久不见了，\n',
            '和父亲住同一个房间不是很好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140621V关于你的母亲……\n',
            '不是有很多话想跟父亲说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140622V#007F虽然是这样没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140623V让约修亚和雪拉姐住同一个房间，\n',
            '这样我是怎么也不能允……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140624V#014F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140625V#503F没、没什么啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140626V#008F不说这个了……\n',
            '我们还是到王城外面逛逛吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140627V街上好像很热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140628V#010F#2P是啊，我们到处转转吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140629V如果逛得感到累了，\n',
            '就去东街区的休息处歇歇脚好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140630V#501F啊，是百货商店后面的休息处吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140631V#001F那么，我们先在街上参观，\n',
            '最后再去那里休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_69(0x0000, 0)
    OP_6A(0x0000)
    OP_92(0x0001, 0x0000, 0, 10000, 0x00)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetDirection(0x0102, 180, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    Sleep(500)

    OP_28(0x004F, 0x01, 0x0020)
    OP_28(0x004F, 0x01, 0x0040)
    OP_28(0x004F, 0x01, 0x0080)
    OP_28(0x004F, 0x01, 0x0100)
    OP_28(0x004F, 0x01, 0x0200)
    OP_28(0x004F, 0x01, 0x0400)
    OP_28(0x004F, 0x01, 0x0800)
    OP_28(0x0050, 0x04, 0x40)
    OP_28(0x0051, 0x04, 0x40)
    MapClearFlags(0x00000800)
    MapClearFlags(0x02000000)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x61A2
@scena.Code('func_12_61A2')
def func_12_61A2():
    ChrMoveToRelative(0x00FE, -3470, 0, 38000, 800, 0x00)

    Return()

# id: 0x0013 offset: 0x61B7
@scena.Code('func_13_61B7')
def func_13_61B7():
    ChrMoveToRelative(0x00FE, -3470, 0, 38000, 800, 0x00)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrTurnDirection(0x0102, 0x001B, 400)

    Return()

# id: 0x0014 offset: 0x61DD
@scena.Code('func_14_61DD')
def func_14_61DD():
    ChrMoveToRelative(0x00FE, -3470, 0, 38000, 800, 0x00)
    ChrSetChipByIndex(0x001B, 10)
    ChrSetSubChip(0x001B, 0)
    ChrTurnDirection(0x001B, 0x0101, 400)

    Return()

# id: 0x0015 offset: 0x6203
@scena.Code('func_15_6203')
def func_15_6203():
    ChrWalkTo(0x001B, 70, 750, 43730, 2000, 0x00)
    ChrWalkTo(0x001B, 400, 750, 48060, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
