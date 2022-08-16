import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
    ]

# id: 0x10001 offset: 0x1A2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '特莱斯主任',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '海泽尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '索黛丽娅',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            name                = '阿利瑟',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            name                = '米优',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            name                = '斯坦因',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            name                = '温丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
        ),
        ScenaNpcData(
            name                = '埃尔文',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0029,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x002A,
        ),
        ScenaNpcData(
            name                = '莱恩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '科奇莫爷爷',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            name                = '伊格尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '普利亚姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '爱玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '雷曼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '鲁迪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '菲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '埃里克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '康丝坦茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '雨果',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '普罗梅笛',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '雷伊',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '蒂亚利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '米妮亚姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '威尔姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            name                = '蔡斯飞艇坪',
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
            name                = '蔡斯市·市街区',
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

# id: 0x10002 offset: 0x5E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x5E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -10910,
            y           = 7000,
            z           = 63300,
            range       = -12900,
            dword_10    = 0x00002328,
            dword_14    = 0x0000D480,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000002D,
        ),
        ScenaEventData(
            x           = -19010,
            y           = 7000,
            z           = 74090,
            range       = -26870,
            dword_10    = 0x00002328,
            dword_14    = 0x00012714,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000034,
        ),
        ScenaEventData(
            x           = -50430,
            y           = 24000,
            z           = 53980,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = -35690,
            y           = 9750,
            z           = 58940,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000036,
        ),
        ScenaEventData(
            x           = -23010,
            y           = 7750,
            z           = 74850,
            range       = 1500,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000037,
        ),
    )

# id: 0x10004 offset: 0x682
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -50000,
            triggerZ            = 25000,
            triggerY            = 54010,
            triggerRange        = 800,
            actorX              = -50000,
            actorZ              = 26000,
            actorY              = 54010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_6B4',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_32_5F0E)

    def _loc_6B4(): pass

    label('loc_6B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_6CB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_33_6660)

    def _loc_6CB(): pass

    label('loc_6CB')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_6E3'),
        (0x00000067, 'loc_722'),
        (0x0000006B, 'loc_722'),
        (0x00000068, 'loc_735'),
        (-1, 'loc_73D'),
    )

    def _loc_6E3(): pass

    label('loc_6E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 3, 0x51B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6F9',
    )

    SetScenaFlags(ScenaFlag(0x00A3, 3, 0x51B))
    Event(0, func_2E_3DAE)

    Jump('loc_71F')

    def _loc_6F9(): pass

    label('loc_6F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70C',
    )

    Event(0, func_30_5099)

    Jump('loc_71F')

    def _loc_70C(): pass

    label('loc_70C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_71F',
    )

    SetScenaFlags(ScenaFlag(0x00A6, 7, 0x537))
    Event(0, func_31_598F)

    def _loc_71F(): pass

    label('loc_71F')

    Jump('loc_73D')

    def _loc_722(): pass

    label('loc_722')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_732',
    )

    Event(0, func_2F_41AF)

    def _loc_732(): pass

    label('loc_732')

    Jump('loc_73D')

    def _loc_735(): pass

    label('loc_735')

    PlaySE(14, 0x00, 0x64)

    Jump('loc_73D')

    def _loc_73D(): pass

    label('loc_73D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_79F',
    )

    ChrSetPos(0x000D, -14600, 8000, 63040, 6)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x0010, -15440, 8000, 63040, 3)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_E6F')

    def _loc_79F(): pass

    label('loc_79F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_832',
    )

    ChrSetPos(0x000D, -21460, 8000, 58770, 270)
    ChrSetPos(0x0010, -20870, 8000, 59640, 270)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -23240, 8000, 57820, 45)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -23310, 8000, 59800, 135)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_E6F')

    def _loc_832(): pass

    label('loc_832')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_868',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_E6F')

    def _loc_868(): pass

    label('loc_868')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_89E',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -25190, 8000, 66790, 275)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -17150, 8000, 63800, 358)

    Jump('loc_E6F')

    def _loc_89E(): pass

    label('loc_89E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_98D',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -23800, 10000, 46930, 180)
    CreateThread(0x0011, 0x00, 0x00, func_03_10F6)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -23170, 8000, 59080, 91)
    CreateThread(0x0012, 0x00, 0x00, func_05_12A2)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -25200, 8000, 67400, 272)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, -31870, 10000, 49240, 326)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -33120, 10000, 50470, 135)
    ChrSetFlags(0x0017, 0x0010)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -23610, 8000, 70240, 5)
    CreateThread(0x001A, 0x00, 0x00, func_06_12C6)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, -48310, 22000, 49830, 163)

    Jump('loc_E6F')

    def _loc_98D(): pass

    label('loc_98D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_CF9',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -30660, 9000, 60810, 69)
    CreateThread(0x000A, 0x00, 0x00, func_03_10F6)

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0025, -24500, 8750, 51360, 18)

    ExecExpressionWithValue(
        0x0025,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -34110, 10000, 62990, 166)
    CreateThread(0x0011, 0x00, 0x00, func_04_127E)

    ExecExpressionWithValue(
        0x0011,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    ExecExpressionWithValue(
        0x0019,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -23610, 8000, 70240, 5)
    CreateThread(0x001A, 0x00, 0x00, func_06_12C6)

    ExecExpressionWithValue(
        0x001A,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -27110, 8000, 60420, 69)
    ChrSetFlags(0x001B, 0x0010)

    ExecExpressionWithValue(
        0x001B,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, -27070, 8000, 59620, 359)
    ChrSetFlags(0x001C, 0x0010)

    ExecExpressionWithValue(
        0x001C,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -33870, 10000, 57010, 292)

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -30810, 10000, 48800, 320)
    CreateThread(0x001D, 0x00, 0x00, func_07_12EA)

    ExecExpressionWithValue(
        0x001D,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32630, 10000, 58920, 255)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, -26600, 8000, 55790, 279)

    ExecExpressionWithValue(
        0x001E,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, -21730, 8000, 53410, 270)
    CreateThread(0x001F, 0x00, 0x00, func_08_130E)

    ExecExpressionWithValue(
        0x001F,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -29430, 8000, 57220, 85)
    ChrSetFlags(0x0017, 0x0010)

    ExecExpressionWithValue(
        0x0017,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x0021, -22660, 8000, 61960, 82)
    CreateThread(0x0021, 0x00, 0x00, func_0A_1356)

    ExecExpressionWithValue(
        0x0021,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0022, 0x0080)
    ChrSetPos(0x0022, -33530, 10000, 52430, 296)

    ExecExpressionWithValue(
        0x0022,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0023, -33770, 10000, 51140, 330)

    ExecExpressionWithValue(
        0x0023,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, -25860, 8000, 60310, 263)

    ExecExpressionWithValue(
        0x0024,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0026, -21670, 8000, 66490, 242)

    ExecExpressionWithValue(
        0x0026,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0020, -23200, 10000, 47850, 272)
    CreateThread(0x0020, 0x00, 0x00, func_09_1332)

    ExecExpressionWithValue(
        0x0020,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -30230, 10000, 47900, 298)

    ExecExpressionWithValue(
        0x000F,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_E6F')

    def _loc_CF9(): pass

    label('loc_CF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_D4C',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -23610, 8000, 70240, 5)
    CreateThread(0x001A, 0x00, 0x00, func_06_12C6)

    Jump('loc_E6F')

    def _loc_D4C(): pass

    label('loc_D4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_D82',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_E6F')

    def _loc_D82(): pass

    label('loc_D82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_DB8',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_E6F')

    def _loc_DB8(): pass

    label('loc_DB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_E10',
    )

    ChrSetPos(0x000D, -14600, 8000, 63040, 6)
    ChrSetPos(0x0010, -15440, 8000, 63040, 3)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_E6F')

    def _loc_E10(): pass

    label('loc_E10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_E6F',
    )

    ChrSetPos(0x000D, -14600, 8000, 63040, 6)
    ChrSetFlags(0x000D, 0x0010)
    ChrSetPos(0x0010, -15440, 8000, 63040, 3)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    def _loc_E6F(): pass

    label('loc_E6F')

    Return()

# id: 0x0001 offset: 0xE70
@scena.Code('func_01_E70')
def func_01_E70():
    OP_16(0x02, 4000, -151000, -69000, 196690)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E9A',
    )

    OP_B1('t3101_y')

    Jump('loc_EA3')

    def _loc_E9A(): pass

    label('loc_E9A')

    OP_B1('t3101_n')

    def _loc_EA3(): pass

    label('loc_EA3')

    OP_6F(0x0005, 40)
    OP_70(0x0005, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EC9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_EF6')

    def _loc_EC9(): pass

    label('loc_EC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EE1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_EF6')

    def _loc_EE1(): pass

    label('loc_EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EF6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EF6(): pass

    label('loc_EF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F0A',
    )

    OP_72(0x0003, 0x0010)

    Jump('loc_F0E')

    def _loc_F0A(): pass

    label('loc_F0A')

    OP_64(0x00, 0x0001)

    def _loc_F0E(): pass

    label('loc_F0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_109C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1090',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 7, 0x547)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 0, 0x548)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 1, 0x549)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 2, 0x54A)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 3, 0x54B)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1090',
    )

    LoadEffect(0x00, 'map\\\\mp011_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -49690, 25000, 54030, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 1000)
    PlayEffect(0x00, 0xFF, 0x00FF, -39390, 22000, 56200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 1000)
    PlayEffect(0x00, 0xFF, 0x00FF, -39390, 22000, 61640, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 1000)
    PlayEffect(0x00, 0xFF, 0x00FF, -39850, 19620, 65980, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 1000)
    PlayEffect(0x00, 0xFF, 0x00FF, -39770, 17290, 50070, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 1000)
    PlayEffect(0x00, 0xFF, 0x00FF, -37130, 10000, 58950, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 1000)

    def _loc_1090(): pass

    label('loc_1090')

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 60)

    def _loc_109C(): pass

    label('loc_109C')

    OP_25(0x00A0, -4620, 5320, 59280, 10000, 30000, 0x64, 0x00000000)
    CreateThread(0x0027, 0x00, 0x00, func_02_10C0)

    Return()

# id: 0x0002 offset: 0x10C0
@scena.Code('func_02_10C0')
def func_02_10C0():
    OP_72(0x0005, 0x0020)
    OP_72(0x0004, 0x0020)
    def _loc_10CA(): pass

    label('loc_10CA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10F5',
    )

    OP_6F(0x0005, 40)
    OP_70(0x0005, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 40)
    OP_73(0x0005)

    Jump('loc_10CA')

    def _loc_10F5(): pass

    label('loc_10F5')

    Return()

# id: 0x0003 offset: 0x10F6
@scena.Code('func_03_10F6')
def func_03_10F6():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        'loc_1126',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_1268')

    def _loc_1126(): pass

    label('loc_1126')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_113F',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_1268')

    def _loc_113F(): pass

    label('loc_113F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1158',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_1268')

    def _loc_1158(): pass

    label('loc_1158')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1171',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_1268')

    def _loc_1171(): pass

    label('loc_1171')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_118A',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_1268')

    def _loc_118A(): pass

    label('loc_118A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A3',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_1268')

    def _loc_11A3(): pass

    label('loc_11A3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11BC',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_1268')

    def _loc_11BC(): pass

    label('loc_11BC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_1268')

    def _loc_11D5(): pass

    label('loc_11D5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11EE',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_1268')

    def _loc_11EE(): pass

    label('loc_11EE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1207',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_1268')

    def _loc_1207(): pass

    label('loc_1207')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1220',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_1268')

    def _loc_1220(): pass

    label('loc_1220')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1239',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_1268')

    def _loc_1239(): pass

    label('loc_1239')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1252',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_1268')

    def _loc_1252(): pass

    label('loc_1252')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1268',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_1268(): pass

    label('loc_1268')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_127D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_1268')

    def _loc_127D(): pass

    label('loc_127D')

    Return()

# id: 0x0004 offset: 0x127E
@scena.Code('func_04_127E')
def func_04_127E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12A1',
    )

    OP_8D(0x00FE, -35270, 61360, -33040, 64150, 3000)

    Jump('func_04_127E')

    def _loc_12A1(): pass

    label('loc_12A1')

    Return()

# id: 0x0005 offset: 0x12A2
@scena.Code('func_05_12A2')
def func_05_12A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12C5',
    )

    OP_8D(0x00FE, -26390, 55950, -19770, 61950, 3000)

    Jump('func_05_12A2')

    def _loc_12C5(): pass

    label('loc_12C5')

    Return()

# id: 0x0006 offset: 0x12C6
@scena.Code('func_06_12C6')
def func_06_12C6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12E9',
    )

    OP_8D(0x00FE, -25190, 68440, -20920, 71850, 3000)

    Jump('func_06_12C6')

    def _loc_12E9(): pass

    label('loc_12E9')

    Return()

# id: 0x0007 offset: 0x12EA
@scena.Code('func_07_12EA')
def func_07_12EA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_130D',
    )

    OP_8D(0x00FE, -32689, 46510, -30620, 50700, 3000)

    Jump('func_07_12EA')

    def _loc_130D(): pass

    label('loc_130D')

    Return()

# id: 0x0008 offset: 0x130E
@scena.Code('func_08_130E')
def func_08_130E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1331',
    )

    OP_8D(0x00FE, -25190, 54660, -20780, 60740, 3000)

    Jump('func_08_130E')

    def _loc_1331(): pass

    label('loc_1331')

    Return()

# id: 0x0009 offset: 0x1332
@scena.Code('func_09_1332')
def func_09_1332():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1355',
    )

    OP_8D(0x00FE, -26510, 46520, -19100, 49060, 3000)

    Jump('func_09_1332')

    def _loc_1355(): pass

    label('loc_1355')

    Return()

# id: 0x000A offset: 0x1356
@scena.Code('func_0A_1356')
def func_0A_1356():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1379',
    )

    OP_8D(0x00FE, -23960, 59250, -21170, 66410, 3000)

    Jump('func_0A_1356')

    def _loc_1379(): pass

    label('loc_1379')

    Return()

# id: 0x000B offset: 0x137A
@scena.Code('func_0B_137A')
def func_0B_137A():
    Return()

# id: 0x000C offset: 0x137B
@scena.Code('func_0C_137B')
def func_0C_137B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_13DF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560080721V#690F这烟真是好大啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560080722V连中央工房的换气能力\n',
            '也应付不过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13DF(): pass

    label('loc_13DF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x13E3
@scena.Code('func_0D_13E3')
def func_0D_13E3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1435',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '好久没有这么拼命地奔跑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，真糟糕。\n',
            '情况糟透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1435(): pass

    label('loc_1435')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1439
@scena.Code('func_0E_1439')
def func_0E_1439():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_148B',
    )

    ChrTalk(
        0x00FE,
        (
            '工房里面\n',
            '已经到处是浓烟了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼～～～～\n',
            '我还以为死定了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_148B(): pass

    label('loc_148B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x148F
@scena.Code('func_0F_148F')
def func_0F_148F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_14D0',
    )

    ChrTalk(
        0x00FE,
        (
            '有没有受伤的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有的话\n',
            '要马上通知我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14D0(): pass

    label('loc_14D0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x14D4
@scena.Code('func_10_14D4')
def func_10_14D4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1522',
    )

    ChrTalk(
        0x00FE,
        (
            '前、前辈！\n',
            '怎么办呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生火灾的话，\n',
            '研究数据就要毁掉了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1522(): pass

    label('loc_1522')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1526
@scena.Code('func_11_1526')
def func_11_1526():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_15BB',
    )

    ChrTalk(
        0x00FE,
        (
            '……呼，好奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论怎么看\n',
            '都不像火灾所冒出的烟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '大家也都没有能冒烟的实验装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么这些烟\n',
            '是从哪里出来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15BB(): pass

    label('loc_15BB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x15BF
@scena.Code('func_12_15BF')
def func_12_15BF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_162A',
    )

    ChrTalk(
        0x00FE,
        (
            '我都不清楚\n',
            '自己是怎么逃出来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在逃生的途中\n',
            '我突然想起了空贼事件……\n',
            '脚差点踩空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_162A(): pass

    label('loc_162A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x162E
@scena.Code('func_13_162E')
def func_13_162E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_16F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_169A',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来\n',
            '的确没有看到拉赛尔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那家伙应该不用让人担心。\n',
            '肯定已经逃出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16EF')

    def _loc_169A(): pass

    label('loc_169A')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '紧急通道也是很有用处的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没那玩意儿的话\n',
            '就只能从阳台上跳下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16EF(): pass

    label('loc_16EF')

    Jump('loc_172E')

    def _loc_16F2(): pass

    label('loc_16F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_172E',
    )

    ChrTalk(
        0x00FE,
        (
            '痛、痛痛痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不小心踏空楼梯，\n',
            '扭到腰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_172E(): pass

    label('loc_172E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x1732
@scena.Code('func_14_1732')
def func_14_1732():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_17B9',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在做实验的时候，\n',
            '突然冒起了漫天烟雾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '我是拼命逃出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想大家也\n',
            '应该都逃出来了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17B9(): pass

    label('loc_17B9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x17BD
@scena.Code('func_15_17BD')
def func_15_17BD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_17DC',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵呀～噢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17DC(): pass

    label('loc_17DC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x17E0
@scena.Code('func_16_17E0')
def func_16_17E0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_1A34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 5, 0x1D)),
            Expr.Return,
        ),
        'loc_184E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是早点回家吧。\n',
            '不管再发生什么我都要回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A31')

    def _loc_184E(): pass

    label('loc_184E')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_18B8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是早点回家吧。\n',
            '不管再发生什么我都要回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0003, 5, 0x1D))

    Jump('loc_1A31')

    def _loc_18B8(): pass

    label('loc_18B8')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_1943',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔，这种情况下\n',
            '还是不要谈工作的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不好意思，\n',
            '明天再把书给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0003, 5, 0x1D))

    Jump('loc_1A31')

    def _loc_1943(): pass

    label('loc_1943')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_19C6',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，建筑物里都是烟，\n',
            '好讨厌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唔，这种情况下\n',
            '还是不要谈工作的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '委托的事\n',
            '只好拖到明天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0003, 5, 0x1D))

    Jump('loc_1A31')

    def _loc_19C6(): pass

    label('loc_19C6')

    ChrTalk(
        0x00FE,
        (
            '呼，因为刚才拼命地跑，\n',
            '身上的肌肉痛得受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是早点回家吧。\n',
            '不管再发生什么我都要回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0003, 5, 0x1D))

    def _loc_1A31(): pass

    label('loc_1A31')

    Jump('loc_1A7A')

    def _loc_1A34(): pass

    label('loc_1A34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1A7A',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '好久没有这样剧烈运动过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，痛啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A7A(): pass

    label('loc_1A7A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x1A7E
@scena.Code('func_17_1A7E')
def func_17_1A7E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1AF5',
    )

    ChrTalk(
        0x0009,
        (
            '#0550080723V#800F博士应该在三楼的工作室。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080724V首先去那里确认一下。\n',
            '如果危险的话就马上撤离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF5(): pass

    label('loc_1AF5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x1AF9
@scena.Code('func_18_1AF9')
def func_18_1AF9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1B60',
    )

    ChrTalk(
        0x0008,
        (
            '#0280080725V#150F我也想一起去呀。\n',
            '但没办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080726V小艾你们千万要小心呀。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B60(): pass

    label('loc_1B60')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x1B64
@scena.Code('func_19_1B64')
def func_19_1B64():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1BAD',
    )

    ChrTalk(
        0x00FE,
        (
            '客、客人，\n',
            '你们都顺利逃出来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这烟也太大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BAD(): pass

    label('loc_1BAD')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x1BB1
@scena.Code('func_1A_1BB1')
def func_1A_1BB1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1C1B',
    )

    ChrTalk(
        0x00FE,
        (
            '哪里都找不到\n',
            '拉赛尔博士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定……\n',
            '难道还在工房里面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，该怎么办才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C1B(): pass

    label('loc_1C1B')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x1C1F
@scena.Code('func_1B_1C1F')
def func_1B_1C1F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1C3F',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁迪，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3F(): pass

    label('loc_1C3F')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x1C43
@scena.Code('func_1C_1C43')
def func_1C_1C43():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1CA1',
    )

    ChrTalk(
        0x00FE,
        (
            '咳咳、咳咳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '烟、烟……\n',
            '咳咳、咳咳咳、咳咳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肺、肺……\n',
            '咳咳、咳咳！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CA1(): pass

    label('loc_1CA1')

    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x1CA5
@scena.Code('func_1D_1CA5')
def func_1D_1CA5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1D77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_1D1E',
    )

    ChrTalk(
        0x00FE,
        (
            '不过……\n',
            '那些从里面出来的\n',
            '穿着军装的家伙是谁呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明那么大的烟，\n',
            '他们却好像一点事也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D74')

    def _loc_1D1E(): pass

    label('loc_1D1E')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '中央工房\n',
            '开始冒烟的时候，\n',
            '我可紧张坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，都怪这烟，\n',
            '喉咙又开始渴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D74(): pass

    label('loc_1D74')

    Jump('loc_1E25')

    def _loc_1D77(): pass

    label('loc_1D77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1DBA',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊啊，怎么会这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到、到底\n',
            '发生什么事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E25')

    def _loc_1DBA(): pass

    label('loc_1DBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1E25',
    )

    ChrTalk(
        0x00FE,
        (
            '在整个王国中，\n',
            '穿着作业服的驾驶员也只有我一个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这和衣服没有关系，\n',
            '关键在于技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E25(): pass

    label('loc_1E25')

    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x1E29
@scena.Code('func_1E_1E29')
def func_1E_1E29():
    TalkBegin(0x0018)
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
        'loc_1E87',
    )

    OP_0D()
    OP_A9(0x4D)
    OP_56(0x00)
    TalkEnd(0x0018)

    Return()

    def _loc_1E87(): pass

    label('loc_1E87')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E98',
    )

    TalkEnd(0x0018)

    Return()

    def _loc_1E98(): pass

    label('loc_1E98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Return,
        ),
        'loc_1EF2',
    )

    ChrTalk(
        0x0018,
        (
            '军队的警备飞艇\n',
            '好像停在港口呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '又没有发生什么事件，\n',
            '实在是很少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_1EF2(): pass

    label('loc_1EF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1F77',
    )

    ChrTalk(
        0x0018,
        (
            '哟，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '前些日子，\n',
            '进出工房船的人好频繁呢，\n',
            '不过这两天又恢复平静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '今天的飞艇坪\n',
            '从早上开始就很安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_1F77(): pass

    label('loc_1F77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2005',
    )

    ChrTalk(
        0x0018,
        (
            '哟，你们今天也很忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '说到忙，\n',
            '刚才雷曼那家伙\n',
            '慌张地跑向飞艇坪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '看来很着急\n',
            '要出动工房船的样子。\n',
            '他还真是辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_2005(): pass

    label('loc_2005')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2048',
    )

    ChrTalk(
        0x0018,
        (
            '哟，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '早上最好还是\n',
            '喝杯营养丰富的饮料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_2048(): pass

    label('loc_2048')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_20BE',
    )

    ChrTalk(
        0x0018,
        (
            '哟，这么晚还在辛苦工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哎呀哎呀，\n',
            '今天也累得要命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '差不多该关店了，\n',
            '想要什么就快点选吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_20BE(): pass

    label('loc_20BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_218E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2134',
    )

    ChrTalk(
        0x0018,
        (
            '从中央工房出来的\n',
            '穿蓝色军装的家伙，\n',
            '到底是什么人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '不知道那些军人\n',
            '在工房里面干了些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_218B')

    def _loc_2134(): pass

    label('loc_2134')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0018,
        (
            '呼～\n',
            '看来骚动总算结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '说起来，那些军人\n',
            '在那么浓重的烟雾里干了什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_218B(): pass

    label('loc_218B')

    Jump('loc_24F1')

    def _loc_218E(): pass

    label('loc_218E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_21F1',
    )

    ChrTalk(
        0x0018,
        (
            '这、这种时候\n',
            '必须冷静地行动！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '那么，\n',
            '大家请先喝点清凉的饮料，\n',
            '稍微冷静一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_21F1(): pass

    label('loc_21F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_22E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2273',
    )

    ChrTalk(
        0x0018,
        (
            '那边的雷曼\n',
            '其实是飞艇的驾驶员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '我说的飞艇\n',
            '不是定期船而是工房船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '嗯，\n',
            '反正都是在天上飞的家伙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E3')

    def _loc_2273(): pass

    label('loc_2273')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0018,
        (
            '那边的雷曼\n',
            '怎么看都是个维修员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '不过，\n',
            '其实他是飞艇的驾驶员哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哈哈哈～\n',
            '真是人不可貌相啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22E3(): pass

    label('loc_22E3')

    Jump('loc_24F1')

    def _loc_22E6(): pass

    label('loc_22E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_2400',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_236E',
    )

    ChrTalk(
        0x0018,
        (
            '做生意不只是买卖商品，\n',
            '还必须要考虑经营的手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '想开间有人情味的店，\n',
            '嘴上说起来简单，\n',
            '但是实现起来却很难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23FD')

    def _loc_236E(): pass

    label('loc_236E')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0018,
        (
            '我们的愿望是\n',
            '拥有一间属于我们自己的店子，\n',
            '就算规模很小也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '可以的话，最好能开间\n',
            '像这座城里的『贝尔杂货店』\n',
            '那样有人情味的小店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23FD(): pass

    label('loc_23FD')

    Jump('loc_24F1')

    def _loc_2400(): pass

    label('loc_2400')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2458',
    )

    ChrTalk(
        0x0018,
        (
            '对面卖花的爱玲\n',
            '是我的妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '如果可以的话，\n',
            '希望大家也到那边去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_2458(): pass

    label('loc_2458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_24F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_24BD',
    )

    ChrTalk(
        0x0018,
        (
            '要不要喝点\n',
            '清凉的饮料呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '我这里卖的饮料不仅美味，\n',
            '对身体也很有益哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F1')

    def _loc_24BD(): pass

    label('loc_24BD')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x0018,
        (
            '哟，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '要不要喝点\n',
            '清凉的饮料呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24F1(): pass

    label('loc_24F1')

    TalkEnd(0x0018)

    Return()

# id: 0x001F offset: 0x24F5
@scena.Code('func_1F_24F5')
def func_1F_24F5():
    TalkBegin(0x0019)
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
        'loc_2553',
    )

    OP_0D()
    OP_A9(0x4E)
    OP_56(0x00)
    TalkEnd(0x0019)

    Return()

    def _loc_2553(): pass

    label('loc_2553')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2564',
    )

    TalkEnd(0x0019)

    Return()

    def _loc_2564(): pass

    label('loc_2564')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Return,
        ),
        'loc_25B1',
    )

    ChrTalk(
        0x0019,
        (
            '哎，从飞艇坪那边\n',
            '传来了汽笛的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '……发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_25B1(): pass

    label('loc_25B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2613',
    )

    ChrTalk(
        0x0019,
        (
            '来，请看一看。\n',
            '这里卖的都是很漂亮的花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '忘记讨厌的事，\n',
            '买一盆来舒缓心情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_2613(): pass

    label('loc_2613')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_268F',
    )

    ChrTalk(
        0x0019,
        (
            '啊，客人们都在议论最近的事情，\n',
            '没人来好好欣赏花了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '毕竟发生了那样的事情……\n',
            '不过我还是觉得有些寂寞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_268F(): pass

    label('loc_268F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_26E3',
    )

    ChrTalk(
        0x0019,
        (
            '啊，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '请随意看吧。\n',
            '就算是只闻闻花香\n',
            '也能让你心情愉快的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_26E3(): pass

    label('loc_26E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2734',
    )

    ChrTalk(
        0x0019,
        (
            '啊，晚上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '虽然马上要关店了，\n',
            '不过趁现在挑选鲜花也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_2734(): pass

    label('loc_2734')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2794',
    )

    ChrTalk(
        0x0019,
        (
            '我正想着烟可能快要散了，\n',
            '工房里就出来了几位军人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '难道是他们\n',
            '把烟止住的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_2794(): pass

    label('loc_2794')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_27BD',
    )

    ChrTalk(
        0x0019,
        (
            '不、不好了！\n',
            '怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_27BD(): pass

    label('loc_27BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2828',
    )

    ChrTalk(
        0x0019,
        (
            '蔡斯城里的绿色\n',
            '越来越少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '就算一次也好，\n',
            '好想去参观一下那个\n',
            '以花闻名的玛诺利亚村啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_2828(): pass

    label('loc_2828')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2890',
    )

    ChrTalk(
        0x0019,
        (
            '那边卖饮料的\n',
            '是我的哥哥哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我们的梦想是兄妹一起加油，\n',
            '将来开间属于自己的店子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_2890(): pass

    label('loc_2890')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_28DC',
    )

    ChrTalk(
        0x0019,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '这里有各种漂亮的鲜花，\n',
            '请各位客人慢慢观赏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28DC(): pass

    label('loc_28DC')

    TalkEnd(0x0019)

    Return()

# id: 0x0020 offset: 0x28E0
@scena.Code('func_20_28E0')
def func_20_28E0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2967',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2923',
    )

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
            '喝了点饮料，\n',
            '终于放松下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2967')

    def _loc_2923(): pass

    label('loc_2923')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

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
            '这个案件真是让人震惊啊。\n',
            '没办法安心回去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2967(): pass

    label('loc_2967')

    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x296B
@scena.Code('func_21_296B')
def func_21_296B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2A5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2A02',
    )

    ChrTalk(
        0x00FE,
        (
            '你们没事实在是太好了，\n',
            '不过没看到拉赛尔呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然如果他没事的时候\n',
            '就会给别人带来各种各样的麻烦，\n',
            '不过还是有点担心他啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5B')

    def _loc_2A02(): pass

    label('loc_2A02')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '哦哦，伊格尔。\n',
            '你没受伤真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是从紧急楼梯下来的吗？\n',
            '想必一定很累吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A5B(): pass

    label('loc_2A5B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x2A5F
@scena.Code('func_22_2A5F')
def func_22_2A5F():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x2A66
@scena.Code('func_23_2A66')
def func_23_2A66():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x2A6D
@scena.Code('func_24_2A6D')
def func_24_2A6D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2AD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2AAA',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队的制服……\n',
            '的确是让人在意呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD6')

    def _loc_2AAA(): pass

    label('loc_2AAA')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '工房袭击犯竟然\n',
            '穿着亲卫队的制服吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD6(): pass

    label('loc_2AD6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x2ADA
@scena.Code('func_25_2ADA')
def func_25_2ADA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2B9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2B2C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '越来越想不明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买盆花来\n',
            '调节一下心情吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B99')

    def _loc_2B2C(): pass

    label('loc_2B2C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '尽管如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '袭击中央工房的犯人\n',
            '到现在都还没抓到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军和游击士协会\n',
            '到底都在干什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B99(): pass

    label('loc_2B99')

    Jump('loc_2E24')

    def _loc_2B9C(): pass

    label('loc_2B9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2C1F',
    )

    ChrTalk(
        0x00FE,
        (
            '很多人都说\n',
            '从工房出来的是穿蓝色军装的军人，\n',
            '所以应该是不会有错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且温丝也说他看见了。\n',
            '亲卫队果然很可疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E24')

    def _loc_2C1F(): pass

    label('loc_2C1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2DE1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2C7E',
    )

    ChrTalk(
        0x00FE,
        (
            '我一要买什么，\n',
            '温丝就处处有意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '这个孩子就喜欢斤斤计较。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DDE')

    def _loc_2C7E(): pass

    label('loc_2C7E')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000D, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，提妲，\n',
            '在为客人带路吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，您好，阿利瑟阿姨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在挑选鲜花吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，是呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一要买什么，\n',
            '温丝就处处有意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '这个孩子就喜欢斤斤计较。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000D, 400)

    ChrTalk(
        0x0010,
        (
            '不是我斤斤计较，\n',
            '而是妈妈太浪费啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 0, 300)
    OP_62(0x000D, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#065F哎，这个……请别生气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DDE(): pass

    label('loc_2DDE')

    Jump('loc_2E24')

    def _loc_2DE1(): pass

    label('loc_2DE1')

    ChrTalk(
        0x00FE,
        (
            '哇，好漂亮的花呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过种在阳台上的话，\n',
            '颜色有些不合适。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E24(): pass

    label('loc_2E24')

    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x2E28
@scena.Code('func_26_2E28')
def func_26_2E28():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2EE5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2EAD',
    )

    ChrTalk(
        0x00FE,
        (
            '就连亲卫队\n',
            '也在这里出现了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果顺利的话，\n',
            '我就能出名啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '决定了！\n',
            '我一定要成为工房的接待小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EE5')

    def _loc_2EAD(): pass

    label('loc_2EAD')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎！亲卫队！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果顺利的话，\n',
            '我就能出名啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EE5(): pass

    label('loc_2EE5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x2EE9
@scena.Code('func_27_2EE9')
def func_27_2EE9():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '看起来\n',
            '不像是火灾呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但那么多烟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x2F2B
@scena.Code('func_28_2F2B')
def func_28_2F2B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2FE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2F8B',
    )

    ChrTalk(
        0x00FE,
        (
            '结果最后还是不知道\n',
            '那些穿军装的人的真面目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们到底\n',
            '是什么人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FE6')

    def _loc_2F8B(): pass

    label('loc_2F8B')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '妈妈，王国军和协会\n',
            '都已经尽力去调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只不过那些情况\n',
            '是不可能让我们知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FE6(): pass

    label('loc_2FE6')

    Jump('loc_311B')

    def _loc_2FE9(): pass

    label('loc_2FE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3045',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈，我看见的是\n',
            '『穿蓝色军装的军人』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可没说过\n',
            '我看见的是亲卫队哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_311B')

    def _loc_3045(): pass

    label('loc_3045')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_30F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_307E',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '提妲，\n',
            '工房的工作要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30EF')

    def _loc_307E(): pass

    label('loc_307E')

    ChrTurnDirection(0x00FE, 0x0107, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '提妲，你好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F你好，温丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也要去工房工作吗？\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30EF(): pass

    label('loc_30EF')

    Jump('loc_311B')

    def _loc_30F2(): pass

    label('loc_30F2')

    ChrTalk(
        0x00FE,
        (
            '妈妈，\n',
            '阳台的花坛已经放满花盆了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_311B(): pass

    label('loc_311B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x311F
@scena.Code('func_29_311F')
def func_29_311F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3256',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_31B4',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我也差不多该回店里去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '擅自把商品分发给大家，\n',
            '妻子一定会很生气吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但能对大家有点用，\n',
            '我就非常满足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3253')

    def _loc_31B4(): pass

    label('loc_31B4')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '看来烟总算是散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说没有人受伤，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有东西被偷走了，\n',
            '只要再做个一样的不就行了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我也差不多该回店里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3253(): pass

    label('loc_3253')

    Jump('loc_350D')

    def _loc_3256(): pass

    label('loc_3256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_350D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_32A8',
    )

    ChrTalk(
        0x00FE,
        (
            '遇到有困难的人\n',
            '一定要帮助他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们要小心哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_350D')

    def _loc_32A8(): pass

    label('loc_32A8')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '你们没事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是杂货店的埃尔文。\n',
            '一听到有事就赶来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从店里带来很多东西，\n',
            '想要什么就尽管说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种非常时刻，\n',
            '当然不会收你们钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

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
            TXT(0x00, '【替身木偶】\n'),
            TXT(0x01, '【圣灵药】\n'),
            TXT(0x02, '【石化之刃】\n'),
        ),
    )

    MenuEnd(0x0002)

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
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3401',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '替身木偶',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0145, 1)

    Jump('loc_34A9')

    def _loc_3401(): pass

    label('loc_3401')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_345C',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x01FD, 1)

    Jump('loc_34A9')

    def _loc_345C(): pass

    label('loc_345C')

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '石化之刃',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x027F, 1)

    def _loc_34A9(): pass

    label('loc_34A9')

    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '好，这个就给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果遇到有困难的人\n',
            '一定要帮助他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，你们要小心哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_350D(): pass

    label('loc_350D')

    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x3511
@scena.Code('func_2A_3511')
def func_2A_3511():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Return,
        ),
        'loc_35F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3593',
    )

    ChrTalk(
        0x00FE,
        (
            '可是，我不在的时候\n',
            '竟然发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '冈多夫先生外出时让我留守，\n',
            '发生了这样的事，我简直没脸见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EE')

    def _loc_3593(): pass

    label('loc_3593')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '工房被袭击了……\n',
            '竟然会发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之要先回协会，\n',
            '确认一下状况才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35EE(): pass

    label('loc_35EE')

    Jump('loc_39E1')

    def _loc_35F1(): pass

    label('loc_35F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_39E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_366A',
    )

    ChrTalk(
        0x00FE,
        (
            '我不在的时候\n',
            '竟然发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '冈多夫先生外出时让我留守，\n',
            '发生了这样的事，我简直没脸见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39E1')

    def _loc_366A(): pass

    label('loc_366A')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            (Expr.Eval, "OP_29(0x0028, 0x00, 0x04)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3989',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B9, 5, 0x5CD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_392E',
    )

    SetScenaFlags(ScenaFlag(0x00B9, 5, 0x5CD))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊！是你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F啊，是王先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我刚刚\n',
            '才回到蔡斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这到底发生什么事了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#003F嗯，其实啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#050F喂，你在干什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '赶快回协会去吧。\n',
            '我们可没时间再磨蹭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#009F唔唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#007F哼，虽然不甘心，\n',
            '但阿加特说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#018F……有什么不甘心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0012, 400)

    ChrTalk(
        0x0106,
        (
            '#053F还有你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '作为游击士，\n',
            '应该自己去确认当前的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '……确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '我有点自乱阵脚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '算了，既然已经发生了，\n',
            '现在就考虑一下对策吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#050F……喂，走啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38BF')
    def lambda_38BF():
        ChrTurnDirection(0x0102, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_38BF)

    ChrTurnDirection(0x0101, 0x0012, 400)

    ChrTalk(
        0x0101,
        (
            '#000F回头见，王先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊啊，刚刚真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3986')

    def _loc_392E(): pass

    label('loc_392E')

    ChrTalk(
        0x00FE,
        (
            '工房被袭击了……\n',
            '竟然会发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之要先回协会，\n',
            '确认一下状况才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3986(): pass

    label('loc_3986')

    Jump('loc_39E1')

    def _loc_3989(): pass

    label('loc_3989')

    ChrTalk(
        0x00FE,
        (
            '工房被袭击了……\n',
            '竟然会发生这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之要先回协会，\n',
            '确认一下状况才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39E1(): pass

    label('loc_39E1')

    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0x39E5
@scena.Code('func_2B_39E5')
def func_2B_39E5():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    SetScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

# id: 0x002C offset: 0x39FB
@scena.Code('func_2C_39FB')
def func_2C_39FB():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '按了按钮，没有任何反应。\n',
            '导力梯好像不能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002D offset: 0x3A64
@scena.Code('func_2D_3A64')
def func_2D_3A64():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B35',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3ACC',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080727V#012F我担心博士的情况。\n',
            '赶快去工房里面调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B17')

    def _loc_3ACC(): pass

    label('loc_3ACC')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080728V#012F我担心博士的情况。\n',
            '赶快去工房里面调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B17(): pass

    label('loc_3B17')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3DAD')

    def _loc_3B35(): pass

    label('loc_3B35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 3, 0x50B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DAD',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 3, 0x50B))
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetDirection(0x0102, 90, 0)
    ChrSetDirection(0x0101, 90, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070570V#004F这，这是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(6010, 2000, 59020, 0)
    OP_67(0, 2920, -10000, 0)
    CameraSetDistance(3630, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -13400, 8000, 59680, 90)
    ChrSetPos(0x0102, -13620, 8000, 58750, 90)
    OP_0D()

    @scena.Lambda('lambda_3C1D')
    def lambda_3C1D():
        CameraMove(-13820, 9000, 59010, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3C1D)

    Sleep(1000)

    OP_67(0, 11000, -10000, 5000)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    Fade(1000)
    CameraMove(-13480, 8000, 59160, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020070571V#014F好像是……会移动的楼梯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070572V这楼梯看上去好长啊，\n',
            '自己走下去应该会很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070573V#007F话、话是这样说，\n',
            '但是用机械移动也太……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070574V#509F自从到了这个城镇之后，\n',
            '感觉除了惊讶之外就没有其他反应了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070575V#019F我也有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_3DAD(): pass

    label('loc_3DAD')

    Return()

# id: 0x002E offset: 0x3DAE
@scena.Code('func_2E_3DAE')
def func_2E_3DAE():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-35180, 10000, 58970, 0)
    CameraSetDistance(2410, 0)
    OP_6C(270000, 0)
    ChrSetPos(0x0101, -34470, 10000, 59690, 225)
    ChrSetPos(0x0102, -34480, 10000, 58410, 315)
    ChrSetPos(0x0107, -35490, 10000, 59000, 90)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 2, 0x5D2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FFB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071572V#501F亚尔摩村啊～\n',
            '我已经开始有点期待呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071573V那里是个以温泉著名的胜地吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071574V#061F是的。\n',
            '是个非常棒的地方哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071575V之前我跟爷爷\n',
            '去过那里好几次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071576V#010F要去那个村子的话，\n',
            '该怎么走呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071577V#560F我想想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071578V出了城镇的南面出口\n',
            '就是宽广的平原道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071579V沿着托兰特平原道\n',
            '一直向南走就到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071580V#006FＯＫ！\n',
            '沿着平原道一直往南走对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071581V#001F那么，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41A6')

    def _loc_3FFB(): pass

    label('loc_3FFB')

    ChrTalk(
        0x0101,
        (
            '#0010071582V#501F亚尔摩村啊～\n',
            '我已经开始有点期待呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071583V那里是个以温泉著名的胜地吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071584V#061F是的。\n',
            '是个非常棒的地方哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071585V之前我跟爷爷\n',
            '去过那里好几次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071586V#010F的确是个让人期待的地方，\n',
            '那么我们就赶快前往亚尔摩吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071587V是从南面的门口出去对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071588V#560F是呢，出去之后，\n',
            '沿着托兰特平原道向南走就到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071589V#006FＯＫ！\n',
            '那么，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41A6(): pass

    label('loc_41A6')

    OP_28(0x0040, 0x01, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x002F offset: 0x41AF
@scena.Code('func_2F_41AF')
def func_2F_41AF():
    EventBegin(0x00)
    OP_28(0x0041, 0x04, 0x02)
    OP_28(0x0041, 0x04, 0x04)
    OP_28(0x0041, 0x01, 0x0001)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 60)
    OP_4A(0x0021, 0)
    OP_4A(0x0011, 0)
    OP_4A(0x001F, 0)
    CameraMove(-14970, 8000, 55370, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(224000, 0)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x0008, 255)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    FormationDelMember(0x0F, 0xFF)
    ChrSetPos(0x0101, -14050, 8000, 56120, 270)
    ChrSetPos(0x0102, -13280, 8000, 55260, 270)
    ChrSetPos(0x0107, -13040, 8000, 57050, 270)
    ChrSetPos(0x0008, -12520, 8000, 56020, 270)
    ChrSetPos(0x001C, -37650, 10000, 59010, 0)
    ChrSetPos(0x001B, -37650, 10000, 59010, 0)
    ChrSetPos(0x0017, -37650, 10000, 59010, 0)
    ChrSetPos(0x000B, -37650, 10000, 59010, 0)
    ChrSetPos(0x000A, -37650, 10000, 59010, 0)
    ChrSetPos(0x0009, -26520, 8000, 57300, 0)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_42F8')
    def lambda_42F8():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_42F8')

    DispatchAsync2(0x000B, 0x0001, lambda_42F8)

    @scena.Lambda('lambda_4309')
    def lambda_4309():
        ChrWalkTo(0x00FE, -25070, 8000, 58060, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_4309)

    FadeIn(2000, 0)
    OP_20(0x000005DC)
    OP_0D()
    OP_21()
    PlayBGM(81)

    ChrTalk(
        0x0101,
        (
            '#0010080680V#004F啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4355')
    def lambda_4355():
        CameraMove(-25700, 8000, 55810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4355)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0xFF)
    FadeIn(2000, 0)
    OP_12(0x00000000, 0x0003D090, 0x00000000)
    CameraMove(-35690, 20250, 58940, 0)
    OP_67(0, 20360, -10000, 0)
    CameraSetDistance(3390, 0)
    OP_6C(294000, 0)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetFlags(0x0022, 0x0040)
    ChrSetFlags(0x0023, 0x0040)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x0022, 0x0004)
    ChrSetFlags(0x0023, 0x0004)
    ChrSetFlags(0x000A, 0x0080)
    OP_4A(0x0021, 0)
    OP_4A(0x0011, 0)
    OP_4A(0x001F, 0)
    OP_4A(0x001C, 0)
    OP_4A(0x001B, 0)
    OP_4A(0x0017, 0)
    OP_4A(0x000B, 0)
    OP_4A(0x000A, 0)
    OP_4A(0x0024, 0)
    ChrSetPos(0x0011, -37650, 10000, 59010, 0)
    ChrSetPos(0x0022, -37650, 10000, 59010, 0)
    ChrSetPos(0x0023, -37650, 10000, 59010, 0)
    OP_12(0x00000000, 0x00000000, 0x00002710)

    @scena.Lambda('lambda_4484')
    def lambda_4484():
        OP_6C(225000, 11000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_4484)

    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_4499')
    def lambda_4499():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4499')

    DispatchAsync2(0x000B, 0x0001, lambda_4499)

    @scena.Lambda('lambda_44AA')
    def lambda_44AA():
        ChrWalkTo(0x00FE, -25070, 8000, 58060, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_44AA)

    Sleep(500)

    ChrClearFlags(0x0011, 0x0080)

    @scena.Lambda('lambda_44CF')
    def lambda_44CF():
        ChrSetDirection(0x00FE, 166, 0)
        Yield()

        Jump('lambda_44CF')

    DispatchAsync2(0x0011, 0x0001, lambda_44CF)

    @scena.Lambda('lambda_44E0')
    def lambda_44E0():
        ChrWalkTo(0x00FE, -33620, 10000, 61440, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_44E0)

    Sleep(500)

    ChrClearFlags(0x0017, 0x0080)

    @scena.Lambda('lambda_4505')
    def lambda_4505():
        ChrSetDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_4505')

    DispatchAsync2(0x0017, 0x0001, lambda_4505)

    @scena.Lambda('lambda_4516')
    def lambda_4516():
        ChrWalkTo(0x00FE, -29430, 8000, 57220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_4516)

    Sleep(1000)

    ChrClearFlags(0x0022, 0x0080)

    @scena.Lambda('lambda_453B')
    def lambda_453B():
        ChrSetDirection(0x00FE, 296, 0)
        Yield()

        Jump('lambda_453B')

    DispatchAsync2(0x0022, 0x0001, lambda_453B)

    @scena.Lambda('lambda_454C')
    def lambda_454C():
        ChrWalkTo(0x00FE, -32970, 10000, 56310, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0002, lambda_454C)

    @scena.Lambda('lambda_4567')
    def lambda_4567():
        CameraMove(-35440, 14790, 58910, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4567)

    Sleep(1000)

    @scena.Lambda('lambda_4584')
    def lambda_4584():
        OP_67(0, 12040, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4584)

    ChrClearFlags(0x0023, 0x0080)

    @scena.Lambda('lambda_45A1')
    def lambda_45A1():
        ChrSetDirection(0x00FE, 330, 0)
        Yield()

        Jump('lambda_45A1')

    DispatchAsync2(0x0023, 0x0001, lambda_45A1)

    @scena.Lambda('lambda_45B2')
    def lambda_45B2():
        ChrWalkTo(0x00FE, -33170, 10000, 55430, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0002, lambda_45B2)

    Sleep(1000)

    ChrClearFlags(0x001C, 0x0080)

    @scena.Lambda('lambda_45D7')
    def lambda_45D7():
        ChrSetDirection(0x00FE, 0, 0)
        Yield()

        Jump('lambda_45D7')

    DispatchAsync2(0x001C, 0x0001, lambda_45D7)

    @scena.Lambda('lambda_45E8')
    def lambda_45E8():
        ChrWalkTo(0x00FE, -27070, 8000, 59620, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_45E8)

    Sleep(1000)

    ChrClearFlags(0x001B, 0x0080)

    @scena.Lambda('lambda_460D')
    def lambda_460D():
        ChrSetDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_460D')

    DispatchAsync2(0x001B, 0x0001, lambda_460D)

    @scena.Lambda('lambda_461E')
    def lambda_461E():
        ChrWalkTo(0x00FE, -27110, 8000, 60420, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_461E)

    Sleep(2000)

    @scena.Lambda('lambda_463E')
    def lambda_463E():
        CameraMove(-26430, 8000, 57990, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_463E)

    @scena.Lambda('lambda_4656')
    def lambda_4656():
        OP_67(0, 11000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4656)

    @scena.Lambda('lambda_466E')
    def lambda_466E():
        CameraSetDistance(3000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_466E)

    @scena.Lambda('lambda_467E')
    def lambda_467E():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_467E')

    DispatchAsync2(0x0009, 0x0001, lambda_467E)

    Sleep(300)

    ChrClearFlags(0x000A, 0x0080)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x000A, -26910, 8000, 58700, 4000, 0x00)
    Sleep(1000)

    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)

    ChrTalk(
        0x000A,
        (
            '#1960080681V呼呼……\n',
            '还、还以为死定了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080682V#800F没事比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000B, 400)

    ChrTalk(
        0x0009,
        (
            '#0550080683V#804F好，所有人都没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0009, 400)

    ChrTalk(
        0x000B,
        (
            '#1950080684V是、是的，普通员工都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080685V#2P工房长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_47A6')
    def lambda_47A6():
        CameraMove(-25700, 8000, 55810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_47A6)

    @scena.Lambda('lambda_47BE')
    def lambda_47BE():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_47BE')

    DispatchAsync2(0x0009, 0x0001, lambda_47BE)

    @scena.Lambda('lambda_47CF')
    def lambda_47CF():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_47CF')

    DispatchAsync2(0x000B, 0x0001, lambda_47CF)

    @scena.Lambda('lambda_47E0')
    def lambda_47E0():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_47E0')

    DispatchAsync2(0x000A, 0x0001, lambda_47E0)

    @scena.Lambda('lambda_47F1')
    def lambda_47F1():
        ChrWalkTo(0x00FE, -24560, 8000, 56730, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_47F1)

    Sleep(300)

    @scena.Lambda('lambda_4811')
    def lambda_4811():
        ChrWalkTo(0x00FE, -24810, 8000, 55820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4811)

    Sleep(300)

    @scena.Lambda('lambda_4831')
    def lambda_4831():
        ChrWalkTo(0x00FE, -23850, 8000, 57670, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4831)

    Sleep(300)

    @scena.Lambda('lambda_4851')
    def lambda_4851():
        ChrWalkTo(0x00FE, -23250, 8000, 56230, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4851)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0009, 0)

    ChrTalk(
        0x0009,
        (
            '#0550080686V#802F#2P哦哦，是你们……\n',
            '已经从亚尔摩回来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080687V#002F这骚动究竟是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080688V#804F#2P看来是建筑物内部哪里的\n',
            '瓦斯泄漏了出来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080689V从地下到五楼都是烟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080690V#012F难道是火灾吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080691V#803F#2P灭火装置没有运作，\n',
            '所以应该不用担心是火灾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080692V但是，为什么会漏烟，\n',
            '这一点我实在是想不通……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080693V#063F那、那个，工房长叔叔。\n',
            '爷爷他在哪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)

    ChrTalk(
        0x0009,
        (
            '#0550080694V#802F#2P咦，他不是在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000B, 400)

    ChrTalk(
        0x0009,
        (
            '#0550080695V#802F#2P海泽尔。\n',
            '你不是已经确认过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0009, 400)

    ChrTalk(
        0x000B,
        (
            '#1950080696V那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x000B, 0)

    ChrTalk(
        0x000B,
        (
            '#1950080697V普通员工都已经确认过了，\n',
            '不过唯独拉赛尔博士还没……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080698V#065F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080699V#804F#2P你说什么！\n',
            '他还留在里面吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080700V#005F工房长先生！\n',
            '博士的事就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080701V#012F我们进去看看情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 0)

    ChrTalk(
        0x0009,
        (
            '#0550080702V#805F#2P不、不好意思。\n',
            '又要拜托你们俩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080703V#065F我、我也去……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4C3A')
    def lambda_4C3A():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C3A)

    @scena.Lambda('lambda_4C48')
    def lambda_4C48():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4C48)

    @scena.Lambda('lambda_4C56')
    def lambda_4C56():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4C56)

    @scena.Lambda('lambda_4C64')
    def lambda_4C64():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4C64)

    @scena.Lambda('lambda_4C72')
    def lambda_4C72():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4C72)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080704V#004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080705V#802F#2P提妲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080706V#062F我对中央工房里面的环境\n',
            '比较熟悉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080707V所以所以……\n',
            '我可以为艾丝蒂尔姐姐你们带路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080708V#003F#2P提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080709V#002F明白了，一起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080710V#012F#5P不过，一旦有危险的话，\n',
            '你一定要马上离开，知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080711V#063F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080712V#155F那、那个～\n',
            '我也要跟你们一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4E21')
    def lambda_4E21():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4E21)

    @scena.Lambda('lambda_4E2F')
    def lambda_4E2F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4E2F)

    @scena.Lambda('lambda_4E3D')
    def lambda_4E3D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4E3D)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080713V#002F#2P不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080714V#015F#5P对不起。\n',
            '你还是留在这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080715V#154F唔～好果断的回答啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080716V不过没办法了。\n',
            '你们三个要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080717V#800F#2P假如博士在里面的话，\n',
            '你们上三楼的工作室就应该能找到他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080718V先去那里确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4F74')
    def lambda_4F74():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4F74)

    @scena.Lambda('lambda_4F82')
    def lambda_4F82():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4F82)

    @scena.Lambda('lambda_4F90')
    def lambda_4F90():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4F90)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010080719V#006F嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080720V#012F那么我们去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0021, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x001F, 0x01)
    TerminateThread(0x001C, 0x01)
    TerminateThread(0x001B, 0x01)
    TerminateThread(0x0017, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0024, 0x01)
    OP_4B(0x0021, 0)
    OP_4B(0x0011, 0)
    OP_4B(0x001F, 0)
    OP_4B(0x001C, 0)
    OP_4B(0x001B, 0)
    OP_4B(0x0017, 0)
    OP_4B(0x000B, 0)
    OP_4B(0x000A, 0)
    OP_4B(0x0024, 0)
    ChrClearFlags(0x001C, 0x0040)
    ChrClearFlags(0x001B, 0x0040)
    ChrClearFlags(0x0017, 0x0040)
    ChrClearFlags(0x000B, 0x0040)
    ChrClearFlags(0x0011, 0x0040)
    ChrClearFlags(0x0022, 0x0040)
    ChrClearFlags(0x0023, 0x0040)
    ChrClearFlags(0x0011, 0x0004)
    ChrClearFlags(0x0022, 0x0004)
    ChrClearFlags(0x0023, 0x0004)
    OP_4B(0x000A, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000B, 255)
    OP_4B(0x0008, 255)
    CreateThread(0x0009, 0x00, 0x00, func_03_10F6)
    CreateThread(0x000A, 0x00, 0x00, func_03_10F6)
    CreateThread(0x000B, 0x00, 0x00, func_03_10F6)
    ChrSetDirection(0x0008, 270, 0)
    MapSetFlags(0x02000000)
    MapSetFlags(0x00000800)
    SetScenaFlags(ScenaFlag(0x00A5, 4, 0x52C))
    EventEnd(0x00)

    Return()

# id: 0x0030 offset: 0x5099
@scena.Code('func_30_5099')
def func_30_5099():
    EventBegin(0x00)
    CameraMove(-35220, 10000, 59310, 0)
    OP_4A(0x0021, 0)
    OP_4A(0x0011, 0)
    OP_4A(0x001F, 0)
    OP_4A(0x0021, 0)
    OP_4A(0x0011, 0)
    OP_4A(0x001F, 0)
    OP_4A(0x001C, 0)
    OP_4A(0x001B, 0)
    OP_4A(0x0017, 0)
    OP_4A(0x000B, 0)
    OP_4A(0x000A, 0)
    OP_4A(0x0024, 0)
    ChrSetPos(0x001C, -26070, 8000, 62840, 63)
    ChrSetPos(0x001B, -25060, 8000, 63650, 180)
    ChrSetPos(0x0024, -24740, 8000, 62540, 3)
    ChrSetPos(0x000B, -37650, 10000, 59010, 0)
    ChrSetPos(0x000A, -28440, 8000, 62590, 129)
    ChrSetPos(0x0009, -26520, 8000, 57300, 0)
    ChrSetPos(0x0101, -34600, 10000, 59260, 90)
    ChrSetPos(0x0106, -35290, 10000, 58430, 90)
    ChrSetPos(0x0102, -35240, 10000, 60170, 90)
    ChrSetPos(0x0107, -35880, 10000, 59390, 90)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -26240, 8000, 58320, 270)
    ChrSetPos(0x0008, -27270, 8000, 58010, 270)
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)

    @scena.Lambda('lambda_51C0')
    def lambda_51C0():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_51C0')

    DispatchAsync2(0x0008, 0x0001, lambda_51C0)

    @scena.Lambda('lambda_51D1')
    def lambda_51D1():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_51D1')

    DispatchAsync2(0x0009, 0x0001, lambda_51D1)

    @scena.Lambda('lambda_51E2')
    def lambda_51E2():
        ChrWalkTo(0x00FE, -28110, 8000, 59050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_51E2)

    @scena.Lambda('lambda_51FD')
    def lambda_51FD():
        ChrWalkTo(0x00FE, -27560, 8000, 59930, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_51FD)

    @scena.Lambda('lambda_5218')
    def lambda_5218():
        ChrWalkTo(0x00FE, -26780, 8000, 60730, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5218)

    @scena.Lambda('lambda_5233')
    def lambda_5233():
        ChrWalkTo(0x00FE, -28880, 8000, 60550, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_5233)

    @scena.Lambda('lambda_524E')
    def lambda_524E():
        CameraMove(-27780, 8000, 59800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_524E)

    @scena.Lambda('lambda_5266')
    def lambda_5266():
        CameraSetDistance(2700, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5266)

    FadeIn(1000, 0)

    @scena.Lambda('lambda_527F')
    def lambda_527F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_527F')

    DispatchAsync2(0x0106, 0x0001, lambda_527F)

    @scena.Lambda('lambda_5290')
    def lambda_5290():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_5290')

    DispatchAsync2(0x0101, 0x0001, lambda_5290)

    @scena.Lambda('lambda_52A1')
    def lambda_52A1():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_52A1')

    DispatchAsync2(0x0102, 0x0001, lambda_52A1)

    @scena.Lambda('lambda_52B2')
    def lambda_52B2():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_52B2')

    DispatchAsync2(0x0107, 0x0001, lambda_52B2)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0280080941V#151F啊，小艾你们出来了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080942V#801F哦哦，你们没事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080943V刚才军队的人从里面走出来，\n',
            '我还在想出什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080944V#055F#1P军队的人……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080945V#005F等、等一下！\n',
            '不是穿黑衣服的家伙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080946V#802F你说什么呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080947V是身着蓝白色军装、\n',
            '礼仪端正的王国军军人啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080948V听说他们是从\n',
            '艾尔·雷登关所派来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280080949V#151F从那军装来看，\n',
            '他们的确是女王陛下的亲卫队呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080950V他们样子好帅哦～\n',
            '我毫不犹豫地拍了照片呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080951V#004F亲卫队……的人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080952V#012F就是在卢安\n',
            '把市长逮捕的那些军人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080953V但是，他们怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080954V#062F那、那个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080955V工房长叔叔，\n',
            '那些人没带着爷爷吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080956V#805F带、带着拉赛尔博士！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550080957V没、没有……\n',
            '可是他们带着很大包的货物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080958V#065F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080959V#005F没错，就是他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080960V#057F#1P那些杂碎……\n',
            '在导力梯里换成军服吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080961V#056F哼，太瞧不起人了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080962V#802F等、等一下！\n',
            '这到底是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080963V#016F详细情况我们之后会向您汇报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080964V请问工房长先生，\n',
            '那些军人往哪个方向去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550080965V#805F说、说是有急事，\n',
            '往城镇市街区方向去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080966V#054F#1P快追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0106, 0x0040)

    @scena.Lambda('lambda_57BB')
    def lambda_57BB():
        ChrWalkTo(0x00FE, -13190, 8000, 60190, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_57BB)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010080967V#005F决不能让他们逃走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5804')
    def lambda_5804():
        ChrWalkTo(0x00FE, -13190, 8000, 60190, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5804)

    Sleep(400)

    @scena.Lambda('lambda_5824')
    def lambda_5824():
        ChrWalkTo(0x00FE, -13190, 8000, 60190, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5824)

    Sleep(100)

    @scena.Lambda('lambda_5844')
    def lambda_5844():
        ChrWalkTo(0x00FE, -13190, 8000, 60190, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5844)

    Sleep(2000)

    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_25(0x00A0, -4620, 5320, 59280, 10000, 30000, 0x01, 0x00000000)
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '虽然艾丝蒂尔他们\n',
            '分头在蔡斯市的市街区寻找犯人的踪迹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '但即使是挨家挨户地寻找，\n',
            '仍然没能找到博士和绑架博士的黑衣人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '不久，位于湖畔上的雷斯顿要塞接到通报，\n',
            '派出了王国军的部队前来中央工房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    MapClearFlags(0x40000000)
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x00A6, 6, 0x536))
    OP_28(0x0041, 0x01, 0x0040)
    MapClearFlags(0x00000800)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3115._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0031 offset: 0x598F
@scena.Code('func_31_598F')
def func_31_598F():
    EventBegin(0x00)
    CameraMove(-36480, 10000, 59730, 0)
    OP_67(0, 7190, -10000, 0)
    CameraSetDistance(3350, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0011, 0xFF)
    ChrSetPos(0x0011, -23800, 10000, 46930, 180)
    CreateThread(0x0011, 0x00, 0x00, func_03_10F6)
    FormationDelMember(0x0F, 0xFF)
    ChrSetPos(0x0101, -34420, 10000, 58850, 270)
    ChrSetPos(0x0107, -34550, 10000, 57970, 315)
    ChrSetPos(0x0106, -33590, 10000, 59410, 270)
    ChrSetPos(0x0102, -34780, 10000, 59820, 225)
    ChrSetFlags(0x0008, 0x0040)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -36000, 10000, 58980, 90)
    OP_4A(0x0008, 255)
    OP_6F(0x0000, 60)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0280081029V#153F#1P啊，对了～\n',
            '还得去买感光结晶回路才行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280081030V#150F那我先告辞啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081031V#501F啊，嗯。\n',
            '朵洛希也辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280081032V#154F#1P没有啦。\n',
            '我可是一点忙也没帮上呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280081033V我也会去问问编辑部，\n',
            '调查看看有没有什么情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0280081034V#150F#1P所以……\n',
            '小提，打起精神来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081035V#560F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081036V好的……\n',
            '谢谢……朵洛希姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280081037V#150F#1P不用担心啦～\n',
            '小艾和小约还有红头发大哥\n',
            '一定会平安无事地救出你爷爷的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280081038V#151F那么，再见啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)

    @scena.Lambda('lambda_5C7B')
    def lambda_5C7B():
        CameraMove(-35480, 10000, 59730, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_5C7B)

    ChrWalkTo(0x0008, -37630, 10000, 58990, 3000, 0x00)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    ChrSetFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070081039V#063F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5CEA')
    def lambda_5CEA():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_5CEA)

    @scena.Lambda('lambda_5CF8')
    def lambda_5CF8():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5CF8)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081040V#006F#5P提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081041V#006F打起精神来吧，\n',
            '博士他一定会没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081042V#010F#2P是啊，他们应该不会\n',
            '伤害王国第一的天才学者的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081043V#063F艾丝蒂尔姐姐、约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081044V#067F嗯……是呢。\n',
            '爷爷一定会没事的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081045V#552F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081046V#004F#5P怎么啦，又板着一张严肃脸？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5E9C')
    def lambda_5E9C():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5E9C)

    @scena.Lambda('lambda_5EAA')
    def lambda_5EAA():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5EAA)

    ChrTalk(
        0x0106,
        (
            '#0050081047V#053F……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081048V#050F时间紧迫，\n',
            '我们快点去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0041, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0032 offset: 0x5F0E
@scena.Code('func_32_5F0E')
def func_32_5F0E():
    EventBegin(0x00)
    CameraMove(-22950, 8000, 63790, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0102, -22960, 8000, 73260, 0)
    ChrSetPos(0x0101, -21990, 8000, 74030, 0)
    ChrSetPos(0x0107, -23770, 8000, 73860, 0)

    @scena.Lambda('lambda_5F86')
    def lambda_5F86():
        ChrWalkTo(0x00FE, -22970, 8000, 62960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5F86)

    Sleep(300)

    @scena.Lambda('lambda_5FA6')
    def lambda_5FA6():
        ChrWalkTo(0x00FE, -22220, 8000, 63930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5FA6)

    Sleep(300)

    @scena.Lambda('lambda_5FC6')
    def lambda_5FC6():
        ChrWalkTo(0x00FE, -23360, 8000, 64190, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5FC6)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0107, 0x0001)
    ChrSetDirection(0x0107, 135, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090020V#010F接下来，\n',
            '我们先去游击士协会一趟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090021V说不定雾香小姐已经问到\n',
            '有关黑衣人那艘飞艇的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090022V#006F嗯，如果能从王国军那里\n',
            '得到什么情报就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090023V#004F啊，提妲也一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090024V#560F那、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090025V不好意思呢。\n',
            '我想去照看阿加特大哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090026V他还没醒过来，\n',
            '我有点放心不下呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090027V#501F提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090028V#001F明白了。\n',
            '博士的事就交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090029V#063F对不起……\n',
            '我老是给姐姐你们添麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090030V#506F你这孩子真是的～\n',
            '又在跟我们客气起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090031V#010F虽然阿加特兄现在还没醒来，\n',
            '不过只要有朋友陪在旁边，\n',
            '自己休息的时候也会安心许多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090032V阿加特兄就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090033V#560F嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_62F2')
    def lambda_62F2():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_62F2')

    DispatchAsync2(0x0101, 0x0001, lambda_62F2)

    @scena.Lambda('lambda_6303')
    def lambda_6303():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_6303')

    DispatchAsync2(0x0102, 0x0001, lambda_6303)

    ChrSetDirection(0x0107, 225, 400)

    @scena.Lambda('lambda_631B')
    def lambda_631B():
        OP_6C(270000, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_631B)

    @scena.Lambda('lambda_632B')
    def lambda_632B():
        CameraMove(-22510, 8000, 63590, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_632B)

    ChrWalkTo(0x0107, -28380, 8000, 60860, 5000, 0x00)
    ChrWalkTo(0x0107, -35060, 10000, 59740, 5000, 0x00)
    ChrSetFlags(0x0107, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010090034V#006F啊啊～\n',
            '提妲这孩子真是又坚强又可爱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090035V对那个爱闹别扭的刀子嘴\n',
            '根本用不着那么温柔嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090036V#010F好了好了，别吃醋了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090037V说起来，\n',
            '你和阿加特兄性格倒挺相似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090038V#004F啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090039V#009F真、真讨厌～\n',
            '我和那家伙哪里相似了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090040V#019F行事比较冲动啦，\n',
            '又爱做老好人啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090041V#010F阿加特兄虽然说话刻薄了点，\n',
            '但却很会为对方着想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090042V这一点，\n',
            '我想提妲也应该很清楚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090043V#509F唔唔……\n',
            '虽然有点难以理解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090044V#007F不说这个了，\n',
            '总之先去协会问问看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090045V希望在那刀子嘴伤势康复之前，\n',
            '能够查到什么线索，然后做点成绩给他看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090046V#019F哈哈，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0107, -22820, 8000, 62610, 0)
    EventEnd(0x00)
    FormationDelMember(0x06, 0xFF)

    Return()

# id: 0x0033 offset: 0x6660
@scena.Code('func_33_6660')
def func_33_6660():
    MapClearFlags(0x02000000)
    EventBegin(0x00)
    CameraMove(-23500, 8000, 69230, 0)
    OP_67(0, 8490, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(306000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -24660, 8000, 82550, 0)
    ChrSetPos(0x0102, -22920, 8000, 83030, 0)

    @scena.Lambda('lambda_66CC')
    def lambda_66CC():
        ChrWalkTo(0x00FE, -24250, 8000, 69160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_66CC)

    Sleep(500)

    @scena.Lambda('lambda_66EC')
    def lambda_66EC():
        ChrWalkTo(0x00FE, -22580, 8000, 70110, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_66EC)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100301V#007F哈啊～吓了我一跳呢。',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100302V#012F再磨磨蹭蹭的话，\n',
            '情报部那些人就要过来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100303V我们直接出城吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100304V#002F嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100305V唔……去王都的话，\n',
            '应该从东边的街道走吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100306V#012F没错，沿着利塔街道往北走，\n',
            '到达『圣海姆门』就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100307V穿过大门，\n',
            '就进入王都格兰赛尔地区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0054, 0x01, 0x0010)
    OP_20(0x000005DC)
    Sleep(500)

    EventEnd(0x00)
    PlayBGM(13)

    Return()

# id: 0x0034 offset: 0x6899
@scena.Code('func_34_6899')
def func_34_6899():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Return,
        ),
        'loc_6987',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_690F',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090545V#012F我们最好不要靠近飞艇坪了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090546V还是赶快出城去吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6969')

    def _loc_690F(): pass

    label('loc_690F')

    ChrTalk(
        0x0101,
        (
            '#0010090547V#002F……情报部的人要从飞艇坪过来了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090548V还是不要靠近为好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6969(): pass

    label('loc_6969')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_6A7F')

    def _loc_6987(): pass

    label('loc_6987')

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x035E)"),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_69B8',
    )

    Call(0, 0x0035)

    Jump('loc_6A7F')

    def _loc_69B8(): pass

    label('loc_69B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A7F',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A19',
    )

    ChrTalk(
        0x0102,
        (
            '#0020090549V#012F我担心博士的情况。\n',
            '赶快去工房里面调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A64')

    def _loc_6A19(): pass

    label('loc_6A19')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090550V#012F我担心博士的情况。\n',
            '赶快去工房里面调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A64(): pass

    label('loc_6A64')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6A7F(): pass

    label('loc_6A7F')

    Return()

# id: 0x0035 offset: 0x6A80
@scena.Code('func_35_6A80')
def func_35_6A80():
    EventBegin(0x01)

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6AB7',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x035E)"),
            Expr.Return,
        ),
        'loc_6AB1',
    )

    SetScenaFlags(ScenaFlag(0x0003, 4, 0x1C))

    Jump('loc_6AB4')

    def _loc_6AB1(): pass

    label('loc_6AB1')

    SetScenaFlags(ScenaFlag(0x0003, 2, 0x1A))

    def _loc_6AB4(): pass

    label('loc_6AB4')

    Jump('loc_6AE9')

    def _loc_6AB7(): pass

    label('loc_6AB7')

    If(
        (
            (Expr.Eval, "OP_40(0x035E)"),
            Expr.Return,
        ),
        'loc_6AE9',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0343)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0344)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0345)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6AE6',
    )

    SetScenaFlags(ScenaFlag(0x0003, 4, 0x1C))

    Jump('loc_6AE9')

    def _loc_6AE6(): pass

    label('loc_6AE6')

    SetScenaFlags(ScenaFlag(0x0003, 3, 0x1B))

    def _loc_6AE9(): pass

    label('loc_6AE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Return,
        ),
        'loc_6D14',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6B7D',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180420V#017F我说，艾丝蒂尔。\n',
            '还是先把资料室的书还回去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180421V#008F啊，对、对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C45')

    def _loc_6B7D(): pass

    label('loc_6B7D')

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180422V#010F艾丝蒂尔，\n',
            '说起来我们还没有把资料室的书还回去呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180423V在办理搭乘手续之前\n',
            '赶快去一趟中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180424V#000F啊，对了。\n',
            '要赶快去一趟中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C45(): pass

    label('loc_6C45')

    Jump('loc_6D11')

    def _loc_6C48(): pass

    label('loc_6C48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6C90',
    )

    ChrTalk(
        0x0102,
        (
            '#0020180425V#010F在办理搭乘手续之前\n',
            '先要把书还给资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D11')

    def _loc_6C90(): pass

    label('loc_6C90')

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180426V#010F说起来，\n',
            '我们还没有把资料室的书还回去呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180423V在办理搭乘手续之前\n',
            '赶快去一趟中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D11(): pass

    label('loc_6D11')

    Jump('loc_721C')

    def _loc_6D14(): pass

    label('loc_6D14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 3, 0x1B)),
            Expr.Return,
        ),
        'loc_6F0B',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E4F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6DA9',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180412V#010F我说，艾丝蒂尔。\n',
            '要先去地下工场\n',
            '把信交给菲小姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180413V#000F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E4C')

    def _loc_6DA9(): pass

    label('loc_6DA9')

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180414V#010F艾丝蒂尔，\n',
            '我们最好先去把信送给菲小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180415V在办理搭乘手续之前\n',
            '去一趟地下工场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180416V#004F哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E4C(): pass

    label('loc_6E4C')

    Jump('loc_6F08')

    def _loc_6E4F(): pass

    label('loc_6E4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6E8F',
    )

    ChrTalk(
        0x0102,
        (
            '#0020180417V#010F我们要先去把信交给菲小姐啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F08')

    def _loc_6E8F(): pass

    label('loc_6E8F')

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180418V#010F说起来，\n',
            '还没有还没把信送给菲小姐呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180419V在办理搭乘手续之前\n',
            '赶快去地下工场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F08(): pass

    label('loc_6F08')

    Jump('loc_721C')

    def _loc_6F0B(): pass

    label('loc_6F0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 4, 0x1C)),
            Expr.Return,
        ),
        'loc_721C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6FDB',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180438V#010F我说，艾丝蒂尔。\n',
            '书和信都还没送到呢，\n',
            '赶快去一趟中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180439V#000F对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180440V是二楼的资料室\n',
            '和地下工场的菲小姐对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70DE')

    def _loc_6FDB(): pass

    label('loc_6FDB')

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180428V#010F说起来，\n',
            '我们还没有把书还回资料室……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180429V而且还得把信送给菲小姐。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180423V在办理搭乘手续之前\n',
            '赶快去一趟中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180431V#000F啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180432V菲小姐在地下工场，\n',
            '而资料室在二楼对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70DE(): pass

    label('loc_70DE')

    Jump('loc_721C')

    def _loc_70E1(): pass

    label('loc_70E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_7170',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180433V#010F我们还没有把书还回资料室，\n',
            '而且信也没有送到。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180434V要赶快去一趟\n',
            '中央工房的资料室和地下工场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_721C')

    def _loc_7170(): pass

    label('loc_7170')

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180435V#014F说起来，\n',
            '我们还没有把书还回资料室……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180436V而且还得把信送给菲小姐。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180437V在办理搭乘手续之前\n',
            '赶快去中央工房把它们送到吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_721C(): pass

    label('loc_721C')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0036 offset: 0x7238
@scena.Code('func_36_7238')
def func_36_7238():
    OP_13(0x0085)

    Return()

# id: 0x0037 offset: 0x723C
@scena.Code('func_37_723C')
def func_37_723C():
    OP_13(0x0081)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
