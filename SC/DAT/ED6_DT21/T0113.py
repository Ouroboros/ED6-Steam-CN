import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0113   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0113.x'
    header.mapIndex       = 11
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
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拉欧老人',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亚尔丽 ',
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
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '胡里奥',
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '菲特 ',
            x                   = 37070,
            z                   = 0,
            y                   = 33560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '尤妮',
            x                   = 38800,
            z                   = 0,
            y                   = 30060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '芙莉莎',
            x                   = -4550,
            z                   = 0,
            y                   = 37480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '阿妮娅',
            x                   = 3140,
            z                   = 0,
            y                   = 32100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '加通老大',
            x                   = 3570,
            z                   = 0,
            y                   = 33000,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_241',
    )

    OP_4A(0x0008, 255)
    ChrSetPos(0x0008, -41180, 0, 38000, 270)
    ChrSetPos(0x000A, -41280, 0, 35500, 0)
    ChrSetPos(0x0009, -42700, 0, 37200, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0002)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetSubChip(0x0008, 6)

    def _loc_241(): pass

    label('loc_241')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_258',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0B_ACA)

    def _loc_258(): pass

    label('loc_258')

    Return()

# id: 0x0001 offset: 0x259
@scena.Code('func_01_259')
def func_01_259():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_267',
    )

    OP_6F(0x0002, 15)

    def _loc_267(): pass

    label('loc_267')

    Return()

# id: 0x0002 offset: 0x268
@scena.Code('func_02_268')
def func_02_268():
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
        'loc_28D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3CF')

    def _loc_28D(): pass

    label('loc_28D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A6',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3CF')

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BF',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3CF')

    def _loc_2BF(): pass

    label('loc_2BF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D8',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3CF')

    def _loc_2D8(): pass

    label('loc_2D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F1',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3CF')

    def _loc_2F1(): pass

    label('loc_2F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3CF')

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_323',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3CF')

    def _loc_323(): pass

    label('loc_323')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3CF')

    def _loc_33C(): pass

    label('loc_33C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_355',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3CF')

    def _loc_355(): pass

    label('loc_355')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3CF')

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_387',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3CF')

    def _loc_387(): pass

    label('loc_387')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A0',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3CF')

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3CF')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CF',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3CF(): pass

    label('loc_3CF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3CF')

    def _loc_3E4(): pass

    label('loc_3E4')

    Return()

# id: 0x0003 offset: 0x3E5
@scena.Code('func_03_3E5')
def func_03_3E5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_408',
    )

    OP_8D(0x00FE, -447, 33095, 4354, 30386, 4000)

    Jump('func_03_3E5')

    def _loc_408(): pass

    label('loc_408')

    Return()

# id: 0x0004 offset: 0x409
@scena.Code('func_04_409')
def func_04_409():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_418',
    )

    Call(0, 0x000C)

    Jump('loc_460')

    def _loc_418(): pass

    label('loc_418')

    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '那时的铃声……\n',
            '音色真的很美。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从未听过\n',
            '如此清澈的铃音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    def _loc_460(): pass

    label('loc_460')

    Return()

# id: 0x0005 offset: 0x461
@scena.Code('func_05_461')
def func_05_461():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_470',
    )

    Call(0, 0x000C)

    Jump('loc_4BB')

    def _loc_470(): pass

    label('loc_470')

    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '你们今天巡逻辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那如果想起什么的话\n',
            '我会和协会联络的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    def _loc_4BB(): pass

    label('loc_4BB')

    Return()

# id: 0x0006 offset: 0x4BC
@scena.Code('func_06_4BC')
def func_06_4BC():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_5BF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_528',
    )

    ChrTalk(
        0x00FE,
        (
            '总之在雾散之前\n',
            '我不会让尤妮离开家门半步的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为只有我\n',
            '这个父亲才能保护女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BF')

    def _loc_528(): pass

    label('loc_528')

    ChrTalk(
        0x00FE,
        (
            '听说有好几个人\n',
            '都沉睡不醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还不知道\n',
            '是不是和这场雾有关……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总、总之暂时不能\n',
            '让尤妮外出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能用这种办法\n',
            '来保护自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5BF(): pass

    label('loc_5BF')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x5C3
@scena.Code('func_07_5C3')
def func_07_5C3():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_6C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_63D',
    )

    ChrTalk(
        0x00FE,
        (
            '尤妮虽然也喜欢待在家里，\n',
            '不过完全不让出门我也不喜欢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天要和鲁克他们\n',
            '在外面尽情的玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C1')

    def _loc_63D(): pass

    label('loc_63D')

    ChrTalk(
        0x00FE,
        (
            '今天听了爸爸的话，\n',
            '一整天都待在家里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～不知道鲁克和帕特\n',
            '有没有在外面玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们真好啊……\n',
            '尤妮也想在外面玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_6C1(): pass

    label('loc_6C1')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x6C5
@scena.Code('func_08_6C5')
def func_08_6C5():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_930',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_739',
    )

    ChrTalk(
        0x000F,
        (
            '不巧，手上还有很多工作呢，\n',
            '明天也是一早就要开始工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '嗯，家里的事\n',
            '就拜托空之女神吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_930')

    def _loc_739(): pass

    label('loc_739')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 2, 0x1032)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_896',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '你是以前帮助过我们的\n',
            '游击士小姑娘吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，是玛鲁加矿山的老大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '多亏了你们，\n',
            '新矿脉的开采很顺利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '那时候魔兽跑出来了的洞穴\n',
            '最后用炸药堵上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F真、真…啊哈哈…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '反正过几天也要施工，\n',
            '就把它完全堵住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '但是，多亏这个\n',
            '现在的玛鲁加矿山景气多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0206, 2, 0x1032))

    Jump('loc_8D9')

    def _loc_896(): pass

    label('loc_896')

    ChrTalk(
        0x000F,
        (
            '哟，游击士小姑娘？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我们的玛鲁加矿山\n',
            '仍像以往一样地景气，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D9(): pass

    label('loc_8D9')

    ChrTalk(
        0x000F,
        (
            '所以我很忙啊，\n',
            '得过４、５天才能回家一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '而且很快又得上山，\n',
            '真是不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_930(): pass

    label('loc_930')

    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0x934
@scena.Code('func_09_934')
def func_09_934():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_A2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_9A0',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫明天又得\n',
            '一早去矿山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我不想让他去……\n',
            '但默默地送别也是妻子的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A2C')

    def _loc_9A0(): pass

    label('loc_9A0')

    ChrTalk(
        0x00FE,
        (
            '今天难得全家\n',
            '聚在一起吃晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城里虽是这种状况，\n',
            '我们家里却是很幸福的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽然我丈夫明天要工作，\n',
            '也算是一瞬间的幸福吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_A2C(): pass

    label('loc_A2C')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0xA30
@scena.Code('func_0A_A30')
def func_0A_A30():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_AC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_A86',
    )

    ChrTalk(
        0x00FE,
        (
            '阿妮娅喂爸爸吃了\n',
            '一口饭，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后爸爸很开心地\n',
            '说很好吃哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AC6')

    def _loc_A86(): pass

    label('loc_A86')

    ChrTalk(
        0x00FE,
        (
            '今天是三个人的晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，阿妮娅\n',
            '要喂爸爸吃饭～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_AC6(): pass

    label('loc_AC6')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0xACA
@scena.Code('func_0B_ACA')
def func_0B_ACA():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_4A(0x0008, 255)
    OP_6F(0x0002, 15)
    ChrSetPos(0x0008, -41180, 0, 38000, 270)
    ChrSetPos(0x000A, -41280, 0, 35500, 0)
    ChrSetPos(0x0009, -42700, 0, 37200, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0002)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetSubChip(0x0008, 6)
    CameraMove(-39410, 0, 35550, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    CameraMove(-41180, 0, 38910, 3000)
    OP_0D()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0134._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0xBBD
@scena.Code('func_0C_BBD')
def func_0C_BBD():
    EventBegin(0x00)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    Fade(1000)
    ChrSetPos(0x0101, -42370, 0, 34440, 0)
    ChrSetPos(0x0103, -41320, 0, 34290, 0)
    ChrSetPos(0x00F8, -42850, 0, 33200, 0)
    ChrSetPos(0x00F9, -41450, 0, 33100, 0)
    ChrSetDirection(0x000A, 180, 0)
    ChrSetDirection(0x0009, 180, 0)
    CameraMove(-41270, 0, 36170, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x000A,
        (
            '#3390281683V#5P哎呀，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281684V#5P艾丝蒂尔和……\n',
            '雪拉扎德小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281685V#020F#4P嗯，晚上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281686V#1015F#6P我们受市长先生的委托\n',
            '来调查此次的事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281687V拉欧爷爷的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281688V#5P嗯……还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281689V#5P看上去睡得很香，\n',
            '可怎么也叫不醒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281690V#5P是不是只能等到\n',
            '明天早上再说了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281691V#026F#4P嗯……\n',
            '现在可能这样比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281692V#022F那么，我们有几个问题想\n',
            '问一下，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281693V#5P嗯，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281694V#5P只要我们能回答的，\n',
            '请尽管问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281695V#020F#4P感谢你们的合作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281696V首先是拉欧爷爷是\n',
            '在何时何地昏倒的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281697V#5P时间……\n',
            '5点半左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281698V#5P地点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F48')
    def lambda_0F48():
        CameraMove(-42950, 0, 34680, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F48)

    ChrSetDirection(0x000A, 230, 400)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#3390281699V#5P是在那扇门朝外的那一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F99')
    def lambda_0F99():
        ChrSetDirection(0x00FE, 230, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F99)

    Sleep(50)

    @scena.Lambda('lambda_0FAC')
    def lambda_0FAC():
        ChrSetDirection(0x00FE, 230, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0FAC)

    Sleep(50)

    @scena.Lambda('lambda_0FBF')
    def lambda_0FBF():
        ChrSetDirection(0x00FE, 230, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0FBF)

    Sleep(50)

    @scena.Lambda('lambda_0FD2')
    def lambda_0FD2():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0FD2)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010281700V#1015F#5P门朝外的那一面……\n',
            '也就是在走廊里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281701V#5P嗯，一边敲门一边说\n',
            '『我回来了』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281702V#5P我打开门出去接他时\n',
            '我岳父就已经倒在地上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1099')
    def lambda_1099():
        CameraMove(-41270, 0, 36170, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1099)

    ChrSetDirection(0x000A, 180, 400)

    @scena.Lambda('lambda_10B8')
    def lambda_10B8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10B8)

    Sleep(50)

    @scena.Lambda('lambda_10CB')
    def lambda_10CB():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_10CB)

    Sleep(50)

    @scena.Lambda('lambda_10DE')
    def lambda_10DE():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_10DE)

    Sleep(50)

    @scena.Lambda('lambda_10F1')
    def lambda_10F1():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_10F1)

    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#3400281703V#5P我以为爸爸是因为去了\n',
            '酒馆而醉倒的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281704V#5P可他身上一点酒气也没有，\n',
            '今天看来是没喝过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281705V#5P但他还是不醒，\n',
            '实在是让人觉得古怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281706V#5P我就去找教区长先生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281707V#026F#4P是这样啊……\n',
            '大致状况我已经明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281529V#022F最后一个问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281709V在拉欧爷爷昏倒前\n',
            '有没有发生什么怪事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281710V#5P怪事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281711V#5P你是说这雾吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281712V#020F#4P不，这倒不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281713V比如见到陌生人或者\n',
            '听到怪异的声音？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#3390281714V#2P经你这么一说……\n',
            '我抬父亲进来的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000A, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#3400281715V#5P嗯……\n',
            '你也注意到了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281716V#5P那时候一阵慌乱，\n',
            '到现在才想起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281717V#1004F#6P请问……是什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)
    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#3390281718V#5P我正准备扶昏倒的\n',
            '岳父到床上时……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281719V#5P听到了微弱的铃声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1523',
    )

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
            TXT(0x00, '【◇没听到过铃声的说法（没从米蕾奴夫人那里听说）】\n'),
            TXT(0x01, '【◇听到过铃声的说法（已从米蕾奴夫人那里听说）】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1517'),
        (0x00000001, 'loc_151D'),
        (-1, 'loc_1523'),
    )

    def _loc_1517(): pass

    label('loc_1517')

    ClearScenaFlags(ScenaFlag(0x0302, 3, 0x1813))

    Jump('loc_1523')

    def _loc_151D(): pass

    label('loc_151D')

    SetScenaFlags(ScenaFlag(0x0302, 3, 0x1813))

    Jump('loc_1523')

    def _loc_1523(): pass

    label('loc_1523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_158A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030281537V#023F#4P铃声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281721V#1004F#6P难道是……\n',
            '我们也听到过的那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E9')

    def _loc_158A(): pass

    label('loc_158A')

    ChrTalk(
        0x0103,
        (
            '#0030281722V#022F#4P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281723V#1002F#6P在这里也能听到铃声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E9(): pass

    label('loc_15E9')

    ChrTalk(
        0x0009,
        (
            '#3400281724V#5P音色非常美啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281725V#5P大概是有人在\n',
            '外面摇响的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281726V#026F#4P……谢谢。\n',
            '你们给了我们很多参考。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281727V#020F要是还想起来什么的话\n',
            '请联系协会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3400281728V#5P嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281729V#1006F#6P那我们就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281730V明天我们还会来看看情况的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3390281731V#5P嗯……\n',
            '拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1753')
    def lambda_1753():
        ChrSetDirection(0x000A, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1753)

    ChrSetDirection(0x0009, 90, 400)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    SetScenaFlags(ScenaFlag(0x0302, 5, 0x1815))
    OP_28(0x0090, 0x02, 0x0080)
    OP_28(0x0090, 0x01, 0x0100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1795',
    )

    OP_28(0x0090, 0x01, 0x0200)

    Jump('loc_1795')

    def _loc_1795(): pass

    label('loc_1795')

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
