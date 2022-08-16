import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2523_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2523   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2523.x'
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
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02280._CH', 'ED6_DT07/CH02280P._CP'),
        ('ED6_DT07/CH02260._CH', 'ED6_DT07/CH02260P._CP'),
        ('ED6_DT07/CH02270._CH', 'ED6_DT07/CH02270P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT06/CH20088._CH', 'ED6_DT06/CH20088P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH02413._CH', 'ED6_DT07/CH02413P._CP'),
        ('ED6_DT07/CH02063._CH', 'ED6_DT07/CH02063P._CP'),
        ('ED6_DT07/CH02103._CH', 'ED6_DT07/CH02103P._CP'),
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT06/CH20069._CH', 'ED6_DT06/CH20069P._CP'),
        ('ED6_DT06/CH20068._CH', 'ED6_DT06/CH20068P._CP'),
        ('ED6_DT06/CH20071._CH', 'ED6_DT06/CH20071P._CP'),
        ('ED6_DT06/CH20070._CH', 'ED6_DT06/CH20070P._CP'),
        ('ED6_DT06/CH20072._CH', 'ED6_DT06/CH20072P._CP'),
        ('ED6_DT06/CH20073._CH', 'ED6_DT06/CH20073P._CP'),
        ('ED6_DT06/CH20075._CH', 'ED6_DT06/CH20075P._CP'),
        ('ED6_DT06/CH20076._CH', 'ED6_DT06/CH20076P._CP'),
        ('ED6_DT07/CH01223._CH', 'ED6_DT07/CH01223P._CP'),
        ('ED6_DT07/CH01573._CH', 'ED6_DT07/CH01573P._CP'),
        ('ED6_DT06/CH20131._CH', 'ED6_DT06/CH20131P._CP'),
        ('ED6_DT06/CH20135._CH', 'ED6_DT06/CH20135P._CP'),
        ('ED6_DT06/CH20136._CH', 'ED6_DT06/CH20136P._CP'),
        ('ED6_DT07/CH02573._CH', 'ED6_DT07/CH02573P._CP'),
    ]

# id: 0x10001 offset: 0x202
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔儿',
            x                   = 59640,
            z                   = 1000,
            y                   = 13450,
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
            name                = '汉斯',
            x                   = 66040,
            z                   = 1000,
            y                   = 16210,
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
            name                = '波利',
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '特蕾莎院长',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '达尼艾尔',
            x                   = 6000,
            z                   = 200,
            y                   = 22200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '玛丽',
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '克拉姆',
            x                   = 4300,
            z                   = 200,
            y                   = 22900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '白色公主塞茜莉亚',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红骑士尤利乌斯',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
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
            name                = '苍骑士奥斯卡',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
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
            name                = '侍女玲珐',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
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
            name                = '侍女蕾妮',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
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
            name                = '拉多公爵',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '科洛多议长',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '醉汉',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '平民男子',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '王都的主教',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族女孩',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空之女神爱德丝',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '杜南公爵',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '管家菲利普',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '戴尔蒙市长',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '奈尔',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '凯诺娜上尉',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '梅贝尔市长',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '莉拉',
            x                   = 4300,
            z                   = 200,
            y                   = 2900,
            direction           = 180,
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
            name                = '莱维',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '米克',
            x                   = -64500,
            z                   = 0,
            y                   = 4500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '勤务员巴克斯',
            x                   = -30,
            z                   = 0,
            y                   = -2630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '\u3000',
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
            name                = '观众',
            x                   = -3500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3500,
            z                   = 200,
            y                   = 7100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65575,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 852007,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131111,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196647,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262183,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3500,
            z                   = 200,
            y                   = 5100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589863,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655399,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 720935,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3500,
            z                   = 200,
            y                   = 3100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327719,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 852007,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917543,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983079,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1048615,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1114151,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179687,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1245223,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3500,
            z                   = 200,
            y                   = 1100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393255,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -3500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1376295,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -2500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1441831,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -1500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458791,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = -500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65575,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131111,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 1500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196647,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 2500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262183,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '观众',
            x                   = 3500,
            z                   = 200,
            y                   = -900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xAE2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xAE2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xAE2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xAE2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_AEC',
    )

    Jump('loc_BE9')

    def _loc_AEC(): pass

    label('loc_AEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_AF6',
    )

    Jump('loc_BE9')

    def _loc_AF6(): pass

    label('loc_AF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_BA1',
    )

    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, -64400, 0, 3560, 270)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0025, 140, 0, 7810, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000B, -37340, 1000, 5500, 0)
    ChrSetPos(0x000E, -33510, 1000, 7750, 90)
    ChrSetPos(0x000C, -34240, 1000, 8280, 45)
    ChrSetPos(0x000A, -37450, 1000, 9490, 0)
    ChrSetPos(0x000D, -36430, 1000, 8790, 0)
    CreateThread(0x000C, 0x00, 0x00, func_03_D9B)

    Jump('loc_BE9')

    def _loc_BA1(): pass

    label('loc_BA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_BB0',
    )

    ChrClearFlags(0x0025, 0x0080)

    Jump('loc_BE9')

    def _loc_BB0(): pass

    label('loc_BB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_BBA',
    )

    Jump('loc_BE9')

    def _loc_BBA(): pass

    label('loc_BBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_BC4',
    )

    Jump('loc_BE9')

    def _loc_BC4(): pass

    label('loc_BC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_BCE',
    )

    Jump('loc_BE9')

    def _loc_BCE(): pass

    label('loc_BCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_BD8',
    )

    Jump('loc_BE9')

    def _loc_BD8(): pass

    label('loc_BD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_BE2',
    )

    Jump('loc_BE9')

    def _loc_BE2(): pass

    label('loc_BE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_BE9',
    )

    def _loc_BE9(): pass

    label('loc_BE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_C00',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0B_10F7)

    def _loc_C00(): pass

    label('loc_C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_C0E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0C_193E)

    def _loc_C0E(): pass

    label('loc_C0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_C1C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_10_22DD)

    def _loc_C1C(): pass

    label('loc_C1C')

    Return()

# id: 0x0001 offset: 0xC1D
@scena.Code('func_01_C1D')
def func_01_C1D():
    Return()

# id: 0x0002 offset: 0xC1E
@scena.Code('func_02_C1E')
def func_02_C1E():
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
        'loc_C43',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_D85')

    def _loc_C43(): pass

    label('loc_C43')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C5C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_D85')

    def _loc_C5C(): pass

    label('loc_C5C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C75',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_D85')

    def _loc_C75(): pass

    label('loc_C75')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C8E',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_D85')

    def _loc_C8E(): pass

    label('loc_C8E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_D85')

    def _loc_CA7(): pass

    label('loc_CA7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC0',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_D85')

    def _loc_CC0(): pass

    label('loc_CC0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CD9',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_D85')

    def _loc_CD9(): pass

    label('loc_CD9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_D85')

    def _loc_CF2(): pass

    label('loc_CF2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D0B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_D85')

    def _loc_D0B(): pass

    label('loc_D0B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D24',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_D85')

    def _loc_D24(): pass

    label('loc_D24')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D3D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_D85')

    def _loc_D3D(): pass

    label('loc_D3D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D56',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_D85')

    def _loc_D56(): pass

    label('loc_D56')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D6F',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_D85')

    def _loc_D6F(): pass

    label('loc_D6F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D85',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_D85(): pass

    label('loc_D85')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D9A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_D85')

    def _loc_D9A(): pass

    label('loc_D9A')

    Return()

# id: 0x0003 offset: 0xD9B
@scena.Code('func_03_D9B')
def func_03_D9B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DD9',
    )

    ChrMoveTo(0x00FE, -35090, 1000, 9150, 2000, 0x00)
    Sleep(5000)

    ChrMoveTo(0x00FE, -34730, 1000, 8670, 2000, 0x00)
    Sleep(5000)

    Jump('func_03_D9B')

    def _loc_DD9(): pass

    label('loc_DD9')

    Return()

# id: 0x0004 offset: 0xDDA
@scena.Code('func_04_DDA')
def func_04_DDA():
    TalkBegin(0x0024)

    ChrTalk(
        0x00FE,
        (
            '唉，好困啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '演出什么的好麻烦，\n',
            '真不想干呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些都是那个\n',
            '多事的学生会长想出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0024)

    Return()

# id: 0x0005 offset: 0xE45
@scena.Code('func_05_E45')
def func_05_E45():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_E9B',
    )

    ChrTalk(
        0x00FE,
        (
            '再过一会儿演出就要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多该\n',
            '用广播把演员们召集过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F6E')

    def _loc_E9B(): pass

    label('loc_E9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_F6E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_F01',
    )

    ChrTalk(
        0x00FE,
        (
            '这里只能在下午使用时才开放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在正照科林兹校长的吩咐\n',
            '进行安全检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F6E')

    def _loc_F01(): pass

    label('loc_F01')

    ChrTalk(
        0x00FE,
        (
            '呼，昨天学院的庭院装饰\n',
            '忙得我眼都花了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次总算赶上了，\n',
            '下次再做这个的话，\n',
            '必须要请同学们帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F6E(): pass

    label('loc_F6E')

    TalkEnd(0x0025)

    Return()

# id: 0x0006 offset: 0xF72
@scena.Code('func_06_F72')
def func_06_F72():
    TalkBegin(0x000E)

    ChrTalk(
        0x00FE,
        (
            '#0400060400V#772F波利对各种事情都观察得很细致……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060401V不过平时就喜欢一直发呆……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0007 offset: 0xFDE
@scena.Code('func_07_FDE')
def func_07_FDE():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '#0420060402V姐姐们，\n',
            '我好期待你们的演出呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x1016
@scena.Code('func_08_1016')
def func_08_1016():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '#0430060403V约修亚哥哥刚才\n',
            '神情慌张地去找那个\n',
            '银色头发的哥哥了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1063
@scena.Code('func_09_1063')
def func_09_1063():
    TalkBegin(0x000D)

    ChrTalk(
        0x00FE,
        (
            '#0410060404V啊……\n',
            '好漂亮的连衣裙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410060405V长大之后\n',
            '我也一定要穿穿看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x10C0
@scena.Code('func_0A_10C0')
def func_0A_10C0():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '#0390060399V#752F怎么样，\n',
            '找到约修亚了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x10F7
@scena.Code('func_0B_10F7')
def func_0B_10F7():
    FormationAddMember(0x01, 0xFF)
    EventBegin(0x00)
    CameraMove(60000, 1000, 15800, 0)
    OP_67(0, 6230, -10000, 0)
    CameraSetDistance(1420, 0)
    OP_6C(0, 0)
    OP_6E(672, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetPos(0x0101, 60020, 1000, 13500, 0)
    ChrSetPos(0x0105, 61000, 1000, 14070, 315)
    ChrSetPos(0x0102, 59020, 1000, 14260, 45)
    ChrSetPos(0x0009, 59630, 1000, 15700, 180)
    ChrSetPos(0x0008, 60430, 1000, 15570, 180)
    OP_20(0x00000000)
    FadeOut(0, 0, -1)
    Sleep(3000)

    OP_1E()
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0510060001V#644F#2P大道具、小道具全准备妥当了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060002V灯光也调整好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060003V#641F好！\n',
            '这样一切都准备好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060004V#730F#1P差不多可以对外开放了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060005V离上演还有点时间，\n',
            '在那之前你们先四处玩玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060006V#001F那是当然的啦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060007V我要去把小吃摊\n',
            '一个个地逛个够才行～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060008V#019F逛逛倒是没什么关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060009V不过可别吃得太撑，\n',
            '万一演到一半动不了可就不妙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060010V#000F这、这我知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060011V#000F说起来……\n',
            '大家要一起去逛吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060012V#640F#2P我和汉斯还有学生会的事要做，\n',
            '所以就不能陪你们去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060013V你们自己玩得开心点吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060014V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060015V#044F学生会的事……\n',
            '难道是昨天说的那件？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060016V我也去帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060017V#648F#2P不用不用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060018V你就带着艾丝蒂尔他们\n',
            '在学院里好好逛一圈吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060019V而且，\n',
            '那些小家伙也差不多该到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060020V#043F嗯……那工作就麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060021V#730F#1P不要紧，有时间的话，\n',
            '我们也会好好地玩一番哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060022V#733F啊，对了，约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060023V#731F要是在客人当中\n',
            '看到了我喜欢的那类女生，\n',
            '记得要悄悄地过来告诉我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060024V我好溜出去找她搭讪㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060025V#017F是是，知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060026V#010F漂亮的身材高的\n',
            '有成熟魅力的大姐姐是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060027V#731F#1P喔，这才是我的好哥们儿⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 1, 0x449)),
            Expr.Return,
        ),
        'loc_179E',
    )

    ChrTalk(
        0x0008,
        (
            '#0510060028V#645F#2P真是的，男生就是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060029V#503F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060030V#045F……哎，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060031V#643F#2P哎，你们两个怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1816')

    def _loc_179E(): pass

    label('loc_179E')

    ChrTalk(
        0x0008,
        (
            '#0510060032V#645F#2P真是的，男生就是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060033V#007F嗯，真是搞不懂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060034V#045F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1816(): pass

    label('loc_1816')

    PlaySE(196, 0x00, 0x64)
    OP_20(0x000005DC)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            '#1560060035V',
            (TxtCtl.SetColor, 0x5),
            '……让各位久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1560060036V',
            (TxtCtl.SetColor, 0x5),
            '杰尼丝王立学院第５２届学园祭，\n',
            '现在正式开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x193E
@scena.Code('func_0C_193E')
def func_0C_193E():
    FormationDelMember(0x01, 0xFF)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(-34250, 1000, 11220, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0101, -36570, 250, 850, 0)
    ChrSetPos(0x0105, -36570, 250, 850, 0)
    ChrSetPos(0x000B, -36570, 250, 850, 0)
    ChrSetPos(0x000A, -35500, 1000, 9370, 0)
    ChrSetPos(0x000C, -36440, 1000, 8910, 0)
    ChrSetPos(0x000D, -37080, 1000, 9450, 0)
    ChrSetPos(0x000E, -36170, 1000, 9850, 0)
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000B, 255)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0105, 0x0040)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0400060341V#771F#4P哇～\n',
            '看这个，太帅了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060342V要是我也能穿就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410060343V你太矮了，不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410060344V我也好想穿穿\n',
            '这白礼服试试啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1AFB')
    def lambda_1AFB():
        CameraMove(-34950, 1000, 8980, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AFB)

    CreateThread(0x0101, 0x01, 0x00, func_0D_21A8)
    CreateThread(0x0105, 0x01, 0x00, func_0E_220A)
    CreateThread(0x000B, 0x01, 0x00, func_0F_2271)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010060345V#001F呵～呵～\n',
            '看来大家都很开心嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060346V#004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010060347V#004F约修亚去哪里了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BBB')
    def lambda_1BBB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1BBB)

    Sleep(100)

    @scena.Lambda('lambda_1BCE')
    def lambda_1BCE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1BCE)

    @scena.Lambda('lambda_1BDC')
    def lambda_1BDC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1BDC)

    Sleep(100)

    @scena.Lambda('lambda_1BEF')
    def lambda_1BEF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1BEF)

    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#0400060348V#774F约修亚哥哥？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060349V他把我们\n',
            '带到这儿之后，\n',
            '就不知跑到哪儿去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410060350V他说要我们\n',
            '等着姐姐们过来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060351V#002F嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060352V#043F到底怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060353V#2P嘿嘿～\n',
            '波利知道哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060354V#2P约修亚哥哥\n',
            '肯定是去找那个\n',
            '银色头发的哥哥了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000A, 400)
    ChrTurnDirection(0x0101, 0x000A, 400)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010060355V#501F银色头发的哥哥？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060356V#2P就是火灾的时候\n',
            '把波利和大家\n',
            '救出来的那位哥哥啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060357V#2P头发是银色的，好漂亮呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010060358V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060359V#044F那、那个人\n',
            '在学院里出现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060360V#2P嗯～\n',
            '不过我只看到了一眼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060361V#2P而且约修亚哥哥\n',
            '也把眼睛睁得圆圆的看着他呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000E, 0xFF)
    ChrTurnDirection(0x000E, 0x000A, 400)

    ChrTalk(
        0x000E,
        (
            '#0400060362V#772F波利，你这家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400060363V为什么那时候\n',
            '没跟我们说啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0430060364V#2P因为因为，\n',
            '我那时在忙着吃薄荷饼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060365V#042F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060366V#002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060367V#002F特蕾莎院长。\n',
            '我们失陪一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0390060368V#750F嗯……\n',
            '你还是快去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060369V科洛丝。\n',
            '你也陪她一起去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390060370V找到约修亚要紧，\n',
            '你们不用管我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000B, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060371V#043F对不起，老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0420060372V哎？\n',
            '姐姐你们也要走吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000E, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060373V#045F嗯……抱歉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060374V#040F好好等着舞台剧开演吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060375V#006F是啊是啊，\n',
            '大家要睁大眼睛好好看哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2500._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x21A8
@scena.Code('func_0D_21A8')
def func_0D_21A8():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -35720, 0, 3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -34090, 0, 5180, 3000, 0x00)
    ChrWalkTo(0x00FE, -34240, 1000, 7390, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -36760, 1000, 7200, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x220A
@scena.Code('func_0E_220A')
def func_0E_220A():
    Sleep(500)

    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -35720, 0, 3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -34090, 0, 5180, 3000, 0x00)
    ChrWalkTo(0x00FE, -34240, 1000, 7390, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -35670, 1000, 7150, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x2271
@scena.Code('func_0F_2271')
def func_0F_2271():
    Sleep(500)

    Sleep(700)

    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -35720, 0, 3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -34090, 0, 5180, 3000, 0x00)
    ChrWalkTo(0x00FE, -34240, 1000, 7390, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -34750, 1000, 8550, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0010 offset: 0x22DD
@scena.Code('func_10_22DD')
def func_10_22DD():
    FormationAddMember(0x01, 0xFF)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(2220, 0, 290, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetFlags(0x001D, 0x0004)
    ChrSetFlags(0x001C, 0x0004)
    ChrSetFlags(0x001E, 0x0004)
    ChrSetFlags(0x001B, 0x0004)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetFlags(0x0021, 0x0004)
    ChrSetFlags(0x0022, 0x0004)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x001F, 0x0004)
    ChrSetFlags(0x0025, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)
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
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrSetPos(0x001D, 500, 0, 7200, 0)
    ChrSetPos(0x001C, -500, 200, 7200, 0)
    ChrSetPos(0x001E, -2500, 200, 7200, 0)
    ChrSetPos(0x001B, -3500, 200, 7200, 0)
    ChrSetPos(0x0020, 2500, 200, 5200, 0)
    ChrSetPos(0x0021, 2500, 200, 7200, 0)
    ChrSetPos(0x0022, 3500, 0, 7200, 0)
    ChrSetPos(0x000D, -3500, 200, 3200, 0)
    ChrSetPos(0x000A, -2500, 200, 3200, 0)
    ChrSetPos(0x000B, -1500, 200, 3200, 0)
    ChrSetPos(0x000C, -500, 200, 3200, 0)
    ChrSetPos(0x000E, 500, 200, 3200, 0)
    ChrSetChipByIndex(0x000B, 42)
    ChrSetSubChip(0x000B, 0)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    ChrSetPos(0x001F, 3500, 200, -800, 0)
    ChrSetPos(0x0023, 0, -250, -5430, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 4700, 1000, 14420, 180)
    FadeIn(2000, 0)
    CameraMove(4700, 1000, 14420, 5000)
    ChrSetDirection(0x0010, 90, 400)
    ChrWalkTo(0x0010, 6060, 1000, 14670, 3000, 0x00)
    Fade(1000)
    CameraMove(-34890, 1000, 8480, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0014, -36680, 1000, 9450, 180)
    ChrSetPos(0x0015, -37710, 1000, 8930, 180)
    ChrSetPos(0x0016, -37550, 1000, 9790, 180)
    ChrSetPos(0x0018, 60020, 1000, 18870, 180)
    ChrSetPos(0x0012, -34800, 1000, 8460, 225)
    ChrSetPos(0x0013, -34310, 1000, 7560, 270)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x000F, -35990, 1000, 8670, 180)
    ChrSetPos(0x0011, -36100, 1000, 7440, 270)
    ChrSetPos(0x0010, -40540, 1000, 6830, 180)
    ChrSetPos(0x0008, -36960, 1000, 5930, 0)
    ChrSetPos(0x0009, -37860, 1000, 6000, 0)

    @scena.Lambda('lambda_2697')
    def lambda_2697():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2697')

    DispatchAsync2(0x000F, 0x0001, lambda_2697)

    @scena.Lambda('lambda_26A8')
    def lambda_26A8():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_26A8')

    DispatchAsync2(0x0008, 0x0001, lambda_26A8)

    @scena.Lambda('lambda_26B9')
    def lambda_26B9():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_26B9')

    DispatchAsync2(0x0009, 0x0001, lambda_26B9)

    ChrWalkTo(0x0010, -37540, 1000, 7580, 3000, 0x00)

    NpcTalk(
        0x0010,
        '艾丝蒂尔',
        (
            '#0010060455V#343F哇～……\n',
            '真的好多人呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060456V#347F啊～已经开始感到紧张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0011,
        '科洛丝',
        (
            '#0060060457V#355F#2P没事的，艾丝蒂尔。\n',
            '毕竟我们练习了不少时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '约修亚',
        (
            '#0020060458V#360F#5P而且只要演出一开始，\n',
            '就会完全注意不到其他的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060459V因为你是那种\n',
            '只能专注于一件事的类型嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '艾丝蒂尔',
        (
            '#0010060460V#349F哼，就知道取笑我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060461V#341F不过算啦，你现在这副样子，\n',
            '不管说什么我都不会生气哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '约修亚',
        (
            '#0020060462V#368F#5P哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060463V#644F好了好了。\n',
            '打情骂俏就到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0008, 400)
    ChrTurnDirection(0x0011, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0510060464V#644F……今年的学园祭盛况空前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060465V虽然有公爵啊市长啊\n',
            '这样的大人物在，\n',
            '但是我们也用不着太过紧张。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060466V#648F像练习时那样表演就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060467V#730F#6P这么盛大的学园祭，\n',
            '全是凭我们自己的双手举办的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060468V#731F就让我们坚持到最后，\n',
            '来个花团锦簇的完美结局吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Call(0, 0x0016)
    CameraMove(63040, 4300, 7500, 0)
    OP_20(0x000003E8)
    OP_72(0x0009, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Sleep(1000)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    PlaySE(139, 0x00, 0x64)
    Sleep(9000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            '#1560060469V',
            (TxtCtl.SetColor, 0x5),
            '……让各位观众久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1560060470V',
            (TxtCtl.SetColor, 0x5),
            '由学生会主办的历史剧『白花恋诗』，\n',
            '现在正式开演。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1560060471V',
            (TxtCtl.SetColor, 0x5),
            '请各位观众慢慢地\n',
            '欣赏这部经典的舞台剧吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1500, 0)
    OP_0D()
    MapSetFlags(0x00000004)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x26),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0026, 0x0040)
    ChrSetFlags(0x0026, 0x0004)
    ChrSetPos(0x0026, 63580, 2000, 13750, 180)
    ChrSetPos(0x0008, 63580, 1000, 13750, 180)
    def _loc_2BCC(): pass

    label('loc_2BCC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BF1',
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x1A),
            (Expr.PushLong, 0x5DC0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2BED',
    )

    Jump('loc_2BF1')

    def _loc_2BED(): pass

    label('loc_2BED')

    Yield()

    Jump('loc_2BCC')

    def _loc_2BF1(): pass

    label('loc_2BF1')

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x5DC0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0510060472V#647F#5P时值七耀历１１００年……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060473V１００年前的利贝尔，\n',
            '贵族制度还依然存在着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060474V#642F同时，以商人为中心的\n',
            '平民势力也开始崭露头角……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060475V贵族势力与平民势力之间的\n',
            '对立和争斗日趋激烈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060476V#647F王家和教会的居间调停\n',
            '也无法化解双方的矛盾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(93)
    ChrSetPos(0x000F, 60000, 1000, 14400, 180)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2D4B')
    def lambda_2D4B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2D4B)

    def _loc_2D57(): pass

    label('loc_2D57')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2D7C',
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x1A),
            (Expr.PushLong, 0x13880),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2D78',
    )

    Jump('loc_2D7C')

    def _loc_2D78(): pass

    label('loc_2D78')

    Yield()

    Jump('loc_2D57')

    def _loc_2D7C(): pass

    label('loc_2D7C')

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0510060477V#644F#5P就在那样的时代……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060478V当时的国王病逝之后，\n',
            '大约过了一年左右……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060479V一个早春的夜晚，\n',
            '在格兰赛尔城顶层的空中庭园中，\n',
            '故事开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E3A')
    def lambda_2E3A():
        ChrMoveTo(0x00FE, 60000, 2300, 15560, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_2E3A)

    @scena.Lambda('lambda_2E55')
    def lambda_2E55():
        CameraMove(60010, 4300, 7500, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2E55)

    ChrSetDirection(0x0008, 315, 400)
    ChrWalkTo(0x0008, 62220, 1000, 15730, 2000, 0x00)
    ChrWalkTo(0x0008, 62650, 1000, 16940, 2000, 0x00)
    ChrWalkTo(0x0008, 65600, 1000, 18740, 2000, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0026, 0x0001)
    ChrSetPos(0x0013, 55350, 1000, 17130, 90)
    ChrSetPos(0x0012, 55440, 1000, 18180, 90)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x000003E8)
    WaitForThreadExit(0x0026, 0x0001)
    Sleep(1500)

    ChrTalk(
        0x000F,
        (
            '#0020060480V#363F#5P街道的光华，是人的灵魂在闪耀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060481V那点点灯火之下，\n',
            '人们沉醉于各自的幸福中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060482V#365F啊啊，然而我却……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_2F9E')
    def lambda_2F9E():
        ChrWalkTo(0x00FE, 61390, 1000, 16880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2F9E)

    Sleep(700)

    @scena.Lambda('lambda_2FBE')
    def lambda_2FBE():
        ChrWalkTo(0x00FE, 58700, 1000, 16700, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2FBE)

    WaitForThreadExit(0x0013, 0x0001)

    @scena.Lambda('lambda_2FDE')
    def lambda_2FDE():
        ChrSetDirection(0x00FE, 135, 300)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2FDE)

    WaitForThreadExit(0x0012, 0x0001)

    @scena.Lambda('lambda_2FF1')
    def lambda_2FF1():
        ChrSetDirection(0x00FE, 225, 300)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2FF1)

    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#1570060483V#1P公主殿下……\n',
            '原来您在这儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060484V#2P是时候就寝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060485V#2P如此深夜还未作息，\n',
            '会累坏身子的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060486V#363F#5P不要紧。\n',
            '如果我病倒了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060487V就不会成为\n',
            '点燃这场利贝尔纷争的火种。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#1570060488V#1P啊，公主殿下，\n',
            '请千万不要这么说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060489V#2P公主殿下是利贝尔的至宝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060490V#2P将会与优秀的驸马殿下结合，\n',
            '共同治理王国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060491V#367F#5P我，不会成婚的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060492V虽说是父王的遗言，\n',
            '但仅此一事无论如何也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#1570060493V#1P为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#1570060494V#1P有那样杰出的求婚者，\n',
            '而且还是两位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060495V#2P一位是公爵家的长子，\n',
            '近卫骑士团长尤利乌斯大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#1570060496V#1P另一位是，虽为平民出身，\n',
            '却在与帝国的战斗中功勋卓著的\n',
            '猛将奥斯卡大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#2P#1K啊～两位都是那么无懈可击㈱',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0013,
        (
            '#1570060498V#1P#1K啊～两位都是那么无懈可击㈱',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(500)

    OP_56(0x01)
    OP_59()
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#0020060499V#363F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060500V他们都是优秀的人物，\n',
            '这点我比谁都更加清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 180, 300)
    Sleep(200)

    ChrWalkTo(0x000F, 60020, 1000, 12610, 1500, 0x00)
    ChrSetChipByIndex(0x000F, 41)
    ChrSetFlags(0x000F, 0x0002)
    OP_99(0x000F, 0x00, 0x04, 1000)
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#0020060501V#365F#5P啊，奥斯卡、尤利乌斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060502V我到底……\n',
            '该选择谁才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_1F(0x5A, 0x000000C8)
    OP_66(0x0001)
    CameraMove(3120, 0, 7140, 0)
    Call(0, 0x0017)
    OP_0D()

    ChrTalk(
        0x0021,
        (
            '#0360060503V#611F#5P（啊，那名公主殿下……\n',
            '　不就是约修亚吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060504V（呵呵，竟然是男女反串……\n',
            '　看来乔儿也真是煞费苦心了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0370060505V#621F#2P（是的，小姐。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370060506V#623F（约修亚先生的演技自不必说，\n',
            '　但他身边的两名侍女实在是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    Call(0, 0x0016)
    OP_71(0x0009, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0010, 61060, 1000, 14810, 242)
    ChrSetPos(0x0011, 58970, 1000, 12820, 47)

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x7530),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xE, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xE, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xE, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0026, 0x00, 0x00, func_12_92C7)
    PlayBGM(94)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0010,
        (
            '#0010060507V#420F#2P还记得吗，奥斯卡？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060508V小时候，提着半截木棍\n',
            '在这小胡同里四处乱跑的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060509V#352F尤利乌斯……\n',
            '我怎么会忘得了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060510V那些和你，还有塞茜莉亚殿下\n',
            '一起度过的无忧无虑的快乐日子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060511V是我一生中无可取代的回忆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 180, 400)

    @scena.Lambda('lambda_3769')
    def lambda_3769():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_3769')

    DispatchAsync2(0x0011, 0x0000, lambda_3769)

    ChrWalkTo(0x0010, 60990, 1000, 12860, 2000, 0x00)

    ChrTalk(
        0x0010,
        (
            '#0010060512V#420F呵呵，那时真是吃了一惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060513V没想到偷偷溜去玩的\n',
            '竟然不止我一个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0011, 0xFF)
    ChrSetDirection(0x0011, 180, 300)

    ChrTalk(
        0x0011,
        (
            '#0060060514V#358F如飘舞散落的樱花般楚楚可怜，\n',
            '又如清水般纯洁无暇的少女。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060515V塞茜莉亚殿下对我们来说，\n',
            '简直就是如同太阳般的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 225, 300)

    ChrTalk(
        0x0010,
        (
            '#0010060516V#421F然而，\n',
            '那份光辉却日渐蒙上阴影。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060517V贵族势力和平民势力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060518V两者的对立\n',
            '已迎来无可回避的局面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060519V#424F公主的叹息也无济于事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 135, 300)

    ChrTalk(
        0x0011,
        (
            '#0060060520V#359F而且……\n',
            '啊啊，的确是难以言表。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060521V加深了那叹息的并非他人，\n',
            '正是我们二人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_1F(0x5A, 0x000000C8)
    CameraMove(-1340, 0, 3500, 0)
    Call(0, 0x0017)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0410060522V#5P（呀呀！\n',
            '　姐姐他们好酷呢！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0400060523V#774F#2P（虽、虽然不服气……\n',
            '　不过简直比男人还帅啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0390060524V#751F#5P（呵呵……\n',
            '　大家安安静静地看哦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0016)
    OP_71(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0014, 0x0004)
    ChrSetChipByIndex(0x0014, 37)
    ChrSetPos(0x0014, 57800, 1200, 17630, 135)
    ChrSetPos(0x0010, 60510, 1000, 13460, 315)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x14, 0x1),
            (Expr.GetChrWork, 0x10, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x14, 0x2),
            (Expr.GetChrWork, 0x10, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x14, 0x3),
            (Expr.GetChrWork, 0x10, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0026, 0x00, 0x00, func_13_9314)
    FadeIn(1000, 0)
    PlayBGM(95)
    OP_0D()

    ChrTalk(
        0x0014,
        (
            '#1590060525V#5P尤利乌斯，你该明白吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060526V#5P不能再让平民势力\n',
            '继续增大下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060527V#5P若是有一天，\n',
            '我们要尊奉的主人是平民出身……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060528V#5P那么，拥有优秀传统的利贝尔\n',
            '就将会威严扫地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0010, 59120, 1000, 15160, 2000, 0x00)

    ChrTalk(
        0x0010,
        (
            '#0010060529V#424F#2P恕我直言，父亲大人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060530V自东方的共和国建国以来，\n',
            '到现在已过了１０年的岁月。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060531V#421F我想，平民势力的抬头，\n',
            '恐怕也是时代趋势的必然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D01')
    def lambda_3D01():
        ChrTurnDirection(0x00FE, 0x0014, 0)
        Yield()

        Jump('lambda_3D01')

    DispatchAsync2(0x0010, 0x0000, lambda_3D01)

    ChrSetChipByIndex(0x0014, 12)
    ChrJumpTo(0x0014, 57510, 1000, 17030, 300, 5000)
    ChrWalkTo(0x0014, 57470, 1000, 15280, 3000, 0x00)
    ChrTurnDirection(0x0014, 0x0010, 800)

    ChrTalk(
        0x0014,
        (
            '#1590060532V#5P#3S别说这种混帐话！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetFlags(0x0014, 0x0040)
    OP_92(0x0014, 0x0010, 400, 3000, 0x00)

    @scena.Lambda('lambda_3D95')
    def lambda_3D95():
        OP_94(0x01, 0x0014, 0x0000, 0x0000012C, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3D95)

    OP_94(0x01, 0x0010, 0x00B4, 0x00000258, 0x00000BB8, 0x00)
    OP_94(0x01, 0x0010, 0x00B4, 0x0000012C, 0x000005DC, 0x00)
    WaitForThreadExit(0x0014, 0x0003)

    ChrTalk(
        0x0014,
        (
            '#1590060533V#5P#3S什么叫自由！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetFlags(0x0014, 0x0040)
    OP_92(0x0014, 0x0010, 400, 3000, 0x00)

    @scena.Lambda('lambda_3E16')
    def lambda_3E16():
        OP_94(0x01, 0x0014, 0x0000, 0x0000012C, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_3E16)

    OP_94(0x01, 0x0010, 0x00B4, 0x00000258, 0x00000BB8, 0x00)
    OP_94(0x01, 0x0010, 0x00B4, 0x0000012C, 0x000005DC, 0x00)
    WaitForThreadExit(0x0014, 0x0003)

    ChrTalk(
        0x0014,
        (
            '#1590060534V#5P#3S什么叫平等！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060535V#5P根本就是丢弃传统，\n',
            '将高贵和下贱混为一谈的无耻想法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060536V#5P就算向帝国投降，\n',
            '也远比屈膝于平民之下要好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0010060537V#422F#2P#3S父亲大人！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_1F(0x5A, 0x000000C8)
    TerminateThread(0x0010, 0xFF)
    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x00000000)
    CameraMove(20, 0, 6850, 0)
    Call(0, 0x0017)
    OP_0D()

    ChrTalk(
        0x001C,
        (
            '#0640060538V#227F嗝……\n',
            '这公爵说的也是理所当然啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640060539V容许平民放肆的话，\n',
            '就只会让利贝尔威严扫地而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0660060540V#722F（公爵大人……\n',
            '　请您说话时稍微小声些……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0016)
    OP_71(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x15, 0x1),
            (Expr.GetChrWork, 0x11, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x15, 0x2),
            (Expr.GetChrWork, 0x11, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x15, 0x3),
            (Expr.GetChrWork, 0x11, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0026, 0x00, 0x00, func_15_93AE)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    ChrSetPos(0x0015, 58930, 1000, 17140, 138)
    ChrSetPos(0x0011, 61080, 1000, 15250, 336)

    @scena.Lambda('lambda_40DA')
    def lambda_40DA():
        ChrTurnDirection(0x00FE, 0x0015, 0)
        Yield()

        Jump('lambda_40DA')

    DispatchAsync2(0x0011, 0x0001, lambda_40DA)

    OP_1F(0x64, 0x000000C8)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0015,
        (
            '#1600060541V#5P奥斯卡。\n',
            '我对你抱有很高的期望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060542V#5P只要得到王家的支持，\n',
            '那我们必定压倒贵族派。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060543V#5P这样一来，\n',
            '我们平民派就能掌握主导权了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060544V#352F#2P但是议长……\n',
            '请恕我无法接受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060545V我不能为了如此的政治目的，\n',
            '而利用纯洁的塞茜莉亚殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060546V#5P哼哼，说得真是清高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060547V#5P虽说国王只是空有名号，\n',
            '但这毕竟是千载难逢的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0015, 59000, 1000, 13450, 2000, 0x00)
    ChrSetDirection(0x0015, 223, 300)
    Sleep(300)

    ChrTalk(
        0x0015,
        (
            '#1600060548V#5P如果你拒绝，\n',
            '那唯有发起流血的革命了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060549V#5P不要说贵族，\n',
            '就连王族也要消失在历史的黑暗之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0060060550V#356F#2P#3S议长！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    TerminateThread(0x0026, 0xFF)
    Sleep(100)

    Fade(1000)
    OP_1F(0x5A, 0x000000C8)
    TerminateThread(0x0011, 0xFF)
    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x00000000)
    CameraMove(-2940, 0, 7230, 0)
    Call(0, 0x0017)
    OP_0D()

    ChrTalk(
        0x001E,
        (
            '#0490060551V#661F（嗯，了不起啊。\n',
            '　时代考证的确做得相当精细。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490060552V（最先听说是男女反串时，\n',
            '　我还担心他们不知会弄出什么来呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0530060553V#781F（呵呵，\n',
            '　这都是全体学生努力的成果。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060554V#780F（而且还要多亏\n',
            '　那两名游击士的鼎力协助……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0016)
    OP_71(0x000C, 0x0004)
    OP_72(0x000D, 0x0004)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0026, 60000, 1000, 14500, 135)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    ChrSetPos(0x0011, 59530, 1000, 13290, 135)
    ChrSetPos(0x0016, 64230, 1000, 18550, 60)
    ChrSetRGBAMask(0x0016, 255, 255, 255, 0, 0)
    OP_1F(0x64, 0x000000C8)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0011,
        (
            '#0060060555V#357F#5P我绝不能允许\n',
            '有任何流血革命发生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060556V绝不能让尤利乌斯和\n',
            '塞茜莉亚殿下遭遇不测……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060557V#359F我到底……\n',
            '该怎么做才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x000007D0)

    @scena.Lambda('lambda_45E6')
    def lambda_45E6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_45E6)

    ChrWalkTo(0x0016, 61730, 1000, 16780, 2000, 0x00)

    ChrTalk(
        0x0016,
        (
            '#1610060558V#10A#5P呃……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_462B')
    def lambda_462B():
        ChrTurnDirection(0x0011, 0x0016, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_462B)

    OP_97(0x0016, 62350, 15650, -120000, 2000, 0x0000)
    OP_97(0x0016, 62350, 15650, 10000, 4000, 0x0000)
    OP_97(0x0016, 62350, 15650, -10000, 4000, 0x0000)

    @scena.Lambda('lambda_4678')
    def lambda_4678():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0000, lambda_4678)

    OP_9E(0x0016, 30, 0, 500, 3000)

    ChrTalk(
        0x0016,
        (
            '#1610060559V#5P呜呜……\n',
            '不行了……好恶心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0016, 400)
    ChrTurnDirection(0x0011, 0x0016, 400)

    ChrTalk(
        0x0011,
        (
            '#0060060560V#354F#5P啊，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 60850, 1000, 13840, 2000, 0x00)

    ChrTalk(
        0x0011,
        (
            '#0060060561V#352F#5P喝得太多会伤身子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060562V就算已经到了春天，\n',
            '睡在这种地方还是会着凉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0016, 0x0011, 200)

    ChrTalk(
        0x0016,
        (
            '#1610060563V#2P呜呜……好心的骑士大人……\n',
            '真是谢谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060564V#357F#5P不要叫我骑士大人了……\n',
            '其实我并不是什么大人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060565V#359F只是一个不知自己该做什么，\n',
            '迷失了方向的傻瓜罢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1610060566V#2P一点都没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060567V#354F#5P什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0016, 0x0004)
    OP_92(0x0016, 0x0011, 400, 8000, 0x00)
    PlaySE(509, 0x00, 0x64)

    @scena.Lambda('lambda_48AE')
    def lambda_48AE():
        OP_94(0x01, 0x0016, 0x0000, 0x0000012C, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_48AE)

    ChrTurnDirection(0x0011, 0x0016, 0)
    OP_94(0x01, 0x0011, 0x00B4, 0x000003E8, 0x00001F40, 0x00)
    OP_94(0x01, 0x0011, 0x00B4, 0x000001F4, 0x00000FA0, 0x00)
    LoadEffect(0x00, 'map\\\\mp020_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 60320, 1050, 12670, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0016, 0x0003)
    OP_77(0xA0, 0x1E, 0x1E, 0x00, 0x000005DC)
    Fade(1000)
    ChrSetChipByIndex(0x0011, 34)
    ChrSetSubChip(0x0011, 0)
    OP_0D()
    Sleep(500)

    OP_9E(0x0011, 30, 0, 300, 4000)

    ChrTalk(
        0x0011,
        (
            '#0060060568V#430F呜，我的手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0016, 62540, 1900, 15340, 1800, 5000)

    ChrTalk(
        0x0016,
        (
            '#1610060569V#2P嘿嘿嘿……\n',
            '这匕首上涂有麻药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1610060570V#2P你就老老实实地认命吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0011, 0x00, 0x04, 800)

    ChrTalk(
        0x0011,
        (
            '#0060060571V#356F你……\n',
            '是谁派你来行刺的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0016,
        '暗杀者',
        (
            '#1610060572V#2P某位大人嫌你十分碍眼，\n',
            '于是他就请了我来收拾你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0016,
        '暗杀者',
        (
            '#1610060573V#2P定金也给得很大方，\n',
            '你就给我去死吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    MapClearFlags(0x00000004)
    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x00000000)
    MapSetFlags(0x00000004)
    CameraMove(5120, 0, 670, 0)
    Call(0, 0x0017)
    OP_1F(0x5A, 0x000000C8)
    OP_0D()

    ChrTalk(
        0x001F,
        (
            '#0270060574V#141F#5P（原来如此……\n',
            '　编剧做得很不错啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060575V（之后的剧情又会怎样呢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060576V#143F（……坏了坏了。\n',
            '　差点把正事给忘了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    StopEffect(0x00, 0x00)
    Call(0, 0x0016)
    OP_71(0x000D, 0x0004)
    OP_72(0x000E, 0x0004)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x000F, 0x0002)
    ChrSetSubChip(0x000F, 0)
    ChrSetChipByIndex(0x000F, 40)
    ChrSetPos(0x0010, 66410, 1000, 16219, 90)
    ChrSetPos(0x000F, 58610, 1000, 14250, 315)
    FadeIn(1000, 0)
    PlayBGM(96)
    OP_0D()
    ChrWalkTo(0x0010, 61510, 1000, 14130, 2000, 0x00)
    ChrSetDirection(0x0010, 225, 400)

    ChrTalk(
        0x0010,
        (
            '#0010060577V#420F好久不见了，公主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 135, 400)

    ChrTalk(
        0x000F,
        (
            '#0020060578V#360F#5P尤利乌斯……\n',
            '真是好久不见了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060579V今天……\n',
            '没和奥斯卡一起来吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060580V父王还健在的时候……\n',
            '你们在宫廷谈笑风生的英姿，\n',
            '曾经让侍女们仰慕不已呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060581V#424F……公主您也知道，\n',
            '王国正面临存亡的危机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060582V要我和他亲密如初，\n',
            '恐怕已是遥不可及的梦想了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060583V#363F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060584V#421F今天，\n',
            '我是来向公主请求一件事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060585V#364F#5P请求……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060586V#421F我和奥斯卡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060587V请允许我们，以近卫骑士团长\n',
            '与青年猛将的身份进行决斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060588V并希望胜利者……\n',
            '能有幸成为公主的夫婿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060589V#362F#5P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(2830, 0, 5700, 0)
    Call(0, 0x0017)
    OP_0D()

    ChrTalk(
        0x0020,
        (
            '#0610060590V#182F（呵呵……\n',
            '　很有戏剧性嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0011)

    Return()

# id: 0x0011 offset: 0x4F4E
@scena.Code('func_11_4F4E')
def func_11_4F4E():
    EventBegin(0x00)
    ChrSetPos(0x0101, 56670, 1000, 13640, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    Call(0, 0x0016)
    CameraMove(60000, 4300, 7500, 0)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_72(0x000F, 0x0004)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetFlags(0x001D, 0x0004)
    ChrSetFlags(0x001C, 0x0004)
    ChrSetFlags(0x001E, 0x0004)
    ChrSetFlags(0x001B, 0x0004)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetFlags(0x0021, 0x0004)
    ChrSetFlags(0x0022, 0x0004)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x001F, 0x0004)
    ChrSetFlags(0x0025, 0x0080)
    ChrClearFlags(0x002F, 0x0080)
    ChrClearFlags(0x0030, 0x0080)
    ChrClearFlags(0x0031, 0x0080)
    ChrClearFlags(0x0032, 0x0080)
    ChrClearFlags(0x0033, 0x0080)
    ChrClearFlags(0x0034, 0x0080)
    ChrClearFlags(0x0036, 0x0080)
    ChrClearFlags(0x003C, 0x0080)
    ChrClearFlags(0x003D, 0x0080)
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
    ChrClearFlags(0x004B, 0x0080)
    ChrClearFlags(0x004C, 0x0080)
    ChrClearFlags(0x004D, 0x0080)
    ChrSetPos(0x001D, 500, 0, 7200, 0)
    ChrSetPos(0x001C, -500, 200, 7200, 0)
    ChrSetPos(0x001E, -2500, 200, 7200, 0)
    ChrSetPos(0x001B, -3500, 200, 7200, 0)
    ChrSetPos(0x0020, 2500, 200, 5200, 0)
    ChrSetPos(0x0021, 2500, 200, 7200, 0)
    ChrSetPos(0x0022, 3500, 0, 7200, 0)
    ChrSetPos(0x000D, -3500, 200, 3200, 0)
    ChrSetPos(0x000A, -2500, 200, 3200, 0)
    ChrSetPos(0x000B, -1500, 200, 3200, 0)
    ChrSetPos(0x000C, -500, 200, 3200, 0)
    ChrSetPos(0x000E, 500, 200, 3200, 0)
    ChrSetChipByIndex(0x000B, 42)
    ChrSetSubChip(0x000B, 0)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    ChrSetPos(0x001F, 3500, 200, -800, 0)
    ChrSetPos(0x0023, 0, -250, -5430, 0)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    FadeIn(1000, 0)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, 57100, 1000, 14000, 129)
    ChrSetPos(0x0011, 62900, 1000, 14000, 219)
    ChrSetPos(0x0015, 62100, 1000, 16600, 225)
    ChrSetPos(0x0014, 57900, 1000, 16600, 135)
    ChrSetPos(0x0017, 58300, 1000, 18930, 180)
    ChrSetPos(0x0018, 60000, 1000, 17730, 180)
    ChrSetPos(0x0019, 61700, 1000, 18930, 180)
    ChrSetPos(0x0013, 59250, 1000, 18200, 180)
    ChrSetPos(0x0012, 60750, 1000, 18200, 180)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0015, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0014, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0017, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0018, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0019, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0010, 7)
    ChrSetChipByIndex(0x0011, 8)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0011, 0)
    MapSetFlags(0x00000004)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x26),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0026, 0x0040)
    ChrSetFlags(0x0026, 0x0004)
    ChrSetPos(0x0026, 60000, 2000, 12500, 180)
    ChrSetPos(0x0008, 60000, 1000, 12500, 180)
    def _loc_5380(): pass

    label('loc_5380')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_53A5',
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x1A),
            (Expr.PushLong, 0x5DC0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_53A1',
    )

    Jump('loc_53A5')

    def _loc_53A1(): pass

    label('loc_53A1')

    Yield()

    Jump('loc_5380')

    def _loc_53A5(): pass

    label('loc_53A5')

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x5DC0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0510060591V#647F#5P在贵族势力和平民势力的\n',
            '斗争漩涡中身不由己……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060592V曾亲密无间的两位骑士\n',
            '终于走上了决斗的舞台。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060593V意识到他们决心的公主\n',
            '也唯有默默无言地面对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060594V#642F终于到了决斗的那一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(97)

    @scena.Lambda('lambda_549F')
    def lambda_549F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_549F)

    @scena.Lambda('lambda_54B1')
    def lambda_54B1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_54B1)

    @scena.Lambda('lambda_54C3')
    def lambda_54C3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_54C3)

    @scena.Lambda('lambda_54D5')
    def lambda_54D5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_54D5)

    @scena.Lambda('lambda_54E7')
    def lambda_54E7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_54E7)

    @scena.Lambda('lambda_54F9')
    def lambda_54F9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_54F9)

    @scena.Lambda('lambda_550B')
    def lambda_550B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_550B)

    @scena.Lambda('lambda_551D')
    def lambda_551D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_551D)

    @scena.Lambda('lambda_552F')
    def lambda_552F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_552F)

    @scena.Lambda('lambda_5541')
    def lambda_5541():
        ChrMoveTo(0x00FE, 60000, 2300, 15560, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_5541)

    def _loc_5556(): pass

    label('loc_5556')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_557B',
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x1A),
            (Expr.PushLong, 0x13880),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5577',
    )

    Jump('loc_557B')

    def _loc_5577(): pass

    label('loc_5577')

    Yield()

    Jump('loc_5556')

    def _loc_557B(): pass

    label('loc_557B')

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0026, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0510060595V#647F王都的王立竞技场上，\n',
            '挺立着两位骑士的身姿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060596V贵族、平民、中立人士，\n',
            '成群结队的人们前来观战……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060597V但是，当中却唯独不见\n',
            '塞茜莉亚公主的身影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_5653')
    def lambda_5653():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_5653')

    DispatchAsync2(0x0015, 0x0001, lambda_5653)

    @scena.Lambda('lambda_5664')
    def lambda_5664():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_5664')

    DispatchAsync2(0x0014, 0x0001, lambda_5664)

    @scena.Lambda('lambda_5675')
    def lambda_5675():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_5675')

    DispatchAsync2(0x0017, 0x0001, lambda_5675)

    @scena.Lambda('lambda_5686')
    def lambda_5686():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_5686')

    DispatchAsync2(0x0018, 0x0001, lambda_5686)

    @scena.Lambda('lambda_5697')
    def lambda_5697():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_5697')

    DispatchAsync2(0x0019, 0x0001, lambda_5697)

    @scena.Lambda('lambda_56A8')
    def lambda_56A8():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_56A8')

    DispatchAsync2(0x0013, 0x0001, lambda_56A8)

    @scena.Lambda('lambda_56B9')
    def lambda_56B9():
        ChrTurnDirection(0x00FE, 0x0026, 0)
        Yield()

        Jump('lambda_56B9')

    DispatchAsync2(0x0012, 0x0001, lambda_56B9)

    ChrWalkTo(0x0008, 63920, 1000, 11840, 2000, 0x00)

    @scena.Lambda('lambda_56DE')
    def lambda_56DE():
        ChrWalkTo(0x00FE, 64290, 0, 6930, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_56DE)

    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x000007D0)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0080)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0010060598V#424F挚友啊。\n',
            '事已至此你我别无选择……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060599V命中注定\n',
            '我们终要决一雌雄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x0010, 29)
    ChrSetDirection(0x0010, 90, 0)
    ChrSetSubChip(0x0010, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0010060600V#421F拔剑！\n',
            '为了彼此所背负的责任！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060601V更为了你我心爱的公主！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0060060602V#359F所谓命运，\n',
            '是凭自己的双手开拓的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060603V本应承担的立场与公主的微笑，\n',
            '此时此刻是那么的遥远……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060604V#422F你怕了吗，奥斯卡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060605V#357F然而，此刻驱使着身体的，\n',
            '这近乎疯狂的热情究竟是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060606V我似乎再次不可避免地\n',
            '在此与你一决高下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x0011, 31)
    ChrSetDirection(0x0011, 270, 0)
    ChrSetSubChip(0x0011, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0060060607V#352F在以革命之名的暴风雨\n',
            '将一切吞没之前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060608V以手中的剑刃决定命运吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060609V#420F啊啊……\n',
            '空之女神将见证你我二人的灵魂！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060610V来吧，一决胜负！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060611V#356F来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x15F90),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.GetChrWork, 0x11, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x10, 0x2),
            (Expr.GetChrWork, 0x11, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.GetChrWork, 0x11, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0026, 0x00, 0x00, func_15_93AE)
    OP_20(0x000003E8)
    OP_21()
    Sleep(1000)

    PlayBGM(98)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetChipByIndex(0x0011, 32)
    ChrSetChipByIndex(0x0010, 30)

    @scena.Lambda('lambda_5A8C')
    def lambda_5A8C():
        ChrWalkTo(0x00FE, 60900, 1000, 14300, 7000, 0x01)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5A8C)

    @scena.Lambda('lambda_5AA7')
    def lambda_5AA7():
        ChrWalkTo(0x00FE, 59100, 1000, 13700, 7000, 0x01)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5AA7)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_5AC7')
    def lambda_5AC7():
        ChrWalkTo(0x00FE, 60700, 1000, 14300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5AC7)

    @scena.Lambda('lambda_5AE2')
    def lambda_5AE2():
        ChrWalkTo(0x00FE, 59300, 1000, 13700, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5AE2)

    ChrSetChipByIndex(0x0011, 31)
    ChrSetChipByIndex(0x0010, 29)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0010, 0x0020)
    ChrSetSubChip(0x0011, 2)
    ChrSetSubChip(0x0010, 2)
    WaitForThreadExit(0x0011, 0x0001)
    PlaySE(132, 0x00, 0x64)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_5B2A')
    def lambda_5B2A():
        ChrMoveTo(0x00FE, 60800, 1000, 14300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5B2A)

    @scena.Lambda('lambda_5B45')
    def lambda_5B45():
        ChrMoveTo(0x00FE, 59200, 1000, 13700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5B45)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_5B65')
    def lambda_5B65():
        OP_9E(0x00FE, 30, 0, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_5B65)

    @scena.Lambda('lambda_5B7F')
    def lambda_5B7F():
        OP_9E(0x00FE, 30, 0, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_5B7F)

    @scena.Lambda('lambda_5B99')
    def lambda_5B99():
        ChrMoveTo(0x00FE, 60400, 1000, 14000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5B99)

    @scena.Lambda('lambda_5BB4')
    def lambda_5BB4():
        ChrMoveTo(0x00FE, 59600, 1000, 14000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5BB4)

    Sleep(200)

    ChrSetDirection(0x0010, 135, 0)
    ChrSetDirection(0x0011, 225, 0)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0011, 0x0002)
    ChrSetSubChip(0x0011, 13)
    ChrSetSubChip(0x0010, 13)
    ChrSetDirection(0x0010, 90, 0)
    ChrSetDirection(0x0011, 270, 0)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_5C09')
    def lambda_5C09():
        ChrJumpTo(0x00FE, 61600, 1000, 14000, 350, 5000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5C09)

    @scena.Lambda('lambda_5C27')
    def lambda_5C27():
        ChrJumpTo(0x00FE, 58400, 1000, 14000, 350, 5000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5C27)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetSubChip(0x0011, 12)
    ChrSetSubChip(0x0010, 12)
    PlaySE(164, 0x00, 0x64)
    Sleep(400)

    @scena.Lambda('lambda_5C5E')
    def lambda_5C5E():
        OP_97(0x00FE, 60000, 14000, 30000, 1400, 0x0002)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5C5E)

    @scena.Lambda('lambda_5C7A')
    def lambda_5C7A():
        OP_97(0x00FE, 60000, 14000, 30000, 1400, 0x0002)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5C7A)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_5C9B')
    def lambda_5C9B():
        OP_97(0x00FE, 60000, 14000, 32000, 1700, 0x0002)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5C9B)

    @scena.Lambda('lambda_5CB7')
    def lambda_5CB7():
        OP_97(0x00FE, 60000, 14000, 32000, 1700, 0x0002)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5CB7)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_5CD8')
    def lambda_5CD8():
        OP_97(0x00FE, 60000, 14000, 33000, 2000, 0x0002)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5CD8)

    @scena.Lambda('lambda_5CF4')
    def lambda_5CF4():
        OP_97(0x00FE, 60000, 14000, 33000, 2000, 0x0002)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5CF4)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_5D15')
    def lambda_5D15():
        OP_97(0x00FE, 60000, 14000, 30000, 1500, 0x0002)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5D15)

    @scena.Lambda('lambda_5D31')
    def lambda_5D31():
        OP_97(0x00FE, 60000, 14000, 30000, 1500, 0x0002)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5D31)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_5D52')
    def lambda_5D52():
        OP_97(0x00FE, 60000, 14000, 15000, 1000, 0x0002)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5D52)

    @scena.Lambda('lambda_5D6E')
    def lambda_5D6E():
        OP_97(0x00FE, 60000, 14000, 15000, 1000, 0x0002)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5D6E)

    WaitForThreadExit(0x0011, 0x0001)
    Sleep(400)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0010, 13)

    @scena.Lambda('lambda_5D9E')
    def lambda_5D9E():
        ChrJumpTo(0x00FE, 59280, 1000, 13470, 1500, 6000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5D9E)

    Sleep(400)

    PlaySE(132, 0x00, 0x64)
    PlaySE(214, 0x00, 0x64)
    ChrSetSubChip(0x0010, 2)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_5DD5')
    def lambda_5DD5():
        ChrMoveTo(0x00FE, 58180, 1000, 12240, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5DD5)

    Sleep(20)

    ChrSetSubChip(0x0011, 8)

    @scena.Lambda('lambda_5DFA')
    def lambda_5DFA():
        ChrMoveTo(0x00FE, 58180, 1000, 12240, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5DFA)

    Sleep(20)

    @scena.Lambda('lambda_5E1A')
    def lambda_5E1A():
        ChrMoveTo(0x00FE, 58180, 1000, 12240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5E1A)

    Sleep(20)

    @scena.Lambda('lambda_5E3A')
    def lambda_5E3A():
        ChrMoveTo(0x00FE, 58180, 1000, 12240, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5E3A)

    WaitForThreadExit(0x0011, 0x0001)
    Sleep(50)

    ChrSetSubChip(0x0010, 3)
    ChrSetSubChip(0x0011, 8)

    @scena.Lambda('lambda_5E69')
    def lambda_5E69():
        OP_97(0x00FE, 59280, 13470, -90000, 7000, 0x0002)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5E69)

    Sleep(200)

    @scena.Lambda('lambda_5E8A')
    def lambda_5E8A():
        ChrSetDirection(0x00FE, 146, 800)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5E8A)

    WaitForThreadExit(0x0011, 0x0001)
    Sleep(100)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0011, 9)
    ChrMoveTo(0x0011, 60040, 1000, 12730, 8000, 0x00)
    PlaySE(214, 0x00, 0x64)
    ChrSetSubChip(0x0010, 0)
    ChrMoveTo(0x0010, 58520, 1000, 14510, 8000, 0x00)

    @scena.Lambda('lambda_5EDE')
    def lambda_5EDE():
        OP_9E(0x00FE, 30, 0, 400, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5EDE)

    OP_9E(0x0010, 30, 0, 400, 4000)
    ChrSetSubChip(0x0010, 8)
    Sleep(100)

    PlaySE(214, 0x00, 0x64)
    ChrSetSubChip(0x0010, 10)
    ChrSetDirection(0x0011, 270, 0)
    Sleep(100)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0010, 11)
    ChrSetSubChip(0x0011, 12)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_5F3F')
    def lambda_5F3F():
        ChrJumpTo(0x00FE, 60090, 1000, 14650, 500, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5F3F)

    WaitForThreadExit(0x0011, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0010, 5)
    Sleep(300)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0010, 7)

    @scena.Lambda('lambda_5F7B')
    def lambda_5F7B():
        ChrWalkTo(0x00FE, 61060, 1000, 14760, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5F7B)

    Sleep(50)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0011, 13)

    @scena.Lambda('lambda_5FA5')
    def lambda_5FA5():
        ChrJumpTo(0x00FE, 59130, 1000, 14760, 1600, 7000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5FA5)

    WaitForThreadExit(0x0011, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0011, 12)
    ChrSetDirection(0x0011, 269, 0)
    WaitForThreadExit(0x0010, 0x0001)
    ChrSetSubChip(0x0010, 12)
    ChrSetDirection(0x0010, 91, 0)
    Sleep(300)

    ChrSetSubChip(0x0010, 6)
    ChrSetSubChip(0x0011, 6)

    @scena.Lambda('lambda_5FF9')
    def lambda_5FF9():
        ChrSetDirection(0x0010, 225, 700)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5FF9)

    @scena.Lambda('lambda_6007')
    def lambda_6007():
        ChrSetDirection(0x0011, 135, 700)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6007)

    @scena.Lambda('lambda_6015')
    def lambda_6015():
        ChrMoveTo(0x00FE, 60700, 1000, 14760, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6015)

    @scena.Lambda('lambda_6030')
    def lambda_6030():
        ChrMoveTo(0x00FE, 59300, 1000, 14760, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_6030)

    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_605A')
    def lambda_605A():
        OP_9E(0x00FE, 20, 0, 1500, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_605A)

    @scena.Lambda('lambda_6074')
    def lambda_6074():
        OP_9E(0x00FE, 20, 0, 1500, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_6074)

    Sleep(100)

    @scena.Lambda('lambda_6093')
    def lambda_6093():
        ChrMoveTo(0x00FE, 61100, 1000, 14760, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6093)

    @scena.Lambda('lambda_60AE')
    def lambda_60AE():
        ChrMoveTo(0x00FE, 58900, 1000, 14760, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_60AE)

    Sleep(300)

    ChrSetDirection(0x0010, 270, 0)
    ChrSetDirection(0x0011, 90, 0)

    @scena.Lambda('lambda_60DC')
    def lambda_60DC():
        ChrMoveTo(0x00FE, 60700, 1000, 14760, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_60DC)

    @scena.Lambda('lambda_60F7')
    def lambda_60F7():
        ChrMoveTo(0x00FE, 59300, 1000, 14760, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_60F7)

    Sleep(100)

    ChrSetDirection(0x0010, 315, 0)
    ChrSetDirection(0x0011, 45, 0)
    Sleep(1000)

    PlaySE(163, 0x00, 0x64)
    ChrSetDirection(0x0010, 270, 0)
    ChrSetDirection(0x0011, 90, 0)

    @scena.Lambda('lambda_613D')
    def lambda_613D():
        ChrJumpTo(0x00FE, 58000, 1000, 14800, 400, 8000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_613D)

    @scena.Lambda('lambda_615B')
    def lambda_615B():
        ChrJumpTo(0x00FE, 62000, 1000, 14800, 400, 8000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_615B)

    WaitForThreadExit(0x0011, 0x0001)
    PlaySE(164, 0x00, 0x64)
    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0010, 3)
    ChrSetSubChip(0x0011, 3)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x0010, 0x0004)

    @scena.Lambda('lambda_619C')
    def lambda_619C():
        ChrJumpTo(0x00FE, 59500, 3000, 14800, 2050, 8000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_619C)

    @scena.Lambda('lambda_61BA')
    def lambda_61BA():
        ChrJumpTo(0x00FE, 60500, 3000, 14800, 2050, 8000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_61BA)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetPos(0x0011, 60000, 3000, 14800, 90)
    ChrSetPos(0x0010, 60000, 3000, 14800, 270)
    ChrSetChipByIndex(0x0011, 33)
    ChrSetSubChip(0x0011, 0)
    ChrSetFlags(0x0010, 0x0080)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_6213')
    def lambda_6213():
        ChrSetDirection(0x00FE, 270, 700)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_6213)

    @scena.Lambda('lambda_6221')
    def lambda_6221():
        ChrSetDirection(0x00FE, 90, 700)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_6221)

    @scena.Lambda('lambda_622F')
    def lambda_622F():
        ChrJumpTo(0x00FE, 59910, 1000, 14800, 0, 6000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_622F)

    @scena.Lambda('lambda_624D')
    def lambda_624D():
        ChrJumpTo(0x00FE, 60090, 1000, 14800, 0, 6000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_624D)

    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_6270')
    def lambda_6270():
        OP_9E(0x00FE, 20, 0, 1000, 3500)
        Yield()

        Jump('lambda_6270')

    DispatchAsync2(0x0011, 0x0002, lambda_6270)

    @scena.Lambda('lambda_628D')
    def lambda_628D():
        OP_9E(0x00FE, 20, 0, 1000, 3500)
        Yield()

        Jump('lambda_628D')

    DispatchAsync2(0x0010, 0x0002, lambda_628D)

    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0060060612V#352F#2P不错啊，尤利乌斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060613V#420F#1P彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060614V但是，似乎……\n',
            '你心中仍存留着迷茫吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetChipByIndex(0x0011, 31)
    ChrSetSubChip(0x0011, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0011, 60500, 1000, 14800, 270)
    ChrSetPos(0x0010, 59500, 1000, 14800, 90)
    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0010, 5)
    ChrJumpTo(0x0010, 58800, 1000, 14800, 400, 6000)
    ChrSetSubChip(0x0010, 6)
    PlaySE(132, 0x00, 0x64)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_639F')
    def lambda_639F():
        ChrMoveTo(0x00FE, 60000, 1000, 14700, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_639F)

    @scena.Lambda('lambda_63BA')
    def lambda_63BA():
        ChrMoveTo(0x00FE, 62000, 1000, 14800, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_63BA)

    Sleep(30)

    @scena.Lambda('lambda_63DA')
    def lambda_63DA():
        ChrMoveTo(0x00FE, 62000, 1000, 14800, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_63DA)

    Sleep(30)

    @scena.Lambda('lambda_63FA')
    def lambda_63FA():
        ChrMoveTo(0x00FE, 62000, 1000, 14800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_63FA)

    Sleep(30)

    @scena.Lambda('lambda_641A')
    def lambda_641A():
        ChrMoveTo(0x00FE, 62000, 1000, 14800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_641A)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetSubChip(0x0010, 5)
    Sleep(100)

    ChrSetSubChip(0x0010, 7)

    @scena.Lambda('lambda_6449')
    def lambda_6449():
        ChrMoveTo(0x00FE, 61610, 1000, 14810, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6449)

    PlaySE(132, 0x00, 0x64)
    PlaySE(214, 0x00, 0x64)
    ChrSetDirection(0x0011, 315, 0)

    @scena.Lambda('lambda_6475')
    def lambda_6475():
        ChrMoveTo(0x00FE, 63000, 1000, 14300, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6475)

    Sleep(30)

    @scena.Lambda('lambda_6495')
    def lambda_6495():
        ChrMoveTo(0x00FE, 63000, 1000, 14300, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6495)

    Sleep(30)

    @scena.Lambda('lambda_64B5')
    def lambda_64B5():
        ChrMoveTo(0x00FE, 63000, 1000, 14300, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_64B5)

    Sleep(30)

    @scena.Lambda('lambda_64D5')
    def lambda_64D5():
        ChrMoveTo(0x00FE, 63000, 1000, 14300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_64D5)

    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    ChrSetSubChip(0x0010, 6)

    @scena.Lambda('lambda_64FF')
    def lambda_64FF():
        OP_9E(0x00FE, 20, 0, 600, 3500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_64FF)

    @scena.Lambda('lambda_6519')
    def lambda_6519():
        OP_9E(0x00FE, 20, 0, 600, 3500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6519)

    Sleep(300)

    @scena.Lambda('lambda_6538')
    def lambda_6538():
        ChrMoveTo(0x00FE, 62280, 1000, 14880, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6538)

    @scena.Lambda('lambda_6553')
    def lambda_6553():
        ChrMoveTo(0x00FE, 63000, 1000, 14000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6553)

    WaitForThreadExit(0x0010, 0x0001)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_6578')
    def lambda_6578():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_6578')

    DispatchAsync2(0x0010, 0x0001, lambda_6578)

    @scena.Lambda('lambda_6589')
    def lambda_6589():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_6589')

    DispatchAsync2(0x0011, 0x0003, lambda_6589)

    @scena.Lambda('lambda_659A')
    def lambda_659A():
        OP_97(0x00FE, 61610, 14810, 90000, 15000, 0x0000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_659A)

    WaitForThreadExit(0x0011, 0x0002)
    ChrSetSubChip(0x0010, 5)
    ChrSetSubChip(0x0011, 12)

    @scena.Lambda('lambda_65C5')
    def lambda_65C5():
        ChrMoveTo(0x00FE, 59490, 1000, 14830, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_65C5)

    Sleep(30)

    @scena.Lambda('lambda_65E5')
    def lambda_65E5():
        ChrMoveTo(0x00FE, 59490, 1000, 14830, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_65E5)

    Sleep(30)

    @scena.Lambda('lambda_6605')
    def lambda_6605():
        ChrMoveTo(0x00FE, 59490, 1000, 14830, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6605)

    Sleep(30)

    @scena.Lambda('lambda_6625')
    def lambda_6625():
        ChrMoveTo(0x00FE, 59490, 1000, 14830, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6625)

    Sleep(30)

    @scena.Lambda('lambda_6645')
    def lambda_6645():
        ChrMoveTo(0x00FE, 59490, 1000, 14830, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6645)

    Sleep(30)

    @scena.Lambda('lambda_6665')
    def lambda_6665():
        ChrMoveTo(0x00FE, 59490, 1000, 14830, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6665)

    WaitForThreadExit(0x0011, 0x0001)
    Sleep(200)

    ChrSetSubChip(0x0010, 4)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0011, 57600, 1000, 14830, 600, 4000)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0011, 32)
    ChrClearFlags(0x0011, 0x0020)
    ChrSetSubChip(0x0011, 0)

    @scena.Lambda('lambda_66BF')
    def lambda_66BF():
        ChrMoveTo(0x00FE, 60790, 1000, 14760, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_66BF)

    Sleep(380)

    ChrSetChipByIndex(0x0011, 31)
    ChrSetSubChip(0x0011, 0)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetSubChip(0x0010, 2)
    PlaySE(132, 0x00, 0x64)

    @scena.Lambda('lambda_66F8')
    def lambda_66F8():
        ChrMoveTo(0x00FE, 61400, 1000, 14880, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_66F8)

    @scena.Lambda('lambda_6713')
    def lambda_6713():
        ChrMoveTo(0x00FE, 58610, 1000, 14880, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6713)

    Sleep(20)

    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_6738')
    def lambda_6738():
        ChrMoveTo(0x00FE, 58610, 1000, 14880, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6738)

    Sleep(20)

    @scena.Lambda('lambda_6758')
    def lambda_6758():
        ChrMoveTo(0x00FE, 58610, 1000, 14880, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6758)

    Sleep(20)

    @scena.Lambda('lambda_6778')
    def lambda_6778():
        ChrMoveTo(0x00FE, 58610, 1000, 14880, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6778)

    Sleep(20)

    @scena.Lambda('lambda_6798')
    def lambda_6798():
        ChrMoveTo(0x00FE, 58610, 1000, 14880, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6798)

    Sleep(20)

    @scena.Lambda('lambda_67B8')
    def lambda_67B8():
        ChrMoveTo(0x00FE, 58610, 1000, 14880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_67B8)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetSubChip(0x0011, 3)
    Sleep(300)

    ChrTalk(
        0x0010,
        (
            '#0010060615V#345F#2P怎么了奥斯卡！\n',
            '你的剑法就仅此而已了吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060616V击退帝国的赫赫战功，\n',
            '靠的就只是这种程度的本领吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060617V#359F#1P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0060060618V#356F#1P#3S哦哦哦哦哦！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    TerminateThread(0x0011, 0xFF)
    ChrTurnDirection(0x0011, 0x0010, 0)

    @scena.Lambda('lambda_68CE')
    def lambda_68CE():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_68CE')

    DispatchAsync2(0x0010, 0x0001, lambda_68CE)

    ChrSetSubChip(0x0011, 13)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_68E9')
    def lambda_68E9():
        ChrJumpTo(0x0011, 60900, 1000, 14830, 2500, 8000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_68E9)

    Sleep(300)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0011, 2)
    ChrSetSubChip(0x0010, 3)

    @scena.Lambda('lambda_691B')
    def lambda_691B():
        ChrJumpTo(0x00FE, 61890, 1000, 13140, 400, 6000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_691B)

    Sleep(300)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0011, 7)

    @scena.Lambda('lambda_6948')
    def lambda_6948():
        ChrWalkTo(0x0011, 61810, 1000, 13040, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6948)

    Sleep(50)

    ChrSetSubChip(0x0010, 3)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_6972')
    def lambda_6972():
        ChrJumpTo(0x00FE, 63490, 1000, 12960, 400, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6972)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetSubChip(0x0011, 5)
    WaitForThreadExit(0x0010, 0x0001)
    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0011, 6)

    @scena.Lambda('lambda_69A9')
    def lambda_69A9():
        ChrWalkTo(0x0011, 64000, 1000, 13110, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_69A9)

    Sleep(50)

    ChrSetSubChip(0x0011, 7)
    ChrSetSubChip(0x0010, 13)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0010, 64910, 2640, 12820, 1700, 4000)
    PlaySE(164, 0x00, 0x64)
    ChrSetSubChip(0x0010, 12)
    ChrSetSubChip(0x0011, 5)
    Sleep(50)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_6A08')
    def lambda_6A08():
        ChrJumpTo(0x0010, 61480, 1000, 12820, 500, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6A08)

    ChrSetSubChip(0x0010, 12)
    Sleep(50)

    ChrSetSubChip(0x0011, 5)
    ChrSetDirection(0x0011, 270, 400)
    Sleep(100)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0011, 7)

    @scena.Lambda('lambda_6A4B')
    def lambda_6A4B():
        ChrWalkTo(0x0011, 62800, 1000, 12710, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6A4B)

    Sleep(100)

    @scena.Lambda('lambda_6A6B')
    def lambda_6A6B():
        ChrMoveTo(0x0011, 62800, 1000, 12710, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6A6B)

    PlaySE(214, 0x00, 0x64)
    ChrSetDirection(0x0011, 315, 0)
    ChrSetSubChip(0x0011, 6)
    ChrSetSubChip(0x0010, 3)
    Sleep(200)

    @scena.Lambda('lambda_6AA1')
    def lambda_6AA1():
        ChrMoveTo(0x0011, 62800, 1000, 12710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6AA1)

    ChrSetDirection(0x0010, 225, 0)

    @scena.Lambda('lambda_6AC3')
    def lambda_6AC3():
        OP_9E(0x00FE, 20, 0, 400, 3500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_6AC3)

    @scena.Lambda('lambda_6ADD')
    def lambda_6ADD():
        OP_9E(0x00FE, 20, 0, 400, 3500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6ADD)

    Sleep(400)

    ChrSetSubChip(0x0010, 8)

    @scena.Lambda('lambda_6B01')
    def lambda_6B01():
        ChrSetDirection(0x00FE, 135, 340)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6B01)

    @scena.Lambda('lambda_6B0F')
    def lambda_6B0F():
        OP_9E(0x00FE, 20, 0, 400, 3500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_6B0F)

    @scena.Lambda('lambda_6B29')
    def lambda_6B29():
        OP_9E(0x00FE, 20, 0, 400, 3500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6B29)

    Sleep(400)

    ChrSetSubChip(0x0010, 9)
    PlaySE(132, 0x00, 0x64)

    @scena.Lambda('lambda_6B52')
    def lambda_6B52():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6B52)

    @scena.Lambda('lambda_6B60')
    def lambda_6B60():
        ChrJumpTo(0x00FE, 58500, 1000, 12890, 500, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6B60)

    ChrSetSubChip(0x0011, 2)
    ChrSetDirection(0x0011, 270, 0)

    @scena.Lambda('lambda_6B8A')
    def lambda_6B8A():
        OP_94(0x01, 0x0011, 0x0000, 0x000001F4, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_6B8A)

    WaitForThreadExit(0x0010, 0x0002)
    ChrSetSubChip(0x0010, 3)
    WaitForThreadExit(0x0011, 0x0002)
    Sleep(500)

    ChrSetSubChip(0x0011, 3)

    @scena.Lambda('lambda_6BB9')
    def lambda_6BB9():
        ChrMoveTo(0x00FE, 61460, 1000, 12890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_6BB9)

    ChrSetDirection(0x0011, 270, 0)
    OP_77(0x5A, 0x5A, 0x5A, 0x00, 0x000007D0)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0060060619V#357F不愧是尤利乌斯……\n',
            '何等华丽的剑法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0011, 20, 0, 500, 4000)

    ChrTalk(
        0x0011,
        (
            '#0060060620V#430F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0010060621V#422F奥斯卡，你……\n',
            '你的手腕受伤了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060622V#352F不……只是擦伤而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060623V#422F可我们到目前为止\n',
            '并未伤及对方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060624V莫、莫非在决斗前你就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0015,
        (
            '#1600060625V#2P真卑鄙，拉多公爵！\n',
            '都是你搞的鬼吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060626V#5P呵呵呵……\n',
            '请别含血喷人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060627V#5P有证据证明是我指使的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0010060628V#422F父亲大人……你竟然这么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060629V#357F没关系，尤利乌斯。\n',
            '这也是因我的不成熟而造成的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060630V#358F何况，这种程度的伤，\n',
            '在战场上根本算不了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060631V#422F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060632V#357F就用下一剑来决定一切吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060633V#352F我会……\n',
            '全力出剑，绝不留情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060634V#421F奥斯卡，你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060635V#424F明白了……\n',
            '我也会在下一剑上赌上一切。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_6F7D')
    def lambda_6F7D():
        ChrJumpTo(0x00FE, 56300, 1000, 12860, 500, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_6F7D)

    @scena.Lambda('lambda_6F9B')
    def lambda_6F9B():
        ChrJumpTo(0x00FE, 63700, 1000, 12860, 500, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_6F9B)

    WaitForThreadExit(0x0010, 0x0002)
    PlaySE(164, 0x00, 0x64)
    Sleep(500)

    Fade(1000)
    ChrSetDirection(0x0010, 135, 0)
    ChrSetDirection(0x0011, 225, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0011, 0)
    OP_0D()

    ChrTalk(
        0x0010,
        (
            '#0010060636V#420F今后的人生、公主的笑颜，\n',
            '以及王国的未来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060637V胜者将要\n',
            '背负所有的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060638V#358F而败者则将\n',
            '化作灵魂守护这一切……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060639V无论胜负如何，都同为骑士的骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060640V#420F呵呵，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060641V#424F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060642V#357F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    ChrSetSubChip(0x0011, 5)
    ChrSetSubChip(0x0010, 5)
    ChrSetDirection(0x0010, 90, 0)
    ChrSetDirection(0x0011, 270, 0)
    OP_0D()

    @scena.Lambda('lambda_7151')
    def lambda_7151():
        OP_9E(0x00FE, 20, 0, 1000, 3500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_7151)

    @scena.Lambda('lambda_716B')
    def lambda_716B():
        OP_9E(0x00FE, 20, 0, 1000, 3500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_716B)

    ChrTalk(
        0x0010,
        (
            '#10A#1P#3S喝啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0011,
        (
            '#0060060644V#10A#2P#3S哦哦哦哦哦哦！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    ChrClearFlags(0x0011, 0x0020)
    ChrClearFlags(0x0010, 0x0020)
    ChrSetChipByIndex(0x0011, 32)
    ChrSetChipByIndex(0x0010, 30)

    @scena.Lambda('lambda_71E6')
    def lambda_71E6():
        ChrWalkTo(0x00FE, 59000, 1000, 14530, 7000, 0x01)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_71E6)

    @scena.Lambda('lambda_7201')
    def lambda_7201():
        ChrWalkTo(0x00FE, 61000, 1000, 14530, 7000, 0x01)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7201)

    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_7231')
    def lambda_7231():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_7231)

    ChrSetPos(0x000F, 62800, 1000, 18980, 0)

    @scena.Lambda('lambda_7254')
    def lambda_7254():
        ChrWalkTo(0x00FE, 60000, 1000, 13160, 9000, 0x01)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7254)

    OP_20(0x000003E8)
    FadeOut(500, 0, -1)
    Sleep(100)

    PlaySE(155, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女孩的声音')

    Talk(
        (
            '#0020060645V',
            (TxtCtl.SetColor, 0x0),
            '住手——————！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_0D()
    OP_56(0x00)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    ChrSetChipByIndex(0x0011, 31)
    ChrSetChipByIndex(0x0010, 29)
    ChrSetSubChip(0x0011, 2)
    ChrSetSubChip(0x0010, 2)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetFlags(0x0010, 0x0020)
    TerminateThread(0x000F, 0xFF)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 255, 0)
    ChrSetFlags(0x000F, 0x0800)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 35)
    ChrSetSubChip(0x000F, 0)
    ChrSetPos(0x000F, 60000, 1000, 13160, 0)
    FadeIn(300, 0)
    TerminateThread(0x0026, 0xFF)
    ChrSetPos(0x0026, 60010, 1000, 13880, 0)

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0xC350),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_734D')
    def lambda_734D():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_734D')

    DispatchAsync2(0x0015, 0x0001, lambda_734D)

    @scena.Lambda('lambda_735E')
    def lambda_735E():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_735E')

    DispatchAsync2(0x0014, 0x0001, lambda_735E)

    @scena.Lambda('lambda_736F')
    def lambda_736F():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_736F')

    DispatchAsync2(0x0017, 0x0001, lambda_736F)

    @scena.Lambda('lambda_7380')
    def lambda_7380():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_7380')

    DispatchAsync2(0x0018, 0x0001, lambda_7380)

    @scena.Lambda('lambda_7391')
    def lambda_7391():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_7391')

    DispatchAsync2(0x0019, 0x0001, lambda_7391)

    @scena.Lambda('lambda_73A2')
    def lambda_73A2():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_73A2')

    DispatchAsync2(0x0013, 0x0001, lambda_73A2)

    @scena.Lambda('lambda_73B3')
    def lambda_73B3():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_73B3')

    DispatchAsync2(0x0012, 0x0001, lambda_73B3)

    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0020060646V#364F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 3)
    ChrSetSubChip(0x0011, 3)

    @scena.Lambda('lambda_73F0')
    def lambda_73F0():
        OP_99(0x00FE, 0x00, 0x0D, 700)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_73F0)

    @scena.Lambda('lambda_7400')
    def lambda_7400():
        ChrSetDirection(0x0010, 225, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7400)

    @scena.Lambda('lambda_740E')
    def lambda_740E():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_740E)

    ChrTalk(
        0x0010,
        (
            '#422F#13A#2P什…………',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0011,
        (
            '#0060060648V#354F#13A#1P塞……茜莉亚……？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1300)

    ChrSetChipByIndex(0x0011, 8)

    @scena.Lambda('lambda_7472')
    def lambda_7472():
        ChrWalkTo(0x00FE, 59500, 1000, 14530, 2000, 0x01)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_7472)

    @scena.Lambda('lambda_748D')
    def lambda_748D():
        ChrSetDirection(0x00FE, 126, 0)
        Yield()

        Jump('lambda_748D')

    DispatchAsync2(0x0011, 0x0001, lambda_748D)

    ChrSetChipByIndex(0x0010, 7)
    ChrClearFlags(0x0010, 0x0020)

    @scena.Lambda('lambda_74A8')
    def lambda_74A8():
        ChrWalkTo(0x0010, 60960, 1000, 12170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_74A8)

    @scena.Lambda('lambda_74C3')
    def lambda_74C3():
        ChrTurnDirection(0x0010, 0x000F, 0)
        Yield()

        Jump('lambda_74C3')

    DispatchAsync2(0x0010, 0x0001, lambda_74C3)

    WaitForThreadExit(0x000F, 0x0001)
    ChrSetFlags(0x0011, 0x0080)
    OP_99(0x000F, 0x0E, 0x10, 1000)
    Sleep(800)

    PlayBGM(99)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0010060649V#422F#3S公、公主——————！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060650V#356F#1P塞茜莉亚，为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060651V你明明不在场的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000F, 0x10, 0x12, 900)
    Sleep(200)

    ChrTalk(
        0x000F,
        (
            '#0020060652V#361F太、太好了……\n',
            '奥斯卡、尤利乌斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060653V我本不想目睹\n',
            '你们两人决斗的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060654V但终究还是担心……\n',
            '所以……来阻止你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060655V#365F啊啊，幸好赶上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060656V#359F#5P塞茜莉亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060657V#422F公、公主……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060658V#361F请大家……听我说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060659V看在我的份上……\n',
            '请各位停止争斗吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060660V大家……都是深爱着利贝尔这片土地的\n',
            '……难能可贵的伙伴……不是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060661V只是……爱的方式……\n',
            '有少许不同罢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060662V如果大家携起手来……\n',
            '一定能够冲破这道墙壁的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060663V#5P公、公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060664V#2P够了……\n',
            '请别再多说话了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000F, 0x12, 0x11, 1000)

    ChrTalk(
        0x000F,
        (
            '#0020060665V#363F啊……眼睛好模糊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060666V对了……你们两个……\n',
            '都在……还在……这里吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060667V#343F是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060668V#359F#5P就在你的身边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000F, 0x13, 0x16, 700)
    Sleep(200)

    ChrTalk(
        0x000F,
        (
            '#0020060669V#361F真不可思议……\n',
            '我又看见那情景了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060670V小时候……溜出城堡……\n',
            '在那小胡同里玩耍……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060671V奥斯卡……尤利乌斯……\n',
            '大家都那样开心地笑着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060672V我……\n',
            '好喜欢……你们的笑容……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060673V#365F所…以……请你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060674V……永远开心地笑……着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060675V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000F, 0x16, 0x18, 700)
    Sleep(160)

    Fade(500)
    OP_99(0x000F, 0x19, 0x19, 700)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0010060676V#422F#2P公主……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060677V这不是真的吧，公主！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0010060678V#423F#2P#3S求求你告诉我这不是真的！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_99(0x000F, 0x19, 0x1B, 900)

    ChrTalk(
        0x0011,
        (
            '#0060060679V#359F#5P塞茜莉亚……我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060680V#357F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#1570060681V#5P公主殿下，太不幸了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060682V#2P啊，为什么会发生这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060683V#5P殿下为了阻止我们的纷争，\n',
            '连自己宝贵的生命也在所不惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060684V#5P和这份崇高的节操相比……\n',
            '贵族的荣誉又是何等的渺小……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060685V#5P若不是我们互相争斗，\n',
            '就不会发生这样的憾事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060686V#2P人总是要等大错铸成之后，\n',
            '才会发觉自己的愚蠢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060687V#2P灵魂为何要被束缚于身体上？\n',
            '这也是人类之子的宿命吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060688V#2P爱德丝啊，伟大的空之女神。\n',
            '您为何如此不公……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            '#1650060689V',
            (TxtCtl.SetColor, 0x5),
            '看来……\n',
            '你们还是不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    ChrSetPos(0x001A, 59990, 7000, 13110, 0)
    PlaySE(215, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp005_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 59990, 8500, 13110, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_77(0x1E, 0x1E, 0xA0, 0x00, 0x00000FA0)
    Sleep(4000)

    OP_99(0x000F, 0x1B, 0x19, 1200)
    TalkSetChrName('女性的声音')

    Talk(
        (
            '#1650060690V',
            (TxtCtl.SetColor, 0x5),
            '……我的确赐予了你们\n',
            '作为寄宿灵魂而存在的肉体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060691V',
            (TxtCtl.SetColor, 0x5),
            '但是，人类的灵魂，\n',
            '本应是更加崇高而自由的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060692V',
            (TxtCtl.SetColor, 0x5),
            '轻贱灵魂的不是他人，\n',
            '正是你们自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0017,
        (
            '#1620060693V#5P好、好耀眼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1630060694V#2P好美妙的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1640060695V#5P哦哦……天啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1640060696V#5P诸位，真是不胜惶恐，\n',
            '女神降临了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060697V#422F这就是女神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060698V#359F#5P何等的庄严啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('女神爱德丝')

    Talk(
        (
            '#1650060699V',
            (TxtCtl.SetColor, 0x5),
            '年轻的骑士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060700V',
            (TxtCtl.SetColor, 0x5),
            '你们的决斗，\n',
            '我已经全部目睹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060701V',
            (TxtCtl.SetColor, 0x5),
            '虽然勇猛可嘉……\n',
            '但却缺少了至关重要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0010,
        (
            '#0010060702V#424F的确如您所说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060703V#352F#5P一切都是\n',
            '我们的不成熟所造成的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('女神爱德丝')

    Talk(
        (
            '#1650060704V',
            (TxtCtl.SetColor, 0x5),
            '议长啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060705V',
            (TxtCtl.SetColor, 0x5),
            '你太过拘泥于身分的区别。\n',
            '但是，你是否忘记了，\n',
            '贵族与王族其实都同样是人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0015,
        (
            '#1600060706V#2P……真是惭愧万分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('女神爱德丝')

    Talk(
        (
            '#1650060707V',
            (TxtCtl.SetColor, 0x5),
            '公爵啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060708V',
            (TxtCtl.SetColor, 0x5),
            '自身的罪孽，\n',
            '你应该最为清楚吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0014,
        (
            '#1590060709V#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('女神爱德丝')

    Talk(
        (
            '#1650060710V',
            (TxtCtl.SetColor, 0x5),
            '还有，\n',
            '旁观了此事的人们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060711V',
            (TxtCtl.SetColor, 0x5),
            '你们也同样\n',
            '欠缺了一些重要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060712V',
            (TxtCtl.SetColor, 0x5),
            '请你们将手放在胸前仔细思索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(400)

    OP_62(0x0017, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0018, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0019, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1600)

    OP_63(0x0017)
    OP_63(0x0018)
    OP_63(0x0019)
    Sleep(400)

    TalkSetChrName('女神爱德丝')

    Talk(
        (
            '#1650060713V',
            (TxtCtl.SetColor, 0x5),
            '呵呵，\n',
            '看来大家也都各有所悟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060714V',
            (TxtCtl.SetColor, 0x5),
            '那么，\n',
            '利贝尔就还应该存有未来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1650060715V',
            (TxtCtl.SetColor, 0x5),
            '请将今日之事\n',
            '永远铭记于心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000007D0)
    StopEffect(0x00, 0x02)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000BB8)
    Sleep(3000)

    OP_21()

    ChrTalk(
        0x0013,
        (
            '#1570060716V#5P啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060717V#2P消失了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#0020060718V#5P…………嗯………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_99(0x000F, 0x19, 0x16, 700)
    Sleep(300)

    OP_99(0x000F, 0x16, 0x14, 850)
    OP_99(0x000F, 0x14, 0x16, 850)
    Sleep(100)

    OP_99(0x000F, 0x16, 0x14, 1100)
    OP_99(0x000F, 0x14, 0x16, 1100)

    ChrTalk(
        0x000F,
        (
            '#0020060719V#364F啊……这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060720V#422F公、公主！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060721V#354F#5P塞茜莉亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060722V#364F啊……\n',
            '尤利乌斯，奥斯卡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060723V难道……\n',
            '连你们也到天国来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#422F#2P#1K………………',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0011,
        (
            '#0060060725V#354F#1P#1K………………',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0018,
        (
            '#1640060726V#5P这、这……\n',
            '这简直就是奇迹啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    LoadEffect(0x00, 'map\\\\mp016_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 59990, 2000, 13110, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    ChrClearFlags(0x0011, 0x0020)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 59370, 1000, 13750, 126)
    ChrSetChipByIndex(0x000F, 40)
    ChrClearFlags(0x000F, 0x0002)
    ChrSetSubChip(0x000F, 0)
    ChrSetDirection(0x000F, 180, 0)
    PlayBGM(100)
    OP_0D()
    OP_77(0x78, 0x78, 0x78, 0x00, 0x000007D0)
    Sleep(2000)

    ChrTalk(
        0x0013,
        (
            '#1570060727V#10A#5P公主殿下～！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_86E4')
    def lambda_86E4():
        ChrWalkTo(0x00FE, 58600, 1000, 14240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_86E4)

    @scena.Lambda('lambda_86FF')
    def lambda_86FF():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_86FF')

    DispatchAsync2(0x0011, 0x0001, lambda_86FF)

    @scena.Lambda('lambda_8710')
    def lambda_8710():
        ChrWalkTo(0x00FE, 61400, 1000, 14240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_8710)

    @scena.Lambda('lambda_872B')
    def lambda_872B():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_872B')

    DispatchAsync2(0x0010, 0x0001, lambda_872B)

    @scena.Lambda('lambda_873C')
    def lambda_873C():
        ChrSetDirection(0x00FE, 0, 300)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_873C)

    @scena.Lambda('lambda_874A')
    def lambda_874A():
        ChrWalkTo(0x00FE, 60400, 1000, 13860, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_874A)

    @scena.Lambda('lambda_8765')
    def lambda_8765():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_8765')

    DispatchAsync2(0x0012, 0x0001, lambda_8765)

    @scena.Lambda('lambda_8776')
    def lambda_8776():
        ChrWalkTo(0x00FE, 59600, 1000, 13860, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_8776)

    @scena.Lambda('lambda_8791')
    def lambda_8791():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_8791')

    DispatchAsync2(0x0013, 0x0001, lambda_8791)

    @scena.Lambda('lambda_87A2')
    def lambda_87A2():
        ChrWalkTo(0x00FE, 57700, 1000, 12860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_87A2)

    @scena.Lambda('lambda_87BD')
    def lambda_87BD():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_87BD')

    DispatchAsync2(0x0014, 0x0001, lambda_87BD)

    @scena.Lambda('lambda_87CE')
    def lambda_87CE():
        ChrWalkTo(0x00FE, 62300, 1000, 12860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_87CE)

    @scena.Lambda('lambda_87E9')
    def lambda_87E9():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_87E9')

    DispatchAsync2(0x0015, 0x0001, lambda_87E9)

    @scena.Lambda('lambda_87FA')
    def lambda_87FA():
        ChrWalkTo(0x00FE, 58600, 1000, 16870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_87FA)

    @scena.Lambda('lambda_8815')
    def lambda_8815():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_8815')

    DispatchAsync2(0x0017, 0x0001, lambda_8815)

    @scena.Lambda('lambda_8826')
    def lambda_8826():
        ChrWalkTo(0x00FE, 61400, 1000, 16870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_8826)

    @scena.Lambda('lambda_8841')
    def lambda_8841():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_8841')

    DispatchAsync2(0x0019, 0x0001, lambda_8841)

    @scena.Lambda('lambda_8852')
    def lambda_8852():
        ChrWalkTo(0x00FE, 60000, 1000, 16400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_8852)

    @scena.Lambda('lambda_886D')
    def lambda_886D():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_886D')

    DispatchAsync2(0x0018, 0x0001, lambda_886D)

    WaitForThreadExit(0x0012, 0x0002)

    ChrTalk(
        0x0012,
        (
            '#1580060728V#2P真是、真是太好了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060729V#364F哎……？\n',
            '你们两个怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060730V啊……\n',
            '公爵……连议长都……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060731V我……不是应该死了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060732V#5P啊，女神啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1590060733V#5P感谢您！\n',
            '将利贝尔的至宝还给了我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1600060734V#2P感谢您的大慈大悲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_89AD')
    def lambda_89AD():
        ChrMoveTo(0x00FE, 60700, 1000, 15300, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_89AD)

    @scena.Lambda('lambda_89C8')
    def lambda_89C8():
        ChrMoveTo(0x00FE, 59300, 1000, 15300, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_89C8)

    WaitForThreadExit(0x0012, 0x0002)

    @scena.Lambda('lambda_89E8')
    def lambda_89E8():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_89E8)

    @scena.Lambda('lambda_89F6')
    def lambda_89F6():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_89F6)

    ChrTurnDirection(0x000F, 0x0010, 300)
    Sleep(500)

    ChrTurnDirection(0x000F, 0x0011, 300)

    ChrTalk(
        0x000F,
        (
            '#0020060735V#362F奥斯卡、尤利乌斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060736V这……\n',
            '究竟是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0010, 0xFF)

    ChrTalk(
        0x0011,
        (
            '#0060060737V#357F#5P塞茜莉亚殿下……\n',
            '您再也无须担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060738V#358F长久以来的对立已经结束……\n',
            '一切都开始向着好的方向发展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060739V#420F#2P你太天真了，奥斯卡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060740V你我之间的胜负\n',
            '还未见分晓对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060741V#353F#5P尤利乌斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 300)

    ChrTalk(
        0x000F,
        (
            '#0020060742V#363F难道……\n',
            '你们还要继续战斗吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060743V#424F#2P不……\n',
            '这次的决斗就到此为止了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060744V因为那个笨蛋\n',
            '使剑的手腕受了伤。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060745V#420F但是，声势浩大的一场决斗却没有胜者，\n',
            '这未免太说不过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060746V那么，就将胜利给予在不利条件下\n',
            '仍能毫不逊色地战斗的人吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0060060747V#352F#5P等等，尤利乌斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0011, 300)
    ChrTurnDirection(0x0010, 0x0011, 400)

    ChrTalk(
        0x0010,
        (
            '#0010060748V#420F#2P别误会，奥斯卡。\n',
            '这并不代表我放弃了公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060749V等你伤愈之后，\n',
            '我们再来以木剑一决胜负吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060750V就像小时候那样，打个痛快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0010, 400)

    ChrTalk(
        0x0011,
        (
            '#0060060751V#358F#5P这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060752V呵呵……\n',
            '好的，我接受了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 300)

    ChrTalk(
        0x000F,
        (
            '#0020060753V#367F真是的，你们两个……\n',
            '完全忽视了我的存在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 400)
    ChrTurnDirection(0x0011, 0x000F, 400)

    ChrTalk(
        0x0011,
        (
            '#0060060754V#354F#5P不、不是这个意思……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0010060755V#420F#2P但是公主……\n',
            '今天请先给予胜者胜利之吻吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060756V因为大家都期待着这一幕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0020060757V#360F……好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8EE7')
    def lambda_8EE7():
        ChrWalkTo(0x00FE, 59680, 1000, 13600, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_8EE7)

    ChrMoveTo(0x000F, 60200, 1000, 12850, 1500, 0x00)
    ChrTurnDirection(0x000F, 0x0011, 300)
    Sleep(1000)

    ChrSetFlags(0x0011, 0x0080)
    ChrSetPos(0x000F, 60000, 1000, 13160, 0)
    ChrSetFlags(0x000F, 0x0020)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 36)
    ChrSetSubChip(0x000F, 0)
    Sleep(200)

    OP_99(0x000F, 0x00, 0x03, 900)
    Sleep(500)

    OP_99(0x000F, 0x03, 0x00, 900)
    Sleep(200)

    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0014, 0xFF)
    TerminateThread(0x0015, 0xFF)

    ChrTalk(
        0x0013,
        (
            '#1570060758V#5P哎呀哎呀㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1580060759V#2P两人好般配呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0010060760V#420F#2P#3S请空之女神见证！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0010060761V#420F#2P#3S愿今日的美好，\n',
            '永世长存！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x000F, 0x0020)
    ChrClearFlags(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 40)
    ChrSetSubChip(0x000F, 0)
    ChrMoveTo(0x0011, 59000, 1000, 13710, 1000, 0x00)
    ChrSetDirection(0x0011, 180, 400)
    ChrSetDirection(0x000F, 180, 400)
    Sleep(500)

    ChrSetDirection(0x0014, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0014,
        (
            '#1590060762V#5P#3S愿利贝尔永远和平！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x0015, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0015,
        (
            '#1600060763V#5P#3S愿利贝尔永远繁荣！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0800)
    PlaySE(191, 0x00, 0x64)
    PlaySE(175, 0x00, 0x64)
    OP_70(0x0005, 120)
    OP_73(0x0005)
    Sleep(2000)

    Fade(1000)
    OP_1F(0x5A, 0x000000C8)
    CameraMove(130, 0, -1840, 0)
    Call(0, 0x0017)
    ChrClearFlags(0x0023, 0x0080)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0023,
        '银发青年',
        (
            '#0140060764V#122F#2P呵呵……\n',
            '最后果然还是大团圆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140060765V#125F不过……这样也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0023, 180, 400)
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)

    @scena.Lambda('lambda_91E7')
    def lambda_91E7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_91E7)

    ChrWalkTo(0x0023, 0, 0, -7840, 1500, 0x00)
    ChrSetFlags(0x0023, 0x0080)
    OP_0D()
    OP_21()
    Sleep(500)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，舞台剧『白花恋诗』\n',
            '在观众的一片赞叹声中完满地落幕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '同时，校园里\n',
            '响起了宣告学园祭结束的广播。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '来参观的客人们\n',
            '都带着满足的表情离开了学院……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T2513._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x92C7
@scena.Code('func_12_92C7')
def func_12_92C7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9313',
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x11, 0x1),
            (Expr.GetChrWork, 0x10, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x11, 0x2),
            (Expr.GetChrWork, 0x10, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x11, 0x3),
            (Expr.GetChrWork, 0x10, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_12_92C7')

    def _loc_9313(): pass

    label('loc_9313')

    Return()

# id: 0x0013 offset: 0x9314
@scena.Code('func_13_9314')
def func_13_9314():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9360',
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x14, 0x1),
            (Expr.GetChrWork, 0x10, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x14, 0x2),
            (Expr.GetChrWork, 0x10, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x14, 0x3),
            (Expr.GetChrWork, 0x10, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_13_9314')

    def _loc_9360(): pass

    label('loc_9360')

    Return()

# id: 0x0014 offset: 0x9361
@scena.Code('func_14_9361')
def func_14_9361():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_93AD',
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x15, 0x1),
            (Expr.GetChrWork, 0x11, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x15, 0x2),
            (Expr.GetChrWork, 0x11, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x15, 0x3),
            (Expr.GetChrWork, 0x11, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_14_9361')

    def _loc_93AD(): pass

    label('loc_93AD')

    Return()

# id: 0x0015 offset: 0x93AE
@scena.Code('func_15_93AE')
def func_15_93AE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_93FA',
    )

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.GetChrWork, 0x11, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x10, 0x2),
            (Expr.GetChrWork, 0x11, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.GetChrWork, 0x11, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_15_93AE')

    def _loc_93FA(): pass

    label('loc_93FA')

    Return()

# id: 0x0016 offset: 0x93FB
@scena.Code('func_16_93FB')
def func_16_93FB():
    CameraMove(60010, 4300, 7500, 0)
    OP_67(0, 840, -10000, 0)
    CameraSetDistance(910, 0)
    OP_6C(0, 0)
    OP_6E(581, 0)

    Return()

# id: 0x0017 offset: 0x9439
@scena.Code('func_17_9439')
def func_17_9439():
    OP_67(0, 6470, -10000, 0)
    CameraSetDistance(2830, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
