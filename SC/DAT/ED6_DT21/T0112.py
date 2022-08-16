import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0112_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0112   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0112.x'
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
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '鲁克',
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
            name                = '玛茜婆婆',
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
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '帕特',
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
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '雷特拉',
            x                   = 93320,
            z                   = 0,
            y                   = 162900,
            direction           = 0,
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
            name                = '赛拉',
            x                   = 88100,
            z                   = 0,
            y                   = 162410,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x172
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1D3',
    )

    OP_4A(0x0008, 255)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 55200, 100, 159950, 180)
    ChrSetPos(0x0009, 55120, 0, 161430, 180)
    ChrSetPos(0x000A, 56170, 0, 161420, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetSubChip(0x0008, 4)

    def _loc_1D3(): pass

    label('loc_1D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1EA',
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
    Event(0, func_07_696)

    def _loc_1EA(): pass

    label('loc_1EA')

    Return()

# id: 0x0001 offset: 0x1EB
@scena.Code('func_01_1EB')
def func_01_1EB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1F9',
    )

    OP_6F(0x0002, 15)

    def _loc_1F9(): pass

    label('loc_1F9')

    Return()

# id: 0x0002 offset: 0x1FA
@scena.Code('func_02_1FA')
def func_02_1FA():
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
        'loc_21F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_361')

    def _loc_21F(): pass

    label('loc_21F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_238',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_361')

    def _loc_238(): pass

    label('loc_238')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_251',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_361')

    def _loc_251(): pass

    label('loc_251')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_361')

    def _loc_26A(): pass

    label('loc_26A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_283',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_361')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_361')

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_361')

    def _loc_2B5(): pass

    label('loc_2B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_361')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_361')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_300',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_361')

    def _loc_300(): pass

    label('loc_300')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_319',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_361')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_332',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_361')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_361')

    def _loc_34B(): pass

    label('loc_34B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_361',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_376',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_361')

    def _loc_376(): pass

    label('loc_376')

    Return()

# id: 0x0003 offset: 0x377
@scena.Code('func_03_377')
def func_03_377():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_386',
    )

    Call(0, 0x0008)

    Jump('loc_464')

    def _loc_386(): pass

    label('loc_386')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3E7',
    )

    ChrTalk(
        0x00FE,
        (
            '这孩子是个精力用不完的\n',
            '淘气小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没事的，到明早一定会\n',
            '像平时一样醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_461')

    def _loc_3E7(): pass

    label('loc_3E7')

    ChrTalk(
        0x00FE,
        (
            '这孩子是个精力用不完的\n',
            '淘气小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没事的，到明早一定会\n',
            '像平时一样醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又会不吃早饭\n',
            '就飞跑出去的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_461(): pass

    label('loc_461')

    TalkEnd(0x0009)

    def _loc_464(): pass

    label('loc_464')

    Return()

# id: 0x0004 offset: 0x465
@scena.Code('func_04_465')
def func_04_465():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_474',
    )

    Call(0, 0x0008)

    Jump('loc_4BA')

    def _loc_474(): pass

    label('loc_474')

    TalkBegin(0x000A)

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔姐姐…\n',
            '我不会再哭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为我不想让鲁克\n',
            '看见我哭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    def _loc_4BA(): pass

    label('loc_4BA')

    Return()

# id: 0x0005 offset: 0x4BB
@scena.Code('func_05_4BB')
def func_05_4BB():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_5AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_52C',
    )

    ChrTalk(
        0x00FE,
        (
            '隔壁的鲁克\n',
            '突然昏倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家帕特也担心得\n',
            '跑去看他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他别受\n',
            '什么打击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AF')

    def _loc_52C(): pass

    label('loc_52C')

    ChrTalk(
        0x00FE,
        (
            '隔壁的鲁克\n',
            '突然昏倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '苏醒药也不起作用，\n',
            '真让人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁克是我家帕特的\n',
            '好朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他别受\n',
            '什么打击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_5AF(): pass

    label('loc_5AF')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x5B3
@scena.Code('func_06_5B3')
def func_06_5B3():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_692',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_605',
    )

    ChrTalk(
        0x00FE,
        (
            '帕特不肯\n',
            '离开鲁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，我只能拜托\n',
            '玛茜婆婆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_692')

    def _loc_605(): pass

    label('loc_605')

    ChrTalk(
        0x00FE,
        (
            '帕特去了隔壁的\n',
            '阿斯顿家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他怎么也不肯\n',
            '离开鲁克……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，我只能拜托\n',
            '玛茜婆婆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想今天再稍微\n',
            '让他在那边待会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_692(): pass

    label('loc_692')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x696
@scena.Code('func_07_696')
def func_07_696():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_4A(0x0008, 255)
    OP_6F(0x0002, 15)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 55200, 100, 159950, 180)
    ChrSetPos(0x0009, 55120, 0, 161430, 180)
    ChrSetPos(0x000A, 56170, 0, 161420, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetSubChip(0x0008, 4)
    CameraMove(52310, 0, 164340, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    CameraMove(54780, 0, 161440, 3000)
    OP_0D()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0113._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x793
@scena.Code('func_08_793')
def func_08_793():
    EventBegin(0x00)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    Fade(1000)
    ChrSetPos(0x0101, 56220, 0, 162560, 180)
    ChrSetPos(0x0103, 55060, 0, 162840, 180)
    ChrSetPos(0x00F8, 55900, 0, 164050, 180)
    ChrSetPos(0x00F9, 54700, 0, 164240, 180)
    ChrSetDirection(0x0009, 0, 0)
    ChrSetDirection(0x000A, 0, 0)
    CameraMove(55170, 0, 162450, 0)
    OP_67(0, 5530, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8D1',
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
            TXT(0x00, '【◇鲁克和帕特没有重逢】\n'),
            TXT(0x01, '【◇鲁克和帕特已经重逢】\n'),
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
        (0x00000000, 'loc_8C5'),
        (0x00000001, 'loc_8CB'),
        (-1, 'loc_8D1'),
    )

    def _loc_8C5(): pass

    label('loc_8C5')

    ClearScenaFlags(ScenaFlag(0x0310, 3, 0x1883))

    Jump('loc_8D1')

    def _loc_8CB(): pass

    label('loc_8CB')

    SetScenaFlags(ScenaFlag(0x0310, 3, 0x1883))

    Jump('loc_8D1')

    def _loc_8D1(): pass

    label('loc_8D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 3, 0x1883)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9A2',
    )

    ChrTalk(
        0x000A,
        (
            '#0860281615V啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281616V#6P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281617V#6P这不是布莱特家的\n',
            '艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281618V#1025F#2P好久不见。\n',
            '玛茜婆婆、帕特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281619V#1003F鲁克……\n',
            '很麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A68')

    def _loc_9A2(): pass

    label('loc_9A2')

    ChrTalk(
        0x000A,
        (
            '#0860281620V啊……\n',
            '艾丝蒂尔姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281616V#6P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281617V#6P这不是布莱特家的\n',
            '艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281623V#1025F#2P那个，晚上好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281619V#1003F鲁克……\n',
            '很麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A68(): pass

    label('loc_A68')

    ChrTalk(
        0x000A,
        (
            '#0860281625V呜呜，姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281626V艾丝蒂尔姐姐！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadChip('ED6_DT26/CH20337._CH', 'ED6_DT26/CH20337P._CP', 5)
    ChrSetFlags(0x000A, 0x0040)
    ChrMoveTo(0x000A, 56270, 0, 162360, 4000, 0x00)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x000A, 0x0080)
    ChrMoveToRelativeAsync(0x0101, 0, 0, 200, 4000, 0x00)

    @scena.Lambda('lambda_0AF7')
    def lambda_0AF7():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0AF7)

    Sleep(50)

    @scena.Lambda('lambda_0B0A')
    def lambda_0B0A():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0B0A)

    Sleep(50)

    @scena.Lambda('lambda_0B1D')
    def lambda_0B1D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0B1D)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010281627V#1004F#2P哇哇……\n',
            '怎么了？帕特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281628V#6P也难怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281629V#6P是这孩子发现鲁克\n',
            '倒在地上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281630V#1003F#2P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281631V#1025F帕特……辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281632V#6P呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030281633V#022F玛茜婆婆，\n',
            '您孙子的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281634V#6P嗯，现在\n',
            '睡得很熟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281635V#6P没事，不用担心，\n',
            '到早上一定会起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281636V#6P因为他是个只有精力用不完的\n',
            '淘气小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281637V#6P怎么可能从此\n',
            '一睡不起呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281638V#522F玛茜婆婆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281639V#1010F#2P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281640V#1002F……我说，帕特，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281641V能不能跟我说说\n',
            '鲁克睡着时的样子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281642V#6P……咦………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281643V#1002F#2P我们受市长先生的委托\n',
            '来调查此次的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281644V如果帕特告诉我们线索，\n',
            '我们就会离案件解决更近一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281645V所以……拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281646V#6P姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281647V……嗯………\n',
            '我……会详细说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x000A, 0x0080)
    OP_0D()
    ChrMoveTo(0x000A, 56170, 0, 162000, 1000, 0x00)
    ChrClearFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_0F1E')
    def lambda_0F1E():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0F1E)

    Sleep(50)

    @scena.Lambda('lambda_0F31')
    def lambda_0F31():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F31)

    Sleep(50)

    @scena.Lambda('lambda_0F44')
    def lambda_0F44():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0F44)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010281648V#1025F#2P谢谢你，帕特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281649V#1002F那么，鲁克是在\n',
            '何时何地睡着的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281650V#6P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281651V我是在钟楼\n',
            '发现鲁克的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281652V时间是……\n',
            '５点过一点点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281653V那时，我们在雾中\n',
            '玩捉迷藏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281654V我扮鬼，正在找\n',
            '躲着的鲁克。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281655V可当我好不容易找到他时，\n',
            '他却睡着了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281656V当我没办法只能把他叫醒的时候，\n',
            '他却醒不过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281657V#1007F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281658V#1015F那么是谁把鲁克\n',
            '送来这里的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281659V#6P啊，嗯，\n',
            '是看守钟楼的潘杜爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281660V正在我感到为难时，\n',
            '他走了上来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281661V他是来查看钟有没有\n',
            '因为雾而出故障的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281662V#1011F#2P是这样啊……\n',
            '的确是潘杜爷爷的作风。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281663V#1006F嗯，大体情况我了解了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281664V#020F……那么，帕特，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281665V捉迷藏时，\n',
            '有没有发生什么怪事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0103, 400)

    ChrTalk(
        0x000A,
        (
            '#0860281666V#6P怪事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281667V#020F比如见到陌生人或者\n',
            '听到怪异的声音？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281668V什么都可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281669V#6P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281670V除了纯白色的雾之外\n',
            '其它不记得什么了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281671V还有就是飞船坪里没有人，\n',
            '稍微有点可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281672V#524F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281673V#1015F#2P看来没什么\n',
            '可疑的事发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281674V#026F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281675V#020F谢谢你们，\n',
            '给我们提供了很好的参考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3410281676V#6P是吗……\n',
            '那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0860281677V#6P艾丝蒂尔姐姐……\n',
            '鲁克，会没事的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281678V#1006F#2P嗯……当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281679V帕特你也\n',
            '别再哭鼻子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281680V不然鲁克醒过来时\n',
            '可会笑话你的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0860281681V#6P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0860281682V是啊。\n',
            '我不会再哭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(53810, 0, 164450, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 53810, 0, 164450, 0)
    ChrSetPos(0x0103, 53810, 0, 164450, 0)
    ChrSetPos(0x00F8, 53810, 0, 164450, 0)
    ChrSetPos(0x00F9, 53810, 0, 164450, 0)
    ChrSetPos(0x000A, 56170, 0, 161420, 180)
    ChrSetDirection(0x0009, 180, 0)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    SetScenaFlags(ScenaFlag(0x0302, 6, 0x1816))
    OP_28(0x0090, 0x02, 0x0020)
    OP_28(0x0090, 0x01, 0x0040)

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
        'loc_1631',
    )

    OP_28(0x0090, 0x01, 0x0200)

    Jump('loc_1631')

    def _loc_1631(): pass

    label('loc_1631')

    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
