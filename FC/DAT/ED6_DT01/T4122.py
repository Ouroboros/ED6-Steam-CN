import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4122_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4122   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4122.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '莉莉',
            x                   = 8790,
            z                   = 0,
            y                   = 10500,
            direction           = 196,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '丹顿',
            x                   = 12170,
            z                   = 0,
            y                   = -4050,
            direction           = 163,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '基蒂',
            x                   = -13610,
            z                   = 250,
            y                   = 11140,
            direction           = 182,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '希娜',
            x                   = -12600,
            z                   = 0,
            y                   = 6400,
            direction           = 9,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '特雷诺',
            x                   = 13600,
            z                   = 0,
            y                   = -8480,
            direction           = 91,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '索菲娜',
            x                   = -8770,
            z                   = 0,
            y                   = -8610,
            direction           = 21,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '卡拉',
            x                   = 410,
            z                   = 0,
            y                   = 3810,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '卢希娅',
            x                   = 2650,
            z                   = 0,
            y                   = 3210,
            direction           = 106,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 9980,
            z                   = 0,
            y                   = 6170,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '艾德尔店长',
            x                   = -50,
            z                   = 0,
            y                   = 10,
            direction           = 204,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '菲尔妲',
            x                   = -1440,
            z                   = 0,
            y                   = 65550,
            direction           = 179,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '莎夏',
            x                   = 1970,
            z                   = 0,
            y                   = 65550,
            direction           = 175,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = -950,
            z                   = 0,
            y                   = 60990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 8850,
            z                   = 0,
            y                   = -10950,
            direction           = 282,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = -10430,
            z                   = 0,
            y                   = 9410,
            direction           = 178,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '蜜蒂',
            x                   = -4540,
            z                   = 0,
            y                   = 9850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
    )

# id: 0x10002 offset: 0x372
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x372
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x372
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 8450,
            triggerZ            = 0,
            triggerY            = 8650,
            triggerRange        = 800,
            actorX              = 8790,
            actorZ              = 1500,
            actorY              = 10500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 11970,
            triggerZ            = 0,
            triggerY            = -5950,
            triggerRange        = 800,
            actorX              = 12170,
            actorZ              = 1500,
            actorY              = -4050,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -6400,
            triggerZ            = 0,
            triggerY            = 9620,
            triggerRange        = 800,
            actorX              = -4540,
            actorZ              = 1500,
            actorY              = 9850,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1370,
            triggerZ            = 0,
            triggerY            = 63610,
            triggerRange        = 800,
            actorX              = -1440,
            actorZ              = 1500,
            actorY              = 65550,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1850,
            triggerZ            = 0,
            triggerY            = 63640,
            triggerRange        = 800,
            actorX              = 1970,
            actorZ              = 1500,
            actorY              = 65550,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x426
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_448',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 10500, 0, 5390, 90)

    def _loc_448(): pass

    label('loc_448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 8850, 0, -10160, 259)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 4100, 0, -10830, 100)
    CreateThread(0x0008, 0x00, 0x00, func_02_727)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x000E, 2470, 0, -3790, 78)

    Jump('loc_6CD')

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4EA',
    )

    ChrSetPos(0x000D, -11310, 0, 6390, 355)
    ChrSetPos(0x000E, 13600, 0, -11620, 107)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_6CD')

    def _loc_4EA(): pass

    label('loc_4EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_520',
    )

    ChrSetPos(0x000D, -13220, 0, 9430, 198)
    ChrSetPos(0x000E, 13600, 0, -7380, 82)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)

    Jump('loc_6CD')

    def _loc_520(): pass

    label('loc_520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_578',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 2890, 0, 3290, 87)
    CreateThread(0x0008, 0x00, 0x00, func_02_727)
    ChrSetPos(0x000D, -8740, 0, 9410, 165)
    ChrSetPos(0x000E, 5870, 0, -10820, 272)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)

    Jump('loc_6CD')

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5B8',
    )

    ChrSetPos(0x000D, -10560, 0, 9490, 200)
    ChrSetPos(0x000E, 4480, 0, -6130, 340)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_6CD')

    def _loc_5B8(): pass

    label('loc_5B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_60B',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 5000, 0, 1510, 0)
    CreateThread(0x0008, 0x00, 0x00, func_02_727)
    ChrSetPos(0x000D, -8890, 0, 6200, 349)
    ChrSetPos(0x000E, 13580, 0, -11020, 70)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    Jump('loc_6CD')

    def _loc_60B(): pass

    label('loc_60B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_641',
    )

    ChrSetPos(0x000D, -7480, 0, 4300, 104)
    ChrSetPos(0x000E, 4480, 0, -6130, 340)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_6CD')

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_661',
    )

    ChrSetPos(0x000D, -7480, 0, 4300, 104)
    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_6CD')

    def _loc_661(): pass

    label('loc_661')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_686',
    )

    ChrSetPos(0x000D, -12210, 250, 11380, 355)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_6CD')

    def _loc_686(): pass

    label('loc_686')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6BC',
    )

    ChrSetPos(0x000D, -11310, 0, 6390, 355)
    ChrSetPos(0x000E, 13580, 0, -11020, 70)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0016, 0x0080)

    Jump('loc_6CD')

    def _loc_6BC(): pass

    label('loc_6BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_6CD',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0016, 0x0080)

    def _loc_6CD(): pass

    label('loc_6CD')

    Return()

# id: 0x0001 offset: 0x6CE
@scena.Code('func_01_6CE')
def func_01_6CE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_701',
    )

    OP_B1('t4122_y')

    Jump('loc_70A')

    def _loc_701(): pass

    label('loc_701')

    OP_B1('t4122_n')

    def _loc_70A(): pass

    label('loc_70A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_71A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_71A(): pass

    label('loc_71A')

    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x727
@scena.Code('func_02_727')
def func_02_727():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_73C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_727')

    def _loc_73C(): pass

    label('loc_73C')

    Return()

# id: 0x0003 offset: 0x73D
@scena.Code('func_03_73D')
def func_03_73D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_760',
    )

    OP_8D(0x00FE, -12460, -5460, -5830, -11220, 3000)

    Jump('func_03_73D')

    def _loc_760(): pass

    label('loc_760')

    Return()

# id: 0x0004 offset: 0x761
@scena.Code('func_04_761')
def func_04_761():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_784',
    )

    OP_8D(0x00FE, 2190, 5370, 2900, 2580, 3000)

    Jump('func_04_761')

    def _loc_784(): pass

    label('loc_784')

    Return()

# id: 0x0005 offset: 0x785
@scena.Code('func_05_785')
def func_05_785():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_80C',
    )

    ChrTalk(
        0x0018,
        (
            '#0660140783V#720F殿下虚心地接受了\n',
            '陛下严厉的训斥和教育。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660140784V现在正在艾尔贝离宫的房间里面深刻地反省。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AA2')

    def _loc_80C(): pass

    label('loc_80C')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x0101,
        (
            '#0010140771V#004F哎呀，是菲利普先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0660140772V#720F……这、这不是\n',
            '艾丝蒂尔小姐和约修亚先生吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660140773V#722F前些日子由于我的教导无方，\n',
            '殿下给你们添了不少麻烦，实在是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140774V#505F说起来，\n',
            '杜南公爵现在到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0660140775V#720F哦，殿下虚心地接受了\n',
            '陛下严厉的训斥和教育。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660140776V现在正在艾尔贝离宫的房间里面深刻地反省。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140777V#000F哦，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140778V#014F那么菲利普先生今天来王都做什么呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0660140779V#722F啊，实、实际上\n',
            '是殿下叫我来帮他买炸面圈的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140780V#506F呵，呵～呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140781V（真的是在反省吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140782V#010F（可能还是老样子吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AA2(): pass

    label('loc_AA2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xAA6
@scena.Code('func_06_AA6')
def func_06_AA6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_B4F',
    )

    ChrTalk(
        0x0017,
        (
            '#0030140752V#020F等回了洛连特之后，\n',
            '大家一起去逛街购物吧。\n',
            '已经很久没有去了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140749V作为对你成为正游击士的奖赏，\n',
            '我会给你买一些好看的衣服哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D82')

    def _loc_B4F(): pass

    label('loc_B4F')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x00DD, 4, 0x6EC))

    ChrTalk(
        0x0017,
        (
            '#0030140742V#023F哎呀，是你们两个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140743V#000F雪拉姐，你在做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0030140744V#020F呵呵，偶尔也和同伴们\n',
            '来享受一下购物的乐趣嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140745V好不容易才有这样的机会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140746V#505F对了，\n',
            '小时候雪拉姐就经常\n',
            '带着我们去买东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0030140747V#021F是啊，老师外出时\n',
            '我们还时常三个人一起去呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140748V#020F怎么样？\n',
            '等回了洛连特之后，\n',
            '大家一起去逛街购物吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140749V作为对你成为正游击士的奖赏，\n',
            '我会给你买一些好看的衣服哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140750V#001F啊，真的吗？\n',
            '我要去我要去！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140751V雪拉姐，就这么定了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D82(): pass

    label('loc_D82')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xD86
@scena.Code('func_07_D86')
def func_07_D86():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D93',
    )

    Jump('loc_EAA')

    def _loc_D93(): pass

    label('loc_D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_D9D',
    )

    Jump('loc_EAA')

    def _loc_D9D(): pass

    label('loc_D9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_DA7',
    )

    Jump('loc_EAA')

    def _loc_DA7(): pass

    label('loc_DA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_DB1',
    )

    Jump('loc_EAA')

    def _loc_DB1(): pass

    label('loc_DB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_DBB',
    )

    Jump('loc_EAA')

    def _loc_DBB(): pass

    label('loc_DBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_DC5',
    )

    Jump('loc_EAA')

    def _loc_DC5(): pass

    label('loc_DC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_DCF',
    )

    Jump('loc_EAA')

    def _loc_DCF(): pass

    label('loc_DCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_DD9',
    )

    Jump('loc_EAA')

    def _loc_DD9(): pass

    label('loc_DD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_DE3',
    )

    Jump('loc_EAA')

    def _loc_DE3(): pass

    label('loc_DE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_E4D',
    )

    ChrTalk(
        0x00FE,
        (
            '一个个的事件相继发生，\n',
            '让飞艇公社也变得很辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去，\n',
            '现在想要谈买卖都很困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAA')

    def _loc_E4D(): pass

    label('loc_E4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_EAA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '终于到达格兰赛尔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于王国军盘查的缘故，\n',
            '到达的时间推迟了很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAA(): pass

    label('loc_EAA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xEAE
@scena.Code('func_08_EAE')
def func_08_EAE():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0xEB3
@scena.Code('func_09_EB3')
def func_09_EB3():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_EF6',
    )

    ChrTalk(
        0x0015,
        (
            '这下乘客们\n',
            '可以放心地享受\n',
            '愉快舒适的空中旅行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_EF6(): pass

    label('loc_EF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_F45',
    )

    ChrTalk(
        0x0015,
        (
            '真叫人难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '处于现在这种休业状态，\n',
            '什么事情也不能做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_F45(): pass

    label('loc_F45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_F99',
    )

    ChrTalk(
        0x0015,
        (
            '乘客们都\n',
            '纷纷回来退票了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '既然不能搭乘定期船，\n',
            '退票也是应该的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_F99(): pass

    label('loc_F99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_FD0',
    )

    ChrTalk(
        0x0015,
        (
            '武术大会能顺利结束，\n',
            '这可比什么都好呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_FD0(): pass

    label('loc_FD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1039',
    )

    ChrTalk(
        0x0015,
        (
            '今天是武术大会的最后一天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '虽说之前发生了恐怖事件，\n',
            '不过今年的武术大会还是很热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_1039(): pass

    label('loc_1039')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_117E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_10C1',
    )

    ChrTalk(
        0x0015,
        (
            '修理员佩顿师傅是专门负责\n',
            '『埃尔赛尤号』的修理工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '自从发生政变以来，\n',
            '飞船就被军方接管，\n',
            '很是让他郁闷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_117B')

    def _loc_10C1(): pass

    label('loc_10C1')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x0015,
        (
            '修理员佩顿师傅是专门负责\n',
            '『埃尔赛尤号』的修理工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '自从发生政变以来，\n',
            '飞船就被军方接管，\n',
            '很是让他郁闷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '那艘飞艇\n',
            '以前是由亲卫队在使用，\n',
            '本来就是王家的御用飞艇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_117B(): pass

    label('loc_117B')

    Jump('loc_1339')

    def _loc_117E(): pass

    label('loc_117E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_11F9',
    )

    ChrTalk(
        0x0015,
        (
            '因为『埃尔赛尤号』的缘故，\n',
            '我和亲卫队的人\n',
            '经常有谈话的机会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '他们虽然有些保守，\n',
            '但都是很认真的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_11F9(): pass

    label('loc_11F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_123D',
    )

    ChrTalk(
        0x0015,
        (
            '只要不是紧急事态，\n',
            '军队就不应该占用\n',
            '定期船的航线……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_123D(): pass

    label('loc_123D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1281',
    )

    ChrTalk(
        0x0015,
        (
            '这个时期为了\n',
            '武术大会和诞辰庆典\n',
            '而来的旅客果然很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_1281(): pass

    label('loc_1281')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1314',
    )

    ChrTalk(
        0x0015,
        (
            '为了配合诞辰庆典，\n',
            '公社本来准备了\n',
            '许多的活动议程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '但是接二连三的发生了这些事件，\n',
            '可能就不会按原计划执行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '真可惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1339')

    def _loc_1314(): pass

    label('loc_1314')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1339',
    )

    ChrTalk(
        0x0015,
        (
            '欢迎来到利贝尔飞艇公社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1339(): pass

    label('loc_1339')

    TalkEnd(0x0015)

    Return()

# id: 0x000A offset: 0x133D
@scena.Code('func_0A_133D')
def func_0A_133D():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x1342
@scena.Code('func_0B_1342')
def func_0B_1342():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1469',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_13C4',
    )

    ChrTalk(
        0x0014,
        (
            '这个空港曾一度被封锁，\n',
            '竟然是为了便于发动政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '如果早知道是这样，\n',
            '才不会那么轻易就让它被封锁住呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1466')

    def _loc_13C4(): pass

    label('loc_13C4')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x0014,
        (
            '这个空港曾一度被封锁，\n',
            '竟然是为了便于发动政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '如果早知道是这样，\n',
            '才不会那么轻易就让它被封锁住呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '不管怎么说，\n',
            '终归还是平安地迎来了诞辰庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1466(): pass

    label('loc_1466')

    Jump('loc_1BA2')

    def _loc_1469(): pass

    label('loc_1469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_14FB',
    )

    ChrTalk(
        0x0014,
        (
            '说起来，\n',
            '前不久有一位修女\n',
            '去拜访了修理员佩顿师傅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '难道说他因为『埃尔赛尤号』\n',
            '被军队带走而受了打击，\n',
            '准备出家做修道士了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_14FB(): pass

    label('loc_14FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_156D',
    )

    ChrTalk(
        0x0014,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '空港再一次被\n',
            '王国军给封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '他们做得也有些太过分了吧。\n',
            '不知道什么叫适可而止吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_156D(): pass

    label('loc_156D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_15E8',
    )

    ChrTalk(
        0x0014,
        (
            '今天王城里的晚宴，\n',
            '公爵邀请的都是像\n',
            '各地市长这样有权有势的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '如果这时出现恐怖袭击，\n',
            '那该怎么办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_15E8(): pass

    label('loc_15E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1667',
    )

    ChrTalk(
        0x0014,
        (
            '托柏斯的空贼事件和\n',
            '王国军最近封锁政策的福，\n',
            '公社这个财政季度又是大赤字了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '最近就没有什么\n',
            '好一点的消息吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_1667(): pass

    label('loc_1667')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_17A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_16FC',
    )

    ChrTalk(
        0x0014,
        (
            '因为看守『埃尔赛尤号』\n',
            '也是要重点加强的工作，\n',
            '军方还说要我们帮他们的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '不过即使协助军方，\n',
            '他们也不会给公社\n',
            '任何补贴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A6')

    def _loc_16FC(): pass

    label('loc_16FC')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x0014,
        (
            '军方似乎加强了\n',
            '大街上的警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '因为看守『埃尔赛尤号』\n',
            '也是要重点加强的工作，\n',
            '军方还说要我们帮他们的忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '不过即使协助军方，\n',
            '他们也不会给公社\n',
            '任何补贴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A6(): pass

    label('loc_17A6')

    Jump('loc_1BA2')

    def _loc_17A9(): pass

    label('loc_17A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_18BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1822',
    )

    ChrTalk(
        0x0014,
        (
            '其他地区的市民还不是很清楚\n',
            '女王陛下身体欠佳的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '所以仍然有很多人\n',
            '为了诞辰庆典来到王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18B8')

    def _loc_1822(): pass

    label('loc_1822')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x0014,
        (
            '其他地区的市民还不是很清楚\n',
            '女王陛下身体欠佳的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '所以仍然有很多人\n',
            '为了诞辰庆典来到王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '不过，\n',
            '就算在这里抱怨也无济于事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18B8(): pass

    label('loc_18B8')

    Jump('loc_1BA2')

    def _loc_18BB(): pass

    label('loc_18BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_193C',
    )

    ChrTalk(
        0x0014,
        (
            '因为王国军\n',
            '强行占用各地的飞艇坪，\n',
            '定期船运行时刻表都被打乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '之前也是因为军队的行动\n',
            '而导致航班一推再推……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_193C(): pass

    label('loc_193C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_19E5',
    )

    ChrTalk(
        0x0014,
        (
            '在武术大会和诞辰庆典期间，\n',
            '与乘定期船外出的旅客数量相比，\n',
            '抵达这里的旅客要更多一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '抱怨的人和迷路的人也相应增多，\n',
            '必须要以饱满的精神来应对才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_19E5(): pass

    label('loc_19E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A83',
    )

    ChrTalk(
        0x0014,
        (
            '空港里除了定期船，\n',
            '还有其他的飞艇停泊在这里，\n',
            '比如『埃尔赛尤号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '原本这是亲卫队使用的飞艇，\n',
            '但自从政变发生之后，\n',
            '就由王国军代为保管了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_1A83(): pass

    label('loc_1A83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1BA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1AFE',
    )

    ChrTalk(
        0x0014,
        (
            '因为王国军的盘查，\n',
            '原定的航行时刻表被搅乱得一塌糊涂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '哎呀，真希望乘客们\n',
            '能够理解我们的难处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BA2')

    def _loc_1AFE(): pass

    label('loc_1AFE')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x0014,
        (
            '因为王国军的盘查，\n',
            '原定的航行时刻表被搅乱得一塌糊涂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '哎呀，真希望乘客们\n',
            '能够理解我们的难处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '我们又没有什么过错，\n',
            '为何还一定要去赔礼道歉呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BA2(): pass

    label('loc_1BA2')

    TalkEnd(0x0014)

    Return()

# id: 0x000C offset: 0x1BA6
@scena.Code('func_0C_1BA6')
def func_0C_1BA6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1C66',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1C05',
    )

    ChrTalk(
        0x00FE,
        (
            '本店现在正在\n',
            '举行诞辰庆典的降价酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要好好把握这个机会哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C63')

    def _loc_1C05(): pass

    label('loc_1C05')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店现在正在\n',
            '举行诞辰庆典的降价酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要好好把握这个机会哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C63(): pass

    label('loc_1C63')

    Jump('loc_1FF8')

    def _loc_1C66(): pass

    label('loc_1C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1CD4',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典当天的\n',
            '纪念减价销售正在计划中哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在的状况不容乐观，\n',
            '但还是得提前做好准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FF8')

    def _loc_1CD4(): pass

    label('loc_1CD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1CDE',
    )

    Jump('loc_1FF8')

    def _loc_1CDE(): pass

    label('loc_1CDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1CE8',
    )

    Jump('loc_1FF8')

    def _loc_1CE8(): pass

    label('loc_1CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1DDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1D40',
    )

    ChrTalk(
        0x00FE,
        (
            '本店的特点就是对商品进行比较和甄选，\n',
            '尽量为客人提供最优质的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD7')

    def _loc_1D40(): pass

    label('loc_1D40')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '柏斯超市里\n',
            '虽说什么类型的商店都有，\n',
            '不过那里充满活力而又秩序井然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '保持现状难以取胜，\n',
            '我们的百货店也要发展\n',
            '我们自己独特的经营的路线才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD7(): pass

    label('loc_1DD7')

    Jump('loc_1FF8')

    def _loc_1DDA(): pass

    label('loc_1DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1DE4',
    )

    Jump('loc_1FF8')

    def _loc_1DE4(): pass

    label('loc_1DE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1E76',
    )

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '就算本店在格兰赛尔一家独大，\n',
            '也难以在利贝尔王国成为顶尖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束之后，\n',
            '就和员工们一起去柏斯研修！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F44')

    def _loc_1E76(): pass

    label('loc_1E76')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '就算本店在格兰赛尔一家独大，\n',
            '也难以在利贝尔王国成为顶尖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……好的，决定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束之后，\n',
            '和员工们一起去柏斯研修！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要知己知彼才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然也要顺便购购物啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F44(): pass

    label('loc_1F44')

    Jump('loc_1FF8')

    def _loc_1F47(): pass

    label('loc_1F47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1F51',
    )

    Jump('loc_1FF8')

    def _loc_1F51(): pass

    label('loc_1F51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1FE7',
    )

    ChrTalk(
        0x00FE,
        (
            '好～的，鼓足干劲吧。\n',
            '目标是打倒柏斯超市哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在和丈夫一起旅行时，\n',
            '我对各地的商店进行了研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要把我的商店变得更加令人满意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FF8')

    def _loc_1FE7(): pass

    label('loc_1FE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1FF1',
    )

    Jump('loc_1FF8')

    def _loc_1FF1(): pass

    label('loc_1FF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1FF8',
    )

    def _loc_1FF8(): pass

    label('loc_1FF8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1FFC
@scena.Code('func_0D_1FFC')
def func_0D_1FFC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_2055',
    )

    ChrTalk(
        0x0012,
        (
            '#0280141632V#151F对了对了，明天我还要去大会取材呢，\n',
            '到时候请多关照啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D9')

    def _loc_2055(): pass

    label('loc_2055')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x0012,
        (
            '#0280141630V#151F啊，你们俩来了啊。\n',
            '比赛的照片拍得超棒呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280141631V已经预定要出版武术大会的特辑了，\n',
            '你们要好好期待哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20D9(): pass

    label('loc_20D9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x20DD
@scena.Code('func_0E_20DD')
def func_0E_20DD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_20EA',
    )

    Jump('loc_2354')

    def _loc_20EA(): pass

    label('loc_20EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_20F4',
    )

    Jump('loc_2354')

    def _loc_20F4(): pass

    label('loc_20F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_20FE',
    )

    Jump('loc_2354')

    def _loc_20FE(): pass

    label('loc_20FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2108',
    )

    Jump('loc_2354')

    def _loc_2108(): pass

    label('loc_2108')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2112',
    )

    Jump('loc_2354')

    def _loc_2112(): pass

    label('loc_2112')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2220',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2173',
    )

    ChrTalk(
        0x00FE,
        (
            '卢希娅这次要给\n',
            '那位高个子大叔加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过妈妈却支持\n',
            '戴红头盔的哥哥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_221D')

    def _loc_2173(): pass

    label('loc_2173')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '卢希娅这次要给\n',
            '那位高个子大叔加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过妈妈却支持\n',
            '戴红头盔的哥哥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F（……大叔，\n',
            '　是在说金先生吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F（他本人听见了一定会很难过的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_221D(): pass

    label('loc_221D')

    Jump('loc_2354')

    def _loc_2220(): pass

    label('loc_2220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_225A',
    )

    ChrTalk(
        0x00FE,
        (
            '比赛还没有开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢希娅相当期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2354')

    def _loc_225A(): pass

    label('loc_225A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_22A7',
    )

    ChrTalk(
        0x00FE,
        (
            '戴红头巾的哥哥们\n',
            '最后还是输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢希娅为他们加油了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2354')

    def _loc_22A7(): pass

    label('loc_22A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_22EA',
    )

    ChrTalk(
        0x00FE,
        (
            '卢希娅啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拼命支持那些\n',
            '绑着红头巾的哥哥们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2354')

    def _loc_22EA(): pass

    label('loc_22EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2328',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我要给我的朋友波利他们\n',
            '买些礼物带回去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2354')

    def _loc_2328(): pass

    label('loc_2328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2354',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '我是和妈妈一起来的哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2354(): pass

    label('loc_2354')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2358
@scena.Code('func_0F_2358')
def func_0F_2358():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2365',
    )

    Jump('loc_27E7')

    def _loc_2365(): pass

    label('loc_2365')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_236F',
    )

    Jump('loc_27E7')

    def _loc_236F(): pass

    label('loc_236F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2379',
    )

    Jump('loc_27E7')

    def _loc_2379(): pass

    label('loc_2379')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2383',
    )

    Jump('loc_27E7')

    def _loc_2383(): pass

    label('loc_2383')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_238D',
    )

    Jump('loc_27E7')

    def _loc_238D(): pass

    label('loc_238D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2425',
    )

    ChrTalk(
        0x00FE,
        (
            '在比赛中的双方选手\n',
            '使用各自经过严酷修行练就的本领\n',
            '过招的那一刻可谓是最棒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是那种\n',
            '厚积薄发的力量和信念\n',
            '互相碰撞所迸发出的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27E7')

    def _loc_2425(): pass

    label('loc_2425')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2481',
    )

    ChrTalk(
        0x00FE,
        (
            '我和女儿两人\n',
            '一直在期盼着武术大会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也打算从\n',
            '第一场开始就去观看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27E7')

    def _loc_2481(): pass

    label('loc_2481')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2556',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_24E4',
    )

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮那群孩子\n',
            '果然还是输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我看他们离场时\n',
            '似乎带着满足的神情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2553')

    def _loc_24E4(): pass

    label('loc_24E4')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮那群孩子\n',
            '果然还是输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，也许是我的错觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看他们离场时\n',
            '似乎带着满足的神情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2553(): pass

    label('loc_2553')

    Jump('loc_27E7')

    def _loc_2556(): pass

    label('loc_2556')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2630',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_25A8',
    )

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮不就是\n',
            '卢安的流氓团伙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最好别成为卢安的耻辱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_262D')

    def _loc_25A8(): pass

    label('loc_25A8')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '渡鸦帮不就是\n',
            '被市长利用的\n',
            '卢安的流氓团伙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们还要来参加武术大会，\n',
            '究竟是怎么想的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最好别成为\n',
            '卢安的耻辱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_262D(): pass

    label('loc_262D')

    Jump('loc_27E7')

    def _loc_2630(): pass

    label('loc_2630')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_27A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_26BD',
    )

    ChrTalk(
        0x00FE,
        (
            '卢安的孤儿院\n',
            '现在得到了捐款和赔偿金，\n',
            '正在重建之中了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们在我家开的旅店\n',
            '里面暂时借宿着，\n',
            '大家都非常开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_279F')

    def _loc_26BD(): pass

    label('loc_26BD')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '最近卢安地区还真是不得了。\n',
            '孤儿院被纵火，\n',
            '市长又被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '孤儿院现在得到了捐款和赔偿金，\n',
            '正在重建之中了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孩子们在我家开的旅店\n',
            '里面暂时借宿着，\n',
            '大家都非常开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望新的孤儿院\n',
            '能够早日完工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_279F(): pass

    label('loc_279F')

    Jump('loc_27E7')

    def _loc_27A2(): pass

    label('loc_27A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_27E7',
    )

    ChrTalk(
        0x00FE,
        (
            '我是从卢安地区的\n',
            '玛诺利亚村来的，\n',
            '和女儿一起来王都参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27E7(): pass

    label('loc_27E7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x27EB
@scena.Code('func_10_27EB')
def func_10_27EB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_27F8',
    )

    Jump('loc_2A3E')

    def _loc_27F8(): pass

    label('loc_27F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2802',
    )

    Jump('loc_2A3E')

    def _loc_2802(): pass

    label('loc_2802')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_280C',
    )

    Jump('loc_2A3E')

    def _loc_280C(): pass

    label('loc_280C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_286B',
    )

    ChrTalk(
        0x00FE,
        (
            '明天我要坐\n',
            '定期船回柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然想带点礼物\n',
            '回去送给哥哥，\n',
            '可买什么才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_286B(): pass

    label('loc_286B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_28B4',
    )

    ChrTalk(
        0x00FE,
        (
            '我打算下午去参观\n',
            '西街区的大圣堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是很令人期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_28B4(): pass

    label('loc_28B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_28DF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天该到哪里\n',
            '去参观一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_28DF(): pass

    label('loc_28DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_292E',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '哥哥还让我去买钓鱼用具呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会儿去钓公师团看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_292E(): pass

    label('loc_292E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2988',
    )

    ChrTalk(
        0x00FE,
        (
            '我、我是第一次\n',
            '观看武术大会呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常震撼啊，\n',
            '甚至让我都有些颤抖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_2988(): pass

    label('loc_2988')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_29CF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天做些什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得有武术大会，\n',
            '还是去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_29CF(): pass

    label('loc_29CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2A00',
    )

    ChrTalk(
        0x00FE,
        (
            '好久没来王都了，\n',
            '要好好快乐一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3E')

    def _loc_2A00(): pass

    label('loc_2A00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2A3E',
    )

    ChrTalk(
        0x00FE,
        (
            '为了到这里来买东西，\n',
            '我特地从柏斯乘坐定期船而来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A3E(): pass

    label('loc_2A3E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2A42
@scena.Code('func_11_2A42')
def func_11_2A42():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2B18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2AAE',
    )

    ChrTalk(
        0x00FE,
        (
            '我还是不认为\n',
            '杜南公爵是个坏人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他给别人带来很多麻烦\n',
            '倒是无可辩驳的事实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B15')

    def _loc_2AAE(): pass

    label('loc_2AAE')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '大家虽然说了很多\n',
            '杜南公爵的坏话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是不认为\n',
            '他是个坏人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会只有我这么想吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B15(): pass

    label('loc_2B15')

    Jump('loc_2E01')

    def _loc_2B18(): pass

    label('loc_2B18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2B70',
    )

    ChrTalk(
        0x00FE,
        (
            '街道上到处都是士兵，\n',
            '这绝对不是什么好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天最好还是\n',
            '早些回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2B70(): pass

    label('loc_2B70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2BC1',
    )

    ChrTalk(
        0x00FE,
        (
            '店里的人从刚才起\n',
            '就在神色慌张地讨论着什么……',
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

    Jump('loc_2E01')

    def _loc_2BC1(): pass

    label('loc_2BC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2BFF',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～……\n',
            '我偶尔想来看看\n',
            '给妻子买些什么礼物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2BFF(): pass

    label('loc_2BFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2C6B',
    )

    ChrTalk(
        0x00FE,
        (
            '一开始我觉得餐具之类的东西\n',
            '随便买什么样的都无所谓……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过好的东西\n',
            '始终还是好的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2C6B(): pass

    label('loc_2C6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2CDA',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，\n',
            '要等到什么时候\n',
            '才能抓到恐怖分子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然会有人袭击中央工房，\n',
            '真是万万没有想到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2CDA(): pass

    label('loc_2CDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2D2C',
    )

    ChrTalk(
        0x00FE,
        (
            '我对武术大会\n',
            '不太感兴趣呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '今天就和平常一样度过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2D97',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '今天好像没有什么新东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我原本以为今天\n',
            '会进些新的商品，\n',
            '所以一直都在这里等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2D97(): pass

    label('loc_2D97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2DB7',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～真麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2DB7(): pass

    label('loc_2DB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2DDB',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，这个也很不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E01')

    def _loc_2DDB(): pass

    label('loc_2DDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2E01',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '这个东西非常不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E01(): pass

    label('loc_2E01')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2E05
@scena.Code('func_12_2E05')
def func_12_2E05():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2E6C',
    )

    ChrTalk(
        0x00FE,
        (
            '今天中午\n',
            '做些什么菜好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是诞辰庆典期间，\n',
            '但并不是家庭主妇的休息日呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_2E6C(): pass

    label('loc_2E6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2EC9',
    )

    ChrTalk(
        0x00FE,
        (
            '今天街上到处都是黑衣士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给优雅的格兰赛尔大街\n',
            '带来了很多不和谐的杂色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_2EC9(): pass

    label('loc_2EC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2EFC',
    )

    ChrTalk(
        0x00FE,
        (
            '是我多心了吗，\n',
            '总觉得东西变少了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_2EFC(): pass

    label('loc_2EFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2F40',
    )

    ChrTalk(
        0x00FE,
        (
            '今天有限时降价销售哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不快点的话就抢不到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_2F40(): pass

    label('loc_2F40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2FA8',
    )

    ChrTalk(
        0x00FE,
        (
            '今天不去购物了，\n',
            '找个地方去吃饭吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，现在这个时候\n',
            '肯定哪个角落都有很多人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_2FA8(): pass

    label('loc_2FA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2FD9',
    )

    ChrTalk(
        0x00FE,
        (
            '那～么，\n',
            '今天做些什么菜比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_2FD9(): pass

    label('loc_2FD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3031',
    )

    ChrTalk(
        0x00FE,
        (
            '这样东西就买全了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不写个便条的话，\n',
            '有些东西\n',
            '肯定就会忘记买呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_3031(): pass

    label('loc_3031')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_305E',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '调和油好像已经用完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_305E(): pass

    label('loc_305E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_30FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_309A',
    )

    ChrTalk(
        0x00FE,
        (
            '顺便也去买一点\n',
            '和红茶搭配的点心吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30F9')

    def _loc_309A(): pass

    label('loc_309A')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '咖啡虽然不错，\n',
            '但我还是坚决拥护红茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里大概就是全利贝尔\n',
            '红茶品种最全的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30F9(): pass

    label('loc_30F9')

    Jump('loc_31CE')

    def _loc_30FC(): pass

    label('loc_30FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_315E',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会开始之后，\n',
            '大街就会变得拥挤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要事先\n',
            '尽量多买些东西储备着呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CE')

    def _loc_315E(): pass

    label('loc_315E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_31CE',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '今天拉文努村的特产进货了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '没有钱的时候却看到了想要的东西，\n',
            '这可怎么办好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31CE(): pass

    label('loc_31CE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x31D2
@scena.Code('func_13_31D2')
def func_13_31D2():
    Call(0, 0x0014)

    Return()

# id: 0x0014 offset: 0x31D7
@scena.Code('func_14_31D7')
def func_14_31D7():
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
        'loc_3235',
    )

    OP_0D()
    OP_A9(0x5E)
    OP_56(0x00)
    TalkEnd(0x0019)

    Return()

    def _loc_3235(): pass

    label('loc_3235')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3246',
    )

    TalkEnd(0x0019)

    Return()

    def _loc_3246(): pass

    label('loc_3246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_332B',
    )

    ChrTalk(
        0x0019,
        (
            '只是背地里说姐姐坏话\n',
            '果然还是没办法\n',
            '把红茶销售员的位置给抢过来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '从现在开始我要更加努力地\n',
            '学习与红茶相关的事项，\n',
            '这样迟早会打动店长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '到那时我就一脚把她踢下去，\n',
            '然后把红茶销售员的位置优雅地夺回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36A4')

    def _loc_332B(): pass

    label('loc_332B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3395',
    )

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '啊～想不出来有什么姐姐的坏话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '总、总之，\n',
            '红茶销售员还是我当最合适！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36A4')

    def _loc_3395(): pass

    label('loc_3395')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3554',
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_33BD'),
        (0x00000001, 'loc_33E5'),
        (0x00000002, 'loc_3415'),
        (0x00000003, 'loc_3441'),
        (0x00000004, 'loc_34BC'),
        (0x00000005, 'loc_34F0'),
        (-1, 'loc_3526'),
    )

    def _loc_33BD(): pass

    label('loc_33BD')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐她有脚气！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_33E5(): pass

    label('loc_33E5')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐她是个方向白痴呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_3415(): pass

    label('loc_3415')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '我姐姐很怕蟑螂的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_3441(): pass

    label('loc_3441')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '最近都不理我了。\n',
            '好寂寞哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '刚、刚才说的不算！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '总、总之她最近很冷漠！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_34BC(): pass

    label('loc_34BC')

    ChrTalk(
        0x0019,
        (
            '这～个，这～个，\n',
            '姐姐她喜欢吃甜食却长不胖！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_34F0(): pass

    label('loc_34F0')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐有低血压，早晨很衰弱哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3526')

    def _loc_3526(): pass

    label('loc_3526')

    ChrTalk(
        0x0019,
        (
            '所、所以呢，\n',
            '她不适合做红茶销售员哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36A4')

    def _loc_3554(): pass

    label('loc_3554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_36A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_35D7',
    )

    ChrTalk(
        0x0019,
        (
            '她啊，利用姐姐的特权，\n',
            '把红茶销售员的岗位从我手里抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我一定要赶上她，\n',
            '并把红茶销售员的岗位夺回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36A4')

    def _loc_35D7(): pass

    label('loc_35D7')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x0019,
        (
            '那边的红茶销售员\n',
            '基蒂是我的双胞胎姐姐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '红茶销售员是\n',
            '这里最受欢迎的岗位呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '她啊，利用姐姐的特权，\n',
            '把红茶销售员的岗位从我手里抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '我一定要赶上她，\n',
            '并把红茶销售员的岗位夺回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36A4(): pass

    label('loc_36A4')

    TalkEnd(0x0019)

    Return()

# id: 0x0015 offset: 0x36A8
@scena.Code('func_15_36A8')
def func_15_36A8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_371C',
    )

    ChrTalk(
        0x00FE,
        (
            '这次是不是委托\n',
            '丹顿先生去进一些\n',
            '共和国制作的茶壶来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这种茶壶\n',
            '在女性之间非常流行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C0')

    def _loc_371C(): pass

    label('loc_371C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_37D1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3777',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然我也喜欢柠檬茶，\n',
            '不过最推荐的还是要数\n',
            '北安布里亚产的诺尔基露茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37CE')

    def _loc_3777(): pass

    label('loc_3777')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您喜欢奶茶的话，\n',
            '尝尝这个共和国产的\n',
            '卡尔瓦德混合咖啡如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37CE(): pass

    label('loc_37CE')

    Jump('loc_42C0')

    def _loc_37D1(): pass

    label('loc_37D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3910',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3846',
    )

    ChrTalk(
        0x00FE,
        (
            '那位艾莉茜雅女王陛下\n',
            '也是一位喜欢红茶的人哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下竟然也喜欢红茶，\n',
            '我觉得相当自豪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_390D')

    def _loc_3846(): pass

    label('loc_3846')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这是利贝尔红茶爱好者之间\n',
            '相当有名的一件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那位艾莉茜雅女王陛下\n',
            '也是一位喜欢红茶的人哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王城里面的人\n',
            '时常会来我们店购买茶叶的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下竟然也喜欢红茶，\n',
            '我觉得相当自豪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_390D(): pass

    label('loc_390D')

    Jump('loc_42C0')

    def _loc_3910(): pass

    label('loc_3910')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3A7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3977',
    )

    ChrTalk(
        0x00FE,
        (
            '一定要把\n',
            '最后一滴茶水注入茶杯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要喝到香浓的红茶，\n',
            '这件事就绝对不能忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A7C')

    def _loc_3977(): pass

    label('loc_3977')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '基蒂姐姐的\n',
            '制作香浓红茶\n',
            '黄金准则之六！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要把\n',
            '最后一滴茶水注入茶杯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一滴是最精华的一滴，\n',
            '被人们称为黄金水滴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且倒茶的时候\n',
            '要一边摇匀，\n',
            '一边慢慢地倒茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以上就是本店\n',
            '推荐的香浓红茶\n',
            '黄金六大准则。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么样，很有参考价值吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A7C(): pass

    label('loc_3A7C')

    Jump('loc_42C0')

    def _loc_3A7F(): pass

    label('loc_3A7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3BF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3ADB',
    )

    ChrTalk(
        0x00FE,
        (
            '茶叶一定要泡足时间！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要喝到香浓的红茶，\n',
            '这件事就绝对不能忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BF0')

    def _loc_3ADB(): pass

    label('loc_3ADB')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '基蒂姐姐的\n',
            '制作香浓红茶\n',
            '黄金准则之五！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '茶叶一定要泡足时间！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '红茶刚泡的时候会有点苦味，\n',
            '但之后味道会慢慢变香浓的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以呢，在品尝之前，\n',
            '耐心的等待也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过泡得太久的话，\n',
            '红茶味道会变涩的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '长的茶叶就多泡会儿，\n',
            '短的茶叶就少泡会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BF0(): pass

    label('loc_3BF0')

    Jump('loc_42C0')

    def _loc_3BF3(): pass

    label('loc_3BF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3D59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3C4F',
    )

    ChrTalk(
        0x00FE,
        (
            '正确掌握茶叶的分量！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要喝到香浓的红茶，\n',
            '这件事就绝对不能忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D56')

    def _loc_3C4F(): pass

    label('loc_3C4F')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '基蒂姐姐的\n',
            '制作香浓红茶\n',
            '黄金准则之四！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正确掌握茶叶的分量！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据茶叶的不同会有些许差异，\n',
            '但大体上是按照每一茶杯\n',
            '放一匙茶叶的比例哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '茶叶太多会很苦，\n',
            '放得太少了\n',
            '味道就会不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是短时间放很多茶叶，\n',
            '这种做法泡出来的茶\n',
            '会只剩下苦味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D56(): pass

    label('loc_3D56')

    Jump('loc_42C0')

    def _loc_3D59(): pass

    label('loc_3D59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3EEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3DBA',
    )

    ChrTalk(
        0x00FE,
        (
            '请一定要将\n',
            '茶壶预先加热！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要喝到香浓的红茶，\n',
            '这件事就绝对不能忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EE7')

    def _loc_3DBA(): pass

    label('loc_3DBA')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '基蒂姐姐的\n',
            '制作香浓红茶\n',
            '黄金准则之三！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请一定要将\n',
            '茶壶预先加热！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '倒入热水时，\n',
            '茶叶上下翻滚的现象\n',
            '称为『跳跃』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要泡出香浓的好茶，\n',
            '这是绝对必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，茶壶冷却的话\n',
            '热水也会随之冷却，\n',
            '这样就难以出现跳跃现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '另外，\n',
            '据说将茶壶做成圆形\n',
            '也是为了容易引起跳跃现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EE7(): pass

    label('loc_3EE7')

    Jump('loc_42C0')

    def _loc_3EEA(): pass

    label('loc_3EEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4047',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3F82',
    )

    ChrTalk(
        0x00FE,
        (
            '一定要用纯净的、\n',
            '沸腾的开水冲泡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要喝到香浓的红茶，\n',
            '这件事就绝对不能忘记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺便说一句，\n',
            '沸腾很久的水也不适合泡茶哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4044')

    def _loc_3F82(): pass

    label('loc_3F82')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '基蒂姐姐的\n',
            '制作香浓红茶\n',
            '黄金准则之二！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要用纯净的、\n',
            '沸腾的开水冲泡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要让香浓的成分得以释放，\n',
            '水中必须要溶入\n',
            '充足的空气才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为此，\n',
            '要先把水煮沸，\n',
            '然后再注入茶壶中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4044(): pass

    label('loc_4044')

    Jump('loc_42C0')

    def _loc_4047(): pass

    label('loc_4047')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4171',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_408B',
    )

    ChrTalk(
        0x00FE,
        (
            '首先要采用新鲜优良的茶叶，\n',
            '这是基本中的基本。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_416E')

    def _loc_408B(): pass

    label('loc_408B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '基蒂姐姐的\n',
            '制作香浓红茶\n',
            '黄金准则之一！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先要采用优良的茶叶，\n',
            '这是所有一切的先决条件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说只要红茶没有发霉，\n',
            '或是气味没有变怪，\n',
            '也还是可以泡来喝的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过为了保证味道的香浓，\n',
            '采用新鲜的茶叶才是根本哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_416E(): pass

    label('loc_416E')

    Jump('loc_42C0')

    def _loc_4171(): pass

    label('loc_4171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_41F6',
    )

    ChrTalk(
        0x00FE,
        (
            '客人，\n',
            '您知道泡制香浓红茶的黄金准则吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '泡茶的准则\n',
            '根据地域的不同内容也不尽相同，\n',
            '本店有六条准则可以推荐给您哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C0')

    def _loc_41F6(): pass

    label('loc_41F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_42C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4259',
    )

    ChrTalk(
        0x00FE,
        (
            '推荐您品尝\n',
            '我们这里的红茶～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也可以指导您如何泡茶哦，\n',
            '客人请试一试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C0')

    def _loc_4259(): pass

    label('loc_4259')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '推荐您品尝\n',
            '我们这里的红茶～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也可以指导您如何泡茶哦，\n',
            '客人请试一试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42C0(): pass

    label('loc_42C0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x42C4
@scena.Code('func_16_42C4')
def func_16_42C4():
    Call(0, 0x0017)

    Return()

# id: 0x0017 offset: 0x42C9
@scena.Code('func_17_42C9')
def func_17_42C9():
    TalkBegin(0x000B)
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
        'loc_4327',
    )

    OP_0D()
    OP_A9(0x5D)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_4327(): pass

    label('loc_4327')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4338',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_4338(): pass

    label('loc_4338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4407',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_439A',
    )

    ChrTalk(
        0x000B,
        (
            '不管怎么说，女王陛下平安无事，\n',
            '诞辰庆典也顺利举行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这不就挺好的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4404')

    def _loc_439A(): pass

    label('loc_439A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '哎呀，可喜可贺！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不管怎么说，女王陛下平安无事，\n',
            '诞辰庆典也顺利举行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这不就挺好的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4404(): pass

    label('loc_4404')

    Jump('loc_4AEE')

    def _loc_4407(): pass

    label('loc_4407')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_44DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4474',
    )

    ChrTalk(
        0x000B,
        (
            '亲卫队如果就这么逃走了，\n',
            '我的困惑就烟消云散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那位尤莉亚中尉\n',
            '不可能是恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44D8')

    def _loc_4474(): pass

    label('loc_4474')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '如果亲卫队\n',
            '就这么逃走了的话，\n',
            '我的困惑就烟消云散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '尤莉亚中尉他们\n',
            '肯定不是恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44D8(): pass

    label('loc_44D8')

    Jump('loc_4AEE')

    def _loc_44DB(): pass

    label('loc_44DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_45AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_453C',
    )

    ChrTalk(
        0x000B,
        (
            '军队将空港\n',
            '完全封锁起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '怎么回事啊……\n',
            '这样的话不是没法进货了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45AB')

    def _loc_453C(): pass

    label('loc_453C')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '军队将空港\n',
            '完全封锁起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '怎么回事啊……\n',
            '这样的话不是没法进货了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '可恶，看他们干的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45AB(): pass

    label('loc_45AB')

    Jump('loc_4AEE')

    def _loc_45AE(): pass

    label('loc_45AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_461E',
    )

    ChrTalk(
        0x000B,
        (
            '武术大会好像决出优胜者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '被邀请到王城晚宴的人\n',
            '为了要迎合公爵的脸面，\n',
            '也会穿得体面一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AEE')

    def _loc_461E(): pass

    label('loc_461E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_474E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_46A2',
    )

    ChrTalk(
        0x000B,
        (
            '话说回来，\n',
            '最近柏斯、卢安还有蔡斯\n',
            '都相继发生了一些大案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '什么事情也没有发生的\n',
            '就只剩下王都和洛连特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_474B')

    def _loc_46A2(): pass

    label('loc_46A2')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '话说回来，\n',
            '最近柏斯、卢安还有蔡斯\n',
            '都相继发生了一些大案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '什么事情也没有发生的\n',
            '就只剩下王都和洛连特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '希望就这样安然无恙地\n',
            '什么事情都不发生就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_474B(): pass

    label('loc_474B')

    Jump('loc_4AEE')

    def _loc_474E(): pass

    label('loc_474E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4879',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_47CF',
    )

    ChrTalk(
        0x000B,
        (
            '店长说，\n',
            '诞辰庆典结束之后\n',
            '要带我们去柏斯超市研修。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我们的店长\n',
            '常常提出一些意见，\n',
            '就是因为做了对比吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4876')

    def _loc_47CF(): pass

    label('loc_47CF')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '店长说，\n',
            '诞辰庆典结束之后\n',
            '要带我们去柏斯超市研修。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '其实我也想去\n',
            '那个传说中的柏斯超市\n',
            '参观取经呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我们的店长\n',
            '常常提出一些意见，\n',
            '就是因为做了对比吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4876(): pass

    label('loc_4876')

    Jump('loc_4AEE')

    def _loc_4879(): pass

    label('loc_4879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4987',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_48E2',
    )

    ChrTalk(
        0x000B,
        (
            '最近卢安\n',
            '准备进行市长选举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '长年以来治理那个地区的\n',
            '戴尔蒙家族也终于垮台了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4984')

    def _loc_48E2(): pass

    label('loc_48E2')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '对了，\n',
            '我在《利贝尔通讯》上看到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '最近卢安\n',
            '准备进行市长选举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '长年以来治理那个地区的\n',
            '戴尔蒙家族也终于垮台了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '唉，这也是理所当然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4984(): pass

    label('loc_4984')

    Jump('loc_4AEE')

    def _loc_4987(): pass

    label('loc_4987')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_49F9',
    )

    ChrTalk(
        0x000B,
        (
            '因为卢安市长被捕，\n',
            '现在那儿的情况变得很混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这段时间水产品完全进不了货，\n',
            '实在是让人困扰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AEE')

    def _loc_49F9(): pass

    label('loc_49F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4A5B',
    )

    ChrTalk(
        0x000B,
        (
            '店长前一阵子外出旅行，\n',
            '现在已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '店长在的时候\n',
            '店里的气氛果然会很紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AEE')

    def _loc_4A5B(): pass

    label('loc_4A5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4AC6',
    )

    ChrTalk(
        0x000B,
        (
            '欢迎光临，\n',
            '这里是专卖实用性装饰品\n',
            '和餐具的柜台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果有看中的东西，\n',
            '跟我说一声就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AEE')

    def _loc_4AC6(): pass

    label('loc_4AC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4AEE',
    )

    ChrTalk(
        0x000B,
        (
            '欢迎光临。\n',
            '是来买礼品的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AEE(): pass

    label('loc_4AEE')

    TalkEnd(0x000B)

    Return()

# id: 0x0018 offset: 0x4AF2
@scena.Code('func_18_4AF2')
def func_18_4AF2():
    Call(0, 0x0019)

    Return()

# id: 0x0019 offset: 0x4AF7
@scena.Code('func_19_4AF7')
def func_19_4AF7():
    TalkBegin(0x000A)
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
        'loc_4B6D',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4B59',
    )

    OP_A9(0x69)

    Jump('loc_4B67')

    def _loc_4B59(): pass

    label('loc_4B59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4B65',
    )

    OP_A9(0x68)

    Jump('loc_4B67')

    def _loc_4B65(): pass

    label('loc_4B65')

    OP_A9(0x5C)

    def _loc_4B67(): pass

    label('loc_4B67')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_4B6D(): pass

    label('loc_4B6D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B7E',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_4B7E(): pass

    label('loc_4B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4BEF',
    )

    ChrTalk(
        0x000A,
        (
            '第一时间报道政变的\n',
            '《利贝尔通讯》特刊\n',
            '可以说是疯狂热卖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '刚刚进货不久，\n',
            '一下子就又卖光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4BEF(): pass

    label('loc_4BEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4C4C',
    )

    ChrTalk(
        0x000A,
        (
            '最近，\n',
            '那些士兵频繁地来问话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他们好像在\n',
            '拼尽全力寻找\n',
            '亲卫队队长的下落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4C4C(): pass

    label('loc_4C4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4CBE',
    )

    ChrTalk(
        0x000A,
        (
            '买一本《利贝尔通讯》的\n',
            '武术大会特辑临时增刊怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '无论是观众还是选手，\n',
            '都一定要留个纪念哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4CBE(): pass

    label('loc_4CBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4D0C',
    )

    ChrTalk(
        0x000A,
        (
            '啊～\n',
            '怎么会这么忙呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '武术大会的结果\n',
            '究竟是什么样的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4D0C(): pass

    label('loc_4D0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4D41',
    )

    ChrTalk(
        0x000A,
        (
            '今天天气很不错，\n',
            '店里的饮料也很畅销。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4D41(): pass

    label('loc_4D41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4D8C',
    )

    ChrTalk(
        0x000A,
        (
            '武术大会一开始，\n',
            '人果然就多起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '店长也喜出望外呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4D8C(): pass

    label('loc_4D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4E06',
    )

    ChrTalk(
        0x000A,
        (
            '因为女王殿下身体欠佳的缘故，\n',
            '不知道是否还会举行诞辰庆典呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过即使如此，\n',
            '还是来了很多观光的客人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4E06(): pass

    label('loc_4E06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4E5E',
    )

    ChrTalk(
        0x000A,
        (
            '这里有卖既可以当旅行纪念\n',
            '又具有实用性的格兰赛尔观光地图，\n',
            '来一份怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5069')

    def _loc_4E5E(): pass

    label('loc_4E5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4F6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4EE0',
    )

    ChrTalk(
        0x000A,
        (
            '最近的《利贝尔通讯》\n',
            '都是些无关紧要的新闻，\n',
            '一点都不让人振奋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过上面的照片\n',
            '还是一如既往地漂亮呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F6C')

    def _loc_4EE0(): pass

    label('loc_4EE0')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '最近的《利贝尔通讯》\n',
            '都是些无关紧要的新闻，\n',
            '一点都不让人振奋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '为何会变成这样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过上面的照片\n',
            '还是一如既往地漂亮呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F6C(): pass

    label('loc_4F6C')

    Jump('loc_5069')

    def _loc_4F6F(): pass

    label('loc_4F6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_503D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4FAB',
    )

    ChrTalk(
        0x000A,
        (
            '我们百货店\n',
            '从礼品到日用品都一应俱全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_503A')

    def _loc_4FAB(): pass

    label('loc_4FAB')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '我们百货店\n',
            '从礼品到日用品都一应俱全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然在规模方面\n',
            '的确不及柏斯超市……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过这里也有\n',
            '相当多的优良商品，\n',
            '不会比他们差的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_503A(): pass

    label('loc_503A')

    Jump('loc_5069')

    def _loc_503D(): pass

    label('loc_503D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5069',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎光临！\n',
            '这里是艾德尔百货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5069(): pass

    label('loc_5069')

    TalkEnd(0x000A)

    Return()

# id: 0x001A offset: 0x506D
@scena.Code('func_1A_506D')
def func_1A_506D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_50F3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320140754V#835F我一般是不会\n',
            '到这种地方来购物的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320140755V可是雪拉扎德和亚妮拉丝\n',
            '不管怎么说都要把我给拉来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5154')

    def _loc_50F3(): pass

    label('loc_50F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_50FD',
    )

    Jump('loc_5154')

    def _loc_50FD(): pass

    label('loc_50FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5107',
    )

    Jump('loc_5154')

    def _loc_5107(): pass

    label('loc_5107')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5111',
    )

    Jump('loc_5154')

    def _loc_5111(): pass

    label('loc_5111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_511B',
    )

    Jump('loc_5154')

    def _loc_511B(): pass

    label('loc_511B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5125',
    )

    Jump('loc_5154')

    def _loc_5125(): pass

    label('loc_5125')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_512F',
    )

    Jump('loc_5154')

    def _loc_512F(): pass

    label('loc_512F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5139',
    )

    Jump('loc_5154')

    def _loc_5139(): pass

    label('loc_5139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5143',
    )

    Jump('loc_5154')

    def _loc_5143(): pass

    label('loc_5143')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_514D',
    )

    Jump('loc_5154')

    def _loc_514D(): pass

    label('loc_514D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5154',
    )

    def _loc_5154(): pass

    label('loc_5154')

    TalkEnd(0x0009)

    Return()

# id: 0x001B offset: 0x5158
@scena.Code('func_1B_5158')
def func_1B_5158():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_53D2',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 9240, 0, 5790, 90)
    ChrSetPos(0x0102, 9180, 0, 4760, 90)
    ChrSetPos(0x0108, 8280, 0, 5410, 90)
    ChrTurnDirection(0x0008, 0x0108, 0)
    ChrSetSubChip(0x0008, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 4, 0x64C))
    OP_28(0x004B, 0x01, 0x0040)

    If(
        (
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0020)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0040)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_51DF',
    )

    OP_28(0x004B, 0x01, 0x0100)

    def _loc_51DF(): pass

    label('loc_51DF')

    CameraMove(10020, 0, 5390, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0120130129V#850F啊呀，这不是\n',
            '两位游击士新人和金大哥吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130130V这么快就从城里回来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130131V#505F嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130132V#012F亚妮拉丝小姐。\n',
            '占用你一点时间好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120130133V#811F什么事，什么事？\n',
            '有什么好玩儿的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130134V#007F唔～～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130135V好玩儿倒是不至于，\n',
            '不过你听了肯定会吓一跳呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120130136V#810F咦……\n',
            '好像不太好玩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120130137V#850F在这儿站着不好说话，\n',
            '我们到外面的休息处去如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_589D')

    def _loc_53D2(): pass

    label('loc_53D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_570F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5444',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120140769V#810F之前第一次\n',
            '和你们一起执行任务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120140760V你们俩配合得\n',
            '还真是默契呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_570C')

    def _loc_5444(): pass

    label('loc_5444')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0101,
        (
            '#0010140756V#001F亚妮拉丝前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120140757V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140758V#008F怎么了啊？\n',
            '目不转睛地盯着我的脸看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120140759V#810F没什么，\n',
            '之前第一次和你们一起执行任务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120140760V你们俩配合得\n',
            '还真是默契呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140761V#505F大概是因为我们一直都在一起，\n',
            '彼此很熟悉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_570C',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120140762V#818F是这样没错啦，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '亚妮拉丝在艾丝蒂尔的耳边\n',
            '说了几句悄悄话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x00FE,
        (
            '#0120140763V#816F（嘻嘻，以我个人的看法，\n',
            '　你们俩会成为恩爱的一对哦㈱）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140764V#008F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120140765V#811F（别害羞别害羞！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120140766V#851F（啊～连我也很向往能有约修亚那样\n',
            '　俊俏的男孩做自己的男朋友呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140767V#503F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140768V#014F？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_570C(): pass

    label('loc_570C')

    Jump('loc_589D')

    def _loc_570F(): pass

    label('loc_570F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5719',
    )

    Jump('loc_589D')

    def _loc_5719(): pass

    label('loc_5719')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5723',
    )

    Jump('loc_589D')

    def _loc_5723(): pass

    label('loc_5723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_57BF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120111967V#818F唔～挑哪个好呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111968V#851F每个都很可爱呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111969V#811F难得来到繁华的王都，\n',
            '要抓紧时间享受购物的乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_589D')

    def _loc_57BF(): pass

    label('loc_57BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_57C9',
    )

    Jump('loc_589D')

    def _loc_57C9(): pass

    label('loc_57C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_586E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120111970V#810F啊，两位新人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111971V#856F今天好可惜呢。\n',
            '虽然我们已经竭尽全力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120111972V#816F真有点不服气，\n',
            '下次我们要再比试一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_589D')

    def _loc_586E(): pass

    label('loc_586E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5878',
    )

    Jump('loc_589D')

    def _loc_5878(): pass

    label('loc_5878')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5882',
    )

    Jump('loc_589D')

    def _loc_5882(): pass

    label('loc_5882')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_588C',
    )

    Jump('loc_589D')

    def _loc_588C(): pass

    label('loc_588C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5896',
    )

    Jump('loc_589D')

    def _loc_5896(): pass

    label('loc_5896')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_589D',
    )

    def _loc_589D(): pass

    label('loc_589D')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
