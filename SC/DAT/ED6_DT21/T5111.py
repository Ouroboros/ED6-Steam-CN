import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5111   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚妮拉丝'),
    TXT(0x02, '克鲁茨'),
    TXT(0x03, '维修师罗伯特'),
    TXT(0x04, '菲莉斯管理员'),
    TXT(0x05, '猎兵'),
    TXT(0x06, '女猎兵'),
    TXT(0x07, '发烟筒用目标角色'),
    TXT(0x08, '目标用照相机'),
    TXT(0x09, '器皿'),
    TXT(0x0A, '器皿'),
    TXT(0x0B, '器皿'),
    TXT(0x0C, '咖啡'),
    TXT(0x0D, '咖啡'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5111.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3860
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
        ('ED6_DT27/CH03090._CH', 'ED6_DT27/CH03090P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT27/CH03093._CH', 'ED6_DT27/CH03093P._CP'),
        ('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT27/CH03900._CH', 'ED6_DT27/CH03900P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00261._CH', 'ED6_DT07/CH00261P._CP'),
        ('ED6_DT06/CH20008._CH', 'ED6_DT06/CH20008P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20000P._CP'),
        ('ED6_DT07/CH00414._CH', 'ED6_DT07/CH00414P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT27/CH04820._CH', 'ED6_DT27/CH04820P._CP'),
        ('ED6_DT27/CH04821._CH', 'ED6_DT27/CH04821P._CP'),
        ('ED6_DT27/CH04640._CH', 'ED6_DT27/CH04640P._CP'),
        ('ED6_DT27/CH04641._CH', 'ED6_DT27/CH04641P._CP'),
        ('ED6_DT06/CH20067._CH', 'ED6_DT06/CH20067P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT27/CH03093._CH', 'ED6_DT27/CH03093P._CP'),
        ('ED6_DT27/CH03133._CH', 'ED6_DT27/CH03133P._CP'),
        ('ED6_DT27/CH03091._CH', 'ED6_DT27/CH03091P._CP'),
        ('ED6_DT27/CH04824._CH', 'ED6_DT27/CH04824P._CP'),
        ('ED6_DT26/CH20265._CH', 'ED6_DT26/CH20265P._CP'),
        ('ED6_DT26/CH20267._CH', 'ED6_DT26/CH20267P._CP'),
    ]

# id: 0x10002 offset: 0x19A
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
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
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
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 26690,
            z                   = 0,
            y                   = 5140,
            direction           = 270,
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
            x                   = 24500,
            z                   = 0,
            y                   = 12470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
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
            dword_10            = 18,
            chipIndex           = 18,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900553,
            chipIndex           = 9,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
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
            dword_10            = 65547,
            chipIndex           = 11,
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
            dword_10            = 65547,
            chipIndex           = 11,
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
            dword_10            = 65547,
            chipIndex           = 11,
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
            dword_10            = 1572875,
            chipIndex           = 11,
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
            dword_10            = 1638411,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x33A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x33A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 120250,
            y           = 0,
            z           = 1000,
            range       = 123170,
            dword_10    = 0x000007D0,
            dword_14    = 0x000007D0,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10005 offset: 0x35A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 25470,
            triggerZ            = -300,
            triggerY            = 4940,
            triggerRange        = 800,
            actorX              = 26690,
            actorZ              = 1500,
            actorY              = 5140,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22500,
            triggerZ            = 0,
            triggerY            = 12360,
            triggerRange        = 800,
            actorX              = 24500,
            actorZ              = 1500,
            actorY              = 12470,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 85780,
            triggerZ            = 0,
            triggerY            = 41480,
            triggerRange        = 800,
            actorX              = 85180,
            actorZ              = 500,
            actorY              = 41480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3C6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 4, 0x100C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48D',
    )

    SetChrPos(0x0010, 18160, 800, 11990, 0)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0013, 17670, 800, 12040, 0)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0011, 17600, 800, 11180, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0014, 18270, 750, 10980, 0)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0012, 18190, 750, 11550, 0)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0008, 115820, 0, 39550, 90)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0009, 88540, 200, -30700, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0010)
    SetChrFlags(0x0009, 0x0004)
    SetChrChipByIndex(0x0009, 25)
    SetChrSubChip(0x0009, 0)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    def _loc_48D(): pass

    label('loc_48D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 3, 0x100B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_499',
    )

    Event(0, 0x0009)

    def _loc_499(): pass

    label('loc_499')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 4, 0x100C)),
            Expr.Return,
        ),
        'loc_4B0',
    )

    Event(0, 0x000B)

    def _loc_4B0(): pass

    label('loc_4B0')

    Return()

# id: 0x0001 offset: 0x4B1
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 3, 0x100B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 4, 0x100C)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4C4',
    )

    OP_64(0x02, 0x0001)

    Jump('loc_4C8')

    def _loc_4C4(): pass

    label('loc_4C4')

    OP_65(0x02, 0x0001)

    def _loc_4C8(): pass

    label('loc_4C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 5, 0x100D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4DF',
    )

    OP_72(0x0000, 0x0020)
    OP_70(0x0019, 0x00000000)

    Jump('loc_4EB')

    def _loc_4DF(): pass

    label('loc_4DF')

    OP_72(0x0000, 0x0020)
    OP_6F(0x0019, 60)

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x397),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_50C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_521')

    def _loc_50C(): pass

    label('loc_50C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 4, 0x100C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 5, 0x100D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_521',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x29),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_521(): pass

    label('loc_521')

    Return()

# id: 0x0002 offset: 0x522
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_553'),
        (0x00000001, 'loc_55F'),
        (0x00000002, 'loc_56B'),
        (0x00000003, 'loc_577'),
        (0x00000004, 'loc_583'),
        (0x00000005, 'loc_58F'),
        (0x00000006, 'loc_59B'),
        (-1, 'loc_5A7'),
    )

    def _loc_553(): pass

    label('loc_553')

    OP_99(0x00FE, 0x00, 0x07, 0x000005AA)

    Jump('loc_5B3')

    def _loc_55F(): pass

    label('loc_55F')

    OP_99(0x00FE, 0x00, 0x07, 0x0000060E)

    Jump('loc_5B3')

    def _loc_56B(): pass

    label('loc_56B')

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('loc_5B3')

    def _loc_577(): pass

    label('loc_577')

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('loc_5B3')

    def _loc_583(): pass

    label('loc_583')

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_5B3')

    def _loc_58F(): pass

    label('loc_58F')

    OP_99(0x00FE, 0x00, 0x07, 0x00000546)

    Jump('loc_5B3')

    def _loc_59B(): pass

    label('loc_59B')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B3')

    def _loc_5A7(): pass

    label('loc_5A7')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B3')

    def _loc_5B3(): pass

    label('loc_5B3')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C8',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B3')

    def _loc_5C8(): pass

    label('loc_5C8')

    Return()

# id: 0x0003 offset: 0x5C9
@scena.Code('func_03_5C9')
def func_03_5C9():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_659',
    )

    Jump('loc_69B')

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_675',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_69B')

    def _loc_675(): pass

    label('loc_675')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_691',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_69B')

    def _loc_691(): pass

    label('loc_691')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_69B(): pass

    label('loc_69B')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0009, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0207, 1, 0x1039)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB2',
    )

    OP_A2(0x1039)

    ChrTalk(
        0x0009,
        (
            '#0330191020V#840F哟，是艾丝蒂尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191021V#1000F嘿嘿，晚上好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191022V克鲁茨前辈在看书？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191023V#840F嗯嗯、正在复习\n',
            '东方的兵书呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191024V虽然记载的是古代战争，\n',
            '但我们也能从中学到不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191025V建议你也看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191026V#1016F唔、嗯～对我来说\n',
            '大概有点难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191027V#1015F不过、东方的兵书啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191028V……那个，克鲁茨前辈\n',
            '难道是东方出身的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191029V#843F嗯，出身虽是利贝尔，\n',
            '但原本好像是来自东方的家族。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191030V据说我祖父那代是\n',
            '从那边远道移民而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191031V#840F我施展的方术也是祖父\n',
            '传授的家传秘技。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191032V#1011F啊，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191033V这么方便的法术，\n',
            '我说怎么从来没见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191034V#844F确实在利贝尔\n',
            '没见过除我之外的使用者……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191035V#840F你要是有心、艾丝蒂尔。\n',
            '传授给你怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191036V#1004F真、真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191037V#840F啊啊，当然是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191038V不过，在那之前需要\n',
            '读破万卷兵书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191039V#1007F又受打击了…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191040V我，我办不到啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5C')

    def _loc_AB2(): pass

    label('loc_AB2')

    ChrTalk(
        0x0009,
        (
            '#0330191041V#840F古代的书里\n',
            '隐藏着大量值得学习的智慧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191042V如果有机会可别对它们敬而远之，\n',
            '还是多多接触才好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191043V广泛增长见识\n',
            '也是游击士所必须的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B5C(): pass

    label('loc_B5C')

    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0xB65
@scena.Code('func_04_B65')
def func_04_B65():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0207, 0, 0x1038)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D68',
    )

    OP_A2(0x1038)

    ChrTalk(
        0x0008,
        (
            '#0120191044V#814F啊、艾丝蒂尔。\n',
            '还没休息啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191045V难道你\n',
            '在准备明天的训练？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191046V#1011F啊，嗯。\n',
            '准备是有准备啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191047V亚妮拉丝在做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191048V#810F嗯，和小熊们\n',
            '稍微说说话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191049V#1004F小、小熊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191050V#1310F很可爱吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191051V#1311F啊～这蓬蓬松松\n',
            '又柔软无比～的毛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191052V只是摸摸\n',
            '就精神十足哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191053V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191054V这就是亚妮拉丝\n',
            '的精神之源啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191055V#816F嗯！就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC7')

    def _loc_D68(): pass

    label('loc_D68')

    ChrTalk(
        0x0008,
        (
            '#0120191056V#1311F啊～抱着玩偶\n',
            '就能被治愈呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191057V#811F嗯！果然\n',
            '可爱就是正义啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DC7(): pass

    label('loc_DC7')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xDCB
@scena.Code('func_05_DCB')
def func_05_DCB():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xDD0
@scena.Code('func_06_DD0')
def func_06_DD0():
    TalkBegin(0x000B)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DF8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_DF0',
    )

    OP_A9(0xFC)

    Jump('loc_DF2')

    def _loc_DF0(): pass

    label('loc_DF0')

    OP_A9(0xFF)

    def _loc_DF2(): pass

    label('loc_DF2')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_DF8(): pass

    label('loc_DF8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E09',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_E09(): pass

    label('loc_E09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 6, 0x1036)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FC3',
    )

    OP_A2(0x1036)

    ChrTalk(
        0x000B,
        (
            '#2750191058V哎呀，艾丝蒂尔。\n',
            '演习辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750191059V哈哈哈，看这表情\n',
            '似乎相当地严苛呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191060V#1007F嗯，全身都快散架了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191061V#1006F不过，训练还在继续。\n',
            '这点程度得要忍受下去才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750191062V嗯嗯，就是这种气势㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750191063V那么，为了明天\n',
            '还得补充装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750191064V早上来做就太匆忙了，\n',
            '最好是趁现在就做好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191065V#1011F啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191066V那么，麻烦\n',
            '再给我看看道具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_102D')

    def _loc_FC3(): pass

    label('loc_FC3')

    ChrTalk(
        0x000B,
        (
            '#2750191067V为了明天的训练趁现在\n',
            '补充一下装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750191068V早上再做的话，\n',
            '匆匆忙忙挺麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_102D(): pass

    label('loc_102D')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x1031
@scena.Code('func_07_1031')
def func_07_1031():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x1036
@scena.Code('func_08_1036')
def func_08_1036():
    TalkBegin(0x000A)
    OP_A2(0x1007)

    If(
        (
            (Expr.Eval, "OP_40(0x02D6, 0x00)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 1, 0x1041)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_117B',
    )

    ChrTalk(
        0x000A,
        (
            '#2760191069V啊，艾丝蒂尔……\n',
            '得到『天眼』了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191070V那可是所谓的\n',
            '高级结晶回路呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191071V要安装的话\n',
            '需要强化结晶孔才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191072V虽然需要相应的耀晶片，\n',
            '但能提高最大ＥＰ，所以推荐试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191073V工房的菜单里\n',
            '选[改造·换钱]-[结晶孔]\n',
            '就能强化结晶孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)
    OP_A2(0x1041)
    TalkEnd(0x000A)

    Return()

    def _loc_117B(): pass

    label('loc_117B')

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
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '买东西\n'),
            TXT(0x03, '离开\n'),
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
        'loc_11E1',
    )

    OP_0D()
    OP_A9(0xFA)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_11E1(): pass

    label('loc_11E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11F7',
    )

    OP_0D()
    OP_A9(0xFB)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_11F7(): pass

    label('loc_11F7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1208',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_1208(): pass

    label('loc_1208')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1298',
    )

    ChrTalk(
        0x000A,
        (
            '#2760191074V没有强化过的结晶孔\n',
            '是不能安装高级结晶回路的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191075V强化结晶孔需要耀晶片，\n',
            '但能提高最大ＥＰ，就试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E1')

    def _loc_1298(): pass

    label('loc_1298')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_136D',
    )

    OP_A2(0x0001)

    ChrTalk(
        0x000A,
        (
            '#2760191076V哟，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191077V今天的演习中应该也\n',
            '得到了一些耀晶片吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191078V可以的话就试着\n',
            '合成新结晶回路看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191079V为了适应新型导力器\n',
            '不断尝试也很重要哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E1')

    def _loc_136D(): pass

    label('loc_136D')

    ChrTalk(
        0x000A,
        (
            '#2760191078V可以的话就试着\n',
            '合成新结晶回路看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760191081V总之与其学习不如习惯。\n',
            '不断尝试也很重要哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13E1(): pass

    label('loc_13E1')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x13E5
@scena.Code('func_09_13E5')
def func_09_13E5():
    EventBegin(0x00)
    OP_70(0x0019, 0x00000000)
    OP_6D(27560, 0, 11600, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x010A, 0x0004)
    SetChrPos(0x010A, 18080, 200, 12890, 180)
    SetChrPos(0x0101, 18120, 200, 10470, 0)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x010A, 0)
    SetChrChipByIndex(0x0101, 1)
    SetChrChipByIndex(0x010A, 2)
    SetChrPos(0x0010, 18160, 800, 11990, 0)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0013, 17670, 800, 12040, 0)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0011, 17600, 800, 11180, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0014, 18270, 800, 10980, 0)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0012, 18190, 800, 11550, 0)
    ClearChrFlags(0x0012, 0x0080)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_14E8')
    def lambda_14E8():
        OP_6D(18250, 200, 11830, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14E8)

    @scena.Lambda('lambda_1500')
    def lambda_1500():
        OP_67(0, 7000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1500)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120190967V#819F#5P唉……\n',
            '今天真是严苛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190968V#810F不过，在这里的训练\n',
            '也差不多快结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190969V#1015F嗯～\n',
            '好像又高兴，又遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190970V#1011F不过话说回来……\n',
            '克鲁茨前辈相当强吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190971V即使面对我们２人\n',
            '还绰绰有余的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190972V#811F#5P啊哈哈，那当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190973V#816F说到『方术使』克鲁茨\n',
            '那可是利贝尔游击士的ＮＯ．２啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190974V第一就不用说了，\n',
            '当然是艾丝蒂尔的爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190975V#1025F啊、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190976V#810F#5P顺带一提，正游击士的等级\n',
            '从Ｇ到Ａ有７级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190977V比如说我，花了半年\n',
            '才终于升级到Ｆ……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190978V克鲁茨前辈可是马上\n',
            '要从Ｂ升级到Ａ了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190979V#1011F啊、Ａ级的话\n',
            '就和金先生一样了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190980V#1003F（不过，让那么厉害的克鲁茨前辈\n',
            '失忆的犯人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190981V（我……能阻止吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190982V#814F#5P……艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190983V怎么了，一脸严肃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190984V#1004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190985V#1013F抱、抱歉。\n',
            '稍微发了会儿呆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190986V#812F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190987V难道…\n',
            '在想约修亚的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190988V#1013F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190989V#1025F嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190990V#1314F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190991V我从雪拉前辈\n',
            '那里稍微听说了点情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190992V你很担心他吧……\n',
            '现在，在哪里呢?在干什么呢?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190993V#1003F……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190994V#1006F不过，没关系！\n',
            '不用太担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190995V反正约修亚\n',
            '只不过是一个自己在胡乱\n',
            '钻牛角尖的离家小孩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190996V#1005F我一定要找到他，\n',
            '用绳子套住他的脖子拖回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190997V#811F#5P对了，就是这股气势！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190998V#816F艾丝蒂尔只要有这种气势，\n',
            '就绝对能够找到约修亚的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190999V姐姐向你保证哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191000V#1016F哈哈，谢谢你啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191001V#1015F啊，不过……\n',
            '亚妮拉丝前辈可没什么\n',
            '姐姐的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191002V#812F#5P啊～好过分，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191003V你一直觉得\n',
            '我很孩子气对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191004V#1008F（这……）\n',
            '哪、哪有～那倒不至于啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191005V#1316F#5P嗯，再怎么说，\n',
            '我也比你大两岁啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191006V#810F不过算了，与其被看作前辈，\n',
            '不如以朋友的身份交往要更开心一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191007V#811F呵呵，今后就请多指教啰？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191008V#1008F啊……\n',
            '嗯，彼此彼此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)
    SetChrSubChip(0x010A, 0)
    SetChrChipByIndex(0x010A, 0)
    ClearChrFlags(0x010A, 0x0004)
    SetChrPos(0x010A, 19230, 0, 12970, 98)
    OP_0D()
    SetChrSubChip(0x0101, 2)
    ChrTurnDirection(0x010A, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191009V#810F#5P好了～也该休息了，\n',
            '明天还要早起呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191010V今天也很累了。\n',
            '明天的晨练，还能参加吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191011V#1006F啊，那没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191012V我无论多累\n',
            '第二天都会没事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191013V只要亚妮拉丝前辈还撑得住，\n',
            '多少个回合都奉陪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191014V#811F#5P太好了，就是要这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191015V#1310F那就晚安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191016V#1011F嗯，晚安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x010A, 20820, 0, 9330, 3000, 0x00)

    @scena.Lambda('lambda_1EFE')
    def lambda_1EFE():
        OP_8E(0x010A, 27820, 2000, 9030, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1EFE)

    @scena.Lambda('lambda_1F19')
    def lambda_1F19():
        OP_6D(20870, 200, 10700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F19)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_1F3B')
    def lambda_1F3B():
        OP_8E(0x010A, 27780, 2000, 10940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1F3B)

    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_1F5B')
    def lambda_1F5B():
        OP_8E(0x010A, 25560, 3500, 11290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1F5B)

    @scena.Lambda('lambda_1F76')
    def lambda_1F76():
        OP_9F(0x010A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_1F76)

    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_1F8D')
    def lambda_1F8D():
        OP_69(0x0101, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F8D)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrFlags(0x010A, 0x0080)
    SetChrSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191017V#1012F#5P好了……\n',
            '我也该回房间休息了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191018V#1015F啊，对了。\n',
            '演习时候得到了很多耀晶片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191019V#1006F想准备点新的结晶回路，\n',
            '睡觉前先去工房看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(19120, 0, 10210, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0004)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 19120, 0, 10210, 103)
    FormationDelMember(0x09, 0xFF)
    OP_A2(0x100B)
    OP_28(0x007E, 0x01, 0x0100)
    OP_28(0x007E, 0x01, 0x0200)
    OP_28(0x007E, 0x01, 0x0400)
    OP_28(0x007E, 0x01, 0x0800)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x20F2
@scena.Code('func_0A_20F2')
def func_0A_20F2():
    TalkBegin(0x00FF)
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
            TXT(0x00, '【暂时还不休息】\n'),
            TXT(0x01, '【今天可以休息了】\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2160',
    )

    TalkEnd(0x00FF)

    Return()

    def _loc_2160(): pass

    label('loc_2160')

    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010191082V#1007F啊，快累瘫了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191083V#1000F为了明天\n',
            '还是赶快去睡吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_20(0x000003E8)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    OP_0D()
    Sleep(5000)

    SetChrFlags(0x0008, 0x0080)
    OP_22(0x01F7, 0x00, 0x1E)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x28)
    Sleep(150)

    OP_22(0x01F7, 0x00, 0x23)
    Sleep(500)

    OP_22(0x01F7, 0x00, 0x28)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x32)
    Sleep(150)

    OP_22(0x01F7, 0x00, 0x2D)
    Sleep(400)

    OP_22(0x01F7, 0x00, 0x32)
    Sleep(100)

    OP_22(0x01F7, 0x00, 0x3C)
    Sleep(150)

    OP_22(0x01F7, 0x00, 0x37)
    Sleep(300)

    OP_22(0x020F, 0x00, 0x4B)
    Sleep(800)

    OP_22(0x01F7, 0x00, 0x4B)
    Sleep(300)

    OP_22(0x0246, 0x00, 0x5A)
    Sleep(800)

    OP_22(0x01F7, 0x00, 0x5A)
    Sleep(400)

    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0101, 0x0002)
    SetChrPos(0x0101, 85170, 300, 42180, 180)
    SetChrChipByIndex(0x0101, 8)
    SetChrSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010191084V#5P#455F（嗯……？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191085V#452F（这是……什么声音……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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
            TXT(0x00, '【马上起来】\n'),
            TXT(0x01, '【不管它继续睡】\n'),
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
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_273C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010191086V#459F（嗯－……好困啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191087V#455F（……不行……爬不起来……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191088V（…………………………………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191089V#456F……丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0072, 0x00, 0x64)
    Sleep(300)

    Sleep(1000)

    SetChrPos(0x0008, 86790, 0, 33860, 0)

    NpcTalk(
        0x0008,
        '女孩的声音',
        (
            '#0120191090V#40W#5P………蒂尔………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    NpcTalk(
        0x0008,
        '女孩的声音',
        (
            '#0120191091V#40W#5P……艾丝蒂尔……\n',
            '…………………快起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191092V#459F#5P………？…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0006, 0x00, 0x64)
    OP_22(0x001B, 0x00, 0x3C)
    Sleep(300)

    OP_22(0x001C, 0x00, 0x3C)
    Sleep(300)

    OP_22(0x001B, 0x00, 0x46)
    Sleep(300)

    OP_22(0x001C, 0x00, 0x46)
    Sleep(300)

    OP_22(0x001B, 0x00, 0x50)
    Sleep(300)

    OP_22(0x001C, 0x00, 0x50)
    Sleep(300)

    OP_22(0x001B, 0x00, 0x5A)
    Sleep(300)

    OP_22(0x001C, 0x00, 0x5A)
    Sleep(300)

    OP_22(0x001B, 0x00, 0x64)
    Sleep(300)

    OP_22(0x001C, 0x00, 0x64)
    Sleep(300)

    OP_22(0x001B, 0x00, 0x64)
    Sleep(300)

    OP_22(0x001C, 0x00, 0x64)
    Sleep(300)

    SetChrPos(0x0008, 86100, 0, 41700, 270)
    TerminateThread(0x0008, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0120191093V#5P#3S……起来啦！\n',
            '艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191094V#453F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, 86510, 0, 40980, 259)
    SetChrSubChip(0x0008, 0)
    ClearChrFlags(0x0008, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000014)
    OP_99(0x0101, 0x00, 0x08, 0x000004B0)
    OP_99(0x0101, 0x11, 0x12, 0x000004B0)
    SetChrSubChip(0x0101, 23)

    ChrTalk(
        0x0101,
        (
            '#0010191095V#453F啊……\n',
            '亚妮拉丝……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191096V#2P#812F艾丝蒂尔，起来啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191097V好，赶快准备吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191098V#451F怎、怎么了？\n',
            '神色那么慌张……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191099V而且这个声音……\n',
            '……难道是枪声！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191100V#2P#815F虽然不明白发生了什么\n',
            '但好像是有什么人来袭击了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191101V克鲁茨前辈正在应战\n',
            '艾丝蒂尔也赶快吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29BD')

    def _loc_273C(): pass

    label('loc_273C')

    OP_2B(0x007E, 0x0003)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000014)
    OP_99(0x0101, 0x00, 0x08, 0x000003E8)
    OP_99(0x0101, 0x11, 0x12, 0x000003E8)

    ChrTalk(
        0x0101,
        (
            '#0010191102V#451F这是什么声音……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191103V#453F难道是枪声！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0072, 0x00, 0x64)
    Sleep(300)

    SetChrPos(0x0008, 86790, 0, 33860, 0)

    ChrTalk(
        0x0008,
        (
            '#0120191104V#1P……艾丝蒂尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191105V艾丝蒂尔，起来了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_22(0x0006, 0x00, 0x64)
    Sleep(300)

    Sleep(200)

    SetChrPos(0x0008, 86530, 0, 35990, 0)
    OP_9F(0x0008, 0x00, 0x00, 0x00, 0x00, 0x00000000)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 26)

    @scena.Lambda('lambda_286C')
    def lambda_286C():
        OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_286C)

    OP_8E(0x0008, 86530, 0, 39780, 4000, 0x00)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0101, 23)

    ChrTalk(
        0x0101,
        (
            '#0010191106V#451F亚妮拉丝！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191107V#2P#812F太好了！\n',
            '你醒啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191097V好，赶快准备吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191109V#451F嗯，嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191110V这个枪声不会是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120191100V#2P#815F虽然不清楚怎么了，\n',
            '但好像是有什么人来袭击了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191101V克鲁茨前辈正在应战，\n',
            '艾丝蒂尔也赶快吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29BD(): pass

    label('loc_29BD')

    OP_1D(0x29)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(86600, 0, 40930, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrPos(0x0101, 86600, 0, 40930, 180)
    SetChrFlags(0x0008, 0x0080)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF7, 0xFF)
    Sleep(500)

    OP_A2(0x100C)
    OP_28(0x007F, 0x04, 0x02)
    OP_28(0x007F, 0x04, 0x08)
    OP_28(0x007F, 0x01, 0x0001)
    OP_64(0x02, 0x0001)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x2A5D
@scena.Code('func_0B_2A5D')
def func_0B_2A5D():
    EventBegin(0x00)
    OP_4A(0x000A, 255)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x000B, 0x00)
    SetChrPos(0x0101, 27210, 2000, 9020, 253)
    SetChrPos(0x010A, 28160, 2000, 8910, 262)
    SetChrPos(0x000A, 18980, -300, 5950, 166)
    SetChrPos(0x000B, 17150, -300, 5260, 170)
    SetChrPos(0x0009, 19400, -550, 370, 0)
    SetChrPos(0x000C, 20970, 0, 18840, 176)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x010A, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    ChrTurnDirection(0x000A, 0x0009, 1000)
    ChrTurnDirection(0x000B, 0x0009, 1000)

    @scena.Lambda('lambda_2B02')
    def lambda_2B02():
        ChrTurnDirection(0x000A, 0x0009, 0)
        Yield()

        Jump('lambda_2B02')

    DispatchAsync2(0x000A, 0x0001, lambda_2B02)

    @scena.Lambda('lambda_2B13')
    def lambda_2B13():
        ChrTurnDirection(0x000B, 0x0009, 0)
        Yield()

        Jump('lambda_2B13')

    DispatchAsync2(0x000B, 0x0001, lambda_2B13)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x9, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x9, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x9, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_9F(0x0009, 0x00, 0x00, 0x00, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_2B72')
    def lambda_2B72():
        OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2B72)

    OP_8E(0x0009, 19400, -550, 1850, 1000, 0x00)
    Sleep(500)

    OP_8C(0x0009, 180, 2000)
    Sleep(500)

    WaitForThreadExit(0x0009, 0x0001)
    OP_22(0x0073, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0330191113V#847F唔……\n',
            '这下暂且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x0009, 10)
    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x0009, 0x00, 0x03, 0x000004B0)

    ChrTalk(
        0x000A,
        (
            '#2760191114V#5P没、没事吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C1D')
    def lambda_2C1D():
        OP_8E(0x000B, 18740, -550, 2200, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2C1D)

    Sleep(500)

    @scena.Lambda('lambda_2C3D')
    def lambda_2C3D():
        OP_8E(0x000A, 18950, -300, 3810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2C3D)

    WaitForThreadExit(0x000B, 0x0001)
    OP_8C(0x000B, 125, 500)

    ChrTalk(
        0x000B,
        (
            '#2750191115V#5P不、不得了！\n',
            '手臂受伤了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191116V#844F没关系……\n',
            '只是擦伤……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191117V别说这个了……\n',
            '赶快抵御敌人的入侵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2CF3')
    def lambda_2CF3():
        OP_6D(21710, 0, 8600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2CF3)

    @scena.Lambda('lambda_2D0B')
    def lambda_2D0B():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2D0B)

    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x010A, 0x0080)

    @scena.Lambda('lambda_2D2D')
    def lambda_2D2D():
        OP_8E(0x0101, 21710, 0, 8600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D2D)

    Sleep(200)

    @scena.Lambda('lambda_2D4D')
    def lambda_2D4D():
        OP_8E(0x010A, 23180, 0, 8860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2D4D)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0009, 1000)
    ChrTurnDirection(0x010A, 0x0009, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(200)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191118V#1020F#5P克、克鲁茨前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191119V#815F#5P前、前辈！？\n',
            '受伤了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 1000)
    ChrTurnDirection(0x000A, 0x0101, 1000)

    ChrTalk(
        0x000B,
        (
            '#2750191120V#1P艾丝蒂尔！\n',
            '亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E4B')
    def lambda_2E4B():
        OP_6D(19720, -300, 3340, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E4B)

    @scena.Lambda('lambda_2E63')
    def lambda_2E63():
        OP_8E(0x0101, 19720, -300, 3340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_2E63)

    Sleep(200)

    @scena.Lambda('lambda_2E83')
    def lambda_2E83():
        OP_8E(0x010A, 20950, -300, 3130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_2E83)

    ChrTurnDirection(0x000A, 0x0009, 500)
    ChrTurnDirection(0x000B, 0x0009, 500)
    WaitForThreadExit(0x010A, 0x0001)
    WaitForThreadExit(0x010A, 0x0002)
    ChrTurnDirection(0x0101, 0x0009, 1000)
    ChrTurnDirection(0x010A, 0x0009, 1000)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 29)
    SetChrSubChip(0x0009, 1)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#0330191121V#844F抱歉，一时大意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191122V你们都看到了，武装集团\n',
            '袭击了这建筑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191123V你们俩快协助迎击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191124V#1005F明、明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191125V#813F#5P怎么会……\n',
            '居然让前辈受伤……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191126V#815F是谁在攻击！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191127V#844F刚才稍微交过手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191128V那个样子……\n',
            '恐怕是『猎兵团』中的一支部队吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010191129V#1004F猎兵团……\n',
            '那些身经百战的佣兵们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191130V#1317F#5P但、但是……\n',
            '为什么他们会！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330191131V#844F利贝尔国外\n',
            '游击士协会和猎兵团\n',
            '常因一些事情而对立……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191132V这里成为他们的靶子\n',
            '也并不奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330191133V#843F难不成……\n',
            '又是那个结社做的手脚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191134V#1020F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0134, 0x00, 0x64)
    OP_72(0x0019, 0x0020)
    OP_6F(0x0019, 0)
    OP_70(0x0019, 0x0000003C)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(40)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(40)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(40)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_323E')
    def lambda_323E():
        OP_6D(21830, 0, 13880, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_323E)

    @scena.Lambda('lambda_3256')
    def lambda_3256():
        ChrTurnDirection(0x0101, 0x000C, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3256)

    @scena.Lambda('lambda_3264')
    def lambda_3264():
        ChrTurnDirection(0x010A, 0x000C, 600)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_3264)

    @scena.Lambda('lambda_3272')
    def lambda_3272():
        ChrTurnDirection(0x000A, 0x000C, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3272)

    @scena.Lambda('lambda_3280')
    def lambda_3280():
        ChrTurnDirection(0x000B, 0x000C, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3280)

    Sleep(800)

    SetChrChipByIndex(0x000C, 17)
    OP_9F(0x000C, 0x00, 0x00, 0x00, 0x00, 0x00000000)
    SetChrFlags(0x000C, 0x0040)
    ClearChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_32AD')
    def lambda_32AD():
        OP_9F(0x000C, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_32AD)

    OP_96(0x000C, 0x000052D0, 0x00000000, 0x00003A7A, 0x000007D0, 0x00001B58)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x000C, 16)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191135V#1P#1317F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191136V#1P#1005F糟了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3329')
    def lambda_3329():
        OP_6D(21130, 0, 9590, 800)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_3329)

    SetChrChipByIndex(0x000C, 17)

    @scena.Lambda('lambda_3346')
    def lambda_3346():
        OP_8E(0x000C, 20920, 0, 10100, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3346)

    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x010A, 0x1000)
    SetChrChipByIndex(0x0101, 21)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x010A, 22)
    SetChrSubChip(0x010A, 0)

    @scena.Lambda('lambda_337F')
    def lambda_337F():
        OP_8E(0x0101, 20780, -300, 7470, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_337F)

    Sleep(100)

    @scena.Lambda('lambda_339F')
    def lambda_339F():
        OP_8E(0x010A, 21980, -300, 7530, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_339F)

    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x00000397, 0x00000000, 0x00, 0x0000, 0xFF)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_3408'),
        (0x00000000, 'loc_3415'),
        (-1, 'loc_3422'),
    )

    def _loc_3408(): pass

    label('loc_3408')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3422')

    def _loc_3415(): pass

    label('loc_3415')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3422')

    def _loc_3422(): pass

    label('loc_3422')

    EventBegin(0x00)
    OP_72(0x0019, 0x0020)
    OP_72(0x0019, 0x0008)
    OP_6F(0x0019, 60)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_344B',
    )

    OP_28(0x007F, 0x01, 0x0040)

    Jump('loc_37F7')

    def _loc_344B(): pass

    label('loc_344B')

    OP_2B(0x007E, 0x0003)
    OP_6D(21510, 0, 12500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x000B, 0x00)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, 20540, 0, 9660, 0)
    SetChrChipByIndex(0x0101, 14)
    SetChrPos(0x010A, 21750, 0, 9710, 0)
    SetChrChipByIndex(0x010A, 15)
    SetChrPos(0x000C, 21300, 0, 14260, 170)
    SetChrPos(0x000D, 21060, 0, 18750, 182)
    SetChrChipByIndex(0x000C, 27)
    SetChrSubChip(0x000C, 3)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010191137V#6P#1002F呼呼……\n',
            '总、总算是赢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191138V#815F#4P那、那边的人！\n',
            '快放下武器投降吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310191139V#2P#5P呵呵……\n',
            '比想象中的还能干呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0310191140V#2P#5P只不过在最后关头，你们太天真了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191141V#814F#4P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_360E')
    def lambda_360E():
        OP_6D(21490, 0, 14710, 1200)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_360E)

    @scena.Lambda('lambda_3626')
    def lambda_3626():
        OP_67(0, 8000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3626)

    SetChrChipByIndex(0x000D, 19)
    SetChrSubChip(0x000D, 2)
    SetChrFlags(0x000D, 0x0040)
    ClearChrFlags(0x000D, 0x0080)
    OP_96(0x000D, 0x00004F1A, 0x00000000, 0x00003B4C, 0x000007D0, 0x00001B58)
    SetChrChipByIndex(0x000D, 18)
    SetChrSubChip(0x000D, 0)
    OP_22(0x00A4, 0x00, 0x64)
    OP_99(0x000C, 0x03, 0x00, 0x00000708)
    SetChrChipByIndex(0x000C, 16)
    SetChrChipByIndex(0x000D, 28)
    SetChrFlags(0x000D, 0x0002)
    LoadEffect(0x00, 'map\\\\mp004_00.eff')
    SetChrPos(0x000E, 21290, 0, 11110, 13)

    @scena.Lambda('lambda_36B5')
    def lambda_36B5():
        OP_99(0x00FE, 0x00, 0x09, 0x000005DC)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_36B5)

    Sleep(800)

    PlayEffect(0x00, 0xFF, 0x000D, 250, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0x000E, 0, 0, 0, 0)
    Sleep(300)

    @scena.Lambda('lambda_3704')
    def lambda_3704():
        OP_6D(21360, 0, 11490, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_3704)

    Sleep(1000)

    OP_22(0x007F, 0x00, 0x64)
    Sleep(500)

    FadeOut(500, 16777215, -1)
    OP_0D()
    OP_71(0x000D, 0x0004)
    Sleep(2000)

    ChrTalk(
        0x010A,
        (
            '#0120191142V#1317F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191143V#6P#1020F发、发烟筒！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0320191144V#5P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0320191145V#5P睡吧，小猫咪们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C4(0x00, 0x00000010)
    OP_82(0x00, 0x00)
    OP_82(0x01, 0x00)
    Sleep(1000)

    FadeIn(0, 16777215)
    OP_0D()
    FadeOut(3000, 0, -1)
    OP_0D()
    OP_C4(0x01, 0x00000010)
    OP_28(0x007F, 0x01, 0x0010)

    def _loc_37F7(): pass

    label('loc_37F7')

    NewScene('ED6_DT21/C5504._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x3801
@scena.Code('func_0C_3801')
def func_0C_3801():
    EventBegin(0x01)
    OP_8C(0x0000, 174, 500)
    OP_22(0x0071, 0x00, 0x64)
    Sleep(1000)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_90(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
