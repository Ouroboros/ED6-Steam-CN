import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3101.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01750._CH', 'ED6_DT07/CH01750P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
    ]

# id: 0x10001 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '普利亚姆',
            x                   = -26340,
            z                   = 8000,
            y                   = 65489,
            direction           = 74,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '爱玲',
            x                   = -18800,
            z                   = 8000,
            y                   = 64430,
            direction           = 164,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '列曼',
            x                   = -24430,
            z                   = 8000,
            y                   = 68160,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '冈多夫',
            x                   = -24460,
            z                   = 8000,
            y                   = 67320,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿利瑟',
            x                   = -14900,
            z                   = 8000,
            y                   = 63190,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '温丝',
            x                   = -16239,
            z                   = 8000,
            y                   = 63190,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '雷伊',
            x                   = -19310,
            z                   = 8000,
            y                   = 60470,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
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
            name                = '格斯塔夫维修长',
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
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 19,
            chipIndex           = 19,
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
            dword_10            = 23,
            chipIndex           = 23,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 18,
            chipIndex           = 18,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 21,
            chipIndex           = 21,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 16,
            chipIndex           = 16,
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
            dword_10            = 11,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 19,
            chipIndex           = 19,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
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
            name                = '斯坦因',
            x                   = -48400,
            z                   = 25180,
            y                   = 59290,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '康丝坦茨',
            x                   = -41320,
            z                   = 22000,
            y                   = 50520,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '蔡斯飞船坪',
            x                   = -23030,
            z                   = 8000,
            y                   = 86970,
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
            name                = '蔡斯市·市区',
            x                   = 28060,
            z                   = 8000,
            y                   = 58980,
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

# id: 0x10002 offset: 0x65A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x65A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -35690,
            y           = 9750,
            z           = 58940,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = -23010,
            y           = 7750,
            z           = 74850,
            range       = 1500,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000015,
        ),
    )

# id: 0x10004 offset: 0x69A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -52000,
            triggerZ            = 25000,
            triggerY            = 59710,
            triggerRange        = 1700,
            actorX              = -52000,
            actorZ              = 26000,
            actorY              = 59710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6BE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_707',
    )

    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -49500, 25000, 57820, 270)
    ChrSetDirection(0x002B, 270, 0)
    ChrSetPos(0x002C, -45970, 25180, 58340, 270)
    ChrClearFlags(0x002C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_704',
    )

    def _loc_704(): pass

    label('loc_704')

    Jump('loc_777')

    def _loc_707(): pass

    label('loc_707')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_720',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_777')

    def _loc_720(): pass

    label('loc_720')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_743',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_777')

    def _loc_743(): pass

    label('loc_743')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_75C',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_777')

    def _loc_75C(): pass

    label('loc_75C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_777',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0010)

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_78E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0C_27E3)

    def _loc_78E(): pass

    label('loc_78E')

    Return()

# id: 0x0001 offset: 0x78F
@scena.Code('func_01_78F')
def func_01_78F():
    OP_16(0x02, 4000, -151000, -69000, 2293842)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_809',
    )

    OP_6F(0x0000, 59)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0001, 59)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0002, 59)
    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_76(0x00FF, 0x00000021, 0x0000, 0, 0, 0, 0x00, 0x00)
    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)
    StopEffect(0x83, 0x00)
    OP_10(0x04, 0x00)

    Jump('loc_82C')

    def _loc_809(): pass

    label('loc_809')

    OP_25(0x00A0, -4620, 5320, 59280, 10000, 30000, 0x64, 0x00000000)
    CreateThread(0x002A, 0x00, 0x00, func_02_839)

    def _loc_82C(): pass

    label('loc_82C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_838',
    )

    OP_64(0x00, 0x0001)

    def _loc_838(): pass

    label('loc_838')

    Return()

# id: 0x0002 offset: 0x839
@scena.Code('func_02_839')
def func_02_839():
    OP_72(0x0005, 0x0020)
    OP_72(0x0004, 0x0020)
    def _loc_843(): pass

    label('loc_843')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_86E',
    )

    OP_6F(0x0005, 40)
    OP_70(0x0005, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 40)
    OP_73(0x0005)

    Jump('loc_843')

    def _loc_86E(): pass

    label('loc_86E')

    Return()

# id: 0x0003 offset: 0x86F
@scena.Code('func_03_86F')
def func_03_86F():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_889',
    )

    OP_A9(0x9C)
    TalkEnd(0x0008)

    Return()

    def _loc_889(): pass

    label('loc_889')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89A',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_89A(): pass

    label('loc_89A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_9A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_94D',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎。\n',
            '来点冷饮怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听说了，\n',
            '导力器的恢复装置\n',
            '现在导力机能全部丧失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种时候更需要饮料！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来喝一瓶吧！\n',
            '恢复体力是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_9A6')

    def _loc_94D(): pass

    label('loc_94D')

    ChrTalk(
        0x00FE,
        (
            '在这种时候更需要饮料！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是滋补强身型还是营养补充型，\n',
            '各种饮料我这里都有哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A6(): pass

    label('loc_9A6')

    Jump('loc_D01')

    def _loc_9A9(): pass

    label('loc_9A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A4D',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器停止运转的时候\n',
            '引起了很大骚乱，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房长虽然拼命解释说明，\n',
            '但还是无法平息大家的不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也一样，连卖饮料\n',
            '的心情都受影响了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_A98')

    def _loc_A4D(): pass

    label('loc_A4D')

    ChrTalk(
        0x00FE,
        (
            '之前的骚乱真是不得了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都围在一起，\n',
            '工房长简直都快哭出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A98(): pass

    label('loc_A98')

    Jump('loc_D01')

    def _loc_A9B(): pass

    label('loc_A9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_B30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AEC',
    )

    ChrTalk(
        0x00FE,
        (
            '工房船刚才\n',
            '开走了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像有好几个研究员\n',
            '乘坐在上面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2D')

    def _loc_AEC(): pass

    label('loc_AEC')

    ChrTalk(
        0x00FE,
        (
            '工房船刚才\n',
            '开走了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎已经很久\n',
            '没看见那艘船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_B2D(): pass

    label('loc_B2D')

    Jump('loc_D01')

    def _loc_B30(): pass

    label('loc_B30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_BF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B85',
    )

    ChrTalk(
        0x00FE,
        (
            '工房船似乎已经\n',
            '开始准备出港了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目的地好像是\n',
            '雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BED')

    def _loc_B85(): pass

    label('loc_B85')

    ChrTalk(
        0x00FE,
        (
            '工房船似乎已经\n',
            '开始准备出港了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '列曼那家伙也\n',
            '充满干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来一定是很\n',
            '重要的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_BED(): pass

    label('loc_BED')

    Jump('loc_D01')

    def _loc_BF0(): pass

    label('loc_BF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_C3C',
    )

    ChrTalk(
        0x00FE,
        (
            '哟～辛苦了。\n',
            '要喝点什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里也有很多\n',
            '保健型饮品哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D01')

    def _loc_C3C(): pass

    label('loc_C3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_D01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C96',
    )

    ChrTalk(
        0x0008,
        (
            '呼～地震时真是吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在受惊的时候\n',
            '只要喝点饮料就会平静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D01')

    def _loc_C96(): pass

    label('loc_C96')

    ChrTalk(
        0x0008,
        (
            '呼～地震时真是吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在受惊的时候\n',
            '只要喝点饮料就会平静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以啦，\n',
            '要不要喝点冷饮？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_D01(): pass

    label('loc_D01')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xD05
@scena.Code('func_04_D05')
def func_04_D05():
    TalkBegin(0x0009)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F',
    )

    OP_A9(0x9D)
    TalkEnd(0x0009)

    Return()

    def _loc_D1F(): pass

    label('loc_D1F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D30',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_D30(): pass

    label('loc_D30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_DF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA2',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎光临。\n',
            '要买花吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算着急\n',
            '也没有任何用，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这样的时候\n',
            '就更想看花了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_DF0')

    def _loc_DA2(): pass

    label('loc_DA2')

    ChrTalk(
        0x00FE,
        (
            '就算着急\n',
            '也是没用的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，倒不如专心插花，\n',
            '还能让心情变得平静些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF0(): pass

    label('loc_DF0')

    Jump('loc_11CB')

    def _loc_DF3(): pass

    label('loc_DF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_EA1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E7D',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房的骚乱\n',
            '非常可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城里的居民们\n',
            '似乎都来势汹汹…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那样的事情，\n',
            '真希望不要再发生第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_E9E')

    def _loc_E7D(): pass

    label('loc_E7D')

    ChrTalk(
        0x00FE,
        (
            '中央工房的骚乱\n',
            '非常可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E9E(): pass

    label('loc_E9E')

    Jump('loc_11CB')

    def _loc_EA1(): pass

    label('loc_EA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_F7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EFC',
    )

    ChrTalk(
        0x00FE,
        (
            '本想让繁忙的他们\n',
            '多欣赏欣赏花草的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～看来要\n',
            '更加努力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F78')

    def _loc_EFC(): pass

    label('loc_EFC')

    ChrTalk(
        0x00FE,
        (
            '中央工房的人们\n',
            '好像总是那么忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本想让繁忙的他们\n',
            '多看看花，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，却总是从门前路过\n',
            '从不留步看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_F78(): pass

    label('loc_F78')

    Jump('loc_11CB')

    def _loc_F7B(): pass

    label('loc_F7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1039',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FEC',
    )

    ChrTalk(
        0x00FE,
        (
            '如果地方不大的话\n',
            '推荐选用小一些的花来摆放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在有限的空间内装饰\n',
            '多种颜色的花也很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1036')

    def _loc_FEC(): pass

    label('loc_FEC')

    ChrTalk(
        0x00FE,
        (
            '最近稍许素雅些的\n',
            '小型花很受欢迎哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经变成了花坛中的主角。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1036(): pass

    label('loc_1036')

    Jump('loc_11CB')

    def _loc_1039(): pass

    label('loc_1039')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_112B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_10A6',
    )

    ChrTalk(
        0x00FE,
        (
            '除了观赏用的花之外，\n',
            '还有在制作料理中使用的花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '请一定要试一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1128')

    def _loc_10A6(): pass

    label('loc_10A6')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '插花是很有意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除了观赏用的花之外，\n',
            '还有在制作料理中使用的花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话\n',
            '请一定要试一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1128(): pass

    label('loc_1128')

    Jump('loc_11CB')

    def _loc_112B(): pass

    label('loc_112B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_11CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1180',
    )

    ChrTalk(
        0x0009,
        (
            '飞船坪那边\n',
            '好像震得相当厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '在这里都能听得到\n',
            '惨叫声呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11CB')

    def _loc_1180(): pass

    label('loc_1180')

    ChrTalk(
        0x0009,
        (
            '还好……\n',
            '商品全都没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '已经好久没有过地震了，\n',
            '真是吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_11CB(): pass

    label('loc_11CB')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x11CF
@scena.Code('func_05_11CF')
def func_05_11CF():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1326',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1276',
    )

    ChrTalk(
        0x00FE,
        (
            '听说军队的警备艇\n',
            '好像也有一些紧急迫降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以时间来看的话，\n',
            '也许工房船也会有同样遭遇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么一想的话，\n',
            '也许我们还算是幸运的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1323')

    def _loc_1276(): pass

    label('loc_1276')

    ChrTalk(
        0x00FE,
        (
            '听说军队的警备艇\n',
            '好像也有一些紧急迫降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房船如果遇到相同遭遇的话，\n',
            '也许后果就不堪设想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为工房船和警备艇的性格构造是不同的，\n',
            '没办法进行那种安全着陆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1323(): pass

    label('loc_1323')

    Jump('loc_1573')

    def _loc_1326(): pass

    label('loc_1326')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13A4',
    )

    ChrTalk(
        0x00FE,
        (
            '工房船还没有从船库\n',
            '中出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还在\n',
            '整备状态中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我是操舵手，\n',
            '那些事不是我负责的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_13FA')

    def _loc_13A4(): pass

    label('loc_13A4')

    ChrTalk(
        0x00FE,
        (
            '导力引擎可不是\n',
            '普通的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有诗人在的话，\n',
            '一定会把机翼比作鸟的翅膀吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13FA(): pass

    label('loc_13FA')

    Jump('loc_1573')

    def _loc_13FD(): pass

    label('loc_13FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_14D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1456',
    )

    ChrTalk(
        0x00FE,
        (
            '新型引擎和\n',
            '『埃尔赛尤』的组合吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是想想就要让人\n',
            '流鼻血了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D6')

    def _loc_1456(): pass

    label('loc_1456')

    ChrTalk(
        0x00FE,
        (
            '说到最近的重要工作，\n',
            '那就是『埃尔赛尤』的主机换装了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新型的引擎\n',
            '要装载上去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来要去雷斯顿要塞\n',
            '进行工事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_14D6(): pass

    label('loc_14D6')

    Jump('loc_1573')

    def _loc_14D9(): pass

    label('loc_14D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1573',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～不管怎么说，地震在\n',
            '船降落后才发生真是幸运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是在降落的瞬间震动\n',
            '那后果就严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '驾驶定期船的那些人\n',
            '现在大概也是满手冷汗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1573(): pass

    label('loc_1573')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x1577
@scena.Code('func_06_1577')
def func_06_1577():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 1, 0x1641)),
            Expr.Return,
        ),
        'loc_15C2',
    )

    ChrTalk(
        0x00FE,
        (
            '军队的委托\n',
            '就交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到了王都那边\n',
            '也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C6E')

    def _loc_15C2(): pass

    label('loc_15C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18B8',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '喔！这不是阿加特吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#052F冈多夫，你回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，刚刚回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每次都把烂摊子留给你，\n',
            '真是不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 500)

    ChrTalk(
        0x00FE,
        (
            '还有那位小姐，\n',
            '也多亏你的帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔·布莱特的\n',
            '事迹我可是一直都有所耳闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在说这个可能有些晚了，\n',
            '不过还是祝贺你晋升为正游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿嘿，谢谢啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，经常会和那么危险\n',
            '的事件有关啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正也已经\n',
            '习惯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……对了。\n',
            '你们要离开蔡斯了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，接下来要去王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '王国军\n',
            '发来了正式委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '嘿，军队的委托？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我来的时候\n',
            '怎么就没有那种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F看来是凑巧了吧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '没赶对时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也好，那边就\n',
            '拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那么，在王都也\n',
            '也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯，再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C6B')

    def _loc_18B8(): pass

    label('loc_18B8')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0103, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哦，还以为是谁呢，\n',
            '那不是雪拉扎德吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F冈多夫？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你已经回蔡斯了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，刚刚回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀～不管怎样，\n',
            '真是好久没见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看样子你比以前\n',
            '又老练了不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F呵呵，说好话也没礼物给你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，帮我分担这么多工作就够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近经常出去办事，\n',
            '总是担心谁在负责蔡斯的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 500)

    ChrTalk(
        0x00FE,
        (
            '这位小姐也是\n',
            '帮了不少忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔·布莱特的\n',
            '事迹我可是一直都有所耳闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在说这个可能有些晚了，\n',
            '不过还是祝贺你晋升为正游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿嘿，谢谢啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，经常会和那么危险\n',
            '的事件有关啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正也已经\n',
            '习惯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……对了。\n',
            '你们要离开蔡斯了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，接下来要去王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '王国军\n',
            '发来了正式委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '嘿，军队的委托？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我来的时候\n',
            '怎么就没有那种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F……好像是搞错了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '没赶对时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也好，那边就\n',
            '拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '那么，在王都也\n',
            '也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯，再见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C6B(): pass

    label('loc_1C6B')

    SetScenaFlags(ScenaFlag(0x02C8, 1, 0x1641))

    def _loc_1C6E(): pass

    label('loc_1C6E')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x1C72
@scena.Code('func_07_1C72')
def func_07_1C72():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1D2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1CDE',
    )

    ChrTalk(
        0x00FE,
        (
            '我家的阳台已经\n',
            '没有放花坛的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～要是再放新花坛的话\n',
            '就要准备新架子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D29')

    def _loc_1CDE(): pass

    label('loc_1CDE')

    ChrTalk(
        0x00FE,
        (
            '可以只用小型花朵\n',
            '插载盆景哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～可是阳台已经\n',
            '没有地方放了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1D29(): pass

    label('loc_1D29')

    Jump('loc_1DDD')

    def _loc_1D2C(): pass

    label('loc_1D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1DDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1D8D',
    )

    ChrTalk(
        0x00FE,
        (
            '柔弱可怜的小型花朵\n',
            '也是很可爱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵～简直就像是\n',
            '年轻时的我一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DDD')

    def _loc_1D8D(): pass

    label('loc_1D8D')

    ChrTalk(
        0x00FE,
        (
            '哇，这个也很可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然大朵的花很漂亮，\n',
            '不过小型的花也是很可爱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1DDD(): pass

    label('loc_1DDD')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x1DE1
@scena.Code('func_08_1DE1')
def func_08_1DE1():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1F18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EB1',
    )

    ChrTalk(
        0x00FE,
        (
            '那么巨大的东西\n',
            '是怎么浮在天上的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是和飞船一样\n',
            '装载了导力引擎吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽然是这么想，\n',
            '但仔细思考一下的话还是不可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再怎么强的导力器也\n',
            '不可能有那么强的性能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1F15')

    def _loc_1EB1(): pass

    label('loc_1EB1')

    ChrTalk(
        0x00FE,
        (
            '那个东西能浮在天上，\n',
            '原理应该和飞船完全不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，导力引擎\n',
            '不可能有那么强的性能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F15(): pass

    label('loc_1F15')

    Jump('loc_2293')

    def _loc_1F18(): pass

    label('loc_1F18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2029',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FBC',
    )

    ChrTalk(
        0x00FE,
        (
            '也是很厉害的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个浮游物体一定\n',
            '是超越我们常识范围了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通过距离也许可以\n',
            '推算出它的大小吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那就要靠王国军\n',
            '来调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2026')

    def _loc_1FBC(): pass

    label('loc_1FBC')

    ChrTalk(
        0x00FE,
        (
            '那个浮游物体一定\n',
            '是超越我们常识范围内的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要测算出它的距离\n',
            '应该就可以知道它的具体大小了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2026(): pass

    label('loc_2026')

    Jump('loc_2293')

    def _loc_2029(): pass

    label('loc_2029')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_206C',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈已经忘记当初\n',
            '的目的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震对策怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2293')

    def _loc_206C(): pass

    label('loc_206C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_2225',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_20C7',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士的发明\n',
            '总是很惊人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他的做事效率\n',
            '一般人实在比不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2222')

    def _loc_20C7(): pass

    label('loc_20C7')

    ChrTurnDirection(0x000D, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那之后好久不见了。\n',
            '上次主日学校之后就一直没见面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F好久不见，温丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '和妈妈来买东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，是呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲\n',
            '今天也在工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，我们正要去设置\n',
            '最新的测量仪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是拉赛尔博士的新发明吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等下次在主日学校见面的时候\n',
            '再详细给我介绍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，下次见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F啊，嗯、下次见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2222(): pass

    label('loc_2222')

    Jump('loc_2293')

    def _loc_2225(): pass

    label('loc_2225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2293',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2255',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈最近只栽种\n',
            '那个品种。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2293')

    def _loc_2255(): pass

    label('loc_2255')

    ChrTalk(
        0x00FE,
        (
            '妈妈，请想一想吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '改变花坛配置\n',
            '是为了防止地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2293(): pass

    label('loc_2293')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x2297
@scena.Code('func_09_2297')
def func_09_2297():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2369',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_22F1',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵～目标\n',
            '已经定下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，回去以后\n',
            '马上准备必要材料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2366')

    def _loc_22F1(): pass

    label('loc_22F1')

    ChrTalk(
        0x00FE,
        (
            '呼～接下来准备构想\n',
            '种植在温室的作物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它的目的是『净化心灵』，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让人们心情平衡。\n',
            '一定会很受欢迎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2366(): pass

    label('loc_2366')

    Jump('loc_2473')

    def _loc_2369(): pass

    label('loc_2369')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2473',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_23C1',
    )

    ChrTalk(
        0x00FE,
        (
            '原来如此，观赏用吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那确实也是人类喜爱植物\n',
            '的一个理由呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2473')

    def _loc_23C1(): pass

    label('loc_23C1')

    ChrTalk(
        0x00FE,
        (
            '嗯，观赏用的花吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '摆上一盆，让研究室充满生机\n',
            '似乎也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以观赏用为视点\n',
            '似乎很有意思呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那确实也是人类喜爱植物\n',
            '的一个理由呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2473(): pass

    label('loc_2473')

    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x2477
@scena.Code('func_0A_2477')
def func_0A_2477():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_259B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2520',
    )

    ChrTalk(
        0x00FE,
        (
            '那个浮游物体出现的时候，\n',
            '据说天空闪耀着金色的光辉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从七耀石的属性来说的话，\n',
            '金是象征着『空间』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，两者之间\n',
            '应该有什么关联吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259B')

    def _loc_2520(): pass

    label('loc_2520')

    ChrTalk(
        0x00FE,
        (
            '我听说出现了奇怪的物体\n',
            '才特意来这里看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但没想到竟然是\n',
            '这么巨大的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国内究竟\n',
            '发生了什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_259B(): pass

    label('loc_259B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x259F
@scena.Code('func_0B_259F')
def func_0B_259F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_26C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_267C',
    )

    ChrTalk(
        0x00FE,
        (
            '本以为再过不久就是\n',
            '世界末日了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……距离黄昏似乎\n',
            '还有一段时间哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是回去拿一下\n',
            '遮阳伞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '长期遭受日晒的话\n',
            '皮肤会变差的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是要到另一个世界\n',
            '也要以最美的状态过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_26BE')

    def _loc_267C(): pass

    label('loc_267C')

    ChrTalk(
        0x00FE,
        (
            '看来世界末日\n',
            '还没有降临呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是回去拿一下\n',
            '遮阳伞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26BE(): pass

    label('loc_26BE')

    Jump('loc_27DF')

    def _loc_26C1(): pass

    label('loc_26C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_27DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2765',
    )

    ChrTalk(
        0x00FE,
        (
            '天空中漂浮着那种东西时\n',
            '还去工作的话简直就是傻瓜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '世界的末日大概\n',
            '已经不远了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在人生的尽头还在工作岗位上的话\n',
            '那也实在太逊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_27DF')

    def _loc_2765(): pass

    label('loc_2765')

    ChrTalk(
        0x00FE,
        (
            '天空中漂浮着那种东西时\n',
            '还去工作的话简直就是傻瓜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些整天只懂埋头工作的人，\n',
            '真正重要的东西他们都完全看不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27DF(): pass

    label('loc_27DF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x27E3
@scena.Code('func_0C_27E3')
def func_0C_27E3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    ChrSetPos(0x000F, -35290, 10000, 59780, 90)
    ChrSetPos(0x0010, -35230, 10000, 58160, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0009, -33900, 10000, 56360, 331)
    ChrSetPos(0x0008, -32920, 10000, 61360, 211)
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0011, -33530, 10000, 57330, 270)
    ChrSetPos(0x0012, -33050, 10000, 58910, 270)
    ChrSetPos(0x0013, -33880, 10000, 61340, 225)
    ChrSetPos(0x0014, -32500, 10000, 60280, 270)
    ChrSetPos(0x0015, -32360, 10000, 57680, 270)
    ChrSetPos(0x0016, -31130, 9600, 59060, 270)
    ChrSetPos(0x0017, -30660, 9100, 60320, 270)
    ChrSetPos(0x0018, -30670, 9200, 57500, 270)
    ChrSetPos(0x0019, -29220, 8000, 58710, 270)
    ChrSetPos(0x001A, -29090, 8000, 60610, 270)
    ChrSetPos(0x001B, -27830, 8000, 57460, 270)
    ChrSetPos(0x001C, -27220, 8000, 59380, 270)
    ChrSetPos(0x001D, -27240, 8000, 61340, 225)
    ChrSetPos(0x001E, -25050, 8000, 57430, 270)
    ChrSetPos(0x001F, -23040, 8000, 59720, 270)
    ChrSetPos(0x0020, -22340, 8000, 61820, 270)
    ChrSetPos(0x0021, -21800, 8000, 56830, 315)
    ChrSetPos(0x0022, -23720, 8000, 58160, 270)
    ChrSetPos(0x0023, -20480, 8000, 59330, 270)
    ChrSetPos(0x0024, -19770, 8000, 57860, 270)
    ChrSetPos(0x0025, -25080, 8000, 60640, 270)
    ChrSetPos(0x0026, -23770, 8000, 55620, 315)
    ChrSetPos(0x0027, -8950, 7510, 56760, 270)
    ChrSetPos(0x0028, -7210, 6760, 56690, 270)
    ChrSetPos(0x0029, -7900, 7010, 61680, 270)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
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
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
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
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    CameraMove(-14360, 8000, 59650, 0)
    OP_67(0, 8840, -10000, 0)
    CameraSetDistance(1580, 0)
    OP_6C(299000, 0)
    OP_6E(455, 0)
    CreateThread(0x000F, 0x01, 0x00, func_11_2DD3)
    CreateThread(0x0010, 0x01, 0x00, func_12_2E1D)
    CreateThread(0x0027, 0x00, 0x00, func_0E_2D0D)
    CreateThread(0x0028, 0x00, 0x00, func_0F_2D4F)
    CreateThread(0x0029, 0x00, 0x00, func_10_2D91)
    CreateThread(0x0011, 0x00, 0x00, func_0D_2BA3)
    OP_C8(0x0200, 0x0046, 'C_PLAC23._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_2B3D')
    def lambda_2B3D():
        CameraMove(-35500, 10000, 59580, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2B3D)

    @scena.Lambda('lambda_2B55')
    def lambda_2B55():
        OP_67(0, 7230, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_2B55)

    @scena.Lambda('lambda_2B6D')
    def lambda_2B6D():
        OP_6C(314000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_2B6D)

    OP_6E(513, 7000)
    Sleep(1000)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R0203._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x2BA3
@scena.Code('func_0D_2BA3')
def func_0D_2BA3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2D0C',
    )

    OP_62(0x0011, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    OP_62(0x0016, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x001B, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0020, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    OP_62(0x0025, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    Sleep(500)

    OP_62(0x0012, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0017, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0021, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    OP_62(0x0026, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    Sleep(500)

    OP_62(0x0013, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0018, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    OP_62(0x0022, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    Sleep(500)

    OP_62(0x0014, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0019, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0023, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    Sleep(500)

    OP_62(0x0015, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)
    OP_62(0x001A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_62(0x0024, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    Sleep(500)

    Jump('func_0D_2BA3')

    def _loc_2D0C(): pass

    label('loc_2D0C')

    Return()

# id: 0x000E offset: 0x2D0D
@scena.Code('func_0E_2D0D')
def func_0E_2D0D():
    ChrWalkTo(0x00FE, -12150, 8000, 56920, 4000, 0x00)
    ChrWalkTo(0x00FE, -16970, 8000, 58140, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)

    Return()

# id: 0x000F offset: 0x2D4F
@scena.Code('func_0F_2D4F')
def func_0F_2D4F():
    ChrWalkTo(0x00FE, -12150, 8000, 56920, 4000, 0x00)
    ChrWalkTo(0x00FE, -19540, 8000, 56110, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)

    Return()

# id: 0x0010 offset: 0x2D91
@scena.Code('func_10_2D91')
def func_10_2D91():
    ChrWalkTo(0x00FE, -12220, 8000, 61640, 4000, 0x00)
    ChrWalkTo(0x00FE, -19890, 8000, 60510, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 1900, 0x2C, 0x2F, 0x00000096, 0x01)

    Return()

# id: 0x0011 offset: 0x2DD3
@scena.Code('func_11_2DD3')
def func_11_2DD3():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    def _loc_2DE5(): pass

    label('loc_2DE5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E1C',
    )

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)

    Jump('loc_2DE5')

    def _loc_2E1C(): pass

    label('loc_2E1C')

    Return()

# id: 0x0012 offset: 0x2E1D
@scena.Code('func_12_2E1D')
def func_12_2E1D():
    Sleep(500)

    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    def _loc_2E34(): pass

    label('loc_2E34')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E6B',
    )

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)

    Jump('loc_2E34')

    def _loc_2E6B(): pass

    label('loc_2E6B')

    Return()

# id: 0x0013 offset: 0x2E6C
@scena.Code('func_13_2E6C')
def func_13_2E6C():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS185._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x2E9A
@scena.Code('func_14_2E9A')
def func_14_2E9A():
    OP_13(0x0085)

    Return()

# id: 0x0015 offset: 0x2E9E
@scena.Code('func_15_2E9E')
def func_15_2E9E():
    OP_13(0x0081)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
