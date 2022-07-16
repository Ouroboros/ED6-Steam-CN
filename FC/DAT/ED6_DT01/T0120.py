import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0120   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '佛莱迪'),
    TXT(0x02, '梅尔达斯'),
    TXT(0x03, '埃尔格'),
    TXT(0x04, '斯蒂娜'),
    TXT(0x05, '雪拉扎德'),
    TXT(0x06, '朵洛希'),
    TXT(0x07, '目标用摄像机'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0120.x'
    header.mapIndex       = 4
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0120._SN', 'ED6_DT01/T0120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7C01
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFF67A8,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFF060,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 4,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFF67A8,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFEC78,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 6,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFF5808,
            dword_04        = 0x00000000,
            dword_08        = 0x000007D0,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 6,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFF6F78,
            dword_04        = 0x00000000,
            dword_08        = 0x000101D0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 4,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0x174
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
    ]

# id: 0x10002 offset: 0x1A6
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -38180,
            z                   = 0,
            y                   = -497,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -39499,
            z                   = 0,
            y                   = 678,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -36678,
            z                   = 0,
            y                   = 73751,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -86132,
            z                   = 0,
            y                   = 71210,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 200,
            z                   = 0,
            y                   = 74200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -44500,
            z                   = 0,
            y                   = -360,
            direction           = 279,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x286
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x286
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -41900,
            y           = 0,
            z           = 1877,
            range       = -44000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x000010A4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -37700,
            y           = 0,
            z           = -5500,
            range       = -40500,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFFDF76,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
    )

# id: 0x10005 offset: 0x2C6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -38537,
            triggerZ            = 0,
            triggerY            = -1845,
            triggerRange        = 400,
            actorX              = -38180,
            actorZ              = 1500,
            actorY              = -497,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -41599,
            triggerZ            = 0,
            triggerY            = 299,
            triggerRange        = 1000,
            actorX              = -39499,
            actorZ              = 1500,
            actorY              = 678,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -36170,
            triggerZ            = 0,
            triggerY            = 71651,
            triggerRange        = 1000,
            actorX              = -36678,
            actorZ              = 1500,
            actorY              = 73751,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x332
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_340',
    )

    SetChrDirection(0x0009, 90, 0)

    def _loc_340(): pass

    label('loc_340')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_350'),
        (0x00000066, 'loc_363'),
        (-1, 'loc_376'),
    )

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x000A, 0x00, 0x02)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_363',
    )

    Event(0, 0x000F)

    def _loc_363(): pass

    label('loc_363')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_373',
    )

    Event(0, 0x0010)

    def _loc_373(): pass

    label('loc_373')

    Jump('loc_376')

    def _loc_376(): pass

    label('loc_376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_39D',
    )

    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000D, 0x0008)
    SetChrPos(0x000D, -44500, 0, -320, 283)

    def _loc_39D(): pass

    label('loc_39D')

    Return()

# id: 0x0001 offset: 0x39E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B6',
    )

    OP_B1('t0120_y')

    Jump('loc_3BF')

    def _loc_3B6(): pass

    label('loc_3B6')

    OP_B1('t0120_n')

    def _loc_3BF(): pass

    label('loc_3BF')

    Return()

# id: 0x0002 offset: 0x3C0
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3D5(): pass

    label('loc_3D5')

    Return()

# id: 0x0003 offset: 0x3D6
@scena.Code('func_03_3D6')
def func_03_3D6():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x3DB
@scena.Code('func_04_3DB')
def func_04_3DB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 0, 0x228)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_472',
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
        'loc_461',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_44C',
    )

    OP_A9(0x00)

    Jump('loc_45B')

    def _loc_44C(): pass

    label('loc_44C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 6, 0x29E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_459',
    )

    OP_A9(0x09)

    Jump('loc_45B')

    def _loc_459(): pass

    label('loc_459')

    OP_A9(0x70)

    def _loc_45B(): pass

    label('loc_45B')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_461(): pass

    label('loc_461')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_472',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_472(): pass

    label('loc_472')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_554',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_518',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '市长先生委托\n',
            '我们加工的七耀石\n',
            '终于送到工房这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我还是第一次见到\n',
            '这么漂亮的翠耀石呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在父亲正在\n',
            '对那块翠耀石进行加工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_551')

    def _loc_518(): pass

    label('loc_518')

    ChrTalk(
        0x0008,
        (
            '要制造七耀石的工艺品，\n',
            '这种活儿也只有父亲才能胜任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_551(): pass

    label('loc_551')

    Jump('loc_134F')

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_579',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))
    Call(1, 0x0003)

    Jump('loc_134F')

    def _loc_579(): pass

    label('loc_579')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_652',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5FF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '虽然市长先生委托\n',
            '我们加工七耀石……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但最关键的翠耀石\n',
            '却到现在还没有送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是不是出什么事了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64F')

    def _loc_5FF(): pass

    label('loc_5FF')

    ChrTalk(
        0x0008,
        (
            '市长先生委托\n',
            '我们加工七耀石……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但最关键的翠耀石\n',
            '却到现在还没有送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64F(): pass

    label('loc_64F')

    Jump('loc_134F')

    def _loc_652(): pass

    label('loc_652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_738',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '市长先生委托\n',
            '我们加工七耀石。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在还没送来，\n',
            '不过听说是极品的翠耀石。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不知道是什么样的东西呢，\n',
            '有点期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_735')

    def _loc_6E5(): pass

    label('loc_6E5')

    ChrTalk(
        0x0008,
        (
            '市长先生委托\n',
            '我们加工七耀石。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在还没送来，\n',
            '不过听说是极品的翠耀石。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_735(): pass

    label('loc_735')

    Jump('loc_134F')

    def _loc_738(): pass

    label('loc_738')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_9AA',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Return,
        ),
        'loc_89F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0008, 0x0110, 400)

    ChrTalk(
        0x0008,
        (
            '朵洛希小姐的相机是最新款的，\n',
            '货色相当不错的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过那是专业型的，\n',
            '不是两三下就能\n',
            '操作的东西吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#150F呵呵呵，\n',
            '你是说这小不点么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '小、小不点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#151F它是个好孩子，\n',
            '很听话的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哦、哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#145F认认真真听这家伙说话\n',
            '纯粹只是白费力气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89C')

    def _loc_86B(): pass

    label('loc_86B')

    ChrTalk(
        0x0008,
        (
            '哈哈，生意做久了\n',
            '就会碰到各种各样的客人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89C(): pass

    label('loc_89C')

    Jump('loc_9A7')

    def _loc_89F(): pass

    label('loc_89F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_936',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '矿山的新矿脉中\n',
            '好像发现了巨大的七耀石呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这种等级的东西\n',
            '想必应该非常昂贵，\n',
            '不过听说很快就找到买主了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不知道是谁买的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A7')

    def _loc_936(): pass

    label('loc_936')

    ChrTalk(
        0x0008,
        (
            '矿山的新矿脉中\n',
            '好像发现了巨大的七耀石呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这种等级的东西\n',
            '想必应该非常昂贵，\n',
            '不过听说很快就找到买主了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A7(): pass

    label('loc_9A7')

    Jump('loc_134F')

    def _loc_9AA(): pass

    label('loc_9AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_B66',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_A4E',
    )

    ChrTalk(
        0x0008,
        (
            '啊，是你们两个。\n',
            '路灯的修理辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有什么关于导力器的问题的话\n',
            '就随时找我来谈好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以后我们工房的生意\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B63')

    def _loc_A4E(): pass

    label('loc_A4E')

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x40)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A6B',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))
    Call(1, 0x0000)

    Jump('loc_B63')

    def _loc_A6B(): pass

    label('loc_A6B')

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B03',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '导力器的运用\n',
            '都掌握得差不多了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想使用新的结晶回路，\n',
            '改造这个步骤是必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想改造的时候，\n',
            '你们来这里找我就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B63')

    def _loc_B03(): pass

    label('loc_B03')

    ChrTalk(
        0x0008,
        (
            '想使用新的结晶回路，\n',
            '改造这个步骤是必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想改造的时候，\n',
            '你们来这里找我就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B63(): pass

    label('loc_B63')

    Jump('loc_134F')

    def _loc_B66(): pass

    label('loc_B66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_BE1',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    ChrTalk(
        0x0008,
        (
            '从柏斯飞往王都的定期船\n',
            '似乎已经到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过今天反正也没采购什么东西，\n',
            '就在店里好好地集中精神工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134F')

    def _loc_BE1(): pass

    label('loc_BE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_CFE',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C99',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '要想成为一流的游击士，\n',
            '就必须娴熟细致\n',
            '使用导力魔法才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这个小店常常有\n',
            '各种不同的游击士光顾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们看看自己的导力器，\n',
            '仔细考虑一下该怎么改造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CFB')

    def _loc_C99(): pass

    label('loc_C99')

    ChrTalk(
        0x0008,
        (
            '这个小店常常有\n',
            '各种不同的游击士光顾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们看看自己的导力器，\n',
            '仔细考虑一下该怎么改造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CFB(): pass

    label('loc_CFB')

    Jump('loc_134F')

    def _loc_CFE(): pass

    label('loc_CFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_F66',
    )

    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 2, 0x2A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1C',
    )

    SetScenaFlags(ScenaFlag(0x0054, 2, 0x2A2))

    ChrTalk(
        0x0008,
        (
            '是你们啊，研修辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……哦！你们胸前那枚徽章是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '恭喜你们俩！\n',
            '终于成为游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F哈哈哈，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F艾丝蒂尔从刚才开始\n',
            '就一直高兴得像要飞上天了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#001F约修亚真是够古板的，开心些不好吗？\n',
            '我们可是很辛苦才得到这成绩呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#502F不过今天我很高兴，就不和你计较这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#017F唉，真拿她没办法啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 500)

    ChrTalk(
        0x0008,
        (
            '既然成为游击士了，那就要克服\n',
            '不擅长导力魔法这一点才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈哈～\n',
            '以后我们工房的生意\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_F63')

    def _loc_F1C(): pass

    label('loc_F1C')

    ChrTalk(
        0x0008,
        (
            '两位游击士新人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以后我们工房的生意\n',
            '还要请你们多多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_F63(): pass

    label('loc_F63')

    Jump('loc_134F')

    def _loc_F66(): pass

    label('loc_F66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_FCB',
    )

    ChrTalk(
        0x0008,
        (
            '你们研修要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果要改造导力器的话，\n',
            '在菜单上选择『改造·换钱』就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134F')

    def _loc_FCB(): pass

    label('loc_FCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 0, 0x228)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12DD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0041, 5, 0x20D))
    SetScenaFlags(ScenaFlag(0x0045, 0, 0x228))

    ChrTalk(
        0x0008,
        (
            '哟，\n',
            '原来是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '之前调整了导力器\n',
            '现在使用起来习惯吗？\n',
            '我想对你们来说应该不难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#017F对艾丝蒂尔来说，\n',
            '比起导力器的好坏问题，\n',
            '还是使用方法比较让她难懂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#017F不管讲解得怎样通俗易懂，\n',
            '她理解起来总是会有困难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F同样要领悟一点，\n',
            '就要比别人多花几倍精力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#002F哼，不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '没关系啦，\n',
            '一开始谁都会有些困惑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过一旦掌握了诀窍，\n',
            '就可以很快精通了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F对呀，就是嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F只要等我习惯之后，\n',
            '就可以比约修亚运用得更加娴熟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在我刚进蔡斯的\n',
            '中央工房的时候\n',
            '也是完全不会使用导力器的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 500)

    ChrTalk(
        0x0101,
        (
            '#004F佛莱迪先生以前也是那样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是啊，不断使用不断熟悉，\n',
            '现在连技术师也当上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔也要以\n',
            '游击士为目标而努力加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_134F')

    def _loc_12DD(): pass

    label('loc_12DD')

    ChrTalk(
        0x0008,
        (
            '对于战术导力器的运用\n',
            '一开始谁都会有些困惑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过一旦掌握了诀窍，\n',
            '对于艾丝蒂尔来说肯定可以很快精通的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_134F(): pass

    label('loc_134F')

    OP_56(0x00)
    TalkEnd(0x0008)
    Sleep(300)

    Return()

# id: 0x0005 offset: 0x135A
@scena.Code('func_05_135A')
def func_05_135A():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x135F
@scena.Code('func_06_135F')
def func_06_135F():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1450',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1418',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '市长的七耀石\n',
            '终于送过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这可是一块不得了的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而且听说还是\n',
            '送给女王陛下的生日礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好久都没做工艺品的加工了，\n',
            '我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144D')

    def _loc_1418(): pass

    label('loc_1418')

    ChrTalk(
        0x0009,
        (
            '要完成这种活儿，\n',
            '暂时还不能交给佛莱迪单独去做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_144D(): pass

    label('loc_144D')

    Jump('loc_1F66')

    def _loc_1450(): pass

    label('loc_1450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1541',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '我们从市长那里\n',
            '接了一份活儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但都已经过了约好的时间了，\n',
            '他却还没把东西送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他应该向来\n',
            '都是遵守时间的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_153E')

    def _loc_14E4(): pass

    label('loc_14E4')

    ChrTalk(
        0x0009,
        (
            '我们从市长那里\n',
            '接了一份活儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但都已经过了约好的时间了，\n',
            '他却还没把东西送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_153E(): pass

    label('loc_153E')

    Jump('loc_1F66')

    def _loc_1541(): pass

    label('loc_1541')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1641',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15D5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '导力器似乎是\n',
            '以远古时期的工具\n',
            '为参考而发明出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也就是说了不起的不是现代人，\n',
            '而是古代人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真有点不甘心哪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_163E')

    def _loc_15D5(): pass

    label('loc_15D5')

    ChrTalk(
        0x0009,
        (
            '导力器似乎是\n',
            '以远古时期的工具\n',
            '为参考而发明出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也就是说了不起的不是现代人，\n',
            '而是古代人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_163E(): pass

    label('loc_163E')

    Jump('loc_1F66')

    def _loc_1641(): pass

    label('loc_1641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1782',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 3, 0x253)),
            Expr.Return,
        ),
        'loc_168D',
    )

    ChrTalk(
        0x0009,
        (
            '真是的，佛莱迪也\n',
            '在那里喳喳呼呼的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真不像话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_177F')

    def _loc_168D(): pass

    label('loc_168D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_171F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '刚才我看见了市长，\n',
            '他看上去出奇地心神不定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的， \n',
            '他一直都是个不够沉着的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '身为市长应该\n',
            '表现得更沉稳一些嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_177F')

    def _loc_171F(): pass

    label('loc_171F')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '刚才我看见了市长，\n',
            '他看上去出奇地心神不定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的， \n',
            '他一直都是个不够沉着的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_177F(): pass

    label('loc_177F')

    Jump('loc_1F66')

    def _loc_1782(): pass

    label('loc_1782')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1884',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1838',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '听说飞艇上都装有\n',
            '一种叫做导力引擎的巨型机械。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那是一种利用了\n',
            '导力器原理制成的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '全都是蔡斯的伟大学者们\n',
            '开发出来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哎？扯得没边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1881')

    def _loc_1838(): pass

    label('loc_1838')

    ChrTalk(
        0x0009,
        (
            '听说飞艇上都装有\n',
            '一种叫做导力引擎的巨型机械。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哎？扯得没边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1881(): pass

    label('loc_1881')

    Jump('loc_1F66')

    def _loc_1884(): pass

    label('loc_1884')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_197A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1936',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '是艾丝蒂尔和约修亚啊。\n',
            '可别妨碍我们工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……不过你们也已经不是那种爱捣乱的年纪了。\n',
            '都已经成了游击士了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真了不起呢，\n',
            '让人刮目相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1977')

    def _loc_1936(): pass

    label('loc_1936')

    ChrTalk(
        0x0009,
        (
            '都已经成了游击士了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真了不起呢，\n',
            '让人刮目相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1977(): pass

    label('loc_1977')

    Jump('loc_1F66')

    def _loc_197A(): pass

    label('loc_197A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_19E5',
    )

    ChrTalk(
        0x0009,
        (
            '哦，到时间了，\n',
            '差不多该关门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们俩也不要\n',
            '在这里晃来晃去的了，\n',
            '早点回去吧，回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F66')

    def _loc_19E5(): pass

    label('loc_19E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1B29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AC1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '现在的导力器\n',
            '都是以钟表的结构而制成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以老一辈的技术人员\n',
            '还是可以摆弄一下它们的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我可是非常\n',
            '精通结晶回路的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也不知道这东西是\n',
            '哪里的什么人发明的，\n',
            '真是个很复杂的机械啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B26')

    def _loc_1AC1(): pass

    label('loc_1AC1')

    ChrTalk(
        0x0009,
        (
            '我可是非常\n',
            '精通结晶回路的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '也不知道这东西是\n',
            '哪里的什么人发明的，\n',
            '真是个很复杂的机械啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B26(): pass

    label('loc_1B26')

    Jump('loc_1F66')

    def _loc_1B29(): pass

    label('loc_1B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1B76',
    )

    ChrTalk(
        0x0009,
        (
            '哦，研修辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要使用工房的话，\n',
            '和佛莱迪说一声就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F66')

    def _loc_1B76(): pass

    label('loc_1B76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EBB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '喂！现在还没有开始营业呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……哦，原来是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '今天怎么这么早啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F早上好，\n',
            '梅尔达斯爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 500)

    ChrTalk(
        0x0102,
        (
            '#010F早上好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F不久之前您帮我们\n',
            '修理了家外面的导力灯，\n',
            '真是太感谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们家外面的导力灯坏了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F导力器果然是日常生活中\n',
            '不可缺少的必需品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……想当年我们\n',
            '这一代还小的时候，\n',
            '哪里有这样的导力器卖啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到了现在什么灯呀火呀\n',
            '简简单单地就点着了，\n',
            '天上还有飞艇在到处乱飞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是让人觉得不习惯啊，\n',
            '是不是有些方便得过头了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#007F（糟糕……\n',
            '　又开始说个不停了。）',
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
            '#017F（……谁叫你刚才\n',
            '　说了多余的话啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们年轻的时候拼死拼活，\n',
            '流血流汗地让今天的一切得以实现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而现在的年轻人根本就不愿意去做\n',
            '稍微有一点辛苦的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#008F哈～哈哈～说、说得对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F66')

    def _loc_1EBB(): pass

    label('loc_1EBB')

    ChrTalk(
        0x0009,
        (
            '因为导力器带来的便利，年轻一代\n',
            '连稍微辛苦一点的事情都不愿去做，\n',
            '我真有些为他们感到担忧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我说得对吗，艾丝蒂尔、约修亚。\n',
            '不要忘记要用你们自己的双手去开拓未来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F66(): pass

    label('loc_1F66')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1F6A
@scena.Code('func_07_1F6A')
def func_07_1F6A():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x1F6F
@scena.Code('func_08_1F6F')
def func_08_1F6F():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0044, 6, 0x226)),
            Expr.Return,
        ),
        'loc_1FE5',
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
        'loc_1FD4',
    )

    OP_0D()
    OP_A9(0x01)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_1FD4(): pass

    label('loc_1FD4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FE5',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_1FE5(): pass

    label('loc_1FE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_2251',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哟，是约修亚和艾丝蒂尔啊。\n',
            '怎么了？两个人都拿着行李。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '向埃尔格说明了事情的来龙去脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '卡西乌斯他……！？\n',
            '所以你们就要去柏斯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过没想到\n',
            '那家伙坐的那艘飞艇会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊，我们已经决定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F所以呢，\n',
            '我们打算去柏斯那里调查一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呆在这里什么都不做\n',
            '也的确不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '原来如此啊。\n',
            '这样做才像你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '也好，\n',
            '雪拉扎德和你们一起的话我也就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之你们一路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，那我们出发了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_224E')

    def _loc_21F8(): pass

    label('loc_21F8')

    ChrTalk(
        0x000A,
        (
            '对了，你们的事情\n',
            '还是由我来和斯蒂娜说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '要不然她又会\n',
            '放心不下唠唠叨叨的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_224E(): pass

    label('loc_224E')

    Jump('loc_3681')

    def _loc_2251(): pass

    label('loc_2251')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_23EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_239C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '啊，艾丝蒂尔和约修亚，\n',
            '……雪拉扎德也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F我们正好一起工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是吗，\n',
            '我这里本来预定进新鞭子的，\n',
            '不凑巧到现在还没送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……说起来雪拉姐\n',
            '在训练的时候也用剑的，\n',
            '为什么工作时候用鞭子呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F是啊……\n',
            '从小时候起\n',
            '我就比较习惯用近身武器啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F（……鞭子是近身武器？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23E8')

    def _loc_239C(): pass

    label('loc_239C')

    ChrTalk(
        0x000A,
        (
            '工作前要好好地\n',
            '检查自己的装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，我想这个\n',
            '应该不需要我说了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23E8(): pass

    label('loc_23E8')

    Jump('loc_3681')

    def _loc_23EB(): pass

    label('loc_23EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_24B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2478',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哟，我听说\n',
            '你们两个很活跃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好像解决了\n',
            '一个又一个的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，\n',
            '你已经从我这里的打工锻炼出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B6')

    def _loc_2478(): pass

    label('loc_2478')

    ChrTalk(
        0x000A,
        (
            '卡西乌斯也好，\n',
            '雪拉扎德也好，\n',
            '洛连特的游击士就是很优秀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24B6(): pass

    label('loc_24B6')

    Jump('loc_3681')

    def _loc_24B9(): pass

    label('loc_24B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_25A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_254A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哟，你们两个\n',
            '看起来好像很忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '有空就去见见斯蒂娜，\n',
            '和她聊聊天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不管怎么说，\n',
            '她就是对你们放不下心来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259E')

    def _loc_254A(): pass

    label('loc_254A')

    ChrTalk(
        0x000A,
        (
            '有空就去见见斯蒂娜，\n',
            '和她聊聊天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不管怎么说，\n',
            '她就是对你们放不下心来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_259E(): pass

    label('loc_259E')

    Jump('loc_3681')

    def _loc_25A1(): pass

    label('loc_25A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_277A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_270F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哟，我听说了哦。\n',
            '你们那么快就\n',
            '开始游击士的工作了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '做得怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F还行，总算还应付得来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#502F总之帕赛尔农场的任务\n',
            '算是完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是这样吗……\n',
            '虽说只是暂时顶替卡西乌斯先生，\n',
            '不过你们已经是出色的游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔，可别莽莽撞撞的，\n',
            '老是给约修亚添麻烦可不好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F真是的，大叔干嘛啦，\n',
            '总是只针对我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2777')

    def _loc_270F(): pass

    label('loc_270F')

    ChrTalk(
        0x000A,
        (
            '是吗，你们也已经是\n',
            '出色的游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔，可别莽莽撞撞的，\n',
            '老是给约修亚添麻烦可不好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2777(): pass

    label('loc_2777')

    Jump('loc_3681')

    def _loc_277A(): pass

    label('loc_277A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_2A15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 1, 0x2A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2999',
    )

    SetScenaFlags(ScenaFlag(0x0054, 1, 0x2A1))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哟，新人游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '卡西乌斯这家伙\n',
            '是不是又要出一阵门啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们刚刚去送他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '大叔的消息还真灵通呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，还好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '以前卡西乌斯出门的时候，\n',
            '经常把艾丝蒂尔送到我家托我照看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过自从你来了之后，\n',
            '就一直是你们俩一起看家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '想不到艾丝蒂尔\n',
            '还挺怕寂寞的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '来我家时，\n',
            '刚开始总是像\n',
            '借来的小猫似的老实呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F真是的～大叔。\n',
            '哪儿有这种事嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过过个两三天\n',
            '她就完全放松了，\n',
            '开始吃得好玩得好睡得好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，这个可以想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F哼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A12')

    def _loc_2999(): pass

    label('loc_2999')

    ChrTalk(
        0x000A,
        (
            '卡西乌斯那家伙不在，\n',
            '你们家挺冷清的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们俩现在\n',
            '也可以来我家住哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '用不着客气。\n',
            '我想斯蒂娜也会高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A12(): pass

    label('loc_2A12')

    Jump('loc_3681')

    def _loc_2A15(): pass

    label('loc_2A15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_2E24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 6, 0x20E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0044, 5, 0x225)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2AF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2ABA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '唔，已经到时间了，\n',
            '今天一天的工作还算不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '接下来就该关门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔、约修亚。\n',
            '我很期待你们今后有活跃的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AF4')

    def _loc_2ABA(): pass

    label('loc_2ABA')

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔、约修亚，\n',
            '我很期待你们\n',
            '今后有活跃的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AF4(): pass

    label('loc_2AF4')

    Jump('loc_2E21')

    def _loc_2AF7(): pass

    label('loc_2AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 0, 0x2A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DB7',
    )

    SetScenaFlags(ScenaFlag(0x0054, 0, 0x2A0))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '你们好，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F晚上好～\n',
            '埃尔格大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F晚上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦～对啦，今天不是\n',
            '你们研修的最后一天吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，\n',
            '不久之前你来这里的时候\n',
            '我好像听到你这么说过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那，研修如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '你们胸前那个徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不愧是卡西乌斯的孩子……\n',
            '真是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过我们还处于见习阶段。\n',
            '和前辈比起来还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是这样啊。\n',
            '不过，这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看起来，\n',
            '你以后就不能来这里打工了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F实在很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没事，不要放在心上，\n',
            '之前我就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你对于武器的挑选很有眼光。\n',
            '不能来打工还是让我有些遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是你也有你自己选择的道路。\n',
            '从现在开始你一定要努力，\n',
            '成为一名优秀的游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E21')

    def _loc_2DB7(): pass

    label('loc_2DB7')

    ChrTalk(
        0x000A,
        (
            '约修亚不到我这里来打工\n',
            '虽然让我有些遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过嘛，我以前就知道会这样的，\n',
            '这也是没有办法的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E21(): pass

    label('loc_2E21')

    Jump('loc_3681')

    def _loc_2E24(): pass

    label('loc_2E24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_33DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 6, 0x20E)),
            Expr.Return,
        ),
        'loc_30B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 0, 0x2A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_304A',
    )

    SetScenaFlags(ScenaFlag(0x0054, 0, 0x2A0))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x0101,
        (
            '#001F您好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '课上得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '你们胸前那个徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不愧是卡西乌斯的孩子……\n',
            '真是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过我们还处于见习阶段。\n',
            '和前辈比起来还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是这样啊。\n',
            '不过，这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看起来，\n',
            '你以后就不能来这里打工了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F实在很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没事，不要放在心上，\n',
            '之前我就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你对于武器的挑选很有眼光。\n',
            '不能来打工还是让我有些遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是你也有你自己选择的道路。\n',
            '从现在开始你一定要努力，\n',
            '成为一名优秀的游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30B4')

    def _loc_304A(): pass

    label('loc_304A')

    ChrTalk(
        0x000A,
        (
            '约修亚不到我这里来打工\n',
            '虽然让我有些遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过嘛，我以前就知道会这样的，\n',
            '这也是没有办法的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30B4(): pass

    label('loc_30B4')

    Jump('loc_33D9')

    def _loc_30B7(): pass

    label('loc_30B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0044, 5, 0x225)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_336F',
    )

    SetScenaFlags(ScenaFlag(0x0044, 5, 0x225))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哟，艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F您好啊～\n',
            '埃尔格大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦～对啦，今天不是\n',
            '你们研修的最后一天吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，\n',
            '不久之前你来这里的时候\n',
            '我好像听到你这么说过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那，研修如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '你们胸前那个徽章是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不愧是卡西乌斯的孩子……\n',
            '真是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过我们还处于见习阶段。\n',
            '和前辈比起来还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是这样啊。\n',
            '不过，这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看起来，\n',
            '你以后就不能来这里打工了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F实在很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '没事，不要放在心上，\n',
            '之前我就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你对于武器的挑选很有眼光。\n',
            '不能来打工还是让我有些遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是你也有你自己选择的道路。\n',
            '从现在开始你一定要努力，\n',
            '成为一名优秀的游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33D9')

    def _loc_336F(): pass

    label('loc_336F')

    ChrTalk(
        0x000A,
        (
            '约修亚不到我这里来打工\n',
            '虽然让我有些遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过嘛，我以前就知道会这样的，\n',
            '这也是没有办法的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33D9(): pass

    label('loc_33D9')

    Jump('loc_3681')

    def _loc_33DC(): pass

    label('loc_33DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0044, 6, 0x226)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3619',
    )

    SetScenaFlags(ScenaFlag(0x0041, 6, 0x20E))
    SetScenaFlags(ScenaFlag(0x0044, 6, 0x226))

    ChrTalk(
        0x000A,
        (
            '哦～早上好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F早上好～\n',
            '埃尔格大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天你们怎么来得这么早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦～对啦，今天不是\n',
            '你们研修的最后一天吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，\n',
            '不久之前你来这里的时候\n',
            '我好像听到你这么说过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样啊，\n',
            '约修亚你肯定没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，艾丝蒂尔\n',
            '就让我有些不放心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '从小时候开始\n',
            '就总是冒冒失失的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '她从小时候起\n',
            '就一直是个冒失鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#009F喂～！ 说够了没有！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#009F冒冒失失，冒冒失失，\n',
            '有完没完！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好了，别吵架了，\n',
            '还是早点去游击士协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3681')

    def _loc_3619(): pass

    label('loc_3619')

    ChrTalk(
        0x000A,
        (
            '哎呀～那个不久之前\n',
            '还抓住卡西乌斯裤腿不放的小艾丝蒂尔\n',
            '就要成为游击士了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '岁月真是不饶人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3681(): pass

    label('loc_3681')

    OP_56(0x00)
    TalkEnd(0x000A)
    Sleep(300)

    Return()

# id: 0x0009 offset: 0x368C
@scena.Code('func_09_368C')
def func_09_368C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_3799',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3758',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '哎唷，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，有没有去认真工作呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F（……我们的事\n',
            '　还是不要告诉阿姨比较好吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F（唔……嗯，的确是……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#007F（我怕又会让她哭起来……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3796')

    def _loc_3758(): pass

    label('loc_3758')

    ChrTalk(
        0x00FE,
        (
            '大家，有没有去认真工作呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太蛮干的话可是不行的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3796(): pass

    label('loc_3796')

    Jump('loc_49F5')

    def _loc_3799(): pass

    label('loc_3799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_3993',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 0, 0x2B0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_396B',
    )

    SetScenaFlags(ScenaFlag(0x0056, 0, 0x2B0))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '呀，小雪拉。\n',
            '今天三个人一起？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '今天我们正好一起工作。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，是这样啊……\n',
            '三个人要是能好好合作的话，\n',
            '阿姨我会非常高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，小雪拉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是让艾丝蒂尔和约修亚\n',
            '学坏可不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F真过分呢，阿姨。\n',
            '把人家说得像坏人一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为小雪拉你啊，\n',
            '就算平常是好孩子，\n',
            '坏习惯也是一大堆呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听好了，别教这两个孩子\n',
            '一些奇怪的东西哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我会伤心的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F……好，好，我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3990')

    def _loc_396B(): pass

    label('loc_396B')

    ChrTalk(
        0x00FE,
        (
            '你们也别学\n',
            '小雪拉那些坏习惯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3990(): pass

    label('loc_3990')

    Jump('loc_49F5')

    def _loc_3993(): pass

    label('loc_3993')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_3A8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A3B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '欢迎。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们两个\n',
            '真是血气方刚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我还是希望\n',
            '艾丝蒂尔能够更像女孩子点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F哈哈哈……\n',
            '嗯，我会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A89')

    def _loc_3A3B(): pass

    label('loc_3A3B')

    ChrTalk(
        0x00FE,
        (
            '你们两个\n',
            '真是血气方刚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我还是希望\n',
            '艾丝蒂尔能够更像女孩子点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A89(): pass

    label('loc_3A89')

    Jump('loc_49F5')

    def _loc_3A8C(): pass

    label('loc_3A8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_3BEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 7, 0x2AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BC3',
    )

    SetScenaFlags(ScenaFlag(0x0055, 7, 0x2AF))
    ChrTurnDirection(0x000B, 0x0101, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F怎、怎么啦，阿姨？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我刚洗过脸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔呀，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你看起来长得\n',
            '越来越像莱娜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真、真的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#008F那真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，好怀念呀……\n',
            '让我想起了过去的很多事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE8')

    def _loc_3BC3(): pass

    label('loc_3BC3')

    ChrTalk(
        0x00FE,
        (
            '你们两个可要\n',
            '认认真真地工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BE8(): pass

    label('loc_3BE8')

    Jump('loc_49F5')

    def _loc_3BEB(): pass

    label('loc_3BEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_3E2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 6, 0x2AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DBD',
    )

    SetScenaFlags(ScenaFlag(0x0055, 6, 0x2AE))

    ChrTalk(
        0x00FE,
        (
            '你们俩都要努力啊，\n',
            '要争取让卡西乌斯先生\n',
            '看到好成绩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，太拼命了也不行。\n',
            '最重要的是量力而行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嗯，知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们还是新手，\n',
            '有麻烦的话只管向周围求助，\n',
            '没什么可害羞的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤其是约修亚，\n',
            '你是那种有烦恼也自己一个人扛的类型吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我看来，这最叫人担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#011F对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一点上艾丝蒂尔\n',
            '倒是完全不用操心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#502F就是！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#009F……唔？阿姨您\n',
            '这是夸我还是损我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '不过反正不是什么坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2C')

    def _loc_3DBD(): pass

    label('loc_3DBD')

    ChrTalk(
        0x00FE,
        (
            '你们还是新手，\n',
            '有麻烦的话只管向周围求助，\n',
            '没什么可害羞的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有需要的话，\n',
            '可以随时来找阿姨谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E2C(): pass

    label('loc_3E2C')

    Jump('loc_49F5')

    def _loc_3E2F(): pass

    label('loc_3E2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_3F93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 5, 0x2AD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F1E',
    )

    SetScenaFlags(ScenaFlag(0x0055, 5, 0x2AD))

    ChrTalk(
        0x00FE,
        (
            '欢迎，两位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生\n',
            '要出门一阵是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有用得着的地方\n',
            '就随时向我们开口哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们认识\n',
            '也不是一天两天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太客气的话我可是要生气的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F啊哈哈，\n',
            '谢谢阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F90')

    def _loc_3F1E(): pass

    label('loc_3F1E')

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生\n',
            '要出门一阵是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有用得着的地方\n',
            '就随时向我们开口哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太客气的话我可是要生气的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F90(): pass

    label('loc_3F90')

    Jump('loc_49F5')

    def _loc_3F93(): pass

    label('loc_3F93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_424A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3FD3',
    )

    ChrTalk(
        0x00FE,
        (
            '如果你们有空了，\n',
            '随时都欢迎你们来吃饭哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4247')

    def _loc_3FD3(): pass

    label('loc_3FD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 4, 0x2AC)),
            Expr.Return,
        ),
        'loc_407A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '如果你们有空了，\n',
            '随时都欢迎你们来吃饭哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做游击士很需要体力的，\n',
            '一定要保证营养才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小雪拉也\n',
            '常常到这里吃饭的，\n',
            '要不你们一起过来也行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4247')

    def _loc_407A(): pass

    label('loc_407A')

    SetScenaFlags(ScenaFlag(0x0055, 4, 0x2AC))
    OP_62(0x00FE, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '我马上就开始准备晚餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔你们\n',
            '也一起来吃如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让我好好给你们做一顿饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F啊，今天就算了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么，\n',
            '不喜欢阿姨做的料理吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小时候明明\n',
            '那么喜欢吃的。\n',
            '呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#004F不、不是啦，阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F抱歉，阿姨，\n',
            '因为今天父亲在家里等我们回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卡西乌斯先生一个人在家的话，\n',
            '那也很可怜的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4247(): pass

    label('loc_4247')

    Jump('loc_49F5')

    def _loc_424A(): pass

    label('loc_424A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_44E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 3, 0x2AB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_446D',
    )

    SetScenaFlags(ScenaFlag(0x0055, 3, 0x2AB))

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F阿姨，听我说！听我说！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我终于成为\n',
            '一名游击士了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，真的吗？\n',
            '这么说来约修亚也是了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '呵呵，恭喜！\n',
            '你们俩真不赖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不·过·啊，\n',
            '小艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能因为成为游击士了\n',
            '而高兴过头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这还只是开始而已。\n',
            '以后的路还长着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F嗯、嗯，我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从现在开始\n',
            '你们两个要好好积累\n',
            '作为游击士的经验哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从你们选择了游击士\n',
            '这条道路开始，\n',
            '就要为之感到自豪才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从现在开始就好好努力吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E3')

    def _loc_446D(): pass

    label('loc_446D')

    ChrTalk(
        0x00FE,
        (
            '从现在开始\n',
            '你们两个要好好积累\n',
            '作为游击士的经验哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从你们选择了游击士\n',
            '这条道路开始，\n',
            '就要为之感到自豪才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44E3(): pass

    label('loc_44E3')

    Jump('loc_49F5')

    def _loc_44E6(): pass

    label('loc_44E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 7, 0x20F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_498B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0041, 7, 0x20F))

    ChrTalk(
        0x0101,
        (
            '#000F斯蒂娜阿姨，\n',
            '早上好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊……\n',
            '是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '待会儿还要去做游击士训练吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯。\n',
            '阿姨，您看好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#502F在经过严格的训练之后\n',
            '我一定会成为不输给\n',
            '雪拉姐的女游击士的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵，真让人欣慰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '咦？艾丝蒂尔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F什、什么事？\n',
            '为什么这样盯着人家的脸看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你～洗脸了吗？\n',
            '好好刷牙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你和约修亚不一样，\n',
            '女孩子要懂得礼仪才行哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#008F真是的，\n',
            '阿姨您又老生常谈了啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在我已经不是以前那样啦。\n',
            '是吧，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F对了，说起这个来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#017F你之前不是急急忙忙头发蓬乱地\n',
            '从家里跑出去吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#008F啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0102, 1000)

    ChrTalk(
        0x0101,
        (
            '#008F那、那是因为有很急的事情嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#008F因为那时里农老板的店里\n',
            '进了『斯托雷加』运动鞋的新品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4S艾－丝－蒂－尔！#3S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 800)

    ChrTalk(
        0x000B,
        (
            '你觉得你这么做行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '怎么说你也已经到了要嫁人的年龄了，\n',
            '至少也应该注意一下仪表了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '衣冠不整的话，就算作为一个游击士\n',
            '也不会让别人觉得可靠，你说是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且衣冠整齐也是\n',
            '精神状态良好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F好、好的，\n',
            '我会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '这才对嘛，\n',
            '要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F（呼～斯蒂娜阿姨\n',
            '　还是那么啰里啰嗦啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49F5')

    def _loc_498B(): pass

    label('loc_498B')

    ChrTalk(
        0x000B,
        (
            '衣冠不整的话，就算作为一个游击士\n',
            '也不会让别人觉得可靠呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且衣冠整齐也是\n',
            '精神状态良好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49F5(): pass

    label('loc_49F5')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x49F9
@scena.Code('func_0A_49F9')
def func_0A_49F9():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 7, 0x29F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BCC',
    )

    If(
        (
            (Expr.Eval, "OP_BB(0x00, 0x01)"),
            (Expr.Eval, "OP_BB(0x00, 0x05)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4A96',
    )

    SetScenaFlags(ScenaFlag(0x0053, 7, 0x29F))

    ChrTalk(
        0x000C,
        (
            '#0030000453V#020F打开的是艾丝蒂尔的结晶孔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000454V艾丝蒂尔中间的结晶孔是全属性类型的，\n',
            '所以安装任何一种结晶回路都可以。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BCC')

    def _loc_4A96(): pass

    label('loc_4A96')

    If(
        (
            (Expr.Eval, "OP_BB(0x01, 0x01)"),
            (Expr.Eval, "OP_BB(0x01, 0x05)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4B28',
    )

    SetScenaFlags(ScenaFlag(0x0053, 7, 0x29F))

    ChrTalk(
        0x000C,
        (
            '#0030000455V#020F打开的是约修亚的结晶孔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000456V约修亚中间的结晶孔是限定属性类型的，\n',
            '所以还是早点打开其他结晶孔比较好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BCC')

    def _loc_4B28(): pass

    label('loc_4B28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 6, 0x29E)),
            Expr.Return,
        ),
        'loc_4BCC',
    )

    ChrTalk(
        0x000C,
        (
            '#0030000451V#020F先到前台那里，\n',
            '然后在工房菜单中选择『结晶孔』，\n',
            '这样就可以开封新的结晶孔的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000452V到底打开谁的结晶孔，\n',
            '你们就自己商量着决定吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

    def _loc_4BCC(): pass

    label('loc_4BCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 6, 0x29E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56F7',
    )

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x006E)"),
            (Expr.Eval, "OP_BA(0x01, 0x000A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4BE9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4BE9(): pass

    label('loc_4BE9')

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x006E)"),
            (Expr.Eval, "OP_BA(0x01, 0x0014)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4BFE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4BFE(): pass

    label('loc_4BFE')

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x006E)"),
            (Expr.Eval, "OP_BA(0x01, 0x001E)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C13',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C13(): pass

    label('loc_4C13')

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x006E)"),
            (Expr.Eval, "OP_BA(0x01, 0x0032)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C28',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C28(): pass

    label('loc_4C28')

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x006E)"),
            (Expr.Eval, "OP_BA(0x01, 0x0041)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C3D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C3D(): pass

    label('loc_4C3D')

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x006E)"),
            (Expr.Eval, "OP_BA(0x01, 0x006E)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C52',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C52(): pass

    label('loc_4C52')

    If(
        (
            (Expr.Eval, "OP_BA(0x01, 0x006E)"),
            (Expr.Eval, "OP_BA(0x00, 0x000A)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C67',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C67(): pass

    label('loc_4C67')

    If(
        (
            (Expr.Eval, "OP_BA(0x01, 0x006E)"),
            (Expr.Eval, "OP_BA(0x00, 0x0014)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C7C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C7C(): pass

    label('loc_4C7C')

    If(
        (
            (Expr.Eval, "OP_BA(0x01, 0x006E)"),
            (Expr.Eval, "OP_BA(0x00, 0x001E)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C91',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4C91(): pass

    label('loc_4C91')

    If(
        (
            (Expr.Eval, "OP_BA(0x01, 0x006E)"),
            (Expr.Eval, "OP_BA(0x00, 0x0032)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CA6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_4CB8')

    def _loc_4CA6(): pass

    label('loc_4CA6')

    If(
        (
            (Expr.Eval, "OP_BA(0x01, 0x006E)"),
            (Expr.Eval, "OP_BA(0x00, 0x0041)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CB8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_4CB8(): pass

    label('loc_4CB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_5543',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 5, 0x29D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_510E',
    )

    SetScenaFlags(ScenaFlag(0x0053, 6, 0x29E))
    SetScenaFlags(ScenaFlag(0x0053, 5, 0x29D))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4E48',
    )

    ChrTalk(
        0x000C,
        (
            '#0030000446V#023F啊，已经设定好结晶回路了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000447V#020F看来你们已经\n',
            '可以使用回复和攻击的魔法了。\n',
            '不用我再说明什么了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000448V平衡好两个人能使用的魔法，\n',
            '这样战斗起来会更加得心应手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000449V顺便一提，\n',
            '结晶回路所具有的功能和魔法效果，\n',
            '都在游击士手册里有详细的记载。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000450V如果想使用更强力的魔法，\n',
            '自己多花点功夫研究手册里的\n',
            '魔法列表和结晶回路列表就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0014)

    Jump('loc_510B')

    def _loc_4E48(): pass

    label('loc_4E48')

    ChrTalk(
        0x000C,
        (
            '#0030000435V#023F怎么，已经设定好结晶回路了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000436V#020F嗯，看来你们已经\n',
            '可以使用回复和攻击的魔法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000437V平衡好两个人能使用的魔法，\n',
            '这样战斗起来会更加得心应手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000438V顺便一提，\n',
            '结晶回路所具有的功能和魔法效果，\n',
            '都在游击士手册里有详细的记载。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000439V如果想使用更强力的魔法，\n',
            '自己多花点功夫研究手册里的\n',
            '魔法列表和结晶回路列表就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000440V——那么，\n',
            '在工房的研修也接近尾声了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000441V最后要做的就是\n',
            '让你们试试开封新的结晶孔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000442V结晶孔数增加的话，\n',
            '可供使用的魔法也就更加多样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000443V使用魔法时所消耗的ＥＰ值上限\n',
            '也由打开的结晶孔数量决定，\n',
            '所以早点开封既有利又方便自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000444V那么，就用试试这些耀晶片\n',
            '开封导力器上的结晶孔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000445V打开谁的结晶孔都没关系，\n',
            '你们两人自己决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_510B(): pass

    label('loc_510B')

    Jump('loc_54E7')

    def _loc_510E(): pass

    label('loc_510E')

    SetScenaFlags(ScenaFlag(0x0053, 6, 0x29E))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_5250',
    )

    ChrTalk(
        0x000C,
        (
            '#0030000476V#020F嗯，看来你们已经\n',
            '可以使用回复和攻击的魔法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000477V平衡好两个人能使用的魔法，\n',
            '这样战斗起来会更加得心应手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000478V顺便一提，\n',
            '结晶回路所具有的功能和魔法效果，\n',
            '都在游击士手册里有详细的记载。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000479V如果想使用更强力的魔法，\n',
            '自己多花点功夫研究手册里的\n',
            '魔法列表和结晶回路列表就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0014)

    Jump('loc_54E7')

    def _loc_5250(): pass

    label('loc_5250')

    ChrTalk(
        0x000C,
        (
            '#0030000466V#020F嗯，看来你们已经\n',
            '可以使用回复和攻击的魔法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000467V平衡好两个人能使用的魔法，\n',
            '这样战斗起来会更加得心应手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000468V顺便一提，\n',
            '结晶回路所具有的功能和魔法效果，\n',
            '都在游击士手册里有详细的记载。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000469V如果想使用更强力的魔法，\n',
            '自己多花点功夫研究手册里的\n',
            '魔法列表和结晶回路列表就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000470V——那么，\n',
            '在工房的研修也接近尾声了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000471V最后要做的就是\n',
            '让你们试试开封新的结晶孔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000472V结晶孔数增加的话，\n',
            '可供使用的魔法也就更加多样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000473V使用魔法时所消耗的ＥＰ值上限\n',
            '也由打开的结晶孔数量决定，\n',
            '所以早点开封既有利又方便自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000474V那么，就用试试这些耀晶片\n',
            '开封导力器上的结晶孔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000475V打开谁的结晶孔都没关系，\n',
            '你们两人自己决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54E7(): pass

    label('loc_54E7')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '得到各种属性的耀晶片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x00)
    FadeIn(300, 0)
    AddSepith(0x00, 30)
    AddSepith(0x01, 30)
    AddSepith(0x02, 30)
    AddSepith(0x03, 30)
    TalkEnd(0x000C)

    Return()

    def _loc_5543(): pass

    label('loc_5543')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 5, 0x29D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_554E',
    )

    Jump('loc_56F7')

    def _loc_554E(): pass

    label('loc_554E')

    ChrTalk(
        0x000C,
        (
            '#0030000457V#020F把结晶回路安装在导力器上，\n',
            '保证可以使用回复魔法和攻击魔法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000458V观察自己的导力器，\n',
            '合理分配回复魔法和攻击魔法的比例。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000459V至于要安装哪种结晶回路，\n',
            '可以参考游击士手册中的\n',
            '魔法列表和结晶回路列表。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000460V如果结晶回路缺少的话，\n',
            '可以在工房合成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请在艾丝蒂尔的导力器的中心孔安装#90IＨＰ１，\n',
            '在约修亚的导力器的中心孔安装#93I行动力１，\n',
            '使两人分别获得回复魔法和攻击魔法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x000C)

    Return()

    def _loc_56F7(): pass

    label('loc_56F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 5, 0x29D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58A3',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0273)"),
            (Expr.Eval, "OP_40(0x0258)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x025E)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x0261)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x026D)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_581E',
    )

    SetScenaFlags(ScenaFlag(0x0053, 5, 0x29D))

    ChrTalk(
        0x000C,
        (
            '#0030000463V#020F嗯，看来你们已经合好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000464V那么，接下来就试试\n',
            '增加可使用的魔法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000465V确保可以使用\n',
            '回复魔法和攻击魔法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※结晶回路的安装在[Orbment]界面进行。\n',
            '　要开启[Orbment]界面\n',
            '　只需在Camp中点击[Orbment]即可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x000C)

    Return()

    def _loc_581E(): pass

    label('loc_581E')

    ChrTalk(
        0x000C,
        (
            '#0030000461V#020F试试合成结晶回路吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000462V艾丝蒂尔任何属性的都ＯＫ，\n',
            '不过约修亚不能安装时属性以外的，\n',
            '所以这点要注意一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

    def _loc_58A3(): pass

    label('loc_58A3')

    Call(0, 0x0014)

    Return()

# id: 0x000B offset: 0x58A8
@scena.Code('func_0B_58A8')
def func_0B_58A8():
    TalkBegin(0x000D)

    NpcTalk(
        0x000D,
        '戴眼镜的女性',
        (
            '#0280010454V#0151F哇～～好可爱呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x58DF
@scena.Code('func_0C_58DF')
def func_0C_58DF():
    ChrMoveTo(0x0101, -39981, 0, -4821, 3000, 0x00)
    SetChrDirection(0x0101, 0, 0)
    ChrMoveTo(0x0101, -39193, 0, -7010, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x590F
@scena.Code('func_0D_590F')
def func_0D_590F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5995',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_69(0x000C, 800)

    @scena.Lambda('lambda_592F')
    def lambda_592F():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_592F)

    @scena.Lambda('lambda_593D')
    def lambda_593D():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_593D)

    ChrTalk(
        0x000C,
        (
            '#0030000433V#024F怎么了，想出去吗？\n',
            '研修还没结束呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5995(): pass

    label('loc_5995')

    Return()

# id: 0x000E offset: 0x5996
@scena.Code('func_0E_5996')
def func_0E_5996():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A1C',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_69(0x000C, 800)

    @scena.Lambda('lambda_59B6')
    def lambda_59B6():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_59B6)

    @scena.Lambda('lambda_59C4')
    def lambda_59C4():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_59C4)

    ChrTalk(
        0x000C,
        (
            '#0030000434V#024F怎么了，想出去吗？\n',
            '研修还没结束呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5A1C(): pass

    label('loc_5A1C')

    Return()

# id: 0x000F offset: 0x5A1D
@scena.Code('func_0F_5A1D')
def func_0F_5A1D():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000C, 0x0008)

    If(
        (
            (Expr.Eval, "OP_BB(0x00, 0x01)"),
            (Expr.Eval, "OP_BB(0x00, 0x05)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5A44',
    )

    SetScenaFlags(ScenaFlag(0x0053, 7, 0x29F))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_5A57')

    def _loc_5A44(): pass

    label('loc_5A44')

    If(
        (
            (Expr.Eval, "OP_BB(0x01, 0x01)"),
            (Expr.Eval, "OP_BB(0x01, 0x05)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_5A57',
    )

    SetScenaFlags(ScenaFlag(0x0053, 7, 0x29F))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_5A57(): pass

    label('loc_5A57')

    SetChrPos(0x000C, -41600, 0, -1337, 270)
    SetChrPos(0x0101, -43651, 0, -651, 90)
    SetChrPos(0x0102, -43651, 0, -2165, 90)
    CameraMove(-43106, 0, -929, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x000C,
        (
            '#0030000390V#020F在这里学习一下\n',
            '有关工房的主要用途和具体操作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000391V#020F在工房里，\n',
            '可以改造驱动导力魔法所专用的导力器，\n',
            '以及合成功能各异的结晶回路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000392V#020F魔法能发挥各种不同的效果，\n',
            '熟练掌握的话会给工作带来种种的便利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000393V#020F游击士是一种经常伴随着危险的职业，\n',
            '因此每一个游击士都会\n',
            '长时间和各地的工房打交道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000394V#020F……嗯，\n',
            '我能说的也只有这些了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000395V#020F关于导力器技术方面的内容\n',
            '就要由专家为你们解释了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000396V#020F……就是这样了。\n',
            '梅尔达斯先生，之后就麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5C96')
    def lambda_5C96():
        ChrTurnDirection(0x000C, 0x0000, 0)
        Yield()

        Jump('lambda_5C96')

    DispatchAsync2(0x000C, 0x0001, lambda_5C96)

    OP_4A(0x0009, 0)
    CameraMove(-41136, 0, -889, 800)

    ChrTalk(
        0x0009,
        (
            '#0830000397V嗯，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5CD7')
    def lambda_5CD7():
        OP_69(0x0009, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_5CD7)

    @scena.Lambda('lambda_5CE5')
    def lambda_5CE5():
        ChrWalkTo(0x0102, -41609, 0, -400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5CE5)

    ChrWalkTo(0x0101, -41609, 0, 423, 3000, 0x00)
    SetChrDirection(0x0101, 90, 400)
    SetChrDirection(0x0102, 90, 400)
    def _loc_5D1C(): pass

    label('loc_5D1C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6728',
    )

    ChrTalk(
        0x0009,
        (
            '#0830000398V那么，想知道什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_5DB1',
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【导力魔法（魔法）】\n'),
            TXT(0x02, '【结晶回路】\n'),
            TXT(0x03, '【耀晶片】\n'),
            TXT(0x04, '【放弃】\n'),
        ),
    )

    Jump('loc_5DF2')

    def _loc_5DB1(): pass

    label('loc_5DB1')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【导力魔法（魔法）】\n'),
            TXT(0x02, '【结晶回路】\n'),
            TXT(0x03, '【耀晶片】\n'),
        ),
    )

    def _loc_5DF2(): pass

    label('loc_5DF2')

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
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5E2C'),
        (0x00000001, 'loc_6126'),
        (0x00000002, 'loc_63EB'),
        (0x00000003, 'loc_6592'),
        (0x00000004, 'loc_6713'),
        (-1, 'loc_6723'),
    )

    def _loc_5E2C(): pass

    label('loc_5E2C')

    ChrTalk(
        0x0009,
        (
            '#0830000399V导力器就是\n',
            '通过设定结晶回路来\n',
            '发挥各种各样效果的机械部件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000400V按照这个定义，\n',
            '照明用具、飞艇引擎等物品\n',
            '都是用导力器制成的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000401V不过这里所说的导力器是指\n',
            (TxtCtl.SetColor, 0x4),
            '提高持有者身体能力、使其能够使用魔法\n',
            (TxtCtl.SetColor, 0x0),
            '的『战术导力器』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000402V这是按照各人实际情况而定制的一种导力器，\n',
            '也是最适合个人使用的战斗工具。\n',
            (TxtCtl.SetColor, 0x4),
            '持有者不同，其结构也会有所差异',
            (TxtCtl.SetColor, 0x0),
            '的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000403V具体来说，限定属性的结晶孔和\n',
            '连接结晶孔的结晶链形状都有所不同……\n',
            '不过，现在还不需要讲得太深奥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000404V要想设定结晶回路，\n',
            '就要先开封结晶孔才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000405V中间的结晶孔一开始就是打开的，\n',
            '其余的就必须要在工房进行开封。\n',
            '要注意，开封的时候需要耀晶片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000406V用来发动导力魔法的ＥＰ值上限，\n',
            (TxtCtl.SetColor, 0x4),
            '会随着开封的结晶孔数增加',
            (TxtCtl.SetColor, 0x0),
            '而不断上升。\n',
            '所以尽快把结晶孔全部打开是很有益处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6723')

    def _loc_6126(): pass

    label('loc_6126')

    ChrTalk(
        0x0009,
        (
            '#0830000407V这个嘛……\n',
            '说得通俗点说就是\n',
            '使用专用的『战术导力器』来发动的魔法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000408V也就是使用导力器中蓄积的\n',
            '一种叫做『导力』的能量，\n',
            '来引起各种各样奇妙的现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000409V因为导力魔法这个名字念起来太拗口，\n',
            '所以现在大家都魔法、魔法这样地称呼。\n',
            '真是的，一开始就这么叫不就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000410V魔法有很多不同的种类，\n',
            '想要使用的话，\n',
            '先得在工房合成结晶回路才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000411V然后把合成好的结晶回路\n',
            '安装在导力器的结晶孔里面，\n',
            '这样就可以使用魔法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000412V可供使用的魔法\n',
            (TxtCtl.SetColor, 0x4),
            '会依照安装在导力器里的\n',
            (TxtCtl.SetColor, 0x0),
            '结晶回路的属性组合而变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000413V想使用水系的魔法，\n',
            '将带有水属性值的结晶回路\n',
            '安装在导力器里面就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000414V……嗯，老实说，\n',
            '实际操作要比单纯解释原理更加复杂，\n',
            '不过目前掌握这些知识就够用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6723')

    def _loc_63EB(): pass

    label('loc_63EB')

    ChrTalk(
        0x0009,
        (
            '#0830000415V结晶回路其实就是\n',
            '用耀晶片加工而成的回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000416V',
            (TxtCtl.SetColor, 0x4),
            '提升持有者各项能力',
            (TxtCtl.SetColor, 0x0),
            '的同时，\n',
            (TxtCtl.SetColor, 0x4),
            '使其能够使用各种魔法',
            (TxtCtl.SetColor, 0x0),
            '是结晶回路最重要的作用。\n',
            '这种回路拥有的效果实在是非常之多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000417V结晶回路必须安装在导力器的结晶孔里\n',
            '才能发挥作用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000418V而根据结晶孔的不同，也有些',
            (TxtCtl.SetColor, 0x4),
            '只能安装\n',
            '某种属性结晶回路',
            (TxtCtl.SetColor, 0x0),
            '的具有限定属性的结晶孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000419V合成新的结晶回路之前，\n',
            '最好先考虑好要把它\n',
            '安装在导力器的哪一个位置上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6723')

    def _loc_6592(): pass

    label('loc_6592')

    ChrTalk(
        0x0009,
        (
            '#0830000420V耀晶片指的是\n',
            '魔兽身上掉落的七耀石碎片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000421V颜色和属性相对，一共分为\n',
            '#182I地（棕色）、#56I水（蓝色）、火（红色）、风（绿色）、\n',
            '时（黑色）、空（金色）、幻（银色）\n',
            '７种耀晶片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000422V虽说在王国每个城市里都有很多\n',
            (TxtCtl.SetColor, 0x4),
            '可以把耀晶片换成流通货币米拉',
            (TxtCtl.SetColor, 0x0),
            '的店铺……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0830000423V不过在工房里可以用它来\n',
            '合成具有各种不同属性的结晶回路，\n',
            '以及开封用来安装结晶回路的结晶孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6723')

    def _loc_6713(): pass

    label('loc_6713')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_6723')

    def _loc_6723(): pass

    label('loc_6723')

    OP_56(0x00)

    Jump('loc_5D1C')

    def _loc_6728(): pass

    label('loc_6728')

    @scena.Lambda('lambda_672E')
    def lambda_672E():
        ChrTurnDirection(0x0000, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_672E)

    @scena.Lambda('lambda_673C')
    def lambda_673C():
        ChrTurnDirection(0x0001, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_673C)

    OP_69(0x000C, 1000)

    ChrTalk(
        0x000C,
        (
            '#0030000424V#020F看起来没什么问题了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000425V那么，\n',
            '接下来就要动手自己操作一下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000426V为了让你们动手试试，\n',
            '我给你们准备了一些必要的耀晶片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '得到各种属性的耀晶片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x00)
    FadeIn(300, 0)
    AddSepith(0x00, 20)
    AddSepith(0x01, 20)
    AddSepith(0x02, 20)
    AddSepith(0x03, 20)
    AddSepith(0x04, 20)
    AddSepith(0x05, 20)
    AddSepith(0x06, 20)

    ChrTalk(
        0x000C,
        (
            '#0030000427V#020F有了这些耀晶片，\n',
            '就可以合成几个结晶回路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000428V先合成与自己的导力器\n',
            '相应属性的结晶回路看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000429V艾丝蒂尔任何属性的都ＯＫ，\n',
            '不过约修亚只能安装时属性的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000430V本来在商店可以把耀晶片换成钱，\n',
            '不过考虑到现在是研修中，\n',
            '所以暂时还不能让你们换。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※站在柜台附近时会出现『TALK』的标记，\n',
            '　用右键点击会出现选择菜单。\n',
            '　选择工房菜单中的『改造·换钱』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    EventEnd(0x00)
    OP_4B(0x0009, 0)

    Return()

# id: 0x0010 offset: 0x69DB
@scena.Code('func_10_69DB')
def func_10_69DB():
    SetScenaFlags(ScenaFlag(0x004A, 3, 0x253))
    OP_28(0x0019, 0x01, 0x0040)
    EventBegin(0x00)
    FormationAddMember(0x0F, 0xFF)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A2B',
    )

    SetChrPos(0x0101, -42590, 0, 1660, 135)
    SetChrPos(0x0102, -43440, 0, 1640, 135)
    SetChrPos(0x0002, -42910, 0, 520, 135)

    Jump('loc_6A5E')

    def _loc_6A2B(): pass

    label('loc_6A2B')

    SetChrPos(0x0101, -38220, 0, -5030, 0)
    SetChrPos(0x0102, -39380, 0, -5260, 0)
    SetChrPos(0x0002, -38890, 0, -4019, 0)

    def _loc_6A5E(): pass

    label('loc_6A5E')

    SetChrPos(0x0003, -38530, 0, -2400, 0)
    OP_4A(0x0008, 0)
    ChrTurnDirection(0x0008, 0x0003, 0)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x3, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x3, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x3, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(2000, 0)
    OP_69(0x000E, 2000)
    OP_0D()
    OP_62(0x0003, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    NpcTalk(
        0x0003,
        '戴眼镜的女性',
        (
            '#0280010521V#152F啊啊，求求您～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010522V#152F我什么都愿意做，\n',
            '只要能把照相机还我！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010523V#152F那可是比我的生命还宝贵的东西啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840010524V真、真伤脑筋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0840010525V老爹，该怎么办好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0009, 0)
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0830010526V那是你接下的工作，\n',
            '你自己处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 270, 400)
    OP_4B(0x0009, 0)
    ChrTurnDirection(0x0008, 0x0003, 400)

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x3, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x3, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x3, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000E, 800)

    ChrTalk(
        0x0101,
        (
            '#0010010527V#004F大家好像在争吵什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010528V#014F难道，就是那个人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0002,
        (
            '#0270010529V#145F……………………就是她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000E, 0x01, 0x00, 0x0011)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CFB',
    )

    ChrWalkTo(0x0002, -41735, 0, -2400, 3000, 0x00)
    ChrWalkTo(0x0002, -39550, 0, -2400, 3000, 0x00)

    Jump('loc_6D0F')

    def _loc_6CFB(): pass

    label('loc_6CFB')

    ChrWalkTo(0x0002, -39550, 0, -2400, 2000, 0x00)

    def _loc_6D0F(): pass

    label('loc_6D0F')

    ChrTurnDirection(0x0002, 0x0003, 400)

    ChrTalk(
        0x0002,
        (
            '#0270010530V#144F#3P喂，朵洛希！\n',
            '你要我等到什么时候啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0003, 0x0002, 400)
    ChrTurnDirection(0x0008, 0x0002, 400)

    ChrTalk(
        0x0003,
        (
            '#0280010531V#153F#2P啊啊，奈尔前辈！\n',
            '你来得正好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010532V#152F呜呜，赶快帮帮我呀～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0002,
        (
            '#0270010533V#142F#3P这次你又干了些什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010534V#142F是不是乱花钱，\n',
            '结果照相机的修理费不够了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0003,
        (
            '#0280010535V#153F#2P哇，真是太厉害了！\n',
            '你怎么会知道的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010536V#153F前辈，难道你有超能力？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0002,
        (
            '#0270010537V#144F#3P老是重复又重复地做同样的蠢事，\n',
            '白痴也会知道啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840010538V客人，您认识这位小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840010539V如果认识的话……\n',
            '可以麻烦您替她垫付一下修理费吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0002, 0x0008, 400)

    ChrTalk(
        0x0002,
        (
            '#0270010540V#145F#3P没办法……\n',
            '就算在经费里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010541V#145F多少钱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840010542V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840010543V照相机和装饰用钟表的修理费\n',
            '一共是２０００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0002, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0002,
        (
            '#0270010544V#144F#3P等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010545V#144F照相机就算了，\n',
            '那个装饰用钟表是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0003,
        (
            '#0280010546V#151F#2P那个，你听我说，\n',
            '修理相机的时候我在店里参观。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010547V#151F然后发现一个漂亮的座钟，\n',
            '可是我拿起来看的时候却弄坏了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010548V#151F不过不过，你来了就好了㈱\n',
            '那个也可以算在经费里～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0002, 0x0003, 400)

    ChrTalk(
        0x0002,
        (
            '#0270010549V#144F#3P这种东西怎可以算在经费里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010550V#145F可、可恶……\n',
            '只能先自掏腰包垫上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0002, 0x0008, 400)

    ChrTalk(
        0x0002,
        (
            '#0270010551V#142F#3P给，２０００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0840010552V好的，这是收据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_71F3',
    )

    CameraMove(-42770, 0, 1380, 1500)

    Jump('loc_7204')

    def _loc_71F3(): pass

    label('loc_71F3')

    CameraMove(-38130, 0, -4670, 1500)

    def _loc_7204(): pass

    label('loc_7204')

    ChrTalk(
        0x0101,
        (
            '#0010010553V#008F（看、看起来……\n',
            '　这对记者组合挺有趣的呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010554V#010F（确实是……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010555V#010F（虽然那个男的脾气不太好，\n',
            '　不过看起来也很会照顾人啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0003, 0xFF)
    CreateThread(0x0002, 0x01, 0x00, 0x0012)
    Sleep(500)

    SetChrDirection(0x0008, 180, 400)
    OP_4B(0x0008, 0)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7303',
    )

    ChrWalkTo(0x0003, -41630, 0, -2450, 3000, 0x00)
    ChrWalkTo(0x0003, -42760, 0, -730, 3000, 0x00)
    SetChrDirection(0x0003, 0, 400)

    Jump('loc_731E')

    def _loc_7303(): pass

    label('loc_7303')

    SetChrDirection(0x0003, 180, 400)
    ChrWalkTo(0x0003, -38500, 0, -3740, 2000, 0x00)

    def _loc_731E(): pass

    label('loc_731E')

    ChrTalk(
        0x0002,
        (
            '#0270010556V#145F哦哦，久等了。\n',
            '稍微遇到了点麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0003,
        (
            '#0280010557V#150F咦，前辈，这些孩子是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0002,
        (
            '#0270010558V#140F他们是给我们护卫兼带路的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010559V#140F代替卡西乌斯·布莱特\n',
            '接受我们委托的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0003,
        (
            '#0280010560V#153F哇，这么年轻的孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010561V#000F我叫艾丝蒂尔，请多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010562V#010F我叫约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0003,
        (
            '#0280010563V#151F是小艾和小约啊。\n',
            '虽然很年轻，不过看起来很可靠啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010564V#151F我叫朵洛希·海娅特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010565V#151F是刚进入《利贝尔通讯》的新人摄影师哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280010566V#151F正在奈尔前辈的指导下努力工作，\n',
            '也请你们多多指教哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0002,
        (
            '#0270010567V#145F为什么非要我照顾\n',
            '这么一个脱线的女生呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010568V#145F真是的，那个大胡子总编……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0003,
        (
            '#0280010569V#151F算啦算啦～\n',
            '努力到最后一定会有好报的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0002, 0x0003, 400)

    ChrTalk(
        0x0002,
        (
            '#0270010570V#144F你给我住嘴，你呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010571V#145F唉，算了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0002, 0x0102, 400)

    ChrTalk(
        0x0002,
        (
            '#0270010572V#140F人已经到齐了，\n',
            '我们赶快出发去取材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010573V#010F目的地是城外的『翡翠之塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010574V#001F好的～我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0003,
        (
            '#0280010575V#151F噢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x76B5
@scena.Code('func_11_76B5')
def func_11_76B5():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76D5',
    )

    CameraMove(-39730, 0, -1830, 2000)

    Jump('loc_76E6')

    def _loc_76D5(): pass

    label('loc_76D5')

    CameraMove(-37205, 0, -2234, 2000)

    def _loc_76E6(): pass

    label('loc_76E6')

    Return()

# id: 0x0012 offset: 0x76E7
@scena.Code('func_12_76E7')
def func_12_76E7():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7733',
    )

    ChrWalkTo(0x0002, -41630, 0, -2450, 3000, 0x00)
    ChrWalkTo(0x0002, -43560, 0, 30, 3000, 0x00)
    SetChrDirection(0x0002, 0, 400)
    SetChrDirection(0x0101, 180, 400)
    SetChrDirection(0x0102, 180, 400)

    Jump('loc_774E')

    def _loc_7733(): pass

    label('loc_7733')

    SetChrDirection(0x0002, 180, 400)
    ChrWalkTo(0x0002, -39440, 0, -3950, 2000, 0x00)

    def _loc_774E(): pass

    label('loc_774E')

    Return()

# id: 0x0013 offset: 0x774F
@scena.Code('func_13_774F')
def func_13_774F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_776A',
    )

    ChrTurnDirection(0x0003, 0x0002, 0)
    ChrTurnDirection(0x0008, 0x0002, 0)
    Yield()

    Jump('func_13_774F')

    def _loc_776A(): pass

    label('loc_776A')

    Return()

# id: 0x0014 offset: 0x776B
@scena.Code('func_14_776B')
def func_14_776B():
    Sleep(100)

    Fade(1000)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    TerminateThread(0x000C, 0x01)
    SetChrDirection(0x000C, 270, 0)
    SetChrPos(0x0101, -42760, 0, -2149, 45)
    SetChrPos(0x0102, -42760, 0, -936, 135)
    CameraMove(-42964, 0, -712, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0030000480V#020F这么一来，\n',
            '在工房的研修就结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000481V那么，接下来终于轮到\n',
            '你们期盼已久的认定考试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000482V#004F……哎？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000483V#004F考、考试，是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    @scena.Lambda('lambda_7889')
    def lambda_7889():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7889)

    ChrTalk(
        0x0102,
        (
            '#0020000484V#018F……不会吧，你真的忘了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000485V今天早上才刚和你说过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000486V#008F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000487V这么说来，\n',
            '好像听说过，又好像没有……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_792D')
    def lambda_792D():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_792D)

    ChrTalk(
        0x000C,
        (
            '#0030000488V#025F唉……\n',
            '你还真是个不负众望的孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000489V#020F算了。\n',
            '不管了，赶快去考场再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010000490V#004F哎！？这、这就！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000491V#004F等、等一下，\n',
            '我还没做好心理准备呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030000492V#024F好啦好啦，\n',
            '乖乖地跟着我走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000C, 0xFF)
    ChrWalkTo(0x000C, -42253, 0, -2549, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0101, 0)
    SetChrDirection(0x000C, 315, 400)
    SetChrDirection(0x0101, 315, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x0101, 0x01, 0x00, 0x000C)
    ChrWalkTo(0x000C, -39981, 0, -4821, 3000, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrWalkTo(0x000C, -39193, 0, -7010, 3000, 0x00)
    Sleep(200)

    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 190)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 200)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010000493V#003F约修亚，救命啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    OP_63(0x0102)
    Sleep(100)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000494V#010F梅尔达斯先生、弗莱迪先生，\n',
            '非常感谢你们的指点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0009, 0)
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#0830000495V不客气，考试考好点就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 0)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0840000496V好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000497V#009F喂～约修亚！\n',
            '你给我记住～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT01/T0100._SN', 2, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
