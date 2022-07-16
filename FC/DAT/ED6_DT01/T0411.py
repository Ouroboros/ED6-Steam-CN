import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0411_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0411   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '缇欧'),
    TXT(0x02, '维鲁'),
    TXT(0x03, '查儿'),
    TXT(0x04, '弗兰兹'),
    TXT(0x05, '汉娜'),
    TXT(0x06, '目标用摄像机'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0411.x'
    header.mapIndex       = 13
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1E54
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
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
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
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
    ]

# id: 0x10002 offset: 0x11E
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -75800,
            z                   = 0,
            y                   = 2400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 1730,
            z                   = 0,
            y                   = 24300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 1730,
            z                   = 0,
            y                   = 23000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -39050,
            z                   = 0,
            y                   = 33240,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 1270,
            z                   = 0,
            y                   = 37600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
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

# id: 0x10003 offset: 0x1DE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1DE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1DE
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 0, 0x230)),
            Expr.Return,
        ),
        'loc_218',
    )

    SetChrPos(0x0009, -77350, 0, -1160, 270)
    SetChrPos(0x000A, -71660, 0, 2710, 0)
    SetChrPos(0x0008, 2700, 0, 34460, 180)

    def _loc_218(): pass

    label('loc_218')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_22C'),
        (0x00000070, 'loc_2F1'),
        (0x00000071, 'loc_2F1'),
        (-1, 'loc_309'),
    )

    def _loc_22C(): pass

    label('loc_22C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_294',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0102, 0x0040)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrPos(0x0101, -70500, 0, -32040, 287)
    SetChrPos(0x0102, -70500, 0, -32040, 287)
    CameraMove(-77800, 0, -31130, 0)
    Event(0, 0x000E)

    Jump('loc_2EE')

    def _loc_294(): pass

    label('loc_294')

    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrPos(0x0101, -74500, 0, 2590, 0)
    SetChrPos(0x0102, 735, 0, 23000, 0)
    CameraMove(700, 0, 30000, 0)
    ChrTurnDirection(0x000A, 0x0001, 0)
    ChrTurnDirection(0x0009, 0x0001, 0)
    FadeIn(1000, 0)
    Event(0, 0x000A)

    def _loc_2EE(): pass

    label('loc_2EE')

    Jump('loc_309')

    def _loc_2F1(): pass

    label('loc_2F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 2, 0x232)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_306',
    )

    SetScenaFlags(ScenaFlag(0x0046, 2, 0x232))
    OP_28(0x0002, 0x01, 0x0020)
    Event(0, 0x000D)

    def _loc_306(): pass

    label('loc_306')

    Jump('loc_309')

    def _loc_309(): pass

    label('loc_309')

    Return()

# id: 0x0001 offset: 0x30A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x30B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_320',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_320(): pass

    label('loc_320')

    Return()

# id: 0x0003 offset: 0x321
@scena.Code('func_03_321')
def func_03_321():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 0, 0x230)),
            Expr.Return,
        ),
        'loc_34E',
    )

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34B',
    )

    OP_8D(0x00FE, 560, 22800, 2860, 25700, 3000)

    Jump('loc_328')

    def _loc_34B(): pass

    label('loc_34B')

    Jump('loc_376')

    def _loc_34E(): pass

    label('loc_34E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_376',
    )

    ChrJumpToRelative(0x00FE, 0, 0, 0, 200, 1600)
    Sleep(1000)

    Jump('loc_34E')

    def _loc_376(): pass

    label('loc_376')

    Return()

# id: 0x0004 offset: 0x377
@scena.Code('func_04_377')
def func_04_377():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 0, 0x230)),
            Expr.Return,
        ),
        'loc_3A4',
    )

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A1',
    )

    OP_8D(0x00FE, -1400, 22900, 2600, 25700, 4000)

    Jump('loc_37E')

    def _loc_3A1(): pass

    label('loc_3A1')

    Jump('loc_42F')

    def _loc_3A4(): pass

    label('loc_3A4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_42F',
    )

    ChrWalkTo(0x00FE, 0, 0, 24300, 3000, 0x00)
    ChrWalkTo(0x00FE, 0, 0, 23300, 3000, 0x00)
    ChrWalkTo(0x00FE, 0, 0, 24300, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0102, 0)
    ChrJumpTo(0x00FE, 1730, 0, 24300, 600, 1600)
    ChrTurnDirection(0x00FE, 0x0102, 300)
    ChrJumpTo(0x00FE, 0, 0, 24300, 600, 1600)
    ChrTurnDirection(0x00FE, 0x0102, 300)

    Jump('loc_3A4')

    def _loc_42F(): pass

    label('loc_42F')

    Return()

# id: 0x0005 offset: 0x430
@scena.Code('func_05_430')
def func_05_430():
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '外面已经很暗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们两个要小心呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x465
@scena.Code('func_06_465')
def func_06_465():
    TalkBegin(0x000A)
    ChrTurnDirection(0x00FE, 0x0102, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '嗯，那个……\n',
            '约修亚哥哥要去消灭魔兽吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不害怕吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F没关系啦。\n',
            '我们已经是游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……约修亚好厉害呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_518')

    def _loc_4FE(): pass

    label('loc_4FE')

    ChrTalk(
        0x00FE,
        (
            '……约修亚好厉害呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_518(): pass

    label('loc_518')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x51C
@scena.Code('func_07_51C')
def func_07_51C():
    TalkBegin(0x0009)
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '约修亚哥哥，刚才真开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次再玩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x55A
@scena.Code('func_08_55A')
def func_08_55A():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '虽然那些魔兽\n',
            '不是很凶暴，\n',
            '不过速度相当快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们千万要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x5A7
@scena.Code('func_09_5A7')
def func_09_5A7():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '虽然听缇欧说\n',
            '你们正在以游击士为目标努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过没想到协会\n',
            '会派你们两个来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要小心点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x61A
@scena.Code('func_0A_61A')
def func_0A_61A():
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    PlayBGM(84)
    EventBegin(0x00)
    CameraMove(460, 0, 35390, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrTurnDirection(0x0102, 0x000A, 0)
    CameraMove(460, 0, 24000, 5000)
    ChrTurnDirection(0x0101, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Fade(1000)
    SetChrChipByIndex(0x0101, 5)
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0101, -74100, 350, 2590, 270)
    CameraMove(-75700, 0, 3000, 0)
    CameraSetDistance(2800, 0)
    TerminateThread(0x0102, 0xFF)
    Sleep(1000)

    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)

    ChrTalk(
        0x0101,
        (
            '#0010001398V#001F哈～好饱啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001399V#001F真的太好吃了，\n',
            '汉娜阿姨还是那么会做菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001400V#5P呵呵，每次家里来客人的时候，\n',
            '妈妈她都会干劲十足的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001401V#5P话说回来，\n',
            '今天真是辛苦约修亚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001402V#5P还要他陪小孩子玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001403V#000F哈哈，这不是很好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001404V#000F约修亚和那些小孩子\n',
            '意外地合得来啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001405V#000F明明是那种很拘谨的性格……\n',
            '真有点不可思议呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001406V#5P哎呀，才不是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001407V#5P的确，他总是彬彬有礼，\n',
            '在别人面前甚至可说是拘谨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001408V#5P不过一旦熟识了，\n',
            '就会发现他很会照顾别人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001409V#5P那种不经意间流露出的温柔，\n',
            '更让人觉得很心动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001410V#505F是、是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001411V#5P再加上端正的相貌、\n',
            '神秘的琥珀色眼睛、乌黑的头发……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001412V#5P会引起女生尖叫也是理所当然的啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001413V#004F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001414V#004F约修亚这么受欢迎吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001415V#5P你到现在才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001416V#5P据说想和他交往的\n',
            '女生不止一个两个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001417V#5P不过他好像全部都拒绝掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001418V#007F我、我不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001419V#509F那个约修亚也真是的，\n',
            '什么都不和我说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001420V#509F不知道该说他是神神秘秘呢，\n',
            '还是冷淡无情呢。真是不够意思！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001421V#5P那当然，男孩子也就罢了，\n',
            '这话题怎么能和女孩子谈嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001422V#5P更何况……是和艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001423V#004F啊……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0102, -37400, 0, -3350, 0)
    PlaySE(113, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001424V艾丝蒂尔，可以了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001425V差不多到巡逻的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010001426V#004F啊～嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(100)

    SetChrChipByIndex(0x0101, 65535)
    ChrJumpTo(0x0101, -74830, 0, 2260, 600, 6000)
    ClearChrFlags(0x0101, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010001427V#006F好了，\n',
            '我要去执行任务了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001428V这个话题我们下次再聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001429V#5P啊～那好吧。\n',
            '要小心一点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -74760, 0, 1280, 3000, 0x00)
    ChrWalkTo(0x0101, -71730, 0, -765, 3000, 0x00)
    ChrWalkTo(0x0101, -68700, 0, -1260, 3000, 0x00)
    SetChrPos(0x0101, -37500, 0, -1980, 0)
    PlaySE(6, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    PlaySE(7, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0890001430V#5P这个艾丝蒂尔还是老样子……\n',
            '该说她不懂事呢，还是太迟钝呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001431V#5P这样的话约修亚还真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0000, 0x0001, 0)
    ChrTurnDirection(0x0001, 0x0000, 0)
    Fade(1000)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 0)
    CameraMove(-37800, 0, -2850, 0)
    CameraSetDistance(2600, 0)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020001432V#010F看样子，\n',
            '魔兽似乎总是在这个时间出现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001433V#010F我们这就开始巡逻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001434V#509F………………（盯着看）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001435V#014F怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001436V#009F喂～约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001437V#009F你是不是有什么事情瞒着我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001438V#014F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001439V#014F为什么突然这么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001440V#003F自从约修亚来到这个家……\n',
            '我们俩就一直在一起对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001441V#003F虽然经常吵架，\n',
            '不过这也是美好的回忆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001442V#003F我……\n',
            '一直都把约修亚当作自己真正的家人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001443V#010F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001444V#002F所以呢……\n',
            '如果有什么事情一定要和我说啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001445V#007F我是说……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001446V#503F比如……青春的烦恼之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001447V#018F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001448V#008F不、不说这个了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001449V还是赶快开始巡逻吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x0001, 0x01, 0x00, 0x000B)
    ChrWalkTo(0x0101, -38220, 0, -3400, 5000, 0x00)
    ChrWalkTo(0x0101, -38680, 0, -12270, 6000, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020001450V#017F缇欧都和她说了些什么啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001451V#013F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001452V#013F…………瞒着她……吗………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0046, 0, 0x230))
    OP_28(0x0002, 0x01, 0x0008)
    FadeOut(1000, 0, -1)
    NewScene('ED6_DT01/T0401._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x126F
@scena.Code('func_0B_126F')
def func_0B_126F():
    SetChrDirection(0x0102, 315, 400)
    SetChrDirection(0x0102, 180, 400)

    Return()

# id: 0x000C offset: 0x127E
@scena.Code('func_0C_127E')
def func_0C_127E():
    CameraMove(-2800, 0, 22400, 8000)

    Return()

# id: 0x000D offset: 0x1290
@scena.Code('func_0D_1290')
def func_0D_1290():
    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x70),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12D4',
    )

    SetChrPos(0x0101, 42290, 0, 5450, 270)
    SetChrPos(0x0102, 43520, 0, 4400, 270)
    CameraMove(38110, 0, 5520, 2000)

    Jump('loc_1307')

    def _loc_12D4(): pass

    label('loc_12D4')

    SetChrPos(0x0101, 42150, 0, 35430, 270)
    SetChrPos(0x0102, 43340, 0, 34350, 270)
    CameraMove(37700, 0, 35640, 2000)

    def _loc_1307(): pass

    label('loc_1307')

    ChrTalk(
        0x0102,
        (
            '#0020001468V#012F#1P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001469V#012F果然不在这里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001470V#501F#1P不过，这里感觉很好呢，\n',
            '导力器的光芒有种迷幻般的气氛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001471V#001F心情真舒畅㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001472V#017F#1P你还真是悠闲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001473V#509F#1P是约修亚你太不解风情啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x000E offset: 0x1431
@scena.Code('func_0E_1431')
def func_0E_1431():
    EventBegin(0x00)
    CameraMove(-76360, 0, -31950, 0)
    CameraSetDistance(2600, 0)
    FadeIn(2000, 0)
    Sleep(1000)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ClearChrFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_1486')
    def lambda_1486():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1486)

    @scena.Lambda('lambda_1498')
    def lambda_1498():
        ChrWalkTo(0x00FE, -76240, 0, -31900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1498)

    Sleep(1600)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_14BD')
    def lambda_14BD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14BD)

    ChrWalkTo(0x0101, -74280, 0, -31900, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010001563V#007F哈啊～我快累得不行了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001564V#007F今天已经很晚了，\n',
            '赶快睡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001565V#015F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001566V#000F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001567V#000F怎么了，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001568V#013F…………抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001569V#013F让大家感到不快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001570V#004F啊，是指刚才的事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001571V#001F你真是爱担心～\n',
            '才不会有人那么想呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001572V#001F其实按道理来说，\n',
            '约修亚的主张是正确的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001573V#013F这并不是什么正确。\n',
            '……只是我冷酷无情而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001574V#013F到现在我还是认为，\n',
            '应该毫不留情地把它们杀死才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001575V#013F和艾丝蒂尔、缇欧不一样，\n',
            '我根本没有可怜它们的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001576V#002F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001577V#013F这种时候……\n',
            '我会不由自主地厌恶起自己来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001578V#013F是不是我的人格有缺陷呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001579V#019F哈哈，\n',
            '说不定是心里的某些地方已经坏掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_17F9')
    def lambda_17F9():
        ChrWalkTo(0x00FE, -75300, 0, -31900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_17F9)

    CameraMove(-77400, 0, -31900, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010001580V#005F#5S约修亚是大笨蛋！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001581V#005F你怎么能这样随便对自己下结论呢！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrMoveTo(0x0102, -76500, 0, -31900, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020001582V#014F#5P艾、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001583V#009F这五年来，\n',
            '约修亚的事情我一直看在眼里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001584V#009F好的地方、不好的地方，\n',
            '我有自信比任何人都清楚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001585V#009F说不定比你本人还要清楚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001586V#014F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001587V#005F不要无视我的存在，\n',
            '净说些乱七八糟的话！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001588V#005F坏掉什么的……\n',
            '我绝对不许你那么说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001589V#013F#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001590V#013F抱歉，说了些傻话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001591V#002F知道了就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001592V#002F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001593V#013F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001594V#501F呵呵，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001595V今天我真的有点高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001596V#014F#5P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001597V#003F约修亚你啊，\n',
            '不是一直都自己一个人忍受着吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001598V#003F痛苦的时候，烦恼的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001599V#003F总是装出一副若无其事的样子，\n',
            '一个人去解决问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001600V#500F你每次都这样…… \n',
            '有考虑过我的感受吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001601V#013F#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001602V#013F艾丝蒂尔，我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001603V#006F不过今天，\n',
            '你很坦率地说出了自己的烦恼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001604V#006F这不就意味着，\n',
            '你对我的信赖加深了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001605V#001F所以我觉得很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001606V#018F#5P你、你说什么呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001607V#018F这么难为情的话你也说得出来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001608V#502F嘿嘿，别管这个啦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001609V#006F好了，该睡觉了。\n',
            '今天光是抓那些魔兽就够累的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001610V#015F#5P这也是啊……\n',
            '晚安，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001611V#010F……真的，谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001612V#506F不要客气啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001613V#000F晚安，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    NewScene('ED6_DT01/T0400._SN', 1, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
