import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3103   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3103.x'
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
            dword_00        = 0x000105B8,
            dword_04        = 0x00000000,
            dword_08        = 0x0000CF08,
            word_0C         = 0x0004,
            word_0E         = 0x013B,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
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
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
    ]

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '索黛丽娅',
            x                   = 17600,
            z                   = 3500,
            y                   = 53760,
            direction           = 283,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '阿利瑟',
            x                   = 18000,
            z                   = 3500,
            y                   = 52580,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '米优',
            x                   = 24380,
            z                   = 3500,
            y                   = 53780,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
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
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '加雷利',
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
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '库诺',
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
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '呆呆',
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
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '莱恩',
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
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '科奇莫爷爷',
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
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
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
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '伊格尔',
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '拉德米拉',
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
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '卡雷尔',
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
            talkScenaIndex      = 0x0007,
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
            name                = '蔡斯中央工房方向',
            x                   = -17220,
            z                   = 8000,
            y                   = 59000,
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
            name                = '托兰特平原道方向',
            x                   = 81330,
            z                   = 0,
            y                   = 53110,
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
            name                = '利塔街道方向',
            x                   = 42990,
            z                   = 0,
            y                   = 104270,
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

# id: 0x10002 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x382
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 39600,
            y           = -1000,
            z           = 90600,
            range       = 46400,
            dword_10    = 0x000003E8,
            dword_14    = 0x00016828,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = 69400,
            y           = -1000,
            z           = 56700,
            range       = 71000,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000B734,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 43700,
            y           = 0,
            z           = 63080,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 40200,
            y           = 0,
            z           = 66870,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 52230,
            y           = 0,
            z           = 54590,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 47450,
            y           = 450,
            z           = 51500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 47450,
            y           = 450,
            z           = 48500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 59950,
            y           = 0,
            z           = 25220,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 36000,
            y           = 0,
            z           = 54740,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 27020,
            y           = 0,
            z           = 63460,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = 23130,
            y           = 0,
            z           = 82450,
            range       = 1200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 64030,
            y           = 0,
            z           = 69550,
            range       = 1200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
    )

# id: 0x10004 offset: 0x502
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x502
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_57A',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 38910, 0, 68560, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 47810, 0, 37590, 185)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 38650, 0, 46790, 258)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_A42')

    def _loc_57A(): pass

    label('loc_57A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_5E6',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 38910, 0, 68560, 90)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 38910, 0, 69580, 177)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 41890, 0, 52020, 267)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)

    Jump('loc_A42')

    def _loc_5E6(): pass

    label('loc_5E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_6B1',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 16250, 3500, 71750, 39)
    CreateThread(0x0009, 0x00, 0x00, func_04_C3A)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 38910, 0, 68560, 90)
    ChrSetFlags(0x000D, 0x0010)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 38910, 0, 69580, 177)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 41890, 0, 52020, 267)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 38650, 0, 46790, 258)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 32970, 500, 85010, 175)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 39900, 0, 67550, 4)

    Jump('loc_A42')

    def _loc_6B1(): pass

    label('loc_6B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_6BB',
    )

    Jump('loc_A42')

    def _loc_6BB(): pass

    label('loc_6BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_6F1',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 22230, 0, 80520, 215)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_A42')

    def _loc_6F1(): pass

    label('loc_6F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_74C',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 20340, 0, 80730, 227)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 11290, 0, 64040, 258)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_A42')

    def _loc_74C(): pass

    label('loc_74C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_7F7',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 16780, 3500, 73480, 97)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 17830, 3500, 72380, 8)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 8690, 0, 54740, 180)
    CreateThread(0x000C, 0x00, 0x00, func_05_C5E)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 41890, 0, 52020, 267)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 47290, 0, 54830, 275)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 45580, 0, 54810, 97)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_A42')

    def _loc_7F7(): pass

    label('loc_7F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_859',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 16780, 3500, 73480, 97)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 17830, 3500, 72380, 8)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 41890, 0, 52020, 267)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)

    Jump('loc_A42')

    def _loc_859(): pass

    label('loc_859')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_929',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 16780, 3500, 73480, 97)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 17830, 3500, 72380, 8)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 41900, 0, 61970, 17)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 41890, 0, 52020, 267)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 38650, 0, 46790, 258)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, 46850, 0, 87800, 238)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 9770, 0, 59280, 277)

    Jump('loc_A42')

    def _loc_929(): pass

    label('loc_929')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_9B7',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 8690, 0, 54740, 306)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 38910, 0, 68560, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 47810, 0, 37590, 185)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 38650, 0, 46790, 258)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_A42')

    def _loc_9B7(): pass

    label('loc_9B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_A42',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 8690, 0, 54740, 306)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 38910, 0, 68560, 90)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 47810, 0, 37590, 185)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 38650, 0, 46790, 258)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 32930, 0, 83370, 1)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 45470, 0, 62220, 1)

    def _loc_A42(): pass

    label('loc_A42')

    Return()

# id: 0x0001 offset: 0xA43
@scena.Code('func_01_A43')
def func_01_A43():
    OP_16(0x02, 4000, -93000, -69000, 196689)
    OP_6F(0x0010, 40)
    OP_70(0x0010, 0)
    OP_25(0x00A0, 460, 2780, 58940, 10000, 40000, 0x64, 0x00000000)
    CreateThread(0x0016, 0x00, 0x00, func_02_A87)

    Return()

# id: 0x0002 offset: 0xA87
@scena.Code('func_02_A87')
def func_02_A87():
    OP_72(0x0010, 0x0020)
    OP_72(0x000E, 0x0020)
    def _loc_A91(): pass

    label('loc_A91')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_ABC',
    )

    OP_6F(0x0010, 40)
    OP_70(0x0010, 0)
    OP_6F(0x000E, 0)
    OP_70(0x000E, 40)
    OP_73(0x0010)

    Jump('loc_A91')

    def _loc_ABC(): pass

    label('loc_ABC')

    Return()

# id: 0x0003 offset: 0xABD
@scena.Code('func_03_ABD')
def func_03_ABD():
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
        'loc_AE2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_C24')

    def _loc_AE2(): pass

    label('loc_AE2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AFB',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_C24')

    def _loc_AFB(): pass

    label('loc_AFB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B14',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_C24')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B2D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_C24')

    def _loc_B2D(): pass

    label('loc_B2D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B46',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_C24')

    def _loc_B46(): pass

    label('loc_B46')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5F',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_C24')

    def _loc_B5F(): pass

    label('loc_B5F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B78',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_C24')

    def _loc_B78(): pass

    label('loc_B78')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B91',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_C24')

    def _loc_B91(): pass

    label('loc_B91')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BAA',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_C24')

    def _loc_BAA(): pass

    label('loc_BAA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC3',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_C24')

    def _loc_BC3(): pass

    label('loc_BC3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDC',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_C24')

    def _loc_BDC(): pass

    label('loc_BDC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF5',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_C24')

    def _loc_BF5(): pass

    label('loc_BF5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0E',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_C24')

    def _loc_C0E(): pass

    label('loc_C0E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C24',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_C24(): pass

    label('loc_C24')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C39',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_C24')

    def _loc_C39(): pass

    label('loc_C39')

    Return()

# id: 0x0004 offset: 0xC3A
@scena.Code('func_04_C3A')
def func_04_C3A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C5D',
    )

    OP_8D(0x00FE, 17510, 71160, 14830, 73220, 3000)

    Jump('func_04_C3A')

    def _loc_C5D(): pass

    label('loc_C5D')

    Return()

# id: 0x0005 offset: 0xC5E
@scena.Code('func_05_C5E')
def func_05_C5E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C81',
    )

    OP_8D(0x00FE, 11460, 51180, 8590, 67130, 3000)

    Jump('func_05_C5E')

    def _loc_C81(): pass

    label('loc_C81')

    Return()

# id: 0x0006 offset: 0xC82
@scena.Code('func_06_C82')
def func_06_C82():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_D65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_CEE',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '兰达那家伙也在很拼命地工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙，\n',
            '从什么时候开始在酒馆工作了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D65')

    def _loc_CEE(): pass

    label('loc_CEE')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '怎么了，\n',
            '街上的钟变慢了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来如此。\n',
            '看来导力停止过的事情\n',
            '是真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，我明白了。\n',
            '等一下去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D65(): pass

    label('loc_D65')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xD69
@scena.Code('func_07_D69')
def func_07_D69():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1046',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FE3',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找齿轮的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你要回卡尔瓦德共和国去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '不，在那之前要先去中央工房。\n',
            '因为在格兰赛尔卖了些东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老妈说用那些米拉\n',
            '买些导力器回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正老妈也开始知道\n',
            '什么东西才是有价值的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F怎么样都好啦，\n',
            '你还是老样子，那么自大傲慢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗？我觉得自己 \n',
            '只不过是说了理所当然的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此……\n',
            '这种自动导力梯真是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看多少次都不会厌烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1046')

    def _loc_FE3(): pass

    label('loc_FE3')

    ChrTalk(
        0x00FE,
        (
            '这种自动导力梯，真是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '走着上下楼梯\n',
            '的确有点麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，就让楼梯动起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1046(): pass

    label('loc_1046')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x104A
@scena.Code('func_08_104A')
def func_08_104A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1161',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_10B2',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀……？\n',
            '说起来卡雷尔在哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个笨蛋儿子，\n',
            '又在什么地方闲逛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1161')

    def _loc_10B2(): pass

    label('loc_10B2')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '唉，真是的。\n',
            '好不容易来到蔡斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来的行程是\n',
            '要到一个叫中央工房的地方\n',
            '去看看那些导力制品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在那之前，我还是想稍微落一下脚。\n',
            '找个合适的地方歇歇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1161(): pass

    label('loc_1161')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1165
@scena.Code('func_09_1165')
def func_09_1165():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1279',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_11EC',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '之后是回收破碎的结晶回路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～～\n',
            '怎么一大早就觉得没有干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是去礼拜堂\n',
            '祈祷一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1276')

    def _loc_11EC(): pass

    label('loc_11EC')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '唔，一盒８号的螺丝，\n',
            '两套导力压的测定仪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，总觉得每周\n',
            '都在干一成不变的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在仓库里检查零件\n',
            '其实是很辛苦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1276(): pass

    label('loc_1276')

    Jump('loc_17B8')

    def _loc_1279(): pass

    label('loc_1279')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_12EB',
    )

    ChrTalk(
        0x00FE,
        (
            '总是很难找到\n',
            '要找的箱子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然跟耶鲁克说了让他把这里整理一下，\n',
            '不过他肯定会拖到下次再做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B8')

    def _loc_12EB(): pass

    label('loc_12EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_136E',
    )

    ChrTalk(
        0x00FE,
        (
            '好吧，从今早开始\n',
            '要以全新的精神面貌进行工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一定要对\n',
            '武器店的耶鲁克说清楚，\n',
            '叫他把箱子里的零件都整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B8')

    def _loc_136E(): pass

    label('loc_136E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_13A8',
    )

    ChrTalk(
        0x00FE,
        (
            '工房的人们呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经都去避难了吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B8')

    def _loc_13A8(): pass

    label('loc_13A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_14E0',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_1456',
    )

    ChrTalk(
        0x00FE,
        (
            '本来是想去\n',
            '和耶鲁克店长商量\n',
            '把这里好好整理一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我又拿不出\n',
            '和他说话的勇气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我也不能去向\n',
            '斯坦因老板告密，\n',
            '打小报告总是不好的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_1456(): pass

    label('loc_1456')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '该死，\n',
            '又找不到想要的零件箱子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来是想去\n',
            '和耶鲁克店长商量\n',
            '把这里好好整理一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我又拿不出\n',
            '和他说话的勇气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14DD(): pass

    label('loc_14DD')

    Jump('loc_17B8')

    def _loc_14E0(): pass

    label('loc_14E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1621',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_1582',
    )

    ChrTalk(
        0x00FE,
        (
            '尽管如此……\n',
            '这里的整理还真是乱七八糟呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，等找到需要的零件，\n',
            '也不知道花了多长时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '进步总是伴随着牺牲的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_161E')

    def _loc_1582(): pass

    label('loc_1582')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '昨天真是大吃一惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照明被切断的时候\n',
            '大伙都惊呆了好一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '演算室的那些家伙\n',
            '脸色比我还要苍白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，\n',
            '进步总是伴随着牺牲的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_161E(): pass

    label('loc_161E')

    Jump('loc_17B8')

    def _loc_1621(): pass

    label('loc_1621')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1696',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，提妲。\n',
            '总是要你帮忙整理零件，谢谢啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回去请和你爷爷说，\n',
            '如果有零件用完了，\n',
            '就尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B8')

    def _loc_1696(): pass

    label('loc_1696')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_17B8',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_16E4',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剩下的任务\n',
            '就只剩回收破损的结晶回路啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17B8')

    def _loc_16E4(): pass

    label('loc_16E4')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '嗯，一盒８号的螺丝，\n',
            '两套导力压的测定仪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，清点各个仓库的零件\n',
            '这种工作也不轻松啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为在蔡斯，\n',
            '到处都有大大小小的研究所啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里有博士的孙女儿\n',
            '来帮忙进行整理，\n',
            '工作起来还是很容易的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17B8(): pass

    label('loc_17B8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x17BC
@scena.Code('func_0A_17BC')
def func_0A_17BC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1817',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '今天时钟走得也很准呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不确认一下这个，\n',
            '我的一天就无法开始呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAF')

    def _loc_1817(): pass

    label('loc_1817')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_18A1',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '时钟终于走准了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要这个钟还在工作，\n',
            '我们这一代人就必须努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不然的话，\n',
            '就没有别人\n',
            '会照顾这个时钟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAF')

    def _loc_18A1(): pass

    label('loc_18A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1A7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_18E5',
    )

    ChrTalk(
        0x0013,
        (
            '那么，\n',
            '这就开始校正时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A7B')

    def _loc_18E5(): pass

    label('loc_18E5')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '抱歉，在你正忙的时候麻烦你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '哪里，\n',
            '其实我也没什么忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '反正我也就是个\n',
            '落后于时代的技师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你在说什么呀。\n',
            '你要知道自己是参与了\n',
            '『埃尔赛尤号』建造的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明参与了\n',
            '世上最新的高速飞艇的建造工作，\n',
            '却还常说跟不上时代什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '哈哈，多谢夸奖了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '本来想在建造『埃尔赛尤号』的工作中\n',
            '给拉赛尔帮点忙的，\n',
            '果然还是太勉强了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '唉，不能不服老啊。\n',
            '还是尽全力发挥余热吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A7B(): pass

    label('loc_1A7B')

    Jump('loc_1DAF')

    def _loc_1A7E(): pass

    label('loc_1A7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1AAA',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些烟是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAF')

    def _loc_1AAA(): pass

    label('loc_1AAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1B8F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1B1B',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，像我和兰达这样年纪的人\n',
            '已经很害怕摆弄机械了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有困难的时候\n',
            '也只有依靠年轻人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B8C')

    def _loc_1B1B(): pass

    label('loc_1B1B')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '喂喂，伊格尔。\n',
            '还是那么有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会儿帮我瞧瞧街上的钟表吧。\n',
            '因为昨天的那件事，今天似乎有点慢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B8C(): pass

    label('loc_1B8C')

    Jump('loc_1DAF')

    def _loc_1B8F(): pass

    label('loc_1B8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1C49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1C08',
    )

    ChrTalk(
        0x00FE,
        (
            '果然是因为昨晚\n',
            '导力停止的原因呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在需要调整时间，\n',
            '待会儿去叫伊格尔那家伙来修理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C46')

    def _loc_1C08(): pass

    label('loc_1C08')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '喔，钟慢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是因为昨晚\n',
            '导力停止的原因呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C46(): pass

    label('loc_1C46')

    Jump('loc_1DAF')

    def _loc_1C49(): pass

    label('loc_1C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1DAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1CDD',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '导力器是从钟表技术中发展起来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近又把导力作为动力源\n',
            '制作出一些导力钟表。\n',
            '『技术』这东西还真是有趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DAF')

    def _loc_1CDD(): pass

    label('loc_1CDD')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '呼，每次看到都让人感到怀念。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个啊，是以前我和拉赛尔他们\n',
            '一起制造的导力钟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它是用导力器驱动的。\n',
            '只要导力不停止，就会永远转动下去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个钟是蔡斯还是钟表之城时\n',
            '为数不多的纪念品之一了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DAF(): pass

    label('loc_1DAF')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1DB3
@scena.Code('func_0B_1DB3')
def func_0B_1DB3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1E63',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，教你们一个\n',
            '买东西不用犹豫的好办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不知道想买哪个，\n',
            '就选最右边的那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话， \n',
            '就算不知道东西是好是坏，\n',
            '也可以很顺利地把东西买回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E7')

    def _loc_1E63(): pass

    label('loc_1E63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1F38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1ED4',
    )

    ChrTalk(
        0x00FE,
        (
            '话又说回来，\n',
            '商品的标示最好能再清楚些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不写上一大堆参数的话，\n',
            '会让消费者很为难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F35')

    def _loc_1ED4(): pass

    label('loc_1ED4')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '今天我\n',
            '是来买罐头的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯！比买面包要简单哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为标签上写了\n',
            '里面装了些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F35(): pass

    label('loc_1F35')

    Jump('loc_21E7')

    def _loc_1F38(): pass

    label('loc_1F38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1F8E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～太好了。\n',
            '看来终于安静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '我又可以专心去买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E7')

    def _loc_1F8E(): pass

    label('loc_1F8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1FE6',
    )

    ChrTalk(
        0x00FE,
        (
            '杂货铺的老板\n',
            '不知道跑到什么地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是去看\n',
            '工房那边的骚乱了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E7')

    def _loc_1FE6(): pass

    label('loc_1FE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2103',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2095',
    )

    ChrTalk(
        0x00FE,
        (
            '我爸爸是导力技师，\n',
            '平时我习惯去买机器零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '机器零件都附有说明书的，\n',
            '选起来也非常简单轻松……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '为什么偏偏就面包没有说明书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2100')

    def _loc_2095(): pass

    label('loc_2095')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '面包啊面包……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '到底哪一个才是好面包呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少也要附张说明书\n',
            '让我看看才能判断啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2100(): pass

    label('loc_2100')

    Jump('loc_21E7')

    def _loc_2103(): pass

    label('loc_2103')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_21E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2176',
    )

    ChrTalk(
        0x00FE,
        (
            '我还是头一次\n',
            '自己来买吃的东西呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可所有面包看起来都一样。\n',
            '它们到底有什么不同呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E7')

    def _loc_2176(): pass

    label('loc_2176')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '啊，怎么办呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天爸爸\n',
            '让我自己来买面包……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可所有面包看起来都一样。\n',
            '它们到底有什么不同呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21E7(): pass

    label('loc_21E7')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x21EB
@scena.Code('func_0C_21EB')
def func_0C_21EB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_22D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_225D',
    )

    ChrTalk(
        0x00FE,
        (
            '我自己很累就不用说了，\n',
            '做护卫的游击士也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，这也是我们的工作，\n',
            '没办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22CF')

    def _loc_225D(): pass

    label('loc_225D')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '呼，今天下午又要去\n',
            '沃尔费堡垒那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '共和国的那些家伙真是的，\n',
            '要给他们出口多少导力器\n',
            '他们才会满意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22CF(): pass

    label('loc_22CF')

    Jump('loc_26AD')

    def _loc_22D2(): pass

    label('loc_22D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_23AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_233D',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，没办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在时间还早，\n',
            '不过还是赶快去委托\n',
            '游击士协会承担护卫工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AB')

    def _loc_233D(): pass

    label('loc_233D')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '刚想好不容易回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '马上又要去\n',
            '沃尔费堡垒那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '连发牢骚的空闲也没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AB(): pass

    label('loc_23AB')

    Jump('loc_26AD')

    def _loc_23AE(): pass

    label('loc_23AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_24E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2456',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，这些家伙都是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光在这里聊昨天的事，\n',
            '也不动手做点事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就我一个人需要\n',
            '马上去沃尔费堡垒送货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎，\n',
            '能干的男人就是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E1')

    def _loc_2456(): pass

    label('loc_2456')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '好，货物都装好了，\n',
            '再过一阵就要出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后再对货物\n',
            '进行一次检查吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……呀，对了。\n',
            '还要连络一下\n',
            '护卫的游击士才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E1(): pass

    label('loc_24E1')

    Jump('loc_26AD')

    def _loc_24E4(): pass

    label('loc_24E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_25CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2563',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然想让搬运车进行一次检查，\n',
            '可这里的维修员也很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像他们的名字一样，\n',
            '一直在这里那里的到处跑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C7')

    def _loc_2563(): pass

    label('loc_2563')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '话说回来，\n',
            '这辆搬运车也要尽快\n',
            '让修理员检查一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '车子可不能在魔兽\n',
            '出没的地方抛锚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25C7(): pass

    label('loc_25C7')

    Jump('loc_26AD')

    def _loc_25CA(): pass

    label('loc_25CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_26AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2639',
    )

    ChrTalk(
        0x00FE,
        (
            '其实要是能用飞艇\n',
            '来运送出口货物就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，直航共和国的运输艇\n',
            '只会从王都出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AD')

    def _loc_2639(): pass

    label('loc_2639')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '差不多该按计划\n',
            '去确认货物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把预定的货物装好，\n',
            '用这部搬运车把这些\n',
            '向共和国出口的货物运往沃尔费堡垒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26AD(): pass

    label('loc_26AD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x26B1
@scena.Code('func_0D_26B1')
def func_0D_26B1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_26D3',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么了？那股烟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26D3(): pass

    label('loc_26D3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x26D7
@scena.Code('func_0E_26D7')
def func_0E_26D7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2772',
    )

    ChrTalk(
        0x00FE,
        (
            '袭击中央工房的\n',
            '好像是亲卫队的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的温丝\n',
            '说看见了那些是\n',
            '穿着蓝色军装的军人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说这话很难让人相信，\n',
            '但那孩子从不说谎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B4')

    def _loc_2772(): pass

    label('loc_2772')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2794',
    )

    ChrTalk(
        0x00FE,
        (
            '不，不是火灾吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B4')

    def _loc_2794(): pass

    label('loc_2794')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_27FE',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，确实像孩子说的那样，\n',
            '花坛里面已经放不下更多的花了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '分一点花\n',
            '给对面的索黛丽娅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B4')

    def _loc_27FE(): pass

    label('loc_27FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_28B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_285B',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，温丝。\n',
            '这样搭配怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不觉得花色间的平衡感\n',
            '很不错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28B4')

    def _loc_285B(): pass

    label('loc_285B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '听我家的老公说，\n',
            '昨天的现象\n',
            '是因为导力停止所造成的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的会有这样的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28B4(): pass

    label('loc_28B4')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x28B8
@scena.Code('func_0F_28B8')
def func_0F_28B8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2941',
    )

    ChrTalk(
        0x00FE,
        (
            '总觉得妈妈\n',
            '似乎是弄错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很想做一名\n',
            '中央工房的接待小姐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '海泽尔的年纪也不小了，\n',
            '要我跟她比肯定不在话下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2941(): pass

    label('loc_2941')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2945
@scena.Code('func_10_2945')
def func_10_2945():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2A8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_29DB',
    )

    ChrTalk(
        0x00FE,
        (
            '这样说来，\n',
            '中央工房的防范体制\n',
            '会因为这件事而被重新评估吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '要是工房那种自由的风气被限制了，\n',
            '总觉得有点可惜呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8A')

    def _loc_29DB(): pass

    label('loc_29DB')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '有一群穿着蓝色制服的军人\n',
            '刚刚从这里跑过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恰好在这个时候出现，\n',
            '我想那些人和中央工房\n',
            '被袭的事件脱不了干系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可惜……没有带着导力相机，\n',
            '真是有点不甘心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A8A(): pass

    label('loc_2A8A')

    Jump('loc_2D1A')

    def _loc_2A8D(): pass

    label('loc_2A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2AEB',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么回事？\n',
            '看起来不像是火灾的浓烟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些气体是\n',
            '从什么实验装置排出的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D1A')

    def _loc_2AEB(): pass

    label('loc_2AEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2C44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2BAF',
    )

    ChrTalk(
        0x00FE,
        (
            '有机会的话，\n',
            '我很想去资料室查阅一下\n',
            '关于那个现象的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，在那之前，\n',
            '必须让康丝坦茨\n',
            '整理一下资料室才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起调查原因，\n',
            '整理资料室所花费的工夫要多得多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C41')

    def _loc_2BAF(): pass

    label('loc_2BAF')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '导力停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这方面的资料\n',
            '我也从来没看见过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说实验就是导力停止的原因，\n',
            '不过到底做了什么样的实验\n',
            '会导致那种事情发生呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C41(): pass

    label('loc_2C41')

    Jump('loc_2D1A')

    def _loc_2C44(): pass

    label('loc_2C44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2D1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2C8C',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个花坛\n',
            '哪里变得不一样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D1A')

    def _loc_2C8C(): pass

    label('loc_2C8C')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '导力这东西\n',
            '竟然会自己停下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前读过的初等导力理论\n',
            '都没有记载过这种现象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来得要阅读一下\n',
            '更详细的专业书籍才行呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D1A(): pass

    label('loc_2D1A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2D1E
@scena.Code('func_11_2D1E')
def func_11_2D1E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2E07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2DB1',
    )

    ChrTalk(
        0x00FE,
        (
            '那里似乎是个\n',
            '非常富有东方风情的温泉胜地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实际上我对东方的文化\n',
            '抱有相当浓烈的兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '真是让人相当期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E04')

    def _loc_2DB1(): pass

    label('loc_2DB1')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我听说\n',
            '这附近好像有温泉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然来到这城市了，\n',
            '有机会一定要去那里看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E04(): pass

    label('loc_2E04')

    Jump('loc_2E96')

    def _loc_2E07(): pass

    label('loc_2E07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2E96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2E5F',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是不习惯的话，\n',
            '还是很难掌握乘上去的时机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E96')

    def _loc_2E5F(): pass

    label('loc_2E5F')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '哦哦，好厉害呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和传闻一样，楼梯会动呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E96(): pass

    label('loc_2E96')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2E9A
@scena.Code('func_12_2E9A')
def func_12_2E9A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2FFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2F60',
    )

    ChrTalk(
        0x00FE,
        (
            '好的，今天就从罐子的摆放开始\n',
            '好好整理一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……将卖剩下的罐子\n',
            '摆到前列的最右边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将最想卖掉的东西\n',
            '摆放在手容易够到的地方，\n',
            '这可是商品摆放技术里基本中的基本哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FFA')

    def _loc_2F60(): pass

    label('loc_2F60')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我很想快点将\n',
            '商品摆放的要领\n',
            '教给我的弟弟呆呆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许还是太早了点吧。\n',
            '那家伙很快就会厌烦不干的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '看来暂时还是必须由我来干啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x00FE, 0x0010)

    def _loc_2FFA(): pass

    label('loc_2FFA')

    Jump('loc_3516')

    def _loc_2FFD(): pass

    label('loc_2FFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_30CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_305C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，呆呆，\n',
            '你摆放得太靠边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的话，\n',
            '不就破坏了整体的平衡吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30C8')

    def _loc_305C(): pass

    label('loc_305C')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '嗯，小心点。\n',
            '我觉得将右边的罐子移动到左边的话\n',
            '一定更美观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说呆呆，\n',
            '快点照我说的那样做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30C8(): pass

    label('loc_30C8')

    Jump('loc_3516')

    def _loc_30CB(): pass

    label('loc_30CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3192',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3144',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得也差不多\n',
            '该让弟弟来尝试一下工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '商品摆放包涵的学问多着呢，\n',
            '我很想早点多教他点知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318F')

    def _loc_3144(): pass

    label('loc_3144')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '听好了，呆呆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要将客人动过的商品\n',
            '整整齐齐地放回原位啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_318F(): pass

    label('loc_318F')

    Jump('loc_3516')

    def _loc_3192(): pass

    label('loc_3192')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_32F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_31EB',
    )

    ChrTalk(
        0x00FE,
        (
            '原来真正的夜晚\n',
            '竟然那么黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我往窗外一看，\n',
            '真是吓坏我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32F0')

    def _loc_31EB(): pass

    label('loc_31EB')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '啊，提妲。\n',
            '欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，\n',
            '昨天怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲家的导力\n',
            '也都全部停止了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F哎……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……啊，嗯，是啊！\n',
            '停了停了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～也就是说\n',
            '城里的导力都停了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '原来真正的夜晚竟然那么黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我往窗外一看，\n',
            '真是吓坏我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32F0(): pass

    label('loc_32F0')

    Jump('loc_3516')

    def _loc_32F3(): pass

    label('loc_32F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_346F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3354',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '果然还是不够美观啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次把左边的那个罐子\n',
            '再往左边挪一点试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_346C')

    def _loc_3354(): pass

    label('loc_3354')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '唔……为什么\n',
            '整体的协调感还是这么差呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯？\n',
            '哎，是提妲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你今天也要\n',
            '去给爷爷帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '库诺也在店里帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，\n',
            '我负责摆放商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '接下来该摆放水果了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回头见，提妲。\n',
            '下次主日学校见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯。\n',
            '加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_346C(): pass

    label('loc_346C')

    Jump('loc_3516')

    def _loc_346F(): pass

    label('loc_346F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3516',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_34B9',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，不好看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把右边的罐子\n',
            '重新垒一遍试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3516')

    def _loc_34B9(): pass

    label('loc_34B9')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '为什么整体的协调感还是这么差呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把这个左边的罐子\n',
            '再往左边挪一点试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3516(): pass

    label('loc_3516')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x351A
@scena.Code('func_13_351A')
def func_13_351A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_355E',
    )

    ChrTalk(
        0x00FE,
        (
            '哎～我已经烦了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哥哥真是的～\n',
            '没办法～啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35E8')

    def _loc_355E(): pass

    label('loc_355E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_35E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_35BD',
    )

    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '导力引擎，开动！\n',
            '将罐子抓住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………好的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35E8')

    def _loc_35BD(): pass

    label('loc_35BD')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '了解，库诺博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35E8(): pass

    label('loc_35E8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x35EC
@scena.Code('func_14_35EC')
def func_14_35EC():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_362A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010081392V#002F（啊，这边是城外……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372D')

    def _loc_362A(): pass

    label('loc_362A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3681',
    )

    ChrTalk(
        0x0102,
        (
            '#0020081393V#012F（这里是城的出口啊……\n',
            '　现在没有必要出城去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372D')

    def _loc_3681(): pass

    label('loc_3681')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36BD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070081394V#062F（啊，这边是出口……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372D')

    def _loc_36BD(): pass

    label('loc_36BD')

    ChrTalk(
        0x0108,
        (
            '#0080081395V#070F（呼，晚上的街道吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081396V（虽然是个不错的修行场所，\n',
            '　不过下次有机会再说吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_372D(): pass

    label('loc_372D')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0015 offset: 0x3749
@scena.Code('func_15_3749')
def func_15_3749():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3787',
    )

    ChrTalk(
        0x0101,
        (
            '#0010081392V#002F（啊，这边是城外……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_388A')

    def _loc_3787(): pass

    label('loc_3787')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37DE',
    )

    ChrTalk(
        0x0102,
        (
            '#0020081393V#012F（这里是城的出口啊……\n',
            '　现在没有必要出城去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_388A')

    def _loc_37DE(): pass

    label('loc_37DE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_381A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070081394V#062F（啊，这边是出口……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_388A')

    def _loc_381A(): pass

    label('loc_381A')

    ChrTalk(
        0x0108,
        (
            '#0080081395V#070F（呼，晚上的街道吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081396V（虽然是个不错的修行场所，\n',
            '　不过下次有机会再说吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_388A(): pass

    label('loc_388A')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0016 offset: 0x38A6
@scena.Code('func_16_38A6')
def func_16_38A6():
    OP_13(0x007D)

    Return()

# id: 0x0017 offset: 0x38AA
@scena.Code('func_17_38AA')
def func_17_38AA():
    OP_13(0x007F)

    Return()

# id: 0x0018 offset: 0x38AE
@scena.Code('func_18_38AE')
def func_18_38AE():
    OP_13(0x0082)

    Return()

# id: 0x0019 offset: 0x38B2
@scena.Code('func_19_38B2')
def func_19_38B2():
    OP_13(0x007C)

    Return()

# id: 0x001A offset: 0x38B6
@scena.Code('func_1A_38B6')
def func_1A_38B6():
    OP_13(0x007A)

    Return()

# id: 0x001B offset: 0x38BA
@scena.Code('func_1B_38BA')
def func_1B_38BA():
    OP_13(0x007B)

    Return()

# id: 0x001C offset: 0x38BE
@scena.Code('func_1C_38BE')
def func_1C_38BE():
    OP_13(0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
