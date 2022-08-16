import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4402.x'
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '菲利奥',
            x                   = 500,
            z                   = 0,
            y                   = 540,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 1520,
            z                   = 0,
            y                   = 9460,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = 3010,
            z                   = 0,
            y                   = 400,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '菲',
            x                   = 2520,
            z                   = 0,
            y                   = 9450,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '桑顿',
            x                   = 6550,
            z                   = 0,
            y                   = 11890,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1050,
            triggerZ            = 0,
            triggerY            = 7890,
            triggerRange        = 800,
            actorX              = 150,
            actorZ              = 1700,
            actorY              = 7890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1050,
            triggerZ            = 0,
            triggerY            = 10640,
            triggerRange        = 800,
            actorX              = 150,
            actorZ              = 1700,
            actorY              = 10640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1720,
            triggerZ            = 0,
            triggerY            = 540,
            triggerRange        = 600,
            actorX              = 500,
            actorZ              = 1500,
            actorY              = 540,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1F9',
    )

    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_20A')

    def _loc_1F9(): pass

    label('loc_1F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_20A',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)

    def _loc_20A(): pass

    label('loc_20A')

    Return()

# id: 0x0001 offset: 0x20B
@scena.Code('func_01_20B')
def func_01_20B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22B',
    )

    OP_B1('t4402_y')

    Jump('loc_234')

    def _loc_22B(): pass

    label('loc_22B')

    OP_B1('t4402_n')

    def _loc_234(): pass

    label('loc_234')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_255',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)

    Jump('loc_273')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_273',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)

    def _loc_273(): pass

    label('loc_273')

    Return()

# id: 0x0002 offset: 0x274
@scena.Code('func_02_274')
def func_02_274():
    ExecExpressionWithReg(
        0x0001,
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
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_299',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3DB')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B2',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3DB')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CB',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3DB')

    def _loc_2CB(): pass

    label('loc_2CB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E4',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3DB')

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FD',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3DB')

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_316',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3DB')

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3DB')

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_348',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3DB')

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_361',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3DB')

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3DB')

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_393',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3DB')

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3DB')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3DB')

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3DB')

    def _loc_3F0(): pass

    label('loc_3F0')

    Return()

# id: 0x0003 offset: 0x3F1
@scena.Code('func_03_3F1')
def func_03_3F1():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x3F6
@scena.Code('func_04_3F6')
def func_04_3F6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_409',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_41F')

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x00, 0x80)"),
            Expr.Return,
        ),
        'loc_419',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_41F')

    def _loc_419(): pass

    label('loc_419')

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_41F(): pass

    label('loc_41F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A7',
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
            TXT(0x00, '【◇QST104成功】\n'),
            TXT(0x01, '【◇QST104失败】\n'),
            TXT(0x02, '【◇QST104过期】\n'),
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
        (0x00000000, 'loc_492'),
        (0x00000001, 'loc_498'),
        (0x00000002, 'loc_49E'),
        (-1, 'loc_4A7'),
    )

    def _loc_492(): pass

    label('loc_492')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_4A7')

    def _loc_498(): pass

    label('loc_498')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_4A7')

    def _loc_49E(): pass

    label('loc_49E')

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_4A7')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_609',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_606',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_508',
    )

    ChrTalk(
        0x0008,
        (
            '我已不再玩了\n',
            '和妻子约好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说起来，飞船\n',
            '也还是不能动啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_606')

    def _loc_508(): pass

    label('loc_508')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_596',
    )

    ChrTalk(
        0x0008,
        (
            '……卢安的游戏吧\n',
            '好像没用导力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '反正也不能工作，\n',
            '再去游戏吧玩玩也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唔，我这蠢材蠢材蠢材！\n',
            '约定不再玩了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_606')

    def _loc_596(): pass

    label('loc_596')

    ChrTalk(
        0x0008,
        (
            '因为这个异常现象\n',
            '和卢安联络不上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '船何时到达\n',
            '完全都不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……既然导力停了\n',
            '难道船也停了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_606(): pass

    label('loc_606')

    Jump('loc_FF6')

    def _loc_609(): pass

    label('loc_609')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_81E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 5, 0x1655)),
            Expr.Return,
        ),
        'loc_67E',
    )

    ChrTalk(
        0x0008,
        (
            '今后要请求王国军合作\n',
            '来保护引擎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了保证不被夺走\n',
            '好好管理到签字仪式当日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_81B')

    def _loc_67E(): pass

    label('loc_67E')

    ChrTalk(
        0x0008,
        (
            '你，你们……\n',
            '那天晚上的游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯！在协会\n',
            '是来看看情况的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '多亏你们\n',
            '新型引擎的样品\n',
            '也平安返回了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是给大家添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_73D',
    )

    ChrTalk(
        0x0106,
        (
            '#050F警备方面没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75A')

    def _loc_73D(): pass

    label('loc_73D')

    ChrTalk(
        0x0103,
        (
            '#020F警备方面没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_75A(): pass

    label('loc_75A')

    ChrTalk(
        0x0008,
        (
            '那个事件以来，似乎\n',
            '王国军也愿意合作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不管怎么，这可是缔结互不侵犯条约\n',
            '不可或缺的重要之物嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们如果也有\n',
            '要存在仓库的东西，\n',
            '请尽管开口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊哈哈，有机会的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CA, 5, 0x1655))

    def _loc_81B(): pass

    label('loc_81B')

    Jump('loc_FF6')

    def _loc_81E(): pass

    label('loc_81E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_8AD',
    )

    ChrTalk(
        0x0008,
        (
            '新型引擎的样品\n',
            '签字仪式的那天前都保管在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这个事务所本身，\n',
            '原本也是出租仓库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里经常有人待着，\n',
            '警备也相当严格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FF6')

    def _loc_8AD(): pass

    label('loc_8AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_98E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_8FD',
    )

    ChrTalk(
        0x0008,
        (
            '妻子给我送了便当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今后夜班会增加，\n',
            '可得加油才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98B')

    def _loc_8FD(): pass

    label('loc_8FD')

    ChrTalk(
        0x0008,
        (
            '妻子给我送了便当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样的我\n',
            '也会想到啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……今天预定有\n',
            '非常重要的东西存到仓库来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今后夜班会增加，\n',
            '可得加油才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_98B(): pass

    label('loc_98B')

    Jump('loc_FF6')

    def _loc_98E(): pass

    label('loc_98E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Or,
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 4, 0x1654)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A27',
    )

    ChrTalk(
        0x0008,
        (
            '想起来，我可是\n',
            '尽给妻子添麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '没有钱还搬来王都，\n',
            '沉沦这个又输光光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样果然是不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9D')

    def _loc_A27(): pass

    label('loc_A27')

    ChrTalk(
        0x0008,
        (
            '呼，妻子简直\n',
            '变得像外人一样严厉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '早上不知不觉睡过头了\n',
            '穿着睡衣就跑出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼呼，看来睡狮\n',
            '觉醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_A9D(): pass

    label('loc_A9D')

    Jump('loc_BF1')

    def _loc_AA0(): pass

    label('loc_AA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_B25',
    )

    ChrTalk(
        0x0008,
        (
            '去游戏吧旅行\n',
            '也让妻子够受的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……不过让她吃苦\n',
            '也不是这次才开始的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想起来，结婚以后我一直\n',
            '给妻子添麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF1')

    def _loc_B25(): pass

    label('loc_B25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_BF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B88',
    )

    ChrTalk(
        0x0008,
        (
            '这里是管理港湾区\n',
            '工作的事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '接受货轮的搬运\n',
            '和使用出租仓库的请求哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF1')

    def _loc_B88(): pass

    label('loc_B88')

    ChrTalk(
        0x0008,
        (
            '哎呀，客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里是管理港湾区\n',
            '工作的事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '接受货轮的搬运\n',
            '和使用出租仓库的要求哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_BF1(): pass

    label('loc_BF1')

    Jump('loc_C46')

    def _loc_BF4(): pass

    label('loc_BF4')

    ChrTalk(
        0x0008,
        (
            '这里是管理港湾区\n',
            '工作的事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '接受货轮的搬运\n',
            '和使用出租仓库的要求哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_C46(): pass

    label('loc_C46')

    Jump('loc_FF6')

    def _loc_C49(): pass

    label('loc_C49')

    ChrTalk(
        0x0008,
        (
            '哎呀？没有预约\n',
            '的客人真新奇啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_DAA',
    )

    ChrTalk(
        0x0008,
        (
            '你，你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这不是以前，在卢安的游戏吧\n',
            '打败了我的人吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1001F啊哈哈，那时候\n',
            '承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎～听我说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然那之后为了赢回输掉的钱\n',
            '挑战了各种各样的游戏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但跟你们的\n',
            '胜负是命运的转折点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '等到发现时之前\n',
            '赢的钱都输光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC8')

    def _loc_DAA(): pass

    label('loc_DAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EC8',
    )

    ChrTalk(
        0x0008,
        (
            '你，你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这不是以前，在卢安的游戏吧\n',
            '不是挑战我输了的人吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1008F啊哈哈，那时候\n',
            '承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呀～听我说啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那之后我来了劲，和店里的\n',
            '女孩子比扑克牌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '结果，看来跟你们比\n',
            '把最后的运气都用光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '等到发现时之前\n',
            '赢的钱都输光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC8(): pass

    label('loc_EC8')

    ChrTalk(
        0x0101,
        (
            '#1004F是、是这样吗？\n',
            '好像很难受啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F2C',
    )

    ChrTalk(
        0x0104,
        (
            '#035F呼，到最后\n',
            '就像一夜幻梦一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7E')

    def _loc_F2C(): pass

    label('loc_F2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_F56',
    )

    ChrTalk(
        0x0106,
        (
            '#051F不过，这就是\n',
            '这个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F7E')

    def _loc_F56(): pass

    label('loc_F56')

    ChrTalk(
        0x0103,
        (
            '#021F嗯，所谓这个\n',
            '往往就是那样啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F7E(): pass

    label('loc_F7E')

    ChrTalk(
        0x0008,
        (
            '……真是吃到苦头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '做任何事情都是\n',
            '适可而止最重要啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '也让妻子担心了，\n',
            '于是决定在这里认真工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CA, 4, 0x1654))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_FF6(): pass

    label('loc_FF6')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xFFA
@scena.Code('func_05_FFA')
def func_05_FFA():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1058',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校指示引擎\n',
            '由我们来戒备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '若再次被偷，影响签字仪式\n',
            '那可就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1058(): pass

    label('loc_1058')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x105C
@scena.Code('func_06_105C')
def func_06_105C():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_11B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_10CE',
    )

    ChrTalk(
        0x00FE,
        (
            '#0561130046V#691F我们去找这里的哥们\n',
            '盖个受领的章就回去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130047V你们工作也要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B8')

    def _loc_10CE(): pass

    label('loc_10CE')

    ChrTalk(
        0x00FE,
        (
            '#0561130048V#692F哦，艾丝蒂尔你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130049V#691F刚才样本已经\n',
            '平安运送完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130050V之后到签字仪式当天\n',
            '只需保管在这里就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130046V我们去找这里的哥们\n',
            '盖个受领的章就回去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0561130047V你们工作也要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_11B8(): pass

    label('loc_11B8')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x11BC
@scena.Code('func_07_11BC')
def func_07_11BC():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_12AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_121C',
    )

    ChrTalk(
        0x00FE,
        (
            '这个引擎集中了\n',
            '技术人员种种构想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我说不好……\n',
            '不想被背叛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AF')

    def _loc_121C(): pass

    label('loc_121C')

    ChrTalk(
        0x00FE,
        (
            '嗯～没想到\n',
            '会这么白白让出啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也不是\n',
            '想要什么抵押……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个引擎集中了\n',
            '技术人员种种构想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我说不好……\n',
            '不想被背叛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_12AF(): pass

    label('loc_12AF')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x12B3
@scena.Code('func_08_12B3')
def func_08_12B3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12E5',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，工作又堆积起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12E5(): pass

    label('loc_12E5')

    Jump('loc_1424')

    def _loc_12E8(): pass

    label('loc_12E8')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1424',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_12FE',
    )

    Jump('loc_1424')

    def _loc_12FE(): pass

    label('loc_12FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_134B',
    )

    ChrTalk(
        0x00FE,
        (
            '新型引擎啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这东西看起来\n',
            '就很让人期待其高输出能力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1424')

    def _loc_134B(): pass

    label('loc_134B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_138E',
    )

    ChrTalk(
        0x00FE,
        (
            '菲利奥吃爱妻便当啊……\n',
            '呼，真令人打从心底里羡慕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1424')

    def _loc_138E(): pass

    label('loc_138E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13C1',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '今天也扎实工作了一天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1424')

    def _loc_13C1(): pass

    label('loc_13C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_13F8',
    )

    ChrTalk(
        0x00FE,
        (
            '负责接待的菲利奥虽是新人\n',
            '却非常努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1424')

    def _loc_13F8(): pass

    label('loc_13F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1424',
    )

    ChrTalk(
        0x00FE,
        (
            '如果有工作的事，\n',
            '麻烦去柜台啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1424(): pass

    label('loc_1424')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1428
@scena.Code('func_09_1428')
def func_09_1428():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有埃尔赛尤用的新型引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
