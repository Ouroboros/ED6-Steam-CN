import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4215_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4215   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4215.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '茜亚',
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
            name                = '吉尔维厨师长',
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
            name                = '福卢克',
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
            name                = '里吉斯',
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

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x15A
@scena.Code('Init')
def Init():
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

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_184(): pass

    label('loc_184')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1C6',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -68800, 0, 72170, 273)
    CreateThread(0x0008, 0x00, 0x00, func_02_225)
    ChrSetPos(0x0009, -61660, 0, 68120, 76)

    Jump('loc_21A')

    def _loc_1C6(): pass

    label('loc_1C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1E1',
    )

    ChrSetPos(0x000B, -68420, 0, 78980, 0)

    Jump('loc_21A')

    def _loc_1E1(): pass

    label('loc_1E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1F5',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_21A')

    def _loc_1F5(): pass

    label('loc_1F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_209',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_21A')

    def _loc_209(): pass

    label('loc_209')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_213',
    )

    Jump('loc_21A')

    def _loc_213(): pass

    label('loc_213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_21A',
    )

    def _loc_21A(): pass

    label('loc_21A')

    Return()

# id: 0x0001 offset: 0x21B
@scena.Code('func_01_21B')
def func_01_21B():
    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x225
@scena.Code('func_02_225')
def func_02_225():
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
        'loc_24A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_38C')

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_263',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_38C')

    def _loc_263(): pass

    label('loc_263')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_38C')

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_295',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_38C')

    def _loc_295(): pass

    label('loc_295')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AE',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_38C')

    def _loc_2AE(): pass

    label('loc_2AE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C7',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_38C')

    def _loc_2C7(): pass

    label('loc_2C7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E0',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_38C')

    def _loc_2E0(): pass

    label('loc_2E0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_38C')

    def _loc_2F9(): pass

    label('loc_2F9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_312',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_38C')

    def _loc_312(): pass

    label('loc_312')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_38C')

    def _loc_32B(): pass

    label('loc_32B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_344',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_38C')

    def _loc_344(): pass

    label('loc_344')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35D',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_38C')

    def _loc_35D(): pass

    label('loc_35D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_376',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_38C')

    def _loc_376(): pass

    label('loc_376')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_38C')

    def _loc_3A1(): pass

    label('loc_3A1')

    Return()

# id: 0x0003 offset: 0x3A2
@scena.Code('func_03_3A2')
def func_03_3A2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_3AF',
    )

    Jump('loc_5BC')

    def _loc_3AF(): pass

    label('loc_3AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_40D',
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

    Jump('loc_4A2')

    def _loc_40D(): pass

    label('loc_40D')

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

    def _loc_4A2(): pass

    label('loc_4A2')

    Jump('loc_5BC')

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    Jump('loc_5BC')

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_4B9',
    )

    Jump('loc_5BC')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_529',
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

    Jump('loc_5BC')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_5BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_567',
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

    Jump('loc_5BC')

    def _loc_567(): pass

    label('loc_567')

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

    def _loc_5BC(): pass

    label('loc_5BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x5C0
@scena.Code('func_04_5C0')
def func_04_5C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_5CD',
    )

    Jump('loc_6A8')

    def _loc_5CD(): pass

    label('loc_5CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_616',
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

    Jump('loc_6A8')

    def _loc_616(): pass

    label('loc_616')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_620',
    )

    Jump('loc_6A8')

    def _loc_620(): pass

    label('loc_620')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_62A',
    )

    Jump('loc_6A8')

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_657',
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

    Jump('loc_6A8')

    def _loc_657(): pass

    label('loc_657')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_6A8',
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

    def _loc_6A8(): pass

    label('loc_6A8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x6AC
@scena.Code('func_05_6AC')
def func_05_6AC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_711',
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

    Jump('loc_97D')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_75D',
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

    Jump('loc_97D')

    def _loc_75D(): pass

    label('loc_75D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_767',
    )

    Jump('loc_97D')

    def _loc_767(): pass

    label('loc_767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_85E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7AE',
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

    Jump('loc_85B')

    def _loc_7AE(): pass

    label('loc_7AE')

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

    ChrTalk(
        0x0138,
        (
            '#0650860007V#710F待会儿我会来找您谈的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860008V等事情办完之后我就来，\n',
            '所以请您再等一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85B(): pass

    label('loc_85B')

    Jump('loc_97D')

    def _loc_85E(): pass

    label('loc_85E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_899',
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

    Jump('loc_97D')

    def _loc_899(): pass

    label('loc_899')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_97D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_907',
    )

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

    Jump('loc_97D')

    def _loc_907(): pass

    label('loc_907')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

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

    def _loc_97D(): pass

    label('loc_97D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x981
@scena.Code('func_06_981')
def func_06_981():
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
