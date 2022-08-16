import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2101.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH00472._CH', 'ED6_DT07/CH00472P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
    ]

# id: 0x10001 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '梅尔茨',
            x                   = 31640,
            z                   = 0,
            y                   = 10890,
            direction           = 180,
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
            name                = '哈尔德',
            x                   = 30790,
            z                   = 0,
            y                   = 9980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '昆茨',
            x                   = 54040,
            z                   = 0,
            y                   = 25560,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '布诺安',
            x                   = 19700,
            z                   = 0,
            y                   = 28620,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '哈古',
            x                   = 35750,
            z                   = 0,
            y                   = 25180,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '布兰塔婆婆',
            x                   = 75930,
            z                   = 0,
            y                   = 10740,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '贝尔夫',
            x                   = 41000,
            z                   = 1050,
            y                   = 21010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '洛克',
            x                   = 59750,
            z                   = 0,
            y                   = 6040,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '波尔多斯',
            x                   = 32140,
            z                   = 0,
            y                   = 6240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '加布',
            x                   = 51030,
            z                   = 0,
            y                   = 25340,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '皮卡罗',
            x                   = 27010,
            z                   = 0,
            y                   = 11360,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '汽油罐',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966088,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '汽油罐',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966088,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '汽油罐',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1966088,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '中年男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '穆拉德老人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '罗伊德',
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
            name                = '小船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00A0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿伊纳街道方向',
            x                   = 73210,
            z                   = 0,
            y                   = -16650,
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
            name                = '卢安市·北街区',
            x                   = 50980,
            z                   = 400,
            y                   = 77990,
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

# id: 0x10002 offset: 0x55A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x55A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 70000,
            y           = 0,
            z           = -2100,
            range       = 76500,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFFBB4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 17690,
            y           = 2000,
            z           = 7750,
            range       = 16040,
            dword_10    = 0xFFFFF8F8,
            dword_14    = 0x00001036,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 54040,
            y           = -1000,
            z           = 25560,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 35750,
            y           = -1000,
            z           = 25180,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 26200,
            y           = -2000,
            z           = 14000,
            range       = 31900,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00003E80,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 31200,
            y           = 0,
            z           = 25340,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 77280,
            y           = 0,
            z           = 22060,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000020,
        ),
    )

# id: 0x10004 offset: 0x63A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 50320,
            triggerZ            = 1000,
            triggerY            = 9400,
            triggerRange        = 800,
            actorX              = 50320,
            actorZ              = 2000,
            actorY              = 9400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31960,
            triggerZ            = 1000,
            triggerY            = 3430,
            triggerRange        = 800,
            actorX              = 31960,
            actorZ              = 2000,
            actorY              = 3430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23540,
            triggerZ            = 1000,
            triggerY            = 3430,
            triggerRange        = 800,
            actorX              = 23540,
            actorZ              = 2000,
            actorY              = 3430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 77600,
            triggerZ            = 0,
            triggerY            = 12330,
            triggerRange        = 800,
            actorX              = 77900,
            actorZ              = 1000,
            actorY              = 12330,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1270,
            triggerZ            = 0,
            triggerY            = 29530,
            triggerRange        = 1000,
            actorX              = -1300,
            actorZ              = -2000,
            actorY              = 34150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6EE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B9',
    )

    ChrSetPos(0x0016, 18790, -1800, 11600, 0)
    ChrSetPos(0x0017, 17990, -1800, 11600, 90)
    ChrSetPos(0x0018, 17220, -1800, 11420, 90)
    ChrSetPos(0x0019, 16490, -1800, 11290, 90)
    ChrSetPos(0x001A, 15770, -1800, 11470, 90)
    ChrSetPos(0x001B, 15050, -1800, 11610, 90)
    ChrSetPos(0x001C, 14440, -1800, 10960, 45)
    ChrSetPos(0x001D, 14560, -1800, 10210, 0)
    ChrSetPos(0x001E, 14410, -1800, 9520, 0)
    ChrSetPos(0x001F, 14460, -1800, 8730, 0)
    ChrSetPos(0x0020, 14350, -1800, 7960, 0)
    ChrSetPos(0x0021, 14470, -1800, 7260, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x000A, 22700, -1800, 20620, 180)
    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, func_02_A05)
    ChrSetPos(0x000D, 40940, 1050, 21050, 200)
    ChrSetPos(0x0010, 24760, 0, 24750, 225)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_894',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 31330, 0, 20020, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x000F, 0x0010)
    CreateThread(0x000F, 0x00, 0x00, func_02_A05)
    ChrSetPos(0x000F, 54610, 0, 24160, 270)
    ChrSetChipByIndex(0x000F, 21)

    def _loc_894(): pass

    label('loc_894')

    ChrSetPos(0x000C, 3800, -1800, 23920, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 0, 0x2010)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8B6',
    )

    ChrSetFlags(0x000C, 0x0010)

    def _loc_8B6(): pass

    label('loc_8B6')

    Jump('loc_950')

    def _loc_8B9(): pass

    label('loc_8B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_8E5',
    )

    CreateThread(0x000F, 0x01, 0x00, func_03_B82)
    ChrClearFlags(0x000F, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_8E2',
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_8E2(): pass

    label('loc_8E2')

    Jump('loc_950')

    def _loc_8E5(): pass

    label('loc_8E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_91B',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000B, 17990, 0, 1680, 180)
    ChrSetPos(0x000A, 50910, 0, 23310, 288)
    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_950')

    def _loc_91B(): pass

    label('loc_91B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_944',
    )

    ChrSetPos(0x000B, 15930, -1800, 25220, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_950')

    def _loc_944(): pass

    label('loc_944')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_950',
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_950(): pass

    label('loc_950')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_963',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_15_3F9E)

    def _loc_963(): pass

    label('loc_963')

    Return()

# id: 0x0001 offset: 0x964
@scena.Code('func_01_964')
def func_01_964():
    OP_16(0x02, 4000, -88000, -100000, 2293832)
    PlaySE(453, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 2, 0x1242)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_987',
    )

    OP_64(0x04, 0x0001)

    def _loc_987(): pass

    label('loc_987')

    OP_72(0x0016, 0x0010)
    OP_6F(0x0016, 60)
    OP_72(0x0012, 0x0010)
    OP_72(0x0014, 0x0010)
    OP_72(0x0015, 0x0010)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9FF',
    )

    OP_6F(0x0011, 1500)
    OP_72(0x0021, 0x0002)
    OP_71(0x0022, 0x0004)
    OP_64(0x03, 0x0001)
    OP_71(0x0023, 0x0004)
    OP_71(0x0024, 0x0004)
    OP_71(0x0025, 0x0004)
    OP_71(0x0026, 0x0004)

    def _loc_9FF(): pass

    label('loc_9FF')

    OP_1C(0x13, 0x00, 0x001A)

    Return()

# id: 0x0002 offset: 0xA05
@scena.Code('func_02_A05')
def func_02_A05():
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
        'loc_A2A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_B6C')

    def _loc_A2A(): pass

    label('loc_A2A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A43',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_B6C')

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A5C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_B6C')

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A75',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_B6C')

    def _loc_A75(): pass

    label('loc_A75')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A8E',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_B6C')

    def _loc_A8E(): pass

    label('loc_A8E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AA7',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_B6C')

    def _loc_AA7(): pass

    label('loc_AA7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC0',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_B6C')

    def _loc_AC0(): pass

    label('loc_AC0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_B6C')

    def _loc_AD9(): pass

    label('loc_AD9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AF2',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_B6C')

    def _loc_AF2(): pass

    label('loc_AF2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_B6C')

    def _loc_B0B(): pass

    label('loc_B0B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B24',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_B6C')

    def _loc_B24(): pass

    label('loc_B24')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B3D',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_B6C')

    def _loc_B3D(): pass

    label('loc_B3D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B56',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_B6C')

    def _loc_B56(): pass

    label('loc_B56')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_B6C(): pass

    label('loc_B6C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B81',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_B6C')

    def _loc_B81(): pass

    label('loc_B81')

    Return()

# id: 0x0003 offset: 0xB82
@scena.Code('func_03_B82')
def func_03_B82():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BA1',
    )

    OP_99(0x00FE, 0x01, 0x07, 3000)
    ChrSetSubChip(0x00FE, 0)
    Sleep(250)

    Jump('func_03_B82')

    def _loc_BA1(): pass

    label('loc_BA1')

    Return()

# id: 0x0004 offset: 0xBA2
@scena.Code('func_04_BA2')
def func_04_BA2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BD4',
    )

    def _loc_BAE(): pass

    label('loc_BAE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BD1',
    )

    OP_8D(0x00FE, 48840, 21930, 53280, 24890, 2000)

    Jump('loc_BAE')

    def _loc_BD1(): pass

    label('loc_BD1')

    Jump('loc_D44')

    def _loc_BD4(): pass

    label('loc_BD4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BED',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_D2F')

    def _loc_BED(): pass

    label('loc_BED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C06',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_D2F')

    def _loc_C06(): pass

    label('loc_C06')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C1F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_D2F')

    def _loc_C1F(): pass

    label('loc_C1F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C38',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_D2F')

    def _loc_C38(): pass

    label('loc_C38')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C51',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_D2F')

    def _loc_C51(): pass

    label('loc_C51')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C6A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_D2F')

    def _loc_C6A(): pass

    label('loc_C6A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C83',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_D2F')

    def _loc_C83(): pass

    label('loc_C83')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C9C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_D2F')

    def _loc_C9C(): pass

    label('loc_C9C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_D2F')

    def _loc_CB5(): pass

    label('loc_CB5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CCE',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_D2F')

    def _loc_CCE(): pass

    label('loc_CCE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE7',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_D2F')

    def _loc_CE7(): pass

    label('loc_CE7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D00',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_D2F')

    def _loc_D00(): pass

    label('loc_D00')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D19',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_D2F')

    def _loc_D19(): pass

    label('loc_D19')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D2F',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D44',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_D2F')

    def _loc_D44(): pass

    label('loc_D44')

    Return()

# id: 0x0005 offset: 0xD45
@scena.Code('func_05_D45')
def func_05_D45():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_DA2',
    )

    ChrTalk(
        0x00FE,
        (
            '#1761F我们那些家伙一不看着\n',
            '就会马上偷懒的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以要来定期巡视\n',
            '给他们打气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DED')

    def _loc_DA2(): pass

    label('loc_DA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_DC0',
    )

    ChrTalk(
        0x00FE,
        (
            '#1767F哼！哼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DED')

    def _loc_DC0(): pass

    label('loc_DC0')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '#1767F哼！哼！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1766F还没完呢……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DED(): pass

    label('loc_DED')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xDF1
@scena.Code('func_06_DF1')
def func_06_DF1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_E50',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时候，迫不得已\n',
            '也得出来自己打工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是，在父亲的事务所\n',
            '工作啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAC')

    def _loc_E50(): pass

    label('loc_E50')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '去北街区\n',
            '找过工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过世间还真是残酷啊。\n',
            '工作只有选举运动\n',
            '的兼职什么的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAC(): pass

    label('loc_EAC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xEB0
@scena.Code('func_07_EB0')
def func_07_EB0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_F5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1D',
    )

    ChrTalk(
        0x00FE,
        (
            '渡口比以前\n',
            '更混乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前每家都\n',
            '有自己的小船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不用人人\n',
            '都去坐渡船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_F59')

    def _loc_F1D(): pass

    label('loc_F1D')

    ChrTalk(
        0x00FE,
        (
            '渡口比以前\n',
            '更混乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '站在那里都够累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F59(): pass

    label('loc_F59')

    Jump('loc_12D8')

    def _loc_F5C(): pass

    label('loc_F5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1044',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FE7',
    )

    ChrTalk(
        0x00FE,
        (
            '桥竟然不能动了，\n',
            '好像返回到从前一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然渡口有免费的船，\n',
            '但真是不方便啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太习惯方便的生活了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1041')

    def _loc_FE7(): pass

    label('loc_FE7')

    ChrTalk(
        0x00FE,
        (
            '桥竟然不能动了，\n',
            '好像返回到从前一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然渡口有免费的船，\n',
            '但真是不方便啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1041(): pass

    label('loc_1041')

    Jump('loc_12D8')

    def _loc_1044(): pass

    label('loc_1044')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1144',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_10B1',
    )

    ChrTalk(
        0x00FE,
        (
            '从前这一片也是很有活力的。\n',
            '到处都有摊子和市场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的光景\n',
            '现在已经看不到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1141')

    def _loc_10B1(): pass

    label('loc_10B1')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '从前这一片也是很有活力的。\n',
            '到处都有摊子和市场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的选举，港口的年轻人\n',
            '似乎也都很努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的光景\n',
            '现在已经看不到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1141(): pass

    label('loc_1141')

    Jump('loc_12D8')

    def _loc_1144(): pass

    label('loc_1144')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_11F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_117A',
    )

    ChrTalk(
        0x00FE,
        (
            '年轻人就是要有\n',
            '那种精神才好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11EE')

    def _loc_117A(): pass

    label('loc_117A')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '呀，刚才的骚动\n',
            '我看到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '船员们聚在一起\n',
            '那样的争吵是经常的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '年轻人就是要有\n',
            '那种精神才好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11EE(): pass

    label('loc_11EE')

    Jump('loc_12D8')

    def _loc_11F1(): pass

    label('loc_11F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1249',
    )

    ChrTalk(
        0x00FE,
        (
            '名门戴尔蒙家\n',
            '也没落了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所谓时代的转折，\n',
            '大概就是这种事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D8')

    def _loc_1249(): pass

    label('loc_1249')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 6, 0x120E)),
            Expr.Return,
        ),
        'loc_1291',
    )

    ChrTalk(
        0x00FE,
        (
            '诺曼的家…\n',
            '看，就在那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 135, 400)

    ChrTalk(
        0x00FE,
        (
            '那边的宅子就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D8')

    def _loc_1291(): pass

    label('loc_1291')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_12D8',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，每张都\n',
            '照得很有风度嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拍照的人\n',
            '技术一定很好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D8(): pass

    label('loc_12D8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x12DC
@scena.Code('func_08_12DC')
def func_08_12DC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 0, 0x2010)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12F2',
    )

    Call(0, 0x0014)

    Jump('loc_17ED')

    def _loc_12F2(): pass

    label('loc_12F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_140F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1353',
    )

    ChrTalk(
        0x00FE,
        (
            '还要汽油的话\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个油可燃性很强，\n',
            '不能用在油灯里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_140C')

    def _loc_1353(): pass

    label('loc_1353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13C4',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，要是船不来\n',
            '还真是不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仓库里的物资\n',
            '很有限……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真、真不想\n',
            '考虑未来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_140C')

    def _loc_13C4(): pass

    label('loc_13C4')

    ChrTalk(
        0x00FE,
        (
            '船不来的话\n',
            '还真是不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，未来的事\n',
            '还是别去多想吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_140C(): pass

    label('loc_140C')

    Jump('loc_17ED')

    def _loc_140F(): pass

    label('loc_140F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_153A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1470',
    )

    ChrTalk(
        0x00FE,
        (
            '还要汽油的话\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个油可燃性很强，\n',
            '不能用在油灯里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1537')

    def _loc_1470(): pass

    label('loc_1470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14EB',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～好久没有这样\n',
            '活动身体了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '搬运那么多货物\n',
            '真的很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，起重机不能动啊。\n',
            '没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1537')

    def _loc_14EB(): pass

    label('loc_14EB')

    ChrTalk(
        0x00FE,
        (
            '１００％人力作业\n',
            '真是好久没经历过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，平时都是\n',
            '用起重机的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1537(): pass

    label('loc_1537')

    Jump('loc_17ED')

    def _loc_153A(): pass

    label('loc_153A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1626',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_15A9',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～我支持波尔多斯～\n',
            '请多关照市长候选人波尔多斯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '开创港口未来！\n',
            '请多支持波尔多斯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1623')

    def _loc_15A9(): pass

    label('loc_15A9')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任是长年\n',
            '处理港口事物的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果他当了市长\n',
            '应该会重振港口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，喘口气了，\n',
            '那么继续喊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1623(): pass

    label('loc_1623')

    Jump('loc_17ED')

    def _loc_1626(): pass

    label('loc_1626')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_16B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_166A',
    )

    ChrTalk(
        0x00FE,
        (
            '应该从更远处\n',
            '眺望才对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '寿命都缩短了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B4')

    def _loc_166A(): pass

    label('loc_166A')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '跑去围观看吵架，\n',
            '差点被卷进去真把我急坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～吓了一大跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16B4(): pass

    label('loc_16B4')

    Jump('loc_17ED')

    def _loc_16B7(): pass

    label('loc_16B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1764',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1710',
    )

    ChrTalk(
        0x00FE,
        (
            '太偷懒的话\n',
            '布诺安会生气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙要是发起怒来\n',
            '可恐怖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1761')

    def _loc_1710(): pass

    label('loc_1710')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '好，差不多\n',
            '是下一班船来的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作忙里偷闲，\n',
            '选举运动可真辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1761(): pass

    label('loc_1761')

    Jump('loc_17ED')

    def _loc_1764(): pass

    label('loc_1764')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_17ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_17B3',
    )

    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '啊～支持波尔多斯～\n',
            '请多支持～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请多支持波尔多斯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17ED')

    def _loc_17B3(): pass

    label('loc_17B3')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯～这里人不多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在可能去桥对面\n',
            '比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17ED(): pass

    label('loc_17ED')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x17F1
@scena.Code('func_09_17F1')
def func_09_17F1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_184A',
    )

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮的小子们\n',
            '好像也开始什么活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为事态紧急\n',
            '终于醒悟了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF6')

    def _loc_184A(): pass

    label('loc_184A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1987',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_18C1',
    )

    ChrTalk(
        0x00FE,
        (
            '新市长那家伙\n',
            '这么快就露出马脚了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果，那家伙只会嘴上逞能，\n',
            '没有了主任就什么也做不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1984')

    def _loc_18C1(): pass

    label('loc_18C1')

    ChrTalk(
        0x00FE,
        (
            '由于主任的指示，不管怎样\n',
            '至少生活物资都进仓库了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是燃料和食品都用光了\n',
            '就真的完蛋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来新市长那家伙\n',
            '到底在哪里干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在港口前线指挥全部工作的\n',
            '都是波尔多斯主任！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1984(): pass

    label('loc_1984')

    Jump('loc_1CF6')

    def _loc_1987(): pass

    label('loc_1987')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1B73',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1A89',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_19F9',
    )

    ChrTalk(
        0x00FE,
        (
            '昆茨好像为骚动的事\n',
            '去道歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他也参加了煽动，\n',
            '其实是彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A86')

    def _loc_19F9(): pass

    label('loc_19F9')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '昆茨好像为骚动的事\n',
            '去道歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他也参加了煽动，\n',
            '其实是彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，让我们这边的人\n',
            '先去道歉的\n',
            '好像是波尔多斯主任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A86(): pass

    label('loc_1A86')

    Jump('loc_1B70')

    def _loc_1A89(): pass

    label('loc_1A89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1AE3',
    )

    ChrTalk(
        0x00FE,
        (
            '昆茨好像为骚动的事\n',
            '去道歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他也参加了煽动，\n',
            '其实是彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B70')

    def _loc_1AE3(): pass

    label('loc_1AE3')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '昆茨好像为骚动的事\n',
            '去道歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他也参加了煽动，\n',
            '其实是彼此彼此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，让我们这边的人\n',
            '先去道歉的\n',
            '好像是波尔多斯主任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B70(): pass

    label('loc_1B70')

    Jump('loc_1CF6')

    def _loc_1B73(): pass

    label('loc_1B73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1BD4',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么幽灵的事\n',
            '会变成我们的错？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种傻事也别一直做嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，真是火大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF6')

    def _loc_1BD4(): pass

    label('loc_1BD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1CA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C35',
    )

    ChrTalk(
        0x00FE,
        (
            '我也希望波尔多斯主任\n',
            '能当上市长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为没有比他\n',
            '更有声望的人啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA6')

    def _loc_1C35(): pass

    label('loc_1C35')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '帮忙选举没有错。\n',
            '不过也要专心点做事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到底在这种地方\n',
            '大声喊叫有意义吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有海鸥听得到啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CA6(): pass

    label('loc_1CA6')

    Jump('loc_1CF6')

    def _loc_1CA9(): pass

    label('loc_1CA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1CF6',
    )

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任\n',
            '正忙于选举活动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在由我代理\n',
            '掌管港口现场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF6(): pass

    label('loc_1CF6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1CFA
@scena.Code('func_0A_1CFA')
def func_0A_1CFA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1DE8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D8F',
    )

    ChrTalk(
        0x00FE,
        (
            '主任好像打算和诺曼市长\n',
            '同心协力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是波尔多斯主任。\n',
            '器量真大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '输掉了市长选举，\n',
            '回想起来还是遗憾啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1DE5')

    def _loc_1D8F(): pass

    label('loc_1D8F')

    ChrTalk(
        0x00FE,
        (
            '主任好像打算和诺曼市长\n',
            '同心协力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，现在是紧急时刻\n',
            '不团结一致是不行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DE5(): pass

    label('loc_1DE5')

    Jump('loc_211A')

    def _loc_1DE8(): pass

    label('loc_1DE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1E44',
    )

    ChrTalk(
        0x00FE,
        (
            '起重机不能启动，\n',
            '现在只能靠腕力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新市长那家伙也出来\n',
            '帮忙搬运货物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_211A')

    def _loc_1E44(): pass

    label('loc_1E44')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1EF6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1EAA',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，差不多\n',
            '两阵营也该和好了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去，搞不好\n',
            '又会发生什么事件的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF3')

    def _loc_1EAA(): pass

    label('loc_1EAA')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '喔，是各位游击士啊。\n',
            '刚才帮我大忙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差点被\n',
            '当作犯人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EF3(): pass

    label('loc_1EF3')

    Jump('loc_211A')

    def _loc_1EF6(): pass

    label('loc_1EF6')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_1F51',
    )

    ChrTalk(
        0x00FE,
        (
            '喔，是各位游击士啊。\n',
            '在酒店辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，不管怎么说，\n',
            '真相大白就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_211A')

    def _loc_1F51(): pass

    label('loc_1F51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2068',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1FB8',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来那些家伙，\n',
            '连幽灵都要怪到我们头上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～回想起来\n',
            '又开始焦躁不安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2065')

    def _loc_1FB8(): pass

    label('loc_1FB8')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '波尔多斯主任叫我来\n',
            '向诺曼先生道歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明是对方找的麻烦,\n',
            '为什么要我去谢罪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，虽然我说过那些贬低他儿子的话，\n',
            '确实做的不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是～无法接受啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2065(): pass

    label('loc_2065')

    Jump('loc_211A')

    def _loc_2068(): pass

    label('loc_2068')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_20A8',
    )

    ChrTalk(
        0x00FE,
        (
            '海的男人，波尔多斯～！\n',
            '市长选举请投波尔多斯1票！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_211A')

    def _loc_20A8(): pass

    label('loc_20A8')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '海的男人，波尔多斯～！\n',
            '市长选举请投波尔多斯1票！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯将保护你的港口！\n',
            '海的男人波尔多斯请多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_211A(): pass

    label('loc_211A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x211E
@scena.Code('func_0B_211E')
def func_0B_211E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_21F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_218F',
    )

    ChrTalk(
        0x0009,
        (
            '这就是有问题的仓库区吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果要作为旅游地来发展，\n',
            '这里可得想办法处理一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21F9')

    def _loc_218F(): pass

    label('loc_218F')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '这就是有问题的仓库区吗～？\n',
            '好像有不良少年出没呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '听说很危险\n',
            '还找了保镖，\n',
            '是不是有点夸张了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21F9(): pass

    label('loc_21F9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x21FD
@scena.Code('func_0C_21FD')
def func_0C_21FD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_22D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2277',
    )

    ChrTalk(
        0x00FE,
        (
            '好啊，辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才去了市长官邸\n',
            '报告了学院的事件！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '返回协会之前\n',
            '在这里休息一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_22CD')

    def _loc_2277(): pass

    label('loc_2277')

    ChrTalk(
        0x00FE,
        (
            '刚才去了市长官邸\n',
            '报告了学院的事件！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说平安解决了，\n',
            '不愧是艾丝蒂尔你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22CD(): pass

    label('loc_22CD')

    Jump('loc_2387')

    def _loc_22D0(): pass

    label('loc_22D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_22DA',
    )

    Jump('loc_2387')

    def _loc_22DA(): pass

    label('loc_22DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2387',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_234D',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到要在城里\n',
            '当保镖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安的治安好像变得很差，\n',
            '身为地区所属的游击士真该负责啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2387')

    def _loc_234D(): pass

    label('loc_234D')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '啊，辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在给\n',
            '来视察的商人当保镖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2387(): pass

    label('loc_2387')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x238B
@scena.Code('func_0D_238B')
def func_0D_238B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2393',
    )

    Return()

    def _loc_2393(): pass

    label('loc_2393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_23B2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_23AE',
    )

    Jump('loc_23AF')

    def _loc_23AE(): pass

    label('loc_23AE')

    Return()

    def _loc_23AF(): pass

    label('loc_23AF')

    Jump('loc_23CD')

    def _loc_23B2(): pass

    label('loc_23B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_23BA',
    )

    Return()

    def _loc_23BA(): pass

    label('loc_23BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_23C6',
    )

    Return()

    def _loc_23C6(): pass

    label('loc_23C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_23CD',
    )

    def _loc_23CD(): pass

    label('loc_23CD')

    OP_4A(0x000A, 0)

    ChrTalk(
        0x000A,
        (
            '#4A市长候选人波尔多斯！\n',
            '请多支持波尔多斯！',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_4B(0x000A, 0)

    Return()

# id: 0x000E offset: 0x240A
@scena.Code('func_0E_240A')
def func_0E_240A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2412',
    )

    Return()

    def _loc_2412(): pass

    label('loc_2412')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_241C',
    )

    Jump('loc_2442')

    def _loc_241C(): pass

    label('loc_241C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2424',
    )

    Return()

    def _loc_2424(): pass

    label('loc_2424')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2432',
    )

    Jump('loc_2442')

    def _loc_2432(): pass

    label('loc_2432')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2442',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 2, 0x1242)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2442',
    )

    Return()

    def _loc_2442(): pass

    label('loc_2442')

    OP_4A(0x000C, 0)

    ChrTalk(
        0x000C,
        (
            '#4A啊～我支持波尔多斯～\n',
            '请多支持～',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_4B(0x000C, 0)

    Return()

# id: 0x000F offset: 0x2477
@scena.Code('func_0F_2477')
def func_0F_2477():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 5, 0x20D5)),
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24E2',
    )

    ChrTalk(
        0x00FE,
        (
            '#1810370606V呀，要找的东西\n',
            '好像找到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1810370607V看起来挺急的，\n',
            '要当心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AFF')

    def _loc_24E2(): pass

    label('loc_24E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 0, 0x2010)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_288A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 5, 0x20D5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2833',
    )

    ChrSetDirection(0x00FE, 225, 0)
    OP_4A(0x00FE, 255)
    EventBegin(0x00)
    Fade(500)
    CameraMove(25350, 0, 25220, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 26090, 0, 25080, 270)
    ChrSetPos(0x0102, 26250, 0, 24080, 270)
    ChrSetPos(0x00F8, 27170, 0, 24990, 270)
    ChrSetPos(0x00F9, 27360, 0, 23940, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010370592V#1025F#4P那个～打扰一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1810370593V#5P有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370594V#1040F#6P是的。\n',
            '能占用您一点时间吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人说明了情况，\n',
            '并向波尔多斯出示了工房长的介绍信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#1810370595V#5P呼，我的确是\n',
            '港湾区的负责人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1810370596V#5P不过关于这件事\n',
            '最好去问问哈古。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370597V#1015F#4P哈古先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1810370598V#5P啊啊，在我们港口\n',
            '负责货物销售的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1810370599V#5P应该在这个堤防深处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370600V#1006F#4P明白，那里的哈古先生对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370601V#1040F#6P马上去找他谈谈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370602V感谢您的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1810370603V#5P啊啊，当心哦。\n',
            '可别太慌张掉进海里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041A, 5, 0x20D5))
    EventEnd(0x00)

    Jump('loc_2887')

    def _loc_2833(): pass

    label('loc_2833')

    ChrTalk(
        0x00FE,
        (
            '#1810370604V找东西的事\n',
            '问问哈古就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1810370605V应该在这个堤防\n',
            '的深处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2887(): pass

    label('loc_2887')

    Jump('loc_2AFF')

    def _loc_288A(): pass

    label('loc_288A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_29AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_295B',
    )

    ChrTalk(
        0x00FE,
        (
            '我和新市长诺曼\n',
            '保持着良好的关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是市长选举中的对手，\n',
            '但热爱故乡的心情是一样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果互相配合，\n',
            '一定能开拓港湾的未来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，目前这个状况\n',
            '是得想个办法才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_29AB')

    def _loc_295B(): pass

    label('loc_295B')

    ChrTalk(
        0x00FE,
        (
            '我和新市长诺曼\n',
            '保持着良好的关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想渡过这个难关\n',
            '合作比什么都重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29AB(): pass

    label('loc_29AB')

    Jump('loc_2AFF')

    def _loc_29AE(): pass

    label('loc_29AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2AFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA9',
    )

    ChrTalk(
        0x00FE,
        (
            '和诺曼市长也谈过了，\n',
            '总之先把生活物资\n',
            '聚集到仓库里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话目前市民的生活\n',
            '应该能支撑一阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家对新市长的能力\n',
            '也相当怀疑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但想守护卢安的心情\n',
            '我和市长都是一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也要齐心合力\n',
            '支撑市民的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_2AFF')

    def _loc_2AA9(): pass

    label('loc_2AA9')

    ChrTalk(
        0x00FE,
        (
            '总之先把生活物资\n',
            '聚集到仓库里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话目前市民的生活\n',
            '应该能支撑一阵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AFF(): pass

    label('loc_2AFF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2B03
@scena.Code('func_10_2B03')
def func_10_2B03():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2BC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B86',
    )

    ChrTalk(
        0x00FE,
        (
            '反正没人在，\n',
            '正想稍微偷懒一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好洛克大哥\n',
            '过来巡视了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近大哥真是的，\n',
            '总紧张兮兮的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_2BC1')

    def _loc_2B86(): pass

    label('loc_2B86')

    ChrTalk(
        0x00FE,
        (
            '真是的，洛克大哥\n',
            '到底怎么了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近紧张兮兮的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BC1(): pass

    label('loc_2BC1')

    Jump('loc_2CAA')

    def _loc_2BC4(): pass

    label('loc_2BC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2CAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C56',
    )

    ChrTalk(
        0x00FE,
        (
            '桥吊着不能动，\n',
            '这里无法通行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仓库街有渡船出航，\n',
            '要去北区的话就乘那个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '附近应该有我们的成员\n',
            '为你引导的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_2CAA')

    def _loc_2C56(): pass

    label('loc_2C56')

    ChrTalk(
        0x00FE,
        (
            '想去北区的时候\n',
            '就使用仓库街的渡口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '向导的标志\n',
            '就是这个红色印花大手帕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CAA(): pass

    label('loc_2CAA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2CAE
@scena.Code('func_11_2CAE')
def func_11_2CAE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2D8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '总觉得最近，\n',
            '城里的人们都好和善。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才又有不认识的女孩子\n',
            '对我说谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是女神大人\n',
            '在哪保佑我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2D89')

    def _loc_2D3D(): pass

    label('loc_2D3D')

    ChrTalk(
        0x00FE,
        (
            '总觉得最近，\n',
            '城里的人们都好和善。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是女神大人\n',
            '在哪保佑我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D89(): pass

    label('loc_2D89')

    Jump('loc_2E17')

    def _loc_2D8C(): pass

    label('loc_2D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2E17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DDB',
    )

    ChrTalk(
        0x00FE,
        (
            '去北区的小船\n',
            '在这边出发～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请按顺序排队\n',
            '等候～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2E17')

    def _loc_2DDB(): pass

    label('loc_2DDB')

    ChrTalk(
        0x00FE,
        (
            '去北区的小船\n',
            '在这边出发～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长请客\n',
            '不用就亏了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E17(): pass

    label('loc_2E17')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2E1B
@scena.Code('func_12_2E1B')
def func_12_2E1B():
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

# id: 0x0013 offset: 0x2E61
@scena.Code('func_13_2E61')
def func_13_2E61():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3196',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 6, 0x120E)),
            Expr.Return,
        ),
        'loc_2FF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F38',
    )

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200962V#050F还没找贝尔夫那家伙\n',
            '问亡灵的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200963V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200965V#1006F是市长官邸右边的房子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF6')

    def _loc_2F38(): pass

    label('loc_2F38')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200966V#020F还没找叫贝尔夫的孩子\n',
            '问白影的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200967V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200965V#1006F是市长官邸右边的房子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FF6(): pass

    label('loc_2FF6')

    Jump('loc_317B')

    def _loc_2FF9(): pass

    label('loc_2FF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_30BF',
    )

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200970V#050F还没找渡鸦帮那些小子\n',
            '问亡灵的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200963V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200973V#1006F要先去港口的仓库才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_317B')

    def _loc_30BF(): pass

    label('loc_30BF')

    ChrTurnDirection(0x00F7, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200974V#020F还没找渡鸦帮的小子们\n',
            '问白影的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200967V要出城的话先去问问再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200964V#1007F啊，是喔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200973V#1006F要先去港口的仓库才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_317B(): pass

    label('loc_317B')

    ChrMoveToRelative(0x0000, 0, 0, 2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3196(): pass

    label('loc_3196')

    Return()

# id: 0x0014 offset: 0x3197
@scena.Code('func_14_3197')
def func_14_3197():
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
        'loc_31BC',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_31BC(): pass

    label('loc_31BC')

    Fade(1000)
    CameraMove(4330, -1800, 24700, 0)
    OP_67(0, 6230, -10000, 0)
    CameraSetDistance(3170, 0)
    OP_6C(315000, 0)
    OP_6E(282, 0)
    ChrSetPos(0x0101, 5170, -1800, 23340, 270)
    ChrSetPos(0x0102, 5260, -1800, 24300, 270)
    ChrSetPos(0x00F8, 6400, -1800, 22950, 270)
    ChrSetPos(0x00F9, 6380, -1800, 24230, 270)
    OP_4A(0x000C, 255)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010370608V#1011F#6P那个～打扰一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 90, 400)

    ChrTalk(
        0x000C,
        (
            '#1800370609V#5P嗯，什么事？',
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
            '艾丝蒂尔等人说明了情况，\n',
            '并向哈古出示了工房长的介绍信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000C,
        (
            '#1800370610V#5P汽油啊……\n',
            '啊啊，确实送来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1800370611V打算送去蔡斯之前\n',
            '发生了这状况，\n',
            '就一直保管在仓库了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370612V#1006F#6P太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370613V#1040F#4P能马上\n',
            '交给我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1800370614V#5P可以倒是可以……\n',
            '不过量很多哟？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1800370615V全部搬出来\n',
            '应该是不可能的吧。',
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
        'loc_3480',
    )

    ChrTalk(
        0x0103,
        (
            '#0030281595V#026F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370617V#020F总之先拿我们\n',
            '拿得动的份量好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354D')

    def _loc_3480(): pass

    label('loc_3480')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34E9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370618V#053F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370619V#051F嗯，总之先拿我们\n',
            '拿得动的份量好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354D')

    def _loc_34E9(): pass

    label('loc_34E9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_354D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370620V#074F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370621V#070F总之先拿我们\n',
            '拿得动的份量就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_354D(): pass

    label('loc_354D')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(2000)

    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)
    OP_6F(0x0015, 60)
    ChrSetPos(0x0013, 24000, 1000, 4010, 315)
    ChrSetPos(0x0014, 23300, 1000, 4010, 315)
    ChrSetPos(0x0015, 22600, 1000, 4010, 315)
    OP_A1(0x0013, 0x0027)
    OP_72(0x0027, 0x0004)
    OP_A1(0x0014, 0x0028)
    OP_72(0x0028, 0x0004)
    OP_A1(0x0015, 0x0029)
    OP_72(0x0029, 0x0004)
    CameraMove(24300, 500, 4860, 0)
    OP_67(0, 4760, -10000, 0)
    CameraSetDistance(3720, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 23900, 0, 6280, 180)
    ChrSetPos(0x0102, 22750, 0, 6280, 180)
    ChrSetPos(0x00F8, 22200, 0, 7500, 180)
    ChrSetPos(0x00F9, 23870, 0, 7500, 180)
    ChrSetPos(0x000C, 23300, 250, 4960, 180)
    FadeIn(1000, 0)
    OP_0D()
    ChrSetDirection(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#1800370622V#2P嗯……\n',
            '就先这些吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36DC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370623V#560F#6P嗯，有这些\n',
            '应该能维持一阵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3716')

    def _loc_36DC(): pass

    label('loc_36DC')

    ChrTalk(
        0x0102,
        (
            '#0020370624V#1040F#6P嗯嗯，有这些\n',
            '应该能维持一阵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3716(): pass

    label('loc_3716')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3755',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370625V#071F#6P嗯，这点很轻松的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37D4')

    def _loc_3755(): pass

    label('loc_3755')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3795',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370626V#051F#6P这点的话\n',
            '应该能搬动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37D4')

    def _loc_3795(): pass

    label('loc_3795')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37D4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370627V#524F#6P呼……\n',
            '好像肌肉要痛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37D4(): pass

    label('loc_37D4')

    Sleep(200)

    FadeOut(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到３个',
            (TxtCtl.Item, ItemTable['汽油罐']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['汽油罐'], 3)
    OP_71(0x0027, 0x0004)
    OP_71(0x0028, 0x0004)
    OP_71(0x0029, 0x0004)
    Sleep(500)

    OP_6F(0x0015, 0)
    OP_70(0x0015, 0)
    OP_73(0x0015)
    ChrSetPos(0x000C, 23290, 1000, 3980, 180)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#1800370628V#2P好了……\n',
            '如果还需要\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1800370629V不过，在此之前没有比\n',
            '渡过现在这难关更重要的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370630V#1007F#6P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370631V#1040F#6P给您添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_393B')
    def lambda_393B():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_393B')

    DispatchAsync2(0x0101, 0x0001, lambda_393B)

    @scena.Lambda('lambda_394C')
    def lambda_394C():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_394C')

    DispatchAsync2(0x0102, 0x0001, lambda_394C)

    @scena.Lambda('lambda_395D')
    def lambda_395D():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_395D')

    DispatchAsync2(0x00F8, 0x0001, lambda_395D)

    @scena.Lambda('lambda_396E')
    def lambda_396E():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_396E')

    DispatchAsync2(0x00F9, 0x0001, lambda_396E)

    @scena.Lambda('lambda_397F')
    def lambda_397F():
        CameraMove(26650, 0, 7870, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_397F)

    ChrWalkTo(0x000C, 28500, 0, 7890, 3000, 0x00)
    ChrWalkTo(0x000C, 28500, 330, 17370, 3000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    CameraMove(24210, 0, 5890, 1500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B3B',
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
            TXT(0x00, '【◇得到了内燃机】\n'),
            TXT(0x01, '【◇没有内燃机但请雾香询问了要塞】\n'),
            TXT(0x02, '【◇没有内燃机但向塞缪尔询问过内燃机的事】\n'),
            TXT(0x03, '【◇没有内燃机也没有询问要塞但问过维修长】\n'),
            TXT(0x04, '【◇没有内燃机没有询问要塞也没问过维修长】\n'),
            TXT(0x05, '【◇不变更】\n'),
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
        (0x00000000, 'loc_3AF9'),
        (0x00000001, 'loc_3AFF'),
        (0x00000002, 'loc_3B0E'),
        (0x00000003, 'loc_3B1D'),
        (0x00000004, 'loc_3B2C'),
        (-1, 'loc_3B3B'),
    )

    def _loc_3AF9(): pass

    label('loc_3AF9')

    SetScenaFlags(ScenaFlag(0x0401, 7, 0x200F))

    Jump('loc_3B3B')

    def _loc_3AFF(): pass

    label('loc_3AFF')

    ClearScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    SetScenaFlags(ScenaFlag(0x0401, 4, 0x200C))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))

    Jump('loc_3B3B')

    def _loc_3B0E(): pass

    label('loc_3B0E')

    ClearScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    ClearScenaFlags(ScenaFlag(0x0401, 4, 0x200C))
    SetScenaFlags(ScenaFlag(0x0401, 6, 0x200E))

    Jump('loc_3B3B')

    def _loc_3B1D(): pass

    label('loc_3B1D')

    ClearScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    SetScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    ClearScenaFlags(ScenaFlag(0x0401, 4, 0x200C))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))

    Jump('loc_3B3B')

    def _loc_3B2C(): pass

    label('loc_3B2C')

    ClearScenaFlags(ScenaFlag(0x0401, 7, 0x200F))
    ClearScenaFlags(ScenaFlag(0x0401, 3, 0x200B))
    ClearScenaFlags(ScenaFlag(0x0401, 4, 0x200C))
    ClearScenaFlags(ScenaFlag(0x0401, 6, 0x200E))

    Jump('loc_3B3B')

    def _loc_3B3B(): pass

    label('loc_3B3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Return,
        ),
        'loc_3D2A',
    )

    OP_28(0x00C2, 0x01, 0x1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C36',
    )

    @scena.Lambda('lambda_3B5C')
    def lambda_3B5C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3B5C)

    Sleep(100)

    @scena.Lambda('lambda_3B6F')
    def lambda_3B6F():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3B6F)

    Sleep(100)

    @scena.Lambda('lambda_3B82')
    def lambda_3B82():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3B82)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370632V#1006F#5P好了……\n',
            '这样材料就齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370520V赶快返回亚尔摩\n',
            '开始改造水泵装置吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370634V#061F#6P嗯，我\n',
            '随时准备ＯＫ的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D27')

    def _loc_3C36(): pass

    label('loc_3C36')

    @scena.Lambda('lambda_3C3C')
    def lambda_3C3C():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3C3C)

    Sleep(100)

    @scena.Lambda('lambda_3C4F')
    def lambda_3C4F():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3C4F)

    Sleep(100)

    @scena.Lambda('lambda_3C62')
    def lambda_3C62():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3C62)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370635V#1006F#5P好了……\n',
            '这样材料就齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370523V#1015F必须要有提妲\n',
            '才能改造水泵装置吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370524V#1040F#4P是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370525V先返回协会\n',
            '和提妲会合吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D27(): pass

    label('loc_3D27')

    Jump('loc_3F75')

    def _loc_3D2A(): pass

    label('loc_3D2A')

    @scena.Lambda('lambda_3D30')
    def lambda_3D30():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3D30)

    Sleep(100)

    @scena.Lambda('lambda_3D43')
    def lambda_3D43():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3D43)

    Sleep(100)

    @scena.Lambda('lambda_3D56')
    def lambda_3D56():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3D56)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370639V#1006F#5P好了……\n',
            '这样汽油就ＯＫ了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370640V#1015F接着是内燃机……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E60',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020370641V#1040F#4P似乎着陆在托兰特平原的\n',
            '警备艇在运送那机械。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370642V去那边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370643V#1006F#5P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F75')

    def _loc_3E60(): pass

    label('loc_3E60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            Expr.Return,
        ),
        'loc_3EF4',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370644V#1035F#4P好像又被王国军\n',
            '借去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370645V#1040F只好去雷斯顿要塞\n',
            '问问看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370646V#1006F#5P是吗，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F75')

    def _loc_3EF4(): pass

    label('loc_3EF4')

    ChrTalk(
        0x0102,
        (
            '#0020370647V#1040F#4P记得保管人\n',
            '是格斯塔夫维修长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370648V去蔡斯飞船坪看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370649V#1006F#5P嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F75(): pass

    label('loc_3F75')

    SetScenaFlags(ScenaFlag(0x0402, 1, 0x2011))
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    OP_28(0x00C2, 0x01, 0x0800)
    ChrSetPos(0x000C, 3800, -1800, 23920, 270)
    ChrClearFlags(0x000C, 0x0010)
    OP_4B(0x000C, 255)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x3F9E
@scena.Code('func_15_3F9E')
def func_15_3F9E():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FC0',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)

    def _loc_3FC0(): pass

    label('loc_3FC0')

    LoadChip('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP', 22)
    LoadChip('ED6_DT27/CH03013._CH', 'ED6_DT27/CH03013P._CP', 23)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_3FED'),
        (0x00000005, 'loc_3FFA'),
        (0x00000006, 'loc_4007'),
        (0x00000007, 'loc_4014'),
        (-1, 'loc_4021'),
    )

    def _loc_3FED(): pass

    label('loc_3FED')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 24)

    Jump('loc_4021')

    def _loc_3FFA(): pass

    label('loc_3FFA')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 24)

    Jump('loc_4021')

    def _loc_4007(): pass

    label('loc_4007')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 24)

    Jump('loc_4021')

    def _loc_4014(): pass

    label('loc_4014')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 24)

    Jump('loc_4021')

    def _loc_4021(): pass

    label('loc_4021')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_403A'),
        (0x00000005, 'loc_4047'),
        (0x00000006, 'loc_4054'),
        (0x00000007, 'loc_4061'),
        (-1, 'loc_406E'),
    )

    def _loc_403A(): pass

    label('loc_403A')

    LoadChip('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP', 25)

    Jump('loc_406E')

    def _loc_4047(): pass

    label('loc_4047')

    LoadChip('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP', 25)

    Jump('loc_406E')

    def _loc_4054(): pass

    label('loc_4054')

    LoadChip('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP', 25)

    Jump('loc_406E')

    def _loc_4061(): pass

    label('loc_4061')

    LoadChip('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP', 25)

    Jump('loc_406E')

    def _loc_406E(): pass

    label('loc_406E')

    ChrSetChipByIndex(0x0101, 22)
    ChrSetChipByIndex(0x0102, 23)
    ChrSetChipByIndex(0x00F8, 24)
    ChrSetChipByIndex(0x00F9, 25)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    OP_4A(0x001F, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0021, 255)
    LoadEffect(0x00, 'map\\\\mp013_00.eff')
    PlayEffect(0x00, 0x00, 0x0024, 0, -100, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x002A, 0x0004)
    OP_71(0x002A, 0x0002)
    OP_71(0x002A, 0x0040)
    OP_71(0x002A, 0x0020)
    OP_B0(0x002A, 0x1E)
    OP_6F(0x002A, 1)
    OP_70(0x002A, 240)
    OP_A1(0x0024, 0x002A)
    ChrSetFlags(0x0024, 0x0040)
    ChrSetPos(0x0024, 4000, -2900, 14170, 180)
    ChrSetDirection(0x0024, 90, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrSetFlags(0x0022, 0x0040)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0020)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x00F8, 0x0020)
    ChrSetFlags(0x00F9, 0x0020)
    Yield()
    ChrSetDirection(0x0024, 270, 0)
    OP_89(0x0101, 4900, -2800, 13940, 90)
    OP_89(0x0102, 4900, -2800, 14580, 90)
    OP_89(0x00F8, 3550, -2800, 14580, 90)
    OP_89(0x00F9, 3550, -2800, 13940, 90)
    OP_89(0x0022, 2900, -3000, 13800, 180)
    ChrSetBattleFlags(0x0022, 0x0020)
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x0102, 0x0020)
    ChrSetBattleFlags(0x00F8, 0x0020)
    ChrSetBattleFlags(0x00F9, 0x0020)
    Yield()
    CameraMove(15100, -1800, 13700, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_4243')
    def lambda_4243():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_4243')

    DispatchAsync2(0x0016, 0x0001, lambda_4243)

    @scena.Lambda('lambda_4254')
    def lambda_4254():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_4254')

    DispatchAsync2(0x0017, 0x0001, lambda_4254)

    @scena.Lambda('lambda_4265')
    def lambda_4265():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_4265')

    DispatchAsync2(0x0018, 0x0001, lambda_4265)

    @scena.Lambda('lambda_4276')
    def lambda_4276():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_4276')

    DispatchAsync2(0x0019, 0x0001, lambda_4276)

    @scena.Lambda('lambda_4287')
    def lambda_4287():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_4287')

    DispatchAsync2(0x001A, 0x0001, lambda_4287)

    @scena.Lambda('lambda_4298')
    def lambda_4298():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_4298')

    DispatchAsync2(0x001B, 0x0001, lambda_4298)

    @scena.Lambda('lambda_42A9')
    def lambda_42A9():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_42A9')

    DispatchAsync2(0x001C, 0x0001, lambda_42A9)

    @scena.Lambda('lambda_42BA')
    def lambda_42BA():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_42BA')

    DispatchAsync2(0x001D, 0x0001, lambda_42BA)

    @scena.Lambda('lambda_42CB')
    def lambda_42CB():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_42CB')

    DispatchAsync2(0x001E, 0x0001, lambda_42CB)

    @scena.Lambda('lambda_42DC')
    def lambda_42DC():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_42DC')

    DispatchAsync2(0x001F, 0x0001, lambda_42DC)

    @scena.Lambda('lambda_42ED')
    def lambda_42ED():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_42ED')

    DispatchAsync2(0x0020, 0x0001, lambda_42ED)

    @scena.Lambda('lambda_42FE')
    def lambda_42FE():
        ChrTurnDirection(0x00FE, 0x0024, 400)
        Yield()

        Jump('lambda_42FE')

    DispatchAsync2(0x0021, 0x0001, lambda_42FE)

    @scena.Lambda('lambda_430F')
    def lambda_430F():
        ChrMoveTo(0x00FE, 18000, -2900, 14170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_430F)

    @scena.Lambda('lambda_432A')
    def lambda_432A():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_432A)

    @scena.Lambda('lambda_4345')
    def lambda_4345():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4345)

    @scena.Lambda('lambda_4360')
    def lambda_4360():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4360)

    @scena.Lambda('lambda_437B')
    def lambda_437B():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_437B)

    @scena.Lambda('lambda_4396')
    def lambda_4396():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4396)

    Sleep(2000)

    @scena.Lambda('lambda_43B6')
    def lambda_43B6():
        CameraMove(17380, -1800, 13360, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_43B6)

    Sleep(4000)

    @scena.Lambda('lambda_43D3')
    def lambda_43D3():
        ChrMoveTo(0x00FE, 18170, -2900, 14170, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_43D3)

    @scena.Lambda('lambda_43EE')
    def lambda_43EE():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_43EE)

    @scena.Lambda('lambda_4409')
    def lambda_4409():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4409)

    @scena.Lambda('lambda_4424')
    def lambda_4424():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4424)

    @scena.Lambda('lambda_443F')
    def lambda_443F():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_443F)

    @scena.Lambda('lambda_445A')
    def lambda_445A():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_445A)

    Sleep(2000)

    @scena.Lambda('lambda_447A')
    def lambda_447A():
        ChrMoveTo(0x00FE, 18170, -2900, 14170, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_447A)

    @scena.Lambda('lambda_4495')
    def lambda_4495():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_4495)

    @scena.Lambda('lambda_44B0')
    def lambda_44B0():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44B0)

    @scena.Lambda('lambda_44CB')
    def lambda_44CB():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_44CB)

    @scena.Lambda('lambda_44E6')
    def lambda_44E6():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_44E6)

    @scena.Lambda('lambda_4501')
    def lambda_4501():
        ChrMoveToRelativeAsync(0x00FE, 14000, 0, 0, 750, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4501)

    WaitForThreadExit(0x0024, 0x0001)
    TerminateThread(0x0022, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    StopEffect(0x00, 0x02)
    TerminateThread(0x0101, 0x01)
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0024, 0x01)
    TerminateThread(0x0016, 0x01)
    TerminateThread(0x0017, 0x01)
    TerminateThread(0x0018, 0x01)
    TerminateThread(0x0019, 0x01)
    TerminateThread(0x001A, 0x01)
    TerminateThread(0x001B, 0x01)
    TerminateThread(0x001C, 0x01)
    TerminateThread(0x001D, 0x01)
    TerminateThread(0x001E, 0x01)
    TerminateThread(0x001F, 0x01)
    TerminateThread(0x0020, 0x01)
    TerminateThread(0x0021, 0x01)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetPos(0x0000, 18420, 0, 6280, 90)
    ChrSetPos(0x0001, 18420, 0, 6280, 90)
    ChrSetPos(0x0002, 18420, 0, 6280, 90)
    ChrSetPos(0x0003, 18420, 0, 6280, 90)
    ChrSetFlags(0x0101, 0x0001)
    ChrSetFlags(0x0102, 0x0001)
    ChrSetFlags(0x00F8, 0x0001)
    ChrSetFlags(0x00F9, 0x0001)
    ChrClearFlags(0x0022, 0x0020)
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0102, 0x0020)
    ChrClearFlags(0x00F8, 0x0020)
    ChrClearFlags(0x00F9, 0x0020)
    CameraMove(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x002A, 0x0004)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetPos(0x0016, 18790, -1800, 11600, 0)
    ChrSetPos(0x0017, 17990, -1800, 11600, 90)
    ChrSetPos(0x0018, 17220, -1800, 11420, 90)
    ChrSetPos(0x0019, 16490, -1800, 11290, 90)
    ChrSetPos(0x001A, 15770, -1800, 11470, 90)
    ChrSetPos(0x001B, 15050, -1800, 11610, 90)
    ChrSetPos(0x001C, 14440, -1800, 10960, 45)
    ChrSetPos(0x001D, 14560, -1800, 10210, 0)
    ChrSetPos(0x001E, 14410, -1800, 9520, 0)
    ChrSetPos(0x001F, 14460, -1800, 8730, 0)
    ChrSetPos(0x0020, 14350, -1800, 7960, 0)
    ChrSetPos(0x0021, 14470, -1800, 7260, 0)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)
    OP_4B(0x001F, 255)
    OP_4B(0x0020, 255)
    OP_4B(0x0021, 255)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    OP_DC()
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x4750
@scena.Code('func_16_4750')
def func_16_4750():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_475D',
    )

    Return()

    def _loc_475D(): pass

    label('loc_475D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 5, 0x2035)),
            Expr.Return,
        ),
        'loc_4769',
    )

    Call(0, 0x0017)

    Return()

    def _loc_4769(): pass

    label('loc_4769')

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
        'loc_4789',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)
    FadeIn(0, 0)

    def _loc_4789(): pass

    label('loc_4789')

    SetScenaFlags(ScenaFlag(0x0406, 5, 0x2035))
    Fade(1000)
    ChrSetPos(0x0101, 16260, -1300, 6720, 310)
    ChrSetPos(0x0102, 16260, -1300, 5650, 310)
    ChrSetPos(0x00F8, 17170, -550, 6760, 310)
    ChrSetPos(0x00F9, 17240, -550, 5550, 310)
    CameraMove(17120, -1300, 7040, 0)
    OP_67(0, 4230, -10000, 0)
    CameraSetDistance(2180, 0)
    OP_6C(134000, 0)
    OP_6E(481, 0)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    OP_4A(0x001F, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0021, 255)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4950',
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
            TXT(0x00, '【◇绕道去嘉恩那里(修好了卢安支部的通讯器)】\n'),
            TXT(0x01, '【◇不绕道(没修好卢安支部的通讯器)】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_48F1'),
        (0x00000001, 'loc_48F7'),
        (-1, 'loc_48FD'),
    )

    def _loc_48F1(): pass

    label('loc_48F1')

    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))

    Jump('loc_48FD')

    def _loc_48F7(): pass

    label('loc_48F7')

    ClearScenaFlags(ScenaFlag(0x0400, 1, 0x2001))

    Jump('loc_48FD')

    def _loc_48FD(): pass

    label('loc_48FD')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Return,
        ),
        'loc_4918',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4918(): pass

    label('loc_4918')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Return,
        ),
        'loc_4929',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_4929(): pass

    label('loc_4929')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Return,
        ),
        'loc_493A',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_493A(): pass

    label('loc_493A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_494D',
    )

    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))

    Jump('loc_4950')

    def _loc_494D(): pass

    label('loc_494D')

    ClearScenaFlags(ScenaFlag(0x0412, 1, 0x2091))

    def _loc_4950(): pass

    label('loc_4950')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C69',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360221V#1004F#5P这、这怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360222V#1042F#2P好混乱啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0021, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_49C7')
    def lambda_49C7():
        CameraMove(17090, -1800, 5230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_49C7)

    ChrTurnDirection(0x0021, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0021,
        (
            '#3860360223V#4P怎么，你们也要\n',
            '前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    CameraMove(16700, -1050, 7050, 0)
    OP_67(0, 7280, -10000, 0)
    CameraSetDistance(1630, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_0D()

    @scena.Lambda('lambda_4A63')
    def lambda_4A63():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4A63)

    Sleep(100)

    @scena.Lambda('lambda_4A76')
    def lambda_4A76():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4A76)

    Sleep(100)

    @scena.Lambda('lambda_4A89')
    def lambda_4A89():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4A89)

    Sleep(100)

    ChrSetDirection(0x00F9, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360224V#1004F#5P啊……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#3860360187V#6P怎么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360188V伦格兰德大桥吊起来\n',
            '不动了知道吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360189V因为这个，要去对面\n',
            '只能乘小船了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360190V而这里就是渡口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360229V#1007F#5P是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360192V#1043F#2P那……\n',
            '还是很不方便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#3860360193V#6P不方便当然不方便。\n',
            '说实话，真是受不了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360194V虽然由于新市长的安排\n',
            '坐船是免费的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360195V尽管如此，光是排队\n',
            '就要等上３０分钟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E9A')

    def _loc_4C69(): pass

    label('loc_4C69')

    ChrTalk(
        0x0101,
        (
            '#0010360234V#1004F#5P这个，难道就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360235V#1042F#2P嘉恩先生说的\n',
            '小船渡口呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0021, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_4CE7')
    def lambda_4CE7():
        CameraMove(17090, -1800, 5230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4CE7)

    ChrTurnDirection(0x0021, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0021,
        (
            '#3860360223V#4P怎么，你们也\n',
            '前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    CameraMove(16700, -1050, 7050, 0)
    OP_67(0, 7280, -10000, 0)
    CameraSetDistance(1630, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_0D()

    @scena.Lambda('lambda_4D81')
    def lambda_4D81():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D81)

    Sleep(100)

    @scena.Lambda('lambda_4D94')
    def lambda_4D94():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4D94)

    Sleep(100)

    @scena.Lambda('lambda_4DA7')
    def lambda_4DA7():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4DA7)

    Sleep(100)

    ChrSetDirection(0x00F9, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360237V#1025F#5P啊，嗯。\n',
            '虽然有这打算……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360200V需要花钱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#3860360201V#6P不，由于新市长的安排\n',
            '坐船是免费的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360202V尽管如此，光是排队\n',
            '就要等上３０分钟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3860360203V说实话，真是受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E9A(): pass

    label('loc_4E9A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EDC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360242V#065F#2P呜哎～……\n',
            '要那么久吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F4F')

    def _loc_4EDC(): pass

    label('loc_4EDC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F17',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360243V#025F#2P那可够久的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F4F')

    def _loc_4F17(): pass

    label('loc_4F17')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F4F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360244V#052F#2P那可够久的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F4F(): pass

    label('loc_4F4F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FAB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360245V#074F#2P不过，因为是往返航程，\n',
            '需要这么长时间也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5060')

    def _loc_4FAB(): pass

    label('loc_4FAB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5007',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360246V#053F#2P不过，因为是往返航程，\n',
            '需要这么长时间也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5060')

    def _loc_5007(): pass

    label('loc_5007')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5060',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360247V#025F#2P不过，因为是往返航程，\n',
            '需要这么长时间也没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5060(): pass

    label('loc_5060')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020360210V#1042F#4P怎么办、艾丝蒂尔。\n',
            '我们也前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360249V#1015F#5P唔、嗯～……',
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
            TXT(0x00, '【渡去北街区】\n'),
            TXT(0x01, '【先不过去】\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_528E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360250V#1025F#5P不，先不去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360213V做完手上的事之后\n',
            '再去对面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360214V#1040F#4P知道了。\n',
            '那么回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 18420, 0, 6280, 90)
    ChrSetPos(0x0001, 18420, 0, 6280, 90)
    ChrSetPos(0x0002, 18420, 0, 6280, 90)
    ChrSetPos(0x0003, 18420, 0, 6280, 90)
    OP_69(0x0000, 0)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)
    OP_4B(0x001F, 255)
    OP_4B(0x0020, 255)
    OP_4B(0x0021, 255)
    ChrSetDirection(0x0021, 0, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_528E(): pass

    label('loc_528E')

    SetScenaFlags(ScenaFlag(0x0406, 6, 0x2036))

    ChrTalk(
        0x0101,
        (
            '#0010360253V#1007F#5P……没法子。\n',
            '似乎也没其他的办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360216V#1040F#4P知道了。\n',
            '那么排队吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(15520, -1550, 8870, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x001A, 18790, -1800, 11600, 0)
    ChrSetPos(0x001B, 17990, -1800, 11600, 90)
    ChrSetPos(0x001C, 17220, -1800, 11420, 90)
    ChrSetPos(0x001D, 16490, -1800, 11290, 90)
    ChrSetPos(0x001E, 15770, -1800, 11470, 90)
    ChrSetPos(0x001F, 15050, -1800, 11610, 90)
    ChrSetPos(0x0020, 14440, -1800, 10960, 45)
    ChrSetPos(0x0021, 14560, -1800, 10210, 0)
    ChrSetPos(0x0101, 14410, -1800, 9520, 0)
    ChrSetPos(0x0102, 14460, -1800, 8730, 0)
    ChrSetPos(0x00F8, 14350, -1800, 7960, 0)
    ChrSetPos(0x00F9, 14470, -1800, 7260, 0)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(14870, -1800, 11420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x001E, 18790, -1800, 11600, 0)
    ChrSetPos(0x001F, 17990, -1800, 11600, 90)
    ChrSetPos(0x0020, 17220, -1800, 11420, 90)
    ChrSetPos(0x0021, 16490, -1800, 11290, 90)
    ChrSetPos(0x0101, 15770, -1800, 11470, 90)
    ChrSetPos(0x0102, 15050, -1800, 11610, 90)
    ChrSetPos(0x00F8, 14440, -1800, 10960, 45)
    ChrSetPos(0x00F9, 14560, -1800, 10210, 0)
    ChrSetPos(0x0018, 14410, -1800, 9520, 0)
    ChrSetPos(0x0016, 14460, -1800, 8730, 0)
    ChrSetPos(0x0019, 14350, -1800, 7960, 0)
    ChrSetPos(0x0017, 14470, -1800, 7260, 0)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(17470, -1800, 11460, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 18790, -1800, 11600, 0)
    ChrSetPos(0x0102, 17990, -1800, 11600, 90)
    ChrSetPos(0x00F8, 17220, -1800, 11420, 90)
    ChrSetPos(0x00F9, 16490, -1800, 11290, 90)
    ChrSetPos(0x0018, 15770, -1800, 11470, 90)
    ChrSetPos(0x0016, 15050, -1800, 11610, 90)
    ChrSetPos(0x0019, 14440, -1800, 10960, 45)
    ChrSetPos(0x0017, 14560, -1800, 10210, 0)
    ChrSetPos(0x001A, 14410, -1800, 9520, 0)
    ChrSetPos(0x001C, 14460, -1800, 8730, 0)
    ChrSetPos(0x001B, 14350, -1800, 7960, 0)
    ChrSetPos(0x001D, 14470, -1800, 7260, 0)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(18450, -1800, 12450, 0)
    OP_67(0, 4950, -10000, 0)
    CameraSetDistance(2220, 0)
    OP_6C(135000, 0)
    OP_6E(381, 0)
    ChrSetPos(0x0101, 19290, -1800, 11600, 0)
    ChrSetPos(0x0102, 18490, -1800, 11600, 0)
    ChrSetPos(0x00F8, 17720, -1800, 11420, 0)
    ChrSetPos(0x00F9, 16990, -1800, 11290, 0)
    LoadEffect(0x01, 'map\\\\mp013_02.eff')
    PlayEffect(0x01, 0x01, 0x0024, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x002A, 0x0004)
    OP_72(0x002A, 0x0002)
    OP_71(0x002A, 0x0400)
    OP_71(0x002A, 0x0040)
    OP_71(0x002A, 0x0020)
    OP_B0(0x002A, 0x1E)
    OP_6F(0x002A, 1)
    OP_70(0x002A, 240)
    OP_A1(0x0024, 0x002A)
    ChrSetFlags(0x0024, 0x0040)
    ChrSetPos(0x0024, 18170, -2900, 14170, 90)
    ChrSetDirection(0x0024, 90, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrSetFlags(0x0022, 0x0040)
    ChrClearBattleFlags(0x0022, 0x0020)
    ChrSetPos(0x0022, 19600, -3000, 14300, 180)
    Yield()
    FadeIn(1000, 0)
    OP_0D()
    OP_DC()

    ChrTalk(
        0x0022,
        (
            '#1520360217V#6P久等了。\n',
            '轮到你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1520360218V赶快上小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360257V#1006F#5P啊，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360258V#1040F#2P那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x01, 0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(460, 0x00, 0x64)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/T2100._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x58E2
@scena.Code('func_17_58E2')
def func_17_58E2():
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
        'loc_5902',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)
    FadeIn(0, 0)

    def _loc_5902(): pass

    label('loc_5902')

    Fade(1000)
    ChrSetPos(0x0101, 16260, -1300, 6720, 270)
    ChrSetPos(0x0102, 16260, -1300, 5650, 270)
    ChrSetPos(0x00F8, 17170, -550, 6760, 270)
    ChrSetPos(0x00F9, 17240, -550, 5550, 270)
    CameraMove(16700, -1050, 7050, 0)
    OP_67(0, 7090, -10000, 0)
    CameraSetDistance(1640, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    OP_4A(0x001F, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0021, 255)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A2C',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020360272V#1042F怎么办、艾丝蒂尔。\n',
            '我们也前往对面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360249V#1015F#5P唔、嗯～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A2C(): pass

    label('loc_5A2C')

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
            TXT(0x00, '【渡去北街区】\n'),
            TXT(0x01, '【先不过去】\n'),
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
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B1B',
    )

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360250V#1025F#5P不，先不去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360213V做完手上的事之后\n',
            '再去对面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360276V#1040F明白了。\n',
            '那么回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B1B(): pass

    label('loc_5B1B')

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 18420, 0, 6280, 90)
    ChrSetPos(0x0001, 18420, 0, 6280, 90)
    ChrSetPos(0x0002, 18420, 0, 6280, 90)
    ChrSetPos(0x0003, 18420, 0, 6280, 90)
    OP_69(0x0000, 0)
    OP_4B(0x0016, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x001B, 255)
    OP_4B(0x001C, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)
    OP_4B(0x001F, 255)
    OP_4B(0x0020, 255)
    OP_4B(0x0021, 255)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_5BEA(): pass

    label('loc_5BEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C6A',
    )

    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(700)

    ChrTalk(
        0x0101,
        (
            '#0010360253V#1007F#5P……没法子。\n',
            '似乎也没其他的办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360216V#1040F#4P知道了。\n',
            '那么排队吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C6A(): pass

    label('loc_5C6A')

    OP_DB()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(15520, -1550, 8870, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x001A, 18790, -1800, 11600, 0)
    ChrSetPos(0x001B, 17990, -1800, 11600, 90)
    ChrSetPos(0x001C, 17220, -1800, 11420, 90)
    ChrSetPos(0x001D, 16490, -1800, 11290, 90)
    ChrSetPos(0x001E, 15770, -1800, 11470, 90)
    ChrSetPos(0x001F, 15050, -1800, 11610, 90)
    ChrSetPos(0x0020, 14440, -1800, 10960, 45)
    ChrSetPos(0x0021, 14560, -1800, 10210, 0)
    ChrSetPos(0x0101, 14410, -1800, 9520, 0)
    ChrSetPos(0x0102, 14460, -1800, 8730, 0)
    ChrSetPos(0x00F8, 14350, -1800, 7960, 0)
    ChrSetPos(0x00F9, 14470, -1800, 7260, 0)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(14870, -1800, 11420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x001E, 18790, -1800, 11600, 0)
    ChrSetPos(0x001F, 17990, -1800, 11600, 90)
    ChrSetPos(0x0020, 17220, -1800, 11420, 90)
    ChrSetPos(0x0021, 16490, -1800, 11290, 90)
    ChrSetPos(0x0101, 15770, -1800, 11470, 90)
    ChrSetPos(0x0102, 15050, -1800, 11610, 90)
    ChrSetPos(0x00F8, 14440, -1800, 10960, 45)
    ChrSetPos(0x00F9, 14560, -1800, 10210, 0)
    ChrSetPos(0x0018, 14410, -1800, 9520, 0)
    ChrSetPos(0x0016, 14460, -1800, 8730, 0)
    ChrSetPos(0x0019, 14350, -1800, 7960, 0)
    ChrSetPos(0x0017, 14470, -1800, 7260, 0)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(17470, -1800, 11460, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 18790, -1800, 11600, 0)
    ChrSetPos(0x0102, 17990, -1800, 11600, 90)
    ChrSetPos(0x00F8, 17220, -1800, 11420, 90)
    ChrSetPos(0x00F9, 16490, -1800, 11290, 90)
    ChrSetPos(0x0018, 15770, -1800, 11470, 90)
    ChrSetPos(0x0016, 15050, -1800, 11610, 90)
    ChrSetPos(0x0019, 14440, -1800, 10960, 45)
    ChrSetPos(0x0017, 14560, -1800, 10210, 0)
    ChrSetPos(0x001A, 14410, -1800, 9520, 0)
    ChrSetPos(0x001C, 14460, -1800, 8730, 0)
    ChrSetPos(0x001B, 14350, -1800, 7960, 0)
    ChrSetPos(0x001D, 14470, -1800, 7260, 0)
    ChrSetFlags(0x001E, 0x0080)
    ChrSetFlags(0x001F, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x0021, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    CameraMove(18450, -1800, 12450, 0)
    OP_67(0, 4950, -10000, 0)
    CameraSetDistance(2220, 0)
    OP_6C(135000, 0)
    OP_6E(381, 0)
    ChrSetPos(0x0101, 19290, -1800, 11600, 0)
    ChrSetPos(0x0102, 18490, -1800, 11600, 0)
    ChrSetPos(0x00F8, 17720, -1800, 11420, 0)
    ChrSetPos(0x00F9, 16990, -1800, 11290, 0)
    LoadEffect(0x01, 'map\\\\mp013_02.eff')
    PlayEffect(0x01, 0x01, 0x0024, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x002A, 0x0004)
    OP_72(0x002A, 0x0002)
    OP_71(0x002A, 0x0400)
    OP_71(0x002A, 0x0040)
    OP_71(0x002A, 0x0020)
    OP_B0(0x002A, 0x1E)
    OP_6F(0x002A, 1)
    OP_70(0x002A, 240)
    OP_A1(0x0024, 0x002A)
    ChrSetFlags(0x0024, 0x0040)
    ChrSetPos(0x0024, 18170, -2900, 14170, 90)
    ChrSetDirection(0x0024, 90, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrSetFlags(0x0022, 0x0040)
    ChrClearBattleFlags(0x0022, 0x0020)
    ChrSetPos(0x0022, 19600, -3000, 14200, 180)
    Yield()
    FadeIn(1000, 0)
    OP_0D()
    OP_DC()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0406, 6, 0x2036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6238',
    )

    SetScenaFlags(ScenaFlag(0x0406, 6, 0x2036))

    ChrTalk(
        0x0022,
        (
            '#1520360217V#6P久等了。\n',
            '轮到你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1520360218V赶快上小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360281V#1006F#5P啊，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360282V#1040F#2P那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6284')

    def _loc_6238(): pass

    label('loc_6238')

    ChrTalk(
        0x0022,
        (
            '#1520360270V#6P好，轮到你们了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1520360271V后面很挤\n',
            '赶快上小船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6284(): pass

    label('loc_6284')

    StopEffect(0x01, 0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(460, 0x00, 0x64)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/T2100._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x62A9
@scena.Code('func_18_62A9')
def func_18_62A9():
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
        (0x00000000, 'loc_6323'),
        (0x00000001, 'loc_6329'),
        (-1, 'loc_632F'),
    )

    def _loc_6323(): pass

    label('loc_6323')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_632F')

    def _loc_6329(): pass

    label('loc_6329')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_632F')

    def _loc_632F(): pass

    label('loc_632F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_633D',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_6341')

    def _loc_633D(): pass

    label('loc_633D')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_6341(): pass

    label('loc_6341')

    Return()

# id: 0x0019 offset: 0x6342
@scena.Code('func_19_6342')
def func_19_6342():
    MapClearFlags(0x00000001)
    CameraMove(122280, 0, 24310, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x001A offset: 0x639B
@scena.Code('func_1A_639B')
def func_1A_639B():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

# id: 0x001B offset: 0x63A2
@scena.Code('func_1B_63A2')
def func_1B_63A2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　    卢安市长选举\n',
            '※投票日请务必\n',
            '　要去投票所\n',
            '　　　　　选举管理委员会',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001C offset: 0x641C
@scena.Code('func_1C_641C')
def func_1C_641C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0248, 2, 0x1242)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6429',
    )

    Return()

    def _loc_6429(): pass

    label('loc_6429')

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
        'loc_6445',
    )

    Call(0, 0x0018)
    FadeIn(0, 0)

    def _loc_6445(): pass

    label('loc_6445')

    Fade(1000)
    ChrSetPos(0x0101, 29960, 1050, 15670, 180)
    ChrSetPos(0x00F7, 29070, 900, 16290, 180)
    ChrSetPos(0x0023, 24000, 0, 8780, 90)
    ChrClearFlags(0x0023, 0x0080)

    @scena.Lambda('lambda_6488')
    def lambda_6488():
        OP_69(0x0025, 0)
        Yield()

        Jump('lambda_6488')

    DispatchAsync2(0x0025, 0x0001, lambda_6488)

    CreateThread(0x0025, 0x02, 0x00, func_1D_6E50)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_64CC')
    def lambda_64CC():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_64CC)

    Sleep(200)

    @scena.Lambda('lambda_64E7')
    def lambda_64E7():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_64E7)

    @scena.Lambda('lambda_64FD')
    def lambda_64FD():
        ChrWalkTo(0x00FE, 29380, 0, 8780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_64FD)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200926V#1004F啊……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200927V难不成是罗伊德大叔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0023, 0x0001)
    TerminateThread(0x0025, 0x01)
    TerminateThread(0x0025, 0x02)
    OP_62(0x0023, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0023, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0023,
        (
            '#1230200928V噢，原来是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0023, 0, 400)

    @scena.Lambda('lambda_65D4')
    def lambda_65D4():
        ChrWalkTo(0x00FE, 29490, 640, 13220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_65D4)

    CameraMove(29180, 1050, 14710, 2000)

    ChrTalk(
        0x0023,
        (
            '#1230200929V怎样，想马上\n',
            '试试鱼竿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200930V#1015F不，还不行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200931V还有些地方要去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200932V原来如此，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200933V这样的话，要不先去\n',
            '附近的钓鱼点看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200934V有个很近的好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200935V#1018F真的！？要去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_677D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200936V#552F……喂，不是要去找渡鸦帮\n',
            '问亡灵的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67BB')

    def _loc_677D(): pass

    label('loc_677D')

    ChrTalk(
        0x0103,
        (
            '#0030200937V#023F不是要去找渡鸦帮那帮小子\n',
            '问亡灵的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_67BB(): pass

    label('loc_67BB')

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x00F7, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010200938V#1008F我、我当然知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200939V就是，稍微\n',
            '绕个道而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6864',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200940V#551F唉，真没办法……\n',
            '赶快搞定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_689C')

    def _loc_6864(): pass

    label('loc_6864')

    ChrTalk(
        0x0103,
        (
            '#0030200941V#021F呵呵，真没办法呢。\n',
            '好吧，陪你去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_689C(): pass

    label('loc_689C')

    ChrTalk(
        0x0023,
        (
            '#1230200942V哈哈，不必担心。\n',
            '不会占用多少时间的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200943V那么，我带你们去吧。\n',
            '跟我来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0023, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200944V#1001F嗯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(19780, 0, 26480, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(96000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -1690, 0, 29190, 0)
    ChrSetPos(0x00F7, -880, 0, 28060, 0)
    ChrSetPos(0x0023, -310, 0, 29250, 0)

    @scena.Lambda('lambda_69AF')
    def lambda_69AF():
        CameraMove(-980, 0, 29260, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_69AF)

    @scena.Lambda('lambda_69C7')
    def lambda_69C7():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_69C7)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010200945V#1011F这里就是那个钓鱼点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200946V唔，仔细看水面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-1300, -2000, 34150, 2000)

    ChrTalk(
        0x0023,
        (
            '#1230200947V#1P看，有波纹吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200948V#1P出现波纹的地方\n',
            '就证明一定有鱼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200949V#1P在水边仔细找找就能看到了，\n',
            '到各处积极奔走寻找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200950V#1006FＯＫ。\n',
            '关键就是注意水面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-980, 0, 29260, 0)
    CameraSetDistance(2800, 0)
    OP_6E(262, 0)
    ChrTurnDirection(0x0101, 0x0023, 0)
    ChrTurnDirection(0x0023, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x0023,
        (
            '#1230200951V地点就是这样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200952V接着给你这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了５个',
            (TxtCtl.Item, ItemTable['海参']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['海参'], 5)

    ChrTalk(
        0x0023,
        (
            '#1230200953V这是钓鱼用的饵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200954V不过店里是买不到的，\n',
            '所以要自己弄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200955V魔兽经常会掉落，\n',
            '应该难不倒身为游击士的你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200956V#1018F啊，这真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200957V当前要说明的\n',
            '就是这些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200958V接下来就\n',
            '自己多多尝试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200959V#1006F嗯，知道了。\n',
            '谢谢您关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200960V不不，这也是\n',
            '『钓公师团』的职责嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#1230200961V那么，回头见。\n',
            '期待你出色的钓鱼成果哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6DA1')
    def lambda_6DA1():
        ChrTurnDirection(0x00FE, 0x0023, 400)
        Yield()

        Jump('lambda_6DA1')

    DispatchAsync2(0x0101, 0x0001, lambda_6DA1)

    @scena.Lambda('lambda_6DB2')
    def lambda_6DB2():
        ChrTurnDirection(0x00FE, 0x0023, 400)
        Yield()

        Jump('lambda_6DB2')

    DispatchAsync2(0x00F7, 0x0001, lambda_6DB2)

    @scena.Lambda('lambda_6DC3')
    def lambda_6DC3():
        OP_69(0x0101, 1500)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_6DC3)

    ChrSetFlags(0x0023, 0x0040)
    ChrWalkTo(0x0023, 150, 0, 28080, 2000, 0x00)
    ChrWalkTo(0x0023, 2710, 0, 28080, 2000, 0x00)
    ChrWalkTo(0x0023, 3530, 0, 28920, 2000, 0x00)
    ChrWalkTo(0x0023, 5300, 0, 29000, 2000, 0x00)
    ChrWalkTo(0x0023, 5950, -1800, 25240, 2000, 0x00)
    ChrSetFlags(0x0023, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    WaitForThreadExit(0x0025, 0x0001)
    OP_65(0x04, 0x0001)
    SetScenaFlags(ScenaFlag(0x0248, 2, 0x1242))
    EventEnd(0x00)

    Return()

# id: 0x001D offset: 0x6E50
@scena.Code('func_1D_6E50')
def func_1D_6E50():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6E9C',
    )

    ExecExpressionWithValue(
        0x0025,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF7, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF7, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0025,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF7, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_1D_6E50')

    def _loc_6E9C(): pass

    label('loc_6E9C')

    Return()

# id: 0x001E offset: 0x6E9D
@scena.Code('func_1E_6E9D')
def func_1E_6E9D():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6ED5')
    def lambda_6ED5():
        CameraMove(-1300, 0, 34150, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6ED5)

    @scena.Lambda('lambda_6EED')
    def lambda_6EED():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_6EED)

    @scena.Lambda('lambda_6EFD')
    def lambda_6EFD():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_6EFD)

    Sleep(1500)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FA2',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x101, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    OP_C0(0x0E, 0x00000018, 0xFFFFFC22, 0x00000000, 0x0000738C, 0x00000000, 0xFFFFFAEC, 0xFFFFF448, 0x00008566)

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()
    EventEnd(0x01)

    Jump('loc_6FB1')

    def _loc_6FA2(): pass

    label('loc_6FA2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FB1',
    )

    EventEnd(0x01)

    def _loc_6FB1(): pass

    label('loc_6FB1')

    Return()

# id: 0x001F offset: 0x6FB2
@scena.Code('func_1F_6FB2')
def func_1F_6FB2():
    OP_13(0x0069)

    Return()

# id: 0x0020 offset: 0x6FB6
@scena.Code('func_20_6FB6')
def func_20_6FB6():
    OP_13(0x0052)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
