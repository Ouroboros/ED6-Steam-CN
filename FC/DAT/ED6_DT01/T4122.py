import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4122_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4122   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚妮拉丝'),
    TXT(0x02, '卡露娜'),
    TXT(0x03, '莉莉'),
    TXT(0x04, '丹顿'),
    TXT(0x05, '基蒂'),
    TXT(0x06, '希娜'),
    TXT(0x07, '特雷诺'),
    TXT(0x08, '索菲娜'),
    TXT(0x09, '卡拉'),
    TXT(0x0A, '卢希娅'),
    TXT(0x0B, '朵洛希'),
    TXT(0x0C, '艾德尔店长'),
    TXT(0x0D, '菲尔妲'),
    TXT(0x0E, '莎夏'),
    TXT(0x0F, '鲁特尔'),
    TXT(0x10, '雪拉扎德'),
    TXT(0x11, '管家菲利普'),
    TXT(0x12, '蜜蒂'),
    TXT(0x13, ''),
]

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

# id: 0xFFFF offset: 0x57A8
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

# id: 0x10002 offset: 0x132
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
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

# id: 0x10003 offset: 0x372
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x372
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x372
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
@scena.Code('PreInit')
def PreInit():
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

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 10500, 0, 5390, 90)

    def _loc_448(): pass

    label('loc_448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 8850, 0, -10160, 259)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 4100, 0, -10830, 100)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x000E, 2470, 0, -3790, 78)

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

    SetChrPos(0x000D, -11310, 0, 6390, 355)
    SetChrPos(0x000E, 13600, 0, -11620, 107)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)

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

    SetChrPos(0x000D, -13220, 0, 9430, 198)
    SetChrPos(0x000E, 13600, 0, -7380, 82)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

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

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 2890, 0, 3290, 87)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x000D, -8740, 0, 9410, 165)
    SetChrPos(0x000E, 5870, 0, -10820, 272)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)

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

    SetChrPos(0x000D, -10560, 0, 9490, 200)
    SetChrPos(0x000E, 4480, 0, -6130, 340)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)

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

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 5000, 0, 1510, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x000D, -8890, 0, 6200, 349)
    SetChrPos(0x000E, 13580, 0, -11020, 70)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

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

    SetChrPos(0x000D, -7480, 0, 4300, 104)
    SetChrPos(0x000E, 4480, 0, -6130, 340)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0013, 0x0080)

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

    SetChrPos(0x000D, -7480, 0, 4300, 104)
    ClearChrFlags(0x000F, 0x0080)

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

    SetChrPos(0x000D, -12210, 250, 11380, 355)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0013, 0x0080)

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

    SetChrPos(0x000D, -11310, 0, 6390, 355)
    SetChrPos(0x000E, 13580, 0, -11020, 70)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0016, 0x0080)

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

    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0016, 0x0080)

    def _loc_6CD(): pass

    label('loc_6CD')

    Return()

# id: 0x0001 offset: 0x6CE
@scena.Code('Init')
def Init():
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
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_73C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

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
        'loc_802',
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

    Jump('loc_A5C')

    def _loc_802(): pass

    label('loc_802')

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

    def _loc_A5C(): pass

    label('loc_A5C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xA60
@scena.Code('func_06_A60')
def func_06_A60():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_AFF',
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

    Jump('loc_D00')

    def _loc_AFF(): pass

    label('loc_AFF')

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

    def _loc_D00(): pass

    label('loc_D00')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xD04
@scena.Code('func_07_D04')
def func_07_D04():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D11',
    )

    Jump('loc_E28')

    def _loc_D11(): pass

    label('loc_D11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_D1B',
    )

    Jump('loc_E28')

    def _loc_D1B(): pass

    label('loc_D1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_D25',
    )

    Jump('loc_E28')

    def _loc_D25(): pass

    label('loc_D25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_D2F',
    )

    Jump('loc_E28')

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_D39',
    )

    Jump('loc_E28')

    def _loc_D39(): pass

    label('loc_D39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_D43',
    )

    Jump('loc_E28')

    def _loc_D43(): pass

    label('loc_D43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_D4D',
    )

    Jump('loc_E28')

    def _loc_D4D(): pass

    label('loc_D4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_D57',
    )

    Jump('loc_E28')

    def _loc_D57(): pass

    label('loc_D57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_D61',
    )

    Jump('loc_E28')

    def _loc_D61(): pass

    label('loc_D61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_DCB',
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

    Jump('loc_E28')

    def _loc_DCB(): pass

    label('loc_DCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_E28',
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

    def _loc_E28(): pass

    label('loc_E28')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xE2C
@scena.Code('func_08_E2C')
def func_08_E2C():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0xE31
@scena.Code('func_09_E31')
def func_09_E31():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_E74',
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

    Jump('loc_12B7')

    def _loc_E74(): pass

    label('loc_E74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_EC3',
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

    Jump('loc_12B7')

    def _loc_EC3(): pass

    label('loc_EC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_F17',
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

    Jump('loc_12B7')

    def _loc_F17(): pass

    label('loc_F17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_F4E',
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

    Jump('loc_12B7')

    def _loc_F4E(): pass

    label('loc_F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_FB7',
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

    Jump('loc_12B7')

    def _loc_FB7(): pass

    label('loc_FB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_10FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_103F',
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

    Jump('loc_10F9')

    def _loc_103F(): pass

    label('loc_103F')

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

    def _loc_10F9(): pass

    label('loc_10F9')

    Jump('loc_12B7')

    def _loc_10FC(): pass

    label('loc_10FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1177',
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

    Jump('loc_12B7')

    def _loc_1177(): pass

    label('loc_1177')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_11BB',
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

    Jump('loc_12B7')

    def _loc_11BB(): pass

    label('loc_11BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_11FF',
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

    Jump('loc_12B7')

    def _loc_11FF(): pass

    label('loc_11FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1292',
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

    Jump('loc_12B7')

    def _loc_1292(): pass

    label('loc_1292')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_12B7',
    )

    ChrTalk(
        0x0015,
        (
            '欢迎来到利贝尔飞艇公社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12B7(): pass

    label('loc_12B7')

    TalkEnd(0x0015)

    Return()

# id: 0x000A offset: 0x12BB
@scena.Code('func_0A_12BB')
def func_0A_12BB():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x12C0
@scena.Code('func_0B_12C0')
def func_0B_12C0():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_13E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1342',
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

    Jump('loc_13E4')

    def _loc_1342(): pass

    label('loc_1342')

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

    def _loc_13E4(): pass

    label('loc_13E4')

    Jump('loc_1B20')

    def _loc_13E7(): pass

    label('loc_13E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1479',
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

    Jump('loc_1B20')

    def _loc_1479(): pass

    label('loc_1479')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_14EB',
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

    Jump('loc_1B20')

    def _loc_14EB(): pass

    label('loc_14EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1566',
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

    Jump('loc_1B20')

    def _loc_1566(): pass

    label('loc_1566')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_15E5',
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

    Jump('loc_1B20')

    def _loc_15E5(): pass

    label('loc_15E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1727',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_167A',
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

    Jump('loc_1724')

    def _loc_167A(): pass

    label('loc_167A')

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

    def _loc_1724(): pass

    label('loc_1724')

    Jump('loc_1B20')

    def _loc_1727(): pass

    label('loc_1727')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1839',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_17A0',
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

    Jump('loc_1836')

    def _loc_17A0(): pass

    label('loc_17A0')

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

    def _loc_1836(): pass

    label('loc_1836')

    Jump('loc_1B20')

    def _loc_1839(): pass

    label('loc_1839')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_18BA',
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

    Jump('loc_1B20')

    def _loc_18BA(): pass

    label('loc_18BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1963',
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

    Jump('loc_1B20')

    def _loc_1963(): pass

    label('loc_1963')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1A01',
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

    Jump('loc_1B20')

    def _loc_1A01(): pass

    label('loc_1A01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1B20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1A7C',
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

    Jump('loc_1B20')

    def _loc_1A7C(): pass

    label('loc_1A7C')

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

    def _loc_1B20(): pass

    label('loc_1B20')

    TalkEnd(0x0014)

    Return()

# id: 0x000C offset: 0x1B24
@scena.Code('func_0C_1B24')
def func_0C_1B24():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1BE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1B83',
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

    Jump('loc_1BE1')

    def _loc_1B83(): pass

    label('loc_1B83')

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

    def _loc_1BE1(): pass

    label('loc_1BE1')

    Jump('loc_1F76')

    def _loc_1BE4(): pass

    label('loc_1BE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1C52',
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

    Jump('loc_1F76')

    def _loc_1C52(): pass

    label('loc_1C52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1C5C',
    )

    Jump('loc_1F76')

    def _loc_1C5C(): pass

    label('loc_1C5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1C66',
    )

    Jump('loc_1F76')

    def _loc_1C66(): pass

    label('loc_1C66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1D58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1CBE',
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

    Jump('loc_1D55')

    def _loc_1CBE(): pass

    label('loc_1CBE')

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

    def _loc_1D55(): pass

    label('loc_1D55')

    Jump('loc_1F76')

    def _loc_1D58(): pass

    label('loc_1D58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1D62',
    )

    Jump('loc_1F76')

    def _loc_1D62(): pass

    label('loc_1D62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1EC5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_1DF4',
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

    Jump('loc_1EC2')

    def _loc_1DF4(): pass

    label('loc_1DF4')

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

    def _loc_1EC2(): pass

    label('loc_1EC2')

    Jump('loc_1F76')

    def _loc_1EC5(): pass

    label('loc_1EC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1ECF',
    )

    Jump('loc_1F76')

    def _loc_1ECF(): pass

    label('loc_1ECF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1F65',
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

    Jump('loc_1F76')

    def _loc_1F65(): pass

    label('loc_1F65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1F6F',
    )

    Jump('loc_1F76')

    def _loc_1F6F(): pass

    label('loc_1F6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1F76',
    )

    def _loc_1F76(): pass

    label('loc_1F76')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1F7A
@scena.Code('func_0D_1F7A')
def func_0D_1F7A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1FCE',
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

    Jump('loc_2048')

    def _loc_1FCE(): pass

    label('loc_1FCE')

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

    def _loc_2048(): pass

    label('loc_2048')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x204C
@scena.Code('func_0E_204C')
def func_0E_204C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2059',
    )

    Jump('loc_22C3')

    def _loc_2059(): pass

    label('loc_2059')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2063',
    )

    Jump('loc_22C3')

    def _loc_2063(): pass

    label('loc_2063')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_206D',
    )

    Jump('loc_22C3')

    def _loc_206D(): pass

    label('loc_206D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2077',
    )

    Jump('loc_22C3')

    def _loc_2077(): pass

    label('loc_2077')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2081',
    )

    Jump('loc_22C3')

    def _loc_2081(): pass

    label('loc_2081')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_218F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_20E2',
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

    Jump('loc_218C')

    def _loc_20E2(): pass

    label('loc_20E2')

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

    def _loc_218C(): pass

    label('loc_218C')

    Jump('loc_22C3')

    def _loc_218F(): pass

    label('loc_218F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_21C9',
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

    Jump('loc_22C3')

    def _loc_21C9(): pass

    label('loc_21C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2216',
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

    Jump('loc_22C3')

    def _loc_2216(): pass

    label('loc_2216')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2259',
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

    Jump('loc_22C3')

    def _loc_2259(): pass

    label('loc_2259')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2297',
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

    Jump('loc_22C3')

    def _loc_2297(): pass

    label('loc_2297')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_22C3',
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

    def _loc_22C3(): pass

    label('loc_22C3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x22C7
@scena.Code('func_0F_22C7')
def func_0F_22C7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_22D4',
    )

    Jump('loc_2756')

    def _loc_22D4(): pass

    label('loc_22D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_22DE',
    )

    Jump('loc_2756')

    def _loc_22DE(): pass

    label('loc_22DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_22E8',
    )

    Jump('loc_2756')

    def _loc_22E8(): pass

    label('loc_22E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_22F2',
    )

    Jump('loc_2756')

    def _loc_22F2(): pass

    label('loc_22F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_22FC',
    )

    Jump('loc_2756')

    def _loc_22FC(): pass

    label('loc_22FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2394',
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

    Jump('loc_2756')

    def _loc_2394(): pass

    label('loc_2394')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_23F0',
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

    Jump('loc_2756')

    def _loc_23F0(): pass

    label('loc_23F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_24C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2453',
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

    Jump('loc_24C2')

    def _loc_2453(): pass

    label('loc_2453')

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

    def _loc_24C2(): pass

    label('loc_24C2')

    Jump('loc_2756')

    def _loc_24C5(): pass

    label('loc_24C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_259F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2517',
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

    Jump('loc_259C')

    def _loc_2517(): pass

    label('loc_2517')

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

    def _loc_259C(): pass

    label('loc_259C')

    Jump('loc_2756')

    def _loc_259F(): pass

    label('loc_259F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2711',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_262C',
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

    Jump('loc_270E')

    def _loc_262C(): pass

    label('loc_262C')

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

    def _loc_270E(): pass

    label('loc_270E')

    Jump('loc_2756')

    def _loc_2711(): pass

    label('loc_2711')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2756',
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

    def _loc_2756(): pass

    label('loc_2756')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x275A
@scena.Code('func_10_275A')
def func_10_275A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2767',
    )

    Jump('loc_29AD')

    def _loc_2767(): pass

    label('loc_2767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2771',
    )

    Jump('loc_29AD')

    def _loc_2771(): pass

    label('loc_2771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_277B',
    )

    Jump('loc_29AD')

    def _loc_277B(): pass

    label('loc_277B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_27DA',
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

    Jump('loc_29AD')

    def _loc_27DA(): pass

    label('loc_27DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2823',
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

    Jump('loc_29AD')

    def _loc_2823(): pass

    label('loc_2823')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_284E',
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

    Jump('loc_29AD')

    def _loc_284E(): pass

    label('loc_284E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_289D',
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

    Jump('loc_29AD')

    def _loc_289D(): pass

    label('loc_289D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_28F7',
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

    Jump('loc_29AD')

    def _loc_28F7(): pass

    label('loc_28F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_293E',
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

    Jump('loc_29AD')

    def _loc_293E(): pass

    label('loc_293E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_296F',
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

    Jump('loc_29AD')

    def _loc_296F(): pass

    label('loc_296F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_29AD',
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

    def _loc_29AD(): pass

    label('loc_29AD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x29B1
@scena.Code('func_11_29B1')
def func_11_29B1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2A87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2A1D',
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

    Jump('loc_2A84')

    def _loc_2A1D(): pass

    label('loc_2A1D')

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

    def _loc_2A84(): pass

    label('loc_2A84')

    Jump('loc_2D70')

    def _loc_2A87(): pass

    label('loc_2A87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2ADF',
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

    Jump('loc_2D70')

    def _loc_2ADF(): pass

    label('loc_2ADF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2B30',
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

    Jump('loc_2D70')

    def _loc_2B30(): pass

    label('loc_2B30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2B6E',
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

    Jump('loc_2D70')

    def _loc_2B6E(): pass

    label('loc_2B6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2BDA',
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

    Jump('loc_2D70')

    def _loc_2BDA(): pass

    label('loc_2BDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2C49',
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

    Jump('loc_2D70')

    def _loc_2C49(): pass

    label('loc_2C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2C9B',
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

    Jump('loc_2D70')

    def _loc_2C9B(): pass

    label('loc_2C9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2D06',
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

    Jump('loc_2D70')

    def _loc_2D06(): pass

    label('loc_2D06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2D26',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～真麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D70')

    def _loc_2D26(): pass

    label('loc_2D26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2D4A',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，这个也很不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D70')

    def _loc_2D4A(): pass

    label('loc_2D4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2D70',
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

    def _loc_2D70(): pass

    label('loc_2D70')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x2D74
@scena.Code('func_12_2D74')
def func_12_2D74():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2DDB',
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

    Jump('loc_313D')

    def _loc_2DDB(): pass

    label('loc_2DDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2E38',
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

    Jump('loc_313D')

    def _loc_2E38(): pass

    label('loc_2E38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2E6B',
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

    Jump('loc_313D')

    def _loc_2E6B(): pass

    label('loc_2E6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2EAF',
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

    Jump('loc_313D')

    def _loc_2EAF(): pass

    label('loc_2EAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2F17',
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

    Jump('loc_313D')

    def _loc_2F17(): pass

    label('loc_2F17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2F48',
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

    Jump('loc_313D')

    def _loc_2F48(): pass

    label('loc_2F48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2FA0',
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

    Jump('loc_313D')

    def _loc_2FA0(): pass

    label('loc_2FA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2FCD',
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

    Jump('loc_313D')

    def _loc_2FCD(): pass

    label('loc_2FCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_306B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3009',
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

    Jump('loc_3068')

    def _loc_3009(): pass

    label('loc_3009')

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

    def _loc_3068(): pass

    label('loc_3068')

    Jump('loc_313D')

    def _loc_306B(): pass

    label('loc_306B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_30CD',
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

    Jump('loc_313D')

    def _loc_30CD(): pass

    label('loc_30CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_313D',
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

    def _loc_313D(): pass

    label('loc_313D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3141
@scena.Code('func_13_3141')
def func_13_3141():
    Call(0, 0x0014)

    Return()

# id: 0x0014 offset: 0x3146
@scena.Code('func_14_3146')
def func_14_3146():
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
        'loc_31A4',
    )

    OP_0D()
    OP_A9(0x5E)
    OP_56(0x00)
    TalkEnd(0x0019)

    Return()

    def _loc_31A4(): pass

    label('loc_31A4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31B5',
    )

    TalkEnd(0x0019)

    Return()

    def _loc_31B5(): pass

    label('loc_31B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_329A',
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

    Jump('loc_3613')

    def _loc_329A(): pass

    label('loc_329A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3304',
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

    Jump('loc_3613')

    def _loc_3304(): pass

    label('loc_3304')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_34C3',
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_332C'),
        (0x00000001, 'loc_3354'),
        (0x00000002, 'loc_3384'),
        (0x00000003, 'loc_33B0'),
        (0x00000004, 'loc_342B'),
        (0x00000005, 'loc_345F'),
        (-1, 'loc_3495'),
    )

    def _loc_332C(): pass

    label('loc_332C')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐她有脚气！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3495')

    def _loc_3354(): pass

    label('loc_3354')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐她是个方向白痴呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3495')

    def _loc_3384(): pass

    label('loc_3384')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '我姐姐很怕蟑螂的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3495')

    def _loc_33B0(): pass

    label('loc_33B0')

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

    Jump('loc_3495')

    def _loc_342B(): pass

    label('loc_342B')

    ChrTalk(
        0x0019,
        (
            '这～个，这～个，\n',
            '姐姐她喜欢吃甜食却长不胖！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3495')

    def _loc_345F(): pass

    label('loc_345F')

    ChrTalk(
        0x0019,
        (
            '那～个，那～个，\n',
            '姐姐有低血压，早晨很衰弱哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3495')

    def _loc_3495(): pass

    label('loc_3495')

    ChrTalk(
        0x0019,
        (
            '所、所以呢，\n',
            '她不适合做红茶销售员哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3613')

    def _loc_34C3(): pass

    label('loc_34C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3613',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_3546',
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

    Jump('loc_3613')

    def _loc_3546(): pass

    label('loc_3546')

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

    def _loc_3613(): pass

    label('loc_3613')

    TalkEnd(0x0019)

    Return()

# id: 0x0015 offset: 0x3617
@scena.Code('func_15_3617')
def func_15_3617():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_368B',
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

    Jump('loc_422F')

    def _loc_368B(): pass

    label('loc_368B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_3740',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_36E6',
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

    Jump('loc_373D')

    def _loc_36E6(): pass

    label('loc_36E6')

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

    def _loc_373D(): pass

    label('loc_373D')

    Jump('loc_422F')

    def _loc_3740(): pass

    label('loc_3740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_387F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_37B5',
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

    Jump('loc_387C')

    def _loc_37B5(): pass

    label('loc_37B5')

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

    def _loc_387C(): pass

    label('loc_387C')

    Jump('loc_422F')

    def _loc_387F(): pass

    label('loc_387F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_39EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_38E6',
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

    Jump('loc_39EB')

    def _loc_38E6(): pass

    label('loc_38E6')

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

    def _loc_39EB(): pass

    label('loc_39EB')

    Jump('loc_422F')

    def _loc_39EE(): pass

    label('loc_39EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3B62',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3A4A',
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

    Jump('loc_3B5F')

    def _loc_3A4A(): pass

    label('loc_3A4A')

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

    def _loc_3B5F(): pass

    label('loc_3B5F')

    Jump('loc_422F')

    def _loc_3B62(): pass

    label('loc_3B62')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3CC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3BBE',
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

    Jump('loc_3CC5')

    def _loc_3BBE(): pass

    label('loc_3BBE')

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

    def _loc_3CC5(): pass

    label('loc_3CC5')

    Jump('loc_422F')

    def _loc_3CC8(): pass

    label('loc_3CC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3E59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3D29',
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

    Jump('loc_3E56')

    def _loc_3D29(): pass

    label('loc_3D29')

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

    def _loc_3E56(): pass

    label('loc_3E56')

    Jump('loc_422F')

    def _loc_3E59(): pass

    label('loc_3E59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3FB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3EF1',
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

    Jump('loc_3FB3')

    def _loc_3EF1(): pass

    label('loc_3EF1')

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

    def _loc_3FB3(): pass

    label('loc_3FB3')

    Jump('loc_422F')

    def _loc_3FB6(): pass

    label('loc_3FB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_40E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3FFA',
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

    Jump('loc_40DD')

    def _loc_3FFA(): pass

    label('loc_3FFA')

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

    def _loc_40DD(): pass

    label('loc_40DD')

    Jump('loc_422F')

    def _loc_40E0(): pass

    label('loc_40E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4165',
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

    Jump('loc_422F')

    def _loc_4165(): pass

    label('loc_4165')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_422F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_41C8',
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

    Jump('loc_422F')

    def _loc_41C8(): pass

    label('loc_41C8')

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

    def _loc_422F(): pass

    label('loc_422F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x4233
@scena.Code('func_16_4233')
def func_16_4233():
    Call(0, 0x0017)

    Return()

# id: 0x0017 offset: 0x4238
@scena.Code('func_17_4238')
def func_17_4238():
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
        'loc_4296',
    )

    OP_0D()
    OP_A9(0x5D)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_4296(): pass

    label('loc_4296')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42A7',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_42A7(): pass

    label('loc_42A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4376',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4309',
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

    Jump('loc_4373')

    def _loc_4309(): pass

    label('loc_4309')

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

    def _loc_4373(): pass

    label('loc_4373')

    Jump('loc_4A5D')

    def _loc_4376(): pass

    label('loc_4376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_444A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_43E3',
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

    Jump('loc_4447')

    def _loc_43E3(): pass

    label('loc_43E3')

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

    def _loc_4447(): pass

    label('loc_4447')

    Jump('loc_4A5D')

    def _loc_444A(): pass

    label('loc_444A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_451D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_44AB',
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

    Jump('loc_451A')

    def _loc_44AB(): pass

    label('loc_44AB')

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

    def _loc_451A(): pass

    label('loc_451A')

    Jump('loc_4A5D')

    def _loc_451D(): pass

    label('loc_451D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_458D',
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

    Jump('loc_4A5D')

    def _loc_458D(): pass

    label('loc_458D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_46BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4611',
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

    Jump('loc_46BA')

    def _loc_4611(): pass

    label('loc_4611')

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

    def _loc_46BA(): pass

    label('loc_46BA')

    Jump('loc_4A5D')

    def _loc_46BD(): pass

    label('loc_46BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_47E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_473E',
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

    Jump('loc_47E5')

    def _loc_473E(): pass

    label('loc_473E')

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

    def _loc_47E5(): pass

    label('loc_47E5')

    Jump('loc_4A5D')

    def _loc_47E8(): pass

    label('loc_47E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_48F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4851',
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

    Jump('loc_48F3')

    def _loc_4851(): pass

    label('loc_4851')

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

    def _loc_48F3(): pass

    label('loc_48F3')

    Jump('loc_4A5D')

    def _loc_48F6(): pass

    label('loc_48F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4968',
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

    Jump('loc_4A5D')

    def _loc_4968(): pass

    label('loc_4968')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_49CA',
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

    Jump('loc_4A5D')

    def _loc_49CA(): pass

    label('loc_49CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4A35',
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

    Jump('loc_4A5D')

    def _loc_4A35(): pass

    label('loc_4A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4A5D',
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

    def _loc_4A5D(): pass

    label('loc_4A5D')

    TalkEnd(0x000B)

    Return()

# id: 0x0018 offset: 0x4A61
@scena.Code('func_18_4A61')
def func_18_4A61():
    Call(0, 0x0019)

    Return()

# id: 0x0019 offset: 0x4A66
@scena.Code('func_19_4A66')
def func_19_4A66():
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
        'loc_4ADC',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4AC8',
    )

    OP_A9(0x69)

    Jump('loc_4AD6')

    def _loc_4AC8(): pass

    label('loc_4AC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4AD4',
    )

    OP_A9(0x68)

    Jump('loc_4AD6')

    def _loc_4AD4(): pass

    label('loc_4AD4')

    OP_A9(0x5C)

    def _loc_4AD6(): pass

    label('loc_4AD6')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_4ADC(): pass

    label('loc_4ADC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AED',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_4AED(): pass

    label('loc_4AED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4B5E',
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

    Jump('loc_4FD8')

    def _loc_4B5E(): pass

    label('loc_4B5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4BBB',
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

    Jump('loc_4FD8')

    def _loc_4BBB(): pass

    label('loc_4BBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4C2D',
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

    Jump('loc_4FD8')

    def _loc_4C2D(): pass

    label('loc_4C2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4C7B',
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

    Jump('loc_4FD8')

    def _loc_4C7B(): pass

    label('loc_4C7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4CB0',
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

    Jump('loc_4FD8')

    def _loc_4CB0(): pass

    label('loc_4CB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4CFB',
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

    Jump('loc_4FD8')

    def _loc_4CFB(): pass

    label('loc_4CFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4D75',
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

    Jump('loc_4FD8')

    def _loc_4D75(): pass

    label('loc_4D75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4DCD',
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

    Jump('loc_4FD8')

    def _loc_4DCD(): pass

    label('loc_4DCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4EDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4E4F',
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

    Jump('loc_4EDB')

    def _loc_4E4F(): pass

    label('loc_4E4F')

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

    def _loc_4EDB(): pass

    label('loc_4EDB')

    Jump('loc_4FD8')

    def _loc_4EDE(): pass

    label('loc_4EDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4FAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4F1A',
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

    Jump('loc_4FA9')

    def _loc_4F1A(): pass

    label('loc_4F1A')

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

    def _loc_4FA9(): pass

    label('loc_4FA9')

    Jump('loc_4FD8')

    def _loc_4FAC(): pass

    label('loc_4FAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4FD8',
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

    def _loc_4FD8(): pass

    label('loc_4FD8')

    TalkEnd(0x000A)

    Return()

# id: 0x001A offset: 0x4FDC
@scena.Code('func_1A_4FDC')
def func_1A_4FDC():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5058',
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

    Jump('loc_50B9')

    def _loc_5058(): pass

    label('loc_5058')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5062',
    )

    Jump('loc_50B9')

    def _loc_5062(): pass

    label('loc_5062')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_506C',
    )

    Jump('loc_50B9')

    def _loc_506C(): pass

    label('loc_506C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5076',
    )

    Jump('loc_50B9')

    def _loc_5076(): pass

    label('loc_5076')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5080',
    )

    Jump('loc_50B9')

    def _loc_5080(): pass

    label('loc_5080')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_508A',
    )

    Jump('loc_50B9')

    def _loc_508A(): pass

    label('loc_508A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5094',
    )

    Jump('loc_50B9')

    def _loc_5094(): pass

    label('loc_5094')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_509E',
    )

    Jump('loc_50B9')

    def _loc_509E(): pass

    label('loc_509E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_50A8',
    )

    Jump('loc_50B9')

    def _loc_50A8(): pass

    label('loc_50A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_50B2',
    )

    Jump('loc_50B9')

    def _loc_50B2(): pass

    label('loc_50B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_50B9',
    )

    def _loc_50B9(): pass

    label('loc_50B9')

    TalkEnd(0x0009)

    Return()

# id: 0x001B offset: 0x50BD
@scena.Code('func_1B_50BD')
def func_1B_50BD():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_530A',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 9240, 0, 5790, 90)
    SetChrPos(0x0102, 9180, 0, 4760, 90)
    SetChrPos(0x0108, 8280, 0, 5410, 90)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetChrSubChip(0x0008, 0)
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
        'loc_5144',
    )

    OP_28(0x004B, 0x01, 0x0100)

    def _loc_5144(): pass

    label('loc_5144')

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

    Jump('loc_576C')

    def _loc_530A(): pass

    label('loc_530A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_55FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5372',
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

    Jump('loc_55F9')

    def _loc_5372(): pass

    label('loc_5372')

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
        'loc_55F9',
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
    SetChrName('')

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

    def _loc_55F9(): pass

    label('loc_55F9')

    Jump('loc_576C')

    def _loc_55FC(): pass

    label('loc_55FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5606',
    )

    Jump('loc_576C')

    def _loc_5606(): pass

    label('loc_5606')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5610',
    )

    Jump('loc_576C')

    def _loc_5610(): pass

    label('loc_5610')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_569D',
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

    Jump('loc_576C')

    def _loc_569D(): pass

    label('loc_569D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_56A7',
    )

    Jump('loc_576C')

    def _loc_56A7(): pass

    label('loc_56A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_573D',
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

    Jump('loc_576C')

    def _loc_573D(): pass

    label('loc_573D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5747',
    )

    Jump('loc_576C')

    def _loc_5747(): pass

    label('loc_5747')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5751',
    )

    Jump('loc_576C')

    def _loc_5751(): pass

    label('loc_5751')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_575B',
    )

    Jump('loc_576C')

    def _loc_575B(): pass

    label('loc_575B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5765',
    )

    Jump('loc_576C')

    def _loc_5765(): pass

    label('loc_5765')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_576C',
    )

    def _loc_576C(): pass

    label('loc_576C')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
