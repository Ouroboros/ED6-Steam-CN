import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4137_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4137   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奥利维尔'),
    TXT(0x02, '奈尔'),
    TXT(0x03, '朵洛希'),
    TXT(0x04, '总编'),
    TXT(0x05, '库拉茨'),
    TXT(0x06, '克鲁茨'),
    TXT(0x07, '科蕾蒂'),
    TXT(0x08, '彭萨'),
    TXT(0x09, '金'),
    TXT(0x0A, '奥利维尔'),
    TXT(0x0B, '米亚尔'),
    TXT(0x0C, '戈万'),
    TXT(0x0D, '帕菲'),
    TXT(0x0E, '娜娜'),
    TXT(0x0F, '巴拉尔'),
    TXT(0x10, '科尼嘉'),
    TXT(0x11, '诺蒂亚'),
    TXT(0x12, '法尔茨'),
    TXT(0x13, '莎莉亚'),
    TXT(0x14, '士兵丹'),
    TXT(0x15, '士兵阿尔兹'),
    TXT(0x16, '阿加特'),
    TXT(0x17, '提妲'),
    TXT(0x18, '拉赛尔'),
    TXT(0x19, '　'),
    TXT(0x1A, '　'),
    TXT(0x1B, '　'),
    TXT(0x1C, '　'),
    TXT(0x1D, '　'),
    TXT(0x1E, '　'),
    TXT(0x1F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4137.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xAC9A
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT06/CH20050._CH', 'ED6_DT06/CH20050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT06/CH20086._CH', 'ED6_DT06/CH20086P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
    ]

# id: 0x10002 offset: 0x182
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -54180,
            z                   = 0,
            y                   = 61080,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0111,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 5200,
            z                   = 4000,
            y                   = 2130,
            direction           = 182,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = 4560,
            z                   = 0,
            y                   = 2500,
            direction           = 186,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 4460,
            z                   = 0,
            y                   = -3910,
            direction           = 94,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x01D6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -3600,
            z                   = 0,
            y                   = -2029,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -3520,
            z                   = 0,
            y                   = -4540,
            direction           = 6,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 58680,
            z                   = 0,
            y                   = -3720,
            direction           = 188,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 59970,
            z                   = 0,
            y                   = -4990,
            direction           = 263,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 61020,
            z                   = 0,
            y                   = 2490,
            direction           = 197,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 61340,
            z                   = 0,
            y                   = 550,
            direction           = 347,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -57020,
            z                   = 0,
            y                   = 61110,
            direction           = 327,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -59180,
            z                   = 0,
            y                   = 59600,
            direction           = 5,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -56630,
            z                   = 0,
            y                   = 5500,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -3620,
            z                   = 0,
            y                   = -2020,
            direction           = 171,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -3550,
            z                   = 0,
            y                   = -4570,
            direction           = 9,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65562,
            chipIndex           = 26,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572890,
            chipIndex           = 26,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572890,
            chipIndex           = 26,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572890,
            chipIndex           = 26,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x542
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x542
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x542
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x542
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_550',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x001C)

    def _loc_550(): pass

    label('loc_550')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_55E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x001D)

    def _loc_55E(): pass

    label('loc_55E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_56C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x001E)

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_57A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, 0x0021)

    def _loc_57A(): pass

    label('loc_57A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_586'),
        (-1, 'loc_5AF'),
    )

    def _loc_586(): pass

    label('loc_586')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_599',
    )

    SetScenaFlags(ScenaFlag(0x00C4, 7, 0x627))
    Event(0, 0x001F)

    def _loc_599(): pass

    label('loc_599')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 6, 0x64E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AC',
    )

    SetScenaFlags(ScenaFlag(0x00C9, 6, 0x64E))
    Event(0, 0x0020)

    def _loc_5AC(): pass

    label('loc_5AC')

    Jump('loc_5AF')

    def _loc_5AF(): pass

    label('loc_5AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D1',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 4650, 0, 600, 0)

    def _loc_5D1(): pass

    label('loc_5D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_675',
    )

    ClearChrFlags(0x001E, 0x0080)
    SetChrPos(0x001E, 57670, 0, -5070, 111)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001F, 59920, 0, -5060, 275)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 5860, 4000, -4760, 350)
    SetChrFlags(0x000C, 0x0010)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -3620, 0, -2160, 186)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x001D, -3600, 0, -4420, 359)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 62780, 0, -3550, 162)
    CreateThread(0x000A, 0x00, 0x00, 0x0003)

    Jump('loc_8AC')

    def _loc_675(): pass

    label('loc_675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6C8',
    )

    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -54200, 0, 63010, 194)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrPos(0x0018, -53520, 0, 123230, 98)
    CreateThread(0x0018, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)

    Jump('loc_8AC')

    def _loc_6C8(): pass

    label('loc_6C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6F9',
    )

    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -54200, 0, 63010, 194)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Jump('loc_8AC')

    def _loc_6F9(): pass

    label('loc_6F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_74F',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 5860, 4000, -4760, 350)
    SetChrFlags(0x000C, 0x0010)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 62780, 0, -3550, 162)
    CreateThread(0x000A, 0x00, 0x00, 0x0003)

    Jump('loc_8AC')

    def _loc_74F(): pass

    label('loc_74F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_759',
    )

    Jump('loc_8AC')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_7C9',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -3620, 0, -2160, 186)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -3690, 0, -4720, 344)
    SetChrFlags(0x0008, 0x0010)
    SetChrPos(0x0018, -60680, 0, 122710, 160)
    CreateThread(0x0018, 0x00, 0x00, 0x0005)
    SetChrPos(0x0019, -54350, 0, 1120, 265)
    CreateThread(0x0019, 0x00, 0x00, 0x0002)

    Jump('loc_8AC')

    def _loc_7C9(): pass

    label('loc_7C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_7D3',
    )

    Jump('loc_8AC')

    def _loc_7D3(): pass

    label('loc_7D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_830',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -3620, 0, -2160, 186)
    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -3690, 0, -4720, 344)
    SetChrFlags(0x0008, 0x0010)
    SetChrPos(0x0018, -63230, 0, 59560, 338)
    CreateThread(0x0018, 0x00, 0x00, 0x0002)
    SetChrFlags(0x0019, 0x0080)

    Jump('loc_8AC')

    def _loc_830(): pass

    label('loc_830')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_83A',
    )

    Jump('loc_8AC')

    def _loc_83A(): pass

    label('loc_83A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_872',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_86F',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 910, 0, -3650, 189)
    SetChrPos(0x000E, 610, 0, -3020, 146)

    def _loc_86F(): pass

    label('loc_86F')

    Jump('loc_8AC')

    def _loc_872(): pass

    label('loc_872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_8AC',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 5860, 4000, -4760, 350)
    SetChrFlags(0x000C, 0x0010)
    SetChrPos(0x0018, -63230, 0, 59560, 338)
    CreateThread(0x0018, 0x00, 0x00, 0x0002)

    def _loc_8AC(): pass

    label('loc_8AC')

    Return()

# id: 0x0001 offset: 0x8AD
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_8BD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8BD(): pass

    label('loc_8BD')

    Return()

# id: 0x0002 offset: 0x8BE
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8D3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_8D3(): pass

    label('loc_8D3')

    Return()

# id: 0x0003 offset: 0x8D4
@scena.Code('func_03_8D4')
def func_03_8D4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8F7',
    )

    OP_8D(0x00FE, 61240, -1420, 64280, -5700, 3000)

    Jump('func_03_8D4')

    def _loc_8F7(): pass

    label('loc_8F7')

    Return()

# id: 0x0004 offset: 0x8F8
@scena.Code('func_04_8F8')
def func_04_8F8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_91B',
    )

    OP_8D(0x00FE, -57970, 64269, -56460, 57520, 3000)

    Jump('func_04_8F8')

    def _loc_91B(): pass

    label('loc_91B')

    Return()

# id: 0x0005 offset: 0x91C
@scena.Code('func_05_91C')
def func_05_91C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_93F',
    )

    OP_8D(0x00FE, -62670, 124500, -59560, 120770, 3000)

    Jump('func_05_91C')

    def _loc_93F(): pass

    label('loc_93F')

    Return()

# id: 0x0006 offset: 0x940
@scena.Code('func_06_940')
def func_06_940():
    TalkBegin(0x00FE)

    ChrTalk(
        0x010B,
        (
            '#0541270004V#100F呼～逃亡的生活\n',
            '对于我这一把老骨头而言真是艰苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270005V多亏了你们，\n',
            '又回到了从前那样\n',
            '安安稳稳的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x9BF
@scena.Code('func_07_9BF')
def func_07_9BF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_A3E',
    )

    ChrTalk(
        0x001E,
        (
            '#060F终于实现\n',
            '和爷爷一起\n',
            '吃冰淇淋的愿望了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890013V本来还想和阿加特大哥哥\n',
            '一起来这里吃的，\n',
            '结果他生气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B96')

    def _loc_A3E(): pass

    label('loc_A3E')

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))

    ChrTalk(
        0x001E,
        (
            '#060F啊……艾丝蒂尔姐姐和\n',
            '约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F提妲，\n',
            '你好像很开心嘛。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#060F嘿嘿，因为终于实现\n',
            '和爷爷一起\n',
            '吃冰淇淋的愿望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊～真不错呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#060F嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890012V本来还想和阿加特大哥哥\n',
            '一起来这里吃的，\n',
            '结果他生气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F要阿加特吃冰淇淋……\n',
            '哈哈，他会生气也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#060F啊……\n',
            '冰淇淋很好吃的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B96(): pass

    label('loc_B96')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xB9A
@scena.Code('func_08_B9A')
def func_08_B9A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_BE4',
    )

    ChrTalk(
        0x0106,
        (
            '#050F武术大会啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140720V的确是个\n',
            '一试身手的好机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD3')

    def _loc_BE4(): pass

    label('loc_BE4')

    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    ChrTalk(
        0x0106,
        (
            '#050F武术大会啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140714V的确是个\n',
            '一试身手的好机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且那个『不动金』\n',
            '这次也参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140716V#000F明年阿加特\n',
            '你也来参加如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F……哼，虽然是有兴趣，\n',
            '但我可不想被别人看热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是一点都不老实的说法～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD3(): pass

    label('loc_CD3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xCD7
@scena.Code('func_09_CD7')
def func_09_CD7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '由特务兵来镇守王都，\n',
            '王都守卫队却撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难以理解，\n',
            '而且根本不知道\n',
            '是谁下达的这个命令啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xD47
@scena.Code('func_0A_D47')
def func_0A_D47():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_DA8',
    )

    ChrTalk(
        0x00FE,
        (
            '对于最近发生的事情，\n',
            '我们也是一头雾水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之王都的正规军\n',
            '基本上都撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1E')

    def _loc_DA8(): pass

    label('loc_DA8')

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '对于发生的事情，\n',
            '我们也是一头雾水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之王都的正规军\n',
            '基本上都撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '这么一来可如何是好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E1E(): pass

    label('loc_E1E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xE22
@scena.Code('func_0B_E22')
def func_0B_E22():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_E8E',
    )

    ChrTalk(
        0x00FE,
        (
            '政变的发动人\n',
            '竟然是那位理查德上校……\n',
            '让我好震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '能防范于未然实在是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_E8E(): pass

    label('loc_E8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_EDF',
    )

    ChrTalk(
        0x00FE,
        (
            '要发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些王都的守卫队士兵\n',
            '都已经慌忙地撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_EDF(): pass

    label('loc_EDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_F41',
    )

    ChrTalk(
        0x00FE,
        (
            '为了筹备庆典的取材，\n',
            '大家都在忙着做准备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但说实话，\n',
            '庆典到底会怎么样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_F41(): pass

    label('loc_F41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_FAB',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会的优胜者\n',
            '好像是朵洛希认识的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她呀，高兴过头了，\n',
            '一边跳着舞一边跑回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_FAB(): pass

    label('loc_FAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_108B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_100A',
    )

    ChrTalk(
        0x00FE,
        (
            '一大早，\n',
            '朵洛希就拿着照相机\n',
            '跑到竞技场去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看她好像充满干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1088')

    def _loc_100A(): pass

    label('loc_100A')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x00FE,
        (
            '早上好。\n',
            '今天是武术大会总决赛的日子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一大早，\n',
            '朵洛希就拿着照相机\n',
            '跑到竞技场去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看她好像充满干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1088(): pass

    label('loc_1088')

    Jump('loc_131D')

    def _loc_108B(): pass

    label('loc_108B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_10E5',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '王国军的人每天都会过来检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们通讯社\n',
            '并没有做什么坏事对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_10E5(): pass

    label('loc_10E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_11C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_1140',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真是个很棒的男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也好想去\n',
            '对他进行采访取材呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11BE')

    def _loc_1140(): pass

    label('loc_1140')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '真是个很棒的男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '举止文雅，知识渊博，\n',
            '风度翩翩，一表人才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也好想去\n',
            '对他进行采访取材呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11BE(): pass

    label('loc_11BE')

    Jump('loc_131D')

    def _loc_11C1(): pass

    label('loc_11C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1232',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才奈尔记者\n',
            '从外面回来了。\n',
            '感觉有好一阵子没见到他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他这个人啊，\n',
            '经常会突然失踪好几天呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_1232(): pass

    label('loc_1232')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1270',
    )

    ChrTalk(
        0x00FE,
        (
            '本社的记者们\n',
            '白天外出取材，\n',
            '很少呆在通讯社里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_1270(): pass

    label('loc_1270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_12D7',
    )

    ChrTalk(
        0x00FE,
        (
            '下班之后约朵洛希\n',
            '一起去外面玩的计划\n',
            '又泡汤了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别看她那个样子，\n',
            '其实工作很忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131D')

    def _loc_12D7(): pass

    label('loc_12D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_131D',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到利贝尔通讯社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一楼是接待处，\n',
            '二楼是编辑室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_131D(): pass

    label('loc_131D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1321
@scena.Code('func_0C_1321')
def func_0C_1321():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1366',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来就去\n',
            '最近引起热门话题的\n',
            '冰淇淋店进行取材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAE')

    def _loc_1366(): pass

    label('loc_1366')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1422',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_13B7',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔前辈他\n',
            '被军队逮捕了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸亏我是\n',
            '文化专栏的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_141F')

    def _loc_13B7(): pass

    label('loc_13B7')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '奈尔前辈他\n',
            '被军队逮捕了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就知道\n',
            '他迟早会落到如此下场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸亏我是\n',
            '文化专栏的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_141F(): pass

    label('loc_141F')

    Jump('loc_1AAE')

    def _loc_1422(): pass

    label('loc_1422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1518',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1493',
    )

    ChrTalk(
        0x00FE,
        (
            '本打算去到柏斯的\n',
            '『安特洛丝餐厅』取材的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么办啊……\n',
            '只能写一篇别的报道来代替了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1515')

    def _loc_1493(): pass

    label('loc_1493')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '哇呀呀，\n',
            '定期船停飞了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本打算去到柏斯的\n',
            '『安特洛丝餐厅』取材的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么办啊……\n',
            '只能写一篇别的报道来代替了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1515(): pass

    label('loc_1515')

    Jump('loc_1AAE')

    def _loc_1518(): pass

    label('loc_1518')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_163D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1594',
    )

    ChrTalk(
        0x00FE,
        (
            '取材的方式是\n',
            '去美味的店品尝料理，\n',
            '然后展示在文化专栏里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要做出可以向\n',
            '奈尔前辈炫耀的东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_163A')

    def _loc_1594(): pass

    label('loc_1594')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '这次就以现在热门的餐厅\n',
            '为主题作一期特辑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '取材的方式是\n',
            '去美味的店品尝料理，\n',
            '然后展示在文化专栏里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要做出可以向\n',
            '奈尔前辈炫耀的东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_163A(): pass

    label('loc_163A')

    Jump('loc_1AAE')

    def _loc_163D(): pass

    label('loc_163D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1770',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_16B6',
    )

    ChrTalk(
        0x00FE,
        (
            '朵洛希虽说是个新人，\n',
            '不过实力确实非常强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，让她进入我们通讯社的\n',
            '总编的眼光更加令人佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176D')

    def _loc_16B6(): pass

    label('loc_16B6')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '朵洛希虽说是个新人，\n',
            '不过实力确实非常强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是拍武术大会的照片，\n',
            '还是料理的照片，\n',
            '她总能选择最佳的角度去拍摄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，让她进入我们通讯社的\n',
            '总编的眼光更加令人佩服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_176D(): pass

    label('loc_176D')

    Jump('loc_1AAE')

    def _loc_1770(): pass

    label('loc_1770')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_185F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_17CF',
    )

    ChrTalk(
        0x00FE,
        (
            '很多作家或者撰稿人\n',
            '每逢截稿的时间临近\n',
            '就会犯感冒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人头疼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_185C')

    def _loc_17CF(): pass

    label('loc_17CF')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '很多作家或者撰稿人\n',
            '每逢截稿的时间临近\n',
            '就会犯感冒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能是太过拼命，\n',
            '结果把身体弄坏了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再或者就是装病，\n',
            '总之很让人头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_185C(): pass

    label('loc_185C')

    Jump('loc_1AAE')

    def _loc_185F(): pass

    label('loc_185F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1959',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_18C4',
    )

    ChrTalk(
        0x00FE,
        (
            '唉唉，\n',
            '我乘坐定期船去外地取原稿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果到了之后\n',
            '才被作者告知还没有写好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1956')

    def _loc_18C4(): pass

    label('loc_18C4')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '唉唉，\n',
            '我乘坐定期船去外地取原稿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果到了之后\n',
            '才被作者告知还没有写好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果导力通信能够更加普及的话，\n',
            '联络起来就会方便了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1956(): pass

    label('loc_1956')

    Jump('loc_1AAE')

    def _loc_1959(): pass

    label('loc_1959')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1963',
    )

    Jump('loc_1AAE')

    def _loc_1963(): pass

    label('loc_1963')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_19BD',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我要乘坐定期船\n',
            '去外地取原稿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要早点做好准备\n',
            '才不至于延误乘船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAE')

    def _loc_19BD(): pass

    label('loc_19BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A48',
    )

    ChrTalk(
        0x00FE,
        (
            '《利贝尔通讯》的文化专栏\n',
            '是由我来担当编辑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本专栏通常会刊登\n',
            '连载小说和读者的意见，\n',
            '也会对一些热门话题进行取材报道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAE')

    def _loc_1A48(): pass

    label('loc_1A48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1AAE',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '如果不能快点取回作者的原稿，\n',
            '我会被责骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奈尔和诺蒂亚\n',
            '都要比总编严厉许多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AAE(): pass

    label('loc_1AAE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1AB2
@scena.Code('func_0D_1AB2')
def func_0D_1AB2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1AE6',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '这次又麻烦奈尔帮我的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A8')

    def _loc_1AE6(): pass

    label('loc_1AE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1B0C',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的情况很奇怪呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A8')

    def _loc_1B0C(): pass

    label('loc_1B0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1B8F',
    )

    ChrTalk(
        0x00FE,
        (
            '奈尔从刚来杂志社的时候\n',
            '就会做些让人目瞪口呆的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过大概正因为如此，\n',
            '才能抢在别人之前\n',
            '报道一些独家新闻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A8')

    def _loc_1B8F(): pass

    label('loc_1B8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1C8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1BEC',
    )

    ChrTalk(
        0x00FE,
        (
            '那个狐狸眼睛的女上尉，\n',
            '实在让人生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管走到哪里\n',
            '都要挖苦别人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C88')

    def _loc_1BEC(): pass

    label('loc_1BEC')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '理查德上校是很不错，\n',
            '但情报部和特务兵\n',
            '那些家伙就不敢恭维了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是那个\n',
            '长着狐狸眼睛的女上尉，\n',
            '实在让人生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管走到哪里\n',
            '都要挖苦别人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C88(): pass

    label('loc_1C88')

    Jump('loc_21A8')

    def _loc_1C8B(): pass

    label('loc_1C8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1CFF',
    )

    ChrTalk(
        0x00FE,
        (
            '呼呼，情报部的监视非常严，\n',
            '取材也寸步难行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们这样做，\n',
            '和当年埃雷波尼亚帝国的宪兵有什么区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A8')

    def _loc_1CFF(): pass

    label('loc_1CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1E2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1D8C',
    )

    ChrTalk(
        0x00FE,
        (
            '我和奈尔常常都会\n',
            '围绕着杂志报道方针的问题\n',
            '与总编极力争辩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总编总能以\n',
            '一副笑脸哄着我们，\n',
            '我们很吃他的怀柔政策呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E29')

    def _loc_1D8C(): pass

    label('loc_1D8C')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '总编是一个不可思议的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和奈尔常常都会\n',
            '围绕着杂志报道方针的问题\n',
            '与总编极力争辩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总编总能以\n',
            '一副笑脸哄着我们，\n',
            '我们很吃他的怀柔政策呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E29(): pass

    label('loc_1E29')

    Jump('loc_21A8')

    def _loc_1E2C(): pass

    label('loc_1E2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F0E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1E8D',
    )

    ChrTalk(
        0x00FE,
        (
            '直到今天早上\n',
            '奈尔还在调查什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是发现了什么\n',
            '好的新闻线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0B')

    def _loc_1E8D(): pass

    label('loc_1E8D')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '直到今天早上\n',
            '奈尔还在调查什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是发现了什么\n',
            '好的新闻线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～作为前辈，\n',
            '我也不能就这样输给他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F0B(): pass

    label('loc_1F0B')

    Jump('loc_21A8')

    def _loc_1F0E(): pass

    label('loc_1F0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1F88',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '大会今年改成了团体赛，\n',
            '想拍摄好的确很困难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能的话，\n',
            '真想找个好一点的摄影师\n',
            '来替我拍摄啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A8')

    def _loc_1F88(): pass

    label('loc_1F88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2047',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1FDC',
    )

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯正在准备\n',
            '出版武术大会的特刊哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要努力取材啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2044')

    def _loc_1FDC(): pass

    label('loc_1FDC')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '今天终于到大会的正式赛了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔通讯正在准备\n',
            '出版武术大会的特刊哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要努力取材啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2044(): pass

    label('loc_2044')

    Jump('loc_21A8')

    def _loc_2047(): pass

    label('loc_2047')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_213D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_20A8',
    )

    ChrTalk(
        0x00FE,
        (
            '还是老样子，\n',
            '奈尔又是一去不复返。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚回来没多久，\n',
            '就立刻又飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213A')

    def _loc_20A8(): pass

    label('loc_20A8')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '还是老样子，\n',
            '奈尔又是一去不复返。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚回来没多久，\n',
            '就立刻又飞奔出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他脸色不太健康是因为吸烟的缘故，\n',
            '但体力至少是常人的一倍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_213A(): pass

    label('loc_213A')

    Jump('loc_21A8')

    def _loc_213D(): pass

    label('loc_213D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_21A8',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，真是的，\n',
            '再不快点，预选赛就要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，器材带上了，\n',
            '取材用的通行许可证也带上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21A8(): pass

    label('loc_21A8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x21AC
@scena.Code('func_0E_21AC')
def func_0E_21AC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2377',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_2228',
    )

    ChrTalk(
        0x0110,
        (
            '#0280140863V#150F对了，奈尔前辈\n',
            '告诉我了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280140864V因为这次的报道，\n',
            '前辈和我很有可能会获得\n',
            '菲利策奖哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2374')

    def _loc_2228(): pass

    label('loc_2228')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0110,
        (
            '#150F啊，是小艾你们啊～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，奈尔前辈\n',
            '告诉我了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280140864V因为这次的报道，\n',
            '前辈和我很有可能会获得\n',
            '菲利策奖哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F菲利策？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140866V#010F在新闻、文学和音乐等领域\n',
            '取得年度最佳成绩的人\n',
            '被授予的奖项。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140867V对于记者而言\n',
            '毫无疑问是最高荣誉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊～真不错呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#150F嘿嘿嘿，这也是\n',
            '托小艾你们的福啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2374(): pass

    label('loc_2374')

    Jump('loc_252B')

    def _loc_2377(): pass

    label('loc_2377')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_23B2',
    )

    ChrTalk(
        0x0110,
        (
            '#150F呜～哇！\n',
            '奈尔前辈还活着，\n',
            '真是太好了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_23B2(): pass

    label('loc_23B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_23FD',
    )

    ChrTalk(
        0x0110,
        (
            '#150F啊，拜托了～！\n',
            '小艾～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130359V一定要救救奈尔前辈～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_23FD(): pass

    label('loc_23FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_24E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_245B',
    )

    ChrTalk(
        0x0110,
        (
            '#0281080007V#150F虽然总编让我\n',
            '去找奈尔前辈～……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130362V但上哪去找呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E5')

    def _loc_245B(): pass

    label('loc_245B')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x0110,
        (
            '#0280111976V#150F呀，是小艾你们啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111977V恭喜你们获得优胜～\n',
            '比赛真是很精彩啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280111978V我太兴奋了，\n',
            '我拍了好多照片，\n',
            '请你们期待哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E5(): pass

    label('loc_24E5')

    Jump('loc_252B')

    def _loc_24E8(): pass

    label('loc_24E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_24F2',
    )

    Jump('loc_252B')

    def _loc_24F2(): pass

    label('loc_24F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_24FC',
    )

    Jump('loc_252B')

    def _loc_24FC(): pass

    label('loc_24FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2506',
    )

    Jump('loc_252B')

    def _loc_2506(): pass

    label('loc_2506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2510',
    )

    Jump('loc_252B')

    def _loc_2510(): pass

    label('loc_2510')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_251A',
    )

    Jump('loc_252B')

    def _loc_251A(): pass

    label('loc_251A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2524',
    )

    Jump('loc_252B')

    def _loc_2524(): pass

    label('loc_2524')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_252B',
    )

    def _loc_252B(): pass

    label('loc_252B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x252F
@scena.Code('func_0F_252F')
def func_0F_252F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_26B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_25A7',
    )

    ChrTalk(
        0x010F,
        (
            '#140F对你们的采访\n',
            '读者的反响尤为强烈呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140878V如果以后有什么有趣的消息，\n',
            '还要靠你们提供了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26B5')

    def _loc_25A7(): pass

    label('loc_25A7')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x010F,
        (
            '#140F哟，艾丝蒂尔、约修亚！\n',
            '这次你们真是出尽风头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140873V多亏了你们，\n',
            '这次与政变相关的特刊简直卖疯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了对了，你们的\n',
            '读者的反响尤为强烈呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不管怎么说你们也是\n',
            '阻止了理查德上校\n',
            '政变阴谋的小小英雄呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270140878V如果以后有什么有趣的消息，\n',
            '还要靠你们提供了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26B5(): pass

    label('loc_26B5')

    Jump('loc_2719')

    def _loc_26B8(): pass

    label('loc_26B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_26C2',
    )

    Jump('loc_2719')

    def _loc_26C2(): pass

    label('loc_26C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_26CC',
    )

    Jump('loc_2719')

    def _loc_26CC(): pass

    label('loc_26CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_26D6',
    )

    Jump('loc_2719')

    def _loc_26D6(): pass

    label('loc_26D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_26E0',
    )

    Jump('loc_2719')

    def _loc_26E0(): pass

    label('loc_26E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_26EA',
    )

    Jump('loc_2719')

    def _loc_26EA(): pass

    label('loc_26EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_26F4',
    )

    Jump('loc_2719')

    def _loc_26F4(): pass

    label('loc_26F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_26FE',
    )

    Jump('loc_2719')

    def _loc_26FE(): pass

    label('loc_26FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2708',
    )

    Jump('loc_2719')

    def _loc_2708(): pass

    label('loc_2708')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2712',
    )

    Jump('loc_2719')

    def _loc_2712(): pass

    label('loc_2712')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2719',
    )

    def _loc_2719(): pass

    label('loc_2719')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x271D
@scena.Code('func_10_271D')
def func_10_271D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2850',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_27AA',
    )

    ChrTalk(
        0x00FE,
        (
            '连游击士和亲卫队\n',
            '攻入城内的场面都有，\n',
            '这部分报道相当有魄力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来《利贝尔通讯》的发行量\n',
            '又要大幅上涨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_284D')

    def _loc_27AA(): pass

    label('loc_27AA')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '很久没有看到过\n',
            '如此精彩的报道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连游击士和亲卫队\n',
            '攻入城内的场面都有，\n',
            '这部分报道相当有魄力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来《利贝尔通讯》的发行量\n',
            '又要大幅上涨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_284D(): pass

    label('loc_284D')

    Jump('loc_2C09')

    def _loc_2850(): pass

    label('loc_2850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_28BF',
    )

    ChrTalk(
        0x00FE,
        (
            '这几天阅读了\n',
            '很多书籍和新闻，\n',
            '从中得到了不少启示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我们看不见的地方，\n',
            '似乎正有暗流涌动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_28BF(): pass

    label('loc_28BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_292D',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得亲卫队的人们\n',
            '虽然有些作风古板……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那种高雅的气质和举止\n',
            '看上去就让人心情很愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_292D(): pass

    label('loc_292D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_299B',
    )

    ChrTalk(
        0x00FE,
        (
            '关于女王病情的详情，\n',
            '现在也没有对外发表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '陛下本人也没有作出声明，\n',
            '我怀疑真的是生病了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_299B(): pass

    label('loc_299B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_29D8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～对于我来说，\n',
            '喝杯咖啡就能驱散早晨的困倦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_29D8(): pass

    label('loc_29D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2A0E',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '士兵为什么都那样\n',
            '粗暴不知礼节呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_2A0E(): pass

    label('loc_2A0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2A36',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，书籍是心灵的养料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_2A36(): pass

    label('loc_2A36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2AA5',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的老板以前\n',
            '是外交使节的一员呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为工作关系，\n',
            '他好像去过帝国、共和国\n',
            '等等很多的国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_2AA5(): pass

    label('loc_2AA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2AE2',
    )

    ChrTalk(
        0x00FE,
        (
            '我是属于那种只要知道\n',
            '比赛结果就满足了的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C09')

    def _loc_2AE2(): pass

    label('loc_2AE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2BAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2B3C',
    )

    ChrTalk(
        0x00FE,
        (
            '最近的《利贝尔通讯》\n',
            '给人的感觉有些平淡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一点都不让人吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BA9')

    def _loc_2B3C(): pass

    label('loc_2B3C')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '最近《利贝尔通讯》\n',
            '给人的感觉有些平淡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基本上都是\n',
            '普普通通的新闻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一点都不让人吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BA9(): pass

    label('loc_2BA9')

    Jump('loc_2C09')

    def _loc_2BAC(): pass

    label('loc_2BAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2C09',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，这个地方很舒适嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里一边喝咖啡\n',
            '一边看书的话，\n',
            '时间很快就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C09(): pass

    label('loc_2C09')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2C0D
@scena.Code('func_11_2C0D')
def func_11_2C0D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2C98',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '没想到表面上是在召开武术大会，\n',
            '暗地里却是在策划政变。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来，\n',
            '像理查德上校这样的人\n',
            '怎么还会感到不满足呢。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3330')

    def _loc_2C98(): pass

    label('loc_2C98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2D90',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2D01',
    )

    ChrTalk(
        0x00FE,
        (
            '我感到军队的警戒\n',
            '好像又提高了一个层次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这件事事先也没有\n',
            '向我们市民通知一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D8D')

    def _loc_2D01(): pass

    label('loc_2D01')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '我感到军队的警戒\n',
            '好像又提高了一个层次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这件事事先也没有\n',
            '向我们市民通知一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没有发生什么事情，\n',
            '但总是觉得有些不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D8D(): pass

    label('loc_2D8D')

    Jump('loc_3330')

    def _loc_2D90(): pass

    label('loc_2D90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2E8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2DF9',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才来的特务兵\n',
            '嘴里嘟囔个不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于搜捕亲卫队的事，\n',
            '市民好像不是很配合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E87')

    def _loc_2DF9(): pass

    label('loc_2DF9')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '刚才来的特务兵\n',
            '嘴里嘟囔个不停……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于搜捕亲卫队的事，\n',
            '市民好像不是很配合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，主要还是因为\n',
            '亲卫队平时很受大家欢迎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E87(): pass

    label('loc_2E87')

    Jump('loc_3330')

    def _loc_2E8A(): pass

    label('loc_2E8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2EF4',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会的优胜者\n',
            '好像已经产生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王城里的利贝尔宫廷料理\n',
            '可都是十分丰盛的，好羡慕呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3330')

    def _loc_2EF4(): pass

    label('loc_2EF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2F8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2F3A',
    )

    ChrTalk(
        0x00FE,
        (
            '各位客人要不要尝尝\n',
            '本店引以为荣的『浓缩咖啡』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8A')

    def _loc_2F3A(): pass

    label('loc_2F3A')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '你们好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位客人要不要尝尝\n',
            '本店引以为荣的『浓缩咖啡』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F8A(): pass

    label('loc_2F8A')

    Jump('loc_3330')

    def _loc_2F8D(): pass

    label('loc_2F8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3089',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3001',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才来的士兵说什么\n',
            '晚上９点以后严禁外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，\n',
            '还是早些关店门，\n',
            '听听音乐休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3086')

    def _loc_3001(): pass

    label('loc_3001')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '王国军的士兵们到店里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们说什么\n',
            '晚上９点以后严禁外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，\n',
            '还是早些关店门，\n',
            '听听音乐休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3086(): pass

    label('loc_3086')

    Jump('loc_3330')

    def _loc_3089(): pass

    label('loc_3089')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_311B',
    )

    ChrTalk(
        0x00FE,
        (
            '这个西街区，\n',
            '在王都格兰赛尔的街区当中\n',
            '也算是相当安静的区域了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了要开这家店，\n',
            '我曾经到处寻找地方，\n',
            '最后发现还是这里最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3330')

    def _loc_311B(): pass

    label('loc_311B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3222',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3180',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '我过去因为工作的关系\n',
            '到过好多的国家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，饮食文化真是深奥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_321F')

    def _loc_3180(): pass

    label('loc_3180')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '我过去因为工作的关系\n',
            '到过好多的国家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时可以说\n',
            '吃遍了各国的美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里卖的咖喱饭\n',
            '就是其中一种哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，饮食文化真是深奥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_321F(): pass

    label('loc_321F')

    Jump('loc_3330')

    def _loc_3222(): pass

    label('loc_3222')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_327C',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你们请随便坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店会让顾客\n',
            '享受到宾至如归\n',
            '而又舒适悠闲的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3330')

    def _loc_327C(): pass

    label('loc_327C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_32F6',
    )

    ChrTalk(
        0x00FE,
        (
            '旁边的建筑就是现在大受欢迎的\n',
            '《利贝尔通讯》的出版社办公楼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的记者和编辑\n',
            '也常到这里来吃饭休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3330')

    def _loc_32F6(): pass

    label('loc_32F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3330',
    )

    ChrTalk(
        0x00FE,
        (
            '你们，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欢迎来到\n',
            '巴拉尔咖啡厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3330(): pass

    label('loc_3330')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x3334
@scena.Code('func_12_3334')
def func_12_3334():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_333E',
    )

    Jump('loc_3461')

    def _loc_333E(): pass

    label('loc_333E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3394',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '那么一会儿去吃冰淇淋如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我知道有一家店的\n',
            '冰淇淋很好吃哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3461')

    def _loc_3394(): pass

    label('loc_3394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_33C0',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典之前都没什么事做呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3461')

    def _loc_33C0(): pass

    label('loc_33C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_341E',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '我觉得明年肯定会变回个人战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话～\n',
            '我只给约修亚君一个人加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3461')

    def _loc_341E(): pass

    label('loc_341E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3428',
    )

    Jump('loc_3461')

    def _loc_3428(): pass

    label('loc_3428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3432',
    )

    Jump('loc_3461')

    def _loc_3432(): pass

    label('loc_3432')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_343C',
    )

    Jump('loc_3461')

    def _loc_343C(): pass

    label('loc_343C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3446',
    )

    Jump('loc_3461')

    def _loc_3446(): pass

    label('loc_3446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3450',
    )

    Jump('loc_3461')

    def _loc_3450(): pass

    label('loc_3450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_345A',
    )

    Jump('loc_3461')

    def _loc_345A(): pass

    label('loc_345A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3461',
    )

    def _loc_3461(): pass

    label('loc_3461')

    Return()

# id: 0x0013 offset: 0x3462
@scena.Code('func_13_3462')
def func_13_3462():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_346C',
    )

    Jump('loc_3563')

    def _loc_346C(): pass

    label('loc_346C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_34A4',
    )

    ChrTalk(
        0x00FE,
        (
            '超级不爽啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在要做些什么好呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3563')

    def _loc_34A4(): pass

    label('loc_34A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_34F3',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '诞辰庆典真的会如期举办吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下似乎病了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3563')

    def _loc_34F3(): pass

    label('loc_34F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3520',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '洛伦斯大人竟然输掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3563')

    def _loc_3520(): pass

    label('loc_3520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_352A',
    )

    Jump('loc_3563')

    def _loc_352A(): pass

    label('loc_352A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3534',
    )

    Jump('loc_3563')

    def _loc_3534(): pass

    label('loc_3534')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_353E',
    )

    Jump('loc_3563')

    def _loc_353E(): pass

    label('loc_353E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3548',
    )

    Jump('loc_3563')

    def _loc_3548(): pass

    label('loc_3548')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3552',
    )

    Jump('loc_3563')

    def _loc_3552(): pass

    label('loc_3552')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_355C',
    )

    Jump('loc_3563')

    def _loc_355C(): pass

    label('loc_355C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3563',
    )

    def _loc_3563(): pass

    label('loc_3563')

    Return()

# id: 0x0014 offset: 0x3564
@scena.Code('func_14_3564')
def func_14_3564():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3571',
    )

    Jump('loc_361A')

    def _loc_3571(): pass

    label('loc_3571')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_357B',
    )

    Jump('loc_361A')

    def _loc_357B(): pass

    label('loc_357B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3585',
    )

    Jump('loc_361A')

    def _loc_3585(): pass

    label('loc_3585')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_35D7',
    )

    ChrTalk(
        0x00FE,
        (
            '金小组，\n',
            '优胜万岁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后的最后，\n',
            '还是我支持的队伍取得了胜利！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_361A')

    def _loc_35D7(): pass

    label('loc_35D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_35E1',
    )

    Jump('loc_361A')

    def _loc_35E1(): pass

    label('loc_35E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_35EB',
    )

    Jump('loc_361A')

    def _loc_35EB(): pass

    label('loc_35EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_35F5',
    )

    Jump('loc_361A')

    def _loc_35F5(): pass

    label('loc_35F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_35FF',
    )

    Jump('loc_361A')

    def _loc_35FF(): pass

    label('loc_35FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3609',
    )

    Jump('loc_361A')

    def _loc_3609(): pass

    label('loc_3609')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3613',
    )

    Jump('loc_361A')

    def _loc_3613(): pass

    label('loc_3613')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_361A',
    )

    def _loc_361A(): pass

    label('loc_361A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x361E
@scena.Code('func_15_361E')
def func_15_361E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_362B',
    )

    Jump('loc_3778')

    def _loc_362B(): pass

    label('loc_362B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3635',
    )

    Jump('loc_3778')

    def _loc_3635(): pass

    label('loc_3635')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_363F',
    )

    Jump('loc_3778')

    def _loc_363F(): pass

    label('loc_363F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3735',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_36AC',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我和他都支持同一个小组，\n',
            '所以很合得来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比赛结束之后\n',
            '我们就来这里一起喝酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3732')

    def _loc_36AC(): pass

    label('loc_36AC')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '因为我和他都支持同一个小组，\n',
            '所以很合得来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比赛结束之后\n',
            '我们就来这里一起喝酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天肯定也会彻夜狂欢吧。\n',
            '哈哈哈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3732(): pass

    label('loc_3732')

    Jump('loc_3778')

    def _loc_3735(): pass

    label('loc_3735')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_373F',
    )

    Jump('loc_3778')

    def _loc_373F(): pass

    label('loc_373F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3749',
    )

    Jump('loc_3778')

    def _loc_3749(): pass

    label('loc_3749')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3753',
    )

    Jump('loc_3778')

    def _loc_3753(): pass

    label('loc_3753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_375D',
    )

    Jump('loc_3778')

    def _loc_375D(): pass

    label('loc_375D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3767',
    )

    Jump('loc_3778')

    def _loc_3767(): pass

    label('loc_3767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3771',
    )

    Jump('loc_3778')

    def _loc_3771(): pass

    label('loc_3771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3778',
    )

    def _loc_3778(): pass

    label('loc_3778')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x377C
@scena.Code('func_16_377C')
def func_16_377C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3789',
    )

    Jump('loc_3A06')

    def _loc_3789(): pass

    label('loc_3789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3793',
    )

    Jump('loc_3A06')

    def _loc_3793(): pass

    label('loc_3793')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_379D',
    )

    Jump('loc_3A06')

    def _loc_379D(): pass

    label('loc_379D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_37A7',
    )

    Jump('loc_3A06')

    def _loc_37A7(): pass

    label('loc_37A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_37B1',
    )

    Jump('loc_3A06')

    def _loc_37B1(): pass

    label('loc_37B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_38BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3831',
    )

    ChrTalk(
        0x0104,
        (
            '#030F哎呀，和雪拉君\n',
            '可不是在这样的\n',
            '节奏和气氛下喝酒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141620V和她喝酒的时候，\n',
            '总有一种欲生欲死的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38B8')

    def _loc_3831(): pass

    label('loc_3831')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0104,
        (
            '#030F哈·哈·哈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141619V哎呀，和雪拉君\n',
            '可不是在这样的\n',
            '节奏和气氛下喝酒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141620V和她喝酒的时候，\n',
            '总有一种欲生欲死的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38B8(): pass

    label('loc_38B8')

    Jump('loc_3A06')

    def _loc_38BB(): pass

    label('loc_38BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_38C5',
    )

    Jump('loc_3A06')

    def _loc_38C5(): pass

    label('loc_38C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_39AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3931',
    )

    ChrTalk(
        0x0104,
        (
            '#0041050010V#030F呵，食物可以滋润心灵，\n',
            '创造生命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141627V哎呀呀，厨师真是\n',
            '伟大的存在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39A9')

    def _loc_3931(): pass

    label('loc_3931')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0104,
        (
            '#030F哈·哈·哈，\n',
            '夜幕降临了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141624V来吧，继续畅饮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F奥利维尔明明这么瘦，\n',
            '为什么能装下那么多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39A9(): pass

    label('loc_39A9')

    Jump('loc_3A06')

    def _loc_39AC(): pass

    label('loc_39AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_39B6',
    )

    Jump('loc_3A06')

    def _loc_39B6(): pass

    label('loc_39B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_39FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_39FC',
    )

    ChrTalk(
        0x0104,
        (
            '#030F唔，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040141629V青春诚短暂，恋爱吧少女……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39FC(): pass

    label('loc_39FC')

    Jump('loc_3A06')

    def _loc_39FF(): pass

    label('loc_39FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3A06',
    )

    def _loc_3A06(): pass

    label('loc_3A06')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x3A0A
@scena.Code('func_17_3A0A')
def func_17_3A0A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3CB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3A83',
    )

    ChrTalk(
        0x0010,
        (
            '#0080140711V#070F我打算暂时留在这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140712V难得来到这里，\n',
            '等和各位高手较量过之后\n',
            '再回国也不迟嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CB1')

    def _loc_3A83(): pass

    label('loc_3A83')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0010,
        (
            '#070F哟，是你们俩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140698V#010F金大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140699V#000F对了，金大哥你\n',
            '接下来准备做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140700V真的要回去共和国吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080140701V#070F不，在共和国\n',
            '没有发生什么大事，\n',
            '我准备在这儿呆一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140702V这个国家有几位\n',
            '很著名的年轻游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难得来到这里，\n',
            '等和他们切磋了技艺之后\n',
            '再回国也不迟嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F著名的游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#070F是啊……\n',
            '首先是对面的『重剑阿加特』，\n',
            '然后是『银闪雪拉扎德』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140706V而且……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一定得和你们俩\n',
            '也较量一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇，这真有些难为情啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，我很期待！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140710V#010F到时候\n',
            '还要请您手下留情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CB1(): pass

    label('loc_3CB1')

    Jump('loc_3E5C')

    def _loc_3CB4(): pass

    label('loc_3CB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3CBE',
    )

    Jump('loc_3E5C')

    def _loc_3CBE(): pass

    label('loc_3CBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3CC8',
    )

    Jump('loc_3E5C')

    def _loc_3CC8(): pass

    label('loc_3CC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3CD2',
    )

    Jump('loc_3E5C')

    def _loc_3CD2(): pass

    label('loc_3CD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3CDC',
    )

    Jump('loc_3E5C')

    def _loc_3CDC(): pass

    label('loc_3CDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3D2A',
    )

    ChrTalk(
        0x0010,
        (
            '#0080111471V#070F明天就是决赛了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111472V记得多吃点，\n',
            '睡个好觉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E5C')

    def _loc_3D2A(): pass

    label('loc_3D2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3D34',
    )

    Jump('loc_3E5C')

    def _loc_3D34(): pass

    label('loc_3D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3E41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3D74',
    )

    ChrTalk(
        0x0010,
        (
            '#0080111478V#070F嗝，怎么样？\n',
            '你们也来喝吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E3E')

    def _loc_3D74(): pass

    label('loc_3D74')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0010,
        (
            '#0080111473V#070F哦哦～！\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111474V怎么样？\n',
            '你们也来喝吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111475V#000F我们可是未成年人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080111476V#070F什么，不喝\n',
            '我的酒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111477V#010F哈哈，好像已经\n',
            '完全喝醉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E3E(): pass

    label('loc_3E3E')

    Jump('loc_3E5C')

    def _loc_3E41(): pass

    label('loc_3E41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3E4B',
    )

    Jump('loc_3E5C')

    def _loc_3E4B(): pass

    label('loc_3E4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3E55',
    )

    Jump('loc_3E5C')

    def _loc_3E55(): pass

    label('loc_3E55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3E5C',
    )

    def _loc_3E5C(): pass

    label('loc_3E5C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x3E60
@scena.Code('func_18_3E60')
def func_18_3E60():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3F6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3EE1',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然是理查德上校\n',
            '策动的这起政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前接受杂志的访谈\n',
            '说的那些了不起的话，\n',
            '也只是表面文章而已吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F69')

    def _loc_3EE1(): pass

    label('loc_3EE1')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '竟然是理查德上校\n',
            '策动的这起政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前接受杂志的访谈\n',
            '说的那些了不起的话，\n',
            '也只是表面文章而已吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想到就觉得震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F69(): pass

    label('loc_3F69')

    Jump('loc_4679')

    def _loc_3F6C(): pass

    label('loc_3F6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3FC6',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道为什么，\n',
            '总觉得街上的气氛很怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉像是\n',
            '暴风雨来临之前的宁静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_3FC6(): pass

    label('loc_3FC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4028',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典马上就到了，\n',
            '王城里面如果能快点\n',
            '发布公告就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不要这样就中止啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_4028(): pass

    label('loc_4028')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4090',
    )

    ChrTalk(
        0x00FE,
        (
            '大会明明都结束了，\n',
            '士兵的数量却一点也没有减少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下又身体欠佳，\n',
            '真是不吉利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_4090(): pass

    label('loc_4090')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4181',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4103',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天晚上满街都是士兵，\n',
            '回家的时候被他们叫住了四次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道我的样子\n',
            '真的像是一个坏人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_417E')

    def _loc_4103(): pass

    label('loc_4103')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上满街都是士兵，\n',
            '回家的时候被他们叫住了四次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道我的样子\n',
            '真的像是一个坏人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人泄气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_417E(): pass

    label('loc_417E')

    Jump('loc_4679')

    def _loc_4181(): pass

    label('loc_4181')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4202',
    )

    ChrTalk(
        0x00FE,
        (
            '自从《利贝尔通讯》刊登采访以来，\n',
            '理查德上校的人气\n',
            '最近一段时间急剧上升啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论男女老少，\n',
            '支持他的人都很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_4202(): pass

    label('loc_4202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_426E',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然『巴拉尔』咖啡厅的\n',
            '帝国风味早点也很不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我更喜欢这个店里的\n',
            '利贝尔风味的早餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_426E(): pass

    label('loc_426E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4370',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_42E1',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '难道说造成柏斯混乱的空贼\n',
            '也参加了比武大会吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们不在监狱服役，这样好吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_436D')

    def _loc_42E1(): pass

    label('loc_42E1')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '难道说造成柏斯混乱的空贼\n',
            '也参加了比武大会吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他们的确很有实力，\n',
            '比赛也很有意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是不在监狱服役好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_436D(): pass

    label('loc_436D')

    Jump('loc_4679')

    def _loc_4370(): pass

    label('loc_4370')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_44CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_440A',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会原本是军人用来\n',
            '展示武技和进行演习的活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从现在的女王陛下继位以来，\n',
            '就逐渐转变成普通民众\n',
            '也可以参与的开放式比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44CC')

    def _loc_440A(): pass

    label('loc_440A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '武术大会原本是军人用来\n',
            '展示武技和进行演习的活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从现在的女王陛下继位以来，\n',
            '就逐渐转变成普通民众\n',
            '也可以参与的开放式比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那个时候开始，\n',
            '普通民众也可以\n',
            '报名参加大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44CC(): pass

    label('loc_44CC')

    Jump('loc_4679')

    def _loc_44CF(): pass

    label('loc_44CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4538',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会变更为团体赛，\n',
            '这还是头一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是那个\n',
            '差劲公爵出的主意，\n',
            '不过也算挺有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_4538(): pass

    label('loc_4538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4679',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_456E',
    )

    ChrTalk(
        0x00FE,
        (
            '哎哟，\n',
            '吓得我被通心粉给哽住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_456E(): pass

    label('loc_456E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_45D3',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队因为有制造恐怖活动的嫌疑，\n',
            '正在被王国军追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这类事情还真是接连不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4679')

    def _loc_45D3(): pass

    label('loc_45D3')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '亲卫队因为有制造恐怖活动的嫌疑，\n',
            '正在被王国军追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯的空贼带来的混乱，\n',
            '卢安的市长被捕事件，\n',
            '蔡斯的导力停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这类事情还真是接连不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4679(): pass

    label('loc_4679')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x467D
@scena.Code('func_19_467D')
def func_19_467D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4759',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_46C8',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然发生了许多事情，\n',
            '但现在终于可以平静地生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4756')

    def _loc_46C8(): pass

    label('loc_46C8')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '看到女王陛下健康的样子，\n',
            '我就放心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亲卫队的嫌疑\n',
            '也只是被人嫁祸了而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然发生了许多事情，\n',
            '但现在可以平静地生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4756(): pass

    label('loc_4756')

    Jump('loc_4C88')

    def _loc_4759(): pass

    label('loc_4759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_47A6',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有几个士兵\n',
            '慌慌张张跑过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底会发生什么事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_47A6(): pass

    label('loc_47A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_480F',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '在街上能看到很多士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亲卫队的人策划了\n',
            '这次的恐怖事件的说法\n',
            '果然是真的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_480F(): pass

    label('loc_480F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_486A',
    )

    ChrTalk(
        0x00FE,
        (
            '今天奥利维尔先生没有来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说他们取得了优胜，\n',
            '本来想特地庆贺一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_486A(): pass

    label('loc_486A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_48D9',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我也想去竞技场看比赛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干我们这种工作，\n',
            '在别人在玩乐的时候，\n',
            '自己却非要工作不可啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_48D9(): pass

    label('loc_48D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_493E',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '王国军的人来了，\n',
            '告诉我说只能营业到晚上９点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '难得最近的生意那么好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_493E(): pass

    label('loc_493E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_49B5',
    )

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生，\n',
            '你们今天要参加武术大会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我往年支持的亲卫队\n',
            '今年不能来参加，\n',
            '所以就给你们加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_49B5(): pass

    label('loc_49B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_49FA',
    )

    ChrTalk(
        0x00FE,
        (
            '第一天的比赛\n',
            '好像已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果究竟如何呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_49FA(): pass

    label('loc_49FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4AE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4A43',
    )

    ChrTalk(
        0x00FE,
        (
            '你们都是奥利维尔先生的朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比赛要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AE6')

    def _loc_4A43(): pass

    label('loc_4A43')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎呀，奥利维尔先生，\n',
            '昨天撞到的头没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F哈·哈·哈，你看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我那充满世间博爱的\n',
            '热烈心跳将会\n',
            '持续到永恒的那一刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，看来是没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AE6(): pass

    label('loc_4AE6')

    Jump('loc_4C88')

    def _loc_4AE9(): pass

    label('loc_4AE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4BA3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_4B67',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀……仔细看看，\n',
            '这不是经常在这里演奏的\n',
            '奥利维尔先生吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又是因为对女性纠缠不休\n',
            '而被打飞的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BA0')

    def _loc_4B67(): pass

    label('loc_4B67')

    ChrTalk(
        0x00FE,
        (
            '大会的预选赛好像已经结束了。\n',
            '这里客人立刻多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BA0(): pass

    label('loc_4BA0')

    Jump('loc_4C88')

    def _loc_4BA3(): pass

    label('loc_4BA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4C88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4C00',
    )

    ChrTalk(
        0x00FE,
        (
            '说亲卫队的人是\n',
            '恐怖分子什么的，\n',
            '我难以相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是哪里搞错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C88')

    def _loc_4C00(): pass

    label('loc_4C00')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '说亲卫队的人是\n',
            '恐怖分子什么的，\n',
            '我难以相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说他们很少到这里来，\n',
            '但我知道他们都是很正直的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是哪里搞错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C88(): pass

    label('loc_4C88')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x4C8C
@scena.Code('func_1A_4C8C')
def func_1A_4C8C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4E5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4D10',
    )

    ChrTalk(
        0x00FE,
        (
            '立下了那么多功绩，\n',
            '你们俩现在已经是\n',
            '优秀的正游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330140723V不要就此满足，\n',
            '要向更高的目标发起冲击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E5C')

    def _loc_4D10(): pass

    label('loc_4D10')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哟，\n',
            '这回的事件解决得不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '立下了那么多功绩，\n',
            '你们俩现在已经是\n',
            '优秀的正游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330140723V不要就此满足，\n',
            '要向更高的目标发起冲击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140724V#000F嘿嘿，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140725V#010F克鲁茨大哥，\n',
            '你的身体已经没什么大碍了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '你看看，棒得很啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '遗憾的是……\n',
            '到底是谁消除了我的记忆，\n',
            '我怎么也想不起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E5C(): pass

    label('loc_4E5C')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x4E60
@scena.Code('func_1B_4E60')
def func_1B_4E60():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_522F',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 3930, 0, -620, 0)
    SetChrPos(0x0102, 5070, 0, -540, 0)
    SetChrPos(0x0108, 4540, 0, -1430, 0)
    ChrTurnDirection(0x000C, 0x0108, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 2, 0x64A))
    CameraMove(4720, 0, 250, 1000)

    ChrTalk(
        0x0101,
        (
            '#000F库拉茨大哥，终于找到你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哦，\n',
            '优胜组出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '晚宴后应该在城里住住吧，\n',
            '怎么这么快就回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310130103V想必一定是吃了\n',
            '不少美味佳肴吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F的确是很美味……\n',
            '不过远非如此简单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '远非如此？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把至今为止发生的事情\n',
            '和女王的委托\n',
            '依次予以说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000C,
        (
            '…………………………\n',
            '……喂喂，没搞错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F很可惜，\n',
            '确实是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130108V我可以用我的称号作为赌注。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '『不动金』……\n',
            '你所担保的事情\n',
            '肯定是勿庸置疑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#824F『不动金』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你所担保的事情\n',
            '肯定是勿庸置疑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#823F好，我明白了，\n',
            '让我也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F谢谢你，库拉茨大哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F首先要召开作战会议，\n',
            '请回游击士协会去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130114V大家都会集中在那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '明白了，待会儿见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_518A')
    def lambda_518A():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_518A')

    DispatchAsync2(0x0101, 0x0001, lambda_518A)

    @scena.Lambda('lambda_519B')
    def lambda_519B():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_519B')

    DispatchAsync2(0x0102, 0x0001, lambda_519B)

    @scena.Lambda('lambda_51AC')
    def lambda_51AC():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_51AC')

    DispatchAsync2(0x0108, 0x0001, lambda_51AC)

    ChrWalkTo(0x000C, 3050, 0, 30, 3000, 0x00)
    ChrWalkTo(0x000C, 1030, 0, -3070, 3000, 0x00)
    ChrWalkTo(0x000C, 710, -250, -5490, 3000, 0x00)

    @scena.Lambda('lambda_51F9')
    def lambda_51F9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_51F9)

    ChrWalkTo(0x000C, 710, -250, -7470, 3000, 0x00)
    SetChrFlags(0x000C, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    EventEnd(0x00)

    Jump('loc_56FC')

    def _loc_522F(): pass

    label('loc_522F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_53F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_528C',
    )

    ChrTalk(
        0x00FE,
        (
            '我们以后可能就要\n',
            '一起执行任务了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310140739V到时候还要多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53F3')

    def _loc_528C(): pass

    label('loc_528C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哟，英雄们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140731V#000F库拉茨大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们两个\n',
            '干得真漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310140733V竟然还只是准游击士，\n',
            '简直不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '其实这是大家共同努力\n',
            '所换回来的美好结果呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '到了最后还是老爸\n',
            '出手相助的，\n',
            '我们的本领还没到家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你们真的\n',
            '已经做得很好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们以后可能就要\n',
            '一起执行任务了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310140739V到时候还要多多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53F3(): pass

    label('loc_53F3')

    Jump('loc_56FC')

    def _loc_53F6(): pass

    label('loc_53F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5400',
    )

    Jump('loc_56FC')

    def _loc_5400(): pass

    label('loc_5400')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_540A',
    )

    Jump('loc_56FC')

    def _loc_540A(): pass

    label('loc_540A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_551E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_546D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310111949V咦？\n',
            '那个金发的兄弟到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111950V他的枪法\n',
            '有相当的水准呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_551B')

    def _loc_546D(): pass

    label('loc_546D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0310111951V哦哦，\n',
            '这不是优胜组的成员吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111952V今天的比赛，\n',
            '我们都认真地观摩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111953V虽然说我们也想取得优胜，\n',
            '不过这个冠军让你们拿了\n',
            '我们一点也没觉得遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_551B(): pass

    label('loc_551B')

    Jump('loc_56FC')

    def _loc_551E(): pass

    label('loc_551E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5528',
    )

    Jump('loc_56FC')

    def _loc_5528(): pass

    label('loc_5528')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5532',
    )

    Jump('loc_56FC')

    def _loc_5532(): pass

    label('loc_5532')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_553C',
    )

    Jump('loc_56FC')

    def _loc_553C(): pass

    label('loc_553C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5546',
    )

    Jump('loc_56FC')

    def _loc_5546(): pass

    label('loc_5546')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_56EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_559A',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310111945V就算是游击士，\n',
            '也要保证良好的睡眠，\n',
            '早饭也要吃好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56E8')

    def _loc_559A(): pass

    label('loc_559A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#0310111943V哟，\n',
            '你们也是来吃早饭的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111944V#000F啊，是库拉茨大哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111945V就算是游击士，\n',
            '也要保证良好的睡眠，\n',
            '早饭也要吃好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310111946V你们在协会的研修中也学了吧。\n',
            '如果没有休息好，判断力和身体都会迟钝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111947V#010F哈哈，\n',
            '艾丝蒂尔只有对这一点是完全理解的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111948V#000F喂……\n',
            '那个『只有』是什么意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56E8(): pass

    label('loc_56E8')

    Jump('loc_56FC')

    def _loc_56EB(): pass

    label('loc_56EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_56F5',
    )

    Jump('loc_56FC')

    def _loc_56F5(): pass

    label('loc_56F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_56FC',
    )

    def _loc_56FC(): pass

    label('loc_56FC')

    TalkEnd(0x000C)

    Return()

# id: 0x001C offset: 0x5700
@scena.Code('func_1C_5700')
def func_1C_5700():
    Return()

# id: 0x001D offset: 0x5701
@scena.Code('func_1D_5701')
def func_1D_5701():
    EventBegin(0x00)
    SetChrFlags(0x0108, 0x0004)
    SetChrPos(0x0108, -3800, 0, -2180, 180)
    SetChrPos(0x0101, -3460, 0, -4600, 0)
    SetChrPos(0x0102, -4940, 0, -4600, 0)
    CameraMove(-3770, 0, -3540, 0)

    ChrTalk(
        0x0108,
        (
            '#0080101493V#070F……原来如此，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101494V我问你们一件事，\n',
            '为什么要参加武术大会呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……看过预选赛之后，\n',
            '身体就按耐不住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101496V情不自禁地想要\n',
            '和强大的对手大战一场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们现在以正游击士为目标\n',
            '在王国各地旅行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101498V所以想借此机会\n',
            '测试一下至今的修行成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可以啊。\n',
            '一起组队吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101501V在明天大会开始之前\n',
            '去报一下名就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F太好了～㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……嗯，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F你们的实力\n',
            '我之前就见识过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101505V作为协助我的人已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿……\n',
            '谢谢，金先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101507V我会尽全力加油的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101508V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101509V#070F彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，本来是打算挑战一下，\n',
            '只靠１个人能够到达什么程度的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101511V现在有了协助的人，\n',
            '就不能不想到要拿冠军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那当然了！\n',
            '既然参加就要拿冠军！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过，如果这样打算的话，\n',
            '缺少一个人，还是很难办到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101514V团体赛的人数是４个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是啊……\n',
            '还缺少一个人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，\n',
            '只要鼓足干劲的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F不，如果目标提高的话，\n',
            '就要做好万全的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040007V作战在拳脚相加之前\n',
            '就应该要开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……确实是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这个时候，\n',
            '如果雪拉姐在就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '喂，我们去拜托艾南先生\n',
            '联络一下洛连特支部吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……\n',
            '但是雪拉姐姐一定会很忙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101523V父亲和我们都不在，\n',
            '洛连特支部正缺少人手呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是……是这样没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊～真是的，不管是谁都好，\n',
            '有没有能帮我们的人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, -1920, 4000, 4680, 180)
    ClearChrFlags(0x0008, 0x0080)

    ChrTalk(
        0x0008,
        (
            '唔……\n',
            '我就是在等这句话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这、这个声音是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-1290, 4000, 5210, 3000)

    @scena.Lambda('lambda_5CE7')
    def lambda_5CE7():
        CameraMove(-2350, 0, -630, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5CE7)

    ChrWalkTo(0x0008, -4690, 2000, 4550, 3000, 0x00)
    ChrWalkTo(0x0008, -4810, 0, -390, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F果然出现了～\n',
            '这个乱侃的演奏家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101528V不会一直在２楼潜伏着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101529V#010F难道……\n',
            '刚才的话你都听见了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F呵呵……\n',
            '一字不漏地全都听见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101531V于是就想：这次轮到我出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0004)
    ChrJumpTo(0x0008, -5020, 0, -2270, 1000, 5000)

    ChrTalk(
        0x0101,
        (
            '#000F啊，等一下！\n',
            '怎么随便就坐下来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F这个不是弹钢琴的\n',
            '那个演奏家小哥嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101534V是你们的熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F该说是熟人呢，\n',
            '还是缘分的捉弄呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……还没有达到\n',
            '熟人这种程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101537V#030F本人是奥利维尔·朗海姆。\n',
            '来自埃雷波尼亚的旅行演奏家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101538V和艾丝蒂尔君、约修亚君\n',
            '是在之前的事件中认识的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '从那以后，关系变得很不一般呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F请不要用容易引起误会的方式说话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101541V#070F嗯，虽然不知道是怎么回事，\n',
            '我也来报个名字吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040008V金·瓦赛克，\n',
            '来自卡尔瓦德的游击士，\n',
            '以武术之道为志向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101543V你的钢琴\n',
            '我一直很欣赏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F嘻嘻……\n',
            '能得到夸奖真是光荣至极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '本人也听说了\n',
            '你在武术大会预选赛中的武勇事迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101546V面对４个人的对手，\n',
            '只凭借１个人就获得压倒性胜利对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101547V#070F遇到新手的对手，只是运气好罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101548V那么，演奏家先生\n',
            '找我们到底有什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F给我等一下～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101550V#010F奥利维尔先生……\n',
            '我想确认一件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101551V难道最近\n',
            '你没有事情可做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F不愧是约修亚君，\n',
            '这个问题真是尖锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '来到王都的这１个月间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101554V到处观光一遍之后，\n',
            '剩下的格兰赛尔城\n',
            '却因为有士兵把守而无法进入……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101555V想去别的地方看看，\n',
            '诞辰庆典又快要到了，\n',
            '现在还舍不得离开王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F总之，就是很闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101557V#030F然后突然听到了\n',
            '『缺少一个队员』的谈话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101558V而且最重要的是，\n',
            '优胜者会得到豪华晚餐会的招待……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '简直是女神的启示！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我就知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101562V#030F就是这样，\n',
            '能不能让我也成为参加武术大会的伙伴呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101563V#070F为什么不呢？',
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
            '#000F等、等一下金先生。\n',
            '这么简单就……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101565V你还不知道\n',
            '奥利维尔的战斗方法吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040009V#070F他擅长的是导力枪对吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101567V这样可以采取广泛的战术，\n',
            '我觉得能组成很好的队伍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F哎～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F这真是……让人吃惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101570V是不是从腰间的鼓起\n',
            '和走路的方式判断出来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101571V#070F还有视线移动的方式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101572V武术家和剑士捕捉移动的目标时\n',
            '视线是沿着线移动的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101573V而你对别人的行动的把握\n',
            '集中在一个一个点上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101574V这是使枪的人移动视线的特殊之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿哎，真是专业啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F原来如此……\n',
            '确实很有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#030F嗯……\n',
            '今后我要注意一点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，在你这位高手的眼光看来，\n',
            '我就算合格了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120116V#070F啊，请多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯。\n',
            '虽然感觉有点不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101581V#010F奥利维尔先生，\n',
            '请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x66FA
@scena.Code('func_1E_66FA')
def func_1E_66FA():
    EventBegin(0x00)
    CameraMove(63970, 200, 7220, 0)
    OP_67(0, 7860, -10000, 0)
    CameraSetDistance(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0017, 0x0080)
    SetChrChipByIndex(0x0101, 23)
    SetChrChipByIndex(0x0102, 24)
    SetChrChipByIndex(0x0009, 25)
    SetChrPos(0x0020, 58830, 640, -4430, 0)
    SetChrPos(0x0025, 58360, 640, -4450, 0)
    SetChrPos(0x0022, 59290, 640, -4980, 0)
    SetChrPos(0x0023, 59290, 640, -4720, 0)
    SetChrPos(0x0021, 58740, 640, -5400, 0)
    SetChrPos(0x0024, 58930, 640, -5550, 0)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    SetChrPos(0x0101, 60050, 200, -4970, 270)
    SetChrPos(0x0009, 58770, 200, -3750, 180)
    SetChrPos(0x0102, 58770, 200, -6150, 0)
    SetChrPos(0x0016, 62360, 0, 2910, 0)
    ClearChrFlags(0x0009, 0x0080)
    FadeIn(1000, 0)
    CameraMove(59510, 200, -4760, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010110522V#001F哈～虽然有点辣，\n',
            '不过很好吃呢㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110523V#008F香脆的里脊肉和松软的蒸土豆，\n',
            '真的是极佳的配搭呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110524V#019F饭后的咖啡也是非常香浓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110525V虽然听说过用玻璃器具泡咖啡\n',
            '有相当的难度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110526V#142F真是的，花别人的钱，\n',
            '就可以这么狼吞虎咽的吃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110527V我那点可怜的工资都给你们吃完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110528V#502F好啦好啦。\n',
            '总之谢谢你招待我们啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110529V#006F那么……\n',
            '你果然在为新闻素材伤脑筋吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110530V#142F哼……\n',
            '新闻素材要多少有多少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110531V#145F不过，都是些关于亲卫队的恐怖活动、\n',
            '女王身体欠佳之类的小道消息，\n',
            '这些东西的可信度很难保证啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110532V明确地说，\n',
            '我想要的是没有经过军队过滤的、\n',
            '新鲜可靠的、最新最快的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110533V#505F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110534V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110535V#140F我从朵洛希那里听说了一些\n',
            '关于蔡斯发生的绑架事件的消息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110536V就开门见山地说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110537V你们对那个理查德上校\n',
            '到底调查到什么程度了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110538V#006F该怎么说呢，真是一针见血啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110539V#010F能提出这样深入的问题，\n',
            '您应该已经有所推测了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110540V#145F果然上校就是幕后主谋啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110541V我们杂志还因采访过他而人气大增，\n',
            '真是不想接受这个现实啊……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110542V#142F反叛者马上就要有所行动了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110543V#015F他是否对女王陛下有反叛企图，\n',
            '现在我们还不得而知。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110544V但是，他们把杜南公爵作为傀儡，\n',
            '在暗地企图什么是可以肯定的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110545V#142F杜南公爵吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110546V趁着陛下身体欠佳，\n',
            '把自己当成格兰赛尔城的主人，\n',
            '一个肆意妄为的王室败家子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110547V不可思议的是，\n',
            '军队的高官为什么听之任之呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110548V#007F唉，那个是因为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110549V#505F……喂，约修亚。\n',
            '这个可以说出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110550V#015F是啊……\n',
            '我们也要尽可能地收集相关的情报。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110551V#010F如果是奈尔先生的话，\n',
            '我想一定能帮助我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110552V#143F喂喂，怎么了。\n',
            '你们果然知道些什么吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110553V#012F我事先声明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110554V接下来要说的事情，\n',
            '是不能作为报道写出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110555V#507F也就是说，先要做好心理准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110556V#142F可恶……\n',
            '这不是很糟糕的事情吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110557V算了，赶快说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetChrSubChip(0x0009, 3)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0270110558V#145F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110559V#003F啊～\n',
            '所以我说要做好心理准备嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110560V#145F这怎么可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110561V#142F喂……这是千真万确的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110562V#012F虽然很遗憾，不过事实就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110563V先是空贼事件，然后是孤儿院纵火事件，\n',
            '之后是中央工房的袭击事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110564V所有这些事情，\n',
            '都和情报部的特务兵有关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110565V#007F而且，军队的上层都被抓住了痛脚，\n',
            '连摩尔根将军也被强制软禁了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110566V亲卫队被强加上莫须有的罪名，\n',
            '被当作恐怖分子受到追捕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    SetChrSubChip(0x0009, 0)

    ChrTalk(
        0x0009,
        (
            '#0270110567V#144F啊啊～真是的！\n',
            '怎么又是这样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110568V#145F可恶……\n',
            '这怎么能写成报道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110569V最近我们杂志也要接受军队的检查……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110570V印刷的时候肯定会被拦下来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110571V#505F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110572V#142F没办法……\n',
            '只好勉强报道一下与这些事情\n',
            '没什么关系的武术大会了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110573V#143F……啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110574V你们参加武术大会，\n',
            '也是有什么特别的理由吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110575V#006F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110576V虽然和委托的内容有关，\n',
            '所以不能告诉你详细的情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110577V#010F您只要知道这是为了打开目前局面\n',
            '所采取的行动就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110578V#142F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110579V#145F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110580V……好，我决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110581V#142F虽然作为记者不能够做些什么……\n',
            '不过，我也来帮你们忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110582V游击士协会调查不到的事情，\n',
            '就由我通过私人的途径来调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110583V#006F谢谢，真是帮大忙了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110584V#012F对方可是军队啊，\n',
            '这样做的话恐怕太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110585V即使这样，你也愿意帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110586V#144F真啰嗦，这是我的战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110587V作为一名记者，\n',
            '我怎么能眼睁睁地看着笔杆输给刀剑呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110588V#004F奈尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110589V#015F我明白了……\n',
            '那么这件事就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110590V#141F嗯，就交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110591V那么，还有一点，\n',
            '具体来说你们想调查些什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110592V#505F这个嘛……\n',
            '应该是军队的动向吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110593V亲卫队的人是不是都被逮捕了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110594V摩尔根将军被囚禁在哪里……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110595V#142F知道了，\n',
            '我会多加注意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110596V除了调查这些事情，\n',
            '……还有没有其他的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110597V#013F……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110598V有关情报部成员的经历，\n',
            '请问能帮我们调查一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110599V#004F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110600V#143F情报部成员的经历吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110601V#012F说具体一点，\n',
            '就是作为核心的理查德上校、凯诺娜上尉，\n',
            '以及洛伦斯少尉这三个人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110602V因为以后要和他们对决，\n',
            '所以想知道他们的一些详细经历……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110603V#141F我明白了……\n',
            '你的意思是『知己知彼，百战不殆』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110604V#002F没错，除了上校，\n',
            '那个少尉的事情也想知道得更多一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110605V约修亚刚才也说了，\n',
            '明天或者后天的比赛中说不定\n',
            '会和这个人领衔的特务部队对战……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110606V#012F奈尔先生，这件事拜托您可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110607V#145F……我在军队里认识不少人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110608V军队的机密情报先不说，\n',
            '如果是单纯的简历的话说不定能弄到手。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110609V#141F好吧，我就试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110610V#006F那真是太感谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110611V#010F那就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110612V#141F哎呀，没什么大不了的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110613V总之大家就要有来有往嘛。\n',
            '如果你们取得优胜后被招待进王城的话，\n',
            '一定要把详细情形都告诉我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110614V#007F果然是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110615V#010F我知道了，\n',
            '只要是能说出来的都会告诉你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，艾丝蒂尔他们和奈尔在咖啡厅分手，\n',
            '接着就回到酒店早早地休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '然后，第二天早上——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x00)
    Sleep(500)

    PlaySE(13, 0x00, 0x64)
    Sleep(3000)

    SetMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x7C12
@scena.Code('func_1F_7C12')
def func_1F_7C12():
    EventBegin(0x00)
    CameraMove(-61470, 0, 67180, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0009, -56660, 0, 64750, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, -61900, 0, 67420, 135)
    SetChrPos(0x0102, -63460, 0, 66810, 135)

    ChrTalk(
        0x0101,
        (
            '#000F喂～奈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7CA4')
    def lambda_7CA4():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7CA4)

    ChrTalk(
        0x0102,
        (
            '#0020110950V#010F打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F……哦哦，终于来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110952V朵洛希那家伙，\n',
            '传话难得能成功一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7D19')
    def lambda_7D19():
        CameraMove(-57890, 0, 65099, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7D19)

    @scena.Lambda('lambda_7D31')
    def lambda_7D31():
        CameraSetDistance(2600, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_7D31)

    @scena.Lambda('lambda_7D41')
    def lambda_7D41():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_7D41')

    DispatchAsync2(0x0101, 0x0001, lambda_7D41)

    @scena.Lambda('lambda_7D52')
    def lambda_7D52():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_7D52')

    DispatchAsync2(0x0009, 0x0001, lambda_7D52)

    @scena.Lambda('lambda_7D63')
    def lambda_7D63():
        ChrWalkTo(0x00FE, -59150, 0, 64660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7D63)

    ChrWalkTo(0x0102, -60560, 0, 66670, 3000, 0x00)

    @scena.Lambda('lambda_7D92')
    def lambda_7D92():
        ChrWalkTo(0x00FE, -57490, 0, 64410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_7D92)

    ChrWalkTo(0x0102, -60490, 0, 64560, 3000, 0x00)
    ChrWalkTo(0x0102, -58840, 0, 63880, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#140F对了，\n',
            '今天你们也赢了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110954V朵洛希那家伙，\n',
            '回来的时候兴高采烈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那么奈尔先生，\n',
            '关于那件事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F哦，真是开门见山啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '给你……\n',
            '主要成员的经历都收集到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奈尔拿出\n',
            '一本黑色封皮的文件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#000F这是……王国军的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110960V#140F啊，虽然机密度不是很高，\n',
            '不过也是不能随便拿出来的文件呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110961V好不容易说服军队中的熟人\n',
            '才借来的，不要往外说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110962V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那么，\n',
            '我们就在这里看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '翻看着那本黑色封皮的文件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_8014(): pass

    label('loc_8014')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_87DC',
    )

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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 3, 0x673)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 4, 0x674)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 5, 0x675)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_808F',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '关于理查德上校\n'),
            TXT(0x01, '关于凯诺娜上尉\n'),
            TXT(0x02, '关于洛伦斯少尉\n'),
            TXT(0x03, '关闭文件\n'),
        ),
    )

    Jump('loc_80C5')

    def _loc_808F(): pass

    label('loc_808F')

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '关于理查德上校\n'),
            TXT(0x01, '关于凯诺娜上尉\n'),
            TXT(0x02, '关于洛伦斯少尉\n'),
        ),
    )

    def _loc_80C5(): pass

    label('loc_80C5')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_80F8'),
        (0x00000001, 'loc_83C7'),
        (0x00000002, 'loc_85B4'),
        (0x00000003, 'loc_87C9'),
        (-1, 'loc_87D9'),
    )

    def _loc_80F8(): pass

    label('loc_80F8')

    FadeOut(300, 0, 100)

    Talk(
        (
            '#0270110964V',
            (TxtCtl.SetColor, 0x5),
            '亚兰·理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110965V',
            (TxtCtl.SetColor, 0x5),
            '七耀历１１６８年，\n',
            '生于利贝尔王国卢安地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '作为士官学校的主席毕业之后，\n',
            '编入了卡西乌斯·布莱特上校\n',
            '加入了独立机动部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在１０年前的百日战役中\n',
            '作为卡西乌斯上校的部下\n',
            '在反攻作战中屡立战功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯上校退役之后，\n',
            '被提拔为军队作战中心的成员，\n',
            '在组织改革中建立了很多功绩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '１年前，作出了设立情报部的提案。\n',
            '之后获得了艾莉茜雅女王的承认，\n',
            '就任情报部首任指挥官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 3, 0x673)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_83C4',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 3, 0x673))

    ChrTalk(
        0x0101,
        (
            '#000F该怎么说呢……\n',
            '这就是所谓的精英吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110971V他可是主席呢，主席。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F确实是个很厉害的人物呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110973V希德少校说得没错，\n',
            '１０年前战争的时候，\n',
            '他确实是父亲的部下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，老爸\n',
            '真的当过上校呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110975V明明这么了不起，\n',
            '为什么要辞掉呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_83C4(): pass

    label('loc_83C4')

    Jump('loc_87D9')

    def _loc_83C7(): pass

    label('loc_83C7')

    FadeOut(300, 0, 100)

    Talk(
        (
            '#0270110976V',
            (TxtCtl.SetColor, 0x5),
            '凯诺娜·亚马尔迪亚上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110977V',
            (TxtCtl.SetColor, 0x5),
            '七耀历１１７５年，\n',
            '生于利贝尔王国王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '以优秀的成绩从士官学校毕业之后，\n',
            '被提拔为军队作战中心的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '１年前，在情报部设立的同时，\n',
            '得到理查德上校的提拔，\n',
            '调到了情报部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110980V',
            (TxtCtl.SetColor, 0x5),
            '之后，作为理查德上校的副官，\n',
            '担当辅佐其进行作战指挥的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 4, 0x674)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85B1',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 4, 0x674))

    ChrTalk(
        0x0101,
        (
            '#000F『以优秀的成绩毕业』，\n',
            '看起来又是一个精英呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F自从她担任军官以来，\n',
            '她好像一直在\n',
            '理查德上校手下做事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110983V真是相当地忠诚呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85B1(): pass

    label('loc_85B1')

    Jump('loc_87D9')

    def _loc_85B4(): pass

    label('loc_85B4')

    FadeOut(300, 0, 100)

    Talk(
        (
            '#0270110984V',
            (TxtCtl.SetColor, 0x5),
            '洛伦斯·博格少尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110985V',
            (TxtCtl.SetColor, 0x5),
            '年龄、国籍不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110986V',
            (TxtCtl.SetColor, 0x5),
            '原属佣兵部队『杰斯塔猎兵团』，\n',
            '应理查德上校的征召，\n',
            '成为了情报部的一员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110987V',
            (TxtCtl.SetColor, 0x5),
            '在这之前的经历不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 5, 0x675)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87C6',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 5, 0x675))

    ChrTalk(
        0x0101,
        (
            '#000F那个戴面具的家伙……\n',
            '不是利贝尔人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且作为原佣兵的经历不明\n',
            '是怎么一回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……不知道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所谓『猎兵团』，\n',
            '是只有最高级别的佣兵部队\n',
            '才能获得的称号……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是不是因为战斗能力很强，\n',
            '才得到上校提拔的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『杰斯塔猎兵团』……\n',
            '这名字我好像在哪听到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_87C6(): pass

    label('loc_87C6')

    Jump('loc_87D9')

    def _loc_87C9(): pass

    label('loc_87C9')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_87D9')

    def _loc_87D9(): pass

    label('loc_87D9')

    Jump('loc_8014')

    def _loc_87DC(): pass

    label('loc_87DC')

    ChrTalk(
        0x0101,
        (
            '#000F谢谢你，奈尔。\n',
            '不管怎么说，能看清敌人的样子了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F能帮上忙就再好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110998V我在调查资料的时候，\n',
            '也发现了很多有趣的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#010F有趣的事情……是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F比如，现在被通缉的\n',
            '亲卫队的尤莉亚中尉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111001V在士官学校和凯诺娜上尉\n',
            '是同一年级的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过看起来，\n',
            '那两个人的关系\n',
            '好像不是很好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F不管怎么说，她们是\n',
            '互相竞争主席职位的对手呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '学问有凯诺娜上尉，\n',
            '武术有尤莉亚中尉。\n',
            '两个人真是很好的对照呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F原来如此……\n',
            '我大概能想象出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F尤莉亚中尉威风凛凛的\n',
            '好像过去的骑士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111008V#140F还有……\n',
            '虽然这个和军队没有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111009V你们听说过\n',
            '『科洛蒂娅公主』这个名字吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F科洛蒂娅公主……\n',
            '好像在哪里听说过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我记得，是在海难事故中去世的\n',
            '王太子夫妻的遗孤吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111012V是女王陛下的孙女……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111013V#140F嗯，虽然不太有名，\n',
            '不过可是直系中的直系呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111014V她好像一直生活在\n',
            '格兰赛尔城的女王宫里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111015V而且，好像某个人物正在寻找\n',
            '那位公主殿下的相亲对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F相亲对象啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111017V虽然对大户人家来说，\n',
            '不是什么新鲜事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过觉得有点可怜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔，重点不在那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在应该注意的问题是\n',
            '『某个人物』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F呵呵，真是敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎，那个人难道是……',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '艾莉茜雅女王？\n'),
            TXT(0x01, '杜南公爵？\n'),
            TXT(0x02, '理查德上校？\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_8D11'),
        (0x00000001, 'loc_8DA9'),
        (0x00000002, 'loc_8E37'),
        (-1, 'loc_8ED4'),
    )

    def _loc_8D11(): pass

    label('loc_8D11')

    ChrTalk(
        0x0009,
        (
            '#140F啊，名义上是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111024V不过实际上，派人去外国\n',
            '寻找合适的候选人的，\n',
            '是那个理查德上校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可、可是，这不是很奇怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8ED4')

    def _loc_8DA9(): pass

    label('loc_8DA9')

    ChrTalk(
        0x0009,
        (
            '#140F没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111029V不过实际上，派人去外国\n',
            '寻找合适的候选人的，\n',
            '是那个理查德上校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可、可是，这不是很奇怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8ED4')

    def _loc_8E37(): pass

    label('loc_8E37')

    ChrTalk(
        0x0009,
        (
            '#140Fほ哦，还真是敏锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111034V实际上，派人去外国\n',
            '寻找合适的候选人的，\n',
            '是那个理查德上校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111035V#000F果然是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是……这不是很奇怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8ED4')

    def _loc_8ED4(): pass

    label('loc_8ED4')

    ChrTalk(
        0x0101,
        (
            '#000F为什么会是理查德上校\n',
            '来寻找公主的结婚对象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F所以我说，\n',
            '到处充满了可疑的气味呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111039V所以说……\n',
            '有件事情想拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F——如果明天的比赛能获胜，\n',
            '被招待进城参加晚餐会的话，\n',
            '打听一下这方面的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111042V是这样没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是的，\n',
            '不过确实告诉我们很多事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F我调查到的只有这些了。\n',
            'Give&take是理所当然的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F确实帮了我们很多忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F没办法呢～\n',
            '如果知道了什么，就告诉你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F嘿，早这样说不就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，就算不拜托你们，\n',
            '运气好的话今天也能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    TerminateThread(0x0009, 0xFF)
    ChrWalkTo(0x0009, -55760, 0, 64459, 3000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0270111051V#140F喂。\n',
            '这里是利贝尔通讯社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哦，是你啊！\n',
            '我一直在等你的联络呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '什么……现在就？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，知道了。\n',
            '我立刻过去找你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F怎么，发生什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, -57490, 0, 64410, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#140F稍微有点私事。\n',
            '现在要去和别人会面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很重要的事吗。\n',
            '太阳已经下山了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F本来我就是夜猫子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为要带那个我行我素的丫头\n',
            '进行新人研修，\n',
            '才改变成白天型的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉，不说这件事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111061V我要出去了，\n',
            '你们接着干你们的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111063V要加油工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F你们也是，明天的比赛，\n',
            '一定不能输啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9359')
    def lambda_9359():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_9359')

    DispatchAsync2(0x0101, 0x0001, lambda_9359)

    @scena.Lambda('lambda_936A')
    def lambda_936A():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_936A')

    DispatchAsync2(0x0102, 0x0001, lambda_936A)

    ChrWalkTo(0x0009, -58470, 0, 65300, 3000, 0x00)
    ChrWalkTo(0x0009, -60060, 0, 65300, 3000, 0x00)
    ChrWalkTo(0x0009, -60840, 0, 66460, 3000, 0x00)
    ChrWalkTo(0x0009, -63690, 0, 66460, 3000, 0x00)
    ChrWalkTo(0x0009, -63690, -2230, 62470, 3000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯……\n',
            '我们该怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F是呀……\n',
            '总之，先顺路去协会，\n',
            '然后就回旅馆吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '最好把奈尔先生调查到的情报\n',
            '向协会报告一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111068V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0020 offset: 0x949B
@scena.Code('func_20_949B')
def func_20_949B():
    EventBegin(0x00)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -56250, 0, 60940, 90)
    SetChrPos(0x0101, -60190, 0, 65280, 135)
    SetChrPos(0x0102, -61190, 0, 64849, 135)
    SetChrPos(0x0108, -60700, 0, 66190, 135)
    CameraMove(-54490, 0, 61730, 0)

    ChrTalk(
        0x000A,
        (
            '#150F主编，真的好奇怪～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130250V已经两天没有取得联络了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130251V嗯，我想他是沉浸\n',
            '在寻找独家新闻\n',
            '的美梦中了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130252V不过在这个戒严时期\n',
            '不能取得联系的确有些奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x000B,
        (
            '#2310130253V咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_95E3')
    def lambda_95E3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_95E3)

    CameraMove(-56640, 0, 63970, 2000)

    ChrTalk(
        0x000A,
        (
            '#150F啊，小艾你们来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_961F')
    def lambda_961F():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_961F')

    DispatchAsync2(0x000A, 0x0001, lambda_961F)

    @scena.Lambda('lambda_9630')
    def lambda_9630():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_9630')

    DispatchAsync2(0x0101, 0x0001, lambda_9630)

    @scena.Lambda('lambda_9641')
    def lambda_9641():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_9641')

    DispatchAsync2(0x0102, 0x0001, lambda_9641)

    @scena.Lambda('lambda_9652')
    def lambda_9652():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_9652')

    DispatchAsync2(0x0108, 0x0001, lambda_9652)

    @scena.Lambda('lambda_9663')
    def lambda_9663():
        ChrWalkTo(0x00FE, -54540, 0, 62770, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9663)

    Sleep(100)

    @scena.Lambda('lambda_9683')
    def lambda_9683():
        ChrWalkTo(0x00FE, -55570, 0, 62750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_9683)

    Sleep(300)

    @scena.Lambda('lambda_96A3')
    def lambda_96A3():
        ChrWalkTo(0x00FE, -56620, 0, 62700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_96A3)

    CameraMove(-54340, 0, 62290, 3000)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)

    ChrTalk(
        0x000B,
        (
            '#2310130257V哦，武术大会的优胜者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130258V本人就是\n',
            '《利贝尔通讯》的总编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130259V我从奈尔和朵洛希那里\n',
            '听说过你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130260V你们二位是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面，请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130263V《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130264V哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130265V对了，你们\n',
            '是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是的，可以这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130267V是你们啊……\n',
            '你总算来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F你好，打扰了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130269V我们是来找奈尔的，\n',
            '难道他出去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130270V我们刚才正在\n',
            '谈起这件事请呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '事实上奈尔他昨天和今天\n',
            '都没有到编辑部来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130272V完全不能和他取得联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F昨天和今天都……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130275V我们前天傍晚\n',
            '还在这里和奈尔先生\n',
            '商讨事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#150F真、真的吗～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_99EB')
    def lambda_99EB():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_99EB)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#000F什么真的假的呀，给奈尔捎口信\n',
            '的不就是朵洛希你吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '半决赛之后，\n',
            '让我们到这里来向他打听情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#150F啊－我想起来了，\n',
            '是那件事情－啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '请问，奈尔前辈\n',
            '那时是怎么说的呢～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130281V他到哪里去了呢～',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '去收集新闻了\n'),
            TXT(0x01, '有人叫他出去\n'),
            TXT(0x02, '一起去吃晚餐了\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9B49'),
        (0x00000001, 'loc_9BCD'),
        (0x00000002, 'loc_9C25'),
        (-1, 'loc_9C97'),
    )

    def _loc_9B49(): pass

    label('loc_9B49')

    ChrTalk(
        0x0102,
        (
            '#010F嗯，很有可能是去\n',
            '外面收集新闻了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '事实上当时有人叫他出去，\n',
            '于是他可能到某个地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130284V#000F啊，是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C97')

    def _loc_9BCD(): pass

    label('loc_9BCD')

    ChrTalk(
        0x0102,
        (
            '#010F啊，的确是那样的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130286V当时有人叫他出去，\n',
            '于是他可能到某个地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C97')

    def _loc_9C25(): pass

    label('loc_9C25')

    ChrTalk(
        0x0102,
        (
            '#010F不，那是３天前的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '２天前的傍晚奈尔先生\n',
            '是被某个人用通信器叫出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C97')

    def _loc_9C97(): pass

    label('loc_9C97')

    ChrTalk(
        0x000B,
        (
            '#2310130290V你们说的是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9CBC')
    def lambda_9CBC():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9CBC)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0102,
        (
            '#010F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130292V大概这就是为何从那时开始\n',
            '到现在为止他都没有消息的原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#150F怎、怎么会！\n',
            '前辈你不能死啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎，不要说那些\n',
            '莫名其妙的话！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '从今天开始定期船\n',
            '也停止航行了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '到昨天为止还是在航行的，\n',
            '他会不会到别的地方去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130297V已经到飞艇坪看过了，\n',
            '在登艇名单上没有记载。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9E0B')
    def lambda_9E0B():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9E0B)

    @scena.Lambda('lambda_9E19')
    def lambda_9E19():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_9E19)

    ChrTalk(
        0x000B,
        (
            '也就是说他应该\n',
            '还在王都这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你们俩在和那个记者\n',
            '最后一次见面的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130301V那个名叫奈尔的记者\n',
            '不是提起过，说他得到\n',
            '了什么新闻材料吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9EC9')
    def lambda_9EC9():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_9EC9)

    @scena.Lambda('lambda_9ED7')
    def lambda_9ED7():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9ED7)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130303V#070F现在这种局势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130304V大众传媒也被\n',
            '军队所管制吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130305V对吗，主编先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130306V是啊，的确如此呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130307V特别是围绕情报部的话题，\n',
            '正处于被拼命的审批的状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130308V一时的气话而已，你们别放在心上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F……在这种状况下，\n',
            '可以报道的新闻自然就少了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，作为一个记者，\n',
            '哪怕是有一点新的消息，\n',
            '都想尽快传达给读者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130311V#010F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130312V情报部的管制不成问题，\n',
            '以新的具有话题性的消息为重……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130313V关于这个，奈尔先生\n',
            '曾经是提起过什么的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，对了……',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '武术大会优胜者的相关事宜\n'),
            TXT(0x01, '科洛蒂亚公主婚姻的相关事宜\n'),
            TXT(0x02, '尤莉亚和凯诺娜过去的相关事宜\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_A1A9'),
        (0x00000001, 'loc_A2EB'),
        (0x00000002, 'loc_A318'),
        (-1, 'loc_A453'),
    )

    def _loc_A1A9(): pass

    label('loc_A1A9')

    ChrTalk(
        0x0108,
        (
            '#070F要把这个作为新闻的话，\n',
            '也应该是在我们取得优胜之前的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130316V作为现在的新的消息就不太行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130318V的确，因为特务兵他们\n',
            '还是有可能取胜的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……还有一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '奈尔先生对科洛蒂亚公主\n',
            '的婚姻问题似乎很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哦，晚宴的时候\n',
            '公爵所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A453')

    def _loc_A2EB(): pass

    label('loc_A2EB')

    ChrTalk(
        0x0108,
        (
            '#070F哦，晚宴的时候\n',
            '公爵所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A453')

    def _loc_A318(): pass

    label('loc_A318')

    ChrTalk(
        0x0108,
        (
            '#0081040010V#070F情报部的才女和\n',
            '和逃亡中的女亲卫队员\n',
            '在士官学校里是对手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然很有趣，不过对于情报部来说\n',
            '这种事情允许取材吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，确实……\n',
            '不能作为报道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……还有一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '奈尔先生对科洛蒂亚公主\n',
            '的婚姻问题似乎很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哦，晚宴的时候\n',
            '公爵所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A453')

    def _loc_A453(): pass

    label('loc_A453')

    ChrTalk(
        0x000B,
        (
            '什么，奈尔和你们\n',
            '谈到了这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A47E')
    def lambda_A47E():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A47E)

    @scena.Lambda('lambda_A48C')
    def lambda_A48C():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A48C)

    ChrTalk(
        0x000B,
        (
            '#2310130332V如果是真的，\n',
            '那就是个爆炸性的新闻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130333V总算是可以获取\n',
            '一些内幕了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F那个叫奈尔的记者\n',
            '怎么会知道这些事情？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130335V不是说与王室无关\n',
            '的人员都不知道这个情报的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#150F他可能是从那个在艾尔贝离宫\n',
            '工作的朋友那里听说的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还有一个不能报道的消息，公主殿下\n',
            '也被恐怖分子作为目标了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130338V因此公主殿下在艾尔贝离宫\n',
            '里面被秘密保护了起来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_A654')
    def lambda_A654():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A654)

    @scena.Lambda('lambda_A662')
    def lambda_A662():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A662)

    @scena.Lambda('lambda_A670')
    def lambda_A670():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_A670)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F……果然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130340V#070F呵呵呵，\n',
            '得来全不费工夫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F难道那天叫奈尔出去的\n',
            '就是他在离宫里面工作的朋友吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130342V这样一来奈尔先生在离宫\n',
            '的可能性就很高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130343V是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130344V也许奈尔为了\n',
            '去采访公主殿下，\n',
            '强行潜入了离宫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130345V然后被士兵发现了，\n',
            '抓了起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#150F呜～哇！\n',
            '奈尔前辈死定了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这样才不会死呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是，如果这是事实，\n',
            '他是不会被轻易释放的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130350V他和科洛蒂娅公主站在\n',
            '同样立场的可能性比较高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130351V你们是……\n',
            '你们究竟知道了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '在这个王都……不，\n',
            '在利贝尔究竟发生了什么事，\n',
            '你们不会是知道什么吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A8E6')
    def lambda_A8E6():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A8E6)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#000F唔－嗯，对不起。\n',
            '请恕我们无可奉告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F奈尔先生的事情，\n',
            '请交给我们游击士协会去办。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130355V如果的确是被拘捕了，\n',
            '那我们一定会把他解救出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130356V太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130357V我明白了，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#150F啊，拜托了～！\n',
            '小艾～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130359V一定要救救奈尔前辈～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0xAA33
@scena.Code('func_21_AA33')
def func_21_AA33():
    EventBegin(0x00)
    CameraMove(-53660, 0, 62750, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x000A, -59130, 0, 59600, 0)
    SetChrPos(0x0009, -53500, 0, 62630, 90)
    CameraMove(-54490, 0, 61730, 0)

    ChrTalk(
        0x0009,
        (
            '#140F嘁……\n',
            '终于开始了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_AADA')
    def lambda_AADA():
        CameraMove(-56110, 0, 62480, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_AADA)

    ChrWalkTo(0x0009, -56320, 0, 62540, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x000A, 400)

    ChrTalk(
        0x0009,
        (
            '#140F出发，朵洛希！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270131112V必须要确保找到\n',
            '可以从远处眺望这场战斗的最佳位置！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#150F等、等一下好吗～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280131114V感光回路马上就可以\n',
            '设置好了的呀～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310131115V喂喂，到底是怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这三天来你去哪里旅游了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000B, 400)

    ChrTalk(
        0x0009,
        (
            '#140F这可是独家新闻！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270131118V『利贝尔通讯社』建社以来\n',
            ' 前所未有过的独家新闻啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4240._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
