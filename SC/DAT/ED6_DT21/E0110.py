import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0110   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '多伦'),
    TXT(0x03, '吉尔'),
    TXT(0x04, '空贼雷古'),
    TXT(0x05, '通信员利昂'),
    TXT(0x06, '空贼阿伦'),
    TXT(0x07, '空贼罗尔'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0110.x'
    header.mapIndex       = 1
    header.bgm            = 87
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x420A
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
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT27/CH03760._CH', 'ED6_DT27/CH03760P._CP'),
        ('ED6_DT27/CH03770._CH', 'ED6_DT27/CH03770P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT27/CH03101._CH', 'ED6_DT27/CH03101P._CP'),
        ('ED6_DT26/CH20416._CH', 'ED6_DT26/CH20416P._CP'),
    ]

# id: 0x10002 offset: 0xDA
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
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
            talkScenaIndex      = 0x0004,
        ),
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 51600,
            triggerZ            = 0,
            triggerY            = 74000,
            triggerRange        = 1000,
            actorX              = 51600,
            actorZ              = 1000,
            actorY              = 74000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FB',
    )

    OP_89(0x0000, 49900, 500, 77980, 270)

    def _loc_1FB(): pass

    label('loc_1FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_255',
    )

    SetChrPos(0x000A, 45810, 0, 6940, 0)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrPos(0x000B, -21870, 650, 4940, 315)
    ClearChrFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    SetChrPos(0x000D, 46020, 0, 77750, 0)
    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_326')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_2C5',
    )

    SetChrPos(0x000A, 45810, 0, 6940, 0)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    SetChrPos(0x000B, -21870, 650, 4940, 315)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0010)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    SetChrPos(0x000C, -22620, 650, 5630, 135)
    SetChrPos(0x000D, 46020, 0, 77750, 0)
    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_326')

    def _loc_2C5(): pass

    label('loc_2C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_2CF',
    )

    Jump('loc_326')

    def _loc_2CF(): pass

    label('loc_2CF')

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000B, 45590, 0, 6950, 0)
    SetChrPos(0x000D, 46020, 0, 77750, 0)
    SetChrPos(0x000E, 47720, 0, 6300, 45)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)

    def _loc_326(): pass

    label('loc_326')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_340',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x85),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F4)
    Event(0, 0x000B)

    Jump('loc_3AC')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_351',
    )

    OP_A3(0x10F0)
    Event(0, 0x0008)

    Jump('loc_3AC')

    def _loc_351(): pass

    label('loc_351')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_368',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0009)

    Jump('loc_3AC')

    def _loc_368(): pass

    label('loc_368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_37F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000A)

    Jump('loc_3AC')

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_390',
    )

    OP_A3(0x10F3)
    Event(0, 0x000C)

    Jump('loc_3AC')

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AC',
    )

    Event(0, 0x0007)

    def _loc_3AC(): pass

    label('loc_3AC')

    Return()

# id: 0x0001 offset: 0x3AD
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CB',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3CB(): pass

    label('loc_3CB')

    OP_22(0x007A, 0x01, 0x3C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 0, 0x1C00)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3EF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_40B')

    def _loc_3EF(): pass

    label('loc_3EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_402',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_40B')

    def _loc_402(): pass

    label('loc_402')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_40B(): pass

    label('loc_40B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_460',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_460(): pass

    label('loc_460')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_478',
    )

    OP_10(0x00, 0x00)
    OP_10(0x05, 0x01)
    OP_10(0x06, 0x00)

    Jump('loc_481')

    def _loc_478(): pass

    label('loc_478')

    OP_10(0x00, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x06, 0x01)

    def _loc_481(): pass

    label('loc_481')

    Return()

# id: 0x0002 offset: 0x482
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_497',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_497(): pass

    label('loc_497')

    Return()

# id: 0x0003 offset: 0x498
@scena.Code('func_03_498')
def func_03_498():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_8D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_852',
    )

    OP_A2(0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 6, 0x2296)),
            Expr.Return,
        ),
        'loc_652',
    )

    ChrTalk(
        0x000A,
        (
            '#0290400629V#200F哟，是你们吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400630V航行控制的故障\n',
            '总算已经解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_561',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400711V#210F真、真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400712V太棒了！\n',
            '不愧是吉尔兄啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_594')

    def _loc_561(): pass

    label('loc_561')

    ChrTalk(
        0x0101,
        (
            '#0010400713V#1000F啊，真的吗？\n',
            '那不是很好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_594(): pass

    label('loc_594')

    ChrTalk(
        0x000A,
        (
            '#0290400634V#200F其实，这全都多亏了\n',
            '拉赛尔博士的建议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400715V真是个了不起的老爷爷啊。\n',
            '连看都没看过，就可以\n',
            '马上说出故障的部位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400636V果然不愧是世界著名的\n',
            '导力学者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84F')

    def _loc_652(): pass

    label('loc_652')

    ChrTalk(
        0x000A,
        (
            '#0290400629V#200F哟，是你们吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400638V航行控制方面出了一些毛病，\n',
            '不过总算已经解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_71F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400719V#210F嘿嘿，吉尔哥哥果然厉害，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400640V简直比导力技师\n',
            '还要了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_78A')

    def _loc_71F(): pass

    label('loc_71F')

    ChrTalk(
        0x0101,
        (
            '#0010400721V#1000F哦～挺了不起的嘛。\n',
            '居然可以自己一个人修理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400642V真是没有辜负空贼的称号呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_78A(): pass

    label('loc_78A')

    ChrTalk(
        0x000A,
        (
            '#0290400643V#200F不，其实都多亏了\n',
            '拉赛尔博士的建议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400644V我们通过导力通信进行联络，\n',
            '他马上就找到了原因。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400645V真是好厉害的老爷爷呢。\n',
            '身为世界著名的导力学者，\n',
            '果然是名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_84F(): pass

    label('loc_84F')

    Jump('loc_8D4')

    def _loc_852(): pass

    label('loc_852')

    ChrTalk(
        0x000A,
        (
            '#0290400646V#200F拉赛尔博士\n',
            '果然是个了不起的学者啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400727V只是听了一下症状，\n',
            '马上就能找到故障部位……\n',
            '实在太厉害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_8D4(): pass

    label('loc_8D4')

    Jump('loc_E50')

    def _loc_8D7(): pass

    label('loc_8D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_E50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 7, 0x221F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 5, 0x222D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8F2',
    )

    Call(0, 0x000D)
    OP_A2(0x0005)

    Return()

    def _loc_8F2(): pass

    label('loc_8F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_95D',
    )

    ChrTalk(
        0x000A,
        (
            '#0290400648V#200F车站终端的密码吗……\n',
            '确实有这个可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400649V总之有试一试\n',
            '的价值呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E50')

    def _loc_95D(): pass

    label('loc_95D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 6, 0x2296)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE1',
    )

    ChrTalk(
        0x000A,
        (
            '#0290400730V#200F呼～真是麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CA',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400731V#210F吉尔哥，有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F0')

    def _loc_9CA(): pass

    label('loc_9CA')

    ChrTalk(
        0x0101,
        (
            '#0010400732V#1000F有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F0(): pass

    label('loc_9F0')

    ChrTalk(
        0x000A,
        (
            '#0290400733V#200F嗯，航行控制方面\n',
            '稍微出了点问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400734V虽然可以勉强起飞，\n',
            '但是无法进行长距离的飞行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A97',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400735V#210F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AD6')

    def _loc_A97(): pass

    label('loc_A97')

    ChrTalk(
        0x0101,
        (
            '#0010400736V#1000F虽、虽然听不大懂，\n',
            '不过看起来很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD6(): pass

    label('loc_AD6')

    ChrTalk(
        0x000A,
        (
            '#0290400737V#200F船体的修复还算可以，\n',
            '但精密仪器就无能为力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400658V不如和『埃尔赛尤』\n',
            '联络一下寻求帮助吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400739V呼、也不知道在通信中\n',
            '能不能解决问题…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400740V#1000F嗯……\n',
            '提妲不能帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070400741V#060F我、我虽然懂得一点……\n',
            '不过最好还是让专业人员来做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400662V因为飞翔引擎在飞船中\n',
            '是最为复杂的部分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400743V#1000F有、有那么复杂啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400744V#1030F看来只能够\n',
            '询问一下了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_CA0(): pass

    label('loc_CA0')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D1F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400665V#210F不过也只有试试看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400666V难得这次可以彼此携手合作，\n',
            '要是不利用一下就太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8B')

    def _loc_D1F(): pass

    label('loc_D1F')

    ChrTalk(
        0x0101,
        (
            '#0010400747V#1000F不过，还是有\n',
            '试试看的必要吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400748V拉赛尔博士也在那里，\n',
            '或许可以给点提示哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8B(): pass

    label('loc_D8B')

    ChrTalk(
        0x000A,
        (
            '#0290400669V#200F嗯，就是这么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400670V还是再耐心地\n',
            '等一等吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2296)

    Jump('loc_E50')

    def _loc_DE1(): pass

    label('loc_DE1')

    ChrTalk(
        0x000A,
        (
            '#0290400671V#200F航行控制的问题\n',
            '凭我们是解决不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400752V毕竟这种精密仪器\n',
            '不是一般人可以修理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E50(): pass

    label('loc_E50')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xE54
@scena.Code('func_04_E54')
def func_04_E54():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_103A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF7',
    )

    OP_A2(0x0001)

    ChrTalk(
        0x000B,
        (
            '噢，小姐，\n',
            '联络工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '多亏『埃尔赛尤』的帮忙，\n',
            '飞翔引擎也修理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '双方一起协力合作，\n',
            '果然是有所价值啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F65')

    def _loc_EF7(): pass

    label('loc_EF7')

    ChrTalk(
        0x000B,
        (
            '多亏『埃尔赛尤』的帮忙，\n',
            '飞翔引擎也修理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呼，毕竟要是帮不上忙的话，\n',
            '协力合作就没有什么价值了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F65(): pass

    label('loc_F65')

    Jump('loc_1037')

    def _loc_F68(): pass

    label('loc_F68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FE9',
    )

    OP_A2(0x0002)

    ChrTalk(
        0x000B,
        (
            '控制装置的故障\n',
            '似乎也已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么～我们也要\n',
            '赶紧调整计量器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '再磨磨蹭蹭的话\n',
            '会被老大骂的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1037')

    def _loc_FE9(): pass

    label('loc_FE9')

    ChrTalk(
        0x000B,
        (
            '控制装置的故障\n',
            '似乎也已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么～我们也要\n',
            '赶紧调整计量器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1037(): pass

    label('loc_1037')

    Jump('loc_1226')

    def _loc_103A(): pass

    label('loc_103A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_11ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1176',
    )

    OP_A2(0x0002)

    ChrTalk(
        0x000C,
        (
            '这里是埃尔赛尤号……\n',
            '……山猫号，请回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '……重复一次，山猫号请回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊啊，这里是山猫号……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '接收信号良好……\n',
            '埃尔赛尤号，你们那里听得清楚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '埃尔赛尤呼叫山猫号……\n',
            '我们这边的信号也很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '贵舰现在有\n',
            '什么物资不足吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '重复一次……\n',
            '山猫号，有什么物资不足吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11EA')

    def _loc_1176(): pass

    label('loc_1176')

    ChrTalk(
        0x000B,
        (
            '呃～其实我们的航行控制装置\n',
            '出了点问题无法解决，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '希望贵舰的维修员能提供建议。\n',
            '重复一次，希望贵舰的维修员…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11EA(): pass

    label('loc_11EA')

    Jump('loc_1226')

    def _loc_11ED(): pass

    label('loc_11ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_11F7',
    )

    Jump('loc_1226')

    def _loc_11F7(): pass

    label('loc_11F7')

    ChrTalk(
        0x000B,
        (
            '喔！快点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '多伦老大\n',
            '在舰桥等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1226(): pass

    label('loc_1226')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x122A
@scena.Code('func_05_122A')
def func_05_122A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_1377',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_131A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12C1',
    )

    OP_A2(0x0003)

    ChrTalk(
        0x000D,
        (
            '啊，小姐……\n',
            '您辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '飞翔引擎也修好了，\n',
            '现在已经完全恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '『山猫号』马上\n',
            '就能完全复原了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1317')

    def _loc_12C1(): pass

    label('loc_12C1')

    ChrTalk(
        0x000D,
        (
            '飞翔引擎也修好了，\n',
            '现在已经完全恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '『山猫号』马上\n',
            '就能完全复原了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1317(): pass

    label('loc_1317')

    Jump('loc_1374')

    def _loc_131A(): pass

    label('loc_131A')

    ChrTalk(
        0x00FE,
        (
            '飞翔引擎修复完毕\n',
            '可真是个好消息啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样看来的话，\n',
            '『山猫号』就能再次起飞了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1374(): pass

    label('loc_1374')

    Jump('loc_155D')

    def _loc_1377(): pass

    label('loc_1377')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_1505',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1431',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13E6',
    )

    OP_A2(0x0003)

    ChrTalk(
        0x000D,
        (
            '啊，小姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '嘿嘿，刚才您\n',
            '真是太帅了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '小姐果然\n',
            '是我们的女神啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_142E')

    def _loc_13E6(): pass

    label('loc_13E6')

    ChrTalk(
        0x000D,
        (
            '嘿嘿，刚才您\n',
            '真是太帅了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我们会努力修船，\n',
            '请小姐耐心期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_142E(): pass

    label('loc_142E')

    Jump('loc_1502')

    def _loc_1431(): pass

    label('loc_1431')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14A4',
    )

    OP_A2(0x0004)

    ChrTalk(
        0x000D,
        (
            '哦，是你们啊。\n',
            '刚才多谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '『结社』的那群家伙\n',
            '还真是奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '你们最好\n',
            '也多加小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1502')

    def _loc_14A4(): pass

    label('loc_14A4')

    ChrTalk(
        0x000D,
        (
            '『结社』的那群家伙\n',
            '还真是奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我们本来也有相当的实力，\n',
            '但却完全不是他们的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1502(): pass

    label('loc_1502')

    Jump('loc_155D')

    def _loc_1505(): pass

    label('loc_1505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_150F',
    )

    Jump('loc_155D')

    def _loc_150F(): pass

    label('loc_150F')

    ChrTalk(
        0x00FE,
        (
            '不过多伦老大竟然会\n',
            '下这种作战命令，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仔细想想的话\n',
            '实在太冒险了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_155D(): pass

    label('loc_155D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1561
@scena.Code('func_06_1561')
def func_06_1561():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '『山猫号』一切顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，也就是说\n',
            '接下来就看你的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x15A9
@scena.Code('func_07_15A9')
def func_07_15A9():
    EventBegin(0x00)
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x000A, -18850, 3000, 5010, 270)
    SetChrPos(0x0009, -22460, 650, 4800, 315)
    SetChrPos(0x0008, -19890, 0, 3030, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0102, -15530, 500, 4940, 270)
    SetChrFlags(0x0102, 0x0080)
    OP_6D(-20530, 650, 5540, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(313000, 0)
    OP_6E(282, 0)
    Call(0, 0x000E)
    OP_79(0x09, 0x0001)
    OP_7B()
    FadeIn(1000, 0)
    OP_0D()
    ClearChrFlags(0x0102, 0x0080)
    OP_9F(0x0102, 0x00, 0x00, 0x00, 0x00, 0x00000000)

    @scena.Lambda('lambda_166E')
    def lambda_166E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_166E)

    OP_8E(0x0102, -17510, 0, 4860, 2000, 0x00)
    OP_8C(0x0009, 90, 400)
    Sleep(100)

    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#0300320068V#190F喔，来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320069V#215F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320070V#1032F状况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300320071V#490F嘿，果然如你所料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320072V过来。\n',
            '看这里的屏幕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1766')
    def lambda_1766():
        OP_6D(-22030, 650, 5690, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1766)

    @scena.Lambda('lambda_177E')
    def lambda_177E():
        OP_6C(322000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_177E)

    @scena.Lambda('lambda_178E')
    def lambda_178E():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_178E)

    @scena.Lambda('lambda_179C')
    def lambda_179C():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_179C')

    DispatchAsync2(0x0008, 0x0001, lambda_179C)

    OP_8E(0x0102, -21700, 650, 5340, 2000, 0x00)
    OP_8C(0x0102, 315, 400)
    Sleep(200)

    WaitForThreadExit(0x0102, 0x0002)
    TerminateThread(0x0008, 0x01)
    OP_8C(0x0102, 315, 400)

    ChrTalk(
        0x0009,
        (
            '#0300320073V#198F#6P他们正在１５６０亚矩的高度，\n',
            '以２１００塞尔矩的时速\n',
            '从东北方向潜入利贝尔领空…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320074V从这种高度和速度来看，\n',
            '绝对不是普通的飞船啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320075V#197F你装上的这个特殊雷达\n',
            '看来还真有点用处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320076V#1035F#6P不，现在还不能确定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320077V#1031F也有可能是帝国的\n',
            '侦察艇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000A, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020320078V#1030F#5P吉尔，目视的情况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290320079V#201F……捕捉到了！\n',
            '我把影像传到你们那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMapFlags(0x02000000)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x19AA
@scena.Code('func_08_19AA')
def func_08_19AA():
    EventBegin(0x00)
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x000A, -18850, 3000, 5010, 280)
    SetChrPos(0x0009, -22460, 650, 4800, 315)
    SetChrPos(0x0008, -19890, 0, 3030, 315)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0102, -21700, 650, 5340, 315)
    OP_6D(-22030, 650, 5690, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(282, 0)
    Call(0, 0x000E)
    OP_79(0x09, 0x0001)
    OP_7B()
    OP_74(0x0004, 0x00000005, 0x0010)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320080V#1032F#6P……没错。\n',
            '这就是此次的目标',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290320081V#200F#2P嘿嘿……\n',
            '终于准备妥当了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320082V还真是有些紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0300320083V#198F#5P好！这就开始吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320084V#490F小子！\n',
            '做好心理准备了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320085V#1031F#4P没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320086V等我站好位置之后，\n',
            '马上就可以开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 90, 400)

    @scena.Lambda('lambda_1BC0')
    def lambda_1BC0():
        OP_8E(0x00FE, -17510, 0, 4860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1BC0)

    @scena.Lambda('lambda_1BDB')
    def lambda_1BDB():
        OP_6D(-21030, 500, 5850, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1BDB)

    @scena.Lambda('lambda_1BF3')
    def lambda_1BF3():
        OP_6C(313000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1BF3)

    @scena.Lambda('lambda_1C03')
    def lambda_1C03():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1C03')

    DispatchAsync2(0x0008, 0x0003, lambda_1C03)

    ChrTalk(
        0x0008,
        (
            '#0090320087V#216F#12A啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_8C(0x000A, 90, 400)
    WaitForThreadExit(0x0102, 0x0001)
    TerminateThread(0x0008, 0x03)
    OP_8C(0x0008, 90, 400)
    OP_20(0x000005DC)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0102)
    Sleep(500)

    OP_1D(0x50)
    Sleep(1500)

    ChrTalk(
        0x0102,
        (
            '#0020320088V#1035F#5P多伦兄，吉尔兄，\n',
            '还有乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320089V#1031F这些日子…多谢你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320090V虽然我们只是互利性质的合作关系，\n',
            '但我是真正发自内心地感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320091V#213F#5P……咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290320092V#201F#5P嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300320093V#192F#5P噢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320094V#1031F#4P这些话本来想在战斗\n',
            '结束之后再说的，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320095V也许再也没有那个机会了，\n',
            '所以就趁现在先对你们说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320096V#1053F那么，各位多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 90, 400)
    Sleep(500)

    @scena.Lambda('lambda_1E52')
    def lambda_1E52():
        OP_6D(-20270, 500, 6030, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1E52)

    @scena.Lambda('lambda_1E6A')
    def lambda_1E6A():
        OP_8E(0x00FE, -16450, 250, 4900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1E6A)

    WaitForThreadExit(0x0102, 0x0000)

    @scena.Lambda('lambda_1E8A')
    def lambda_1E8A():
        OP_8E(0x00FE, -15500, 500, 4920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1E8A)

    @scena.Lambda('lambda_1EA5')
    def lambda_1EA5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1EA5)

    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)
    SetChrFlags(0x0102, 0x0080)
    Sleep(1000)

    @scena.Lambda('lambda_1ED0')
    def lambda_1ED0():
        OP_6D(-22030, 650, 5690, 1800)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1ED0)

    WaitForThreadExit(0x0102, 0x0002)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0290320097V#207F#5P那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300320098V#197F#5P真是的……\n',
            '都到最后关头了还是这个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320099V#212F#5P……呜………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 4)

    @scena.Lambda('lambda_1F84')
    def lambda_1F84():
        OP_6D(-20270, 500, 6030, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1F84)

    OP_8E(0x0008, -18860, 0, 2930, 5000, 0x00)
    OP_8E(0x0008, -17980, 0, 4310, 5000, 0x00)
    OP_8E(0x0008, -16450, 250, 4900, 5000, 0x00)

    @scena.Lambda('lambda_1FD8')
    def lambda_1FD8():
        OP_8E(0x00FE, -15500, 500, 4920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1FD8)

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x0008, 0x0080)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x2015
@scena.Code('func_09_2015')
def func_09_2015():
    EventBegin(0x00)
    OP_A3(0x10F1)
    OP_24(0x007A, 0x64)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, -24400, -1000, 4970, 270)
    SetChrPos(0x0009, -22260, 650, 5230, 308)
    SetChrPos(0x0008, -18850, 3000, 5010, 280)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x000A, 5)
    SetChrSubChip(0x000A, 0)
    OP_6D(-22890, 0, 6950, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(267, 0)
    Call(0, 0x000E)
    OP_79(0x09, 0x0001)
    OP_7B()
    OP_76(0x000C, 0x00000000, 0x0001, 0xFFFFFFEC, 0xFFFFFFFC, 0x00000000, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0090320136V#415F#2P好啊！！……他成功了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300320137V#191F#6P哦哦！\n',
            '竟然成功了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290320138V#201F#6P很好！\n',
            '那我们也可以撤退了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x2191
@scena.Code('func_0A_2191')
def func_0A_2191():
    EventBegin(0x00)
    OP_A3(0x10F2)
    OP_24(0x007A, 0x50)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, -24400, -1000, 4970, 270)
    SetChrPos(0x0009, -22260, 650, 5230, 308)
    SetChrPos(0x0008, -18850, 3000, 5010, 280)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x000A, 5)
    SetChrSubChip(0x000A, 0)
    OP_6D(-22890, 0, 6950, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(322000, 0)
    OP_6E(267, 0)
    Call(0, 0x000E)
    OP_76(0x000C, 0x00000000, 0x0001, 0xFFFFFFF6, 0xFFFFFFFE, 0x00000000, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0300320147V#490F#6P嘿嘿……\n',
            '他们放弃追击了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320148V一切都和那小子\n',
            '预料的一模一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320149V#215F#2P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320150V#413F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000A, 2)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0290320151V#204F#6P乔丝特，不用担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320152V#200F那家伙的话……\n',
            '一定可以平安回来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090320153V#215F#2P嗯……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320154V#210F我们约定好的……\n',
            '一定要平安回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_20(0x00000FA0)
    Sleep(300)

    OP_24(0x007A, 0x46)
    Sleep(300)

    OP_24(0x007A, 0x3C)
    Sleep(300)

    OP_24(0x007A, 0x32)
    Sleep(300)

    OP_24(0x007A, 0x28)
    Sleep(300)

    OP_24(0x007A, 0x1E)
    Sleep(300)

    OP_24(0x007A, 0x14)
    Sleep(300)

    OP_24(0x007A, 0x0A)
    Sleep(300)

    OP_23(0x007A)
    OP_0D()
    OP_21()
    OP_AD(0x002400A9, 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    ClearMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x2465
@scena.Code('func_0B_2465')
def func_0B_2465():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrPos(0x000A, -24300, -1000, 4970, 270)
    SetChrPos(0x0009, -21860, 650, 4770, 270)
    SetChrPos(0x0008, -18850, 3000, 5010, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    OP_6D(-24130, 0, 7440, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(322000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x000B, 0x0080)
    TerminateThread(0x000A, 0xFF)
    SetChrChipByIndex(0x000A, 5)
    SetChrSubChip(0x000A, 0)
    Call(0, 0x000F)
    OP_22(0x007A, 0x01, 0x50)
    OP_76(0x000B, 0x00000000, 0x0001, 0x00000000, 0x00000000, 0x00000000, 0x00, 0x00)
    OP_76(0x000B, 0x00000001, 0x0001, 0xFFFFFFFF, 0x00000000, 0x00000000, 0x00, 0x00)
    OP_76(0x000B, 0x00000002, 0x0001, 0xFFFFFFFC, 0x00000000, 0x00000000, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_6B(3100, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0090421135V#418F#2P求求你，吉尔哥！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090421136V这样下去的话\n',
            '约修亚他们就……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290421137V#204F#6P没用的，乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290421138V#207F……照现在的样子来看，他们恐怕已经……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090421139V#417F#2P怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300421140V#198F……可恶……\n',
            '都已经到了最后一步，为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300421141V#196F这种时候……\n',
            '女神到底在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x26DA
@scena.Code('func_0C_26DA')
def func_0C_26DA():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x000A, -24300, -1000, 4970, 270)
    SetChrPos(0x0009, -21860, 650, 4770, 315)
    SetChrPos(0x0008, -18850, 3000, 5010, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    OP_6D(-24130, 0, 8000, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(322000, 0)
    OP_6E(322, 0)
    SetChrChipByIndex(0x000A, 5)
    SetChrSubChip(0x000A, 0)
    Call(0, 0x000F)
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x01, 'C_VIS227._CH')
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C5(0x01, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS180._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 1000, 0)
    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    Sleep(1000)

    OP_22(0x007C, 0x00, 0x64)
    OP_C5(0x02, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS181._CH')
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    Sleep(1000)

    Sleep(1000)

    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName('女孩的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0090350001V不、不会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x02, 0x03, 16777215, 1000, 0)
    Sleep(1000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    FadeIn(1000, 0)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    OP_8F(0x0008, -18410, 3000, 4730, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0090350002V#216F#2P那、那是什么东西啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090350003V竟然那么大……\n',
            '也太夸张了吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300350004V#192F#6P那东西，大概有\n',
            '５０００亚矩以上吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300350005V简直是个巨大的空中浮岛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290350006V#204F#6P不……基本上像是座人造建筑物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290350007V#206F与其说是岛屿，\n',
            '不如说是一座浮游都市……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350008V#213F#2P浮、浮游都市……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300350009V#198F#6P……这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0004)
    OP_8C(0x0009, 270, 400)
    OP_8E(0x0009, -22410, 650, 4680, 1500, 0x00)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0300350010V#196F#6P#3S……很好～～！小子们！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0300350011V#196F#6P#3S一鼓作气给我冲上那座浮游都市！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x000A, 2)

    ChrTalk(
        0x000A,
        (
            '#0290350012V#201F#6P大、大哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350013V#213F#2P你、你是认真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x0009, -21860, 650, 4770, 2000, 0x00)
    OP_8C(0x0009, 135, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0300350014V#490F#5P当然是说真的！真的不能再真！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300350015V#198F如果这东西是『结社』的那群家伙\n',
            '所召唤出来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300350016V#191F里面肯定会有\n',
            '数不尽的神秘宝藏！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290350017V#203F#6P大、大哥，你就饶了我们吧～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290350018V#201F凭我们的实力，\n',
            '要硬闯的话实在是太冒险了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290350019V乔丝特，你也是这么想的吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350020V#413F#2P嗯、这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090350021V#215F我觉得、都已经到这种地步了，\n',
            '不如去确认一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290350022V#203F#6P呃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350023V#415F#2P好、好了！总之从昨夜开始\n',
            '就有点不对劲，还是小心点比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090350024V导力通讯也完全收不到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0300350025V#197F#5P的确，军方和协会也就算了，\n',
            '但民间的通信也收不到的话──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    OP_20(0x000007D0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6D(-24130, 0, 8000, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(322000, 0)
    OP_6E(322, 0)
    OP_0D()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x000A, 0)
    OP_8C(0x0009, 270, 500)

    ChrTalk(
        0x0009,
        (
            '#0300350026V#192F#6P呜喔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290350027V#201F#6P什…什么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350028V#213F#2P光、光波……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    OP_82(0x80, 0x00)
    OP_0D()
    Fade(500)
    OP_22(0x00E1, 0x00, 0x64)
    OP_23(0x007A)
    OP_71(0x0005, 0x0004)
    Sleep(100)

    OP_71(0x0006, 0x0004)
    Sleep(100)

    OP_71(0x0007, 0x0004)
    Sleep(100)

    OP_71(0x0008, 0x0004)
    Sleep(100)

    OP_71(0x0009, 0x0004)
    OP_74(0x0004, 0x00000005, 0x0000)
    OP_0D()
    Sleep(500)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0090350029V#216F#2P哎哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x51)
    Sleep(500)

    OP_8C(0x0009, 315, 400)

    ChrTalk(
        0x0009,
        (
            '#0300350030V#192F#6P怎么回事？！故障吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, -14000, 500, 4660, 270)
    OP_4A(0x000B, 255)

    ChrTalk(
        0x000B,
        (
            '#1040350031V#1P老大，不好了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_318A')
    def lambda_318A():
        OP_6D(-22710, 0, 7190, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_318A)

    @scena.Lambda('lambda_31A2')
    def lambda_31A2():
        OP_67(0, 4640, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_31A2)

    @scena.Lambda('lambda_31BA')
    def lambda_31BA():
        OP_6B(2920, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_31BA)

    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_31CF')
    def lambda_31CF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_31CF)

    @scena.Lambda('lambda_31E1')
    def lambda_31E1():
        OP_8E(0x000B, -15500, 500, 4870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_31E1)

    WaitForThreadExit(0x000B, 0x0001)
    ClearChrFlags(0x000B, 0x0004)

    @scena.Lambda('lambda_3206')
    def lambda_3206():
        OP_8E(0x000B, -17510, 0, 4860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3206)

    @scena.Lambda('lambda_3221')
    def lambda_3221():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3221)

    Sleep(50)

    @scena.Lambda('lambda_3234')
    def lambda_3234():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3234)

    Sleep(50)

    WaitForThreadExit(0x000B, 0x0001)
    Sleep(500)

    WaitForThreadExit(0x0009, 0x0000)

    ChrTalk(
        0x000B,
        (
            '#1040350032V#4P导力引擎、还有飞翔引擎\n',
            '全都突然停止运转了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#0300350033V#196F#5P什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350034V#216F#5P这是怎、怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290350035V#206F#6P……这下麻烦了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290350036V飞翔引擎所产生的\n',
            '反重力力场下降……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290350037V舵也没有反应了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_33AF')
    def lambda_33AF():
        OP_6D(-24130, 0, 7440, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_33AF)

    @scena.Lambda('lambda_33C7')
    def lambda_33C7():
        OP_67(0, 5440, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_33C7)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0009, 0x000A, 400)
    ChrTurnDirection(0x0008, 0x000A, 400)
    WaitForThreadExit(0x0009, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#0300350038V#196F#5P等、等一下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090350039V#214F#2P怎、怎么会这样呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290350040V#204F#6P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290350041V#207F……到这种地步的话，\n',
            '我们能做的就只有一件事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#192F#1P是什么！？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0090350043V#213F#2P是什么！？',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Sleep(100)

    SetChrSubChip(0x000A, 2)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0290350044V#203F#6P向女神祈祷，让我们不要\n',
            '这么早就被召唤到天堂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x000007D0)
    OP_22(0x00EC, 0x00, 0x64)
    OP_D0(5000, 0)
    Sleep(1000)

    OP_22(0x013B, 0x00, 0x64)

    @scena.Lambda('lambda_35A3')
    def lambda_35A3():
        OP_6D(-18330, 15000, 5500, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_35A3)

    @scena.Lambda('lambda_35BB')
    def lambda_35BB():
        OP_D0(25000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_35BB)

    Sleep(1000)

    SetMapFlags(0x02000000)
    SetMapFlags(0x00100000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x35EC
@scena.Code('func_0D_35EC')
def func_0D_35EC():
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
        'loc_3611',
    )

    Call(0, 0x0010)
    Call(0, 0x0011)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_3611(): pass

    label('loc_3611')

    Fade(500)
    OP_6D(45440, 0, 6250, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 45620, 0, 5160, 0)
    SetChrPos(0x0102, 46440, 0, 5370, 0)
    SetChrPos(0x00F8, 44470, 0, 5520, 45)
    SetChrPos(0x00F9, 47260, 0, 5750, 315)
    OP_8C(0x000A, 180, 0)
    OP_4A(0x000A, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0290400567V#200F对了……忘了一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400568V你们听过\n',
            '『Ｏ·Ｒ·Ｐ·Ｈ·Ｅ·Ｕ·Ｓ』\n',
            '这个词吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400569V#1000F那、那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_377F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400570V#210FＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F4')

    def _loc_377F(): pass

    label('loc_377F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37CA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400571V#040FＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F4')

    def _loc_37CA(): pass

    label('loc_37CA')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3815',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400572V#030FＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F4')

    def _loc_3815(): pass

    label('loc_3815')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3861',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400573V#1060FＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F4')

    def _loc_3861(): pass

    label('loc_3861')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38AC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400574V#060FＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38F4')

    def _loc_38AC(): pass

    label('loc_38AC')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38F4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400575V#050FＯＲＰＨＥＵＳ……\n',
            '是读作奥菲斯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38F4(): pass

    label('loc_38F4')

    ChrTalk(
        0x0102,
        (
            '#0020400576V#1030F……这个词怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290400577V#200F没什么，只是监视我们的\n',
            '猎兵们曾经提到过它。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400578V我觉得它可能有什么含义，\n',
            '所以就记下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A1E',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400579V#210F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400580V#1000F嗯……\n',
            '确实让人很在意呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400581V（啊……也许是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A6F')

    def _loc_3A1E(): pass

    label('loc_3A1E')

    ChrTalk(
        0x0101,
        (
            '#0010400580V#1000F嗯……\n',
            '确实让人很在意呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400583V（啊……也许是！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A6F(): pass

    label('loc_3A6F')

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
            TXT(0x00, '【工业区域的通称】\n'),
            TXT(0x01, '【福音的正式名称】\n'),
            TXT(0x02, '【终端密码】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3AEB'),
        (0x00000001, 'loc_3B9F'),
        (0x00000002, 'loc_3C5E'),
        (-1, 'loc_3CD0'),
    )

    def _loc_3AEB(): pass

    label('loc_3AEB')

    ChrTalk(
        0x0102,
        (
            '#0020400584V#1030F不对，工业区域的名称是\n',
            '『法克特里亚』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400585V也许是……\n',
            '工业区域的终端所要求输入\n',
            '的密码也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400586V#1000F啊……是车站的终端！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CD0')

    def _loc_3B9F(): pass

    label('loc_3B9F')

    ChrTalk(
        0x0102,
        (
            '#0020400587V#1030F不，『福音』的名字\n',
            '在这座都市里似乎也是\n',
            '同样的叫法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400588V也许是……\n',
            '工业区域的终端所要求输入\n',
            '的密码也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400586V#1000F啊……是车站的终端！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CD0')

    def _loc_3C5E(): pass

    label('loc_3C5E')

    ChrTalk(
        0x0102,
        (
            '#0020400590V#1030F嗯。\n',
            '大概就是工业区域车站的终端密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400591V#1000F啊，约修亚也是这么想的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CD0')

    def _loc_3CD0(): pass

    label('loc_3CD0')

    ChrTalk(
        0x000A,
        (
            '#0290400592V#200F？　怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将工业区域终端\n',
            '需要输入密码才能打开地下道入口\n',
            '的事情向吉尔说明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x000A,
        (
            '#0290400593V#200F原来如此……\n',
            '确实有这个可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400594V看来很有试一试的价值啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400595V#1000F嘿嘿嘿，果然没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E0C',
    )

    ChrTalk(
        0x010B,
        (
            '#0090400596V#210F谢谢啦，吉尔哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E0C(): pass

    label('loc_3E0C')

    ChrTalk(
        0x0102,
        (
            '#0020400597V#1030F我们赶快去确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 0, 400)
    OP_4B(0x000A, 0)
    OP_A2(0x222D)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x3E4B
@scena.Code('func_0E_3E4B')
def func_0E_3E4B():
    OP_71(0x0002, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)

    Return()

# id: 0x000F offset: 0x3E83
@scena.Code('func_0F_3E83')
def func_0F_3E83():
    OP_71(0x0002, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)

    Return()

# id: 0x0010 offset: 0x3EBB
@scena.Code('func_10_3EBB')
def func_10_3EBB():
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
        (0x00000000, 'loc_3F35'),
        (0x00000001, 'loc_3F3B'),
        (-1, 'loc_3F41'),
    )

    def _loc_3F35(): pass

    label('loc_3F35')

    OP_A2(0x1200)

    Jump('loc_3F41')

    def _loc_3F3B(): pass

    label('loc_3F3B')

    OP_A2(0x1201)

    Jump('loc_3F41')

    def _loc_3F41(): pass

    label('loc_3F41')

    Return()

# id: 0x0011 offset: 0x3F42
@scena.Code('func_11_3F42')
def func_11_3F42():
    FadeOut(0, 0, -1)
    OP_6D(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0012 offset: 0x3FD5
@scena.Code('func_12_3FD5')
def func_12_3FD5():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4028',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_41E3')

    def _loc_4028(): pass

    label('loc_4028')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
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
            TXT(0x00, '在这里休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41C8',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_82(0x00, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x000A, 0)
    OP_70(0x000A, 0x00000032)
    OP_73(0x000A)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 51600, 1000, 74000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x000A, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_41C8(): pass

    label('loc_41C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41E2',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_41E2(): pass

    label('loc_41E2')

    Return()

    def _loc_41E3(): pass

    label('loc_41E3')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
