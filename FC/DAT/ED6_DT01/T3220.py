import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3220_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3220   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3220.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拜舍尔',
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
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '艾德',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '林',
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '莉西亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '希利尔',
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
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '艾缇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '拉克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '希玛',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '库安',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x23A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2440,
            triggerZ            = 250,
            triggerY            = 2960,
            triggerRange        = 400,
            actorX              = 2550,
            actorZ              = 1750,
            actorY              = 4470,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x25E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_27E',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)

    Jump('loc_3E9')

    def _loc_27E(): pass

    label('loc_27E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_29E',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)

    Jump('loc_3E9')

    def _loc_29E(): pass

    label('loc_29E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2BE',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)

    Jump('loc_3E9')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2F4',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -960, 250, -2580, 188)

    Jump('loc_3E9')

    def _loc_2F4(): pass

    label('loc_2F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_32A',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -5240, 500, -330, 108)

    Jump('loc_3E9')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_376',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 590, 250, 2540, 10)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 4130, 0, -2220, 291)

    Jump('loc_3E9')

    def _loc_376(): pass

    label('loc_376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_3AC',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -3250, 250, 4820, 348)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)

    Jump('loc_3E9')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3CC',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)

    Jump('loc_3E9')

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3E9',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 2550, 250, 4470, 192)

    def _loc_3E9(): pass

    label('loc_3E9')

    Return()

# id: 0x0001 offset: 0x3EA
@scena.Code('func_01_3EA')
def func_01_3EA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_402',
    )

    OP_B1('t3220_y')

    Jump('loc_40B')

    def _loc_402(): pass

    label('loc_402')

    OP_B1('t3220_n')

    def _loc_40B(): pass

    label('loc_40B')

    Return()

# id: 0x0002 offset: 0x40C
@scena.Code('func_02_40C')
def func_02_40C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_421',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_40C')

    def _loc_421(): pass

    label('loc_421')

    Return()

# id: 0x0003 offset: 0x422
@scena.Code('func_03_422')
def func_03_422():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_42F',
    )

    Jump('loc_52D')

    def _loc_42F(): pass

    label('loc_42F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_439',
    )

    Jump('loc_52D')

    def _loc_439(): pass

    label('loc_439')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_443',
    )

    Jump('loc_52D')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_44D',
    )

    Jump('loc_52D')

    def _loc_44D(): pass

    label('loc_44D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_457',
    )

    Jump('loc_52D')

    def _loc_457(): pass

    label('loc_457')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_461',
    )

    Jump('loc_52D')

    def _loc_461(): pass

    label('loc_461')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_51C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿～真有意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个就是东方的陶器吧\n',
            '素朴又可爱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_519')

    def _loc_4AF(): pass

    label('loc_4AF')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '离吃饭还早着呢，\n',
            '温泉又因为水泵的故障不能用了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这样的话， \n',
            '要做的事果然就是购物了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_519(): pass

    label('loc_519')

    Jump('loc_52D')

    def _loc_51C(): pass

    label('loc_51C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_526',
    )

    Jump('loc_52D')

    def _loc_526(): pass

    label('loc_526')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_52D',
    )

    def _loc_52D(): pass

    label('loc_52D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x531
@scena.Code('func_04_531')
def func_04_531():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x538
@scena.Code('func_05_538')
def func_05_538():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x53F
@scena.Code('func_06_53F')
def func_06_53F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_54C',
    )

    Jump('loc_662')

    def _loc_54C(): pass

    label('loc_54C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_556',
    )

    Jump('loc_662')

    def _loc_556(): pass

    label('loc_556')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_560',
    )

    Jump('loc_662')

    def _loc_560(): pass

    label('loc_560')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_56A',
    )

    Jump('loc_662')

    def _loc_56A(): pass

    label('loc_56A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_574',
    )

    Jump('loc_662')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_647',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5F3',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '有没有其他要买的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 330, 800)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个碟子，\n',
            '还真是可爱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_644')

    def _loc_5F3(): pass

    label('loc_5F3')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '嗯……我记得……\n',
            '酱油和酒都用完了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '有没有其他要买的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_644(): pass

    label('loc_644')

    Jump('loc_662')

    def _loc_647(): pass

    label('loc_647')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_651',
    )

    Jump('loc_662')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_65B',
    )

    Jump('loc_662')

    def _loc_65B(): pass

    label('loc_65B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_662',
    )

    def _loc_662(): pass

    label('loc_662')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x666
@scena.Code('func_07_666')
def func_07_666():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x66D
@scena.Code('func_08_66D')
def func_08_66D():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x674
@scena.Code('func_09_674')
def func_09_674():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x67B
@scena.Code('func_0A_67B')
def func_0A_67B():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x682
@scena.Code('func_0B_682')
def func_0B_682():
    TalkBegin(0x000F)
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
        'loc_6E0',
    )

    OP_0D()
    OP_A9(0x44)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_6E0(): pass

    label('loc_6E0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F1',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_6F1(): pass

    label('loc_6F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_7E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_756',
    )

    ChrTalk(
        0x000F,
        (
            '因为女王的诞辰庆典快到了，\n',
            '客人也越来越少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我这个看店的\n',
            '也困得要命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E3')

    def _loc_756(): pass

    label('loc_756')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '哎呀哎呀……\n',
            '还以为是谁，原来有客人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为几乎没人来，\n',
            '我都已经在想\n',
            '是不是该关门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '啊，想帮帮我的话，\n',
            '就买点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7E3(): pass

    label('loc_7E3')

    Jump('loc_EFF')

    def _loc_7E6(): pass

    label('loc_7E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_928',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_865',
    )

    ChrTalk(
        0x000F,
        (
            '很遗憾啊，我想在这个村子里\n',
            '大概也不会找到什么线索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '但是难得来了，\n',
            '不如买点温泉鸡蛋之类的特产吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_925')

    def _loc_865(): pass

    label('loc_865')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '啊，是你们啊……\n',
            '工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我从毛婆婆那里\n',
            '听说了你们的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我想在这个村子里\n',
            '大概也不会找到什么线索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '算了，难得来一次，\n',
            '至少看看这些特产，\n',
            '挑点想买的带回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_925(): pass

    label('loc_925')

    Jump('loc_EFF')

    def _loc_928(): pass

    label('loc_928')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_ABD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_9D9',
    )

    ChrTalk(
        0x000F,
        (
            '仔细想想看，\n',
            '还是小时候最幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……我和妻子相遇的时候，\n',
            '年纪正好像库安那么大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '那时候自己\n',
            '还是个和库安一样的少年……\n',
            '现在想想简直不敢相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABA')

    def _loc_9D9(): pass

    label('loc_9D9')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '关于蔡斯事件的话题\n',
            '在大人们当中引起了很大的骚动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '但是库安他们一点也没受影响，\n',
            '还是和往常一样天真无邪地在外边玩耍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '仔细想想看，\n',
            '还是小时候最幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '……我和妻子相遇的时候，\n',
            '年纪正好像库安那么大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABA(): pass

    label('loc_ABA')

    Jump('loc_EFF')

    def _loc_ABD(): pass

    label('loc_ABD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_B33',
    )

    ChrTalk(
        0x000F,
        (
            '哟，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '已经要回去了吗？\n',
            '买点特产作纪念怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '来这里的游客们\n',
            '都会买很多特产带回去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EFF')

    def _loc_B33(): pass

    label('loc_B33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_BDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_B87',
    )

    ChrTalk(
        0x000F,
        (
            '呼，腰痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '把店里收拾完以后\n',
            '就去『红叶亭』休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BDA')

    def _loc_B87(): pass

    label('loc_B87')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '咦……\n',
            '还以为是谁，原来有客人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '马上就关门了，\n',
            '要买东西请尽快哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDA(): pass

    label('loc_BDA')

    Jump('loc_EFF')

    def _loc_BDD(): pass

    label('loc_BDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_CB9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_C34',
    )

    ChrTalk(
        0x000F,
        (
            '哎呀……\n',
            '又到天黑的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这一天\n',
            '就这样平平淡淡地结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB6')

    def _loc_C34(): pass

    label('loc_C34')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '我们会向观光的客人\n',
            '推荐这里的土特产品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '当然，\n',
            '本店里同样也卖村民的生活必需品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为村子里\n',
            '没有其他的商店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB6(): pass

    label('loc_CB6')

    Jump('loc_EFF')

    def _loc_CB9(): pass

    label('loc_CB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_D72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_D0E',
    )

    ChrTalk(
        0x000F,
        (
            '啊，\n',
            '终于有客人来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这些陶器很值得推荐，\n',
            '请慢慢看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6F')

    def _loc_D0E(): pass

    label('loc_D0E')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '啊，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '等了好久，\n',
            '终于有客人来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这些陶器很值得推荐，\n',
            '请慢慢看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D6F(): pass

    label('loc_D6F')

    Jump('loc_EFF')

    def _loc_D72(): pass

    label('loc_D72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_E29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_DD7',
    )

    ChrTalk(
        0x000F,
        (
            '我的儿子库安\n',
            '性格十分活泼外向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '这一点不太像我，\n',
            '倒更像我已经去世的妻子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E26')

    def _loc_DD7(): pass

    label('loc_DD7')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '呼，\n',
            '今天没什么客人光顾呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '库安那小子，\n',
            '有没有在用心招呼客人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E26(): pass

    label('loc_E26')

    Jump('loc_EFF')

    def _loc_E29(): pass

    label('loc_E29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_EFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_E8B',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎～请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '温泉鸡蛋的食用方法\n',
            '也有很多种哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '请一定要试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EFF')

    def _loc_E8B(): pass

    label('loc_E8B')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '啊啊……\n',
            '还以为是谁，原来有客人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '欢迎。\n',
            '请、请慢慢看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我个人最推荐的特产\n',
            '就要数温泉蛋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EFF(): pass

    label('loc_EFF')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0xF03
@scena.Code('func_0C_F03')
def func_0C_F03():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_F10',
    )

    Jump('loc_1122')

    def _loc_F10(): pass

    label('loc_F10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_F1A',
    )

    Jump('loc_1122')

    def _loc_F1A(): pass

    label('loc_F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_F24',
    )

    Jump('loc_1122')

    def _loc_F24(): pass

    label('loc_F24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_F65',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，真没劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店里的事做完之后\n',
            '就去外边玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1122')

    def _loc_F65(): pass

    label('loc_F65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_106F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_FE3',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然这么说，\n',
            '没有客人来真是不太安心。\n',
            '爸爸让我去招揽顾客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的爸爸就像\n',
            '图画书里的那个没用的爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106C')

    def _loc_FE3(): pass

    label('loc_FE3')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '我的爸爸\n',
            '对生意不很热心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是正累的时候\n',
            '有客人前来光顾，\n',
            '他就会摆出一副臭脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样可不行啊。\n',
            '爸爸根本不适合做生意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106C(): pass

    label('loc_106C')

    Jump('loc_1122')

    def _loc_106F(): pass

    label('loc_106F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1107',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_10BF',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，怎么了？\n',
            '要买温泉蛋吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咕噜咕噜的，咕噜咕噜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1104')

    def _loc_10BF(): pass

    label('loc_10BF')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '啊～～\n',
            '来点温泉蛋怎么样～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咕噜咕噜的\n',
            '好吃的温泉蛋啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1104(): pass

    label('loc_1104')

    Jump('loc_1122')

    def _loc_1107(): pass

    label('loc_1107')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_1111',
    )

    Jump('loc_1122')

    def _loc_1111(): pass

    label('loc_1111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_111B',
    )

    Jump('loc_1122')

    def _loc_111B(): pass

    label('loc_111B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1122',
    )

    def _loc_1122(): pass

    label('loc_1122')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1126
@scena.Code('func_0D_1126')
def func_0D_1126():
    Call(0, 0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
