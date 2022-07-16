import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1304_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1304   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '古兰托机长'),
    TXT(0x02, '特里诺'),
    TXT(0x03, '乘务员卡拉莉丝'),
    TXT(0x04, '波嘉'),
    TXT(0x05, '卡尔托斯'),
    TXT(0x06, '迪蒙'),
    TXT(0x07, '登克'),
    TXT(0x08, '芬尼尔'),
    TXT(0x09, '布拉奥'),
    TXT(0x0A, '普罗梅笛'),
    TXT(0x0B, '莉诺'),
    TXT(0x0C, '雷加洛'),
    TXT(0x0D, '希尔碧'),
    TXT(0x0E, '巴雷尔'),
    TXT(0x0F, '鲁蓓'),
    TXT(0x10, '阿杰'),
    TXT(0x11, '空贼阿伦'),
    TXT(0x12, '空贼洛西'),
    TXT(0x13, '空贼雷古'),
    TXT(0x14, '空贼蒂诺'),
    TXT(0x15, '空贼'),
    TXT(0x16, '空贼'),
    TXT(0x17, '空贼'),
    TXT(0x18, '空贼'),
    TXT(0x19, '空贼'),
    TXT(0x1A, '空贼'),
    TXT(0x1B, '空贼'),
    TXT(0x1C, '空贼'),
    TXT(0x1D, '目标用摄像机'),
    TXT(0x1E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1304.x'
    header.mapIndex       = 52
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x38B6
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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
            word_3A         = 52,
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
        ('ED6_DT07/CH01440._CH', 'ED6_DT07/CH01440P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT07/CH00364._CH', 'ED6_DT07/CH00364P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
        ('ED6_DT07/CH00363._CH', 'ED6_DT07/CH00363P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT06/CH20074._CH', 'ED6_DT06/CH20074P._CP'),
    ]

# id: 0x10002 offset: 0x192
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -51200,
            z                   = 0,
            y                   = -44970,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -44800,
            z                   = 0,
            y                   = -44500,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -49400,
            z                   = 0,
            y                   = -44100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -52870,
            z                   = 0,
            y                   = -45150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -48530,
            z                   = 0,
            y                   = -45460,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -53480,
            z                   = 0,
            y                   = -43740,
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
            x                   = -51250,
            z                   = 0,
            y                   = -43660,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -49800,
            z                   = 0,
            y                   = -41400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -54600,
            z                   = 0,
            y                   = -40800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -56400,
            z                   = 0,
            y                   = -43000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -47800,
            z                   = 0,
            y                   = -42400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -45700,
            z                   = 0,
            y                   = -42960,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -45400,
            z                   = 0,
            y                   = -41900,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -57380,
            z                   = 0,
            y                   = -45290,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -51600,
            z                   = 0,
            y                   = -40500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -52100,
            z                   = 0,
            y                   = -40700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 800,
            z                   = 500,
            y                   = 500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -1000,
            z                   = 500,
            y                   = -2800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2300,
            z                   = 500,
            y                   = -2700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1000,
            z                   = 500,
            y                   = -1900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2300,
            z                   = 500,
            y                   = -2700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1000,
            z                   = 500,
            y                   = -1900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
    )

# id: 0x10003 offset: 0x532
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x532
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x532
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x532
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_540',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0013)

    def _loc_540(): pass

    label('loc_540')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_54E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0014)

    def _loc_54E(): pass

    label('loc_54E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_562'),
        (0x00000066, 'loc_66D'),
        (0x00000065, 'loc_66D'),
        (-1, 'loc_778'),
    )

    def _loc_562(): pass

    label('loc_562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 5, 0x355)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_66A',
    )

    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x0018, 10200, 0, -92518, 225)
    SetChrPos(0x0019, 3520, 0, -93920, 35)
    SetChrPos(0x001C, 2640, 0, -91700, 4)
    SetChrPos(0x001D, 9860, 0, -97730, 260)
    SetChrPos(0x001E, 1950, 0, -97080, 217)
    SetChrPos(0x001F, 2350, 0, -98760, 140)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    SetChrChipByIndex(0x0018, 28)
    SetChrChipByIndex(0x0019, 28)
    SetChrChipByIndex(0x001C, 28)
    SetChrChipByIndex(0x001D, 28)
    SetChrChipByIndex(0x001E, 28)
    SetChrChipByIndex(0x001F, 28)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_66A(): pass

    label('loc_66A')

    Jump('loc_778')

    def _loc_66D(): pass

    label('loc_66D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 6, 0x356)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_775',
    )

    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x0018, -54970, 0, -93490, 315)
    SetChrPos(0x0019, -48920, 0, -91340, 53)
    SetChrPos(0x001C, -45150, 0, -93440, 163)
    SetChrPos(0x001D, -48280, 0, -97510, 119)
    SetChrPos(0x001E, -54960, 0, -97820, 86)
    SetChrPos(0x001F, -53760, 0, -91280, 172)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    SetChrChipByIndex(0x0018, 28)
    SetChrChipByIndex(0x0019, 28)
    SetChrChipByIndex(0x001C, 28)
    SetChrChipByIndex(0x001D, 28)
    SetChrChipByIndex(0x001E, 28)
    SetChrChipByIndex(0x001F, 28)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_775(): pass

    label('loc_775')

    Jump('loc_778')

    def _loc_778(): pass

    label('loc_778')

    Return()

# id: 0x0001 offset: 0x779
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x77A
@scena.Code('ReInit')
def ReInit():
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
        'loc_7AA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_8EC')

    def _loc_7AA(): pass

    label('loc_7AA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C3',
    )

    OP_99(0x00FE, 0x01, 0x07, 1300)

    Jump('loc_8EC')

    def _loc_7C3(): pass

    label('loc_7C3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DC',
    )

    OP_99(0x00FE, 0x02, 0x07, 1250)

    Jump('loc_8EC')

    def _loc_7DC(): pass

    label('loc_7DC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F5',
    )

    OP_99(0x00FE, 0x03, 0x07, 1200)

    Jump('loc_8EC')

    def _loc_7F5(): pass

    label('loc_7F5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80E',
    )

    OP_99(0x00FE, 0x04, 0x07, 1150)

    Jump('loc_8EC')

    def _loc_80E(): pass

    label('loc_80E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_827',
    )

    OP_99(0x00FE, 0x05, 0x07, 1100)

    Jump('loc_8EC')

    def _loc_827(): pass

    label('loc_827')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_840',
    )

    OP_99(0x00FE, 0x06, 0x07, 1050)

    Jump('loc_8EC')

    def _loc_840(): pass

    label('loc_840')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_859',
    )

    OP_99(0x00FE, 0x00, 0x07, 1355)

    Jump('loc_8EC')

    def _loc_859(): pass

    label('loc_859')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_872',
    )

    OP_99(0x00FE, 0x01, 0x07, 1305)

    Jump('loc_8EC')

    def _loc_872(): pass

    label('loc_872')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1255)

    Jump('loc_8EC')

    def _loc_88B(): pass

    label('loc_88B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A4',
    )

    OP_99(0x00FE, 0x03, 0x07, 1205)

    Jump('loc_8EC')

    def _loc_8A4(): pass

    label('loc_8A4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8BD',
    )

    OP_99(0x00FE, 0x04, 0x07, 1155)

    Jump('loc_8EC')

    def _loc_8BD(): pass

    label('loc_8BD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D6',
    )

    OP_99(0x00FE, 0x05, 0x07, 1105)

    Jump('loc_8EC')

    def _loc_8D6(): pass

    label('loc_8D6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8EC',
    )

    OP_99(0x00FE, 0x06, 0x07, 1055)

    def _loc_8EC(): pass

    label('loc_8EC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_901',
    )

    OP_99(0x00FE, 0x00, 0x07, 1200)

    Jump('loc_8EC')

    def _loc_901(): pass

    label('loc_901')

    Return()

# id: 0x0003 offset: 0x902
@scena.Code('func_03_902')
def func_03_902():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_A56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A22',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0101,
        (
            '#006F机长，\n',
            '那些空贼没有逃到这里来吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有，不过我听到外面\n',
            '好像有吵闹声和脚步声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是有人\n',
            '跑到上面去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F艾丝蒂尔，他们果然要坐飞艇逃跑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F嗯，追上去！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F抱歉了，机长。\n',
            '就请你们再稍等片刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，你们也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A53')

    def _loc_A22(): pass

    label('loc_A22')

    ChrTalk(
        0x00FE,
        (
            '那些家伙\n',
            '应该是跑到上面去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A53(): pass

    label('loc_A53')

    Jump('loc_A9A')

    def _loc_A56(): pass

    label('loc_A56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_A9A',
    )

    ChrTalk(
        0x00FE,
        (
            '空贼的头目很可能\n',
            '就在这儿的最底层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A9A(): pass

    label('loc_A9A')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xA9E
@scena.Code('func_04_A9E')
def func_04_A9E():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_B2F',
    )

    ChrTalk(
        0x00FE,
        (
            '我还有不少生意\n',
            '要准备去洽谈呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各～位，无论如何也要坚持下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能回到柏斯，\n',
            '第一件要做的事就是向大家赔礼道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_B2F(): pass

    label('loc_B2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_B84',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到你们竟然能\n',
            '潜入到这种地方来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士也是\n',
            '一个很辛苦的职业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B84(): pass

    label('loc_B84')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xB88
@scena.Code('func_05_B88')
def func_05_B88():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_BD9',
    )

    ChrTalk(
        0x00FE,
        (
            '外面好像\n',
            '还有不少的空贼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们没有尽到\n',
            '保护旅客的职责……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C3C')

    def _loc_BD9(): pass

    label('loc_BD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_C3C',
    )

    ChrTalk(
        0x00FE,
        (
            '能够得到你们的帮助，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有人受伤或者生病，\n',
            '乘务员和乘客都平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C3C(): pass

    label('loc_C3C')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0xC40
@scena.Code('func_06_C40')
def func_06_C40():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_C95',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '游击士还真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '区区几个人\n',
            '就冲入了空贼团的基地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCE')

    def _loc_C95(): pass

    label('loc_C95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_CCE',
    )

    ChrTalk(
        0x00FE,
        (
            '我坚信我们能够获救。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐，谢谢你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCE(): pass

    label('loc_CCE')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0xCD2
@scena.Code('func_07_CD2')
def func_07_CD2():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_DD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D73',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '空贼团的老大\n',
            '实在是太可怕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过空贼团的成员\n',
            '也不是全部都很可恶啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其中也有很亲切的人，\n',
            '无论在哪里都还是有好人的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD3')

    def _loc_D73(): pass

    label('loc_D73')

    ChrTalk(
        0x00FE,
        (
            '空贼团的成员\n',
            '也不是全部都很可恶啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其中也有很亲切的人，\n',
            '无论在哪里都还是有好人的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DD3(): pass

    label('loc_DD3')

    Jump('loc_E26')

    def _loc_DD6(): pass

    label('loc_DD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_E26',
    )

    ChrTalk(
        0x00FE,
        (
            '呀啊，快要受不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个空贼团的老大\n',
            '怎么看都觉得有些不正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E26(): pass

    label('loc_E26')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0xE2A
@scena.Code('func_08_E2A')
def func_08_E2A():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_E60',
    )

    ChrTalk(
        0x00FE,
        (
            '我要尽快把获救的事\n',
            '向飞艇公社报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EDD')

    def _loc_E60(): pass

    label('loc_E60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_EDD',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然得救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我们的『林德号』\n',
            '被弄到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我们被蒙上了眼睛，\n',
            '所以不太清楚当时的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EDD(): pass

    label('loc_EDD')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0xEE1
@scena.Code('func_09_EE1')
def func_09_EE1():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_F4C',
    )

    ChrTalk(
        0x00FE,
        (
            '要是那些家伙现在进来，\n',
            '我一定会狠狠给他们一拳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们是『林德号』的仇敌。\n',
            '不可饶恕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FAD')

    def _loc_F4C(): pass

    label('loc_F4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_FAD',
    )

    ChrTalk(
        0x00FE,
        (
            '那群败类，\n',
            '竟然把我精心维护过的\n',
            '『林德号』的引擎给拆下来带走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对不可饶恕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FAD(): pass

    label('loc_FAD')

    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0xFB1
@scena.Code('func_0A_FB1')
def func_0A_FB1():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_FFB',
    )

    ChrTalk(
        0x00FE,
        (
            '她怎么样了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡特丽亚现在\n',
            '肯定正在担心我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1025')

    def _loc_FFB(): pass

    label('loc_FFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_1025',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '我的店铺现在怎么样了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1025(): pass

    label('loc_1025')

    TalkEnd(0x000F)

    Return()

# id: 0x000B offset: 0x1029
@scena.Code('func_0B_1029')
def func_0B_1029():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_1075',
    )

    ChrTalk(
        0x00FE,
        (
            '本来打算去拜访在洛连特的旧友，\n',
            '可没想到会发生这种事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AF')

    def _loc_1075(): pass

    label('loc_1075')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_10AF',
    )

    ChrTalk(
        0x00FE,
        (
            '哦哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我做梦都在想着\n',
            '能够被救出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10AF(): pass

    label('loc_10AF')

    TalkEnd(0x0010)

    Return()

# id: 0x000C offset: 0x10B3
@scena.Code('func_0C_10B3')
def func_0C_10B3():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_1116',
    )

    ChrTalk(
        0x00FE,
        (
            '我去了王立学院授课，\n',
            '回来的时候乘了定期船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '竟然遇到这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1140')

    def _loc_1116(): pass

    label('loc_1116')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_1140',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，\n',
            '这下终于可以回蔡斯去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1140(): pass

    label('loc_1140')

    TalkEnd(0x0011)

    Return()

# id: 0x000D offset: 0x1144
@scena.Code('func_0D_1144')
def func_0D_1144():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_116D',
    )

    ChrTalk(
        0x00FE,
        (
            '家人肯定很担心我呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A8')

    def _loc_116D(): pass

    label('loc_116D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_11A8',
    )

    ChrTalk(
        0x00FE,
        (
            '谢谢你们，游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下终于可以回家去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A8(): pass

    label('loc_11A8')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x11AC
@scena.Code('func_0E_11AC')
def func_0E_11AC():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_11E0',
    )

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '大家能够平安无事真是万幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_122D')

    def _loc_11E0(): pass

    label('loc_11E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_122D',
    )

    ChrTalk(
        0x00FE,
        (
            '太好了～\n',
            '这下又可以继续旅行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '这回真是被关了好久啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_122D(): pass

    label('loc_122D')

    TalkEnd(0x0013)

    Return()

# id: 0x000F offset: 0x1231
@scena.Code('func_0F_1231')
def func_0F_1231():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_128B',
    )

    ChrTalk(
        0x00FE,
        (
            '要去追击那些空贼吧。\n',
            '虽然帮不上忙，但我会为你们加油的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '加油吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F8')

    def _loc_128B(): pass

    label('loc_128B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_12F8',
    )

    ChrTalk(
        0x00FE,
        (
            '难得我专程赶到柏斯超市去，\n',
            '但是买的东西竟然\n',
            '全部被那些空贼抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士啊，帮我夺回来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F8(): pass

    label('loc_12F8')

    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x12FC
@scena.Code('func_10_12FC')
def func_10_12FC():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_1345',
    )

    ChrTalk(
        0x00FE,
        (
            '现、现在\n',
            '外面还有空贼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快、快点\n',
            '把他们解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_138D')

    def _loc_1345(): pass

    label('loc_1345')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_138D',
    )

    ChrTalk(
        0x00FE,
        (
            '我、我是\n',
            '头一回乘坐定期船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到会遇到这样的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_138D(): pass

    label('loc_138D')

    TalkEnd(0x0015)

    Return()

# id: 0x0011 offset: 0x1391
@scena.Code('func_11_1391')
def func_11_1391():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_13E8',
    )

    ChrTalk(
        0x00FE,
        (
            '那些空贼\n',
            '还给了小孩子面包吃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来他们也并非\n',
            '全部都是坏人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1430')

    def _loc_13E8(): pass

    label('loc_13E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_1430',
    )

    ChrTalk(
        0x00FE,
        (
            '太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与我自己获救相比，\n',
            '孩子能够得救更让我欣慰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1430(): pass

    label('loc_1430')

    TalkEnd(0x0016)

    Return()

# id: 0x0012 offset: 0x1434
@scena.Code('func_12_1434')
def func_12_1434():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Return,
        ),
        'loc_1474',
    )

    ChrTalk(
        0x00FE,
        (
            '那个那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请不要太为难\n',
            '那些叔叔们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B9')

    def _loc_1474(): pass

    label('loc_1474')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_14B9',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐你们\n',
            '是游击士～吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些叔叔们\n',
            '被你们抓住了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14B9(): pass

    label('loc_14B9')

    TalkEnd(0x0017)

    Return()

# id: 0x0013 offset: 0x14BD
@scena.Code('func_13_14BD')
def func_13_14BD():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetMapFlags(0x00400000)
    SetChrPos(0x0101, 4948, 0, -101090, 0)
    SetChrPos(0x0102, 4948, 0, -101090, 0)
    SetChrPos(0x0103, 4948, 0, -101090, 0)
    SetChrPos(0x0104, 4948, 0, -101090, 0)
    SetChrPos(0x0018, 6280, 0, -94290, 270)
    SetChrPos(0x0019, 4610, 0, -94970, 0)
    SetChrPos(0x001C, 9423, 0, -92822, 0)
    SetChrPos(0x001D, 9856, 0, -97201, 90)
    SetChrPos(0x001E, 3340, 0, -93640, 90)
    SetChrPos(0x001F, 88, 0, -97865, 270)
    SetChrFlags(0x0018, 0x0004)
    SetChrFlags(0x0019, 0x0004)
    SetChrFlags(0x001E, 0x0004)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrChipByIndex(0x0101, 20)
    SetChrChipByIndex(0x0102, 22)
    SetChrChipByIndex(0x0103, 24)
    SetChrChipByIndex(0x0104, 26)
    CameraMove(5230, 0, -96500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)
    OP_4A(0x001C, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    OP_4A(0x001F, 255)
    OP_62(0x0018, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0019, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x001C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x001D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x001E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x001F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_16A3')
    def lambda_16A3():
        CameraMove(5440, 0, -94380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_16A3)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_16C0')
    def lambda_16C0():
        ChrWalkTo(0x00FE, 4872, 0, -97679, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16C0)

    Sleep(200)

    ClearChrFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_16E5')
    def lambda_16E5():
        ChrWalkTo(0x00FE, 5681, 0, -97875, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16E5)

    Sleep(200)

    ClearChrFlags(0x0104, 0x0080)

    @scena.Lambda('lambda_170A')
    def lambda_170A():
        ChrWalkTo(0x00FE, 6313, 0, -98593, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_170A)

    Sleep(200)

    ClearChrFlags(0x0103, 0x0080)

    @scena.Lambda('lambda_172F')
    def lambda_172F():
        ChrWalkTo(0x00FE, 3993, 0, -98750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_172F)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0103, 0x0001)

    @scena.Lambda('lambda_175E')
    def lambda_175E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_175E)

    @scena.Lambda('lambda_176C')
    def lambda_176C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_176C)

    @scena.Lambda('lambda_177A')
    def lambda_177A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_177A)

    @scena.Lambda('lambda_1788')
    def lambda_1788():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_1788)

    @scena.Lambda('lambda_1796')
    def lambda_1796():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_1796)

    @scena.Lambda('lambda_17A4')
    def lambda_17A4():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_17A4)

    WaitForThreadExit(0x0018, 0x0001)

    ChrTalk(
        0x0018,
        (
            '#1250031412V啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031413V你们几个，是新来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031414V#007F你说呢……\n',
            '怎么想也不可能吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031415V真是没有紧张感的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1260031416V#1P哎，可是……\n',
            '除了新来的还能是什么人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#1260031417V#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031418V……难、难道是入侵者？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(166, 0x00, 0x64)

    ChrTalk(
        0x0104,
        (
            '#0040031419V#031FＢｉｎｇｏ㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031420V#012F我们是游击士协会的。\n',
            '请你们马上放下武器投降吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0019, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0018, 15)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0019, 15)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x001C, 15)
    Sleep(100)

    SetChrChipByIndex(0x001D, 15)
    Sleep(75)

    SetChrChipByIndex(0x001E, 15)
    Sleep(50)

    SetChrChipByIndex(0x001F, 15)

    ChrTalk(
        0x0019,
        (
            '#1260031421V#1P开、开什么玩笑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031422V干掉他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0018, 0x0004)

    @scena.Lambda('lambda_1A14')
    def lambda_1A14():
        CameraMove(5230, 0, -96500, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A14)

    SetChrChipByIndex(0x0019, 17)

    @scena.Lambda('lambda_1A31')
    def lambda_1A31():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1A31)

    SetChrChipByIndex(0x001C, 17)

    @scena.Lambda('lambda_1A4B')
    def lambda_1A4B():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_1A4B)

    SetChrChipByIndex(0x001D, 17)

    @scena.Lambda('lambda_1A65')
    def lambda_1A65():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_1A65)

    SetChrChipByIndex(0x001E, 17)

    @scena.Lambda('lambda_1A7F')
    def lambda_1A7F():
        OP_92(0x00FE, 0x0101, 1000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_1A7F)

    SetChrChipByIndex(0x001F, 17)

    @scena.Lambda('lambda_1A99')
    def lambda_1A99():
        OP_92(0x00FE, 0x0101, 1000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1A99)

    Sleep(250)

    SetChrChipByIndex(0x0018, 17)

    @scena.Lambda('lambda_1AB8')
    def lambda_1AB8():
        ChrJumpTo(0x0018, 5848, 0, -97073, 1500, 6000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1AB8)

    Sleep(400)

    Battle(0x0000038A, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1AEE'),
        (-1, 'loc_1AF1'),
    )

    def _loc_1AEE(): pass

    label('loc_1AEE')

    OP_B4(0x00)

    Return()

    def _loc_1AF1(): pass

    label('loc_1AF1')

    EventBegin(0x00)
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrPos(0x0101, 5750, 0, -97780, 39)
    SetChrPos(0x0102, 6780, 0, -98300, 4)
    SetChrPos(0x0103, 4320, 0, -97780, 72)
    SetChrPos(0x0104, 4700, 0, -96480, 85)
    SetChrPos(0x0019, 3520, 0, -93920, 35)
    SetChrPos(0x001C, 2640, 0, -91700, 4)
    SetChrPos(0x001D, 9860, 0, -97730, 260)
    SetChrPos(0x001E, 1950, 0, -97080, 217)
    SetChrPos(0x001F, 2350, 0, -98760, 140)
    SetChrPos(0x0018, 6511, 0, -96547, 0)
    ChrTurnDirection(0x0019, 0x0101, 0)
    ChrTurnDirection(0x0018, 0x0101, 0)
    ChrTurnDirection(0x001C, 0x0101, 0)
    ChrTurnDirection(0x001D, 0x0101, 0)
    SetChrChipByIndex(0x0018, 16)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    SetChrChipByIndex(0x0019, 28)
    SetChrChipByIndex(0x001C, 28)
    SetChrChipByIndex(0x001D, 28)
    SetChrChipByIndex(0x001E, 28)
    SetChrChipByIndex(0x001F, 28)

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTurnDirection(0x0101, 0x0018, 0)
    ChrTurnDirection(0x0102, 0x0018, 0)
    ChrTurnDirection(0x0104, 0x0018, 0)
    ChrTurnDirection(0x0103, 0x0018, 0)
    CameraMove(6280, 0, -96740, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(1000)

    ChrTalk(
        0x0018,
        (
            '#1250031423V呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031424V#005F说！\n',
            '人质在哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031425V不老实交代的话，\n',
            '有你好受的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031426V要、要杀要剐随你的便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031427V白痴才会告诉你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031428V#027F啊，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031429V艾丝蒂尔，你先退下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031430V#004F啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DB4')
    def lambda_1DB4():
        ChrWalkTo(0x00FE, 5430, 0, -98610, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DB4)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1DD4')
    def lambda_1DD4():
        CameraMove(6700, 0, -96370, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1DD4)

    @scena.Lambda('lambda_1DEC')
    def lambda_1DEC():
        OP_92(0x0103, 0x0018, 1000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1DEC)

    SetChrDirection(0x0101, 22, 400)
    WaitForThreadExit(0x0103, 0x0001)
    SetChrChipByIndex(0x0103, 24)
    Sleep(1000)

    TerminateThread(0x0103, 0xFF)
    SetChrChipByIndex(0x0103, 19)
    PlaySE(502, 0x00, 0x64)

    @scena.Lambda('lambda_1E25')
    def lambda_1E25():
        OP_99(0x0103, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E25)

    Sleep(200)

    SetChrFlags(0x0018, 0x0020)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(521, 0x00, 0x64)
    PlayEffect(0x12, 0x00, 0x0018, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x0018, 0x0020)
    ChrTurnDirection(0x0018, 0x0103, 0)
    ChrMoveTo(0x0018, 8271, 0, -94711, 8000, 0x00)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    StopEffect(0x00, 0x02)

    ChrTalk(
        0x0018,
        (
            '#1250031431V哎呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031432V#027F#3P呵呵，我可是手下留情了哦，\n',
            '不会那么简单就让你晕过去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031433V老实交代的话，\n',
            '倒是可以让你好好睡上一觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031434V呀呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031435V就在下面的楼层！\n',
            '有我们的兄弟在把守着！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031436V#020F#3P真是乖孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031437V那么你们的首领\n',
            '吉尔和乔丝特又在哪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031438V别、别太过分了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1250031439V大白痴才会告诉你这个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031440V#020F#3P呼，先不说人质，\n',
            '不出卖首领这一点的确算是有骨气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031441V#021F没办法，那就先说声抱歉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    SetChrFlags(0x0103, 0x0020)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_20A4')
    def lambda_20A4():
        CameraMove(8010, 0, -95060, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20A4)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_20C1')
    def lambda_20C1():
        ChrJumpTo(0x0103, 7648, 0, -95333, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20C1)

    Sleep(500)

    PlaySE(502, 0x00, 0x64)

    @scena.Lambda('lambda_20E9')
    def lambda_20E9():
        OP_99(0x0103, 0x01, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20E9)

    Sleep(200)

    SetChrFlags(0x0018, 0x0020)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0018, 18)
    SetChrFlags(0x0018, 0x0004)
    SetChrFlags(0x0018, 0x0020)
    ChrTurnDirection(0x0018, 0x0103, 0)
    PlaySE(521, 0x00, 0x64)
    ChrMoveTo(0x0018, 10200, 1000, -92518, 15000, 0x00)
    PlayEffect(0x12, 0xFF, 0x0018, 0, 0, -500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(142, 0x00, 0x64)
    CameraSetDistance(3070, 0)
    CameraSetDistance(3000, 80)
    Sleep(500)

    ChrMoveTo(0x0018, 10200, 0, -92518, 1000, 0x00)
    PlaySE(37, 0x00, 0x64)
    SetChrChipByIndex(0x0018, 16)
    PlaySE(524, 0x00, 0x64)
    OP_99(0x0018, 0x02, 0x03, 1000)

    ChrTalk(
        0x0018,
        (
            '#1250031442V呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21CF')
    def lambda_21CF():
        CameraMove(6700, 0, -96370, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_21CF)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031443V#007F呜哇～……\n',
            '下手还是那么狠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0103, 0x0020)
    SetChrChipByIndex(0x0103, 24)
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031444V#020F#1P真过分，\n',
            '我已经手下留情了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031445V#033F的确是留了情，\n',
            '看他的样子不是挺舒服的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031446V#027F#1P哎呀，你也想试试吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0104, 0xFF)
    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0104,
        (
            '#0040031447V#035F不了，下次有机会再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031448V#012F人质应该是\n',
            '被囚禁在下面的楼层。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031449V我们赶快过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0018, 0x0040)
    ClearChrFlags(0x0018, 0x0004)
    ClearChrFlags(0x0019, 0x0004)
    ClearChrFlags(0x001E, 0x0004)
    TerminateThread(0x0103, 0xFF)
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    EventEnd(0x00)
    SetScenaFlags(ScenaFlag(0x006A, 5, 0x355))
    OP_28(0x0039, 0x01, 0x0004)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x0014 offset: 0x2387
@scena.Code('func_14_2387')
def func_14_2387():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    SetMapFlags(0x00400000)
    SetChrPos(0x0101, -51020, 0, -100510, 0)
    SetChrPos(0x0102, -51020, 0, -100510, 0)
    SetChrPos(0x0103, -51020, 0, -100510, 0)
    SetChrPos(0x0104, -51020, 0, -100510, 0)
    SetChrPos(0x001A, -49700, 0, -95128, 270)
    SetChrPos(0x001B, -51210, 0, -95060, 90)
    SetChrPos(0x0020, -46020, 0, -97600, 90)
    SetChrPos(0x0021, -50250, 0, -91580, 270)
    SetChrPos(0x0022, -52750, 0, -91250, 90)
    SetChrPos(0x0023, -56510, 0, -97430, 270)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    SetChrChipByIndex(0x0101, 20)
    SetChrChipByIndex(0x0102, 22)
    SetChrChipByIndex(0x0103, 24)
    SetChrChipByIndex(0x0104, 26)
    CameraMove(-50990, 0, -98940, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_4A(0x001A, 255)
    OP_4A(0x001B, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0021, 255)
    OP_4A(0x0022, 255)
    OP_4A(0x0023, 255)
    OP_62(0x001A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0020, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0021, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0022, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0023, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_257C')
    def lambda_257C():
        CameraMove(-51370, 0, -96390, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_257C)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_2599')
    def lambda_2599():
        ChrWalkTo(0x00FE, -51650, 0, -97940, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2599)

    Sleep(200)

    ClearChrFlags(0x0103, 0x0080)

    @scena.Lambda('lambda_25BE')
    def lambda_25BE():
        ChrWalkTo(0x00FE, -50530, 0, -98350, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_25BE)

    Sleep(200)

    ClearChrFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_25E3')
    def lambda_25E3():
        ChrWalkTo(0x00FE, -52790, 0, -98700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_25E3)

    Sleep(200)

    ClearChrFlags(0x0104, 0x0080)

    @scena.Lambda('lambda_2608')
    def lambda_2608():
        ChrWalkTo(0x00FE, -49960, 0, -99250, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2608)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0103, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 270, 0)
    WaitForThreadExit(0x0104, 0x0001)
    SetChrDirection(0x0104, 45, 0)

    @scena.Lambda('lambda_2645')
    def lambda_2645():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_2645)

    @scena.Lambda('lambda_2653')
    def lambda_2653():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2653)

    @scena.Lambda('lambda_2661')
    def lambda_2661():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_2661)

    @scena.Lambda('lambda_266F')
    def lambda_266F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_266F)

    @scena.Lambda('lambda_267D')
    def lambda_267D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_267D)

    @scena.Lambda('lambda_268B')
    def lambda_268B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_268B)

    WaitForThreadExit(0x001A, 0x0001)

    ChrTalk(
        0x001A,
        (
            '#1040031471V你、你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#1050031472V游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#1050031473V从、从哪里进来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031474V#022F看起来，\n',
            '里面的房间就是囚禁人质的地方了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031475V你们还是乖乖地投降吧。\n',
            '不然的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0020, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0021, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0022, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0023, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x001A, 15)

    ExecExpressionWithValue(
        0x001A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x001B, 15)

    ExecExpressionWithValue(
        0x001B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0020, 15)
    Sleep(100)

    SetChrChipByIndex(0x0021, 15)
    Sleep(75)

    SetChrChipByIndex(0x0022, 15)
    Sleep(50)

    SetChrChipByIndex(0x0023, 15)

    ChrTalk(
        0x001A,
        (
            '#1040031476V开、开玩笑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#1050031477V干掉他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0020, 17)

    @scena.Lambda('lambda_283A')
    def lambda_283A():
        OP_92(0x00FE, 0x0101, 1000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_283A)

    SetChrChipByIndex(0x0021, 17)

    @scena.Lambda('lambda_2854')
    def lambda_2854():
        OP_92(0x00FE, 0x0101, 1000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_2854)

    SetChrChipByIndex(0x0022, 17)

    @scena.Lambda('lambda_286E')
    def lambda_286E():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_286E)

    SetChrChipByIndex(0x0023, 17)

    @scena.Lambda('lambda_2888')
    def lambda_2888():
        OP_92(0x00FE, 0x0101, 1000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_2888)

    Sleep(250)

    SetChrChipByIndex(0x001A, 17)

    @scena.Lambda('lambda_28A7')
    def lambda_28A7():
        ChrJumpTo(0x00FE, -50860, 0, -97055, 1900, 5000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_28A7)

    SetChrChipByIndex(0x001B, 17)

    @scena.Lambda('lambda_28CA')
    def lambda_28CA():
        ChrJumpTo(0x00FE, -51310, 0, -96673, 1500, 6000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_28CA)

    Sleep(400)

    Battle(0x0000038B, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2900'),
        (-1, 'loc_2903'),
    )

    def _loc_2900(): pass

    label('loc_2900')

    OP_B4(0x00)

    Return()

    def _loc_2903(): pass

    label('loc_2903')

    EventBegin(0x00)
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrChipByIndex(0x001A, 16)
    SetChrChipByIndex(0x001B, 16)
    SetChrChipByIndex(0x0020, 16)
    SetChrChipByIndex(0x0021, 16)
    SetChrChipByIndex(0x0022, 16)
    SetChrChipByIndex(0x0023, 16)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x0020, 0xFF)
    TerminateThread(0x0021, 0xFF)
    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)

    ExecExpressionWithValue(
        0x001A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001B,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0021,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0022,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0023,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-50610, 0, -43450, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x0016, 255)
    OP_4A(0x0017, 255)
    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0009, 0)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000D, 0)
    SetChrSubChip(0x000E, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0010, 0)
    SetChrSubChip(0x0011, 0)
    SetChrSubChip(0x0012, 0)
    SetChrSubChip(0x0013, 0)
    SetChrSubChip(0x0014, 0)
    SetChrSubChip(0x0015, 0)
    SetChrSubChip(0x0016, 0)
    SetChrSubChip(0x0017, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#1290031478V怎、怎么了……\n',
            '外面发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031479V唔……就算是吵架，\n',
            '也未免也太吵了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0080)
    SetChrPos(0x0101, -51210, 0, -51500, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010031480V#005F#1P大家没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2C53')
    def lambda_2C53():
        CameraMove(-50590, 0, -45100, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C53)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_2C70')
    def lambda_2C70():
        ChrWalkTo(0x00FE, -51870, 0, -47230, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C70)

    Sleep(200)

    SetChrPos(0x0103, -51210, 0, -51500, 0)

    @scena.Lambda('lambda_2CA1')
    def lambda_2CA1():
        ChrWalkTo(0x00FE, -50620, 0, -47560, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2CA1)

    Sleep(200)

    SetChrPos(0x0102, -51210, 0, -51500, 0)
    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_2CD7')
    def lambda_2CD7():
        ChrWalkTo(0x00FE, -52860, 0, -48210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2CD7)

    Sleep(200)

    SetChrPos(0x0104, -51210, 0, -51500, 0)

    @scena.Lambda('lambda_2D08')
    def lambda_2D08():
        ChrWalkTo(0x00FE, -49990, 0, -48740, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2D08)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 0, 0)
    ClearChrFlags(0x0102, 0x0004)
    WaitForThreadExit(0x0104, 0x0001)
    SetChrDirection(0x0104, 0, 0)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0103,
        (
            '#0030031481V#020F我们是游击士协会的人。\n',
            '前来营救大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, -46560, 0, -45980, 4000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#1290031482V真、真的吗……\n',
            '是来救我们的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031483V#010F看守的空贼已经被制伏了，\n',
            '总之请大家放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1300031484V#1P真、真的……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1310031485V#1P得、得救啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031486V#1P我是定期船『林德号』的\n',
            '机长古兰托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031487V#1P真是太感谢你们了……\n',
            '都不知该说些什么才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031488V#006F感谢的话等离开后再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031489V对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)
    Sleep(200)

    SetChrDirection(0x0101, 45, 400)
    Sleep(200)

    SetChrDirection(0x0101, 0, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031490V#004F……咦？咦咦咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031491V#012F好像不在这里面啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031492V#1P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031493V#002F请、请问一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031494V所有的人质都在这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031495V#1P啊啊，说得没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031496V#1P乘坐『林德号』的\n',
            '乘客和乘务员全部都在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031497V#004F怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031498V#012F请问乘客当中有没有\n',
            '有一个叫做卡西乌斯·布莱特的人？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031499V他是游击士协会的成员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031500V#1P卡西乌斯·布莱特……？\n',
            '这名字我好像在哪听到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#1320031501V啊，机长……\n',
            '就是那位客人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)

    ChrTalk(
        0x000A,
        (
            '#1320031502V起航之前下机的那位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031503V#3P啊啊！\n',
            '是有这么一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031504V#002F怎、怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1280031505V#1P啊，在起航之前，\n',
            '有一位客人临时下机了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031506V#1P他是在王都登机的男乘客，\n',
            '的确，我记得就是叫这个名字。',
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
            '#0010031507V#004F怎么会这样……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031508V但、但是乘客名单上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031509V#1P因为是起航前才下机的，\n',
            '所以没来得及办理文件手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031510V#1P本应在到达洛连特之后补办手续的，\n',
            '但我们途中遭劫机，之后被关在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031511V#004F……………………（松了口气）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031512V#015F原来如此，发生了这样的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031513V父亲被空贼抓住，\n',
            '这一点本来就觉得很奇怪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031514V#027F呼……\n',
            '疑惑也终于解开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031515V#031F哈·哈·哈，可真是奇妙的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031516V#009F慢、慢着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031517V这、这么说来……\n',
            '老爸现在到底在做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031518V发生了这么大的骚动，\n',
            '怎么也不联络我们一下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031519V#012F冷静点，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031520V这件事的确很奇怪，\n',
            '不过现在想这问题也无济于事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031521V我们必须优先\n',
            '确保这里人质的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031522V#002F#2P啊……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031523V明白了，先不想这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031524V#020F各位，\n',
            '我们现在要去逮捕空贼的首领。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031525V所以很抱歉，\n',
            '请大家再稍稍忍耐一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1280031526V#1P啊，好的……\n',
            '那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#1290031527V这样的话，我们就忍耐一下吧。\n',
            '现在我们的命都交托在你们手上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1290031528V请你们无论如何也要加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031529V#006F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-51030, 0, -47780, 0)
    CameraSetDistance(2600, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    CreateThread(0x0015, 0x00, 0x00, 0x0002)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    SetChrPos(0x0000, -51030, 0, -47780, 0)
    SetChrPos(0x0001, -51030, 0, -47780, 0)
    SetChrPos(0x0002, -51030, 0, -47780, 0)
    SetChrPos(0x0003, -51030, 0, -47780, 0)
    OP_0D()
    ClearMapFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x006A, 6, 0x356))
    OP_28(0x0039, 0x01, 0x0008)
    OP_28(0x0039, 0x01, 0x0010)
    OP_28(0x0039, 0x01, 0x0020)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x0020, 0x0080)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x0018, -54970, 0, -93490, 315)
    SetChrPos(0x0019, -48920, 0, -91340, 53)
    SetChrPos(0x001C, -45150, 0, -93440, 163)
    SetChrPos(0x001D, -48280, 0, -97510, 119)
    SetChrPos(0x001E, -54960, 0, -97820, 86)
    SetChrPos(0x001F, -53760, 0, -91280, 172)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    TerminateThread(0x001F, 0xFF)
    SetChrChipByIndex(0x0018, 28)
    SetChrChipByIndex(0x0019, 28)
    SetChrChipByIndex(0x001C, 28)
    SetChrChipByIndex(0x001D, 28)
    SetChrChipByIndex(0x001E, 28)
    SetChrChipByIndex(0x001F, 28)

    ExecExpressionWithValue(
        0x0018,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
