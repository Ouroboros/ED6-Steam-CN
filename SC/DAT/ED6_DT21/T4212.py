import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4212_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4212   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4212.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '达扬',
            x                   = -68100,
            z                   = 0,
            y                   = -32320,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '托克斯',
            x                   = -65500,
            z                   = 0,
            y                   = -41540,
            direction           = 279,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '赫穆特',
            x                   = -61160,
            z                   = 0,
            y                   = -35270,
            direction           = 86,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
            x                   = -62490,
            z                   = 0,
            y                   = -31190,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '菲利普',
            x                   = -62170,
            z                   = 0,
            y                   = -33200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = -63350,
            z                   = 0,
            y                   = -33470,
            direction           = 21,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = -65060,
            z                   = 0,
            y                   = -31070,
            direction           = 73,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = -64550,
            z                   = 0,
            y                   = -32810,
            direction           = 48,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '沃尔特议员',
            x                   = -65099,
            z                   = 0,
            y                   = -44670,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10002 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x20A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_22D',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_2B2')

    def _loc_22D(): pass

    label('loc_22D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_292',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetPos(0x000B, -62830, 0, -30860, 220)
    ChrClearFlags(0x000B, 0x0010)
    ChrSetPos(0x000C, -61160, 0, -34980, 335)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetPos(0x0009, -65500, 0, -43300, 165)
    ChrSetFlags(0x0009, 0x0010)

    Jump('loc_2B2')

    def _loc_292(): pass

    label('loc_292')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2A1',
    )

    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_2B2')

    def _loc_2A1(): pass

    label('loc_2A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2B2',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 0, 0x20F0)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D5',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0B_1086)

    def _loc_2D5(): pass

    label('loc_2D5')

    Return()

# id: 0x0001 offset: 0x2D6
@scena.Code('func_01_2D6')
def func_01_2D6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F2',
    )

    OP_B1('t4212_y')

    Jump('loc_2FB')

    def _loc_2F2(): pass

    label('loc_2F2')

    OP_B1('t4212_n')

    def _loc_2FB(): pass

    label('loc_2FB')

    Return()

# id: 0x0002 offset: 0x2FC
@scena.Code('func_02_2FC')
def func_02_2FC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B9',
    )

    ChrTalk(
        0x00FE,
        (
            '因为导力器完全不能用了，\n',
            '来申诉的市民很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵不在的话还真会\n',
            '有一点点忙不过来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话虽如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器停止之后\n',
            '要估算经济损失的话光是王都\n',
            '就相当严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_512')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_466',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，被改动的\n',
            '预算谜团终于解开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来似乎消失了的预算\n',
            '是用作奥尔杰尤的开发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变时那东西如果完成的话\n',
            '会变成怎样呢？。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真让人有点后怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_512')

    def _loc_466(): pass

    label('loc_466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_512',
    )

    ChrTalk(
        0x00FE,
        (
            '政变的善后处理\n',
            '看来还得持续一阵子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在在调查情报部过去的\n',
            '预算和实际的经费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看看这个就知道预算有\n',
            '被大幅度改动的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这笔钱消失去了哪里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_512(): pass

    label('loc_512')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x516
@scena.Code('func_03_516')
def func_03_516():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5AA',
    )

    ChrTalk(
        0x00FE,
        (
            '我都说了，导力停止的\n',
            '原因现在还在调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾莉茜雅女王也很忙，\n',
            '现在不能马上见你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果我们有什么发现\n',
            '会联络大使馆的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BB')

    def _loc_5AA(): pass

    label('loc_5AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_623',
    )

    ChrTalk(
        0x00FE,
        (
            '凯诺娜上尉被捕\n',
            '是件好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这次为了修理港湾设施，\n',
            '还要追加预算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，拜托，\n',
            '别再有下次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BB')

    def _loc_623(): pass

    label('loc_623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_6BB',
    )

    ChrTalk(
        0x00FE,
        (
            '业务倒是逐渐地在正常化，\n',
            '不过还是很忙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市民们对政变\n',
            '提的问题也还很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我负责做出各种各样的补偿，\n',
            '不过总之问题还是堆积如山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BB(): pass

    label('loc_6BB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x6BF
@scena.Code('func_04_6BF')
def func_04_6BF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_754',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，我老婆这时候\n',
            '大概在热衷于钓鱼吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去别说男的尊严了，\n',
            '连丈夫的位置都危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，悄悄特训一下，\n',
            '一定要赶上老婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_754(): pass

    label('loc_754')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x758
@scena.Code('func_05_758')
def func_05_758():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_829',
    )

    ChrTalk(
        0x000B,
        (
            '#0640371145V#223F你们是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371146V#220F要见陛下和科洛蒂娅\n',
            '现在应该还不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371147V想知道详细原因\n',
            '可以去问希尔丹夫人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371148V抱歉，我从早到晚\n',
            '都要应对请愿团……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_8C5')

    def _loc_829(): pass

    label('loc_829')

    ChrTalk(
        0x000B,
        (
            '#0640371146V#220F要见陛下和科洛蒂娅\n',
            '现在应该还不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371150V想知道详细原因\n',
            '可以去问希尔丹夫人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371151V抱歉，我从早到晚\n',
            '都要应对请愿团……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C5(): pass

    label('loc_8C5')

    Jump('loc_A65')

    def _loc_8C8(): pass

    label('loc_8C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_A65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 1, 0x1669)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A08',
    )

    ChrTalk(
        0x000B,
        (
            '#0640271431V#222F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640271432V那些不明\n',
            '身份的人在进出\n',
            '利贝尔吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640271433V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271434V#1011F（哟，一副平时见不到的认真表情呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060271435V#040F（因为这次的事件，叔叔\n',
            '　好像深刻地认识到结社的存在。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060271436V（可能叔叔他也有\n',
            '　自己的想法呢。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CD, 1, 0x1669))

    Jump('loc_A65')

    def _loc_A08(): pass

    label('loc_A08')

    ChrTalk(
        0x000B,
        (
            '#0640271437V#222F那些不明\n',
            '身份的人在进出\n',
            '利贝尔吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640271433V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A65(): pass

    label('loc_A65')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xA69
@scena.Code('func_06_A69')
def func_06_A69():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 1, 0x20F1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C49',
    )

    ChrTalk(
        0x00FE,
        (
            '#0660371152V#721F哟，这不是\n',
            '艾丝蒂尔小姐和约修亚先生吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371153V#1040F菲利普先生，\n',
            '实在久疏问候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371154V是诞辰庆典之后到现在了吧……\n',
            '您的身体还是如此安康，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0660371155V#720F嗯，承蒙你们的关心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660371156V约修亚先生不在时，\n',
            '我和大人都受到了\n',
            '艾丝蒂尔小姐的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371157V#1044F艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371158V#1008F说得我都不好意思了，我可\n',
            '没做什么了不起的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371159V#1040F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041E, 1, 0x20F1))

    Jump('loc_C97')

    def _loc_C49(): pass

    label('loc_C49')

    ChrTalk(
        0x00FE,
        (
            '#0660371160V#720F大人这次终于\n',
            '有了干劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660371161V希望能持续下去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C97(): pass

    label('loc_C97')

    Jump('loc_F10')

    def _loc_C9A(): pass

    label('loc_C9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_F10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 2, 0x166A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED4',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0660271439V#720F哟，这不是艾丝蒂尔小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271440V#1000F菲利普先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0660271441V#720F非常感谢您上次\n',
            '搭救大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271442V#1018F我还要感谢菲利普先生\n',
            '您照顾了大家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0660271443V#722F不敢当，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660271444V我只能以那种方式帮助你们，\n',
            '真是太惭愧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271445V#1015F可我们也是因为\n',
            '有菲利普先生在\n',
            '才能安心地去了港口……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271446V#1001F从这层意义上来说，\n',
            '能搭救公爵是托了\n',
            '菲利普先生的福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0660271447V#721F艾丝蒂尔小姐……\n',
            '您太抬举我了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660271448V#720F希望趁此机会\n',
            '大人能够改变行事作风……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CD, 2, 0x166A))

    Jump('loc_F10')

    def _loc_ED4(): pass

    label('loc_ED4')

    ChrTalk(
        0x00FE,
        (
            '#0660271448V#720F希望趁此机会\n',
            '大人能够改变行事作风……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F10(): pass

    label('loc_F10')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xF14
@scena.Code('func_07_F14')
def func_07_F14():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F72',
    )

    ChrTalk(
        0x00FE,
        (
            '看来杜南公爵远比我们想象中的\n',
            '了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过发型却和传闻一样\n',
            '果然是很……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F72(): pass

    label('loc_F72')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xF76
@scena.Code('func_08_F76')
def func_08_F76():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FCC',
    )

    ChrTalk(
        0x00FE,
        (
            '我得知王室\n',
            '也在那么拼命应对之后\n',
            '就放心多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也得继续加油了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FCC(): pass

    label('loc_FCC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xFD0
@scena.Code('func_09_FD0')
def func_09_FD0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1005',
    )

    ChrTalk(
        0x00FE,
        (
            '原来如此，女王陛下也\n',
            '考虑得很周到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1005(): pass

    label('loc_1005')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1009
@scena.Code('func_0A_1009')
def func_0A_1009():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1082',
    )

    ChrTalk(
        0x00FE,
        (
            '我、我是共和国议会\n',
            '议员沃尔特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做、做好必要的准备\n',
            '总没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我到底什么时候\n',
            '能和本国取得联系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1082(): pass

    label('loc_1082')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1086
@scena.Code('func_0B_1086')
def func_0B_1086():
    EventBegin(0x00)
    CameraMove(-62620, 0, -30760, 0)
    OP_67(0, 5140, -10000, 0)
    CameraSetDistance(2970, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -62430, 0, -40080, 0)
    ChrSetPos(0x0102, -63520, 0, -40530, 0)
    ChrSetPos(0x00F8, -61650, 0, -40780, 0)
    ChrSetPos(0x00F9, -62780, 0, -41900, 0)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#4120371126V导力停止之后，\n',
            '夜晚又冷又暗，\n',
            '做饭也不方便……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4140371127V总之每天\n',
            '都很不安！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4130371128V王室今后究竟\n',
            '怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0640371129V#225F#5P啊～咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371130V#222F关于导力停止现象，\n',
            '正在以王国军为中心进行调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371131V详细情况\n',
            '目前还不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4140371132V太不负责任了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0640371133V#222F#5P算了，冷静点。\n',
            '确实还有很多事是不明原因的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371134V正因为如此，女王希望\n',
            '我们和市民全力配合，\n',
            '尽到最大的努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371135V#225F比如东街区的历史资料馆───\n',
            '为了使市民能尽量放松\n',
            '而免费开放着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371136V#220F另外在陛下的援助保证下，\n',
            '餐饮店也尽量不关门，\n',
            '努力保持着营业状态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371137V我们通过这些方式来\n',
            '平复市民们的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640371138V另外在关键时刻可以把\n',
            '亚宁堡当作避难所……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(1000)
    CameraMove(-61920, 0, -38980, 0)
    OP_67(0, 6840, -10000, 0)
    CameraSetDistance(2940, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010371139V#1004F#4P好、好像公爵在说些\n',
            '非常像模像样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010371140V#1015F是吗？就像武术大会时\n',
            '被人支使的一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020371141V#1040F#6P不，那不是打招呼，\n',
            '并不是事先准备好\n',
            '然后说一通的那种……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371142V明显是以他自己的意志为基础\n',
            '说出来的属于他自己的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020371143V公爵好像是因为某种原因\n',
            '而开始改变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010371144V#1015F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    SetScenaFlags(ScenaFlag(0x041E, 0, 0x20F0))
    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
