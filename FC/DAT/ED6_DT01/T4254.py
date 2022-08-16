import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4254_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4254   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4254.x'
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
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02463._CH', 'ED6_DT07/CH02463P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希尔丹夫人',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '茜亚',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x122
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
        'loc_14C',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 2)
    ChrSetChipByIndex(0x0138, 3)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_14C(): pass

    label('loc_14C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_15A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_05_A52)

    def _loc_15A(): pass

    label('loc_15A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_168',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_07_2E8D)

    def _loc_168(): pass

    label('loc_168')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_174'),
        (-1, 'loc_18A'),
    )

    def _loc_174(): pass

    label('loc_174')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 1, 0x641)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_187',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 2, 0x642))
    Event(0, func_06_11E2)

    def _loc_187(): pass

    label('loc_187')

    Jump('loc_18A')

    def _loc_18A(): pass

    label('loc_18A')

    SetScenaFlags(ScenaFlag(0x00C7, 1, 0x639))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 72500, 0, 68560, 90)
    CreateThread(0x0008, 0x00, 0x00, func_02_2D3)

    Jump('loc_2B8')

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1DB',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 64129, 0, 99150, 167)
    CreateThread(0x0008, 0x00, 0x00, func_02_2D3)

    Jump('loc_2B8')

    def _loc_1DB(): pass

    label('loc_1DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_21F',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 72500, 0, 68560, 90)
    CreateThread(0x0008, 0x00, 0x00, func_02_2D3)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 62980, 0, 65500, 180)
    CreateThread(0x0009, 0x00, 0x00, func_02_2D3)

    Jump('loc_2B8')

    def _loc_21F(): pass

    label('loc_21F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_246',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 70630, 0, 98590, 48)
    CreateThread(0x0009, 0x00, 0x00, func_02_2D3)

    Jump('loc_2B8')

    def _loc_246(): pass

    label('loc_246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_250',
    )

    Jump('loc_2B8')

    def _loc_250(): pass

    label('loc_250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            Expr.Return,
        ),
        'loc_294',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 72490, 0, 68540, 90)
    CreateThread(0x0008, 0x00, 0x00, func_02_2D3)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 70630, 0, 98590, 48)
    CreateThread(0x0009, 0x00, 0x00, func_02_2D3)

    Jump('loc_2B8')

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_2B8',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 70630, 0, 98590, 48)
    CreateThread(0x0009, 0x00, 0x00, func_02_2D3)

    def _loc_2B8(): pass

    label('loc_2B8')

    Return()

# id: 0x0001 offset: 0x2B9
@scena.Code('func_01_2B9')
def func_01_2B9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_2C9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C9(): pass

    label('loc_2C9')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x2D3
@scena.Code('func_02_2D3')
def func_02_2D3():
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
        'loc_2F8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_43A')

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_311',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_43A')

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_43A')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_343',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_43A')

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_43A')

    def _loc_35C(): pass

    label('loc_35C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_375',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_43A')

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_43A')

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_43A')

    def _loc_3A7(): pass

    label('loc_3A7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C0',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_43A')

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_43A')

    def _loc_3D9(): pass

    label('loc_3D9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_43A')

    def _loc_3F2(): pass

    label('loc_3F2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40B',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_43A')

    def _loc_40B(): pass

    label('loc_40B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_424',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_43A')

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_43A(): pass

    label('loc_43A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_43A')

    def _loc_44F(): pass

    label('loc_44F')

    Return()

# id: 0x0003 offset: 0x450
@scena.Code('func_03_450')
def func_03_450():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_45D',
    )

    Jump('loc_6C5')

    def _loc_45D(): pass

    label('loc_45D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_467',
    )

    Jump('loc_6C5')

    def _loc_467(): pass

    label('loc_467')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_4BD',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '希望公主殿下能够平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果我能够\n',
            '陪在她身边就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C5')

    def _loc_4BD(): pass

    label('loc_4BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_520',
    )

    ChrTurnDirection(0x00FE, 0x0138, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚先生的肌肤\n',
            '和女性一样细腻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要化妆得当，\n',
            '就会变得相当漂亮哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C5')

    def _loc_520(): pass

    label('loc_520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_52A',
    )

    Jump('loc_6C5')

    def _loc_52A(): pass

    label('loc_52A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 6, 0x63E)),
            Expr.Return,
        ),
        'loc_5D8',
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
        'loc_5A0',
    )

    ChrTalk(
        0x00FE,
        (
            '晚宴招待的客人们\n',
            '应该都在各自的房间里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚宴的准备工作结束之前\n',
            '请二位耐心等待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D5')

    def _loc_5A0(): pass

    label('loc_5A0')

    ChrTalk(
        0x00FE,
        (
            '晚宴的准备就快做完了。\n',
            '请你们再稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0049, 0x01, 0x0800)

    def _loc_5D5(): pass

    label('loc_5D5')

    Jump('loc_6C5')

    def _loc_5D8(): pass

    label('loc_5D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_6C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_620',
    )

    ChrTalk(
        0x00FE,
        (
            '距晚宴开始\n',
            '还有一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请慢慢在城里参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C5')

    def _loc_620(): pass

    label('loc_620')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么了？\n',
            '是不是有什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，没什么，\n',
            '我们正在城里参观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '距晚宴开始\n',
            '还有一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请慢慢在城里参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C5(): pass

    label('loc_6C5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x6C9
@scena.Code('func_04_6C9')
def func_04_6C9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_7A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_734',
    )

    ChrTalk(
        0x0008,
        (
            '#711F在诞辰庆典上玩累了吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140663V如果有什么难处，\n',
            '尽管告诉我就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7A6')

    def _loc_734(): pass

    label('loc_734')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#711F艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140662V在诞辰庆典上玩累了吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140663V如果有什么难处，\n',
            '尽管告诉我就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7A6(): pass

    label('loc_7A6')

    Jump('loc_A4E')

    def _loc_7A9(): pass

    label('loc_7A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_8A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_825',
    )

    ChrTalk(
        0x0008,
        (
            '#0650140659V#710F因为诞辰庆典，\n',
            '现在街上变得很热闹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140658V你们就去好好玩玩吧，\n',
            '要注意安全哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A2')

    def _loc_825(): pass

    label('loc_825')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#710F啊，\n',
            '你们两个打算出去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为诞辰庆典，\n',
            '现在王都变得很热闹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140658V你们就去好好玩玩吧，\n',
            '要注意安全哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A2(): pass

    label('loc_8A2')

    Jump('loc_A4E')

    def _loc_8A5(): pass

    label('loc_8A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_95B',
    )

    ChrTalk(
        0x0008,
        (
            '#0650120569V#714F因为没有出现什么破绽，\n',
            '所以我想应该不会被发现……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120570V不过在回到房间之前\n',
            '还是要千万小心才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120571V情报部的耳目\n',
            '可是遍布各个角落的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4E')

    def _loc_95B(): pass

    label('loc_95B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_965',
    )

    Jump('loc_A4E')

    def _loc_965(): pass

    label('loc_965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_96F',
    )

    Jump('loc_A4E')

    def _loc_96F(): pass

    label('loc_96F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_A4E',
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
        'loc_9DF',
    )

    ChrTalk(
        0x0008,
        (
            '#0650120565V#711F是问晚宴吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120566V因为料理还在准备，\n',
            '请再稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4E')

    def _loc_9DF(): pass

    label('loc_9DF')

    ChrTalk(
        0x0008,
        (
            '#0650120563V#711F料理准备完毕之后，\n',
            '晚宴就会立刻开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120564V你们就请先回房间休息一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0049, 0x01, 0x0800)

    def _loc_A4E(): pass

    label('loc_A4E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xA52
@scena.Code('func_05_A52')
def func_05_A52():
    EventBegin(0x00)
    CameraMove(62970, 640, 71000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0008, 0xFF)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 64390, 200, 71030, 270)
    ChrSetPos(0x0101, 61580, 200, 71540, 90)
    ChrSetPos(0x0102, 61580, 200, 70620, 90)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0650120535V#713F……你们要说的我都明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120536V想要把拉赛尔博士的传话\n',
            '直接禀告给女王陛下吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120537V#714F就是这件事对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120538V#002F对……就是这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120539V如果女王陛下真的是身体不适，\n',
            '我们就再重新想其他的办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120540V#715F那并不是问题所在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120541V女王宫正处于刚才那些特务兵的\n',
            '２４小时监控状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120542V能够进去的只有公爵大人和上校，\n',
            '以及照料女王的我和一些侍女。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120543V#007F这么说来，\n',
            '想要去见女王果真是非常困难的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 1)

    ChrTalk(
        0x0102,
        (
            '#0020120544V#012F怎么办，艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120545V看来唯有拜托希尔丹夫人\n',
            '将博士的传话禀告给女王陛下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 2)

    ChrTalk(
        0x0101,
        (
            '#0010120546V#505F唔～～～\n',
            '可是还是直接去和女王谈谈更好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120547V杜南公爵的目的和理查德上校的企图……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120548V不清楚的事情还有很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120549V#713F……艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120550V#714F我已经有些打算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120551V晚宴结束之后\n',
            '你们可以再来这里一趟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)
    Sleep(200)

    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010110369V#004F咦，这么说来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120553V#014F我们和女王见面的方法已经有了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120554V#711F这么想也是可以的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120555V虽然可能比较困难……\n',
            '但还是有试一试的价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120556V因为还要做一些准备的工作，\n',
            '所以请等到晚宴结束再来可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120557V#001F好～的，太幸运了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120558V#010F我明白了。\n',
            '晚宴一结束就来向您请教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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
        'loc_109D',
    )

    ChrTalk(
        0x0008,
        (
            '#0650120559V#713F我会等候你们的到来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120560V#711F啊，说到晚宴的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120561V料理还在准备中，请稍等片刻。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1131')

    def _loc_109D(): pass

    label('loc_109D')

    ChrTalk(
        0x0008,
        (
            '#0650120559V#713F我会等候你们的到来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120563V#711F料理准备完毕之后，\n',
            '晚宴就会立刻开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120564V你们可以先回房间休息一下。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0049, 0x01, 0x0800)

    def _loc_1131(): pass

    label('loc_1131')

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, 66930, 0, 66430, 180)
    ChrSetPos(0x0102, 66930, 0, 66430, 180)
    ChrSetPos(0x0008, 72490, 0, 68540, 90)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    ChrClearFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0800)
    CreateThread(0x0008, 0x00, 0x00, func_02_2D3)
    CameraMove(66930, 0, 66430, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x11E2
@scena.Code('func_06_11E2')
def func_06_11E2():
    EventBegin(0x00)
    CameraMove(67590, 0, 65319, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 70120, 0, 69770, 225)
    ChrSetPos(0x0101, 66580, 0, 64769, 45)
    ChrSetPos(0x0102, 67630, 0, 64590, 45)

    @scena.Lambda('lambda_1233')
    def lambda_1233():
        CameraMove(69520, 0, 68800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1233)

    @scena.Lambda('lambda_124B')
    def lambda_124B():
        ChrWalkTo(0x00FE, 68460, 0, 68580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_124B)

    @scena.Lambda('lambda_1266')
    def lambda_1266():
        ChrWalkTo(0x00FE, 69950, 0, 67930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1266)

    WaitForThreadExit(0x0102, 0x0002)
    ChrTurnDirection(0x0102, 0x0008, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0650120936V#710F艾丝蒂尔、约修亚。\n',
            '我一直在等你们哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120937V不觉得迟到了很久吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120938V#506F这个……对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120939V刚才不巧被理查德上校抓住了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120940V#712F上校……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120941V#010F只是谈了一些关于我们父亲过去的事情。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120942V与这边的行动无关，\n',
            '请夫人您不用在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120943V#713F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120944V#710F根据尤莉亚的介绍信来看，\n',
            '你们两位是卡西乌斯先生的孩子吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120945V理查德上校会有\n',
            '一些感慨也是理所当然的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120946V#004F那个～请问一下，\n',
            '希尔丹夫人也知道父亲的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120947V#711F曾经作为摩尔根将军副官的卡西乌斯上校\n',
            '经常到王城这里来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120948V他也是去世的王子……\n',
            '也就是陛下的儿子以前的校友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120949V#505F去世的王子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120950V#012F就是科洛蒂亚公主的父亲。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120951V#715F嗯，王太子夫妇因为\n',
            '１５年前的海难事故而不幸身亡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120952V倘若王子还活着的话，\n',
            '现在这样的局面是不会发生的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101027V#002F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120954V#713F……对于已经发生的事情，\n',
            '后悔是没有用处的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120955V夜色已晚，这就准备出发吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, 69050, 0, 75720, 180)
    ChrClearFlags(0x0009, 0x0080)
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0650120956V#710F茜亚，过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    OP_73(0x0003)

    @scena.Lambda('lambda_1721')
    def lambda_1721():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1721)

    @scena.Lambda('lambda_172F')
    def lambda_172F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_172F)

    Sleep(300)

    @scena.Lambda('lambda_1742')
    def lambda_1742():
        ChrSetDirection(0x00FE, 180, 0)
        Yield()

        Jump('lambda_1742')

    DispatchAsync2(0x0009, 0x0001, lambda_1742)

    @scena.Lambda('lambda_1753')
    def lambda_1753():
        ChrWalkTo(0x00FE, 68810, 0, 70320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1753)

    @scena.Lambda('lambda_176E')
    def lambda_176E():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_176E')

    DispatchAsync2(0x0008, 0x0001, lambda_176E)

    @scena.Lambda('lambda_177F')
    def lambda_177F():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_177F')

    DispatchAsync2(0x0101, 0x0001, lambda_177F)

    @scena.Lambda('lambda_1790')
    def lambda_1790():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_1790')

    DispatchAsync2(0x0102, 0x0001, lambda_1790)

    CameraMove(70030, 0, 70300, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010120957V#004F咦，你不是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120958V#010F您是茜亚小姐对吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120959V#5P你、你们好……\n',
            '艾丝蒂尔小姐，约修亚先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120960V#5P事情我已经知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120961V#711F#2P你们完全可以相信这个孩子。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120962V公主殿下在城里的时候，\n',
            '就是由这位侍女陪伴在身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120963V#501F公主殿下……\n',
            '就是科洛蒂亚公主吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120964V#019F这样的话就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120965V#5P谢、谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120966V#5P那么这就把准备好的制服\n',
            '拿来试穿一下可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120967V#5P总之小姐您应该会称心的。\n',
            '丝带啊头饰啊那些细小的方面\n',
            '我都已经准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120968V#004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120969V#014F这么说……难道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0650120970V#711F#2P是啊，艾丝蒂尔如果\n',
            '装扮成侍女的样子就可以进入女王宫了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120971V再把头发的样式改变一下，\n',
            '看守的那些人也就觉察不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120972V#501F原～来是这～样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120973V#010F的确，制服可以很好地\n',
            '将个人的特征隐藏起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120974V用来掩人耳目就再好不过了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120975V#008F啊～侍女的服饰啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120976V之前看到过莉拉小姐的着装，\n',
            '觉得那款式很不错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120977V既飘逸而又很可爱，\n',
            '行动起来也很方便的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120978V#5P嘻嘻，如果行动不方便的话，\n',
            '那扫除的时候就麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120979V#006F啊，真的是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120980V#001F那就立刻穿上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120981V#019F#2P很开心嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120982V#010F蹦蹦跳跳的虽然是可以，\n',
            '但不要在陛下面前失礼哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120983V这次我是不能和你一起去了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120984V#004F啊，为什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120985V约修亚也换装不就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020120986V#014F#2P#5S……咦。',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0650120987V#712F#2P艾丝蒂尔，你说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120988V#501F约修亚你在学园祭的舞台剧里\n',
            '扮演的公主不是很好看的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120989V礼服和侍女装不是差不多吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120990V#018F#2P这、这可不是在演戏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120991V和女王陛下见面却身着女装，\n',
            '这实在是有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120992V#001F没关系，没关系。\n',
            '一点都不难看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120993V当时约修亚扮演的公主可是非常美丽哦！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120994V#017F#2P又、又来了……别开玩笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120995V#012F希尔丹夫人你们也帮我说说情啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0650120996V#712F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120997V#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020120998V#018F我、我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650120999V#713F#2P原来如此……\n',
            '好像的确没有什么问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121000V#710F茜亚，\n',
            '为公主殿下准备的假发还在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121001V#5P是、是的……\n',
            '一次都没有使用过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121002V#5P如果是长长的黑发，\n',
            '和约修亚先生会很配的哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121003V#018F我、我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121004V#001F三比一，少数服从多数～\n',
            '最终的结果已经揭晓⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121005V#5P那就请到这边来。\n',
            '您的服装已经准备好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_221D')
    def lambda_221D():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_221D')

    DispatchAsync2(0x0008, 0x0001, lambda_221D)

    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetDirection(0x0009, 0, 400)

    @scena.Lambda('lambda_2249')
    def lambda_2249():
        ChrWalkTo(0x00FE, 68680, 0, 77130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2249)

    Sleep(300)

    ChrWalkTo(0x0101, 69620, 0, 68330, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020121006V#012F请等一下！\n',
            '我换衣服这件事怎么一句话就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 69610, 0, 67850, 2000, 0x00)
    ChrSetDirection(0x0102, 180, 400)

    @scena.Lambda('lambda_22D8')
    def lambda_22D8():
        CameraMove(69970, 0, 72360, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_22D8)

    @scena.Lambda('lambda_22F0')
    def lambda_22F0():
        ChrWalkTo(0x00FE, 68680, 0, 77130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22F0)

    @scena.Lambda('lambda_230B')
    def lambda_230B():
        ChrMoveTo(0x00FE, 68680, 0, 77130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_230B)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_72(0x0003, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)
    OP_73(0x0003)
    OP_71(0x0003, 0x0800)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020121007V#4P我知道，我知道啦……\n',
            '衣服什么的由我自己来脱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121008V啊……茜亚小姐……\n',
            '还要化妆的啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0650121009V#716F呼……\n',
            '现在的年轻人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(69200, 0, 72370, 0)
    ChrSetPos(0x0008, 68890, 0, 69520, 0)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    Sleep(500)

    FadeIn(2000, 0)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    OP_73(0x0003)

    @scena.Lambda('lambda_246F')
    def lambda_246F():
        ChrSetDirection(0x00FE, 225, 0)
        Yield()

        Jump('lambda_246F')

    DispatchAsync2(0x0101, 0x0002, lambda_246F)

    @scena.Lambda('lambda_2480')
    def lambda_2480():
        ChrWalkTo(0x00FE, 69730, 0, 71410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2480)

    Sleep(600)

    @scena.Lambda('lambda_24A0')
    def lambda_24A0():
        ChrWalkTo(0x00FE, 69120, 0, 73080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_24A0)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_24C0')
    def lambda_24C0():
        ChrWalkTo(0x00FE, 67850, 0, 73240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_24C0)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_24E0')
    def lambda_24E0():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_24E0)

    ChrTalk(
        0x0008,
        (
            '#0650121010V#712F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121011V#321F#5P#3S您～好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    ChrSetDirection(0x0101, 317, 400)
    ChrSetDirection(0x0101, 75, 400)
    ChrSetDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121012V#328F#5P嗯，怎么样～呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121013V嘻嘻嘻……\n',
            '非常合适呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650121014V#711F从乡村地方到城里不久、\n',
            '活泼开朗的实习侍女……\n',
            '这种解释十分有说服力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121015V头发披下来之后，\n',
            '就更不容易被别人察觉到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121016V不如就到我们这个\n',
            '格兰赛尔城来工作如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121017V#474F#5P游、游击士协会那边还有任务，\n',
            '所以这个就不好意思了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121018V#471F啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121019V#321F喂喂，约修亚。\n',
            '快点出来吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_270C')
    def lambda_270C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_270C)

    @scena.Lambda('lambda_271A')
    def lambda_271A():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_271A)

    CameraMove(69080, 0, 73680, 1000)
    ChrSetPos(0x0102, 69050, 0, 77130, 180)

    ChrTalk(
        0x0102,
        (
            '#0020121020V#4P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121021V不出来不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121022V#326F不～行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121023V再喋喋不休的话，\n',
            '我就进去把你拖出来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121024V#4P我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121025V唉，没办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2814')
    def lambda_2814():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2814')

    DispatchAsync2(0x0009, 0x0001, lambda_2814)

    @scena.Lambda('lambda_2825')
    def lambda_2825():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2825')

    DispatchAsync2(0x0008, 0x0001, lambda_2825)

    @scena.Lambda('lambda_2836')
    def lambda_2836():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2836')

    DispatchAsync2(0x0101, 0x0001, lambda_2836)

    @scena.Lambda('lambda_2847')
    def lambda_2847():
        OP_6C(5000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2847)

    @scena.Lambda('lambda_2857')
    def lambda_2857():
        OP_67(0, 6130, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2857)

    Sleep(1600)

    @scena.Lambda('lambda_2874')
    def lambda_2874():
        ChrWalkTo(0x00FE, 69050, 0, 73160, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2874)

    Sleep(3000)

    @scena.Lambda('lambda_2894')
    def lambda_2894():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2894)

    @scena.Lambda('lambda_28A4')
    def lambda_28A4():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_28A4)

    OP_62(0x0102, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(500)

    PlaySE(137, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)
    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020121026V#333F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650121027V#712F这衣服和你竟然会……\n',
            '相称到如此惊人的程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121028V#326F怎么样，我说过的吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121029V#327F约修亚真是的……\n',
            '竟然比身为少女的我还要漂亮，\n',
            '这到底是怎～么回事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121030V嘻嘻……\n',
            '我还为他好好地化了妆的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121031V#335F#5P好了……\n',
            '请不要再说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(68990, 0, 71660, 1000)

    @scena.Lambda('lambda_2A56')
    def lambda_2A56():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A56)

    @scena.Lambda('lambda_2A64')
    def lambda_2A64():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2A64)

    ChrSetDirection(0x0102, 180, 0)

    ChrTalk(
        0x0008,
        (
            '#0650121032V#710F嗯……准备完毕了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121033V那么，我现在就\n',
            '带领你们两个去女王宫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121034V彻底地把自己当成实习侍女，\n',
            '这一点你们一定要记住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121035V#471F啊，好的，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121036V#322F唔……\n',
            '终于要见到女王了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121037V#332F嗯……到了关键时刻了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121038V集中精力，\n',
            '无论如何也要进入女王宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121039V#475F噗……你这身打扮配合\n',
            '这样严肃的口气真是天衣无缝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 800)

    ChrTalk(
        0x0102,
        (
            '#0020121040V#337F太、太坏了！\n',
            '什么天衣无缝！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121041V#333F我都打扮成这副模样了，\n',
            '你还在取笑我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121042V#321F对不起～对不起。\n',
            '不要生气嘛～约修亚最听话的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121043V下次我请你吃冰淇淋～\n',
            '总之你就消消气啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121044V#332F哼，我又不是你，\n',
            '用零食是不能收买我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121045V#476F我、我什么时候\n',
            '被零食什么的给收买过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121046V嘻嘻……\n',
            '真是一对好伙伴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650121047V#713F时间快来不及了……\n',
            '立刻前往女王宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapSetFlags(0x80000000)
    OP_28(0x004A, 0x01, 0x0020)
    OP_28(0x004A, 0x01, 0x0040)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x0009, 0x0080)
    FormationAddMember(0x37, 0xFF)
    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 2)
    ChrSetChipByIndex(0x0138, 3)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 67460, 0, 69310, 180)
    ChrSetPos(0x0102, 67460, 0, 69310, 180)
    ChrSetPos(0x0138, 67460, 0, 69310, 180)
    CameraMove(67460, 0, 69310, 0)
    OP_6F(0x0003, 0)
    OP_71(0x0003, 0x0010)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x2E8D
@scena.Code('func_07_2E8D')
def func_07_2E8D():
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(68370, 0, 69650, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 68920, 0, 70070, 180)
    ChrSetPos(0x0009, 67750, 0, 70350, 180)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    FormationDelMember(0x37, 0xFF)
    ChrSetPos(0x0101, 68360, 0, 68190, 0)
    ChrSetPos(0x0102, 67080, 0, 68350, 45)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010121467V#006F希尔丹夫人、茜亚小姐，\n',
            '今天真是太感谢你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121468V#010F帮了我们大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0650121469V#711F哪里，这是身为服侍女王陛下的我\n',
            '理所当然要做的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121470V陛下委托的任务就拜托你们了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121471V我、我……\n',
            '我也要拜托你们了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121472V请一定要帮我们……\n',
            '把公主殿下救出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121473V#002F啊……\n',
            '茜亚小姐服侍过公主殿下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121474V嗯，服侍过……\n',
            '虽然能够照顾她的机会并不多，\n',
            '这是我非常遗憾的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121475V但是她把我这种下人\n',
            '当作朋友一样对待，\n',
            '是一位平易近人而又温柔的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121476V当听说她被那些坏人捉去，\n',
            '被囚禁在不知道什么地方的时候，\n',
            '我每天都担心得睡不着觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121477V#006F不用担心……\n',
            '我们一定会把她救出来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121478V#010F那我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    MapClearFlags(0x80000000)
    CreateThread(0x0008, 0x00, 0x00, func_02_2D3)
    CreateThread(0x0009, 0x00, 0x00, func_02_2D3)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
