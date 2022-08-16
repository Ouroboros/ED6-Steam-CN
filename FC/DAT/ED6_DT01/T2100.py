import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2100.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2100._SN', 'ED6_DT01/T2100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00006590,
            dword_04        = 0x00000000,
            dword_08        = 0x0001B580,
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT06/CH20159._CH', 'ED6_DT06/CH20159P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT07/CH00045._CH', 'ED6_DT07/CH00045P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT07/CH00045._CH', 'ED6_DT07/CH00045P._CP'),
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT06/CH20160._CH', 'ED6_DT06/CH20160P._CP'),
    ]

# id: 0x10001 offset: 0x1A2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奈尔',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
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
            name                = '克拉姆',
            x                   = 37220,
            z                   = 1700,
            y                   = -36830,
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
            name                = '穆拉德老人',
            x                   = 2420,
            z                   = -250,
            y                   = 94980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '特蕾莎院长',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
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
            name                = '利顿',
            x                   = -4300,
            z                   = 4000,
            y                   = 3300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '希艾尔',
            x                   = 1700,
            z                   = 0,
            y                   = 5200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 21800,
            z                   = 0,
            y                   = 73300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '兰达老人',
            x                   = 21000,
            z                   = 0,
            y                   = 74300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '米优',
            x                   = 20400,
            z                   = 0,
            y                   = 72900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '男性的声音',
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
            name                = '梅尔茨',
            x                   = 16600,
            z                   = -1800,
            y                   = 111000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 41290,
            z                   = -1970,
            y                   = 66200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '拜舍尔',
            x                   = 16430,
            z                   = -1800,
            y                   = 111960,
            direction           = 280,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 47400,
            z                   = 0,
            y                   = 81500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 45940,
            z                   = 0,
            y                   = 80850,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '雷加洛',
            x                   = 49870,
            z                   = 0,
            y                   = 79770,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '希尔碧',
            x                   = 49320,
            z                   = 0,
            y                   = 81240,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '鲁蓓',
            x                   = 31510,
            z                   = 0,
            y                   = 89810,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '阿杰',
            x                   = 29470,
            z                   = 0,
            y                   = 87520,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '玛奇尔达',
            x                   = 23580,
            z                   = 2160,
            y                   = 102820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '船',
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
            name                = '船',
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
            name                = '梅威海道方向',
            x                   = 25260,
            z                   = 0,
            y                   = 128199,
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
            name                = '卢安市·南街区',
            x                   = 51060,
            z                   = 400,
            y                   = 27190,
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
            name                = '卢安飞艇坪',
            x                   = 81750,
            z                   = 0,
            y                   = 80640,
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

# id: 0x10002 offset: 0x502
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x502
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 52790,
            y           = 2000,
            z           = 67850,
            range       = 49030,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x0000FD8E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 47550,
            y           = 2000,
            z           = 53890,
            range       = 55410,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x0000C33C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 35920,
            y           = 5000,
            z           = 88550,
            range       = 99180,
            dword_10    = 0xFFFFEC78,
            dword_14    = 0x0000FCEE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000022,
        ),
        ScenaEventData(
            x           = 27150,
            y           = 2000,
            z           = 78400,
            range       = 25490,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00011F80,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000025,
        ),
        ScenaEventData(
            x           = 44990,
            y           = 0,
            z           = 89330,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002C,
        ),
        ScenaEventData(
            x           = 38080,
            y           = 0,
            z           = 78540,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002D,
        ),
        ScenaEventData(
            x           = 37930,
            y           = 0,
            z           = 89380,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002E,
        ),
        ScenaEventData(
            x           = 30610,
            y           = 0,
            z           = 96060,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002E,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 108200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002F,
        ),
        ScenaEventData(
            x           = 20930,
            y           = -1500,
            z           = 93960,
            range       = 3500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000030,
        ),
        ScenaEventData(
            x           = 61000,
            y           = 0,
            z           = 78900,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000031,
        ),
        ScenaEventData(
            x           = 66890,
            y           = -500,
            z           = 93800,
            range       = 2200,
            dword_10    = 0x00000898,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000032,
        ),
        ScenaEventData(
            x           = 73630,
            y           = 0,
            z           = 80790,
            range       = 3500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000033,
        ),
    )

# id: 0x10004 offset: 0x6A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 13500,
            triggerZ            = 0,
            triggerY            = 73400,
            triggerRange        = 1000,
            actorX              = 13500,
            actorZ              = 1500,
            actorY              = 73400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23750,
            triggerZ            = 1000,
            triggerY            = 102860,
            triggerRange        = 1000,
            actorX              = 23580,
            actorZ              = 4000,
            actorY              = 102820,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_727',
    )

    ChrSetPos(0x0015, 14980, 0, 68500, 180)
    ChrSetPos(0x0018, 45320, 0, 82680, 270)
    ChrSetPos(0x0019, 43580, 0, 82680, 90)

    Jump('loc_A73')

    def _loc_727(): pass

    label('loc_727')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_764',
    )

    ChrSetPos(0x0015, 14980, 0, 68500, 180)
    ChrSetPos(0x0018, 51500, 1000, 103610, 270)
    ChrSetPos(0x0019, 51500, 1000, 102530, 270)

    Jump('loc_A73')

    def _loc_764(): pass

    label('loc_764')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_7CD',
    )

    ChrSetPos(0x0015, 14980, 0, 68500, 180)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0016, 13750, 0, 69100, 180)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, 12090, 0, 69000, 180)
    ChrSetPos(0x0018, 64440, 0, 89630, 280)
    ChrSetPos(0x0019, 65900, 0, 99540, 0)

    Jump('loc_A73')

    def _loc_7CD(): pass

    label('loc_7CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_885',
    )

    ChrSetPos(0x0015, 14980, 0, 68500, 180)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x0010, 26)
    TerminateThread(0x0010, 0x00)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetPos(0x0010, 42710, -1800, 69570, 270)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetChipByIndex(0x0011, 27)
    TerminateThread(0x0011, 0x00)
    ChrSetFlags(0x0011, 0x0010)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0011, 39480, -1800, 69500, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x000F, 28)
    TerminateThread(0x000F, 0x00)
    ChrSetFlags(0x000F, 0x0010)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetPos(0x000F, 36220, -1800, 69550, 180)
    ChrSetPos(0x0018, 45320, 0, 82680, 270)
    ChrSetPos(0x0019, 43580, 0, 82680, 90)

    Jump('loc_A73')

    def _loc_885(): pass

    label('loc_885')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_935',
    )

    ChrSetPos(0x0015, 10810, 0, 72960, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 46060, 0, 79390, 90)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 17800, 0, 73500, 90)
    ChrClearFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 48870, 0, 80920, 180)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 48270, 0, 78680, 180)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 49650, 0, 78980, 180)
    ChrSetPos(0x0018, 24590, 0, 69200, 135)
    ChrSetPos(0x0019, 22240, 0, 68440, 180)

    Jump('loc_A73')

    def _loc_935(): pass

    label('loc_935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_9F6',
    )

    ChrSetPos(0x0015, 10810, 0, 72960, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 45860, 0, 78450, 180)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 17800, 0, 73500, 90)
    ChrClearFlags(0x0013, 0x0080)
    CreateThread(0x0013, 0x00, 0x00, func_05_E71)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 18050, -1800, 111280, 270)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 18320, -1800, 113600, 225)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 18190, -1800, 110060, 270)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0018, 19630, 0, 72720, 270)
    ChrSetPos(0x0019, 20110, 0, 74150, 270)

    Jump('loc_A73')

    def _loc_9F6(): pass

    label('loc_9F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_A22',
    )

    ChrSetPos(0x0018, 47130, 0, 78430, 180)
    ChrSetPos(0x0019, 45970, 0, 78440, 180)

    Jump('loc_A73')

    def _loc_A22(): pass

    label('loc_A22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_A73',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 47840, 0, 78500, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 17800, 0, 73500, 90)
    ChrClearFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)

    def _loc_A73(): pass

    label('loc_A73')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0004)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A91',
    )

    OP_64(0x00, 0x0001)

    def _loc_A91(): pass

    label('loc_A91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_A9F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_1A_41CD)

    def _loc_A9F(): pass

    label('loc_A9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_AAD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_1E_48B5)

    def _loc_AAD(): pass

    label('loc_AAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_ABB',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_1F_51C7)

    def _loc_ABB(): pass

    label('loc_ABB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_AD2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_20_54A8)

    def _loc_AD2(): pass

    label('loc_AD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Return,
        ),
        'loc_AE0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    Event(0, func_24_5F88)

    def _loc_AE0(): pass

    label('loc_AE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Return,
        ),
        'loc_AF1',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    Event(0, func_27_7901)
    SetScenaFlags(ScenaFlag(0x0082, 2, 0x412))

    def _loc_AF1(): pass

    label('loc_AF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Return,
        ),
        'loc_B08',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    Event(0, func_26_741F)

    def _loc_B08(): pass

    label('loc_B08')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_B14'),
        (-1, 'loc_B39'),
    )

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 2, 0x412)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B23',
    )

    SetScenaFlags(ScenaFlag(0x0082, 2, 0x412))
    Event(0, func_17_3748)

    def _loc_B23(): pass

    label('loc_B23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 1, 0x429)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B36',
    )

    SetScenaFlags(ScenaFlag(0x0085, 1, 0x429))
    Event(0, func_21_5928)

    def _loc_B36(): pass

    label('loc_B36')

    Jump('loc_B39')

    def _loc_B39(): pass

    label('loc_B39')

    ExecExpressionWithValue(
        0x000C,
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

# id: 0x0001 offset: 0xB4B
@scena.Code('func_01_B4B')
def func_01_B4B():
    OP_16(0x02, 4000, -88000, -44000, 196679)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_B7E',
    )

    OP_B1('t2100_y')

    Jump('loc_B87')

    def _loc_B7E(): pass

    label('loc_B7E')

    OP_B1('t2100_n')

    def _loc_B87(): pass

    label('loc_B87')

    ChrSetBattleFlags(0x000A, 0x0020)
    OP_89(0x000A, -960, -2780, 92980, 135)
    OP_72(0x0012, 0x0002)
    OP_71(0x0012, 0x0400)
    OP_71(0x0012, 0x0040)

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0004)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BCA',
    )

    OP_64(0x00, 0x0001)

    def _loc_BCA(): pass

    label('loc_BCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_BD4',
    )

    Jump('loc_C71')

    def _loc_BD4(): pass

    label('loc_BD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_BEA',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x001A, 0x0002)

    Jump('loc_C71')

    def _loc_BEA(): pass

    label('loc_BEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_BF4',
    )

    Jump('loc_C71')

    def _loc_BF4(): pass

    label('loc_BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_C0F',
    )

    OP_1B(0x00, 0x00, 0x002B)
    OP_6F(0x0011, 1020)
    OP_72(0x001A, 0x0002)

    Jump('loc_C71')

    def _loc_C0F(): pass

    label('loc_C0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 2, 0x42A)),
            Expr.Return,
        ),
        'loc_C25',
    )

    OP_6F(0x0011, 1020)
    OP_72(0x001A, 0x0002)

    Jump('loc_C71')

    def _loc_C25(): pass

    label('loc_C25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_C2F',
    )

    Jump('loc_C71')

    def _loc_C2F(): pass

    label('loc_C2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_C3E',
    )

    OP_1B(0x00, 0x00, 0x002A)

    Jump('loc_C71')

    def _loc_C3E(): pass

    label('loc_C3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 1, 0x419)),
            Expr.Return,
        ),
        'loc_C59',
    )

    OP_1B(0x00, 0x00, 0x0029)
    OP_6F(0x0011, 1020)
    OP_72(0x001A, 0x0002)

    Jump('loc_C71')

    def _loc_C59(): pass

    label('loc_C59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_C71',
    )

    OP_1B(0x00, 0x00, 0x0028)
    OP_6F(0x0011, 1020)
    OP_72(0x001A, 0x0002)

    def _loc_C71(): pass

    label('loc_C71')

    If(
        (
            (Expr.PushValueByIndex, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C82',
    )

    PlaySE(453, 0x01, 0x64)

    def _loc_C82(): pass

    label('loc_C82')

    Return()

# id: 0x0002 offset: 0xC83
@scena.Code('func_02_C83')
def func_02_C83():
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
        'loc_CA8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_DEA')

    def _loc_CA8(): pass

    label('loc_CA8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC1',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_DEA')

    def _loc_CC1(): pass

    label('loc_CC1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CDA',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_DEA')

    def _loc_CDA(): pass

    label('loc_CDA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF3',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_DEA')

    def _loc_CF3(): pass

    label('loc_CF3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D0C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_DEA')

    def _loc_D0C(): pass

    label('loc_D0C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D25',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_DEA')

    def _loc_D25(): pass

    label('loc_D25')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D3E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_DEA')

    def _loc_D3E(): pass

    label('loc_D3E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D57',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_DEA')

    def _loc_D57(): pass

    label('loc_D57')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D70',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_DEA')

    def _loc_D70(): pass

    label('loc_D70')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D89',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_DEA')

    def _loc_D89(): pass

    label('loc_D89')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DA2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_DEA')

    def _loc_DA2(): pass

    label('loc_DA2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DBB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_DEA')

    def _loc_DBB(): pass

    label('loc_DBB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DD4',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_DEA')

    def _loc_DD4(): pass

    label('loc_DD4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DEA',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_DEA(): pass

    label('loc_DEA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DFF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_DEA')

    def _loc_DFF(): pass

    label('loc_DFF')

    Return()

# id: 0x0003 offset: 0xE00
@scena.Code('func_03_E00')
def func_03_E00():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E4C',
    )

    OP_99(0x00FE, 0x00, 0x03, 1500)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x3),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E2B',
    )

    Sleep(1000)

    Jump('loc_E49')

    def _loc_E2B(): pass

    label('loc_E2B')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E44',
    )

    Sleep(2000)

    Jump('loc_E49')

    def _loc_E44(): pass

    label('loc_E44')

    Sleep(3000)

    def _loc_E49(): pass

    label('loc_E49')

    Jump('func_03_E00')

    def _loc_E4C(): pass

    label('loc_E4C')

    Return()

# id: 0x0004 offset: 0xE4D
@scena.Code('func_04_E4D')
def func_04_E4D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E70',
    )

    OP_8D(0x00FE, 28870, 90550, 28960, 83580, 4000)

    Jump('func_04_E4D')

    def _loc_E70(): pass

    label('loc_E70')

    Return()

# id: 0x0005 offset: 0xE71
@scena.Code('func_05_E71')
def func_05_E71():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EE1',
    )

    ChrWalkTo(0x00FE, 16440, -1800, 109600, 3500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(2000)

    ChrWalkTo(0x00FE, 16530, -1800, 113090, 3500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(2000)

    Jump('func_05_E71')

    def _loc_EE1(): pass

    label('loc_EE1')

    Return()

# id: 0x0006 offset: 0xEE2
@scena.Code('func_06_EE2')
def func_06_EE2():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_FE8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F85',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '不管是爆发战争也好，\n',
            '市长被逮捕也罢，\n',
            '我还是会和平常一样生活……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且今后会出现什么情况\n',
            '也是未知的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算哀怨也无济于事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE5')

    def _loc_F85(): pass

    label('loc_F85')

    ChrTalk(
        0x00FE,
        (
            '不管是爆发战争也好，\n',
            '市长被逮捕也罢，\n',
            '我还是会和平常一样生活……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算哀怨也无济于事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FE5(): pass

    label('loc_FE5')

    Jump('loc_1880')

    def _loc_FE8(): pass

    label('loc_FE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_10C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1092',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '最近的年轻人处理事情\n',
            '都显得太马马虎虎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该要先了解在这世上\n',
            '什么事情才值得在第一时间完成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我活了这几十年\n',
            '所领悟出来的真理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C3')

    def _loc_1092(): pass

    label('loc_1092')

    ChrTalk(
        0x00FE,
        (
            '最近的年轻人处理事情\n',
            '都显得太马马虎虎了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C3(): pass

    label('loc_10C3')

    Jump('loc_1880')

    def _loc_10C6(): pass

    label('loc_10C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1182',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1161',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '水真是不可思议的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每个时候都会有\n',
            '不同的表情呈现出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这几十年来我一直这样看着这片水面，\n',
            '一天也没有感到过厌倦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_117F')

    def _loc_1161(): pass

    label('loc_1161')

    ChrTalk(
        0x00FE,
        (
            '水真是不可思议的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_117F(): pass

    label('loc_117F')

    Jump('loc_1880')

    def _loc_1182(): pass

    label('loc_1182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 3, 0x42B)),
            Expr.Return,
        ),
        'loc_1235',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11FD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '是你们几个啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '只要小船能帮上你们的忙就好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次希望你们\n',
            '能来尽兴地玩一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1232')

    def _loc_11FD(): pass

    label('loc_11FD')

    ChrTalk(
        0x00FE,
        (
            '是你们几个啊……\n',
            '下次希望你们能来尽兴地玩一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1232(): pass

    label('loc_1232')

    Jump('loc_1880')

    def _loc_1235(): pass

    label('loc_1235')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 3, 0x42B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 2, 0x42A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17AF',
    )

    SetScenaFlags(ScenaFlag(0x0085, 3, 0x42B))
    OP_28(0x003C, 0x01, 0x0010)
    EventBegin(0x00)
    OP_69(0x00FE, 1000)

    ChrTalk(
        0x00FE,
        (
            '#1520050608V唔……？\n',
            '怎么了，你们几个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050609V#002F这船可以租给我们吗！？\n',
            '我们急着要去对岸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520050610V很遗憾，\n',
            '这船已经被那个什么公爵给订下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520050611V他等一下好像要乘船戏水……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050612V#003F怎、怎么会这样～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050613V#043F拜托了……\n',
            '请您一定要帮帮我们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050614V如果我们不快点过去的话， \n',
            '有个小男孩可能会遇到危险呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0136, 400)

    ChrTalk(
        0x00FE,
        (
            '#1520050615V哎呀呀，别哭别哭。\n',
            '一看到小姑娘哭我就想起自己孙女来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520050616V好了，船先借给你们吧。\n',
            '总之救人要紧嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520050617V快点上来开船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050618V#048F谢、谢谢您！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050619V#006F老爷爷，谢谢您哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1520050620V呵呵，反正我会跟公爵说\n',
            '这船还在维修当中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1520050621V小子，你会开船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050622V#012F嗯，还可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050623V你们两个快上船吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6C(45000, 0)
    CameraMove(-740, -2260, 92790, 0)
    ChrSetPos(0x001E, -810, -2850, 92590, 90)
    ChrSetFlags(0x001E, 0x0040)
    OP_A1(0x001E, 0x0012)
    OP_72(0x0012, 0x0004)
    OP_72(0x0012, 0x0002)
    OP_71(0x0012, 0x0400)
    OP_71(0x0012, 0x0040)
    Yield()
    Sleep(1)

    ChrSetBattleFlags(0x0000, 0x0020)
    ChrSetBattleFlags(0x0001, 0x0020)
    ChrSetBattleFlags(0x0002, 0x0020)
    ChrClearFlags(0x0000, 0x0004)
    ChrClearFlags(0x0001, 0x0004)
    ChrClearFlags(0x0002, 0x0004)
    ChrSetPos(0x0102, 300, -2760, 92400, 45)
    ChrSetPos(0x0101, -980, -2750, 92300, 270)
    ChrSetPos(0x0136, -1000, -2750, 93000, 270)
    ChrSetFlags(0x0000, 0x0020)
    ChrSetFlags(0x0001, 0x0020)
    ChrSetFlags(0x0002, 0x0020)
    ChrClearBattleFlags(0x000A, 0x0020)
    ChrSetPos(0x000A, -760, -2260, 94400, 180)

    @scena.Lambda('lambda_1642')
    def lambda_1642():
        ChrTurnDirection(0x00FE, 0x0136, 0)
        Yield()

        Jump('lambda_1642')

    DispatchAsync2(0x000A, 0x0001, lambda_1642)

    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    PlaySE(146, 0x00, 0x64)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlayEffect(0x04, 0x00, 0x001E, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x01, 0x001E, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_16FE')
    def lambda_16FE():
        ChrMoveTo(0x00FE, -19660, -2500, 93230, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_16FE)

    Sleep(500)

    @scena.Lambda('lambda_171E')
    def lambda_171E():
        ChrMoveTo(0x00FE, -19660, -2500, 93230, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_171E)

    Sleep(500)

    @scena.Lambda('lambda_173E')
    def lambda_173E():
        ChrMoveTo(0x00FE, -19660, -2500, 93230, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_173E)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_24(0x0092, 0x5A)
    Sleep(100)

    OP_24(0x0092, 0x50)
    Sleep(100)

    OP_24(0x0092, 0x46)
    Sleep(100)

    OP_24(0x0092, 0x3C)
    Sleep(100)

    OP_24(0x0092, 0x32)
    Sleep(100)

    OP_24(0x0092, 0x28)
    Sleep(100)

    OP_24(0x0092, 0x1E)
    Sleep(100)

    OP_23(0x0092)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1880')

    def _loc_17AF(): pass

    label('loc_17AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1801',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安很早以前\n',
            '就被称为水上之都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理由显而易见。\n',
            '谁都能明白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1880')

    def _loc_1801(): pass

    label('loc_1801')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_1861',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的晚霞\n',
            '依旧是这么美丽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再没有什么地方比卢安\n',
            '更加配得上晚霞的美景了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1880')

    def _loc_1861(): pass

    label('loc_1861')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1880',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么了，要坐船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1880(): pass

    label('loc_1880')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1884
@scena.Code('func_07_1884')
def func_07_1884():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_192D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18F9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '本酒店也为各位\n',
            '准备了一艘小船，\n',
            '大家可以泛舟眺望卢安的街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请务必游览一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)

    Jump('loc_192A')

    def _loc_18F9(): pass

    label('loc_18F9')

    ChrTalk(
        0x00FE,
        (
            '很抱歉，请不要打扰我。\n',
            '现在我正在招待旅客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_192A(): pass

    label('loc_192A')

    Jump('loc_1AE9')

    def _loc_192D(): pass

    label('loc_192D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_19DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19BB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '嗯，下午的安排是\n',
            '带客人们去参观艾尔·雷登……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为是以体味大海为主题的旅游，\n',
            '晚饭还是在拉旺塔尔解决吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)

    Jump('loc_19DA')

    def _loc_19BB(): pass

    label('loc_19BB')

    ChrTalk(
        0x00FE,
        (
            '很抱歉，\n',
            '现在我正忙着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19DA(): pass

    label('loc_19DA')

    Jump('loc_1AE9')

    def _loc_19DD(): pass

    label('loc_19DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1AE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '各位，请看一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在可以在我的左手边看到\n',
            '海港都市卢安的标志——\n',
            '伦格兰德大桥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '降下的时候，\n',
            '开合桥的全长约为１０９亚矩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将桥吊起的机器是\n',
            '蔡斯中央工房制造的\n',
            '特制导力引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)

    Jump('loc_1AE9')

    def _loc_1AB8(): pass

    label('loc_1AB8')

    ChrTalk(
        0x00FE,
        (
            '很抱歉，请不要打扰我。\n',
            '现在我正在招待旅客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AE9(): pass

    label('loc_1AE9')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0x1AED
@scena.Code('func_08_1AED')
def func_08_1AED():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1B51',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然马上就要到儿子学校的学园祭了，\n',
            '但是我工作很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道能不能请到假……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C5C')

    def _loc_1B51(): pass

    label('loc_1B51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_1C2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BE4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '这里的灯塔是在大约４０年，\n',
            '也就是和伦格兰德大桥\n',
            '同时期建造起来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是这个城市\n',
            '免遭战火摧残的建筑物之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000E, 0x0010)

    Jump('loc_1C29')

    def _loc_1BE4(): pass

    label('loc_1BE4')

    ChrTalk(
        0x00FE,
        (
            '今天放弃休假继续工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女儿能够帮忙做家务\n',
            '真是替我分忧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C29(): pass

    label('loc_1C29')

    Jump('loc_1C5C')

    def _loc_1C2C(): pass

    label('loc_1C2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1C5C',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '然后就是带领各位去酒店了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C5C(): pass

    label('loc_1C5C')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x1C60
@scena.Code('func_09_1C60')
def func_09_1C60():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D22',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0013,
        (
            '唔～\n',
            '您的假牙就是掉在这附近的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不素不素，\n',
            '在靠今海便那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '什么？在海面上？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '偶素说在海便！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '唔……\n',
            '我听不懂啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0013, 0x0010)
    ChrClearFlags(0x0010, 0x0010)

    Jump('loc_1D5C')

    def _loc_1D22(): pass

    label('loc_1D22')

    ChrTalk(
        0x00FE,
        (
            '这样的话，\n',
            '我就跳下去一点一点找，\n',
            '直到把假牙找回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D5C(): pass

    label('loc_1D5C')

    TalkEnd(0x0013)

    Return()

# id: 0x000A offset: 0x1D60
@scena.Code('func_0A_1D60')
def func_0A_1D60():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E0A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '好吧……\n',
            '今天没什么事干，\n',
            '就放松一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人们一提到柏斯的商人，\n',
            '总是说他们\n',
            '日夜不停地工作工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要真是那样的话，\n',
            '身体怎么可能受得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E3A')

    def _loc_1E0A(): pass

    label('loc_1E0A')

    ChrTalk(
        0x00FE,
        (
            '好吧……\n',
            '今天没什么事干，\n',
            '就放松一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E3A(): pass

    label('loc_1E3A')

    TalkEnd(0x0014)

    Return()

# id: 0x000B offset: 0x1E3E
@scena.Code('func_0B_1E3E')
def func_0B_1E3E():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1EA9',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来我打算\n',
            '到蔡斯地区去钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是第一次去蔡斯，\n',
            '不知道会钓到什么，真是期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_240A')

    def _loc_1EA9(): pass

    label('loc_1EA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1FF8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FC8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '即使在同一个钓鱼场，\n',
            '按照同样的钓鱼方式，\n',
            '也不见得就会钓到相同的猎物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常分析每天的状况，\n',
            '从而得出自己的结论是非常有必要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个结论谁也不会告诉你。\n',
            '要自己经常去探索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那才正是垂钓的\n',
            '真正乐趣所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我的意思可不是说\n',
            '这样就无法钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FF5')

    def _loc_1FC8(): pass

    label('loc_1FC8')

    ChrTalk(
        0x00FE,
        (
            '……我的意思可不是说\n',
            '这样就无法钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FF5(): pass

    label('loc_1FF5')

    Jump('loc_240A')

    def _loc_1FF8(): pass

    label('loc_1FF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_203F',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管名人怎么有名，\n',
            '钓不到的时候就是钓不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_240A')

    def _loc_203F(): pass

    label('loc_203F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_20E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '对垂钓来说，\n',
            '地点的选择也是非常重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在鱼游不到的地方\n',
            '一直守着不动也是没有用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20DF')

    def _loc_20B2(): pass

    label('loc_20B2')

    ChrTalk(
        0x00FE,
        (
            '对垂钓来说，\n',
            '地点的选择也是非常重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20DF(): pass

    label('loc_20DF')

    Jump('loc_240A')

    def _loc_20E2(): pass

    label('loc_20E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_212B',
    )

    ChrTalk(
        0x00FE,
        (
            '嘘——！\n',
            '请千万不要发出响声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为鱼对声音特别敏感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_240A')

    def _loc_212B(): pass

    label('loc_212B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2186',
    )

    ChrTalk(
        0x00FE,
        (
            '我不知道你们在急什么，\n',
            '不过请千万不要发出响声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为鱼对声音特别敏感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_240A')

    def _loc_2186(): pass

    label('loc_2186')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2285',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2231',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '今天的钓鱼成果只是一般啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '仅仅满足于此可不是我的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一定会超过纪录，\n',
            '钓到大鱼给你们看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赌上我们『钓公师团』的名声！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2282')

    def _loc_2231(): pass

    label('loc_2231')

    ChrTalk(
        0x00FE,
        (
            '我一定会钓到一条大鱼，\n',
            '破个纪录给你们看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赌上我们『钓公师团』的名声！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2282(): pass

    label('loc_2282')

    Jump('loc_240A')

    def _loc_2285(): pass

    label('loc_2285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2360',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2319',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '现在这个时候——\n',
            '也就是傍晚时分，\n',
            '正是鱼儿们特别活跃的时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '当然这也是鱼儿最容易上钩的时候哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_235D')

    def _loc_2319(): pass

    label('loc_2319')

    ChrTalk(
        0x00FE,
        (
            '现在这个时候——\n',
            '也就是傍晚时分，\n',
            '正是鱼儿们特别活跃的时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_235D(): pass

    label('loc_235D')

    Jump('loc_240A')

    def _loc_2360(): pass

    label('loc_2360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_240A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23D3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '千里迢～迢\n',
            '来到～这～水上之都～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，在亚瑟利亚湾的某处\n',
            '有一只传说中的庞然大物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_240A')

    def _loc_23D3(): pass

    label('loc_23D3')

    ChrTalk(
        0x00FE,
        (
            '唔，在亚瑟利亚湾的某处\n',
            '有一只传说中的庞然大物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_240A(): pass

    label('loc_240A')

    TalkEnd(0x0015)

    Return()

# id: 0x000C offset: 0x240E
@scena.Code('func_0C_240E')
def func_0C_240E():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2481',
    )

    ChrTalk(
        0x00FE,
        (
            '在翻烂了导游手册之后，\n',
            '我决定今天就在这儿吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲和女儿对这里也很满意，\n',
            '真让我高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D1')

    def _loc_2481(): pass

    label('loc_2481')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_24C5',
    )

    ChrTalk(
        0x00FE,
        (
            '看着这座桥，\n',
            '我再次感到导力器的发明\n',
            '真的是太厉害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D1')

    def _loc_24C5(): pass

    label('loc_24C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2512',
    )

    ChrTalk(
        0x00FE,
        (
            '你们怎么了，这么慌张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说，\n',
            '你们找刚才的男孩子有事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D1')

    def _loc_2512(): pass

    label('loc_2512')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_253F',
    )

    ChrTalk(
        0x00FE,
        (
            '父亲不小心\n',
            '把假牙掉到海里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D1')

    def _loc_253F(): pass

    label('loc_253F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_25D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25A4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我带着父亲和女儿\n',
            '来卢安旅游……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，但是我必须\n',
            '随时盯住他们两个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D1')

    def _loc_25A4(): pass

    label('loc_25A4')

    ChrTalk(
        0x00FE,
        (
            '如果没有我在的话，\n',
            '真不知道会怎么样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25D1(): pass

    label('loc_25D1')

    TalkEnd(0x000F)

    Return()

# id: 0x000D offset: 0x25D5
@scena.Code('func_0D_25D5')
def func_0D_25D5():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_25FA',
    )

    ChrTalk(
        0x00FE,
        (
            '这还真是特等席啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A5')

    def _loc_25FA(): pass

    label('loc_25FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2620',
    )

    ChrTalk(
        0x00FE,
        (
            '真是一座富有生命的桥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A5')

    def _loc_2620(): pass

    label('loc_2620')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2669',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2639',
    )

    TalkEnd(0x0010)
    Call(0, 0x0009)

    Jump('loc_2666')

    def _loc_2639(): pass

    label('loc_2639')

    ChrTalk(
        0x00FE,
        (
            '真素的……\n',
            '真不番便……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶地牙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2666(): pass

    label('loc_2666')

    Jump('loc_26A5')

    def _loc_2669(): pass

    label('loc_2669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_26A5',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈，原来如此原来如此。\n',
            '王国军也非常有创意嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A5(): pass

    label('loc_26A5')

    TalkEnd(0x0010)

    Return()

# id: 0x000E offset: 0x26A9
@scena.Code('func_0E_26A9')
def func_0E_26A9():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_270A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，好舒服～！\n',
            '要在这种地方吃饭吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然知道这么好的饭店，\n',
            '爸爸真是不赖！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27A5')

    def _loc_270A(): pass

    label('loc_270A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_272C',
    )

    ChrTalk(
        0x00FE,
        (
            '真厉害，太厉害了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27A5')

    def _loc_272C(): pass

    label('loc_272C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_277F',
    )

    ChrTalk(
        0x00FE,
        (
            '在旅游中遇到困难的话，\n',
            '还是要找游击士协会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在外国也没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27A5')

    def _loc_277F(): pass

    label('loc_277F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_27A5',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸他呀，\n',
            '总是提不起劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27A5(): pass

    label('loc_27A5')

    TalkEnd(0x0011)

    Return()

# id: 0x000F offset: 0x27A9
@scena.Code('func_0F_27A9')
def func_0F_27A9():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_2808',
    )

    ChrTalk(
        0x00FE,
        (
            '一开始我就在热切期待了，\n',
            '学园祭果然很有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小摊上的食物\n',
            '又便宜又好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_284A')

    def _loc_2808(): pass

    label('loc_2808')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_284A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然我在明信片上看到过，\n',
            '但这还是我第一次看到实物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_284A(): pass

    label('loc_284A')

    TalkEnd(0x0016)

    Return()

# id: 0x0010 offset: 0x284E
@scena.Code('func_10_284E')
def func_10_284E():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_2903',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28EA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '那出剧真是杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然最开始男女角色反串演出\n',
            '有些让人感到奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是马上就能被这个故事本身吸引住，\n',
            '真是不可思议呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2900')

    def _loc_28EA(): pass

    label('loc_28EA')

    ChrTalk(
        0x00FE,
        (
            '那出剧真是杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2900(): pass

    label('loc_2900')

    Jump('loc_2920')

    def _loc_2903(): pass

    label('loc_2903')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2920',
    )

    ChrTalk(
        0x00FE,
        (
            '这可真是壮观……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2920(): pass

    label('loc_2920')

    TalkEnd(0x0017)

    Return()

# id: 0x0011 offset: 0x2924
@scena.Code('func_11_2924')
def func_11_2924():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_294B',
    )

    ChrTalk(
        0x00FE,
        (
            '街上在吵闹什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_294B(): pass

    label('loc_294B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2982',
    )

    ChrTalk(
        0x00FE,
        (
            '如果随便借走那艘船的话，\n',
            '估计会被骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_2982(): pass

    label('loc_2982')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_29DC',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的弥撒，\n',
            '卢安的市长也来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是位非常\n',
            '威严且沉着冷静的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_29DC(): pass

    label('loc_29DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2A06',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来去哪个地方看看呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_2A06(): pass

    label('loc_2A06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2A60',
    )

    ChrTalk(
        0x00FE,
        (
            '绀碧之空与海之缝隙中\n',
            '漂浮着的白色街道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安真是个\n',
            '美丽的城市啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_2A60(): pass

    label('loc_2A60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2A8D',
    )

    ChrTalk(
        0x00FE,
        (
            '这里也残留着\n',
            '百日战役的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_2A8D(): pass

    label('loc_2A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2AE3',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '幸好我事先问了拉桥的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到这么大的东西\n',
            '也能动起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B00')

    def _loc_2AE3(): pass

    label('loc_2AE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2B00',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……这真厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B00(): pass

    label('loc_2B00')

    TalkEnd(0x0018)

    Return()

# id: 0x0012 offset: 0x2B04
@scena.Code('func_12_2B04')
def func_12_2B04():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2B2B',
    )

    ChrTalk(
        0x00FE,
        (
            '是不是出什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2B2B(): pass

    label('loc_2B2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2B83',
    )

    ChrTalk(
        0x00FE,
        (
            '如果要租船的话\n',
            '应该到哪里去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果去问游击士协会\n',
            '他们会告诉我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2B83(): pass

    label('loc_2B83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_2BBF',
    )

    ChrTalk(
        0x00FE,
        (
            '真不愧是传说中的水之教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常浪漫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2BBF(): pass

    label('loc_2BBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2BF4',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安这个地方\n',
            '值得一看的地方还真多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2BF4(): pass

    label('loc_2BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2C57',
    )

    ChrTalk(
        0x00FE,
        (
            '在水上还真是不可思议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得能从生活中解放自己，\n',
            '这里给了我安逸祥和的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2C57(): pass

    label('loc_2C57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2C94',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然景色很漂亮，\n',
            '但是也向人传达了悲惨的历史。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2C94(): pass

    label('loc_2C94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2CCB',
    )

    ChrTalk(
        0x00FE,
        (
            '伫立在夕阳中的\n',
            '大桥的风景也非常美丽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CEC')

    def _loc_2CCB(): pass

    label('loc_2CCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_2CEC',
    )

    ChrTalk(
        0x00FE,
        (
            '比想象中的要大呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CEC(): pass

    label('loc_2CEC')

    TalkEnd(0x0019)

    Return()

# id: 0x0013 offset: 0x2CF0
@scena.Code('func_13_2CF0')
def func_13_2CF0():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_2D72',
    )

    ChrTalk(
        0x00FE,
        (
            '《利贝尔通讯》\n',
            '刊登的事情是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道市长\n',
            '真的是纵火犯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他平时的为人\n',
            '并不是令人十分爱戴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2D72(): pass

    label('loc_2D72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2DAD',
    )

    ChrTalk(
        0x00FE,
        (
            '港口的负责人波尔多斯\n',
            '是一个非常有声望的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2DAD(): pass

    label('loc_2DAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_2DF0',
    )

    ChrTalk(
        0x00FE,
        (
            '已经这个时候了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多该回家\n',
            '准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2DF0(): pass

    label('loc_2DF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_2E5A',
    )

    ChrTalk(
        0x00FE,
        (
            '玛西亚孤儿院被人放火，\n',
            '犯人真是过分了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的孩子们\n',
            '好像和我的女儿差不多年龄呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2E5A(): pass

    label('loc_2E5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_2EC6',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才的那个男孩子……\n',
            '他的妈妈好像来接他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道发生了什么，\n',
            '不过这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2EC6(): pass

    label('loc_2EC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2F07',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '有个男孩子飞奔过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2F07(): pass

    label('loc_2F07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_2F60',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，观光客增加了许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要仓库里那群家伙们\n',
            '不要惹出什么麻烦来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2F60(): pass

    label('loc_2F60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_2FAC',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '已经到这个时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快把东西买好，\n',
            '然后回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3009')

    def _loc_2FAC(): pass

    label('loc_2FAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_3009',
    )

    ChrTalk(
        0x00FE,
        (
            '空贼终于被抓住了，\n',
            '我也回到了久违的故乡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是\n',
            '卢安清爽的空气最宜人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3009(): pass

    label('loc_3009')

    TalkEnd(0x001A)

    Return()

# id: 0x0014 offset: 0x300D
@scena.Code('func_14_300D')
def func_14_300D():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3046',
    )

    ChrTalk(
        0x00FE,
        (
            '市长干了坏事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长不是个好人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3292')

    def _loc_3046(): pass

    label('loc_3046')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_309B',
    )

    ChrTalk(
        0x00FE,
        (
            '我好期待下一次的主日学校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又可以见到朋友了，\n',
            '而且神父也很有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3292')

    def _loc_309B(): pass

    label('loc_309B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_30C6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，今天玩得很尽兴哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3292')

    def _loc_30C6(): pass

    label('loc_30C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_3185',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_313A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '姐姐的制服，\n',
            '看上去真是可爱呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F呵呵，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果主日学校\n',
            '也有制服就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3182')

    def _loc_313A(): pass

    label('loc_313A')

    ChrTalk(
        0x00FE,
        (
            '姐姐的制服，\n',
            '看上去真是可爱呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果主日学校\n',
            '也有制服就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3182(): pass

    label('loc_3182')

    Jump('loc_3292')

    def _loc_3185(): pass

    label('loc_3185')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Return,
        ),
        'loc_31B0',
    )

    ChrTalk(
        0x00FE,
        (
            '可不能让妈妈\n',
            '为自己担心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3292')

    def _loc_31B0(): pass

    label('loc_31B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_3218',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31F2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '喂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在大街上这样奔跑\n',
            '是很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3215')

    def _loc_31F2(): pass

    label('loc_31F2')

    ChrTalk(
        0x00FE,
        (
            '在大街上这样奔跑\n',
            '是很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3215(): pass

    label('loc_3215')

    Jump('loc_3292')

    def _loc_3218(): pass

    label('loc_3218')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_3245',
    )

    ChrTalk(
        0x00FE,
        (
            '不要一个人\n',
            '到大桥的对面去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3292')

    def _loc_3245(): pass

    label('loc_3245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_3269',
    )

    ChrTalk(
        0x00FE,
        (
            '我的肚子已经饿扁了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3292')

    def _loc_3269(): pass

    label('loc_3269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_3292',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我正在和妈妈一起玩呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3292(): pass

    label('loc_3292')

    TalkEnd(0x001B)

    Return()

# id: 0x0015 offset: 0x3296
@scena.Code('func_15_3296')
def func_15_3296():
    Call(0, 0x0016)

    Return()

# id: 0x0016 offset: 0x329B
@scena.Code('func_16_329B')
def func_16_329B():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3306',
    )

    ChrTalk(
        0x001C,
        (
            '如果就这样无所事事度过自己的一生，\n',
            '那真是不幸啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '因此我们一定要\n',
            '好好活下去才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3744')

    def _loc_3306(): pass

    label('loc_3306')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3345',
    )

    ChrTalk(
        0x001C,
        (
            '……为什么在无法回来的时候\n',
            '才会看到它的光芒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3744')

    def _loc_3345(): pass

    label('loc_3345')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_3437',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 3, 0x4CB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3418',
    )

    SetScenaFlags(ScenaFlag(0x0099, 3, 0x4CB))

    ChrTalk(
        0x001C,
        (
            '我知道很唐突，\n',
            '不过这本书还是送给你们吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0216, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第５卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x001C,
        (
            '……问我为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '因为人生充满矛盾，\n',
            '是非常捉摸不透的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3434')

    def _loc_3418(): pass

    label('loc_3418')

    ChrTalk(
        0x001C,
        (
            '……在这里看夕阳真美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3434(): pass

    label('loc_3434')

    Jump('loc_3744')

    def _loc_3437(): pass

    label('loc_3437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_355B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34ED',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x001C,
        (
            '……卢安是个很大的城市哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '众多来往的人们，\n',
            '各自交错的人生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '在那之中，\n',
            '有时候会觉得自己好像是一颗\n',
            '被丢弃在路边的小石子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '这是为什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3558')

    def _loc_34ED(): pass

    label('loc_34ED')

    ChrTalk(
        0x001C,
        (
            '众多来往的人们，\n',
            '各自交错的人生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '在那之中，\n',
            '有时候会觉得自己好像是一颗\n',
            '被丢弃在路边的小石子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3558(): pass

    label('loc_3558')

    Jump('loc_3744')

    def _loc_355B(): pass

    label('loc_355B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_35AE',
    )

    ChrTalk(
        0x001C,
        (
            '蓝天的彼方，\n',
            '星星是否在闪耀呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '……啊啊，太远了，我看不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3744')

    def _loc_35AE(): pass

    label('loc_35AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_36D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3681',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x001C,
        (
            '鸟啊，鸟儿们啊，你们飞向哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '展开庞大的翅膀，\n',
            '向着未知的大地飞去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '在天空之中\n',
            '它们显得如此渺小，\n',
            '却又为何是如此坚强的生物呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我也想像它们那样\n',
            '自由自在地生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D0')

    def _loc_3681(): pass

    label('loc_3681')

    ChrTalk(
        0x001C,
        (
            '鸟啊，鸟儿们啊，你们飞向哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '我也想像它们那样\n',
            '自由自在地生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36D0(): pass

    label('loc_36D0')

    Jump('loc_3744')

    def _loc_36D3(): pass

    label('loc_36D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Return,
        ),
        'loc_371C',
    )

    ChrTalk(
        0x001C,
        (
            '啊啊……\n',
            '我仿佛要被夕阳射穿了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '不行，太耀眼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3744')

    def _loc_371C(): pass

    label('loc_371C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_3744',
    )

    ChrTalk(
        0x001C,
        (
            '呵呵……\n',
            '欢迎来到水上之都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3744(): pass

    label('loc_3744')

    TalkEnd(0x001C)

    Return()

# id: 0x0017 offset: 0x3748
@scena.Code('func_17_3748')
def func_17_3748():
    EventBegin(0x00)
    OP_67(0, 5600, -10000, 0)
    OP_6C(315000, 0)
    CameraSetDistance(6800, 0)
    CameraMove(52424, 0, 68700, 0)
    OP_12(0x00009470, 0x00030D40, 0x00000000)
    ChrSetPos(0x0101, 25470, 0, 115060, 180)
    ChrSetPos(0x0102, 24790, 0, 116060, 180)
    ChrSetPos(0x0136, 26160, 0, 116640, 180)

    @scena.Lambda('lambda_37C4')
    def lambda_37C4():
        OP_6C(45000, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37C4)

    Sleep(5000)

    @scena.Lambda('lambda_37D9')
    def lambda_37D9():
        OP_67(0, 9500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37D9)

    @scena.Lambda('lambda_37F1')
    def lambda_37F1():
        CameraSetDistance(2800, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_37F1)

    @scena.Lambda('lambda_3801')
    def lambda_3801():
        CameraMove(25850, 0, 115000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3801)

    OP_12(0x00009470, 0x00014C08, 0x00001F40)
    Sleep(8000)

    ChrTalk(
        0x0101,
        (
            '#0010040914V#501F哇～……\n',
            '这里就是卢安市啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040915V真是个好漂亮的城市呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040916V#010F蓝色的大海，白色的建筑……\n',
            '真是眩目的对比。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040917V的确是海港都市的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040918V#041F呵呵，\n',
            '这里有很多值得一看的地方呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040919V这附近就有一个\n',
            '竖立着灯台的海边小公园。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040920V街道后面就是教堂，\n',
            '那里的建筑风格也十分独特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040921V#040F还有，最值得一看的地方\n',
            '也许就要数『伦格兰德大桥』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_39E0')
    def lambda_39E0():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_39E0)

    Sleep(200)

    @scena.Lambda('lambda_39F3')
    def lambda_39F3():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39F3)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010040922V#000F#4P『伦格兰德大桥』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040923V#040F是连接这里\n',
            '与对岸南街区的大桥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040924V那是一座\n',
            '装有卷轴装置的开合桥哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040925V#010F#3P开合桥吗……\n',
            '听起来挺有意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040926V#040F对了，\n',
            '游击士协会就在这个北街区的中央。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040927V正好在大桥的前面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040928V#006F#4PＯＫ～\n',
            '就先去那边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x3B5E
@scena.Code('func_18_3B5E')
def func_18_3B5E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 5, 0x445)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C8F',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushValueByIndex, 0x64),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0088, 5, 0x445))
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrTurnDirection(0x0136, 0x0000, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040929V#040F啊，游击士协会支部就在这个街区。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040930V看，就是那幢建筑物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0136, 0, 400)

    @scena.Lambda('lambda_3BEF')
    def lambda_3BEF():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3BEF)

    @scena.Lambda('lambda_3BFD')
    def lambda_3BFD():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3BFD)

    @scena.Lambda('lambda_3C0B')
    def lambda_3C0B():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_3C0B)

    CameraMove(44460, 0, 92190, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010040931V#501F#1P啊，真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_69(0x0000, 0)

    ExecExpressionWithVar(
        0x64,
        (
            (Expr.PushReg, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020040932V#010F我们赶快过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CEC')

    def _loc_3C8F(): pass

    label('loc_3C8F')

    EventBegin(0x01)
    ChrTurnDirection(0x0136, 0x0000, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040933V#040F游击士协会支部就在这个街区。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040934V就是那幢建筑物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CEC(): pass

    label('loc_3CEC')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3D07(): pass

    label('loc_3D07')

    Return()

# id: 0x0019 offset: 0x3D08
@scena.Code('func_19_3D08')
def func_19_3D08():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 5, 0x415)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41CC',
    )

    SetScenaFlags(ScenaFlag(0x0082, 5, 0x415))
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0136,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0136,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040973V#004F呜哇……\n',
            '这就是伦格兰德大桥吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_3D91')
    def lambda_3D91():
        OP_6C(90000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D91)

    @scena.Lambda('lambda_3DA1')
    def lambda_3DA1():
        OP_67(0, 6115, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3DA1)

    @scena.Lambda('lambda_3DB9')
    def lambda_3DB9():
        CameraSetDistance(7760, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3DB9)

    @scena.Lambda('lambda_3DC9')
    def lambda_3DC9():
        CameraMove(51680, 400, 52400, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3DC9)

    OP_12(0x00009470, 0x0003D090, 0x00001770)
    ChrSetDirection(0x0102, 270, 400)

    @scena.Lambda('lambda_3DF5')
    def lambda_3DF5():
        ChrSetDirection(0x0136, 270, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_3DF5)

    Sleep(9000)

    Fade(1000)
    OP_6C(45000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    CameraMove(48350, 400, 52340, 0)
    OP_12(0x00009470, 0x00014C08, 0x00000000)
    ChrSetPos(0x0101, 49512, 400, 51770, 270)
    ChrSetPos(0x0102, 49512, 400, 50400, 270)
    ChrSetPos(0x0136, 49512, 400, 53040, 270)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040974V#501F真的是好大哦。\n',
            '恐怕有威尔特桥的几倍大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040975V#040F听说这座桥是在\n',
            '大约４０年前建造的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040976V在那之前，\n',
            '这里的市民一直是用渡船来往于两岸的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040977V#004F哎……？\n',
            '那为什么不早点建座大桥呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040978V#010F是因为卢比诺川是连接\n',
            '大海与瓦雷利亚湖的唯一河流吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040979V要是去位于湖畔的王都时，\n',
            '船被大桥挡住可就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040980V#041F没错，完全正确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040981V直到５０年前，\n',
            '因为导力革命的出现，\n',
            '才让建造这种大规模的开合桥成为了可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040982V#501F原来是这样啊……\n',
            '导力器真是神通广大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040983V#001F话说回来，\n',
            '真想亲眼看看这桥被分开的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040984V#040F这座开合桥\n',
            '每天会按时分离三次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040985V从现在算起的话……\n',
            '我想到傍晚就可以看见了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040986V#006F好～吧，\n',
            '到时候我们一定要来这看看哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040987V#019F是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_41CC(): pass

    label('loc_41CC')

    Return()

# id: 0x001A offset: 0x41CD
@scena.Code('func_1A_41CD')
def func_1A_41CD():
    EventBegin(0x00)
    CameraMove(45290, 0, 87610, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 45000, 500, 91157, 0)
    ChrSetPos(0x0102, 45000, 500, 91157, 0)
    ChrSetPos(0x0136, 45000, 500, 91157, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_70(0x0005, 30)
    OP_73(0x0005)
    CreateThread(0x0101, 0x01, 0x00, func_1B_4810)
    CreateThread(0x0102, 0x01, 0x00, func_1C_4843)
    CreateThread(0x0136, 0x01, 0x00, func_1D_487B)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0136, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010041225V#501F哇，已经傍晚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041226V#001F看看，好漂亮的夕阳呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041227V#010F这里的夕阳很特别，\n',
            '与白色的街道相映生辉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041228V#041F呵呵，我也很喜欢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041229V#040F对了……\n',
            '我想差不多该到时间了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0136, 400)
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041230V#004F哎？到什么时间？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(148, 0x01, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_6F(0x0011, 0)
    Fade(1000)
    OP_67(0, 6115, -10000, 0)
    CameraSetDistance(7760, 0)
    CameraMove(51680, 400, 52400, 0)
    OP_6C(36000, 0)
    OP_12(0x00009470, 0x0003D090, 0x00000000)
    Sleep(1500)

    PlaySE(147, 0x01, 0x64)
    OP_70(0x0011, 1000)
    OP_6C(315000, 18000)
    OP_73(0x0011)
    PlaySE(154, 0x00, 0x64)
    OP_23(0x0093)
    OP_23(0x0094)
    OP_6F(0x0011, 1000)
    OP_70(0x0011, 1020)
    Sleep(1000)

    Fade(1000)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_12(0x00009470, 0x00014C08, 0x00001F40)
    CameraMove(58250, -1800, 70690, 0)
    ChrSetPos(0x0101, 59330, -1800, 70537, 180)
    ChrSetPos(0x0102, 58480, -1800, 70537, 180)
    ChrSetPos(0x0136, 60300, -1800, 70537, 180)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010041231V#501F#3P哇～好精彩的压轴戏啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041232V对了对了，\n',
            '开合桥分开的状态会维持多久呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041233V#040F#4P应该是３０分钟左右。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041234V清晨、上午、傍晚共３次，\n',
            '一直到所有的船都通过为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041235V#010F#1P原来如此，\n',
            '是选择了来往行人比较少的时间段啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041236V#041F#4P呵呵，刚到这里的人\n',
            '最初都会有点摸不着规律呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041237V#044F啊，说起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0136,
        (
            '#0060041238V#040F#4P艾丝蒂尔你们\n',
            '今晚住在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0136, 400)
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041239V#000F#3P嗯～这个嘛……\n',
            '其实我们原定住在协会的二楼的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041240V不过刚来这几天，\n',
            '我还是想找家酒店好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041241V#040F#4P这样的话，\n',
            '那你们快点去订个房间比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041242V因为现在是旅游旺季，\n',
            '我想酒店很快就会住满人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041243V#010F#1P这样啊……\n',
            '看来要快点才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041244V#000F#3P嗯，现在去酒店吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x001A, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x4810
@scena.Code('func_1B_4810')
def func_1B_4810():
    ChrWalkTo(0x00FE, 45240, 0, 88310, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 46060, 0, 87220, 3000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x001C offset: 0x4843
@scena.Code('func_1C_4843')
def func_1C_4843():
    Sleep(300)

    ChrWalkTo(0x00FE, 45240, 0, 88310, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 44770, 0, 87220, 3000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x001D offset: 0x487B
@scena.Code('func_1D_487B')
def func_1D_487B():
    Sleep(600)

    ChrWalkTo(0x00FE, 45240, 0, 88310, 3000, 0x00)
    OP_72(0x0005, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0005, 30)
    OP_70(0x0005, 0)
    OP_73(0x0005)
    OP_71(0x0005, 0x0800)

    Return()

# id: 0x001E offset: 0x48B5
@scena.Code('func_1E_48B5')
def func_1E_48B5():
    EventBegin(0x00)
    CameraMove(24380, 0, 94810, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 24040, 0, 94400, 90)
    ChrSetPos(0x0102, 23870, 0, 93300, 90)
    ChrSetPos(0x0136, 25410, 0, 93880, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0136,
        (
            '#0060041272V#040F#4P今天能让我陪着你们，\n',
            '我真是十分感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041273V#008F#1P啊哈哈，别这么说嘛。\n',
            '应该是我们多谢你才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041274V#019F#1P说得没错。\n',
            '谢谢你带我们参观了这么多好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041275V#045F#4P你们太客气了，而且我又没做什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041276V#040F对了，\n',
            '你们两个会在卢安呆上一段时间吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041277V如果你们不介意的话，\n',
            '可以来参加下周末的学园祭吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041278V#004F#1P学园祭？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041279V#010F#1P这个名字听起来\n',
            '似乎是某种活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041280V#041F#4P嗯，是获得校方许可的\n',
            '由学生自发组织和筹办的活动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041281V这可是王立学院的传统活动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041282V#004F#1P啊，学生活动……\n',
            '听起来真的挺有趣呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041283V#001F会有货摊和节目表演吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041284V#041F#4P呵呵，当然了。\n',
            '而且都是很正规的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041285V#001F#1P我去我去，绝～对要去！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041286V其实我很想和你们\n',
            '一起为学园祭做准备呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041287V#018F#3P我说艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041288V刚刚嘉恩先生才说了我们可能会很忙，\n',
            '你这么快就忘了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041289V#007F哦哦，还有这档子事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041290V#019F#3P不过，只是学园祭当天去的话，\n',
            '倒也刚好可以作为休息的节目……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041291V在那之前先好好工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041292V#007F#2P哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060041293V#045F#4P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041294V#048F艾丝蒂尔、约修亚。\n',
            '那么我这就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041295V过两天再见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041296V#006F#1P嗯，再见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0136, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041297V#010F#1P路上小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0136, 0, 400)

    @scena.Lambda('lambda_4EDD')
    def lambda_4EDD():
        CameraMove(25200, 0, 97530, 2000)

        ExitThread()

    DispatchAsync(0x0136, 0x0002, lambda_4EDD)

    @scena.Lambda('lambda_4EF5')
    def lambda_4EF5():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_4EF5')

    DispatchAsync2(0x0101, 0x0002, lambda_4EF5)

    @scena.Lambda('lambda_4F06')
    def lambda_4F06():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_4F06')

    DispatchAsync2(0x0102, 0x0002, lambda_4F06)

    ChrWalkTo(0x0136, 26120, 0, 109460, 3000, 0x00)
    ChrSetFlags(0x0136, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_4F38')
    def lambda_4F38():
        CameraMove(23990, 0, 93830, 1500)

        ExitThread()

    DispatchAsync(0x0136, 0x0002, lambda_4F38)

    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)
    WaitForThreadExit(0x0136, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010041298V#501F嗯～真的是个惹人怜爱的女孩子，\n',
            '而且又有正义感，给人一种靠得住的感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041299V我要是男孩子的话，\n',
            '毫无疑问一定会喜欢上她的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041300V#015F嗯，这个暂且不说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041301V#010F不像有什么企图的样子，\n',
            '看得出她的确是个好女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041302V#007F那还用说。\n',
            '她又不是那个傲慢的女空贼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041303V#000F不过，既认识了好朋友，\n',
            '又订到了酒店顶楼的好房间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041304V#001F在玛诺利亚村的瞭望台上看见了基库，\n',
            '果然是件好事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041305V#019F呵呵，也许吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041306V#010F……那么，\n',
            '我们先回房间整理一下行李吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041307V#001F嗯，是顶楼呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0136, 0x0080)
    ChrSetPos(0x0136, 27020, 0, 94830, 180)
    EventEnd(0x00)
    FormationDelMember(0x35, 0xFF)

    Return()

# id: 0x001F offset: 0x51C7
@scena.Code('func_1F_51C7')
def func_1F_51C7():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 9880, 4200, 91480, 270)
    ChrSetPos(0x0102, 10260, 4200, 92590, 270)
    CameraMove(-10010, 4200, 90430, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_12(0x00009470, 0x000186A0, 0x00000000)
    FadeIn(2000, 0)
    CameraMove(10690, 4200, 93000, 5000)

    ChrTalk(
        0x0102,
        (
            '#0020041319V#014F#1P真壮观啊……\n',
            '居然还有这么漂亮的露台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010041320V#501F嗯……真的是绝佳的风景呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041321V#007F不过，这房间光我们两个住，\n',
            '我觉得真是有点太浪费呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041322V#003F……要是老爸也在的话，\n',
            '那该多好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020041323V#013F#1P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041324V#015F父亲他在哪里，\n',
            '现在又在做些什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0012, 12770, 4200, 93110, 0)

    NpcTalk(
        0x0012,
        '男性的声音',
        (
            '#0640041325V#3P呵呵……\n',
            '这房间倒是很不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041326V#004F刚才那是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041327V#012F#1P嗯，\n',
            '似乎是从房间里传来的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x54A8
@scena.Code('func_20_54A8')
def func_20_54A8():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(24130, 0, 93980, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 23540, 0, 94500, 90)
    ChrSetPos(0x0102, 23610, 0, 93330, 45)
    ChrSetPos(0x0008, 25170, 0, 94000, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001A, 0x0008)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001B, 0x0008)
    FadeOut(0, 0, -1)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    PlaySE(13, 0x00, 0x64)
    Sleep(5000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '——次日早晨，卢安市街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    PlayBGM(12)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(453, 0x01, 0x64)

    ChrTalk(
        0x0008,
        (
            '#0270050028V#145F哈～～～～～欠……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050029V头好痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050030V#006F真是标准的宿醉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050031V明明没酒量，\n',
            '却偏要喝那么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050032V#010F要我去买点药来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270050033V#142F不用……没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050034V好了， \n',
            '我要去取材了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050035V#501F这样啊……\n',
            '#001F多谢你昨天让我们留宿哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050036V#010F也非常感谢您请我们吃饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270050037V#141F小意思，要是有什么有趣的新闻，\n',
            '你们可要记得告诉我啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050038V我最近也会呆在卢安的……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270050039V#145F那么，干活去了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 300)

    @scena.Lambda('lambda_57E2')
    def lambda_57E2():
        CameraMove(25330, 0, 91170, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_57E2)

    @scena.Lambda('lambda_57FA')
    def lambda_57FA():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_57FA')

    DispatchAsync2(0x0101, 0x0002, lambda_57FA)

    @scena.Lambda('lambda_580B')
    def lambda_580B():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_580B')

    DispatchAsync2(0x0102, 0x0002, lambda_580B)

    ChrWalkTo(0x0008, 26210, 0, 90200, 2000, 0x00)
    ChrWalkTo(0x0008, 30740, 0, 85650, 2000, 0x00)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 200)
    Sleep(200)

    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Sleep(300)

    @scena.Lambda('lambda_5866')
    def lambda_5866():
        CameraMove(23600, 0, 93950, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_5866)

    ChrTurnDirection(0x0102, 0x0101, 400)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020050040V#010F好了，\n',
            '我们也差不多该去协会了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050041V#006F嗯，好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050042V去嘉恩哥哥那看看有什么工作。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001A, 0x0008)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001B, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0x5928
@scena.Code('func_21_5928')
def func_21_5928():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 25470, 0, 115060, 180)
    ChrSetPos(0x0102, 24790, 0, 116060, 180)
    ChrSetPos(0x0136, 26160, 0, 116640, 180)
    OP_6C(45000, 0)
    CameraMove(25850, 0, 115000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010050565V#003F#4P……街道上不见那孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050566V难道已经闯到了\n',
            '那帮流氓的地盘里去吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050567V#043F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050568V#012F总之赶快去南街区的仓库吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003C, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0022 offset: 0x5A49
@scena.Code('func_22_5A49')
def func_22_5A49():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 2, 0x42A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 1, 0x429)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F5E',
    )

    SetScenaFlags(ScenaFlag(0x0085, 2, 0x42A))
    OP_28(0x003C, 0x01, 0x0004)
    OP_28(0x003C, 0x01, 0x0008)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    PlaySE(148, 0x01, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0136, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020050592V#012F糟了，已经是晌午了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrClearFlags(0x0009, 0x0080)
    Fade(1000)
    ChrSetPos(0x0009, 50820, 400, 57120, 0)
    OP_6C(45000, 0)
    CameraMove(50820, 400, 50000, 0)

    @scena.Lambda('lambda_5B29')
    def lambda_5B29():
        CameraMove(50820, 200, 35000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5B29)

    ChrWalkTo(0x0009, 50820, 200, 37420, 6000, 0x00)
    CreateThread(0x0009, 0x03, 0x00, func_23_5F5F)

    @scena.Lambda('lambda_5B5C')
    def lambda_5B5C():
        ChrWalkTo(0x0009, 50820, 200, 26000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5B5C)

    Sleep(2000)

    @scena.Lambda('lambda_5B7C')
    def lambda_5B7C():
        CameraMove(50890, 0, 70000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5B7C)

    Sleep(1000)

    ChrSetPos(0x0101, 50210, 0, 90000, 180)
    ChrSetPos(0x0102, 51440, 0, 90000, 180)
    ChrSetPos(0x0136, 50920, 0, 90000, 225)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0136, 0x0040)

    @scena.Lambda('lambda_5BDB')
    def lambda_5BDB():
        ChrWalkTo(0x00FE, 50920, 0, 70750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_5BDB)

    Sleep(200)

    @scena.Lambda('lambda_5BFB')
    def lambda_5BFB():
        ChrWalkTo(0x00FE, 50210, 0, 72110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5BFB)

    Sleep(200)

    @scena.Lambda('lambda_5C1B')
    def lambda_5C1B():
        ChrWalkTo(0x00FE, 51440, 0, 72070, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5C1B)

    OP_6C(135000, 3600)
    ChrSetFlags(0x0009, 0x0080)

    ChrTalk(
        0x0136,
        (
            '#0060050593V#043F#2P啊啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050594V克拉姆，等等！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050595V#013F#1P没用的……\n',
            '看来他根本听不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050596V#005F#4P真是的！\n',
            '桥怎么偏偏在这种时候分开！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050597V这下要足足等３０分钟啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050598V#049F#2P怎能这样呢……\n',
            '这样下去的话，那孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050599V怎么办……该怎么办才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0136, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050600V#012F#1P科洛丝，冷静点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050601V你忘记了吗？\n',
            '昨天你还告诉过我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0136, 0x0102, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050602V#044F#2P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050603V#010F#1P这座桥还未建成的时候，\n',
            '是用什么工具来往于两岸的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0136, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010050604V#004F#4P啊，是小船！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050605V#042F#2P……对了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050606V我记得酒店后面\n',
            '好像有出租用的小船！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050607V#006F#4P好极了！\n',
            '就乘那个去对岸吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x001A, 0x0002)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0102, 0x0040)
    ChrClearFlags(0x0136, 0x0040)
    EventEnd(0x00)

    def _loc_5F5E(): pass

    label('loc_5F5E')

    Return()

# id: 0x0023 offset: 0x5F5F
@scena.Code('func_23_5F5F')
def func_23_5F5F():
    PlaySE(147, 0x01, 0x64)
    OP_70(0x0011, 1000)
    OP_73(0x0011)
    PlaySE(154, 0x00, 0x64)
    OP_23(0x0093)
    OP_23(0x0094)
    OP_6F(0x0011, 1000)
    OP_70(0x0011, 1020)

    Return()

# id: 0x0024 offset: 0x5F88
@scena.Code('func_24_5F88')
def func_24_5F88():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 24790, 0, 116060, 180)
    ChrSetPos(0x0009, 26160, 0, 116640, 180)
    ChrSetPos(0x0101, 24790, 0, 114060, 0)
    ChrSetPos(0x0105, 26160, 0, 114640, 0)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetPos(0x0102, 26225, 0, 104380, 0)
    OP_6C(45000, 0)
    CameraMove(25850, 0, 115000, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0390050761V#750F#1P真是太感谢各位了。\n',
            '都不知该怎么报答你们才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050762V#001F不用这么客气啦。\n',
            '这也是我们份内的工作嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050763V#000F话说回来，真的不用我们\n',
            '送你们回玛诺利亚村吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0390050764V#751F嗯，没问题的。\n',
            '梅威海道就像我家的花园一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050765V如果再继续给你们添麻烦的话，\n',
            '恐怕就要受到天罚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050766V#008F其实不用介意啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050767V#043F老师……至少让我陪你们回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0390050768V#750F呵呵，\n',
            '你就继续专心准备学园祭的事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050769V而且， \n',
            '这些孩子也都很期待你的表演哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050770V#040F……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050771V#1P太好了，赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_627D')
    def lambda_627D():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_627D)

    @scena.Lambda('lambda_628B')
    def lambda_628B():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_628B)

    ChrWalkTo(0x0102, 25860, 0, 113000, 4000, 0x00)
    ChrClearFlags(0x0102, 0x0004)

    ChrTalk(
        0x0102,
        (
            '#0020050772V#010F船已经还回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050773V#001F啊，谢了☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050774V#040F真不好意思……\n',
            '让你自己一个人去还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050775V#010F别客气。\n',
            '又不是什么麻烦事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0390050776V#750F约修亚……\n',
            '这次真是太感谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_639C')
    def lambda_639C():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_639C)

    ChrTurnDirection(0x0105, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#0400050777V#775F科洛丝姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050778V还有艾丝蒂尔姐姐和\n',
            '约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050779V今天真是谢谢你们。\n',
            '谢谢你们救了我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050780V我……真的是个笨蛋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050781V#043F克拉姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400050782V#773F明明一点本事都没有，\n',
            '却硬着头皮去报仇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050783V最后反而要\n',
            '姐姐你们来救我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050784V#777F真是……太丢脸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050785V#004F没、没这回事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050786V#015F我觉得一点都不丢脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_655F')
    def lambda_655F():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_655F)

    @scena.Lambda('lambda_656D')
    def lambda_656D():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_656D)

    @scena.Lambda('lambda_657B')
    def lambda_657B():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_657B)

    @scena.Lambda('lambda_6589')
    def lambda_6589():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6589)

    ChrTalk(
        0x0009,
        (
            '#0400050787V#777F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_65B6')
    def lambda_65B6():
        CameraMove(25850, 0, 117000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_65B6)

    @scena.Lambda('lambda_65CE')
    def lambda_65CE():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_65CE')

    DispatchAsync2(0x0009, 0x0001, lambda_65CE)

    @scena.Lambda('lambda_65DF')
    def lambda_65DF():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_65DF')

    DispatchAsync2(0x000B, 0x0001, lambda_65DF)

    @scena.Lambda('lambda_65F0')
    def lambda_65F0():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_65F0')

    DispatchAsync2(0x0101, 0x0001, lambda_65F0)

    @scena.Lambda('lambda_6601')
    def lambda_6601():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_6601')

    DispatchAsync2(0x0105, 0x0001, lambda_6601)

    ChrWalkTo(0x0102, 27180, 0, 114180, 3000, 0x00)
    ChrWalkTo(0x0102, 26930, 0, 116290, 3000, 0x00)
    ChrSetDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050788V#010F为了保护自己身边重要的人，\n',
            '奋不顾身挺身而出……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050789V这种事有时候\n',
            '连大人都不一定做得到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050790V#019F所以我觉得\n',
            '你的勇气真的非常可嘉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400050791V#775F#1P约修亚哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050792V#012F只不过，搜捕犯人和\n',
            '惩治犯人这种事可以由我们来做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050793V而你，应该用自己力所能及的方法，\n',
            '去保护老师和其他孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050794V陪在他们身边，互相帮忙、\n',
            '互相鼓励，成为大家信赖的伙伴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050795V#011F克拉姆……\n',
            '这是只有你才做得到的事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400050796V#774F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050797V只有我才做得到的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050798V#770F嗯，知道了。\n',
            '我明白哥哥的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050799V#010F怎么样，能做到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400050800V#771F#1P那当然啦！\n',
            '就包在我身上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6902')
    def lambda_6902():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6902')

    DispatchAsync2(0x0102, 0x0001, lambda_6902)

    @scena.Lambda('lambda_6913')
    def lambda_6913():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6913')

    DispatchAsync2(0x0101, 0x0001, lambda_6913)

    @scena.Lambda('lambda_6924')
    def lambda_6924():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_6924')

    DispatchAsync2(0x0105, 0x0001, lambda_6924)

    ChrTalk(
        0x000B,
        (
            '#0390050801V#751F呵呵，太好了。\n',
            '真的是太谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000B, 0xFF)
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0390050802V#750F那么各位，\n',
            '我们这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0009, 0x0105, 400)

    ChrTalk(
        0x0009,
        (
            '#0400050803V#770F#1P啊，科洛丝姐姐！\n',
            '我等着看你的舞台剧哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050804V#041F嗯，我会加油的，\n',
            '大家要一起来看哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400050805V#770F#1P那当然啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050806V#771F再见，哥哥姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 0, 400)

    @scena.Lambda('lambda_6A80')
    def lambda_6A80():
        ChrWalkTo(0x00FE, 24800, 0, 133060, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6A80)

    ChrSetDirection(0x0009, 0, 400)

    @scena.Lambda('lambda_6AA2')
    def lambda_6AA2():
        ChrWalkTo(0x00FE, 26000, 0, 133060, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6AA2)

    Sleep(4000)

    ChrTalk(
        0x0101,
        (
            '#0010050807V#007F#3P呼～太好了。\n',
            '总算又打起精神来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050808V#006F#3P约修亚你呀，\n',
            '什么时候都那么会说话㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0105, 0xFF)

    @scena.Lambda('lambda_6B4B')
    def lambda_6B4B():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_6B4B')

    DispatchAsync2(0x0105, 0x0001, lambda_6B4B)

    ChrTalk(
        0x0105,
        (
            '#0060050809V#048F呵呵，我也吃了一惊呢。\n',
            '那孩子这么快又活泼起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050810V#041F约修亚……\n',
            '真的是太谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050811V#015F#1P不……\n',
            '其实我又没说什么了不起的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050812V#013F保护身边重要的人……吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0102, 270, 400)

    @scena.Lambda('lambda_6C78')
    def lambda_6C78():
        CameraMove(25400, 0, 115000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6C78)

    ChrWalkTo(0x0102, 25000, 0, 115680, 2000, 0x00)
    TerminateThread(0x0102, 0xFF)
    ChrSetDirection(0x0102, 180, 400)
    TerminateThread(0x0105, 0xFF)
    ChrSetDirection(0x0105, 270, 0)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020050813V#010F#1P总之，\n',
            '那孩子没事真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050814V科洛丝，谢谢你帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050815V#045F怎能这样呢……\n',
            '其实该道谢的是我才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050816V#044F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050817V不知道对那些人的调查\n',
            '进行得怎样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050818V#501F啊，那个阿加特说了\n',
            '会好好审问那些家伙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050819V不知道有没有结果了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050820V#010F#1P总之，先回协会去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050821V科洛丝也一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060050822V#042F嗯，可以的话，\n',
            '我也想知道真相到底是怎样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050823V犯人究竟是什么人呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050824V#006F那么，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0025 offset: 0x6EE6
@scena.Code('func_25_6EE6')
def func_25_6EE6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 0, 0x450)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_741E',
    )

    SetScenaFlags(ScenaFlag(0x008A, 0, 0x450))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 0, 0x418)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_741E',
    )

    EventBegin(0x00)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x000F, 0xFF)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0011, 0)
    ChrSetSubChip(0x000F, 0)

    @scena.Lambda('lambda_6F25')
    def lambda_6F25():
        CameraMove(18500, 0, 73800, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6F25)

    @scena.Lambda('lambda_6F3D')
    def lambda_6F3D():
        OP_6C(225000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F3D)

    Sleep(3000)

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……这里就是为了纪念\n',
            '百日战役结束而建造的公园。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯……那么，\n',
            '现在考大家一个问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '众所周知，\n',
            '沿着这条卢比诺川溯流而上，\n',
            '就可以通到座落于湖畔的王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在百日战役的时候，\n',
            '为了防止帝国海军的入侵，\n',
            '王国军曾在这里采取了一项措施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '有谁知道那项措施究竟是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpToRelative(0x0010, 0, 0, 0, 1000, 8000)
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好，请回答！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嘿嘿，\n',
            '这个我知道哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他们在卢安市里\n',
            '调集了很多大炮对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唔～答错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '当时的确调集了很多大炮过来，\n',
            '但由于帝国的攻击太猛烈了，\n',
            '所以没能来得及装上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '给大家一点提示吧。\n',
            '是更直接有效的措施哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7184')
    def lambda_7184():
        ChrJumpToRelative(0x0011, 0, 0, 0, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7184)

    Sleep(10)

    ChrSetDirection(0x0011, 30, 2200)
    ChrSetDirection(0x0011, 150, 2200)
    ChrSetDirection(0x0011, 270, 2200)
    ChrSetDirection(0x0011, 30, 2200)
    ChrSetDirection(0x0011, 150, 2200)
    ChrSetDirection(0x0011, 270, 2200)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '我知道我知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好的。\n',
            '那位小姐，请回答！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '是不是炸沉了\n',
            '那座伦格兰德大桥啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '啊啊，可惜！\n',
            '答案完～全不对啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '当时大桥一直处于分离状态，\n',
            '听说是导力器发生故障了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '嘁～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '公布正确答案～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '其实是调集了许多已经要废弃的船，\n',
            '然后让它们从上游顺流而下，\n',
            '最后在河口将它们炸沉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为河口变浅了，\n',
            '所以帝国军就无法\n',
            '由卢比诺川入侵王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊～真厉害，\n',
            '不过这么做好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '怎么说这也有点过激了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '那么接下来，\n',
            '大家可以自由活动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在规定的时间之前，\n',
            '就请在附近好好游览一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_85(0x000E)
    OP_85(0x0010)
    OP_85(0x0011)
    OP_85(0x000F)
    EventEnd(0x00)

    def _loc_741E(): pass

    label('loc_741E')

    Return()

# id: 0x0026 offset: 0x741F
@scena.Code('func_26_741F')
def func_26_741F():
    EventBegin(0x00)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlaySE(148, 0x01, 0x64)
    PlayEffect(0x04, 0x04, 0x001F, 0, 50, 2700, 180, 0, 0, 2500, 500, 10000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x001E, 0, 50, 2400, 180, 0, 0, 1600, 500, 10000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0xFF, 0x001F, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0xFF, 0x001E, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0018, 0x0002)
    OP_71(0x0018, 0x0020)
    OP_71(0x0018, 0x0040)
    OP_6F(0x0018, 301)
    OP_70(0x0018, 360)
    OP_72(0x0019, 0x0002)
    OP_71(0x0019, 0x0020)
    OP_71(0x0019, 0x0040)
    OP_6F(0x0019, 301)
    OP_70(0x0019, 360)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetBattleFlags(0x001D, 0x0020)
    OP_89(0x001D, 89820, -2850, 52390, 270)
    ChrSetPos(0x0101, 98260, -1000, 52020, 270)
    ChrSetPos(0x0102, 100490, -1000, 51980, 90)
    ChrSetPos(0x0105, 99510, -1000, 52230, 270)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x0105, 0x0020)
    ChrSetChipByIndex(0x0101, 17)
    ChrSetChipByIndex(0x0102, 18)
    ChrSetChipByIndex(0x0105, 19)
    OP_A1(0x001F, 0x0018)
    OP_A1(0x001E, 0x0019)
    ChrSetPos(0x001F, 90000, -3000, 53000, 90)
    ChrSetPos(0x001E, 100000, -3000, 52000, 90)
    FadeIn(2000, 0)
    CameraMove(50010, 400, 40640, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(336000, 0)
    OP_6E(371, 0)
    ChrSetPos(0x0011, 52500, 400, 59820, 90)
    ChrSetPos(0x000F, 51400, 400, 60600, 90)
    ChrSetPos(0x0010, 52190, 400, 58970, 90)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_7682')
    def lambda_7682():
        OP_6C(322000, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7682)

    CameraMove(51480, 400, 59800, 4000)
    TerminateThread(0x000F, 0xFF)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    TerminateThread(0x0010, 0xFF)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    TerminateThread(0x0011, 0xFF)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_12(0x00009470, 0x0003D090, 0x00002710)
    Sleep(700)

    PlaySE(147, 0x00, 0x64)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 1020)
    Sleep(300)

    ChrTalk(
        0x0010,
        (
            '#10A#3P哇啊啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_7753')
    def lambda_7753():
        ChrWalkTo(0x00FE, 50850, 0, 67820, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7753)

    Sleep(100)

    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_7785')
    def lambda_7785():
        ChrWalkTo(0x00FE, 50850, 0, 67820, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7785)

    ChrTalk(
        0x0011,
        (
            '#1710061745V#10A#2P啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(100)

    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_77DC')
    def lambda_77DC():
        ChrWalkTo(0x00FE, 50850, 0, 67820, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_77DC)

    @scena.Lambda('lambda_77F7')
    def lambda_77F7():
        CameraMove(51130, 400, 52010, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_77F7)

    @scena.Lambda('lambda_780F')
    def lambda_780F():
        OP_67(0, 6250, -10000, 8600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_780F)

    @scena.Lambda('lambda_7827')
    def lambda_7827():
        OP_6C(270000, 8600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7827)

    @scena.Lambda('lambda_7837')
    def lambda_7837():
        OP_6E(729, 8600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7837)

    Sleep(2000)

    OP_63(0x0010)
    OP_63(0x000F)
    OP_63(0x0011)
    ChrSetFlags(0x001F, 0x0004)
    ChrSetFlags(0x001E, 0x0004)
    ChrSetFlags(0x001F, 0x0040)
    ChrSetFlags(0x001E, 0x0040)
    ChrSetFlags(0x0000, 0x0004)
    ChrSetFlags(0x0001, 0x0004)
    ChrSetFlags(0x0002, 0x0004)
    Sleep(1800)

    @scena.Lambda('lambda_787D')
    def lambda_787D():
        ChrMoveTo(0x00FE, -5650, 400, 53000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_787D)

    Sleep(1800)

    PlaySE(217, 0x00, 0x64)

    @scena.Lambda('lambda_78A2')
    def lambda_78A2():
        ChrMoveTo(0x00FE, -5650, 400, 51930, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_78A2)

    Sleep(3000)

    @scena.Lambda('lambda_78C2')
    def lambda_78C2():
        CameraMove(26670, -810, 52180, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_78C2)

    @scena.Lambda('lambda_78DA')
    def lambda_78DA():
        CameraSetDistance(1750, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_78DA)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0027 offset: 0x7901
@scena.Code('func_27_7901')
def func_27_7901():
    SetScenaFlags(ScenaFlag(0x00A0, 0, 0x500))
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(51000, 400, 61600, 0)
    OP_67(0, 6700, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(21000, 0)
    FadeIn(2000, 0)
    ChrSetPos(0x000C, 62600, 6000, 68000, 0)
    ChrSetPos(0x0105, 50500, 0, 67700, 0)
    ChrSetPos(0x0101, 50500, 0, 67700, 0)
    ChrSetPos(0x0102, 50500, 0, 67700, 0)

    @scena.Lambda('lambda_7992')
    def lambda_7992():
        ChrWalkTo(0x00FE, 50900, 400, 52100, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7992)

    @scena.Lambda('lambda_79AD')
    def lambda_79AD():
        CameraMove(50900, 400, 52100, 4800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_79AD)

    @scena.Lambda('lambda_79C5')
    def lambda_79C5():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_79C5)

    Sleep(500)

    @scena.Lambda('lambda_79DA')
    def lambda_79DA():
        ChrWalkTo(0x00FE, 52100, 400, 52800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_79DA)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010070086V#501F#3P……果然，\n',
            '好像还没有来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070087V我们是不是来得太早了点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020070088V#010F是啊。\n',
            '要不先去酒吧打发一会儿时间吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070089V#001F#3P不用了，吹吹风也挺舒服的。\n',
            '我们就在这里等吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070090V站在桥上看着河水流动，\n',
            '完全不会感到无聊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070091V#019F嗯，那好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)

    @scena.Lambda('lambda_7B49')
    def lambda_7B49():
        CameraMove(49130, 400, 51740, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7B49)

    @scena.Lambda('lambda_7B61')
    def lambda_7B61():
        ChrWalkTo(0x00FE, 49500, 400, 51200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7B61)

    ChrSetDirection(0x0102, 270, 400)

    @scena.Lambda('lambda_7B83')
    def lambda_7B83():
        ChrWalkTo(0x00FE, 49500, 400, 52300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7B83)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 0)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010070092V#006F#2P话说回来，\n',
            '卢安也终于恢复了以往的平静呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070093V前阵子戴尔蒙市长被捕的时候，\n',
            '整个城市还闹得沸沸扬扬的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070094V#015F#1P因为现任市长被捕\n',
            '确实是前所未闻的事情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070095V假如说洛连特的\n',
            '克劳斯市长遭到了逮捕，\n',
            '我想也一样会闹得沸沸扬扬的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070096V#004F#2P哇，要是发生了那种事情，\n',
            '肯定不是一般的轰动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070097V#000F不过这样一比较，\n',
            '卢安的百姓反而还算冷静呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070098V虽然大家都非常吃惊，\n',
            '但看来并没有受到太大打击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070099V#010F#1P嗯，因为卢安的市长\n',
            '一直都是按照传统继任的，\n',
            '由戴尔蒙家族的主人担任这个角色。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070100V并不是因为市长本人\n',
            '受到卢安市民仰慕的缘故。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070101V#007F#2P和受洛连特市民爱戴的\n',
            '克劳斯市长完全不一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070102V嗯……虽说是自作自受，\n',
            '不过想起来还是觉得他挺可怜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0105, 300)

    ChrTalk(
        0x0102,
        (
            '#0020070103V#010F#1P好像来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070104V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7F1F')
    def lambda_7F1F():
        CameraMove(51540, 400, 57590, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7F1F)

    @scena.Lambda('lambda_7F37')
    def lambda_7F37():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7F37)

    ChrClearFlags(0x000C, 0x0080)
    PlaySE(140, 0x00, 0x64)
    ChrWalkTo(0x000C, 53900, 1300, 57000, 4000, 0x00)
    ChrSetFlags(0x000C, 0x0020)

    @scena.Lambda('lambda_7F6A')
    def lambda_7F6A():
        OP_99(0x00FE, 0x00, 0x07, 5000)
        Yield()

        Jump('lambda_7F6A')

    DispatchAsync2(0x000C, 0x0002, lambda_7F6A)

    ChrTurnDirection(0x0102, 0x000C, 400)
    ChrTurnDirection(0x0101, 0x000C, 400)

    @scena.Lambda('lambda_7F8B')
    def lambda_7F8B():
        ChrSetDirection(0x00FE, 270, 100)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_7F8B)

    ChrMoveTo(0x000C, 53800, 1100, 57000, 500, 0x00)
    TerminateThread(0x000C, 0x02)
    ChrSetChipByIndex(0x000C, 16)
    ChrSetSubChip(0x000C, 3)
    Sleep(100)

    ChrSetSubChip(0x000C, 4)
    Sleep(100)

    ChrSetSubChip(0x000C, 0)
    ChrClearFlags(0x000C, 0x0020)

    ChrTalk(
        0x0101,
        (
            '#0010070105V#001F啊，基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 1)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0440070106V#310F#5P啾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0105,
        '女孩的声音',
        (
            '#0060070107V#4P艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0105, 51000, 400, 57700, 5000, 0x00)

    ChrTalk(
        0x0105,
        (
            '#0060070108V#045F#1P哈啊哈啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070109V对不起，我迟到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_80A9')
    def lambda_80A9():
        ChrWalkTo(0x00FE, 50400, 400, 56100, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_80A9)

    Sleep(200)

    @scena.Lambda('lambda_80C9')
    def lambda_80C9():
        ChrWalkTo(0x00FE, 51300, 400, 55900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_80C9)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020070110V#010F没关系呢，\n',
            '其实我们也是刚到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070111V#004F难、难道说\n',
            '你是特地一路跑过来的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070112V不用那么着急嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060070113V#048F#1P不行呢，我可是来送行的，\n',
            '怎么能慢悠悠地走过来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070114V幸好你们通知了我，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070115V#008F哎呀～科洛丝真是的。\n',
            '该说谢谢的是我们两个啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070116V#001F还有基库……\n',
            '谢谢你来送我们哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0440070117V#311F#2P啾～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070118V#019F哈哈，那么……\n',
            '我们是时候出发了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070119V#006F嗯，好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070120V要前往蔡斯地区的话，\n',
            '是从南街区的门口出去对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 4, 0x53C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8422',
    )

    ChrTalk(
        0x0105,
        (
            '#0060070121V#040F#1P嗯，南面街道的尽头有个\n',
            '通往蔡斯方面的『艾尔·雷登』关所。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070122V由于那里有一座非常宏伟的瀑布，\n',
            '所以作为观光地也非常有名哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070123V#501F哎～那还真是值得期待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070124V#001F好，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E8')

    def _loc_8422(): pass

    label('loc_8422')

    ChrTalk(
        0x0105,
        (
            '#0060070126V#040F#1P嗯，南面街道的尽头有个\n',
            '叫做『艾尔·雷登』的关所。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060070127V从那里一直走，\n',
            '就是通往蔡斯的街道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070128V#006F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070129V#001F那么，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84E8(): pass

    label('loc_84E8')

    ChrTalk(
        0x000C,
        (
            '#0440070125V#311F#2P啾～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 180, 400)
    ChrSetSubChip(0x000C, 4)
    Sleep(100)

    ChrSetSubChip(0x000C, 3)
    Sleep(100)

    ChrSetChipByIndex(0x000C, 4)
    ChrSetSubChip(0x000C, 0)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_8538')
    def lambda_8538():
        ChrWalkTo(0x00FE, 51300, 6000, 40000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_8538)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventEnd(0x00)
    ChrSetFlags(0x000C, 0x0080)

    Return()

# id: 0x0028 offset: 0x855E
@scena.Code('func_28_855E')
def func_28_855E():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8627',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ChrTurnDirection(0x0136, 0x0000, 400)

    ChrTalk(
        0x0136,
        (
            '#0060041245V#040F嗯～\n',
            '我想还是先去预定好房间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041246V现在这个旅游旺季\n',
            '酒店很容易客满的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_85DF')
    def lambda_85DF():
        ChrTurnDirection(0x0102, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_85DF)

    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041247V#000F啊，是这样，\n',
            '那就赶快去预定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8693')

    def _loc_8627(): pass

    label('loc_8627')

    ChrTurnDirection(0x0136, 0x0000, 400)

    ChrTalk(
        0x0136,
        (
            '#0060041248V#040F我想还是先去预定好房间吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060041249V现在这个旅游旺季\n',
            '酒店很容易客满的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8693(): pass

    label('loc_8693')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0029 offset: 0x86AF
@scena.Code('func_29_86AF')
def func_29_86AF():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_879C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041308V#010F已经是傍晚时分了，\n',
            '还是别去街道那边比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041309V就算在城里散步，\n',
            '也要先去房间把东西放好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010041310V#000F啊，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010041311V我们的房间在酒店的最顶层对吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_881E')

    def _loc_879C(): pass

    label('loc_879C')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020041312V#010F已经是傍晚时分了，\n',
            '还是别去街道那边比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020041313V就算在城里散步，\n',
            '也要先去房间把东西放好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_881E(): pass

    label('loc_881E')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002A offset: 0x883A
@scena.Code('func_2A_883A')
def func_2A_883A():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89A9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88EC',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050043V#010F在去城外之前先到协会报到吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050044V嘉恩先生不是说\n',
            '要给我们分配工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050045V#000F啊，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89A6')

    def _loc_88EC(): pass

    label('loc_88EC')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050046V#000F哎……\n',
            '要到城外去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050047V#010F不了，\n',
            '还是先去协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050048V嘉恩先生不是说\n',
            '要给我们分配工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050049V#006F啊，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89A6(): pass

    label('loc_89A6')

    Jump('loc_8A15')

    def _loc_89A9(): pass

    label('loc_89A9')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050050V#010F在去城外之前去协会报到吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050051V嘉恩先生不是说\n',
            '要给我们分配工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8A15(): pass

    label('loc_8A15')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002B offset: 0x8A31
@scena.Code('func_2B_8A31')
def func_2B_8A31():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A49',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_8A50')

    def _loc_8A49(): pass

    label('loc_8A49')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_8A50(): pass

    label('loc_8A50')

    ChrTalk(
        0x0102,
        (
            '#0020050825V#010F还是先回协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050826V调查的结果说不定已经出来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002C offset: 0x8AC0
@scena.Code('func_2C_8AC0')
def func_2C_8AC0():
    OP_13(0x0048)

    Return()

# id: 0x002D offset: 0x8AC4
@scena.Code('func_2D_8AC4')
def func_2D_8AC4():
    OP_13(0x004D)

    Return()

# id: 0x002E offset: 0x8AC8
@scena.Code('func_2E_8AC8')
def func_2E_8AC8():
    OP_13(0x004C)

    Return()

# id: 0x002F offset: 0x8ACC
@scena.Code('func_2F_8ACC')
def func_2F_8ACC():
    OP_13(0x004A)

    Return()

# id: 0x0030 offset: 0x8AD0
@scena.Code('func_30_8AD0')
def func_30_8AD0():
    OP_13(0x004E)

    Return()

# id: 0x0031 offset: 0x8AD4
@scena.Code('func_31_8AD4')
def func_31_8AD4():
    OP_13(0x004B)

    Return()

# id: 0x0032 offset: 0x8AD8
@scena.Code('func_32_8AD8')
def func_32_8AD8():
    OP_13(0x0049)

    Return()

# id: 0x0033 offset: 0x8ADC
@scena.Code('func_33_8ADC')
def func_33_8ADC():
    OP_13(0x004F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
