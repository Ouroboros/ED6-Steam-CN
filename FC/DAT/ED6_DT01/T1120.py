import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1120   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '马尔科'),
    TXT(0x02, '尼冈德'),
    TXT(0x03, '卡莉娅'),
    TXT(0x04, '赛恩'),
    TXT(0x05, '奈尔'),
    TXT(0x06, '朵洛希'),
    TXT(0x07, '科梅尔斯'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1120.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x24C2
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
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -25890,
            z                   = 0,
            y                   = 1370,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -24500,
            z                   = 0,
            y                   = 4690,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -28800,
            z                   = 0,
            y                   = 24200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 500,
            z                   = 0,
            y                   = 7400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -24500,
            z                   = 0,
            y                   = 4690,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -24000,
            triggerZ            = 0,
            triggerY            = 3580,
            triggerRange        = 700,
            actorX              = -24500,
            actorZ              = 1500,
            actorY              = 4690,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 920,
            triggerZ            = 0,
            triggerY            = 6280,
            triggerRange        = 700,
            actorX              = 500,
            actorZ              = 1500,
            actorY              = 7400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x20A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_228',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0008, 0x0080)

    Jump('loc_292')

    def _loc_228(): pass

    label('loc_228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_248',
    )

    SetChrFlags(0x0009, 0x0010)
    SetChrPos(0x000A, -27920, 0, 87590, 270)

    Jump('loc_292')

    def _loc_248(): pass

    label('loc_248')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_26D',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0010)
    SetChrPos(0x000A, -27920, 0, 87590, 270)

    Jump('loc_292')

    def _loc_26D(): pass

    label('loc_26D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_277',
    )

    Jump('loc_292')

    def _loc_277(): pass

    label('loc_277')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_281',
    )

    Jump('loc_292')

    def _loc_281(): pass

    label('loc_281')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_28B',
    )

    Jump('loc_292')

    def _loc_28B(): pass

    label('loc_28B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_292',
    )

    def _loc_292(): pass

    label('loc_292')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_2A2'),
        (0x0000006A, 'loc_2A2'),
        (-1, 'loc_2B8'),
    )

    def _loc_2A2(): pass

    label('loc_2A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 0, 0x338)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B5',
    )

    SetScenaFlags(ScenaFlag(0x0067, 0, 0x338))
    Event(0, 0x0010)

    def _loc_2B5(): pass

    label('loc_2B5')

    Jump('loc_2B8')

    def _loc_2B8(): pass

    label('loc_2B8')

    Return()

# id: 0x0001 offset: 0x2B9
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CB',
    )

    OP_10(0x07, 0x01)
    OP_10(0x03, 0x00)

    def _loc_2CB(): pass

    label('loc_2CB')

    Return()

# id: 0x0002 offset: 0x2CC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2E1(): pass

    label('loc_2E1')

    Return()

# id: 0x0003 offset: 0x2E2
@scena.Code('func_03_2E2')
def func_03_2E2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_36A',
    )

    TalkBegin(0x000E)
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
        'loc_34B',
    )

    OP_0D()
    OP_A9(0x0A)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_34B(): pass

    label('loc_34B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35C',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_35C(): pass

    label('loc_35C')

    Call(0, 0x000B)
    SetChrDirection(0x000E, 180, 0)

    Jump('loc_3E8')

    def _loc_36A(): pass

    label('loc_36A')

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

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '改造·换钱\n'),
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
        'loc_3CC',
    )

    OP_0D()
    OP_A9(0x0A)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DD',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_3DD(): pass

    label('loc_3DD')

    Call(0, 0x0004)
    SetChrDirection(0x0009, 180, 0)
    def _loc_3E8(): pass

    label('loc_3E8')

    Return()

# id: 0x0004 offset: 0x3E9
@scena.Code('func_04_3E9')
def func_04_3E9():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_519',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '账、账、账、\n',
            '账本被军队没收了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '糟了糟了糟了啊……',
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
            '不、不，等等……\n',
            '应该不会出事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为最不能被查到的东西\n',
            '已经被强盗拿走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_516')

    def _loc_4B4(): pass

    label('loc_4B4')

    ChrTalk(
        0x0009,
        (
            '账本虽然被军队没收了，\n',
            '不过应该不会出事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为最不能被查到的东西\n',
            '已经被强盗拿走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_516(): pass

    label('loc_516')

    Jump('loc_9CF')

    def _loc_519(): pass

    label('loc_519')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_68F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_638',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '工、工、工房～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我、我的工房里……商品都被～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要、要快点去向\n',
            '军队或者游击士协会通报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不、不，等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果他们来调查\n',
            '被盗走的那个东西的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '哇哇哇哇……\n',
            '我该怎么做才好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68C')

    def _loc_638(): pass

    label('loc_638')

    ChrTalk(
        0x0009,
        (
            '如果他们来调查\n',
            '被盗走的那个东西的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哇哇哇哇……\n',
            '我该怎么做才好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_68C(): pass

    label('loc_68C')

    Jump('loc_9CF')

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_74E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_722',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '店里的营业额走势非常好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然在与工匠的沟通上还有些问题，\n',
            '不过没关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嘿嘿嘿……\n',
            '这样下去真能大赚一笔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_74B')

    def _loc_722(): pass

    label('loc_722')

    ChrTalk(
        0x0009,
        (
            '嘿嘿嘿……\n',
            '这样下去真能大赚一笔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_74B(): pass

    label('loc_74B')

    Jump('loc_9CF')

    def _loc_74E(): pass

    label('loc_74E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_850',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7EF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '说起来，\n',
            '那个人也真是太老实了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哼，\n',
            '这在商人的世界里\n',
            '可是站不住脚的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我才最适合\n',
            '当这家店的店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哇～哈～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84D')

    def _loc_7EF(): pass

    label('loc_7EF')

    ChrTalk(
        0x0009,
        (
            '说起来，\n',
            '那个人也真是太老实了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我才最适合\n',
            '当这家店的店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哇～哈～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84D(): pass

    label('loc_84D')

    Jump('loc_9CF')

    def _loc_850(): pass

    label('loc_850')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_964',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '呼～呼～呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哇～哈～哈～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '笑得合不拢嘴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '没想到这么简单\n',
            '就弄到自己的工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这个世界只有聪明的人\n',
            '才能够生存下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_961')

    def _loc_8FF(): pass

    label('loc_8FF')

    ChrTalk(
        0x0009,
        (
            '没想到这么简单\n',
            '就弄到自己的工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '笑得合不拢嘴了。\n',
            '这个世界只有聪明的人才能生存下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_961(): pass

    label('loc_961')

    Jump('loc_9CF')

    def _loc_964(): pass

    label('loc_964')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_9CF',
    )

    ChrTalk(
        0x0009,
        (
            '呼，从今天开始\n',
            '我就是这里的经营者了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '太棒了！\n',
            '我要赚越来越多的钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哇～哈～哈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9CF(): pass

    label('loc_9CF')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x9D3
@scena.Code('func_05_9D3')
def func_05_9D3():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_AC1',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_A38',
    )

    ChrTalk(
        0x00FE,
        (
            '以前的店主\n',
            '回到店里来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢天谢地，\n',
            '这下又可以专心地研究技术了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ABE')

    def _loc_A38(): pass

    label('loc_A38')

    ChrTalk(
        0x00FE,
        (
            '不知道为什么，\n',
            '店主被军队带走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我只追求自己的技术，\n',
            '只要有一个工作的环境就可以了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是店长不在果然很让人头痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABE(): pass

    label('loc_ABE')

    Jump('loc_E09')

    def _loc_AC1(): pass

    label('loc_AC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_BE5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B8C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '店主好像比以前\n',
            '更加冷静不下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于强盗入室这件事\n',
            '好像受了非常大的打击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我平时只管\n',
            '强化自己的工艺技术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要给我一个工作的地方，\n',
            '就没有什么可以担心的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE2')

    def _loc_B8C(): pass

    label('loc_B8C')

    ChrTalk(
        0x00FE,
        (
            '店主好像比以前\n',
            '更加冷静不下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于强盗入室这件事\n',
            '好像受了非常大的打击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE2(): pass

    label('loc_BE2')

    Jump('loc_E09')

    def _loc_BE5(): pass

    label('loc_BE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_C41',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，那些强盗们\n',
            '把大部分的商品都拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天应该是店主\n',
            '负责关店门的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E09')

    def _loc_C41(): pass

    label('loc_C41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_CD4',
    )

    ChrTalk(
        0x00FE,
        (
            '我不会做出\n',
            '歪曲自己审美意识的作品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新来的店主所要求的作品中\n',
            '品位低下的居多啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要看到他那张脸，\n',
            '我就没有创作欲望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E09')

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_D34',
    )

    ChrTalk(
        0x00FE,
        (
            '新的店主\n',
            '总是提出各种各样奇怪的要求……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前的店主\n',
            '却能给我自由创作的空间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E09')

    def _loc_D34(): pass

    label('loc_D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_DC9',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道什么时候\n',
            '尼冈德变成店主了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我平时只管\n',
            '强化自己的工艺技术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要给我一个工作的地方，\n',
            '谁当店主对我来说都没什么影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E09')

    def _loc_DC9(): pass

    label('loc_DC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_E09',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '最近店长都没来店里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是不是生病了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E09(): pass

    label('loc_E09')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0xE0D
@scena.Code('func_06_E0D')
def func_06_E0D():
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

    FadeIn(300, 0)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E6B',
    )

    OP_0D()
    OP_A9(0x0B)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_E6B(): pass

    label('loc_E6B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E7C',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_E7C(): pass

    label('loc_E7C')

    Call(0, 0x0007)
    SetChrDirection(0x000B, 180, 0)

    Return()

# id: 0x0007 offset: 0xE88
@scena.Code('func_07_E88')
def func_07_E88():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_F1C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '被空贼偷走的商品\n',
            '都被军队找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我终于能够静下心来\n',
            '好好做买卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F19')

    def _loc_EF0(): pass

    label('loc_EF0')

    ChrTalk(
        0x000B,
        (
            '希望军队能够\n',
            '好好教训一下那帮空贼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F19(): pass

    label('loc_F19')

    Jump('loc_145B')

    def _loc_F1C(): pass

    label('loc_F1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_FFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FAC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '还没有找到\n',
            '那些可恶的强盗犯吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不管如何，\n',
            '军队都一定要抓住犯人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '再这样下去的话，\n',
            '满肚子牢骚就发不完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FFA')

    def _loc_FAC(): pass

    label('loc_FAC')

    ChrTalk(
        0x000B,
        (
            '还没有找到\n',
            '那些可恶的强盗犯吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不管如何，\n',
            '军队都一定要抓住犯人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FFA(): pass

    label('loc_FFA')

    Jump('loc_145B')

    def _loc_FFD(): pass

    label('loc_FFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1113',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10BC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '可恶至极！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '我的店铺也被那些强盗洗劫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '值钱的商品都被\n',
            '拿得一点都不剩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这种时候本来就没什么东西好卖，\n',
            '我该怎么办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1110')

    def _loc_10BC(): pass

    label('loc_10BC')

    ChrTalk(
        0x000B,
        (
            '可恶至极！\n',
            '我的店铺也被那些强盗洗劫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '值钱的商品都被\n',
            '拿得一点都不剩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1110(): pass

    label('loc_1110')

    Jump('loc_145B')

    def _loc_1113(): pass

    label('loc_1113')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1219',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11B4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '在超市里开店的时候，\n',
            '我的工作可是辛苦得很啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我想正是有了那份辛苦与经验，\n',
            '我才有能力经营这家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '果然积累是最重要的一环啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1216')

    def _loc_11B4(): pass

    label('loc_11B4')

    ChrTalk(
        0x000B,
        (
            '正因为在超市里\n',
            '积攒了不少辛苦与经验，\n',
            '我才有能力经营这家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '果然积累是最重要的一环啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1216(): pass

    label('loc_1216')

    Jump('loc_145B')

    def _loc_1219(): pass

    label('loc_1219')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1337',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12DC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '柏斯的商人\n',
            '大多都是从超市起家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '一开始会得到市政府的援助，\n',
            '而且如果有在超市经营的经验，\n',
            '自己开店就会容易得到认可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '从很远的地方\n',
            '特意来到这里的商人也有不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1334')

    def _loc_12DC(): pass

    label('loc_12DC')

    ChrTalk(
        0x000B,
        (
            '一开始会得到市政府的援助，\n',
            '而且如果有在超市经营的经验，\n',
            '自己开店就会容易得到认可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1334(): pass

    label('loc_1334')

    Jump('loc_145B')

    def _loc_1337(): pass

    label('loc_1337')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_142A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13CB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '我年轻的时候\n',
            '也在柏斯超市拥有店铺呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '现在去超市的时候\n',
            '还是会感到很怀念。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '希望年轻人\n',
            '也能够努力干出一番事业来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1427')

    def _loc_13CB(): pass

    label('loc_13CB')

    ChrTalk(
        0x000B,
        (
            '我年轻的时候\n',
            '也在柏斯超市拥有店铺呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '希望现在的年轻人\n',
            '也能够努力干出一番事业来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1427(): pass

    label('loc_1427')

    Jump('loc_145B')

    def _loc_142A(): pass

    label('loc_142A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_145B',
    )

    ChrTalk(
        0x000B,
        (
            '噢，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你们慢慢挑选吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_145B(): pass

    label('loc_145B')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x145F
@scena.Code('func_08_145F')
def func_08_145F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1581',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1511',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我是来做买卖的，\n',
            '但不知道什么时候\n',
            '这家店的主人好像变了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我也只能和新的店主\n',
            '从头开始谈判了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我什么时候才能把\n',
            '好消息带回帝都去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_157E')

    def _loc_1511(): pass

    label('loc_1511')

    ChrTalk(
        0x00FE,
        (
            '我是来做买卖的，\n',
            '但不知道什么时候\n',
            '这家店的主人好像变了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我也只能和新的店主\n',
            '从头开始谈判了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_157E(): pass

    label('loc_157E')

    Jump('loc_1623')

    def _loc_1581(): pass

    label('loc_1581')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15E1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '和我做生意的那家店\n',
            '好像被强盗洗劫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的确不是谈论\n',
            '做买卖的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1623')

    def _loc_15E1(): pass

    label('loc_15E1')

    ChrTalk(
        0x00FE,
        (
            '话又说回来，\n',
            '现在连记者都赶到了，\n',
            '为什么早没人去通知游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1623(): pass

    label('loc_1623')

    TalkEnd(0x0008)

    Return()

# id: 0x0009 offset: 0x1627
@scena.Code('func_09_1627')
def func_09_1627():
    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '#0270030480V#141F多亏了你们提供的消息，\n',
            '这次的杂志篇幅将会非常大哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030481V如果再有什么新闻的话一定要告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x169E
@scena.Code('func_0A_169E')
def func_0A_169E():
    TalkBegin(0x000D)

    ChrTalk(
        0x000D,
        (
            '#0280030482V#150F听说这里展示的最新型相机\n',
            '也被空贼盗走了呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280030483V那些空贼，\n',
            '是不是对拍照很感兴趣呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x170E
@scena.Code('func_0B_170E')
def func_0B_170E():
    TalkBegin(0x000E)

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1869',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_180E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000E,
        (
            '尼冈德做的坏事\n',
            '终于被查出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我也重新成为了\n',
            '这家店的店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '真是不禁令人感叹啊。\n',
            '从此作为商人重新出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我以前确实太老实了，\n',
            '也说不定因此而让人看不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然不甘心，\n',
            '不过多亏了尼冈德让我认识了这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1866')

    def _loc_180E(): pass

    label('loc_180E')

    ChrTalk(
        0x000E,
        (
            '不过，\n',
            '尼冈德毕竟曾经与我共患难过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '找个时间去给他送饭，\n',
            '顺便看望一下他吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1866(): pass

    label('loc_1866')

    Jump('loc_18EE')

    def _loc_1869(): pass

    label('loc_1869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_18EE',
    )

    ChrTalk(
        0x000E,
        (
            '尼冈德那家伙\n',
            '被带到哈肯大门那里去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '没有办法， \n',
            '只好由我来暂时接管这个工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '那家伙好像\n',
            '干了相当坏的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18EE(): pass

    label('loc_18EE')

    TalkEnd(0x000E)

    Return()

# id: 0x000C offset: 0x18F2
@scena.Code('func_0C_18F2')
def func_0C_18F2():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_191C',
    )

    Sleep(500)

    Sleep(500)

    ChrWalkTo(0x00FE, -23790, 0, 91820, 3000, 0x00)

    def _loc_191C(): pass

    label('loc_191C')

    ChrWalkTo(0x00FE, -23010, 0, 89730, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000D, 400)

    Return()

# id: 0x000D offset: 0x1938
@scena.Code('func_0D_1938')
def func_0D_1938():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1967',
    )

    Sleep(500)

    Sleep(500)

    Sleep(500)

    ChrWalkTo(0x00FE, -23790, 0, 91820, 3000, 0x00)

    def _loc_1967(): pass

    label('loc_1967')

    ChrWalkTo(0x00FE, -22370, 0, 90460, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000C, 400)

    Return()

# id: 0x000E offset: 0x1983
@scena.Code('func_0E_1983')
def func_0E_1983():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A8',
    )

    Sleep(500)

    ChrWalkTo(0x00FE, -23790, 0, 91820, 3000, 0x00)

    def _loc_19A8(): pass

    label('loc_19A8')

    ChrWalkTo(0x00FE, -23990, 0, 89110, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000C, 400)

    Return()

# id: 0x000F offset: 0x19C4
@scena.Code('func_0F_19C4')
def func_0F_19C4():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19E4',
    )

    ChrWalkTo(0x00FE, -23790, 0, 91820, 3000, 0x00)

    def _loc_19E4(): pass

    label('loc_19E4')

    ChrWalkTo(0x00FE, -21410, 0, 89670, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000C, 400)

    Return()

# id: 0x0010 offset: 0x1A00
@scena.Code('func_10_1A00')
def func_10_1A00():
    EventBegin(0x00)
    CameraMove(-23490, 0, 87480, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    SetChrPos(0x000D, -24322, 0, 85809, 270)
    SetChrPos(0x000C, -21888, 0, 88170, 135)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AC6',
    )

    SetChrPos(0x0101, -28760, -2000, 92070, 180)
    SetChrPos(0x0102, -28760, -2000, 92070, 180)
    SetChrPos(0x0103, -28760, -2000, 92070, 180)
    SetChrPos(0x0104, -28760, -2000, 92070, 180)

    Jump('loc_1B0A')

    def _loc_1AC6(): pass

    label('loc_1AC6')

    SetChrPos(0x0101, -21890, 0, 91590, 180)
    SetChrPos(0x0102, -21160, 0, 92440, 180)
    SetChrPos(0x0103, -20430, 0, 91410, 180)
    SetChrPos(0x0104, -22770, 0, 92110, 180)

    def _loc_1B0A(): pass

    label('loc_1B0A')

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0280030349V#151F嘿嘿，照得挺可爱的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000C, 400)

    ChrTalk(
        0x000D,
        (
            '#0280030350V#150F奈尔前辈～\n',
            '照出这种感觉就可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000D, 400)

    ChrTalk(
        0x000C,
        (
            '#0270030351V#140F啊啊，我要的就是这种。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030352V#140F不过只能从里面挑选一张，\n',
            '抉择起来还真是很难啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030353V#142F………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C02')
    def lambda_1C02():
        SetChrDirection(0x000C, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1C02)

    @scena.Lambda('lambda_1C10')
    def lambda_1C10():
        CameraMove(-22600, 0, 89590, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C10)

    CreateThread(0x0101, 0x01, 0x00, 0x000C)
    CreateThread(0x0102, 0x01, 0x00, 0x000D)
    CreateThread(0x0103, 0x01, 0x00, 0x000F)
    CreateThread(0x0104, 0x01, 0x00, 0x000E)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0102,
        (
            '#0020030354V#010F#2P你们好。\n',
            '又要赶着去取材吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030355V#000F#1P你们也很辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030356V#141F哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280030357V#153F啊～！\n',
            '是小艾和小约呢～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000D, -22970, 0, 87400, 3000, 0x00)
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0280030358V#151F太好了，终于释放了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030359V#141F我们已经听说了。\n',
            '军队那些家伙在废坑把你们逮捕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030360V真是的～害我们担心死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030361V#007F#1P说得好像完全事不关己一样，\n',
            '你会担心才怪呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030362V不知道是谁给的情报，\n',
            '害我们在村子遇到那种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030363V#141F喂喂，怎么反过来怪我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030364V#010F#2P奈尔先生你们\n',
            '也去过拉文努村的废坑那里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280030365V#150F是的～就是昨天呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280030366V#150F就在小约你们\n',
            '被那些军人带走之后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030367V#142F要是我们也在逮捕现场的话，\n',
            '一定会给你们拍几张有趣的照片……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030368V#147F呵呵，拿来自己收藏也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030369V#009F哼，大叔你太过分了！\n',
            '亏你还是个专业的杂志记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030370V#020F对了，记者先生。 \n',
            '你认为昨天的盗窃案是空贼干的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030371V#140F啊啊，应该就是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030372V现在军队也在\n',
            '到处寻找案件的线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030373V不过暂时还没有头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030374V#026F哎呀，真的挺棘手啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030375V#030F记者先生，可以问你一下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030376V那些空贼，\n',
            '是从哪个方向进入城里的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0104, 400)

    ChrTalk(
        0x000C,
        (
            '#0270030377V#140F啊啊，根据目击者的口述，\n',
            '好像是从西门进来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030378V#030F是吗，那就奇怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030379V西门附近不就是\n',
            '市长官邸和柏斯超市吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030380V按道理，向这两个地方下手\n',
            '反而能得到更多好处才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030381V#143F这么说来，的确是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030382V#142F……对了，你是哪位？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030383V#035F呵呵，你要仔细听好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030384V奥利维尔·朗海姆……\n',
            '漂泊的诗人，天才演奏家就是本人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030385V你们应该听说过我的名字吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0280030386V#151F啊～在餐厅里偷喝了\n',
            '高级葡萄酒然后逃之夭夭的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280030387V能够认识你真是太荣幸了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030388V#031F哈哈，我都被你称赞得脸红了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030389V如果你们有需要的话，\n',
            '我可是非常乐意接受你们的采访哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0280030390V#151F呜哇～真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030391V#007F真是服了这两个人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030392V#019F从某种意义上说……\n',
            '他们也算是同一类型的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0270030393V#145F这丫头，不理睬一起干事的同伴，\n',
            '却偏对刚认识的人这么热情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030394V#021F呵呵，怎么吃起醋来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0037, 0x01, 0x0002)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
