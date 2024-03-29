import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3150_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3150   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3150.x'
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
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雾香',
            x                   = 3500,
            z                   = 0,
            y                   = 1200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦',
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
            talkScenaIndex      = 0x0008,
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
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
            name                = '斯坦因',
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
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '埃尔文',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '艾妲',
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '库诺',
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '呆呆',
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
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '耶鲁克',
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
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '冈多夫',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '布鲁诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '加鲁诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 4220,
            z                   = 0,
            y                   = -740,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10002 offset: 0x32A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x32A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x32A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3480,
            triggerZ            = 0,
            triggerY            = -710,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 1200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1830,
            triggerZ            = 1000,
            triggerY            = 51000,
            triggerRange        = 400,
            actorX              = 1780,
            actorZ              = 2500,
            actorY              = 53000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53210,
            triggerZ            = 0,
            triggerY            = 520,
            triggerRange        = 400,
            actorX              = 52970,
            actorZ              = 1500,
            actorY              = 2400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1320,
            triggerZ            = 0,
            triggerY            = -4700,
            triggerRange        = 1400,
            actorX              = -1320,
            actorZ              = 2000,
            actorY              = -4700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3BA
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3C6'),
        (-1, 'loc_3DE'),
    )

    def _loc_3C6(): pass

    label('loc_3C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 6, 0x58E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DB',
    )

    MapSetFlags(0x10000000)
    Event(0, func_15_3EC1)

    def _loc_3DB(): pass

    label('loc_3DB')

    Jump('loc_3DE')

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_471',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_403',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0017, 4220, 0, -740, 0)

    def _loc_403(): pass

    label('loc_403')

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1780, 1000, 53000, 183)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 52200, 0, 53760, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 52110, 0, 50520, 255)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 59030, 0, 54500, 355)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 52970, 0, 2400, 172)

    def _loc_471(): pass

    label('loc_471')

    Return()

# id: 0x0001 offset: 0x472
@scena.Code('func_01_472')
def func_01_472():
    Return()

# id: 0x0002 offset: 0x473
@scena.Code('func_02_473')
def func_02_473():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_488',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_473')

    def _loc_488(): pass

    label('loc_488')

    Return()

# id: 0x0003 offset: 0x489
@scena.Code('func_03_489')
def func_03_489():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4AC',
    )

    OP_8D(0x00FE, 52620, 51160, 59990, 53120, 3000)

    Jump('func_03_489')

    def _loc_4AC(): pass

    label('loc_4AC')

    Return()

# id: 0x0004 offset: 0x4AD
@scena.Code('func_04_4AD')
def func_04_4AD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_5E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_50B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，说起来\n',
            '外面还真是吵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又是主日学校的孩子们\n',
            '在翘课打闹吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E2')

    def _loc_50B(): pass

    label('loc_50B')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '这把导力枪\n',
            '可以将内部驱动导力器的性能\n',
            '发挥至极限呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说平衡性确实差了点，\n',
            '很有必要加以改进，\n',
            '不过也算是在可以忍受的范围内吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总而言之一切还算顺利。\n',
            '这样的话，\n',
            '应该可以比预定时间更早做出成品来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E2(): pass

    label('loc_5E2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5E6
@scena.Code('func_05_5E6')
def func_05_5E6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_657',
    )

    ChrTalk(
        0x0110,
        (
            '#0280091654V#150F小艾，\n',
            '了解到什么的话要告诉我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091655V我想让这次的特辑\n',
            '有更多独家新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_657(): pass

    label('loc_657')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x65B
@scena.Code('func_06_65B')
def func_06_65B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_6CA',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，商品的说明果然\n',
            '必须像这样写才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '射程……精度……驱动时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，多么具体啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CA(): pass

    label('loc_6CA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x6CE
@scena.Code('func_07_6CE')
def func_07_6CE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_773',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_728',
    )

    ChrTalk(
        0x00FE,
        (
            '……杨？好像不是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就是……汪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，好像两个都不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_773')

    def _loc_728(): pass

    label('loc_728')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '之前给我担任护卫的那个兄弟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '他到底叫什么来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_773(): pass

    label('loc_773')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x777
@scena.Code('func_08_777')
def func_08_777():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_7D3',
    )

    ChrTalk(
        0x010E,
        (
            '#0150091688V#130F看来发生了不得了的事情啊……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091689V请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D3(): pass

    label('loc_7D3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x7D7
@scena.Code('func_09_7D7')
def func_09_7D7():
    TalkBegin(0x0008)
    FadeOut(300, 0, 70)

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
            TXT(0x01, '报告\n'),
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
        'loc_933',
    )

    OP_0D()

    If(
        (
            (Expr.Eval, "OP_A9(0x40)"),
            Expr.Return,
        ),
        'loc_8B5',
    )

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0580081435V#790F辛苦了。\n',
            '看来你们很顺利地完成了任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081436V如果完成其他任务的话，\n',
            '别忘记回协会报告一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_92D')

    def _loc_8B5(): pass

    label('loc_8B5')

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0580081437V#790F啊，\n',
            '现在没有需要报告的工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081438V如果完成其他任务的话，\n',
            '别忘记回协会报告一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_92D(): pass

    label('loc_92D')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_933(): pass

    label('loc_933')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_944',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_944(): pass

    label('loc_944')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 6, 0x556)),
            Expr.Return,
        ),
        'loc_9B3',
    )

    ChrTalk(
        0x0008,
        (
            '#0580081431V#790F……已经拿到塞姆里亚苔藓了吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081432V必须分秒必争。\n',
            '赶快去礼拜堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC7')

    def _loc_9B3(): pass

    label('loc_9B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_BC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A22',
    )

    ChrTalk(
        0x0008,
        (
            '#0580081433V#790F阿加特的情况\n',
            '已经不容耽搁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081434V你们现在赶快去礼拜堂吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC7')

    def _loc_A22(): pass

    label('loc_A22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5C',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 3400, 0, -1800, 0)
    ChrSetPos(0x0102, 3600, 0, -3160, 0)
    ChrSetPos(0x0107, 4470, 0, -2270, 0)
    ChrTurnDirection(0x0008, 0x0101, 0)
    ChrSetDirection(0x0017, 180, 0)
    OP_4A(0x0017, 255)
    CameraMove(3390, 0, -770, 1000)

    ChrTalk(
        0x0008,
        (
            '#0580081426V#790F那么……\n',
            '教区长怎么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081427V#012F嗯……',
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
            '艾丝蒂尔说明了关于『塞姆里亚苔藓』的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0017,
        (
            '#0080081428V#073F哦，苔藓吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Call(0, 0x0016)

    Jump('loc_BC7')

    def _loc_B5C(): pass

    label('loc_B5C')

    ChrTalk(
        0x0008,
        (
            '#0580081429V#790F金这家伙就供你们随便使唤吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081430V不用担心，\n',
            '这种情况他还是能应付得来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC7(): pass

    label('loc_BC7')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0xBCB
@scena.Code('func_0A_BCB')
def func_0A_BCB():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1A',
    )

    ChrTalk(
        0x0017,
        (
            '#0080081388V#070F嗯？怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081389V不是要去教会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C74')

    def _loc_C1A(): pass

    label('loc_C1A')

    ChrTalk(
        0x0017,
        (
            '#0080081390V#070F哦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081391V如果打听到什么消息，\n',
            '赶快去向雾香报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C74(): pass

    label('loc_C74')

    TalkEnd(0x0017)

    Return()

# id: 0x000B offset: 0xC78
@scena.Code('func_0B_C78')
def func_0B_C78():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_CBD',
    )

    ChrTalk(
        0x00FE,
        (
            '店里面也没有受到损失，\n',
            '暂且可以安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D9B')

    def _loc_CBD(): pass

    label('loc_CBD')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上导力停止了，\n',
            '真是把我吓坏了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说以前也听说过\n',
            '只有在特殊的结晶回路中\n',
            '才会有那种力量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到会产生\n',
            '影响到那么大范围的现象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这力量用于武器研制的话，\n',
            '恐怕会导致各国的军力失去平衡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D9B(): pass

    label('loc_D9B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0xD9F
@scena.Code('func_0C_D9F')
def func_0C_D9F():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0xDA4
@scena.Code('func_0D_DA4')
def func_0D_DA4():
    TalkBegin(0x000D)
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
        'loc_E1A',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 1, 0x571)),
            Expr.Return,
        ),
        'loc_E06',
    )

    OP_A9(0x4C)

    Jump('loc_E14')

    def _loc_E06(): pass

    label('loc_E06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_E12',
    )

    OP_A9(0x4B)

    Jump('loc_E14')

    def _loc_E12(): pass

    label('loc_E12')

    OP_A9(0x3E)

    def _loc_E14(): pass

    label('loc_E14')

    OP_56(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_E1A(): pass

    label('loc_E1A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2B',
    )

    TalkEnd(0x000D)

    Return()

    def _loc_E2B(): pass

    label('loc_E2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_ED9',
    )

    ChrTalk(
        0x000D,
        (
            '哦～早上好啊。\n',
            '这里是贝尔杂货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '本店商品种类非常齐全，\n',
            '能充分满足各位顾客的要求哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '所以……\n',
            '想买什么就请来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '本店的经营\n',
            '也要靠大家的支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1588')

    def _loc_ED9(): pass

    label('loc_ED9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_F2D',
    )

    ChrTalk(
        0x000D,
        (
            '啊，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '贝尔杂货店\n',
            '今天也会以齐全的商品\n',
            '来满足大家的要求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1588')

    def _loc_F2D(): pass

    label('loc_F2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_10C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FD0',
    )

    ChrTalk(
        0x000D,
        (
            '妻子她表示了\n',
            '对我想法的理解呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她说店里以后也要像以前那样\n',
            '保持商品种类的齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '妻子为了我也很努力。\n',
            '我以后也要\n',
            '更加努力才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C0')

    def _loc_FD0(): pass

    label('loc_FD0')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '啊，早上好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天一大早\n',
            '就有开心的事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '妻子头一次\n',
            '对我的想法表示理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她说店里以后也要像以前那样\n',
            '保持商品种类的齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽说经营方面形势严峻，\n',
            '但是只要节约开支的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这样的话\n',
            '我就能安心地和顾客面对面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C0(): pass

    label('loc_10C0')

    Jump('loc_1588')

    def _loc_10C3(): pass

    label('loc_10C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_11BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_113D',
    )

    ChrTalk(
        0x000D,
        (
            '唔～通常情况下， \n',
            '只要我擅作主张降了价，她就会生气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天，她心情很不错呢，\n',
            '发生了什么好事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11BA')

    def _loc_113D(): pass

    label('loc_113D')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '总觉得最近\n',
            '妻子的态度有点奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '她应该知道，出事的时候\n',
            '我在给镇里面的人分派商品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '……为什么她不生气呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11BA(): pass

    label('loc_11BA')

    Jump('loc_1588')

    def _loc_11BD(): pass

    label('loc_11BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_12A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_120C',
    )

    ChrTalk(
        0x000D,
        (
            '妻子艾妲\n',
            '肩膀酸疼得厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天也要去\n',
            '礼拜堂拿药呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_129D')

    def _loc_120C(): pass

    label('loc_120C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '妻子艾妲\n',
            '肩膀酸疼得厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今天也要去\n',
            '礼拜堂拿药呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '中央工房里面\n',
            '也有研究医学的老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '但效果还是比不上\n',
            '传统的医疗法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_129D(): pass

    label('loc_129D')

    Jump('loc_1588')

    def _loc_12A0(): pass

    label('loc_12A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1377',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_130D',
    )

    ChrTalk(
        0x000D,
        (
            '我家大儿子\n',
            '似乎对商品陈列很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '放着他不管的话，\n',
            '他会整整一天都在搞那些东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1374')

    def _loc_130D(): pass

    label('loc_130D')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x000D, 0x000F, 400)

    ChrTalk(
        0x000D,
        (
            '喂喂，库诺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不要再动\n',
            '那些商品了好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不是说好了\n',
            '一天只整理一次商品吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0010)

    def _loc_1374(): pass

    label('loc_1374')

    Jump('loc_1588')

    def _loc_1377(): pass

    label('loc_1377')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1488',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13D2',
    )

    ChrTalk(
        0x000D,
        (
            '整个城市的导力\n',
            '全部都停止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '世界上还有\n',
            '这么不可思议的事呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1485')

    def _loc_13D2(): pass

    label('loc_13D2')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000D,
        (
            '昨天晚上\n',
            '你们没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我以为是照明灯出故障了，\n',
            '打算立即去工房看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '谁知一走到外面，\n',
            '发现整个城镇就像森林里一样漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我马上就意识到\n',
            '这不是什么简单的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1485(): pass

    label('loc_1485')

    Jump('loc_1588')

    def _loc_1488(): pass

    label('loc_1488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1531',
    )

    ChrTalk(
        0x000D,
        (
            '我立志要把这个店\n',
            '经营成受大家喜爱的店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不管什么样的人来，\n',
            '都能在这里找到称心的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '虽然这样采购的时候会很麻烦，\n',
            '不过毕竟不努力就不会成功啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1588')

    def _loc_1531(): pass

    label('loc_1531')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1588',
    )

    ChrTalk(
        0x000D,
        (
            '您好，欢迎光临。\n',
            '这里是贝尔杂货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '从食品到日用品，\n',
            '这里都一应俱全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1588(): pass

    label('loc_1588')

    TalkEnd(0x000D)

    Return()

# id: 0x000E offset: 0x158C
@scena.Code('func_0E_158C')
def func_0E_158C():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_15FD',
    )

    ChrTalk(
        0x000E,
        (
            '呼，这样子的话\n',
            '下个月可能也很辛苦吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，我早已经有思想准备了，\n',
            '一定要努力渡过难关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C40')

    def _loc_15FD(): pass

    label('loc_15FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1646',
    )

    ChrTalk(
        0x000E,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这里是贝尔杂货店。\n',
            '请慢慢挑选喜欢的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C40')

    def _loc_1646(): pass

    label('loc_1646')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_170F',
    )

    ChrTalk(
        0x000E,
        (
            '今天早上，我和丈夫商量了一下，\n',
            '制定了今后的经营方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我们决定努力\n',
            '让商品种类更加齐全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '和以前不同， \n',
            '采购的活儿由我全部负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这样做到底会怎么样。\n',
            '不尝试一下不会知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C40')

    def _loc_170F(): pass

    label('loc_170F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_186B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_17D8',
    )

    ChrTalk(
        0x000E,
        (
            '我似乎也开始明白\n',
            '丈夫的目标了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '他只会常常做梦，\n',
            '不能说是个会做生意的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '他总想让我们的店\n',
            '能给大家带来最大的方便和好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果真能做成这样的店，\n',
            '的确是很了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1868')

    def _loc_17D8(): pass

    label('loc_17D8')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '听说今天在出事现场，\n',
            '丈夫给避难的人们\n',
            '配发了必要物资。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这样的话， \n',
            '这个月又会是赤字了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唉，没办法啦。\n',
            '就当是捐赠，算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1868(): pass

    label('loc_1868')

    Jump('loc_1C40')

    def _loc_186B(): pass

    label('loc_186B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_193E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_18D0',
    )

    ChrTalk(
        0x000E,
        (
            '真是让人难以置信。\n',
            '中央工房竟然会遭到袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '为什么丈夫\n',
            '会发现这件事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193B')

    def _loc_18D0(): pass

    label('loc_18D0')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '刚才听说，\n',
            '中央工房遭到袭击了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我丈夫也是，\n',
            '出去后到现在还没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '真是让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_193B(): pass

    label('loc_193B')

    Jump('loc_1C40')

    def _loc_193E(): pass

    label('loc_193E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_19C8',
    )

    ChrTalk(
        0x000E,
        (
            '丈夫他嘴里说着\n',
            '出了点奇怪的事什么的，\n',
            '就跑出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '而且还擅自将\n',
            '店里面的商品也带走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '唉，\n',
            '他究竟在想什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C40')

    def _loc_19C8(): pass

    label('loc_19C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1AAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1A37',
    )

    ChrTalk(
        0x000E,
        (
            '呼呼，\n',
            '说起来还有工作没完成呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '时间早的话，收拾一下，\n',
            '然后去礼拜堂拿点治肩酸的药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAA')

    def _loc_1A37(): pass

    label('loc_1A37')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '导力器使用不了的话，\n',
            '我们就什么都干不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '昨天发生了那样的事情之后，\n',
            '我们不得不考虑一下这件事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AAA(): pass

    label('loc_1AAA')

    Jump('loc_1C40')

    def _loc_1AAD(): pass

    label('loc_1AAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1BCC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1B1E',
    )

    ChrTalk(
        0x000E,
        (
            '如果不进一些好卖的商品，\n',
            '那就谈不上有什么利润了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啊，不但肩膀重，\n',
            '头也开始疼了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC9')

    def _loc_1B1E(): pass

    label('loc_1B1E')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '我丈夫也不考虑\n',
            '商品能不能卖出去，\n',
            '只会一味地进货又进货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果不清楚这些商品能不能卖掉，\n',
            '经营起来真的是很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '都不知道他有没有想过\n',
            '怎么去把生意做好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BC9(): pass

    label('loc_1BC9')

    Jump('loc_1C40')

    def _loc_1BCC(): pass

    label('loc_1BCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1C40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C08',
    )

    ChrTalk(
        0x000E,
        (
            '呼，一看见账簿\n',
            '我就觉得肩膀好沉重……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C40')

    def _loc_1C08(): pass

    label('loc_1C08')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000E,
        (
            '哈啊……\n',
            '真令人头疼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这个月又快超支了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C40(): pass

    label('loc_1C40')

    TalkEnd(0x000E)

    Return()

# id: 0x000F offset: 0x1C44
@scena.Code('func_0F_1C44')
def func_0F_1C44():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1C84',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈她\n',
            '竟然会表扬爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E39')

    def _loc_1C84(): pass

    label('loc_1C84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1D13',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸他为什么要拿走\n',
            '各种各样的东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '药品、食品什么的也就罢了，\n',
            '带着人偶打算干什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还一副\n',
            '慌慌张张的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E39')

    def _loc_1D13(): pass

    label('loc_1D13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1D69',
    )

    ChrTalk(
        0x00FE,
        (
            '……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯。\n',
            '这下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经没有我\n',
            '去帮忙的必要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E39')

    def _loc_1D69(): pass

    label('loc_1D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_1E39',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1DD2',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然爸爸说\n',
            '一天整理一次商品就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过客人已经动过了，\n',
            '必须按照原样放好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E39')

    def _loc_1DD2(): pass

    label('loc_1DD2')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '然后将这条鱼放回左边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，这下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，终于又回到\n',
            '最完美的陈列状态了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E39(): pass

    label('loc_1E39')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1E3D
@scena.Code('func_10_1E3D')
def func_10_1E3D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1EA8',
    )

    ChrTalk(
        0x00FE,
        (
            '博士！不得了了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妈妈的肩\n',
            '好像开始疼起来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么！赶快啊。\n',
            '快点和教区长联系！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2088')

    def _loc_1EA8(): pass

    label('loc_1EA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1ECD',
    )

    ChrTalk(
        0x00FE,
        (
            '今天去\n',
            '肯定还来得及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2088')

    def _loc_1ECD(): pass

    label('loc_1ECD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1EFD',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸在哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2088')

    def _loc_1EFD(): pass

    label('loc_1EFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_1F3F',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天晚上\n',
            '外面好暗呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我睡在床上\n',
            '都看见了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2088')

    def _loc_1F3F(): pass

    label('loc_1F3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2067',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1F90',
    )

    ChrTalk(
        0x00FE,
        (
            '博士！\n',
            '导力压下降了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么！\n',
            '导力引擎的功率很正常啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2064')

    def _loc_1F90(): pass

    label('loc_1F90')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '哇～啊，\n',
            '是提妲姐～姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们来玩导力技师游戏吧。\n',
            '玩导力技师游戏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F不好意思啊，呆呆。\n',
            '姐姐现在要给客人们带路啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#061F所以呢，还是再下次玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，好吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我明白～了，提妲博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2064(): pass

    label('loc_2064')

    Jump('loc_2088')

    def _loc_2067(): pass

    label('loc_2067')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2088',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐～你们是谁～啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2088(): pass

    label('loc_2088')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x208C
@scena.Code('func_11_208C')
def func_11_208C():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x2091
@scena.Code('func_12_2091')
def func_12_2091():
    TalkBegin(0x0011)
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
        'loc_20EF',
    )

    OP_0D()
    OP_A9(0x3D)
    OP_56(0x00)
    TalkEnd(0x0011)

    Return()

    def _loc_20EF(): pass

    label('loc_20EF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2100',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_2100(): pass

    label('loc_2100')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_225B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_219B',
    )

    ChrTalk(
        0x0011,
        (
            '不管怎么说\n',
            '老板也是个成功的人，\n',
            '值得学习的地方我也要学着点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '唉，\n',
            '就是觉得他思想有点顽固……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '把这些也算在\n',
            '学习范围之内吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2258')

    def _loc_219B(): pass

    label('loc_219B')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '昨天，和斯坦因老板\n',
            '商量了一下采购的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '暂时先决定按照\n',
            '老板的意向来选择商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过我并没有完全理解\n',
            '这位重视可靠性的\n',
            '斯坦因老板的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，这也是需要学习的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2258(): pass

    label('loc_2258')

    Jump('loc_2AC3')

    def _loc_225B(): pass

    label('loc_225B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2383',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_22E1',
    )

    ChrTalk(
        0x0011,
        (
            '唔，\n',
            '那个加鲁诺竟然会这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我也渐渐觉得\n',
            '老板的话有些合理了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……不、不行。\n',
            '不能受别人的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2380')

    def _loc_22E1(): pass

    label('loc_22E1')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '今天一大清早加鲁诺就来了，\n',
            '只说了一句『我明白老板话里的意思了』，\n',
            '之后就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '唔，\n',
            '那个加鲁诺竟然会这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '老板的想法\n',
            '到底哪里正确了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2380(): pass

    label('loc_2380')

    Jump('loc_2AC3')

    def _loc_2383(): pass

    label('loc_2383')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_244C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_23D7',
    )

    ChrTalk(
        0x0011,
        (
            '唔，加鲁诺那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不知道怎么\n',
            '就被斯坦因老板给教唆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2449')

    def _loc_23D7(): pass

    label('loc_23D7')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '今天一大清早加鲁诺就来了，\n',
            '只说了一句『我明白老板话里的意思了』，\n',
            '之后就回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那家伙\n',
            '到底怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2449(): pass

    label('loc_2449')

    Jump('loc_2AC3')

    def _loc_244C(): pass

    label('loc_244C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_249F',
    )

    ChrTalk(
        0x0011,
        (
            '哦，这么晚还有客人来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '店还没有关门，\n',
            '请放心挑选我们的商品吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AC3')

    def _loc_249F(): pass

    label('loc_249F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_254F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_24E9',
    )

    ChrTalk(
        0x0011,
        (
            '有什么损失吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '要是研究计划\n',
            '没受影响就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_254C')

    def _loc_24E9(): pass

    label('loc_24E9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '喂，你们听说了吗？\n',
            '中央工房遭到袭击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '当时我在店里面忙着聊天，\n',
            '一点都没有注意到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_254C(): pass

    label('loc_254C')

    Jump('loc_2AC3')

    def _loc_254F(): pass

    label('loc_254F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2680',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_25B6',
    )

    ChrTalk(
        0x0011,
        (
            '哇，\n',
            '真的是一把非常棒的导力枪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '平衡性若是再好些，\n',
            '我想肯定会更加畅销的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_267D')

    def _loc_25B6(): pass

    label('loc_25B6')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '中央工房的加鲁诺\n',
            '把研究中的导力枪带来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '那家伙真厉害。\n',
            '真是把很棒的导力枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过整体的平衡性有些特殊\n',
            '导致难以操作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '就算操作多多少少有点难，\n',
            '不过只要威力强大就足以弥补了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_267D(): pass

    label('loc_267D')

    Jump('loc_2AC3')

    def _loc_2680(): pass

    label('loc_2680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2814',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_26E9',
    )

    ChrTalk(
        0x0011,
        (
            '啊啊，加鲁诺……\n',
            '快把试制品拿来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '最近唯一的期盼\n',
            '就是能看到那件产品了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2811')

    def _loc_26E9(): pass

    label('loc_26E9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '呵呵，欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哎呀，\n',
            '又和斯坦因老板因为采购的事\n',
            '而发生争执了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不管我们怎么说，\n',
            '他就是不愿意引进\n',
            '还处于研究阶段的导力枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '虽然我已经尽可能劝说他了，\n',
            '不过我只是个被雇来的店长，没有权利管他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊啊，加鲁诺……\n',
            '快把试制品拿来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '最近嘛，\n',
            '只有这么点期盼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2811(): pass

    label('loc_2811')

    Jump('loc_2AC3')

    def _loc_2814(): pass

    label('loc_2814')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_28EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2875',
    )

    ChrTalk(
        0x0011,
        (
            '中央工房里面\n',
            '现在一定乱成一团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为那里\n',
            '全都是测量用的机器呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28E7')

    def _loc_2875(): pass

    label('loc_2875')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '昨天晚上，\n',
            '我正在调整导力枪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '突然，\n',
            '测量器停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我还以为把商品弄坏了，\n',
            '当时一下子傻了眼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28E7(): pass

    label('loc_28E7')

    Jump('loc_2AC3')

    def _loc_28EA(): pass

    label('loc_28EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2A60',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2963',
    )

    ChrTalk(
        0x0011,
        (
            '我虽然也明白老板\n',
            '把武器的可靠性放在第一位的信条……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过稍微想想，\n',
            '老板是否有点太过固执了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A5D')

    def _loc_2963(): pass

    label('loc_2963')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0011,
        (
            '我们这里的老板是斯坦因，\n',
            '就住在这附近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '根据斯坦因先生的原则，\n',
            '我们是绝对不会引进\n',
            '最先进的高尖端武器的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这好像是因为\n',
            '过于先进的武器\n',
            '可靠性还得不到认可……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '有个工房的研究员亲自来出售\n',
            '正在研究中的超级导力枪，\n',
            '也被老板拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A5D(): pass

    label('loc_2A5D')

    Jump('loc_2AC3')

    def _loc_2A60(): pass

    label('loc_2A60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2AC3',
    )

    ChrTalk(
        0x0011,
        (
            '哦，欢迎光临。\n',
            '这里是斯坦因武器商会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '本店全是各种各样的好商品。\n',
            '请慢慢地看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AC3(): pass

    label('loc_2AC3')

    TalkEnd(0x0011)

    Return()

# id: 0x0013 offset: 0x2AC7
@scena.Code('func_13_2AC7')
def func_13_2AC7():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2BF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2B49',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说我也很在意博士这件事，\n',
            '不过现在也只有相信阿加特那家伙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟我们身上也有些\n',
            '非做不可的任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BED')

    def _loc_2B49(): pass

    label('loc_2B49')

    ChrTalk(
        0x00FE,
        (
            '哦，是你们啊。\n',
            '我听说你们的营救作战了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然事情还不算完美解决，\n',
            '不过现在也只有相信阿加特那家伙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是那家伙出马， \n',
            '应该能让博士他们安全逃离的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BED(): pass

    label('loc_2BED')

    Jump('loc_33E2')

    def _loc_2BF0(): pass

    label('loc_2BF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2FA0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 6, 0x57E)),
            Expr.Return,
        ),
        'loc_2CAB',
    )

    ChrTalk(
        0x00FE,
        (
            '王那家伙好像也是充满干劲地工作着，\n',
            '这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前还担心他会因为\n',
            '觉得自己应该对事故负责\n',
            '而意志消沉下来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是雾香\n',
            '用什么巧妙的办法激励他了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F9D')

    def _loc_2CAB(): pass

    label('loc_2CAB')

    SetScenaFlags(ScenaFlag(0x00AF, 6, 0x57E))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Return,
        ),
        'loc_2D71',
    )

    ChrTalk(
        0x0101,
        (
            '#000F啊，冈多夫先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是刚从王都回来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，我刚得知了消息。\n',
            '然后就匆匆忙忙赶回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾香她已经告诉我\n',
            '这边大概的事情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿加特那家伙\n',
            '已经没事了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E28')

    def _loc_2D71(): pass

    label('loc_2D71')

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '你们就是那两个准游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是蔡斯所属的游击士，\n',
            '名叫冈多夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听到消息之后， \n',
            '就从出差地王都赶了回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大体情况我已经问过雾香了……\n',
            '呃，阿加特他没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E28(): pass

    label('loc_2E28')

    ChrTalk(
        0x0101,
        (
            '#000F嗯，还好度过了危险期……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……哎，你认识阿加特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，因为工作的关系\n',
            '我们已经见过很多次面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很久之前他\n',
            '就已经是个非常有名的家伙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总之，\n',
            '他没事就好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，搜查的工作\n',
            '就交给你们和阿加特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而我们就尽量去\n',
            '处理一些日常的零碎工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那就拜托您了。\n',
            '冈多夫先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，你们要保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F9D(): pass

    label('loc_2F9D')

    Jump('loc_33E2')

    def _loc_2FA0(): pass

    label('loc_2FA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_33E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3398',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 5, 0x57D))

    ChrTalk(
        0x0013,
        (
            '嗯？　出差！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '冈多夫先生你……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊，不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '因为军方直接点名……\n',
            '我必须去一趟王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '又不是只剩下你一个，\n',
            '那些准游击士也在嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们同心协力的话，\n',
            '两三天肯定能应付过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '是啊，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我明白了。\n',
            '我会拼命努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哦……\n',
            '总之乐观一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0000, 400)

    ChrTalk(
        0x0012,
        (
            '……哦，\n',
            '这就是传闻中的两个人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们两个\n',
            '来得真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31F2',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 4, 0x57C))

    ChrTalk(
        0x0013,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '难道……\n',
            '你们就是那些准游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，没错。\n',
            '我们就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面。\n',
            '我是准游击士约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3232')

    def _loc_31F2(): pass

    label('loc_31F2')

    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '啊，\n',
            '是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '你们来得正是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3232(): pass

    label('loc_3232')

    ChrTalk(
        0x0012,
        (
            '呵呵，果然是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '看到你们，\n',
            '我终于明白雾香说的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对了，\n',
            '请问您要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊啊，没错。\n',
            '那边有很紧急的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '蔡斯支部的工作\n',
            '就交给你们和王负责了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们就好好努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '……就是这样。\n',
            '总之希望能借助你们的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好，我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那就这样吧。\n',
            '拜托你们留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0010)

    Jump('loc_33E2')

    def _loc_3398(): pass

    label('loc_3398')

    ChrTalk(
        0x0012,
        (
            '不好意思，\n',
            '拜托你们在这里留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们要和王那家伙\n',
            '好好合作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33E2(): pass

    label('loc_33E2')

    TalkEnd(0x0012)

    Return()

# id: 0x0014 offset: 0x33E6
@scena.Code('func_14_33E6')
def func_14_33E6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3518',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3473',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '听说你们要去王都了对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系，\n',
            '你们肯定能够很快成为正游击士的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后也要精力充沛地\n',
            '努力工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3515')

    def _loc_3473(): pass

    label('loc_3473')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

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
            '我听说了哦，\n',
            '营救作战按照计划顺利实行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然博士他们以后会怎样\n',
            '现在还不能放心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，很感谢你们。\n',
            '谢谢把他们救了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3515(): pass

    label('loc_3515')

    Jump('loc_3EBD')

    def _loc_3518(): pass

    label('loc_3518')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3999',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3910',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 5, 0x57D))

    ChrTalk(
        0x0013,
        (
            '嗯？　出差！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '冈多夫先生你……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊，不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '因为军方直接点名……\n',
            '我必须去一趟王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '又不是只剩下你一个，\n',
            '那些准游击士也在嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们同心协力的话，\n',
            '两三天肯定能应付过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '是啊，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我明白了。\n',
            '我会拼命努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哦……\n',
            '总之乐观一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0000, 400)

    ChrTalk(
        0x0012,
        (
            '……哦，\n',
            '这就是传闻中的两个人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们两个\n',
            '来得真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_376A',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 4, 0x57C))

    ChrTalk(
        0x0013,
        (
            '……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '难道……\n',
            '你们就是那些准游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，没错。\n',
            '我们就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F初次见面。\n',
            '我是准游击士约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37AA')

    def _loc_376A(): pass

    label('loc_376A')

    ChrTurnDirection(0x0013, 0x0000, 400)

    ChrTalk(
        0x0013,
        (
            '啊，\n',
            '是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '你们来得正是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37AA(): pass

    label('loc_37AA')

    ChrTalk(
        0x0012,
        (
            '呵呵，果然是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '看到你们，\n',
            '我终于明白雾香说的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对了，\n',
            '请问您要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊啊，没错。\n',
            '那边有很紧急的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '蔡斯支部的工作\n',
            '就交给你们和王负责了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们就好好努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '……就是这样。\n',
            '总之希望能借助你们的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好，我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那就这样吧。\n',
            '拜托你们留守了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0010)
    ChrClearFlags(0x0013, 0x0010)

    Jump('loc_3996')

    def _loc_3910(): pass

    label('loc_3910')

    ChrTalk(
        0x00FE,
        (
            '接下来一段时间\n',
            '冈多夫先生要到别的地方出差……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吧，今后的工作， \n',
            '必须更加充满干劲去做才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望你们\n',
            '也能够协助我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3996(): pass

    label('loc_3996')

    Jump('loc_3EBD')

    def _loc_3999(): pass

    label('loc_3999')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3DAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D3D',
    )

    SetScenaFlags(ScenaFlag(0x00AF, 4, 0x57C))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39EE',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然会来武器店，真少见啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A19')

    def _loc_39EE(): pass

    label('loc_39EE')

    ChrTalk(
        0x00FE,
        (
            '嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '原来是提妲来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A19(): pass

    label('loc_3A19')

    ChrTalk(
        0x00FE,
        (
            '咦……？\n',
            '这两位不会是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，是的。\n',
            '他们都是游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我现在要带他们\n',
            '到我家里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，果然是这样啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的名字叫做王。\n',
            '是蔡斯支部所属的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在还是个新人，\n',
            '和你们差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，是这样啊。请多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是准游击士艾丝蒂尔。\n',
            '旁边的那位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我是约修亚，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我之前听雾香说过\n',
            '有关你们的事情。\n',
            '果然来了很厉害的准游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说你们在全国各地\n',
            '都做出了相当的成绩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，就算是这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F说到成绩，\n',
            '我们只是尽了自己的本分而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且多亏得到了游击士前辈\n',
            '和各地百姓的鼎力相助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '我觉得能够得到百姓信任，\n',
            '得到他们的帮助也是一种才能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实际上，\n',
            '我们支部也处于人手不足的状态。\n',
            '我相当期待你们的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后这段时间\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F还请以后多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DA9')

    def _loc_3D3D(): pass

    label('loc_3D3D')

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔、约修亚。\n',
            '我相当期待你们今后的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许相处时间不会太长，\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3DA9(): pass

    label('loc_3DA9')

    Jump('loc_3EBD')

    def _loc_3DAC(): pass

    label('loc_3DAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3EBD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3E3C',
    )

    ChrTalk(
        0x00FE,
        (
            '是选平衡性呢，\n',
            '还是选突出的特性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，归根到底\n',
            '还是要看使用者的本事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我大概还没有可以\n',
            '选择武器的实力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBD')

    def _loc_3E3C(): pass

    label('loc_3E3C')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '唔，好难啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是选性能比较平衡的武器呢，\n',
            '还是选非常有特点的武器呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能二者兼顾的话，\n',
            '就不用那么烦恼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EBD(): pass

    label('loc_3EBD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x3EC1
@scena.Code('func_15_3EC1')
def func_15_3EC1():
    EventBegin(0x00)
    MapClearFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00B1, 6, 0x58E))
    ChrSetPos(0x0101, 1750, 0, -4500, 53)
    ChrSetPos(0x0102, 730, 0, -5190, 44)
    ChrSetPos(0x0107, 1790, 0, -5680, 57)
    ChrSetPos(0x0017, 4240, 0, -800, 17)
    OP_4A(0x0017, 255)
    OP_4A(0x0008, 255)
    CameraMove(2460, 0, -2580, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0017, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0017, 180, 400)

    ChrTalk(
        0x0017,
        (
            '#0080081439V#070F哦哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081440V#501F啊，金先生！\n',
            '原来你还在这啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FEF')
    def lambda_3FEF():
        CameraMove(3390, 0, -770, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3FEF)

    @scena.Lambda('lambda_4007')
    def lambda_4007():
        ChrWalkTo(0x00FE, 3400, 0, -1800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4007)

    Sleep(300)

    @scena.Lambda('lambda_4027')
    def lambda_4027():
        ChrWalkTo(0x00FE, 4470, 0, -2270, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_4027)

    Sleep(300)

    @scena.Lambda('lambda_4047')
    def lambda_4047():
        ChrWalkTo(0x00FE, 3600, 0, -3160, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4047)

    @scena.Lambda('lambda_4062')
    def lambda_4062():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_4062')

    DispatchAsync2(0x0101, 0x0001, lambda_4062)

    @scena.Lambda('lambda_4073')
    def lambda_4073():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_4073')

    DispatchAsync2(0x0102, 0x0001, lambda_4073)

    @scena.Lambda('lambda_4084')
    def lambda_4084():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_4084')

    DispatchAsync2(0x0107, 0x0001, lambda_4084)

    Sleep(2000)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010081441V#000F刚才真是多谢\n',
            '你帮忙把阿加特背回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081442V#010F真是麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0080081443V#071F哇哈哈，别客气。\n',
            '同行就是要相互帮助的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081444V#790F那么……\n',
            '阿加特的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081445V#013F那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4369',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们把阿加特的情况\n',
            '和皮克塞恩教区长的事情说明了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0017,
        (
            '#0080081446V#072F唔……\n',
            '情况比想象的更危险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081447V#792F教会的传统医疗法吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081448V现在也只能\n',
            '赌一赌这种可能性了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081449V#002F嗯，\n',
            '总之现在要赶快去礼拜堂看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081450V我们在这里说话的时候，\n',
            '阿加特一直在受苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081451V#012F那么，\n',
            '我们这就去七耀教会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081452V#790F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0017, 255)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Jump('loc_4414')

    def _loc_4369(): pass

    label('loc_4369')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们把阿加特的情况\n',
            '和『塞姆里亚苔藓』的事情说明了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0017,
        (
            '#0080081453V#072F唔……\n',
            '情况比想象的更危险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Call(0, 0x0016)

    def _loc_4414(): pass

    label('loc_4414')

    Return()

# id: 0x0016 offset: 0x4415
@scena.Code('func_16_4415')
def func_16_4415():
    ChrSetStatus(0x0007, 0x00, 27)
    OP_B5(0x0007, 0x00)
    OP_B5(0x0007, 0x01)
    OP_B5(0x0007, 0x02)
    OP_B5(0x0007, 0x03)
    OP_B5(0x0007, 0x04)
    OP_B5(0x0007, 0x05)
    EquipCmd(0x07, 0x00D3)
    EquipCmd(0x07, 0x00F5)
    EquipCmd(0x07, 0x0113)
    EquipCmd(0x07, 0x0261, 0x00)
    EquipCmd(0x07, 0x0259, 0x01)
    EquipCmd(0x07, 0x025E, 0x02)
    EquipCmd(0x07, 0x0274, 0x03)
    AddCraft(0x0007, 0x00DC)
    AddCraft(0x0007, 0x00DD)
    AddCraft(0x0007, 0x00DE)
    AddCraft(0x0007, 0x00DF)
    AddSCraft(0x0007, 0x0109)
    FormationAddMember(0x07, 0xFF)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetPos(0x0101, 3400, 0, -1800, 0)
    ChrSetPos(0x0102, 3600, 0, -3160, 0)
    ChrSetPos(0x0107, 4470, 0, -2270, 0)
    ChrSetPos(0x0108, 4220, 0, -740, 180)
    CameraMove(3390, 0, -770, 1200)

    ChrTalk(
        0x0008,
        (
            '#0580081454V#790F那个『塞姆里亚苔藓』，\n',
            '教会以前确实委托我们采集过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081455V#792F请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4532')
    def lambda_4532():
        ChrTurnDirection(0x00FE, 0x0008, 300)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_4532)

    ChrSetDirection(0x0008, 180, 400)

    @scena.Lambda('lambda_4547')
    def lambda_4547():
        CameraMove(3980, 0, 800, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4547)

    ChrWalkTo(0x0008, 3600, 0, 2390, 1500, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0580081456V#790F……找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081457V是在卡鲁迪亚钟乳洞西北区域的\n',
            '洞窟湖的岸边采集到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081458V#002F钟乳洞的西北……洞窟湖对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081459V#010F在手册上记下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0580081460V#790F不过事先说明……\n',
            '那个钟乳洞里的魔兽相当难对付。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580081461V以前采集的时候，\n',
            '都是由四个经验丰富的游击士\n',
            '组成队伍在那里进行药料搜索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081462V#004F四、四个游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081463V#012F的确很麻烦的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#0080081464V#070F#4P唔，那样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4773')
    def lambda_4773():
        CameraMove(3390, 0, -770, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4773)

    ChrWalkTo(0x0008, 3720, 0, 1300, 1500, 0x00)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0580081465V#791F就是因为这样，\n',
            '你们就把这男人一起带去好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 0)

    ChrTalk(
        0x0108,
        (
            '#0080081466V#075F……（晕倒）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0008, 600)

    ChrTalk(
        0x0108,
        (
            '#0080081467V#072F喂，我说！\n',
            '不要随便替我做决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081468V#792F怎么了，\n',
            '你不打算陪他们去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081469V#073F那、那倒不是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081470V#075F真是的……\n',
            '你的性格还真是一点都没变啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580081471V#791F多谢夸奖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081472V#072F谁夸奖你，才不是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010081473V#506F呵呵，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081474V关键就是说，\n',
            '金先生也会陪我们去钟乳洞吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0108, 180, 400)

    ChrTalk(
        0x0108,
        (
            '#0080081475V#070F啊，是的……\n',
            '这也是一种缘分嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081476V明天我就要去王都，\n',
            '所以只能在今天内为你们一尽绵力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081477V#001F足够了！\n',
            '这样已经帮了我们大忙啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081478V#010F那就请多多指教了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0107)
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081479V#063F#4P那、那个……\n',
            '艾丝蒂尔姐姐、约修亚哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081480V我也想去……可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4B39')
    def lambda_4B39():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4B39)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081481V#004F#5P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081482V#561F#4P我也知道……\n',
            '自己只会碍手碍脚的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081483V但是……但是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081484V#069F阿加特大哥哥\n',
            '是因为我才会受伤的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081485V要是不能为他做点什么的话，\n',
            '我……会恨死自己的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081486V#003F#5P提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010081487V#005F#5P喂，约修亚。\n',
            '就当我再次求求你了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081488V让她跟着我们一起去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081489V#015F真没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081490V#012F我说，提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081491V你能向我们保证\n',
            '这次绝对不会再乱来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4D3B')
    def lambda_4D3B():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D3B)

    ChrTalk(
        0x0107,
        (
            '#0070081492V#062F#4P嗯、嗯，保证……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020081493V#010F嗯，就这样决定了。\n',
            '金先生也不会介意吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080081494V#070F啊哈哈。\n',
            '我当然不介意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081495V#071F多指教了，小姑娘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0108, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081496V#560F啊……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081497V#006F#5P好的，既然商量好的话，\n',
            '那我们马上向钟乳洞出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081498V#010F首先要到中央工房地下，\n',
            '乘导力梯到卡鲁迪亚隧道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00AA, 2, 0x552))
    OP_28(0x0042, 0x01, 0x0020)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x4ED4
@scena.Code('func_17_4ED4')
def func_17_4ED4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_4EF1',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0x0034, 0xFFFF)

    Jump('loc_4F80')

    def _loc_4EF1(): pass

    label('loc_4EF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Return,
        ),
        'loc_4F0E',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0x0034, 0xFFFF)

    Jump('loc_4F80')

    def _loc_4F0E(): pass

    label('loc_4F0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_4F29',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0xFFFF)

    Jump('loc_4F80')

    def _loc_4F29(): pass

    label('loc_4F29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_4F44',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0xFFFF)

    Jump('loc_4F80')

    def _loc_4F44(): pass

    label('loc_4F44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4F5F',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0x0028, 0x002B, 0x002C, 0x0033, 0xFFFF)

    Jump('loc_4F80')

    def _loc_4F5F(): pass

    label('loc_4F5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_4F72',
    )

    OP_2A(0x002D, 0x0032, 0x002A, 0xFFFF)

    Jump('loc_4F80')

    def _loc_4F72(): pass

    label('loc_4F72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_4F80',
    )

    OP_2A(0x002D, 0x0032, 0xFFFF)

    def _loc_4F80(): pass

    label('loc_4F80')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
