import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4255_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4255   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '茜亚'),
    TXT(0x02, '吉尔维厨师长'),
    TXT(0x03, '福卢克'),
    TXT(0x04, '里吉斯'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4255.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9D2
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -68800,
            z                   = 0,
            y                   = 73190,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -62700,
            z                   = 0,
            y                   = 67500,
            direction           = 258,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -71490,
            z                   = 0,
            y                   = 65550,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x15A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_184',
    )

    SetChrChipByIndex(0x0000, 0)
    SetChrChipByIndex(0x0001, 1)
    SetChrChipByIndex(0x0138, 2)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_184(): pass

    label('loc_184')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1C6',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -68800, 0, 72170, 273)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x0009, -61660, 0, 68120, 76)

    Jump('loc_20E')

    def _loc_1C6(): pass

    label('loc_1C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1D0',
    )

    Jump('loc_20E')

    def _loc_1D0(): pass

    label('loc_1D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1E9',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0009, 0x0080)

    Jump('loc_20E')

    def _loc_1E9(): pass

    label('loc_1E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1FD',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)

    Jump('loc_20E')

    def _loc_1FD(): pass

    label('loc_1FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_207',
    )

    Jump('loc_20E')

    def _loc_207(): pass

    label('loc_207')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_20E',
    )

    def _loc_20E(): pass

    label('loc_20E')

    Return()

# id: 0x0001 offset: 0x20F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_21F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_21F(): pass

    label('loc_21F')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x229
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_390')

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_267',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_390')

    def _loc_267(): pass

    label('loc_267')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_280',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_390')

    def _loc_280(): pass

    label('loc_280')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_299',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_390')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B2',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_390')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CB',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_390')

    def _loc_2CB(): pass

    label('loc_2CB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E4',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_390')

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_390')

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_316',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_390')

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_390')

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_348',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_390')

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_361',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_390')

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_390')

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_390',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_390')

    def _loc_3A5(): pass

    label('loc_3A5')

    Return()

# id: 0x0003 offset: 0x3A6
@scena.Code('func_03_3A6')
def func_03_3A6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_3B3',
    )

    Jump('loc_5C0')

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_411',
    )

    ChrTalk(
        0x00FE,
        (
            '不单是发动了政变，\n',
            '居然还把老鼠带来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙，太可耻了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A6')

    def _loc_411(): pass

    label('loc_411')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我知道老鼠是从哪儿来的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然是从宝物库的\n',
            '深处跑出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不单是发动了政变，\n',
            '居然还把老鼠带来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '情报部的家伙，太可耻了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A6(): pass

    label('loc_4A6')

    Jump('loc_5C0')

    def _loc_4A9(): pass

    label('loc_4A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_4B3',
    )

    Jump('loc_5C0')

    def _loc_4B3(): pass

    label('loc_4B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_4BD',
    )

    Jump('loc_5C0')

    def _loc_4BD(): pass

    label('loc_4BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_52D',
    )

    ChrTalk(
        0x00FE,
        (
            '为了不让老鼠糟蹋粮食，\n',
            '必须把食物小心保管起来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过话说回来，\n',
            '老鼠为何那么喜欢奶酪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C0')

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_5C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_56B',
    )

    ChrTalk(
        0x00FE,
        (
            '这些可恶的老鼠，\n',
            '到底是从哪里钻进来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C0')

    def _loc_56B(): pass

    label('loc_56B')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '感觉最近老鼠\n',
            '好像多了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于讨厌老鼠的我来说，\n',
            '这可是超紧急事态啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C0(): pass

    label('loc_5C0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x5C4
@scena.Code('func_04_5C4')
def func_04_5C4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_5D1',
    )

    Jump('loc_6AC')

    def _loc_5D1(): pass

    label('loc_5D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_61A',
    )

    ChrTalk(
        0x00FE,
        (
            '做蔬菜料理\n',
            '可是我的拿手戏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我是在洛连特长大的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AC')

    def _loc_61A(): pass

    label('loc_61A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_624',
    )

    Jump('loc_6AC')

    def _loc_624(): pass

    label('loc_624')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_62E',
    )

    Jump('loc_6AC')

    def _loc_62E(): pass

    label('loc_62E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_65B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '早点收拾好就可以回家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AC')

    def _loc_65B(): pass

    label('loc_65B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_6AC',
    )

    ChrTalk(
        0x00FE,
        (
            '厨师长不仅精于宫廷料理，\n',
            '而且据说他可以烹制出\n',
            '上千种各式风味的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6AC(): pass

    label('loc_6AC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x6B0
@scena.Code('func_05_6B0')
def func_05_6B0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_715',
    )

    ChrTalk(
        0x00FE,
        (
            '鸡骨头、洋葱、芹菜、\n',
            '胡萝卜、月桂叶还有香菜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在调制\n',
            '明天做饭用的底汤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_982')

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_761',
    )

    ChrTalk(
        0x00FE,
        (
            '陛下和公主好久没有\n',
            '像现在这样聚在一起了，\n',
            '我得大显身手才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_982')

    def _loc_761(): pass

    label('loc_761')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_76B',
    )

    Jump('loc_982')

    def _loc_76B(): pass

    label('loc_76B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_855',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7B2',
    )

    ChrTalk(
        0x00FE,
        (
            '最重要的是\n',
            '要给卧病在床的陛下\n',
            '多多补充营养啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_852')

    def _loc_7B2(): pass

    label('loc_7B2')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '稍后我想和您谈一下\n',
            '陛下的饮食方面的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#710F待会儿我会来找您谈的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等事情办完之后我就来，\n',
            '所以请您再等一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_852(): pass

    label('loc_852')

    Jump('loc_982')

    def _loc_855(): pass

    label('loc_855')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_890',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '料理的味道\n',
            '你们还满意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_982')

    def _loc_890(): pass

    label('loc_890')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_982',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 2, 0x63A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 3, 0x63B)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 4, 0x63C)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_91F',
    )

    ChrTalk(
        0x00FE,
        (
            '十分抱歉，客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在料理\n',
            '还没有准备完毕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '准备好了之后，\n',
            '会有侍者去叫你们的，\n',
            '请在房间稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_982')

    def _loc_91F(): pass

    label('loc_91F')

    ChrTalk(
        0x00FE,
        (
            '料理的准备工作\n',
            '马上就要做完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '准备好了之后，\n',
            '会有侍者去叫你们的，\n',
            '请在房间稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_982(): pass

    label('loc_982')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x986
@scena.Code('func_06_986')
def func_06_986():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '你在找约修亚先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像没有\n',
            '来过这边呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
