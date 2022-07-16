import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4150_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4150   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奥利维尔'),
    TXT(0x02, '士兵'),
    TXT(0x03, '士兵'),
    TXT(0x04, '士兵'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '士兵'),
    TXT(0x09, '士兵'),
    TXT(0x0A, '王都格兰赛尔·北街区'),
    TXT(0x0B, '庭园大道方向'),
    TXT(0x0C, '王都格兰赛尔·东街区'),
    TXT(0x0D, '王都格兰赛尔·西街区'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4150.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2F1E
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 4200,
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT07/CH00133._CH', 'ED6_DT07/CH00133P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000C,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000D,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000E,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000F,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 10,
            z                   = 250,
            y                   = 36990,
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
            x                   = -50,
            z                   = 0,
            y                   = -90220,
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
            x                   = 54990,
            z                   = 0,
            y                   = -1130,
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
            x                   = -44420,
            z                   = 0,
            y                   = -19990,
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

# id: 0x10003 offset: 0x2F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 5270,
            y           = -1000,
            z           = -67700,
            range       = -6090,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF0182,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -25000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = -10280,
            y           = 0,
            z           = -11040,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = -14940,
            y           = 0,
            z           = -15750,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = -10290,
            y           = 0,
            z           = -30020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 9240,
            y           = 0,
            z           = -13010,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 15900,
            y           = 0,
            z           = 6330,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000020,
        ),
    )

# id: 0x10005 offset: 0x3D2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3D2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3E0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0005)

    def _loc_3E0(): pass

    label('loc_3E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_3F3',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0007)

    def _loc_3F3(): pass

    label('loc_3F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_401',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0010)

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_40F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, 0x0011)

    def _loc_40F(): pass

    label('loc_40F')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_41F'),
        (0x00000067, 'loc_435'),
        (-1, 'loc_44B'),
    )

    def _loc_41F(): pass

    label('loc_41F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 7, 0x607)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_432',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 0, 0x608))
    Event(0, 0x0003)

    def _loc_432(): pass

    label('loc_432')

    Jump('loc_44B')

    def _loc_435(): pass

    label('loc_435')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 1, 0x629)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_448',
    )

    SetScenaFlags(ScenaFlag(0x00C5, 1, 0x629))
    Event(0, 0x0008)

    def _loc_448(): pass

    label('loc_448')

    Jump('loc_44B')

    def _loc_44B(): pass

    label('loc_44B')

    Return()

# id: 0x0001 offset: 0x44C
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -148000, 196699)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 1, 0x611)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_46F',
    )

    OP_1C(0x10, 0x00, 0x0004)

    def _loc_46F(): pass

    label('loc_46F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 1, 0x609)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47F',
    )

    OP_1B(0x00, 0x00, 0x0012)

    Jump('loc_51C')

    def _loc_47F(): pass

    label('loc_47F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_498',
    )

    OP_1B(0x00, 0x00, 0x0006)

    Jump('loc_51C')

    def _loc_498(): pass

    label('loc_498')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 7, 0x61F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4AC',
    )

    OP_1B(0x00, 0x00, 0x0013)

    Jump('loc_51C')

    def _loc_4AC(): pass

    label('loc_4AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 7, 0x61F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 0, 0x620)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_1B(0x00, 0x00, 0x0014)

    Jump('loc_51C')

    def _loc_4C0(): pass

    label('loc_4C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D4',
    )

    OP_1B(0x00, 0x00, 0x0015)

    Jump('loc_51C')

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 0, 0x628)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E8',
    )

    OP_1B(0x00, 0x00, 0x0016)

    Jump('loc_51C')

    def _loc_4E8(): pass

    label('loc_4E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4FC',
    )

    OP_1B(0x00, 0x00, 0x0017)

    Jump('loc_51C')

    def _loc_4FC(): pass

    label('loc_4FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_510',
    )

    OP_1B(0x00, 0x00, 0x0018)

    Jump('loc_51C')

    def _loc_510(): pass

    label('loc_510')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_51C',
    )

    OP_1B(0x00, 0x00, 0x0019)

    def _loc_51C(): pass

    label('loc_51C')

    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0004, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0010, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_605',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    CreateThread(0x000B, 0x01, 0x00, 0x0009)
    CreateThread(0x000C, 0x01, 0x00, 0x0009)
    CreateThread(0x000D, 0x01, 0x00, 0x0009)
    CreateThread(0x000E, 0x01, 0x00, 0x0009)
    CreateThread(0x000F, 0x01, 0x00, 0x0009)
    CreateThread(0x0010, 0x01, 0x00, 0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_599',
    )

    def _loc_599(): pass

    label('loc_599')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_5A4',
    )

    def _loc_5A4(): pass

    label('loc_5A4')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_5C1',
    )

    SetChrFlags(0x000E, 0x0080)
    TerminateThread(0x000E, 0xFF)
    SetChrFlags(0x000F, 0x0080)
    TerminateThread(0x000F, 0xFF)

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_5DE',
    )

    SetChrFlags(0x000B, 0x0080)
    TerminateThread(0x000B, 0xFF)
    SetChrFlags(0x000C, 0x0080)
    TerminateThread(0x000C, 0xFF)

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_5F2',
    )

    SetChrFlags(0x0010, 0x0080)
    TerminateThread(0x0010, 0xFF)

    def _loc_5F2(): pass

    label('loc_5F2')

    CameraSetDistance(4200, 0)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_605(): pass

    label('loc_605')

    Return()

# id: 0x0002 offset: 0x606
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_61B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_61B(): pass

    label('loc_61B')

    Return()

# id: 0x0003 offset: 0x61C
@scena.Code('func_03_61C')
def func_03_61C():
    EventBegin(0x00)
    CameraMove(600, 250, 1950, 0)
    OP_67(0, 17690, -10000, 0)
    CameraSetDistance(2530, 0)
    OP_6C(315000, 0)
    OP_6E(571, 0)
    SetChrPos(0x0101, -340, 0, -51790, 0)
    SetChrPos(0x0102, -1140, 0, -53240, 0)
    SetChrPos(0x010E, 710, 0, -53630, 0)

    @scena.Lambda('lambda_0694')
    def lambda_0694():
        CameraMove(-450, 290, -49040, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0694)

    @scena.Lambda('lambda_06AC')
    def lambda_06AC():
        CameraSetDistance(3600, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06AC)

    @scena.Lambda('lambda_06BC')
    def lambda_06BC():
        OP_67(0, 6190, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06BC)

    @scena.Lambda('lambda_06D4')
    def lambda_06D4():
        OP_6C(315000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06D4)

    @scena.Lambda('lambda_06E4')
    def lambda_06E4():
        OP_6E(262, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_06E4)

    Sleep(8500)

    ChrTalk(
        0x0101,
        (
            '#000F哇～～\n',
            '好大的城市啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100580V以前和老爸一起来的时候，\n',
            '就有这么大吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100581V#010F当然了，这是王国最大的城市嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100582V这条大街的最前方，\n',
            '就是女王陛下所居住的格兰赛尔城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还有七耀教会的大圣堂、王立竞技场，\n',
            '以及各国的大使馆之类的设施呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100585V不过约修亚，你还真是了解啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100586V以前也来过这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F嗯……\n',
            '也是小时候的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100588V#130F真的是……\n',
            '这城市无论何时看起来都是这么美丽呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100589V不过单从规模上来说，\n',
            '帝国和共和国的首都比这里要更大一些。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100590V不过这个格兰赛尔，\n',
            '可是有着其他地方比不上的舒适感呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_094D')
    def lambda_094D():
        ChrTurnDirection(0x00FE, 0x010E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_094D)

    ChrTurnDirection(0x0101, 0x010E, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，真是高兴啊。\n',
            '能听到外国的人这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '说起来……\n',
            '教授，接下来打算干什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100593V留在这里的费用没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0101, 400)

    ChrTalk(
        0x010E,
        (
            '#0150100594V#130F哈哈，其实是有保障的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100595V我要暂时寄住在一个叫\n',
            '『历史资料馆』的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎，还有这样的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100597V#010F是展示发掘出来的文物\n',
            '和美术品之类的博物馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100598V#130F对，作为那里的名誉会员，\n',
            '我要在那里借住一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100599V艾丝蒂尔、约修亚，\n',
            '如果方便的话你们也过来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呜……说到博物馆，\n',
            '就有一种很严肃的气氛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是不是要说『既然来了，就学习吧』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0151850001V#130F呵呵，如果你愿意的话，\n',
            '我也可以认真地教教你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0151850002V……开玩笑的，\n',
            '只是参观一下展示品，\n',
            '就会感到很开心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100604V那么，我就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C11')
    def lambda_0C11():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_0C11')

    DispatchAsync2(0x0101, 0x0001, lambda_0C11)

    @scena.Lambda('lambda_0C22')
    def lambda_0C22():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_0C22')

    DispatchAsync2(0x0102, 0x0001, lambda_0C22)

    ChrWalkTo(0x010E, 3960, 0, -49800, 2000, 0x00)

    @scena.Lambda('lambda_0C47')
    def lambda_0C47():
        ChrWalkTo(0x00FE, 4950, 0, -35100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_0C47)

    @scena.Lambda('lambda_0C62')
    def lambda_0C62():
        CameraMove(-1030, 0, -52400, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C62)

    Sleep(2000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#000F哈～怎么说呢，\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过说到名誉会员，\n',
            '应该是个相当有名的学者吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，说不定就是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，我们先去\n',
            '拜访一下游击士协会吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100609V要办理转属手续……\n',
            '而且要完成博士的委托，\n',
            '也要先和协会商量一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯，没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100611V仔细想想，\n',
            '该怎么和女王陛下会面呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '肯定不会是去城里\n',
            '就能见到那样简单吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x010E, -100, 0, -52250, 0)
    SetChrFlags(0x010E, 0x0080)
    EventEnd(0x00)
    FormationDelMember(0x0D, 0xFF)

    Return()

# id: 0x0004 offset: 0xDEB
@scena.Code('func_04_DEB')
def func_04_DEB():
    EventBegin(0x00)
    CameraMove(16030, 500, 7220, 1000)

    ChrTalk(
        0x0101,
        (
            '#000F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101257V这是……钢琴？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，不是放唱片。\n',
            '好像是里面有人在弹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F有点不好的预感呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xE84
@scena.Code('func_05_E84')
def func_05_E84():
    EventBegin(0x00)
    CameraMove(16020, 250, 7280, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0040)
    SetChrPos(0x0101, 15830, 740, 8470, 0)
    SetChrPos(0x0102, 15830, 740, 8470, 0)
    SetChrPos(0x0008, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x0010, 60)
    OP_73(0x0010)

    @scena.Lambda('lambda_0EE5')
    def lambda_0EE5():
        ChrWalkTo(0x00FE, 15230, 250, 3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EE5)

    Sleep(400)

    @scena.Lambda('lambda_0F05')
    def lambda_0F05():
        ChrWalkTo(0x00FE, 16480, 250, 3690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F05)

    Sleep(500)

    @scena.Lambda('lambda_0F25')
    def lambda_0F25():
        ChrWalkTo(0x00FE, 16030, 250, 5370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F25)

    CameraMove(16100, 250, 4400, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#000F我说，为什么这么\n',
            '理所当然地就跟出来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F哈·哈·哈。\n',
            '别说这么无情的话啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101319V旅行要结伴才愉快嘛，\n',
            '而且我也可以帮忙找人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还是……\n',
            '……我妨碍到你们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0041050017V#030F哈·哈·哈。\n',
            '真是天真啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050018V刚刚意识到自己心中爱情花蕾的存在，\n',
            '却又害怕它开放的少女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050019V……嘻嘻，感觉不错啊， \n',
            '让我都有一些春心萌动了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F…………呜………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101327V你说的是什么意思啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F嘻嘻，那就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#000F嘿呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x00, 0x07, 2000)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x1000)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 2)

    ChrTalk(
        0x0008,
        (
            '#030F啊～～……！#10A',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_119B')
    def lambda_119B():
        ChrMoveTo(0x00FE, 15830, 740, 8470, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_119B)

    OP_99(0x0101, 0x07, 0x0C, 2000)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2710101331V哇哇，怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2720101332V这位客人，请振作一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2730101333V不行了……\n',
            '已经翻白眼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101335V不知道你在生什么气，\n',
            '不过这也太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 3)
    SetChrFlags(0x0101, 0x0002)
    OP_99(0x0101, 0x00, 0x13, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F……我已经避开了要害，\n',
            '只是把他打飞而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101337V不会受很重的伤的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 65535)

    ChrTalk(
        0x0008,
        (
            '#030F呵呵……\n',
            '艾丝蒂尔……真害羞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……确实没什么事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_138B',
    )

    ChrTalk(
        0x0101,
        (
            '#000F好啦，再去找人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '赶快去大使馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13BA')

    def _loc_138B(): pass

    label('loc_138B')

    ChrTalk(
        0x0101,
        (
            '#000F好啦，再去找人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '赶快去周游道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13BA(): pass

    label('loc_13BA')

    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x13BD
@scena.Code('func_06_13BD')
def func_06_13BD():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_143A',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101218V#010F艾丝蒂尔，还不知道\n',
            '金先生到底去了哪里呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101219V我们去东街区的\n',
            '卡尔瓦德大使馆问问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F6')

    def _loc_143A(): pass

    label('loc_143A')

    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101220V#000F啊，对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101221V不是说金大哥\n',
            '时常在酒廊喝酒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101222V#010F啊，艾南先生\n',
            '确实这么说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101223V为了慎重起见，去周游道之前\n',
            '先到酒廊看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F6(): pass

    label('loc_14F6')

    Call(0, 0x001B)

    Return()

# id: 0x0007 offset: 0x14FB
@scena.Code('func_07_14FB')
def func_07_14FB():
    ClearMapFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(16020, 250, 7280, 0)
    FormationDelMember(0x07, 0xFF)
    SetChrPos(0x0101, 15830, 740, 8470, 0)
    SetChrPos(0x0102, 15830, 740, 8470, 0)
    OP_0D()
    OP_70(0x000D, 59)
    OP_73(0x000D)

    @scena.Lambda('lambda_1549')
    def lambda_1549():
        ChrWalkTo(0x00FE, 15230, 250, 3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1549)

    Sleep(400)

    @scena.Lambda('lambda_1569')
    def lambda_1569():
        ChrWalkTo(0x00FE, 16480, 250, 3690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1569)

    CameraMove(16100, 250, 4400, 2000)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 90, 400)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 270, 400)
    Fade(1000)
    CameraSetDistance(3000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010101582V#008F呼～……\n',
            '吃得肚子鼓鼓的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101583V#007F那两个人，都已经吃了那么多了，\n',
            '还在不停地狼吞虎咽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101584V他们还真是合得来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101585V#019F金先生是那样的体格，\n',
            '奥利维尔又很能吃嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101586V只要不影响到明天的正式赛，\n',
            '就应该没什么关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101587V#006F嗯，确实他们两个都不用让人担心。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101588V#010F天色已经黑了，\n',
            '我们也该去北街区的酒店了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101589V艾南先生一定已经给我们订好房间了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x176E
@scena.Code('func_08_176E')
def func_08_176E():
    EventBegin(0x00)
    OP_6F(0x0001, 60)
    SetChrPos(0x0101, 8940, 250, -12710, 270)
    SetChrPos(0x0102, 8980, 250, -13870, 270)
    SetChrPos(0x0009, 1930, 0, -4430, 0)
    SetChrPos(0x000A, 1040, 0, -5320, 0)
    SetChrChipByIndex(0x0009, 20)
    SetChrChipByIndex(0x000A, 20)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    CameraMove(9320, 440, -13270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeOut(0, 0, -1)
    PlaySE(6, 0x00, 0x64)
    Sleep(1500)

    FadeIn(1500, 0)
    OP_72(0x0001, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0001, 0)
    OP_71(0x0001, 0x0800)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010111131V#004F哇……\n',
            '已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111132V#010F我们还是赶快回到旅馆比较好吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#4190111133V#4P喂，那边的人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_18FC')
    def lambda_18FC():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18FC)

    @scena.Lambda('lambda_190A')
    def lambda_190A():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_190A)

    @scena.Lambda('lambda_1918')
    def lambda_1918():
        CameraMove(8710, 250, -11760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1918)

    @scena.Lambda('lambda_1930')
    def lambda_1930():
        OP_6C(90000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1930)

    @scena.Lambda('lambda_1940')
    def lambda_1940():
        ChrWalkTo(0x00FE, 7030, 250, -10460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1940)

    Sleep(300)

    @scena.Lambda('lambda_1960')
    def lambda_1960():
        ChrWalkTo(0x00FE, 5920, 0, -11500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1960)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010111134V#004F哎……\n',
            '士兵先生，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111135V#1P我们是巡逻人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111136V#1P从今天开始，\n',
            '作为恐怖活动的应付对策之一，\n',
            '夜间的巡视要进行强化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111137V因此，晚上请尽量克制一下，\n',
            '最好不要擅自外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111138V你们也赶快回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111139V#509F晚上不让外出……\n',
            '这不是很不方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111140V这是上面的决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111141V#1P虽然很抱歉，还是请你们服从指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111142V#1P对了……\n',
            '你们住在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111143V#010F我们住在北街区的罗恩鲍姆酒店。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111144V武术大会期间都会住在那里的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111145V武术大会期间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111146V等一下，\n',
            '我好像在哪里见过你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#4190111147V#3S#1P啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111148V#1P这两个孩子，\n',
            '不就是进入武术大会决赛的选手吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111149V你这样一说，还真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111150V#501F啊，士兵先生，\n',
            '你们也去看比赛了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111151V哈哈，是趁着做警卫的时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2490111152V特别是今天白热化的比赛，\n',
            '真是让我感到很兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111153V#1P明天就是决赛了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#4190111154V#1P我们送你们回旅馆，\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111155V#008F哎，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111156V#010F知道了。\n',
            '谢谢你们的好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x1DB3
@scena.Code('func_09_1DB3')
def func_09_1DB3():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_201A',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1DE6',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1DE6(): pass

    label('loc_1DE6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1E0C',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1E0C(): pass

    label('loc_1E0C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1E32',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1E32(): pass

    label('loc_1E32')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1E59',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1E59(): pass

    label('loc_1E59')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1E7F',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1E7F(): pass

    label('loc_1E7F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1EA5',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1EA5(): pass

    label('loc_1EA5')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1ECA',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1ECA(): pass

    label('loc_1ECA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1EEF',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F03')

    def _loc_1EEF(): pass

    label('loc_1EEF')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F03(): pass

    label('loc_1F03')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2017',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2008',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111259V#580F（糟糕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111260V#017F（被发现了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2008(): pass

    label('loc_2008')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_2017(): pass

    label('loc_2017')

    Jump('func_09_1DB3')

    def _loc_201A(): pass

    label('loc_201A')

    Return()

# id: 0x000A offset: 0x201B
@scena.Code('func_0A_201B')
def func_0A_201B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2088',
    )

    SetChrPos(0x00FE, -29750, 250, -16079, 270)
    ChrWalkTo(0x00FE, -8010, 250, -16079, 3000, 0x00)
    ChrWalkTo(0x00FE, -8010, 250, 12010, 3000, 0x00)
    ChrWalkTo(0x00FE, -8010, 250, -16079, 3000, 0x00)
    ChrWalkTo(0x00FE, -29750, 250, -16079, 3000, 0x00)

    Jump('func_0A_201B')

    def _loc_2088(): pass

    label('loc_2088')

    Return()

# id: 0x000B offset: 0x2089
@scena.Code('func_0B_2089')
def func_0B_2089():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_20F6',
    )

    SetChrPos(0x00FE, -29910, 250, -23870, 270)
    ChrWalkTo(0x00FE, -8440, 250, -23870, 3000, 0x00)
    ChrWalkTo(0x00FE, -8660, 250, -33400, 3000, 0x00)
    ChrWalkTo(0x00FE, -8440, 250, -23870, 3000, 0x00)
    ChrWalkTo(0x00FE, -29910, 250, -23870, 3000, 0x00)

    Jump('func_0B_2089')

    def _loc_20F6(): pass

    label('loc_20F6')

    Return()

# id: 0x000C offset: 0x20F7
@scena.Code('func_0C_20F7')
def func_0C_20F7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_213C',
    )

    SetChrPos(0x00FE, -6720, 0, -19860, 270)
    ChrWalkTo(0x00FE, -31200, 0, -19860, 3000, 0x00)
    ChrWalkTo(0x00FE, -6720, 0, -19860, 3000, 0x00)

    Jump('func_0C_20F7')

    def _loc_213C(): pass

    label('loc_213C')

    Return()

# id: 0x000D offset: 0x213D
@scena.Code('func_0D_213D')
def func_0D_213D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2182',
    )

    SetChrPos(0x00FE, 3810, 0, 10100, 180)
    ChrWalkTo(0x00FE, 3810, 0, -35560, 3000, 0x00)
    ChrWalkTo(0x00FE, 3810, 0, 10100, 3000, 0x00)

    Jump('func_0D_213D')

    def _loc_2182(): pass

    label('loc_2182')

    Return()

# id: 0x000E offset: 0x2183
@scena.Code('func_0E_2183')
def func_0E_2183():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_21C8',
    )

    SetChrPos(0x00FE, -3690, 0, -34890, 180)
    ChrWalkTo(0x00FE, -3690, 0, 9690, 3000, 0x00)
    ChrWalkTo(0x00FE, -3690, 0, -34890, 3000, 0x00)

    Jump('func_0E_2183')

    def _loc_21C8(): pass

    label('loc_21C8')

    Return()

# id: 0x000F offset: 0x21C9
@scena.Code('func_0F_21C9')
def func_0F_21C9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2236',
    )

    SetChrPos(0x00FE, -1740, 0, -6830, 180)
    ChrWalkTo(0x00FE, -1740, 0, -20710, 3000, 0x00)
    ChrWalkTo(0x00FE, 2040, 0, -20890, 3000, 0x00)
    ChrWalkTo(0x00FE, 2040, 0, -6990, 3000, 0x00)
    ChrWalkTo(0x00FE, -1740, 0, -6830, 3000, 0x00)

    Jump('func_0F_21C9')

    def _loc_2236(): pass

    label('loc_2236')

    Return()

# id: 0x0010 offset: 0x2237
@scena.Code('func_10_2237')
def func_10_2237():
    EventBegin(0x00)
    FormationDelMember(0x00, 0xFF)
    FormationAddMember(0x03, 0xFF)
    FadeIn(2000, 0)
    CameraMove(-90, 0, -64700, 0)
    OP_67(0, 6090, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(196000, 0)
    OP_6E(372, 0)
    SetChrPos(0x0104, -190, 0, -63320, 197)
    SetChrPos(0x0102, 560, 0, -64300, 200)
    SetChrPos(0x0108, -890, 0, -64430, 197)

    @scena.Lambda('lambda_22BE')
    def lambda_22BE():
        ChrWalkTo(0x00FE, 150, 0, -54130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_22BE)

    @scena.Lambda('lambda_22D9')
    def lambda_22D9():
        ChrWalkTo(0x00FE, 1010, 0, -55550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_22D9)

    @scena.Lambda('lambda_22F4')
    def lambda_22F4():
        ChrWalkTo(0x00FE, -840, 0, -55820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_22F4)

    CameraMove(280, 0, -55900, 3000)
    WaitForThreadExit(0x0104, 0x0001)
    SetChrDirection(0x0104, 0, 400)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#010F……虽然没有巡逻兵了，\n',
            '不过街上的气氛十分紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040011V#070F嗯……\n',
            '确实有种大乱来临的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040012V和昨天的气氛明显不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F很好，此刻就让我\n',
            '用鲁特琴缓和一下\n',
            '这里的紧张空气吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2402')
    def lambda_2402():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2402)

    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#010F如果你做了那么引人注目的事情，\n',
            '那个人一定又会飞奔而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我记得他是叫穆拉对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F是、是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050020V你们两个千万不能\n',
            '接近帝国大使馆啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131009V#070F哈哈，我们才没有\n',
            '那份闲心跑去大使馆那儿呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131010V准备完毕之后\n',
            '就进地下水路里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x251A
@scena.Code('func_11_251A')
def func_11_251A():
    EventBegin(0x00)
    FadeIn(2000, 0)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    CameraMove(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(320000, 0)
    OP_6E(580, 0)

    @scena.Lambda('lambda_257C')
    def lambda_257C():
        CameraMove(-20, 250, 7140, 20000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_257C)

    @scena.Lambda('lambda_2594')
    def lambda_2594():
        OP_6C(0, 20000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_2594)

    Sleep(17000)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x25BB
@scena.Code('func_12_25BB')
def func_12_25BB():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2658',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020100613V#010F还是先去协会支部打声招呼吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100614V要先办理转属手续……\n',
            '而且还有博士的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100615V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26BB')

    def _loc_2658(): pass

    label('loc_2658')

    ChrTalk(
        0x0102,
        (
            '#0020100616V#010F还是先去协会支部打声招呼吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100614V要先办理转属手续……\n',
            '而且还有博士的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26BB(): pass

    label('loc_26BB')

    Call(0, 0x001B)

    Return()

# id: 0x0013 offset: 0x26C0
@scena.Code('func_13_26C0')
def func_13_26C0():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2748',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020110442V#010F赶快回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110443V再磨磨蹭蹭的天就要黑了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110444V#006F嗯，现在就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2790')

    def _loc_2748(): pass

    label('loc_2748')

    ChrTalk(
        0x0102,
        (
            '#0020110442V#010F赶快回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110443V再磨磨蹭蹭的天就要黑了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2790(): pass

    label('loc_2790')

    Call(0, 0x001B)

    Return()

# id: 0x0014 offset: 0x2795
@scena.Code('func_14_2795')
def func_14_2795():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_282E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020110447V#010F已经很晚了，\n',
            '我们回酒店去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110448V该休息的时候就是要好好休息。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110449V#000F酒店在北街区对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2887')

    def _loc_282E(): pass

    label('loc_282E')

    ChrTalk(
        0x0102,
        (
            '#0020110450V#010F已经很晚了，\n',
            '我们回酒店去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110451V明天还有比赛，\n',
            '我们最好早点休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2887(): pass

    label('loc_2887')

    Call(0, 0x001B)

    Return()

# id: 0x0015 offset: 0x288C
@scena.Code('func_15_288C')
def func_15_288C():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_299B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_291E',
    )

    ChrTalk(
        0x0102,
        (
            '#0020110937V#010F我想奈尔先生正在等我们吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110938V去西街区的通讯社看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2998')

    def _loc_291E(): pass

    label('loc_291E')

    ChrTalk(
        0x0102,
        (
            '#0020110940V#010F艾丝蒂尔，那边是城门哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110941V奈尔先生的通讯社应该在西街区吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110942V#006F哦～呵呵，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2998(): pass

    label('loc_2998')

    Jump('loc_29F5')

    def _loc_299B(): pass

    label('loc_299B')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110943V#010F我想奈尔先生正在等我们吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110938V去西街区的通讯社看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_29F5(): pass

    label('loc_29F5')

    Call(0, 0x001B)

    Return()

# id: 0x0016 offset: 0x29FA
@scena.Code('func_16_29FA')
def func_16_29FA():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A94',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020111069V#010F总之我们先回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111070V最好把奈尔的调查结果也告诉艾南先生。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110444V#006F嗯，现在就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AEE')

    def _loc_2A94(): pass

    label('loc_2A94')

    ChrTalk(
        0x0102,
        (
            '#0020111069V#010F总之我们先回协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111070V最好把奈尔的调查结果也告诉艾南先生。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AEE(): pass

    label('loc_2AEE')

    Call(0, 0x001B)

    Return()

# id: 0x0017 offset: 0x2AF3
@scena.Code('func_17_2AF3')
def func_17_2AF3():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B6B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080111935V#070F呼，已经傍晚了。\n',
            '我们尽量不要外出了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111936V今天就别修行了，\n',
            '赶快去城里参加晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BD7')

    def _loc_2B6B(): pass

    label('loc_2B6B')

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111937V#070F喂喂，\n',
            '难道你们还打算外出吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111938V就算是再热衷于修炼，\n',
            '现在还是快去参加晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BD7(): pass

    label('loc_2BD7')

    Call(0, 0x001B)

    Return()

# id: 0x0018 offset: 0x2BDC
@scena.Code('func_18_2BDC')
def func_18_2BDC():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C3D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080131011V#070F现在没空去街道外面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131012V做好准备后就向地下水路进发吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C94')

    def _loc_2C3D(): pass

    label('loc_2C3D')

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080131013V#070F现在没空去街道外面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131014V做好准备后就向地下水路进发吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C94(): pass

    label('loc_2C94')

    Call(0, 0x001B)

    Return()

# id: 0x0019 offset: 0x2C99
@scena.Code('func_19_2C99')
def func_19_2C99():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D40',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140901V#501F啊，这边是城外……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140902V#000F我说，\n',
            '我们还是在城里再散散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140903V#010F嗯，好啊。\n',
            '还有很多地方没看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC1')

    def _loc_2D40(): pass

    label('loc_2D40')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010140904V#000F我说，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140905V在城里面再散会儿步吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020140903V#010F嗯，好啊。\n',
            '还有很多地方没看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC1(): pass

    label('loc_2DC1')

    Call(0, 0x001B)

    Return()

# id: 0x001A offset: 0x2DC6
@scena.Code('func_1A_2DC6')
def func_1A_2DC6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 4, 0x62C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EAB',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E5F',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111296V#012F艾丝蒂尔，\n',
            '已经快到指定的时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111297V我们赶快去大圣堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111298V#002F嗯……明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EA7')

    def _loc_2E5F(): pass

    label('loc_2E5F')

    ChrTalk(
        0x0102,
        (
            '#0020111299V#012F已经快到指定的时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111297V我们赶快去大圣堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EA7(): pass

    label('loc_2EA7')

    Call(0, 0x001B)

    def _loc_2EAB(): pass

    label('loc_2EAB')

    Return()

# id: 0x001B offset: 0x2EAC
@scena.Code('func_1B_2EAC')
def func_1B_2EAC():
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x001C offset: 0x2EC8
@scena.Code('func_1C_2EC8')
def func_1C_2EC8():
    OP_13(0x00B9)

    Return()

# id: 0x001D offset: 0x2ECC
@scena.Code('func_1D_2ECC')
def func_1D_2ECC():
    OP_13(0x00B0)

    Return()

# id: 0x001E offset: 0x2ED0
@scena.Code('func_1E_2ED0')
def func_1E_2ED0():
    OP_13(0x00B2)

    Return()

# id: 0x001F offset: 0x2ED4
@scena.Code('func_1F_2ED4')
def func_1F_2ED4():
    OP_13(0x00AE)

    Return()

# id: 0x0020 offset: 0x2ED8
@scena.Code('func_20_2ED8')
def func_20_2ED8():
    OP_13(0x00B3)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
