import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4137_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4137   ._SN')

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

# id: 0x10001 offset: 0x182
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奥利维尔',
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
            name                = '奈尔',
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
            name                = '朵洛希',
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
            name                = '总编',
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
            name                = '库拉茨',
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
            name                = '克鲁茨',
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
            name                = '科蕾蒂',
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
            name                = '彭萨',
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
            name                = '金',
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
            name                = '奥利维尔',
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
            name                = '米亚尔',
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
            name                = '戈万',
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
            name                = '帕菲',
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
            name                = '娜娜',
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
            name                = '巴拉尔',
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
            name                = '科尼嘉',
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
            name                = '诺蒂亚',
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
            name                = '法尔茨',
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
            name                = '莎莉亚',
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
            name                = '士兵丹',
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
            name                = '士兵阿尔兹',
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
            name                = '阿加特',
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
            name                = '提妲',
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
            name                = '拉赛尔',
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
            name                = '\u3000',
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
            name                = '\u3000',
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
            name                = '\u3000',
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
            name                = '\u3000',
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
            name                = '\u3000',
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
            name                = '\u3000',
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

# id: 0x10002 offset: 0x542
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x542
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x542
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x542
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_550',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_1C_5854)

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
    Event(0, func_1D_5855)

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
    Event(0, func_1E_6925)

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
    Event(0, func_21_AFEC)

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
    Event(0, func_1F_8013)

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
    Event(0, func_20_995A)

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

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 4650, 0, 600, 0)

    def _loc_5D1(): pass

    label('loc_5D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_675',
    )

    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, 57670, 0, -5070, 111)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, 59920, 0, -5060, 275)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 5860, 4000, -4760, 350)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -3620, 0, -2160, 186)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -3600, 0, -4420, 359)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 62780, 0, -3550, 162)
    CreateThread(0x000A, 0x00, 0x00, func_03_8D4)

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

    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -54200, 0, 63010, 194)
    CreateThread(0x000A, 0x00, 0x00, func_02_8BE)
    ChrSetPos(0x0018, -53520, 0, 123230, 98)
    CreateThread(0x0018, 0x00, 0x00, func_02_8BE)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)

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

    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -54200, 0, 63010, 194)
    CreateThread(0x000A, 0x00, 0x00, func_02_8BE)

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

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 5860, 4000, -4760, 350)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 62780, 0, -3550, 162)
    CreateThread(0x000A, 0x00, 0x00, func_03_8D4)

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

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -3620, 0, -2160, 186)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -3690, 0, -4720, 344)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0018, -60680, 0, 122710, 160)
    CreateThread(0x0018, 0x00, 0x00, func_05_91C)
    ChrSetPos(0x0019, -54350, 0, 1120, 265)
    CreateThread(0x0019, 0x00, 0x00, func_02_8BE)

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

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -3620, 0, -2160, 186)
    ChrSetFlags(0x0010, 0x0010)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -3690, 0, -4720, 344)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0018, -63230, 0, 59560, 338)
    CreateThread(0x0018, 0x00, 0x00, func_02_8BE)
    ChrSetFlags(0x0019, 0x0080)

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

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 910, 0, -3650, 189)
    ChrSetPos(0x000E, 610, 0, -3020, 146)

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

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 5860, 4000, -4760, 350)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x0018, -63230, 0, 59560, 338)
    CreateThread(0x0018, 0x00, 0x00, func_02_8BE)

    def _loc_8AC(): pass

    label('loc_8AC')

    Return()

# id: 0x0001 offset: 0x8AD
@scena.Code('func_01_8AD')
def func_01_8AD():
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
@scena.Code('func_02_8BE')
def func_02_8BE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8D3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_8BE')

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

# id: 0x0007 offset: 0x9C9
@scena.Code('func_07_9C9')
def func_07_9C9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_A4D',
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

    Jump('loc_BAA')

    def _loc_A4D(): pass

    label('loc_A4D')

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

    def _loc_BAA(): pass

    label('loc_BAA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xBAE
@scena.Code('func_08_BAE')
def func_08_BAE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_BFD',
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

    Jump('loc_CF6')

    def _loc_BFD(): pass

    label('loc_BFD')

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

    def _loc_CF6(): pass

    label('loc_CF6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xCFA
@scena.Code('func_09_CFA')
def func_09_CFA():
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

# id: 0x000A offset: 0xD6A
@scena.Code('func_0A_D6A')
def func_0A_D6A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_DCB',
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

    Jump('loc_E41')

    def _loc_DCB(): pass

    label('loc_DCB')

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

    def _loc_E41(): pass

    label('loc_E41')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xE45
@scena.Code('func_0B_E45')
def func_0B_E45():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_EB1',
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

    Jump('loc_1340')

    def _loc_EB1(): pass

    label('loc_EB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_F02',
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

    Jump('loc_1340')

    def _loc_F02(): pass

    label('loc_F02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_F64',
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

    Jump('loc_1340')

    def _loc_F64(): pass

    label('loc_F64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_FCE',
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

    Jump('loc_1340')

    def _loc_FCE(): pass

    label('loc_FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_10AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_102D',
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

    Jump('loc_10AB')

    def _loc_102D(): pass

    label('loc_102D')

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

    def _loc_10AB(): pass

    label('loc_10AB')

    Jump('loc_1340')

    def _loc_10AE(): pass

    label('loc_10AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1108',
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

    Jump('loc_1340')

    def _loc_1108(): pass

    label('loc_1108')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_11E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_1163',
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

    Jump('loc_11E1')

    def _loc_1163(): pass

    label('loc_1163')

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

    def _loc_11E1(): pass

    label('loc_11E1')

    Jump('loc_1340')

    def _loc_11E4(): pass

    label('loc_11E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1255',
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

    Jump('loc_1340')

    def _loc_1255(): pass

    label('loc_1255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1293',
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

    Jump('loc_1340')

    def _loc_1293(): pass

    label('loc_1293')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_12FA',
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

    Jump('loc_1340')

    def _loc_12FA(): pass

    label('loc_12FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1340',
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

    def _loc_1340(): pass

    label('loc_1340')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1344
@scena.Code('func_0C_1344')
def func_0C_1344():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1389',
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

    Jump('loc_1AD1')

    def _loc_1389(): pass

    label('loc_1389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1445',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_13DA',
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

    Jump('loc_1442')

    def _loc_13DA(): pass

    label('loc_13DA')

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

    def _loc_1442(): pass

    label('loc_1442')

    Jump('loc_1AD1')

    def _loc_1445(): pass

    label('loc_1445')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_153B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_14B6',
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

    Jump('loc_1538')

    def _loc_14B6(): pass

    label('loc_14B6')

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

    def _loc_1538(): pass

    label('loc_1538')

    Jump('loc_1AD1')

    def _loc_153B(): pass

    label('loc_153B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1660',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_15B7',
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

    Jump('loc_165D')

    def _loc_15B7(): pass

    label('loc_15B7')

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

    def _loc_165D(): pass

    label('loc_165D')

    Jump('loc_1AD1')

    def _loc_1660(): pass

    label('loc_1660')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1793',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_16D9',
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

    Jump('loc_1790')

    def _loc_16D9(): pass

    label('loc_16D9')

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

    def _loc_1790(): pass

    label('loc_1790')

    Jump('loc_1AD1')

    def _loc_1793(): pass

    label('loc_1793')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1882',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_17F2',
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

    Jump('loc_187F')

    def _loc_17F2(): pass

    label('loc_17F2')

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

    def _loc_187F(): pass

    label('loc_187F')

    Jump('loc_1AD1')

    def _loc_1882(): pass

    label('loc_1882')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_197C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_18E7',
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

    Jump('loc_1979')

    def _loc_18E7(): pass

    label('loc_18E7')

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

    def _loc_1979(): pass

    label('loc_1979')

    Jump('loc_1AD1')

    def _loc_197C(): pass

    label('loc_197C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1986',
    )

    Jump('loc_1AD1')

    def _loc_1986(): pass

    label('loc_1986')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_19E0',
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

    Jump('loc_1AD1')

    def _loc_19E0(): pass

    label('loc_19E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A6B',
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

    Jump('loc_1AD1')

    def _loc_1A6B(): pass

    label('loc_1A6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1AD1',
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

    def _loc_1AD1(): pass

    label('loc_1AD1')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1AD5
@scena.Code('func_0D_1AD5')
def func_0D_1AD5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1B09',
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

    Jump('loc_21CB')

    def _loc_1B09(): pass

    label('loc_1B09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1B2F',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的情况很奇怪呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21CB')

    def _loc_1B2F(): pass

    label('loc_1B2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1BB2',
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

    Jump('loc_21CB')

    def _loc_1BB2(): pass

    label('loc_1BB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1CAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1C0F',
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

    Jump('loc_1CAB')

    def _loc_1C0F(): pass

    label('loc_1C0F')

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

    def _loc_1CAB(): pass

    label('loc_1CAB')

    Jump('loc_21CB')

    def _loc_1CAE(): pass

    label('loc_1CAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1D22',
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

    Jump('loc_21CB')

    def _loc_1D22(): pass

    label('loc_1D22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1E4F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1DAF',
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

    Jump('loc_1E4C')

    def _loc_1DAF(): pass

    label('loc_1DAF')

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

    def _loc_1E4C(): pass

    label('loc_1E4C')

    Jump('loc_21CB')

    def _loc_1E4F(): pass

    label('loc_1E4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1EB0',
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

    Jump('loc_1F2E')

    def _loc_1EB0(): pass

    label('loc_1EB0')

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

    def _loc_1F2E(): pass

    label('loc_1F2E')

    Jump('loc_21CB')

    def _loc_1F31(): pass

    label('loc_1F31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1FAB',
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

    Jump('loc_21CB')

    def _loc_1FAB(): pass

    label('loc_1FAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_206A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1FFF',
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

    Jump('loc_2067')

    def _loc_1FFF(): pass

    label('loc_1FFF')

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

    def _loc_2067(): pass

    label('loc_2067')

    Jump('loc_21CB')

    def _loc_206A(): pass

    label('loc_206A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2160',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_20CB',
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

    Jump('loc_215D')

    def _loc_20CB(): pass

    label('loc_20CB')

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

    def _loc_215D(): pass

    label('loc_215D')

    Jump('loc_21CB')

    def _loc_2160(): pass

    label('loc_2160')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_21CB',
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

    def _loc_21CB(): pass

    label('loc_21CB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x21CF
@scena.Code('func_0E_21CF')
def func_0E_21CF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_23B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_2255',
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

    Jump('loc_23B0')

    def _loc_2255(): pass

    label('loc_2255')

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

    def _loc_23B0(): pass

    label('loc_23B0')

    Jump('loc_2585')

    def _loc_23B3(): pass

    label('loc_23B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_23EE',
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

    Jump('loc_2585')

    def _loc_23EE(): pass

    label('loc_23EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_243E',
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

    Jump('loc_2585')

    def _loc_243E(): pass

    label('loc_243E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2542',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_24A6',
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

    Jump('loc_253F')

    def _loc_24A6(): pass

    label('loc_24A6')

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

    def _loc_253F(): pass

    label('loc_253F')

    Jump('loc_2585')

    def _loc_2542(): pass

    label('loc_2542')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_254C',
    )

    Jump('loc_2585')

    def _loc_254C(): pass

    label('loc_254C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2556',
    )

    Jump('loc_2585')

    def _loc_2556(): pass

    label('loc_2556')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2560',
    )

    Jump('loc_2585')

    def _loc_2560(): pass

    label('loc_2560')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_256A',
    )

    Jump('loc_2585')

    def _loc_256A(): pass

    label('loc_256A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2574',
    )

    Jump('loc_2585')

    def _loc_2574(): pass

    label('loc_2574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_257E',
    )

    Jump('loc_2585')

    def _loc_257E(): pass

    label('loc_257E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2585',
    )

    def _loc_2585(): pass

    label('loc_2585')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2589
@scena.Code('func_0F_2589')
def func_0F_2589():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2721',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_2606',
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

    Jump('loc_271E')

    def _loc_2606(): pass

    label('loc_2606')

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

    def _loc_271E(): pass

    label('loc_271E')

    Jump('loc_2782')

    def _loc_2721(): pass

    label('loc_2721')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_272B',
    )

    Jump('loc_2782')

    def _loc_272B(): pass

    label('loc_272B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2735',
    )

    Jump('loc_2782')

    def _loc_2735(): pass

    label('loc_2735')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_273F',
    )

    Jump('loc_2782')

    def _loc_273F(): pass

    label('loc_273F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2749',
    )

    Jump('loc_2782')

    def _loc_2749(): pass

    label('loc_2749')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2753',
    )

    Jump('loc_2782')

    def _loc_2753(): pass

    label('loc_2753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_275D',
    )

    Jump('loc_2782')

    def _loc_275D(): pass

    label('loc_275D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2767',
    )

    Jump('loc_2782')

    def _loc_2767(): pass

    label('loc_2767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2771',
    )

    Jump('loc_2782')

    def _loc_2771(): pass

    label('loc_2771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_277B',
    )

    Jump('loc_2782')

    def _loc_277B(): pass

    label('loc_277B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2782',
    )

    def _loc_2782(): pass

    label('loc_2782')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x2786
@scena.Code('func_10_2786')
def func_10_2786():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_28B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2813',
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

    Jump('loc_28B6')

    def _loc_2813(): pass

    label('loc_2813')

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

    def _loc_28B6(): pass

    label('loc_28B6')

    Jump('loc_2C72')

    def _loc_28B9(): pass

    label('loc_28B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2928',
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

    Jump('loc_2C72')

    def _loc_2928(): pass

    label('loc_2928')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2996',
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

    Jump('loc_2C72')

    def _loc_2996(): pass

    label('loc_2996')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2A04',
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

    Jump('loc_2C72')

    def _loc_2A04(): pass

    label('loc_2A04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2A41',
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

    Jump('loc_2C72')

    def _loc_2A41(): pass

    label('loc_2A41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2A77',
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

    Jump('loc_2C72')

    def _loc_2A77(): pass

    label('loc_2A77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2A9F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，书籍是心灵的养料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C72')

    def _loc_2A9F(): pass

    label('loc_2A9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2B0E',
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

    Jump('loc_2C72')

    def _loc_2B0E(): pass

    label('loc_2B0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2B4B',
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

    Jump('loc_2C72')

    def _loc_2B4B(): pass

    label('loc_2B4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2C15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_2BA5',
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

    Jump('loc_2C12')

    def _loc_2BA5(): pass

    label('loc_2BA5')

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

    def _loc_2C12(): pass

    label('loc_2C12')

    Jump('loc_2C72')

    def _loc_2C15(): pass

    label('loc_2C15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2C72',
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

    def _loc_2C72(): pass

    label('loc_2C72')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2C76
@scena.Code('func_11_2C76')
def func_11_2C76():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2D01',
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

    Jump('loc_3399')

    def _loc_2D01(): pass

    label('loc_2D01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2DF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2D6A',
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

    Jump('loc_2DF6')

    def _loc_2D6A(): pass

    label('loc_2D6A')

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

    def _loc_2DF6(): pass

    label('loc_2DF6')

    Jump('loc_3399')

    def _loc_2DF9(): pass

    label('loc_2DF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2EF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2E62',
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

    Jump('loc_2EF0')

    def _loc_2E62(): pass

    label('loc_2E62')

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

    def _loc_2EF0(): pass

    label('loc_2EF0')

    Jump('loc_3399')

    def _loc_2EF3(): pass

    label('loc_2EF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2F5D',
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

    Jump('loc_3399')

    def _loc_2F5D(): pass

    label('loc_2F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2FF6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2FA3',
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

    Jump('loc_2FF3')

    def _loc_2FA3(): pass

    label('loc_2FA3')

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

    def _loc_2FF3(): pass

    label('loc_2FF3')

    Jump('loc_3399')

    def _loc_2FF6(): pass

    label('loc_2FF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_30F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_306A',
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

    Jump('loc_30EF')

    def _loc_306A(): pass

    label('loc_306A')

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

    def _loc_30EF(): pass

    label('loc_30EF')

    Jump('loc_3399')

    def _loc_30F2(): pass

    label('loc_30F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3184',
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

    Jump('loc_3399')

    def _loc_3184(): pass

    label('loc_3184')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_328B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_31E9',
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

    Jump('loc_3288')

    def _loc_31E9(): pass

    label('loc_31E9')

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

    def _loc_3288(): pass

    label('loc_3288')

    Jump('loc_3399')

    def _loc_328B(): pass

    label('loc_328B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_32E5',
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

    Jump('loc_3399')

    def _loc_32E5(): pass

    label('loc_32E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_335F',
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

    Jump('loc_3399')

    def _loc_335F(): pass

    label('loc_335F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3399',
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

    def _loc_3399(): pass

    label('loc_3399')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x339D
@scena.Code('func_12_339D')
def func_12_339D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_33A7',
    )

    Jump('loc_34CA')

    def _loc_33A7(): pass

    label('loc_33A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_33FD',
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

    Jump('loc_34CA')

    def _loc_33FD(): pass

    label('loc_33FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3429',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典之前都没什么事做呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CA')

    def _loc_3429(): pass

    label('loc_3429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3487',
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

    Jump('loc_34CA')

    def _loc_3487(): pass

    label('loc_3487')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3491',
    )

    Jump('loc_34CA')

    def _loc_3491(): pass

    label('loc_3491')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_349B',
    )

    Jump('loc_34CA')

    def _loc_349B(): pass

    label('loc_349B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_34A5',
    )

    Jump('loc_34CA')

    def _loc_34A5(): pass

    label('loc_34A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_34AF',
    )

    Jump('loc_34CA')

    def _loc_34AF(): pass

    label('loc_34AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_34B9',
    )

    Jump('loc_34CA')

    def _loc_34B9(): pass

    label('loc_34B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_34C3',
    )

    Jump('loc_34CA')

    def _loc_34C3(): pass

    label('loc_34C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_34CA',
    )

    def _loc_34CA(): pass

    label('loc_34CA')

    Return()

# id: 0x0013 offset: 0x34CB
@scena.Code('func_13_34CB')
def func_13_34CB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_34D5',
    )

    Jump('loc_35CC')

    def _loc_34D5(): pass

    label('loc_34D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_350D',
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

    Jump('loc_35CC')

    def _loc_350D(): pass

    label('loc_350D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_355C',
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

    Jump('loc_35CC')

    def _loc_355C(): pass

    label('loc_355C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3589',
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

    Jump('loc_35CC')

    def _loc_3589(): pass

    label('loc_3589')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3593',
    )

    Jump('loc_35CC')

    def _loc_3593(): pass

    label('loc_3593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_359D',
    )

    Jump('loc_35CC')

    def _loc_359D(): pass

    label('loc_359D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_35A7',
    )

    Jump('loc_35CC')

    def _loc_35A7(): pass

    label('loc_35A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_35B1',
    )

    Jump('loc_35CC')

    def _loc_35B1(): pass

    label('loc_35B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_35BB',
    )

    Jump('loc_35CC')

    def _loc_35BB(): pass

    label('loc_35BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_35C5',
    )

    Jump('loc_35CC')

    def _loc_35C5(): pass

    label('loc_35C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_35CC',
    )

    def _loc_35CC(): pass

    label('loc_35CC')

    Return()

# id: 0x0014 offset: 0x35CD
@scena.Code('func_14_35CD')
def func_14_35CD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_35DA',
    )

    Jump('loc_3683')

    def _loc_35DA(): pass

    label('loc_35DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_35E4',
    )

    Jump('loc_3683')

    def _loc_35E4(): pass

    label('loc_35E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_35EE',
    )

    Jump('loc_3683')

    def _loc_35EE(): pass

    label('loc_35EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3640',
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

    Jump('loc_3683')

    def _loc_3640(): pass

    label('loc_3640')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_364A',
    )

    Jump('loc_3683')

    def _loc_364A(): pass

    label('loc_364A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3654',
    )

    Jump('loc_3683')

    def _loc_3654(): pass

    label('loc_3654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_365E',
    )

    Jump('loc_3683')

    def _loc_365E(): pass

    label('loc_365E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3668',
    )

    Jump('loc_3683')

    def _loc_3668(): pass

    label('loc_3668')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3672',
    )

    Jump('loc_3683')

    def _loc_3672(): pass

    label('loc_3672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_367C',
    )

    Jump('loc_3683')

    def _loc_367C(): pass

    label('loc_367C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3683',
    )

    def _loc_3683(): pass

    label('loc_3683')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x3687
@scena.Code('func_15_3687')
def func_15_3687():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3694',
    )

    Jump('loc_37E1')

    def _loc_3694(): pass

    label('loc_3694')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_369E',
    )

    Jump('loc_37E1')

    def _loc_369E(): pass

    label('loc_369E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_36A8',
    )

    Jump('loc_37E1')

    def _loc_36A8(): pass

    label('loc_36A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_379E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3715',
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

    Jump('loc_379B')

    def _loc_3715(): pass

    label('loc_3715')

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

    def _loc_379B(): pass

    label('loc_379B')

    Jump('loc_37E1')

    def _loc_379E(): pass

    label('loc_379E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_37A8',
    )

    Jump('loc_37E1')

    def _loc_37A8(): pass

    label('loc_37A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_37B2',
    )

    Jump('loc_37E1')

    def _loc_37B2(): pass

    label('loc_37B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_37BC',
    )

    Jump('loc_37E1')

    def _loc_37BC(): pass

    label('loc_37BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_37C6',
    )

    Jump('loc_37E1')

    def _loc_37C6(): pass

    label('loc_37C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_37D0',
    )

    Jump('loc_37E1')

    def _loc_37D0(): pass

    label('loc_37D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_37DA',
    )

    Jump('loc_37E1')

    def _loc_37DA(): pass

    label('loc_37DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_37E1',
    )

    def _loc_37E1(): pass

    label('loc_37E1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x37E5
@scena.Code('func_16_37E5')
def func_16_37E5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_37F2',
    )

    Jump('loc_3A92')

    def _loc_37F2(): pass

    label('loc_37F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_37FC',
    )

    Jump('loc_3A92')

    def _loc_37FC(): pass

    label('loc_37FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3806',
    )

    Jump('loc_3A92')

    def _loc_3806(): pass

    label('loc_3806')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3810',
    )

    Jump('loc_3A92')

    def _loc_3810(): pass

    label('loc_3810')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_381A',
    )

    Jump('loc_3A92')

    def _loc_381A(): pass

    label('loc_381A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3933',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_389F',
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

    Jump('loc_3930')

    def _loc_389F(): pass

    label('loc_389F')

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

    def _loc_3930(): pass

    label('loc_3930')

    Jump('loc_3A92')

    def _loc_3933(): pass

    label('loc_3933')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_393D',
    )

    Jump('loc_3A92')

    def _loc_393D(): pass

    label('loc_393D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3A33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_39B3',
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

    Jump('loc_3A30')

    def _loc_39B3(): pass

    label('loc_39B3')

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

    def _loc_3A30(): pass

    label('loc_3A30')

    Jump('loc_3A92')

    def _loc_3A33(): pass

    label('loc_3A33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3A3D',
    )

    Jump('loc_3A92')

    def _loc_3A3D(): pass

    label('loc_3A3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3A8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_3A88',
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

    def _loc_3A88(): pass

    label('loc_3A88')

    Jump('loc_3A92')

    def _loc_3A8B(): pass

    label('loc_3A8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3A92',
    )

    def _loc_3A92(): pass

    label('loc_3A92')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x3A96
@scena.Code('func_17_3A96')
def func_17_3A96():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3D6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3B19',
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

    Jump('loc_3D6A')

    def _loc_3B19(): pass

    label('loc_3B19')

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

    def _loc_3D6A(): pass

    label('loc_3D6A')

    Jump('loc_3F3D')

    def _loc_3D6D(): pass

    label('loc_3D6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3D77',
    )

    Jump('loc_3F3D')

    def _loc_3D77(): pass

    label('loc_3D77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3D81',
    )

    Jump('loc_3F3D')

    def _loc_3D81(): pass

    label('loc_3D81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3D8B',
    )

    Jump('loc_3F3D')

    def _loc_3D8B(): pass

    label('loc_3D8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3D95',
    )

    Jump('loc_3F3D')

    def _loc_3D95(): pass

    label('loc_3D95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3DED',
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

    Jump('loc_3F3D')

    def _loc_3DED(): pass

    label('loc_3DED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3DF7',
    )

    Jump('loc_3F3D')

    def _loc_3DF7(): pass

    label('loc_3DF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3F22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3E3C',
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

    Jump('loc_3F1F')

    def _loc_3E3C(): pass

    label('loc_3E3C')

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

    def _loc_3F1F(): pass

    label('loc_3F1F')

    Jump('loc_3F3D')

    def _loc_3F22(): pass

    label('loc_3F22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3F2C',
    )

    Jump('loc_3F3D')

    def _loc_3F2C(): pass

    label('loc_3F2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3F36',
    )

    Jump('loc_3F3D')

    def _loc_3F36(): pass

    label('loc_3F36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3F3D',
    )

    def _loc_3F3D(): pass

    label('loc_3F3D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x3F41
@scena.Code('func_18_3F41')
def func_18_3F41():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_404D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3FC2',
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

    Jump('loc_404A')

    def _loc_3FC2(): pass

    label('loc_3FC2')

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

    def _loc_404A(): pass

    label('loc_404A')

    Jump('loc_475A')

    def _loc_404D(): pass

    label('loc_404D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_40A7',
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

    Jump('loc_475A')

    def _loc_40A7(): pass

    label('loc_40A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4109',
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

    Jump('loc_475A')

    def _loc_4109(): pass

    label('loc_4109')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4171',
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

    Jump('loc_475A')

    def _loc_4171(): pass

    label('loc_4171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4262',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_41E4',
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

    Jump('loc_425F')

    def _loc_41E4(): pass

    label('loc_41E4')

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

    def _loc_425F(): pass

    label('loc_425F')

    Jump('loc_475A')

    def _loc_4262(): pass

    label('loc_4262')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_42E3',
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

    Jump('loc_475A')

    def _loc_42E3(): pass

    label('loc_42E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_434F',
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

    Jump('loc_475A')

    def _loc_434F(): pass

    label('loc_434F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4451',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_43C2',
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

    Jump('loc_444E')

    def _loc_43C2(): pass

    label('loc_43C2')

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

    def _loc_444E(): pass

    label('loc_444E')

    Jump('loc_475A')

    def _loc_4451(): pass

    label('loc_4451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_45B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_44EB',
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

    Jump('loc_45AD')

    def _loc_44EB(): pass

    label('loc_44EB')

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

    def _loc_45AD(): pass

    label('loc_45AD')

    Jump('loc_475A')

    def _loc_45B0(): pass

    label('loc_45B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4619',
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

    Jump('loc_475A')

    def _loc_4619(): pass

    label('loc_4619')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_475A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_464F',
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

    Jump('loc_475A')

    def _loc_464F(): pass

    label('loc_464F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_46B4',
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

    Jump('loc_475A')

    def _loc_46B4(): pass

    label('loc_46B4')

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

    def _loc_475A(): pass

    label('loc_475A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x475E
@scena.Code('func_19_475E')
def func_19_475E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_483A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_47A9',
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

    Jump('loc_4837')

    def _loc_47A9(): pass

    label('loc_47A9')

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

    def _loc_4837(): pass

    label('loc_4837')

    Jump('loc_4D69')

    def _loc_483A(): pass

    label('loc_483A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4887',
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

    Jump('loc_4D69')

    def _loc_4887(): pass

    label('loc_4887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_48F0',
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

    Jump('loc_4D69')

    def _loc_48F0(): pass

    label('loc_48F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_494B',
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

    Jump('loc_4D69')

    def _loc_494B(): pass

    label('loc_494B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_49BA',
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

    Jump('loc_4D69')

    def _loc_49BA(): pass

    label('loc_49BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4A1F',
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

    Jump('loc_4D69')

    def _loc_4A1F(): pass

    label('loc_4A1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4A96',
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

    Jump('loc_4D69')

    def _loc_4A96(): pass

    label('loc_4A96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4ADB',
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

    Jump('loc_4D69')

    def _loc_4ADB(): pass

    label('loc_4ADB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4BCA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4B24',
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

    Jump('loc_4BC7')

    def _loc_4B24(): pass

    label('loc_4B24')

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

    def _loc_4BC7(): pass

    label('loc_4BC7')

    Jump('loc_4D69')

    def _loc_4BCA(): pass

    label('loc_4BCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4C84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_4C48',
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

    Jump('loc_4C81')

    def _loc_4C48(): pass

    label('loc_4C48')

    ChrTalk(
        0x00FE,
        (
            '大会的预选赛好像已经结束了。\n',
            '这里客人立刻多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C81(): pass

    label('loc_4C81')

    Jump('loc_4D69')

    def _loc_4C84(): pass

    label('loc_4C84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4D69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4CE1',
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

    Jump('loc_4D69')

    def _loc_4CE1(): pass

    label('loc_4CE1')

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

    def _loc_4D69(): pass

    label('loc_4D69')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x4D6D
@scena.Code('func_1A_4D6D')
def func_1A_4D6D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4F51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4DF6',
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

    Jump('loc_4F51')

    def _loc_4DF6(): pass

    label('loc_4DF6')

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

    def _loc_4F51(): pass

    label('loc_4F51')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x4F55
@scena.Code('func_1B_4F55')
def func_1B_4F55():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5333',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 3930, 0, -620, 0)
    ChrSetPos(0x0102, 5070, 0, -540, 0)
    ChrSetPos(0x0108, 4540, 0, -1430, 0)
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

    @scena.Lambda('lambda_528E')
    def lambda_528E():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_528E')

    DispatchAsync2(0x0101, 0x0001, lambda_528E)

    @scena.Lambda('lambda_529F')
    def lambda_529F():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_529F')

    DispatchAsync2(0x0102, 0x0001, lambda_529F)

    @scena.Lambda('lambda_52B0')
    def lambda_52B0():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_52B0')

    DispatchAsync2(0x0108, 0x0001, lambda_52B0)

    ChrWalkTo(0x000C, 3050, 0, 30, 3000, 0x00)
    ChrWalkTo(0x000C, 1030, 0, -3070, 3000, 0x00)
    ChrWalkTo(0x000C, 710, -250, -5490, 3000, 0x00)

    @scena.Lambda('lambda_52FD')
    def lambda_52FD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_52FD)

    ChrWalkTo(0x000C, 710, -250, -7470, 3000, 0x00)
    ChrSetFlags(0x000C, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    EventEnd(0x00)

    Jump('loc_5850')

    def _loc_5333(): pass

    label('loc_5333')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_550E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5395',
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

    Jump('loc_550B')

    def _loc_5395(): pass

    label('loc_5395')

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

    def _loc_550B(): pass

    label('loc_550B')

    Jump('loc_5850')

    def _loc_550E(): pass

    label('loc_550E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5518',
    )

    Jump('loc_5850')

    def _loc_5518(): pass

    label('loc_5518')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5522',
    )

    Jump('loc_5850')

    def _loc_5522(): pass

    label('loc_5522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_564F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_558F',
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

    Jump('loc_564C')

    def _loc_558F(): pass

    label('loc_558F')

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

    def _loc_564C(): pass

    label('loc_564C')

    Jump('loc_5850')

    def _loc_564F(): pass

    label('loc_564F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5659',
    )

    Jump('loc_5850')

    def _loc_5659(): pass

    label('loc_5659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5663',
    )

    Jump('loc_5850')

    def _loc_5663(): pass

    label('loc_5663')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_566D',
    )

    Jump('loc_5850')

    def _loc_566D(): pass

    label('loc_566D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5677',
    )

    Jump('loc_5850')

    def _loc_5677(): pass

    label('loc_5677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_583F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_56D0',
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

    Jump('loc_583C')

    def _loc_56D0(): pass

    label('loc_56D0')

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

    def _loc_583C(): pass

    label('loc_583C')

    Jump('loc_5850')

    def _loc_583F(): pass

    label('loc_583F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5849',
    )

    Jump('loc_5850')

    def _loc_5849(): pass

    label('loc_5849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5850',
    )

    def _loc_5850(): pass

    label('loc_5850')

    TalkEnd(0x000C)

    Return()

# id: 0x001C offset: 0x5854
@scena.Code('func_1C_5854')
def func_1C_5854():
    Return()

# id: 0x001D offset: 0x5855
@scena.Code('func_1D_5855')
def func_1D_5855():
    EventBegin(0x00)
    ChrSetFlags(0x0108, 0x0004)
    ChrSetPos(0x0108, -3800, 0, -2180, 180)
    ChrSetPos(0x0101, -3460, 0, -4600, 0)
    ChrSetPos(0x0102, -4940, 0, -4600, 0)
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
    ChrSetPos(0x0008, -1920, 4000, 4680, 180)
    ChrClearFlags(0x0008, 0x0080)

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

    @scena.Lambda('lambda_5E7C')
    def lambda_5E7C():
        CameraMove(-2350, 0, -630, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5E7C)

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
    ChrSetFlags(0x0008, 0x0004)
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

# id: 0x001E offset: 0x6925
@scena.Code('func_1E_6925')
def func_1E_6925():
    EventBegin(0x00)
    CameraMove(63970, 200, 7220, 0)
    OP_67(0, 7860, -10000, 0)
    CameraSetDistance(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetChipByIndex(0x0101, 23)
    ChrSetChipByIndex(0x0102, 24)
    ChrSetChipByIndex(0x0009, 25)
    ChrSetPos(0x0020, 58830, 640, -4430, 0)
    ChrSetPos(0x0025, 58360, 640, -4450, 0)
    ChrSetPos(0x0022, 59290, 640, -4980, 0)
    ChrSetPos(0x0023, 59290, 640, -4720, 0)
    ChrSetPos(0x0021, 58740, 640, -5400, 0)
    ChrSetPos(0x0024, 58930, 640, -5550, 0)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0101, 60050, 200, -4970, 270)
    ChrSetPos(0x0009, 58770, 200, -3750, 180)
    ChrSetPos(0x0102, 58770, 200, -6150, 0)
    ChrSetPos(0x0016, 62360, 0, 2910, 0)
    ChrClearFlags(0x0009, 0x0080)
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

    ChrSetSubChip(0x0009, 3)
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

    ChrSetSubChip(0x0009, 0)

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
    TalkSetChrName('')

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

    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x8013
@scena.Code('func_1F_8013')
def func_1F_8013():
    EventBegin(0x00)
    CameraMove(-61470, 0, 67180, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0009, -56660, 0, 64750, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, -61900, 0, 67420, 135)
    ChrSetPos(0x0102, -63460, 0, 66810, 135)

    ChrTalk(
        0x0101,
        (
            '#000F喂～奈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_80A5')
    def lambda_80A5():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_80A5)

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

    @scena.Lambda('lambda_8124')
    def lambda_8124():
        CameraMove(-57890, 0, 65099, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8124)

    @scena.Lambda('lambda_813C')
    def lambda_813C():
        CameraSetDistance(2600, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_813C)

    @scena.Lambda('lambda_814C')
    def lambda_814C():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_814C')

    DispatchAsync2(0x0101, 0x0001, lambda_814C)

    @scena.Lambda('lambda_815D')
    def lambda_815D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_815D')

    DispatchAsync2(0x0009, 0x0001, lambda_815D)

    @scena.Lambda('lambda_816E')
    def lambda_816E():
        ChrWalkTo(0x00FE, -59150, 0, 64660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_816E)

    ChrWalkTo(0x0102, -60560, 0, 66670, 3000, 0x00)

    @scena.Lambda('lambda_819D')
    def lambda_819D():
        ChrWalkTo(0x00FE, -57490, 0, 64410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_819D)

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
    def _loc_8433(): pass

    label('loc_8433')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C3C',
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
        'loc_84AE',
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

    Jump('loc_84E4')

    def _loc_84AE(): pass

    label('loc_84AE')

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

    def _loc_84E4(): pass

    label('loc_84E4')

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
        (0x00000000, 'loc_8517'),
        (0x00000001, 'loc_87FF'),
        (0x00000002, 'loc_8A00'),
        (0x00000003, 'loc_8C29'),
        (-1, 'loc_8C39'),
    )

    def _loc_8517(): pass

    label('loc_8517')

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
        'loc_87FC',
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

    def _loc_87FC(): pass

    label('loc_87FC')

    Jump('loc_8C39')

    def _loc_87FF(): pass

    label('loc_87FF')

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
        'loc_89FD',
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

    def _loc_89FD(): pass

    label('loc_89FD')

    Jump('loc_8C39')

    def _loc_8A00(): pass

    label('loc_8A00')

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
        'loc_8C26',
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

    def _loc_8C26(): pass

    label('loc_8C26')

    Jump('loc_8C39')

    def _loc_8C29(): pass

    label('loc_8C29')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_8C39')

    def _loc_8C39(): pass

    label('loc_8C39')

    Jump('loc_8433')

    def _loc_8C3C(): pass

    label('loc_8C3C')

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
        (0x00000000, 'loc_919E'),
        (0x00000001, 'loc_923B'),
        (0x00000002, 'loc_92CE'),
        (-1, 'loc_9375'),
    )

    def _loc_919E(): pass

    label('loc_919E')

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

    Jump('loc_9375')

    def _loc_923B(): pass

    label('loc_923B')

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

    Jump('loc_9375')

    def _loc_92CE(): pass

    label('loc_92CE')

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

    Jump('loc_9375')

    def _loc_9375(): pass

    label('loc_9375')

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

    @scena.Lambda('lambda_9813')
    def lambda_9813():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_9813')

    DispatchAsync2(0x0101, 0x0001, lambda_9813)

    @scena.Lambda('lambda_9824')
    def lambda_9824():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_9824')

    DispatchAsync2(0x0102, 0x0001, lambda_9824)

    ChrWalkTo(0x0009, -58470, 0, 65300, 3000, 0x00)
    ChrWalkTo(0x0009, -60060, 0, 65300, 3000, 0x00)
    ChrWalkTo(0x0009, -60840, 0, 66460, 3000, 0x00)
    ChrWalkTo(0x0009, -63690, 0, 66460, 3000, 0x00)
    ChrWalkTo(0x0009, -63690, -2230, 62470, 3000, 0x00)
    ChrSetFlags(0x0009, 0x0080)
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

# id: 0x0020 offset: 0x995A
@scena.Code('func_20_995A')
def func_20_995A():
    EventBegin(0x00)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -56250, 0, 60940, 90)
    ChrSetPos(0x0101, -60190, 0, 65280, 135)
    ChrSetPos(0x0102, -61190, 0, 64849, 135)
    ChrSetPos(0x0108, -60700, 0, 66190, 135)
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

    @scena.Lambda('lambda_9AB6')
    def lambda_9AB6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_9AB6)

    CameraMove(-56640, 0, 63970, 2000)

    ChrTalk(
        0x000A,
        (
            '#150F啊，小艾你们来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9AF2')
    def lambda_9AF2():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_9AF2')

    DispatchAsync2(0x000A, 0x0001, lambda_9AF2)

    @scena.Lambda('lambda_9B03')
    def lambda_9B03():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_9B03')

    DispatchAsync2(0x0101, 0x0001, lambda_9B03)

    @scena.Lambda('lambda_9B14')
    def lambda_9B14():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_9B14')

    DispatchAsync2(0x0102, 0x0001, lambda_9B14)

    @scena.Lambda('lambda_9B25')
    def lambda_9B25():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_9B25')

    DispatchAsync2(0x0108, 0x0001, lambda_9B25)

    @scena.Lambda('lambda_9B36')
    def lambda_9B36():
        ChrWalkTo(0x00FE, -54540, 0, 62770, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9B36)

    Sleep(100)

    @scena.Lambda('lambda_9B56')
    def lambda_9B56():
        ChrWalkTo(0x00FE, -55570, 0, 62750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_9B56)

    Sleep(300)

    @scena.Lambda('lambda_9B76')
    def lambda_9B76():
        ChrWalkTo(0x00FE, -56620, 0, 62700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_9B76)

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

    @scena.Lambda('lambda_9EFA')
    def lambda_9EFA():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9EFA)

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
        (0x00000000, 'loc_A05D'),
        (0x00000001, 'loc_A0E6'),
        (0x00000002, 'loc_A143'),
        (-1, 'loc_A1B5'),
    )

    def _loc_A05D(): pass

    label('loc_A05D')

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

    Jump('loc_A1B5')

    def _loc_A0E6(): pass

    label('loc_A0E6')

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

    Jump('loc_A1B5')

    def _loc_A143(): pass

    label('loc_A143')

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

    Jump('loc_A1B5')

    def _loc_A1B5(): pass

    label('loc_A1B5')

    ChrTalk(
        0x000B,
        (
            '#2310130290V你们说的是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A1DF')
    def lambda_A1DF():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A1DF)

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

    @scena.Lambda('lambda_A338')
    def lambda_A338():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A338)

    @scena.Lambda('lambda_A346')
    def lambda_A346():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_A346)

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

    @scena.Lambda('lambda_A3FB')
    def lambda_A3FB():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_A3FB)

    @scena.Lambda('lambda_A409')
    def lambda_A409():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A409)

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
        (0x00000000, 'loc_A708'),
        (0x00000001, 'loc_A854'),
        (0x00000002, 'loc_A881'),
        (-1, 'loc_A9C1'),
    )

    def _loc_A708(): pass

    label('loc_A708')

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

    Jump('loc_A9C1')

    def _loc_A854(): pass

    label('loc_A854')

    ChrTalk(
        0x0108,
        (
            '#070F哦，晚宴的时候\n',
            '公爵所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9C1')

    def _loc_A881(): pass

    label('loc_A881')

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

    Jump('loc_A9C1')

    def _loc_A9C1(): pass

    label('loc_A9C1')

    ChrTalk(
        0x000B,
        (
            '什么，奈尔和你们\n',
            '谈到了这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A9EC')
    def lambda_A9EC():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A9EC)

    @scena.Lambda('lambda_A9FA')
    def lambda_A9FA():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A9FA)

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

    @scena.Lambda('lambda_ABD6')
    def lambda_ABD6():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_ABD6)

    @scena.Lambda('lambda_ABE4')
    def lambda_ABE4():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_ABE4)

    @scena.Lambda('lambda_ABF2')
    def lambda_ABF2():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_ABF2)

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

    @scena.Lambda('lambda_AE8B')
    def lambda_AE8B():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_AE8B)

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

# id: 0x0021 offset: 0xAFEC
@scena.Code('func_21_AFEC')
def func_21_AFEC():
    EventBegin(0x00)
    CameraMove(-53660, 0, 62750, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x000A, -59130, 0, 59600, 0)
    ChrSetPos(0x0009, -53500, 0, 62630, 90)
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

    @scena.Lambda('lambda_B093')
    def lambda_B093():
        CameraMove(-56110, 0, 62480, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_B093)

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
