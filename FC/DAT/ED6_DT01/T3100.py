import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '索黛丽娅'),
    TXT(0x02, '阿利瑟'),
    TXT(0x03, '米优'),
    TXT(0x04, '温丝'),
    TXT(0x05, '加雷利'),
    TXT(0x06, '库诺'),
    TXT(0x07, '呆呆'),
    TXT(0x08, '莱恩'),
    TXT(0x09, '科奇莫爷爷'),
    TXT(0x0A, '莫妮卡'),
    TXT(0x0B, '布鲁诺'),
    TXT(0x0C, '伊格尔'),
    TXT(0x0D, '拉德米拉'),
    TXT(0x0E, '卡雷尔'),
    TXT(0x0F, ' '),
    TXT(0x10, '蔡斯市·工房区'),
    TXT(0x11, '托兰特平原道方向'),
    TXT(0x12, '利塔街道方向'),
    TXT(0x13, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3100.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5741
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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
            word_36         = 270,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
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
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 23890,
            z                   = 3500,
            y                   = 53440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
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

# id: 0x10003 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x382
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
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 69400,
            y           = -1000,
            z           = 56700,
            range       = 71000,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000B734,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 7780,
            y           = -1000,
            z           = 63930,
            range       = 6420,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000EA1A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 6420,
            y           = -1000,
            z           = 58250,
            range       = 7860,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000D5D4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 43700,
            y           = 0,
            z           = 63080,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 40200,
            y           = 0,
            z           = 66870,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 52230,
            y           = 0,
            z           = 54590,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 47450,
            y           = 450,
            z           = 51500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 47450,
            y           = 450,
            z           = 48500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 59950,
            y           = 0,
            z           = 25220,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000020,
        ),
        ScenaEventData(
            x           = 36000,
            y           = 0,
            z           = 54740,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = 27020,
            y           = 0,
            z           = 63460,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000022,
        ),
        ScenaEventData(
            x           = 23130,
            y           = 0,
            z           = 82450,
            range       = 1200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000023,
        ),
        ScenaEventData(
            x           = 64030,
            y           = 0,
            z           = 69550,
            range       = 1200,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000024,
        ),
    )

# id: 0x10005 offset: 0x542
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 33000,
            triggerZ            = 500,
            triggerY            = 85510,
            triggerRange        = 800,
            actorX              = 33000,
            actorZ              = 1500,
            actorY              = 85510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x566
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_574',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0019)

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_582',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x001A)

    def _loc_582(): pass

    label('loc_582')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_58E'),
        (-1, 'loc_5AD'),
    )

    def _loc_58E(): pass

    label('loc_58E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 2, 0x52A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AA',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 3, 0x52B))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x001B)

    def _loc_5AA(): pass

    label('loc_5AA')

    Jump('loc_5AD')

    def _loc_5AD(): pass

    label('loc_5AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_625',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 38910, 0, 68560, 90)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41020, 0, 53780, 180)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 39400, 0, 46910, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_B56')

    def _loc_625(): pass

    label('loc_625')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_691',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 38910, 0, 68560, 90)
    SetChrFlags(0x000D, 0x0010)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 38910, 0, 69580, 90)
    SetChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41890, 0, 52020, 267)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)

    Jump('loc_B56')

    def _loc_691(): pass

    label('loc_691')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_76B',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 16250, 3500, 71750, 39)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 45110, 0, 62220, 90)
    SetChrFlags(0x000D, 0x0010)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 46310, 0, 62180, 0)
    SetChrFlags(0x000E, 0x0010)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41020, 0, 53780, 180)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 39400, 0, 46910, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 32970, 500, 85010, 175)
    SetChrFlags(0x0013, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 38670, 0, 68820, 90)

    Jump('loc_B56')

    def _loc_76B(): pass

    label('loc_76B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_775',
    )

    Jump('loc_B56')

    def _loc_775(): pass

    label('loc_775')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_7AB',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 22230, 0, 80520, 215)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_B56')

    def _loc_7AB(): pass

    label('loc_7AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_806',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 20340, 0, 80730, 227)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 14670, 0, 60890, 270)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_B56')

    def _loc_806(): pass

    label('loc_806')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_8BB',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 16780, 3500, 73480, 97)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 17830, 3500, 72380, 8)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 8690, 0, 54740, 180)
    CreateThread(0x000C, 0x00, 0x00, 0x0005)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41890, 0, 52020, 267)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 45910, 0, 57120, 270)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 44430, 0, 57110, 90)
    SetChrFlags(0x0013, 0x0010)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_B56')

    def _loc_8BB(): pass

    label('loc_8BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_95F',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 16780, 3500, 73480, 97)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 17830, 3500, 72380, 8)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41890, 0, 52020, 267)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 46850, 0, 87800, 238)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 9770, 0, 59280, 277)

    Jump('loc_B56')

    def _loc_95F(): pass

    label('loc_95F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_A2F',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 16780, 3500, 73480, 97)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 17830, 3500, 72380, 8)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 41900, 0, 61970, 17)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41890, 0, 52020, 267)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 39400, 0, 46910, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 46850, 0, 87800, 238)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 9770, 0, 59280, 277)

    Jump('loc_B56')

    def _loc_A2F(): pass

    label('loc_A2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_AC4',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 10650, 0, 59050, 270)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 35280, 0, 69150, 90)
    CreateThread(0x000D, 0x00, 0x00, 0x0006)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41020, 0, 53780, 180)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 39400, 0, 46910, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)

    Jump('loc_B56')

    def _loc_AC4(): pass

    label('loc_AC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B56',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 10650, 0, 59050, 270)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 35280, 0, 69150, 90)
    CreateThread(0x000D, 0x00, 0x00, 0x0006)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 41020, 0, 53780, 180)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 39400, 0, 46910, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 32930, 0, 83370, 1)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 45470, 0, 62220, 1)

    def _loc_B56(): pass

    label('loc_B56')

    Return()

# id: 0x0001 offset: 0xB57
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -93000, -69000, 196689)
    OP_6F(0x0010, 40)
    OP_70(0x0010, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_B81',
    )

    Jump('loc_BAE')

    def _loc_B81(): pass

    label('loc_B81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_B90',
    )

    OP_71(0x0011, 0x0004)

    Jump('loc_BAE')

    def _loc_B90(): pass

    label('loc_B90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_B9F',
    )

    OP_71(0x0011, 0x0004)

    Jump('loc_BAE')

    def _loc_B9F(): pass

    label('loc_B9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_BAE',
    )

    OP_71(0x0011, 0x0004)

    Jump('loc_BAE')

    def _loc_BAE(): pass

    label('loc_BAE')

    OP_25(0x00A0, 460, 2780, 58940, 10000, 30000, 0x64, 0x00000000)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0002 offset: 0xBD2
@scena.Code('ReInit')
def ReInit():
    OP_72(0x0010, 0x0020)
    OP_72(0x000E, 0x0020)
    def _loc_BDC(): pass

    label('loc_BDC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C07',
    )

    OP_6F(0x0010, 40)
    OP_70(0x0010, 0)
    OP_6F(0x000E, 0)
    OP_70(0x000E, 40)
    OP_73(0x0010)

    Jump('loc_BDC')

    def _loc_C07(): pass

    label('loc_C07')

    Return()

# id: 0x0003 offset: 0xC08
@scena.Code('func_03_C08')
def func_03_C08():
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
        'loc_C2D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_D6F')

    def _loc_C2D(): pass

    label('loc_C2D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C46',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_D6F')

    def _loc_C46(): pass

    label('loc_C46')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C5F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_D6F')

    def _loc_C5F(): pass

    label('loc_C5F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C78',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_D6F')

    def _loc_C78(): pass

    label('loc_C78')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C91',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_D6F')

    def _loc_C91(): pass

    label('loc_C91')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CAA',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_D6F')

    def _loc_CAA(): pass

    label('loc_CAA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC3',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_D6F')

    def _loc_CC3(): pass

    label('loc_CC3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CDC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_D6F')

    def _loc_CDC(): pass

    label('loc_CDC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_D6F')

    def _loc_CF5(): pass

    label('loc_CF5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D0E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_D6F')

    def _loc_D0E(): pass

    label('loc_D0E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D27',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_D6F')

    def _loc_D27(): pass

    label('loc_D27')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D40',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_D6F')

    def _loc_D40(): pass

    label('loc_D40')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D59',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_D6F')

    def _loc_D59(): pass

    label('loc_D59')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D6F',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_D6F(): pass

    label('loc_D6F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D84',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_D6F')

    def _loc_D84(): pass

    label('loc_D84')

    Return()

# id: 0x0004 offset: 0xD85
@scena.Code('func_04_D85')
def func_04_D85():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DA8',
    )

    OP_8D(0x00FE, 17510, 71160, 14830, 73220, 3000)

    Jump('func_04_D85')

    def _loc_DA8(): pass

    label('loc_DA8')

    Return()

# id: 0x0005 offset: 0xDA9
@scena.Code('func_05_DA9')
def func_05_DA9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_DCC',
    )

    OP_8D(0x00FE, 11460, 51180, 8590, 67130, 3000)

    Jump('func_05_DA9')

    def _loc_DCC(): pass

    label('loc_DCC')

    Return()

# id: 0x0006 offset: 0xDCD
@scena.Code('func_06_DCD')
def func_06_DCD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E31',
    )

    ChrWalkTo(0x00FE, 38920, 0, 69150, 3500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    Sleep(1500)

    OP_63(0x000D)
    ChrWalkTo(0x00FE, 35280, 0, 69150, 3500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x000D, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x000D)

    Jump('func_06_DCD')

    def _loc_E31(): pass

    label('loc_E31')

    Return()

# id: 0x0007 offset: 0xE32
@scena.Code('func_07_E32')
def func_07_E32():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1025',
    )

    OP_4A(0x0013, 255)
    OP_4A(0x0010, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_E81',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '这就开始校正时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101A')

    def _loc_E81(): pass

    label('loc_E81')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x0010,
        (
            '抱歉，在你正忙的时候麻烦你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，\n',
            '其实我也没什么忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正我也就是个\n',
            '落后于时代的技师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '你在说什么呀。\n',
            '你要知道自己是参与了\n',
            '『埃尔赛尤号』建造的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '明明参与了\n',
            '世上最新的高速飞艇的建造工作，\n',
            '却还常说跟不上时代什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
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

    def _loc_101A(): pass

    label('loc_101A')

    OP_4B(0x0013, 255)
    OP_4B(0x0010, 255)

    Jump('loc_1105')

    def _loc_1025(): pass

    label('loc_1025')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1105',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_108E',
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

    Jump('loc_1105')

    def _loc_108E(): pass

    label('loc_108E')

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

    def _loc_1105(): pass

    label('loc_1105')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1109
@scena.Code('func_08_1109')
def func_08_1109():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_13F1',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_138E',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

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
            '寻找结晶回路碎片的那个孩子啊。',
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
            '老妈说要用那些米拉\n',
            '买些导力器回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，老妈也开始知道\n',
            '什么东西才是有价值的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F怎么样都好啦。\n',
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

    Jump('loc_13F1')

    def _loc_138E(): pass

    label('loc_138E')

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

    def _loc_13F1(): pass

    label('loc_13F1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x13F5
@scena.Code('func_09_13F5')
def func_09_13F5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_150C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_145D',
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

    Jump('loc_150C')

    def _loc_145D(): pass

    label('loc_145D')

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

    def _loc_150C(): pass

    label('loc_150C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1510
@scena.Code('func_0A_1510')
def func_0A_1510():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1624',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_1597',
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

    Jump('loc_1621')

    def _loc_1597(): pass

    label('loc_1597')

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

    def _loc_1621(): pass

    label('loc_1621')

    Jump('loc_1B6A')

    def _loc_1624(): pass

    label('loc_1624')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1696',
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

    Jump('loc_1B6A')

    def _loc_1696(): pass

    label('loc_1696')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1719',
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

    Jump('loc_1B6A')

    def _loc_1719(): pass

    label('loc_1719')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1753',
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

    Jump('loc_1B6A')

    def _loc_1753(): pass

    label('loc_1753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_188B',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_1801',
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

    Jump('loc_1888')

    def _loc_1801(): pass

    label('loc_1801')

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

    def _loc_1888(): pass

    label('loc_1888')

    Jump('loc_1B6A')

    def _loc_188B(): pass

    label('loc_188B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_19CC',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_192D',
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

    Jump('loc_19C9')

    def _loc_192D(): pass

    label('loc_192D')

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

    def _loc_19C9(): pass

    label('loc_19C9')

    Jump('loc_1B6A')

    def _loc_19CC(): pass

    label('loc_19CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1A48',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

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

    Jump('loc_1B6A')

    def _loc_1A48(): pass

    label('loc_1A48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1B6A',
    )

    If(
        (
            (Expr.PushLong, 0x7),
            Expr.Return,
        ),
        'loc_1A96',
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

    Jump('loc_1B6A')

    def _loc_1A96(): pass

    label('loc_1A96')

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

    def _loc_1B6A(): pass

    label('loc_1B6A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1B6E
@scena.Code('func_0B_1B6E')
def func_0B_1B6E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1BC9',
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

    Jump('loc_2174')

    def _loc_1BC9(): pass

    label('loc_1BC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1C53',
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

    Jump('loc_2174')

    def _loc_1C53(): pass

    label('loc_1C53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1E43',
    )

    OP_4A(0x0013, 255)
    OP_4A(0x0010, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1C9F',
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

    Jump('loc_1E38')

    def _loc_1C9F(): pass

    label('loc_1C9F')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
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

    def _loc_1E38(): pass

    label('loc_1E38')

    OP_4B(0x0013, 255)
    OP_4B(0x0010, 255)

    Jump('loc_2174')

    def _loc_1E43(): pass

    label('loc_1E43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1E6F',
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

    Jump('loc_2174')

    def _loc_1E6F(): pass

    label('loc_1E6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1F54',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1EE0',
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

    Jump('loc_1F51')

    def _loc_1EE0(): pass

    label('loc_1EE0')

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

    def _loc_1F51(): pass

    label('loc_1F51')

    Jump('loc_2174')

    def _loc_1F54(): pass

    label('loc_1F54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_200E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1FCD',
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

    Jump('loc_200B')

    def _loc_1FCD(): pass

    label('loc_1FCD')

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

    def _loc_200B(): pass

    label('loc_200B')

    Jump('loc_2174')

    def _loc_200E(): pass

    label('loc_200E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2174',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_20A2',
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

    Jump('loc_2174')

    def _loc_20A2(): pass

    label('loc_20A2')

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

    def _loc_2174(): pass

    label('loc_2174')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2178
@scena.Code('func_0C_2178')
def func_0C_2178():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2228',
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

    Jump('loc_25AC')

    def _loc_2228(): pass

    label('loc_2228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_22FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2299',
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

    Jump('loc_22FA')

    def _loc_2299(): pass

    label('loc_2299')

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

    def _loc_22FA(): pass

    label('loc_22FA')

    Jump('loc_25AC')

    def _loc_22FD(): pass

    label('loc_22FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2353',
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

    Jump('loc_25AC')

    def _loc_2353(): pass

    label('loc_2353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_23AB',
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

    Jump('loc_25AC')

    def _loc_23AB(): pass

    label('loc_23AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_24C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_245A',
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

    Jump('loc_24C5')

    def _loc_245A(): pass

    label('loc_245A')

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

    def _loc_24C5(): pass

    label('loc_24C5')

    Jump('loc_25AC')

    def _loc_24C8(): pass

    label('loc_24C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_25AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_253B',
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

    Jump('loc_25AC')

    def _loc_253B(): pass

    label('loc_253B')

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

    def _loc_25AC(): pass

    label('loc_25AC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x25B0
@scena.Code('func_0D_25B0')
def func_0D_25B0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2697',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2622',
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

    Jump('loc_2694')

    def _loc_2622(): pass

    label('loc_2622')

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

    def _loc_2694(): pass

    label('loc_2694')

    Jump('loc_2A72')

    def _loc_2697(): pass

    label('loc_2697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2773',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2702',
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

    Jump('loc_2770')

    def _loc_2702(): pass

    label('loc_2702')

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

    def _loc_2770(): pass

    label('loc_2770')

    Jump('loc_2A72')

    def _loc_2773(): pass

    label('loc_2773')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_28A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_281B',
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

    Jump('loc_28A6')

    def _loc_281B(): pass

    label('loc_281B')

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

    def _loc_28A6(): pass

    label('loc_28A6')

    Jump('loc_2A72')

    def _loc_28A9(): pass

    label('loc_28A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_298F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2928',
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
            '就像文字上写的那样，\n',
            '一直在这里那里的到处跑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_298C')

    def _loc_2928(): pass

    label('loc_2928')

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

    def _loc_298C(): pass

    label('loc_298C')

    Jump('loc_2A72')

    def _loc_298F(): pass

    label('loc_298F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2A72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_29FE',
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

    Jump('loc_2A72')

    def _loc_29FE(): pass

    label('loc_29FE')

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

    def _loc_2A72(): pass

    label('loc_2A72')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2A76
@scena.Code('func_0E_2A76')
def func_0E_2A76():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2A98',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么了？那股烟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A98(): pass

    label('loc_2A98')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2A9C
@scena.Code('func_0F_2A9C')
def func_0F_2A9C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2B37',
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

    Jump('loc_2C80')

    def _loc_2B37(): pass

    label('loc_2B37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2B59',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不是火灾吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C80')

    def _loc_2B59(): pass

    label('loc_2B59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2BC3',
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

    Jump('loc_2C80')

    def _loc_2BC3(): pass

    label('loc_2BC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2C80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2C27',
    )

    ChrTurnDirection(0x0009, 0x000B, 0)

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

    Jump('loc_2C80')

    def _loc_2C27(): pass

    label('loc_2C27')

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

    def _loc_2C80(): pass

    label('loc_2C80')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2C84
@scena.Code('func_10_2C84')
def func_10_2C84():
    TalkBegin(0x00FE)

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
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2D0A
@scena.Code('func_11_2D0A')
def func_11_2D0A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2E52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2DA0',
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

    Jump('loc_2E4F')

    def _loc_2DA0(): pass

    label('loc_2DA0')

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

    def _loc_2E4F(): pass

    label('loc_2E4F')

    Jump('loc_30E6')

    def _loc_2E52(): pass

    label('loc_2E52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2EB0',
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

    Jump('loc_30E6')

    def _loc_2EB0(): pass

    label('loc_2EB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3009',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2F74',
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

    Jump('loc_3006')

    def _loc_2F74(): pass

    label('loc_2F74')

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

    def _loc_3006(): pass

    label('loc_3006')

    Jump('loc_30E6')

    def _loc_3009(): pass

    label('loc_3009')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_30E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3058',
    )

    ChrTurnDirection(0x00FE, 0x0009, 0)

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

    Jump('loc_30E6')

    def _loc_3058(): pass

    label('loc_3058')

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

    def _loc_30E6(): pass

    label('loc_30E6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x30EA
@scena.Code('func_12_30EA')
def func_12_30EA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_31D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_317D',
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

    Jump('loc_31D0')

    def _loc_317D(): pass

    label('loc_317D')

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

    def _loc_31D0(): pass

    label('loc_31D0')

    Jump('loc_3262')

    def _loc_31D3(): pass

    label('loc_31D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3262',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_322B',
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

    Jump('loc_3262')

    def _loc_322B(): pass

    label('loc_322B')

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

    def _loc_3262(): pass

    label('loc_3262')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3266
@scena.Code('func_13_3266')
def func_13_3266():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_33D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_332C',
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

    Jump('loc_33CD')

    def _loc_332C(): pass

    label('loc_332C')

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
    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    def _loc_33CD(): pass

    label('loc_33CD')

    Jump('loc_39F0')

    def _loc_33D0(): pass

    label('loc_33D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_349E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_342F',
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

    Jump('loc_349B')

    def _loc_342F(): pass

    label('loc_342F')

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

    def _loc_349B(): pass

    label('loc_349B')

    Jump('loc_39F0')

    def _loc_349E(): pass

    label('loc_349E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3565',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3517',
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

    Jump('loc_3562')

    def _loc_3517(): pass

    label('loc_3517')

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
    ClearChrFlags(0x00FE, 0x0010)

    def _loc_3562(): pass

    label('loc_3562')

    Jump('loc_39F0')

    def _loc_3565(): pass

    label('loc_3565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_370C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_35BE',
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

    Jump('loc_3709')

    def _loc_35BE(): pass

    label('loc_35BE')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x000D, 0x0107, 400)

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
            '哎呀，昨天吓死人了。',
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
    ChrTurnDirection(0x0107, 0x000D, 400)
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#061F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是、是呀，全都停了，\n',
            '真是吓了一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '果然城里的导力全都停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我往窗外一看，\n',
            '城里漆黑一片，吓死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有了导力灯，\n',
            '夜晚竟然那么黑暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F是、是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3709(): pass

    label('loc_3709')

    Jump('loc_39F0')

    def _loc_370C(): pass

    label('loc_370C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3949',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_376D',
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

    Jump('loc_3946')

    def _loc_376D(): pass

    label('loc_376D')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_63(0x000D)

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我都已经很注重商品的摆放了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么整体的协调感\n',
            '还是这么差呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0107, 400)

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
            '你今天也要去工房帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F嗯，是啊。',
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
            '因为爸爸他\n',
            '对这方面很不在行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊，那些东西摆放得这么漂亮，\n',
            '原来都是库诺你的功劳啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，还好啦。',
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
            '#061F嗯，再见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过你要乖乖地\n',
            '完成作业才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3946(): pass

    label('loc_3946')

    Jump('loc_39F0')

    def _loc_3949(): pass

    label('loc_3949')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_39F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3993',
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

    Jump('loc_39F0')

    def _loc_3993(): pass

    label('loc_3993')

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

    def _loc_39F0(): pass

    label('loc_39F0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x39F4
@scena.Code('func_14_39F4')
def func_14_39F4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3A38',
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

    Jump('loc_3AC2')

    def _loc_3A38(): pass

    label('loc_3A38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3AC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3A97',
    )

    SetChrDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '导力引擎，开动！\n',
            '将苹果抓住！',
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

    Jump('loc_3AC2')

    def _loc_3A97(): pass

    label('loc_3A97')

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

    def _loc_3AC2(): pass

    label('loc_3AC2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x3AC6
@scena.Code('func_15_3AC6')
def func_15_3AC6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B31',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100280V#010F首先我们要去飞艇坪去把票退掉。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100281V然后我们再出发。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_3B31(): pass

    label('loc_3B31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CFB',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C06',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100172V#006F这边是街道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100173V#502F嘿嘿⊙\n',
            '这次不用再走路了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100174V#010F嗯，\n',
            '总觉得很不习惯呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100175V那么，去飞艇坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100176V#001F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF4')

    def _loc_3C06(): pass

    label('loc_3C06')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C44',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100177V#010F艾丝蒂尔，去飞艇坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF4')

    def _loc_3C44(): pass

    label('loc_3C44')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100178V#010F这边是街道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100179V虽然时间比较充裕，\n',
            '不过还是不要跑得太远吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100180V#007F嗯，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100181V好不容易有次空中旅行，\n',
            '绝对不能错过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CF4(): pass

    label('loc_3CF4')

    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_3CFB(): pass

    label('loc_3CFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3EEC',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D9F',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0101,
        (
            '#0010071051V#000F啊，\n',
            '总之现在要先回协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071052V在没有情报的情况下\n',
            '是不能随便行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071053V#010F是啊。\n',
            '赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DF6')

    def _loc_3D9F(): pass

    label('loc_3D9F')

    ChrTalk(
        0x0101,
        (
            '#0010071054V#000F总之，\n',
            '现在要先回协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071055V在没有情报的情况下\n',
            '是不能随便行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DF6(): pass

    label('loc_3DF6')

    Jump('loc_3EE5')

    def _loc_3DF9(): pass

    label('loc_3DF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E84',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071056V#010F总之现在先回协会\n',
            '听听雾香姐怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071057V说不定能发现什么有价值的线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071058V#000F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EE5')

    def _loc_3E84(): pass

    label('loc_3E84')

    ChrTalk(
        0x0102,
        (
            '#0020071059V#010F总之现在先回协会\n',
            '听听雾香姐怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071060V说不定能发现什么有价值的线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EE5(): pass

    label('loc_3EE5')

    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_3EEC(): pass

    label('loc_3EEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4002',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FA3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F5E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050071061V#050F嘁……\n',
            '现在再追也不会有线索的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050071062V总之先回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FA0')

    def _loc_3F5E(): pass

    label('loc_3F5E')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050071063V#050F喂，你们去哪儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050071064V赶快回协会去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FA0(): pass

    label('loc_3FA0')

    Jump('loc_3FFB')

    def _loc_3FA3(): pass

    label('loc_3FA3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FB9',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_3FC0')

    def _loc_3FB9(): pass

    label('loc_3FB9')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_3FC0(): pass

    label('loc_3FC0')

    ChrTalk(
        0x0106,
        (
            '#0050071065V#050F往那边追也不会有线索的。\n',
            '总之先回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3FFB(): pass

    label('loc_3FFB')

    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_4002(): pass

    label('loc_4002')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4102',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_405E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071066V#002F啊，这边是街道……\n',
            '要快点赶到中央工房才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40FB')

    def _loc_405E(): pass

    label('loc_405E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40B8',
    )

    ChrTalk(
        0x0102,
        (
            '#0020071067V#012F中央工房的样子看起来有点怪……\n',
            '我们最好还是快点过去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40FB')

    def _loc_40B8(): pass

    label('loc_40B8')

    ChrTalk(
        0x0107,
        (
            '#0070071068V#062F中央工房似乎发生了什么事……\n',
            '快点过去看看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40FB(): pass

    label('loc_40FB')

    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_4102(): pass

    label('loc_4102')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4239',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41D0',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071069V#010F博士要的东西还没有送过去呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071070V……委托的事情，\n',
            '你有没有好好记下来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071071V#009F真、真讨厌～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071072V这不是清清楚楚地记下来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4232')

    def _loc_41D0(): pass

    label('loc_41D0')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071073V#010F博士要的东西还没有送过去呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071074V总之现在要帮忙工作机械的改造。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4232(): pass

    label('loc_4232')

    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_4239(): pass

    label('loc_4239')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_42B0',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_425D',
    )

    ChrTurnDirection(0x0107, 0x0001, 400)

    Jump('loc_4264')

    def _loc_425D(): pass

    label('loc_425D')

    ChrTurnDirection(0x0107, 0x0000, 400)

    def _loc_4264(): pass

    label('loc_4264')

    ChrTalk(
        0x0107,
        (
            '#0070071075V#060F那个，这边是街道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071076V中央工房在城里的北边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_42B0(): pass

    label('loc_42B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_433D',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42D4',
    )

    ChrTurnDirection(0x0107, 0x0001, 400)

    Jump('loc_42DB')

    def _loc_42D4(): pass

    label('loc_42D4')

    ChrTurnDirection(0x0107, 0x0000, 400)

    def _loc_42DB(): pass

    label('loc_42DB')

    ChrTalk(
        0x0107,
        (
            '#0070071077V#060F啊，从这里出去\n',
            '就是通往王都的街道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071078V我家是在城里的西南边呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0017)

    Jump('loc_4454')

    def _loc_433D(): pass

    label('loc_433D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 3, 0x50B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 4, 0x50C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4454',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43E9',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071079V#010F在出城之前， \n',
            '先到游击士协会打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071080V有很多事情需要商量一下呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071081V#000F嗯，那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4450')

    def _loc_43E9(): pass

    label('loc_43E9')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071082V#010F在出城之前， \n',
            '先到游击士协会打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071083V有很多事情需要商量一下呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4450(): pass

    label('loc_4450')

    Call(0, 0x0017)

    def _loc_4454(): pass

    label('loc_4454')

    Return()

# id: 0x0016 offset: 0x4455
@scena.Code('func_16_4455')
def func_16_4455():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44C0',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100280V#010F首先我们要去飞艇坪去把票退掉。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100281V然后我们再出发。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_44C0(): pass

    label('loc_44C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_468C',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4595',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100182V#006F这边是街道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100173V#502F嘿嘿⊙\n',
            '这次不用再走路了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100174V#010F嗯，\n',
            '总觉得很不习惯呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100175V那么，去飞艇坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100176V#001F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4685')

    def _loc_4595(): pass

    label('loc_4595')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45D3',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100177V#010F艾丝蒂尔，去飞艇坪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4685')

    def _loc_45D3(): pass

    label('loc_45D3')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100188V#010F这边是平原道哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100179V虽然时间比较充裕，\n',
            '不过还是不要跑得太远吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100180V#007F嗯，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100181V好不容易有次空中旅行，\n',
            '绝对不能错过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4685(): pass

    label('loc_4685')

    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_468C(): pass

    label('loc_468C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_487E',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4757',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071084V#017F艾丝蒂尔，方向不对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071085V去雷斯顿要塞的话，\n',
            '要从城东门出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071086V#004F呀？\n',
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071087V#018F……真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47B8')

    def _loc_4757(): pass

    label('loc_4757')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071088V#017F去雷斯顿要塞的话，\n',
            '要从城东门出去才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071089V你刚才不是记下来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47B8(): pass

    label('loc_47B8')

    Jump('loc_4877')

    def _loc_47BB(): pass

    label('loc_47BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_481F',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071090V#012F这边是托兰特平原道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071091V去雷斯顿要塞的话，\n',
            '要从城东门出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4877')

    def _loc_481F(): pass

    label('loc_481F')

    ChrTalk(
        0x0102,
        (
            '#0020071092V#012F这边是托兰特平原道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071093V去雷斯顿要塞的话，\n',
            '要从城东门出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4877(): pass

    label('loc_4877')

    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_487E(): pass

    label('loc_487E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A6F',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_497C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4922',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0101,
        (
            '#0010071094V#000F啊，\n',
            '总之现在要先回协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071095V在没有情报的情况下\n',
            '是不能随便行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071096V#010F是啊。\n',
            '赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4979')

    def _loc_4922(): pass

    label('loc_4922')

    ChrTalk(
        0x0101,
        (
            '#0010071097V#000F总之，\n',
            '现在要先回协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071098V在没有情报的情况下\n',
            '是不能随便行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4979(): pass

    label('loc_4979')

    Jump('loc_4A68')

    def _loc_497C(): pass

    label('loc_497C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A07',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071099V#010F总之现在先回协会\n',
            '听听雾香姐怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071100V说不定能发现什么有价值的线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071101V#000F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A68')

    def _loc_4A07(): pass

    label('loc_4A07')

    ChrTalk(
        0x0102,
        (
            '#0020071102V#010F总之现在先回协会\n',
            '听听雾香姐怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071103V说不定能发现什么有价值的线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A68(): pass

    label('loc_4A68')

    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_4A6F(): pass

    label('loc_4A6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B85',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B26',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AE1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050071104V#050F嘁……\n',
            '现在再追也不会有线索的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050071105V总之先回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B23')

    def _loc_4AE1(): pass

    label('loc_4AE1')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050071106V#050F喂，你们去哪儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050071107V赶快回协会去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B23(): pass

    label('loc_4B23')

    Jump('loc_4B7E')

    def _loc_4B26(): pass

    label('loc_4B26')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B3C',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_4B43')

    def _loc_4B3C(): pass

    label('loc_4B3C')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_4B43(): pass

    label('loc_4B43')

    ChrTalk(
        0x0106,
        (
            '#0050071108V#050F往那边追也不会有线索的。\n',
            '总之先回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4B7E(): pass

    label('loc_4B7E')

    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_4B85(): pass

    label('loc_4B85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 3, 0x52B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C85',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BE1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071109V#002F啊，这边是街道……\n',
            '要快点赶到中央工房才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C7E')

    def _loc_4BE1(): pass

    label('loc_4BE1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C3B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020071110V#012F中央工房的样子看起来有点怪……\n',
            '我们最好还是快点过去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C7E')

    def _loc_4C3B(): pass

    label('loc_4C3B')

    ChrTalk(
        0x0107,
        (
            '#0070071111V#062F中央工房似乎发生了什么事……\n',
            '快点过去看看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C7E(): pass

    label('loc_4C7E')

    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_4C85(): pass

    label('loc_4C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DBC',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D53',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071112V#010F博士要的东西还没有送过去呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071113V……委托的事情，\n',
            '你有没有好好记下来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071114V#009F真、真讨厌～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071115V这不是清清楚楚地记下来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DB5')

    def _loc_4D53(): pass

    label('loc_4D53')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071116V#010F博士要的东西还没有送过去呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071117V总之现在要帮忙工作机械的改造。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DB5(): pass

    label('loc_4DB5')

    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_4DBC(): pass

    label('loc_4DBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E33',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DE0',
    )

    ChrTurnDirection(0x0107, 0x0001, 400)

    Jump('loc_4DE7')

    def _loc_4DE0(): pass

    label('loc_4DE0')

    ChrTurnDirection(0x0107, 0x0000, 400)

    def _loc_4DE7(): pass

    label('loc_4DE7')

    ChrTalk(
        0x0107,
        (
            '#0070071118V#060F啊，这边是平原道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071119V中央工房在城里的北边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_4E33(): pass

    label('loc_4E33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EAF',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E57',
    )

    ChrTurnDirection(0x0107, 0x0001, 400)

    Jump('loc_4E5E')

    def _loc_4E57(): pass

    label('loc_4E57')

    ChrTurnDirection(0x0107, 0x0000, 400)

    def _loc_4E5E(): pass

    label('loc_4E5E')

    ChrTalk(
        0x0107,
        (
            '#0070071120V#060F啊，\n',
            '从这里出去就是平原道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071121V我的家就在这西边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0018)

    Jump('loc_4FC6')

    def _loc_4EAF(): pass

    label('loc_4EAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 3, 0x50B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 4, 0x50C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4FC6',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F5B',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x0102,
        (
            '#0020071122V#010F在出城之前， \n',
            '先到游击士协会打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071123V有很多事情需要商量一下呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071124V#000F嗯，那就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4FC2')

    def _loc_4F5B(): pass

    label('loc_4F5B')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071125V#010F在出城之前， \n',
            '先到游击士协会打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071126V有很多事情需要商量一下呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FC2(): pass

    label('loc_4FC2')

    Call(0, 0x0018)

    def _loc_4FC6(): pass

    label('loc_4FC6')

    Return()

# id: 0x0017 offset: 0x4FC7
@scena.Code('func_17_4FC7')
def func_17_4FC7():
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0018 offset: 0x4FE3
@scena.Code('func_18_4FE3')
def func_18_4FE3():
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0019 offset: 0x4FFF
@scena.Code('func_19_4FFF')
def func_19_4FFF():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_67(0, 5600, -10000, 0)
    CameraMove(58400, 3900, 51600, 0)
    CameraSetDistance(4700, 0)
    OP_6C(276000, 0)

    @scena.Lambda('lambda_5040')
    def lambda_5040():
        CameraMove(57400, 3900, 23700, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5040)

    OP_6C(204000, 6000)

    @scena.Lambda('lambda_5061')
    def lambda_5061():
        CameraSetDistance(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5061)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T3133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x5088
@scena.Code('func_1A_5088')
def func_1A_5088():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(60080, 0, 26320, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 60090, 0, 27140, 180)
    SetChrPos(0x0102, 60590, 0, 25950, 315)
    SetChrPos(0x0107, 59500, 0, 26070, 0)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010071044V#001F嘿嘿～\n',
            '美味的早饭已经享用完了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071045V我们这就去中央工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071046V#010F在此之前，\n',
            '我们先回游击士协会一趟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071047V为了慎重起见，\n',
            '还是向雾香小姐报告昨天的事比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071048V#006F啊，也对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071049V提妲，\n',
            '稍微绕个道好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071050V#061F#2P好的，当然可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    ClearMapFlags(0x10000000)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0x523C
@scena.Code('func_1B_523C')
def func_1B_523C():
    EventBegin(0x00)
    CameraMove(66850, 0, 53050, 0)
    OP_6C(270000, 0)
    SetChrPos(0x0101, 66140, 0, 53000, 270)
    SetChrPos(0x0107, 66790, 0, 52290, 270)
    SetChrPos(0x0102, 66830, 0, 53720, 270)
    SetChrPos(0x0110, 67900, 0, 52960, 270)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010080672V#004F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080673V#064F怎么了？\n',
            '艾丝蒂尔姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080674V#505F可能是我的心理作用吧，\n',
            '总觉得好像有什么骚动似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 315, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020080675V#012F……不是心理作用，\n',
            '我听到远处的确有嘈杂声。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080676V是中央工房的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_53D2')
    def lambda_53D2():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_53D2)

    @scena.Lambda('lambda_53E0')
    def lambda_53E0():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53E0)

    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080677V#065F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080678V#154F咦咦，怎么回事～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080679V#002F不知道……\n',
            '我们最好快点过去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(13)
    EventEnd(0x00)

    Return()

# id: 0x001C offset: 0x5467
@scena.Code('func_1C_5467')
def func_1C_5467():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 2, 0x512)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5674',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_55C7',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_551C',
    )

    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071127V#010F提妲，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071128V能不能稍微绕个远路呢？\n',
            '我们想去协会打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070071129V#060F啊，好的。\n',
            '当然可以啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_55C4')

    def _loc_551C(): pass

    label('loc_551C')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071130V#010F虽然会绕个远路，\n',
            '不过还是去协会打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071131V为慎重起见，\n',
            '还是把昨天发生的事报告上去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071132V#000F啊，嗯。\n',
            '这样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_55C4(): pass

    label('loc_55C4')

    Jump('loc_5659')

    def _loc_55C7(): pass

    label('loc_55C7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55DD',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_55E4')

    def _loc_55DD(): pass

    label('loc_55DD')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_55E4(): pass

    label('loc_55E4')

    ChrTalk(
        0x0102,
        (
            '#0020071133V#010F虽然会绕个远路，\n',
            '不过还是去协会打个招呼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071134V为慎重起见，\n',
            '还是把昨天发生的事报告上去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_5659(): pass

    label('loc_5659')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5674(): pass

    label('loc_5674')

    Return()

# id: 0x001D offset: 0x5675
@scena.Code('func_1D_5675')
def func_1D_5675():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '《导力式时钟第１号机》\n',
            '　七耀历１１６２年·蔡斯技术工房制造',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x001E offset: 0x56DB
@scena.Code('func_1E_56DB')
def func_1E_56DB():
    OP_13(0x007D)

    Return()

# id: 0x001F offset: 0x56DF
@scena.Code('func_1F_56DF')
def func_1F_56DF():
    OP_13(0x007F)

    Return()

# id: 0x0020 offset: 0x56E3
@scena.Code('func_20_56E3')
def func_20_56E3():
    OP_13(0x0082)

    Return()

# id: 0x0021 offset: 0x56E7
@scena.Code('func_21_56E7')
def func_21_56E7():
    OP_13(0x007C)

    Return()

# id: 0x0022 offset: 0x56EB
@scena.Code('func_22_56EB')
def func_22_56EB():
    OP_13(0x007A)

    Return()

# id: 0x0023 offset: 0x56EF
@scena.Code('func_23_56EF')
def func_23_56EF():
    OP_13(0x007B)

    Return()

# id: 0x0024 offset: 0x56F3
@scena.Code('func_24_56F3')
def func_24_56F3():
    OP_13(0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
