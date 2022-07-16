import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4214_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4214   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '希尔丹夫人'),
    TXT(0x02, '茜亚'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4214.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x25A8
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
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
    ]

# id: 0x10002 offset: 0xCA
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x10A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x10A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x10A
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
        'loc_134',
    )

    SetChrChipByIndex(0x0000, 0)
    SetChrChipByIndex(0x0001, 2)
    SetChrChipByIndex(0x0138, 3)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_134(): pass

    label('loc_134')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_142',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0005)

    def _loc_142(): pass

    label('loc_142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_150',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0007)

    def _loc_150(): pass

    label('loc_150')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_15C'),
        (-1, 'loc_172'),
    )

    def _loc_15C(): pass

    label('loc_15C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 1, 0x641)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16F',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 2, 0x642))
    Event(0, 0x0006)

    def _loc_16F(): pass

    label('loc_16F')

    Jump('loc_172')

    def _loc_172(): pass

    label('loc_172')

    SetScenaFlags(ScenaFlag(0x00C7, 1, 0x639))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_19C',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 64129, 0, 99150, 167)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    Jump('loc_23F')

    def _loc_19C(): pass

    label('loc_19C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1C3',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 70620, 0, 69790, 90)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    Jump('loc_23F')

    def _loc_1C3(): pass

    label('loc_1C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1CD',
    )

    Jump('loc_23F')

    def _loc_1CD(): pass

    label('loc_1CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1F4',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 70630, 0, 98590, 48)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    Jump('loc_23F')

    def _loc_1F4(): pass

    label('loc_1F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1FE',
    )

    Jump('loc_23F')

    def _loc_1FE(): pass

    label('loc_1FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_23F',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 64129, 0, 99150, 167)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 70630, 0, 98590, 48)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    def _loc_23F(): pass

    label('loc_23F')

    Return()

# id: 0x0001 offset: 0x240
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x24A
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
        'loc_26F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3B1')

    def _loc_26F(): pass

    label('loc_26F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_288',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3B1')

    def _loc_288(): pass

    label('loc_288')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A1',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3B1')

    def _loc_2A1(): pass

    label('loc_2A1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BA',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3B1')

    def _loc_2BA(): pass

    label('loc_2BA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D3',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3B1')

    def _loc_2D3(): pass

    label('loc_2D3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3B1')

    def _loc_2EC(): pass

    label('loc_2EC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_305',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3B1')

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3B1')

    def _loc_31E(): pass

    label('loc_31E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_337',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3B1')

    def _loc_337(): pass

    label('loc_337')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_350',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3B1')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_369',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3B1')

    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_382',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3B1')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3B1')

    def _loc_39B(): pass

    label('loc_39B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B1',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3B1(): pass

    label('loc_3B1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3B1')

    def _loc_3C6(): pass

    label('loc_3C6')

    Return()

# id: 0x0003 offset: 0x3C7
@scena.Code('func_03_3C7')
def func_03_3C7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_3D4',
    )

    Jump('loc_53B')

    def _loc_3D4(): pass

    label('loc_3D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3DE',
    )

    Jump('loc_53B')

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_3E8',
    )

    Jump('loc_53B')

    def _loc_3E8(): pass

    label('loc_3E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_444',
    )

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

    Jump('loc_53B')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_44E',
    )

    Jump('loc_53B')

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_53B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_496',
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

    Jump('loc_53B')

    def _loc_496(): pass

    label('loc_496')

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

    def _loc_53B(): pass

    label('loc_53B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x53F
@scena.Code('func_04_53F')
def func_04_53F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_61E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5AC',
    )

    ChrTalk(
        0x0008,
        (
            '#0650140664V#710F在诞辰庆典上玩累了吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140663V如果有什么难处，\n',
            '尽管告诉我就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61B')

    def _loc_5AC(): pass

    label('loc_5AC')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0650140661V#710F艾丝蒂尔。',
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

    def _loc_61B(): pass

    label('loc_61B')

    Jump('loc_7DF')

    def _loc_61E(): pass

    label('loc_61E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_719',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_690',
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

    Jump('loc_716')

    def _loc_690(): pass

    label('loc_690')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0650140656V#711F啊，\n',
            '你们两个打算出去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140657V因为诞辰庆典，\n',
            '现在王都变得很热闹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650140658V你们就去好好玩玩吧，\n',
            '要注意安全哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_716(): pass

    label('loc_716')

    Jump('loc_7DF')

    def _loc_719(): pass

    label('loc_719')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_723',
    )

    Jump('loc_7DF')

    def _loc_723(): pass

    label('loc_723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_72D',
    )

    Jump('loc_7DF')

    def _loc_72D(): pass

    label('loc_72D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_737',
    )

    Jump('loc_7DF')

    def _loc_737(): pass

    label('loc_737')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_7DF',
    )

    ChrTalk(
        0x0008,
        (
            '#710F是问晚宴吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120561V因为料理还在准备，\n',
            '请再稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F料理准备完毕之后，\n',
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

    def _loc_7DF(): pass

    label('loc_7DF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x7E3
@scena.Code('func_05_7E3')
def func_05_7E3():
    EventBegin(0x00)
    CameraMove(62970, 640, 71000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 64390, 0, 71030, 270)
    SetChrPos(0x0101, 61580, 0, 71540, 90)
    SetChrPos(0x0102, 61580, 0, 70620, 90)

    ChrTalk(
        0x0008,
        (
            '#710F……你们要说的我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120536V想要把拉赛尔博士的传话\n',
            '直接的告诉女王陛下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就是这件事对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F对……就是这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120539V如果女王陛下真的是身体不适，\n',
            '我们就重新再考虑一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F那并不是主要的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860002V女王宫正处于刚才那些特务兵\n',
            '的２４小时监控状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860003V能够进去的只有公爵大人和上校，\n',
            '以及在女王身边照料她的\n',
            '我和侍女们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这么说来，想要去见女王\n',
            '果真是非常困难的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F怎么办，艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120545V只有把博士的传话让\n',
            '希尔丹夫人转达这个办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔～嗯，可是还是\n',
            '直接去和女王谈谈更好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120547V杜南公爵的目的\n',
            '和理查德上校的企图……',
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
            '#710F……艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我已经有些打算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120551V晚宴结束之后\n',
            '你们再来这里一趟可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦，这么说来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们和女王见面的\n',
            '方法已经有了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F这样认为也是可以的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120555V虽然可能比较困难……\n',
            '但还是有试一试的价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120556V因为还要做一些准备的缘故，\n',
            '请等到晚宴结束，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F好～的，太幸运了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120558V#010F明白了。\n',
            '晚宴一结束就来向您请教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F我会等候你们的到来的。',
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
        'loc_CDC',
    )

    ChrTalk(
        0x0008,
        (
            '#710F啊，说到晚宴的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120561V因为料理还在准备，\n',
            '请再稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D40')

    def _loc_CDC(): pass

    label('loc_CDC')

    ChrTalk(
        0x0008,
        (
            '#710F料理准备完毕之后，\n',
            '晚宴就会立刻开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120564V先回房间休息一下\n',
            '也许是个不错的选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0049, 0x01, 0x0800)

    def _loc_D40(): pass

    label('loc_D40')

    Sleep(300)

    Fade(1000)
    SetChrPos(0x0101, 62550, 0, 68550, 45)
    SetChrPos(0x0102, 62550, 0, 68550, 45)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xD6F
@scena.Code('func_06_D6F')
def func_06_D6F():
    EventBegin(0x00)
    CameraMove(67590, 0, 65319, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 70120, 0, 69770, 225)
    SetChrPos(0x0101, 66580, 0, 64769, 45)
    SetChrPos(0x0102, 67630, 0, 64590, 45)

    @scena.Lambda('lambda_0DC0')
    def lambda_0DC0():
        CameraMove(69520, 0, 68800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DC0)

    @scena.Lambda('lambda_0DD8')
    def lambda_0DD8():
        ChrWalkTo(0x00FE, 68460, 0, 68580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DD8)

    @scena.Lambda('lambda_0DF3')
    def lambda_0DF3():
        ChrWalkTo(0x00FE, 69950, 0, 67930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0DF3)

    WaitForThreadExit(0x0102, 0x0002)
    ChrTurnDirection(0x0102, 0x0008, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0650860004V料理还在准备中，\n',
            '请稍等片刻。',
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
            '#000F这个……对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120939V不巧被理查德上校\n',
            '抓住了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F上校……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120941V#010F只是谈了谈关于我们\n',
            '父亲过去的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120942V与这边的行动无关，\n',
            '请不用在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860005V根据介绍信来看，\n',
            '你们两位是卡西乌斯先生\n',
            '的孩子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120945V理查德上校\n',
            '会有一些感慨也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F请问，希尔丹夫人也\n',
            '知道父亲的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F曾经作为摩尔根将军副官\n',
            '的他经常到王城这里来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120948V是去世的王子……陛下的儿子\n',
            '以前的学友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F去世的王子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F就是科洛蒂亚公主\n',
            '的父亲大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F嗯，因为１５年前的海难事故\n',
            '而不幸身亡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120952V倘若王子还活着的话，\n',
            '现在这样的局面是\n',
            '不会发生的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F……对于已经发生的事情，\n',
            '后悔是没有用处的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '夜色已晚，\n',
            '这就准备出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '茜亚，过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 69050, 0, 75720, 180)

    @scena.Lambda('lambda_116D')
    def lambda_116D():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_116D)

    @scena.Lambda('lambda_117B')
    def lambda_117B():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_117B)

    @scena.Lambda('lambda_1189')
    def lambda_1189():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1189)

    Sleep(300)

    @scena.Lambda('lambda_119C')
    def lambda_119C():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_119C')

    DispatchAsync2(0x0009, 0x0001, lambda_119C)

    @scena.Lambda('lambda_11AD')
    def lambda_11AD():
        ChrWalkTo(0x00FE, 68810, 0, 70320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_11AD)

    @scena.Lambda('lambda_11C8')
    def lambda_11C8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_11C8')

    DispatchAsync2(0x0008, 0x0001, lambda_11C8)

    @scena.Lambda('lambda_11D9')
    def lambda_11D9():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_11D9')

    DispatchAsync2(0x0101, 0x0001, lambda_11D9)

    @scena.Lambda('lambda_11EA')
    def lambda_11EA():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_11EA')

    DispatchAsync2(0x0102, 0x0001, lambda_11EA)

    CameraMove(70030, 0, 70300, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F咦，你不是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120958V#010F您是茜亚小姐\n',
            '对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你、你们好……\n',
            '艾丝蒂尔小姐，约修亚先生，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '事情我已经知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F这个孩子\n',
            '你们完全可以相信她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860006V公主殿下在城里的时候，\n',
            '就是由这位侍女照顾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F公主殿下……\n',
            '就是科洛蒂亚公主吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这样的话就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '谢、谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么这就把准备好的制服\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '丝带呀头饰呀那些\n',
            '细小的方面我都已经\n',
            '准备完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这么说……难道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#710F是啊，艾丝蒂尔如果\n',
            '装扮成侍女的样子\n',
            '就可以进入女王宫了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120971V在把头发的样式改变一下，\n',
            '看守也就觉察不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F原～来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120973V#010F的确，制服可以很好\n',
            '将个人特点隐藏起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120974V用于潜入\n',
            '就再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊～侍女的服饰啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120976V看到过莉拉小姐的着装，\n',
            '觉得很不错呢。',
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
            '嘻嘻，如果行动不方便\n',
            '那扫除的时候就麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，果然是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那就立刻穿上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F很开心嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '蹦蹦跳跳的虽然是可以，\n',
            '但不要在陛下面前失礼哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120983V这次我是\n',
            '不能和你一起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎？为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120985V约修亚也换装不就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1693')
    def lambda_1693():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1693)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#710F你说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚你在学院祭的舞台剧\n',
            '中扮演的公主不是很合适的吗？',
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
            '#010F这、这可不是在演戏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120991V和女王陛下见面时\n',
            '却穿的女装，这有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F没关系，没关系。\n',
            '一点都不难看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120993V当时约修亚装扮的公主\n',
            '可是非常美丽哟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F又、又来了……别开玩笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '希尔丹夫人你们\n',
            '怎么说我就怎么做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1811')
    def lambda_1811():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1811)

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#710F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '………………………………',
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
            '#010F我、我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F原来如此……\n',
            '好像的确没有什么问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '茜亚，为公主殿下准备的\n',
            '假发还在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是、是的……\n',
            '一次都没有使用过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果是长长的黑发，\n',
            '和约修亚公子是很配的哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我、我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F就这样，３比１多数取胜，\n',
            '最终的结果出现⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那就请到这边来。\n',
            '更衣室已经准备好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_19BF')
    def lambda_19BF():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_19BF')

    DispatchAsync2(0x0008, 0x0001, lambda_19BF)

    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_19E4')
    def lambda_19E4():
        ChrWalkTo(0x00FE, 68680, 0, 77130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_19E4)

    Sleep(300)

    ChrWalkTo(0x0101, 69620, 0, 68330, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#010F请等一下！\n',
            '我换衣服这件事怎么一句话就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 69610, 0, 67850, 2000, 0x00)
    SetChrDirection(0x0102, 180, 400)

    @scena.Lambda('lambda_1A67')
    def lambda_1A67():
        CameraMove(69970, 0, 72360, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A67)

    @scena.Lambda('lambda_1A7F')
    def lambda_1A7F():
        ChrWalkTo(0x00FE, 68680, 0, 77130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A7F)

    @scena.Lambda('lambda_1A9A')
    def lambda_1A9A():
        ChrMoveTo(0x00FE, 68680, 0, 77130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1A9A)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    ChrTalk(
        0x0102,
        (
            '#010F我知道，我知道的啊……\n',
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
            '#710F呼……\n',
            '现在的年轻人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(69200, 0, 72370, 0)
    SetChrPos(0x0008, 68890, 0, 69520, 0)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0101, 2)
    SetChrChipByIndex(0x0102, 3)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1BA9')
    def lambda_1BA9():
        ChrWalkTo(0x00FE, 69730, 0, 71410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1BA9)

    Sleep(600)

    @scena.Lambda('lambda_1BC9')
    def lambda_1BC9():
        ChrWalkTo(0x00FE, 69120, 0, 73080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1BC9)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_1BE9')
    def lambda_1BE9():
        ChrWalkTo(0x00FE, 67850, 0, 73240, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1BE9)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_1C09')
    def lambda_1C09():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1C09)

    ChrTalk(
        0x0008,
        (
            '#710F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 317, 400)
    SetChrDirection(0x0101, 75, 400)
    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#000F您～好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，怎么样－呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121013V嘿嘿嘿……\n',
            '非常合适呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F刚到城里不久，\n',
            '活泼开郎的实习侍女……\n',
            '这种说法十分有说服力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121015V头发也批下来之后，\n',
            '就更不容易被注意到了。',
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
            '#000F游、游击士那边还有任务，\n',
            '所以这个就……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F喂喂，约修亚。\n',
            '快点出来吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D9C')
    def lambda_1D9C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D9C)

    @scena.Lambda('lambda_1DAA')
    def lambda_1DAA():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1DAA)

    CameraMove(69080, 0, 73680, 1000)

    ChrTalk(
        0x0102,
        (
            '#010F啊……',
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
            '#000F不－行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121023V再喋喋不休的话\n',
            '我就去把你拖出来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121025V唉，没办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E62')
    def lambda_1E62():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1E62')

    DispatchAsync2(0x0009, 0x0001, lambda_1E62)

    @scena.Lambda('lambda_1E73')
    def lambda_1E73():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1E73')

    DispatchAsync2(0x0008, 0x0001, lambda_1E73)

    @scena.Lambda('lambda_1E84')
    def lambda_1E84():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1E84')

    DispatchAsync2(0x0101, 0x0001, lambda_1E84)

    ChrWalkTo(0x0102, 69050, 0, 73160, 1000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#010F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F这竟然会……\n',
            '相称的到了可怕的程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F怎么样，我说过的吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是的，竟然比身为\n',
            '女子的我还要有形，\n',
            '这到底是怎－么回事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121030V嘿嘿嘿……\n',
            '我还为他好好的化了妆的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好了……\n',
            '请不要再说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(68990, 0, 71660, 1000)

    @scena.Lambda('lambda_1FC0')
    def lambda_1FC0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FC0)

    @scena.Lambda('lambda_1FCE')
    def lambda_1FCE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FCE)

    ChrTalk(
        0x0008,
        (
            '#0650121032V#710F嗯……\n',
            '准备完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121033V那么我现在就\n',
            '带领你们去女王宫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121034V彻底的把自己当成\n',
            '实习侍女，这一点要记住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，好的，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唔……\n',
            '终于要见到女王了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……到了关键时刻了。',
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
            '#000F噗哧，你这身打扮配合这样\n',
            '严肃的话真是天衣无缝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 800)

    ChrTalk(
        0x0102,
        (
            '#010F太、太坏了！\n',
            '什么天衣无缝！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我都打扮成这副\n',
            '模样了，你还取笑我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F对不起对不起，\n',
            '不要那么倔犟嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121043V下次我请你吃冰淇淋\n',
            '消消气哈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哼，我又不像你，\n',
            '用吃的是不能收买我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我、我什么时候\n',
            '被吃的给收买过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121046V嘿嘿嘿……\n',
            '真是一对好伙伴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#710F时间快来不及了……\n',
            '立刻前往女王宫吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004A, 0x01, 0x0020)
    OP_28(0x004A, 0x01, 0x0040)
    SetChrFlags(0x0008, 0x0040)

    @scena.Lambda('lambda_2292')
    def lambda_2292():
        OP_92(0x00FE, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2292)

    EventEnd(0x00)
    FormationAddMember(0x37, 0xFF)
    SetChrChipByIndex(0x0000, 0)
    SetChrChipByIndex(0x0001, 2)
    SetChrChipByIndex(0x0138, 3)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)
    SetChrFlags(0x0008, 0x0080)

    Return()

# id: 0x0007 offset: 0x22CA
@scena.Code('func_07_22CA')
def func_07_22CA():
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(68370, 0, 69650, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 68920, 0, 70070, 180)
    SetChrPos(0x0009, 67750, 0, 70350, 180)
    FormationDelMember(0x37, 0xFF)
    SetChrPos(0x0101, 67080, 0, 68350, 0)
    SetChrPos(0x0102, 68360, 0, 68190, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#000F希尔丹夫人，茜亚小姐，\n',
            '真是太感谢你们了！',
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
            '#710F哪里，这是为陛下服务\n',
            '的人理所当然的义务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121470V陛下委托的任务\n',
            '无论如何拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121471V那、那个……\n',
            '我也要拜托你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121472V请一定替我们……\n',
            '把公主殿下救出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，茜亚小姐\n',
            '服侍过公主殿下的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121474V是、是的……\n',
            '虽然能够照顾她的\n',
            '机会并不多，很遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121475V但是她把我这种下人\n',
            '当作朋友一样对待，\n',
            '是一个平易近人而又温柔的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300121476V当听说她被\n',
            '囚禁了的时候，\n',
            '我每天都担心的睡不着觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……\n',
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
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
