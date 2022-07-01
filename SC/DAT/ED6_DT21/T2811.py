import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2811_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2811   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔儿'),
    TXT(0x02, '汉斯'),
    TXT(0x03, '德波拉'),
    TXT(0x04, '目标用照相机'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2811.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1966
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH02393._CH', 'ED6_DT07/CH02393P._CP'),
        ('ED6_DT07/CH02553._CH', 'ED6_DT07/CH02553P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 3500,
            z                   = 0,
            y                   = 4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
    )

# id: 0x10003 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3060,
            triggerZ            = 0,
            triggerY            = 2500,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 4500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x176
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_189',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0007)

    def _loc_189(): pass

    label('loc_189')

    Return()

# id: 0x0001 offset: 0x18A
@scena.Code('Init')
def Init():
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0008, -1810, 300, -1250, 269)
    SetChrPos(0x0009, -3520, 300, 200, 158)
    SetChrChipByIndex(0x0008, 3)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0009, 4)
    SetChrSubChip(0x0009, 0)

    Return()

# id: 0x0002 offset: 0x1DD
@scena.Code('ReInit')
def ReInit():
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
        'loc_202',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_344')

    def _loc_202(): pass

    label('loc_202')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_344')

    def _loc_21B(): pass

    label('loc_21B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_234',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_344')

    def _loc_234(): pass

    label('loc_234')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_344')

    def _loc_24D(): pass

    label('loc_24D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_266',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_344')

    def _loc_266(): pass

    label('loc_266')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_344')

    def _loc_27F(): pass

    label('loc_27F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_298',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_344')

    def _loc_298(): pass

    label('loc_298')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B1',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_344')

    def _loc_2B1(): pass

    label('loc_2B1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CA',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_344')

    def _loc_2CA(): pass

    label('loc_2CA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E3',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_344')

    def _loc_2E3(): pass

    label('loc_2E3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FC',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_344')

    def _loc_2FC(): pass

    label('loc_2FC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_315',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_344')

    def _loc_315(): pass

    label('loc_315')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32E',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_344')

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_344',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_344(): pass

    label('loc_344')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_359',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_344')

    def _loc_359(): pass

    label('loc_359')

    Return()

# id: 0x0003 offset: 0x35A
@scena.Code('func_03_35A')
def func_03_35A():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x35F
@scena.Code('func_04_35F')
def func_04_35F():
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
            TXT(0x02, '招牌菜『大小姐料理』　800米拉\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x72)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x320),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_4B0',
    )

    SubMira(800)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '大小姐料理',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFD, 1200)
    SetChrStatus(ChrTable['约修亚'], 0xFD, 1200)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFD, 1200)
    SetChrStatus(ChrTable['奥利维尔'], 0xFD, 1200)
    SetChrStatus(ChrTable['科洛丝'], 0xFD, 1200)
    SetChrStatus(ChrTable['阿加特'], 0xFD, 1200)
    SetChrStatus(ChrTable['提妲'], 0xFD, 1200)
    SetChrStatus(ChrTable['金'], 0xFD, 1200)
    SetChrStatus(ChrTable['凯文神父'], 0xFD, 1200)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A2',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0009)"),
            Expr.Return,
        ),
        'loc_478',
    )

    Jump('loc_4A2')

    def _loc_478(): pass

    label('loc_478')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '大小姐料理',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A2(): pass

    label('loc_4A2')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_4D6')

    def _loc_4B0(): pass

    label('loc_4B0')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_4D6(): pass

    label('loc_4D6')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000A)

    Return()

    def _loc_4E5(): pass

    label('loc_4E5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FF',
    )

    FadeIn(300, 0)
    TalkEnd(0x000A)

    Return()

    def _loc_4FF(): pass

    label('loc_4FF')

    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '现在要去哪儿？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '外边很暗\n',
            '要当心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x539
@scena.Code('func_05_539')
def func_05_539():
    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_55E',
    )

    SetChrSubChip(0x0008, 2)

    Jump('loc_58F')

    def _loc_55E(): pass

    label('loc_55E')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_574',
    )

    SetChrSubChip(0x0008, 1)

    Jump('loc_58F')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_58A',
    )

    SetChrSubChip(0x0008, 0)

    Jump('loc_58F')

    def _loc_58A(): pass

    label('loc_58A')

    SetChrSubChip(0x0008, 2)

    def _loc_58F(): pass

    label('loc_58F')

    OP_8C(0x0008, 269, 0)
    SetChrFlags(0x0008, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 2, 0x122A)),
            Expr.Return,
        ),
        'loc_654',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_602',
    )

    ChrTalk(
        0x0008,
        (
            '#0511300001V#640F嗯～秘密的地下室啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0511300002V还有卡片的谜题\n',
            '真令人开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_651')

    def _loc_602(): pass

    label('loc_602')

    OP_A2(0x0000)

    ChrTalk(
        0x0008,
        (
            '#0511300001V#640F嗯～秘密的地下室啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0511300003V相当有趣\n',
            '的发展嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_651(): pass

    label('loc_651')

    Jump('loc_6C2')

    def _loc_654(): pass

    label('loc_654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_6C2',
    )

    ChrTalk(
        0x0008,
        (
            '#0511300004V#640F我们就在这里等吧。\n',
            '碍手碍脚就不好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0511300005V那么，当心。\n',
            '期待冒险见闻哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C2(): pass

    label('loc_6C2')

    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x6CB
@scena.Code('func_06_6CB')
def func_06_6CB():
    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6F0',
    )

    SetChrSubChip(0x0009, 1)

    Jump('loc_721')

    def _loc_6F0(): pass

    label('loc_6F0')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_706',
    )

    SetChrSubChip(0x0009, 0)

    Jump('loc_721')

    def _loc_706(): pass

    label('loc_706')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_71C',
    )

    SetChrSubChip(0x0009, 2)

    Jump('loc_721')

    def _loc_71C(): pass

    label('loc_71C')

    SetChrSubChip(0x0009, 0)

    def _loc_721(): pass

    label('loc_721')

    OP_8C(0x0009, 172, 0)
    SetChrFlags(0x0009, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 2, 0x122A)),
            Expr.Return,
        ),
        'loc_861',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7A1',
    )

    ChrTalk(
        0x0009,
        (
            '#0520210956V#730F听说旧校舍是\n',
            '由古老的城塞改建的，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210957V即使有秘密地下室\n',
            '也不奇怪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_85E')

    def _loc_7A1(): pass

    label('loc_7A1')

    OP_A2(0x0001)

    ChrTalk(
        0x0009,
        (
            '#0520210958V#730F隐藏的楼梯吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210959V资料中也没有\n',
            '记载那些东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210960V只是听说旧校舍是\n',
            '以前的城塞改建的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210961V即使有秘密地下室\n',
            '所以即使如此也很正常吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85E(): pass

    label('loc_85E')

    Jump('loc_8B6')

    def _loc_861(): pass

    label('loc_861')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_8B6',
    )

    ChrTalk(
        0x0009,
        (
            '#0520210962V#730F在这种时候\n',
            '先在原地待命吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210963V一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B6(): pass

    label('loc_8B6')

    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x8BF
@scena.Code('func_07_8BF')
def func_07_8BF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8D0',
    )

    Call(0, 0x000A)

    def _loc_8D0(): pass

    label('loc_8D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8DE',
    )

    Call(0, 0x0008)

    Jump('loc_8E2')

    def _loc_8DE(): pass

    label('loc_8DE')

    Call(0, 0x0009)

    def _loc_8E2(): pass

    label('loc_8E2')

    Return()

# id: 0x0008 offset: 0x8E3
@scena.Code('func_08_8E3')
def func_08_8E3():
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    SetChrPos(0x0101, 240, 0, -2890, 225)
    SetChrPos(0x00F7, 560, 0, -3920, 275)
    SetChrPos(0x0105, -600, 0, -2190, 185)
    SetChrPos(0x0104, -260, 0, -5270, 0)
    SetChrPos(0x0127, -1510, 0, -5190, 45)
    SetChrPos(0x0008, -1990, 0, -4400, 45)
    SetChrPos(0x0009, -8610, 0, -3090, 90)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    OP_6D(1300, 0, 4690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_09D0')
    def lambda_09D0():
        OP_6D(-120, 0, -3010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_09D0)

    @scena.Lambda('lambda_09E8')
    def lambda_09E8():
        OP_67(0, 6000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09E8)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_0A1E')
    def lambda_0A1E():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0A1E')

    DispatchAsync2(0x0101, 0x0001, lambda_0A1E)

    @scena.Lambda('lambda_0A2F')
    def lambda_0A2F():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0A2F')

    DispatchAsync2(0x00F7, 0x0001, lambda_0A2F)

    @scena.Lambda('lambda_0A40')
    def lambda_0A40():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0A40')

    DispatchAsync2(0x0105, 0x0001, lambda_0A40)

    @scena.Lambda('lambda_0A51')
    def lambda_0A51():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0A51')

    DispatchAsync2(0x0104, 0x0001, lambda_0A51)

    @scena.Lambda('lambda_0A62')
    def lambda_0A62():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0A62')

    DispatchAsync2(0x0127, 0x0001, lambda_0A62)

    @scena.Lambda('lambda_0A73')
    def lambda_0A73():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0A73')

    DispatchAsync2(0x0008, 0x0001, lambda_0A73)

    @scena.Lambda('lambda_0A84')
    def lambda_0A84():
        OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0A84)

    @scena.Lambda('lambda_0A96')
    def lambda_0A96():
        OP_8E(0x00FE, -2500, 0, -3220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A96)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0520211396V#730F给，老师那里\n',
            '借来的后门钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0009, 0x0101, 0x000003E8, 0x000007D0, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['后门的钥匙']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['后门的钥匙'], 1)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0127, 0x01)
    TerminateThread(0x0008, 0x01)
    OP_8F(0x0009, -2200, 0, -3220, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010211397V#1006F多谢，汉斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050211398V#552F精神十足是不错……\n',
            '情况不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211399V#1019F当的然啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211400V赶快调查旧校舍\n',
            '整治幽灵才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050211401V#055F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211402V#031F呵呵、艾丝蒂尔\n',
            '也到了大显身手的时候呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211403V#030F好了……\n',
            '赶快去试胆吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211404V说不定有魔兽，\n',
            '某种程度来说\n',
            '会武术的人去会比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050211405V#053F啊啊，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211406V#050F摄影师小姐倒还好说，\n',
            '学生们就请回避吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211407V#648F#6P知道啦。\n',
            '可能会碍手碍脚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520211408V#730F在这种时候\n',
            '就待在这里待命啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211409V#043F那个、阿加特先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211410V我也……\n',
            '一起去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E07')
    def lambda_0E07():
        ChrTurnDirection(0x0101, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E07)

    ChrTalk(
        0x0106,
        (
            '#0050211411V#052F喂喂，公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211412V你还是不要做出\n',
            '轻率之举比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211413V#047F孤儿院的孩子们也在看着我，\n',
            '以我个人来说也不能置之不理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211414V#040F而且以前我去过\n',
            '好几次旧校舍，\n',
            '应该能帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050211415V#053F……真没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211416V#051F算了，你的本事\n',
            '要同行也还是够的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211417V小心别乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211418V#542F是，我会谨记于心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010211419V#1006F好，那就决定了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211420V为了抓住幽灵\n',
            '去旧校舍吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211421V#151FＧＯ～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-2290, 0, -3350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -2290, 0, -3350, 270)
    SetChrPos(0x00F7, -2290, 0, -3350, 270)
    SetChrPos(0x0105, -2290, 0, -3350, 270)
    SetChrPos(0x0104, -2290, 0, -3350, 270)
    SetChrPos(0x0127, -2290, 0, -3350, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0008, -1810, 300, -1250, 269)
    SetChrPos(0x0009, -3520, 300, 200, 158)
    SetChrChipByIndex(0x0008, 3)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0009, 4)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    FadeIn(1000, 0)
    OP_A2(0x1222)
    OP_28(0x0083, 0x01, 0x0080)
    OP_28(0x0084, 0x04, 0x02)
    OP_28(0x0084, 0x04, 0x08)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x110D
@scena.Code('func_09_110D')
def func_09_110D():
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    SetChrPos(0x0101, 240, 0, -2890, 225)
    SetChrPos(0x00F7, 560, 0, -3920, 275)
    SetChrPos(0x0105, -600, 0, -2190, 185)
    SetChrPos(0x0104, -260, 0, -5270, 0)
    SetChrPos(0x0127, -1510, 0, -5190, 45)
    SetChrPos(0x0008, -1990, 0, -4400, 45)
    SetChrPos(0x0009, -8610, 0, -3090, 90)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    OP_6D(1300, 0, 4690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_11FA')
    def lambda_11FA():
        OP_6D(-120, 0, -3010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11FA)

    @scena.Lambda('lambda_1212')
    def lambda_1212():
        OP_67(0, 6000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1212)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_1248')
    def lambda_1248():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1248')

    DispatchAsync2(0x0101, 0x0001, lambda_1248)

    @scena.Lambda('lambda_1259')
    def lambda_1259():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1259')

    DispatchAsync2(0x00F7, 0x0001, lambda_1259)

    @scena.Lambda('lambda_126A')
    def lambda_126A():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_126A')

    DispatchAsync2(0x0105, 0x0001, lambda_126A)

    @scena.Lambda('lambda_127B')
    def lambda_127B():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_127B')

    DispatchAsync2(0x0104, 0x0001, lambda_127B)

    @scena.Lambda('lambda_128C')
    def lambda_128C():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_128C')

    DispatchAsync2(0x0127, 0x0001, lambda_128C)

    @scena.Lambda('lambda_129D')
    def lambda_129D():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_129D')

    DispatchAsync2(0x0008, 0x0001, lambda_129D)

    @scena.Lambda('lambda_12AE')
    def lambda_12AE():
        OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_12AE)

    @scena.Lambda('lambda_12C0')
    def lambda_12C0():
        OP_8E(0x0009, -2500, 0, -3220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_12C0)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0520211396V#730F给，老师那里\n',
            '借来的后门钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0009, 0x0101, 0x000003E8, 0x000007D0, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['后门的钥匙']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['后门的钥匙'], 1)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0127, 0x01)
    TerminateThread(0x0008, 0x01)
    OP_8F(0x0009, -2200, 0, -3220, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010211423V#1006F多谢，汉斯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211400V赶快调查旧校舍\n',
            '整治幽灵才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211402V#031F呵呵、艾丝蒂尔\n',
            '也到了大显身手的时候呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211403V#030F好了……\n',
            '赶快去试胆吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211404V说不定有魔兽，\n',
            '某种程度来说\n',
            '会武术的人去会比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030211428V#020F那当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211429V朵洛希姑且不论，\n',
            '学生们还是回避吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510211407V#648F#6P知道啦。\n',
            '可能会碍手碍脚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520211408V#730F在这种时候\n',
            '就待在这里待命啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211432V#043F那个、雪拉扎德小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211410V我也……\n',
            '一起去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15A2')
    def lambda_15A2():
        ChrTurnDirection(0x0101, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15A2)

    ChrTalk(
        0x0103,
        (
            '#0030211434V#023F哎呀、公主殿下？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211435V#522F嗯～虽然觉得\n',
            '还是不要轻举妄动为好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211413V#047F孤儿院的孩子们都在看着，\n',
            '以我个人来说也不能置之不理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211414V#040F而且以前我进过\n',
            '好几次旧校舍，\n',
            '应该能帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201371V#026F唔，原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211439V#020F你的本事应该没有问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211440V嗯，好吧。\n',
            '可别太乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211418V#542F是，我会谨记于心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010211419V#1006F好，那就决定了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211420V为了抓住幽灵\n',
            '去旧校舍吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211421V#151FＧＯ～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(-2290, 0, -3350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -2290, 0, -3350, 270)
    SetChrPos(0x00F7, -2290, 0, -3350, 270)
    SetChrPos(0x0105, -2290, 0, -3350, 270)
    SetChrPos(0x0104, -2290, 0, -3350, 270)
    SetChrPos(0x0127, -2290, 0, -3350, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0008, -1810, 300, -1250, 269)
    SetChrPos(0x0009, -3520, 300, 200, 158)
    SetChrChipByIndex(0x0008, 3)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0009, 4)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    FadeIn(1000, 0)
    OP_A2(0x1222)
    OP_28(0x0083, 0x01, 0x0080)
    OP_28(0x0084, 0x04, 0x02)
    OP_28(0x0084, 0x04, 0x08)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x18B7
@scena.Code('func_0A_18B7')
def func_0A_18B7():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_1931'),
        (0x00000001, 'loc_1937'),
        (-1, 'loc_193D'),
    )

    def _loc_1931(): pass

    label('loc_1931')

    OP_A2(0x1200)

    Jump('loc_193D')

    def _loc_1937(): pass

    label('loc_1937')

    OP_A2(0x1201)

    Jump('loc_193D')

    def _loc_193D(): pass

    label('loc_193D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_194B',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_194F')

    def _loc_194B(): pass

    label('loc_194B')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_194F(): pass

    label('loc_194F')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
