import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1121_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1121   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1121.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0002
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02380._CH', 'ED6_DT07/CH02380P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卢格兰老人',
            x                   = 180,
            z                   = 0,
            y                   = 4400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0114,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '艾丝蒂尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x29A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x29A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x29A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 130,
            triggerZ            = 0,
            triggerY            = 3000,
            triggerRange        = 600,
            actorX              = 180,
            actorZ              = 1500,
            actorY              = 4400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4470,
            triggerZ            = 0,
            triggerY            = -2690,
            triggerRange        = 1400,
            actorX              = -4470,
            actorZ              = 2000,
            actorY              = -2690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3520,
            triggerZ            = 0,
            triggerY            = -780,
            triggerRange        = 1400,
            actorX              = 3520,
            actorZ              = 2000,
            actorY              = -780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25860,
            triggerZ            = 0,
            triggerY            = 21810,
            triggerRange        = 1000,
            actorX              = 25860,
            actorZ              = 1000,
            actorY              = 21810,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_340',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_0D_2D79)

    Jump('loc_3DC')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_356',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_10_4EAC)

    Jump('loc_3DC')

    def _loc_356(): pass

    label('loc_356')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_36C',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_17_56A3)

    Jump('loc_3DC')

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_38B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(0, func_19_6C51)

    Jump('loc_3DC')

    def _loc_38B(): pass

    label('loc_38B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_3A1',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    MapSetFlags(0x10000000)
    Event(0, func_18_6310)

    Jump('loc_3DC')

    def _loc_3A1(): pass

    label('loc_3A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_3C0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    MapSetFlags(0x10000000)
    Event(0, func_1A_888E)

    Jump('loc_3DC')

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_3DC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    MapSetFlags(0x10000000)
    Event(0, func_1B_8F42)

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4D2',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_41E',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetPos(0x000B, 26770, 200, -3440, 270)

    def _loc_41E(): pass

    label('loc_41E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_44B',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x000C, 10)
    ChrSetPos(0x000C, 28510, 200, -3980, 90)

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_478',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetChipByIndex(0x000D, 11)
    ChrSetPos(0x000D, 24150, 200, -3440, 90)

    def _loc_478(): pass

    label('loc_478')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4A5',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetChipByIndex(0x000F, 12)
    ChrSetPos(0x000F, 25420, 200, -2270, 180)

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4D2',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetChipByIndex(0x0010, 13)
    ChrSetPos(0x0010, 30780, 200, -3130, 270)

    def _loc_4D2(): pass

    label('loc_4D2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_598',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_514',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetPos(0x000B, 24140, 200, -3410, 90)

    def _loc_514(): pass

    label('loc_514')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_541',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 16)
    ChrSetPos(0x000E, 26770, 200, -3440, 270)

    def _loc_541(): pass

    label('loc_541')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_56B',
    )

    ChrClearFlags(0x000F, 0x0080)
    CreateThread(0x000F, 0x00, 0x00, func_02_5E0)
    ChrSetPos(0x000F, 34230, 0, -1860, 0)

    def _loc_56B(): pass

    label('loc_56B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_598',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetChipByIndex(0x0010, 13)
    ChrSetPos(0x0010, 25420, 200, -2270, 180)

    def _loc_598(): pass

    label('loc_598')

    Return()

# id: 0x0001 offset: 0x599
@scena.Code('func_01_599')
def func_01_599():
    OP_B1('T1121_1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 2, 0x1A12)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B4',
    )

    OP_10(0x00, 0x00)
    OP_10(0x05, 0x01)

    def _loc_5B4(): pass

    label('loc_5B4')

    OP_64(0x03, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0008)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DF',
    )

    OP_65(0x03, 0x0001)

    def _loc_5DF(): pass

    label('loc_5DF')

    Return()

# id: 0x0002 offset: 0x5E0
@scena.Code('func_02_5E0')
def func_02_5E0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5F5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_5E0')

    def _loc_5F5(): pass

    label('loc_5F5')

    Return()

# id: 0x0003 offset: 0x5F6
@scena.Code('func_03_5F6')
def func_03_5F6():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x5FB
@scena.Code('func_04_5FB')
def func_04_5FB():
    TalkBegin(0x0008)
    FadeOut(300, 0, 100)

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
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_64A',
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '呼叫同伴\n'),
            TXT(0x03, '离开\n'),
        ),
    )

    Jump('loc_662')

    def _loc_64A(): pass

    label('loc_64A')

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '离开\n'),
        ),
    )

    def _loc_662(): pass

    label('loc_662')

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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_68F'),
        (0x00000001, 'loc_18A1'),
        (0x00000002, 'loc_1A21'),
        (-1, 'loc_1AE9'),
    )

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_729',
    )

    ChrTalk(
        0x0008,
        (
            '#0380480284V#632F话说回来\n',
            '到底是怎么溜进来的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380480285V就算我上了年纪也难以逃得过我的眼睛。\n',
            '看来，那家伙的确实是个厉害的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6E')

    def _loc_729(): pass

    label('loc_729')

    ChrTalk(
        0x0008,
        (
            '#0380480286V#630F噢，怎么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380480287V感觉有点不寻常，\n',
            '不知道楼上在吵闹些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480288V#1007F嗯，那个，其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向卢格兰爷爷讲述了\n',
            '布卢布兰偷偷溜进协会三楼这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0380480289V#633F什，什么！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380480290V#632F呼啊……\n',
            '竟然眼睁睁地看着被人溜进来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380480291V虽说上了年纪，\n',
            '但也是我卢格兰此生最大的败笔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_930',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480292V#055F喂喂，老爷子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480293V动肝火对身体不好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0106, 400)

    Jump('loc_988')

    def _loc_930(): pass

    label('loc_930')

    ChrTalk(
        0x0101,
        (
            '#0010480294V#1016F卢，卢格兰老爷爷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480295V不，不用\n',
            '这么自责嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    def _loc_988(): pass

    label('loc_988')

    ChrTalk(
        0x0008,
        (
            '#0380480296V#632F不行，这不只是面子问题。\n',
            '不能就此罢休。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380480297V如果不追究的话，\n',
            '协会的权威将荡然无存。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380480298V你们就算把这个柏斯翻个底朝天，\n',
            '也要把那家伙给我抓到！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480299V#1002F嗯……知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrSetDirection(0x0008, 180, 0)

    def _loc_A6E(): pass

    label('loc_A6E')

    Jump('loc_189E')

    def _loc_A71(): pass

    label('loc_A71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_F39',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF5',
    )

    ChrTalk(
        0x0008,
        (
            '#0380350258V#630F噢，是你们啊。\n',
            '发生器的设置真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350259V王都来过联络了，\n',
            '已经去过那边了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350260V#1002F没有，正准备去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350261V#1042F详细的情况不清楚，\n',
            '不过似乎是属于高度机密的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380350262V#634F噢，原来如此。\n',
            '因为这个才不能使用通信机啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350263V#632F也就是说非常重要。\n',
            '去的时候切记万事小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_C52')

    def _loc_BF5(): pass

    label('loc_BF5')

    ChrTalk(
        0x0008,
        (
            '#0380350264V#632F王都的要事……\n',
            '似乎十分紧急啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350265V去的时候务必\n',
            '多加注意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C52(): pass

    label('loc_C52')

    Jump('loc_F36')

    def _loc_C55(): pass

    label('loc_C55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D2F',
    )

    ChrTalk(
        0x0008,
        (
            '#0380350266V#630F『零力场发生器』的设置\n',
            '看来进展的很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350267V爱娜和嘉恩那边\n',
            '刚才已经通过通信机向这里发来了报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350268V虽然只剩下蔡斯一处了，\n',
            '但是未到最后绝对不可以松懈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ECE')

    def _loc_D2F(): pass

    label('loc_D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DFF',
    )

    ChrTalk(
        0x0008,
        (
            '#0380350266V#630F『零力场发生器』的设置\n',
            '看来进展的很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350270V爱娜和雾香那边\n',
            '刚才已经通过通信机向这里发来了报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350271V虽然只剩下卢安一处，\n',
            '但是未到最后绝对不可以松懈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ECE')

    def _loc_DFF(): pass

    label('loc_DFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_ECE',
    )

    ChrTalk(
        0x0008,
        (
            '#0380350266V#630F『零力场发生器』的设置\n',
            '看来进展的很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350273V嘉恩和雾香那边\n',
            '刚才已经通过通信机向这里发来了报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350274V虽然只剩下洛连特一处，\n',
            '但是未到最后绝对不可以松懈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ECE(): pass

    label('loc_ECE')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_F36')

    def _loc_ED4(): pass

    label('loc_ED4')

    ChrTalk(
        0x0008,
        (
            '#0380350275V#630F发生器的设置\n',
            '只剩下最后一处了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350276V切记未到最后绝对不可以松懈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_F36(): pass

    label('loc_F36')

    Jump('loc_189E')

    def _loc_F39(): pass

    label('loc_F39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1058',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FF1',
    )

    ChrTalk(
        0x0008,
        (
            '#0380350277V#632F『零力场发生器』的设置\n',
            '就拜托你们去完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350278V需要到达的目的地是洛连特，卢安，\n',
            '以及蔡斯的协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350279V各位路上务必小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1055')

    def _loc_FF1(): pass

    label('loc_FF1')

    ChrTalk(
        0x0008,
        (
            '#0380350277V#632F『零力场发生器』的设置\n',
            '就拜托你们去完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350279V各位路上务必小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1055(): pass

    label('loc_1055')

    Jump('loc_189E')

    def _loc_1058(): pass

    label('loc_1058')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1243',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_10E8',
    )

    ChrTalk(
        0x0008,
        (
            '#0380490557V#632F来委托工作的女人除了我们以外\n',
            '已经没有别人可依靠了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380490558V我想这工作大概不轻松，\n',
            '尽量想办法找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1240')

    def _loc_10E8(): pass

    label('loc_10E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1169',
    )

    ChrTalk(
        0x0008,
        (
            '#0380320279V#630F川蝉亭就在柏斯以南的\n',
            '瓦雷利亚湖畔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320280V从南街区出去，\n',
            '沿着安塞尔新街一直往南走就到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1240')

    def _loc_1169(): pass

    label('loc_1169')

    ChrTalk(
        0x0008,
        (
            '#0380320279V#630F川蝉亭就在柏斯以南的\n',
            '瓦雷利亚湖畔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320282V从南街区出去，\n',
            '沿着安塞尔新街一直往南走就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320283V#631F住宿那边\n',
            '我已经联系过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320284V暂时把烦恼忘记，\n',
            '悠闲的养精蓄锐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1240(): pass

    label('loc_1240')

    Jump('loc_189E')

    def _loc_1243(): pass

    label('loc_1243')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1490',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_12BD',
    )

    ChrTalk(
        0x0008,
        (
            '#0380311377V#630F迷雾峡谷的西北部\n',
            '是个人迹罕至的危险地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311378V特别要注意\n',
            '准备耐寒措施啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_148D')

    def _loc_12BD(): pass

    label('loc_12BD')

    ChrTalk(
        0x0008,
        (
            '#0380311379V#630F摩尔根将军来联络了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311380V你们是要\n',
            '去迷雾峡谷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311381V#1002F嗯，我们已经习惯在\n',
            '人数不多的情况下行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311382V#050F啊，这就是所谓的各尽其能吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380311383V#634F嗯，既然将军同意了，\n',
            '那我也不好多说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311384V#630F军队说了会提供帮助的。\n',
            '尽管放手去干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311385V#051F噢，正是这么打算的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311386V#1006F责任虽然重大，\n',
            '但会全力以赴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380311387V#631F嗯，等你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_148D(): pass

    label('loc_148D')

    Jump('loc_189E')

    def _loc_1490(): pass

    label('loc_1490')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_1632',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_150E',
    )

    ChrTalk(
        0x0008,
        (
            '#0380311388V#630F和军队碰头的地点是\n',
            '国际空港的第一飞船坪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311389V等一切都准备好，\n',
            '就可以出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_162F')

    def _loc_150E(): pass

    label('loc_150E')

    ChrTalk(
        0x0008,
        (
            '#0380311388V#630F和军队碰头的地点是\n',
            '国际空港的第一飞船坪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311391V时间还很充裕，\n',
            '提前准备好不是更好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311392V超市的商人好像在\n',
            '酒店里临时营业，\n',
            '一些琐碎的东西可以在那里买到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311393V顺便提一下，目的地第一飞船坪在\n',
            '空港上面的甲板处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311394V希望不要弄错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_162F(): pass

    label('loc_162F')

    Jump('loc_189E')

    def _loc_1632(): pass

    label('loc_1632')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_16A0',
    )

    ChrTalk(
        0x0008,
        (
            '#0380311395V#632F沿着西柏斯街道走到一个岔口向北\n',
            '就是拉文努村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311396V总之赶紧去现场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189E')

    def _loc_16A0(): pass

    label('loc_16A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 6, 0x1A0E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 7, 0x1A0F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 0, 0x1A10)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16B6',
    )

    Call(0, 0x000E)

    Jump('loc_189E')

    def _loc_16B6(): pass

    label('loc_16B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_189E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1752',
    )

    ChrTalk(
        0x0008,
        (
            '#0380311397V#630F等把所有的魔兽都消灭了，\n',
            '记得要回来这里报告啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311398V敌人各个都是十分难缠的魔兽。\n',
            '出发前务必做好充足的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189E')

    def _loc_1752(): pass

    label('loc_1752')

    ChrTalk(
        0x0008,
        (
            '#0380311399V#630F有三件事要\n',
            '委托你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311400V首先是出没于古罗尼山顶的\n',
            '『刀刃毒牙』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311401V然后是出没于琥珀之塔的\n',
            '『邪骨章鱼』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311402V最后是出没于迷雾峡谷的\n',
            '『幽灵碑文』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311403V把所有的魔兽都消灭之后，\n',
            '记得要回来这里报告啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311398V敌人各个都是十分难缠的魔兽。\n',
            '出发前务必做好充足的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_189E(): pass

    label('loc_189E')

    Jump('loc_1AE9')

    def _loc_18A1(): pass

    label('loc_18A1')

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1934',
    )

    OP_28(0x00C3, 0x04, 0x20)
    OP_A9(0x36)

    ChrTalk(
        0x0008,
        (
            '#0380311405V#630F嗯。辛苦了。\n',
            '看来任务是已经顺利完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311406V完成了什么任务的话\n',
            '再过来报告就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A1C')

    def _loc_1934(): pass

    label('loc_1934')

    If(
        (
            (Expr.Eval, "OP_A9(0x36)"),
            Expr.Return,
        ),
        'loc_19AF',
    )

    ChrTalk(
        0x0008,
        (
            '#0380311407V#630F嗯。辛苦了。\n',
            '看来任务是已经顺利完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311408V完成了什么任务的话\n',
            '再过来报告就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A1C')

    def _loc_19AF(): pass

    label('loc_19AF')

    ChrTalk(
        0x0008,
        (
            '#0380311409V#630F嗯。目前好像\n',
            '没有可以报告的工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380311410V完成了什么任务的话\n',
            '再过来报告就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A1C(): pass

    label('loc_1A1C')

    OP_56(0x00)

    Jump('loc_1AE9')

    def _loc_1A21(): pass

    label('loc_1A21')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1AE6',
    )

    ChrTalk(
        0x0008,
        (
            '#0380350282V#630F嗯。\n',
            '想要把同伴叫来是吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350283V明白了。\n',
            '我马上就联络他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '联络各支部，\n',
            '集合了待命人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()

    def _loc_1AE6(): pass

    label('loc_1AE6')

    Jump('loc_1AE9')

    def _loc_1AE9(): pass

    label('loc_1AE9')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1AED
@scena.Code('func_05_1AED')
def func_05_1AED():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ChrClearFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1B7D',
    )

    Jump('loc_1BBF')

    def _loc_1B7D(): pass

    label('loc_1B7D')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1B99',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BBF')

    def _loc_1B99(): pass

    label('loc_1B99')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BB5',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BBF')

    def _loc_1BB5(): pass

    label('loc_1BB5')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1BBF(): pass

    label('loc_1BBF')

    ExecExpressionWithValue(
        0x000B,
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
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0030271323V#020F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C60'),
        (-1, 'loc_1CA5'),
    )

    def _loc_1C60(): pass

    label('loc_1C60')

    ChrTalk(
        0x000B,
        (
            '#0030271324V#020F哎呀，要调整队伍吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C9E',
    )

    Call(0, 0x000C)

    Jump('loc_1CA2')

    def _loc_1C9E(): pass

    label('loc_1C9E')

    Call(0, 0x000B)

    def _loc_1CA2(): pass

    label('loc_1CA2')

    Jump('loc_1CFE')

    def _loc_1CA5(): pass

    label('loc_1CA5')

    ChrTalk(
        0x000B,
        (
            '#0030271325V#020F呵呵，我就在这儿\n',
            '休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271326V那么，之后就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CFE')

    def _loc_1CFE(): pass

    label('loc_1CFE')

    ChrSetSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x1D07
@scena.Code('func_06_1D07')
def func_06_1D07():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000C)
    ChrClearFlags(0x000C, 0x0010)
    ChrTurnDirection(0x000C, 0x0000, 0)

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x04,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x05,
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D97',
    )

    Jump('loc_1DD9')

    def _loc_1D97(): pass

    label('loc_1D97')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1DB3',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DD9')

    def _loc_1DB3(): pass

    label('loc_1DB3')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1DCF',
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1DD9')

    def _loc_1DCF(): pass

    label('loc_1DCF')

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.GetChrWork, 0xC, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DD9(): pass

    label('loc_1DD9')

    ExecExpressionWithValue(
        0x000C,
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
        0x000C,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000C, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0040240123V#030F呀，诸位。\n',
            '贵安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040311416V看来好像有什么事……\n',
            '不过先来一曲怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1EB4'),
        (-1, 'loc_1F20'),
    )

    def _loc_1EB4(): pass

    label('loc_1EB4')

    ChrTalk(
        0x000C,
        (
            '#0040240128V#030F呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来是需要\n',
            '我这个天才的力量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F19',
    )

    Call(0, 0x000C)

    Jump('loc_1F1D')

    def _loc_1F19(): pass

    label('loc_1F19')

    Call(0, 0x000B)

    def _loc_1F1D(): pass

    label('loc_1F1D')

    Jump('loc_1F88')

    def _loc_1F20(): pass

    label('loc_1F20')

    ChrTalk(
        0x000C,
        (
            '#0040311419V#033F呀，不要我了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040311420V#035F嗯，爱上我那动听的声音的话\n',
            '就尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F88')

    def _loc_1F88(): pass

    label('loc_1F88')

    ChrSetSubChip(0x000C, 0)
    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x1F91
@scena.Code('func_07_1F91')
def func_07_1F91():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000D)
    ChrClearFlags(0x000D, 0x0010)
    ChrTurnDirection(0x000D, 0x0000, 0)

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x04,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x05,
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xD, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2021',
    )

    Jump('loc_2063')

    def _loc_2021(): pass

    label('loc_2021')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_203D',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2063')

    def _loc_203D(): pass

    label('loc_203D')

    If(
        (
            (Expr.GetChrWork, 0xD, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2059',
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2063')

    def _loc_2059(): pass

    label('loc_2059')

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.GetChrWork, 0xD, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2063(): pass

    label('loc_2063')

    ExecExpressionWithValue(
        0x000D,
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
        0x000D,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000D, 0x0010)

    ChrTalk(
        0x000D,
        (
            '#0060231330V#040F各位，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231331V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2120'),
        (-1, 'loc_2168'),
    )

    def _loc_2120(): pass

    label('loc_2120')

    ChrTalk(
        0x000D,
        (
            '#0060231332V#040F明白了。\n',
            '要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2161',
    )

    Call(0, 0x000C)

    Jump('loc_2165')

    def _loc_2161(): pass

    label('loc_2161')

    Call(0, 0x000B)

    def _loc_2165(): pass

    label('loc_2165')

    Jump('loc_21B5')

    def _loc_2168(): pass

    label('loc_2168')

    ChrTalk(
        0x000D,
        (
            '#0060231333V#040F那我在这里待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231334V如果有事\n',
            '请尽管开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21B5')

    def _loc_21B5(): pass

    label('loc_21B5')

    ChrSetSubChip(0x000D, 0)
    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0x21BE
@scena.Code('func_08_21BE')
def func_08_21BE():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21D0',
    )

    TalkBegin(0x000F)

    Jump('loc_22C7')

    def _loc_21D0(): pass

    label('loc_21D0')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x05,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000F)
    ChrClearFlags(0x000F, 0x0010)
    ChrTurnDirection(0x000F, 0x0000, 0)

    ExecExpressionWithValue(
        0x000F,
        0x04,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x04,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xF, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x05,
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2260',
    )

    Jump('loc_22A2')

    def _loc_2260(): pass

    label('loc_2260')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_227C',
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22A2')

    def _loc_227C(): pass

    label('loc_227C')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2298',
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_22A2')

    def _loc_2298(): pass

    label('loc_2298')

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.GetChrWork, 0xF, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_22A2(): pass

    label('loc_22A2')

    ExecExpressionWithValue(
        0x000F,
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
        0x000F,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000F, 0x0010)

    def _loc_22C7(): pass

    label('loc_22C7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_231D',
    )

    ChrTalk(
        0x000F,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B4')

    def _loc_231D(): pass

    label('loc_231D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2369',
    )

    ChrTalk(
        0x000F,
        (
            '#0070271310V#060F啊、姐姐，是你们啊。\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B4')

    def _loc_2369(): pass

    label('loc_2369')

    ChrTalk(
        0x000F,
        (
            '#0070271311V#060F啊、姐姐，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23B4(): pass

    label('loc_23B4')

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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_240D'),
        (-1, 'loc_24A7'),
    )

    def _loc_240D(): pass

    label('loc_240D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_245B',
    )

    ChrTalk(
        0x000F,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_248D')

    def _loc_245B(): pass

    label('loc_245B')

    ChrTalk(
        0x000F,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_248D(): pass

    label('loc_248D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24A0',
    )

    Call(0, 0x000C)

    Jump('loc_24A4')

    def _loc_24A0(): pass

    label('loc_24A0')

    Call(0, 0x000B)

    def _loc_24A4(): pass

    label('loc_24A4')

    Jump('loc_2586')

    def _loc_24A7(): pass

    label('loc_24A7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2522',
    )

    ChrTalk(
        0x000F,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271320V#060F那我就在这里等，\n',
            '有什么事就来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2583')

    def _loc_2522(): pass

    label('loc_2522')

    ChrTalk(
        0x000F,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271322V#060F那我就在这里等，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2583(): pass

    label('loc_2583')

    Jump('loc_2586')

    def _loc_2586(): pass

    label('loc_2586')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2598',
    )

    TalkEnd(0x000F)

    Jump('loc_25A0')

    def _loc_2598(): pass

    label('loc_2598')

    ChrSetSubChip(0x000F, 0)
    TalkEnd(0x000F)

    def _loc_25A0(): pass

    label('loc_25A0')

    Return()

# id: 0x0009 offset: 0x25A1
@scena.Code('func_09_25A1')
def func_09_25A1():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x10, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x05,
        (
            (Expr.GetChrWork, 0x10, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0010)
    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    ExecExpressionWithValue(
        0x0010,
        0x04,
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x04,
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x10, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x05,
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2631',
    )

    Jump('loc_2673')

    def _loc_2631(): pass

    label('loc_2631')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_264D',
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2673')

    def _loc_264D(): pass

    label('loc_264D')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2669',
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2673')

    def _loc_2669(): pass

    label('loc_2669')

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.GetChrWork, 0x10, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2673(): pass

    label('loc_2673')

    ExecExpressionWithValue(
        0x0010,
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
        0x0010,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0010, 0x0010)

    ChrTalk(
        0x0010,
        (
            '#0080271327V#070F噢，情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2718'),
        (-1, 'loc_2757'),
    )

    def _loc_2718(): pass

    label('loc_2718')

    ChrTalk(
        0x0010,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2750',
    )

    Call(0, 0x000C)

    Jump('loc_2754')

    def _loc_2750(): pass

    label('loc_2750')

    Call(0, 0x000B)

    def _loc_2754(): pass

    label('loc_2754')

    Jump('loc_27B8')

    def _loc_2757(): pass

    label('loc_2757')

    ChrTalk(
        0x0010,
        (
            '#0080311439V#070F什么，不做调整了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080311440V那我在这里等着。\n',
            '需要的时候就说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27B8')

    def _loc_27B8(): pass

    label('loc_27B8')

    ChrSetSubChip(0x0010, 0)
    TalkEnd(0x0010)

    Return()

# id: 0x000A offset: 0x27C1
@scena.Code('func_0A_27C1')
def func_0A_27C1():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000E)
    ChrClearFlags(0x000E, 0x0010)
    ChrTurnDirection(0x000E, 0x0000, 0)

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2851',
    )

    Jump('loc_2893')

    def _loc_2851(): pass

    label('loc_2851')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_286D',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2893')

    def _loc_286D(): pass

    label('loc_286D')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2889',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2893')

    def _loc_2889(): pass

    label('loc_2889')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2893(): pass

    label('loc_2893')

    ExecExpressionWithValue(
        0x000E,
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
        0x000E,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000E, 0x0010)

    ChrTalk(
        0x000E,
        (
            '#0050271304V#051F喔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2934'),
        (-1, 'loc_296D'),
    )

    def _loc_2934(): pass

    label('loc_2934')

    ChrTalk(
        0x000E,
        (
            '#0050271305V#051F噢，知道了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000C)

    Jump('loc_29C9')

    def _loc_296D(): pass

    label('loc_296D')

    ChrTalk(
        0x000E,
        (
            '#0050271306V#052F怎么，不调整了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271307V#050F那需要我的重剑时\n',
            '尽管开口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C9')

    def _loc_29C9(): pass

    label('loc_29C9')

    ChrSetSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x29D2
@scena.Code('func_0B_29D2')
def func_0B_29D2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_29F1',
    )

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_2A2E')

    def _loc_29F1(): pass

    label('loc_29F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2A10',
    )

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['提妲'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_2A2E')

    def _loc_2A10(): pass

    label('loc_2A10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2A2E',
    )

    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_2A2E(): pass

    label('loc_2A2E')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2A82',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetPos(0x000B, 26770, 200, -3440, 270)

    def _loc_2A82(): pass

    label('loc_2A82')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2AAF',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetChipByIndex(0x000C, 10)
    ChrSetPos(0x000C, 28510, 200, -3980, 90)

    def _loc_2AAF(): pass

    label('loc_2AAF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2ADC',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetChipByIndex(0x000D, 11)
    ChrSetPos(0x000D, 24150, 200, -3440, 90)

    def _loc_2ADC(): pass

    label('loc_2ADC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B09',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetChipByIndex(0x000F, 12)
    ChrSetPos(0x000F, 25420, 200, -2270, 180)

    def _loc_2B09(): pass

    label('loc_2B09')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B36',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetChipByIndex(0x0010, 13)
    ChrSetPos(0x0010, 30780, 200, -3130, 270)

    def _loc_2B36(): pass

    label('loc_2B36')

    OP_0D()

    Return()

# id: 0x000C offset: 0x2B38
@scena.Code('func_0C_2B38')
def func_0C_2B38():
    OP_C9(
        0x01,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2BD5',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetPos(0x000B, 24140, 200, -3410, 90)

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BBA',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2BBA(): pass

    label('loc_2BBA')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BD5',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2BD5(): pass

    label('loc_2BD5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2C38',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetChipByIndex(0x000E, 16)
    ChrSetPos(0x000E, 26770, 200, -3440, 270)

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C1D',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2C1D(): pass

    label('loc_2C1D')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C38',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2C38(): pass

    label('loc_2C38')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2C98',
    )

    ChrClearFlags(0x000F, 0x0080)
    CreateThread(0x000F, 0x00, 0x00, func_02_5E0)
    ChrSetPos(0x000F, 34230, 0, -1860, 0)

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C7D',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2C7D(): pass

    label('loc_2C7D')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C98',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2C98(): pass

    label('loc_2C98')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2CFB',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetChipByIndex(0x0010, 13)
    ChrSetPos(0x0010, 25420, 200, -2270, 180)

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE0',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2CE0(): pass

    label('loc_2CE0')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CFB',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2CFB(): pass

    label('loc_2CFB')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2D78',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※要待命的成员\n',
            '　装备着『零力场发生器』。\n',
            '　将其回收加入队伍的携带品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_2D78(): pass

    label('loc_2D78')

    Return()

# id: 0x000D offset: 0x2D79
@scena.Code('func_0D_2D79')
def func_0D_2D79():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D8C',
    )

    Call(0, 0x001C)

    def _loc_2D8C(): pass

    label('loc_2D8C')

    CameraMove(590, 0, 3270, 0)
    OP_67(0, 5580, -10000, 0)
    CameraSetDistance(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -460, 0, 2350, 0)
    ChrSetPos(0x000E, 610, 0, 2350, 0)
    ChrSetPos(0x000F, -430, 0, 1300, 0)
    ChrSetPos(0x000D, -1300, 0, 1150, 0)
    ChrSetPos(0x000B, 820, 0, 1410, 0)
    ChrSetPos(0x000C, -1020, 0, 200, 0)
    ChrSetPos(0x0010, 400, 0, 300, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    OP_4A(0x0008, 255)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetChipByIndex(0x000D, 5)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetChipByIndex(0x0010, 8)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0380300572V#631F呀～从洛连特特意赶来，\n',
            '真的辛苦你们了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300573V#633F而且……\n',
            '除了『不动』，『银闪』，『重剑』之外，\n',
            '还有前途无量的游击士新人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300574V哈哈，怎么说也是相当豪华的阵容啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300575V#1004F前途无量的游击士新人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300576V#631F哈哈，说的就是你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300577V连续破坏『结社』在四个地方所布设的阴谋，\n',
            '突然出现的游击士新星。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300578V像这样的赞美之言，时常可以听到的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300579V#1019F真，真是的，开玩笑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300580V#1007F破坏阴谋什么的，\n',
            '其实我还没有到达那么厉害的程度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300581V况且那些家伙每次做完实验之后，\n',
            '都被他们轻松地逃掉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 315, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0030300582V#021F#2P不过，对于洛连特事件的处理，\n',
            '你不是干的很出色吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300583V#027F我觉得挺值得自豪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300584V#1013F#5P那，那是……\n',
            '其实应该是连串的巧合……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080300585V#071F哈哈，害羞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300586V关键是只要能够做出\n',
            '符合别人评价的工作就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300587V#1007F#5P真是的，不要说的那么简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300588V#1002F先不说这些了……\n',
            '柏斯的情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3282')
    def lambda_3282():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3282)

    Sleep(10)

    ChrSetDirection(0x0010, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0380300589V#630F嗯，到目前还没发生\n',
            '被认为是与『结社』有关的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300590V自从发生了那起抢夺空贼艇事件之后，\n',
            '军队的警戒变得严密了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300591V#634F至于怪事的话……\n',
            '也就是通缉魔兽的数量在增加之类的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300592V#555F#4P呼……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300593V#1015F总感觉柏斯这里的通缉魔兽\n',
            '比其他地方要多呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300594V以前来的时候也是这样，\n',
            '难道有什么特别的原因吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300595V#634F柏斯地区原本就很广阔，\n',
            '四面都是险要地形。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300596V那些地方经常会有凶暴的魔兽跳出来……\n',
            '所以魔兽数量多也不奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300597V#632F话说回来，\n',
            '本月以来已经收到了十起报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030300598V#023F这可真多啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300599V#020F斯丁克最近表现不错吧，\n',
            '我听说很努力地工作来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300600V#630F嗯，此外克鲁茨他们\n',
            '前些日子来的时候顺便去\n',
            '消灭了几只魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300601V但是又有几只出现了，要是可以的话，\n',
            '我们柏斯支部也希望你们能够帮下忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080300602V#074F嗯……\n',
            '帮帮忙比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300603V#072F凶暴魔兽的数量在继续增加……\n',
            '这或许与『结社』有关联也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300604V#1006F嗯嗯，置之不理的话会很危险的，\n',
            '现在还是把剿灭的任务摆在优先的位置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300605V#552F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000E, 400)

    ChrTalk(
        0x000F,
        (
            '#0070300606V#064F#6P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300607V阿加特哥哥。\n',
            '出什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3740')
    def lambda_3740():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3740)

    Sleep(50)

    @scena.Lambda('lambda_3753')
    def lambda_3753():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3753)

    Sleep(50)

    @scena.Lambda('lambda_3766')
    def lambda_3766():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3766)

    Sleep(50)

    @scena.Lambda('lambda_3779')
    def lambda_3779():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3779)

    Sleep(50)

    ChrTurnDirection(0x0010, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300608V#1004F啊，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300609V#053F#4P不……没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000F, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0050300610V#051F#5P总之，现在的工作就是\n',
            '先把已经知道的通缉魔兽全部剿灭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlaySE(113, 0x00, 0x64)
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(300)

    ChrSetPos(0x0009, -4500, 0, -9720, 0)
    ChrSetPos(0x0009, -930, 0, -7000, 0)

    NpcTalk(
        0x0009,
        '女性的声音',
        (
            '#0360300611V#5P……失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000F, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0010, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetPos(0x0009, -500, 0, -7000, 0)
    ChrSetPos(0x000A, -500, 0, -7000, 0)
    ChrClearFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_3971')
    def lambda_3971():
        CameraMove(800, 0, 800, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3971)

    @scena.Lambda('lambda_3989')
    def lambda_3989():
        ChrWalkTo(0x00FE, -490, 0, -1730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3989)

    @scena.Lambda('lambda_39A4')
    def lambda_39A4():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_39A4)

    @scena.Lambda('lambda_39B2')
    def lambda_39B2():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_39B2)

    @scena.Lambda('lambda_39C0')
    def lambda_39C0():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_39C0)

    @scena.Lambda('lambda_39CE')
    def lambda_39CE():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_39CE)

    @scena.Lambda('lambda_39DC')
    def lambda_39DC():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_39DC)

    @scena.Lambda('lambda_39EA')
    def lambda_39EA():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_39EA)

    @scena.Lambda('lambda_39F8')
    def lambda_39F8():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_39F8)

    Sleep(500)

    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_3A10')
    def lambda_3A10():
        ChrWalkTo(0x00FE, 330, 0, -2400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3A10)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010300612V#1018F#5P梅贝尔市长……\n',
            '还有莉拉小姐！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360300613V#611F#6P呵呵，你好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300614V艾丝蒂尔。\n',
            '终于又见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0370300615V#621F……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300616V#1008F#5P哇～真是好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300617V好像是从诞辰庆典以后就没见过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360300618V#611F#6P是啊，是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300619V但在很多地方都能听到\n',
            '关于艾丝蒂尔的传闻呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300620V#610F其余的各位也好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300621V科洛丝……\n',
            '学校已经放假了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300622V#045F#5P不是呢，\n',
            '其实是不久前刚刚休学。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300623V#048F看来梅贝尔前辈和莉拉小姐最近都过得很不错，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300624V#1004F#5P梅贝尔……前辈？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 90, 400)

    ChrTalk(
        0x000D,
        (
            '#0060300625V#542F#6P啊，她是我的前辈啊。\n',
            '王立学院的高材生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360300626V#611F#6P呵呵，这里又不是公众场合，\n',
            '炫耀炫耀也无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300627V#1016F#5P啊哈哈，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#0360300628V#610F#6P还有……\n',
            '阿加特·科洛斯纳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300629V好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300630V#552F#5P……是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300631V#1004F#6P咦，市长\n',
            '认识阿加特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360300632V#610F#6P曾数次委托于他，\n',
            '受了他不少照顾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300633V此外１０年前……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300634V#555F#5P喂喂……我说小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#0360300635V#615F#6P抱歉……失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300636V#610F今天我听说\n',
            '大家都在，\n',
            '特意过来打声招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300637V听说你在四处追捕\n',
            '在王国全范围内引起骚乱的国际犯罪组织，\n',
            '对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300638V#1015F#5P国，国际犯罪组织……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030300639V#022F#5P虽然稍微有点出入，\n',
            '但这么说也没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360300640V#612F#6P我们柏斯市的立场是无论如何\n',
            '也不允许有这样的犯罪组织存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300641V所以，请让我们\n',
            '尽可能地参与协助你们的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300642V#1006F#5P嗯，到那时候就\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300643V#051F#5P哼……\n',
            '不过，我倒是期待你的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360300644V#615F#6P那么，我们\n',
            '就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300645V#611F若是有什么事的话，\n',
            '请来市长官邸找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0370300646V#620F……告辞。（鞠躬）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4151')
    def lambda_4151():
        CameraMove(10, 0, -1540, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4151)

    ChrSetDirection(0x0009, 180, 400)

    @scena.Lambda('lambda_4170')
    def lambda_4170():
        ChrWalkTo(0x00FE, -520, 0, -6500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4170)

    Sleep(800)

    ChrSetDirection(0x000A, 270, 400)
    ChrSetDirection(0x000A, 180, 400)

    @scena.Lambda('lambda_419E')
    def lambda_419E():
        ChrWalkTo(0x00FE, -520, 0, -6500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_419E)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_41C3')
    def lambda_41C3():
        ChrWalkTo(0x00FE, -600, 0, -7190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_41C3)

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 500)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0080)
    WaitForThreadExit(0x000A, 0x0001)
    ChrSetFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_41FD')
    def lambda_41FD():
        ChrWalkTo(0x00FE, -600, 0, -7190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_41FD)

    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 500)
    ChrSetFlags(0x000A, 0x0080)
    PlaySE(7, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_4237')
    def lambda_4237():
        CameraMove(590, 0, 3270, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4237)

    Sleep(1000)

    @scena.Lambda('lambda_4254')
    def lambda_4254():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4254)

    Sleep(50)

    @scena.Lambda('lambda_4267')
    def lambda_4267():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4267)

    Sleep(100)

    @scena.Lambda('lambda_427A')
    def lambda_427A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_427A)

    Sleep(50)

    @scena.Lambda('lambda_428D')
    def lambda_428D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_428D)

    Sleep(100)

    @scena.Lambda('lambda_42A0')
    def lambda_42A0():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_42A0)

    Sleep(50)

    @scena.Lambda('lambda_42B3')
    def lambda_42B3():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_42B3)

    Sleep(100)

    ChrSetDirection(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0380300647V#634F哎呀，阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300648V#632F我说你啊，\n',
            '就不能稍微热情点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300649V#552F#4P抱歉，本性如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300650V况且我是个从事国民安全的游击士。\n',
            '在这一点上就别计较那么多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300651V#1015F#6P嗯，的确是啊……\n',
            '不管对谁，阿加特总是给人一种很傲慢的态度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300652V尽管这样，但我觉得\n',
            '阿加特那种专业的工作态度反而让人感到敬畏呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300653V话说回来，刚才看市长姐姐望着阿加特的神情，\n',
            '感觉到他们之间好像有点隔阂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000E, 400)

    ChrTalk(
        0x000F,
        (
            '#0070300654V#063F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300655V#053F#4P啊？是错觉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300656V#050F别琢磨这些了，\n',
            '我们还是快点剿灭通缉的魔兽吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300657V老爷子，一口气告诉我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0380300658V#630F嗯……\n',
            '目前需要剿灭的通缉魔兽有三个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS130._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    FadeOut(0, 0, -1)
    OP_0D()
    ChrSetDirection(0x000F, 0, 0)
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('卢格兰老人')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0380300659V#634F首先是出没于古罗尼山顶的\n',
            '『刀刃毒牙』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS132._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('卢格兰老人')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0380300660V#632F然后是出没于迷雾峡谷的\n',
            '『幽灵碑文』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS131._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('卢格兰老人')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0380300661V#634F最后是出没于琥珀之塔的\n',
            '『邪骨章鱼』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(0, 0)
    OP_0D()
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010300662V#1006F嗯……\n',
            '已经仔细记下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 225, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0050300663V#050F#5P好。说到剿灭魔兽，\n',
            '就是轮到我的『重剑』出场的时候吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300664V这次就让我来处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_47F2')
    def lambda_47F2():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_47F2)

    Sleep(100)

    @scena.Lambda('lambda_4805')
    def lambda_4805():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4805)

    Sleep(50)

    @scena.Lambda('lambda_4818')
    def lambda_4818():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4818)

    Sleep(50)

    @scena.Lambda('lambda_482B')
    def lambda_482B():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_482B)

    Sleep(100)

    ChrTurnDirection(0x0010, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300665V#1004F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030300666V#027F柏斯地区\n',
            '就是你的故乡呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300667V这次的任务交给你再适合不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080300668V#070F啊，我也没意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050300669V#053F#5P呵，就这么定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 270, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0050300670V#051F#2P那么，艾丝蒂尔。\n',
            '赶紧来挑选队员吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300671V#1019F#6P呼，看来真的要强行入队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_28(0x00B1, 0x04, 0x02)
    OP_28(0x00B1, 0x04, 0x04)
    OP_28(0x00B1, 0x04, 0x08)
    OP_28(0x00B2, 0x04, 0x02)
    OP_28(0x00B2, 0x04, 0x04)
    OP_28(0x00B2, 0x04, 0x08)
    OP_28(0x00B3, 0x04, 0x02)
    OP_28(0x00B3, 0x04, 0x04)
    OP_28(0x00B3, 0x04, 0x08)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1101._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x4AA1
@scena.Code('func_0E_4AA1')
def func_0E_4AA1():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4AC2',
    )

    Call(0, 0x001D)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_4AC2(): pass

    label('loc_4AC2')

    Fade(1000)
    CameraMove(310, 0, 3460, 0)
    OP_67(0, 7010, -10000, 0)
    CameraSetDistance(2680, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -710, 0, 2340, 0)
    ChrSetPos(0x0106, 470, 0, 2350, 0)
    ChrSetPos(0x00F8, -680, 0, 1160, 0)
    ChrSetPos(0x00F9, 440, 0, 1140, 0)
    OP_4A(0x0008, 255)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300796V#1018F我回来了，卢格兰爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300797V#051F#4P通缉魔兽全部消灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300798V#631F#5P噢，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300799V#630F那么先把\n',
            '这次的报酬付给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0093, 0x04, 0x10)
    OP_AF(0x36, 0x0093)
    OP_28(0x00B1, 0x04, 0x10)
    OP_28(0x00B2, 0x04, 0x10)
    OP_28(0x00B3, 0x04, 0x10)
    OP_28(0x00B1, 0x04, 0x20)
    OP_28(0x00B2, 0x04, 0x20)
    OP_28(0x00B3, 0x04, 0x20)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0380300800V#630F#5P嗯嗯，\n',
            '看来确实是把凶猛的魔兽都剿灭了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300801V#1007F嗯～～关于魔兽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300802V#1002F有一件事让我稍微有点在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300803V#633F#5P啊？在意的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300804V#552F#4P啊，其实是──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0342, 2, 0x1A12))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x4D3E
@scena.Code('func_0F_4D3E')
def func_0F_4D3E():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4D77',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4D77(): pass

    label('loc_4D77')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4DC4',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DAC',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_4DC4')

    def _loc_4DAC(): pass

    label('loc_4DAC')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4DC4(): pass

    label('loc_4DC4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4E39',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DF9',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_4E39')

    def _loc_4DF9(): pass

    label('loc_4DF9')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E21',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_4E39')

    def _loc_4E21(): pass

    label('loc_4E21')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4E39(): pass

    label('loc_4E39')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4E86',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E6E',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_4E86')

    def _loc_4E6E(): pass

    label('loc_4E6E')

    FormationAddMember(ChrTable['科洛丝'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4E86(): pass

    label('loc_4E86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4EAB',
    )

    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_4EAB(): pass

    label('loc_4EAB')

    Return()

# id: 0x0010 offset: 0x4EAC
@scena.Code('func_10_4EAC')
def func_10_4EAC():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EC4',
    )

    Call(0, 0x001D)
    Sleep(100)

    def _loc_4EC4(): pass

    label('loc_4EC4')

    CameraMove(310, 0, 3460, 0)
    OP_67(0, 7010, -10000, 0)
    CameraSetDistance(2680, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -710, 0, 2340, 0)
    ChrSetPos(0x0106, 470, 0, 2350, 0)
    ChrSetPos(0x00F8, -680, 0, 1160, 0)
    ChrSetPos(0x00F9, 440, 0, 1140, 0)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0380300823V#632F#5P嗯，魔兽有时会恐慌，\n',
            '有时又变得更加凶暴吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300824V确实是件很奇怪的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300825V#1002F嗯，挺让人害怕的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010300826V#1015F对了，阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300827V你好像说过之前在柏斯地区\n',
            '也发生过类似的事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300828V#633F#5P喔，有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300829V#053F#4P啊……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300830V#050F那是老爷子来柏斯之前的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300831V#1004F咦～卢格兰爷爷\n',
            '以前不住在这里的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300832V#630F#5P嗯，我是在百日战役结束之后\n',
            '才来柏斯任职的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300833V#634F过去利贝尔只在格兰赛尔有\n',
            '游击士协会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300834V各地建立起支部那是\n',
            '战争结束以后的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300835V#630F顺便说一下，直到１０年以前，\n',
            '我一直都在王都支部担任接待的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300836V#1006F咦～是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300837V#552F#4P……在那场『百日战役』即将爆发的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300838V魔兽的样子变得\n',
            '越来越古怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 500)

    ChrTalk(
        0x0101,
        (
            '#0010300839V#1004F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300840V#632F#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_20(0x00000000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(136, 0x00, 0x64)
    OP_7C(0, 400, 5000, 1500)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_538E',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_53CC')

    def _loc_538E(): pass

    label('loc_538E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53B5',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_53CC')

    def _loc_53B5(): pass

    label('loc_53B5')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_53CC(): pass

    label('loc_53CC')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53F8',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5436')

    def _loc_53F8(): pass

    label('loc_53F8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_541F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5436')

    def _loc_541F(): pass

    label('loc_541F')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5436(): pass

    label('loc_5436')

    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0380300841V#633F#5P什，什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300842V#1020F刚，刚才那震动是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 180, 600)
    Sleep(300)

    ChrTalk(
        0x0106,
        (
            '#0050300843V#054F#5P外面……快去看看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT21/T1103._SN', 110, 0, 0)
    IdleLoop()
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x54FF
@scena.Code('func_11_54FF')
def func_11_54FF():
    OP_7C(50, 50, 1500, 500)
    Sleep(500)

    OP_7C(100, 100, 1000, 500)
    Sleep(500)

    OP_7C(200, 200, 1000, 500)
    Sleep(500)

    OP_7C(100, 100, 500, 500)
    Sleep(500)

    OP_7C(50, 50, 250, 500)
    Sleep(500)

    OP_7C(10, 10, 125, 500)
    Sleep(500)

    Return()

# id: 0x0012 offset: 0x5584
@scena.Code('func_12_5584')
def func_12_5584():
    PlaySE(133, 0x01, 0x64)
    Sleep(2000)

    OP_24(0x0085, 0x5F)
    Sleep(100)

    OP_24(0x0085, 0x5A)
    Sleep(100)

    OP_24(0x0085, 0x55)
    Sleep(100)

    OP_24(0x0085, 0x50)
    Sleep(100)

    OP_24(0x0085, 0x4B)
    Sleep(100)

    OP_24(0x0085, 0x46)
    Sleep(100)

    OP_24(0x0085, 0x41)
    Sleep(100)

    OP_24(0x0085, 0x32)
    Sleep(100)

    OP_24(0x0085, 0x37)
    Sleep(100)

    OP_24(0x0085, 0x32)
    OP_23(0x0085)

    Return()

# id: 0x0013 offset: 0x55E7
@scena.Code('func_13_55E7')
def func_13_55E7():
    ChrWalkTo(0x00FE, 1750, 0, 1460, 5000, 0x00)
    ChrWalkTo(0x00FE, -630, 0, -6540, 5000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0x5620
@scena.Code('func_14_5620')
def func_14_5620():
    ChrWalkTo(0x00FE, -2020, 0, 1450, 5000, 0x00)
    ChrWalkTo(0x00FE, -630, 0, -6540, 5000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x5659
@scena.Code('func_15_5659')
def func_15_5659():
    ChrWalkTo(0x00FE, -630, 0, -6540, 5000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0016 offset: 0x567E
@scena.Code('func_16_567E')
def func_16_567E():
    ChrWalkTo(0x00FE, -630, 0, -6540, 5000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 200)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0017 offset: 0x56A3
@scena.Code('func_17_56A3')
def func_17_56A3():
    EventBegin(0x00)
    CameraMove(160, 0, 3130, 0)
    OP_67(0, 7040, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -600, 0, 2340, 0)
    ChrSetPos(0x000B, 720, 0, 2340, 0)
    ChrSetPos(0x000D, -220, 0, 1580, 0)
    ChrSetPos(0x000F, -1290, 0, 890, 0)
    ChrSetPos(0x000C, -20, 0, 520, 0)
    ChrSetPos(0x0010, 1110, 0, 1360, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetChipByIndex(0x000D, 5)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetChipByIndex(0x0010, 8)
    OP_4A(0x0008, 255)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0380300936V#634F#5P……总之\n',
            '辛苦各位了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300937V#632F驻扎在哈肯大门的王国军部队\n',
            '很快就会赶来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300938V柏斯超市的管理和防护\n',
            '就交给他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300939V#1007F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300940V#1003F不过，\n',
            '没想到敌人中竟然会有那种怪物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300941V而且那个洛伦斯少尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030300942V#026F#4P执行者ＮＯ．Ⅱ。\n',
            '『剑帝』莱恩哈特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300943V#022F也被称为『莱维』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040300944V#035F#4P哼……\n',
            '看来真正的身份终于显露出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060300945V#049F#6P在格兰赛尔城相遇的时候，\n',
            '也没有料到他竟然会是个\n',
            '做出这么过分的事的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080300946V#072F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070300947V#063F#6P那，那个，卢格兰爷爷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300948V阿加特哥哥\n',
            '还没有消息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300949V#634F#5P嗯……很遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300950V#632F那个鲁莽的阿加特……\n',
            '到底去搞些什么了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(195, 0x01, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0070300951V#064F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_5B08')
    def lambda_5B08():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5B08)

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300952V#1025F#6P难道说……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5B3E')
    def lambda_5B3E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_5B3E')

    DispatchAsync2(0x0101, 0x0001, lambda_5B3E)

    @scena.Lambda('lambda_5B4F')
    def lambda_5B4F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_5B4F')

    DispatchAsync2(0x000D, 0x0001, lambda_5B4F)

    @scena.Lambda('lambda_5B60')
    def lambda_5B60():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_5B60')

    DispatchAsync2(0x000B, 0x0001, lambda_5B60)

    @scena.Lambda('lambda_5B71')
    def lambda_5B71():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_5B71')

    DispatchAsync2(0x000C, 0x0001, lambda_5B71)

    @scena.Lambda('lambda_5B82')
    def lambda_5B82():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_5B82')

    DispatchAsync2(0x000F, 0x0001, lambda_5B82)

    @scena.Lambda('lambda_5B93')
    def lambda_5B93():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_5B93')

    DispatchAsync2(0x0010, 0x0001, lambda_5B93)

    @scena.Lambda('lambda_5BA4')
    def lambda_5BA4():
        CameraMove(1160, 0, 4059, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5BA4)

    ChrWalkTo(0x0008, 1940, 0, 4690, 1500, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0101, 0x0002)
    OP_23(0x00C3)
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0010, 0x01)

    ChrTalk(
        0x0008,
        (
            '#0380300953V#632F#6P这里是游击士协会\n',
            '所属柏斯支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300954V#633F噢，是你啊。\n',
            '到底怎么了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300955V………………………………\n',
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300956V#632F……什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300957V#1026F#6P（怎，怎么回事……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030300958V#022F（这气氛……好像出什么大事了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300959V#634F#6P嗯，明白了。\n',
            '我这里马上派游击士过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300960V#632F嗯，嗯，请打起精神来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x01, 0x00)
    Sleep(500)

    ChrTurnDirection(0x0008, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0380300961V#632F#5P……刚才……拉文努村莱森村长\n',
            '传达了一些信息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300962V就在刚刚，\n',
            '那条龙袭击了拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300963V#1002F#3S#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030300964V#024F#4P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380300965V#634F#5P据说龙把果树园烧毁之后，\n',
            '很快就离开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380300966V#632F在那之后，阿加特出现并加入\n',
            '到了灭火行动中，但是现在他…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300967V#1005F#6P知道了！\n',
            '我们马上去看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)
    OP_62(0x000F, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0070300968V#065F#6P姐，姐姐！\n',
            '也带我去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231039V#1004F#6P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5FF3')
    def lambda_5FF3():
        CameraMove(860, 0, 2860, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5FF3)

    @scena.Lambda('lambda_600B')
    def lambda_600B():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_600B)

    Sleep(50)

    @scena.Lambda('lambda_601E')
    def lambda_601E():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_601E)

    Sleep(50)

    @scena.Lambda('lambda_6031')
    def lambda_6031():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6031)

    Sleep(50)

    @scena.Lambda('lambda_6044')
    def lambda_6044():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6044)

    Sleep(50)

    ChrTurnDirection(0x000C, 0x000F, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000F,
        (
            '#0070300970V#062F#6P对手假如是在空中飞的龙的话，\n',
            '我觉得导力炮能派上用场……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300971V再加上……再加上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300972V#1025F#5P……嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300973V不过……\n',
            '切记不可以胡来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070300974V#560F#6P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['提妲'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_0D()
    Sleep(200)

    CameraMove(-500, 0, -720, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -500, 0, -720, 180)
    ChrSetPos(0x0107, -500, 0, -720, 180)
    ChrSetPos(0x00F8, -500, 0, -720, 180)
    ChrSetPos(0x00F9, -500, 0, -720, 180)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetPos(0x0008, 180, 0, 4400, 180)
    OP_69(0x0000, 0)
    OP_4B(0x0008, 255)
    OP_10(0x00, 0x00)
    OP_10(0x05, 0x01)
    OP_28(0x007A, 0x04, 0x40)
    OP_28(0x0094, 0x04, 0x02)
    OP_28(0x0094, 0x04, 0x08)
    OP_28(0x0094, 0x01, 0x0001)
    OP_28(0x00B1, 0x04, 0x10)
    OP_28(0x00B1, 0x04, 0x20)
    OP_28(0x00B2, 0x04, 0x10)
    OP_28(0x00B2, 0x04, 0x20)
    OP_28(0x00B3, 0x04, 0x10)
    OP_28(0x00B3, 0x04, 0x20)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x6310
@scena.Code('func_18_6310')
def func_18_6310():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6327',
    )

    Call(0, 0x001C)
    Call(0, 0x001E)

    def _loc_6327(): pass

    label('loc_6327')

    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    CameraMove(40, 0, 3020, 0)
    OP_67(0, 7560, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -590, 0, 2340, 0)
    ChrSetPos(0x000B, 520, 0, 2350, 0)
    ChrSetPos(0x000D, -1690, 0, 1980, 0)
    ChrSetPos(0x000C, -980, 0, 1100, 0)
    ChrSetPos(0x0010, 250, 0, 1100, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetChipByIndex(0x000D, 5)
    ChrSetChipByIndex(0x0010, 8)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    OP_4A(0x0008, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310001V#1017F是吗，\n',
            '超市的修复工程已经开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310002V#021F#4P明明只过了短短几天，　\n',
            '准备的可真周到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380310003V#631F嗯，\n',
            '梅贝尔市长非常的努力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380310004V#630F发放给拉文努村的救援物资\n',
            '也已经运送过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380310005V大家虽然心怀不安，\n',
            '但都在很努力地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 90, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0060310006V#047F#6P已经和王都取得了联系，\n',
            '就在昨晚，\n',
            '祖母大人她发表了声明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310007V#040F声明内容包括迅速对龙采取的对策，\n',
            '以及向被害地区提供援助的保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    @scena.Lambda('lambda_65E0')
    def lambda_65E0():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_65E0)

    @scena.Lambda('lambda_65EE')
    def lambda_65EE():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_65EE)

    @scena.Lambda('lambda_65FC')
    def lambda_65FC():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_65FC)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310008V#1001F#5P是吗，不愧是女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040310009V#035F呵呵，\n',
            '真希望帝国的大人物们也好好学习王国的处事手法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040310010V毕竟比起安抚民众，\n',
            '政党的人发挥团体的精神才更为重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080310011V#075F不过，要这么说的话，\n',
            '共和国也是如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310012V相互太过在意权势，\n',
            '使得工作中难以放开手脚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060310013V#045F#6P呵呵……过奖了，各位。\n',
            '这或许是小国所特有的优势也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060310014V#048F不管怎样……\n',
            '我认为我们已经做好了\n',
            '对付龙的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310015V#1006F#5P那就让我们先\n',
            '见识见识王国军的实力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    @scena.Lambda('lambda_6825')
    def lambda_6825():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6825)

    @scena.Lambda('lambda_6833')
    def lambda_6833():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6833)

    @scena.Lambda('lambda_6841')
    def lambda_6841():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6841)

    @scena.Lambda('lambda_684F')
    def lambda_684F():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_684F)

    ChrTalk(
        0x0101,
        (
            '#0010310016V#1015F那个，我们\n',
            '只要去国际空港就好了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380310017V#631F嗯，没错。\n',
            '上午10点，在第一飞船坪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380310018V现在是9点左右，\n',
            '还有一点时间可以去买东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310019V#1006F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310020V#023F#4P可是，\n',
            '柏斯超市还没有恢复营业吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380310021V#630F超市的商人\n',
            '现在在酒店里避难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380310022V不过他们同时好像也在做买卖，\n',
            '买东西去那里就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310023V#021F#4P呵呵，原来这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080310024V#070F在去空港之前，\n',
            '去那里逛一下，准备一下随身物资也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6A92',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6A92(): pass

    label('loc_6A92')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6ADF',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AC7',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_6ADF')

    def _loc_6AC7(): pass

    label('loc_6AC7')

    FormationAddMember(ChrTable['奥利维尔'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6ADF(): pass

    label('loc_6ADF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6B2C',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B14',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    Jump('loc_6B2C')

    def _loc_6B14(): pass

    label('loc_6B14')

    FormationAddMember(ChrTable['科洛丝'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6B2C(): pass

    label('loc_6B2C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6B51',
    )

    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_6B51(): pass

    label('loc_6B51')

    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    CameraMove(20, 0, -430, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 20, 0, -430, 185)
    ChrSetPos(0x0001, 20, 0, -430, 185)
    ChrSetPos(0x0002, 20, 0, -430, 185)
    ChrSetPos(0x0003, 20, 0, -430, 185)
    ChrSetPos(0x0004, 20, 0, -430, 185)
    ChrSetPos(0x0005, 20, 0, -430, 185)
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x0343, 4, 0x1A1C))
    OP_28(0x0095, 0x04, 0x02)
    OP_28(0x0095, 0x04, 0x08)
    OP_28(0x0095, 0x01, 0x0001)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x6C51
@scena.Code('func_19_6C51')
def func_19_6C51():
    EventBegin(0x00)
    OP_D6(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6C66',
    )

    Call(0, 0x001C)

    def _loc_6C66(): pass

    label('loc_6C66')

    OP_4A(0x0008, 255)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0000, 510, 0, 1930, 270)
    ChrSetPos(0x000E, 1260, 0, 2020, 270)
    ChrSetPos(0x000F, 1140, 0, 1100, 270)
    ChrSetPos(0x0010, -1350, 0, 2000, 90)
    ChrSetPos(0x000B, -1080, 0, 940, 90)
    ChrSetPos(0x0011, 140, 0, 2350, 90)
    ChrSetPos(0x000D, 80, 0, 1350, 90)
    ChrSetPos(0x000C, -380, 0, 230, 45)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    CameraMove(110, 0, -2000, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(2650, 0)
    OP_6C(45000, 0)
    OP_6E(287, 0)

    @scena.Lambda('lambda_6D5D')
    def lambda_6D5D():
        CameraMove(790, 0, 2790, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6D5D)

    @scena.Lambda('lambda_6D75')
    def lambda_6D75():
        OP_67(0, 6000, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6D75)

    FadeIn(1500, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0010320155V#1007F是吗……\n',
            '有这种事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030320156V#022F『剑帝』莱维……\n',
            '的确是个有胆量的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050320157V#053F啊，真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320158V#555F就因为这样，\n',
            '眼睁睁地看着敌人逃走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320159V抱歉，我没有什么可以为自己辩解的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380320160V#634F不，那种场合，\n',
            '让他走才是正确的选择吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320161V至少……\n',
            '不能在墓地引发骚乱啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320162V#632F话说回来……\n',
            '这个叫『哈梅尔』的名字似乎非同一般，\n',
            '总觉得让人很在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320163V#1003F这名字……\n',
            '之前在女王宫和洛伦斯少尉战斗的时候，\n',
            '他好像也提到过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0011,
        (
            '#0010320164V#1015F#5P科洛丝，你知道些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 0, 400)

    @scena.Lambda('lambda_6FF7')
    def lambda_6FF7():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6FF7)

    Sleep(50)

    @scena.Lambda('lambda_700A')
    def lambda_700A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_700A)

    ChrTalk(
        0x000D,
        (
            '#0060320165V#043F#4P很遗憾……不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320166V#049F我想祖母大人她大概会\n',
            '知道点什么吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060320167V但是，如果问起关于国家之间的问题的话，\n',
            '或许她什么也不会告诉我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320168V#1007F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320169V#1015F奥利维尔你呢？\n',
            '那是埃雷波尼亚帝国的村庄吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040320170V#035F嗯……『哈梅尔』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320171V#030F又出现了一个\n',
            '奇妙的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320172V#1004F#5P奇妙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_71A5')
    def lambda_71A5():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_71A5)

    Sleep(50)

    @scena.Lambda('lambda_71B8')
    def lambda_71B8():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_71B8)

    Sleep(50)

    @scena.Lambda('lambda_71CB')
    def lambda_71CB():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_71CB)

    @scena.Lambda('lambda_71D9')
    def lambda_71D9():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_71D9)

    Sleep(50)

    @scena.Lambda('lambda_71EC')
    def lambda_71EC():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_71EC)

    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0040320173V#032F那个哈梅尔\n',
            '是位于帝国最南端的一座村庄的名字……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320174V但是现在这名字\n',
            '并没有记载在帝国的地图上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0010320175V#1020F#5P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070320176V#064F#5P没有记载……\n',
            '为什么没有记载呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040320177V#035F据说在几年前那里发生了山崩，\n',
            '死了很多人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320178V现在似乎是一座废弃的村庄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070320179V#063F#5P废弃的村庄……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050320180V#552F#5P……原来是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320181V#1020F#5P可，可是，\n',
            '据说是死了很多人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040320182V#032F因为是出动了军队前去救灾，\n',
            '民众并不清楚详细的情况……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320183V但有一种说法认为，\n',
            '全村的人几乎都死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320184V#1026F#5P全、全都死了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080320185V#074F#5P确实如此，据说是\n',
            '爆发了一场很严重的山崩，\n',
            '把整个村子都吞没了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320186V#072F好像是叫做『山体滑坡』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030320187V#025F#5P原来如此，很奇妙的说法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320188V#522F不过，这为什么\n',
            '会和利贝尔女王殿下以及将军\n',
            '有关呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040320189V#035F这个嘛……\n',
            '目前一点头绪也没有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380320190V#634F嗯……\n',
            '不如就由我出面向帝国的协会\n',
            '询问一下这些事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320191V#630F好了，关于『哈梅尔』的\n',
            '话题就先聊到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_76CC')
    def lambda_76CC():
        CameraMove(870, 0, 3840, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_76CC)

    @scena.Lambda('lambda_76E4')
    def lambda_76E4():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_76E4)

    @scena.Lambda('lambda_76F2')
    def lambda_76F2():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_76F2)

    Sleep(50)

    @scena.Lambda('lambda_7705')
    def lambda_7705():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7705)

    @scena.Lambda('lambda_7713')
    def lambda_7713():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_7713)

    @scena.Lambda('lambda_7721')
    def lambda_7721():
        ChrSetDirection(0x00FE, 5, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7721)

    Sleep(50)

    @scena.Lambda('lambda_7734')
    def lambda_7734():
        ChrSetDirection(0x00FE, 5, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7734)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0380320192V#630F先把这次的报酬\n',
            '付给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0094, 0x04, 0x10)
    OP_AF(0x36, 0x0094)
    Sleep(100)

    OP_28(0x0095, 0x04, 0x10)
    OP_AF(0x36, 0x0095)
    Sleep(100)

    OP_28(0x0096, 0x04, 0x10)
    OP_28(0x0096, 0x04, 0x20)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0380320193V#631F#5P这次龙引起的骚乱，\n',
            '真的辛苦各位了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320194V真是充分体现了游击士协会\n',
            '的本色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320195V#1008F#6P嘿嘿……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050320196V#552F#4P但是，\n',
            '『实验』本身还是未能彻底阻止……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320197V所以我们还不能放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030320198V#022F#6P而且，直到目前为止，\n',
            '包括王都在内已经有５个地方\n',
            '进行过『实验』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320199V必须立即调查清楚\n',
            '下一步『结社』会采取怎么的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380320200V#634F#5P怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320201V#630F你们几个，\n',
            '稍微休息一下如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0010250939V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7A7A',
    )

    ChrTalk(
        0x000E,
        (
            '#0050320203V#052F#4P休息？\n',
            '怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AA9')

    def _loc_7A7A(): pass

    label('loc_7A7A')

    ChrTalk(
        0x000B,
        (
            '#0030320204V#023F#6P休息？\n',
            '是怎么一回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AA9(): pass

    label('loc_7AA9')

    ChrTalk(
        0x0008,
        (
            '#0380320205V#630F#5P休息就是休息啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320206V以卢安地区为起点的连续５起事件，\n',
            '已经让你们焦头烂额了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320207V不在这时候休息一下的话，\n',
            '会对身心造成负担哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320208V#1026F#6P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7C04',
    )

    ChrTalk(
        0x000E,
        (
            '#0050320209V#555F#4P那些家伙若是再惹出些什么事来，\n',
            '我们就需要出面去应对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320210V实在是没什么时间\n',
            '悠哉游哉的休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C7E')

    def _loc_7C04(): pass

    label('loc_7C04')

    ChrTalk(
        0x000B,
        (
            '#0030320211V#022F#6P那些人若是再引起事端的话，\n',
            '就需要我们行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320212V暂时……\n',
            '我觉得我们没有休息的余地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C7E(): pass

    label('loc_7C7E')

    ChrTalk(
        0x0008,
        (
            '#0380320213V#634F#5P这次因为龙的事件，\n',
            '王国军的警戒也变得严密了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320214V因而，可以说\n',
            '我们也轻松了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320215V#632F再加上……\n',
            '克鲁茨他们恐怕也有了点头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0010320216V#1005F#6P#4S啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7E5E',
    )

    ChrTalk(
        0x000B,
        (
            '#0030320217V#024F#6P有点头绪……\n',
            '是指『噬身之蛇』的基地吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E9D')

    def _loc_7E5E(): pass

    label('loc_7E5E')

    ChrTalk(
        0x000E,
        (
            '#0050320218V#054F#4P所谓头绪……\n',
            '『噬身之蛇』的基地吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E9D(): pass

    label('loc_7E9D')

    ChrTalk(
        0x0008,
        (
            '#0380320219V#634F#5P嗯，几天来\n',
            '我们这里得到了确切的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320220V#630F假如查清了那帮人的基地在哪里的话，\n',
            '肯定会一下子忙碌起来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320221V所以在空闲的时候，\n',
            '我希望你们能多多休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320222V#1015F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080320223V#070F#6P嗯，既然是这样的话，\n',
            '就应该恭敬不如从命才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320224V其实状态的调整也是\n',
            '游击士的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030320225V#027F#6P确实如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050320226V#051F#4P这段时间\n',
            '稍微休息一下也不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(11)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0040320227V#031F呵呵，这不是\n',
            '意见统一了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320228V#030F但是老人家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320229V其实你一直劝我们休息，\n',
            '是不是因为有了什么好东西啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380320230V#631F#5P呵呵，真敏锐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320231V#630F其实，我刚刚从梅贝尔市长那里\n',
            '得到了一样好东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320232V当然，这和龙事件所获的报酬是两回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320233V#1004F#6P市长姐姐送的……好东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380320234V#631F#5P直截了当地告诉你吧，就是\n',
            '位于南面湖畔『川蝉亭』的特別餐券。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380320235V总之，\n',
            '你们大家可以在那里免费住宿三天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320236V#1018F#6P真，真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['住宿票券']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['住宿票券'], 1)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0040320237V#031F呵呵……\n',
            '不愧是威名远播的柏斯市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060320238V#048F呼呼……\n',
            '不愧是前辈，她对我们真是既关心又体贴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 270, 400)

    ChrTalk(
        0x000F,
        (
            '#0070320239V#560F#2P那个，这也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070320240V大家可以一起到郊外游玩，\n',
            '一起外出住宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_83BE')
    def lambda_83BE():
        ChrSetDirection(0x000B, 90, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_83BE)

    Sleep(50)

    @scena.Lambda('lambda_83D1')
    def lambda_83D1():
        ChrSetDirection(0x000D, 90, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_83D1)

    Sleep(50)

    @scena.Lambda('lambda_83E4')
    def lambda_83E4():
        ChrSetDirection(0x0010, 90, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_83E4)

    Sleep(50)

    @scena.Lambda('lambda_83F7')
    def lambda_83F7():
        ChrSetDirection(0x000E, 225, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_83F7)

    Sleep(50)

    @scena.Lambda('lambda_840A')
    def lambda_840A():
        ChrSetDirection(0x0011, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_840A)

    Sleep(300)

    ChrTalk(
        0x000B,
        (
            '#0030320241V#021F#6P呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320242V#027F而且是住在瓦雷利亚湖畔\n',
            '那座景色宜人的旅馆呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320243V不仅酒和料理非常美味，\n',
            '而且还可以乘坐小船游玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070320244V#061F#2P哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080320245V#071F#6P嗯……\n',
            '这可真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050320246V#051F#5P嗯，那里的确是个适合\n',
            '释放心情的好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010320247V#1001F#5P嗯嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320248V#1018F哟哟，既然要休息的话，\n',
            '不如去尽情舒展一下筋骨吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    def _loc_85C2(): pass

    label('loc_85C2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8879',
    )

    SetMessageWindowPos(-1, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※パーティの再編成を行います。\n',
            '　パーティを入れ替えて、必要な装備の変更を行い、\n',
            '　確定したら、【先に進める】を選択してください。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        180,
        80,
        0,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【变更装备】\n'),
            TXT(0x02, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
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
        'loc_8722',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '  请在固定成员以外挑选３名同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_8876')

    def _loc_8722(): pass

    label('loc_8722')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_875B',
    )

    OP_C0(0x13, 0x00000078, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Jump('loc_879F')

    def _loc_875B(): pass

    label('loc_875B')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※パーティの編成を行ってから選択してください。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    def _loc_879F(): pass

    label('loc_879F')

    Jump('loc_8876')

    def _loc_87A2(): pass

    label('loc_87A2')

    TalkSetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※イベントを先に進めても、よろしいですか？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
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
        'loc_8871',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_886B',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>※パーティの編成を行ってから選択してください。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    Jump('loc_886E')

    def _loc_886B(): pass

    label('loc_886B')

    Jump('loc_8879')

    def _loc_886E(): pass

    label('loc_886E')

    Jump('loc_8876')

    def _loc_8871(): pass

    label('loc_8871')

    Sleep(300)

    def _loc_8876(): pass

    label('loc_8876')

    Jump('loc_85C2')

    def _loc_8879(): pass

    label('loc_8879')

    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T1101._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x888E
@scena.Code('func_1A_888E')
def func_1A_888E():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x000F, 255)
    ChrSetPos(0x0011, -490, 0, 2350, 0)
    ChrSetPos(0x0012, 520, 0, 2350, 0)
    ChrSetPos(0x000B, -1340, 0, 950, 0)
    ChrSetPos(0x000E, -400, 0, 860, 0)
    ChrSetPos(0x000F, 950, 0, 1650, 0)
    ChrSetPos(0x0010, 550, 0, 390, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000E, 6)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetChipByIndex(0x0010, 8)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    CameraMove(1110, 0, 3380, 0)
    OP_67(0, 6670, -10000, 0)
    CameraSetDistance(2230, 0)
    OP_6C(45000, 0)
    OP_6E(328, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0380350047V#634F唔唔……\n',
            '竟然在四轮之塔发生这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350048V#632F真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350049V不管怎么样，\n',
            '先付给你们报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x009A, 0x04, 0x10)
    OP_AF(0x36, 0x009A)
    Sleep(100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0380350050V#634F……但是，\n',
            '事态变得一发不可收拾了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350051V#632F没想到导力器无法使用\n',
            '的事件竟然会在全国范围内\n',
            '引起如此大的混乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350052V#1007F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350053V#1003F平日大家受了导力器多少恩惠，\n',
            '现在总算是知道了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020350054V#1043F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350055V#1035F通信、交通、国防、生产线……\n',
            '国家机能如同瘫痪了一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030350056V#025F#6P对市民来说，\n',
            '最担心的是照明和取暖吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350057V#022F对了，\n',
            '昨天夜里…城里是不是非常混乱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380350058V#632F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350059V市民涌向了协会、工房、市长官邸，\n',
            '场面别提多混乱了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350060V可就算问我发生了什么事，\n',
            '我也回答不出来啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350061V#634F所以啊，昨晚睡眠严重不足呢。唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350062V#1015F#6P是吗……辛苦爷爷你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050350063V#555F浮游都市的事还没处理完，\n',
            '状况就变得如此的糟糕了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350064V难道说王国会陷入新一轮危机中吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080350065V#074F但利贝尔的治安很好，\n',
            '不用担心会发生暴动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350066V#072F不过长期持续这种状态的话，\n',
            '也不大好说会怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380350067V#634F嗯……\n',
            '所以要尽早采取措施才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350068V#630F──那，你们几个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350069V拉赛尔博士告诉你们的\n',
            '起死回生的策略到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350070V#1025F#6P呼呼呼……\n',
            '没有起死回生那么夸张啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020350071V#1040F拉赛尔博士给我们提供了\n',
            '最新发明的实验品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x8F42
@scena.Code('func_1B_8F42')
def func_1B_8F42():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x000F, 255)
    ChrSetPos(0x0011, -490, 0, 2350, 0)
    ChrSetPos(0x0012, 520, 0, 2350, 0)
    ChrSetPos(0x000B, -1340, 0, 950, 0)
    ChrSetPos(0x000E, -400, 0, 860, 0)
    ChrSetPos(0x000F, 950, 0, 1650, 0)
    ChrSetPos(0x0010, 550, 0, 390, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000E, 6)
    ChrSetChipByIndex(0x000F, 7)
    ChrSetChipByIndex(0x0010, 8)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    CameraMove(1110, 0, 3380, 0)
    OP_67(0, 6670, -10000, 0)
    CameraSetDistance(2230, 0)
    OP_6C(45000, 0)
    OP_6E(328, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0380350137V#633F什么……\n',
            '让通信器可以使用的装置吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350138V#631F这可是帮大忙啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350139V赶紧拿这个『零力场发生器』\n',
            '来试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350140V#1006F#6P好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0012, -180, 400)
    ChrSetDirection(0x0011, 90, 400)

    ChrTalk(
        0x0012,
        (
            '#0020350141V#1040F#5P提妲，\n',
            '就全拜托你了可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070350142V#061F嗯。\n',
            '稍微等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 90, 400)

    @scena.Lambda('lambda_9170')
    def lambda_9170():
        CameraMove(1020, 0, 3960, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9170)

    @scena.Lambda('lambda_9188')
    def lambda_9188():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_9188')

    DispatchAsync2(0x0008, 0x0001, lambda_9188)

    @scena.Lambda('lambda_9199')
    def lambda_9199():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_9199')

    DispatchAsync2(0x0011, 0x0001, lambda_9199)

    @scena.Lambda('lambda_91AA')
    def lambda_91AA():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_91AA')

    DispatchAsync2(0x0012, 0x0001, lambda_91AA)

    ChrWalkTo(0x000F, 3900, 0, 1880, 3000, 0x00)
    ChrWalkTo(0x000F, 4090, 0, 4980, 3000, 0x00)
    ChrWalkTo(0x000F, 1970, 0, 4690, 3000, 0x00)

    @scena.Lambda('lambda_91F7')
    def lambda_91F7():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_91F7)

    @scena.Lambda('lambda_9205')
    def lambda_9205():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_9205)

    @scena.Lambda('lambda_9213')
    def lambda_9213():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_9213)

    ChrSetDirection(0x000F, 0, 400)
    Sleep(500)

    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0012, 0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲打开了通信器的盖子，\n',
            '把『零力场发生器』放进了里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#0070350143V#062F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(10, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x000F, 225, 400)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0070350144V#061F#5P……嗯。\n',
            '这样就设定好了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050350145V#052F是吗，可真快呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070350146V#067F嘿嘿～～\n',
            '只是把它固定在通信器中而已啦',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350147V#560F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 0, 400)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    PlaySE(131, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0380350148V#633F#6P喔喔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350149V#1008F#6P成功了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030350150V#021F#6P呵呵，\n',
            '看来导力器真的\n',
            '能够不受『导力停止现象』的影响重新工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0070350151V#560F#4P那个，\n',
            '接下来试试看信息能否确实\n',
            '传送出去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350152V我试着和留在埃尔赛尤\n',
            '的爷爷进行联络。',
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
            '提妲拨起了通信器的拨号盘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(500)

    PlaySE(195, 0x00, 0x46)
    Sleep(3000)

    OP_23(0x00C3)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0070350153V#064F#4P喂喂……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350154V#560F啊……爷爷！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350155V#061F嗯！\n',
            '我现在在柏斯的协会里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350156V没事的。\n',
            '发生装置的运作很正常。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070350157V#560F……嗯……嗯。\n',
            '爷爷也加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(500)

    ChrSetDirection(0x000F, 225, 400)

    ChrTalk(
        0x000F,
        (
            '#0070350158V#061F#5P嘻嘻……\n',
            '通信没问题，确实联系上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350159V#1018F#6P成功了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020350160V#1040F#6P不愧是博士的新发明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380350161V#631F#6P哈哈哈。\n',
            '应该怎么感谢博士才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9775')
    def lambda_9775():
        CameraMove(1110, 0, 3380, 1100)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_9775)

    ChrTurnDirection(0x0008, 0x0011, 400)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0380350162V#633F#5P说起来，\n',
            '拉赛尔博士好像留在埃尔赛尤了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350163V那公主殿下和凯文神父去哪儿了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9808')
    def lambda_9808():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_9808)

    Sleep(50)

    @scena.Lambda('lambda_981B')
    def lambda_981B():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_981B)

    Sleep(50)

    @scena.Lambda('lambda_982E')
    def lambda_982E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_982E)

    Sleep(50)

    @scena.Lambda('lambda_9841')
    def lambda_9841():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_9841)

    Sleep(50)

    ChrSetDirection(0x0010, 0, 400)
    Sleep(200)

    ChrTalk(
        0x0011,
        (
            '#0010350164V#1006F#6P啊……\n',
            '他们两个今早和亲卫队队员一起\n',
            '前往王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350165V两个人都有事情要做。\n',
            '科洛丝想找女王殿下谈些事情，\n',
            '凯文是想找大主教问些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380350166V#634F#5P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350167V#630F王室的找王室、教会的找教会，\n',
            '正所谓各司其职啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020350168V#1040F此外，\n',
            '他们两个也接受了把『零力场发生器』\n',
            '带去王都协会的任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350169V过一段时间，\n',
            '我们这边也会收到他们的联络也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380350170V#634F是吗……真是帮了大忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380350171V#630F那么，\n',
            '你们接下来要把剩下的三所协会\n',
            '都走访一遍是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0010350172V#1006F#6P嗯，是这么打算的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350173V#1003F……其实本来是想对那个浮游都市\n',
            '采取点什么措施的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030350174V#025F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350175V况且『结社』的那帮人\n',
            '好像已经进入浮游岛了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9B4B')
    def lambda_9B4B():
        ChrSetDirection(0x0011, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_9B4B)

    Sleep(50)

    ChrSetDirection(0x0012, -180, 400)

    ChrTalk(
        0x000E,
        (
            '#0050350176V#552F但是，飞船无法使用的话，\n',
            '想前往浮游都市基本是不可能的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350177V#551F哼，真是进退两难的境地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0020350178V#1043F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0080350179V#074F也罢，干着急也无济于事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350180V#070F现在，我们要做的，\n',
            '就是把自己力所能及的事情处理完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050350181V#051F#6P说的对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030350182V#020F#6P嗯……\n',
            '加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B7(0x04)
    OP_B7(0x08)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(10350, 0, 17540, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9D30',
    )

    Call(0, 0x001C)

    def _loc_9D30(): pass

    label('loc_9D30')

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetStatus(0x00FF, 0xFE, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0400, 0, 0x2000))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T1101._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x9DCB
@scena.Code('func_1C_9DCB')
def func_1C_9DCB():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9E45'),
        (0x00000001, 'loc_9E4B'),
        (-1, 'loc_9E51'),
    )

    def _loc_9E45(): pass

    label('loc_9E45')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_9E51')

    def _loc_9E4B(): pass

    label('loc_9E4B')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_9E51')

    def _loc_9E51(): pass

    label('loc_9E51')

    Return()

# id: 0x001D offset: 0x9E52
@scena.Code('func_1D_9E52')
def func_1D_9E52():
    FadeOut(0, 0, -1)
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_9F09'),
        (0x00000001, 'loc_9F0F'),
        (-1, 'loc_9F15'),
    )

    def _loc_9F09(): pass

    label('loc_9F09')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_9F15')

    def _loc_9F0F(): pass

    label('loc_9F0F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_9F15')

    def _loc_9F15(): pass

    label('loc_9F15')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x001E offset: 0x9F51
@scena.Code('func_1E_9F51')
def func_1E_9F51():
    FadeOut(0, 0, -1)
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
