import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0210   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '米蕾奴夫人'),
    TXT(0x02, '玲达'),
    TXT(0x03, '克劳斯市长'),
    TXT(0x04, '克劳斯市长'),
    TXT(0x05, '潘杜老人'),
    TXT(0x06, '红茶'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0210.x'
    header.mapIndex       = 12
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0210._SN', 'ED6_DT21/T0210_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x35CF
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
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH02353._CH', 'ED6_DT07/CH02353P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 5860,
            z                   = 0,
            y                   = 64489,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 500,
            z                   = 0,
            y                   = -1800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 6080,
            z                   = 0,
            y                   = -4640,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 5350,
            z                   = 200,
            y                   = -6560,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 3860,
            z                   = 0,
            y                   = -5520,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 200400,
            z                   = 500,
            y                   = 49090,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1D2',
    )

    SetChrPos(0x0009, 7070, 0, 64599, 0)
    SetChrPos(0x0008, 202000, 0, 1390, 82)

    def _loc_1D2(): pass

    label('loc_1D2')

    Jump('loc_2FD')

    def _loc_1D5(): pass

    label('loc_1D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1F0',
    )

    SetChrPos(0x0009, 6700, 0, 62710, 270)

    Jump('loc_2FD')

    def _loc_1F0(): pass

    label('loc_1F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_239',
    )

    SetChrPos(0x0008, 200400, 0, 48360, 90)
    ClearChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0009, 201800, 0, 49000, 270)
    OP_4A(0x0009, 255)
    ClearChrFlags(0x000D, 0x0080)
    SetChrSubChip(0x000D, 25)

    Jump('loc_2FD')

    def _loc_239(): pass

    label('loc_239')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_278',
    )

    SetChrPos(0x0008, 200400, 0, 48360, 90)
    ClearChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0009, 201800, 0, 49000, 270)
    OP_4A(0x0009, 255)

    Jump('loc_2FD')

    def _loc_278(): pass

    label('loc_278')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2BC',
    )

    SetChrPos(0x0008, 200400, 0, 48360, 90)
    ClearChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0009, 201800, 0, 49000, 270)
    OP_4A(0x0009, 255)
    SetChrFlags(0x000A, 0x0080)

    Jump('loc_2FD')

    def _loc_2BC(): pass

    label('loc_2BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0314, 1, 0x18A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D0',
    )

    SetChrFlags(0x0008, 0x0010)

    def _loc_2D0(): pass

    label('loc_2D0')

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0009, 6700, 0, 62710, 270)
    SetChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

    Jump('loc_2FD')

    def _loc_2F3(): pass

    label('loc_2F3')

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_30B',
    )

    OP_A3(0x10F0)
    Event(0, 0x0008)

    def _loc_30B(): pass

    label('loc_30B')

    Return()

# id: 0x0001 offset: 0x30C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_316',
    )

    Jump('loc_353')

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_327',
    )

    OP_6F(0x0005, 10)

    Jump('loc_353')

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_338',
    )

    OP_6F(0x0005, 10)

    Jump('loc_353')

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_349',
    )

    OP_6F(0x0005, 10)

    Jump('loc_353')

    def _loc_349(): pass

    label('loc_349')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_353',
    )

    Jump('loc_353')

    def _loc_353(): pass

    label('loc_353')

    Return()

# id: 0x0002 offset: 0x354
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
        'loc_379',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_4BB')

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_392',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_4BB')

    def _loc_392(): pass

    label('loc_392')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AB',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_4BB')

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C4',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_4BB')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_4BB')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F6',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_4BB')

    def _loc_3F6(): pass

    label('loc_3F6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_4BB')

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_428',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_4BB')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_441',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_4BB')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45A',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_4BB')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_473',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_4BB')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48C',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_4BB')

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A5',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_4BB')

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BB',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_4BB(): pass

    label('loc_4BB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4D0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_4BB')

    def _loc_4D0(): pass

    label('loc_4D0')

    Return()

# id: 0x0003 offset: 0x4D1
@scena.Code('func_03_4D1')
def func_03_4D1():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_5C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_568',
    )

    ChrTalk(
        0x00FE,
        (
            '导力炉不能用了，\n',
            '做饭真是很很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯。晚餐也变得很难处理，\n',
            '不知该做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，还是去找夫人\n',
            '商量商量看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_5C2')

    def _loc_568(): pass

    label('loc_568')

    ChrTalk(
        0x00FE,
        (
            '导力炉不能用了，\n',
            '做饭真是很很麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯。晚餐也变得很难处理，\n',
            '不知该做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C2(): pass

    label('loc_5C2')

    Jump('loc_A98')

    def _loc_5C5(): pass

    label('loc_5C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_681',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_60F',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔，\n',
            '还有雪拉小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_623')

    def _loc_60F(): pass

    label('loc_60F')

    ChrTalk(
        0x00FE,
        (
            '啊、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_623(): pass

    label('loc_623')

    ChrTalk(
        0x00FE,
        (
            '那个那个……起大雾那时多亏\n',
            '你们的照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经恢复健康了，\n',
            '要继续加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_6CD')

    def _loc_681(): pass

    label('loc_681')

    ChrTalk(
        0x00FE,
        (
            '起大雾那时多亏\n',
            '你们的照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经恢复健康了，\n',
            '要继续加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_6CD(): pass

    label('loc_6CD')

    Jump('loc_A98')

    def _loc_6D0(): pass

    label('loc_6D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_7FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_74C',
    )

    ChrTalk(
        0x00FE,
        (
            '昏睡的时候\n',
            '梦见了以前的事呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夫人泡了很香\n',
            '的茶给我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那美味的茶香\n',
            '让我想起了小时候的事情～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7FC')

    def _loc_74C(): pass

    label('loc_74C')

    ChrTalk(
        0x00FE,
        (
            '昏睡的时候\n',
            '梦见了以前的事呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有我刚见到主人和夫人\n',
            '时的事情…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夫人泡了很香\n',
            '的茶给我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那以来我一直\n',
            '就很喜欢那种茶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在梦中也好像\n',
            '能闻见香气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_7FC(): pass

    label('loc_7FC')

    Jump('loc_A98')

    def _loc_7FF(): pass

    label('loc_7FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_984',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_85E',
    )

    ChrTalk(
        0x00FE,
        (
            '整理完茶之后\n',
            '又要扫除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，不能忘了对客人\n',
            '微笑……嘿嘿☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0000)
    OP_A3(0x0001)

    Jump('loc_981')

    def _loc_85E(): pass

    label('loc_85E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8F1',
    )

    ChrTalk(
        0x00FE,
        (
            '夫人非常\n',
            '擅长泡茶呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她泡的茶可以\n',
            '香彻心肺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～能泡这么香，\n',
            '果然是有秘诀吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不行了。\n',
            '要早点把茶准备好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_981')

    def _loc_8F1(): pass

    label('loc_8F1')

    ChrTalk(
        0x00FE,
        (
            '呼，好忙好忙。\n',
            '今天的客人很多，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但要扫除，\n',
            '还要准备好茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又要扫除又要准备茶，\n',
            '然后还是扫除…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是来回来去做这些事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_981(): pass

    label('loc_981')

    Jump('loc_A98')

    def _loc_984(): pass

    label('loc_984')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_A98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9DB',
    )

    ChrTalk(
        0x00FE,
        (
            '主人和夫人现在\n',
            '还在格兰赛尔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在两个人正在王都\n',
            '旅行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A98')

    def _loc_9DB(): pass

    label('loc_9DB')

    ChrTalk(
        0x00FE,
        (
            '啊，你是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士\n',
            '艾丝蒂尔吧？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你回洛连特了啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……主人现在\n',
            '还在格兰赛尔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夫人在主人走之后\n',
            '也出发去格兰赛尔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～夫人没能\n',
            '见到艾丝蒂尔真遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A98(): pass

    label('loc_A98')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0xA9C
@scena.Code('func_04_A9C')
def func_04_A9C():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_B2C',
    )

    Jump('loc_B6E')

    def _loc_B2C(): pass

    label('loc_B2C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B48',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B6E')

    def _loc_B48(): pass

    label('loc_B48')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B64',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B6E')

    def _loc_B64(): pass

    label('loc_B64')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B6E(): pass

    label('loc_B6E')

    ExecExpressionWithValue(
        0x00FE,
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
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 1, 0x1881)),
            Expr.Return,
        ),
        'loc_C7A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C14',
    )

    ChrTalk(
        0x000B,
        (
            '#0340280944V#602F定期船停止航行了，\n',
            '真是非常时期啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280945V嗯，推迟前往王都的计划\n',
            '看来是正确的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C77')

    def _loc_C14(): pass

    label('loc_C14')

    ChrTalk(
        0x000B,
        (
            '#0340280946V#602F定期船停止航行了，\n',
            '真是非常时期啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280947V不好意思，\n',
            '请你们也帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C77(): pass

    label('loc_C77')

    Jump('loc_1432')

    def _loc_C7A(): pass

    label('loc_C7A')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0340280906V#601F噢噢，是艾丝蒂尔啊，\n',
            '雪拉小姐也在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280907V#1006F市长爷爷，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DAB',
    )

    ChrTalk(
        0x000B,
        (
            '#0340280908V#603F公主殿下……\n',
            '您还是很有朝气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280909V#048F是啊，托您的福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280910V#021F市长先生也是一样，\n',
            '看您这么健康我就安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DDF')

    def _loc_DAB(): pass

    label('loc_DAB')

    ChrTalk(
        0x0103,
        (
            '#0030280911V#021F看您还是这么\n',
            '健康我就安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DDF(): pass

    label('loc_DDF')

    ChrTalk(
        0x000B,
        (
            '#0340280912V#601F哈哈，你们两个这么争气，\n',
            '我这个当市长的也感到面上有光啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280913V#600F对了，今天\n',
            '为什么又回洛连特了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280914V有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280915V#1015F嗯……其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将因大雾而被迫停留在\n',
            '洛连特的事情告诉市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000B,
        (
            '#0340280916V#602F原来如此，你们\n',
            '也是这场雾的受害者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280917V嗯，推迟前往王都的计划\n',
            '似乎看来是对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280918V#1015F啊？去王都有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280919V#023F去王都，难道是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280920V互不侵犯条约的签字仪式吗？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010280921V#1004F啊啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280922V签、签字仪式！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0340280923V#603F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280924V我作为地区的代表，\n',
            '自然必须出席…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280925V但看现在这种雾…\n',
            '出发只能推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280926V#1007F说、说的对啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280927V呼，市长爷爷\n',
            '也遇到麻烦了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0340280928V#602F不管怎样，总之要暂时\n',
            '观望一下情况的发展了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280929V如果遇到什么情况的话，\n',
            '就和协会一起思考对策吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340280930V那样的话，\n',
            '也许又要拜托你们帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280931V#1006F嗯，当然没问题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_123F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280932V#050F啊，那是应该的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280933V再次来到这里也算\n',
            '是缘分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1379')

    def _loc_123F(): pass

    label('loc_123F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12A6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080280934V#070F嗯，一定帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280935V再次来到这里也算\n',
            '一定是女神的召唤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1379')

    def _loc_12A6(): pass

    label('loc_12A6')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1311',
    )

    ChrTalk(
        0x0104,
        (
            '#0040280936V#030F呼，交给我们好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280937V再次来到这里也算\n',
            '这也是一种缘分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1379')

    def _loc_1311(): pass

    label('loc_1311')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1379',
    )

    ChrTalk(
        0x0105,
        (
            '#0060280938V#040F是，我们一定会全力帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060280939V能来到这里\n',
            '也算是一种缘分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1379(): pass

    label('loc_1379')

    ChrTalk(
        0x000B,
        (
            '#0340280940V#603F那就先谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280941V#020F那么，有什么事情的话\n',
            '请随时和协会联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280942V爱娜会马上\n',
            '联络到我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0340280943V#600F嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1881)
    OP_A2(0x0002)
    def _loc_1432(): pass

    label('loc_1432')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x143B
@scena.Code('func_05_143B')
def func_05_143B():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_22D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 0, 0x20A8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C17',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0340350536V#601F哟，艾丝蒂尔啊。\n',
            '今天和约修亚一起来了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350537V上次的大雾事件\n',
            '多谢你的帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350538V#1008F您太客气了，市长爷爷。\n',
            '没做什么的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350539V#1044F大雾事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350540V#1043F是吗……\n',
            '果然是结社的『实验』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340350541V#602F不过现在的事态\n',
            '比之前更加严重得多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350542V很可能已经覆盖到了\n',
            '整个王国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350543V#1026F啊……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350544V#1035F是啊，整个利贝尔\n',
            '王国都陷入了导力器瘫痪状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16D0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350545V#522F这样一来，各种运输\n',
            '通道也全部瘫痪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350546V再这么下去的话，市民\n',
            '的生活会受到很严重的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_17F7')

    def _loc_16D0(): pass

    label('loc_16D0')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1763',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350547V#050F这样一来，各种运输\n',
            '方式也全部瘫痪了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350548V再这样下去的话，市民\n',
            '的生活会受到很严重的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_17F7')

    def _loc_1763(): pass

    label('loc_1763')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17F7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350549V#072F各种运输方式\n',
            '也全都瘫痪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350550V这种状态如果不赶快解决的话，\n',
            '市民们的生活会受到很严重的影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0108, 400)

    def _loc_17F7(): pass

    label('loc_17F7')

    ChrTalk(
        0x000A,
        (
            '#0340350551V#603F原来如此……\n',
            '比想象中的还要严重啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350552V看来必须要\n',
            '赶快思考对策了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350553V#1015F不过，在这种非常时期，\n',
            '洛连特城里却很宁静呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350554V简直看不出来和\n',
            '平时有什么区别…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350555V#1040F的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350556V和柏斯等城市\n',
            '比有些不同呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '#0340350557V#600F嗯，洛连特对\n',
            '导力器的依赖不是太严重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350558V这里的主要导力装置\n',
            '也就是钟楼的时钟了…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350559V#601F而且，洛连特的市民\n',
            '本来就很悠闲懒散。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350560V所以即使是面对这种处境，\n',
            '也一样能悠然应对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A38',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350561V#021F呵呵，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA1')

    def _loc_1A38(): pass

    label('loc_1A38')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A6E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350562V#051F嗯，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA1')

    def _loc_1A6E(): pass

    label('loc_1A6E')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AA1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350563V#070F嗯，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA1(): pass

    label('loc_1AA1')

    ChrTalk(
        0x0101,
        (
            '#0010350564V#1007F嗯、嗯……不愧是乡村城镇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0340350565V#600F不管怎么说，在遇到困难时\n',
            '大家要互相帮助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350566V我也要准备一下对\n',
            '其它地区的支援工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350567V#1040F……那可太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350568V#1006F如果需要协会帮忙的话，\n',
            '请随时和支部联络哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340350569V#600F嗯，我会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350570V那么，各位。\n',
            '我期待你们再次活跃啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x20A8)

    Jump('loc_22D1')

    def _loc_1C17(): pass

    label('loc_1C17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_20AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1E76',
    )

    ChrTalk(
        0x000A,
        (
            '#0340350571V#600F对了、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350572V听说玛鲁加矿山的事情\n',
            '已经解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350573V#1000F啊、您已经知道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350574V#1040F虽然过程很危险，\n',
            '不过总算是把矿工们都安全救出了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350575V真是千钧一发啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340350576V#600F嗯，在这种状况下\n',
            '难免会发生意外。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350577V也许以后还会在别处\n',
            '出现这种事件呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350578V抱歉，暂时请继续\n',
            '保持警备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350579V#1000F嗯，了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DFC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350580V#020F嗯，会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6D')

    def _loc_1DFC(): pass

    label('loc_1DFC')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E36',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350581V#050F啊，我们会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6D')

    def _loc_1E36(): pass

    label('loc_1E36')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E6D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350582V#070F嗯，一定会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E6D(): pass

    label('loc_1E6D')

    OP_A3(0x0003)
    OP_A2(0x0002)

    Jump('loc_20AC')

    def _loc_1E76(): pass

    label('loc_1E76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2012',
    )

    ChrTalk(
        0x000A,
        (
            '#0340350583V#600F听说你们已经\n',
            '把矿山的危机解决了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350584V这也是因异变而引起\n',
            '的灾难之一吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350577V也许以后还会在别处\n',
            '出现这种事件呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350578V抱歉，暂时请继续\n',
            '保持警备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350579V#1000F嗯，了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F9B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350580V#020F嗯，会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_200C')

    def _loc_1F9B(): pass

    label('loc_1F9B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FD5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350581V#050F啊，我们会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_200C')

    def _loc_1FD5(): pass

    label('loc_1FD5')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_200C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350582V#070F嗯，一定会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_200C(): pass

    label('loc_200C')

    OP_A2(0x0002)

    Jump('loc_20AC')

    def _loc_2012(): pass

    label('loc_2012')

    ChrTalk(
        0x000A,
        (
            '#0340350591V#600F矿山事件也是因异变而引起\n',
            '的灾难之一吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350577V也许以后还会在别处\n',
            '出现这种事件呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350578V抱歉，暂时请继续\n',
            '保持警备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_20AC(): pass

    label('loc_20AC')

    Jump('loc_22D1')

    def _loc_20AF(): pass

    label('loc_20AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2147',
    )

    ChrTalk(
        0x000A,
        (
            '#0340350594V#600F比起其他城市，\n',
            '洛连特对导力器的依赖性较低。\n',
            '市民们的性情也比较懒散。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350595V所以在这种时候\n',
            '也会表现得比较平静吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22D1')

    def _loc_2147(): pass

    label('loc_2147')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2253',
    )

    ChrTalk(
        0x000A,
        (
            '#0340350596V#603F流通渠道出问题的话，\n',
            '确保生活必需品就成了大问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350597V所幸洛连特的\n',
            '近郊有很多农田。\n',
            '粮食的供给倒是没有问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350598V#602F但柏斯、蔡斯\n',
            '还有王都格兰赛尔\n',
            '可就不是这样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350599V我们也要想想怎么才能支援\n',
            '邻近地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_22D1')

    def _loc_2253(): pass

    label('loc_2253')

    ChrTalk(
        0x000A,
        (
            '#0340350600V#602F流通渠道出问题的话，\n',
            '确保生活必需品就成了大问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340350601V我们也要想想办法\n',
            '怎么才能支援\n',
            '邻近地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22D1(): pass

    label('loc_22D1')

    Jump('loc_29A1')

    def _loc_22D4(): pass

    label('loc_22D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_26C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 3, 0x1A63)),
            Expr.Return,
        ),
        'loc_2356',
    )

    ChrTalk(
        0x000A,
        (
            '#0340300118V#600F看样子你们要继续前往下个地区了啊，\n',
            '路上要小心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340300119V你们的敌人可不是\n',
            '寻常之辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26C6')

    def _loc_2356(): pass

    label('loc_2356')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0340300120V#600F是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340300121V事情的经过我\n',
            '已经听爱娜说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340300122V调查中的事情还有很多，\n',
            '一时也没办法全部问清…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340300123V#603F……嗯，看来想不通\n',
            '的事情还有很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300124V#1007F想不通的事件\n',
            '我们也遇到过很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300125V现在也只能尽力\n',
            '解决各地发生的事件了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300126V#1006F只要努力下去的话，\n',
            '总会找到解决根本问题的方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340300127V#602F嗯，我准备将事件的真相\n',
            '对市民们隐瞒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340300128V昏睡事件已经解决，\n',
            '所以没必要再增加市民们的不安情绪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030300129V#020F……是吗，那最好不过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300130V说出来的话也只能\n',
            '引发骚乱而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340300131V#600F你们似乎要继续前往下个地区了啊。\n',
            '路上要小心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340300119V你们的敌人可不是\n',
            '寻常之辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300133V#1002F嗯！早已有心理准备了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300134V#1000F那么，市长爷爷也要保重！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340300135V#601F嗯，我会平平安安得等你们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A63)

    def _loc_26C6(): pass

    label('loc_26C6')

    Jump('loc_29A1')

    def _loc_26C9(): pass

    label('loc_26C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2849',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2770',
    )

    ChrTalk(
        0x000A,
        (
            '#0340290518V#600F市民的避难引导工作\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290519V矿工们的家人\n',
            '也安心了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290517V不好意思，今后也许还会\n',
            '需要你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2846')

    def _loc_2770(): pass

    label('loc_2770')

    ChrTalk(
        0x000A,
        (
            '#0340290514V#600F在阿斯顿队长的指挥下，\n',
            '士兵们秩序井然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290515V这样的话，引导避难的工作\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290516V矿工们的家人\n',
            '也算是放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290517V不好意思，今后也许还会\n',
            '需要你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2846(): pass

    label('loc_2846')

    Jump('loc_29A1')

    def _loc_2849(): pass

    label('loc_2849')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_29A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_28C9',
    )

    ChrTalk(
        0x000A,
        (
            '#0340290512V#600F刚才阿斯顿队长\n',
            '来打过招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290513V指挥官是出身于我们地区的人，\n',
            '实在是令人安心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29A1')

    def _loc_28C9(): pass

    label('loc_28C9')

    ChrTalk(
        0x000A,
        (
            '#0340290508V#600F刚才阿斯顿队长\n',
            '来打过招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290509V指挥官是出身于我们地区的人，\n',
            '实在是令人安心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290510V不但对这里的地理很熟悉，\n',
            '而且和市民们也都认识。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340290511V简直就像卡西乌斯\n',
            '来了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_29A1(): pass

    label('loc_29A1')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x29A5
@scena.Code('func_06_29A5')
def func_06_29A5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_29BD',
    )

    SetChrFlags(0x00FE, 0x0010)

    def _loc_29BD(): pass

    label('loc_29BD')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2AB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A58',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听老公说过了，\n',
            '矿山好像出事了是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在这里\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也请继续\n',
            '帮助我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_2AAE')

    def _loc_2A58(): pass

    label('loc_2A58')

    ChrTalk(
        0x00FE,
        (
            '矿山事件\n',
            '似乎也是因为这次异变的影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些讨厌的事件也许\n',
            '还会不断发生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AAE(): pass

    label('loc_2AAE')

    Jump('loc_33D4')

    def _loc_2AB1(): pass

    label('loc_2AB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2CCF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C72',
    )

    ChrTalk(
        0x0101,
        (
            '#1001F您好，米蕾奴阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，这不是艾丝蒂尔\n',
            '和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上一次一起来我家玩，\n',
            '好像都是很久以前的事了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是啊……\n',
            '调查强盗事件以后就再没来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#1004F啊，有那么久了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F嗯，好像都是\n',
            '很久之前的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '呵呵，你们已经\n',
            '成熟了不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然工作那么辛苦，\n',
            '不过难得两个人一起返乡，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时间的话\n',
            '就多休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_2CCC')

    def _loc_2C72(): pass

    label('loc_2C72')

    ChrTalk(
        0x00FE,
        (
            '大雾散去，刚松了一口气，\n',
            '导力器就瘫痪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，利贝尔王国最近\n',
            '还真是多灾多难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CCC(): pass

    label('loc_2CCC')

    Jump('loc_33D4')

    def _loc_2CCF(): pass

    label('loc_2CCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2EC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 4, 0x1A64)),
            Expr.Return,
        ),
        'loc_2DA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2D41',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然曾经吃过，\n',
            '但制作方法就不知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '详细的制作方法最好\n',
            '还是去问上年纪的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DA4')

    def _loc_2D41(): pass

    label('loc_2D41')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D6C',
    )

    Call(1, 0x0000)

    Jump('loc_2DA4')

    def _loc_2D6C(): pass

    label('loc_2D6C')

    ChrTalk(
        0x00FE,
        (
            '难得有空\n',
            '回洛连特啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我给你们\n',
            '准备了些茶点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DA4(): pass

    label('loc_2DA4')

    Jump('loc_2EC1')

    def _loc_2DA7(): pass

    label('loc_2DA7')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '大家辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听先生说过了，\n',
            '事件好像顺利解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的玲达也\n',
            '醒过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这都多亏了艾丝蒂尔和大家\n',
            '的帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿，没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哪里，身为游击士，\n',
            '这也是我们的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '难得有空\n',
            '回到洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我给你们\n',
            '准备了些茶点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A64)
    def _loc_2EC1(): pass

    label('loc_2EC1')

    Jump('loc_33D4')

    def _loc_2EC4(): pass

    label('loc_2EC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2F91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2F0E',
    )

    ChrTalk(
        0x00FE,
        (
            '玲达，我给你泡了你最喜欢的\n',
            '柠檬茶哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很香吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F8E')

    def _loc_2F0E(): pass

    label('loc_2F0E')

    ChrTalk(
        0x00FE,
        (
            '之前就有感觉要\n',
            '发生什么事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我泡了玲达\n',
            '最喜欢的柠檬茶哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我也知道\n',
            '没有效果…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但也不能什么也不做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2F8E(): pass

    label('loc_2F8E')

    Jump('loc_33D4')

    def _loc_2F91(): pass

    label('loc_2F91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            Expr.Return,
        ),
        'loc_3074',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2FE8',
    )

    ChrTalk(
        0x00FE,
        (
            '阿斯顿的儿子\n',
            '好像也醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '执行这种任务…\n',
            '还真是难为他了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3071')

    def _loc_2FE8(): pass

    label('loc_2FE8')

    ChrTalk(
        0x00FE,
        (
            '刚才阿斯顿先生\n',
            '来打过招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁克\n',
            '好像也醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还只是个小孩子，\n',
            '竟然会遇到这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿斯顿先生\n',
            '还真是难为他了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_3071(): pass

    label('loc_3071')

    Jump('loc_33D4')

    def _loc_3074(): pass

    label('loc_3074')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_319B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_30E9',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然想她早上就会自然醒，\n',
            '但现实可没有那么美好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调查的事加油吧，\n',
            '现在的希望全在你们身上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3198')

    def _loc_30E9(): pass

    label('loc_30E9')

    ChrTalk(
        0x00FE,
        (
            '虽然幻想玲达\n',
            '到早上就会醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但果然是自欺欺人啊。\n',
            '现实毕竟没有那么美好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玲达让我来\n',
            '照看就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '调查的事情就拜托各位了。\n',
            '现在的希望全在你们身上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_3198(): pass

    label('loc_3198')

    Jump('loc_33D4')

    def _loc_319B(): pass

    label('loc_319B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_33D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3208',
    )

    ChrTalk(
        0x00FE,
        (
            '外边的雾很大，\n',
            '请一定小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也从来没见过这种\n',
            '怪天气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得心中很不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D4')

    def _loc_3208(): pass

    label('loc_3208')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0314, 1, 0x18A1)),
            Expr.Return,
        ),
        'loc_3291',
    )

    ChrTalk(
        0x00FE,
        (
            '我也从来没见过这种\n',
            '怪天气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市民们似乎也很不安，\n',
            '今天一大早就来了好多客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果只是普通的自然现象\n',
            '就最好了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D4')

    def _loc_3291(): pass

    label('loc_3291')

    ChrTalk(
        0x0101,
        (
            '#1000F米蕾奴阿姨，你好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，这不是艾丝蒂尔\n',
            '和雪拉扎德吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是好久不见了。\n',
            '在工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，正在街道巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊…\n',
            '请小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城里最近不大正常，\n',
            '外边的雾一定也很厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也从来没见过这种\n',
            '怪天气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得心中很不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x00FE, 0x0010)
    OP_A2(0x18A1)
    OP_A2(0x0004)

    def _loc_33D4(): pass

    label('loc_33D4')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x33D8
@scena.Code('func_07_33D8')
def func_07_33D8():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_349A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_342C',
    )

    ChrTalk(
        0x00FE,
        (
            '钟楼的事和市长\n',
            '说过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，既然说完了，\n',
            '也该回去啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_349A')

    def _loc_342C(): pass

    label('loc_342C')

    ChrTalk(
        0x00FE,
        (
            '今日的雾也许会让钟楼\n',
            '的零件生锈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为此我马上来和市长\n',
            '商量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼，\n',
            '有事一定要早点说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_349A(): pass

    label('loc_349A')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x349E
@scena.Code('func_08_349E')
def func_08_349E():
    EventBegin(0x00)
    SetMapFlags(0x02000000)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_4A(0x0009, 255)
    OP_6F(0x0005, 10)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0009, 201800, 0, 49000, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 200400, 0, 48360, 90)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0008, 200280, 0, 48270, 60)
    ClearChrFlags(0x0008, 0x0080)
    OP_6D(199670, 0, 45910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_355E')
    def lambda_355E():
        OP_6D(201780, 0, 48770, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_355E)

    FadeIn(1000, 0)
    Sleep(3000)

    SetChrSubChip(0x0009, 1)
    Sleep(300)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0110._SN', 106, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
