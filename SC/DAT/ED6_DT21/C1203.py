import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1203   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '歼灭天使玲'),
    TXT(0x02, '假福音'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1203.x'
    header.mapIndex       = 51
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1299
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
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT29/CH12450._CH', 'ED6_DT29/CH12450P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 11390,
            z                   = 250,
            y                   = 5670,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 8790,
            z           = 250,
            y           = 12470,
            word_0C     = 0x010E,
            word_0E     = 0x0003,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x008E,
            word_18     = 0x2102,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x14E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 11390,
            y           = 250,
            z           = 5670,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x16E
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x16E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 2, 0x2102)),
            Expr.Return,
        ),
        'loc_17A',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_17A(): pass

    label('loc_17A')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_188',
    )

    OP_B5(0x00)

    def _loc_188(): pass

    label('loc_188')

    Return()

# id: 0x0001 offset: 0x189
@scena.Code('Init')
def Init():
    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 7, 0x1A0F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C6',
    )

    ClearChrFlags(0x000A, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_1C6(): pass

    label('loc_1C6')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DD',
    )

    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_72(0x0000, 0x0004)

    def _loc_1DD(): pass

    label('loc_1DD')

    OP_22(0x01C3, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1E3
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1F8',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_1F8(): pass

    label('loc_1F8')

    Return()

# id: 0x0003 offset: 0x1F9
@scena.Code('func_03_1F9')
def func_03_1F9():
    EventBegin(0x01)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '巨大的魔兽正四处徘徊。',
            TxtCtl.Enter,
        ),
    )

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
        32,
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_260'),
        (0x00000001, 'loc_48E'),
        (-1, 'loc_4F6'),
    )

    def _loc_260(): pass

    label('loc_260')

    Battle(0x00000093, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_281'),
        (0x00000002, 'loc_40E'),
        (0x00000001, 'loc_486'),
        (-1, 'loc_48B'),
    )

    def _loc_281(): pass

    label('loc_281')

    EventBegin(0x01)
    FadeOut(0, 0, -1)
    SetChrFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_322',
    )

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
        32,
        0,
        (
            TXT(0x00, '【◇消灭了古罗尼峰和迷雾峡谷的通缉魔兽】\n'),
            TXT(0x01, '【◇什么也没有变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_30D'),
        (-1, 'loc_322'),
    )

    def _loc_30D(): pass

    label('loc_30D')

    OP_A2(0x1A0E)
    OP_A2(0x1A10)
    OP_28(0x00B1, 0x01, 0x0001)
    OP_28(0x00B2, 0x01, 0x0001)

    Jump('loc_322')

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 6, 0x1A0E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 0, 0x1A10)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_334',
    )

    Call(0, 0x0004)

    Jump('loc_40B')

    def _loc_334(): pass

    label('loc_334')

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrPos(0x0000, 11390, 250, 5670, 45)
    SetChrPos(0x0001, 11390, 250, 5670, 45)
    SetChrPos(0x0002, 11390, 250, 5670, 45)
    SetChrPos(0x0003, 11390, 250, 5670, 45)
    OP_69(0x0000, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了琥珀之塔的通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1A0F)
    OP_28(0x00B3, 0x01, 0x0001)
    OP_28(0x0093, 0x02, 0x0010)
    OP_28(0x0093, 0x01, 0x0020)
    OP_28(0x0093, 0x01, 0x0040)
    Sleep(400)

    def _loc_40B(): pass

    label('loc_40B')

    Jump('loc_48B')

    def _loc_40E(): pass

    label('loc_40E')

    EventBegin(0x01)
    FadeOut(0, 0, -1)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrPos(0x0000, 7940, 250, 1990, 45)
    SetChrPos(0x0001, 7940, 250, 1990, 45)
    SetChrPos(0x0002, 7940, 250, 1990, 45)
    SetChrPos(0x0003, 7940, 250, 1990, 45)
    OP_69(0x0000, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_48B')

    def _loc_486(): pass

    label('loc_486')

    OP_B4(0x00)

    Jump('loc_48B')

    def _loc_48B(): pass

    label('loc_48B')

    Jump('loc_4F6')

    def _loc_48E(): pass

    label('loc_48E')

    Fade(500)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrPos(0x0000, 7940, 250, 1990, 45)
    SetChrPos(0x0001, 7940, 250, 1990, 45)
    SetChrPos(0x0002, 7940, 250, 1990, 45)
    SetChrPos(0x0003, 7940, 250, 1990, 45)
    OP_69(0x0000, 0x00000000)
    OP_0D()

    Jump('loc_4F6')

    def _loc_4F6(): pass

    label('loc_4F6')

    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x4F9
@scena.Code('func_04_4F9')
def func_04_4F9():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_50C',
    )

    Call(0, 0x0005)

    def _loc_50C(): pass

    label('loc_50C')

    OP_6D(11780, 250, 5320, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 12050, 250, 4660, 270)
    SetChrPos(0x0106, 11110, 250, 5750, 180)
    SetChrPos(0x00F8, 10510, 250, 3060, 0)
    SetChrPos(0x00F9, 9550, 250, 4240, 90)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300715V#1007F哈～总算是解决了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300716V#1002F不过……\n',
            '这些魔兽的样子似乎很奇怪啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '是哪里和平时不同了呢？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【魔兽变强了】\n'),
            TXT(0x01, '【魔兽变胆怯了】\n'),
            TXT(0x02, '【魔兽非常兴奋】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6B2'),
        (0x00000001, 'loc_8EB'),
        (0x00000002, 'loc_AF2'),
        (-1, 'loc_CFF'),
    )

    def _loc_6B2(): pass

    label('loc_6B2')

    OP_2B(0x0093, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300717V#072F那也没错……\n',
            '不过更明显的是它们的性情变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E2')

    def _loc_73F(): pass

    label('loc_73F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300719V#022F那也说的没错……\n',
            '不过更明显的是它们的性情变了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E2')

    def _loc_7CD(): pass

    label('loc_7CD')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_85D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300721V#032F嗯、那也说的不错，\n',
            '不过更明显的是它们的性情变了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E2')

    def _loc_85D(): pass

    label('loc_85D')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8E2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300723V#043F那样说也对，\n',
            '不过更明显的是它们的性情变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E2(): pass

    label('loc_8E2')

    OP_28(0x0093, 0x01, 0x0400)

    Jump('loc_CFF')

    def _loc_8EB(): pass

    label('loc_8EB')

    OP_2B(0x0093, 0x0003)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_970',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300725V#072F啊啊～每一处的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9')

    def _loc_970(): pass

    label('loc_970')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9EE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300727V#022F哎～每一处的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9')

    def _loc_9EE(): pass

    label('loc_9EE')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A6E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300729V#032F嗯，不管是什么魔兽\n',
            '都好像很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9')

    def _loc_A6E(): pass

    label('loc_A6E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300731V#042F是啊，不管是什么魔兽\n',
            '都很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE9(): pass

    label('loc_AE9')

    OP_28(0x0093, 0x01, 0x1000)

    Jump('loc_CFF')

    def _loc_AF2(): pass

    label('loc_AF2')

    OP_2B(0x0093, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B79',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300725V#072F啊啊～不管是什么魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_B79(): pass

    label('loc_B79')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300727V#022F哎～不管是什么魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_BF9(): pass

    label('loc_BF9')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C79',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300729V#032F嗯，不管是什么魔兽\n',
            '都好像很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_C79(): pass

    label('loc_C79')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CF6',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300731V#042F是啊，不管是什么魔兽\n',
            '也都很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF6(): pass

    label('loc_CF6')

    OP_28(0x0093, 0x01, 0x0800)

    Jump('loc_CFF')

    def _loc_CFF(): pass

    label('loc_CFF')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D5F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300741V#065F我、我也\n',
            '有那种感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300742V#561F好、好可怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7C')

    def _loc_D5F(): pass

    label('loc_D5F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DBE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300743V#043F我也……\n',
            '有那种感觉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300744V究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7C')

    def _loc_DBE(): pass

    label('loc_DBE')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E1D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300745V#032F我也有\n',
            '同样的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300746V嗯，到底是为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7C')

    def _loc_E1D(): pass

    label('loc_E1D')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E7C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300747V#026F我也有同感啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300748V#522F嗯……\n',
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7C(): pass

    label('loc_E7C')

    ChrTalk(
        0x0106,
        (
            '#0050300749V#057F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300750V#1004F嗯？　怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300751V#555F啊，没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300752V或许这是\n',
            '某种前兆也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300753V#1020F前兆……\n',
            '难道是『结社』！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300754V#552F那就不知道了……\n',
            '不过以前也发生过类似的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300755V魔兽突然就变得\n',
            '仓惶不安…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300756V之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300757V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300758V#1004F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_104A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300759V#063F阿加特哥哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104A(): pass

    label('loc_104A')

    ChrTalk(
        0x0106,
        (
            '#0050300760V#053F算了，目前就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300761V#057F不管怎么说，动物的直觉\n',
            '有时候比人还要更加敏锐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300762V我们也必须准备应付\n',
            '随时可能出现的特殊情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300763V#1002F嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300764V那么…\n',
            '我们暂时先返回协会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300765V#050F啊啊～就这样办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A0F)
    OP_28(0x00B3, 0x01, 0x0001)
    OP_28(0x0093, 0x02, 0x0010)
    OP_28(0x0093, 0x01, 0x0020)
    OP_28(0x0093, 0x01, 0x0040)
    OP_28(0x0093, 0x01, 0x2000)

    Return()

# id: 0x0005 offset: 0x118E
@scena.Code('func_05_118E')
def func_05_118E():
    FadeOut(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1245'),
        (0x00000001, 'loc_124B'),
        (-1, 'loc_1251'),
    )

    def _loc_1245(): pass

    label('loc_1245')

    OP_A2(0x1200)

    Jump('loc_1251')

    def _loc_124B(): pass

    label('loc_124B')

    OP_A2(0x1201)

    Jump('loc_1251')

    def _loc_1251(): pass

    label('loc_1251')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x00FF,
            0x00FF,
        ),
        (
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
