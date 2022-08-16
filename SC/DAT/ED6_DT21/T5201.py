import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5201   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5201.x'
    header.mapIndex       = 1
    header.bgm            = 117
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
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT27/CH03770._CH', 'ED6_DT27/CH03770P._CP'),
        ('ED6_DT27/CH03760._CH', 'ED6_DT27/CH03760P._CP'),
        ('ED6_DT26/CH20264._CH', 'ED6_DT26/CH20264P._CP'),
        ('ED6_DT27/CH03101._CH', 'ED6_DT27/CH03101P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '约修亚',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乔丝特',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '白的花束',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '剑',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_1FC)

    Jump('loc_1C2')

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1C2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_03_1401)

    def _loc_1C2(): pass

    label('loc_1C2')

    Return()

# id: 0x0001 offset: 0x1C3
@scena.Code('func_01_1C3')
def func_01_1C3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 0, 0x1040)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DF',
    )

    OP_23(0x01C3)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1DF(): pass

    label('loc_1DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0448, 2, 0x2242)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FB',
    )

    OP_23(0x01C3)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1FB(): pass

    label('loc_1FB')

    Return()

# id: 0x0002 offset: 0x1FC
@scena.Code('func_02_1FC')
def func_02_1FC():
    EventBegin(0x00)
    OP_DB()
    PlaySE(451, 0x00, 0x64)
    CameraMove(450, -1000, -8810, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(2400, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    ChrSetPos(0x0009, -2500, -1000, 14100, 0)
    ChrSetPos(0x000B, -3480, -1000, 13100, 0)
    ChrSetPos(0x000A, -1600, -1000, 13100, 0)
    ChrSetPos(0x0008, -2750, -900, 28300, 0)
    ChrSetPos(0x000C, -2850, -1000, 28850, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x000C, 0x0800)
    ChrSetFlags(0x000C, 0x0040)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 16)
    OP_E5(0x08, 0x00, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_02D6')
    def lambda_02D6():
        CameraMove(-1730, -1000, 28380, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_02D6)

    WaitForThreadExit(0x0008, 0x0000)
    Fade(500)
    CameraMove(-2180, -1000, 29400, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    NpcTalk(
        0x0008,
        '黑发的少年',
        (
            '#0020191710V#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191711V卡琳姐姐……我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 17)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetSubChip(0x000C, 7)
    OP_0D()
    Sleep(1000)

    NpcTalk(
        0x0009,
        '女孩的声音',
        (
            '#0090191712V#1P喂、喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '女孩的声音',
        (
            '#0090191713V#1P你跑到哪里去了啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_0419')
    def lambda_0419():
        CameraMove(-1650, -1000, 23080, 3500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0419)

    @scena.Lambda('lambda_0431')
    def lambda_0431():
        OP_67(0, 9500, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0431)

    @scena.Lambda('lambda_0449')
    def lambda_0449():
        CameraSetDistance(1700, 3500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0449)

    Sleep(1000)

    @scena.Lambda('lambda_045E')
    def lambda_045E():
        ChrWalkTo(0x00FE, -2160, -1000, 18870, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_045E)

    Sleep(200)

    @scena.Lambda('lambda_047E')
    def lambda_047E():
        ChrWalkTo(0x00FE, -1250, -1000, 17670, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_047E)

    Sleep(600)

    @scena.Lambda('lambda_049E')
    def lambda_049E():
        ChrWalkTo(0x00FE, -2790, -1000, 17410, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_049E)

    WaitForThreadExit(0x0009, 0x0000)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0090191714V#415F#6P太好了……终于找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_050A')
    def lambda_050A():
        ChrWalkTo(0x00FE, -2800, -1000, 25850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_050A)

    @scena.Lambda('lambda_0525')
    def lambda_0525():
        CameraMove(-1740, -1000, 27700, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0525)

    @scena.Lambda('lambda_053D')
    def lambda_053D():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_053D)

    Sleep(100)

    @scena.Lambda('lambda_055A')
    def lambda_055A():
        ChrWalkTo(0x00FE, -1800, -1000, 24460, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_055A)

    Sleep(400)

    @scena.Lambda('lambda_057A')
    def lambda_057A():
        ChrWalkTo(0x00FE, -3440, -1000, 23880, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_057A)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0090191715V#210F#6P真是的，别再让我们担心了！\n',
            '一个人跑到这种地方来做什么嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0020191716V#1035F#5P呵……为什么要来这里吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0020191717V#1030F#5P只是一点私人事情，\n',
            '没必要叫你们一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0090191718V#212F#6P真…真是一点都不可爱！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090191719V#214F我们很担心，\n',
            '到处在找你呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290191720V#200F#4P而且要我们对你如此神秘的举动\n',
            '视而不见也不现实嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290191721V据我观察，这里的村落似乎已经\n',
            '荒废１０年之久了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0300191722V#197F#6P我们直到３年前都还一直\n',
            '居住在帝国北部的领地……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191723V不过却从没听说过南部\n',
            '有村庄被废弃啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191724V#190F这村子叫什么名字？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191725V#1033F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0020191726V#1035F#5P……『哈梅尔』。\n',
            '这是它曾经的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090191727V#213F#6P哈梅尔……\n',
            '从来没听过这名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, -180, 400)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0090191728V#212F#5P吉尔哥哥，你听过没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290191729V#204F#4P没……\n',
            '我也从没听说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290191730V#207F大哥呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0300191731V#192F#6P嗯……等我想想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191732V#198F很早以前，帝国政府好像\n',
            '发布过一个通知……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191733V#197F……不行，完全想不起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090191734V#413F#5P什么嘛～竟然连大哥都不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0020191735V#1031F#5P……我的事情已经办完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191736V把你们也牵连到无关的麻烦中，\n',
            '真是非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0090191737V#413F#6P这点小事算不了什么，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090191738V#212F你的态度和初次见面时\n',
            '相比变化也太大了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090191739V难道是在耍我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191740V#1035F#5P……这种话好像\n',
            '不应该从你口中说出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191741V#1031F初次见面时\n',
            '你的演技不是\n',
            '更精彩吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191742V我也和你一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0090191743V#216F#6P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090191744V那、那么说的话，现在这样子\n',
            '难道才是你真正的本性！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191745V#1033F#5P……你这样想也可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191746V#1035F至少现在的我，\n',
            '已经和游击士没有任何关系了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290191747V#203F#4P呼……虽然不知道具体原因，\n',
            '不过看来在你身上发生了不少事情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290191748V#200F算了，既然你能对我们如此坦诚，\n',
            '我们自然也可以相信你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290191749V总比大家互相猜疑好的多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191750V#1034F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0300191751V#490F#6P毕竟当初被王国军\n',
            '追击的时候全靠你的帮忙\n',
            '才能顺利逃脱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191752V看在这个的份上，你这小鬼头的傲慢态度\n',
            '我就不多计较了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191753V#1035F#5P……没有那个必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191754V#1031F我帮助你们，\n',
            '只不过是想利用\n',
            '你们而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191755V想还我人情的话\n',
            '以后多尽力就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0300191756V#198F#6P哼，真是个嘴硬的臭小子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191757V#490F算了，反正你的提议\n',
            '对我们来说也是迟早要做的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300191758V今后大家就互相帮忙，让我们也好好\n',
            '利用你的力量吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191759V#1031F#5P……就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191760V#1035F和我共同行动本来\n',
            '就是件很危险的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191761V为了达成目标\n',
            '大家只能相互协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090191762V#212F#6P真…真是一点都不可爱啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090191763V#215F这种讨厌的家伙\n',
            '我当时竟然还会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191764V#1034F#5P……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0090191765V#214F#6P没什么！\n',
            '别用那种奇怪的眼神看我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0290191766V#203F#4P好啦好啦，乔丝特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290191767V#200F不管怎么说，\n',
            '在达成各自的目的之前\n',
            '我们就是同伴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290191768V#202F请多多关照了，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191769V#1030F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020191770V#1035F嗯，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0300191771V#490F#6P哟……\n',
            '我们也该出发了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020191772V#1031F#5P嗯……回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1230')
    def lambda_1230():
        CameraMove(-1950, -1000, 30090, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1230)

    @scena.Lambda('lambda_1248')
    def lambda_1248():
        OP_67(0, 7140, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1248)

    @scena.Lambda('lambda_1260')
    def lambda_1260():
        CameraSetDistance(1840, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1260)

    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0020191773V#1032F#6P回到利贝尔──\n',
            '那片被阴影笼罩的大地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS150._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    SetScenaFlags(ScenaFlag(0x0208, 0, 0x1040))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x122),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x0D, 0x0000, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_134C',
    )

    ShowSaveMenu()

    def _loc_134C(): pass

    label('loc_134C')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_20(0x00001388)
    OP_AE(0x000000C8)
    OP_24(0x01C3, 0x5F)
    Sleep(200)

    OP_24(0x01C3, 0x5A)
    Sleep(200)

    OP_24(0x01C3, 0x55)
    Sleep(200)

    OP_24(0x01C3, 0x50)
    Sleep(200)

    OP_24(0x01C3, 0x4B)
    Sleep(200)

    OP_24(0x01C3, 0x46)
    Sleep(200)

    OP_24(0x01C3, 0x41)
    Sleep(200)

    OP_24(0x01C3, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x37)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x2D)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    Sleep(200)

    OP_24(0x01C3, 0x23)
    Sleep(200)

    OP_24(0x01C3, 0x1E)
    OP_21()
    OP_23(0x01C3)
    Sleep(1000)

    ClearScenaFlags(ScenaFlag(0x0208, 0, 0x1040))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    NewScene('ED6_DT21/C4302._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1401
@scena.Code('func_03_1401')
def func_03_1401():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_C4(0x00, 0x00000002)
    PlaySE(451, 0x01, 0x46)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x0101, -2830, -1000, 27070, 0)
    ChrSetPos(0x0102, -3640, -960, 28120, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    CameraMove(5280, -1000, 36730, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    LoadChip('ED6_DT26/CH20491._CH', 'ED6_DT26/CH20491P._CP', 6)
    LoadChip('ED6_DT26/CH20492._CH', 'ED6_DT26/CH20492P._CP', 7)
    LoadChip('ED6_DT26/CH20493._CH', 'ED6_DT26/CH20493P._CP', 8)
    LoadChip('ED6_DT26/CH20499._CH', 'ED6_DT26/CH20499P._CP', 9)
    LoadChip('ED6_DT26/CH20438._CH', 'ED6_DT26/CH20438P._CP', 10)
    LoadChip('ED6_DT26/CH20499._CH', 'ED6_DT26/CH20499P._CP', 11)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetChipByIndex(0x0102, 6)
    OP_7E(-700, -1320, 150, 115, 1)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1500')
    def lambda_1500():
        CameraMove(-2160, -1000, 29130, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1500)

    @scena.Lambda('lambda_1518')
    def lambda_1518():
        OP_67(0, 7350, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1518)

    @scena.Lambda('lambda_1530')
    def lambda_1530():
        CameraSetDistance(1790, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1530)

    @scena.Lambda('lambda_1540')
    def lambda_1540():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1540)

    @scena.Lambda('lambda_1550')
    def lambda_1550():
        OP_6E(444, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1550)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020421203V#1035F#6P……姐姐，我回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421204V#1041F这个……\n',
            '是我替莱维带来给你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_99(0x0102, 0x00, 0x06, 1000)
    Fade(500)
    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0102, 7)
    ChrSetChipByIndex(0x000D, 6)
    ChrSetFlags(0x000D, 0x0040)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetSubChip(0x000D, 12)
    ChrSetPos(0x000D, -3650, -1100, 28360, 0)
    ChrClearFlags(0x000D, 0x0080)
    OP_0D()
    Sleep(1000)

    OP_99(0x0102, 0x08, 0x0B, 1500)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrClearFlags(0x0102, 0x0002)
    ChrSetFlags(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020421205V#1053F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421206V#1017F太好了啊，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421207V莱维他……\n',
            '现在也一定会很高兴吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020421208V#1035F#5P……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421209V#1043F莱维和姐姐之间的感情\n',
            '一直都非常好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421210V#1054F当时，他们一定曾有过\n',
            '走到一起的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421211V#1003F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421212V#1025F那个…让我也来\n',
            '和卡琳姐姐打个招呼可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421213V#1053F#5P嗯……当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17F2')
    def lambda_17F2():
        CameraMove(-2620, -790, 29440, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_17F2)

    @scena.Lambda('lambda_180A')
    def lambda_180A():
        ChrMoveTo(0x00FE, -4000, -1000, 27480, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_180A)

    Sleep(100)

    ChrMoveTo(0x0101, -2680, -990, 28040, 1000, 0x00)
    WaitForThreadExit(0x0102, 0x0002)

    @scena.Lambda('lambda_1843')
    def lambda_1843():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1843)

    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421214V#1012F#4P初次见面，卡琳姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421215V#1006F我是艾丝蒂尔。\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421216V是您弟弟的家人，也就是姐姐……',
            TxtCtl.Enter,
            '\n',
            '#1013F基…基本上也可以算是女朋友吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 11)
    ChrSetSubChip(0x0102, 0)
    OP_99(0x0102, 0x00, 0x02, 1500)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020421217V#1048F#6P真是的……\n',
            '为什么还要加上个『基本上』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 10)
    ChrSetSubChip(0x0101, 0)
    OP_99(0x0101, 0x00, 0x02, 1500)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010421218V#1013F#5P可、可是……\n',
            '人家还是有点儿不习惯嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421219V总觉得……\n',
            '有些难为情呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421220V#1052F#6P真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421221V#1054F哈哈，\n',
            '不过这样才像是艾丝蒂尔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421222V#1019F#5P唔……什么嘛。\n',
            '你竟然摆出那种若无其事的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421223V不过话说回来，约修亚。\n',
            '你呀，在两人独处时候…总是很大胆呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_99(0x0101, 0x02, 0x00, 2000)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    @scena.Lambda('lambda_1B28')
    def lambda_1B28():
        OP_99(0x0102, 0x02, 0x00, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1B28)

    ChrTalk(
        0x0101,
        (
            '#0010421224V#1013F#4P啊，对不起！\n',
            '在问候姐姐的时候竟然说起这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421225V#1017F那个……\n',
            '今天，我和约修亚一起回他的故乡，\n',
            '特意来向姐姐您问候的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421226V今后也请您多多关照了……\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 8)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x0002)
    OP_0D()
    OP_99(0x0101, 0x00, 0x08, 1000)
    Fade(250)
    ChrSetSubChip(0x0101, 9)
    ChrSetChipByIndex(0x000C, 8)
    ChrSetFlags(0x000C, 0x0040)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetSubChip(0x000C, 12)
    ChrSetPos(0x000C, -2670, -900, 28900, 0)
    ChrClearFlags(0x000C, 0x0080)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010421227V#1012F#4P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421228V#1035F#6P……谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421229V#1041F姐姐她……\n',
            '一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x0A, 0x0B, 1300)
    Sleep(200)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0101, 0x0002)

    @scena.Lambda('lambda_1D0C')
    def lambda_1D0C():
        CameraMove(-2830, -780, 28720, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1D0C)

    ChrMoveTo(0x0101, -2780, -1000, 27390, 1000, 0x00)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 11)
    ChrSetSubChip(0x0102, 0)
    OP_99(0x0102, 0x00, 0x02, 1500)
    Sleep(100)

    ChrSetDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010421230V#1008F#2P哈哈……\n',
            '那真是太好了啊，不过…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421231V#1007F现在的我还是很孩子气，\n',
            '好像总是给人一种靠不住的感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421232V真不知道卡琳姐姐会不会认为\n',
            '我没资格做他弟弟的女朋友啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421233V#1054F#6P哈哈，你想得太多了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421234V#1053F姐姐如果活着的话，\n',
            '肯定会和你非常投缘的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421235V因为你们的性格有着鲜明的对比啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 11)
    ChrSetSubChip(0x0101, 24)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421236V#1016F#2P嘻嘻嘻～是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 25)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421237V#1019F#2P……唔？\n',
            '怎么觉得这话怪怪的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421238V你不会是想说我没有\n',
            '卡琳姐姐那样\n',
            '坚强沉稳吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421239V#1052F#6P唔……嗯……\n',
            '虽然你内心很坚强……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421240V#1054F不过说到沉稳嘛，\n',
            '确实有些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010421241V#1007F#2P哼哼哼……',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421242V#1041F#6P不过，那不是也很好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421243V总是乐观开朗、积极向上，\n',
            '像太阳一样灿烂耀眼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421244V#1049F所以，\n',
            '我最喜欢的女孩就是这样的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x1B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x1D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x1C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x1B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421245V#1004F#2P#3S！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 90, 600)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421246V#1013F#5P真、真是的！约……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421247V约修亚你总是这样随口就说出\n',
            '一些让人难为情的话啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421248V#1044F#6P哎？你不高兴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 600)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421249V#1019F#2P#3S高兴！高兴！非常高兴！\n',
            '这样总可以了吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421250V#1052F#6P你怎么又突然生气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421251V#1007F#2P……嗯！好了！已经问候过姐姐了，\n',
            '我们差不多也该出发了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421252V再在这里喋喋不休说个没完的话，\n',
            '姐姐大概要烦死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421253V#1044F#6P啊……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421254V#1043F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421255V#1015F#2P嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x02, 0x00, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020421256V#1043F#6P……那个…这样真的好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421257V和我一起\n',
            '离开利贝尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421258V#1004F#2P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421259V#1035F#6P为了偿还在『结社』时代犯下的罪过，\n',
            '周游大陆各地其实只是我一个人的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421260V也为了变得像莱维一样强，\n',
            '我要再次踏上旅程。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421261V#1043F把你也牵连进来，真的好吗？\n',
            '老实说……我还是有点迷茫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 11)
    ChrSetSubChip(0x0101, 11)
    OP_99(0x0101, 0x0B, 0x0D, 1800)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421262V#1007F#2P真是的……\n',
            '你怎么还说这种话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x00, 0x02, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020421263V#1044F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x0D, 0x0F, 1500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421264V#1006F#2P雷格纳特不是说过吗，\n',
            '今后在这个世界中也许还会发生\n',
            '很多很多的大事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421265V『噬身之蛇』肯定还会\n',
            '继续在其他地方制造乱子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x0F, 0x11, 1500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421266V#1029F#2P为了应付这一切，我们还要继续锻炼，\n',
            '要超越老爸才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421267V因此对我来说，\n',
            '这样的旅行也是很有必要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421268V#1054F超越父亲……\n',
            '你又在说大话了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x11, 0x13, 1500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421269V#1006F#2P目标本来就是要定大一些嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x13, 0x15, 1500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421270V#1012F#2P我和莱维也做过约定的，\n',
            '还有玲的去向我也很在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421271V总之，到没有涉足的土地旅行\n',
            '也是一种享受呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x15, 0x17, 1500)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010421272V#1008F#2P#1000F而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    @scena.Lambda('lambda_2860')
    def lambda_2860():
        CameraMove(-3300, -780, 28870, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2860)

    ChrSetFlags(0x0101, 0x0040)
    ChrWalkTo(0x0101, -3300, -1000, 27400, 1000, 0x00)
    Sleep(100)

    ChrSetFlags(0x0102, 0x0800)
    ChrClearFlags(0x0102, 0x0001)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetSubChip(0x0102, 3)
    OP_99(0x0102, 0x03, 0x07, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020421273V#1044F#6P艾、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421274V#1006F#2P最重要的是，我和约修亚在一起\n',
            '难道还需要什么理由吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421117V#1044F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421276V#1040F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421118V#1053F嗯……你说的对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421278V#1054F根本就……不需要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421279V#1016F#2P对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421280V#1017F约修亚真是的，\n',
            '这种事情竟然还要我提醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421281V#1049F#6P哈哈……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A4D')
    def lambda_2A4D():
        OP_99(0x00FE, 0x08, 0x0A, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2A4D)

    @scena.Lambda('lambda_2A5D')
    def lambda_2A5D():
        CameraMove(-4070, -1000, 40590, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2A5D)

    @scena.Lambda('lambda_2A75')
    def lambda_2A75():
        OP_67(0, 7350, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A75)

    @scena.Lambda('lambda_2A8D')
    def lambda_2A8D():
        CameraSetDistance(1790, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A8D)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_C5(0x00, 0, 0, 640, 1024, 0, -540, 1024, 1024, 0, 0, 640, 1024, 0x00FFFFFF, 0x00, 'C_VIS177._CH')
    OP_C5(0x01, 0, 0, 640, 1024, 0, -540, 1024, 1024, 0, 0, 640, 1024, 0x00FFFFFF, 0x00, 'C_VIS178._CH')
    OP_C6(0x00, 0x03, -1, 1000, 0)
    OP_C6(0x00, 0x07, 0, -386000, 3000)
    OP_C7(0x00, 0x00, 0x00)
    Sleep(500)

    OP_C6(0x01, 0x03, -1, 0, 0)
    SetMessageWindowPos(80, 340, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0020421282V──走吧！艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421283V虽然还不知道前方的道路\n',
            '会通向何处……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421284V不过，我相信我们一定可以\n',
            '在旅途里找到属于自己的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(340, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010421285V嗯……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421286V迈开我们的脚步，\n',
            '一步一步向前走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x01, 0x00000002)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x07, 0, 0, 4000)
    OP_C7(0x00, 0x01, 0x00)
    Sleep(1000)

    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS179._CH')
    OP_C6(0x02, 0x03, -1, 3000, 0)
    Sleep(3500)

    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_56(0x02)
    OP_C6(0x02, 0x03, 16777215, 3000, 0)
    Sleep(4000)

    If(
        (
            (Expr.Eval, "OP_40(0x001B, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_40(0x0031, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0417, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2D0E',
    )

    SetScenaFlags(ScenaFlag(0x0456, 3, 0x22B3))

    def _loc_2D0E(): pass

    label('loc_2D0E')

    SetScenaFlags(ScenaFlag(0x0448, 2, 0x2242))
    OP_C4(0x00, 0x00000010)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x12B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_40(0x001B, 0x00)"),
            (Expr.Eval, "OP_40(0x0031, 0x00)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2D3B',
    )

    SetScenaFlags(ScenaFlag(0x0456, 3, 0x22B3))

    def _loc_2D3B(): pass

    label('loc_2D3B')

    RemoveItem(ItemTable['特级钓师认定证书'], 1)
    RemoveItem(ItemTable['数据水晶Ｚ'], 1)
    RemoveItem(ItemTable['白金戒指'], 1)
    RemoveItem(ItemTable['零式导力枪α'], 1)
    RemoveItem(ItemTable['零力场发生器'], 1)
    SetScenaFlags(ScenaFlag(0x0455, 6, 0x22AE))
    SetScenaFlags(ScenaFlag(0x0456, 5, 0x22B5))
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　 ～　<FIXME>クリアデータのセーブについて　～\n',
            '　　  クリアデータを作成し、タイトル画面からロードすると\n',
            '　　  各種データを引き継いだまま２周目を開始できます。',
            TxtCtl.ShowAll,
            0x18,
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【储存通关存档】\n'),
            TXT(0x01, '【回到标题画面】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E55',
    )

    OP_DD()
    EventBegin(0x04)

    def _loc_2E55(): pass

    label('loc_2E55')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C4(0x01, 0x00000010)
    ClearScenaFlags(ScenaFlag(0x0448, 2, 0x2242))
    FadeOut(0, 0, -1)
    OP_20(0x00000BB8)
    MapSetFlags(0x02000000)
    Sleep(200)

    OP_24(0x01C3, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    Sleep(200)

    OP_24(0x01C3, 0x1E)
    Sleep(200)

    OP_24(0x01C3, 0x14)
    Sleep(200)

    OP_24(0x01C3, 0x0A)
    Sleep(200)

    OP_23(0x01C3)
    OP_21()
    Sleep(3000)

    OP_B4(0x01)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
