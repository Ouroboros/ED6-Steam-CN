import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3104   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3104.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
            dword_00        = 0xFFFF8300,
            dword_04        = 0x00002710,
            dword_08        = 0x0000E290,
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
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
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
            talkScenaIndex      = 0x0023,
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
            talkScenaIndex      = 0x0024,
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
            talkScenaIndex      = 0x0025,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
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
            talkScenaIndex      = 0x0027,
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
            talkScenaIndex      = 0x0028,
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
            talkScenaIndex      = 0x0029,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
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
            talkScenaIndex      = 0x001D,
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
            talkScenaIndex      = 0x001E,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
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
            talkScenaIndex      = 0x0015,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
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
            name                = '蔡斯飞艇坪方向',
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
            name                = '蔡斯市街区方向',
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
            x           = -35690,
            y           = 9750,
            z           = 58940,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002A,
        ),
        ScenaEventData(
            x           = -23010,
            y           = 7750,
            z           = 74850,
            range       = 1500,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = -50430,
            y           = 24000,
            z           = 53980,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000002C,
        ),
    )

# id: 0x10004 offset: 0x642
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x642
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_69A',
    )

    ChrSetPos(0x000D, -14600, 8000, 63040, 6)
    ChrSetPos(0x0010, -15440, 8000, 63040, 3)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_BE7')

    def _loc_69A(): pass

    label('loc_69A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_734',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -15510, 8000, 54720, 275)
    ChrSetPos(0x000D, -16920, 8000, 54780, 91)
    ChrSetPos(0x0010, -16950, 8000, 55940, 148)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -15680, 8000, 55990, 243)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -30230, 10000, 47900, 298)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_BE7')

    def _loc_734(): pass

    label('loc_734')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_76A',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_BE7')

    def _loc_76A(): pass

    label('loc_76A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_7A0',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -25190, 8000, 66790, 275)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -17150, 8000, 63800, 358)

    Jump('loc_BE7')

    def _loc_7A0(): pass

    label('loc_7A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_879',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -34110, 10000, 62990, 166)
    CreateThread(0x0011, 0x00, 0x00, func_04_DF3)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -23170, 8000, 59080, 91)
    CreateThread(0x0012, 0x00, 0x00, func_05_E17)
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
    CreateThread(0x001A, 0x00, 0x00, func_06_E3B)

    Jump('loc_BE7')

    def _loc_879(): pass

    label('loc_879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_A7B',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -30660, 9000, 60810, 69)
    CreateThread(0x000A, 0x00, 0x00, func_03_C76)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0025, -24500, 8750, 51360, 18)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -34110, 10000, 62990, 166)
    CreateThread(0x0011, 0x00, 0x00, func_04_DF3)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -23610, 8000, 70240, 5)
    CreateThread(0x001A, 0x00, 0x00, func_06_E3B)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -27110, 8000, 60420, 69)
    ChrSetFlags(0x001B, 0x0010)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, -27070, 8000, 59620, 359)
    ChrSetFlags(0x001C, 0x0010)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -33870, 10000, 57010, 292)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -30810, 10000, 48800, 320)
    CreateThread(0x001D, 0x00, 0x00, func_07_E5F)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32630, 10000, 58920, 255)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, -26600, 8000, 55790, 279)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, -23180, 8000, 58380, 82)
    CreateThread(0x001F, 0x00, 0x00, func_08_E83)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, -29430, 8000, 57220, 85)
    ChrSetFlags(0x0017, 0x0010)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x0021, -22660, 8000, 61960, 82)
    CreateThread(0x0021, 0x00, 0x00, func_0A_ECB)
    ChrClearFlags(0x0022, 0x0080)
    ChrSetPos(0x0022, -33530, 10000, 52430, 296)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0023, -33770, 10000, 51140, 330)
    ChrClearFlags(0x0024, 0x0080)
    ChrSetPos(0x0024, -25860, 8000, 60310, 263)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0026, -21670, 8000, 66490, 242)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0020, -23200, 10000, 47850, 272)
    CreateThread(0x0020, 0x00, 0x00, func_09_EA7)

    Jump('loc_BE7')

    def _loc_A7B(): pass

    label('loc_A7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_ACE',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x001A, -23610, 8000, 70240, 5)
    CreateThread(0x001A, 0x00, 0x00, func_06_E3B)

    Jump('loc_BE7')

    def _loc_ACE(): pass

    label('loc_ACE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_B04',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_BE7')

    def _loc_B04(): pass

    label('loc_B04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_B3A',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_BE7')

    def _loc_B3A(): pass

    label('loc_B3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_B92',
    )

    ChrSetPos(0x000D, -14600, 8000, 63040, 6)
    ChrSetPos(0x0010, -15440, 8000, 63040, 3)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    Jump('loc_BE7')

    def _loc_B92(): pass

    label('loc_B92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_BE7',
    )

    ChrSetPos(0x000D, -14600, 8000, 63040, 6)
    ChrSetPos(0x0010, -15440, 8000, 63040, 3)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0018, -26340, 8000, 65489, 74)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0019, -18800, 8000, 64430, 164)

    def _loc_BE7(): pass

    label('loc_BE7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_BF3'),
        (-1, 'loc_BFB'),
    )

    def _loc_BF3(): pass

    label('loc_BF3')

    PlaySE(14, 0x00, 0x64)

    Jump('loc_BFB')

    def _loc_BFB(): pass

    label('loc_BFB')

    Return()

# id: 0x0001 offset: 0xBFC
@scena.Code('func_01_BFC')
def func_01_BFC():
    OP_16(0x02, 4000, -151000, -69000, 196690)
    OP_6F(0x0005, 40)
    OP_70(0x0005, 0)
    OP_25(0x00A0, -4620, 5320, 59280, 10000, 40000, 0x64, 0x00000000)
    CreateThread(0x0027, 0x00, 0x00, func_02_C40)

    Return()

# id: 0x0002 offset: 0xC40
@scena.Code('func_02_C40')
def func_02_C40():
    OP_72(0x0005, 0x0020)
    OP_72(0x0004, 0x0020)
    def _loc_C4A(): pass

    label('loc_C4A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C75',
    )

    OP_6F(0x0005, 40)
    OP_70(0x0005, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 40)
    OP_73(0x0005)

    Jump('loc_C4A')

    def _loc_C75(): pass

    label('loc_C75')

    Return()

# id: 0x0003 offset: 0xC76
@scena.Code('func_03_C76')
def func_03_C76():
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
        'loc_C9B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_DDD')

    def _loc_C9B(): pass

    label('loc_C9B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB4',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_DDD')

    def _loc_CB4(): pass

    label('loc_CB4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CCD',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_DDD')

    def _loc_CCD(): pass

    label('loc_CCD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE6',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_DDD')

    def _loc_CE6(): pass

    label('loc_CE6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CFF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_DDD')

    def _loc_CFF(): pass

    label('loc_CFF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D18',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_DDD')

    def _loc_D18(): pass

    label('loc_D18')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D31',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_DDD')

    def _loc_D31(): pass

    label('loc_D31')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D4A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_DDD')

    def _loc_D4A(): pass

    label('loc_D4A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D63',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_DDD')

    def _loc_D63(): pass

    label('loc_D63')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D7C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_DDD')

    def _loc_D7C(): pass

    label('loc_D7C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D95',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_DDD')

    def _loc_D95(): pass

    label('loc_D95')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DAE',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_DDD')

    def _loc_DAE(): pass

    label('loc_DAE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DC7',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_DDD')

    def _loc_DC7(): pass

    label('loc_DC7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DDD',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_DDD(): pass

    label('loc_DDD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DF2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_DDD')

    def _loc_DF2(): pass

    label('loc_DF2')

    Return()

# id: 0x0004 offset: 0xDF3
@scena.Code('func_04_DF3')
def func_04_DF3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E16',
    )

    OP_8D(0x00FE, -35270, 61360, -33040, 64150, 3000)

    Jump('func_04_DF3')

    def _loc_E16(): pass

    label('loc_E16')

    Return()

# id: 0x0005 offset: 0xE17
@scena.Code('func_05_E17')
def func_05_E17():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E3A',
    )

    OP_8D(0x00FE, -26390, 55950, -19770, 61950, 3000)

    Jump('func_05_E17')

    def _loc_E3A(): pass

    label('loc_E3A')

    Return()

# id: 0x0006 offset: 0xE3B
@scena.Code('func_06_E3B')
def func_06_E3B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E5E',
    )

    OP_8D(0x00FE, -25190, 68440, -20920, 71850, 3000)

    Jump('func_06_E3B')

    def _loc_E5E(): pass

    label('loc_E5E')

    Return()

# id: 0x0007 offset: 0xE5F
@scena.Code('func_07_E5F')
def func_07_E5F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E82',
    )

    OP_8D(0x00FE, -32689, 46510, -30620, 50700, 3000)

    Jump('func_07_E5F')

    def _loc_E82(): pass

    label('loc_E82')

    Return()

# id: 0x0008 offset: 0xE83
@scena.Code('func_08_E83')
def func_08_E83():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EA6',
    )

    OP_8D(0x00FE, -25190, 54660, -20780, 60740, 3000)

    Jump('func_08_E83')

    def _loc_EA6(): pass

    label('loc_EA6')

    Return()

# id: 0x0009 offset: 0xEA7
@scena.Code('func_09_EA7')
def func_09_EA7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_ECA',
    )

    OP_8D(0x00FE, -26510, 46520, -19100, 49060, 3000)

    Jump('func_09_EA7')

    def _loc_ECA(): pass

    label('loc_ECA')

    Return()

# id: 0x000A offset: 0xECB
@scena.Code('func_0A_ECB')
def func_0A_ECB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EEE',
    )

    OP_8D(0x00FE, -23960, 59250, -21170, 66410, 3000)

    Jump('func_0A_ECB')

    def _loc_EEE(): pass

    label('loc_EEE')

    Return()

# id: 0x000B offset: 0xEEF
@scena.Code('func_0B_EEF')
def func_0B_EEF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_F53',
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

    def _loc_F53(): pass

    label('loc_F53')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0xF57
@scena.Code('func_0C_F57')
def func_0C_F57():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_FA9',
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

    def _loc_FA9(): pass

    label('loc_FA9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0xFAD
@scena.Code('func_0D_FAD')
def func_0D_FAD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_FFF',
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

    def _loc_FFF(): pass

    label('loc_FFF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1003
@scena.Code('func_0E_1003')
def func_0E_1003():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1044',
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

    def _loc_1044(): pass

    label('loc_1044')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1048
@scena.Code('func_0F_1048')
def func_0F_1048():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1096',
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

    def _loc_1096(): pass

    label('loc_1096')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x109A
@scena.Code('func_10_109A')
def func_10_109A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_112F',
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

    def _loc_112F(): pass

    label('loc_112F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1133
@scena.Code('func_11_1133')
def func_11_1133():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_119E',
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

    def _loc_119E(): pass

    label('loc_119E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x11A2
@scena.Code('func_12_11A2')
def func_12_11A2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1266',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_120E',
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

    Jump('loc_1263')

    def _loc_120E(): pass

    label('loc_120E')

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

    def _loc_1263(): pass

    label('loc_1263')

    Jump('loc_12A2')

    def _loc_1266(): pass

    label('loc_1266')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_12A2',
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

    def _loc_12A2(): pass

    label('loc_12A2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x12A6
@scena.Code('func_13_12A6')
def func_13_12A6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_132D',
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

    def _loc_132D(): pass

    label('loc_132D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x1331
@scena.Code('func_14_1331')
def func_14_1331():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1350',
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

    def _loc_1350(): pass

    label('loc_1350')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x1354
@scena.Code('func_15_1354')
def func_15_1354():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_139D',
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

    def _loc_139D(): pass

    label('loc_139D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x13A1
@scena.Code('func_16_13A1')
def func_16_13A1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1418',
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

    def _loc_1418(): pass

    label('loc_1418')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x141C
@scena.Code('func_17_141C')
def func_17_141C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1483',
    )

    ChrTalk(
        0x0110,
        (
            '#0281080003V#150F我也想一起去呀。\n',
            '但没办法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080726V小艾你们千万要小心呀。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1483(): pass

    label('loc_1483')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x1487
@scena.Code('func_18_1487')
def func_18_1487():
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

    def _loc_14D0(): pass

    label('loc_14D0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x14D4
@scena.Code('func_19_14D4')
def func_19_14D4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_153E',
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

    def _loc_153E(): pass

    label('loc_153E')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x1542
@scena.Code('func_1A_1542')
def func_1A_1542():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1562',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁迪，你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1562(): pass

    label('loc_1562')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x1566
@scena.Code('func_1B_1566')
def func_1B_1566():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_15C4',
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

    def _loc_15C4(): pass

    label('loc_15C4')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x15C8
@scena.Code('func_1C_15C8')
def func_1C_15C8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_169A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_1641',
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

    Jump('loc_1697')

    def _loc_1641(): pass

    label('loc_1641')

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

    def _loc_1697(): pass

    label('loc_1697')

    Jump('loc_1748')

    def _loc_169A(): pass

    label('loc_169A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_16DD',
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

    Jump('loc_1748')

    def _loc_16DD(): pass

    label('loc_16DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1748',
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

    def _loc_1748(): pass

    label('loc_1748')

    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x174C
@scena.Code('func_1D_174C')
def func_1D_174C():
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
        'loc_17AA',
    )

    OP_0D()
    OP_A9(0x4D)
    OP_56(0x00)
    TalkEnd(0x0018)

    Return()

    def _loc_17AA(): pass

    label('loc_17AA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17BB',
    )

    TalkEnd(0x0018)

    Return()

    def _loc_17BB(): pass

    label('loc_17BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_1815',
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

    Jump('loc_1E14')

    def _loc_1815(): pass

    label('loc_1815')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_189A',
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

    Jump('loc_1E14')

    def _loc_189A(): pass

    label('loc_189A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1928',
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

    Jump('loc_1E14')

    def _loc_1928(): pass

    label('loc_1928')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_196B',
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

    Jump('loc_1E14')

    def _loc_196B(): pass

    label('loc_196B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_19E1',
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

    Jump('loc_1E14')

    def _loc_19E1(): pass

    label('loc_19E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1AB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1A57',
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

    Jump('loc_1AAE')

    def _loc_1A57(): pass

    label('loc_1A57')

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

    def _loc_1AAE(): pass

    label('loc_1AAE')

    Jump('loc_1E14')

    def _loc_1AB1(): pass

    label('loc_1AB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1B14',
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

    Jump('loc_1E14')

    def _loc_1B14(): pass

    label('loc_1B14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1C09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1B96',
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

    Jump('loc_1C06')

    def _loc_1B96(): pass

    label('loc_1B96')

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

    def _loc_1C06(): pass

    label('loc_1C06')

    Jump('loc_1E14')

    def _loc_1C09(): pass

    label('loc_1C09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1D23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1C91',
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

    Jump('loc_1D20')

    def _loc_1C91(): pass

    label('loc_1C91')

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

    def _loc_1D20(): pass

    label('loc_1D20')

    Jump('loc_1E14')

    def _loc_1D23(): pass

    label('loc_1D23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1D7B',
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

    Jump('loc_1E14')

    def _loc_1D7B(): pass

    label('loc_1D7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1E14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1DE0',
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

    Jump('loc_1E14')

    def _loc_1DE0(): pass

    label('loc_1DE0')

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

    def _loc_1E14(): pass

    label('loc_1E14')

    TalkEnd(0x0018)

    Return()

# id: 0x001E offset: 0x1E18
@scena.Code('func_1E_1E18')
def func_1E_1E18():
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
        'loc_1E76',
    )

    OP_0D()
    OP_A9(0x4E)
    OP_56(0x00)
    TalkEnd(0x0019)

    Return()

    def _loc_1E76(): pass

    label('loc_1E76')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E87',
    )

    TalkEnd(0x0019)

    Return()

    def _loc_1E87(): pass

    label('loc_1E87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_1ED4',
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

    Jump('loc_21FF')

    def _loc_1ED4(): pass

    label('loc_1ED4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1F36',
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

    Jump('loc_21FF')

    def _loc_1F36(): pass

    label('loc_1F36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1FB2',
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

    Jump('loc_21FF')

    def _loc_1FB2(): pass

    label('loc_1FB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2006',
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

    Jump('loc_21FF')

    def _loc_2006(): pass

    label('loc_2006')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2057',
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

    Jump('loc_21FF')

    def _loc_2057(): pass

    label('loc_2057')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_20B7',
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

    Jump('loc_21FF')

    def _loc_20B7(): pass

    label('loc_20B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_20E0',
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

    Jump('loc_21FF')

    def _loc_20E0(): pass

    label('loc_20E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_214B',
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

    Jump('loc_21FF')

    def _loc_214B(): pass

    label('loc_214B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_21B3',
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

    Jump('loc_21FF')

    def _loc_21B3(): pass

    label('loc_21B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_21FF',
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

    def _loc_21FF(): pass

    label('loc_21FF')

    TalkEnd(0x0019)

    Return()

# id: 0x001F offset: 0x2203
@scena.Code('func_1F_2203')
def func_1F_2203():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_228A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2246',
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

    Jump('loc_228A')

    def _loc_2246(): pass

    label('loc_2246')

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

    def _loc_228A(): pass

    label('loc_228A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x228E
@scena.Code('func_20_228E')
def func_20_228E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_237E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2325',
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

    Jump('loc_237E')

    def _loc_2325(): pass

    label('loc_2325')

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

    def _loc_237E(): pass

    label('loc_237E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x2382
@scena.Code('func_21_2382')
def func_21_2382():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x2389
@scena.Code('func_22_2389')
def func_22_2389():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x2390
@scena.Code('func_23_2390')
def func_23_2390():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2407',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_23CD',
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

    Jump('loc_2407')

    def _loc_23CD(): pass

    label('loc_23CD')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房袭击犯竟然\n',
            '穿着亲卫队的制服吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2407(): pass

    label('loc_2407')

    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x240B
@scena.Code('func_24_240B')
def func_24_240B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_24CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_245D',
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

    Jump('loc_24CA')

    def _loc_245D(): pass

    label('loc_245D')

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

    def _loc_24CA(): pass

    label('loc_24CA')

    Jump('loc_26AA')

    def _loc_24CD(): pass

    label('loc_24CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2550',
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

    Jump('loc_26AA')

    def _loc_2550(): pass

    label('loc_2550')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2667',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_25AF',
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

    Jump('loc_2664')

    def _loc_25AF(): pass

    label('loc_25AF')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

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

    def _loc_2664(): pass

    label('loc_2664')

    Jump('loc_26AA')

    def _loc_2667(): pass

    label('loc_2667')

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

    def _loc_26AA(): pass

    label('loc_26AA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x26AE
@scena.Code('func_25_26AE')
def func_25_26AE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_276B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2733',
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
            '我就会出名啦。',
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

    Jump('loc_276B')

    def _loc_2733(): pass

    label('loc_2733')

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
            '我就会出名啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_276B(): pass

    label('loc_276B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x276F
@scena.Code('func_26_276F')
def func_26_276F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_27B4',
    )

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

    def _loc_27B4(): pass

    label('loc_27B4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x27B8
@scena.Code('func_27_27B8')
def func_27_27B8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2876',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2818',
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

    Jump('loc_2873')

    def _loc_2818(): pass

    label('loc_2818')

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

    def _loc_2873(): pass

    label('loc_2873')

    Jump('loc_294F')

    def _loc_2876(): pass

    label('loc_2876')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_28D2',
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

    Jump('loc_294F')

    def _loc_28D2(): pass

    label('loc_28D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2926',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_290C',
    )

    ChrTalk(
        0x00FE,
        (
            '不是我斤斤计较，\n',
            '而是妈妈太浪费啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2923')

    def _loc_290C(): pass

    label('loc_290C')

    ChrTalk(
        0x00FE,
        (
            '提妲，\n',
            '早上好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2923(): pass

    label('loc_2923')

    Jump('loc_294F')

    def _loc_2926(): pass

    label('loc_2926')

    ChrTalk(
        0x00FE,
        (
            '妈妈，\n',
            '阳台的花坛已经放满花盆了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_294F(): pass

    label('loc_294F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x2953
@scena.Code('func_28_2953')
def func_28_2953():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2A8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_29E8',
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

    Jump('loc_2A87')

    def _loc_29E8(): pass

    label('loc_29E8')

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

    def _loc_2A87(): pass

    label('loc_2A87')

    Jump('loc_2BD9')

    def _loc_2A8A(): pass

    label('loc_2A8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2BD9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2ADC',
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

    Jump('loc_2BD9')

    def _loc_2ADC(): pass

    label('loc_2ADC')

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

    def _loc_2BD9(): pass

    label('loc_2BD9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x2BDD
@scena.Code('func_29_2BDD')
def func_29_2BDD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2F04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2C5F',
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

    Jump('loc_2F04')

    def _loc_2C5F(): pass

    label('loc_2C5F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Return,
        ),
        'loc_2EAC',
    )

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
            '#000F啊，是王先生……',
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
            '#000F嗯，其实啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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

    ChrTalk(
        0x0101,
        (
            '#000F唔唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哼，虽然不甘心，\n',
            '但阿加特说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……有什么不甘心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0012, 400)

    ChrTalk(
        0x0106,
        (
            '#050F还有你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '作为游击士，\n',
            '应该自己去确认当前的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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
            '#050F呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '算了，既然已经发生了，\n',
            '现在就考虑一下对策吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……喂，走啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F回头见，王先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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

    Jump('loc_2F04')

    def _loc_2EAC(): pass

    label('loc_2EAC')

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

    def _loc_2F04(): pass

    label('loc_2F04')

    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x2F08
@scena.Code('func_2A_2F08')
def func_2A_2F08():
    OP_13(0x0085)

    Return()

# id: 0x002B offset: 0x2F0C
@scena.Code('func_2B_2F0C')
def func_2B_2F0C():
    OP_13(0x0081)

    Return()

# id: 0x002C offset: 0x2F10
@scena.Code('func_2C_2F10')
def func_2C_2F10():
    ClearScenaFlags(ScenaFlag(0x00A8, 0, 0x540))
    ClearScenaFlags(ScenaFlag(0x00A8, 1, 0x541))
    ClearScenaFlags(ScenaFlag(0x00A8, 6, 0x546))
    ClearScenaFlags(ScenaFlag(0x00A8, 3, 0x543))
    ClearScenaFlags(ScenaFlag(0x00A8, 4, 0x544))
    ClearScenaFlags(ScenaFlag(0x00A8, 5, 0x545))
    SetScenaFlags(ScenaFlag(0x00A8, 6, 0x546))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
