import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2311   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2311.x'
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
        ('ED6_DT07/CH00374._CH', 'ED6_DT07/CH00374P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪恩',
            x                   = -31270,
            z                   = 0,
            y                   = 42780,
            direction           = 90,
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
            name                = '雷斯',
            x                   = -30310,
            z                   = 0,
            y                   = 42270,
            direction           = 90,
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
            name                = '洛克',
            x                   = -28770,
            z                   = 0,
            y                   = 42770,
            direction           = 90,
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
            name                = '青年',
            x                   = -31020,
            z                   = 0,
            y                   = 44700,
            direction           = 90,
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
            name                = '青年',
            x                   = -30070,
            z                   = 0,
            y                   = 44130,
            direction           = 90,
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
            name                = '青年',
            x                   = -29310,
            z                   = 0,
            y                   = 43790,
            direction           = 90,
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
            name                = '青年',
            x                   = -31330,
            z                   = 0,
            y                   = 43790,
            direction           = 90,
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
            name                = '青年',
            x                   = -30780,
            z                   = 0,
            y                   = 43810,
            direction           = 90,
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
            name                = '青年',
            x                   = -30050,
            z                   = 0,
            y                   = 43240,
            direction           = 90,
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
            name                = '秘书基尔巴特',
            x                   = -26650,
            z                   = 0,
            y                   = 44050,
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
            name                = '卡露娜',
            x                   = -30050,
            z                   = 0,
            y                   = 39240,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '阿梅莉娅',
            x                   = -200,
            z                   = 0,
            y                   = 8850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '扎古',
            x                   = -3700,
            z                   = 0,
            y                   = 5500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '索雷诺',
            x                   = -33200,
            z                   = 0,
            y                   = 5700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '塞尔吉村长',
            x                   = -26100,
            z                   = 0,
            y                   = 4800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x2C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2C2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2CC',
    )

    Jump('loc_374')

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_309',
    )

    ChrSetPos(0x0014, -26670, 0, 39530, 90)
    ChrSetPos(0x0016, -30150, 0, 3860, 270)
    ChrSetPos(0x0015, -29310, 0, 43880, 0)

    Jump('loc_374')

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_313',
    )

    Jump('loc_374')

    def _loc_313(): pass

    label('loc_313')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_331',
    )

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0008)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0008)

    Jump('loc_374')

    def _loc_331(): pass

    label('loc_331')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_34F',
    )

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0008)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0008)

    Jump('loc_374')

    def _loc_34F(): pass

    label('loc_34F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_359',
    )

    Jump('loc_374')

    def _loc_359(): pass

    label('loc_359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_363',
    )

    Jump('loc_374')

    def _loc_363(): pass

    label('loc_363')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_36D',
    )

    Jump('loc_374')

    def _loc_36D(): pass

    label('loc_36D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_374',
    )

    def _loc_374(): pass

    label('loc_374')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A1',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x0002)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A1',
    )

    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0008)

    def _loc_3A1(): pass

    label('loc_3A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E4',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3F2',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_08_6AF)

    def _loc_3F2(): pass

    label('loc_3F2')

    Return()

# id: 0x0001 offset: 0x3F3
@scena.Code('func_01_3F3')
def func_01_3F3():
    Return()

# id: 0x0002 offset: 0x3F4
@scena.Code('func_02_3F4')
def func_02_3F4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_409',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3F4')

    def _loc_409(): pass

    label('loc_409')

    Return()

# id: 0x0003 offset: 0x40A
@scena.Code('func_03_40A')
def func_03_40A():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '扎古到游击士协会\n',
            '通报情况去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出事的时候\n',
            '弟弟还是值得依靠的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0004 offset: 0x45B
@scena.Code('func_04_45B')
def func_04_45B():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '知道谁是犯人了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做了那么过分的事，\n',
            '决不能放过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要抓住犯人，\n',
            '并狠狠地惩罚他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_520')

    def _loc_4D2(): pass

    label('loc_4D2')

    ChrTalk(
        0x00FE,
        (
            '做了那么过分的事，\n',
            '决不能放过他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要抓住犯人，\n',
            '并狠狠地惩罚他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_520(): pass

    label('loc_520')

    TalkEnd(0x0014)

    Return()

# id: 0x0005 offset: 0x524
@scena.Code('func_05_524')
def func_05_524():
    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '我想先给孩子们\n',
            '做些吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和旅店的卡拉商量了一下，\n',
            '要了些做菜的材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0015)

    Return()

# id: 0x0006 offset: 0x57D
@scena.Code('func_06_57D')
def func_06_57D():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_605',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '像这样的事件……\n',
            '绝对不允许再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个村庄的每个人\n',
            '都会支持你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了孩子们，\n',
            '请一定要抓住犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_655')

    def _loc_605(): pass

    label('loc_605')

    ChrTalk(
        0x00FE,
        (
            '像这样的事件……\n',
            '绝对不允许再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了孩子们，\n',
            '请一定要抓住犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_655(): pass

    label('loc_655')

    TalkEnd(0x0016)

    Return()

# id: 0x0007 offset: 0x659
@scena.Code('func_07_659')
def func_07_659():
    TalkBegin(0x0012)

    ChrTalk(
        0x0012,
        (
            '那帮家伙由我看着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061360V你们就赶去卢安，\n',
            '向嘉恩报告昨天的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x6AF
@scena.Code('func_08_6AF')
def func_08_6AF():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-29840, 0, 41310, 0)
    FormationDelMember(0x05, 0xFF)
    ChrSetPos(0x0101, -29970, 0, 37680, 0)
    ChrSetPos(0x0102, -30850, 0, 37060, 0)
    ChrSetPos(0x0105, -29450, 0, 36780, 0)
    ChrSetDirection(0x0012, 180, 0)

    ChrTalk(
        0x0012,
        (
            '好了……\n',
            '那帮家伙由我看着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0320061336V你们就赶去卢安，\n',
            '向嘉恩报告昨天的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们倒是没关系，不过……\n',
            '卡露娜姐姐您已经没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '当然啦。只是被人抓住破绽，\n',
            '熏了点催眠药而已嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0321180001V还真是丢脸啊。\n',
            '竟然被那些家伙钻了空子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061341V#010F这也不能怪您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也是四人联手\n',
            '才勉强击退那些犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061343V#040F那些孩子们平安无事，\n',
            '也都多亏了卡露娜小姐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061344V真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '哈哈……\n',
            '是啊，总算是不幸中的大幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我听说阿加特\n',
            '自己一个人去追那帮家伙了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '虽然他的身手不容置疑，\n',
            '但说到底还是有点担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……\n',
            '要是没捉到他们反而受伤的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F现在也唯有相信阿加特先生了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '从昨天他所说的话判断，\n',
            '他好像一直在追那些犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对于他们的做事手法似乎也很了解，\n',
            '我想应该不会那么轻易失手的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……也对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061353V所以，我们现在也应该\n',
            '尽力做好自己能做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '没错，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '在事情了结之前，\n',
            '这些属于特蕾莎院长的捐款\n',
            '就先由我来暂代保管吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0320061356V这次我一定会保护好的，\n',
            '所以你们就安心出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F好的，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#000F那么，我们走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
