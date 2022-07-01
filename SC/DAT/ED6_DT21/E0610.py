import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0610_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0610   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '幻惑之铃露茜奥拉'),
    TXT(0x02, '瘦狼瓦鲁特'),
    TXT(0x03, '小丑肯帕雷拉'),
    TXT(0x04, '红莲士兵'),
    TXT(0x05, '红莲士兵'),
    TXT(0x06, '红莲士兵'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0610.x'
    header.mapIndex       = 1
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3894
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
        ('ED6_DT27/CH03523._CH', 'ED6_DT27/CH03523P._CP'),
        ('ED6_DT27/CH03503._CH', 'ED6_DT27/CH03503P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT26/CH20396._CH', 'ED6_DT26/CH20396P._CP'),
        ('ED6_DT26/CH20387._CH', 'ED6_DT26/CH20387P._CP'),
        ('ED6_DT26/CH20392._CH', 'ED6_DT26/CH20392P._CP'),
    ]

# id: 0x10002 offset: 0xDA
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
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1B9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0002)

    Jump('loc_27D')

    def _loc_1B9(): pass

    label('loc_1B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1D3',
    )

    OP_A3(0x10F1)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0003)

    Jump('loc_27D')

    def _loc_1D3(): pass

    label('loc_1D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_1ED',
    )

    OP_A3(0x10F2)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0004)

    Jump('loc_27D')

    def _loc_1ED(): pass

    label('loc_1ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_207',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F3)
    Event(0, 0x0005)

    Jump('loc_27D')

    def _loc_207(): pass

    label('loc_207')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_221',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F4)
    Event(0, 0x0008)

    Jump('loc_27D')

    def _loc_221(): pass

    label('loc_221')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_23B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F5)
    Event(0, 0x0009)

    Jump('loc_27D')

    def _loc_23B(): pass

    label('loc_23B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_255',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F6)
    Event(0, 0x000A)

    Jump('loc_27D')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Return,
        ),
        'loc_26F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F7)
    Event(0, 0x000B)

    Jump('loc_27D')

    def _loc_26F(): pass

    label('loc_26F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 0, 0x10F8)),
            Expr.Return,
        ),
        'loc_27D',
    )

    OP_A3(0x10F8)
    Event(0, 0x000C)

    def _loc_27D(): pass

    label('loc_27D')

    Return()

# id: 0x0001 offset: 0x27E
@scena.Code('Init')
def Init():
    OP_22(0x007A, 0x01, 0x46)

    Return()

# id: 0x0002 offset: 0x284
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-2140, 0, 2420, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(315000, 0)
    OP_6E(522, 0)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrChipByIndex(0x0008, 0)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0008, 1)
    SetChrSubChip(0x0009, 2)
    SetChrPos(0x0008, -630, 300, 2150, 180)
    SetChrPos(0x0009, 1130, 300, 2150, 180)
    SetChrPos(0x000A, -2470, 0, 1930, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210300021V#240F#5P──所谓的最后实验，\n',
            '对手就是『那个东西』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300022V就算是教授和莱维，\n',
            '也没有办法轻松地解决呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0200300023V#250F#2P呵呵，或许是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300024V怎么说都是传说般的存在。\n',
            '强度完全不在一个档次上啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300025V#252F……但是肯帕雷拉啊。\n',
            '这可不像是你的作风啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0475')
    def lambda_0475():
        OP_8C(0x000A, 90, 300)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0475)

    Sleep(200)

    SetChrSubChip(0x0008, 0)
    Sleep(100)

    SetChrSubChip(0x0008, 2)
    Sleep(200)

    ChrTalk(
        0x000A,
        (
            '#0190300026V#850F#5P哎呀呀，什么地方不像？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0200300027V#252F#2P要是平常的你，\n',
            '应该会很乐意和教授同行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300028V既然你这次没有这么做，\n',
            '肯定是有其他更有趣的事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300029V赶快从实招了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0190300030V#852F#5P讨厌啦，瓦鲁特。\n',
            '就那么不信任我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0200300031V#252F#2P呵呵，信任啊。\n',
            '你的信用就像你的编号一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210300032V#241F#2PＮｏ．０──\n',
            '呵呵，也就是信用为零啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0190300033V#855F#5P哎呀哎呀，你们两个好过分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190300034V#850F嗯，虽然我确实很想跟着去看看，\n',
            '但真是不凑巧，现在有更紧急的工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190300035V我打算向那位大人申请\n',
            '方舟的使用许可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0200300036V#253F#2P哈哈哈！真的假的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300037V居然要\n',
            '使用那种怪物啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210300038V#244F#2P『红色方舟』──古罗力亚斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300039V#242F你该不会……\n',
            '打算把利贝尔化为焦土吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0190300040V#854F#5P呼呼，那就要看\n',
            '教授和莱维怎么决定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 0, 300)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0190300041V#853F#5P所以说，我待会儿\n',
            '就必须马上出去一趟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190300042V实验的经过，等回来之后\n',
            '再慢慢讲给我听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C1600._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x8BB
@scena.Code('func_03_8BB')
def func_03_8BB():
    EventBegin(0x00)
    OP_24(0x007A, 0x46)
    SetChrFlags(0x0102, 0x0080)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, -70600, 1300, -160, 270)
    SetChrPos(0x000C, -70600, 1200, 2150, 270)
    SetChrPos(0x000D, -70600, 1200, -2500, 270)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000D, 0)
    OP_76(0x0004, 0x00000000, 0x0001, 0xFFFFFFFA, 0xFFFFFFFD, 0x00000000, 0x00, 0x00)
    OP_76(0x0004, 0x00000001, 0x0001, 0xFFFFFFF8, 0xFFFFFFFB, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_0997')
    def lambda_0997():
        OP_7C(0x0000000A, 0x0000000A, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_0997')

    DispatchAsync2(0x0101, 0x0003, lambda_0997)

    OP_71(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#4210320119V──高度１５５９亚矩。\n',
            '由北东方向潜入利贝尔的领土内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4210320120V在抵达瓦雷利亚湖上空之前\n',
            '就这样保持航向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#4220320121V明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000C, 1)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#4220320122V利贝尔的警备艇\n',
            '似乎没察觉到我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#4220320123V『隐形机能』吗……\n',
            '实在是个很方便的装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x000D, 2)
    Sleep(300)

    ChrTalk(
        0x000D,
        (
            '#4230320124V#6P不过，要不是有这隐形机能\n',
            '那可就要引起大骚动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4230320125V#6P这艘飞船还不算什么，\n',
            '等到那个怪物入侵的那天……。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#4220320126V哈哈，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000000)
    TerminateThread(0x0101, 0x03)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x000003E8)
    OP_22(0x01F7, 0x00, 0x55)
    Sleep(100)

    OP_22(0x01FA, 0x00, 0x55)
    Sleep(900)

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_22(0x01F7, 0x00, 0x55)
    Sleep(500)

    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x000003E8)
    OP_22(0x01FA, 0x00, 0x55)
    Sleep(1000)

    @scena.Lambda('lambda_0C42')
    def lambda_0C42():
        OP_7C(0x0000000A, 0x0000000A, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_0C42')

    DispatchAsync2(0x0101, 0x0003, lambda_0C42)

    SetChrSubChip(0x000C, 0)
    Sleep(100)

    ChrTalk(
        0x000D,
        (
            '#4230320127V#6P什…么…！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000D, 0)
    Sleep(100)

    ChrTalk(
        0x000C,
        (
            '#4220320128V是敌袭吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_1D(0x59)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#4210320129V#5P别慌张！\n',
            '雷达怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#4220320130V雷达有反应！\n',
            '４点钟方向有小型艇接近！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4230320131V#6P数据库比对──有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4230320132V#6P是帝国莱恩福尔特社制造的飞船。\n',
            '『卡普亚空贼团』所属的山猫号！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4210320133V#5P空贼！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0xDC7
@scena.Code('func_04_DC7')
def func_04_DC7():
    EventBegin(0x00)
    OP_24(0x007A, 0x64)
    SetChrFlags(0x0102, 0x0080)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, -70600, 1300, -160, 270)
    SetChrPos(0x000C, -70600, 1200, 2150, 270)
    SetChrPos(0x000D, -70600, 1200, -2500, 270)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000D, 0)
    OP_76(0x0004, 0x00000000, 0x0001, 0xFFFFFFFA, 0xFFFFFFFD, 0x00000000, 0x00, 0x00)
    OP_76(0x0004, 0x00000001, 0x0001, 0xFFFFFFF8, 0xFFFFFFFB, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_0EA3')
    def lambda_0EA3():
        OP_7C(0x00000014, 0x00000014, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_0EA3')

    DispatchAsync2(0x0101, 0x0003, lambda_0EA3)

    OP_71(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#4220320139V空贼艇，脱离了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4230320140V#6P怎么办、要追击吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4210320141V#5P不……别去管它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4210320142V#5P王国军的警备艇也就罢了，\n',
            '现在不是和小角色纠缠的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4230320143V#6P没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#4220320144V现在以确保『古罗力亚斯』\n',
            '的航线为最优先任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4210320145V#5P……暂时先返航吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4210320146V#5P将空贼的情况\n',
            '汇报给肯帕雷拉大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x02000000)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x1068
@scena.Code('func_05_1068')
def func_05_1068():
    EventBegin(0x00)
    OP_23(0x007A)
    OP_6D(2150, 0, 700, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_74(0x00FF, 0x00000006, 0x0008)
    OP_75(0xFF, 0x00000006, 0x00)
    FadeIn(1000, 0)
    CreateThread(0x0102, 0x01, 0x00, 0x0006)
    Sleep(1500)

    CreateThread(0x0101, 0x01, 0x00, 0x0007)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020330798V#1032F#5P锁上门。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330799V我马上让飞船出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330800V#1005F明、明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 270, 600)

    @scena.Lambda('lambda_1172')
    def lambda_1172():
        OP_8C(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1172)

    @scena.Lambda('lambda_1180')
    def lambda_1180():
        OP_8E(0x00FE, -3170, 0, -90, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1180)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_11A0')
    def lambda_11A0():
        OP_8E(0x00FE, 5750, 0, -10, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11A0)

    WaitForThreadExit(0x0102, 0x0001)
    OP_72(0x0002, 0x0010)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000000F)
    OP_22(0x006D, 0x00, 0x64)
    OP_73(0x0002)
    FadeOut(1000, 0, -1)

    @scena.Lambda('lambda_11EA')
    def lambda_11EA():
        OP_8E(0x00FE, -5870, 0, 140, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_11EA)

    Sleep(100)

    OP_9F(0x0102, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x0102, 0x0080)
    OP_0D()
    Sleep(1500)

    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0102, 0x01)
    OP_9F(0x0102, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    ClearChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0102, 0x0004)
    SetChrChipByIndex(0x0102, 4)
    SetChrSubChip(0x0102, 0)
    SetChrPos(0x0102, -70600, 1200, -220, 270)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020330801V#1033F#5P（启动钥匙认证……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330802V（输入认证编码……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330803V#1035F（……好了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x009D, 0x00, 0x64)
    OP_75(0xFF, 0x00000006, 0x02)
    OP_74(0x00FF, 0x00000006, 0x0008)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x0009)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x000A)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x000B)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x000C)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x000D)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x000E)
    Sleep(100)

    OP_74(0x00FF, 0x00000006, 0x000F)
    Sleep(100)

    OP_75(0xFF, 0x00000006, 0x02)
    Sleep(1000)

    @scena.Lambda('lambda_13A0')
    def lambda_13A0():
        OP_6D(-69000, 1000, 300, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13A0)

    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0101, -63530, 0, -80, 270)

    @scena.Lambda('lambda_13D4')
    def lambda_13D4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13D4)

    OP_8E(0x0101, -66290, 0, -50, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330804V#1004F#4P哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0102, 1)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020330805V#1031F#5P我用远程操控来打开舱口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330806V马上就要出发了，快坐好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330807V#1006F#4P……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5406._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x14BF
@scena.Code('func_06_14BF')
def func_06_14BF():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 7480, 0, -60, 270)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_14E6')
    def lambda_14E6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_14E6)

    OP_8E(0x00FE, 2000, 0, -60, 4000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0007 offset: 0x150E
@scena.Code('func_07_150E')
def func_07_150E():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 7480, 0, -60, 270)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1535')
    def lambda_1535():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1535)

    OP_8E(0x00FE, 5000, 0, -60, 4000, 0x00)

    Return()

# id: 0x0008 offset: 0x1556
@scena.Code('func_08_1556')
def func_08_1556():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_24(0x007A, 0x64)
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, -70610, 1200, 30, 270)
    SetChrPos(0x0101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_76(0x0003, 0x00000000, 0x0001, 0x00000000, 0x00000004, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0x00000000, 0x0000000C, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_161C')
    def lambda_161C():
        OP_7C(0x0000003C, 0x0000003C, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_161C')

    DispatchAsync2(0x0101, 0x0002, lambda_161C)

    OP_D0(5000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330810V#1020F掉、掉下去了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330811V#1031F#6P没关系……\n',
            '马上就会调整过来。',
            TxtCtl.Enter,
        ),
    )

    OP_D0(4000, 0)
    Sleep(500)

    OP_D0(3000, 0)
    Sleep(500)

    OP_D0(2000, 0)
    Sleep(500)

    OP_D0(1000, 0)
    Sleep(500)

    OP_D0(0, 0)
    Sleep(500)

    @scena.Lambda('lambda_16F4')
    def lambda_16F4():
        OP_7C(0x00000014, 0x00000014, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_16F4')

    DispatchAsync2(0x0101, 0x0002, lambda_16F4)

    ChrTalk(
        0x0102,
        (
            '#0020330812V#1035F#6P#20A……好。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    OP_DB()
    Fade(500)
    OP_76(0x0003, 0x00000000, 0x0001, 0x00000000, 0x00000003, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0x00000000, 0x00000009, 0x00000000, 0x00, 0x00)
    OP_0D()
    Sleep(200)

    Fade(500)
    OP_76(0x0003, 0x00000000, 0x0001, 0x00000000, 0x00000001, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0x00000000, 0x00000003, 0x00000000, 0x00, 0x00)
    OP_0D()
    Sleep(200)

    Fade(500)
    OP_76(0x0003, 0x00000000, 0x0001, 0x00000000, 0x00000001, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0x00000000, 0x00000002, 0x00000000, 0x00, 0x00)
    OP_0D()
    Sleep(200)

    Fade(500)
    OP_76(0x0003, 0x00000000, 0x0001, 0x00000000, 0x00000000, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0x00000000, 0x00000000, 0x00000000, 0x00, 0x00)
    OP_0D()
    Sleep(200)

    Fade(500)
    OP_76(0x0003, 0x00000000, 0x0001, 0x00000000, 0xFFFFFFFF, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0x00000000, 0xFFFFFFFE, 0x00000000, 0x00, 0x00)
    OP_0D()
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DB()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/C5408._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x186C
@scena.Code('func_09_186C')
def func_09_186C():
    EventBegin(0x00)
    OP_24(0x007A, 0x64)
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, -70610, 1200, 30, 270)
    SetChrPos(0x0101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_76(0x0003, 0x00000000, 0x0001, 0xFFFFFFFA, 0xFFFFFFFD, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0xFFFFFFF8, 0xFFFFFFFB, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_1928')
    def lambda_1928():
        OP_7C(0x00000014, 0x00000014, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_1928')

    DispatchAsync2(0x0101, 0x0003, lambda_1928)

    FadeIn(1000, 0)
    OP_0D()
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00AB, 0x00, 0x64)
    Sleep(800)

    OP_22(0x00AB, 0x00, 0x64)
    Sleep(800)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_22(0x00AB, 0x00, 0x64)
    Sleep(800)

    Sleep(200)

    SetChrSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010330815V#1020F#2P哇哇……\n',
            '这个是雷达吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330816V有三个光点\n',
            '朝我们接近了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330817V#1030F#6P嗯，是追兵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330818V看来要想办法\n',
            '将他们甩掉才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330819V#1015F#2P约修亚……\n',
            '原来你会操纵飞艇啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330820V#1031F#6P还好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330821V#1035F只是，这艘飞船\n',
            '并没有配备武器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330822V所以情况不容乐观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330823V#1007F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330824V#1004F可是，为什么会特地\n',
            '找了一艘没有武装的飞船呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330825V#1033F#6P……只有这艘正在维修的船，\n',
            '安全防范措施比较薄弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330826V因为当时事态紧急，\n',
            '也没有选择的余地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330827V#1015F#2P事态紧急……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330828V#1026F#2P那个……莫非是指……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330829V我被捉到\n',
            '『古罗力亚斯』的事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330830V#1035F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330831V#1031F没空说闲话了，\n',
            '会有些摇晃，当心点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x01FA, 0x01, 0x50)

    @scena.Lambda('lambda_1D2A')
    def lambda_1D2A():
        OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_1D2A')

    DispatchAsync2(0x0101, 0x0003, lambda_1D2A)

    Sleep(1000)

    OP_22(0x01FA, 0x01, 0x5A)

    @scena.Lambda('lambda_1D4F')
    def lambda_1D4F():
        OP_7C(0x00000000, 0x00000096, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_1D4F')

    DispatchAsync2(0x0101, 0x0003, lambda_1D4F)

    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010330832V#1020F#2P哇哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F9)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x1DBD
@scena.Code('func_0A_1DBD')
def func_0A_1DBD():
    EventBegin(0x00)
    OP_24(0x007A, 0x64)
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, -70610, 1200, 30, 270)
    SetChrPos(0x0101, -70590, 1200, 2020, 270)
    OP_6D(-71670, 900, 1010, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_6D(-72410, 1200, 1310, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_76(0x0003, 0x00000000, 0x0001, 0xFFFFFFFA, 0xFFFFFFFD, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0xFFFFFFF8, 0xFFFFFFFB, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_1EB6')
    def lambda_1EB6():
        OP_7C(0x00000014, 0x00000014, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_1EB6')

    DispatchAsync2(0x0101, 0x0003, lambda_1EB6)

    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020330833V#1032F#6P可恶……真糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330834V#1002F#2P追击我们的这些家伙\n',
            '相当有一手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330835V#1035F#6P应该是使用『结社』的\n',
            '强化程序学会了操纵技术吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330836V虽然还无法灵活应用，\n',
            '不过单方面追击还真不好对付。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330837V#1007F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330838V#1015F但是，既然应用上还不行，\n',
            '也就代表如果发生什么意外的话──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x01FE, 0x00, 0x50)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330839V#1004F#2P中、中弹了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330840V#1034F#6P不……\n',
            '不是我们的船！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FA)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x2136
@scena.Code('func_0B_2136')
def func_0B_2136():
    EventBegin(0x00)
    OP_24(0x007A, 0x64)
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, -70610, 1200, 30, 270)
    SetChrPos(0x0101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_76(0x0003, 0x00000000, 0x0001, 0xFFFFFFFA, 0xFFFFFFFD, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0xFFFFFFF8, 0xFFFFFFFB, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_21F2')
    def lambda_21F2():
        OP_7C(0x00000014, 0x00000014, 0x00000BB8, 0x00000064)
        Yield()

        Jump('lambda_21F2')

    DispatchAsync2(0x0101, 0x0003, lambda_21F2)

    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010330841V#1020F#2P那、那是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330842V#1034F#6P『山猫号』……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x009D, 0x00, 0x46)
    Sleep(1000)

    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName('扩音器的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0090330843V……约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('扩音器的声音')

    Talk(
        (
            '#0090330844V那艘船里的\n',
            '是约修亚吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330845V#1019F#2P（这声音……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330846V#1031F#6P啊啊……我在这里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330847V为什么你们会\n',
            '在这里呢！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330848V我还以为你们早就\n',
            '离开利贝尔了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName('乔丝特')

    Talk(
        (
            '#0090330849V嘿嘿，是哥哥他们担心\n',
            '你会不会遇上什么困难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090330850V于是就一直在远处观察\n',
            '那艘庞然大物的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName('吉尔')

    Talk(
        (
            '#0290330851V哈哈，还真敢说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290330852V当初拼命在拜托我们的人\n',
            '到底是谁啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName('乔丝特')

    Talk(
        (
            '#0090330853V吉、吉尔哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName('多伦')

    Talk(
        (
            '#0300330854V算啦，反正我们和『结社』\n',
            '也有不少帐要算。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300330855V等到全数奉还后\n',
            '再离开利贝尔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0102,
        (
            '#0020330856V#1035F#6P……是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330857V#1031F谢谢你们，真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName('乔丝特')

    Talk(
        (
            '#0090330858V嘿嘿……\n',
            '你可要好好感谢我们哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName('吉尔')

    Talk(
        (
            '#0290330859V不过，刚才一路看下来，\n',
            '你好像没有进行反击呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290330860V出了什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0102,
        (
            '#0020330861V#1035F#6P因为我只弄到\n',
            '一艘没有武装的飞船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330862V所以稍微有点麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName('吉尔')

    Talk(
        (
            '#0290330863V是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName('乔丝特')

    Talk(
        (
            '#0090330864V怎、怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName('多伦')

    Talk(
        (
            '#0300330865V…好～这样的话\n',
            '那就兵分两路吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300330866V只有一艘的话你应该甩得掉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0102,
        (
            '#0020330867V#1031F#6P嗯……没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName('吉尔')

    Talk(
        (
            '#0290330868V那好，愿女神保佑你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName('乔丝特')

    Talk(
        (
            '#0090330869V约修亚……\n',
            '一定要小心哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FB)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x287D
@scena.Code('func_0C_287D')
def func_0C_287D():
    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 5)
    SetChrChipByIndex(0x0102, 4)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, -70610, 1200, 30, 270)
    SetChrPos(0x0101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_76(0x0003, 0x00000000, 0x0001, 0xFFFFFFFA, 0xFFFFFFFD, 0x00000000, 0x00, 0x00)
    OP_76(0x0003, 0x00000001, 0x0001, 0xFFFFFFF8, 0xFFFFFFFB, 0x00000000, 0x00, 0x00)

    @scena.Lambda('lambda_2935')
    def lambda_2935():
        OP_7C(0x00000001, 0x00000001, 0x000007D0, 0x00000064)
        Yield()

        Jump('lambda_2935')

    DispatchAsync2(0x0101, 0x0003, lambda_2935)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    Sleep(100)

    SetChrSubChip(0x0102, 2)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020330870V#1031F#6P#6P艾丝蒂尔，雷达上怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010330871V#1006F#2P嗯……\n',
            '光点已经消失了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330872V看来是完全甩开了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330873V#1031F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330874V#1033F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330875V#1013F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0102)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330876V#1008F#2P嗯、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330877V#1016F那些空贼，\n',
            '是一群挺不错的人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330878V真没想到他们竟会在这种时候\n',
            '跑过来帮助我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330879V#1017F真是要另眼相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330880V#1033F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330881V#1031F契约上的关系\n',
            '虽然已经解除……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330882V但人与人的感情\n',
            '似乎就没那么单纯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330883V#1016F#2P啊哈哈……\n',
            '你到现在才明白这些吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330884V#1006F随着一次次的相遇，\n',
            '时而欢喜，时而争吵，\n',
            '而彼此之间的感情也会不断加深。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330885V这就是人与人之间的交往吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280182V#1035F#6P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330887V#1030F但是在我生存过的世界里，\n',
            '这些东西并非是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330888V#1020F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    Sleep(500)

    SetChrSubChip(0x0102, 0)
    OP_21()
    OP_1D(0x5B)
    Sleep(500)

    @scena.Lambda('lambda_2D62')
    def lambda_2D62():
        OP_6B(2730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D62)

    Sleep(1500)

    ChrTalk(
        0x0102,
        (
            '#0020330889V#1035F#6P杀人，或是被杀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330890V抢夺，或是被抢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330891V我在遇到你之前，\n',
            '只是一直重复着这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330892V#1026F#2P但、但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330893V#1003F你也有过和姐姐、莱维\n',
            '生活在一起的幸福时光吧……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330894V#1033F#6P……莱维和你说的吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330895V#1035F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330896V#1045F那段记忆虽然还在，\n',
            '但对我来说，就像是别人的经历一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330897V#1026F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330898V#1031F#6P我的心灵崩溃的时候……\n',
            '在哈梅尔的那些回忆，\n',
            '就已经不属于我自己了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330899V自那之后，我就已经不再是人，\n',
            '只是一个会呼吸的木偶而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330900V#1026F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330901V#1031F#6P姐姐死去时的状况，\n',
            '至今仍然记忆犹新。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330902V#1035F那个时候，我和姐姐\n',
            '遭到了伏击男子的偷袭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330903V那男人把我打飞……\n',
            '整个人压在姐姐上面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330904V#1020F#2P…………！………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330905V#1033F#6P年幼的我，虽然不明白\n',
            '那意味着什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330906V但心中还是感到厌恶，\n',
            '上前揪住那人的后背。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330907V#1035F我们两人打成一团，\n',
            '结果我马上就被弹开……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330908V但不知何时，我的手中\n',
            '已经握着那男子的枪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330909V#1026F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330910V#1045F#6P现在回想起来，那时的我\n',
            '大概就已经具备杀人的才能了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330911V虽然从来都没学过，\n',
            '但我却迅速地拉开了保险栓，\n',
            '并毫不犹豫地扣动了扳机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330912V喉咙被打穿的男子\n',
            '满脸诧异地望着我，\n',
            '口中吐出了鲜血。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330913V直到这时，我才终于意识到\n',
            '自己开枪杀了人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211824V#1003F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330915V#1032F#6P但是，那男子还没断气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330916V他眼中充满血丝，\n',
            '不停地喘着粗气，\n',
            '接着抽出军刀就向我扑来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330917V#1033F就像面对野兽袭击一样，\n',
            '我不禁蜷起身体闭上了双眼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330918V#1035F但我却没有感受到任何冲击，\n',
            '而是有什么柔软的东西紧紧抱住了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330919V#1026F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330920V#1033F#6P当我睁开双眼时，\n',
            '首先映入眼帘的是姐姐微笑的面容。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330921V那男子不知在何时已经倒下了……\n',
            '而莱维就在一旁呆呆地站着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330922V姐姐在被莱维扶起之后，\n',
            '便将自己的口琴交给了我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330923V#1035F然后缓缓闭上了双眼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330374V#1027F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330925V#1035F#6P……记得很清楚对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330926V#1045F但是，就算这样说出来，\n',
            '我也感觉不到哀伤和痛苦，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330927V就像在读别人的日记一样。\n',
            '实在是不可思议呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330928V#1033F而和你在一起的时候……\n',
            '也是一样的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330929V#1026F#2P………啊啊……………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330930V#1045F#6P在接触到你的温暖之后，\n',
            '我的确感觉到自己变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330931V和你在一起会感到喜悦，\n',
            '也会开始觉得你很可爱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330932V但在我的内心深处，\n',
            '总觉得这一切像是别人的事情一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('约修亚')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0020330933V#20W或许……\n',
            '那才是我真正的感觉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330934V虚无空洞……\n',
            '我就像是有缺陷的人偶一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_24(0x007A, 0x32)
    Sleep(100)

    OP_24(0x007A, 0x28)
    Sleep(100)

    OP_24(0x007A, 0x1E)
    Sleep(100)

    OP_24(0x007A, 0x14)
    Sleep(100)

    OP_24(0x007A, 0x0A)
    Sleep(100)

    OP_24(0x007A, 0x00)
    Sleep(1000)

    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R2201._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
