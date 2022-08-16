import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1230_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1230   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1230.x'
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
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿波尔',
            x                   = -730,
            z                   = 0,
            y                   = 5300,
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
            name                = '莉莫奈',
            x                   = 440,
            z                   = 0,
            y                   = 32439,
            direction           = 270,
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
            name                = '鲁伊',
            x                   = -3550,
            z                   = 0,
            y                   = 32400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '弗兰',
            x                   = -3550,
            z                   = 0,
            y                   = 31160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '贝斯卡',
            x                   = -940,
            z                   = 300,
            y                   = 34630,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '菲戈',
            x                   = -750,
            z                   = 0,
            y                   = 35490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -780,
            triggerZ            = 0,
            triggerY            = 4190,
            triggerRange        = 400,
            actorX              = -700,
            actorZ              = 1500,
            actorY              = 5300,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1500,
            triggerZ            = 0,
            triggerY            = 31600,
            triggerRange        = 400,
            actorX              = 440,
            actorZ              = 1500,
            actorY              = 32439,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1FB',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)

    Jump('loc_20C')

    def _loc_1FB(): pass

    label('loc_1FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_20C',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)

    def _loc_20C(): pass

    label('loc_20C')

    Return()

# id: 0x0001 offset: 0x20D
@scena.Code('func_01_20D')
def func_01_20D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_220',
    )

    OP_B1('T1230_n')

    Jump('loc_23C')

    def _loc_220(): pass

    label('loc_220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_233',
    )

    OP_B1('T1230_y')

    Jump('loc_23C')

    def _loc_233(): pass

    label('loc_233')

    OP_B1('T1230_n')

    def _loc_23C(): pass

    label('loc_23C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_24D(): pass

    label('loc_24D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_263',
    )

    OP_10(0x00, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x08, 0x01)
    OP_10(0x09, 0x01)

    Jump('loc_276')

    def _loc_263(): pass

    label('loc_263')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_276',
    )

    OP_10(0x00, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x06, 0x01)
    OP_10(0x07, 0x01)

    def _loc_276(): pass

    label('loc_276')

    Return()

# id: 0x0002 offset: 0x277
@scena.Code('func_02_277')
def func_02_277():
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
        'loc_29C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3DE')

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3DE')

    def _loc_2B5(): pass

    label('loc_2B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3DE')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E7',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3DE')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_300',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3DE')

    def _loc_300(): pass

    label('loc_300')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_319',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3DE')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_332',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3DE')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3DE')

    def _loc_34B(): pass

    label('loc_34B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_364',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3DE')

    def _loc_364(): pass

    label('loc_364')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3DE')

    def _loc_37D(): pass

    label('loc_37D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_396',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3DE')

    def _loc_396(): pass

    label('loc_396')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AF',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3DE')

    def _loc_3AF(): pass

    label('loc_3AF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C8',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3DE')

    def _loc_3C8(): pass

    label('loc_3C8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3DE')

    def _loc_3F3(): pass

    label('loc_3F3')

    Return()

# id: 0x0003 offset: 0x3F4
@scena.Code('func_03_3F4')
def func_03_3F4():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x3F9
@scena.Code('func_04_3F9')
def func_04_3F9():
    TalkBegin(0x0008)
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
            TXT(0x01, '休息\n'),
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
        'loc_455',
    )

    OP_0D()
    OP_A9(0x47)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_466',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_466(): pass

    label('loc_466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_547',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F8',
    )

    ChrTalk(
        0x0008,
        (
            '仔细想来，最近\n',
            '好像经常发生奇怪的事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '先是出现古龙，\n',
            '然后又有岛浮在天上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真希望\n',
            '以后别再发生任何事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_544')

    def _loc_4F8(): pass

    label('loc_4F8')

    ChrTalk(
        0x0008,
        (
            '我们只想在这村子里\n',
            '平静地生活下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真希望\n',
            '以后别再发生任何事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_544(): pass

    label('loc_544')

    Jump('loc_A07')

    def _loc_547(): pass

    label('loc_547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_64B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E1',
    )

    ChrTalk(
        0x0008,
        (
            '啊，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们村子里的导力器\n',
            '也全停了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，因为我待在这里\n',
            '完全没注意到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……刚才被莉莫奈\n',
            '嘲笑了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_648')

    def _loc_5E1(): pass

    label('loc_5E1')

    ChrTalk(
        0x0008,
        (
            '我们店里本来\n',
            '就是用油灯的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '右边的钟\n',
            '也是发条式的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就，就算没注意到\n',
            '也很正常不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_648(): pass

    label('loc_648')

    Jump('loc_A07')

    def _loc_64B(): pass

    label('loc_64B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_759',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6BC',
    )

    ChrTalk(
        0x0008,
        (
            '果树园的整理也结束了，\n',
            '总算恢复了平日的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '期待树苗结出果实，\n',
            '以后还要更加努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_756')

    def _loc_6BC(): pass

    label('loc_6BC')

    ChrTalk(
        0x0008,
        (
            '啊，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果树园的整理也结束了，\n',
            '总算恢复了平日的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总有一天新树苗\n',
            '会结果的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '衷心期待那天的到来，\n',
            '以后还要更加努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_756(): pass

    label('loc_756')

    Jump('loc_A07')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_833',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7B8',
    )

    ChrTalk(
        0x0008,
        (
            '果树园的人们\n',
            '一直讨论到深夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然知道会很辛苦，\n',
            '但希望他们加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_830')

    def _loc_7B8(): pass

    label('loc_7B8')

    ChrTalk(
        0x0008,
        (
            '果树园的人们\n',
            '一直讨论到深夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然知道会很辛苦，\n',
            '但希望他们加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们的店\n',
            '也要靠果树园才能维持啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_830(): pass

    label('loc_830')

    Jump('loc_A07')

    def _loc_833(): pass

    label('loc_833')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_925',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_89A',
    )

    ChrTalk(
        0x0008,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然我安慰莉莫奈\n',
            '让她打起精神来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但自己却无法轻松\n',
            '转换心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_922')

    def _loc_89A(): pass

    label('loc_89A')

    ChrTalk(
        0x0008,
        (
            '啊，欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然我安慰莉莫奈\n',
            '让她打起精神来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但自己却无法轻松\n',
            '转换心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唉，日复一日，\n',
            '都是叹息不已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_922(): pass

    label('loc_922')

    Jump('loc_A07')

    def _loc_925(): pass

    label('loc_925')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_A07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_98E',
    )

    ChrTalk(
        0x0008,
        (
            '好不容易结果了，\n',
            '却全部都被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '该怎么安慰才好呢，\n',
            '都找不到安慰的话了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A07')

    def _loc_98E(): pass

    label('loc_98E')

    ChrTalk(
        0x0008,
        (
            '火好像已经被扑灭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是，好不容易结果了，\n',
            '却全部都被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '变成这样，怎样\n',
            '安慰果园的人才好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_A07(): pass

    label('loc_A07')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xA0B
@scena.Code('func_05_A0B')
def func_05_A0B():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xA10
@scena.Code('func_06_A10')
def func_06_A10():
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
        'loc_A6E',
    )

    OP_0D()
    OP_A9(0x48)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_A6E(): pass

    label('loc_A6E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A7F',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_A7F(): pass

    label('loc_A7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_DC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 2, 0x2092)),
            Expr.Ez,
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BCA',
    )

    ChrTurnDirection(0x0009, 0x0106, 0)

    ChrTalk(
        0x0009,
        (
            '哎呀，这不是阿加特吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '难道有什么工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F不，不是工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只是来看看\n',
            '村子的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '导力器停了，\n',
            '大家正在发愁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '游击士能来巡视\n',
            '就让人安心多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然很辛苦，今后\n',
            '也请常来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只要到附近来的话\n',
            '就一定再来打扰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0412, 2, 0x2092))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_DC1')

    def _loc_BCA(): pass

    label('loc_BCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C1C',
    )

    ChrTalk(
        0x0009,
        (
            '游击士能来巡视\n',
            '就让人安心多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '从今以后也要\n',
            '也请常来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC1')

    def _loc_C1C(): pass

    label('loc_C1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_D34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CDB',
    )

    ChrTalk(
        0x0009,
        (
            '孩子们也来帮忙了，\n',
            '村里的生活还算好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过导力器停止的原因\n',
            '好像还不清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '王国军方\n',
            '要是有正式声明就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里离帝国很近，\n',
            '说实话真是很不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_D31')

    def _loc_CDB(): pass

    label('loc_CDB')

    ChrTalk(
        0x0009,
        (
            '不过导力器停止的原因\n',
            '好像还不清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里离帝国很近，\n',
            '说实话真是很不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D31(): pass

    label('loc_D31')

    Jump('loc_DC1')

    def _loc_D34(): pass

    label('loc_D34')

    ChrTalk(
        0x0009,
        (
            '哎呀，游击士们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '难道\n',
            '是来巡视的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '村子现在还算平静，\n',
            '不过不知道以后还会发生什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '从今以后也要\n',
            '也请常来露个面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DC1(): pass

    label('loc_DC1')

    Jump('loc_11B4')

    def _loc_DC4(): pass

    label('loc_DC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_E9E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E1C',
    )

    ChrTalk(
        0x0009,
        (
            '村长先生那里\n',
            '似乎收到了各处来的捐款。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是个让人振奋的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E9B')

    def _loc_E1C(): pass

    label('loc_E1C')

    ChrTalk(
        0x0009,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '村长先生那里\n',
            '似乎收到了各处来的捐款。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样果树园\n',
            '就能重建了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，真是个让人振奋的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_E9B(): pass

    label('loc_E9B')

    Jump('loc_11B4')

    def _loc_E9E(): pass

    label('loc_E9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1003',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 1, 0x1A49)),
            Expr.Return,
        ),
        'loc_EFF',
    )

    ChrTalk(
        0x0009,
        (
            '前阵子还受伤躺着，\n',
            '这么快就回来工作啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '游击士\n',
            '果然是辛苦的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1000')

    def _loc_EFF(): pass

    label('loc_EFF')

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就回来工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F啊啊，最近\n',
            '比较忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是吗，游击士\n',
            '果然辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，工作做完了\n',
            '再来我们这儿喝酒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请你喝我们\n',
            '引以为傲的水果酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#051F那我就期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0349, 1, 0x1A49))

    def _loc_1000(): pass

    label('loc_1000')

    Jump('loc_11B4')

    def _loc_1003(): pass

    label('loc_1003')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_10B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1056',
    )

    ChrTalk(
        0x0009,
        (
            '阿加特好像受伤\n',
            '被抬回家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我稍后\n',
            '也去看望他一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10B3')

    def _loc_1056(): pass

    label('loc_1056')

    ChrTalk(
        0x0009,
        (
            '阿加特好像受伤\n',
            '被抬回家里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像有个小女孩\n',
            '跟在他身边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……那是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_10B3(): pass

    label('loc_10B3')

    Jump('loc_11B4')

    def _loc_10B6(): pass

    label('loc_10B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_11B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1119',
    )

    ChrTalk(
        0x0009,
        (
            '大家努力的结晶\n',
            '瞬间就被摧毁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是太不甘心了，\n',
            '我连眼泪都流不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B4')

    def _loc_1119(): pass

    label('loc_1119')

    ChrTalk(
        0x0009,
        (
            '那个果树园是村里人共同\n',
            '管理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '无论刮风下雨\n',
            '大家都一起照顾的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '竟然瞬间\n',
            '就被完全摧毁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是太不甘心了，\n',
            '我连眼泪都流不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_11B4(): pass

    label('loc_11B4')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x11B8
@scena.Code('func_07_11B8')
def func_07_11B8():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 0, 0x1A48)),
            Expr.Return,
        ),
        'loc_13E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_12B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1228',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸他们\n',
            '昨天一直\n',
            '讨论到深夜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果园的事\n',
            '果然有很多问题要处理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B6')

    def _loc_1228(): pass

    label('loc_1228')

    ChrTalk(
        0x00FE,
        (
            '啊，姐姐\n',
            '和阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抓到龙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F不，现在\n',
            '正要去抓呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '是，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '加油哦！\n',
            '我会为你们加油的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_12B6(): pass

    label('loc_12B6')

    Jump('loc_13A9')

    def _loc_12B9(): pass

    label('loc_12B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_1370',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_130E',
    )

    ChrTalk(
        0x00FE,
        (
            '我听爸爸的话\n',
            '乖乖待在这里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸他们还在\n',
            '整理果树园呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136D')

    def _loc_130E(): pass

    label('loc_130E')

    ChrTalk(
        0x00FE,
        (
            '啊，是姐姐你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听爸爸的话\n',
            '乖乖待在这里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸他们还在\n',
            '整理果树园呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_136D(): pass

    label('loc_136D')

    Jump('loc_13A9')

    def _loc_1370(): pass

    label('loc_1370')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_13A9',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐你们也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙是很大很大的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13A9(): pass

    label('loc_13A9')

    Jump('loc_13DE')

    def _loc_13AC(): pass

    label('loc_13AC')

    ChrTalk(
        0x00FE,
        (
            '姐姐你们也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙是很大很大的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_13DE(): pass

    label('loc_13DE')

    Jump('loc_166F')

    def _loc_13E1(): pass

    label('loc_13E1')

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1473',
    )

    ChrTurnDirection(0x00FE, 0x0106, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '还有阿加特哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗨～鲁伊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哟，小鬼。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A6')

    def _loc_1473(): pass

    label('loc_1473')

    ChrTalk(
        0x0101,
        (
            '#1000F嗨～鲁伊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F太好了……\n',
            '你没事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A6(): pass

    label('loc_14A6')

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯，我没事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是……果园……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F真是的，马上就眼泪汪汪的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F没关系的，放心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '姐姐我们来了\n',
            '就不会再让龙乱来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真，真的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_15BE',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F真的真的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，向你保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F所以再忍耐一会儿，\n',
            '听爸爸的话\n',
            '乖乖的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1651')

    def _loc_15BE(): pass

    label('loc_15BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_160E',
    )

    ChrTalk(
        0x0101,
        (
            '#1012F真的真的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F所以在此之前，\n',
            '要听爸爸的话\n',
            '乖乖的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1651')

    def _loc_160E(): pass

    label('loc_160E')

    ChrTalk(
        0x0101,
        (
            '#1012F真的真的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F所以再忍耐一会儿，\n',
            '乖乖待在家里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1651(): pass

    label('loc_1651')

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯……知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0349, 0, 0x1A48))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    def _loc_166F(): pass

    label('loc_166F')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x1673
@scena.Code('func_08_1673')
def func_08_1673():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_16CC',
    )

    ChrTalk(
        0x00FE,
        (
            '贝斯卡和库赖\n',
            '重归于好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两个人都这么大了，\n',
            '差不多该妥协了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1832')

    def _loc_16CC(): pass

    label('loc_16CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_174E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1705',
    )

    ChrTalk(
        0x00FE,
        (
            '还不能出去吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，好无聊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174B')

    def _loc_1705(): pass

    label('loc_1705')

    ChrTalk(
        0x00FE,
        (
            '还不能出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，好无聊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让莉莫奈做点\n',
            '甜点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_174B(): pass

    label('loc_174B')

    Jump('loc_1832')

    def _loc_174E(): pass

    label('loc_174E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_1832',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_179B',
    )

    ChrTalk(
        0x00FE,
        (
            '龙有那么\n',
            '恐怖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '故事里面出现的\n',
            '好像都很善良……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1832')

    def _loc_179B(): pass

    label('loc_179B')

    ChrTalk(
        0x00FE,
        (
            '外面还很危险，\n',
            '不能出去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，龙有那么\n',
            '恐怖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '故事里面出现的\n',
            '好像都很善良……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定像鲁伊和巴德斯一样，\n',
            '龙也有不同性格吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1832(): pass

    label('loc_1832')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x1836
@scena.Code('func_09_1836')
def func_09_1836():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1931',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18E2',
    )

    ChrTalk(
        0x00FE,
        (
            '埃米尔那家伙在发牢骚，\n',
            '因为流通路线好像停了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有运输手段\n',
            '我们的水果也不能出货，\n',
            '日用品也很快就会短缺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这，这好象\n',
            '不太妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_192E')

    def _loc_18E2(): pass

    label('loc_18E2')

    ChrTalk(
        0x00FE,
        (
            '流通路线停了\n',
            '真的是个很严重的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，好像不该\n',
            '在这里喝酒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_192E(): pass

    label('loc_192E')

    Jump('loc_1A18')

    def _loc_1931(): pass

    label('loc_1931')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C9',
    )

    ChrTalk(
        0x00FE,
        (
            '树苗也栽种完了，\n',
            '终于能松一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算导力器停止了，\n',
            '村子的生活也没太大困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '煮饭用火炉就成，\n',
            '照明用油灯也足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_1A18')

    def _loc_19C9(): pass

    label('loc_19C9')

    ChrTalk(
        0x00FE,
        (
            '就算导力器停止了，\n',
            '村子的生活也没太大困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是住在乡下的好处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A18(): pass

    label('loc_1A18')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x1A1C
@scena.Code('func_0A_1A1C')
def func_0A_1A1C():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1B67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AFE',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船停止运航了吗……\n',
            '柏斯那边好像很严重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，定期船不行的话，\n',
            '也就是说飞行舰队也不能飞吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对住在王国境内的人来说，\n',
            '这可是大问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不好声张，\n',
            '但真担心帝国的动向呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_1B64')

    def _loc_1AFE(): pass

    label('loc_1AFE')

    ChrTalk(
        0x00FE,
        (
            '对住在王国境内的人来说，\n',
            '飞行舰队的问题可就大了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不好声张，\n',
            '但真担心帝国的动向呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B64(): pass

    label('loc_1B64')

    Jump('loc_1CDB')

    def _loc_1B67(): pass

    label('loc_1B67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C96',
    )

    ChrTalk(
        0x00FE,
        (
            '树苗也栽种完了，\n',
            '这下总算能安下心来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '松了口气……正想这样呢，\n',
            '但竟然又发生不得了的大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在超市做买卖的\n',
            '罗亚一家没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '记得那家伙和太太\n',
            '一起开一家五金店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器不能动的话，\n',
            '利贝尔最自豪的飞行舰队也白费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不好声张，\n',
            '真担心帝国的动向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_1CDB')

    def _loc_1C96(): pass

    label('loc_1C96')

    ChrTalk(
        0x00FE,
        (
            '柏斯那边应该很严重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真担心在超市做买卖的\n',
            '罗亚一家人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CDB(): pass

    label('loc_1CDB')

    TalkEnd(0x000D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
