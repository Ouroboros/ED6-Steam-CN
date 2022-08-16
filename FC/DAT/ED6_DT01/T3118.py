import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3118_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3118   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3118.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T3118._SN', 'ED6_DT01/T3118_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT06/CH20061._CH', 'ED6_DT06/CH20061P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '米妮亚姆医生',
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0196,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '鲁迪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '书2',
            x                   = -9560,
            z                   = 800,
            y                   = -1360,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1769479,
            chipIndex           = 7,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -9560,
            triggerZ            = 0,
            triggerY            = -1360,
            triggerRange        = 800,
            actorX              = -9560,
            actorZ              = 800,
            actorY              = -1360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1EE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1FC',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_09_2C38)

    def _loc_1FC(): pass

    label('loc_1FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_20A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(1, 0x0004)

    def _loc_20A(): pass

    label('loc_20A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_216'),
        (-1, 'loc_22E'),
    )

    def _loc_216(): pass

    label('loc_216')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 7, 0x557)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22B',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0A_3562)

    def _loc_22B(): pass

    label('loc_22B')

    Jump('loc_22E')

    def _loc_22E(): pass

    label('loc_22E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_24E',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)

    Jump('loc_455')

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_26E',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)

    Jump('loc_455')

    def _loc_26E(): pass

    label('loc_26E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2BA',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -3440, 0, -6430, 90)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -1530, 400, -6000, 0)

    Jump('loc_455')

    def _loc_2BA(): pass

    label('loc_2BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2F0',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -1530, 400, -6000, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)

    Jump('loc_455')

    def _loc_2F0(): pass

    label('loc_2F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_326',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -4680, 0, 6630, 90)

    Jump('loc_455')

    def _loc_326(): pass

    label('loc_326')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_330',
    )

    Jump('loc_455')

    def _loc_330(): pass

    label('loc_330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3AC',
    )

    ChrSetFlags(0x0008, 0x0010)
    ChrClearFlags(0x0008, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_35F',
    )

    ChrSetPos(0x0008, -5680, 0, 6400, 337)

    Jump('loc_393')

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_382',
    )

    ChrSetPos(0x0008, -1160, 0, 6790, 110)
    ChrClearFlags(0x0008, 0x0010)

    Jump('loc_393')

    def _loc_382(): pass

    label('loc_382')

    ChrSetPos(0x0008, -1160, 0, 6790, 110)

    def _loc_393(): pass

    label('loc_393')

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -6210, 0, 6890, 143)

    Jump('loc_455')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_3E2',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -6210, 0, 6890, 143)

    Jump('loc_455')

    def _loc_3E2(): pass

    label('loc_3E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_418',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, -6210, 0, 6890, 143)

    Jump('loc_455')

    def _loc_418(): pass

    label('loc_418')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_438',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)

    Jump('loc_455')

    def _loc_438(): pass

    label('loc_438')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_455',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1750, 0, 6610, 269)

    def _loc_455(): pass

    label('loc_455')

    ChrSetFlags(0x000E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_470',
    )

    ChrClearFlags(0x000E, 0x0080)

    def _loc_470(): pass

    label('loc_470')

    Return()

# id: 0x0001 offset: 0x471
@scena.Code('func_01_471')
def func_01_471():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_489',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4B6')

    def _loc_489(): pass

    label('loc_489')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4B6')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4B6(): pass

    label('loc_4B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CE',
    )

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 20)

    def _loc_4CE(): pass

    label('loc_4CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_530',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_530',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 3, 0x54B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_530',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_530(): pass

    label('loc_530')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_543',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_543(): pass

    label('loc_543')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_563',
    )

    OP_65(0x00, 0x0001)

    def _loc_563(): pass

    label('loc_563')

    Return()

# id: 0x0002 offset: 0x564
@scena.Code('func_02_564')
def func_02_564():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_579',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_564')

    def _loc_579(): pass

    label('loc_579')

    Return()

# id: 0x0003 offset: 0x57A
@scena.Code('func_03_57A')
def func_03_57A():
    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x1000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5A4',
    )

    def _loc_58C(): pass

    label('loc_58C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_58C')

    def _loc_5A1(): pass

    label('loc_5A1')

    Jump('loc_5C7')

    def _loc_5A4(): pass

    label('loc_5A4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C7',
    )

    OP_8D(0x00FE, -5120, 8029, -7290, 5400, 1000)

    Jump('loc_5A4')

    def _loc_5C7(): pass

    label('loc_5C7')

    Return()

# id: 0x0004 offset: 0x5C8
@scena.Code('func_04_5C8')
def func_04_5C8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_606',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x038A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F0',
    )

    Call(1, 0x0003)

    Jump('loc_603')

    def _loc_5F0(): pass

    label('loc_5F0')

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_603(): pass

    label('loc_603')

    Jump('loc_63D')

    def _loc_606(): pass

    label('loc_606')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_623',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵－噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63D')

    def _loc_623(): pass

    label('loc_623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_63D',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63D(): pass

    label('loc_63D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x641
@scena.Code('func_05_641')
def func_05_641():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_696',
    )

    ChrTalk(
        0x0009,
        (
            '#0050081385V#053F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_70D')

    def _loc_696(): pass

    label('loc_696')

    ChrTalk(
        0x0009,
        (
            '#0050081386V#551F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081387V#063F阿加特大哥哥………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70D(): pass

    label('loc_70D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x711
@scena.Code('func_06_711')
def func_06_711():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_B10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_781',
    )

    ChrTalk(
        0x00FE,
        (
            '#0070090156V#060F我还想在这里\n',
            '照顾一会儿阿加特大哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090157V姐姐你们要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B10')

    def _loc_781(): pass

    label('loc_781')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 4, 0x58C)),
            Expr.Return,
        ),
        'loc_84B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0070090152V#060F啊，哥哥，姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090153V阿加特大哥哥\n',
            '现在好像已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090154V#066F不过…………\n',
            '我还想在这里\n',
            '照顾一会儿阿加特大哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090155V姐姐你们要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B10')

    def _loc_84B(): pass

    label('loc_84B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x00B1, 4, 0x58C))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9B6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0070090136V#560F啊，艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090137V#000F怎么样？阿加特现在的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070090138V#060F嗯，睡得很熟。\n',
            '好像已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090139V姐姐你们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090140V#000F我们还在调查那件事。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090141V调查就交给我们，\n',
            '你就好好看着阿加特吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070090142V#060F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090143V姐姐你们也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B10')

    def _loc_9B6(): pass

    label('loc_9B6')

    ChrTalk(
        0x00FE,
        (
            '#0070090144V#560F啊，约修亚哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090145V#010F阿加特现在的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070090146V#060F嗯，睡得很熟。\n',
            '好像已经没事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090147V哥哥你们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090148V#010F现在我们正在尽全力调查。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090149V提妲你就不用担心了，\n',
            '在这里好好照顾病人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070090150V#060F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090151V哥哥你们也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B10(): pass

    label('loc_B10')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xB14
@scena.Code('func_07_B14')
def func_07_B14():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C0D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B7A',
    )

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '军队那边也不可能就这样善罢甘休。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是赶快想想\n',
            '有没有什么对策吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C0A')

    def _loc_B7A(): pass

    label('loc_B7A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '啊，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '营救作战的结果\n',
            '我也已经知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博士他们平安无事\n',
            '比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来我们也只能期待\n',
            '他们能顺利逃脱追捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C0A(): pass

    label('loc_C0A')

    Jump('loc_2BEF')

    def _loc_C0D(): pass

    label('loc_C0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_E10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 3, 0x58B)),
            Expr.Return,
        ),
        'loc_C50',
    )

    ChrTalk(
        0x00FE,
        (
            '你们要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿加特你也不要擅自行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E0D')

    def _loc_C50(): pass

    label('loc_C50')

    SetScenaFlags(ScenaFlag(0x00B1, 3, 0x58B))
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，阿加特。\n',
            '你要去哪儿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我都叮嘱过你\n',
            '要静养一段时间的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F已经没事啦，医生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '身体都变得僵硬了，\n',
            '我去稍微散个步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#053F……而且还打算做些轻量的运动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#509F散、散步……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉～阿加特。\n',
            '这是你自己说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '真是没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '你可是一名游击士，\n',
            '要为自己负起责任才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，随你的便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，千万不要勉强自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊，  \n',
            '我不会再给医生添麻烦的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '多谢你的照顾啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E0D(): pass

    label('loc_E0D')

    Jump('loc_2BEF')

    def _loc_E10(): pass

    label('loc_E10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_F47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E9A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然阿加特还没有醒过来，\n',
            '不过我想他应该已经脱离危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲那么热心地\n',
            '一直在旁边看护着他，\n',
            '真的是帮了我大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F44')

    def _loc_E9A(): pass

    label('loc_E9A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '昨天辛苦了。\n',
            '多亏了你们阿加特才能够得救。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还没有醒过来，\n',
            '不过他已经度过危险期了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在与其说是失去意识，\n',
            '不如说是在沉睡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定会很快醒过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F44(): pass

    label('loc_F44')

    Jump('loc_2BEF')

    def _loc_F47(): pass

    label('loc_F47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_FDC',
    )

    ChrTalk(
        0x00FE,
        (
            '七耀教会积累了\n',
            '上千年的传统医疗方法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '皮克塞恩教区长说不定会知道\n',
            '这种未知毒药的解毒方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想有必要去教会\n',
            '和他商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BEF')

    def _loc_FDC(): pass

    label('loc_FDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_151D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_105F',
    )

    ChrTalk(
        0x00FE,
        (
            '#2000181205V关于烟草搜查的委托\n',
            '就到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181206V虽然有些遗憾，\n',
            '不过再有什么事还请多多照顾哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_151A')

    def _loc_105F(): pass

    label('loc_105F')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1320',
    )

    OP_28(0x002C, 0x01, 0x4000)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#2000181207V据我所知，\n',
            '好像没有人受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181208V虽然案件很严重，\n',
            '不过大家都还平安无事，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181209V对了对了，说到案件，\n',
            '之前拜托你们调查烟草的那件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181210V虽然很遗憾， \n',
            '不过调查就到此为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181211V#004F咦……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000181212V被拿走的烟草\n',
            '不知道什么时候又回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181213V没有证据，\n',
            '就不能抓到犯人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181214V就是这样，\n',
            '这次就放弃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130381V#013F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181216V#007F唔～真是对不起…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181217V唉，如果能够\n',
            '早一点展开调查就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181218V#010F那么，如果还有什么事\n',
            '就再和我们联络吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000181219V嗯，到时候还请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_151A')

    def _loc_1320(): pass

    label('loc_1320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1384',
    )

    ChrTalk(
        0x00FE,
        (
            '据我所知，\n',
            '好像没有人受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然案件很严重，\n',
            '不过大家都还平安无事，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_151A')

    def _loc_1384(): pass

    label('loc_1384')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '啊，各位辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据我所知，\n',
            '好像没有人受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然案件很严重，\n',
            '不过大家都还平安无事，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_151A',
    )

    ChrTalk(
        0x0107,
        (
            '#063F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '提妲，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有哪里不舒服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#060F没、没什么事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我、我只是\n',
            '稍微发个呆而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，可不要勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许你已经有些疲劳了。\n',
            '今天就早点休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，好的。\n',
            '我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_151A(): pass

    label('loc_151A')

    Jump('loc_2BEF')

    def _loc_151D(): pass

    label('loc_151D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_18A6',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_173B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1590',
    )

    ChrTalk(
        0x00FE,
        (
            '今天辛苦你们了。\n',
            '感谢你们为我解决这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话，\n',
            '还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1738')

    def _loc_1590(): pass

    label('loc_1590')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_160E',
    )

    ChrTalk(
        0x00FE,
        (
            '#2000181229V现、现在我正在研究\n',
            '利用动物来减轻压力的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181230V别看我这么说，\n',
            '我可不是在开玩笑哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1738')

    def _loc_160E(): pass

    label('loc_160E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#2000181222V小安东尼～～～\n',
            '你很清楚犯人是谁啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181223V嗯～\n',
            '真是了不起的孩子～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '#2000181224V……啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000181225V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181226V咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181227V哎、哎呀，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181228V请问找我有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1738(): pass

    label('loc_1738')

    Jump('loc_18A3')

    def _loc_173B(): pass

    label('loc_173B')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_1857',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17CF',
    )

    ChrTalk(
        0x00FE,
        (
            '#2000181231V啊，安东尼也在一起啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181232V它肯定会给你们\n',
            '提供什么线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181233V那么，请慢走～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1854')

    def _loc_17CF(): pass

    label('loc_17CF')

    ChrTalk(
        0x00FE,
        (
            '#2000181234V带着安东尼一起去\n',
            '说不定会得到什么线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000181235V它最喜欢的新鲜牛奶\n',
            '在杂货店就可以买得到，\n',
            '你们不妨试一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1854(): pass

    label('loc_1854')

    Jump('loc_18A3')

    def _loc_1857(): pass

    label('loc_1857')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_1868',
    )

    Call(1, 0x0002)

    Jump('loc_18A3')

    def _loc_1868(): pass

    label('loc_1868')

    ChrTalk(
        0x00FE,
        (
            '唔～真是奇怪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我明明记得\n',
            '之前放在这里的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A3(): pass

    label('loc_18A3')

    Jump('loc_2BEF')

    def _loc_18A6(): pass

    label('loc_18A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_234A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1959',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18FA',
    )

    ChrTalk(
        0x00FE,
        (
            '哎，还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之先去演算室\n',
            '看一看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1956')

    def _loc_18FA(): pass

    label('loc_18FA')

    ChrTalk(
        0x00FE,
        (
            '是啊，中央工房太大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不知道想去的地方在哪里，\n',
            '就去一楼的接待处\n',
            '打听一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1956(): pass

    label('loc_1956')

    Jump('loc_2347')

    def _loc_1959(): pass

    label('loc_1959')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 2, 0x58A)),
            Expr.Return,
        ),
        'loc_19E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，调查已经完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '演算室就在五楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19DD')

    def _loc_199D(): pass

    label('loc_199D')

    ChrTalk(
        0x00FE,
        (
            '如果不知道想去的地方在哪里，\n',
            '就去一楼的接待处\n',
            '打听一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19DD(): pass

    label('loc_19DD')

    Jump('loc_2347')

    def _loc_19E0(): pass

    label('loc_19E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 1, 0x589)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FE0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x00B1, 2, 0x58A))
    SetScenaFlags(ScenaFlag(0x00B1, 2, 0x58A))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '昨天大家可都够呛呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个医务室倒还没事，\n',
            '不过其他地方就\n',
            '被弄得一塌糊涂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天早上回来的时候，\n',
            '发现安东尼睡在床上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是其他地方发生骚动，\n',
            '没有地方可以去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#505F安东尼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#560F就是那只小猫的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#560F它很早以前\n',
            '就已经住在中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1B52',
    )

    @scena.Lambda('lambda_1B4A')
    def lambda_1B4A():
        ChrTurnDirection(0x0001, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1B4A)

    def _loc_1B52(): pass

    label('loc_1B52')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1B6C',
    )

    @scena.Lambda('lambda_1B64')
    def lambda_1B64():
        ChrTurnDirection(0x0002, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1B64)

    def _loc_1B6C(): pass

    label('loc_1B6C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1B86',
    )

    @scena.Lambda('lambda_1B7E')
    def lambda_1B7E():
        ChrTurnDirection(0x0003, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1B7E)

    def _loc_1B86(): pass

    label('loc_1B86')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BA0',
    )

    @scena.Lambda('lambda_1B98')
    def lambda_1B98():
        ChrTurnDirection(0x0004, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_1B98)

    def _loc_1BA0(): pass

    label('loc_1BA0')

    ChrTurnDirection(0x0000, 0x000B, 400)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    ChrTalk(
        0x00FE,
        (
            '应该不是某户人家里养的猫，\n',
            '所以谁有兴趣谁就来照顾它了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F原来是这样啊，\n',
            '就算是大家一起养的猫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '安东尼自己\n',
            '也丝毫不在意\n',
            '成为家猫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后在别的地方碰见它，\n',
            '可要好好照顾它哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，那当然啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1CB9',
    )

    @scena.Lambda('lambda_1CB1')
    def lambda_1CB1():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1CB1)

    def _loc_1CB9(): pass

    label('loc_1CB9')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1CD3',
    )

    @scena.Lambda('lambda_1CCB')
    def lambda_1CCB():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1CCB)

    def _loc_1CD3(): pass

    label('loc_1CD3')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1CED',
    )

    @scena.Lambda('lambda_1CE5')
    def lambda_1CE5():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1CE5)

    def _loc_1CED(): pass

    label('loc_1CED')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1D07',
    )

    @scena.Lambda('lambda_1CFF')
    def lambda_1CFF():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_1CFF)

    def _loc_1D07(): pass

    label('loc_1D07')

    ChrTurnDirection(0x0000, 0x0008, 400)

    ChrTalk(
        0x00FE,
        (
            '……那么，\n',
            '安东尼也介绍过了，\n',
            '我也差不多该开始工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F4F',
    )

    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '你们不是也\n',
            '有事情要办吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F嗯，\n',
            '我们打算去五楼的演算室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '稍微有些事情要调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，到演算室？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～没问题吗……\n',
            '最近那里的设备好像一直在调整中啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '没什么，因为是精密仪器，\n',
            '所以要维持正常的机能十分不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '你们去那里看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F唔～没关系吗。\n',
            '好像气氛有一些可疑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F总之先按照医生说的\n',
            '到演算室去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '医生，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170877V#010F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好的，你们慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FDD')

    def _loc_1F4F(): pass

    label('loc_1F4F')

    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '你们不是也\n',
            '有事情要办吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F啊，对了。\n',
            '我们要去取汽油和内燃引擎设备了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那么先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好的，你们慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FDD(): pass

    label('loc_1FDD')

    Jump('loc_2347')

    def _loc_1FE0(): pass

    label('loc_1FE0')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x00B1, 2, 0x58A))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21FC',
    )

    ChrTalk(
        0x00FE,
        (
            '咦，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和拉赛尔博士见过面了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，当然。\n',
            '现在我们正在给博士帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要去演算室\n',
            '调查一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '去演算室调查一些事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～没问题吗……\n',
            '最近那里的设备好像一直在调整中啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '没什么，因为是精密仪器，\n',
            '所以要维持正常的机能十分不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '你们去那里看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔～没关系吗。\n',
            '好像气氛有一些可疑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F总之先按照医生说的\n',
            '到演算室去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '医生，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好的，你们慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2347')

    def _loc_21FC(): pass

    label('loc_21FC')

    ChrTalk(
        0x00FE,
        (
            '咦，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和拉赛尔博士见过面了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，当然。\n',
            '现在我们正在给博士帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们正准备去替博士\n',
            '拿一些研究必要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗，中央工房很大，\n',
            '不要迷路了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不知道想去的地方在哪里，\n',
            '就去一楼的接待处\n',
            '打听一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好的，多谢您的提醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么我也要工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好，我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2347(): pass

    label('loc_2347')

    Jump('loc_2BEF')

    def _loc_234A(): pass

    label('loc_234A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_2923',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_23A3',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士\n',
            '应该在三楼的工作室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想他应该\n',
            '已经开始工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2920')

    def _loc_23A3(): pass

    label('loc_23A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 1, 0x589)),
            Expr.Return,
        ),
        'loc_23F5',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '你们去找过拉赛尔博士了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博士肯定就在\n',
            '三楼的工作室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2920')

    def _loc_23F5(): pass

    label('loc_23F5')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x00B1, 1, 0x589))

    ChrTalk(
        0x00FE,
        (
            '啊，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '昨天大家可都够呛呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#065F啊，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '米妮亚姆医生这里\n',
            '没出什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '医务室倒没遇到什么麻烦，\n',
            '和平时一样一切都很正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过其他地方好像就\n',
            '被弄得一塌糊涂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天早上回来的时候，\n',
            '发现安东尼睡在床上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是其他地方发生骚动，\n',
            '没有地方可以去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#505F安东尼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#560F就是那只小猫的名字。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '它很早以前\n',
            '就已经住在中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_25E3',
    )

    @scena.Lambda('lambda_25DB')
    def lambda_25DB():
        ChrTurnDirection(0x0001, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_25DB)

    def _loc_25E3(): pass

    label('loc_25E3')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_25FD',
    )

    @scena.Lambda('lambda_25F5')
    def lambda_25F5():
        ChrTurnDirection(0x0002, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_25F5)

    def _loc_25FD(): pass

    label('loc_25FD')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2617',
    )

    @scena.Lambda('lambda_260F')
    def lambda_260F():
        ChrTurnDirection(0x0003, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_260F)

    def _loc_2617(): pass

    label('loc_2617')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2631',
    )

    @scena.Lambda('lambda_2629')
    def lambda_2629():
        ChrTurnDirection(0x0004, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_2629)

    def _loc_2631(): pass

    label('loc_2631')

    ChrTurnDirection(0x0000, 0x000B, 400)
    ChrTurnDirection(0x00FE, 0x000B, 400)

    ChrTalk(
        0x00FE,
        (
            '应该不是某户人家里养的猫，\n',
            '所以谁有兴趣谁就来照顾它了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F原来是这样啊，\n',
            '就算是大家一起养的猫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F嘿嘿，\n',
            '就～是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '安东尼自己\n',
            '也丝毫不在意\n',
            '成为家猫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后在别的地方碰见它，\n',
            '可要好好照顾它哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#001F嗯，那当然啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_275F',
    )

    @scena.Lambda('lambda_2757')
    def lambda_2757():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2757)

    def _loc_275F(): pass

    label('loc_275F')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2779',
    )

    @scena.Lambda('lambda_2771')
    def lambda_2771():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2771)

    def _loc_2779(): pass

    label('loc_2779')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2793',
    )

    @scena.Lambda('lambda_278B')
    def lambda_278B():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_278B)

    def _loc_2793(): pass

    label('loc_2793')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_27AD',
    )

    @scena.Lambda('lambda_27A5')
    def lambda_27A5():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_27A5)

    def _loc_27AD(): pass

    label('loc_27AD')

    ChrTurnDirection(0x0000, 0x0008, 400)

    ChrTalk(
        0x00FE,
        (
            '……那么，\n',
            '安东尼也介绍过了，\n',
            '我也差不多该开始工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '提妲你们\n',
            '不是也有事情要办吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，对了，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们正要去爷爷那里呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，\n',
            '拉赛尔博士应该在三楼的工作室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一大早\n',
            '就过来工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F三楼的工作室吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F那我们快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F嗯，好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '米妮亚姆医生，\n',
            '我们就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好的，你们慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003F, 0x01, 0x0040)

    def _loc_2920(): pass

    label('loc_2920')

    Jump('loc_2BEF')

    def _loc_2923(): pass

    label('loc_2923')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2B70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 0, 0x588)),
            Expr.Return,
        ),
        'loc_299B',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士\n',
            '如果也像提妲一样听话，\n',
            '就能让我省不少心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下一次的体检\n',
            '真希望他能够好好配合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B6D')

    def _loc_299B(): pass

    label('loc_299B')

    SetScenaFlags(ScenaFlag(0x00B1, 0, 0x588))
    ChrTurnDirection(0x0008, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，这不是提妲吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近拉赛尔博士身体怎么样？\n',
            '有没有哪里不舒服的感觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊，是。\n',
            '和平常一样很～健康哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，那样就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，如果他再继续保持这样\n',
            '无规律的生活习惯，肯定会出问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以防万一，回去请转告博士\n',
            '务必要来我这里\n',
            '定期检查一下身体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F啊，好的，我会转告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～拉赛尔博士\n',
            '如果也像提妲\n',
            '一样听话就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常编造各种理由\n',
            '逃避身体检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '跟小孩子一样任性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B6D(): pass

    label('loc_2B6D')

    Jump('loc_2BEF')

    def _loc_2B70(): pass

    label('loc_2B70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2BEF',
    )

    ChrTalk(
        0x00FE,
        (
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是工房附属的\n',
            '医疗技术研究所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这里也做一般的诊疗，\n',
            '要是感到身体不舒服的话就过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BEF(): pass

    label('loc_2BEF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x2BF3
@scena.Code('func_08_2BF3')
def func_08_2BF3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_2C34',
    )

    ChrTalk(
        0x00FE,
        (
            '咳、咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '还是感觉胸腔里面很不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C34(): pass

    label('loc_2C34')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x2C38
@scena.Code('func_09_2C38')
def func_09_2C38():
    EventBegin(0x00)
    CameraMove(-3770, 0, 7220, 0)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 20)
    ChrSetPos(0x0009, -1530, 400, -6000, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    FormationDelMember(0x05, 0xFF)
    ChrSetPos(0x0008, -1330, 0, -4950, 180)
    ChrSetPos(0x0107, -2140, 0, -4950, 180)
    ChrSetPos(0x0101, -3440, 0, -6060, 90)
    ChrSetPos(0x0102, 840, 0, 1080, 270)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    CameraMove(-1680, 0, -3300, 4000)

    ChrTalk(
        0x0008,
        (
            '#2000081353V#5P总之要先帮他\n',
            '做一下应急的治疗才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081354V#5P不过……\n',
            '这好像是相当特殊的神经毒药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081355V#5P一般的解毒剂是没有效果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081356V#063F#1P那、那个……\n',
            '阿加特大哥哥会怎么样呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081357V#5P像他这么健壮的人，\n',
            '应该还能撑得住……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081358V#5P不过，要是一直持续这种昏睡状态，\n',
            '还是会有生命危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081359V#069F#1P…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081360V#003F#6P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_70(0x0000, 30)
    OP_73(0x0000)
    ChrWalkTo(0x0102, -1090, 0, 930, 3000, 0x00)
    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)
    ChrWalkTo(0x0102, -3620, 0, -380, 3000, 0x00)

    @scena.Lambda('lambda_2F00')
    def lambda_2F00():
        ChrWalkTo(0x00FE, -3620, 0, -4600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2F00)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_2F3E')
    def lambda_2F3E():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_2F3E')

    DispatchAsync2(0x0101, 0x0001, lambda_2F3E)

    ChrTalk(
        0x0101,
        (
            '#0010081361V#002F#6P啊，约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F77')
    def lambda_2F77():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_2F77')

    DispatchAsync2(0x0107, 0x0001, lambda_2F77)

    @scena.Lambda('lambda_2F88')
    def lambda_2F88():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_2F88')

    DispatchAsync2(0x0008, 0x0001, lambda_2F88)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020081362V#010F#1P抱歉来迟了。\n',
            '我已经向雾香小姐报告过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081363V军队方面也拜托她通报过了，\n',
            '我想过几天应该能得到一些情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081364V#007F#6P是吗……辛苦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081365V#004F对了，金先生呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081366V#010F#1P啊……\n',
            '他和雾香姐好像是旧识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081367V我想他们之间有很多话要聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081368V#000F#6P原来是这样啊……\n',
            '说起来他们两个都是东方出身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020081369V#012F#1P那么……\n',
            '阿加特兄的情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081370V#003F#6P那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081371V#063F#5P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081372V#012F#1P是吗……\n',
            '看来还是有生命危险对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081373V#2P很遗憾，以我的知识……\n',
            '只要不知道这种毒物的具体成分，\n',
            '就没办法为这位先生解毒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081374V#2P不过……\n',
            '或许皮克塞恩教区长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081375V#064F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081376V#505F#6P皮克塞恩教区长？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0107, 0xFF)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081377V#560F#5P那、那个……\n',
            '他是蔡斯教区的神父呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3319')
    def lambda_3319():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3319)

    @scena.Lambda('lambda_3327')
    def lambda_3327():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3327)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#2000081378V#2P七耀教会积累了\n',
            '近千年的传统医疗知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081379V#2P特别是在药学方面，\n',
            '他们有各种各样的独到秘方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081380V#2P或许教会那里会有\n',
            '关于未知毒物的对应疗法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081381V#501F#6P原来是这样啊。\n',
            '以前在洛连特的教区长那里也开过药方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081382V#010F#1P看来有必要去拜访一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081383V虽然已经很晚了……\n',
            '我们还是尽快去一趟教会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081384V#062F#5P嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0042, 0x04, 0x02)
    OP_28(0x0042, 0x04, 0x04)
    OP_28(0x0042, 0x01, 0x0001)
    OP_28(0x0042, 0x01, 0x0002)
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0008, 0xFF)
    CreateThread(0x0008, 0x00, 0x00, func_02_564)
    ChrSetDirection(0x0008, 180, 0)
    ChrSetPos(0x0101, -4490, 0, -1400, 0)
    ChrSetPos(0x0102, -4490, 0, -1400, 0)
    ChrSetPos(0x0107, -4490, 0, -1400, 0)
    CameraMove(-4490, 0, -1400, 0)
    Sleep(500)

    FadeIn(1000, 0)
    MapSetFlags(0x00000800)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x3562
@scena.Code('func_0A_3562')
def func_0A_3562():
    EventBegin(0x00)
    MapClearFlags(0x10000000)
    CameraMove(-2250, 0, -130, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 20)
    ChrSetPos(0x0009, -1530, 400, -6000, 0)
    ChrSetPos(0x0008, -3660, 0, -5180, 135)
    ChrSetPos(0x0101, -1990, 0, 1000, 225)
    ChrSetPos(0x0102, -1280, 0, 1910, 225)
    ChrSetPos(0x0108, -940, 0, 820, 225)
    ChrSetPos(0x0107, -1410, 0, 160, 225)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010081577V#006F医生，让您久等了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0008, 0, 600)

    @scena.Lambda('lambda_3656')
    def lambda_3656():
        CameraMove(-2250, 0, 1000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3656)

    ChrWalkTo(0x0008, -3570, 0, -1160, 4000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#2000081578V#6P怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081579V#061F终于拿到了！\n',
            '教区长已经把药给我们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081580V#6P真的！？\n',
            '不愧是皮克塞恩教区长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -2980, 0, -520, 3000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '亚鲁福灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x0366, 1)
    ChrMoveTo(0x0101, -2440, 0, 270, 3000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#2000081581V#6P原来如此……\n',
            '是活化免疫力的药啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081582V#6P可以试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    ChrSetPos(0x0008, -1330, 0, -4950, 180)
    ChrSetPos(0x0107, -2140, 0, -4950, 180)
    ChrSetPos(0x0101, -3440, 0, -6060, 90)
    ChrSetPos(0x0102, -3430, 0, -6960, 90)
    ChrSetPos(0x0108, -3630, 0, -5030, 135)
    CameraMove(-1680, 0, -3300, 0)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#2000081583V#5P那么……\n',
            '就给他喝喝看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '米妮亚姆医生用吸管\n',
            '轻轻地往阿加特的嘴里喂亚鲁福灵药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#2000081584V#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081585V#002F#6P……（吞口水）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081586V#063F#5P……女神啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050081587V#053F#2P………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 15, 0, 300, 4000)

    ChrTalk(
        0x0009,
        (
            '#0050081588V#053F#2P……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 20, 0, 400, 4000)

    ChrTalk(
        0x0009,
        (
            '#0050081589V#056F#2P呜……呜唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 5)
    OP_9E(0x0009, 30, 0, 500, 4000)

    ChrTalk(
        0x0009,
        (
            '#0050081590V#059F#2P啊啊啊……唔啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081591V#069F#5P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081592V#002F#6P哇哇……！\n',
            '他怎么好像很痛苦啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081593V#010F#6P不要紧……\n',
            '我想，阿加特兄已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081594V#004F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081595V#070F#5P药力已经开始起效了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081596V会感到痛觉得苦就表明\n',
            '身体机能已经重新恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081597V#5P呵呵，正是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081598V#5P这下他已经脱离了\n',
            '神经毒药引起的危险昏睡状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081599V#501F#3P是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081600V#063F#5P但、但是……\n',
            '阿加特大哥哥好像很痛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081601V#5P嗯……\n',
            '至少要这样痛苦一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000081602V#5P不过不要紧，\n',
            '痛苦过后就能完全痊愈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，中毒的阿加特总算度过了危险期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '当大家放下心来之时已经是夜深了，\n',
            '艾丝蒂尔他们决定整夜轮流照看阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x00)
    OP_20(0x000003E8)
    OP_21()
    OP_77(0x70, 0x91, 0xFF, 0x00, 0x00000000)
    ChrSetSubChip(0x0009, 0)
    ChrSetPos(0x0107, -1160, 0, 6540, 90)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(-1160, 0, 6540, 0)
    OP_67(0, 6810, -10000, 0)
    CameraSetDistance(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)

    PlayBGM(83)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070081605V#064F咦，好奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081606V更换的毛巾明明放在这儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050081607V#1P呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050081608V#1P……呜啊啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0107, 255)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081609V#062F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3EAE')
    def lambda_3EAE():
        CameraMove(-1300, 0, -4950, 4500)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3EAE)

    ChrWalkTo(0x0107, -5430, 0, 5190, 5000, 0x00)
    ChrWalkTo(0x0107, -3820, 0, -4720, 5000, 0x00)
    ChrWalkTo(0x0107, -1300, 0, -4950, 5000, 0x00)
    ChrSetDirection(0x0107, 180, 400)
    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0107,
        (
            '#0070081610V#065F#5P阿、阿加特大哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081611V好、好多汗……\n',
            '得帮他擦一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050081612V#553F#2P……呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0009, 1)
    OP_0D()
    Sleep(500)

    OP_62(0x0107, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070081613V#560F#5P啊，阿加特大哥哥！\n',
            '你醒了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081614V我马上去帮你拿水……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x01, 0x03, 800)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050081615V#553F#2P米、米夏吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081616V#064F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050081617V#554F#2P太、太好了……\n',
            '……你在这啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081618V……有哥哥陪着你……\n',
            '已经……不用害怕了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081619V……所以……所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x03, 0x05, 700)
    Sleep(500)

    Fade(500)
    ChrSetSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050081620V#053F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081621V#065F#5P阿、阿加特大哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲慌张地确认阿加特的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '和先前相比，阿加特的呼吸平和了许多，\n',
            '而且还安安稳稳地睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0107,
        (
            '#0070081622V#561F#5P呼，\n',
            '太、太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081623V#066F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1600)

    OP_63(0x0107)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070081624V#063F#5P米夏……\n',
            '刚才是这么叫的吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081625V……会是……谁呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    PlaySE(13, 0x00, 0x64)
    MapSetFlags(0x00100000)
    Sleep(3000)

    SetScenaFlags(ScenaFlag(0x00AB, 0, 0x558))
    OP_28(0x0042, 0x01, 0x0200)
    MapClearFlags(0x00000800)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3102._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
