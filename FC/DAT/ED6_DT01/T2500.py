import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2500   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2500.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2500._SN', 'ED6_DT01/T2500_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
    ]

# id: 0x10001 offset: 0x1CA
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
            name                = '基库',
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 23200,
            z                   = 0,
            y                   = 46000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = 39500,
            z                   = -2000,
            y                   = 36400,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 28300,
            z                   = -2000,
            y                   = 36260,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '亚吉鲁',
            x                   = 27300,
            z                   = -2000,
            y                   = 38300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 39000,
            z                   = -2000,
            y                   = 38100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '莉秋尔',
            x                   = 40400,
            z                   = -2000,
            y                   = 50900,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '巴托姆',
            x                   = 46100,
            z                   = 0,
            y                   = 63100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '德尼斯',
            x                   = 29000,
            z                   = 0,
            y                   = 28100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '芙拉瑟',
            x                   = 28500,
            z                   = -2000,
            y                   = 54600,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '蕾娜',
            x                   = 27600,
            z                   = -2000,
            y                   = 54790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '勤务员巴克斯',
            x                   = 35800,
            z                   = 0,
            y                   = 78000,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 29600,
            z                   = -2000,
            y                   = 56200,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 28300,
            z                   = -2000,
            y                   = 37100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = 47280,
            z                   = 0,
            y                   = 48810,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '雷克斯',
            x                   = 29200,
            z                   = -2000,
            y                   = 51000,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '卡拉',
            x                   = 29500,
            z                   = -2000,
            y                   = 52500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '卢希娅',
            x                   = 29700,
            z                   = -2000,
            y                   = 51300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = 39400,
            z                   = -2000,
            y                   = 39700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '诺莉雅',
            x                   = 38900,
            z                   = -2000,
            y                   = 41300,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 39850,
            z                   = -2000,
            y                   = 45950,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 48940,
            z                   = 0,
            y                   = 27010,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 21080,
            z                   = 0,
            y                   = 31060,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 34850,
            z                   = 0,
            y                   = 74970,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 36840,
            z                   = 0,
            y                   = 68820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 43200,
            z                   = -750,
            y                   = 48790,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 30480,
            z                   = -2000,
            y                   = 34130,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 25790,
            z                   = -1750,
            y                   = 43460,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 39090,
            z                   = -2000,
            y                   = 50780,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 34620,
            z                   = 200,
            y                   = 22890,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 43410,
            z                   = 200,
            y                   = 20470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 42080,
            z                   = 200,
            y                   = 21850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 42150,
            z                   = 200,
            y                   = 16239,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002B,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 37080,
            z                   = 0,
            y                   = 18890,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002C,
        ),
        ScenaNpcData(
            name                = '参观客',
            x                   = 45250,
            z                   = 0,
            y                   = 45990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002D,
        ),
        ScenaNpcData(
            name                = '基尔巴特',
            x                   = 19030,
            z                   = 0,
            y                   = 46080,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002E,
        ),
        ScenaNpcData(
            name                = '王立学院·小道',
            x                   = 84080,
            z                   = 0,
            y                   = 28010,
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
            name                = '街景林道方向',
            x                   = -3490,
            z                   = 0,
            y                   = 46180,
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

# id: 0x10002 offset: 0x6CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x6CA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 12290,
            y           = -1000,
            z           = 47300,
            range       = 14900,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000AE38,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000034,
        ),
        ScenaEventData(
            x           = 41180,
            y           = 0,
            z           = 74060,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000038,
        ),
        ScenaEventData(
            x           = 53030,
            y           = 0,
            z           = 67260,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000038,
        ),
        ScenaEventData(
            x           = 53150,
            y           = 0,
            z           = 59630,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000039,
        ),
        ScenaEventData(
            x           = 48380,
            y           = 0,
            z           = 45960,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000039,
        ),
        ScenaEventData(
            x           = 52870,
            y           = 0,
            z           = 32110,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000039,
        ),
        ScenaEventData(
            x           = 53030,
            y           = 0,
            z           = 24850,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003A,
        ),
        ScenaEventData(
            x           = 47120,
            y           = 0,
            z           = 19010,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003A,
        ),
        ScenaEventData(
            x           = 22030,
            y           = 0,
            z           = 25660,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003B,
        ),
        ScenaEventData(
            x           = 22010,
            y           = 0,
            z           = 67170,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003C,
        ),
    )

# id: 0x10004 offset: 0x80A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 13480,
            triggerZ            = 1000,
            triggerY            = 45900,
            triggerRange        = 1000,
            actorX              = 13480,
            actorZ              = 1000,
            actorY              = 45900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0033,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22030,
            triggerZ            = 500,
            triggerY            = 24930,
            triggerRange        = 800,
            actorX              = 22030,
            actorZ              = 1500,
            actorY              = 24930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0036,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22030,
            triggerZ            = 500,
            triggerY            = 68110,
            triggerRange        = 800,
            actorX              = 22030,
            actorZ              = 1500,
            actorY              = 68110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0035,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22030,
            triggerZ            = 500,
            triggerY            = 24930,
            triggerRange        = 1500,
            actorX              = 22030,
            actorZ              = 3000,
            actorY              = 24930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41770,
            triggerZ            = 0,
            triggerY            = 69260,
            triggerRange        = 1500,
            actorX              = 41770,
            actorZ              = 3000,
            actorY              = 69260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 54350,
            triggerZ            = 0,
            triggerY            = 28820,
            triggerRange        = 1500,
            actorX              = 54350,
            actorZ              = 3000,
            actorY              = 28820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x8E2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_907',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 30130, 0, 26060, 180)

    Jump('loc_B89')

    def _loc_907(): pass

    label('loc_907')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_927',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 42490, 0, 17270, 135)

    Jump('loc_B89')

    def _loc_927(): pass

    label('loc_927')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_9FE',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 39800, -2000, 39200, 270)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 39530, -2000, 52980, 270)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrSetPos(0x002D, 23030, 250, 26410, 180)
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
    ChrSetPos(0x002B, 49710, 0, 30200, 90)
    CreateThread(0x002B, 0x00, 0x00, func_04_FA8)
    ChrSetFlags(0x002B, 0x0010)
    ChrClearFlags(0x002C, 0x0080)

    Jump('loc_B89')

    def _loc_9FE(): pass

    label('loc_9FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_A8C',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 39400, -2000, 54190, 270)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
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

    Jump('loc_B89')

    def _loc_A8C(): pass

    label('loc_A8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_AD1',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 39000, -2000, 37100, 90)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 47880, 0, 56070, 135)

    Jump('loc_B89')

    def _loc_AD1(): pass

    label('loc_AD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_AFB',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 39000, -2000, 37100, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_B89')

    def _loc_AFB(): pass

    label('loc_AFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_B1B',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 34000, -2000, 39780, 180)

    Jump('loc_B89')

    def _loc_B1B(): pass

    label('loc_B1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_B3B',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 39960, 0, 26140, 135)

    Jump('loc_B89')

    def _loc_B3B(): pass

    label('loc_B3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_B5B',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 34250, 0, 63640, 180)

    Jump('loc_B89')

    def _loc_B5B(): pass

    label('loc_B5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_B89',
    )

    ChrClearFlags(0x0011, 0x0080)
    CreateThread(0x0011, 0x00, 0x00, func_03_F84)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 44010, 0, 51050, 315)

    def _loc_B89(): pass

    label('loc_B89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_BA5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000800)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_30_35B7)

    def _loc_BA5(): pass

    label('loc_BA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_BB3',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_31_3E8D)

    def _loc_BB3(): pass

    label('loc_BB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_BCD',
    )

    SetScenaFlags(ScenaFlag(0x0086, 4, 0x434))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_32_42D4)

    def _loc_BCD(): pass

    label('loc_BCD')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_BD9'),
        (-1, 'loc_BF4'),
    )

    def _loc_BD9(): pass

    label('loc_BD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BF1',
    )

    SetScenaFlags(ScenaFlag(0x0085, 6, 0x42E))
    MapClearFlags(0x10000000)
    Event(0, func_2F_31AA)

    def _loc_BF1(): pass

    label('loc_BF1')

    Jump('loc_BF4')

    def _loc_BF4(): pass

    label('loc_BF4')

    ExecExpressionWithValue(
        0x000A,
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

# id: 0x0001 offset: 0xC06
@scena.Code('func_01_C06')
def func_01_C06():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_C27',
    )

    OP_B1('t2500_y')

    Jump('loc_C30')

    def _loc_C27(): pass

    label('loc_C27')

    OP_B1('t2500_n')

    def _loc_C30(): pass

    label('loc_C30')

    OP_16(0x02, 4000, -88000, -82000, 196684)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0001)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C96',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C76',
    )

    OP_65(0x03, 0x0001)

    def _loc_C76(): pass

    label('loc_C76')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C86',
    )

    OP_65(0x04, 0x0001)

    def _loc_C86(): pass

    label('loc_C86')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C96',
    )

    OP_65(0x05, 0x0001)

    def _loc_C96(): pass

    label('loc_C96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_D4A',
    )

    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_71(0x0012, 0x0004)
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
    OP_71(0x001F, 0x0004)
    OP_71(0x0020, 0x0004)
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)
    OP_71(0x0027, 0x0004)
    OP_71(0x0028, 0x0004)
    OP_71(0x0029, 0x0004)
    OP_71(0x002A, 0x0004)
    OP_71(0x002B, 0x0004)
    OP_71(0x002C, 0x0004)

    Jump('loc_E33')

    def _loc_D4A(): pass

    label('loc_D4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_D5D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_E33')

    def _loc_D5D(): pass

    label('loc_D5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_D7A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000800)
    OP_1B(0x0A, 0x00, 0x0002)

    Jump('loc_E33')

    def _loc_D7A(): pass

    label('loc_D7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D89',
    )

    Jump('loc_E33')

    def _loc_D89(): pass

    label('loc_D89')

    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_71(0x0012, 0x0004)
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
    OP_71(0x001F, 0x0004)
    OP_71(0x0020, 0x0004)
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)
    OP_71(0x0027, 0x0004)
    OP_71(0x0028, 0x0004)
    OP_71(0x0029, 0x0004)
    OP_71(0x002A, 0x0004)
    OP_71(0x002B, 0x0004)
    OP_71(0x002C, 0x0004)

    def _loc_E33(): pass

    label('loc_E33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_EA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E6F',
    )

    OP_10(0x19, 0x01)
    OP_10(0x1A, 0x01)
    OP_10(0x1B, 0x01)
    OP_10(0x1C, 0x01)
    OP_10(0x1D, 0x01)
    OP_10(0x03, 0x00)
    OP_10(0x04, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x06, 0x00)
    OP_10(0x07, 0x00)
    OP_10(0x13, 0x01)
    OP_10(0x14, 0x01)
    OP_10(0x08, 0x00)
    OP_10(0x09, 0x00)

    Jump('loc_EA1')

    def _loc_E6F(): pass

    label('loc_E6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EA1',
    )

    OP_10(0x0E, 0x01)
    OP_10(0x0F, 0x01)
    OP_10(0x10, 0x01)
    OP_10(0x11, 0x01)
    OP_10(0x12, 0x01)
    OP_10(0x13, 0x01)
    OP_10(0x14, 0x01)
    OP_10(0x03, 0x00)
    OP_10(0x04, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x06, 0x00)
    OP_10(0x07, 0x00)
    OP_10(0x08, 0x00)
    OP_10(0x09, 0x00)

    def _loc_EA1(): pass

    label('loc_EA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 3, 0x433)),
            Expr.Return,
        ),
        'loc_EBB',
    )

    OP_64(0x00, 0x0001)
    OP_72(0x0021, 0x0010)
    OP_6F(0x0021, 60)

    Jump('loc_F78')

    def _loc_EBB(): pass

    label('loc_EBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_EE7',
    )

    OP_64(0x00, 0x0001)
    OP_72(0x0021, 0x0010)
    OP_6F(0x0021, 60)
    OP_72(0x0004, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_65(0x01, 0x0001)
    OP_65(0x02, 0x0001)

    Jump('loc_F78')

    def _loc_EE7(): pass

    label('loc_EE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F3F',
    )

    OP_72(0x0021, 0x0010)
    OP_71(0x000A, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_71(0x001A, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0002)"),
            Expr.Return,
        ),
        'loc_F1C',
    )

    OP_72(0x001E, 0x0004)

    def _loc_F1C(): pass

    label('loc_F1C')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_F2C',
    )

    OP_72(0x0012, 0x0004)

    def _loc_F2C(): pass

    label('loc_F2C')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_F3C',
    )

    OP_72(0x001A, 0x0004)

    def _loc_F3C(): pass

    label('loc_F3C')

    Jump('loc_F78')

    def _loc_F3F(): pass

    label('loc_F3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_F73',
    )

    OP_64(0x00, 0x0001)
    OP_72(0x0021, 0x0010)
    OP_6F(0x0021, 60)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F70',
    )

    OP_72(0x0004, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_65(0x01, 0x0001)
    OP_65(0x02, 0x0001)

    def _loc_F70(): pass

    label('loc_F70')

    Jump('loc_F78')

    def _loc_F73(): pass

    label('loc_F73')

    OP_72(0x0021, 0x0010)

    def _loc_F78(): pass

    label('loc_F78')

    Return()

# id: 0x0002 offset: 0xF79
@scena.Code('func_02_F79')
def func_02_F79():
    MapClearFlags(0x00000800)
    OP_1B(0x0A, 0x00, 0xFFFF)

    Return()

# id: 0x0003 offset: 0xF84
@scena.Code('func_03_F84')
def func_03_F84():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FA7',
    )

    OP_8D(0x00FE, 49260, 65690, 45050, 60310, 3000)

    Jump('func_03_F84')

    def _loc_FA7(): pass

    label('loc_FA7')

    Return()

# id: 0x0004 offset: 0xFA8
@scena.Code('func_04_FA8')
def func_04_FA8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_FB2',
    )

    Jump('loc_FD9')

    def _loc_FB2(): pass

    label('loc_FB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_FC7',
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

    Jump('loc_FD9')

    def _loc_FC7(): pass

    label('loc_FC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_FD9',
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

    def _loc_FD9(): pass

    label('loc_FD9')

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
        'loc_FFE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_1140')

    def _loc_FFE(): pass

    label('loc_FFE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1017',
    )

    OP_99(0x00FE, 0x01, 0x07, 1300)

    Jump('loc_1140')

    def _loc_1017(): pass

    label('loc_1017')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1030',
    )

    OP_99(0x00FE, 0x02, 0x07, 1250)

    Jump('loc_1140')

    def _loc_1030(): pass

    label('loc_1030')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1049',
    )

    OP_99(0x00FE, 0x03, 0x07, 1200)

    Jump('loc_1140')

    def _loc_1049(): pass

    label('loc_1049')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1062',
    )

    OP_99(0x00FE, 0x04, 0x07, 1150)

    Jump('loc_1140')

    def _loc_1062(): pass

    label('loc_1062')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_107B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1100)

    Jump('loc_1140')

    def _loc_107B(): pass

    label('loc_107B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1094',
    )

    OP_99(0x00FE, 0x06, 0x07, 1050)

    Jump('loc_1140')

    def _loc_1094(): pass

    label('loc_1094')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10AD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1355)

    Jump('loc_1140')

    def _loc_10AD(): pass

    label('loc_10AD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10C6',
    )

    OP_99(0x00FE, 0x01, 0x07, 1305)

    Jump('loc_1140')

    def _loc_10C6(): pass

    label('loc_10C6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10DF',
    )

    OP_99(0x00FE, 0x02, 0x07, 1255)

    Jump('loc_1140')

    def _loc_10DF(): pass

    label('loc_10DF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F8',
    )

    OP_99(0x00FE, 0x03, 0x07, 1205)

    Jump('loc_1140')

    def _loc_10F8(): pass

    label('loc_10F8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1111',
    )

    OP_99(0x00FE, 0x04, 0x07, 1155)

    Jump('loc_1140')

    def _loc_1111(): pass

    label('loc_1111')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_112A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1105)

    Jump('loc_1140')

    def _loc_112A(): pass

    label('loc_112A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1140',
    )

    OP_99(0x00FE, 0x06, 0x07, 1055)

    def _loc_1140(): pass

    label('loc_1140')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1155',
    )

    OP_99(0x00FE, 0x00, 0x07, 1200)

    Jump('loc_1140')

    def _loc_1155(): pass

    label('loc_1155')

    Return()

# id: 0x0005 offset: 0x1156
@scena.Code('func_05_1156')
def func_05_1156():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1179',
    )

    OP_8D(0x00FE, 41490, 48770, 38300, 42820, 3500)

    Jump('func_05_1156')

    def _loc_1179(): pass

    label('loc_1179')

    Return()

# id: 0x0006 offset: 0x117A
@scena.Code('func_06_117A')
def func_06_117A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11D6',
    )

    ChrWalkTo(0x00FE, 45270, 0, 28860, 3000, 0x00)
    ChrWalkTo(0x00FE, 46130, 0, 64060, 3000, 0x00)
    ChrWalkTo(0x00FE, 21970, 0, 64060, 3000, 0x00)
    ChrWalkTo(0x00FE, 22730, 0, 28850, 3000, 0x00)

    Jump('func_06_117A')

    def _loc_11D6(): pass

    label('loc_11D6')

    Return()

# id: 0x0007 offset: 0x11D7
@scena.Code('func_07_11D7')
def func_07_11D7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1233',
    )

    ChrWalkTo(0x00FE, 20830, 0, 64950, 2000, 0x00)
    ChrWalkTo(0x00FE, 46940, 0, 65190, 2000, 0x00)
    ChrWalkTo(0x00FE, 20830, 0, 64950, 2000, 0x00)
    ChrWalkTo(0x00FE, 20650, 0, 28320, 2000, 0x00)

    Jump('func_07_11D7')

    def _loc_1233(): pass

    label('loc_1233')

    Return()

# id: 0x0008 offset: 0x1234
@scena.Code('func_08_1234')
def func_08_1234():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1257',
    )

    OP_8D(0x00FE, 36860, 76920, 34270, 72430, 3500)

    Jump('func_08_1234')

    def _loc_1257(): pass

    label('loc_1257')

    Return()

# id: 0x0009 offset: 0x1258
@scena.Code('func_09_1258')
def func_09_1258():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_127B',
    )

    OP_8D(0x00FE, 37000, 71270, 33980, 67090, 3500)

    Jump('func_09_1258')

    def _loc_127B(): pass

    label('loc_127B')

    Return()

# id: 0x000A offset: 0x127C
@scena.Code('func_0A_127C')
def func_0A_127C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_129F',
    )

    OP_8D(0x00FE, 39610, 24560, 36410, 15240, 3500)

    Jump('func_0A_127C')

    def _loc_129F(): pass

    label('loc_129F')

    Return()

# id: 0x000B offset: 0x12A0
@scena.Code('func_0B_12A0')
def func_0B_12A0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12FC',
    )

    ChrWalkTo(0x00FE, 44270, 0, 29720, 2500, 0x00)
    ChrWalkTo(0x00FE, 23570, 0, 29740, 2500, 0x00)
    ChrWalkTo(0x00FE, 23690, 0, 62340, 2500, 0x00)
    ChrWalkTo(0x00FE, 44280, 0, 62140, 2500, 0x00)

    Jump('func_0B_12A0')

    def _loc_12FC(): pass

    label('loc_12FC')

    Return()

# id: 0x000C offset: 0x12FD
@scena.Code('func_0C_12FD')
def func_0C_12FD():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_138F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '刚刚才结束\n',
            '今天体育课的教学。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '学生不仅要学习，\n',
            '身心也应该得到健全的发展才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少在我的课上\n',
            '我要好好地锻炼他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13ED')

    def _loc_138F(): pass

    label('loc_138F')

    ChrTalk(
        0x00FE,
        (
            '学生不仅要学习，\n',
            '身心也应该得到健全的发展才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少在我的课上\n',
            '我要好好地锻炼他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13ED(): pass

    label('loc_13ED')

    TalkEnd(0x000B)

    Return()

# id: 0x000D offset: 0x13F1
@scena.Code('func_0D_13F1')
def func_0D_13F1():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_14F3',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1456',
    )

    OP_0D()
    OP_A9(0x2E)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_1456(): pass

    label('loc_1456')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1467',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_1467(): pass

    label('loc_1467')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14D3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '欢迎！欢迎！\n',
            '欢～迎呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来吧，那边的姐姐们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来点很美味很美味的\n',
            '爆米花怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_14D3(): pass

    label('loc_14D3')

    ChrTalk(
        0x00FE,
        (
            '欢迎！欢迎！\n',
            '欢～迎呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F0(): pass

    label('loc_14F0')

    Jump('loc_15D1')

    def _loc_14F3(): pass

    label('loc_14F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_152B',
    )

    ChrTalk(
        0x00FE,
        (
            '好，准备稳妥了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来就等明天了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D1')

    def _loc_152B(): pass

    label('loc_152B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_15D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15A6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '今年又到了这个时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起上课，\n',
            '还是学园祭更能提起干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，精神百倍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D1')

    def _loc_15A6(): pass

    label('loc_15A6')

    ChrTalk(
        0x00FE,
        (
            '比起上课，\n',
            '还是学园祭更能提起干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15D1(): pass

    label('loc_15D1')

    TalkEnd(0x000C)

    Return()

# id: 0x000E offset: 0x15D5
@scena.Code('func_0E_15D5')
def func_0E_15D5():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_16E9',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_163A',
    )

    OP_0D()
    OP_A9(0x2F)
    OP_56(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_163A(): pass

    label('loc_163A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_164B',
    )

    TalkEnd(0x000D)

    Return()

    def _loc_164B(): pass

    label('loc_164B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16BB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唔，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '要不要买些点心呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这个是\n',
            '很好吃的点心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E6')

    def _loc_16BB(): pass

    label('loc_16BB')

    ChrTalk(
        0x00FE,
        (
            '呼，还是不习惯，\n',
            '怎么说都有点害羞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16E6(): pass

    label('loc_16E6')

    Jump('loc_1735')

    def _loc_16E9(): pass

    label('loc_16E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1735',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，总算准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天就和社团的各位\n',
            '轮流来担当店员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1735(): pass

    label('loc_1735')

    TalkEnd(0x000D)

    Return()

# id: 0x000F offset: 0x1739
@scena.Code('func_0F_1739')
def func_0F_1739():
    TalkBegin(0x000E)
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1797',
    )

    OP_0D()
    OP_A9(0x2F)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_1797(): pass

    label('loc_1797')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17A8',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_17A8(): pass

    label('loc_17A8')

    ChrTalk(
        0x000E,
        (
            '想吃美味的点心吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '各种各样的味道都有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0010 offset: 0x17E0
@scena.Code('func_10_17E0')
def func_10_17E0():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_18DF',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1845',
    )

    OP_0D()
    OP_A9(0x2E)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_1845(): pass

    label('loc_1845')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1856',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_1856(): pass

    label('loc_1856')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_189B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '欢迎～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来一份精挑细选的\n',
            '美味爆米花怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DC')

    def _loc_189B(): pass

    label('loc_189B')

    ChrTalk(
        0x00FE,
        (
            '作为材料的玉米\n',
            '是从洛连特运过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边的蔬菜很美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18DC(): pass

    label('loc_18DC')

    Jump('loc_19C0')

    def _loc_18DF(): pass

    label('loc_18DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1932',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，器具和材料都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '制作方面我也练习过了，\n',
            '你们放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_1932(): pass

    label('loc_1932')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_19C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1997',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '好，就选这里吧。\n',
            '摆摊的地点是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们弓道部\n',
            '决定摆摊卖爆米花。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_1997(): pass

    label('loc_1997')

    ChrTalk(
        0x00FE,
        (
            '罗迪只有在这个时候\n',
            '才会干劲十足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19C0(): pass

    label('loc_19C0')

    TalkEnd(0x000F)

    Return()

# id: 0x0011 offset: 0x19C4
@scena.Code('func_11_19C4')
def func_11_19C4():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1A82',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A29',
    )

    OP_0D()
    OP_A9(0x2C)
    OP_56(0x00)
    TalkEnd(0x0010)

    Return()

    def _loc_1A29(): pass

    label('loc_1A29')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A3A',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_1A3A(): pass

    label('loc_1A3A')

    ChrTalk(
        0x00FE,
        (
            '啊，是前辈你们呀。\n',
            '来一个冰淇淋怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，很好吃的哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E36')

    def _loc_1A82(): pass

    label('loc_1A82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1B99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B5D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，前辈。\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过明天我不能去看\n',
            '前辈扮成苍骑士的样子………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '一想到这个就觉得可惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是、是吗……\n',
            '真是谢谢你的支持了，莉秋尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B96')

    def _loc_1B5D(): pass

    label('loc_1B5D')

    ChrTalk(
        0x00FE,
        (
            '科洛丝前辈和艾丝蒂尔，\n',
            '你们都好棒啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B96(): pass

    label('loc_1B96')

    Jump('loc_1E36')

    def _loc_1B99(): pass

    label('loc_1B99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1E36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E06',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '前辈！\n',
            '你回来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '我们已经开始准备社团的摊位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对不起，莉秋尔。\n',
            '我都帮不上忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系，\n',
            '前辈一直在忙舞台剧嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，舞台剧的演员人选\n',
            '定下来了没有呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F呵呵，那个就不用担心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '难不成就是你身边的这两位？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#008F啊，感觉好紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0010)

    ChrTalk(
        0x00FE,
        (
            '果然如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '的确是非常合适呀，\n',
            '真不愧是前辈选中的演员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能找到合适的演员，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，我也要演出舞台剧，\n',
            '大家一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，请多指教了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E36')

    def _loc_1E06(): pass

    label('loc_1E06')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '我也要演出舞台剧。\n',
            '大家一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E36(): pass

    label('loc_1E36')

    TalkEnd(0x0010)

    Return()

# id: 0x0012 offset: 0x1E3A
@scena.Code('func_12_1E3A')
def func_12_1E3A():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1F03',
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E9F',
    )

    OP_0D()
    OP_A9(0x2C)
    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_1E9F(): pass

    label('loc_1E9F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EB0',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_1EB0(): pass

    label('loc_1EB0')

    ChrTalk(
        0x00FE,
        (
            '怎么样～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是击剑部的\n',
            '冰淇淋店哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '会出乎你意料地美味哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FE7')

    def _loc_1F03(): pass

    label('loc_1F03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1FE7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FB4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你最近好像很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F巴托姆，不好意思。\n',
            '最近我连社团活动都没空来参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '因为你那边也有很多事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要太介意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FE7')

    def _loc_1FB4(): pass

    label('loc_1FB4')

    ChrTalk(
        0x00FE,
        (
            '科洛丝，有时间的话，\n',
            '请来出席一下社团练习吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FE7(): pass

    label('loc_1FE7')

    TalkEnd(0x0011)

    Return()

# id: 0x0013 offset: 0x1FEB
@scena.Code('func_13_1FEB')
def func_13_1FEB():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2053',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然今天没有课，\n',
            '不过我是来教室自习的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁大家休息的时候学习\n',
            '才是缩短差距的好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2053(): pass

    label('loc_2053')

    TalkEnd(0x0012)

    Return()

# id: 0x0014 offset: 0x2057
@scena.Code('func_14_2057')
def func_14_2057():
    TalkBegin(0x0013)
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20B5',
    )

    OP_0D()
    OP_A9(0x2D)
    OP_56(0x00)
    TalkEnd(0x0013)

    Return()

    def _loc_20B5(): pass

    label('loc_20B5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20C6',
    )

    TalkEnd(0x0013)

    Return()

    def _loc_20C6(): pass

    label('loc_20C6')

    ChrTalk(
        0x00FE,
        (
            '因为我是美术部的，\n',
            '我想肖像画也能做出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，因为我很擅长烹饪，\n',
            '所以大家都没意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0015 offset: 0x2128
@scena.Code('func_15_2128')
def func_15_2128():
    TalkBegin(0x0014)
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2186',
    )

    OP_0D()
    OP_A9(0x2D)
    OP_56(0x00)
    TalkEnd(0x0014)

    Return()

    def _loc_2186(): pass

    label('loc_2186')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2197',
    )

    TalkEnd(0x0014)

    Return()

    def _loc_2197(): pass

    label('loc_2197')

    ChrTalk(
        0x00FE,
        (
            '我很擅长科学和生物实验，\n',
            '可对烹饪却没什么经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，\n',
            '不管学什么要领都是努力再努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x0016 offset: 0x21FF
@scena.Code('func_16_21FF')
def func_16_21FF():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_222D',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多应该\n',
            '修剪一下树丛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_222D(): pass

    label('loc_222D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_227B',
    )

    ChrTalk(
        0x00FE,
        (
            '辛苦你们了。\n',
            '总算完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还剩下一点，\n',
            '我待会儿再收拾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_227B(): pass

    label('loc_227B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2393',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_22FA',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，刚才真是感谢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下面只剩这里了，\n',
            '我一个人就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天的学园祭，\n',
            '大家都非常期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2390')

    def _loc_22FA(): pass

    label('loc_22FA')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0001)"),
            Expr.Return,
        ),
        'loc_238C',
    )

    ChrTalk(
        0x00FE,
        (
            '如果看到没有装饰的地方，\n',
            '还请告诉我一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要稍微注意一下\n',
            '应该就可以发现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 135, 400)

    ChrTalk(
        0x00FE,
        (
            '接下来……\n',
            '首先从这里开始干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2390')

    def _loc_238C(): pass

    label('loc_238C')

    Call(1, 0x0000)

    def _loc_2390(): pass

    label('loc_2390')

    Jump('loc_24B4')

    def _loc_2393(): pass

    label('loc_2393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_23F1',
    )

    ChrTalk(
        0x00FE,
        (
            '每年一到这个时期，\n',
            '同学们总是准备到很晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也不得不\n',
            '巡逻到夜深才能回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_23F1(): pass

    label('loc_23F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2421',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，要出去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要小心点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_2421(): pass

    label('loc_2421')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_2460',
    )

    ChrTalk(
        0x00FE,
        (
            '今天也没有体育课，\n',
            '现在我正在整理学院的庭园呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_2460(): pass

    label('loc_2460')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_24B4',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你们是来参观的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对详细情况不是很清楚，\n',
            '去找接待员问问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24B4(): pass

    label('loc_24B4')

    TalkEnd(0x0015)

    Return()

# id: 0x0017 offset: 0x24B8
@scena.Code('func_17_24B8')
def func_17_24B8():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 5, 0x455)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_263B',
    )

    SetScenaFlags(ScenaFlag(0x008A, 5, 0x455))

    ChrTalk(
        0x00FE,
        (
            '#0270060048V#143F哟，这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060049V你们怎么会在这里的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060050V#004F啊，奈尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060051V连你也来这里玩啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060052V#010F肯定是因为王立学院\n',
            '邀请了各界的名人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060053V奈尔先生是来这里取材的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0270060054V#141F嗯，差不多啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060055V呵呵，\n',
            '刚才正好有点饿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270060056V所以就买了点吃的填肚子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_267D')

    def _loc_263B(): pass

    label('loc_263B')

    ChrTalk(
        0x00FE,
        (
            '#0270060057V#141F刚才正好有点饿了，\n',
            '所以就买了点吃的填肚子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_267D(): pass

    label('loc_267D')

    TalkEnd(0x0016)

    Return()

# id: 0x0018 offset: 0x2681
@scena.Code('func_18_2681')
def func_18_2681():
    TalkBegin(0x0017)

    ChrTalk(
        0x0017,
        (
            '#0610060181V#182F呵呵，让人怀念的点心啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610060182V这种东西到底是在哪儿做出来的呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

# id: 0x0019 offset: 0x26EA
@scena.Code('func_19_26EA')
def func_19_26EA():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27D9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '#0320060406V#832F哦？怎么了，\n',
            '这么慌张……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320060407V难道发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060408V#008F啊，不……\n',
            '不是什么大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320060409V#830F是吗，那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320060410V如果有什么事件发生，\n',
            '一定要立刻告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2817')

    def _loc_27D9(): pass

    label('loc_27D9')

    ChrTalk(
        0x00FE,
        (
            '#0320060411V#830F如果有什么事件发生，\n',
            '一定要立刻告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2817(): pass

    label('loc_2817')

    TalkEnd(0x0018)

    Return()

# id: 0x001A offset: 0x281B
@scena.Code('func_1A_281B')
def func_1A_281B():
    TalkBegin(0x0019)

    ChrTalk(
        0x00FE,
        (
            '一到学园祭，\n',
            '钱就像水一样地流走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x001B offset: 0x284B
@scena.Code('func_1B_284B')
def func_1B_284B():
    TalkBegin(0x001A)

    ChrTalk(
        0x00FE,
        (
            '哎，真是好吃呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001A)

    Return()

# id: 0x001C offset: 0x2868
@scena.Code('func_1C_2868')
def func_1C_2868():
    TalkBegin(0x001B)

    ChrTalk(
        0x00FE,
        (
            '爸爸，我想吃这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001B)

    Return()

# id: 0x001D offset: 0x2887
@scena.Code('func_1D_2887')
def func_1D_2887():
    TalkBegin(0x001C)

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是好有活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '年轻人果然\n',
            '精力都很充沛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001C)

    Return()

# id: 0x001E offset: 0x28C9
@scena.Code('func_1E_28C9')
def func_1E_28C9():
    TalkBegin(0x001D)

    ChrTalk(
        0x00FE,
        (
            '虽然学园祭也不错，\n',
            '但我更想看看平时的上课情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为母亲的我当然很想知道\n',
            '自己的孩子是怎么生活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001D)

    Return()

# id: 0x001F offset: 0x293C
@scena.Code('func_1F_293C')
def func_1F_293C():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2995',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '我用零用钱买了一个冰淇淋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店里的哥哥\n',
            '还给我多加了点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B8')

    def _loc_2995(): pass

    label('loc_2995')

    ChrTalk(
        0x00FE,
        (
            '嗯，好香呀……\n',
            '肚子饿扁扁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29B8(): pass

    label('loc_29B8')

    TalkEnd(0x001E)

    Return()

# id: 0x0020 offset: 0x29BC
@scena.Code('func_20_29BC')
def func_20_29BC():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2A19',
    )

    ChrTalk(
        0x00FE,
        (
            '最近这里的\n',
            '入学考试好像很难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真羡慕那些学生\n',
            '能在这种地方学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A40')

    def _loc_2A19(): pass

    label('loc_2A19')

    ChrTalk(
        0x00FE,
        (
            '嘿，这就是学院啊……\n',
            '真是好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A40(): pass

    label('loc_2A40')

    TalkEnd(0x001F)

    Return()

# id: 0x0021 offset: 0x2A44
@scena.Code('func_21_2A44')
def func_21_2A44():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2AA0',
    )

    ChrTalk(
        0x00FE,
        (
            '舞台剧可是一定不能错过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我还是学生的时候，\n',
            '就已经是传统惯例呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD1')

    def _loc_2AA0(): pass

    label('loc_2AA0')

    ChrTalk(
        0x00FE,
        (
            '我好久没来\n',
            '拜访母校了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是怀念呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD1(): pass

    label('loc_2AD1')

    TalkEnd(0x0020)

    Return()

# id: 0x0022 offset: 0x2AD5
@scena.Code('func_22_2AD5')
def func_22_2AD5():
    TalkBegin(0x0021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2B09',
    )

    ChrTalk(
        0x00FE,
        (
            '这里有舞台剧演出吧。\n',
            '快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B21')

    def _loc_2B09(): pass

    label('loc_2B09')

    ChrTalk(
        0x00FE,
        (
            '从哪儿开始玩好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B21(): pass

    label('loc_2B21')

    TalkEnd(0x0021)

    Return()

# id: 0x0023 offset: 0x2B25
@scena.Code('func_23_2B25')
def func_23_2B25():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2B57',
    )

    ChrTalk(
        0x00FE,
        (
            '今年真的能\n',
            '看到传说中的公主吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7C')

    def _loc_2B57(): pass

    label('loc_2B57')

    ChrTalk(
        0x00FE,
        (
            '我们可是每年\n',
            '都会来这里玩的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B7C(): pass

    label('loc_2B7C')

    TalkEnd(0x0022)

    Return()

# id: 0x0024 offset: 0x2B80
@scena.Code('func_24_2B80')
def func_24_2B80():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2BB6',
    )

    ChrTalk(
        0x00FE,
        (
            '展示很有趣，\n',
            '舞台剧也很值得期待呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BD9')

    def _loc_2BB6(): pass

    label('loc_2BB6')

    ChrTalk(
        0x00FE,
        (
            '哎，\n',
            '有好多各种各样的摊子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BD9(): pass

    label('loc_2BD9')

    TalkEnd(0x0023)

    Return()

# id: 0x0025 offset: 0x2BDD
@scena.Code('func_25_2BDD')
def func_25_2BDD():
    TalkBegin(0x0024)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2C11',
    )

    ChrTalk(
        0x00FE,
        (
            '刚刚才吃了一个，\n',
            '又想再吃一个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C30')

    def _loc_2C11(): pass

    label('loc_2C11')

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '这里好像是点心店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C30(): pass

    label('loc_2C30')

    TalkEnd(0x0024)

    Return()

# id: 0x0026 offset: 0x2C34
@scena.Code('func_26_2C34')
def func_26_2C34():
    TalkBegin(0x0025)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2C82',
    )

    ChrTalk(
        0x00FE,
        (
            '这里真是个恬静的场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里学习\n',
            '想必进步一定很快吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C9E')

    def _loc_2C82(): pass

    label('loc_2C82')

    ChrTalk(
        0x00FE,
        (
            '孙女的教室在哪里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C9E(): pass

    label('loc_2C9E')

    TalkEnd(0x0025)

    Return()

# id: 0x0027 offset: 0x2CA2
@scena.Code('func_27_2CA2')
def func_27_2CA2():
    TalkBegin(0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2CF5',
    )

    ChrTalk(
        0x00FE,
        (
            '这个店是由\n',
            '击剑部来主办的呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '味道十分好，\n',
            '真是吓我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D0B')

    def _loc_2CF5(): pass

    label('loc_2CF5')

    ChrTalk(
        0x00FE,
        (
            '哎呀，真便宜呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D0B(): pass

    label('loc_2D0B')

    TalkEnd(0x0026)

    Return()

# id: 0x0028 offset: 0x2D0F
@scena.Code('func_28_2D0F')
def func_28_2D0F():
    TalkBegin(0x0027)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '稀里糊涂地又转回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D5E')

    def _loc_2D3D(): pass

    label('loc_2D3D')

    ChrTalk(
        0x00FE,
        (
            '呼，先喘口气，\n',
            '再接着逛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D5E(): pass

    label('loc_2D5E')

    TalkEnd(0x0027)

    Return()

# id: 0x0029 offset: 0x2D62
@scena.Code('func_29_2D62')
def func_29_2D62():
    TalkBegin(0x0028)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2D89',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，累死了累死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC7')

    def _loc_2D89(): pass

    label('loc_2D89')

    ChrTalk(
        0x00FE,
        (
            '我是被女儿硬拉来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '学园祭什么的我还是第一次参加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC7(): pass

    label('loc_2DC7')

    TalkEnd(0x0028)

    Return()

# id: 0x002A offset: 0x2DCB
@scena.Code('func_2A_2DCB')
def func_2A_2DCB():
    TalkBegin(0x0029)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2E28',
    )

    ChrTalk(
        0x00FE,
        (
            '我也想进\n',
            '这个学院学习呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在开始拼命学习的话，\n',
            '能通过入学考试吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E53')

    def _loc_2E28(): pass

    label('loc_2E28')

    ChrTalk(
        0x00FE,
        (
            '以前就听说过，\n',
            '这个学校环境真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E53(): pass

    label('loc_2E53')

    TalkEnd(0x0029)

    Return()

# id: 0x002B offset: 0x2E57
@scena.Code('func_2B_2E57')
def func_2B_2E57():
    TalkBegin(0x002A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2E7E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，稍微有点走累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EA1')

    def _loc_2E7E(): pass

    label('loc_2E7E')

    ChrTalk(
        0x00FE,
        (
            '连露天茶座也有，\n',
            '真不错啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EA1(): pass

    label('loc_2EA1')

    TalkEnd(0x002A)

    Return()

# id: 0x002C offset: 0x2EA5
@scena.Code('func_2C_2EA5')
def func_2C_2EA5():
    TalkBegin(0x002B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2EFC',
    )

    ChrTalk(
        0x00FE,
        (
            '……刚才有个\n',
            '黑发的哥哥跑过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边是不是\n',
            '有什么有趣的事呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F12')

    def _loc_2EFC(): pass

    label('loc_2EFC')

    ChrTalk(
        0x00FE,
        (
            '我是来找姐姐的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F12(): pass

    label('loc_2F12')

    TalkEnd(0x002B)

    Return()

# id: 0x002D offset: 0x2F16
@scena.Code('func_2D_2F16')
def func_2D_2F16():
    TalkBegin(0x002C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2F4C',
    )

    ChrTalk(
        0x00FE,
        (
            '下午开始有演出……\n',
            '那真让人期待呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F7D')

    def _loc_2F4C(): pass

    label('loc_2F4C')

    ChrTalk(
        0x00FE,
        (
            '好漂亮的建筑物啊，\n',
            '真不愧是杰尼丝王立学院。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F7D(): pass

    label('loc_2F7D')

    TalkEnd(0x002C)

    Return()

# id: 0x002E offset: 0x2F81
@scena.Code('func_2E_2F81')
def func_2E_2F81():
    TalkBegin(0x002D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_3002',
    )

    ChrTalk(
        0x00FE,
        (
            '#0480060071V#670F我也是在这个宿舍\n',
            '度过自己的学生时代的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480060072V#670F当时有不少出现幽灵之类的传闻哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A6')

    def _loc_3002(): pass

    label('loc_3002')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_313D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0105,
        (
            '#0060060063V#044F啊，是基尔巴特前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0480060064V#670F是科洛丝你们啊……\n',
            '准备已经好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060065V#006F嗯，好了。\n',
            '就等着开始演出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0480060066V#670F是吗，那我真是期待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480060067V#673F真是好久没回来了，\n',
            '还是母校好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480060068V在这里能回忆起\n',
            '学生时代的各种往事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A6')

    def _loc_313D(): pass

    label('loc_313D')

    ChrTalk(
        0x00FE,
        (
            '#0480060069V#673F真是好久没回来了，\n',
            '还是母校好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480060070V在这里能回忆起\n',
            '学生时代的各种往事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31A6(): pass

    label('loc_31A6')

    TalkEnd(0x002D)

    Return()

# id: 0x002F offset: 0x31AA
@scena.Code('func_2F_31AA')
def func_2F_31AA():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(61060, 0, 55000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(6110, 0)
    OP_6C(75000, 0)
    OP_6E(262, 0)
    OP_12(0x00009470, 0x0003D090, 0x00000000)
    ChrSetPos(0x0105, 17200, 0, 46000, 90)
    ChrSetPos(0x0102, 16100, 0, 45600, 90)
    ChrSetPos(0x0101, 16200, 0, 46800, 90)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_323D')
    def lambda_323D():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_323D)

    @scena.Lambda('lambda_324D')
    def lambda_324D():
        CameraMove(15540, 0, 46430, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_324D)

    Sleep(2000)

    OP_12(0x00009470, 0x00014C08, 0x00001F40)

    @scena.Lambda('lambda_3277')
    def lambda_3277():
        CameraSetDistance(2800, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_3277)

    @scena.Lambda('lambda_3287')
    def lambda_3287():
        OP_67(0, 9500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_3287)

    Sleep(8000)

    ChrTalk(
        0x0101,
        (
            '#0010051001V#501F啊～这里就是王立学院啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051002V该怎么说好呢……\n',
            '真是个充满祥和气息的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051003V#010F#1P而且这里也很安静，\n',
            '在这种环境下念书是再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 270, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051004V#045F呵呵，因为学生们现在还在上课。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051005V不过，再过一会儿\n',
            '整个校园就会热闹起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051006V毕竟学园祭也马上就要到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 0)
    Sleep(100)

    ChrTurnDirection(0x0102, 0x0105, 0)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020051007V#019F#1P是吗。\n',
            '大家都要忙着准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051008V#040F是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051009V本来想把你们介绍给学生会长的，\n',
            '不过她现在应该还在上课……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051010V就先带你们到校长室一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051011V#004F校长室？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051012V#040F嗯，就是王立学院的负责人\n',
            '科林兹校长的办公室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051013V在主楼第一层的最右边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051014V#000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051015V#010F#1P那我们就先去\n',
            '和你们的校长打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003D, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0030 offset: 0x35B7
@scena.Code('func_30_35B7')
def func_30_35B7():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(16440, 0, 46820, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 37340, 0, 73890, 225)
    ChrSetPos(0x0102, 38420, 0, 73100, 225)
    ChrSetPos(0x0105, 37160, 0, 72790, 225)
    ChrSetPos(0x0008, 35910, 0, 71960, 225)
    ChrSetPos(0x0009, 36980, 0, 71630, 225)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    OP_4A(0x001E, 0)
    OP_4A(0x001F, 0)
    OP_4A(0x0020, 0)
    OP_4A(0x0021, 0)
    OP_4A(0x0022, 0)
    OP_4A(0x0023, 0)
    OP_4A(0x0024, 0)
    OP_4A(0x0025, 0)
    OP_4A(0x0026, 0)
    OP_4A(0x0019, 0)
    OP_4A(0x001A, 0)
    OP_4A(0x001B, 0)
    OP_4A(0x001C, 0)
    OP_4A(0x002B, 0)
    OP_4A(0x002C, 0)
    ChrSetPos(0x001E, 11300, 0, 46800, 90)
    ChrSetPos(0x0021, 11300, 0, 45500, 90)
    ChrSetPos(0x0020, 10300, 0, 46800, 90)
    ChrSetPos(0x001F, 10300, 0, 45500, 90)
    ChrSetPos(0x0022, 9300, 0, 46800, 90)
    ChrSetPos(0x0023, 9300, 0, 45500, 90)
    ChrSetPos(0x0024, 8300, 0, 46800, 90)
    ChrSetPos(0x0025, 8300, 0, 45500, 90)
    ChrSetPos(0x0026, 7300, 0, 46800, 90)
    ChrSetPos(0x0019, 7300, 0, 45500, 90)
    ChrSetPos(0x001A, 6300, 0, 46800, 90)
    ChrSetPos(0x001B, 6300, 0, 45500, 90)
    ChrSetPos(0x001C, 5300, 0, 46800, 90)
    ChrSetPos(0x002B, 5300, 0, 45500, 90)
    ChrSetPos(0x002C, 4300, 0, 46800, 90)
    OP_4A(0x000C, 0)
    OP_4A(0x000D, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 14270, 0, 44100, 0)
    OP_72(0x0021, 0x0020)
    OP_6F(0x0021, 0)
    OP_70(0x0021, 60)
    OP_73(0x0021)
    OP_71(0x0021, 0x0020)

    @scena.Lambda('lambda_37D4')
    def lambda_37D4():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_37D4)

    @scena.Lambda('lambda_37EF')
    def lambda_37EF():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 4400, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_37EF)

    Sleep(150)

    @scena.Lambda('lambda_380F')
    def lambda_380F():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 2600, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_380F)

    Sleep(100)

    @scena.Lambda('lambda_382F')
    def lambda_382F():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_382F)

    @scena.Lambda('lambda_384A')
    def lambda_384A():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 2400, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_384A)

    @scena.Lambda('lambda_3865')
    def lambda_3865():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_3865)

    Sleep(50)

    Sleep(150)

    @scena.Lambda('lambda_388A')
    def lambda_388A():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 2400, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_388A)

    @scena.Lambda('lambda_38A5')
    def lambda_38A5():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 3400, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_38A5)

    @scena.Lambda('lambda_38C0')
    def lambda_38C0():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 2400, 0x00)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_38C0)

    Sleep(50)

    Sleep(100)

    @scena.Lambda('lambda_38E5')
    def lambda_38E5():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_38E5)

    @scena.Lambda('lambda_3900')
    def lambda_3900():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_3900)

    Sleep(150)

    @scena.Lambda('lambda_3920')
    def lambda_3920():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 4200, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_3920)

    @scena.Lambda('lambda_393B')
    def lambda_393B():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 3200, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_393B)

    Sleep(150)

    @scena.Lambda('lambda_395B')
    def lambda_395B():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 2400, 0x00)

        ExitThread()

    DispatchAsync(0x002B, 0x0001, lambda_395B)

    @scena.Lambda('lambda_3976')
    def lambda_3976():
        ChrWalkTo(0x00FE, 43420, -500, 45840, 3400, 0x00)

        ExitThread()

    DispatchAsync(0x002C, 0x0001, lambda_3976)

    Sleep(900)

    @scena.Lambda('lambda_3996')
    def lambda_3996():
        CameraMove(37180, 0, 72820, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3996)

    OP_6C(45000, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010060037V#004F#1P哇～……\n',
            '这么多客人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060038V#010F#2P真不愧是享有盛名的\n',
            '杰尼丝王立学院。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060039V真不敢相信这只是学院级的活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060040V#041F#1P呵呵，今年的客人\n',
            '似乎比往年多很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0510060041V#640F#3P好极了，终于开始了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060042V汉斯，快点走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0520060043V#730F#4P好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0520060044V#730F#4P我们就在学生会室，\n',
            '有什么事的话就过来找我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3B5A')
    def lambda_3B5A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3B5A')

    DispatchAsync2(0x0101, 0x0001, lambda_3B5A)

    @scena.Lambda('lambda_3B6B')
    def lambda_3B6B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3B6B')

    DispatchAsync2(0x0102, 0x0001, lambda_3B6B)

    @scena.Lambda('lambda_3B7C')
    def lambda_3B7C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3B7C')

    DispatchAsync2(0x0105, 0x0001, lambda_3B7C)

    ChrTalk(
        0x0102,
        (
            '#0020060045V#010F明白。\n',
            '你们两个要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_3BC2')
    def lambda_3BC2():
        ChrWalkTo(0x00FE, 34270, 0, 64690, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3BC2)

    Sleep(500)

    ChrSetDirection(0x0009, 135, 400)
    ChrWalkTo(0x0009, 34270, 0, 64690, 5000, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)

    @scena.Lambda('lambda_3C13')
    def lambda_3C13():
        CameraMove(37840, 0, 73580, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C13)

    ChrSetDirection(0x0105, 45, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060060046V#041F艾丝蒂尔、约修亚，\n',
            '我们就开始参观学园祭吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060047V#001F嗯，走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001E, 39850, -2000, 45950, 270)
    ChrSetPos(0x001F, 48940, 0, 27010, 270)
    ChrSetPos(0x0020, 21080, 0, 31060, 0)
    ChrSetPos(0x0021, 30350, 0, 64730, 225)
    ChrSetPos(0x0022, 31080, 0, 64010, 324)
    ChrSetPos(0x0023, 43200, -750, 48790, 270)
    ChrSetPos(0x0024, 30480, -2000, 34130, 315)
    ChrSetPos(0x0025, 25790, -1750, 43460, 90)
    ChrSetPos(0x0026, 39090, -2000, 50780, 45)
    ChrSetPos(0x0019, 29200, -2000, 51000, 315)
    ChrSetPos(0x001A, 29500, -2000, 52500, 270)
    ChrSetPos(0x001B, 29700, -2000, 51300, 270)
    ChrSetPos(0x001C, 39400, -2000, 39700, 180)
    ChrSetPos(0x002B, 37080, 0, 18890, 0)
    ChrSetPos(0x002C, 45250, 0, 45990, 270)
    ChrSetPos(0x000C, 39500, -2000, 36400, 315)
    ChrSetPos(0x000D, 28300, -2000, 36260, 90)
    OP_4B(0x000C, 0)
    OP_4B(0x000D, 0)
    TerminateThread(0x001E, 0x01)
    TerminateThread(0x001F, 0x01)
    TerminateThread(0x0020, 0x01)
    TerminateThread(0x0021, 0x01)
    TerminateThread(0x0022, 0x01)
    TerminateThread(0x0023, 0x01)
    TerminateThread(0x0024, 0x01)
    TerminateThread(0x0025, 0x01)
    TerminateThread(0x0026, 0x01)
    TerminateThread(0x0019, 0x01)
    TerminateThread(0x001A, 0x01)
    TerminateThread(0x001B, 0x01)
    TerminateThread(0x001C, 0x01)
    TerminateThread(0x002B, 0x01)
    TerminateThread(0x002C, 0x01)
    OP_4B(0x001E, 0)
    OP_4B(0x001F, 0)
    OP_4B(0x0020, 0)
    OP_4B(0x0021, 0)
    OP_4B(0x0022, 0)
    OP_4B(0x0023, 0)
    OP_4B(0x0024, 0)
    OP_4B(0x0025, 0)
    OP_4B(0x0026, 0)
    OP_4B(0x0019, 0)
    OP_4B(0x001A, 0)
    OP_4B(0x001B, 0)
    OP_4B(0x001C, 0)
    OP_4B(0x002B, 0)
    OP_4B(0x002C, 0)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    EventEnd(0x00)

    Return()

# id: 0x0031 offset: 0x3E8D
@scena.Code('func_31_3E8D')
def func_31_3E8D():
    EventBegin(0x00)
    ChrClearFlags(0x000A, 0x0080)
    CameraMove(39830, 0, 74030, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 39550, 0, 73430, 0)
    ChrSetPos(0x0105, 39540, 0, 74630, 180)
    ChrSetPos(0x000A, 38790, 6000, 63670, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010060376V#002F总之……\n',
            '先去找找约修亚吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060377V虽然不知道\n',
            '那个银发男子是谁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060378V#003F但不知怎么的，总有种不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000A, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060379V#047F先等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060380V#042F……基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FEB')
    def lambda_3FEB():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3FEB')

    DispatchAsync2(0x0101, 0x0001, lambda_3FEB)

    @scena.Lambda('lambda_3FFC')
    def lambda_3FFC():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3FFC')

    DispatchAsync2(0x0105, 0x0001, lambda_3FFC)

    @scena.Lambda('lambda_400D')
    def lambda_400D():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_400D)

    PlaySE(140, 0x00, 0x64)
    OP_92(0x000A, 0x0136, 5000, 10000, 0x00)
    OP_92(0x000A, 0x0136, 4000, 8000, 0x00)
    OP_92(0x000A, 0x0136, 3000, 6000, 0x00)
    OP_92(0x000A, 0x0136, 2000, 3000, 0x00)

    @scena.Lambda('lambda_405A')
    def lambda_405A():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_405A)

    ChrMoveTo(0x000A, 38580, 1000, 74200, 1500, 0x00)
    TerminateThread(0x0105, 0xFF)
    ChrSetFlags(0x0105, 0x0020)

    @scena.Lambda('lambda_4085')
    def lambda_4085():
        ChrSetDirection(0x00FE, 225, 200)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_4085)

    @scena.Lambda('lambda_4093')
    def lambda_4093():
        ChrSetDirection(0x00FE, 180, 200)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_4093)

    ChrSetChipByIndex(0x0105, 19)
    ChrSetSubChip(0x0105, 2)
    ChrMoveTo(0x000A, 39230, 0, 74780, 1000, 0x00)
    WaitForThreadExit(0x000A, 0x0003)
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    Fade(250)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetSubChip(0x0105, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0440060381V#310F啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060382V#042F有事想问你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060383V你知道\n',
            '约修亚去哪儿了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440060384V#311F啾～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetSubChip(0x0105, 2)
    OP_0D()

    @scena.Lambda('lambda_4174')
    def lambda_4174():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_4174')

    DispatchAsync2(0x0101, 0x0002, lambda_4174)

    @scena.Lambda('lambda_4185')
    def lambda_4185():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_4185')

    DispatchAsync2(0x0105, 0x0002, lambda_4185)

    @scena.Lambda('lambda_4196')
    def lambda_4196():
        OP_6C(135000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4196)

    @scena.Lambda('lambda_41A6')
    def lambda_41A6():
        CameraMove(39670, 0, 71450, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_41A6)

    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_41C3')
    def lambda_41C3():
        ChrWalkTo(0x00FE, 39360, 4000, 66590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_41C3)

    Sleep(400)

    @scena.Lambda('lambda_41E3')
    def lambda_41E3():
        ChrWalkTo(0x00FE, 39360, 4000, 66590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_41E3)

    Sleep(400)

    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0105, 0x02)
    ChrSetChipByIndex(0x0105, 65535)
    ChrClearFlags(0x0105, 0x0020)
    ChrSetSubChip(0x0105, 0)

    @scena.Lambda('lambda_421A')
    def lambda_421A():
        ChrWalkTo(0x00FE, 45550, 6000, 60210, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_421A)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010060385V#004F它还是那么厉害啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060386V#004F啊，那个方向是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060387V#042F嗯……\n',
            '是主楼后面的旧校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    ChrSetFlags(0x000A, 0x0080)
    OP_28(0x003D, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x0032 offset: 0x42D4
@scena.Code('func_32_42D4')
def func_32_42D4():
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x002D, 0x0080)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
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
    ChrSetFlags(0x002B, 0x0010)
    ChrSetFlags(0x002C, 0x0080)
    EventBegin(0x00)
    CameraMove(17970, 0, 46050, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0101, 17580, 0, 46020, 90)
    ChrSetPos(0x0102, 17920, 0, 45160, 90)
    ChrSetPos(0x0105, 17860, 0, 46810, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 19290, 0, 46470, 270)
    ChrSetPos(0x0009, 19430, 0, 45420, 270)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0510060897V#640F……难得来学院一次，\n',
            '怎么不多留一晚再走呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060898V接下来还有\n',
            '学园祭的庆功宴哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060899V#501F啊哈哈……\n',
            '虽然我也很想参加，不过还是算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060900V我们还是新人，\n',
            '太久不回协会也不大好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060901V#010F我们想在今天把报告完成，\n',
            '所以不好意思，这就要告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060902V#730F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060903V#734F约修亚啊，\n',
            '从今晚起我又孤身一人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060904V孤枕而眠太寂寞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060905V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060906V#017F汉斯……\n',
            '玩笑开过头了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060907V#018F艾丝蒂尔别把他的鬼话当真。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060908V#008F啊、啊哈哈，是玩笑啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060909V#641F这可是真心话啊，\n',
            '跟你们在一起就绝不会感到无聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060910V有机会的话或者有空的话，\n',
            '你们一定要再来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060911V#730F当然也一定要过夜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060912V#006F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060913V#010F我们一定会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060914V#048F呵呵……\n',
            '那我们走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060915V不抓紧的话，\n',
            '天很快就要黑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060916V#640F你现在要去\n',
            '玛诺利亚村吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060917V#041F嗯，我有好多话\n',
            '想和老师他们说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060918V而且学校也允许我今晚在外留宿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060919V#645F本来热热闹闹的庆功宴，\n',
            '主角居然一个都不在，\n',
            '真是太没意思了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060920V#648F不过，也没办法啦。\n',
            '我们就自己好好轻松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060921V#732F说起来，特蕾莎院长他们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060922V带着那么一大笔钱走回去，\n',
            '不觉得有点危险吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060923V#006F哦，这个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060924V因为担任这次学园祭警卫的\n',
            '卡露娜姐姐会负责护送他们回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060925V#010F而且，这还是校长\n',
            '委托协会一定要做的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520060926V#731F不愧是校长。\n',
            '处理事情还真是滴水不漏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060927V#730F……好了，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510060928V#644F多保重啊。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060929V以正游击士为目标，\n',
            '你们两个一定要继续努力哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060930V#001F嗯，看我们的吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060931V#019F你们也要努力念书哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x001C, 0x04, 0x40)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/R2301._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0033 offset: 0x4AFF
@scena.Code('func_33_4AFF')
def func_33_4AFF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B5D',
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

    Jump('loc_553E')

    def _loc_4B5D(): pass

    label('loc_4B5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_4EAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_4BC5',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0136,
        (
            '#0060050560V#040F这里是我就读的杰尼丝王立学院。\n',
            '　\n',
            '下次我再带你们好好参观吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_4EAC')

    def _loc_4BC5(): pass

    label('loc_4BC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 1, 0x451)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4DA8',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, 12200, 0, 46050, 90)
    ChrSetPos(0x0102, 11100, 0, 45460, 90)
    ChrSetPos(0x0136, 11200, 0, 46920, 90)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010050548V#000F哎，这里是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050549V#040F是我就读的杰尼丝王立学院。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050550V#004F哎～是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050551V真是好大啊。\n',
            '你就在这种地方学习吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050552V#043F是啊，如果有时间的话\n',
            '真想带你们好好参观一下呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050553V#012F不过现在必须得赶快\n',
            '回卢安找克拉姆才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050554V#002F是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x008A, 1, 0x451))
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4EAC')

    def _loc_4DA8(): pass

    label('loc_4DA8')

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010050555V#000F哎，\n',
            '这里就是科洛丝就读的学校吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050556V#040F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050557V#043F如果有时间的话\n',
            '真想带你们好好参观一下呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050558V#012F不过现在必须得赶快\n',
            '回卢安找克拉姆才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050559V#002F是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    EventEnd(0x01)

    def _loc_4EAC(): pass

    label('loc_4EAC')

    Jump('loc_553E')

    def _loc_4EAF(): pass

    label('loc_4EAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Return,
        ),
        'loc_5111',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_4F27',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0102,
        (
            '#0020050281V#010F这里就是科洛丝就读的学校吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050282V我们还是赶快去玛诺利亚村吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_510E')

    def _loc_4F27(): pass

    label('loc_4F27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_4F6B',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010050289V#004F这里是王立学院……\n',
            '真是好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_510E')

    def _loc_4F6B(): pass

    label('loc_4F6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 1, 0x451)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50D4',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, 12200, 0, 46050, 90)
    ChrSetPos(0x0102, 11100, 0, 45460, 90)
    ChrSetPos(0x0136, 11200, 0, 46920, 90)
    Sleep(800)

    ChrTalk(
        0x0136,
        (
            '#0060050284V#040F这里是我就读的杰尼丝王立学院。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050285V不过因为现在正在放假，\n',
            '不能带你们参观校园……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050286V#010F哎，就是这里啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050287V#004F这么大啊。\n',
            '就在这种地方学习吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050288V和主日学校果然不一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x008A, 1, 0x451))
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_510E')

    def _loc_50D4(): pass

    label('loc_50D4')

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010050283V#004F这里是王立学院……\n',
            '真是好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    def _loc_510E(): pass

    label('loc_510E')

    Jump('loc_553E')

    def _loc_5111(): pass

    label('loc_5111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_539A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_5189',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0102,
        (
            '#0020050153V#010F这里就是科洛丝就读的学校吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050154V我们还是赶快去孤儿院调查吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_5397')

    def _loc_5189(): pass

    label('loc_5189')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_51CD',
    )

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010050149V#004F这里是王立学院……\n',
            '真是好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_5397')

    def _loc_51CD(): pass

    label('loc_51CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 1, 0x451)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5311',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, 12200, 0, 46050, 90)
    ChrSetPos(0x0102, 11100, 0, 45460, 90)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010050144V#000F……这里是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050145V#010F有好多建筑设施呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050146V难道说这里就是\n',
            '科洛丝就读的杰尼丝王立学院？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050147V#004F这么大啊。\n',
            '就在这种地方学习吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050148V和主日学校果然不一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x008A, 1, 0x451))
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_5397')

    def _loc_5311(): pass

    label('loc_5311')

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010050150V#000F哎，这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050151V#010F是科洛丝就读的学校呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050152V我们还是赶快去孤儿院调查吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    EventEnd(0x01)

    def _loc_5397(): pass

    label('loc_5397')

    Jump('loc_553E')

    def _loc_539A(): pass

    label('loc_539A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_553E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 1, 0x451)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5504',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(13480, 0, 45900, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0101, 12200, 0, 46050, 90)
    ChrSetPos(0x0102, 11100, 0, 45460, 90)
    ChrSetPos(0x0136, 11200, 0, 46920, 90)
    Sleep(800)

    ChrTalk(
        0x0136,
        (
            '#0060040908V#040F这里是我就读的杰尼丝王立学院。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040909V不过因为现在正在放假，\n',
            '不能带你们参观校园……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040910V#010F哎，这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040911V#004F这么大啊。\n',
            '在这种地方学习吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040912V和主日学校果然不一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x008A, 1, 0x451))
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_553E')

    def _loc_5504(): pass

    label('loc_5504')

    EventBegin(0x02)

    ChrTalk(
        0x0101,
        (
            '#0010040913V#004F这里是王立学院……\n',
            '真是好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    def _loc_553E(): pass

    label('loc_553E')

    Return()

# id: 0x0034 offset: 0x553F
@scena.Code('func_34_553F')
def func_34_553F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 3, 0x433)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55F7',
    )

    EventBegin(0x01)
    ChrTurnDirectionByPos(0x0101, 12580, 45980, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060283V#002F啊，现在不能出去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060284V……要赶快去北边的旧校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060285V#042F嗯，赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_5829')

    def _loc_55F7(): pass

    label('loc_55F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5829',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5779',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ChrTurnDirectionByPos(0x0101, 12580, 45980, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060273V#000F啊，这里是校门……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060274V门还打开着，\n',
            '是不是还会有客人来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060275V#010F可能是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060276V到舞台剧开始还有一些时间呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060277V#040F嗯，专门为了看舞台剧\n',
            '而来的人也有不少呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060278V那我们继续参观吧。\n',
            '要尽情地玩也只有趁现在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060279V#001F嗯，走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_580E')

    def _loc_5779(): pass

    label('loc_5779')

    ChrTurnDirectionByPos(0x0101, 12580, 45980, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060280V#000F现在不能出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060281V#010F我们还是回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060282V趁还有空的时候\n',
            '好好享受一下学园祭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_580E(): pass

    label('loc_580E')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5829(): pass

    label('loc_5829')

    Return()

# id: 0x0035 offset: 0x582A
@scena.Code('func_35_582A')
def func_35_582A():
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

    Return()

# id: 0x0036 offset: 0x587A
@scena.Code('func_36_587A')
def func_36_587A():
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

    Return()

# id: 0x0037 offset: 0x58CA
@scena.Code('func_37_58CA')
def func_37_58CA():
    EventBegin(0x02)
    ClearScenaFlags(ScenaFlag(0x008A, 1, 0x451))

    ChrTalk(
        0x0101,
        (
            '#004F就像第一次来一样呢……\n',
            '真是好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x02)

    Return()

# id: 0x0038 offset: 0x5900
@scena.Code('func_38_5900')
def func_38_5900():
    OP_13(0x005F)

    Return()

# id: 0x0039 offset: 0x5904
@scena.Code('func_39_5904')
def func_39_5904():
    OP_13(0x005C)

    Return()

# id: 0x003A offset: 0x5908
@scena.Code('func_3A_5908')
def func_3A_5908():
    OP_13(0x005D)

    Return()

# id: 0x003B offset: 0x590C
@scena.Code('func_3B_590C')
def func_3B_590C():
    OP_13(0x006C)

    Return()

# id: 0x003C offset: 0x5910
@scena.Code('func_3C_5910')
def func_3C_5910():
    OP_13(0x006D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
