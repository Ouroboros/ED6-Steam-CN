import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4121_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4121   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4121.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02580._CH', 'ED6_DT07/CH02580P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01463._CH', 'ED6_DT07/CH01463P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
    ]

# id: 0x10001 offset: 0x1BA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾南',
            x                   = -4460,
            z                   = 0,
            y                   = 960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '金',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '希德中校',
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
            name                = '亚妮拉丝',
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
            name                = '嘉瑟',
            x                   = 53970,
            z                   = 0,
            y                   = 1360,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '诺娜',
            x                   = 57050,
            z                   = 0,
            y                   = 3000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '伯登',
            x                   = 63570,
            z                   = 0,
            y                   = -2300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '拉塔娜',
            x                   = 66490,
            z                   = 0,
            y                   = -2200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '托朗老人',
            x                   = 62300,
            z                   = 0,
            y                   = -3120,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '蒂库',
            x                   = 120580,
            z                   = 0,
            y                   = -2280,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '拉尔斯',
            x                   = 121660,
            z                   = 0,
            y                   = -1200,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '托伊',
            x                   = 120400,
            z                   = 0,
            y                   = -990,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '钓鱼人',
            x                   = 27820,
            z                   = 0,
            y                   = 62520,
            direction           = 191,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '罗伊德',
            x                   = 84510,
            z                   = 0,
            y                   = 56870,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '拜舍尔',
            x                   = 92000,
            z                   = 300,
            y                   = 61850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '塞森',
            x                   = 117070,
            z                   = 0,
            y                   = -1300,
            direction           = 132,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '多姆',
            x                   = 118280,
            z                   = 0,
            y                   = -2510,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '史帕德',
            x                   = 114540,
            z                   = 0,
            y                   = -500,
            direction           = 228,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '夏伊',
            x                   = 113510,
            z                   = 0,
            y                   = -1480,
            direction           = 273,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '科蕾蒂',
            x                   = 57640,
            z                   = 0,
            y                   = -910,
            direction           = 98,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '彭萨',
            x                   = 58990,
            z                   = 0,
            y                   = -920,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '拜舍尔',
            x                   = 117510,
            z                   = 0,
            y                   = 2000,
            direction           = 342,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '比尔爷爷',
            x                   = -870,
            z                   = 0,
            y                   = 2340,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '伊鲁妮婆婆',
            x                   = 540,
            z                   = 0,
            y                   = 2330,
            direction           = 272,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '迪克斯',
            x                   = -2600,
            z                   = 0,
            y                   = -1720,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '塔巴莎',
            x                   = 3340,
            z                   = 0,
            y                   = -3440,
            direction           = 289,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '萨米',
            x                   = 1560,
            z                   = 0,
            y                   = -1380,
            direction           = 360,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '吉恩',
            x                   = 1550,
            z                   = 0,
            y                   = -180,
            direction           = 177,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '钓鱼人',
            x                   = 117540,
            z                   = 0,
            y                   = 3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '巴拉尔',
            x                   = 125600,
            z                   = 0,
            y                   = -3380,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0024,
        ),
    )

# id: 0x10002 offset: 0x61A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x61A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x61A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2600,
            triggerZ            = 0,
            triggerY            = 820,
            triggerRange        = 800,
            actorX              = -4460,
            actorZ              = 1500,
            actorY              = 960,
            flags               = 0x007E,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28140,
            triggerZ            = 0,
            triggerY            = 61240,
            triggerRange        = 800,
            actorX              = 27820,
            actorZ              = 1500,
            actorY              = 62520,
            flags               = 0x007E,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25070,
            triggerZ            = 0,
            triggerY            = 56080,
            triggerRange        = 800,
            actorX              = 24330,
            actorZ              = 3000,
            actorY              = 55900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24870,
            triggerZ            = 0,
            triggerY            = 57940,
            triggerRange        = 800,
            actorX              = 23860,
            actorZ              = 2500,
            actorY              = 58100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24860,
            triggerZ            = 0,
            triggerY            = 59860,
            triggerRange        = 800,
            actorX              = 23870,
            actorZ              = 2800,
            actorY              = 59950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4970,
            triggerZ            = 0,
            triggerY            = -1040,
            triggerRange        = 1400,
            actorX              = 4970,
            actorZ              = 2000,
            actorY              = -1040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6F2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_7CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_709',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_709(): pass

    label('loc_709')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C7',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_746',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 33)
    TerminateThread(0x000A, 0x00)
    ChrSetPos(0x000A, 55450, 200, -2270, 180)

    def _loc_746(): pass

    label('loc_746')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_777',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x0009, 32)
    TerminateThread(0x0009, 0x00)
    ChrSetPos(0x0009, 60680, 200, -3460, 270)

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_79A',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 58950, 0, 2510, 360)

    def _loc_79A(): pass

    label('loc_79A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7C7',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_7C7(): pass

    label('loc_7C7')

    Jump('loc_9E1')

    def _loc_7CA(): pass

    label('loc_7CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_8D6',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_802',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 33)
    TerminateThread(0x000A, 0x00)
    ChrSetPos(0x000A, 55450, 200, -2270, 180)

    def _loc_802(): pass

    label('loc_802')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_833',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x0009, 32)
    TerminateThread(0x0009, 0x00)
    ChrSetPos(0x0009, 55450, 200, -2270, 180)

    def _loc_833(): pass

    label('loc_833')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_860',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetPos(0x000B, 57160, 200, -5120, 270)

    def _loc_860(): pass

    label('loc_860')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_883',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60960, 0, 2280, 0)

    def _loc_883(): pass

    label('loc_883')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8A6',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 58950, 0, 2510, 360)

    def _loc_8A6(): pass

    label('loc_8A6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_8D3',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_8D3(): pass

    label('loc_8D3')

    Jump('loc_9E1')

    def _loc_8D6(): pass

    label('loc_8D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_935',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_905',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60960, 0, 2280, 0)

    def _loc_905(): pass

    label('loc_905')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_932',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_932(): pass

    label('loc_932')

    Jump('loc_9E1')

    def _loc_935(): pass

    label('loc_935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9E1',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_96E',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetPos(0x000B, 57160, 200, -5120, 270)

    def _loc_96E(): pass

    label('loc_96E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_991',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60960, 0, 2280, 0)

    def _loc_991(): pass

    label('loc_991')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9B4',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 58950, 0, 2510, 360)

    def _loc_9B4(): pass

    label('loc_9B4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9E1',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_9E1(): pass

    label('loc_9E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_A6D',
    )

    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)

    Jump('loc_A88')

    def _loc_A6D(): pass

    label('loc_A6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A7C',
    )

    ChrSetFlags(0x001A, 0x0080)

    Jump('loc_A88')

    def _loc_A7C(): pass

    label('loc_A7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_A88',
    )

    ChrSetFlags(0x001B, 0x0080)

    def _loc_A88(): pass

    label('loc_A88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_A9E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_07_3798)

    Jump('loc_B25')

    def _loc_A9E(): pass

    label('loc_A9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_ABD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(1, 0x0025)

    Jump('loc_B25')

    def _loc_ABD(): pass

    label('loc_ABD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 2, 0x1202)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AD1',
    )

    MapSetFlags(0x10000000)
    Event(0, func_06_10F2)

    Jump('loc_B25')

    def _loc_AD1(): pass

    label('loc_AD1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_ADD'),
        (-1, 'loc_B25'),
    )

    def _loc_ADD(): pass

    label('loc_ADD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AF5',
    )

    MapSetFlags(0x10000000)
    Event(0, func_1E_AAF2)

    Jump('loc_B22')

    def _loc_AF5(): pass

    label('loc_AF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 0, 0x1628)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B0D',
    )

    MapSetFlags(0x10000000)
    Event(0, func_18_861A)

    Jump('loc_B22')

    def _loc_B0D(): pass

    label('loc_B0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 1, 0x1619)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B22',
    )

    MapSetFlags(0x10000000)
    Event(0, func_08_4EE7)

    def _loc_B22(): pass

    label('loc_B22')

    Jump('loc_B25')

    def _loc_B25(): pass

    label('loc_B25')

    Return()

# id: 0x0001 offset: 0xB26
@scena.Code('func_01_B26')
def func_01_B26():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B42',
    )

    OP_B1('t4121_y')

    Jump('loc_B4B')

    def _loc_B42(): pass

    label('loc_B42')

    OP_B1('t4121_n')

    def _loc_B4B(): pass

    label('loc_B4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 2, 0x1632)),
            Expr.Return,
        ),
        'loc_B61',
    )

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    Jump('loc_B83')

    def _loc_B61(): pass

    label('loc_B61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Return,
        ),
        'loc_B77',
    )

    OP_65(0x02, 0x0001)
    OP_65(0x03, 0x0001)
    OP_65(0x04, 0x0001)

    Jump('loc_B83')

    def _loc_B77(): pass

    label('loc_B77')

    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)

    def _loc_B83(): pass

    label('loc_B83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_B98',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_B98(): pass

    label('loc_B98')

    Return()

# id: 0x0002 offset: 0xB99
@scena.Code('func_02_B99')
def func_02_B99():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BB8',
    )

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_BCD')

    def _loc_BB8(): pass

    label('loc_BB8')

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_BCD(): pass

    label('loc_BCD')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C1C',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetPos(0x000B, 57160, 200, -5120, 270)

    def _loc_C1C(): pass

    label('loc_C1C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C3F',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60960, 0, 2280, 0)

    def _loc_C3F(): pass

    label('loc_C3F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C62',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 58950, 0, 2510, 360)

    def _loc_C62(): pass

    label('loc_C62')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C8F',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_C8F(): pass

    label('loc_C8F')

    OP_0D()

    Return()

# id: 0x0003 offset: 0xC91
@scena.Code('func_03_C91')
def func_03_C91():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_CAC',
    )

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

    Jump('loc_CBD')

    def _loc_CAC(): pass

    label('loc_CAC')

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

    def _loc_CBD(): pass

    label('loc_CBD')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_CF8',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60960, 0, 2280, 0)

    def _loc_CF8(): pass

    label('loc_CF8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_D25',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_D25(): pass

    label('loc_D25')

    OP_0D()

    Return()

# id: 0x0004 offset: 0xD27
@scena.Code('func_04_D27')
def func_04_D27():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D48',
    )

    OP_C9(
        0x01,
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

    Jump('loc_D5F')

    def _loc_D48(): pass

    label('loc_D48')

    OP_C9(
        0x01,
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

    def _loc_D5F(): pass

    label('loc_D5F')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_DC1',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 33)
    ChrSetSubChip(0x000A, 0)
    TerminateThread(0x000A, 0x00)
    ChrSetPos(0x000A, 55450, 200, -2270, 180)

    def _loc_DC1(): pass

    label('loc_DC1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_DF7',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x0009, 32)
    ChrSetSubChip(0x0009, 0)
    TerminateThread(0x0009, 0x00)
    ChrSetPos(0x0009, 55450, 200, -2270, 180)

    def _loc_DF7(): pass

    label('loc_DF7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E29',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 7)
    ChrSetSubChip(0x000B, 0)
    ChrSetPos(0x000B, 57160, 200, -5120, 270)

    def _loc_E29(): pass

    label('loc_E29')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E4C',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60960, 0, 2280, 0)

    def _loc_E4C(): pass

    label('loc_E4C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E6F',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 58950, 0, 2510, 360)

    def _loc_E6F(): pass

    label('loc_E6F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EA1',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetSubChip(0x000E, 0)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    def _loc_EA1(): pass

    label('loc_EA1')

    OP_0D()

    Return()

# id: 0x0005 offset: 0xEA3
@scena.Code('func_05_EA3')
def func_05_EA3():
    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
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

    Fade(1000)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F49',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x0009, 32)
    ChrSetSubChip(0x0009, 0)
    TerminateThread(0x0009, 0x00)
    ChrSetPos(0x0009, 60680, 200, -3460, 270)

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F2E',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_F2E(): pass

    label('loc_F2E')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F49',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_F49(): pass

    label('loc_F49')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FB5',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 33)
    ChrSetSubChip(0x000A, 0)
    TerminateThread(0x000A, 0x00)
    ChrSetPos(0x000A, 55450, 200, -2270, 180)

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F9A',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_F9A(): pass

    label('loc_F9A')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FB5',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_FB5(): pass

    label('loc_FB5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_100E',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 58950, 0, 2510, 360)

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF3',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_FF3(): pass

    label('loc_FF3')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_100E',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_100E(): pass

    label('loc_100E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1076',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetSubChip(0x000E, 0)
    ChrSetPos(0x000E, 54780, 0, -5080, 90)

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_105B',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_105B(): pass

    label('loc_105B')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1076',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1076(): pass

    label('loc_1076')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_10F1',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※要待命的成员\n',
            '　装备着『零力场发生器』。\n',
            '　回收后加入队伍的携带品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_10F1(): pass

    label('loc_10F1')

    Return()

# id: 0x0006 offset: 0x10F2
@scena.Code('func_06_10F2')
def func_06_10F2():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetPos(0x010A, -2600, 0, 1150, 270)
    ChrSetPos(0x0101, -2600, 0, 300, 270)
    ChrSetPos(0x0009, -500, -130, -7700, 354)
    ChrSetPos(0x000A, 500, -130, -7700, 354)
    CameraMove(1280, 0, -3520, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_1191')
    def lambda_1191():
        CameraMove(-4090, 0, 1200, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1191)

    @scena.Lambda('lambda_11A9')
    def lambda_11A9():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11A9)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    OP_28(0x0080, 0x01, 0x1000)

    ChrTalk(
        0x0008,
        (
            '#0590200088V#760F#5P是吗……\n',
            '你们两个辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200089V那么配合训练的评价\n',
            '把报酬付给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200090V#1004F#6P咦？训练\n',
            '还能得到报酬？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200091V#760F#5P嗯，这也是\n',
            '工作的一环。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200092V当然，也希望你们\n',
            '能够努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200093V#1016F#6P哈哈……我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x007E, 0x04, 0x10)
    OP_AF(0xCD, 0x007E)
    Sleep(100)

    OP_28(0x007F, 0x04, 0x10)
    OP_28(0x007F, 0x04, 0x20)
    OP_28(0x0080, 0x04, 0x10)
    OP_28(0x0080, 0x04, 0x20)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0590200094V#761F#5P看来你们在\n',
            '训练期间挺充实的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200095V#1006F#6P嗯！\n',
            '真是受益匪浅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200096V#1310F如果再有机会的话\n',
            '我还想去训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200097V#761F#5P呵呵，这真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200098V#760F说起来克鲁茨先生他们\n',
            '还在训练场吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200099V#1015F#6P嗯，和卡露娜小姐她们\n',
            '一起接受高级训练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200100V暂时应该回不来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200101V#1316F不过三个正游击士\n',
            '都去了国外。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200102V接下来有够忙的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x010A,
        (
            '#0120200103V#810F#2P卡西乌斯先生也正式\n',
            '在王国军工作了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200104V#1011F#6P啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200105V听说是要去雷斯顿要塞\n',
            '赴任……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200106V#760F#5P卡西乌斯先生以准将的身份\n',
            '就任军队作战指挥部长了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200107V也可以说是现在\n',
            '王国军的总指挥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(900)

    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x010A, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010200108V#1004F#6P军、军队的总指挥！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200109V就是说现在\n',
            '不是摩尔根将军了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200110V#760F#5P当初担任总指挥的本来是摩尔根将军，\n',
            '但将军自愿将\n',
            '权力交给了卡西乌斯先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200111V#761F将军一定是想把未来托付给\n',
            '年轻的卡西乌斯先生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200112V#1019F#6P呼……\n',
            '我怎么对老爸没这种感觉呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200113V#819F哈哈，这也是卡西乌斯先生的\n',
            '作风使然吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200114V#1314F不过这样一来协会的\n',
            '作战能力更加降低了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200115V#764F#5P嗯，虽然比以前\n',
            '更便于和军队合作了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200116V#762F但是现在我们\n',
            '需要警惕的事更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200117V#814F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200118V#1002F#6P那指的是……\n',
            '『结社』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200119V难道他们有什么动向？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200120V#764F#5P不，现在还没。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200121V#765F不过最近一个月\n',
            '发生了一些奇怪的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200122V比如……\n',
            '生活在各地的魔兽变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200123V#1026F#6P魔兽的变化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200124V#812F具体是怎样的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200125V#762F#5P首先是以前从未见过的\n',
            '新型魔兽在各地出现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200126V而且已知的魔兽也比之前\n',
            '难对付多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200127V现在原因还不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200128V#1317F还、还有这种事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200129V#815F就是说是那个『结社』\n',
            '捣的鬼！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200130V#764F#5P不，现在作结论\n',
            '还为时过早。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200131V#762F不过自从女王的诞辰庆典之后\n',
            '就开始发生一些事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200132V这一点是可以确定的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200133V#813F怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200134V#1003F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200135V#760F#5P其实我们对这件事\n',
            '已经做好了对策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200136V希望艾丝蒂尔小姐和\n',
            '亚妮拉丝小姐也能配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200137V#1004F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(800)

    TalkSetChrName('女性的声音')

    NpcTalk(
        0x0009,
        '女性的声音',
        (
            '#0030200138V#2P什么啊，你们已经到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_1CBD')
    def lambda_1CBD():
        CameraMove(-340, 0, -2920, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1CBD)

    @scena.Lambda('lambda_1CD5')
    def lambda_1CD5():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CD5)

    @scena.Lambda('lambda_1CED')
    def lambda_1CED():
        ChrTurnDirection(0x0101, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CED)

    Sleep(100)

    @scena.Lambda('lambda_1D00')
    def lambda_1D00():
        ChrTurnDirection(0x010A, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1D00)

    Sleep(100)

    @scena.Lambda('lambda_1D13')
    def lambda_1D13():
        ChrTurnDirection(0x0008, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D13)

    Sleep(300)

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_1D46')
    def lambda_1D46():
        ChrWalkTo(0x0009, -500, 0, -6000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1D46)

    @scena.Lambda('lambda_1D61')
    def lambda_1D61():
        ChrSetRGBAMask(0x0009, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1D61)

    Sleep(300)

    @scena.Lambda('lambda_1D78')
    def lambda_1D78():
        ChrWalkTo(0x000A, 500, 0, -6000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1D78)

    @scena.Lambda('lambda_1D93')
    def lambda_1D93():
        ChrSetRGBAMask(0x000A, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1D93)

    @scena.Lambda('lambda_1DA5')
    def lambda_1DA5():
        ChrTurnDirection(0x0101, 0x0009, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DA5)

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        ChrTurnDirection(0x010A, 0x0009, 0)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1DB3)

    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x010A,
        (
            '#0120200139V#814F#4P啊，雪拉前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200140V#1004F#6P雪拉姐！？\n',
            '还有阿加特也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E3A')
    def lambda_1E3A():
        CameraMove(-2940, 0, 920, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E3A)

    @scena.Lambda('lambda_1E52')
    def lambda_1E52():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E52)

    @scena.Lambda('lambda_1E6A')
    def lambda_1E6A():
        ChrMoveTo(0x0009, -2580, 0, -1130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1E6A)

    Sleep(300)

    @scena.Lambda('lambda_1E8A')
    def lambda_1E8A():
        ChrMoveTo(0x000A, -1530, 0, -1330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1E8A)

    @scena.Lambda('lambda_1EA5')
    def lambda_1EA5():
        ChrTurnDirection(0x0101, 0x0009, 0)
        Yield()

        Jump('lambda_1EA5')

    DispatchAsync2(0x0101, 0x0002, lambda_1EA5)

    Sleep(1000)

    @scena.Lambda('lambda_1EBB')
    def lambda_1EBB():
        ChrWalkTo(0x010A, -1710, 0, 350, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_1EBB)

    WaitForThreadExit(0x010A, 0x0002)
    ChrSetDirection(0x010A, 180, 400)
    WaitForThreadExit(0x0009, 0x0000)
    ChrTurnDirection(0x0009, 0x0101, 400)
    WaitForThreadExit(0x000A, 0x0000)
    ChrTurnDirection(0x000A, 0x010A, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x02)

    ChrTalk(
        0x0009,
        (
            '#0030200141V#021F欢迎回来，艾丝蒂尔、亚妮拉丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200142V#051F#6P哟，没想到你们\n',
            '这么快就回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200143V#1001F#5P雪拉姐，我回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010200144V#1017F#5P阿加特也好久没见了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200145V#053F#6P嗯，诞辰庆典之后就没见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200146V#552F……约修亚的事\n',
            '我听大叔说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200147V#051F你好像消沉了一阵子……\n',
            '不过看来已经\n',
            '打起精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200148V#1016F#5P嘿嘿，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200149V#1008F不过话说回来……\n',
            '你们两个怎么在一起？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200150V#1310F#2P唔～我也想问。\n',
            '真是少见的搭配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200151V#023F咦，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200152V#053F#6P嗯，我的确\n',
            '很少和她一起工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200153V#760F其实我们是让雪拉扎德小姐\n',
            '和阿加特先生去\n',
            '执行特别的任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200154V所以才让他们来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x010A, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200155V#1004F#6P特别的任务？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0590200156V#762F嗯……\n',
            '『噬身之蛇』的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200157V#1005F#6P『结社』的调查！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200158V#1317F#4P这、这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200159V#020F虽说是调查，不过\n',
            '还没有具体方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200160V因为这组织的存在本身\n',
            '还是一个谜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    ChrTurnDirection(0x010A, 0x000A, 400)

    ChrTalk(
        0x000A,
        (
            '#0050200161V#053F#6P一边工作一边遍访各地，\n',
            '关注『结社』的动向……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200162V#051F总之是既无聊又困难的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200163V#1015F#5P原，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200164V#1007F不过现在也\n',
            '只能这么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x010A, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200165V#1011F#6P那么要我们协助\n',
            '指的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200166V#760F嗯，要你们两个帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200167V为了在王国各地收集信息，\n',
            '我们让阿加特先生和\n',
            '雪拉扎德小姐分开行动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200168V因为单独调查不明身份的\n',
            '『结社』可能非常危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200169V#818F#4P就是说我们的其中一个\n',
            '帮雪拉前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200170V另一个帮阿加特\n',
            '前辈是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200171V#760F就是这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200172V怎么样？\n',
            '愿意协助参加调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200173V#1018F#6P我当然没问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200174V我本来就想调查『结社』的动向，\n',
            '正好能搭顺风船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200175V#1310F#4P也请让我一起帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200176V我绝不能对那些在幕后\n',
            '活动的可疑分子放任不管！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200177V#761F谢谢，这真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    ChrTurnDirection(0x010A, 0x000A, 400)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0030200178V#020F那么问题就是\n',
            '如何分组了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200179V我们倒觉得怎么样\n',
            '都可以接受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200180V#051F#6P大家也都认识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200181V根据自己的适应情况\n',
            '你们俩自己商量着决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200182V#1007F#5P呼……\n',
            '这还真是个难题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200183V#1015F#5P亚妮拉丝你觉得呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200184V#817F#4P嗯，我想想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200185V这么说可能有点不负责任……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200186V#810F不过还是让艾丝蒂尔\n',
            '来决定才最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200187V#1004F#5P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200188V#810F#4P毕竟艾丝蒂尔才刚\n',
            '成为了正游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200189V作为游击士应该还没\n',
            '完全给自己定型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200190V#811F所以以此为契机，\n',
            '来考虑一下自己将来的风格\n',
            '怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200191V#1011F#5P亚妮拉丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200192V#027F呵呵，亚妮拉丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200193V什么时候你也\n',
            '变得这么伶牙俐齿了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x000A, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200194V#811F#2P嘿嘿，承蒙夸奖⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200195V#053F#6P不过这话也有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x000A,
        (
            '#0050200196V#050F#6P比如我和雪拉扎德\n',
            '游击士的排位差不多，\n',
            '可是战斗风格相当不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200197V我是以魔法为辅，\n',
            '以重剑的攻击为主……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200198V#020F我是靠灵活性和长距离鞭攻击，\n',
            '并且灵活运用魔法的类型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200199V这些应该能作为\n',
            '选择的基准。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200200V#021F不过要说到游击士的工作，\n',
            '也不只是战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200201V你最好自己想想再选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200202V#1007F#5P嗯、嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200203V#1008F那么，就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_B7(0x09)
    ChrSetStatus(ChrTable['阿加特'], 0x00, 42)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    EquipCmd(ChrTable['阿加特'], ItemTable['双刃大砍刀'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['纤维护铠'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['金属靴'], 0xFF)
    EquipCmd(ChrTable['阿加特'], ItemTable['封技之刃'], 0x00)
    EquipCmd(ChrTable['阿加特'], ItemTable['移动１'], 0x01)
    EquipCmd(ChrTable['阿加特'], ItemTable['魔防１'], 0x02)
    EquipCmd(ChrTable['阿加特'], ItemTable['攻击１'], 0x05)
    AddCraft(ChrTable['阿加特'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['阿加特'], 0x0000)
    OP_BB(0x05, 0x06, 0x00000100)
    ChrSetStatus(ChrTable['雪拉扎德'], 0x00, 42)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['巨蟒'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['纤维护铠'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['金属靴'], 0xFF)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['睡眠之刃'], 0x00)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['省ＥＰ１'], 0x01)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['精神１'], 0x02)
    EquipCmd(ChrTable['雪拉扎德'], ItemTable['回避１'], 0x04)
    AddCraft(ChrTable['雪拉扎德'], CraftTable['连锁战技１(２人协力)'])
    AddCraft(ChrTable['雪拉扎德'], 0x0000)
    OP_BB(0x02, 0x06, 0x000000F0)

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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '选哪个？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【雪拉扎德】\n'),
            TXT(0x01, '【阿加特】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2CE3'),
        (0x00000001, 'loc_2CE9'),
        (-1, 'loc_2CEF'),
    )

    def _loc_2CE3(): pass

    label('loc_2CE3')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2CEF')

    def _loc_2CE9(): pass

    label('loc_2CE9')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2CEF')

    def _loc_2CEF(): pass

    label('loc_2CEF')

    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3243',
    )

    ChrTalk(
        0x0009,
        (
            '#0030200204V#020F这样啊，那就合作愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200205V#021F呵呵，期待你作为\n',
            '正游击士的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200206V#1007F#5P呼……我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x000A, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200207V#1310F#2P那么我就和\n',
            '阿加特前辈一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200208V#811F合作愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200209V#051F#6P嗯，彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200210V#053F好，那么这个问题\n',
            '总算是解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200211V不过还有一个问题是，\n',
            '访问各地的顺序怎么排？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0030200212V#020F艾南先生。\n',
            '我想听听你的意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    @scena.Lambda('lambda_2EC0')
    def lambda_2EC0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2EC0)

    @scena.Lambda('lambda_2ECE')
    def lambda_2ECE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ECE)

    @scena.Lambda('lambda_2EDC')
    def lambda_2EDC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2EDC)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0590200213V#764F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200214V#760F现在先去支援\n',
            '忙碌的地方支部比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200215V其实，从柏斯支部和卢安支部\n',
            '都发来了支援请求……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200216V#026F嗯，库拉茨和卡露娜\n',
            '都不在，也难怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x010A, 400)

    ChrTalk(
        0x000A,
        (
            '#0050200217V#050F#6P亚妮拉丝。\n',
            '你比较熟悉柏斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x000A, 400)

    ChrTalk(
        0x010A,
        (
            '#0120200218V#816F#2P那当然。\n',
            '我可是土生土长的柏斯孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_303D')
    def lambda_303D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_303D)

    @scena.Lambda('lambda_304B')
    def lambda_304B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_304B)

    ChrTalk(
        0x000A,
        (
            '#0050200219V#050F#6P那我们去\n',
            '柏斯支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200220V我也有点事要去那边办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200221V#1011F#5P啊，阿加特的故乡应该是\n',
            '在拉文努村吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200222V难道是荣归故里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200223V#053F#6P嗯，也差不多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0030200224V#021F那我们就\n',
            '去卢安支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200225V#020F艾丝蒂尔没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200226V#1006F#5P嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200227V#1012F卢安地区啊……\n',
            '不知道大家过的怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200228V#760F我来负责联络\n',
            '各支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200229V那么各位。\n',
            '路上请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3783')

    def _loc_3243(): pass

    label('loc_3243')

    ChrTalk(
        0x000A,
        (
            '#0050200230V#053F#6P是吗？明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200231V#050F既然成了正游击士，\n',
            '你就得更加努力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200232V要有心理准备啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200233V#1006F#5P是是，我知道了啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200234V#1016F真是的，就知道\n',
            '你会说让人讨厌的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200235V#055F#6P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200236V#027F好了好了，禁止斗嘴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x010A, 400)

    ChrTalk(
        0x0009,
        (
            '#0030200237V#021F那么我就和\n',
            '亚妮拉丝配合吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200238V#020F我要看看你的训练成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200239V#816F#2P嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200240V#811F呵呵，好久没和前辈配合了，\n',
            '真开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050200241V#053F#6P好，那么这个问题\n',
            '总算是解决了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200242V#050F不过还有一个问题是，\n',
            '访问各地的顺序怎么排？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0030200212V#020F艾南先生。\n',
            '我想听听你的意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    @scena.Lambda('lambda_34F0')
    def lambda_34F0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_34F0)

    @scena.Lambda('lambda_34FE')
    def lambda_34FE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34FE)

    @scena.Lambda('lambda_350C')
    def lambda_350C():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_350C)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0590200244V#764F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200214V#760F现在先去支援\n',
            '忙碌的地方支部比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200246V其实，从洛连特支部和卢安支部\n',
            '都来了支援请求……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030200247V#025F哎呀，洛连特看来\n',
            '太缺人手了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200248V#020F就算是为了帮爱娜，\n',
            '也是我去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120200249V#810F#2P是啊，我也赞成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120200250V#811F唔～好久没见到\n',
            '爱娜小姐了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0050200251V#051F#6P那我们就去\n',
            '卢安支部吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200252V艾丝蒂尔，没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200226V#1006F#5P嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200227V#1012F卢安地区啊……\n',
            '不知道大家过的怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590200228V#760F我来负责联络\n',
            '各支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590200229V那么各位。\n',
            '你们请小心上路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3783(): pass

    label('loc_3783')

    FadeOut(1500, 0, -1)
    OP_0D()
    NewScene('ED6_DT21/T4105._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x3798
@scena.Code('func_07_3798')
def func_07_3798():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37A9',
    )

    Call(0, 0x0026)

    def _loc_37A9(): pass

    label('loc_37A9')

    EventBegin(0x00)
    ChrSetPos(0x0101, -2600, 0, 1230, 270)
    ChrSetPos(0x00F7, -2600, 0, 190, 270)
    ChrSetPos(0x000D, -2020, 0, -990, 270)
    ChrSetPos(0x000C, -1560, 0, -30, 270)
    ChrSetPos(0x000B, -1600, 0, 1080, 270)
    ChrSetPos(0x000E, -1910, 0, 2020, 270)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x0008, 255)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    CameraMove(-7190, 0, 1580, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_387C')
    def lambda_387C():
        CameraMove(-3380, 0, 980, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_387C)

    @scena.Lambda('lambda_3894')
    def lambda_3894():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3894)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0590240606V#761F#5P各位来的正好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240607V#760F我已经读过你们\n',
            '在卢安和蔡斯做的报告了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240608V真是有劳你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240609V#1007F#4P唔～以『结社』的势力来看，\n',
            '只能算是小试牛刀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240610V面具男和墨镜男\n',
            '也都没有拿出真正实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590240611V#760F#5P不过即便如此，我们也\n',
            '已经可以确定『结社』有动作了，\n',
            '应该说是个不小的收获吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240612V我想，今后跟王国军的合作\n',
            '也会进行得比较顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3ABE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240613V#050F#6P那么，那个军队的委托\n',
            '究竟是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240614V果然是和『结社』有关？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B1D')

    def _loc_3ABE(): pass

    label('loc_3ABE')

    ChrTalk(
        0x0103,
        (
            '#0030240615V#020F#6P那么，那个军队的委托\n',
            '究竟是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240616V果然是和『结社』有关？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B1D(): pass

    label('loc_3B1D')

    ChrTalk(
        0x0008,
        (
            '#0590240617V#764F#5P好像是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240618V#762F不过电话里\n',
            '似乎说不清。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240619V所以军队会直接派人\n',
            '过来说明情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040240620V#035F唔……\n',
            '电话里说不清的内容啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240621V#030F说不定是想要\n',
            '防止窃听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240622V#1020F#5P窃、窃听！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590240623V#762F#5P这很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240624V导力通讯虽然方便，\n',
            '不过也有被偷听的危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240625V#764F协会之间的通讯\n',
            '倒是设有防止窃听用的\n',
            '周波变更功能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240626V#1015F#4P这防窃听功能\n',
            '不能在和军队通讯时使用？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590240627V#765F#5P军队有军队的通讯格式，\n',
            '所以没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240628V只能互相使用一般通讯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240629V#1007F#4P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240630V#1019F唔～索性用\n',
            '同样的规格不就行了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080240631V#070F#2P呵呵，虽说是在合作，不过毕竟是\n',
            '一国的军队和国际民间组织之间的关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240632V不能避免地要有情报安全措施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3EDE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240633V#053F#6P可是艾南。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240634V#051F你好像对军队的委托是什么\n',
            '已经心中有数了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240635V不然你也不会特意\n',
            '把我们叫来蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F6D')

    def _loc_3EDE(): pass

    label('loc_3EDE')

    ChrTalk(
        0x0103,
        (
            '#0030240636V#026F#6P可是艾南先生，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240637V#020F你好像对军队的委托是什么\n',
            '已经心中有数了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240638V还特别把我们从蔡斯\n',
            '叫来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F6D(): pass

    label('loc_3F6D')

    ChrTalk(
        0x0008,
        (
            '#0590240639V#761F#5P哎呀，被你们看穿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240640V#760F虽然这只是我的推测……\n',
            '不过很可能和\n',
            '『互不侵犯条约』有关呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240641V#1004F#4P互不侵犯条约……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240642V#1015F最近倒是经常\n',
            '听说这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240643V这条约具体内容是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#0060240644V#040F#6P是女王陛下提倡、\n',
            '由利贝尔、埃雷波尼亚、卡尔瓦德\n',
            '三国之间签订的条约。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240645V核心思想是不用武力，而是\n',
            '通过协商解决国家间的纠纷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000C, 400)

    @scena.Lambda('lambda_4135')
    def lambda_4135():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4135)

    Sleep(50)

    @scena.Lambda('lambda_4148')
    def lambda_4148():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4148)

    Sleep(50)

    @scena.Lambda('lambda_415B')
    def lambda_415B():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_415B)

    Sleep(50)

    @scena.Lambda('lambda_416E')
    def lambda_416E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_416E)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010240646V#1004F#5P啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240647V这样一来不是就\n',
            '不再有战争了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060240648V#047F#6P不，因为没有强制约束力，\n',
            '所以这看来很难……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240649V#040F不过还是有一定的影响力的，\n',
            '祖母大人是希望这能推动\n',
            '各国国民之间的友好氛围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240650V#1011F#5P哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080240651V#071F#2P不愧是艾莉茜雅陛下,\n',
            '着眼之处很厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240652V#061F#6P如果能成为促使三国友好\n',
            '相处的契机就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590240653V#760F#5P这互不侵犯条约将于下周末\n',
            '在『艾尔贝离宫』签订。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240654V外国的要人也会云集，\n',
            '媒体也将给予关注。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240655V#764F在这种情况下，如果『结社』\n',
            '有什么企图的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_43DC')
    def lambda_43DC():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_43DC)

    Sleep(50)

    @scena.Lambda('lambda_43EF')
    def lambda_43EF():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_43EF)

    Sleep(50)

    @scena.Lambda('lambda_4402')
    def lambda_4402():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_4402)

    Sleep(50)

    @scena.Lambda('lambda_4415')
    def lambda_4415():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4415)

    Sleep(50)

    @scena.Lambda('lambda_4428')
    def lambda_4428():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4428)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010240656V#1002F#4P不错……\n',
            '这可不是闹着玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_44EA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240657V#053F#6P呼……\n',
            '这看来是个严峻的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240658V#051F那在那个负责人来之前，\n',
            '我们在这里等就行了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_455D')

    def _loc_44EA(): pass

    label('loc_44EA')

    ChrTalk(
        0x0103,
        (
            '#0030240659V#026F#6P唔……\n',
            '这看来是个严峻的问题啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240660V#020F那在负责人来之前，\n',
            '我们在这里等就行了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_455D(): pass

    label('loc_455D')

    ChrTalk(
        0x0008,
        (
            '#0590240661V#760F#5P我想想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240662V离约定的时间的还早，\n',
            '你们也可以自由行动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(195, 0x01, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0590240663V#763F#5P哎呀，失敬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)

    @scena.Lambda('lambda_465A')
    def lambda_465A():
        CameraMove(-4530, 0, 870, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_465A)

    ChrWalkTo(0x0008, -5700, 0, -130, 2000, 0x00)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(400)

    OP_23(0x00C3)
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0590240664V#760F#5P这儿是游击士协会。\n',
            '格兰赛尔支部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240665V嗯……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240666V#763F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240667V#765F原来如此……是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240668V嗯，这确实\n',
            '不好办了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240669V#764F请稍等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010240670V#1015F莫非是王国军打来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0590240671V#760F#5P不，是艾尔贝离宫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240672V他们说保护了一个\n',
            '迷路的孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240673V可是却找不到监护人，\n',
            '感到很为难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240674V#1004F啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060240675V#043F#6P这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590240676V#760F#5P他们委托我们去\n',
            '寻找监护人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240677V离军队的负责人来还有些时间,\n',
            '配合我们做一个调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_49D6',
    )

    ChrTalk(
        0x0101,
        (
            '#0010240678V#1006F那是自然，\n',
            '我们接下来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240679V阿加特也没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050240680V#051F#6P真没办法。\n',
            '赶快去离宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A58')

    def _loc_49D6(): pass

    label('loc_49D6')

    ChrTalk(
        0x0101,
        (
            '#0010240678V#1006F那是自然，\n',
            '我们接下来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240682V雪拉姐也没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030240683V#021F#6P当然了。\n',
            '赶快去离宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A58(): pass

    label('loc_4A58')

    ChrTalk(
        0x0008,
        (
            '#0590240684V#760F#5P那太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0590240685V#761F#5P嗯，我们正好有\n',
            '有空的游击士在，\n',
            '我让他们去你们那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240686V#760F请问您的大名是……\n',
            '嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240687V那么请耐心等候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x01, 0x00)
    Sleep(800)

    ChrSetDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_4B47')
    def lambda_4B47():
        CameraMove(-3380, 0, 980, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4B47)

    @scena.Lambda('lambda_4B5F')
    def lambda_4B5F():
        ChrWalkTo(0x00FE, -4480, 0, 960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4B5F)

    Sleep(500)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0590240688V#760F#5P对方是在艾尔贝离宫工作的\n',
            '管家雷蒙德先生，\n',
            '他在照顾那个迷路的孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240689V你们到了离宫请去找他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240690V#1006F#4P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240691V#1015F……雷蒙德先生，\n',
            '好像在哪儿听说过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080240692V#073F#2P嗯～不就是那个年轻的管家吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240693V在解救离宫的时候\n',
            '躲在柜台下面的那位。',
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
            '#0010240694V#1006F#6P哦，就是那个自称是\n',
            '奈尔朋友的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590240695V#761F#5P你们认识的话就\n',
            '更好办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590240696V#760F那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-5650, 0, -18030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6E(262, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4E2E',
    )

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_4E43')

    def _loc_4E2E(): pass

    label('loc_4E2E')

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_4E43(): pass

    label('loc_4E43')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetPos(0x0000, -140, 0, 90, 180)
    ChrSetPos(0x0001, -140, 0, 90, 180)
    ChrSetPos(0x0002, -140, 0, 90, 180)
    ChrSetPos(0x0003, -140, 0, 90, 180)
    CameraMove(-140, 0, 90, 0)
    Sleep(500)

    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x02C1, 3, 0x160B))
    OP_4B(0x0008, 255)
    OP_28(0x0089, 0x04, 0x02)
    OP_28(0x0089, 0x04, 0x08)
    OP_28(0x0089, 0x01, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x4EE7
@scena.Code('func_08_4EE7')
def func_08_4EE7():
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
        'loc_4F02',
    )

    Call(0, 0x0026)
    Call(0, 0x0027)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)

    def _loc_4F02(): pass

    label('loc_4F02')

    ChrSetPos(0x000F, -2310, 0, 2150, 180)
    ChrClearFlags(0x000F, 0x0080)
    OP_4A(0x0008, 255)
    Call(0, 0x001D)
    ChrSetPos(0x00FA, -2600, 0, 500, 360)
    ChrSetPos(0x00FB, -1500, 0, 480, 360)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetFlags(0x012F, 0x0080)
    CameraMove(-110, -250, -5770, 0)
    OP_67(0, 7440, -10000, 0)
    CameraSetDistance(2830, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    CreateThread(0x0101, 0x01, 0x00, func_09_81B7)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_0B_8255)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_0C_82A4)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_0D_82F3)
    Sleep(500)

    CreateThread(0x012F, 0x01, 0x00, func_0A_8206)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010250147V#1006F#6P我们回来了，艾南先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250148V#1004F……啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5032')
    def lambda_5032():
        CameraMove(-2890, 0, 1460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5032)

    @scena.Lambda('lambda_504A')
    def lambda_504A():
        OP_67(0, 7350, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_504A)

    @scena.Lambda('lambda_5062')
    def lambda_5062():
        CameraSetDistance(2780, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5062)

    @scena.Lambda('lambda_5072')
    def lambda_5072():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5072)

    Sleep(100)

    @scena.Lambda('lambda_5085')
    def lambda_5085():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5085)

    Sleep(200)

    @scena.Lambda('lambda_5098')
    def lambda_5098():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_5098)

    Sleep(100)

    @scena.Lambda('lambda_50AB')
    def lambda_50AB():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_50AB)

    WaitForThreadExit(0x00FB, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_5103',
    )

    ChrTalk(
        0x0107,
        (
            '#0070250149V#560F#5P啊，艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5178')

    def _loc_5103(): pass

    label('loc_5103')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_5141',
    )

    ChrTalk(
        0x0108,
        (
            '#0080250150V#070F#5P艾丝蒂尔你回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5178')

    def _loc_5141(): pass

    label('loc_5141')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_5178',
    )

    ChrTalk(
        0x0104,
        (
            '#0040250151V#030F#5P呼，你回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5178(): pass

    label('loc_5178')

    Sleep(300)

    @scena.Lambda('lambda_5183')
    def lambda_5183():
        ChrWalkTo(0x00FE, -2600, 0, 500, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5183)

    If(
        (
            (Expr.Eval, "OP_CB(0xFA)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51BB',
    )

    CreateThread(0x00FB, 0x00, 0x00, func_14_85AA)
    Sleep(400)

    CreateThread(0x00FA, 0x00, 0x00, func_15_85C6)

    Jump('loc_51CE')

    def _loc_51BB(): pass

    label('loc_51BB')

    CreateThread(0x00FB, 0x00, 0x00, func_16_85E2)
    Sleep(400)

    CreateThread(0x00FA, 0x00, 0x00, func_17_85FE)

    def _loc_51CE(): pass

    label('loc_51CE')

    @scena.Lambda('lambda_51D4')
    def lambda_51D4():
        ChrWalkTo(0x00FE, -1580, 0, 480, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_51D4)

    Sleep(200)

    @scena.Lambda('lambda_51F4')
    def lambda_51F4():
        ChrWalkTo(0x00FE, -2440, 0, -680, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_51F4)

    Sleep(300)

    @scena.Lambda('lambda_5214')
    def lambda_5214():
        ChrWalkTo(0x00FE, -1260, 0, -570, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_5214)

    Sleep(300)

    @scena.Lambda('lambda_5234')
    def lambda_5234():
        ChrWalkTo(0x00FE, -1400, 0, -1660, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x012F, 0x0000, lambda_5234)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x000F, 180, 400)
    ChrSetDirection(0x0008, 90, 400)
    WaitForThreadExit(0x00F8, 0x0000)
    ChrSetDirection(0x00F9, 0, 400)

    ChrTalk(
        0x000F,
        (
            '#0620250152V#701F哟，艾丝蒂尔。\n',
            '好几天没见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250153V#1018F#6P咦……\n',
            '这不是希德中校吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x012F, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5344',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250154V#051F哦，原来军队说的负责人\n',
            '就是你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250155V是从雷斯顿要塞来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53A6')

    def _loc_5344(): pass

    label('loc_5344')

    ChrTalk(
        0x0103,
        (
            '#0030250156V#027F原来如此，原来军队说的负责人\n',
            '就是你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250157V你是从雷斯顿要塞来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53A6(): pass

    label('loc_53A6')

    ChrTalk(
        0x000F,
        (
            '#0620250158V#701F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250159V我是刚坐警备艇\n',
            '过来王都的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210884V#1011F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250161V正好我们也\n',
            '工作完回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 135, 400)

    ChrTalk(
        0x0008,
        (
            '#0590250162V#763F#5P哟……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250163V那个小姑娘\n',
            '难道就是那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250164V#1015F#6P啊，嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250165V因为一些原因\n',
            '就把她带回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x012F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250166V#1011F#5P那个，小玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250167V姐姐们有些事要谈，\n',
            '你能不能上２楼等着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5552')
    def lambda_5552():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5552)

    @scena.Lambda('lambda_5560')
    def lambda_5560():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5560)

    Sleep(200)

    @scena.Lambda('lambda_5573')
    def lambda_5573():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5573)

    @scena.Lambda('lambda_5581')
    def lambda_5581():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_5581)

    Sleep(200)

    @scena.Lambda('lambda_5594')
    def lambda_5594():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_5594)

    @scena.Lambda('lambda_55A2')
    def lambda_55A2():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_55A2)

    Sleep(500)

    ChrTalk(
        0x012F,
        (
            '#0220250168V#264F#6P哎呀……\n',
            '难道是工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250169V#1025F#5P嗯、嗯……对不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250170V#266F#6P没关系的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250171V工作、工作，\n',
            '就像我爸爸那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250172V玲不太喜欢\n',
            '这种感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250173V#1013F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x012F, 400)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5729',
    )

    ChrTalk(
        0x0107,
        (
            '#0070250174V#560F#5P我、我说，小玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250175V和我一起\n',
            '聊聊天吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250176V#061F我很想\n',
            '了解小玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_57A3')

    def _loc_5729(): pass

    label('loc_5729')

    ChrTalk(
        0x0107,
        (
            '#0070250177V#560F#2P我、我说……\n',
            '你是叫小玲吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250175V和我一起\n',
            '聊聊天吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250176V#061F我很想\n',
            '了解小玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_57A3(): pass

    label('loc_57A3')

    ChrTurnDirection(0x012F, 0x0107, 400)

    ChrTalk(
        0x012F,
        (
            '#0220250180V#264F#6P和你？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250181V#263F嗯，也好。\n',
            '就和你聊聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_586B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070250182V#067F#5P嘿嘿，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070250183V#560F#6P那么姐姐，\n',
            '我们就在２楼等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58BA')

    def _loc_586B(): pass

    label('loc_586B')

    ChrTalk(
        0x0107,
        (
            '#0070250184V#067F#2P嘿嘿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250185V#560F那么姐姐，\n',
            '我们就在2楼等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58BA(): pass

    label('loc_58BA')

    Sleep(100)

    @scena.Lambda('lambda_58C5')
    def lambda_58C5():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_58C5')

    DispatchAsync2(0x0101, 0x0002, lambda_58C5)

    @scena.Lambda('lambda_58D6')
    def lambda_58D6():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_58D6')

    DispatchAsync2(0x00F7, 0x0002, lambda_58D6)

    @scena.Lambda('lambda_58E7')
    def lambda_58E7():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_58E7')

    DispatchAsync2(0x000F, 0x0002, lambda_58E7)

    @scena.Lambda('lambda_58F8')
    def lambda_58F8():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_58F8')

    DispatchAsync2(0x0008, 0x0002, lambda_58F8)

    @scena.Lambda('lambda_5909')
    def lambda_5909():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_5909')

    DispatchAsync2(0x0104, 0x0002, lambda_5909)

    @scena.Lambda('lambda_591A')
    def lambda_591A():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_591A')

    DispatchAsync2(0x0105, 0x0002, lambda_591A)

    @scena.Lambda('lambda_592B')
    def lambda_592B():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_592B')

    DispatchAsync2(0x0108, 0x0002, lambda_592B)

    @scena.Lambda('lambda_593C')
    def lambda_593C():
        CameraMove(-680, 2000, 1510, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_593C)

    @scena.Lambda('lambda_5954')
    def lambda_5954():
        OP_67(0, 7350, -10000, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_5954)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5984',
    )

    CreateThread(0x0107, 0x01, 0x00, func_10_8439)
    CreateThread(0x012F, 0x01, 0x00, func_11_84A1)

    Jump('loc_59BD')

    def _loc_5984(): pass

    label('loc_5984')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59A2',
    )

    CreateThread(0x0107, 0x01, 0x00, func_0E_8342)
    CreateThread(0x012F, 0x01, 0x00, func_0F_83BE)

    Jump('loc_59BD')

    def _loc_59A2(): pass

    label('loc_59A2')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_59BD',
    )

    CreateThread(0x0107, 0x01, 0x00, func_10_8439)
    CreateThread(0x012F, 0x01, 0x00, func_11_84A1)

    def _loc_59BD(): pass

    label('loc_59BD')

    WaitForThreadExit(0x012F, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x000F, 0x0003)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x000F, 0x02)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0104, 0x02)
    TerminateThread(0x0105, 0x02)
    TerminateThread(0x0108, 0x02)

    @scena.Lambda('lambda_59EE')
    def lambda_59EE():
        CameraMove(-2800, 0, 1820, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_59EE)

    @scena.Lambda('lambda_5A06')
    def lambda_5A06():
        OP_67(0, 7350, -10000, 1500)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_5A06)

    @scena.Lambda('lambda_5A1E')
    def lambda_5A1E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5A1E)

    @scena.Lambda('lambda_5A2C')
    def lambda_5A2C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5A2C)

    Sleep(50)

    @scena.Lambda('lambda_5A3F')
    def lambda_5A3F():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5A3F)

    @scena.Lambda('lambda_5A4D')
    def lambda_5A4D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5A4D)

    Sleep(50)

    @scena.Lambda('lambda_5A60')
    def lambda_5A60():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5A60)

    @scena.Lambda('lambda_5A6E')
    def lambda_5A6E():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_5A6E)

    Sleep(50)

    @scena.Lambda('lambda_5A81')
    def lambda_5A81():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_5A81)

    @scena.Lambda('lambda_5A8F')
    def lambda_5A8F():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5A8F)

    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x000F, 0x0003)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010250186V#1016F#6P呼……\n',
            '帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250187V#760F嗯，具体情况\n',
            '等会儿再问吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250188V先听听希德中校\n',
            '是怎么说的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250189V#1006F#6P啊，嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B97',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250190V#051F那就快让我们\n',
            '听一听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BC4')

    def _loc_5B97(): pass

    label('loc_5B97')

    ChrTalk(
        0x0103,
        (
            '#0030250191V#020F那就快让我们听一听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BC4(): pass

    label('loc_5BC4')

    ChrTalk(
        0x000F,
        (
            '#0620250192V#703F不好意思。\n',
            '我们这边也很急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250193V#700F首先你们可以把这\n',
            '认为是王国军的正式请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250194V需要你们调查一件事情\n',
            '以及搜集信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250195V#1004F#6P调查一件事情……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0620250196V#700F你们知道『互不侵犯条约』吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250197V其实，很多地方都收到了\n',
            '欲图妨碍条约\n',
            '签订的恐吓信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010250198V#1020F#6P恐、恐吓信！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250199V#043F#6P这……\n',
            '还真不能掉以轻心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250200V到底是什么样的内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0620250201V#703F……你们请看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS128._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '参加『互不侵犯条约』缔结的人们啊，\n',
            '你们要立即停止这\n',
            '充满欺骗和妥协的协议。\n',
            '万一还有不予停止的人，\n',
            '就会有大灾降临在他头上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    FadeIn(300, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010250204V#1019F#6P哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F8D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250205V#053F#6P原来如此，确实是恐吓信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250206V#552F就这点内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FDE')

    def _loc_5F8D(): pass

    label('loc_5F8D')

    ChrTalk(
        0x0103,
        (
            '#0030250207V#026F#6P原来如此，确实是恐吓信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250208V#022F就这点内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FDE(): pass

    label('loc_5FDE')

    ChrTalk(
        0x000F,
        (
            '#0620250209V#700F嗯，就这点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250210V而且似乎还刻意隐去了\n',
            '寄信人的名字。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250211V老实说，虽然让人感觉恶作剧的\n',
            '可能性最大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250212V#035F#6P却也有着不像是单纯的\n',
            '恶作剧的特征──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250213V#030F是不是这样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0620250214V#702F嗯……\n',
            '就是收到恐吓信的单位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250215V#703F首先是雷斯顿要塞司令部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250216V然后是飞船公社、格兰赛尔大圣堂、\n',
            '罗恩鲍姆酒店和利贝尔通讯社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250217V#700F还有帝国大使馆、共和国大使馆、\n',
            '格兰赛尔城堡和艾尔贝离宫。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250218V总共9处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250219V#1020F#6P这、这么多！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250220V#072F#6P原来如此……\n',
            '如果只是恶作剧，规模也太大了点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250221V也难怪军队会有所在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_62FF',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250222V#050F#6P不过飞船公社和七耀教会，\n',
            '还有酒店和利贝尔通讯啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250223V表面上看都是和条约缔结\n',
            '没什么关系的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6383')

    def _loc_62FF(): pass

    label('loc_62FF')

    ChrTalk(
        0x0103,
        (
            '#0030250224V#022F#6P不过飞船公社和七耀教会，\n',
            '还有酒店和利贝尔通讯啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250225V表面上看都是和条约缔结\n',
            '没什么关系的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6383(): pass

    label('loc_6383')

    ChrTalk(
        0x000F,
        (
            '#0620250226V#700F不过从严格意义上来说，\n',
            '也并非完全没有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250227V#703F首先飞船公社\n',
            '是接送帝国、共和国有关人员的\n',
            '航班提供者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250228V同样，酒店房间也已经有\n',
            '有关人员在预定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250229V#700F另外大圣堂的卡兰大主教\n',
            '也受女王陛下委托\n',
            '负责监督和观察条约缔结……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250230V利贝尔通讯关于互不侵犯条约的特辑\n',
            '报导在几期之前就开始连载了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250231V#1015F#6P唔～哪边都和条约\n',
            '有着某种联系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250232V到底是什么人的把戏呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250233V#032F#6P呼……\n',
            '这个不能用普通的思维模式来分析。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250234V既然是国际条约，\n',
            '那么打算妨碍它的嫌疑人\n',
            '人选就有多种可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250235V#074F#6P没错。\n',
            '共和国或者帝国的主战派……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250236V或不欢迎三国合作的\n',
            '别国所为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250237V#042F#6P……当然在王国内\n',
            '也是有嫌疑人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250238V#1007F#6P另外……\n',
            '最坏的可能性还有『结社』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_66F5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250239V#050F#6P那么军方希望我们\n',
            '调查什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_672C')

    def _loc_66F5(): pass

    label('loc_66F5')

    ChrTalk(
        0x0103,
        (
            '#0030250240V#022F#6P那么军方希望我们\n',
            '调查什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_672C(): pass

    label('loc_672C')

    ChrTalk(
        0x000F,
        (
            '#0620250241V#701F希望你们调查的\n',
            '不是别的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250242V就是对收到恐吓信的\n',
            '各单位进行调查询问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250243V具体是──除去艾尔贝离宫\n',
            '和雷斯顿要塞的７个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250244V#764F飞船公社、格兰赛尔大圣堂、\n',
            '罗恩鲍姆酒店和利贝尔通讯社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250245V#762F帝国大使馆、共和国大使馆、\n',
            '还有格兰赛尔城堡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250246V#030F#6P呼，都不是穿着制服的军人\n',
            '方便随便出入的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040250247V在已经失去了情报部的现在，\n',
            '也难怪会委托给协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0620250248V#701F惭愧，你说得一点都没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250249V并且新的司令官殿下的方针是\n',
            '能交给协会的工作都要\n',
            '一股脑地交给协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250250V我正在对此进行实践。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250251V#1019F#6P真是的……\n',
            '老爸还真得意忘形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A0F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250252V#551F#6P切，一听就是大叔\n',
            '会说出来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A50')

    def _loc_6A0F(): pass

    label('loc_6A0F')

    ChrTalk(
        0x0103,
        (
            '#0030250253V#021F#6P好了好了。\n',
            '这也是老师他信赖我们的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A50(): pass

    label('loc_6A50')

    ChrTalk(
        0x000F,
        (
            '#0620250254V#701F呵呵，说到底委托你们\n',
            '还是我个人的意见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250255V前不久我被任命负责王都\n',
            '周围的所有警戒工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250256V为了准备警戒体制，\n',
            '就需要尽量多的信息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250257V能不能请你们帮这个忙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250258V#1015F#6P嗯、嗯……\n',
            '我们虽然很愿意接下来，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250259V不过还有一件必须\n',
            '解决的案子已经发生了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250260V#760F就是刚才那个小姑娘的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250261V能不能简单扼要地\n',
            '说明一下情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把在艾尔贝离宫玲的父母\n',
            '丢下玲离开的事说了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#0620250262V#702F原来如此……\n',
            '这确实不能放下不管。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250263V可是，竟然会丢下那么小的\n',
            '孩子不管……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250264V#1002F#6P之前和她的双亲\n',
            '有聊过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250265V看起来是很认真又\n',
            '很为女儿着想的父母。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250266V可能是有什么\n',
            '难言之隐吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250267V#764F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250268V可能是不希望\n',
            '把女儿卷进\n',
            '什么事件里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250269V#760F可是，这样的话\n',
            '说不定能一箭双雕？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250270V#1004F#6P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250271V#760F玲小姐的双亲\n',
            '是外国人呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250272V那去问问大使馆和\n',
            '酒店岂不很好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250273V#1006F#6P啊，对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6EE5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250274V#051F#6P这些地方\n',
            '都收到恐吓信了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250275V还有，飞船公社也\n',
            '应该有乘船记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F41')

    def _loc_6EE5(): pass

    label('loc_6EE5')

    ChrTalk(
        0x0103,
        (
            '#0030250276V#027F#6P这些地方\n',
            '都收到恐吓信了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250277V飞船公社也\n',
            '应该有乘船记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F41(): pass

    label('loc_6F41')

    ChrTalk(
        0x000F,
        (
            '#0620250278V#701F王国军也会向各地命令\n',
            '协助找寻她的父母。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250279V如果通过了哨所就应该会有消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250280V#1008F#6P谢谢你，希德中校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250281V#761F看来接下来的问题就\n',
            '好商量了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250282V#760F具体的调查方法和任务分配\n',
            '就交给我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250283V调查结果的报告\n',
            '用文件和口头形式可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0620250284V#701F嗯，为了避免窃听\n',
            '还是请别使用导力器了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250285V其实从今天开始，艾尔贝离宫\n',
            '将设置警戒本部。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620250286V能不能有劳你们\n',
            '去那边做报告？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250287V#1006F#6P嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250288V那么我们就把调查结果\n',
            '直接送去艾尔贝离宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0620250289V#701F拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000F, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_729C',
    )

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '送走希德中校之后\n',
            '艾丝蒂尔她们讨论了调查方法和任务分配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '结果是由艾丝蒂尔、金、奥利维尔、科洛丝\n',
            '去两国的大使馆和格兰赛尔城堡、利贝尔通讯社……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特一个人去调查\n',
            '去调查其他的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_7381')

    def _loc_729C(): pass

    label('loc_729C')

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '送走希德中校之后\n',
            '艾丝蒂尔她们讨论了调查方法和任务分配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '结果是由艾丝蒂尔、金、奥利维尔、科洛丝\n',
            '去两国的大使馆和格兰赛尔城堡、利贝尔通讯社……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德一个人去调查\n',
            '去调查其他的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_7381(): pass

    label('loc_7381')

    ChrClearFlags(0x012F, 0x0080)
    ChrClearFlags(0x0107, 0x0080)
    ChrSetPos(0x0101, -570, 0, 970, 90)
    ChrSetPos(0x00F7, -940, 0, -70, 90)
    ChrSetPos(0x0104, -2280, 0, 810, 90)
    ChrSetPos(0x0108, -2280, 0, 1980, 90)
    ChrSetPos(0x0105, -1080, 0, 2040, 90)
    ChrSetPos(0x0107, 1570, 0, 170, 270)
    ChrSetPos(0x012F, 1710, 0, 1240, 270)
    ChrSetRGBAMask(0x012F, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0107, 255, 255, 255, 255, 0)
    CameraMove(-160, 0, 1660, 0)
    OP_67(0, 7450, -10000, 0)
    CameraSetDistance(2770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010250290V#1006F#5P那我们就\n',
            '先出去一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250291V提妲、玲。\n',
            '抱歉，你们就呆在家里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250292V#265F#4P关于这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250293V#261F玲准备和提妲\n',
            '一起去购物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250294V#1004F#5P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250295V#560F对、对不起，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250296V小玲非常想去\n',
            '百货商店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250297V#264F#2P哎呀，真出人意料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250298V#263F提妲你不是也说\n',
            '想看看布偶吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250299V#067F啊……\n',
            '小玲你真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250300V#1025F#5P唔、唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250301V不知道什么时候会得到\n',
            '小玲爸爸妈妈的消息，\n',
            '我本来是希望你等在这里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250302V#267F#4P盯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250303V#063F盯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250304V#1019F#5P唔……\n',
            '两个人联合起来这么看着我真狡猾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_776D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250305V#051F#5P没什么关系吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250306V有提妲跟着，\n',
            '买买东西应该没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77C4')

    def _loc_776D(): pass

    label('loc_776D')

    ChrTalk(
        0x0103,
        (
            '#0030250307V#021F#5P没什么关系吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250308V有提妲跟着，\n',
            '买买东西应该没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_77C4(): pass

    label('loc_77C4')

    ChrTalk(
        0x0101,
        (
            '#0010250309V#1007F#5P嗯……也对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250310V#1006F提妲、小玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250311V我们傍晚会回来的，\n',
            '你们可要在此之前回来哦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250312V而且王都很大，\n',
            '可别迷路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250313V#061F嗯，你就放心吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x012F, 400)

    ChrTalk(
        0x0107,
        (
            '#0070250314V#560F那么小玲，\n',
            '我们出发吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0107, 400)

    ChrTalk(
        0x012F,
        (
            '#0220250315V#265F#2P嗯，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0101, 400)

    ChrTalk(
        0x012F,
        (
            '#0220250316V#261F#4P姐姐，一会儿见⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_792D')
    def lambda_792D():
        CameraMove(-230, 0, -3670, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_792D)

    CreateThread(0x0107, 0x01, 0x00, func_12_8508)
    Sleep(500)

    @scena.Lambda('lambda_7951')
    def lambda_7951():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_7951')

    DispatchAsync2(0x0101, 0x0001, lambda_7951)

    @scena.Lambda('lambda_7962')
    def lambda_7962():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_7962')

    DispatchAsync2(0x0008, 0x0001, lambda_7962)

    @scena.Lambda('lambda_7973')
    def lambda_7973():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_7973')

    DispatchAsync2(0x00F7, 0x0001, lambda_7973)

    @scena.Lambda('lambda_7984')
    def lambda_7984():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_7984')

    DispatchAsync2(0x0108, 0x0001, lambda_7984)

    @scena.Lambda('lambda_7995')
    def lambda_7995():
        ChrTurnDirection(0x00FE, 0x012F, 0)
        Yield()

        Jump('lambda_7995')

    DispatchAsync2(0x0104, 0x0001, lambda_7995)

    @scena.Lambda('lambda_79A6')
    def lambda_79A6():
        ChrTurnDirection(0x00FE, 0x012F, 0)
        Yield()

        Jump('lambda_79A6')

    DispatchAsync2(0x0105, 0x0001, lambda_79A6)

    Sleep(200)

    CreateThread(0x012F, 0x01, 0x00, func_13_8559)
    WaitForThreadExit(0x012F, 0x0001)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0108, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0008, 0x01)
    Sleep(500)

    CameraMove(-2590, 0, 1610, 2000)

    ChrTalk(
        0x0105,
        (
            '#0060250317V#048F#2P呵呵，她们很快\n',
            '就交上朋友了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250318V#1016F#5P嗯，果然是\n',
            '同龄人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250319V#1015F不过，小玲和\n',
            '提妲的组合啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250320V有种说不清的不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060250321V#044F#2P咦？为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250322V#1025F#6P不是，你想……\n',
            '提妲不善于推辞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250323V你不觉得她会被小玲\n',
            '使唤得团团转吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250324V#045F#2P确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0008, 400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BD2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250325V#050F#6P对了，艾南。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250326V你问出那孩子\n',
            '父母的名字了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C23')

    def _loc_7BD2(): pass

    label('loc_7BD2')

    ChrTalk(
        0x0103,
        (
            '#0030250327V#020F#6P对了，艾南。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250328V你问出那孩子\n',
            '父母的名字了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C23(): pass

    label('loc_7C23')

    @scena.Lambda('lambda_7C29')
    def lambda_7C29():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7C29)

    Sleep(50)

    @scena.Lambda('lambda_7C3C')
    def lambda_7C3C():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_7C3C)

    Sleep(50)

    @scena.Lambda('lambda_7C4F')
    def lambda_7C4F():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_7C4F)

    Sleep(50)

    @scena.Lambda('lambda_7C62')
    def lambda_7C62():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_7C62)

    Sleep(50)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0590250329V#764F嗯，好不容易。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250330V#762F看来他们夫妇是\n',
            '住在克洛斯贝尔自治州的贸易商。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250331V名字是哈罗德·海瓦斯，\n',
            '以及索菲亚·海瓦茨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250332V#1015F克洛斯贝尔自治州的贸易商，\n',
            '哈罗德和索菲亚夫妇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250333V#1006F嗯，我已经记下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DEE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050250334V#051F我这边也好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250335V结合恐吓信的调查，\n',
            '我们开始询问情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E48')

    def _loc_7DEE(): pass

    label('loc_7DEE')

    ChrTalk(
        0x0103,
        (
            '#0030250336V#021F我这边也好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250337V结合恐吓信的调查，\n',
            '我们开始询问情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E48(): pass

    label('loc_7E48')

    ChrTalk(
        0x0008,
        (
            '#0590250338V#760F按之前说好的，请艾丝蒂尔小姐\n',
            '去帝国、共和国大使馆和格兰赛尔城和\n',
            '利贝尔通讯社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250339V关于各大使馆，就拜托金先生和\n',
            '奥利维尔先生帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040250340V#035F#6P嘿～交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250341V#070F就是说向大使们\n',
            '做引见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250342V#760F关于格兰赛尔城堡，\n',
            '就拜托殿下您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250343V请把艾丝蒂尔小姐引见\n',
            '给合适的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250344V#040F嗯，我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590250345V#761F利贝尔通讯方面自不必说，\n',
            '艾丝蒂尔小姐自己是最合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250346V#1006F嗯，我会去问奈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_80E6',
    )

    ChrTalk(
        0x0008,
        (
            '#0590250347V#760F剩下的是大圣堂、飞船公社和\n',
            '罗恩鲍姆酒店……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250348V都交给阿加特\n',
            '来调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050250349V#051F啊啊。\n',
            '这样比较有效率。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_817D')

    def _loc_80E6(): pass

    label('loc_80E6')

    ChrTalk(
        0x0008,
        (
            '#0590250347V#760F剩下的是大圣堂、飞船公社和\n',
            '罗恩鲍姆酒店……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590250351V都交给雪拉扎德小姐\n',
            '来调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030250352V#020F嗯。\n',
            '这样比较有效率。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_817D(): pass

    label('loc_817D')

    ChrTalk(
        0x0101,
        (
            '#0010250353V#1018F好，开工！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4100._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x81B7
@scena.Code('func_09_81B7')
def func_09_81B7():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -320, -500, -7250, 0)

    @scena.Lambda('lambda_81DE')
    def lambda_81DE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_81DE)

    ChrWalkTo(0x00FE, -790, -250, -4780, 2000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x000A offset: 0x8206
@scena.Code('func_0A_8206')
def func_0A_8206():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 90, -500, -7250, 0)

    @scena.Lambda('lambda_822D')
    def lambda_822D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_822D)

    ChrWalkTo(0x00FE, 320, -500, -7080, 2000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x000B offset: 0x8255
@scena.Code('func_0B_8255')
def func_0B_8255():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 560, -500, -7230, 0)

    @scena.Lambda('lambda_827C')
    def lambda_827C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_827C)

    ChrWalkTo(0x00FE, 440, -250, -4970, 2000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x000C offset: 0x82A4
@scena.Code('func_0C_82A4')
def func_0C_82A4():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -320, -500, -7250, 0)

    @scena.Lambda('lambda_82CB')
    def lambda_82CB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_82CB)

    ChrWalkTo(0x00FE, -460, -250, -6180, 2000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x000D offset: 0x82F3
@scena.Code('func_0D_82F3')
def func_0D_82F3():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 560, -500, -7230, 0)

    @scena.Lambda('lambda_831A')
    def lambda_831A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_831A)

    ChrWalkTo(0x00FE, 720, -250, -6180, 2000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x000E offset: 0x8342
@scena.Code('func_0E_8342')
def func_0E_8342():
    ChrSetDirection(0x00FE, 180, 500)
    ChrWalkTo(0x00FE, -2360, 0, -2490, 2500, 0x00)
    ChrWalkTo(0x00FE, 990, 0, -2530, 2500, 0x00)
    ChrWalkTo(0x00FE, 3450, 0, -280, 2500, 0x00)
    ChrWalkTo(0x00FE, 3600, 0, 4790, 2500, 0x00)
    ChrWalkTo(0x00FE, -4210, 4000, 5170, 2500, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000F offset: 0x83BE
@scena.Code('func_0F_83BE')
def func_0F_83BE():
    @scena.Lambda('lambda_83C4')
    def lambda_83C4():
        ChrTurnDirection(0x00FE, 0x0107, 500)
        Yield()

        Jump('lambda_83C4')

    DispatchAsync2(0x012F, 0x0002, lambda_83C4)

    Sleep(2300)

    TerminateThread(0x012F, 0x02)
    ChrWalkTo(0x00FE, 990, 0, -2530, 2500, 0x00)
    ChrWalkTo(0x00FE, 3450, 0, -280, 2500, 0x00)
    ChrWalkTo(0x00FE, 3600, 0, 4790, 2500, 0x00)
    ChrWalkTo(0x00FE, -4210, 4000, 5170, 2500, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0010 offset: 0x8439
@scena.Code('func_10_8439')
def func_10_8439():
    ChrSetDirection(0x00FE, 90, 500)
    ChrWalkTo(0x00FE, 1470, 0, -30, 2500, 0x00)
    ChrWalkTo(0x00FE, 3580, 0, 1800, 2500, 0x00)
    ChrWalkTo(0x00FE, 3630, 0, 4920, 2500, 0x00)
    ChrWalkTo(0x00FE, -4210, 4000, 5170, 2500, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0011 offset: 0x84A1
@scena.Code('func_11_84A1')
def func_11_84A1():
    @scena.Lambda('lambda_84A7')
    def lambda_84A7():
        ChrTurnDirection(0x00FE, 0x0107, 500)
        Yield()

        Jump('lambda_84A7')

    DispatchAsync2(0x012F, 0x0002, lambda_84A7)

    Sleep(800)

    TerminateThread(0x012F, 0x02)
    ChrWalkTo(0x00FE, 3580, 0, 1800, 2500, 0x00)
    ChrWalkTo(0x00FE, 3600, 0, 4790, 2500, 0x00)
    ChrWalkTo(0x00FE, -4210, 4000, 5170, 2500, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x8508
@scena.Code('func_12_8508')
def func_12_8508():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 630, -250, -6450, 2000, 0x00)
    PlaySE(6, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_8533')
    def lambda_8533():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8533)

    ChrWalkTo(0x00FE, 480, -500, -7250, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0013 offset: 0x8559
@scena.Code('func_13_8559')
def func_13_8559():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 630, -250, -6450, 2000, 0x00)

    @scena.Lambda('lambda_857A')
    def lambda_857A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_857A)

    ChrWalkTo(0x00FE, 480, -500, -7250, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    Sleep(300)

    PlaySE(7, 0x00, 0x64)

    Return()

# id: 0x0014 offset: 0x85AA
@scena.Code('func_14_85AA')
def func_14_85AA():
    ChrWalkTo(0x00FE, -180, 0, 1640, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0015 offset: 0x85C6
@scena.Code('func_15_85C6')
def func_15_85C6():
    ChrWalkTo(0x00FE, -400, 0, 560, 2000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0016 offset: 0x85E2
@scena.Code('func_16_85E2')
def func_16_85E2():
    ChrWalkTo(0x00FE, -180, 0, 1640, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0017 offset: 0x85FE
@scena.Code('func_17_85FE')
def func_17_85FE():
    ChrWalkTo(0x00FE, -400, 0, 560, 2000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0018 offset: 0x861A
@scena.Code('func_18_861A')
def func_18_861A():
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
        'loc_863D',
    )

    Call(0, 0x0026)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    def _loc_863D(): pass

    label('loc_863D')

    MapClearFlags(0x00000001)
    CameraMove(-40, -250, -5780, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    ChrSetFlags(0x0108, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_86B3',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -1780, 0, 1670, 270)

    Jump('loc_86C9')

    def _loc_86B3(): pass

    label('loc_86B3')

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -1780, 0, 1670, 270)

    def _loc_86C9(): pass

    label('loc_86C9')

    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x00, 0x00, func_19_A93D)
    Sleep(400)

    CreateThread(0x0105, 0x00, 0x00, func_1A_A985)
    Sleep(400)

    CreateThread(0x0108, 0x00, 0x00, func_1C_AA15)
    Sleep(400)

    CreateThread(0x0104, 0x00, 0x00, func_1B_A9CD)
    OP_0D()
    WaitForThreadExit(0x0104, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010251362V#1011F#5P我们回来了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_874E',
    )

    @scena.Lambda('lambda_8743')
    def lambda_8743():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_8743)

    Jump('loc_875C')

    def _loc_874E(): pass

    label('loc_874E')

    @scena.Lambda('lambda_8754')
    def lambda_8754():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_8754)

    def _loc_875C(): pass

    label('loc_875C')

    @scena.Lambda('lambda_8762')
    def lambda_8762():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8762)

    @scena.Lambda('lambda_8770')
    def lambda_8770():
        CameraMove(-2910, 0, 830, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8770)

    @scena.Lambda('lambda_8788')
    def lambda_8788():
        OP_67(0, 6310, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8788)

    @scena.Lambda('lambda_87A0')
    def lambda_87A0():
        CameraSetDistance(2900, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_87A0)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_87EC',
    )

    ChrTalk(
        0x000A,
        (
            '#0050251363V#051F#2P哟，\n',
            '回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8814')

    def _loc_87EC(): pass

    label('loc_87EC')

    ChrTalk(
        0x0009,
        (
            '#0030251364V#021F#2P哟，回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8814(): pass

    label('loc_8814')

    @scena.Lambda('lambda_881A')
    def lambda_881A():
        ChrWalkTo(0x00FE, -1920, 0, 60, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_881A)

    Sleep(200)

    @scena.Lambda('lambda_883A')
    def lambda_883A():
        ChrWalkTo(0x00FE, -540, 0, -1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_883A)

    Sleep(500)

    @scena.Lambda('lambda_885A')
    def lambda_885A():
        ChrWalkTo(0x00FE, -2570, 0, -970, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_885A)

    Sleep(500)

    @scena.Lambda('lambda_887A')
    def lambda_887A():
        ChrWalkTo(0x00FE, -1500, 0, -1410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_887A)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251365V#1016F抱歉抱歉。\n',
            '稍微晚了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251366V#1011F嗯……\n',
            '提妲和小玲呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590251367V#761F#5P刚才已经\n',
            '回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251368V现在在楼上互相展示\n',
            '购物的战果呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251369V#1016F这样啊。\n',
            '看来她们玩得挺高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251370V#1006F那么，现在\n',
            '我们也报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590251371V#760F#5P嗯。\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetDirection(0x0101, 0, 400)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8BD4',
    )

    ChrTalk(
        0x000A,
        (
            '#0050251372V#051F#2P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251373V你们也搜集到\n',
            '不少信息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251374V#1007F不过也还是没掌握什么\n',
            '决定性的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251375V#1015F阿加特你怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251376V#053F#2P老实说，哪边都没收获。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251377V大圣堂、酒店、飞船公社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251378V都对寄来恐吓信的\n',
            '罪犯没什么线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251379V#050F飞船公社虽然做好了\n',
            '像上次空贼事件一样\n',
            '接下来会受到金钱敲诈的准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251380V不过现在还没有那种要求出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D88')

    def _loc_8BD4(): pass

    label('loc_8BD4')

    ChrTalk(
        0x0009,
        (
            '#0030251381V#027F#2P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251382V你们也搜集到\n',
            '不少信息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251374V#1007F不过也还是没掌握什么\n',
            '决定性的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251384V#1015F雪拉姐你怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251385V#025F#2P老实说，哪边都没收获。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251386V大圣堂、酒店、飞船公社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251387V都对寄来恐吓信的\n',
            '罪犯没什么线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251388V#022F飞船公社虽然做好了\n',
            '像上次空贼事件一样\n',
            '接下来会受到金钱敲诈的准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251389V不过现在还没有那种要求出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D88(): pass

    label('loc_8D88')

    ChrTalk(
        0x0101,
        (
            '#0010251390V#1007F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251391V#1002F到头来，罪犯的人选\n',
            '还是有很多种可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251392V是『结社』所为的\n',
            '可能性有多少？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590251393V#764F#5P……很难说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251394V#762F根据迄今为止的案件来看，\n',
            '他们现在除了『福音』的\n',
            '实验以外没什么动作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251395V并且已知『福音』会引发\n',
            '一般情况下不会发生的\n',
            '现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251396V#032F#6P呼，从这一点上来看，\n',
            '这次的恐吓事件确实有所不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251397V#072F现在还看不出和结社\n',
            '有关的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251398V#1015F嗯……\n',
            '是不是有点草木皆兵了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590251399V#764F#5P不，谨慎小心\n',
            '是没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251400V#760F总之我们现在已经把\n',
            '该做的调查都做了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251401V我会整理好\n',
            '各位的报告的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251402V明天可以请你们送去艾尔贝离宫\n',
            '给希德中校吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_96D0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010251403V#1025F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251404V到头来还是没查出罪犯的身份，\n',
            '虽然感觉很抱歉，不过也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251405V#1004F对了，阿加特。\n',
            '小玲的事怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251406V#050F#2P那个倒是搞清楚一些事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251407V首先是酒店……\n',
            '那孩子和父母只在王都\n',
            '呆了两个星期。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251408V那段时间都一直\n',
            '住在酒店的同一个房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251409V然后终于在今早\n',
            '办理了退房手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251410V#1002F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251411V#555F#2P接下来是大圣堂……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251412V他们在逗留期间好几次\n',
            '去大圣堂做了礼拜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251413V而招待他们的牧师觉得\n',
            '夫妇二人的样子有点古怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251414V说是礼拜时好像心不在焉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251415V#043F和希尔丹夫人的说法一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251416V#1015F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251417V#053F#2P最后是飞船公社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251418V#552F……实际上。\n',
            '没找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251419V#1004F咦……什么没找到？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251420V#555F#2P克洛斯贝尔出身的\n',
            '海伍兹夫妇和玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251421V在半年时间内的乘客名单上\n',
            '都没有相符的记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251422V#1020F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251423V#032F#6P呼……真神秘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251424V那么他们是不是通过\n',
            '地面交通来的利贝尔？',
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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '玲是通过地面交通来的利贝尔？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【嗯、嗯……】\n'),
            TXT(0x01, '【这不可能】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_950C'),
        (0x00000001, 'loc_95FE'),
        (-1, 'loc_96CD'),
    )

    def _loc_950C(): pass

    label('loc_950C')

    ChrTalk(
        0x0101,
        (
            '#0010191526V#1015F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251426V那要不要直接\n',
            '问问玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251427V#552F#2P不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251428V第一次在艾尔·雷登\n',
            '遇见她时她不是说了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251429V乘飞船到达的时候\n',
            '看见了很大的湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251430V#1002F啊，确实如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96CD')

    def _loc_95FE(): pass

    label('loc_95FE')

    OP_2B(0x0089, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010251431V#1020F这、这不可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251432V因为第一次遇见她的时候，\n',
            '我记得她说过\n',
            '乘飞船到达什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251433V#552F#2P嗯，是在艾尔·雷登吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251434V我记得她说过\n',
            '看见了很大的湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_96CD')

    def _loc_96CD(): pass

    label('loc_96CD')

    Jump('loc_9D75')

    def _loc_96D0(): pass

    label('loc_96D0')

    ChrTalk(
        0x0101,
        (
            '#0010251403V#1025F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251404V到头来还是没查出罪犯的身份，\n',
            '虽然感觉很抱歉，不过也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251437V#1004F对了，雪拉姐。\n',
            '小玲的事怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251438V#020F#2P那个倒是\n',
            '搞清楚一些事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251439V首先是酒店……\n',
            '那孩子和父母在王都\n',
            '呆了两星期左右。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251440V那段时间都一直\n',
            '都住在同一间房间里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251441V然后终于今天早上\n',
            '办理了退房手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251410V#1002F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251443V#022F#2P接下来是大圣堂……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251444V他们在逗留期间好几次\n',
            '去大圣堂做了礼拜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251445V那么……\n',
            '根据接待他们的牧师所说，\n',
            '夫妇的样子有点古怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251446V好象礼拜时心不在焉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251415V#043F和希尔丹夫人的说法一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251416V#1015F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251449V#522F#2P最后是飞船公社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251450V调查完乘客名单\n',
            '发现了一件奇怪的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251451V#1004F咦……奇怪的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251452V#026F#2P克洛斯贝尔出身的\n',
            '海伍兹夫妇和玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251453V#022F在半年时间内的乘客名单上\n',
            '都没有相符的记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251454V#1020F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251423V#032F#6P呼……真神秘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251424V那么他们是不是通过\n',
            '地面交通来的利贝尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '玲是通过地面交通来的利贝尔？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【嗯、嗯……】\n'),
            TXT(0x01, '【这不可能】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9BA4'),
        (0x00000001, 'loc_9CA0'),
        (-1, 'loc_9D75'),
    )

    def _loc_9BA4(): pass

    label('loc_9BA4')

    ChrTalk(
        0x0101,
        (
            '#0010191526V#1015F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251426V那要不要直接\n',
            '问问玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251459V#522F#2P我说，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251460V第一次在艾尔·雷登\n',
            '遇见她时她不是说了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251461V乘飞船到达的时候\n',
            '看见了很大的湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251430V#1002F啊，确实如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D75')

    def _loc_9CA0(): pass

    label('loc_9CA0')

    OP_2B(0x0089, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010251431V#1020F这、这不可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251432V因为第一次遇见她的时候，\n',
            '我记得她说过\n',
            '乘飞船到达什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251465V#022F#2P是那次在艾尔·雷登的时候吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251466V我记得她说过\n',
            '看见了很大的湖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D75')

    def _loc_9D75(): pass

    label('loc_9D75')

    ChrTalk(
        0x0008,
        (
            '#0590251467V#764F#5P嗯，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251468V#762F那么他们夫妇有可能\n',
            '是用了假名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251469V#1020F假、假名……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251470V#072F可能有什么事不便示人\n',
            '或者害怕引来麻烦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251471V无论如何，他们似乎\n',
            '在出行前就预测到危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251472V#1003F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590251473V#764F#5P关于玲小姐父母的事，\n',
            '我已经联络了各地的协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251474V现在还是先别着急，\n',
            '等着消息比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251475V#760F总之玲小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251476V还是暂时让他住在\n',
            '协会比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251477V#1007F嗯……毕竟她也有\n',
            '被卷入麻烦的危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251478V#1006F那个，方便的话就\n',
            '交给我吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251479V毕竟这也是我接下的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590251480V#761F#5P你能这么说真是帮了我大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251481V各位在王都期间的住宿\n',
            '就由协会负责安排。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590251482V玲小姐的住宿费用\n',
            '也由我们出，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251483V#1016F真是太谢谢你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251484V#1004F啊，说起来的话，\n',
            '希尔丹夫人说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A309',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔对阿加特\n',
            '说了希尔丹夫人邀请他们\n',
            '住在王城的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590251485V#763F#5P哟，还有这种事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050251486V#053F#2P……我就算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251487V#050F住了那么多次，\n',
            '感觉还是太拘谨了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251488V住酒店的话，万一有什么事\n',
            '也方便联络协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251489V#1015F确实也有道理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251490V没准玲的父母还会\n',
            '联系我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251491V#1025F#5P科洛丝。\n',
            '不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060251492V#048F呵呵，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251493V我会去跟\n',
            '希尔丹夫人解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A515')

    def _loc_A309(): pass

    label('loc_A309')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔对雪拉扎德\n',
            '说了希尔丹夫人邀请他们\n',
            '住在王城的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0590251485V#763F#5P哟，还有这种事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030251495V#025F#2P唔，说实话这是个\n',
            '令人感激的提议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251496V#020F不过这次\n',
            '就算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251497V万一有什么事，住酒店的话\n',
            '也方便联络协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251489V#1015F确实也有道理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251490V没准玲的父母还会\n',
            '联系我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251491V#1025F#5P科洛丝。\n',
            '不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060251492V#048F呵呵，不用介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251493V我会去跟\n',
            '希尔丹夫人解释。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A515(): pass

    label('loc_A515')

    ChrTalk(
        0x0104,
        (
            '#0040251503V#030F#6P我和金先生\n',
            '住在各自的大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251504V公主殿下则住在格兰赛尔城城堡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251505V你们两个和童子军\n',
            '是准备要住酒店。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251506V#031F在此之前，怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251507V难得一聚，要不要一起\n',
            '去酒馆吃个饭？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    @scena.Lambda('lambda_A60A')
    def lambda_A60A():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_A60A)

    @scena.Lambda('lambda_A618')
    def lambda_A618():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_A618)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010251508V#1006F#2P啊，好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251509V也好久没听\n',
            '奥利维尔弹钢琴了。',
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
            '#0040251510V#035F#6P呵呵，荣幸之至\n',
            '让我高兴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251511V#037F艾丝蒂尔你也终于\n',
            '能品味成年人的情趣了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251512V#1019F#2P别说这种\n',
            '不正经的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251513V#070F#5P不过这样的话，\n',
            '我们就立即动身吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251514V这么一大群人，\n',
            '也有可能找不到座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A7E2',
    )

    ChrTalk(
        0x000A,
        (
            '#0050251515V#051F好，叫上小家伙们，\n',
            '赶紧出发去酒店吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A81E')

    def _loc_A7E2(): pass

    label('loc_A7E2')

    ChrTalk(
        0x0009,
        (
            '#0030251516V#021F呵呵，叫上那两个孩子，\n',
            '一起去酒店吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A81E(): pass

    label('loc_A81E')

    FadeOut(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当晚，艾丝蒂尔一行人和玲一起\n',
            '在『阳光铃铛酒廊』吃了晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当然，也伴随着畅饮和\n',
            '奥利维尔的钢琴演奏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '最后连奈尔和穆拉都被\n',
            '叫来酒馆参与到其中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '王都的傍晚就这样快乐地过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x04, 0xFF)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A92C',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_A930')

    def _loc_A92C(): pass

    label('loc_A92C')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_A930(): pass

    label('loc_A930')

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4153._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0xA93D
@scena.Code('func_19_A93D')
def func_19_A93D():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -150, -500, -7230, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A964')
    def lambda_A964():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A964)

    ChrWalkTo(0x00FE, -290, -250, -4990, 2000, 0x00)

    Return()

# id: 0x001A offset: 0xA985
@scena.Code('func_1A_A985')
def func_1A_A985():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 590, -500, -7250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A9AC')
    def lambda_A9AC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A9AC)

    ChrWalkTo(0x00FE, 910, -250, -5900, 2000, 0x00)

    Return()

# id: 0x001B offset: 0xA9CD
@scena.Code('func_1B_A9CD')
def func_1B_A9CD():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 190, -500, -7250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A9F4')
    def lambda_A9F4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A9F4)

    ChrWalkTo(0x00FE, -50, -250, -6250, 2000, 0x00)

    Return()

# id: 0x001C offset: 0xAA15
@scena.Code('func_1C_AA15')
def func_1C_AA15():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -870, -500, -7250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_AA3C')
    def lambda_AA3C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_AA3C)

    ChrWalkTo(0x00FE, -990, -250, -6010, 2000, 0x00)

    Return()

# id: 0x001D offset: 0xAA5D
@scena.Code('func_1D_AA5D')
def func_1D_AA5D():
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
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AA82',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_AA82(): pass

    label('loc_AA82')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AAAC',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA9E',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    Jump('loc_AAA2')

    def _loc_AA9E(): pass

    label('loc_AA9E')

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    def _loc_AAA2(): pass

    label('loc_AAA2')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_AAAC(): pass

    label('loc_AAAC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AAD6',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AAC8',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    Jump('loc_AACC')

    def _loc_AAC8(): pass

    label('loc_AAC8')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    def _loc_AACC(): pass

    label('loc_AACC')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_AAD6(): pass

    label('loc_AAD6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AAF1',
    )

    FormationAddMember(ChrTable['金'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_AAF1(): pass

    label('loc_AAF1')

    Return()

# id: 0x001E offset: 0xAAF2
@scena.Code('func_1E_AAF2')
def func_1E_AAF2():
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
        'loc_AB17',
    )

    Call(0, 0x0026)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_AB13',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_AB17')

    def _loc_AB13(): pass

    label('loc_AB13')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_AB17(): pass

    label('loc_AB17')

    OP_4A(0x000C, 255)
    OP_4A(0x0008, 255)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0101, 90, -500, -7250, 0)
    ChrSetPos(0x00F7, 90, -500, -7250, 0)
    ChrSetPos(0x0107, 90, -500, -7250, 0)
    ChrSetPos(0x012F, 90, -500, -7250, 0)
    ChrSetPos(0x000C, -2130, 0, -50, 270)
    ChrSetPos(0x000E, -2170, 0, 1060, 270)
    CameraMove(-4300, 0, 1620, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260497V#2P我们回来了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 180, 400)
    ChrSetDirection(0x0008, 135, 400)
    ChrSetDirection(0x000E, 180, 400)

    @scena.Lambda('lambda_AC14')
    def lambda_AC14():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_AC14')

    DispatchAsync2(0x0008, 0x0001, lambda_AC14)

    ChrTalk(
        0x000E,
        (
            '#0080260498V#070F#2P哟，回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060260499V#041F#5P各位，欢迎回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_AC77')
    def lambda_AC77():
        CameraMove(-3840, 0, 950, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_AC77)

    @scena.Lambda('lambda_AC8F')
    def lambda_AC8F():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_AC8F)

    CreateThread(0x0101, 0x00, 0x00, func_1F_C0ED)
    Sleep(600)

    ChrSetDirection(0x000E, 90, 400)

    @scena.Lambda('lambda_ACBA')
    def lambda_ACBA():
        ChrWalkTo(0x00FE, -1730, 0, 1530, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_ACBA)

    Sleep(200)

    ChrSetDirection(0x000C, 90, 400)

    @scena.Lambda('lambda_ACE1')
    def lambda_ACE1():
        ChrWalkTo(0x00FE, -1290, 0, 560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_ACE1)

    WaitForThreadExit(0x000E, 0x0000)

    @scena.Lambda('lambda_AD01')
    def lambda_AD01():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_AD01')

    DispatchAsync2(0x000E, 0x0001, lambda_AD01)

    CreateThread(0x00F7, 0x01, 0x00, func_20_C109)
    Sleep(400)

    WaitForThreadExit(0x000C, 0x0000)

    @scena.Lambda('lambda_AD23')
    def lambda_AD23():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_AD23')

    DispatchAsync2(0x000C, 0x0001, lambda_AD23)

    CreateThread(0x0107, 0x01, 0x00, func_21_C125)
    Sleep(600)

    CreateThread(0x012F, 0x01, 0x00, func_22_C141)
    WaitForThreadExit(0x012F, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0008, 0x01)
    ChrSetDirection(0x000C, 270, 400)
    ChrSetDirection(0x000E, 270, 400)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0590260500V#760F#5P辛苦了。\n',
            '报告书已经交了吧、',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260501V#1000F嗯，那个搞定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260502V#760F#5P刚才王国军汇来了\n',
            '报酬。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260503V你们赶紧\n',
            '拿好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008B, 0x04, 0x10)
    OP_AF(0xCD, 0x008B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010260504V#1001F#4P不愧是希德中校。\n',
            '工作真有效率。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260505V#1015F不过……\n',
            '我听说柏斯地区\n',
            '出现了特务兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260506V#762F#5P离宫那边也收到\n',
            '消息了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260507V我正准备和你们\n',
            '谈谈这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B325',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260508V#050F#6P是协会的人\n',
            '发现的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260509V#764F#5P嗯……\n',
            '是雪拉扎德小姐她们。',
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
            '#0010260510V#1004F#4P雪拉姐她们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260511V#762F#5P说是在拉文努的废坑\n',
            '内部发现了他们的基地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260512V不巧的是他们\n',
            '已经离开了那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260513V#1002F#4P拉文努废坑的内部……\n',
            '和空贼战斗过的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260514V#555F#6P切，真是个盲点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260515V离开了就意味着\n',
            '转去别的地方了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260516V#765F#5P关于这点，据说在柏斯\n',
            '各地都有人目击到特务兵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260517V现在，国境师团正在倾巢\n',
            '出动进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260518V#1015F#4P这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260519V我们是不是也该去\n',
            '柏斯帮忙呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260520V#762F#5P不，敌人有可能是声东击西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260521V在了解当地情况之前\n',
            '还是不要擅自行动为好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260522V而且看来……\n',
            '『结社』也有动向了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260523V#1020F#4P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260524V#054F#6P你说什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260525V#764F#5P雪拉扎德小姐她们\n',
            '在废坑碰见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260526V#762F『小丑』肯帕雷拉──\n',
            '似乎是『执行者』中的一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050260527V#555F#6P呼，又是一张新面孔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B716')

    def _loc_B325(): pass

    label('loc_B325')

    ChrTalk(
        0x0103,
        (
            '#0030260528V#020F#6P是协会的人\n',
            '发现的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260529V#764F#5P嗯……\n',
            '是阿加特他们。',
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
            '#0010260530V#1004F#4P阿加特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260511V#762F#5P说是在拉文努的废坑\n',
            '内部发现了他们的基地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260512V不巧的是他们\n',
            '已经离开了那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260513V#1002F#4P拉文努废坑的内部……\n',
            '是和空贼战斗过的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260534V#026F#6P原来如此，果然是个盲点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260535V#022F离开了就意味着\n',
            '转去别的地方了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260516V#765F#5P关于这点，据说在柏斯\n',
            '各地都有人目击到特务兵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260517V现在，国境师团正在倾巢\n',
            '出动进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260518V#1015F#4P这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260519V我们是不是也该去\n',
            '柏斯帮忙呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260540V#762F#5P不，在了解当地情况之前\n',
            '还是不要擅自行动为好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260522V而且看来……\n',
            '『结社』也有动向了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260523V#1020F#4P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260543V#024F#6P你说什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260544V#764F#5P阿加特他们\n',
            '在废坑碰见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260526V#762F『小丑』肯帕雷拉──\n',
            '似乎是『执行者』中的一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030260546V#022F#6P呼，又是一张新面孔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B716(): pass

    label('loc_B716')

    ChrTalk(
        0x0008,
        (
            '#0590260547V#762F#5P而且在那个基地还\n',
            '发现了奇怪的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260548V首先是名叫『奥尔杰尤』的\n',
            '导力驱动的交通工具的设计图……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260549V还有就是代号为『茶会』的\n',
            '神秘计划记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260550V#1015F#4P『奥尔杰尤』『茶会』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260551V#1007F唔，真不知所云。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260552V#065F#6P导力驱动的交通工具\n',
            '是什么呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060260553V#049F茶会这个说法\n',
            '令人比较在意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000E, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x00F7, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    CreateThread(0x012F, 0x01, 0x00, func_23_C15D)
    Sleep(2000)

    OP_63(0x0101)
    OP_63(0x0107)
    OP_63(0x000C)
    OP_63(0x000E)
    OP_63(0x0008)
    OP_63(0x00F7)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B958',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260554V#552F#6P切，真是不让人\n',
            '清净啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B989')

    def _loc_B958(): pass

    label('loc_B958')

    ChrTalk(
        0x0103,
        (
            '#0030260555V#025F#6P呼，真是不让人\n',
            '清净啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B989(): pass

    label('loc_B989')

    ChrSetDirection(0x000E, 180, 400)

    ChrTalk(
        0x000E,
        (
            '#0080260556V#070F#2P不过也别着急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080260557V因为当地的军队和\n',
            '协会都在努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080260558V很快就能了解到情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260559V#760F#5P嗯，虽然令人着急，\n',
            '不过还是请先留在王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260560V现在你们可以各自\n',
            '自由活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260561V#1007F#4P唔，虽然这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0101, 45, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 135, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260562V#1004F#4P咦？说起来\n',
            '奥利维尔去哪儿了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260563V#760F#5P关于他，帝国大使馆\n',
            '刚才联系了我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260564V他说有点私事，\n',
            '就出去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260565V还说很快会\n',
            '回到协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260566V#1015F#4P哦～？\n',
            '是什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_BBF0')
    def lambda_BBF0():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_BBF0)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010260567V#1004F#5P……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BC26')
    def lambda_BC26():
        CameraMove(-2510, 0, -500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BC26)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010260568V#1026F#5P玲呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260569V#064F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BC86')
    def lambda_BC86():
        ChrSetDirection(0x000C, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_BC86)

    @scena.Lambda('lambda_BC94')
    def lambda_BC94():
        ChrSetDirection(0x00F7, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_BC94)

    Sleep(100)

    @scena.Lambda('lambda_BCA7')
    def lambda_BCA7():
        ChrSetDirection(0x0008, 135, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_BCA7)

    @scena.Lambda('lambda_BCB5')
    def lambda_BCB5():
        ChrSetDirection(0x000E, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_BCB5)

    Sleep(100)

    CreateThread(0x0107, 0x01, 0x00, func_24_C183)
    ChrSetDirection(0x0107, 180, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 180, 300)
    TerminateThread(0x0107, 0x01)

    ChrTalk(
        0x0107,
        (
            '#0070260570V#065F#5P咦、咦咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260571V刚才\n',
            '还在的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BD33')
    def lambda_BD33():
        CameraMove(-3840, 0, 950, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BD33)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010260572V#1015F#5P难道是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260573V听我们说话太无聊\n',
            '就出去了？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    @scena.Lambda('lambda_BDA7')
    def lambda_BDA7():
        ChrSetDirection(0x0008, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_BDA7)

    @scena.Lambda('lambda_BDB5')
    def lambda_BDB5():
        ChrSetDirection(0x000C, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_BDB5)

    @scena.Lambda('lambda_BDC3')
    def lambda_BDC3():
        ChrSetDirection(0x0107, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_BDC3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BDF7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260574V#051F#6P有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE1F')

    def _loc_BDF7(): pass

    label('loc_BDF7')

    ChrTalk(
        0x0103,
        (
            '#0030260575V#524F#6P唔～很有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE1F(): pass

    label('loc_BE1F')

    ChrTalk(
        0x0101,
        (
            '#0010260576V#1007F#5P真是的～拿她没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260577V#1015F可她万一离开了王都\n',
            '也不能丢下她不管……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260578V#1006F#5P……我去找找\n',
            '那孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260579V#560F#6P啊，我也去！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070260580V我有可能知道\n',
            '小玲会去哪儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260581V#1006F#5P是吗？那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BF50')
    def lambda_BF50():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BF50)

    Sleep(50)

    @scena.Lambda('lambda_BF63')
    def lambda_BF63():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_BF63)

    ChrSetDirection(0x0107, 315, 400)
    ChrSetDirection(0x000E, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260582V#1015F#4P艾南先生。\n',
            '你看这事儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0590260583V#760F#5P嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0590260584V我去和各地支部\n',
            '就余党的去向\n',
            '交换一下信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FormationDelMember(0x2E, 0xFF)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-5650, 0, -18030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6E(262, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择固定队员外的一名同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    FadeIn(0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C0C6',
    )

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

    Jump('loc_C0D7')

    def _loc_C0C6(): pass

    label('loc_C0C6')

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

    def _loc_C0D7(): pass

    label('loc_C0D7')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T4100._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0xC0ED
@scena.Code('func_1F_C0ED')
def func_1F_C0ED():
    ChrWalkTo(0x00FE, -2560, 0, 500, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0020 offset: 0xC109
@scena.Code('func_20_C109')
def func_20_C109():
    ChrWalkTo(0x00FE, -1710, 0, -770, 2500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0021 offset: 0xC125
@scena.Code('func_21_C125')
def func_21_C125():
    ChrWalkTo(0x00FE, -2490, 0, -1610, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0022 offset: 0xC141
@scena.Code('func_22_C141')
def func_22_C141():
    ChrWalkTo(0x00FE, -1400, 0, -2290, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0023 offset: 0xC15D
@scena.Code('func_23_C15D')
def func_23_C15D():
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(300)

    ChrWalkTo(0x00FE, -80, -500, -7240, 2000, 0x00)
    ChrSetFlags(0x012F, 0x0080)

    Return()

# id: 0x0024 offset: 0xC183
@scena.Code('func_24_C183')
def func_24_C183():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C1A6',
    )

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    Jump('func_24_C183')

    def _loc_C1A6(): pass

    label('loc_C1A6')

    Return()

# id: 0x0025 offset: 0xC1A7
@scena.Code('func_25_C1A7')
def func_25_C1A7():
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
        'loc_C1C7',
    )

    Call(0, 0x0026)
    Call(0, 0x0028)
    FadeIn(0, 0)

    def _loc_C1C7(): pass

    label('loc_C1C7')

    Fade(1000)
    ChrSetPos(0x0101, 26120, 0, 58670, 270)
    ChrSetPos(0x0107, 26210, 0, 57560, 270)
    ChrSetPos(0x00F7, 27510, 0, 57390, 270)
    ChrSetPos(0x00F9, 27360, 0, 58520, 270)
    ChrSetDirection(0x0019, 180, 0)
    CameraMove(25020, 0, 58400, 0)
    OP_67(0, 5630, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260678V#1018F#6P没有颜色的鱼……\n',
            '是这个啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C2DD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260679V#051F#6P原来是鱼的拓本啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C309')

    def _loc_C2DD(): pass

    label('loc_C2DD')

    ChrTalk(
        0x0103,
        (
            '#0030260680V#021F#6P原来是鱼的拓本啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C309(): pass

    label('loc_C309')

    OP_4A(0x0019, 255)
    CameraMove(26740, 0, 61110, 1200)

    ChrTalk(
        0x0019,
        (
            '#2390260681V哟，你们对这副鱼的拓本\n',
            '感兴趣吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#2390260682V这是在下赢得\n',
            '闪耀的荣光之证啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#2390260683V方便的话，我可以给你们讲讲\n',
            '那个勇敢者的故事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C42D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_C46B')

    def _loc_C42D(): pass

    label('loc_C42D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C454',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_C46B')

    def _loc_C454(): pass

    label('loc_C454')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_C46B(): pass

    label('loc_C46B')

    Sleep(1000)

    @scena.Lambda('lambda_C476')
    def lambda_C476():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C476)

    Sleep(100)

    @scena.Lambda('lambda_C489')
    def lambda_C489():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_C489)

    Sleep(100)

    @scena.Lambda('lambda_C49C')
    def lambda_C49C():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_C49C)

    Sleep(100)

    @scena.Lambda('lambda_C4AF')
    def lambda_C4AF():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_C4AF)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010260684V#1016F#5P嗯，这还是\n',
            '留待下次吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260685V#1006F有没有一个穿着白色\n',
            '礼服的女孩子来过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#2390260686V哦，来过啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#2390260687V问了在下一个奇怪的问题，\n',
            '然后就走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260688V#1007F#5P果然是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260689V#065F#6P请问请问，\n',
            '那是个什么样的问题？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#2390260690V嗯，如果我没记错的话，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#2390260691V是『你知道又辣又苦又美味\n',
            '的店在哪里吗？』。',
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
        'loc_C682',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260692V#070F#6P真是谜团重重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C6AC')

    def _loc_C682(): pass

    label('loc_C682')

    ChrTalk(
        0x0105,
        (
            '#0060260693V#045F#6P真是谜团重重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C6AC(): pass

    label('loc_C6AC')

    ChrTalk(
        0x0101,
        (
            '#0010260694V#1006F#5P『又辣又苦又美味的店』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C6E5')
    def lambda_C6E5():
        CameraMove(26150, 0, 59560, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C6E5)

    ChrSetDirection(0x0101, 135, 400)
    ChrSetDirection(0x00F7, 315, 400)
    ChrSetDirection(0x00F9, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010260695V#1006F#5P那就去找找\n',
            '那家店吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C6, 2, 0x1632))
    OP_28(0x008C, 0x01, 0x0040)
    OP_4B(0x0019, 255)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0026 offset: 0xC75D
@scena.Code('func_26_C75D')
def func_26_C75D():
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
        (0x00000000, 'loc_C7D7'),
        (0x00000001, 'loc_C7DD'),
        (-1, 'loc_C7E3'),
    )

    def _loc_C7D7(): pass

    label('loc_C7D7')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_C7E3')

    def _loc_C7DD(): pass

    label('loc_C7DD')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_C7E3')

    def _loc_C7E3(): pass

    label('loc_C7E3')

    Return()

# id: 0x0027 offset: 0xC7E4
@scena.Code('func_27_C7E4')
def func_27_C7E4():
    MapClearFlags(0x00000001)
    CameraMove(-5650, 0, -18030, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C827',
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
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_C845')

    def _loc_C827(): pass

    label('loc_C827')

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
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_C845(): pass

    label('loc_C845')

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

# id: 0x0028 offset: 0xC865
@scena.Code('func_28_C865')
def func_28_C865():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C8A4',
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

    Jump('loc_C8BE')

    def _loc_C8A4(): pass

    label('loc_C8A4')

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

    def _loc_C8BE(): pass

    label('loc_C8BE')

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

# id: 0x0029 offset: 0xC8DE
@scena.Code('func_29_C8DE')
def func_29_C8DE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C8EF',
    )

    OP_2A(0x00BD, 0x00BE, 0xFFFF)

    Jump('loc_C93C')

    def _loc_C8EF(): pass

    label('loc_C8EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_C906',
    )

    OP_2A(0x00AA, 0x00AC, 0x00C4, 0x00AB, 0x00A9, 0xFFFF)

    Jump('loc_C93C')

    def _loc_C906(): pass

    label('loc_C906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_C91B',
    )

    OP_2A(0x00AA, 0x00AC, 0x00C4, 0x00AB, 0xFFFF)

    Jump('loc_C93C')

    def _loc_C91B(): pass

    label('loc_C91B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_C92E',
    )

    OP_2A(0x00AA, 0x00AC, 0x00C4, 0xFFFF)

    Jump('loc_C93C')

    def _loc_C92E(): pass

    label('loc_C92E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_C93C',
    )

    OP_2A(0x00AA, 0x00AC, 0xFFFF)

    def _loc_C93C(): pass

    label('loc_C93C')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
