import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2520_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2520   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2520.x'
    header.mapIndex       = 1
    header.bgm            = 75
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01780._CH', 'ED6_DT07/CH01780P._CP'),
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
        ('ED6_DT07/CH01373._CH', 'ED6_DT07/CH01373P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01593._CH', 'ED6_DT07/CH01593P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01363._CH', 'ED6_DT07/CH01363P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
    ]

# id: 0x10001 offset: 0x26A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 116010,
            z                   = 0,
            y                   = 4800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '波利',
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特蕾莎院长',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
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
            name                = '达尼艾尔',
            x                   = 6000,
            z                   = 200,
            y                   = 22200,
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
            name                = '玛丽',
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
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
            name                = '克拉姆',
            x                   = 4300,
            z                   = 200,
            y                   = 22900,
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
            name                = '基库',
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '珐奥娜',
            x                   = 41400,
            z                   = 0,
            y                   = 7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '拉迪奥老师',
            x                   = 87700,
            z                   = 0,
            y                   = 1000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 87700,
            z                   = 0,
            y                   = 2800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = 84400,
            z                   = 0,
            y                   = 1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 89260,
            z                   = 0,
            y                   = 1520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = 0,
            z                   = 0,
            y                   = 3100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '坎诺',
            x                   = -2800,
            z                   = 0,
            y                   = 4000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = -700,
            z                   = 0,
            y                   = 4000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 3500,
            z                   = 0,
            y                   = 2000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -3100,
            z                   = 0,
            y                   = 5400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '罗基克',
            x                   = -2900,
            z                   = 0,
            y                   = 30000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '亚吉鲁',
            x                   = -5500,
            z                   = 0,
            y                   = 35500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '罗伊斯',
            x                   = -3400,
            z                   = 0,
            y                   = 28800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = -2000,
            z                   = 0,
            y                   = 700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '塞尔玛',
            x                   = 1500,
            z                   = 0,
            y                   = 34700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '莉秋尔',
            x                   = -6000,
            z                   = 0,
            y                   = 700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '巴托姆',
            x                   = 82700,
            z                   = 0,
            y                   = 33000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '基诺奇奥',
            x                   = 90900,
            z                   = 0,
            y                   = 33400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '妮吉塔',
            x                   = 92300,
            z                   = 0,
            y                   = 33400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '芙拉瑟',
            x                   = 85900,
            z                   = 0,
            y                   = 30400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '蕾娜',
            x                   = 83500,
            z                   = 0,
            y                   = 30000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = -3900,
            z                   = 0,
            y                   = 3100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = -3900,
            z                   = 0,
            y                   = 34700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = -3000,
            z                   = 0,
            y                   = 34100,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 45300,
            z                   = 0,
            y                   = 32600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = 43480,
            z                   = 0,
            y                   = 5500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦教授',
            x                   = 2700,
            z                   = 0,
            y                   = 32500,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = '希艾尔',
            x                   = 89800,
            z                   = 0,
            y                   = 29200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = '爱蕾塔',
            x                   = 88400,
            z                   = 0,
            y                   = 30800,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = '爱珐',
            x                   = 0,
            z                   = 0,
            y                   = 4000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = -6100,
            z                   = 0,
            y                   = 34900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 3060,
            z                   = 0,
            y                   = 30300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = -500,
            z                   = 0,
            y                   = 30900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            name                = '诺莉雅',
            x                   = -100,
            z                   = 0,
            y                   = 32600,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 55,
            chipIndex           = 55,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            name                = '丽泽',
            x                   = 300,
            z                   = 0,
            y                   = 29800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002F,
        ),
        ScenaNpcData(
            name                = '托尼奥',
            x                   = 3090,
            z                   = 0,
            y                   = 32340,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002E,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = -5900,
            z                   = 0,
            y                   = -300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0031,
        ),
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = 41520,
            z                   = 0,
            y                   = 1170,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0030,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 30590,
            z                   = 0,
            y                   = 1500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0032,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 38380,
            z                   = 0,
            y                   = 1600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0033,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 26440,
            z                   = 0,
            y                   = -160,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0034,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 39730,
            z                   = 0,
            y                   = 31370,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0035,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 28810,
            z                   = 0,
            y                   = 31500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0036,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 45020,
            z                   = 0,
            y                   = 30260,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0037,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 57380,
            z                   = 0,
            y                   = 30950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0038,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 43840,
            z                   = 0,
            y                   = 35940,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0039,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 24710,
            z                   = 0,
            y                   = 29820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 45,
            chipIndex           = 45,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x003A,
        ),
        ScenaNpcData(
            name                = 'CH22000',
            x                   = 85590,
            z                   = 700,
            y                   = 3050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835044,
            chipIndex           = 36,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x94A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x94A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 51000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004B,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004C,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004D,
        ),
        ScenaEventData(
            x           = 58990,
            y           = 0,
            z           = 31330,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004E,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 31400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000004F,
        ),
    )

# id: 0x10004 offset: 0x9EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 41160,
            triggerZ            = 0,
            triggerY            = 6230,
            triggerRange        = 400,
            actorX              = 41400,
            actorZ              = 1500,
            actorY              = 7500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 85590,
            triggerZ            = 700,
            triggerY            = 3400,
            triggerRange        = 1000,
            actorX              = 85590,
            actorZ              = 1000,
            actorY              = 3050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 48200,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = 48200,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31580,
            triggerZ            = 0,
            triggerY            = 1450,
            triggerRange        = 800,
            actorX              = 31580,
            actorZ              = 1000,
            actorY              = 1450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 51020,
            triggerZ            = 0,
            triggerY            = 31860,
            triggerRange        = 800,
            actorX              = 51020,
            actorZ              = 1500,
            actorY              = 31860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0040,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57380,
            triggerZ            = 0,
            triggerY            = 31460,
            triggerRange        = 800,
            actorX              = 57380,
            actorZ              = 1000,
            actorY              = 31460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0041,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31630,
            triggerZ            = 0,
            triggerY            = 31460,
            triggerRange        = 800,
            actorX              = 31630,
            actorZ              = 1000,
            actorY              = 31460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0042,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3420,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = 3420,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0043,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3570,
            triggerZ            = 0,
            triggerY            = 34450,
            triggerRange        = 800,
            actorX              = 3570,
            actorZ              = 1200,
            actorY              = 34450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0044,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 790,
            triggerZ            = 0,
            triggerY            = 35530,
            triggerRange        = 800,
            actorX              = 790,
            actorZ              = 1200,
            actorY              = 35530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0045,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5010,
            triggerZ            = 0,
            triggerY            = 29180,
            triggerRange        = 800,
            actorX              = -5010,
            actorZ              = 1200,
            actorY              = 29180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0046,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1970,
            triggerZ            = 0,
            triggerY            = 30780,
            triggerRange        = 800,
            actorX              = -1970,
            actorZ              = 1200,
            actorY              = 30780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0047,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 93560,
            triggerZ            = 0,
            triggerY            = 33350,
            triggerRange        = 800,
            actorX              = 93560,
            actorZ              = 1000,
            actorY              = 33350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0048,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 87220,
            triggerZ            = 0,
            triggerY            = 34060,
            triggerRange        = 800,
            actorX              = 87220,
            actorZ              = 1000,
            actorY              = 34060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0049,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 85030,
            triggerZ            = 0,
            triggerY            = 33920,
            triggerRange        = 800,
            actorX              = 85030,
            actorZ              = 1000,
            actorY              = 33920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x004A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xC06
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_C14',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_3B_5F9C)

    def _loc_C14(): pass

    label('loc_C14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_C7B',
    )

    ChrSetPos(0x0010, 5320, 250, 2110, 270)
    ChrSetPos(0x0011, 5300, 250, 32080, 267)
    ChrSetFlags(0x0011, 0x0010)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, 400, 0, 0, 90)
    ChrSetFlags(0x0014, 0x0004)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetPos(0x0019, -2900, 0, 30000, 90)

    Jump('loc_12BA')

    def _loc_C7B(): pass

    label('loc_C7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_CBC',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001D, 0x0080)

    Jump('loc_12BA')

    def _loc_CBC(): pass

    label('loc_CBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_F31',
    )

    ChrSetPos(0x0012, 95370, 250, 34220, 225)
    ChrSetPos(0x0008, 43470, 0, 5280, 225)
    CreateThread(0x0008, 0x00, 0x00, func_02_1340)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0025, 42090, 0, 3930, 45)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0026, 42970, 0, 2640, 0)
    ChrSetPos(0x0017, -1590, 0, 34700, 0)
    ChrSetPos(0x0010, 2790, 0, 5460, 225)
    ChrSetPos(0x0015, 4500, 250, 2970, 270)
    ChrSetPos(0x0016, -990, 0, -1260, 0)
    ChrSetChipByIndex(0x0016, 47)
    CreateThread(0x0016, 0x00, 0x00, func_03_14EE)
    ChrSetPos(0x0018, -4990, 0, 5010, 180)
    ChrSetChipByIndex(0x0018, 46)
    CreateThread(0x0018, 0x00, 0x00, func_04_153B)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetChipByIndex(0x001E, 51)
    ChrSetPos(0x001E, -6000, 100, 700, 90)
    TerminateThread(0x001E, 0xFF)
    ChrSetFlags(0x001E, 0x0004)
    ChrSetFlags(0x001E, 0x0010)
    ChrClearFlags(0x0032, 0x0080)
    ChrSetChipByIndex(0x0032, 52)
    ChrSetPos(0x0032, -5960, 0, 3010, 90)
    TerminateThread(0x0032, 0xFF)
    ChrSetFlags(0x0032, 0x0004)
    ChrSetFlags(0x0032, 0x0010)
    ChrClearFlags(0x0031, 0x0080)
    ChrSetPos(0x0031, -4000, 0, 4100, 270)
    ChrSetChipByIndex(0x0031, 53)
    TerminateThread(0x0031, 0xFF)
    ChrSetFlags(0x0031, 0x0004)
    ChrSetFlags(0x0031, 0x0010)
    ChrSetPos(0x0014, -70, 0, 3050, 270)
    ChrSetChipByIndex(0x0014, 54)
    TerminateThread(0x0014, 0xFF)
    ChrSetFlags(0x0014, 0x0004)
    ChrSetFlags(0x0014, 0x0010)
    ChrSetPos(0x0011, -6910, 0, 33220, 90)
    ChrSetPos(0x0019, 1300, 0, 28510, 90)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002E, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x0021, 89110, 0, 29220, 90)
    ChrSetFlags(0x0021, 0x0010)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, 89160, 0, 34290, 0)
    ChrClearFlags(0x0033, 0x0080)
    ChrSetPos(0x0033, 85890, 0, 32890, 315)
    ChrClearFlags(0x002C, 0x0080)
    ChrSetPos(0x002C, 90550, 0, 29250, 270)
    ChrClearFlags(0x0027, 0x0080)
    ChrSetFlags(0x0027, 0x0010)
    ChrClearFlags(0x002A, 0x0080)
    ChrSetPos(0x002A, 31660, 0, 100, 0)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x002B, 0x0010)
    ChrSetPos(0x002B, 32619, 0, 320, 270)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)

    Jump('loc_12BA')

    def _loc_F31(): pass

    label('loc_F31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1143',
    )

    ChrSetPos(0x0011, -6910, 0, 33220, 90)
    ChrSetPos(0x0012, 95370, 250, 34220, 225)
    ChrSetPos(0x0008, 42940, 0, 1070, 270)
    ChrSetFlags(0x0008, 0x0010)
    CreateThread(0x0008, 0x00, 0x00, func_02_1340)
    ChrClearFlags(0x0034, 0x0080)
    ChrSetFlags(0x0034, 0x0010)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetPos(0x0010, 2790, 0, 5460, 225)
    ChrSetPos(0x0015, 4500, 250, 2970, 270)
    ChrSetPos(0x0016, -990, 0, -1260, 0)
    ChrSetChipByIndex(0x0016, 47)
    CreateThread(0x0016, 0x00, 0x00, func_03_14EE)
    ChrSetPos(0x0018, -4990, 0, 5010, 180)
    ChrSetChipByIndex(0x0018, 46)
    CreateThread(0x0018, 0x00, 0x00, func_04_153B)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetChipByIndex(0x0024, 48)
    ChrSetPos(0x0024, -4019, 100, 3080, 270)
    TerminateThread(0x0024, 0xFF)
    ChrSetFlags(0x0024, 0x0004)
    ChrSetFlags(0x0024, 0x0010)
    ChrClearFlags(0x0033, 0x0080)
    ChrSetPos(0x0033, -5040, 100, 2050, 0)
    ChrClearFlags(0x002C, 0x0080)
    ChrSetChipByIndex(0x002C, 50)
    ChrSetPos(0x002C, -130, 0, 4000, 270)
    TerminateThread(0x002C, 0xFF)
    ChrSetFlags(0x002C, 0x0004)
    ChrSetFlags(0x002C, 0x0010)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, -1960, 0, -300, 90)
    ChrSetChipByIndex(0x001C, 49)
    TerminateThread(0x001C, 0xFF)
    ChrSetFlags(0x001C, 0x0004)
    ChrSetFlags(0x001C, 0x0010)
    ChrSetPos(0x0019, 1300, 0, 28510, 90)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetFlags(0x0020, 0x0010)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetFlags(0x0025, 0x0010)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetFlags(0x0026, 0x0010)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0035, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x0037, 0x0080)
    ChrClearFlags(0x0038, 0x0080)
    ChrClearFlags(0x0039, 0x0080)
    ChrClearFlags(0x003A, 0x0080)
    ChrClearFlags(0x003B, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008B, 2, 0x45A)),
            Expr.Return,
        ),
        'loc_1140',
    )

    ChrSetPos(0x0025, 88600, 0, 34670, 0)
    ChrSetPos(0x0026, 89570, 0, 34410, 270)
    ChrSetPos(0x0029, -1680, 0, 34680, 0)
    ChrClearFlags(0x0029, 0x0080)

    def _loc_1140(): pass

    label('loc_1140')

    Jump('loc_12BA')

    def _loc_1143(): pass

    label('loc_1143')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1199',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetPos(0x0015, -5200, 0, 2050, 0)
    ChrSetPos(0x0016, 4500, 250, 4019, 270)
    ChrSetPos(0x0019, 790, 0, 34680, 0)

    Jump('loc_12BA')

    def _loc_1199(): pass

    label('loc_1199')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_11C8',
    )

    ChrSetPos(0x0011, 5300, 250, 32080, 267)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)

    Jump('loc_12BA')

    def _loc_11C8(): pass

    label('loc_11C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_11FF',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)

    Jump('loc_12BA')

    def _loc_11FF(): pass

    label('loc_11FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_123B',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)

    Jump('loc_12BA')

    def _loc_123B(): pass

    label('loc_123B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_127C',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)

    Jump('loc_12BA')

    def _loc_127C(): pass

    label('loc_127C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_12BA',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)

    def _loc_12BA(): pass

    label('loc_12BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 3, 0x453)),
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 4, 0x454)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 5, 0x455)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 6, 0x456)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 7, 0x457)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12D4',
    )

    SetScenaFlags(ScenaFlag(0x0088, 3, 0x443))

    def _loc_12D4(): pass

    label('loc_12D4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006E, 'loc_12E0'),
        (-1, 'loc_12F6'),
    )

    def _loc_12E0(): pass

    label('loc_12E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008B, 2, 0x45A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12F3',
    )

    SetScenaFlags(ScenaFlag(0x0086, 2, 0x432))
    Event(0, func_3C_6321)

    def _loc_12F3(): pass

    label('loc_12F3')

    Jump('loc_12F6')

    def _loc_12F6(): pass

    label('loc_12F6')

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x1308
@scena.Code('func_01_1308')
def func_01_1308():
    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_131B',
    )

    OP_65(0x01, 0x0001)

    def _loc_131B(): pass

    label('loc_131B')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_132F',
    )

    OP_64(0x01, 0x0001)
    ChrSetFlags(0x003E, 0x0080)

    def _loc_132F(): pass

    label('loc_132F')

    OP_75(0x06, 0x00000000, 0x00)
    OP_74(0x0006, 0x00000000, 0x0000)

    Return()

# id: 0x0002 offset: 0x1340
@scena.Code('func_02_1340')
def func_02_1340():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_134A',
    )

    Jump('loc_1371')

    def _loc_134A(): pass

    label('loc_134A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_135F',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1371')

    def _loc_135F(): pass

    label('loc_135F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1371',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1371(): pass

    label('loc_1371')

    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1396',
    )

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_14D8')

    def _loc_1396(): pass

    label('loc_1396')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13AF',
    )

    OP_99(0x00FE, 0x01, 0x07, 1300)

    Jump('loc_14D8')

    def _loc_13AF(): pass

    label('loc_13AF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13C8',
    )

    OP_99(0x00FE, 0x02, 0x07, 1250)

    Jump('loc_14D8')

    def _loc_13C8(): pass

    label('loc_13C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13E1',
    )

    OP_99(0x00FE, 0x03, 0x07, 1200)

    Jump('loc_14D8')

    def _loc_13E1(): pass

    label('loc_13E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13FA',
    )

    OP_99(0x00FE, 0x04, 0x07, 1150)

    Jump('loc_14D8')

    def _loc_13FA(): pass

    label('loc_13FA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1413',
    )

    OP_99(0x00FE, 0x05, 0x07, 1100)

    Jump('loc_14D8')

    def _loc_1413(): pass

    label('loc_1413')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_142C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1050)

    Jump('loc_14D8')

    def _loc_142C(): pass

    label('loc_142C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1445',
    )

    OP_99(0x00FE, 0x00, 0x07, 1355)

    Jump('loc_14D8')

    def _loc_1445(): pass

    label('loc_1445')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_145E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1305)

    Jump('loc_14D8')

    def _loc_145E(): pass

    label('loc_145E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1477',
    )

    OP_99(0x00FE, 0x02, 0x07, 1255)

    Jump('loc_14D8')

    def _loc_1477(): pass

    label('loc_1477')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1490',
    )

    OP_99(0x00FE, 0x03, 0x07, 1205)

    Jump('loc_14D8')

    def _loc_1490(): pass

    label('loc_1490')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14A9',
    )

    OP_99(0x00FE, 0x04, 0x07, 1155)

    Jump('loc_14D8')

    def _loc_14A9(): pass

    label('loc_14A9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1105)

    Jump('loc_14D8')

    def _loc_14C2(): pass

    label('loc_14C2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14D8',
    )

    OP_99(0x00FE, 0x06, 0x07, 1055)

    def _loc_14D8(): pass

    label('loc_14D8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_14ED',
    )

    OP_99(0x00FE, 0x00, 0x07, 1200)

    Jump('loc_14D8')

    def _loc_14ED(): pass

    label('loc_14ED')

    Return()

# id: 0x0003 offset: 0x14EE
@scena.Code('func_03_14EE')
def func_03_14EE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_153A',
    )

    ChrWalkTo(0x00FE, -5030, 0, -1260, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, -990, 0, -1260, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('func_03_14EE')

    def _loc_153A(): pass

    label('loc_153A')

    Return()

# id: 0x0004 offset: 0x153B
@scena.Code('func_04_153B')
def func_04_153B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_163F',
    )

    ChrWalkTo(0x00FE, -1010, 0, 4950, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 1490, 0, 4950, 2000, 0x00)
    ChrWalkTo(0x00FE, 1490, 0, 3480, 2000, 0x00)
    ChrWalkTo(0x00FE, 1990, 0, 3090, 2000, 0x00)
    ChrWalkTo(0x00FE, 2540, 0, 2950, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 1990, 0, 3090, 2000, 0x00)
    ChrWalkTo(0x00FE, 1490, 0, 3480, 2000, 0x00)
    ChrWalkTo(0x00FE, 1490, 0, 4950, 2000, 0x00)
    ChrWalkTo(0x00FE, -1010, 0, 4950, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, -4990, 0, 5010, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(3000)

    Jump('func_04_153B')

    def _loc_163F(): pass

    label('loc_163F')

    Return()

# id: 0x0005 offset: 0x1640
@scena.Code('func_05_1640')
def func_05_1640():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1663',
    )

    OP_8D(0x00FE, 24420, 1500, 29350, -1300, 1500)

    Jump('func_05_1640')

    def _loc_1663(): pass

    label('loc_1663')

    Return()

# id: 0x0006 offset: 0x1664
@scena.Code('func_06_1664')
def func_06_1664():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1687',
    )

    OP_8D(0x00FE, 38740, 33660, 43330, 28250, 1500)

    Jump('func_06_1664')

    def _loc_1687(): pass

    label('loc_1687')

    Return()

# id: 0x0007 offset: 0x1688
@scena.Code('func_07_1688')
def func_07_1688():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16AB',
    )

    OP_8D(0x00FE, 42670, 31640, 49420, 28690, 2000)

    Jump('func_07_1688')

    def _loc_16AB(): pass

    label('loc_16AB')

    Return()

# id: 0x0008 offset: 0x16AC
@scena.Code('func_08_16AC')
def func_08_16AC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16CF',
    )

    OP_8D(0x00FE, 23100, 31490, 27030, 28520, 3000)

    Jump('func_08_16AC')

    def _loc_16CF(): pass

    label('loc_16CF')

    Return()

# id: 0x0009 offset: 0x16D0
@scena.Code('func_09_16D0')
def func_09_16D0():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_17F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_177B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530850020V#780F是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850021V犯人总算给逮捕归案了，\n',
            '实在是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850022V等会儿我想听你们\n',
            '说明一下事情的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17F0')

    def _loc_177B(): pass

    label('loc_177B')

    ChrTalk(
        0x00FE,
        (
            '#0530850023V#780F抓到袭击孤儿院的犯人\n',
            '总算是让大家安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850024V你们等会儿可以把\n',
            '把事情的经过告诉我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17F0(): pass

    label('loc_17F0')

    Jump('loc_1D60')

    def _loc_17F3(): pass

    label('loc_17F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_191B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18B6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530850014V#780F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850015V我听说特蕾莎院长的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850016V怎么说呢……\n',
            '实在是很过分的事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850017V这件事实在无法用语言表达……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1918')

    def _loc_18B6(): pass

    label('loc_18B6')

    ChrTalk(
        0x00FE,
        (
            '#0530850018V#780F我听说特蕾莎院长的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850019V怎么说呢……\n',
            '实在是很过分的事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1918(): pass

    label('loc_1918')

    Jump('loc_1D60')

    def _loc_191B(): pass

    label('loc_191B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1A77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A01',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530850009V#780F艾丝蒂尔、约修亚，\n',
            '这次真是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850010V舞台剧的演出很成功。\n',
            '特别是约修亚饰演的塞茜莉亚公主，\n',
            '演技和扮相实在是太感人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850011V下次有机会的话\n',
            '请务必再到我们学院来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A74')

    def _loc_1A01(): pass

    label('loc_1A01')

    ChrTalk(
        0x00FE,
        (
            '#0530850012V#780F艾丝蒂尔、约修亚，\n',
            '这次真是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850013V下次有机会的话\n',
            '请务必再到我们学院来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A74(): pass

    label('loc_1A74')

    Jump('loc_1D60')

    def _loc_1A77(): pass

    label('loc_1A77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1B51',
    )

    ChrClearFlags(0x0008, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B0A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530060101V#780F哦，是你们。\n',
            '这次真是史无前例的盛况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060102V大家都很期待舞台剧，\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B4E')

    def _loc_1B0A(): pass

    label('loc_1B0A')

    ChrTalk(
        0x00FE,
        (
            '#0530060103V#780F大家都很期待舞台剧。\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B4E(): pass

    label('loc_1B4E')

    Jump('loc_1D60')

    def _loc_1B51(): pass

    label('loc_1B51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1CE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 7, 0x457)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C59',
    )

    SetScenaFlags(ScenaFlag(0x008A, 7, 0x457))
    OP_4A(0x0034, 255)

    ChrTalk(
        0x0008,
        (
            '#0530060079V#781F戴尔蒙市长，\n',
            '自从去年的王国会议之后我们也好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060080V这段时间，你身体怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '#0490060081V#661F就像你看到的，结实着呢。\n',
            '科林兹校长也很精神嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490060082V今天我打算好好放松一下。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0010)
    ChrClearFlags(0x0034, 0x0010)
    OP_4B(0x0034, 255)

    Jump('loc_1CE1')

    def _loc_1C59(): pass

    label('loc_1C59')

    ChrTalk(
        0x0008,
        (
            '#0530060083V#781F我还要找时间和市长先生谈谈\n',
            '关于学院运营的事情呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060084V虽说是王立的教育机构，\n',
            '但也要重视地方上的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CE1(): pass

    label('loc_1CE1')

    Jump('loc_1D60')

    def _loc_1CE4(): pass

    label('loc_1CE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1D60',
    )

    ChrTalk(
        0x00FE,
        (
            '#0530060085V#780F你们住宿的地方我们已经给安排好了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060086V学院里也有食堂，\n',
            '你们就安心准备好舞台剧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D60(): pass

    label('loc_1D60')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0x1D64
@scena.Code('func_0A_1D64')
def func_0A_1D64():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x1D69
@scena.Code('func_0B_1D69')
def func_0B_1D69():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1E00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DDC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '啊，怎么了？\n',
            '你们要找人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '现在正好是\n',
            '上课结束的时间。\n',
            '你们可以去和同学们见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DFD')

    def _loc_1DDC(): pass

    label('loc_1DDC')

    ChrTalk(
        0x000F,
        (
            '啊，怎么了？\n',
            '你们要找人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DFD(): pass

    label('loc_1DFD')

    Jump('loc_23CA')

    def _loc_1E00(): pass

    label('loc_1E00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1E4B',
    )

    ChrTalk(
        0x000F,
        (
            '呵呵，学园祭很成功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '学生们正在\n',
            '礼堂那里庆祝胜利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CA')

    def _loc_1E4B(): pass

    label('loc_1E4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1EA9',
    )

    ChrTalk(
        0x000F,
        (
            '说起来\n',
            '真是出乎意料的盛况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '很多人还带了孩子来，\n',
            '要是有小孩迷路就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CA')

    def _loc_1EA9(): pass

    label('loc_1EA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1F84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F37',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '各种活动都在\n',
            '校园和主楼里进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '下午礼堂那边\n',
            '预定要演出舞台剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '食堂作为休息场所开放，\n',
            '你们可以好好利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F81')

    def _loc_1F37(): pass

    label('loc_1F37')

    ChrTalk(
        0x000F,
        (
            '各种活动都在\n',
            '校园和主楼里进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '下午礼堂那边\n',
            '预定要演出舞台剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F81(): pass

    label('loc_1F81')

    Jump('loc_23CA')

    def _loc_1F84(): pass

    label('loc_1F84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2015',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FE9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '准备完成了吗？\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '到了明天\n',
            '就会有许多客人来参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2012')

    def _loc_1FE9(): pass

    label('loc_1FE9')

    ChrTalk(
        0x000F,
        (
            '准备完成了吗？\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2012(): pass

    label('loc_2012')

    Jump('loc_23CA')

    def _loc_2015(): pass

    label('loc_2015')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_20CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2096',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '呵呵，一到下课时间，\n',
            '校园里就会变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '学园祭就要开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '希望同学们\n',
            '都能加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20CB')

    def _loc_2096(): pass

    label('loc_2096')

    ChrTalk(
        0x000F,
        (
            '呵呵，一到下课时间，\n',
            '校园里就会变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20CB(): pass

    label('loc_20CB')

    Jump('loc_23CA')

    def _loc_20CE(): pass

    label('loc_20CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_21E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21A2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '啊，科洛丝。\n',
            '你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对不起，\n',
            '我到现在才回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '呵呵，回来就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要找校长的话，\n',
            '他就在办公室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '他也很担心\n',
            '科洛丝你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，是的。\n',
            '我们现在就过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E4')

    def _loc_21A2(): pass

    label('loc_21A2')

    ChrTalk(
        0x000F,
        (
            '要找校长的话，\n',
            '他就在办公室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '他也很担心\n',
            '科洛丝你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21E4(): pass

    label('loc_21E4')

    Jump('loc_23CA')

    def _loc_21E7(): pass

    label('loc_21E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_22A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_227A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '啊，科洛丝。\n',
            '你们外出回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，不是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，\n',
            '我们还没有办完事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '是吗。\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_229D')

    def _loc_227A(): pass

    label('loc_227A')

    ChrTalk(
        0x000F,
        (
            '科洛丝，\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_229D(): pass

    label('loc_229D')

    Jump('loc_23CA')

    def _loc_22A0(): pass

    label('loc_22A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_22F2',
    )

    ChrTalk(
        0x000F,
        (
            '啊，是想参观吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '很抱歉，\n',
            '现在学生们正在上课，\n',
            '不能带您参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CA')

    def _loc_22F2(): pass

    label('loc_22F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_23CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_239A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000F,
        (
            '啊，科洛丝。\n',
            '已经回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不是，\n',
            '我正要带这两位朋友去卢安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '是吗，难得的假日，\n',
            '就好好地放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CA')

    def _loc_239A(): pass

    label('loc_239A')

    ChrTalk(
        0x000F,
        (
            '科洛丝，\n',
            '难得的假日，\n',
            '就好好地放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23CA(): pass

    label('loc_23CA')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0x23CE
@scena.Code('func_0C_23CE')
def func_0C_23CE():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_240A',
    )

    ChrTalk(
        0x00FE,
        (
            '课虽然上完了，\n',
            '但还有学生们的问题要回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25E7')

    def _loc_240A(): pass

    label('loc_240A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_245C',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '我们班的同学干劲热火朝天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家做布景\n',
            '也非常地努力嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25E7')

    def _loc_245C(): pass

    label('loc_245C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_24AC',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭的主角\n',
            '果然还是学生们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都比平时\n',
            '要活跃许多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25E7')

    def _loc_24AC(): pass

    label('loc_24AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_258C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_254A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '你们好像是\n',
            '从洛连特来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我也是\n',
            '洛连特出身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来我父母\n',
            '也要来参观学园祭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我要是能招待他们就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2589')

    def _loc_254A(): pass

    label('loc_254A')

    ChrTalk(
        0x00FE,
        (
            '对了对了……\n',
            '舞台剧表演我也看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那天真是很开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2589(): pass

    label('loc_2589')

    Jump('loc_25E7')

    def _loc_258C(): pass

    label('loc_258C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_25E7',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭快到了，\n',
            '同学们就连上课\n',
            '都开始坐不安定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这也是没办法的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25E7(): pass

    label('loc_25E7')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0x25EB
@scena.Code('func_0D_25EB')
def func_0D_25EB():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_267B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2651',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '唔唔，\n',
            '这个问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么做好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0011, 0x0010)

    Jump('loc_2678')

    def _loc_2651(): pass

    label('loc_2651')

    ChrTalk(
        0x00FE,
        (
            '呼，这里的学生\n',
            '都很热心于学习呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2678(): pass

    label('loc_2678')

    Jump('loc_28A5')

    def _loc_267B(): pass

    label('loc_267B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_26DD',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，真没劲……\n',
            '还没到演出的时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托你们二位了！\n',
            '我相信一定能取得成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28A5')

    def _loc_26DD(): pass

    label('loc_26DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_278B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2767',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我们班的同学相当认真呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我觉得\n',
            '研究发表什么的太朴素了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这样也好，\n',
            '有很多客人来看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2788')

    def _loc_2767(): pass

    label('loc_2767')

    ChrTalk(
        0x00FE,
        (
            '决不能输给\n',
            '米丽亚的班级……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2788(): pass

    label('loc_2788')

    Jump('loc_28A5')

    def _loc_278B(): pass

    label('loc_278B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_28A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_287E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F碧欧拉老师，\n',
            '我刚刚才回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，\n',
            '我又没来上课。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不是有重要的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时间的话来一下办公室，\n',
            '我给你漏下的上课笔记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，我过会儿就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28A5')

    def _loc_287E(): pass

    label('loc_287E')

    ChrTalk(
        0x00FE,
        (
            '我还是趁现在\n',
            '批改一下考试卷子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28A5(): pass

    label('loc_28A5')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x28A9
@scena.Code('func_0E_28A9')
def func_0E_28A9():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_28FF',
    )

    ChrTalk(
        0x00FE,
        (
            '我是今年\n',
            '入学考试的出题老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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
            '我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BAD')

    def _loc_28FF(): pass

    label('loc_28FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_29F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2999',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '为什么我们班的同学\n',
            '尽办些游戏和占卜的活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维奥拉的班级\n',
            '都是很正经的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个班的老师不行，\n',
            '学生们却都很优秀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29F3')

    def _loc_2999(): pass

    label('loc_2999')

    ChrTalk(
        0x00FE,
        (
            '为什么我们班的同学\n',
            '尽办些游戏和占卜的活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维奥拉的班级\n',
            '都是很正经的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29F3(): pass

    label('loc_29F3')

    Jump('loc_2BAD')

    def _loc_29F6(): pass

    label('loc_29F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2A2A',
    )

    ChrTalk(
        0x00FE,
        (
            '人还真是多呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都很闲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BAD')

    def _loc_2A2A(): pass

    label('loc_2A2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2AC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A95',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论怎样，\n',
            '那天我可不能再啰嗦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AC4')

    def _loc_2A95(): pass

    label('loc_2A95')

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AC4(): pass

    label('loc_2AC4')

    Jump('loc_2BAD')

    def _loc_2AC7(): pass

    label('loc_2AC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2BAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B57',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '在学园祭的准备期间，\n',
            '大家学习都提不起精神来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算在课上\n',
            '也开始不愿动脑筋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要明天\n',
            '来次突击测验呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BAD')

    def _loc_2B57(): pass

    label('loc_2B57')

    ChrTalk(
        0x00FE,
        (
            '在学园祭的准备期间，\n',
            '大家学习都提不起精神来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要明天\n',
            '来次突击测验呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BAD(): pass

    label('loc_2BAD')

    TalkEnd(0x0012)

    Return()

# id: 0x000F offset: 0x2BB1
@scena.Code('func_0F_2BB1')
def func_0F_2BB1():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2BFF',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，差不多该去巡视了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要看看\n',
            '有没有同学太过懒散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E85')

    def _loc_2BFF(): pass

    label('loc_2BFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2CEF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2C7D',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，昨天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是个不称职的老师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了防止再发生突发事件，\n',
            '我在这里待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2C7D(): pass

    label('loc_2C7D')

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '有学生说在旧校舍看到了魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了慎重起见，\n',
            '我把旧校舍的门锁紧了。\n',
            '不过一会儿还是再去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CEC(): pass

    label('loc_2CEC')

    Jump('loc_2E85')

    def _loc_2CEF(): pass

    label('loc_2CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_2DF8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D91',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '这个学园一共设立了\n',
            '三个方向的专业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我教的科目则是\n',
            '所有专业都必修的科目——体育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时候我没有课，\n',
            '就来整理一下教案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DF5')

    def _loc_2D91(): pass

    label('loc_2D91')

    ChrTalk(
        0x00FE,
        (
            '我教的科目则是\n',
            '所有专业都必修的科目——体育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时候我没有课，\n',
            '就来整理一下教案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DF5(): pass

    label('loc_2DF5')

    Jump('loc_2E85')

    def _loc_2DF8(): pass

    label('loc_2DF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2E85',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E64',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '唔，怎么，\n',
            '你们是哪个班的学生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在上课哦。\n',
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E85')

    def _loc_2E64(): pass

    label('loc_2E64')

    ChrTalk(
        0x00FE,
        (
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E85(): pass

    label('loc_2E85')

    TalkEnd(0x0013)

    Return()

# id: 0x0010 offset: 0x2E89
@scena.Code('func_10_2E89')
def func_10_2E89():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2EFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EDD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '今天的课总算上完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EFA')

    def _loc_2EDD(): pass

    label('loc_2EDD')

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EFA(): pass

    label('loc_2EFA')

    Jump('loc_2FBB')

    def _loc_2EFD(): pass

    label('loc_2EFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2FBB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F75',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '我一直在照顾\n',
            '我们社团的店面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '班里的活动\n',
            '就没办法参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '感觉真是很充实呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBB')

    def _loc_2F75(): pass

    label('loc_2F75')

    ChrTalk(
        0x00FE,
        (
            '我一直在照顾\n',
            '我们社团的店面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '都顾不上照顾\n',
            '班里的茶座了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FBB(): pass

    label('loc_2FBB')

    TalkEnd(0x0014)

    Return()

# id: 0x0011 offset: 0x2FBF
@scena.Code('func_11_2FBF')
def func_11_2FBF():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x2FC4
@scena.Code('func_12_2FC4')
def func_12_2FC4():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2FD1',
    )

    Jump('loc_3047')

    def _loc_2FD1(): pass

    label('loc_2FD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3047',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3033',
    )

    OP_0D()
    OP_A9(0x31)
    OP_56(0x00)
    TalkEnd(0x0015)

    Return()

    def _loc_3033(): pass

    label('loc_3033')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3044',
    )

    TalkEnd(0x0015)

    Return()

    def _loc_3044(): pass

    label('loc_3044')

    Jump('loc_3047')

    def _loc_3047(): pass

    label('loc_3047')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3090',
    )

    ChrTalk(
        0x0015,
        (
            '那么，该去社团活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '今天要把\n',
            '画到一半的绘画完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3286')

    def _loc_3090(): pass

    label('loc_3090')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_30D3',
    )

    ChrTalk(
        0x0015,
        (
            '嗯，\n',
            '茶座还是要办成这样才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '辛苦也值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3286')

    def _loc_30D3(): pass

    label('loc_30D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3139',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3113',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0015,
        (
            '……那边桌子的客人\n',
            '难道是真正的女佣？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3136')

    def _loc_3113(): pass

    label('loc_3113')

    ChrTalk(
        0x0015,
        (
            '因为通宵工作，\n',
            '现在好困啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3136(): pass

    label('loc_3136')

    Jump('loc_3286')

    def _loc_3139(): pass

    label('loc_3139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_31D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3188',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0015,
        (
            '唔哇哇！\n',
            '怎么回事！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '呆在这里\n',
            '会来不及准备的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31D0')

    def _loc_3188(): pass

    label('loc_3188')

    ChrTalk(
        0x0015,
        (
            '……难道说\n',
            '这样下去要通宵赶工了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '呼，\n',
            '做衣服花了太多时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31D0(): pass

    label('loc_31D0')

    Jump('loc_3286')

    def _loc_31D3(): pass

    label('loc_31D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_3286',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3268',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0015,
        (
            '啦啦啦～～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我正在做\n',
            '摆摊时穿的衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '唔～就是要在这种时候集中精力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '因为做这种东西\n',
            '是我最喜欢干的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3286')

    def _loc_3268(): pass

    label('loc_3268')

    ChrTalk(
        0x0015,
        (
            '接下来还要做房间的装饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3286(): pass

    label('loc_3286')

    TalkEnd(0x0015)

    Return()

# id: 0x0013 offset: 0x328A
@scena.Code('func_13_328A')
def func_13_328A():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_32D0',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果需要的话，\n',
            '我可以帮你们找空位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3400')

    def _loc_32D0(): pass

    label('loc_32D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3316',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，这件制服很可爱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '坎诺还为我准备了好多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3400')

    def _loc_3316(): pass

    label('loc_3316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_3380',
    )

    ChrTalk(
        0x00FE,
        (
            '一想时间还很充裕\n',
            '就不由自主地松懈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过应该还来得及。\n',
            '努力把店面打扮得漂亮一些吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3400')

    def _loc_3380(): pass

    label('loc_3380')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_3400',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33D1',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '坎诺君的手\n',
            '可巧啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次他缝了个\n',
            '布娃娃给我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3400')

    def _loc_33D1(): pass

    label('loc_33D1')

    ChrTalk(
        0x00FE,
        (
            '就算是演出用的女佣服装\n',
            '也是他自己做的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3400(): pass

    label('loc_3400')

    TalkEnd(0x0016)

    Return()

# id: 0x0014 offset: 0x3404
@scena.Code('func_14_3404')
def func_14_3404():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_34C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3490',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '刚才讲的课，\n',
            '有一些地方不明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我还想问问老师呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米丽亚老师\n',
            '才刚上完课\n',
            '就马上回办公室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34BE')

    def _loc_3490(): pass

    label('loc_3490')

    ChrTalk(
        0x00FE,
        (
            '米丽亚老师\n',
            '才刚上完课\n',
            '就马上回办公室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34BE(): pass

    label('loc_34BE')

    Jump('loc_3592')

    def _loc_34C1(): pass

    label('loc_34C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_3592',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_354D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '社会系各位的作品\n',
            '都是研究成果发表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇……真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们系的同学\n',
            '只会办茶座或者\n',
            '鬼怪屋什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3592')

    def _loc_354D(): pass

    label('loc_354D')

    ChrTalk(
        0x00FE,
        (
            '社会系各位的作品\n',
            '都是研究成果发表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇……真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3592(): pass

    label('loc_3592')

    TalkEnd(0x0017)

    Return()

# id: 0x0015 offset: 0x3596
@scena.Code('func_15_3596')
def func_15_3596():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_35D0',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是我们的茶座『芳塔娜』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3613')

    def _loc_35D0(): pass

    label('loc_35D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3613',
    )

    ChrTalk(
        0x00FE,
        (
            '穿成这个样子\n',
            '虽然有点不好意思，\n',
            '但为了学园祭，忍了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3613(): pass

    label('loc_3613')

    TalkEnd(0x0018)

    Return()

# id: 0x0016 offset: 0x3617
@scena.Code('func_16_3617')
def func_16_3617():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_364B',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '今天也是很有意义的一课啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BF7')

    def _loc_364B(): pass

    label('loc_364B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_375E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36F5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '有很多前辈\n',
            '和市民们前来参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然办娱乐活动很有意思，\n',
            '不过公布我们的研究成果也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽说如此，\n',
            '考试也不会得到更高的分数。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_375B')

    def _loc_36F5(): pass

    label('loc_36F5')

    ChrTalk(
        0x00FE,
        (
            '有很多前辈\n',
            '和市民们前来参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然办娱乐活动很有意思，\n',
            '不过公布我们的研究成果也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_375B(): pass

    label('loc_375B')

    Jump('loc_3BF7')

    def _loc_375E(): pass

    label('loc_375E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_39FD',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_384B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3825',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '我们社会系发表了\n',
            '从各种产业的经济指标上\n',
            '进行经济动向的预测的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也收集了\n',
            '通俗易懂的关于卢安地区\n',
            '历史和发展的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3848')

    def _loc_3825(): pass

    label('loc_3825')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3848(): pass

    label('loc_3848')

    Jump('loc_39FA')

    def _loc_384B(): pass

    label('loc_384B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3950',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '我们社会系发表了\n',
            '从各种产业的经济指标上\n',
            '进行经济动向的预测的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也收集了\n',
            '通俗易懂的关于卢安地区\n',
            '历史和发展的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有几份资料没到手，\n',
            '但在这么点时间里，\n',
            '能做成这么完善的内容也算不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39FA')

    def _loc_3950(): pass

    label('loc_3950')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_39D8',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然没赶上这次发表，\n',
            '但是《卢安经济史》是很贵重的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们看到那三本书的话，\n',
            '麻烦帮我放回资料室的书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39FA')

    def _loc_39D8(): pass

    label('loc_39D8')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39FA(): pass

    label('loc_39FA')

    Jump('loc_3BF7')

    def _loc_39FD(): pass

    label('loc_39FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_3AB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A88',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '唔，还是需要一些\n',
            '辅助研究的资料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '时间不够了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在有限的时间里，\n',
            '内容已经可算是做得很完善了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AB1')

    def _loc_3A88(): pass

    label('loc_3A88')

    ChrTalk(
        0x00FE,
        (
            '唔，还是需要一些\n',
            '辅助研究的资料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AB1(): pass

    label('loc_3AB1')

    Jump('loc_3BF7')

    def _loc_3AB4(): pass

    label('loc_3AB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_3BF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BD9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你终于回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们班级的节目\n',
            '准备工作进展得很顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们舞台剧方面怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说连主要演员\n',
            '都还没决定下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F呵呵，罗基克，\n',
            '那件事已经解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '舞台剧方面我们不会输的。\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BF7')

    def _loc_3BD9(): pass

    label('loc_3BD9')

    ChrTalk(
        0x00FE,
        (
            '科洛丝，我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BF7(): pass

    label('loc_3BF7')

    TalkEnd(0x0019)

    Return()

# id: 0x0017 offset: 0x3BFB
@scena.Code('func_17_3BFB')
def func_17_3BFB():
    TalkBegin(0x001A)

    ChrTalk(
        0x00FE,
        (
            '今年怎么没有\n',
            '鬼怪屋呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这明明是惯例的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001A)

    Return()

# id: 0x0018 offset: 0x3C39
@scena.Code('func_18_3C39')
def func_18_3C39():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3C92',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的女王诞辰庆典上\n',
            '要召开武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的击剑部\n',
            '也好想参加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F1D')

    def _loc_3C92(): pass

    label('loc_3C92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_3D5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D0E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '我太过忙于这里的活动，\n',
            '连社团开的店\n',
            '都没能去帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等到店员需要换班的时候\n',
            '我再过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D5C')

    def _loc_3D0E(): pass

    label('loc_3D0E')

    ChrTalk(
        0x00FE,
        (
            '来这里参观的人\n',
            '真是多啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有热心人向我们\n',
            '提出不少尖锐的问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D5C(): pass

    label('loc_3D5C')

    Jump('loc_3F1D')

    def _loc_3D5F(): pass

    label('loc_3D5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3E50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DF3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '我是从卡尔瓦德共和国\n',
            '来这里进修的留学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我从研究发表的\n',
            '准备中也学到不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我认为这是\n',
            '很有意义的一件事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E4D')

    def _loc_3DF3(): pass

    label('loc_3DF3')

    ChrTalk(
        0x00FE,
        (
            '我是从卡尔瓦德共和国\n',
            '来这里进修的留学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我从研究发表的\n',
            '准备中也学到不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E4D(): pass

    label('loc_3E4D')

    Jump('loc_3F1D')

    def _loc_3E50(): pass

    label('loc_3E50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_3F1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3ECA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们班的活动\n',
            '大致都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过罗基克\n',
            '好像还有些不放心，\n',
            '去了资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F1D')

    def _loc_3ECA(): pass

    label('loc_3ECA')

    ChrTalk(
        0x00FE,
        (
            '我们班的活动\n',
            '大致都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过罗基克\n',
            '好像还有些不放心，\n',
            '去了资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F1D(): pass

    label('loc_3F1D')

    TalkEnd(0x001B)

    Return()

# id: 0x0019 offset: 0x3F21
@scena.Code('func_19_3F21')
def func_19_3F21():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F76',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '下午我就要\n',
            '为社团去看店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此我只有\n',
            '趁现在可以玩一会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FC4')

    def _loc_3F76(): pass

    label('loc_3F76')

    ChrTalk(
        0x00FE,
        (
            '上午是同社团的\n',
            '罗迪在看店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为太热闹了，\n',
            '所以我想很快就能知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FC4(): pass

    label('loc_3FC4')

    TalkEnd(0x001C)

    Return()

# id: 0x001A offset: 0x3FC8
@scena.Code('func_1A_3FC8')
def func_1A_3FC8():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_4029',
    )

    ChrTalk(
        0x00FE,
        (
            '……碧欧拉老师\n',
            '从刚才开始就在打哈欠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得她那么漂亮，\n',
            '可以吸引客人来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40E9')

    def _loc_4029(): pass

    label('loc_4029')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_40E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40A5',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '今天我们给客人当导游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据大家的需要，\n',
            '我们会对社会系的研究成果\n',
            '进行浅显易懂的说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40E9')

    def _loc_40A5(): pass

    label('loc_40A5')

    ChrTalk(
        0x00FE,
        (
            '根据大家的需要，\n',
            '我们会对社会系的研究成果\n',
            '进行浅显易懂的说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40E9(): pass

    label('loc_40E9')

    TalkEnd(0x001D)

    Return()

# id: 0x001B offset: 0x40ED
@scena.Code('func_1B_40ED')
def func_1B_40ED():
    TalkBegin(0x001E)

    ChrTalk(
        0x00FE,
        (
            '啊，是前辈们呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我呀，\n',
            '上午负责看店，\n',
            '下午就可以玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001E)

    Return()

# id: 0x001C offset: 0x413C
@scena.Code('func_1C_413C')
def func_1C_413C():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_4189',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真让人欣慰呀，\n',
            '连基诺奇奥也做得很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4189(): pass

    label('loc_4189')

    TalkEnd(0x001F)

    Return()

# id: 0x001D offset: 0x418D
@scena.Code('func_1D_418D')
def func_1D_418D():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_421E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41F9',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '好像比我想象的更加有趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道提出这个方案的人\n',
            '是怎么想出来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_421B')

    def _loc_41F9(): pass

    label('loc_41F9')

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……好困呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_421B(): pass

    label('loc_421B')

    Jump('loc_426D')

    def _loc_421E(): pass

    label('loc_421E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_426D',
    )

    ChrTalk(
        0x00FE,
        (
            '哎……\n',
            '为什么妈妈和妹妹会来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不是说因为工作\n',
            '不能来了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_426D(): pass

    label('loc_426D')

    TalkEnd(0x0020)

    Return()

# id: 0x001E offset: 0x4271
@scena.Code('func_1E_4271')
def func_1E_4271():
    TalkBegin(0x0021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_42A5',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐！？\n',
            '家里的店没人管不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4389')

    def _loc_42A5(): pass

    label('loc_42A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_4389',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4339',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '结果昨天我们\n',
            '还是没能完成展示的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是今天早上来看，\n',
            '已经全部完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天回去的时候\n',
            '的确是只做到一半啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4389')

    def _loc_4339(): pass

    label('loc_4339')

    ChrTalk(
        0x00FE,
        (
            '昨天回去的时候\n',
            '的确还没有完成啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我问过大家，\n',
            '但每个人都说不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4389(): pass

    label('loc_4389')

    TalkEnd(0x0021)

    Return()

# id: 0x001F offset: 0x438D
@scena.Code('func_1F_438D')
def func_1F_438D():
    TalkBegin(0x0022)

    ChrTalk(
        0x00FE,
        (
            '我和蕾娜不仅\n',
            '属于同一个班级和社团，\n',
            '就连宿舍也是在同一个房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '这可真是受不了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有现在\n',
            '才能享受点自由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0022)

    Return()

# id: 0x0020 offset: 0x4416
@scena.Code('func_20_4416')
def func_20_4416():
    TalkBegin(0x0023)

    ChrTalk(
        0x00FE,
        (
            '差不多把展示的\n',
            '所有内容都看完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过把看店的芙拉瑟给冷落了……\n',
            '不，要好好地鼓励她才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0023)

    Return()

# id: 0x0021 offset: 0x4483
@scena.Code('func_21_4483')
def func_21_4483():
    TalkBegin(0x0024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_44EB',
    )

    ChrTalk(
        0x00FE,
        (
            '#0360060155V#610F呵呵，\n',
            '这个真是很有趣呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060156V演出是在下午吧，\n',
            '我很期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4898')

    def _loc_44EB(): pass

    label('loc_44EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_4898',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4514',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_4545')

    def _loc_4514(): pass

    label('loc_4514')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_452A',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_4545')

    def _loc_452A(): pass

    label('loc_452A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4540',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_4545')

    def _loc_4540(): pass

    label('loc_4540')

    ChrSetSubChip(0x00FE, 2)

    def _loc_4545(): pass

    label('loc_4545')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 3, 0x453)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_480F',
    )

    SetScenaFlags(ScenaFlag(0x008A, 3, 0x453))

    ChrTalk(
        0x0101,
        (
            '#0010060140V#004F啊，梅贝尔市长！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360060141V#613F啊，\n',
            '这不是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060142V#004F市长您为什么会在这里呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360060143V#611F呵呵，\n',
            '其实我是这个学院的毕业生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060144V每年的学园祭都要来出席的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060145V#000F哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0360060146V#610F那么你们俩是为什么来这儿的啊？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060147V难道是为了协会的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060148V#001F嘿嘿，其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔\n',
            '向梅贝尔市长说明了事情的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x00FE,
        (
            '#0360060149V#613F哦，是协助演出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060150V#611F我也认为演出是很考功夫的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060151V呵呵，连艾丝蒂尔\n',
            '和约修亚也参加演出的话，\n',
            '那我真要好好看看才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060152V#017F（唔，真不想让\n',
            '　认识的人看到啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4893')

    def _loc_480F(): pass

    label('loc_480F')

    ChrTalk(
        0x00FE,
        (
            '#0360060153V#610F我也认为演出是很考功夫的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060154V呵呵，连艾丝蒂尔\n',
            '和约修亚也参加演出的话，\n',
            '那我真要好好看看才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4893(): pass

    label('loc_4893')

    ChrSetSubChip(0x00FE, 0)

    def _loc_4898(): pass

    label('loc_4898')

    TalkEnd(0x0024)

    Return()

# id: 0x0022 offset: 0x489C
@scena.Code('func_22_489C')
def func_22_489C():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_49CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_495B',
    )

    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))

    ChrTalk(
        0x00FE,
        (
            '#0640060131V#220F哦，下午要演出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060132V虽然这里及不上\n',
            '在王都举办的华丽舞台剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060133V毕竟应酬还是应酬啊，\n',
            '哈哈，身为未来国王的我就凑合看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49CB')

    def _loc_495B(): pass

    label('loc_495B')

    ChrTalk(
        0x00FE,
        (
            '#0640060134V#220F哦，下午要演出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060135V毕竟应酬还是应酬啊。\n',
            '哈哈，身为未来国王的我就凑合看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49CB(): pass

    label('loc_49CB')

    Jump('loc_4B61')

    def _loc_49CE(): pass

    label('loc_49CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_4B61',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 4, 0x454)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AFC',
    )

    SetScenaFlags(ScenaFlag(0x008A, 4, 0x454))

    ChrTalk(
        0x00FE,
        (
            '#0640060124V#220F这里可是王家出钱办的学院。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060125V我作为女王的外甥，\n',
            '一定要好好视察。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060126V#221F呵呵呵，想必这里的学生\n',
            '一定感到万分的光荣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060127V#509F（怎么把这个大叔也邀请过来了……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060128V#010F（嗯，\n',
            '　好像不邀请也不行啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B61')

    def _loc_4AFC(): pass

    label('loc_4AFC')

    ChrTalk(
        0x0025,
        (
            '#0640060129V#220F这里可是王家出钱办的学院。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060130V我作为女王的外甥，\n',
            '一定要好好视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B61(): pass

    label('loc_4B61')

    TalkEnd(0x0025)

    Return()

# id: 0x0023 offset: 0x4B65
@scena.Code('func_23_4B65')
def func_23_4B65():
    TalkBegin(0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_4BD9',
    )

    ChrTalk(
        0x00FE,
        (
            '#0660060138V#720F这里真不愧是杰尼丝王立学院啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660060139V就连学园祭也办得像模像样的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5C')

    def _loc_4BD9(): pass

    label('loc_4BD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_4C5C',
    )

    OP_62(0x0026, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0660060136V#722F大、大人，\n',
            '请恕冒昧直言……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660060137V在公众面前，\n',
            '请务必注意一下您的言词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C5C(): pass

    label('loc_4C5C')

    TalkEnd(0x0026)

    Return()

# id: 0x0024 offset: 0x4C60
@scena.Code('func_24_4C60')
def func_24_4C60():
    TalkBegin(0x0027)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D15',
    )

    SetScenaFlags(ScenaFlag(0x0003, 2, 0x1A))

    ChrTalk(
        0x00FE,
        (
            '#0270060058V#140F原来下午有演出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060059V#142F而且还是古典名作『白花恋诗』……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060060V不过话说回来，这舞台剧对\n',
            '学生们来说是不是有点太难了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D8B')

    def _loc_4D15(): pass

    label('loc_4D15')

    ChrTalk(
        0x00FE,
        (
            '#0270060061V#142F演出剧目是『白花恋诗』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060062V不过话说回来，这舞台剧对\n',
            '学生们来说是不是有点太难了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D8B(): pass

    label('loc_4D8B')

    TalkEnd(0x0027)

    Return()

# id: 0x0025 offset: 0x4D8F
@scena.Code('func_25_4D8F')
def func_25_4D8F():
    TalkBegin(0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 6, 0x456)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5050',
    )

    SetScenaFlags(ScenaFlag(0x008A, 6, 0x456))

    ChrTalk(
        0x0101,
        (
            '#0010060109V#000F啊，是卡露娜姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060110V#010F您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320060111V#830F呀，是你们啊……\n',
            '我听嘉恩说了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320060112V你们是来给\n',
            '学园祭帮忙的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060113V#000F嘿嘿，差不多这样啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060114V#010F卡露娜前辈\n',
            '是来做警卫之类的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320060115V#830F没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320060116V这里的毕业生大多都是\n',
            '在利贝尔各界活跃的著名人士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320060117V每年的学园祭，\n',
            '他们都会作为客人被邀请到在这里来聚会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320060118V担任警卫的我\n',
            '必须要十分仔细才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 3, 0x453)),
            Expr.Return,
        ),
        'loc_4FBF',
    )

    ChrTalk(
        0x0102,
        (
            '#0020060119V#010F说起来，\n',
            '梅贝尔市长也是这里的毕业生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5003')

    def _loc_4FBF(): pass

    label('loc_4FBF')

    ChrTalk(
        0x0101,
        (
            '#0010060120V#000F哎……说起来，\n',
            '那个谁好像也是这里的毕业生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5003(): pass

    label('loc_5003')

    ChrTalk(
        0x00FE,
        (
            '#0320060121V嗯，警备方面就交给我，\n',
            '你们就尽心帮助学院其他工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x008A, 6, 0x456))

    Jump('loc_5093')

    def _loc_5050(): pass

    label('loc_5050')

    ChrTalk(
        0x00FE,
        (
            '#0320060122V警备工作就交给我，\n',
            '你们就尽心帮助学院其他工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5093(): pass

    label('loc_5093')

    TalkEnd(0x0028)

    Return()

# id: 0x0026 offset: 0x5097
@scena.Code('func_26_5097')
def func_26_5097():
    TalkBegin(0x0029)

    ChrTalk(
        0x00FE,
        (
            '#0150060221V#130F哦哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060222V原来如此，\n',
            '学生们调查得很详细啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0029)

    Return()

# id: 0x0027 offset: 0x50EC
@scena.Code('func_27_50EC')
def func_27_50EC():
    TalkBegin(0x002A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_511A',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '在这里稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F2')

    def _loc_511A(): pass

    label('loc_511A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_51F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 4, 0x1C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51A2',
    )

    SetScenaFlags(ScenaFlag(0x0003, 4, 0x1C))

    ChrTalk(
        0x00FE,
        (
            '今天特地请假\n',
            '来看我儿子的英姿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱蕾塔好像\n',
            '也玩得十分开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在开始我要\n',
            '显出更具母亲魅力的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F2')

    def _loc_51A2(): pass

    label('loc_51A2')

    ChrTalk(
        0x00FE,
        (
            '今天特地请假\n',
            '来看我儿子的英姿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在开始我要\n',
            '显出更具母亲魅力的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51F2(): pass

    label('loc_51F2')

    TalkEnd(0x002A)

    Return()

# id: 0x0028 offset: 0x51F6
@scena.Code('func_28_51F6')
def func_28_51F6():
    TalkBegin(0x002B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5226',
    )

    ChrTalk(
        0x00FE,
        (
            '爱蕾塔渴了，\n',
            '好想喝果汁啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_524E')

    def _loc_5226(): pass

    label('loc_5226')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_524E',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，哥哥～\n',
            '我们来玩了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_524E(): pass

    label('loc_524E')

    TalkEnd(0x002B)

    Return()

# id: 0x0029 offset: 0x5252
@scena.Code('func_29_5252')
def func_29_5252():
    TalkBegin(0x002C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_529E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，找到妹妹了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她在学校里\n',
            '也和基诺奇奥很要好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_530D')

    def _loc_529E(): pass

    label('loc_529E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_530D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，只有在这个时候\n',
            '才能进到学院里面看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，妹妹的教室在哪呢……\n',
            '作为监护人我有应尽的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_530D(): pass

    label('loc_530D')

    TalkEnd(0x002C)

    Return()

# id: 0x002A offset: 0x5311
@scena.Code('func_2A_5311')
def func_2A_5311():
    TalkBegin(0x002D)

    ChrTalk(
        0x00FE,
        (
            '唔唔，\n',
            '百日战役后经济发展的相关考察……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x002D)

    Return()

# id: 0x002B offset: 0x5345
@scena.Code('func_2B_5345')
def func_2B_5345():
    TalkBegin(0x002E)

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '好想在什么地方休息一下啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x002E)

    Return()

# id: 0x002C offset: 0x5373
@scena.Code('func_2C_5373')
def func_2C_5373():
    TalkBegin(0x002F)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '好像都是些十分深奥的东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x002F)

    Return()

# id: 0x002D offset: 0x53A3
@scena.Code('func_2D_53A3')
def func_2D_53A3():
    TalkBegin(0x0030)

    ChrTalk(
        0x00FE,
        (
            '虽然在学校学习是很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是想把孩子\n',
            '培育得更加富有感情些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0030)

    Return()

# id: 0x002E offset: 0x53F3
@scena.Code('func_2E_53F3')
def func_2E_53F3():
    TalkBegin(0x0032)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5452',
    )

    ChrTalk(
        0x00FE,
        (
            '母亲老是对\n',
            '入学的事唠叨个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要考试合格\n',
            '才能进来这里读书的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_547E')

    def _loc_5452(): pass

    label('loc_5452')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_547E',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '平时就是在这里上课的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_547E(): pass

    label('loc_547E')

    TalkEnd(0x0032)

    Return()

# id: 0x002F offset: 0x5482
@scena.Code('func_2F_5482')
def func_2F_5482():
    TalkBegin(0x0031)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_54D7',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '学园祭的活动好充实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '越来越想让我的孩子\n',
            '来这儿读书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5534')

    def _loc_54D7(): pass

    label('loc_54D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5534',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我和儿子一起来\n',
            '侦察著名的王立学院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他以明年的考试为目标，\n',
            '信心很足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5534(): pass

    label('loc_5534')

    TalkEnd(0x0031)

    Return()

# id: 0x0030 offset: 0x5538
@scena.Code('func_30_5538')
def func_30_5538():
    TalkBegin(0x0034)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_56A3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 7, 0x457)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5643',
    )

    SetScenaFlags(ScenaFlag(0x008A, 7, 0x457))
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0008,
        (
            '#0530060073V#781F戴尔蒙市长，\n',
            '自从去年的王国会议之后我们也好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060074V这段时间，你身体怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0034,
        (
            '#0490060075V#661F就像你看到的，结实着呢。\n',
            '科林兹校长也很精神嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490060076V今天我打算好好放松一下。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0010)
    ChrClearFlags(0x0034, 0x0010)
    OP_4B(0x0008, 255)

    Jump('loc_56A3')

    def _loc_5643(): pass

    label('loc_5643')

    ChrTalk(
        0x0034,
        (
            '#0490060077V#661F啊，你们也来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490060078V我每年都受到王立学院的邀请来参加学园祭。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56A3(): pass

    label('loc_56A3')

    TalkEnd(0x0034)

    Return()

# id: 0x0031 offset: 0x56A7
@scena.Code('func_31_56A7')
def func_31_56A7():
    TalkBegin(0x0033)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5710',
    )

    ChrTalk(
        0x00FE,
        (
            '#0360060397V#620F刚才看到约修亚先生\n',
            '一脸紧张地走过去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060398V发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AE3')

    def _loc_5710(): pass

    label('loc_5710')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5AE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 3, 0x453)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AA1',
    )

    SetScenaFlags(ScenaFlag(0x008A, 3, 0x453))

    ChrTalk(
        0x0101,
        (
            '#0010060157V#004F啊，莉拉小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0370060158V#621F……二位真是好久没见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0024, 0x0010)
    ChrTurnDirection(0x0024, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x24, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_579A',
    )

    ChrSetSubChip(0x0024, 2)

    Jump('loc_57CB')

    def _loc_579A(): pass

    label('loc_579A')

    If(
        (
            (Expr.GetChrWork, 0x24, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_57B0',
    )

    ChrSetSubChip(0x0024, 1)

    Jump('loc_57CB')

    def _loc_57B0(): pass

    label('loc_57B0')

    If(
        (
            (Expr.GetChrWork, 0x24, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_57C6',
    )

    ChrSetSubChip(0x0024, 0)

    Jump('loc_57CB')

    def _loc_57C6(): pass

    label('loc_57C6')

    ChrSetSubChip(0x0024, 2)

    def _loc_57CB(): pass

    label('loc_57CB')

    ChrSetDirection(0x0024, 270, 0)
    ChrSetFlags(0x0024, 0x0010)

    ChrTalk(
        0x0024,
        (
            '#0360060159V#613F啊，这不是\n',
            '艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0024, 0)
    ChrTurnDirection(0x0102, 0x0024, 0)
    ChrTurnDirection(0x0105, 0x0024, 0)

    ChrTalk(
        0x0101,
        (
            '#0010060160V#004F啊，梅贝尔市长也在！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060161V你们两位为什么会在这里呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#0360060162V#611F呵呵，\n',
            '其实我是这个学院的毕业生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060163V每年的学园祭都要来出席的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060164V#000F哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#0360060165V#610F那么你们俩是为什么来这儿的啊？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060166V难道是为了协会的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060167V#001F嘿嘿，其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔\n',
            '向梅贝尔市长说明了事情的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0024,
        (
            '#0360060168V#613F哦，是协助演出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060169V#611F我也认为演出是很考功夫的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060170V呵呵，连艾丝蒂尔\n',
            '和约修亚也参加演出的话，\n',
            '那我真要好好看看才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060171V#017F（唔，真不想让\n',
            '　认识的人看到啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0024, 0)

    Jump('loc_5AE3')

    def _loc_5AA1(): pass

    label('loc_5AA1')

    ChrTalk(
        0x00FE,
        (
            '#0370060172V#621F……二位真是好久没见了。\n',
            '还是那么有精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AE3(): pass

    label('loc_5AE3')

    TalkEnd(0x0033)

    Return()

# id: 0x0032 offset: 0x5AE7
@scena.Code('func_32_5AE7')
def func_32_5AE7():
    TalkBegin(0x0035)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5B35',
    )

    ChrTalk(
        0x00FE,
        (
            '过去的学园祭，\n',
            '班级展示全都是研究发表……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '时代变迁啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B92')

    def _loc_5B35(): pass

    label('loc_5B35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5B92',
    )

    ChrTalk(
        0x00FE,
        (
            '在我们的学生时代，\n',
            '还没有这个校舍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这北面的古老建筑物\n',
            '就是以前的校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B92(): pass

    label('loc_5B92')

    TalkEnd(0x0035)

    Return()

# id: 0x0033 offset: 0x5B96
@scena.Code('func_33_5B96')
def func_33_5B96():
    TalkBegin(0x0036)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5BF9',
    )

    ChrTalk(
        0x00FE,
        (
            '……期末考试成绩优秀者\n',
            '……科洛丝·琳希……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，\n',
            '她和乔儿那孩子都好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C2D')

    def _loc_5BF9(): pass

    label('loc_5BF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5C2D',
    )

    ChrTalk(
        0x00FE,
        (
            '和主日学校相比，\n',
            '这里的学习更专业呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C2D(): pass

    label('loc_5C2D')

    TalkEnd(0x0036)

    Return()

# id: 0x0034 offset: 0x5C31
@scena.Code('func_34_5C31')
def func_34_5C31():
    TalkBegin(0x0037)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5C94',
    )

    ChrTalk(
        0x00FE,
        (
            '下午的舞台剧\n',
            '好像有很有趣的看点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我问过女儿，\n',
            '但她没告诉我详细情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CE4')

    def _loc_5C94(): pass

    label('loc_5C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5CE4',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是学院啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然女儿在这里上学，\n',
            '不过我还是第一次来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CE4(): pass

    label('loc_5CE4')

    TalkEnd(0x0037)

    Return()

# id: 0x0035 offset: 0x5CE8
@scena.Code('func_35_5CE8')
def func_35_5CE8():
    TalkBegin(0x0038)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5D1C',
    )

    ChrTalk(
        0x00FE,
        (
            '走得好累呀，\n',
            '去茶座休息一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D4C')

    def _loc_5D1C(): pass

    label('loc_5D1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5D4C',
    )

    ChrTalk(
        0x00FE,
        (
            '在二楼的是自然系\n',
            '和社会系的教室……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D4C(): pass

    label('loc_5D4C')

    TalkEnd(0x0038)

    Return()

# id: 0x0036 offset: 0x5D50
@scena.Code('func_36_5D50')
def func_36_5D50():
    TalkBegin(0x0039)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5D8C',
    )

    ChrTalk(
        0x00FE,
        (
            '各种展示都很有趣啊，\n',
            '孩子们也感到很开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DB1')

    def _loc_5D8C(): pass

    label('loc_5D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5DB1',
    )

    ChrTalk(
        0x00FE,
        (
            '从什么地方开始看好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DB1(): pass

    label('loc_5DB1')

    TalkEnd(0x0039)

    Return()

# id: 0x0037 offset: 0x5DB5
@scena.Code('func_37_5DB5')
def func_37_5DB5():
    TalkBegin(0x003A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5E0D',
    )

    ChrTalk(
        0x00FE,
        (
            '我看了很多展示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅很有趣，\n',
            '也能从中看到学生们平时的学习成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E3D')

    def _loc_5E0D(): pass

    label('loc_5E0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5E3D',
    )

    ChrTalk(
        0x00FE,
        (
            '真没想到这个建筑物里\n',
            '有这么多地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E3D(): pass

    label('loc_5E3D')

    TalkEnd(0x003A)

    Return()

# id: 0x0038 offset: 0x5E41
@scena.Code('func_38_5E41')
def func_38_5E41():
    TalkBegin(0x003B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5E95',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这个班级真让人吃惊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些学生竟然\n',
            '能做出那种东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EC3')

    def _loc_5E95(): pass

    label('loc_5E95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5EC3',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵……\n',
            '这里就是自然系的教室啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EC3(): pass

    label('loc_5EC3')

    TalkEnd(0x003B)

    Return()

# id: 0x0039 offset: 0x5EC7
@scena.Code('func_39_5EC7')
def func_39_5EC7():
    TalkBegin(0x003C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5EFF',
    )

    ChrTalk(
        0x00FE,
        (
            '展示好像快要结束了，\n',
            '要快点看完才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F27')

    def _loc_5EFF(): pass

    label('loc_5EFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5F27',
    )

    ChrTalk(
        0x00FE,
        (
            '今年来的人\n',
            '好像特别多啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F27(): pass

    label('loc_5F27')

    TalkEnd(0x003C)

    Return()

# id: 0x003A offset: 0x5F2B
@scena.Code('func_3A_5F2B')
def func_3A_5F2B():
    TalkBegin(0x003D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_5F68',
    )

    ChrTalk(
        0x00FE,
        (
            '一早我就在想着舞台剧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F98')

    def _loc_5F68(): pass

    label('loc_5F68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_5F98',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是学习的地方？\n',
            '不是玩的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F98(): pass

    label('loc_5F98')

    TalkEnd(0x003D)

    Return()

# id: 0x003B offset: 0x5F9C
@scena.Code('func_3B_5F9C')
def func_3B_5F9C():
    EventBegin(0x00)
    CameraMove(-5190, 0, 34000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0031, 3150, 0, 31480, 90)
    ChrSetPos(0x0019, -5600, 0, 29020, 90)
    ChrSetPos(0x0025, 88600, 0, 34670, 0)
    ChrSetPos(0x0026, 89570, 0, 34410, 270)
    ChrClearFlags(0x0029, 0x0080)
    OP_4A(0x0029, 255)
    ChrSetPos(0x0101, 2630, 0, 29470, 0)
    ChrSetPos(0x0102, 2510, 0, 28440, 0)
    ChrSetPos(0x0105, 1400, 0, 28920, 0)
    ChrSetPos(0x0029, 1690, 0, 30250, 0)
    FadeIn(2000, 0)
    CameraMove(2050, 0, 29480, 4000)

    ChrTalk(
        0x0029,
        (
            '#0150060210V#132F呀～这里就是了。\n',
            '的确是十分正规的展览啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060211V从历史到经济，\n',
            '各个领域的作品都有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0029, 180, 400)

    ChrTalk(
        0x0029,
        (
            '#0150060212V#130F哎呀，真是太好了。\n',
            '我对这里的展览十分感兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060213V#048F您太过奖了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060214V我也是社会系专业的，\n',
            '十分荣幸您会对展览感兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060215V#506F嗯～不过我对这种复杂的东西\n',
            '就比较头痛了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060216V#017F唉，我说你啊，\n',
            '偶尔也该对这类东西有点兴趣嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060217V#010F因为游击士也经常\n',
            '会用到各种各样的知识哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060218V#509F哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0029,
        (
            '#0150060219V#130F哈哈，\n',
            '那么我这就开始参观了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150060220V真是感谢你们带我来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0029, 315, 400)

    @scena.Lambda('lambda_62EA')
    def lambda_62EA():
        CameraMove(1000, 0, 31440, 2000)

        ExitThread()

    DispatchAsync(0x0029, 0x0001, lambda_62EA)

    ChrWalkTo(0x0029, -1680, 0, 34680, 2000, 0x00)
    ChrSetDirection(0x0029, 0, 400)
    OP_4B(0x0029, 255)
    SetScenaFlags(ScenaFlag(0x008B, 2, 0x45A))
    EventEnd(0x00)

    Return()

# id: 0x003C offset: 0x6321
@scena.Code('func_3C_6321')
def func_3C_6321():
    EventBegin(0x00)
    ChrSetFlags(0x0028, 0x0080)
    ChrSetFlags(0x0034, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    ChrSetPos(0x0009, 41350, -250, -3330, 0)
    ChrSetPos(0x000A, 40790, -250, -4570, 0)
    ChrSetPos(0x000B, 39420, 0, -2040, 0)
    ChrSetPos(0x000C, 41420, -250, -2220, 0)
    ChrSetPos(0x000D, 40840, 0, -1870, 0)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x0101, 46630, 2000, 7580, 180)
    ChrSetPos(0x0102, 46550, 2000, 8570, 180)
    ChrSetPos(0x0105, 45690, 2000, 8960, 180)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0400060286V#1P啊，是姐姐他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_6471')
    def lambda_6471():
        CameraMove(44200, 0, 1160, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6471)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_648E')
    def lambda_648E():
        ChrWalkTo(0x00FE, 45690, 0, 3810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_648E)

    @scena.Lambda('lambda_64A9')
    def lambda_64A9():
        ChrWalkTo(0x00FE, 42950, 0, 90, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_64A9)

    Sleep(200)

    @scena.Lambda('lambda_64C9')
    def lambda_64C9():
        ChrWalkTo(0x00FE, 43970, 0, -660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_64C9)

    @scena.Lambda('lambda_64E4')
    def lambda_64E4():
        ChrWalkTo(0x00FE, 42190, 0, 270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_64E4)

    Sleep(200)

    @scena.Lambda('lambda_6504')
    def lambda_6504():
        ChrWalkTo(0x00FE, 43080, 0, -700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6504)

    Sleep(100)

    @scena.Lambda('lambda_6524')
    def lambda_6524():
        ChrWalkTo(0x00FE, 47000, 0, 3050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6524)

    Sleep(500)

    @scena.Lambda('lambda_6544')
    def lambda_6544():
        ChrWalkTo(0x00FE, 45690, 0, 3810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6544)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_6564')
    def lambda_6564():
        ChrWalkTo(0x00FE, 43120, 0, 1560, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6564)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_6584')
    def lambda_6584():
        ChrWalkTo(0x00FE, 44840, 0, 420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6584)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_65A4')
    def lambda_65A4():
        ChrWalkTo(0x00FE, 44290, 0, 1370, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_65A4)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 225, 400)
    WaitForThreadExit(0x0105, 0x0001)
    ChrSetDirection(0x0105, 225, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060287V#041F孩子们……\n',
            '你们来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060288V#001F#1P你们终于来了，小家伙们⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060289V#019F#2P怎么样，玩得开心吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0430060290V嗯～！\n',
            '很开心哦～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0420060291V我今天吃了\n',
            '好多好多点心呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0410060292V你就知道吃，\n',
            '去哪儿吃到哪儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060293V#048F呵呵……\n',
            '你们是和特蕾莎老师一起来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#0400060294V#770F嗯，\n',
            '她在那边和别人聊天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0400060295V#771F啊，来啦来啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_67A5')
    def lambda_67A5():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_67A5)

    @scena.Lambda('lambda_67B3')
    def lambda_67B3():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_67B3)

    @scena.Lambda('lambda_67C1')
    def lambda_67C1():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_67C1)

    @scena.Lambda('lambda_67CF')
    def lambda_67CF():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_67CF')

    DispatchAsync2(0x0101, 0x0002, lambda_67CF)

    @scena.Lambda('lambda_67E0')
    def lambda_67E0():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_67E0')

    DispatchAsync2(0x0102, 0x0002, lambda_67E0)

    @scena.Lambda('lambda_67F1')
    def lambda_67F1():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_67F1')

    DispatchAsync2(0x0105, 0x0002, lambda_67F1)

    ChrClearFlags(0x000A, 0x0080)
    ChrWalkTo(0x000A, 42000, 0, -1100, 2000, 0x00)
    ChrTurnDirection(0x000A, 0x0105, 400)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x000A,
        (
            '#0390060296V#750F呵呵，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060297V#004F#1P啊，特蕾莎院长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060298V#048F老师……您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390060299V#751F今天邀请我们来参加学园祭，\n',
            '真的是感谢你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060300V我和孩子们\n',
            '今天真的玩得很开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0105, 400)

    ChrTalk(
        0x000D,
        (
            '#0400060301V#770F对了，科洛丝姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060302V姐姐演的舞台剧\n',
            '什么时候才开始啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6970')
    def lambda_6970():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_6970)

    @scena.Lambda('lambda_697E')
    def lambda_697E():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_697E)

    @scena.Lambda('lambda_698C')
    def lambda_698C():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_698C)

    ChrTurnDirection(0x000C, 0x0105, 400)

    ChrTalk(
        0x000C,
        (
            '#0410060303V对啊对啊。\n',
            '我们都很期待呢☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060304V#040F是啊……\n',
            '还要再等一会儿哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060305V#041F顺便说一句，不光是我，\n',
            '艾丝蒂尔他们也会参加演出哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0420060306V真的？\n',
            '哇，好期待呢～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#0430060307V约修亚哥哥\n',
            '演的是什么角色啊～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060308V#018F#2P这个……\n',
            '该怎么说好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060309V#001F#1P啊哈哈……\n',
            '总之你们看了一定会喜欢的㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060310V#000F对了，特蕾莎院长。\n',
            '你们还住在玛诺利亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390060311V#750F是的，承蒙旅店主人的好意，\n',
            '让我们用很便宜的价钱租了个房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060312V#757F但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060313V#501F#1P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060314V#015F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060315V#010F好了，孩子们。\n',
            '想去看看舞台剧的服装吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060316V有好多漂亮的\n',
            '晚礼服和骑士装哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6C7E')
    def lambda_6C7E():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6C7E)

    @scena.Lambda('lambda_6C8C')
    def lambda_6C8C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6C8C)

    @scena.Lambda('lambda_6C9A')
    def lambda_6C9A():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6C9A)

    @scena.Lambda('lambda_6CA8')
    def lambda_6CA8():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6CA8)

    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '#0410060317V漂亮的晚礼服！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6CDF')
    def lambda_6CDF():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6CDF)

    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x000D,
        (
            '#0400060318V#774F骑士装！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060319V#019F呵呵……\n',
            '看来你们很有兴趣啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060320V那么哥哥就破例，\n',
            '带你们到舞台后面参观一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0420060321V好呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0430060322V波利也要去～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060323V#010F（我们先到舞台休息室去，\n',
            '　你们待会儿过来吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6E07')
    def lambda_6E07():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E07')

    DispatchAsync2(0x0105, 0x0001, lambda_6E07)

    @scena.Lambda('lambda_6E18')
    def lambda_6E18():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E18')

    DispatchAsync2(0x0101, 0x0001, lambda_6E18)

    @scena.Lambda('lambda_6E29')
    def lambda_6E29():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E29')

    DispatchAsync2(0x000A, 0x0001, lambda_6E29)

    @scena.Lambda('lambda_6E3A')
    def lambda_6E3A():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E3A')

    DispatchAsync2(0x000D, 0x0001, lambda_6E3A)

    @scena.Lambda('lambda_6E4B')
    def lambda_6E4B():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E4B')

    DispatchAsync2(0x000C, 0x0001, lambda_6E4B)

    @scena.Lambda('lambda_6E5C')
    def lambda_6E5C():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E5C')

    DispatchAsync2(0x0009, 0x0001, lambda_6E5C)

    @scena.Lambda('lambda_6E6D')
    def lambda_6E6D():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6E6D')

    DispatchAsync2(0x000B, 0x0001, lambda_6E6D)

    ChrSetFlags(0x0102, 0x0004)
    ChrSetDirection(0x0102, 180, 400)
    ChrWalkTo(0x0102, 45060, 0, -920, 2000, 0x00)
    ChrWalkTo(0x0102, 43190, 0, -1790, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x000D, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060324V#010F那么大家跟我来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 225, 400)
    ChrWalkTo(0x0102, 42040, -250, -2580, 2000, 0x00)
    ChrClearFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_6F02')
    def lambda_6F02():
        ChrWalkTo(0x00FE, 42040, -250, -5100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6F02)

    @scena.Lambda('lambda_6F1D')
    def lambda_6F1D():
        ChrWalkTo(0x00FE, 42040, -250, -5100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6F1D)

    Sleep(700)

    @scena.Lambda('lambda_6F3D')
    def lambda_6F3D():
        ChrWalkTo(0x00FE, 42530, -250, -2310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6F3D)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_6F62')
    def lambda_6F62():
        ChrWalkTo(0x00FE, 42040, -250, -5100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6F62)

    @scena.Lambda('lambda_6F7D')
    def lambda_6F7D():
        ChrWalkTo(0x00FE, 42040, -250, -5100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6F7D)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_6FA2')
    def lambda_6FA2():
        ChrWalkTo(0x00FE, 41270, 0, -820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6FA2)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_6FC2')
    def lambda_6FC2():
        ChrWalkTo(0x00FE, 42040, -250, -5100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6FC2)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0080)
    WaitForThreadExit(0x000D, 0x0001)
    ChrSetFlags(0x000D, 0x0080)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetFlags(0x000B, 0x0080)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000A, 0xFF)

    @scena.Lambda('lambda_700C')
    def lambda_700C():
        CameraMove(42780, 0, 270, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_700C)

    @scena.Lambda('lambda_7024')
    def lambda_7024():
        ChrWalkTo(0x00FE, 43260, 0, -70, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_7024)

    Sleep(400)

    @scena.Lambda('lambda_7044')
    def lambda_7044():
        ChrWalkTo(0x00FE, 42100, 0, 500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7044)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x000A, 400)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0390060325V#750F呵呵，\n',
            '约修亚真是个敏锐的孩子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060326V#757F其实我是有些话\n',
            '不方便在孩子们面前说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_70E2')
    def lambda_70E2():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_70E2)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060327V#002F#1P这么说，难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0390060328V#754F嗯，因为已经考虑了好几天，\n',
            '所以我还是决定接受市长的提议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060329V毕竟不能再给\n',
            '玛诺利亚的村民们添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060330V#750F今天的学园祭结束之后，\n',
            '我就会告诉孩子们这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060331V#049F#2P这样……啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060332V虽然以后会很寂寞……\n',
            '但我尊重老师您的决定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390060333V#751F呵呵，别这么没精打采嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060334V虽说要搬到王都，\n',
            '但坐定期船的话一下子就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060335V#750F而且我打算\n',
            '到了王都之后去找份工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060336V我会慢慢地赚钱，\n',
            '总有一天孤儿院能再重建的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060337V#003F#1P特蕾莎院长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060338V#049F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0390060339V#751F好了……\n',
            '你们不去找那些孩子吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060340V怎么说也不能把孩子们\n',
            '全扔给约修亚一个人管啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2523._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x003D offset: 0x7406
@scena.Code('func_3D_7406')
def func_3D_7406():
    PlaySE(17, 0x00, 0x64)
    ChrSetFlags(0x003E, 0x0080)
    OP_64(0x01, 0x0001)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0080)
    TalkEnd(0x00FF)

    Return()

# id: 0x003E offset: 0x746C
@scena.Code('func_3E_746C')
def func_3E_746C():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　前面是校长室和办公室　　　　\n',
            '※谢绝外来人员进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x003F offset: 0x74D6
@scena.Code('func_3F_74D6')
def func_3F_74D6():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '人文系模拟店铺\n',
            '茶座『芳塔娜』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0040 offset: 0x7526
@scena.Code('func_40_7526')
def func_40_7526():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　走　\n',
            '　　廊　\n',
            '　　里　\n',
            '　　请　\n',
            '　　保　\n',
            '　学持　\n',
            '　生安　\n',
            '　指静　\n',
            '　导！　\n',
            '　部　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0041 offset: 0x75B2
@scena.Code('func_41_75B2')
def func_41_75B2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '自然系成果展示\n',
            '『结晶回路与导力技术』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0042 offset: 0x760A
@scena.Code('func_42_760A')
def func_42_760A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　社会系成果展示\n',
            '『卢安地区的历史与经济』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0043 offset: 0x7668
@scena.Code('func_43_7668')
def func_43_7668():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '欢迎光临！\n',
            '这里是茶座『芳塔娜』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0044 offset: 0x76BC
@scena.Code('func_44_76BC')
def func_44_76BC():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里分析了导力器产业的发展动向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0045 offset: 0x770F
@scena.Code('func_45_770F')
def func_45_770F():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里用图表展示了每年观光客数量的变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0046 offset: 0x7768
@scena.Code('func_46_7768')
def func_46_7768():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里整理了国内主要产品的出口方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0047 offset: 0x77BD
@scena.Code('func_47_77BD')
def func_47_77BD():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里归纳了人口移动的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0048 offset: 0x780A
@scena.Code('func_48_780A')
def func_48_780A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　《导力演算器的存储装置》　　\n',
            '※这个展示品是从\n',
            '　蔡斯的中央工房借来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0049 offset: 0x7887
@scena.Code('func_49_7887')
def func_49_7887():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '《导力相性占卜机》\n',
            '　 ※好评工作中！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x004A offset: 0x78DE
@scena.Code('func_4A_78DE')
def func_4A_78DE():
    EventBegin(0x00)
    Fade(1000)

    @scena.Lambda('lambda_78EB')
    def lambda_78EB():
        CameraMove(84960, 1650, 32920, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_78EB)

    @scena.Lambda('lambda_7903')
    def lambda_7903():
        OP_67(0, 1300, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7903)

    @scena.Lambda('lambda_791B')
    def lambda_791B():
        CameraSetDistance(1400, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_791B)

    @scena.Lambda('lambda_792B')
    def lambda_792B():
        OP_6C(0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_792B)

    @scena.Lambda('lambda_793B')
    def lambda_793B():
        OP_6E(262, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_793B)

    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_7963',
    )

    Jump('loc_79B0')

    def _loc_7963(): pass

    label('loc_7963')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_796D',
    )

    Jump('loc_79B0')

    def _loc_796D(): pass

    label('loc_796D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_7995',
    )

    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0033, 0x0080)
    ChrSetFlags(0x002C, 0x0080)

    Jump('loc_79B0')

    def _loc_7995(): pass

    label('loc_7995')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_79B0',
    )

    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrSetFlags(0x0022, 0x0080)

    def _loc_79B0(): pass

    label('loc_79B0')

    Sleep(1000)

    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    Fade(500)
    OP_74(0x0006, 0x00000000, 0x0001)
    OP_0D()
    Sleep(500)

    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#1721170001V',
            (TxtCtl.SetColor, 0x2),
            '导力相性占卜机\n',
            'Version:1.0014.4082\n',
            '(C)Genis Royal School 1202',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    TalkSetChrName('占卜机')

    Talk(
        (
            '#1720060224V',
            (TxtCtl.SetColor, 0x5),
            '想要占卜一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7A6A(): pass

    label('loc_7A6A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D3A',
    )

    SetMessageWindowPos(72, 290, 56, 3)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        1,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0001)
    OP_5F(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_7AC1'),
        (0x00000001, 'loc_7AC4'),
        (-1, 'loc_7AD1'),
    )

    def _loc_7AC1(): pass

    label('loc_7AC1')

    Jump('loc_7ADE')

    def _loc_7AC4(): pass

    label('loc_7AC4')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7A6A')

    def _loc_7AD1(): pass

    label('loc_7AD1')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7A6A')

    def _loc_7ADE(): pass

    label('loc_7ADE')

    Talk(
        (
            '#1720060225V',
            (TxtCtl.SetColor, 0x5),
            '要输入谁的资料呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        55,
        5,
        0,
        (
            TXT(0x00, '【艾丝蒂尔】\n'),
            TXT(0x01, '【约修亚】\n'),
            TXT(0x02, '【雪拉扎德】\n'),
            TXT(0x03, '【奥利维尔】\n'),
            TXT(0x04, '【科洛丝】\n'),
            TXT(0x05, '【奈尔】\n'),
            TXT(0x06, '【朵洛希】\n'),
        ),
    )

    MenuEnd(0x0001)

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_7B97'),
        (0x00000001, 'loc_7BEB'),
        (0x00000002, 'loc_7C41'),
        (0x00000003, 'loc_7C97'),
        (0x00000004, 'loc_7CED'),
        (0x00000005, 'loc_7D41'),
        (0x00000006, 'loc_7D93'),
        (-1, 'loc_7DE7'),
    )

    def _loc_7B97(): pass

    label('loc_7B97')

    Talk(
        (
            '#1720060226V',
            (TxtCtl.SetColor, 0x5),
            '【艾丝蒂尔·布莱特】\n',
            '七耀历１１８６年８月７日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7BEB(): pass

    label('loc_7BEB')

    Talk(
        (
            '#1720060227V',
            (TxtCtl.SetColor, 0x5),
            '【约修亚·布莱特】\n',
            '七耀历１１８５年１２月２０日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7C41(): pass

    label('loc_7C41')

    Talk(
        (
            '#1720060228V',
            (TxtCtl.SetColor, 0x5),
            '【雪拉扎德·哈维】\n',
            '七耀历１１７９年５月１４日生出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7C97(): pass

    label('loc_7C97')

    Talk(
        (
            '#1720060229V',
            (TxtCtl.SetColor, 0x5),
            '【奥利维尔·朗海姆】\n',
            '七耀历１１７７年４月１日生出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7CED(): pass

    label('loc_7CED')

    Talk(
        (
            '#1720060230V',
            (TxtCtl.SetColor, 0x5),
            '【科洛丝·琳希】\n',
            '七耀历１１８６年１０月１１日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7D41(): pass

    label('loc_7D41')

    Talk(
        (
            '#1720060231V',
            (TxtCtl.SetColor, 0x5),
            '【奈尔·班兹】\n',
            '七耀历１１７２年１１月２５日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7D93(): pass

    label('loc_7D93')

    Talk(
        (
            '#1720060232V',
            (TxtCtl.SetColor, 0x5),
            '【朵洛希·海娅特】\n',
            '七耀历１１８２年１月２２日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7DE7')

    def _loc_7DE7(): pass

    label('loc_7DE7')

    Talk(
        (
            '#1720060233V',
            (TxtCtl.SetColor, 0x5),
            '接下来请输入\n',
            '对方的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        426,
        5,
        0,
        (
            TXT(0x00, '【艾丝蒂尔】\n'),
            TXT(0x01, '【约修亚】\n'),
            TXT(0x02, '【雪拉扎德】\n'),
            TXT(0x03, '【奥利维尔】\n'),
            TXT(0x04, '【科洛丝】\n'),
            TXT(0x05, '【奈尔】\n'),
            TXT(0x06, '【朵洛希】\n'),
        ),
    )

    MenuEnd(0x0001)

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_7EA7'),
        (0x00000001, 'loc_7EFB'),
        (0x00000002, 'loc_7F51'),
        (0x00000003, 'loc_7FA7'),
        (0x00000004, 'loc_7FFD'),
        (0x00000005, 'loc_8051'),
        (0x00000006, 'loc_80A3'),
        (-1, 'loc_80F7'),
    )

    def _loc_7EA7(): pass

    label('loc_7EA7')

    Talk(
        (
            '#1720060234V',
            (TxtCtl.SetColor, 0x5),
            '【艾丝蒂尔·布莱特】\n',
            '七耀历１１８６年８月７日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_7EFB(): pass

    label('loc_7EFB')

    Talk(
        (
            '#1720060235V',
            (TxtCtl.SetColor, 0x5),
            '【约修亚·布莱特】\n',
            '七耀历１１８５年１２月２０日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xA),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_7F51(): pass

    label('loc_7F51')

    Talk(
        (
            '#1720060236V',
            (TxtCtl.SetColor, 0x5),
            '【雪拉扎德·哈维】\n',
            '七耀历１１７９年５月１４日生出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x14),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_7FA7(): pass

    label('loc_7FA7')

    Talk(
        (
            '#1720060237V',
            (TxtCtl.SetColor, 0x5),
            '【奥利维尔·朗海姆】\n',
            '七耀历１１７７年４月１日生出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1E),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_7FFD(): pass

    label('loc_7FFD')

    Talk(
        (
            '#1720060238V',
            (TxtCtl.SetColor, 0x5),
            '【科洛丝·琳希】\n',
            '七耀历１１８６年１０月１１日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x28),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_8051(): pass

    label('loc_8051')

    Talk(
        (
            '#1720060239V',
            (TxtCtl.SetColor, 0x5),
            '【奈尔·班兹】\n',
            '七耀历１１７２年１１月２５日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x32),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_80A3(): pass

    label('loc_80A3')

    Talk(
        (
            '#1720060240V',
            (TxtCtl.SetColor, 0x5),
            '【朵洛希·海娅特】\n',
            '七耀历１１８２年１月２２日出生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3C),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_80F7')

    def _loc_80F7(): pass

    label('loc_80F7')

    TalkSetChrName('占卜机')

    Talk(
        (
            '#1720060241V',
            (TxtCtl.SetColor, 0x5),
            '那么，占卜现在开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(39, 0x00, 0x64)
    OP_75(0x06, 0x00000000, 0x00)
    Sleep(50)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0001)
    Sleep(60)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0002)
    Sleep(70)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0003)
    Sleep(80)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0004)
    Sleep(90)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0005)
    Sleep(100)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0006)
    Sleep(110)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0007)
    Sleep(120)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0001)
    Sleep(130)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0002)
    Sleep(140)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0003)
    Sleep(150)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0004)
    Sleep(160)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0005)
    Sleep(170)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0006)
    Sleep(180)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0007)
    Sleep(190)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0001)
    Sleep(200)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0002)
    Sleep(210)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0003)
    Sleep(220)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0004)
    Sleep(230)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0005)
    Sleep(240)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0006)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0007)
    Sleep(260)

    TalkSetChrName('占卜机')

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000004, 'loc_839C'),
        (0x00000028, 'loc_839C'),
        (0x0000000C, 'loc_839C'),
        (0x00000015, 'loc_839C'),
        (0x00000018, 'loc_839C'),
        (0x0000002A, 'loc_839C'),
        (0x00000024, 'loc_839C'),
        (0x0000003F, 'loc_839C'),
        (0x00000005, 'loc_8503'),
        (0x00000032, 'loc_8503'),
        (0x0000000E, 'loc_8503'),
        (0x00000029, 'loc_8503'),
        (0x0000001A, 'loc_8503'),
        (0x0000003E, 'loc_8503'),
        (0x00000002, 'loc_8651'),
        (0x00000014, 'loc_8651'),
        (0x00000006, 'loc_8651'),
        (0x0000003C, 'loc_8651'),
        (0x0000000F, 'loc_8651'),
        (0x00000033, 'loc_8651'),
        (0x00000001, 'loc_87AD'),
        (0x0000000A, 'loc_87AD'),
        (0x0000000D, 'loc_87AD'),
        (0x0000001F, 'loc_87AD'),
        (0x00000019, 'loc_87AD'),
        (0x00000034, 'loc_87AD'),
        (0x0000002E, 'loc_87AD'),
        (0x00000040, 'loc_87AD'),
        (0x00000010, 'loc_88F8'),
        (0x0000003D, 'loc_88F8'),
        (0x00000017, 'loc_88F8'),
        (0x00000020, 'loc_88F8'),
        (0x00000022, 'loc_88F8'),
        (0x0000002B, 'loc_88F8'),
        (0x00000038, 'loc_88F8'),
        (0x00000041, 'loc_88F8'),
        (0x00000003, 'loc_8A6D'),
        (0x0000001E, 'loc_8A6D'),
        (0x00000023, 'loc_8A6D'),
        (0x00000035, 'loc_8A6D'),
        (0x0000002D, 'loc_8A6D'),
        (0x00000036, 'loc_8A6D'),
        (0x00000000, 'loc_8BB5'),
        (0x0000000B, 'loc_8BB5'),
        (0x00000016, 'loc_8BB5'),
        (0x00000021, 'loc_8BB5'),
        (0x0000002C, 'loc_8BB5'),
        (0x00000037, 'loc_8BB5'),
        (0x00000042, 'loc_8BB5'),
        (-1, 'loc_8CF7'),
    )

    def _loc_839C(): pass

    label('loc_839C')

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0003)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0006)
    Sleep(1000)

    Talk(
        (
            '#1720060242V',
            (TxtCtl.SetColor, 0x5),
            '今天是你们\n',
            '彼此都很主动的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060243V',
            (TxtCtl.SetColor, 0x5),
            '要主动采取行动，\n',
            '这样两人应该能度过快乐的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060244V',
            (TxtCtl.SetColor, 0x5),
            '谈话很容易投机，\n',
            '只要能够两人独处，\n',
            '很快就能得到对方的心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060245V',
            (TxtCtl.SetColor, 0x5),
            '如果被邀请的话，\n',
            '不要犹豫，马上接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060246V',
            (TxtCtl.SetColor, 0x5),
            '有共同兴趣和目的的情况下，\n',
            '两人的关系会发展得十分顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF7')

    def _loc_8503(): pass

    label('loc_8503')

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0004)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0007)
    Sleep(1000)

    Talk(
        (
            '#1720060247V',
            (TxtCtl.SetColor, 0x5),
            '今天两人的意识很协调，\n',
            '能度过开心的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060248V',
            (TxtCtl.SetColor, 0x5),
            '在两人中的一个遇到麻烦的情况下，\n',
            '不要嫌麻烦，马上帮助对方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060249V',
            (TxtCtl.SetColor, 0x5),
            '有共同意识的情况下，\n',
            '能知道对方隐蔽的一面，\n',
            '两人的友情也会进一步加深。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060250V',
            (TxtCtl.SetColor, 0x5),
            '今天两人会有爱情\n',
            '或注意到对方是特别的朋友这种意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF7')

    def _loc_8651(): pass

    label('loc_8651')

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0001)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0005)
    Sleep(1000)

    Talk(
        (
            '#1720060251V',
            (TxtCtl.SetColor, 0x5),
            '今天两人会对\n',
            '事物的看法非常乐观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060252V',
            (TxtCtl.SetColor, 0x5),
            '即使各自的主张\n',
            '有出入也没有关系，\n',
            '很快就能安稳度过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060253V',
            (TxtCtl.SetColor, 0x5),
            '平时可能有一方会\n',
            '将自己的意见强加于对方，\n',
            '使关系变得紧张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060254V',
            (TxtCtl.SetColor, 0x5),
            '不过在这一天\n',
            '两人的情绪会非常安定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060255V',
            (TxtCtl.SetColor, 0x5),
            '平时不能说的话，\n',
            '今天就有机会说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF7')

    def _loc_87AD(): pass

    label('loc_87AD')

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0007)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0002)
    Sleep(1000)

    Talk(
        (
            '#1720060256V',
            (TxtCtl.SetColor, 0x5),
            '今天两人非常主动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060257V',
            (TxtCtl.SetColor, 0x5),
            '如果有两人都想做的事，\n',
            '一起来做是个\n',
            '绝好的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060258V',
            (TxtCtl.SetColor, 0x5),
            '不过，不要太过\n',
            '把自己的意见强加于对方，\n',
            '这一点必须要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060259V',
            (TxtCtl.SetColor, 0x5),
            '尊重对方的步调，\n',
            '关系会有快速进展的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060260V',
            (TxtCtl.SetColor, 0x5),
            '总之首先考虑\n',
            '对方的心情是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF7')

    def _loc_88F8(): pass

    label('loc_88F8')

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0007)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0004)
    Sleep(1000)

    Talk(
        (
            '#1720060261V',
            (TxtCtl.SetColor, 0x5),
            '今天两人就算在一起，\n',
            '无论到哪儿都会是不顺利的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060262V',
            (TxtCtl.SetColor, 0x5),
            '隐藏的秘密会暴露，\n',
            '如果欺骗对方的话，\n',
            '会让对方感到不可信任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060263V',
            (TxtCtl.SetColor, 0x5),
            '找不到共同的话题，\n',
            '谈话也总是不投机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060264V',
            (TxtCtl.SetColor, 0x5),
            '这样的日子还是不要硬靠近，\n',
            '下决心做其他的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060265V',
            (TxtCtl.SetColor, 0x5),
            '留出距离和时间，\n',
            '应该能再确认一下对方的重要性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF7')

    def _loc_8A6D(): pass

    label('loc_8A6D')

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0006)
    Sleep(250)

    PlaySE(39, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0003)
    Sleep(1000)

    Talk(
        (
            '#1720060266V',
            (TxtCtl.SetColor, 0x5),
            '今天两人会\n',
            '对某事都不做出让步，\n',
            '可能会导致吵架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060267V',
            (TxtCtl.SetColor, 0x5),
            '吵架拖太长的话，\n',
            '可能会发展到非本意的离别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060268V',
            (TxtCtl.SetColor, 0x5),
            '这样的日子最好\n',
            '不要两人单独相处，\n',
            '应该和共同的朋友一起行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1720060269V',
            (TxtCtl.SetColor, 0x5),
            '如果对方说了什么不好的话，\n',
            '不要太过在意，\n',
            '要用自己宽容的心去听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8CF7')

    def _loc_8BB5(): pass

    label('loc_8BB5')

    OP_74(0x0006, 0x00000000, 0x0000)
    PlaySE(236, 0x00, 0x64)
    OP_7C(0, 300, 3000, 100)
    PlaySE(247, 0x00, 0x64)
    OP_20(0x00000000)
    FadeOut(500, 0, -1)
    OP_5F(0x0001)
    OP_5F(0x0000)
    OP_56(0x00)
    OP_0D()
    Sleep(500)

    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '4 Error(s)...  0 Warning(s)...\n',
            '导力相性占卜机...强制中止',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1721170002V',
            (TxtCtl.SetColor, 0x2),
            '导力相性占卜机\n',
            'Version:1.0014.4082\n',
            '(C)Genis Royal School 1202\n',
            '#200W　#20W\n',
            'MEMORY_CHECK#100W..........#20WOK!\n',
            '#200W　#20W\n',
            '重启动',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 290, 56, 3)
    OP_56(0x00)
    FadeIn(500, 0)
    OP_1E()
    PlaySE(157, 0x00, 0x64)
    OP_74(0x0006, 0x00000000, 0x0001)
    OP_0D()

    Jump('loc_8CF7')

    def _loc_8CF7(): pass

    label('loc_8CF7')

    SetMessageWindowPos(72, 290, 56, 3)
    OP_5F(0x0001)
    OP_5F(0x0000)
    OP_74(0x0006, 0x00000000, 0x0001)
    TalkSetChrName('占卜机')

    Talk(
        (
            '#1720060272V',
            (TxtCtl.SetColor, 0x5),
            '要继续占卜吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7A6A')

    def _loc_8D3A(): pass

    label('loc_8D3A')

    SetMessageWindowPos(72, 320, 56, 3)
    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)
    Fade(1000)
    OP_74(0x0006, 0x00000000, 0x0000)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_8D7D',
    )

    Jump('loc_8DCA')

    def _loc_8D7D(): pass

    label('loc_8D7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_8D87',
    )

    Jump('loc_8DCA')

    def _loc_8D87(): pass

    label('loc_8D87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_8DAF',
    )

    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x002C, 0x0080)

    Jump('loc_8DCA')

    def _loc_8DAF(): pass

    label('loc_8DAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_8DCA',
    )

    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)

    def _loc_8DCA(): pass

    label('loc_8DCA')

    EventEnd(0x01)

    Return()

# id: 0x004B offset: 0x8DCD
@scena.Code('func_4B_8DCD')
def func_4B_8DCD():
    OP_13(0x006F)

    Return()

# id: 0x004C offset: 0x8DD1
@scena.Code('func_4C_8DD1')
def func_4C_8DD1():
    OP_13(0x005E)

    Return()

# id: 0x004D offset: 0x8DD5
@scena.Code('func_4D_8DD5')
def func_4D_8DD5():
    OP_13(0x006E)

    Return()

# id: 0x004E offset: 0x8DD9
@scena.Code('func_4E_8DD9')
def func_4E_8DD9():
    OP_13(0x0074)

    Return()

# id: 0x004F offset: 0x8DDD
@scena.Code('func_4F_8DDD')
def func_4F_8DDD():
    OP_13(0x0073)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
