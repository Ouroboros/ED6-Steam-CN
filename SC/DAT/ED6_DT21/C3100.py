import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3100.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT27/CH03125._CH', 'ED6_DT27/CH03125P._CP'),
        ('ED6_DT27/CH03120._CH', 'ED6_DT27/CH03120P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '凯诺娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵塞缪尔',
            x                   = 0,
            z                   = 0,
            y                   = -3230,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德中校',
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
            name                = '测量仪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贝尔克副队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x22A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x22A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4990,
            y           = 0,
            z           = -35710,
            range       = 5060,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF7D1A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 5460,
            triggerZ            = -60,
            triggerY            = -46490,
            triggerRange        = 2000,
            actorX              = 5460,
            actorZ              = -60,
            actorY              = -46490,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6000,
            triggerZ            = 0,
            triggerY            = -45540,
            triggerRange        = 1500,
            actorX              = 6000,
            actorZ              = 1500,
            actorY              = -45540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31750,
            triggerZ            = -30,
            triggerY            = -32759,
            triggerRange        = 1000,
            actorX              = 32009,
            actorZ              = -1030,
            actorY              = -29320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2B6
@scena.Code('Init')
def Init():
    ChrClearFlags(0x0009, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2DA',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_0D_4F3C)

    Jump('loc_32D')

    def _loc_2DA(): pass

    label('loc_2DA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 4, 0x141C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FB',
    )

    MapSetFlags(0x10000000)
    Event(0, func_04_F17)

    Jump('loc_32D')

    def _loc_2FB(): pass

    label('loc_2FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_311',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(1, 0x0003)

    Jump('loc_32D')

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_32D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_0E_51B4)

    def _loc_32D(): pass

    label('loc_32D')

    Return()

# id: 0x0001 offset: 0x32E
@scena.Code('func_01_32E')
def func_01_32E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_33C',
    )

    OP_6F(0x0000, 110)

    def _loc_33C(): pass

    label('loc_33C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 6, 0x141E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34F',
    )

    OP_65(0x00, 0x0001)

    Jump('loc_353')

    def _loc_34F(): pass

    label('loc_34F')

    OP_64(0x00, 0x0001)

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_380',
    )

    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    PlaySE(158, 0x01, 0x64)
    OP_24(0x009E, 0x4B)

    def _loc_380(): pass

    label('loc_380')

    PlaySE(461, 0x01, 0x5A)

    Return()

# id: 0x0002 offset: 0x386
@scena.Code('func_02_386')
def func_02_386():
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
        (0x00000000, 'loc_3B7'),
        (0x00000001, 'loc_3C3'),
        (0x00000002, 'loc_3CF'),
        (0x00000003, 'loc_3DB'),
        (0x00000004, 'loc_3E7'),
        (0x00000005, 'loc_3F3'),
        (0x00000006, 'loc_3FF'),
        (-1, 'loc_40B'),
    )

    def _loc_3B7(): pass

    label('loc_3B7')

    OP_99(0x00FE, 0x00, 0x07, 1450)

    Jump('loc_417')

    def _loc_3C3(): pass

    label('loc_3C3')

    OP_99(0x00FE, 0x00, 0x07, 1550)

    Jump('loc_417')

    def _loc_3CF(): pass

    label('loc_3CF')

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_417')

    def _loc_3DB(): pass

    label('loc_3DB')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('loc_417')

    def _loc_3E7(): pass

    label('loc_3E7')

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_417')

    def _loc_3F3(): pass

    label('loc_3F3')

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_417')

    def _loc_3FF(): pass

    label('loc_3FF')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_417')

    def _loc_40B(): pass

    label('loc_40B')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_417')

    def _loc_417(): pass

    label('loc_417')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_42C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_417')

    def _loc_42C(): pass

    label('loc_42C')

    Return()

# id: 0x0003 offset: 0x42D
@scena.Code('func_03_42D')
def func_03_42D():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 5, 0x200D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_448',
    )

    Call(0, 0x000F)

    Jump('loc_80B')

    def _loc_448(): pass

    label('loc_448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_57E',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51A',
    )

    ChrTalk(
        0x00FE,
        (
            '与各关所之间的通讯恢复了，\n',
            '王国军也做好了作战准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然维持治安也是件十分重要的事情，\n',
            '不过，如何解决目前的导力停止问题\n',
            '才是当务之急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就连卡西乌斯准将\n',
            '也感到很伤脑筋吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_578')

    def _loc_51A(): pass

    label('loc_51A')

    ChrTalk(
        0x00FE,
        (
            '不过，如何解决目前的导力停止问题\n',
            '才是当务之急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就连卡西乌斯准将\n',
            '也感到很伤脑筋吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_578(): pass

    label('loc_578')

    TalkEnd(0x0009)

    Jump('loc_80B')

    def _loc_57E(): pass

    label('loc_57E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Return,
        ),
        'loc_79D',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Return,
        ),
        'loc_70D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BA',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，你们……\n',
            '找到内燃机了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，已经顺利取得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F警备艇的各位\n',
            '也好象没有受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗？这可是好消息。\n',
            '赶快去报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '救援部队很快\n',
            '就会来收容他们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，也请你们\n',
            '努力地修理温泉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F感谢你们帮了那么多忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F那就先失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_70A')

    def _loc_6BA(): pass

    label('loc_6BA')

    ChrTalk(
        0x00FE,
        (
            '去向司令部报告\n',
            '有关警备艇的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，也请你们\n',
            '努力地修理温泉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70A(): pass

    label('loc_70A')

    Jump('loc_797')

    def _loc_70D(): pass

    label('loc_70D')

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯准将\n',
            '为了重整混乱的王国军\n',
            '正向各地发出指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然说是紧急情况，\n',
            '但是他那不眠不休地进行指挥的身影，\n',
            '真可说是全军的楷模。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_797(): pass

    label('loc_797')

    TalkEnd(0x0009)

    Jump('loc_80B')

    def _loc_79D(): pass

    label('loc_79D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Return,
        ),
        'loc_807',
    )

    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '警备艇应该是停在\n',
            '托兰特平原的某个地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有关内燃机的事情，\n',
            '请你们去问他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Jump('loc_80B')

    def _loc_807(): pass

    label('loc_807')

    Call(0, 0x0010)

    def _loc_80B(): pass

    label('loc_80B')

    Return()

    def _loc_80C(): pass

    label('loc_80C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 4, 0x141C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 5, 0x141D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_81D',
    )

    Call(0, 0x0005)

    Return()

    def _loc_81D(): pass

    label('loc_81D')

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_84C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_847',
    )

    Call(1, 0x0000)

    Return()

    def _loc_847(): pass

    label('loc_847')

    Call(1, 0x0001)

    Return()

    def _loc_84C(): pass

    label('loc_84C')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_966',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8E0',
    )

    ChrTalk(
        0x0009,
        (
            '可以预料，担任实际警戒任务的\n',
            '也将以驻留要塞的部队为主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '由我们来守护王国军的中枢\n',
            '承担这中流砥柱的职责也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_963')

    def _loc_8E0(): pass

    label('loc_8E0')

    ChrTalk(
        0x0009,
        (
            '不久希德中校\n',
            '就要出发去王都了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '当然是为了签字仪式的警戒工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然是国家性的仪式，\n',
            '不过中校去的话就让人放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_963(): pass

    label('loc_963')

    Jump('loc_F13')

    def _loc_966(): pass

    label('loc_966')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_A50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9C7',
    )

    ChrTalk(
        0x0009,
        (
            '多亏收到了待命的命令，\n',
            '因此几乎没有受到损害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这个命令来得\n',
            '真是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4D')

    def _loc_9C7(): pass

    label('loc_9C7')

    ChrTalk(
        0x0009,
        (
            '现在在要塞内部\n',
            '正在确认受损情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然震度不弱，\n',
            '不过并没有受到损害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这都是因为事先接到了\n',
            '准备防范地震的待机命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A4D(): pass

    label('loc_A4D')

    Jump('loc_F13')

    def _loc_A50(): pass

    label('loc_A50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Return,
        ),
        'loc_B3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_A9C',
    )

    ChrTalk(
        0x0009,
        (
            '你、你们和准将\n',
            '谈了些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可恶，真令人羡慕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3C')

    def _loc_A9C(): pass

    label('loc_A9C')

    ChrTalk(
        0x0009,
        (
            '刚、刚才是作战本部的\n',
            '卡西乌斯准将吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你、你们……\n',
            '谈了些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就连我这个已经服役十几年的老兵\n',
            '也没跟他说过话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可恶，真令人羡慕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_B3C(): pass

    label('loc_B3C')

    Jump('loc_F13')

    def _loc_B3F(): pass

    label('loc_B3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 5, 0x141D)),
            Expr.Return,
        ),
        'loc_BE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B85',
    )

    ChrTalk(
        0x0009,
        (
            '请避开铺装路面。\n',
            '否则车辆通过的时候会有麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE0')

    def _loc_B85(): pass

    label('loc_B85')

    ChrTalk(
        0x0009,
        (
            '请避开铺装路面。\n',
            '否则车辆通过的时候会有麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '其他的地方你们\n',
            '可以随意设置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_BE0(): pass

    label('loc_BE0')

    Jump('loc_F13')

    def _loc_BE3(): pass

    label('loc_BE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_E0A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x40)"),
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006D, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C7B',
    )

    ChrTalk(
        0x0009,
        (
            '蔡斯各地好像\n',
            '都在发生地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要塞的留驻部队也处于警戒状态\n',
            '以防万一出现的紧急情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCC')

    def _loc_C7B(): pass

    label('loc_C7B')

    ChrTalk(
        0x0009,
        (
            '最近蔡斯各地好像\n',
            '都在发生地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们要塞留驻部队也\n',
            '也正在加强警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_CCC(): pass

    label('loc_CCC')

    Jump('loc_D21')

    def _loc_CCF(): pass

    label('loc_CCF')

    ChrTalk(
        0x00FE,
        (
            '很遗憾，训练\n',
            '已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正进行抗震准备的工作，\n',
            '已经顾不上训练了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D21(): pass

    label('loc_D21')

    Jump('loc_E07')

    def _loc_D24(): pass

    label('loc_D24')

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们\n',
            '来得太迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '训练早就\n',
            '已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，果然是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '上面的确写着要尽快过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，而且现在正在进行抗震准备的工作，\n',
            '似乎不是训练的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队的高官已经\n',
            '聚集在一起开始讨论了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006D, 0x01, 0x8000)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    def _loc_E07(): pass

    label('loc_E07')

    Jump('loc_F13')

    def _loc_E0A(): pass

    label('loc_E0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_F13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E4E',
    )

    ChrTalk(
        0x0009,
        (
            '哟，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今天的训练\n',
            '看来相当严格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F13')

    def _loc_E4E(): pass

    label('loc_E4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_EB6',
    )

    ChrTalk(
        0x0009,
        (
            '因为是重要的军事设施，\n',
            '所以是禁止摄影的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就算再怎么样也不能以\n',
            '要塞为背景进行摄影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F13')

    def _loc_EB6(): pass

    label('loc_EB6')

    ChrTalk(
        0x0009,
        (
            '这是王国军的根据地\n',
            '雷斯顿水上要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '民间人士\n',
            '请勿进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '能不能请你们回去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_F13(): pass

    label('loc_F13')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0xF17
@scena.Code('func_04_F17')
def func_04_F17():
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
        'loc_F2E',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)

    def _loc_F2E(): pass

    label('loc_F2E')

    ChrSetPos(0x0101, -1130, 0, -60200, 0)
    ChrSetPos(0x0107, -120, 0, -61110, 0)
    ChrSetPos(0x00F7, -1370, 0, -61940, 0)
    ChrSetPos(0x00F9, -500, 0, -62650, 0)
    MapClearFlags(0x00000010)
    CameraMove(560, 0, -4680, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(5110, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0FBA')
    def lambda_0FBA():
        CameraMove(680, -140, -49070, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FBA)

    @scena.Lambda('lambda_0FD2')
    def lambda_0FD2():
        OP_67(0, 9500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FD2)

    OP_C8(0x0200, 0x0046, 'C_PLAC10._CH', 0x00, 0x03E8)
    ShowPlaceName('雷斯顿要塞')
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_101A')
    def lambda_101A():
        ChrWalkTo(0x00FE, -360, -80, -49000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_101A)

    Sleep(100)

    @scena.Lambda('lambda_103A')
    def lambda_103A():
        ChrWalkTo(0x00FE, 780, -120, -49260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_103A)

    Sleep(100)

    @scena.Lambda('lambda_105A')
    def lambda_105A():
        ChrWalkTo(0x00FE, -750, -70, -50590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_105A)

    Sleep(100)

    @scena.Lambda('lambda_107A')
    def lambda_107A():
        ChrWalkTo(0x00FE, 520, -110, -50770, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_107A)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    Fade(1000)
    OP_12(0x00009470, 0x0001FBD0, 0x00000000)
    CameraMove(190, -40, -49730, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0107, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x01, 0x0001)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1144',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230387V#1011F#5P雷斯顿要塞……\n',
            '总觉得好怀念。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_1144(): pass

    label('loc_1144')

    ChrTalk(
        0x0101,
        (
            '#0010230388V#1011F#5P雷斯顿要塞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230389V来参加训练的时候\n',
            '总觉得好怀念。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_119A(): pass

    label('loc_119A')

    ChrTalk(
        0x0107,
        (
            '#0070230390V#067F#2P嘿嘿嘿……\n',
            '我也有那种心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230391V#560F因为上次是在晚上和姐姐你们分开的，\n',
            '所以和印象中有点不同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1283',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230392V#051F嗯，因为上次是\n',
            '冒险潜入进来的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230393V因此也就变得更加怀念。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12EB')

    def _loc_1283(): pass

    label('loc_1283')

    ChrTalk(
        0x0103,
        (
            '#0030230394V#027F说起来，你们似乎为了\n',
            '营救博士而潜入过这里吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230395V真是的，老是这么乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12EB(): pass

    label('loc_12EB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13D2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230396V#032F唔，这么有趣的事情\n',
            '居然没找我一起去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230397V你们几个太无情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230398V#1007F#5P为什么非要\n',
            '特地去叫你啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230399V#1006F别说这个了，还是\n',
            '赶快设置测量仪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B3')

    def _loc_13D2(): pass

    label('loc_13D2')

    ChrTalk(
        0x0105,
        (
            '#0060230400V#542F原来还发生过那种事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230401V你们竟然能够潜入\n',
            '这座铜墙铁壁的要塞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230402V#1016F#5P嘿嘿……\n',
            '稍微用了一点小把戏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230399V#1006F别说这个了，还是\n',
            '赶快设置测量仪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14B3(): pass

    label('loc_14B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1532',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230404V#051F不，先去向门卫\n',
            '取得设置许可比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230405V雾香应该已经联系过了，\n',
            '大概马上就会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A7')

    def _loc_1532(): pass

    label('loc_1532')

    ChrTalk(
        0x0103,
        (
            '#0030230406V#020F先去向门卫\n',
            '取得设置许可比较好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230407V雾香小姐应该已经联系过了，\n',
            '大概马上就会同意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A7(): pass

    label('loc_15A7')

    ChrTalk(
        0x0101,
        (
            '#0010230408V#1006F#5P嗯，ＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0283, 4, 0x141C))
    OP_28(0x0087, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x15D8
@scena.Code('func_05_15D8')
def func_05_15D8():
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
        'loc_15F8',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)
    FadeIn(0, 0)

    def _loc_15F8(): pass

    label('loc_15F8')

    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0101, -500, 0, -4790, 0)
    ChrSetPos(0x00F7, 900, 0, -4790, 0)
    ChrSetPos(0x0107, -540, 160, -6150, 0)
    ChrSetPos(0x00F9, 480, 160, -6270, 0)
    CameraMove(320, 0, -3840, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#3110230409V#5P这里是王国军的根据地\n',
            '雷斯顿水上要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110230410V#5P民间人士\n',
            '请勿进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110230411V#5P能不能请你们回去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230412V#1015F#6P那个，我们是\n',
            '游击士协会的人。',
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
            '#3110230413V#5P哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110230414V#5P我听司令部说过了。\n',
            '好像要设置什么装置吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1830',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230415V#051F#2P尽量长话短说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230416V我们想早点进行设置，\n',
            '能不能让我们自由行动呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1899')

    def _loc_1830(): pass

    label('loc_1830')

    ChrTalk(
        0x0103,
        (
            '#0030230417V#020F#2P还是尽量长话短说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230418V我们想早点进行设置，\n',
            '能不能让我们自由行动呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1899(): pass

    label('loc_1899')

    ChrTalk(
        0x0009,
        (
            '#3110230419V#5P嗯，既然已经有许可了，\n',
            '就请你们随意设置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110230420V#5P不过，请不要设置\n',
            '在铺装路面上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110230421V#5P否则车辆通过的时候会有麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230422V#1006F#6P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    ChrSetDirection(0x00F7, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230423V#1006F#5P那么\n',
            '我们就找个合适的地点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230424V#061F#6P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)
    SetScenaFlags(ScenaFlag(0x0283, 5, 0x141D))
    OP_28(0x0087, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x19E1
@scena.Code('func_06_19E1')
def func_06_19E1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 5, 0x141D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 6, 0x141E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_19EE',
    )

    Return()

    def _loc_19EE(): pass

    label('loc_19EE')

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
        'loc_1A0E',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)
    FadeIn(0, 0)

    def _loc_1A0E(): pass

    label('loc_1A0E')

    SetScenaFlags(ScenaFlag(0x0283, 6, 0x141E))
    Fade(1000)
    ChrSetPos(0x0101, -910, 250, -36040, 180)
    ChrSetPos(0x0107, 140, 250, -36150, 180)
    ChrSetPos(0x00F7, 70, 250, -35070, 180)
    ChrSetPos(0x00F9, -910, 250, -34770, 180)
    CameraMove(-200, -230, -46450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_1A9E')
    def lambda_1A9E():
        ChrMoveToRelative(0x00FE, 0, 0, -11000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A9E)

    Sleep(150)

    @scena.Lambda('lambda_1ABE')
    def lambda_1ABE():
        ChrMoveToRelative(0x00FE, 0, 0, -11000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1ABE)

    Sleep(100)

    @scena.Lambda('lambda_1ADE')
    def lambda_1ADE():
        ChrMoveToRelative(0x00FE, 0, 0, -10700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1ADE)

    Sleep(200)

    @scena.Lambda('lambda_1AFE')
    def lambda_1AFE():
        ChrMoveToRelative(0x00FE, 0, 0, -10600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1AFE)

    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetDirection(0x0101, 90, 400)
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230425V#1006F#6P那么，提妲。\n',
            '设置在哪儿比较好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230426V#560F#2P嗯，稍微等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 400)

    @scena.Lambda('lambda_1B97')
    def lambda_1B97():
        CameraSetDistance(3270, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_1B97)

    @scena.Lambda('lambda_1BA7')
    def lambda_1BA7():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_1BA7')

    DispatchAsync2(0x0101, 0x0001, lambda_1BA7)

    @scena.Lambda('lambda_1BB8')
    def lambda_1BB8():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_1BB8')

    DispatchAsync2(0x00F7, 0x0001, lambda_1BB8)

    @scena.Lambda('lambda_1BC9')
    def lambda_1BC9():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_1BC9')

    DispatchAsync2(0x00F9, 0x0001, lambda_1BC9)

    ChrWalkTo(0x0107, 750, -190, -48660, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0107, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 180, 400)
    WaitForThreadExit(0x0001, 0x0000)

    ChrTalk(
        0x0107,
        (
            '#0070230427V#064F#5P嗯，除了铺装路面\n',
            '以外能放的地方嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 45, 400)

    @scena.Lambda('lambda_1C5D')
    def lambda_1C5D():
        CameraMove(2690, -160, -46040, 2500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_1C5D)

    Sleep(500)

    ChrWalkTo(0x0107, 4740, -40, -47430, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0107, 0, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070230428V#060F#5P……虽然旁边有照明设备，\n',
            '不过这样的距离应该是没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070230429V#060F#5P蔡斯在那边……\n',
            '嗯，方向也没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070230430V#061F#2P虽然就在牌子前面，\n',
            '我想在这里就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230116V现在就开始设置测量仪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)
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
            TXT(0x00, '【设置测量仪】\n'),
            TXT(0x01, '【先不设置】\n'),
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
        'loc_1E6D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070230432V#560F#2P那么\n',
            '开始进行设置作业啰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230028V请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F99')

    def _loc_1E6D(): pass

    label('loc_1E6D')

    ChrTalk(
        0x0107,
        (
            '#0070230434V#064F#2P哎……不设置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230030V#060F那就等准备好以后\n',
            '再来这个地方调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230031V到时再进行设置工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-910, -140, -47040, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -910, -140, -47040, 90)
    ChrSetPos(0x0001, -910, -140, -47040, 90)
    ChrSetPos(0x0002, -910, -140, -47040, 90)
    ChrSetPos(0x0003, -910, -140, -47040, 90)
    OP_69(0x0000, 0)
    OP_65(0x00, 0x0001)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_1F99(): pass

    label('loc_1F99')

    Call(0, 0x0008)

    Return()

# id: 0x0007 offset: 0x1F9E
@scena.Code('func_07_1F9E')
def func_07_1F9E():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 3460, -40, -46290, 90)
    ChrSetPos(0x0107, 4450, -20, -46910, 90)
    ChrSetPos(0x00F7, 3170, -40, -47550, 90)
    ChrSetPos(0x00F9, 4100, 70, -48420, 0)
    CameraMove(4450, -20, -46910, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
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
            TXT(0x00, '【设置测量仪】\n'),
            TXT(0x01, '【先不设置】\n'),
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
        'loc_20DD',
    )

    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230437V#061F#2P那么\n',
            '开始进行设置作业啰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230028V请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2170')

    def _loc_20DD(): pass

    label('loc_20DD')

    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230434V#064F#2P哎……不设置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230030V#060F那就等准备好以后\n',
            '再来这个地方调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230031V到时再进行设置工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    EventEnd(0x00)

    Return()

    def _loc_2170(): pass

    label('loc_2170')

    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x2175
@scena.Code('func_08_2175')
def func_08_2175():
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, 3460, -40, -46290, 90)
    ChrSetPos(0x0107, 4450, -20, -46910, 90)
    ChrSetPos(0x00F7, 3170, -40, -47550, 90)
    ChrSetPos(0x00F9, 4100, 70, -48420, 0)
    CameraMove(4450, -20, -46910, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070230442V#061F嗯，设置完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2363',
    )

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
            TXT(0x00, '【◇第一次设置测量仪】\n'),
            TXT(0x01, '【◇已经在托兰特平原设置了测量仪】\n'),
            TXT(0x02, '【◇已经在卡鲁迪亚隧道设置了测量仪】\n'),
            TXT(0x03, '【◇已经在卡鲁迪亚隧道和托兰特平原设置了测量仪】\n'),
            TXT(0x04, '【◇不变更】\n'),
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
        (0x00000000, 'loc_2333'),
        (0x00000001, 'loc_233F'),
        (0x00000002, 'loc_234B'),
        (0x00000003, 'loc_2357'),
        (-1, 'loc_2363'),
    )

    def _loc_2333(): pass

    label('loc_2333')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_2363')

    def _loc_233F(): pass

    label('loc_233F')

    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_2363')

    def _loc_234B(): pass

    label('loc_234B')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_2363')

    def _loc_2357(): pass

    label('loc_2357')

    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_2363')

    def _loc_2363(): pass

    label('loc_2363')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28C5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230443V#1004F#3P哟，组装起来以后\n',
            '原来是这个样子的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230039V#1015F不过……\n',
            '这个像盘子一样的东西是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230445V#060F#2P这叫碟型天线，\n',
            '是个可以集中导力波的天线。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230041V通过它可以把强力的导力波\n',
            '传送到很远的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230042V即使在卡鲁迪亚隧道那种地方\n',
            '也都一样可以传送到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2633',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230448V#033F哦……\n',
            '那可是很厉害的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230044V#030F那么…\n',
            '有打算在市面上销售吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230450V#560F啊，我也不是\n',
            '很清楚呢，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230046V不过，爷爷的发明一般在问世\n',
            '半年后就会在市面上销售了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230452V#031F呵，这真是令人期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2630',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230453V#027F哎呀……和你的『本职工作』有关吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230454V#035F我听不懂你在说什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2630(): pass

    label('loc_2630')

    Jump('loc_27E1')

    def _loc_2633(): pass

    label('loc_2633')

    ChrTalk(
        0x0105,
        (
            '#0060230455V#044F那个，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230051V我以前听说过，导力波遇到障碍物\n',
            '就会减弱，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230457V即使在卡鲁迪亚隧道那种地方\n',
            '那种地方也可以传送呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230458V#560F嗯，这种天线\n',
            '会赋予导力波指向性，\n',
            '所以可以顺利进行传送。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230054V即使是像洞窟那种地方，\n',
            '导力波似乎也能藉由墙壁反射\n',
            '持续传送到出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230460V#040F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230056V#041F不愧是拉赛尔博士啊，\n',
            '天才的称号果然不是浪得虚名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_27E1(): pass

    label('loc_27E1')

    ChrTalk(
        0x0101,
        (
            '#0010230462V#1007F#3P唔，虽然现在还\n',
            '无法亲身体会其厉害之处……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230058V#1006F不过这样一来就可以\n',
            '把地震情报传送出去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230464V#560F#2P啊，不是。\n',
            '还没有启动呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230465V现在就打开开关了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_292C')

    def _loc_28C5(): pass

    label('loc_28C5')

    ChrTalk(
        0x0101,
        (
            '#0010230466V#1006F#3P那么只剩下\n',
            '打开开关了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230467V#560F#2P嗯，我马上就打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_292C(): pass

    label('loc_292C')

    ChrSetDirection(0x0107, 90, 400)
    ChrSetDirection(0x00F9, 0, 400)
    Sleep(500)

    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 6)
    OP_0D()
    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    PlaySE(158, 0x01, 0x64)
    OP_24(0x009E, 0x4B)
    Sleep(2000)

    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B0D',
    )

    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230468V#061F#2P嗯⊙\n',
            '这样启动就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230469V#1006F#3P辛苦呢了，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230470V天线虽然看起来很容易坏掉，\n',
            '不过放在这里的话就不用担心会有魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230471V#560F#2P嗯，而且这个装置\n',
            '有类似街灯一样\n',
            '驱赶魔兽的功能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230472V所以就算设置在其它地方，\n',
            '我想也不必担心会有什么事情发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230473V#1011F#3P是吗，那我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B9D')

    def _loc_2B0D(): pass

    label('loc_2B0D')

    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230468V#061F#2P嗯⊙\n',
            '这样启动就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2B75',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230475V#051F#6P哦，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B9D')

    def _loc_2B75(): pass

    label('loc_2B75')

    ChrTalk(
        0x0103,
        (
            '#0030230476V#021F#6P呵呵，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B9D(): pass

    label('loc_2B9D')

    ChrSetPos(0x000A, 1460, 250, -34530, 180)
    ChrClearFlags(0x000A, 0x0080)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0160230477V#4P哟，你们在工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230478V#1004F#3P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C0C')
    def lambda_2C0C():
        CameraMove(2480, -90, -43470, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C0C)

    @scena.Lambda('lambda_2C24')
    def lambda_2C24():
        OP_67(0, 8500, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2C24)

    @scena.Lambda('lambda_2C3C')
    def lambda_2C3C():
        ChrWalkTo(0x000A, 1460, 180, -39370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2C3C)

    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0107, 0, 400)
    ChrSetDirection(0x00F7, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x000A, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010230479V#1004F#2P#3S老爸！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2D2F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230480V#052F#6P大叔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D53')

    def _loc_2D2F(): pass

    label('loc_2D2F')

    ChrTalk(
        0x0103,
        (
            '#0030230481V#023F#6P老师……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D53(): pass

    label('loc_2D53')

    @scena.Lambda('lambda_2D59')
    def lambda_2D59():
        CameraMove(1780, 0, -41760, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D59)

    CreateThread(0x0101, 0x00, 0x00, func_09_4ECC)
    Sleep(200)

    @scena.Lambda('lambda_2D7D')
    def lambda_2D7D():
        ChrWalkTo(0x00FE, 1560, 0, -40860, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2D7D)

    CreateThread(0x00F7, 0x00, 0x00, func_0B_4F04)
    Sleep(300)

    CreateThread(0x0107, 0x00, 0x00, func_0A_4EE8)
    Sleep(200)

    CreateThread(0x00F9, 0x00, 0x00, func_0C_4F20)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x000A, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0160230482V#1120F#5P好久不见了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230483V虽然说得有些晚，\n',
            '不过强化训练，真是辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0107, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010230484V#1008F#4P真是的～！\n',
            '不是辛苦不辛苦的问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230485V什么啊，老爸。\n',
            '你怎么在这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230486V#1120F#5P哈哈，别忘了我可是个军人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230487V这里是作战总部的据点，\n',
            '所以大多数时间都会在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230488V#1017F#4P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F86',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230489V#051F#6P听说你当上\n',
            '作战总部长了是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FBD')

    def _loc_2F86(): pass

    label('loc_2F86')

    ChrTalk(
        0x0103,
        (
            '#0030230490V#020F#6P听说你当上\n',
            '作战总部长了是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FBD(): pass

    label('loc_2FBD')

    ChrTalk(
        0x000A,
        (
            '#0160230491V#1123F#5P嗯，摩尔根将军\n',
            '三番五次地劝说我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230492V最后实在拗不过他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230493V所以现在搞得天天连点休息的时间也都没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3141',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230494V#051F#6P嘿嘿，这叫平日\n',
            '『积德』所致。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230495V#1016F#4P哈哈，您就不要抱怨了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230496V#1006F不过，老爸穿军服的样子\n',
            '乍一看，还真感觉有点不协调，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230497V但仔细看看也挺\n',
            '有板有眼的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_321F')

    def _loc_3141(): pass

    label('loc_3141')

    ChrTalk(
        0x0103,
        (
            '#0030230498V#021F#6P呵呵，您辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230499V#1016F#4P不过老爸\n',
            '说不定算是自作自受呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230496V#1006F不过，老爸穿军服的样子\n',
            '乍一看，还真感觉有点不协调，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230497V但仔细看看也挺\n',
            '有板有眼的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_321F(): pass

    label('loc_321F')

    ChrTalk(
        0x000A,
        (
            '#0160230502V#1121F#5P哼哼，那是当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230503V我以前可是号称\n',
            '王国军第一美男子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230504V理查德算得了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230505V#1007F#4P真是的，马上就得意忘形了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230506V#1017F嘿嘿……不过太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230507V听说你那么忙\n',
            '我还有点担心呢，\n',
            '不过看上去您比我想象中还要有精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230508V#1125F#5P嗯，现在还算好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230509V#1122F话说回来……\n',
            '我已经看过来自协会的报告书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230510V他们似乎已经在卢安开始行动了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230511V#1003F#4P啊……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230512V#1002F『噬身之蛇』的党羽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_34AC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230513V#050F#6P和报告书上写的一样，\n',
            '那些家伙比预料中的还要厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230514V军方不准备拟定相应的对策吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3525')

    def _loc_34AC(): pass

    label('loc_34AC')

    ChrTalk(
        0x0103,
        (
            '#0030230515V#022F#6P和报告书上写的一样，\n',
            '看来那些家伙比预料中的还要危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230516V军方不准备拟定相应的对策吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3525(): pass

    label('loc_3525')

    ChrTalk(
        0x000A,
        (
            '#0160230517V#1125F#5P嗯，要是能尽快建立起一个\n',
            '可以代替情报部的机构就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230518V正规军和国境师团的改组\n',
            '总算是刚结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230519V#1120F目前，有关调查的事情\n',
            '只能暂时拜托协会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230520V关于这次的怪异地震\n',
            '也指望着你们能调查出一些眉目出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_366D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230521V#551F#6P真是的……\n',
            '我就知道是这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3695')

    def _loc_366D(): pass

    label('loc_366D')

    ChrTalk(
        0x0103,
        (
            '#0030230522V#027F#6P呵呵，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3695(): pass

    label('loc_3695')

    ChrTalk(
        0x0101,
        (
            '#0010230523V#1006F#4P反正老爸平时也\n',
            '很少拜托我做什么事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230524V这次，就当是我孝敬您吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230525V#1120F#5P噢，什么时候开始变得会那么说话了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230526V你的新衣服也挺合适的，\n',
            '似乎多了点点女人味了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230527V如果约修亚看到你现在这个样子，一定会感到很吃惊的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230528V#1025F#4P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230529V#1016F嘿嘿，真是那样的话就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000B, 690, 250, -31680, 180)
    ChrClearFlags(0x000B, 0x0080)

    NpcTalk(
        0x000B,
        '男性的声音',
        (
            '#0620230530V#4P卡西乌斯准将！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    @scena.Lambda('lambda_3865')
    def lambda_3865():
        CameraMove(1780, 0, -39760, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3865)

    @scena.Lambda('lambda_387D')
    def lambda_387D():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_387D)

    ChrWalkTo(0x000B, 510, 250, -38760, 2500, 0x00)

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3905',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230533V#1004F#4P啊……希德少校！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3902',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230534V#052F#6P还真是好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3902(): pass

    label('loc_3902')

    Jump('loc_3961')

    def _loc_3905(): pass

    label('loc_3905')

    ChrTalk(
        0x0101,
        (
            '#0010230531V#1011F#4P啊……希德中校！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3961',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230532V#051F#6P哟，又见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3961(): pass

    label('loc_3961')

    @scena.Lambda('lambda_3967')
    def lambda_3967():
        CameraMove(1780, 0, -41760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3967)

    @scena.Lambda('lambda_397F')
    def lambda_397F():
        ChrWalkTo(0x000B, 510, 0, -40760, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_397F)

    Sleep(1000)

    ChrTurnDirection(0x000A, 0x00F9, 400)
    WaitForThreadExit(0x000B, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x006D, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DA4',
    )

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620230535V#701F哈哈，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230536V拉赛尔博士绑架事件时\n',
            '给你们添了不少麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230537V我一直打算有机会的话\n',
            '要好好地向你们道歉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230538V#1016F#4P哈哈，没关系啦。\n',
            '你不是也放我们逃跑了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230539V#560F那个那个……\n',
            '真是非常感谢您的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000B,
        '希德',
        (
            '#0620230540V#703F是吗……\n',
            '你们能这么想我真是松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230541V#1120F#5P顺便说一下\n',
            '由于在镇压政变时的活跃表现，\n',
            '希德最近已经升任为中校了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230542V今后你们就叫他希德中校吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#0620230543V#702F#6P准、准将……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230544V#1011F#4P哟～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230545V#1001F恭喜你，希德中校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230546V#061F恭喜恭喜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3C97',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230547V#051F#6P哈哈，这不是好事吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230548V像你这样的人\n',
            '就应该得到相当高的评价。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C97(): pass

    label('loc_3C97')

    ChrTurnDirection(0x000B, 0x00F7, 400)

    ChrTalk(
        0x000B,
        (
            '#0620230549V#701F那个……谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230550V我只是做了我应该做的事，\n',
            '真有点不太好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230551V#1006F#4P又来了～\n',
            '你真是个谦虚的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230552V#1125F#5P嗯，希德你也应该再\n',
            '多担负起一些责任来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230553V不然，我到什么时候\n',
            '才能引退啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFF')

    def _loc_3DA4(): pass

    label('loc_3DA4')

    ChrTalk(
        0x000A,
        (
            '#0160230554V#1124F#5P哟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230555V你们已经打过招呼了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620230556V#701F是，在那次特别训练中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230557V托你们的福，\n',
            '训练也获得了很好的成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230558V#1125F#5P是吗，看来我不在的时候\n',
            '你干得不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230559V既然晋升中校了，那就期待希德你\n',
            '今后能表现的更加活跃一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230553V不然，我到什么时候\n',
            '才能引退啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3EFF(): pass

    label('loc_3EFF')

    ChrSetDirection(0x000B, 90, 400)

    ChrTalk(
        0x000B,
        (
            '#0620230561V#702F#6P过奖了，不过，要是您轻易引退的话，\n',
            '我们会感到很为难的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230562V至少也请等到\n',
            '摩尔根将军退役之后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230563V#1123F#5P啊，那要等到何年何月啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#0160230564V#1124F#5P对了，希德。\n',
            '你不是有事找我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0620230565V#700F#6P是的，摩尔根将军说\n',
            '会比预定的时间提早到达。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620230566V再过一会儿\n',
            '就会到达起降场了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230567V#1125F#5P没办法……\n',
            '那位大人也真性急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)
    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#0160230568V#1120F#5P……好了\n',
            '我要去参加军事会议了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230569V真抱歉，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230570V#1017F#4P没关系，别介意。\n',
            '能跟你说上几句话，我就已经很开心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230571V#1120F#5P嗯，我也一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x00F7, 400)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_424C',
    )

    ChrTalk(
        0x000A,
        (
            '#0160230572V#1120F#5P阿加特。\n',
            '不好意思，艾丝蒂尔就拜托你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230573V虽然她已经是一名正游击士了，\n',
            '但是，肯定经验还尚浅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050230574V#051F#6P嗯，放心交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42FD')

    def _loc_424C(): pass

    label('loc_424C')

    ChrTalk(
        0x000A,
        (
            '#0160230575V#1120F#5P雪拉扎德。\n',
            '不好意思，艾丝蒂尔就拜托你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230573V虽然她已经是一名正游击士了，\n',
            '但是，肯定经验还尚浅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230577V#027F#6P嗯，放心交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42FD(): pass

    label('loc_42FD')

    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0160230578V#1121F#5P提妲你也\n',
            '很努力嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230579V虽然你姐姐不成器，\n',
            '不过还是请多帮助她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230580V#067F嘿嘿，我知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230581V#560F另外，关于\n',
            '『福音』的解析……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230582V爷爷兴奋地说他\n',
            '找到了意想不到的关键点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230583V#1120F#5P是吗……\n',
            '这可真令人期待。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230584V替我向博士问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230585V#061F是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45F4',
    )

    ChrTalk(
        0x000A,
        (
            '#0160230586V#1120F#5P听说奥利维尔\n',
            '也在帮我那个不成器的女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230587V抛开那件事不说，我还是要谢谢你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230588V#035F#6P呵呵，您客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230589V#030F难得一看的歌剧第二幕。\n',
            '我没理由不参加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230590V#1125F#5P呵呵……也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230591V#1120F不过也别忘了\n',
            '你自己的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230592V#031F#6P嗯，我会谨记在心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230593V#1015F#2P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47E5')

    def _loc_45F4(): pass

    label('loc_45F4')

    ChrTalk(
        0x000A,
        (
            '#0160230594V#1125F#5P公主殿下，也感谢您\n',
            '帮助我这个不成器的女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230595V#1120F不过，有机会的话也请您\n',
            '能把自己的想法说给周围人听吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230596V不论陛下是怎么想的，\n',
            '尤莉亚上尉和摩尔根将军他们\n',
            '看上去似乎都有些焦虑不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230597V#047F#4P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230598V#040F我会找机会好好跟他们说明\n',
            '并寻求他们的理解的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230599V我需要进行一次\n',
            '找寻自我的旅程……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230600V#1120F#5P哈呵呵，殿下您\n',
            '一定能成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230601V#048F#4P谢谢……\n',
            '能听到你说这句话，我就安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47E5(): pass

    label('loc_47E5')

    ChrTalk(
        0x000A,
        (
            '#0160230602V#1125F#5P……那么我就先走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230603V#1120F虽然无法直接帮助你们，\n',
            '不过，如果有协会应付不了的事情\n',
            '就随时联系我好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230604V我会尽力协助你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230605V#1006F#4P嗯……\n',
            '我会记住的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230606V#1018F老爸你也要努力工作啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0160230607V#1121F#5P哈哈，我自然知道会怎么做\n',
            '而不至于被摩尔根将军所骂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#0160230608V#1120F#2P希德，我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 90, 400)

    ChrTalk(
        0x000B,
        (
            '#0620230609V#701F#6P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 0, 400)

    @scena.Lambda('lambda_499C')
    def lambda_499C():
        ChrMoveToRelative(0x00FE, 0, 0, 14000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_499C)

    Sleep(600)

    ChrSetDirection(0x000B, 0, 400)

    @scena.Lambda('lambda_49C3')
    def lambda_49C3():
        ChrMoveToRelative(0x00FE, 0, 0, 14000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_49C3)

    @scena.Lambda('lambda_49DE')
    def lambda_49DE():
        CameraMove(1780, 250, -37820, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_49DE)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_4A05')
    def lambda_4A05():
        CameraMove(1780, 0, -41540, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4A05)

    @scena.Lambda('lambda_4A1D')
    def lambda_4A1D():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4A1D)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010230610V#1017F#5P唔～老爸他们比我\n',
            '想象中的还要忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230611V既然如此，作为游击士协会\n',
            '理所当然也不能输给他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4B1B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230612V#051F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230613V好好做出成果来\n',
            '让大叔刮目相看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B75')

    def _loc_4B1B(): pass

    label('loc_4B1B')

    ChrTalk(
        0x0103,
        (
            '#0030230614V#021F#6P呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230615V#020F好好做出成果来\n',
            '让老师也吃一惊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B75(): pass

    label('loc_4B75')

    ChrSetDirection(0x00F7, 90, 400)
    ChrSetDirection(0x0101, 270, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4C03',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230616V#051F#6P好，这个地方就ＯＫ了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230617V保持这种步调，\n',
            '将剩下的测量仪也设置完毕吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C68')

    def _loc_4C03(): pass

    label('loc_4C03')

    ChrTalk(
        0x0103,
        (
            '#0030230618V#027F#6P好，这个地方就搞定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230619V保持这种步调，\n',
            '继续设置剩下的测量仪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C68(): pass

    label('loc_4C68')

    ChrTalk(
        0x0101,
        (
            '#0010230620V#1006F#2P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EBC')

    def _loc_4C8C(): pass

    label('loc_4C8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4D69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4CF3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230621V#051F#6P好，这是第二个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230098V去把最后一个也搞定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D45')

    def _loc_4CF3(): pass

    label('loc_4CF3')

    ChrTalk(
        0x0103,
        (
            '#0030230623V#526F#6P那么，这是第二个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230100V马上去设置最后一个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D45(): pass

    label('loc_4D45')

    ChrTalk(
        0x0101,
        (
            '#0010230625V#1000F#2PＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EBC')

    def _loc_4D69(): pass

    label('loc_4D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4DF1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230626V#051F#6P好，这样一来所有的\n',
            '测量仪都设置完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230103V老爷子还在等着我们，\n',
            '赶快去中央工房的演算室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E7E')

    def _loc_4DF1(): pass

    label('loc_4DF1')

    ChrTalk(
        0x0103,
        (
            '#0030230628V#026F#6P那么，这样一来所有的\n',
            '测量仪都设置完毕了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230105V#020F拉赛尔博士还在等着我们，\n',
            '现在就回中央工房的演算室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E7E(): pass

    label('loc_4E7E')

    ChrTalk(
        0x0101,
        (
            '#0010230630V#1006F#2PＯＫ。\n',
            '就在中央工房的５楼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0087, 0x01, 0x0200)
    def _loc_4EBC(): pass

    label('loc_4EBC')

    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))
    OP_28(0x0087, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x4ECC
@scena.Code('func_09_4ECC')
def func_09_4ECC():
    ChrWalkTo(0x0101, 1870, 0, -42120, 2500, 0x00)
    ChrSetDirection(0x0101, 0, 400)

    Return()

# id: 0x000A offset: 0x4EE8
@scena.Code('func_0A_4EE8')
def func_0A_4EE8():
    ChrWalkTo(0x0107, 1980, -70, -43370, 2000, 0x00)
    ChrSetDirection(0x0107, 0, 400)

    Return()

# id: 0x000B offset: 0x4F04
@scena.Code('func_0B_4F04')
def func_0B_4F04():
    ChrWalkTo(0x00F7, 780, 0, -42240, 2500, 0x00)
    ChrSetDirection(0x00F7, 0, 400)

    Return()

# id: 0x000C offset: 0x4F20
@scena.Code('func_0C_4F20')
def func_0C_4F20():
    ChrWalkTo(0x00F9, 970, -50, -43410, 2000, 0x00)
    ChrSetDirection(0x00F9, 0, 400)

    Return()

# id: 0x000D offset: 0x4F3C
@scena.Code('func_0D_4F3C')
def func_0D_4F3C():
    EventBegin(0x00)
    CameraMove(7290, 8370, -11590, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2880, 0)
    OP_6C(310000, 0)
    OP_6E(326, 0)
    OP_E5(0x09, 0x00, 0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 41020, 8200, -35260, 270)

    @scena.Lambda('lambda_4FB4')
    def lambda_4FB4():
        CameraMove(38570, 8950, -35140, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4FB4)

    @scena.Lambda('lambda_4FCC')
    def lambda_4FCC():
        OP_67(0, 3000, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4FCC)

    @scena.Lambda('lambda_4FE4')
    def lambda_4FE4():
        OP_6C(315000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4FE4)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0610240107V#1182F#6P监视塔上有导力感应器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610240108V水中设置鱼雷群……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610240109V防守果然是滴水不漏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610240110V#1322F呼，没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610240111V还是像他们说的一样，\n',
            '只能使用那个东西了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    ChrSetDirection(0x0008, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0610240112V#1181F#5P阁下……很快就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610240113V请再等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_24(0x01CD, 0x5A)
    Sleep(200)

    OP_24(0x01CD, 0x50)
    Sleep(200)

    OP_24(0x01CD, 0x46)
    Sleep(200)

    OP_24(0x01CD, 0x3C)
    Sleep(200)

    OP_24(0x01CD, 0x32)
    Sleep(200)

    OP_24(0x01CD, 0x28)
    Sleep(200)

    OP_24(0x01CD, 0x1E)
    Sleep(200)

    OP_23(0x01CD)
    OP_0D()
    OP_AD('ED6_DT24/C_VIS143._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    SetScenaFlags(ScenaFlag(0x02C0, 0, 0x1600))
    NewScene('ED6_DT21/T3100._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x51B4
@scena.Code('func_0E_51B4')
def func_0E_51B4():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(40, 3450, -7970, 0)
    OP_67(0, 3180, -10000, 0)
    CameraSetDistance(4019, 0)
    OP_6C(330000, 0)
    OP_6E(496, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC10._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C3110._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x5243
@scena.Code('func_0F_5243')
def func_0F_5243():
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
        'loc_5263',
    )

    Call(0, 0x0012)
    Call(0, 0x0014)
    FadeIn(0, 0)

    def _loc_5263(): pass

    label('loc_5263')

    OP_4A(0x0009, 255)
    Fade(1000)
    ChrSetPos(0x0101, -440, 0, -4750, 0)
    ChrSetPos(0x0102, 590, 0, -4750, 0)
    ChrSetPos(0x00F8, -840, 150, -6050, 0)
    ChrSetPos(0x00F9, 480, 100, -6050, 0)
    ChrSetDirection(0x0009, 180, 0)
    CameraMove(800, 0, -3520, 0)
    OP_67(0, 7630, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#3110370441V#5P你们……\n',
            '我记得你们是游击士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370442V雷斯顿要塞现在\n',
            '已经处于紧急警戒状态了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370443V没有紧要事情的话\n',
            '就请你们回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370444V#1015F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370445V卡西乌斯准将\n',
            '现在在要塞里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110370446V#5P当然在……\n',
            '因为通讯障碍和导力兵器的停止\n',
            '王国军正陷入大混乱之中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370447V为了重整指挥系统\n',
            '准将大人日夜不停地在\n',
            '向各地做出指示。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370448V就算是游击士\n',
            '也没办法让你们见他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370449V#1025F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370450V#1035F#4P请问……\n',
            '能不能通融一下呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370451V#1043F其实她是准将的女儿。',
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
            '#3110370452V#5P是、是吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370453V倒是听说过他有个\n',
            '当游击士的女儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370454V要是这样的话就另当别论了！\n',
            '我现在马上去报告！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370455V#1004F#6P啊，不用了。\n',
            '还是算了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370456V#1008F我也不想在他这么忙的时候\n',
            '打扰他的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020370457V#1044F#2P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56C4',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030370458V#524F#6P只是一小会儿的话\n',
            '应该无所谓吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_5777')

    def _loc_56C4(): pass

    label('loc_56C4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_571C',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050370459V#555F#6P只是一小会儿的话\n',
            '应该无所谓吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_5777')

    def _loc_571C(): pass

    label('loc_571C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5777',
    )

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080370460V#072F#6P只是一小会儿的话\n',
            '我想应该无所谓吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    def _loc_5777(): pass

    label('loc_5777')

    ChrTalk(
        0x0101,
        (
            '#0010370461V#1011F#5P我和老爸都有\n',
            '自己该走的路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370462V#1012F老爸那边在努力的话，\n',
            '我们的工作也会变得更加轻松些……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370463V而我们多努力一点的话，\n',
            '我想，老爸的工作也会稍微轻松一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370464V#1006F所以现在还是不要去打扰他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58A4',
    )

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370465V#560F#4P姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58A4(): pass

    label('loc_58A4')

    ChrTalk(
        0x0102,
        (
            '#0020370466V#1053F#2P这样啊……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_58D7')
    def lambda_58D7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_58D7)

    Sleep(100)

    @scena.Lambda('lambda_58EA')
    def lambda_58EA():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_58EA)

    Sleep(100)

    @scena.Lambda('lambda_58FD')
    def lambda_58FD():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_58FD)

    Sleep(100)

    ChrSetDirection(0x00F8, 0, 400)
    Sleep(200)

    ChrTalk(
        0x0102,
        (
            '#0020370467V#1040F#4P那么我们就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370468V有机会的话\n',
            '替我们向准将问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110370469V#5P嗯……当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370470V我会在他吃饭的时候\n',
            '报告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370471V#1017F#6P嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0401, 5, 0x200D))
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x59E9
@scena.Code('func_10_59E9')
def func_10_59E9():
    TalkBegin(0x0009)
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
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A45',
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【说话】\n'),
            TXT(0x01, '【询问关于内燃机的事】\n'),
            TXT(0x02, '【离开】\n'),
        ),
    )

    Jump('loc_5A60')

    def _loc_5A45(): pass

    label('loc_5A45')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【说话】\n'),
            TXT(0x01, '【离开】\n'),
        ),
    )

    def _loc_5A60(): pass

    label('loc_5A60')

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
        'loc_5B14',
    )

    ChrTalk(
        0x0009,
        (
            '卡西乌斯准将\n',
            '为了重整混乱的王国军\n',
            '正向各地发出指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然说是紧急情况，\n',
            '但是他那不眠不休地进行指挥的身影，\n',
            '真可说是全军的楷模。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BAB')

    def _loc_5B14(): pass

    label('loc_5B14')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B36',
    )

    Call(0, 0x0011)

    Jump('loc_5BAB')

    def _loc_5B36(): pass

    label('loc_5B36')

    ChrTalk(
        0x0009,
        (
            '根据亲卫队传来的消息，\n',
            '雷斯顿要塞的通讯功能\n',
            '正在逐步恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今后如果有紧急的事情\n',
            '就直接从协会支部联络好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BAB(): pass

    label('loc_5BAB')

    TalkEnd(0x0009)

    Return()

# id: 0x0011 offset: 0x5BAF
@scena.Code('func_11_5BAF')
def func_11_5BAF():
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
        'loc_5BCF',
    )

    Call(0, 0x0012)
    Call(0, 0x0014)
    FadeIn(0, 0)

    def _loc_5BCF(): pass

    label('loc_5BCF')

    Fade(1000)
    ChrSetPos(0x0101, -440, 0, -4750, 0)
    ChrSetPos(0x0102, 590, 0, -4750, 0)
    ChrSetPos(0x00F8, -840, 150, -6050, 0)
    ChrSetPos(0x00F9, 480, 100, -6050, 0)
    ChrSetPos(0x0009, 500, 0, -3240, 0)
    ChrSetDirection(0x0009, 180, 0)
    ChrSetSubChip(0x0009, 0)
    CameraMove(800, 0, -3520, 0)
    OP_67(0, 7630, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人说明了情况\n',
            '询问了关于内燃机的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#3110370472V#5P唔，虽然不清楚是什么事，\n',
            '不过听起来好像相当重要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370473V你们在这里等着。\n',
            '我现在就去问问看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)

    @scena.Lambda('lambda_5D4F')
    def lambda_5D4F():
        ChrMoveToRelative(0x00FE, 0, 0, 6800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5D4F)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(2000)

    WaitForThreadExit(0x0009, 0x0001)
    FadeIn(2000, 0)
    ChrWalkTo(0x0009, 500, 0, -3240, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#3110370474V#5P我去问了负责人──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370475V这座要塞里好像\n',
            '没有那个什么『内燃机』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(70)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E51',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5E8F')

    def _loc_5E51(): pass

    label('loc_5E51')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E78',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5E8F')

    def _loc_5E78(): pass

    label('loc_5E78')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5E8F(): pass

    label('loc_5E8F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5EB6',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5EF4')

    def _loc_5EB6(): pass

    label('loc_5EB6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5EDD',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_5EF4')

    def _loc_5EDD(): pass

    label('loc_5EDD')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_5EF4(): pass

    label('loc_5EF4')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010370476V#1009F#6P怎、怎么可能！\n',
            '维修长说了在这里啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3110370477V#5P我只是说『这座要塞』里没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370478V似乎刚好为了要归还给中央工房\n',
            '而装进了一艘警备艇里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370479V听说那艘警备艇因为那个异常现象\n',
            '而紧急着陆在托兰特平原了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370480V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6056',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370481V#070F#6P原来如此，是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60D5')

    def _loc_6056(): pass

    label('loc_6056')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6093',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370482V#027F#6P原来是这么一回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60D5')

    def _loc_6093(): pass

    label('loc_6093')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_60D5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370483V#051F#6P原来如此，事情是那样的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_60D5(): pass

    label('loc_60D5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_612F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370484V#560F#6P这么说，只要拜托\n',
            '那艘警备艇上的士兵就可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6179')

    def _loc_612F(): pass

    label('loc_612F')

    ChrTalk(
        0x0102,
        (
            '#0020370485V#1040F#4P这么说，只要拜托\n',
            '那艘警备艇的负责人就可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6179(): pass

    label('loc_6179')

    ChrTalk(
        0x0009,
        (
            '#3110370486V#5P嗯，麻烦你们\n',
            '去那边看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3110370487V警备艇应该在托兰特平原的\n',
            '某个地方才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetScenaFlags(ScenaFlag(0x0401, 6, 0x200E))
    OP_28(0x00C2, 0x01, 0x0020)
    OP_28(0x00C2, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x61F5
@scena.Code('func_12_61F5')
def func_12_61F5():
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
        (0x00000000, 'loc_626F'),
        (0x00000001, 'loc_6275'),
        (-1, 'loc_627B'),
    )

    def _loc_626F(): pass

    label('loc_626F')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_627B')

    def _loc_6275(): pass

    label('loc_6275')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_627B')

    def _loc_627B(): pass

    label('loc_627B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_6289',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_628D')

    def _loc_6289(): pass

    label('loc_6289')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_628D(): pass

    label('loc_628D')

    Return()

# id: 0x0013 offset: 0x628E
@scena.Code('func_13_628E')
def func_13_628E():
    MapClearFlags(0x00000001)
    CameraMove(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_62C8',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    Jump('loc_62E2')

    def _loc_62C8(): pass

    label('loc_62C8')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    def _loc_62E2(): pass

    label('loc_62E2')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0014 offset: 0x62F4
@scena.Code('func_14_62F4')
def func_14_62F4():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0015 offset: 0x634D
@scena.Code('func_15_634D')
def func_15_634D():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　警告！　　　　\n',
            '禁止在军事区域摄影',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0016 offset: 0x63A9
@scena.Code('func_16_63A9')
def func_16_63A9():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_63E1')
    def lambda_63E1():
        CameraMove(32020, -50, -31290, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_63E1)

    @scena.Lambda('lambda_63F9')
    def lambda_63F9():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_63F9)

    @scena.Lambda('lambda_6411')
    def lambda_6411():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_6411)

    @scena.Lambda('lambda_6421')
    def lambda_6421():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_6421)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_64A8',
    )

    OP_C0(0x0E, 0x00000024, 0x00007E71, 0xFFFFFFCE, 0xFFFF813E, 0x00000000, 0x00007A08, 0xFFFFFE0C, 0xFFFF8AE4)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_64B7')

    def _loc_64A8(): pass

    label('loc_64A8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_64B7',
    )

    EventEnd(0x01)

    def _loc_64B7(): pass

    label('loc_64B7')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
