import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5401   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5401.x'
    header.mapIndex       = 1
    header.bgm            = 28
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
        ('ED6_DT26/CH20383._CH', 'ED6_DT26/CH20383P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT27/CH04547._CH', 'ED6_DT27/CH04547P._CP'),
        ('ED6_DT27/CH04548._CH', 'ED6_DT27/CH04548P._CP'),
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04003._CH', 'ED6_DT27/CH04003P._CP'),
        ('ED6_DT27/CH04004._CH', 'ED6_DT27/CH04004P._CP'),
        ('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP'),
        ('ED6_DT27/CH03540._CH', 'ED6_DT27/CH03540P._CP'),
        ('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP'),
        ('ED6_DT26/CH20237._CH', 'ED6_DT26/CH20237P._CP'),
        ('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP'),
        ('ED6_DT26/CH20305._CH', 'ED6_DT26/CH20305P._CP'),
        ('ED6_DT26/CH20439._CH', 'ED6_DT26/CH20439P._CP'),
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '怀斯曼教授',
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
            name                = '剑帝莱维',
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
            name                = '怪盗布卢布兰',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瘦狼瓦鲁特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '幻惑之铃露茜奥拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '小丑肯帕雷拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '歼灭天使玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x2B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2B2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2C3',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0A_3288)

    Jump('loc_2DC')

    def _loc_2C3(): pass

    label('loc_2C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 5, 0x1C1D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x79),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_02_2FC)

    def _loc_2DC(): pass

    label('loc_2DC')

    Return()

# id: 0x0001 offset: 0x2DD
@scena.Code('func_01_2DD')
def func_01_2DD():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FB',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2FB(): pass

    label('loc_2FB')

    Return()

# id: 0x0002 offset: 0x2FC
@scena.Code('func_02_2FC')
def func_02_2FC():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetPos(0x0101, -960, 0, 45690, 0)
    ChrSetPos(0x0008, -1000, 1600, 89800, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_033B')
    def lambda_033B():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_033B')

    DispatchAsync2(0x0008, 0x0000, lambda_033B)

    CameraMove(-740, 0, 50090, 0)
    OP_67(0, 13680, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(410, 0)
    OP_1F(0x64, 0x000003E8)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_039A')
    def lambda_039A():
        CameraMove(1180, 1500, 94610, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_039A)

    @scena.Lambda('lambda_03B2')
    def lambda_03B2():
        OP_67(0, 16910, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03B2)

    @scena.Lambda('lambda_03CA')
    def lambda_03CA():
        CameraSetDistance(2900, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03CA)

    @scena.Lambda('lambda_03DA')
    def lambda_03DA():
        OP_6C(45000, 9000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03DA)

    @scena.Lambda('lambda_03EA')
    def lambda_03EA():
        OP_6E(550, 9000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_03EA)

    @scena.Lambda('lambda_03FA')
    def lambda_03FA():
        ChrWalkTo(0x00FE, -960, 0, 63560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03FA)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_0423')
    def lambda_0423():
        CameraMove(-350, 1500, 90480, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0423)

    @scena.Lambda('lambda_043B')
    def lambda_043B():
        OP_67(0, 5350, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_043B)

    @scena.Lambda('lambda_0453')
    def lambda_0453():
        CameraSetDistance(2020, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0453)

    @scena.Lambda('lambda_0463')
    def lambda_0463():
        OP_6C(57000, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0463)

    @scena.Lambda('lambda_0473')
    def lambda_0473():
        OP_6E(512, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0473)

    WaitForThreadExit(0x0101, 0x0000)
    OP_71(0x0004, 0x0004)
    OP_79(0x09, 0x0002)
    OP_7B()
    ChrSetPos(0x0101, -900, 0, 78060, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(1000)

    CameraSetDistance(1600, 6000)
    Sleep(1000)

    OP_20(0x000007D0)
    OP_21()
    TerminateThread(0x0008, 0x00)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0150330090V#1154F#5P欢迎……\n',
            '欢迎来到『红色方舟』古罗力亚斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetPos(0x0008, -2000, 1500, 89380, 0)
    OP_0D()
    PlayBGM(112)
    Sleep(500)

    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150330091V#1151F#5P好久不见了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    CameraMove(-1380, 1600, 84070, 0)
    OP_67(0, 4660, -10000, 0)
    CameraSetDistance(2180, 0)
    OP_6C(33000, 0)
    OP_6E(545, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330092V#1002F亚鲁瓦教授……\n',
            '果然是你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330093V刚才听到你的声音\n',
            '总算想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330094V#1154F#5P呵呵，\n',
            '不愧是『剑圣』的女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330095V#1150F虽然我并没有施加重咒，但想不到你\n',
            '竟然能靠自己的力量将封锁的记忆找回。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330096V#1002F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_06EA')
    def lambda_06EA():
        ChrMoveTo(0x0008, -900, 1500, 85950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_06EA)

    Sleep(1000)

    Fade(500)
    OP_72(0x0004, 0x0004)
    OP_79(0x09, 0x0001)
    OP_7B()
    CameraMove(-900, 0, 88050, 0)
    OP_67(0, 3050, -10000, 0)
    CameraSetDistance(3330, 0)
    OP_6C(0, 0)
    OP_6E(362, 0)
    CameraMove(-960, 0, 88610, 0)
    OP_67(0, 2550, -10000, 0)
    CameraSetDistance(3330, 0)
    OP_6C(0, 0)
    OP_6E(362, 0)
    WaitForThreadExit(0x0008, 0x0003)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150330097V#1150F#5P顺带一提，\n',
            '我真正的名字叫盖鲁格·怀斯曼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330098V负责掌管『噬身之蛇』，\n',
            '是『蛇之使徒』的一柱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330099V#1002F#6P『蛇之使徒』……\n',
            '就是『结社』的最高干部？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330100V#1154F#5P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330101V#1150F好了，正如之前所说，\n',
            '我准备要回答你的疑问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330102V有什么想问的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330103V#1003F#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330104V#1007F……想问的事情太多，\n',
            '都不知道该从哪里问起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330105V#1151F#5P不用着急。\n',
            '慢慢想一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330106V不介意的话，\n',
            '听我弹奏一曲如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330107V#1007F#6P不用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330108V#1019F不过话说回来，\n',
            '没想到你还有这种兴趣……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330109V看来以前自称贫穷考古学者\n',
            '的那些话全部都是谎言吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330110V#1154F呵呵，贫穷不贫穷暂且不去计较，\n',
            '研究考古学倒是真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330111V#1150F顺带一提，在我还身处教会的时候\n',
            '就开始喜欢风琴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330112V虽然没那个帝国人那么厉害，\n',
            '不过水平也还拿得出手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330113V#1004F#6P身、身处教会……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330114V#1151F只是所谓的学僧啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330115V#1154F虽然遇到『盟主』之后\n',
            '我就舍弃了信仰之道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330116V不过那时学到的古代遗物知识\n',
            '直到现在也相当有用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330117V#1150F没错，在这次的计划中也是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330118V#1002F#6P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330119V挑唆上校\n',
            '发动政变……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330120V在各地进行『福音』实验，\n',
            '引发各种混乱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330121V也全部……都是你干的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330122V#1154F说得没错──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330123V#1151F一切都是为了『福音计划』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330124V#1002F#6P『福音计划』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330125V那个研究所的数据库里\n',
            '也有这个项目……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330126V总之就是要拿到\n',
            '『辉之环』的计划对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330127V#1154F说拿到\n',
            '有点不恰当……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330128V#1150F不过，这么想\n',
            '也可以吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330129V#1005F#6P『辉之环』是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330130V据说是女神的至宝，\n',
            '不过具体是怎样的东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330131V#1151F关于『辉之环』的真面目，\n',
            '目前请让我暂时保密。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330132V难得的巨大惊喜，\n',
            '我可不想提前透露出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330133V#1019F#6P惊喜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330134V#1150F计划已经进行到第３阶段。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330135V再过不久，它的真正面目\n',
            '就会呈现在所有人的面前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330136V#1154F呵呵……请期待那一刻的到来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330137V#1002F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330138V#1154F而当『环』现身之时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330139V#1151F我们将能够确认\n',
            '人类的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330140V#1015F#6P人类的可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330141V『雷格纳特』似乎也说过\n',
            '这样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330142V#1153F哦，那只圣兽\n',
            '连这些话也告诉你们了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330143V#1150F唔，看来你不光是\n',
            '顶着父亲的光环而已呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330144V#1022F#6P恭维话就到此为止吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330145V#1019F什么嘛……说是回答我的问题，\n',
            '结果还不是自己一个人喋喋不休。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330146V#1154F这真是失礼了……\n',
            '我并不是有意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330147V#1150F不过，你最想问的事情\n',
            '我应该能很清楚地回答哦。',
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
            '#0010330148V#1026F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330149V#1151F哎呀，为何\n',
            '如此地犹豫呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330150V不必害怕，\n',
            '鼓起勇气问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330151V#1003F#6P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330152V约修亚……他在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330153V#1154F呵呵……\n',
            '这我也不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330154V好像是与空贼们在一起\n',
            '谋划着什么的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330155V目前的动向还不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330156V#1150F不过现在应该还平安无事，这一点\n',
            '应该是没有错才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330157V#1025F#6P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330158V#1154F将约修亚的能力调整为\n',
            '隐密活动和对集团作战这项工作，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330159V是我亲手进行的。\n',
            '不过，完成度似乎远远超出我的预料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330160V#1151F呵呵呵……他究竟能奋战到\n',
            '什么程度呢？真是令人期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330161V#1002F#6P你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330162V#1153F啊啊，别露出\n',
            '那么可怕的表情嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330163V#1150F当初托付给我的时候，\n',
            '约修亚的心已经崩溃了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330164V要重新构筑这样的心，\n',
            '对我来说也是第一次尝试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330165V#1154F作为一个研究者，\n',
            '在意自己的成果不是理所当然的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330103V#1003F#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330167V……那场诞辰庆典的时候，\n',
            '你对约修亚说了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330168V#1150F我只是解除了封锁的记忆，\n',
            '将真相告诉给他而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330169V#1154F被你家收养的他，\n',
            '在无意识下作为间谍\n',
            '向『结社』传送情报的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330170V还有，多亏有他的情报，\n',
            '理查德上校的政变才能成功，\n',
            '而我们的计划也准备就绪的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330171V#1151F作为奖励，\n',
            '我就把他从『结社』中解放了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330172V#1027F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330173V……我终于明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330174V约修亚为什么……\n',
            '会在那个夜晚……消失不见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330175V为什么会露出那样的表情……\n',
            '对我说再见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330176V#1150F呀，有关这一点，\n',
            '我也觉得很遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330177V恢复自我的约修亚\n',
            '竟然会从你们面前消失。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330178V#1154F我曾经还特意劝说过他，\n',
            '让他装作一无所知的样子，\n',
            '继续和你们一起生活就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330179V#1151F呵呵，好心没好报吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    OP_71(0x0004, 0x0004)
    OP_79(0x09, 0x0002)
    OP_7B()
    CameraMove(270, 420, 83800, 0)
    OP_67(0, 4650, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(386, 0)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    OP_9E(0x0101, 15, 0, 300, 4000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330180V#1025F#2P你竟然……\n',
            '说得出这种话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330181V明明就是你逼得约修亚\n',
            '只能选择这条路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330182V#1027F逼得他…现出那副表情……\n',
            '把口琴交给我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330183V对我说再见了……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    Sleep(500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330184V#1023F#3S#2P这全部的全部！#2S！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330185V#1023F#3S#2P不都是你造成的吗！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_1B44')
    def lambda_1B44():
        CameraMove(-660, 1500, 85500, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1B44)

    @scena.Lambda('lambda_1B5C')
    def lambda_1B5C():
        CameraSetDistance(2200, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_1B5C)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0101, 0x00, 0x00, func_04_2F0A)
    Sleep(100)

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetSubChip(0x0009, 9)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0009, -990, 2500, 84790, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x1000)

    @scena.Lambda('lambda_1BB1')
    def lambda_1BB1():
        ChrMoveTo(0x00FE, -990, 1500, 84790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1BB1)

    @scena.Lambda('lambda_1BCC')
    def lambda_1BCC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1BCC)

    PlaySE(153, 0x00, 0x64)
    Sleep(300)

    CreateThread(0x0009, 0x00, 0x00, func_03_2EED)
    Sleep(500)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0101, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 200, 3000, 100)

    @scena.Lambda('lambda_1C3F')
    def lambda_1C3F():
        CameraMove(-980, 1500, 81840, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1C3F)

    @scena.Lambda('lambda_1C57')
    def lambda_1C57():
        OP_67(0, 3600, -10000, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1C57)

    @scena.Lambda('lambda_1C6F')
    def lambda_1C6F():
        CameraSetDistance(2800, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1C6F)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x02)
    CreateThread(0x0101, 0x00, 0x00, func_05_2F81)

    ChrTalk(
        0x0101,
        (
            '#0010330186V#2P啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    WaitForThreadExit(0x0101, 0x0000)
    OP_99(0x0101, 0x01, 0x03, 1500)
    PlaySE(524, 0x00, 0x64)
    ChrClearFlags(0x0009, 0x1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    OP_99(0x0009, 0x06, 0x07, 1500)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140220037V#121F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330188V#1021F#2P『剑帝』莱维……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330189V你、你到底是从哪里出现的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140330190V#124F#5P……我从一开始就在这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330191V#120F只是你没注意到而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 100, -1, -1)
    TalkSetChrName('男人的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170330192V真是的……\n',
            '实在是没有风度的举止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    @scena.Lambda('lambda_1E30')
    def lambda_1E30():
        CameraMove(-450, 1500, 84100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E30)

    @scena.Lambda('lambda_1E48')
    def lambda_1E48():
        OP_67(0, 3600, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E48)

    @scena.Lambda('lambda_1E60')
    def lambda_1E60():
        CameraSetDistance(2420, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E60)

    @scena.Lambda('lambda_1E70')
    def lambda_1E70():
        OP_6C(35000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E70)

    ChrSetPos(0x000A, -5300, 1500, 85140, 135)
    ChrSetPos(0x000B, 5040, 1500, 85050, 225)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0004)
    CreateThread(0x000A, 0x00, 0x00, func_06_305F)
    Sleep(500)

    CreateThread(0x000B, 0x00, 0x00, func_07_30AA)
    Sleep(2000)

    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrSetPos(0x000C, 570, 1500, 84590, 180)

    @scena.Lambda('lambda_1EEA')
    def lambda_1EEA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_1EEA)

    PlaySE(153, 0x00, 0x64)
    CreateThread(0x0011, 0x01, 0x00, func_08_3106)
    CreateThread(0x0012, 0x01, 0x00, func_09_31C7)
    Sleep(800)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_1F30')
    def lambda_1F30():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_1F30')

    DispatchAsync2(0x0101, 0x0003, lambda_1F30)

    OP_99(0x0101, 0x03, 0x00, 1000)
    TerminateThread(0x0101, 0x03)
    Fade(250)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_205A',
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
            TXT(0x00, '【◆布卢布兰的挑战全部完成】\n'),
            TXT(0x01, '【◆布卢布兰的挑战完成１个以上】\n'),
            TXT(0x02, '【◆无视了布卢布兰的挑战】\n'),
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
        (0x00000000, 'loc_200C'),
        (0x00000001, 'loc_2023'),
        (0x00000002, 'loc_203A'),
        (-1, 'loc_2051'),
    )

    def _loc_200C(): pass

    label('loc_200C')

    OP_28(0x006C, 0x04, 0x10)
    OP_28(0x0077, 0x04, 0x10)
    OP_28(0x0078, 0x04, 0x10)
    OP_28(0x00C4, 0x04, 0x10)

    Jump('loc_2051')

    def _loc_2023(): pass

    label('loc_2023')

    OP_28(0x006C, 0x04, 0x10)
    OP_28(0x0077, 0x03, 0x10)
    OP_28(0x0078, 0x03, 0x10)
    OP_28(0x00C4, 0x03, 0x10)

    Jump('loc_2051')

    def _loc_203A(): pass

    label('loc_203A')

    OP_28(0x006C, 0x03, 0x10)
    OP_28(0x0077, 0x03, 0x10)
    OP_28(0x0078, 0x03, 0x10)
    OP_28(0x00C4, 0x03, 0x10)

    Jump('loc_2051')

    def _loc_2051(): pass

    label('loc_2051')

    FadeIn(300, 0)

    def _loc_205A(): pass

    label('loc_205A')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_206E',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_206E(): pass

    label('loc_206E')

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2082',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2082(): pass

    label('loc_2082')

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2096',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_2096(): pass

    label('loc_2096')

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_20AA',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_20AA(): pass

    label('loc_20AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2127',
    )

    ChrTalk(
        0x000A,
        (
            '#0170330193V#231F#5P毕竟你也曾出色地\n',
            '完成过我的挑战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170330194V在做出行动之前还是先稍微动动脑子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223B')

    def _loc_2127(): pass

    label('loc_2127')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21BA',
    )

    ChrTalk(
        0x000A,
        (
            '#0170330195V#232F#5P虽然有些勉强，\n',
            '但至少你也曾经接受过我的挑战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170330194V在做出行动之前还是先稍微动动脑子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223B')

    def _loc_21BA(): pass

    label('loc_21BA')

    ChrTalk(
        0x000A,
        (
            '#0170330197V#233F#5P都是因为你一直无视我的挑战，\n',
            '所以才会表现得这么差劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170330194V在做出行动之前还是先稍微动动脑子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_223B(): pass

    label('loc_223B')

    ChrTalk(
        0x000B,
        (
            '#0200330199V#252F#5P哇哈哈，别这么说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200330200V毫不犹豫地打向『白面』，\n',
            '没有一定的胆量也是办不到的呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210330201V#244F#5P呵呵～暂且不说本领如何，\n',
            '单单就这勇气而言，确实可嘉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210330202V#240F还是说，只是因为天生反应迟钝呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2336')
    def lambda_2336():
        CameraMove(-450, 960, 82000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2336)

    Sleep(500)

    ChrMoveTo(0x0101, -1050, 0, 75600, 1000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330203V#1026F#2P啊……呜………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, 2800, 0, 79120, 225)
    SetMessageWindowPos(400, 150, -1, -1)
    TalkSetChrName('少年的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0190330204V哈哈哈……\n',
            '你就是『剑圣』的千金吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2417')
    def lambda_2417():
        CameraMove(340, 480, 81240, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2417)

    @scena.Lambda('lambda_242F')
    def lambda_242F():
        OP_67(0, 4260, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_242F)

    @scena.Lambda('lambda_2447')
    def lambda_2447():
        CameraSetDistance(2460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2447)

    Sleep(500)

    ChrTurnDirection(0x0101, 0x000D, 400)
    Sleep(1000)

    LoadEffect(0x01, 'map\\\\mp055_00.eff')
    ChrSetFlags(0x000D, 0x8000)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)
    ChrClearFlags(0x000D, 0x0080)
    PlayEffect(0x01, 0x01, 0x000D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_24C6')
    def lambda_24C6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_24C6)

    PlaySE(153, 0x00, 0x64)
    Sleep(1800)

    StopEffect(0x01, 0x02)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0190330205V#853F#5P呵呵，初次见面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000D, 18)
    ChrSetSubChip(0x000D, 0)
    OP_99(0x000D, 0x00, 0x03, 1500)

    ChrTalk(
        0x000D,
        (
            '#0190330206V#854F#5P我是执行者Ｎｏ．０──\n',
            '『小丑』肯帕雷拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190330207V#851F今后多多关照哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000D, 0x03, 0x00, 1500)
    ChrClearFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 7)
    ChrSetSubChip(0x000D, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330208V#1020F#5P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -1010, 0, 67570, 0)

    NpcTalk(
        0x000E,
        '少女的声音',
        (
            '#0220330209V#1P真是的，大家不要一起\n',
            '吓唬艾丝蒂尔啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2632')
    def lambda_2632():
        CameraMove(-1070, 0, 74320, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2632)

    @scena.Lambda('lambda_264A')
    def lambda_264A():
        CameraSetDistance(2600, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_264A)

    ChrTurnDirection(0x0101, 0x000E, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_266B')
    def lambda_266B():
        CameraMove(-890, 0, 78320, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_266B)

    @scena.Lambda('lambda_2683')
    def lambda_2683():
        CameraSetDistance(2430, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2683)

    ChrWalkTo(0x000E, -1080, 0, 73740, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010330210V#1026F#5P玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0220330211V#263F#4P嘻嘻……\n',
            '不必担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330212V#260F他们并不是为了杀艾丝蒂尔\n',
            '才聚集在这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311209V#1004F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2757')
    def lambda_2757():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_2757')

    DispatchAsync2(0x0101, 0x0001, lambda_2757)

    @scena.Lambda('lambda_2768')
    def lambda_2768():
        CameraMove(-380, 950, 82220, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2768)

    @scena.Lambda('lambda_2780')
    def lambda_2780():
        OP_67(0, 4710, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2780)

    @scena.Lambda('lambda_2798')
    def lambda_2798():
        CameraSetDistance(2820, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2798)

    @scena.Lambda('lambda_27A8')
    def lambda_27A8():
        OP_6E(360, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_27A8)

    ChrWalkTo(0x000E, 370, 0, 75480, 2000, 0x00)
    ChrWalkTo(0x000E, 370, 0, 77800, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x000E,
        (
            '#0220330214V#261F#2P对了，教授。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330215V早点把那件事\n',
            '告诉艾丝蒂尔吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330216V#1154F#6P呵呵……\n',
            '就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_286A')
    def lambda_286A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_286A)

    @scena.Lambda('lambda_2878')
    def lambda_2878():
        CameraMove(-940, 940, 81750, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2878)

    @scena.Lambda('lambda_2890')
    def lambda_2890():
        OP_67(0, 4230, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2890)

    @scena.Lambda('lambda_28A8')
    def lambda_28A8():
        CameraSetDistance(3000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28A8)

    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 14)

    @scena.Lambda('lambda_28C2')
    def lambda_28C2():
        ChrWalkTo(0x00FE, -2580, 1500, 84810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_28C2)

    Sleep(200)

    @scena.Lambda('lambda_28E2')
    def lambda_28E2():
        ChrWalkTo(0x00FE, -1260, 1500, 83000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_28E2)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetDirection(0x0009, 180, 400)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0150330217V#1150F#5P如何，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330218V你是否愿意加入\n',
            '我们『噬身之蛇』呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330219V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330220V#1016F#2P……抱歉。\n',
            '我好像听错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330221V#1008F能不能再说一次？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330222V#1154F#5P我在问你，要不要\n',
            '加入『噬身之蛇』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0151850005V#1151F一开始先作为『执行者』候补。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330223V#1020F#2P什、什、什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330224V#1005F#2P#4S你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330225V#1151F#5P呵呵，不必\n',
            '那么吃惊吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330226V考虑一下吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330227V如果你加入『结社』的话，\n',
            '约修亚也就不用那么为难了，\n',
            '他一定会乖乖回到你身边来，你难道不这么想吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330228V#1026F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0220330229V#265F#5P艾丝蒂尔的愿望\n',
            '不就是想和约修亚重逢么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330230V只要加入『结社』，\n',
            '这个愿望马上就能实现了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330231V#261F呵呵呵……\n',
            '这还有什么要考虑的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330232V#1003F#6P……但、但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330233V………我…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150330234V#1150F#5P呵呵，慢慢考虑吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330235V#1154F等一下我们必须\n',
            '暂时离开舰艇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330236V当我回来的时候\n',
            '再给我答案吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0008, 19)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(300)

    ChrSetSubChip(0x0008, 1)
    PlaySE(188, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x000F, -1830, 0, 69620, 0)
    ChrSetPos(0x0010, -220, 0, 69620, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2DCE')
    def lambda_2DCE():
        CameraMove(360, 680, 80540, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DCE)

    @scena.Lambda('lambda_2DE6')
    def lambda_2DE6():
        OP_67(0, 3470, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DE6)

    @scena.Lambda('lambda_2DFE')
    def lambda_2DFE():
        CameraSetDistance(3220, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DFE)

    @scena.Lambda('lambda_2E0E')
    def lambda_2E0E():
        ChrWalkTo(0x00FE, -1830, 0, 74000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2E0E)

    Sleep(100)

    @scena.Lambda('lambda_2E2E')
    def lambda_2E2E():
        ChrWalkTo(0x00FE, -220, 0, 74000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2E2E)

    ChrSetDirection(0x0101, 180, 400)
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0150330237V#1151F#5P不好意思，在那之前\n',
            '我必须要限制你的自由。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150330238V需要什么东西\n',
            '尽管跟他们说就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    SetScenaFlags(ScenaFlag(0x0392, 3, 0x1C93))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C5400._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x2EED
@scena.Code('func_03_2EED')
def func_03_2EED():
    OP_99(0x0009, 0x09, 0x0F, 3500)
    ChrSetChipByIndex(0x0009, 3)
    OP_99(0x0009, 0x00, 0x05, 3500)
    PlaySE(501, 0x00, 0x64)

    Return()

# id: 0x0004 offset: 0x2F0A
@scena.Code('func_04_2F0A')
def func_04_2F0A():
    ChrSetChipByIndex(0x0101, 10)
    ChrSetFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_2F1A')
    def lambda_2F1A():
        ChrWalkTo(0x00FE, -990, 1500, 83550, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F1A)

    Sleep(200)

    ChrSetChipByIndex(0x0101, 20)
    PlaySE(163, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_2F49')
    def lambda_2F49():
        ChrJumpTo(0x00FE, -990, 1800, 83600, 3000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F49)

    Sleep(100)

    @scena.Lambda('lambda_2F6C')
    def lambda_2F6C():
        OP_99(0x00FE, 0x00, 0x07, 2300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2F6C)

    Sleep(100)

    PlaySE(500, 0x00, 0x64)

    Return()

# id: 0x0005 offset: 0x2F81
@scena.Code('func_05_2F81')
def func_05_2F81():
    ChrSetFlags(0x0101, 0x0010)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 1)
    ChrSetChipByIndex(0x0101, 11)

    @scena.Lambda('lambda_2FA0')
    def lambda_2FA0():
        ChrJumpTo(0x00FE, -880, 0, 79690, 1500, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FA0)

    WaitForThreadExit(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_2FC8')
    def lambda_2FC8():
        ChrJumpTo(0x00FE, -920, 0, 77370, 500, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FC8)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2FEB')
    def lambda_2FEB():
        ChrMoveTo(0x00FE, -840, 0, 76070, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FEB)

    Sleep(100)

    @scena.Lambda('lambda_300B')
    def lambda_300B():
        ChrMoveTo(0x00FE, -840, 0, 76070, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_300B)

    Sleep(100)

    @scena.Lambda('lambda_302B')
    def lambda_302B():
        ChrMoveTo(0x00FE, -840, 0, 76070, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_302B)

    WaitForThreadExit(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0101, 0x0010)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 12)
    ChrSetSubChip(0x0101, 0)

    Return()

# id: 0x0006 offset: 0x305F
@scena.Code('func_06_305F')
def func_06_305F():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3075')
    def lambda_3075():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3075)

    ChrWalkTo(0x00FE, -4420, 1500, 84600, 1500, 0x00)
    ChrWalkTo(0x00FE, -4070, 1500, 83840, 1500, 0x00)

    Return()

# id: 0x0007 offset: 0x30AA
@scena.Code('func_07_30AA')
def func_07_30AA():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_30C0')
    def lambda_30C0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_30C0)

    ChrWalkTo(0x00FE, 2730, 1500, 84850, 1500, 0x00)
    ChrWalkTo(0x00FE, 1430, 1500, 83000, 1500, 0x00)
    ChrSetDirection(0x00FE, 205, 400)
    ChrSetChipByIndex(0x00FE, 17)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0008 offset: 0x3106
@scena.Code('func_08_3106')
def func_08_3106():
    ChrSetSubChip(0x0011, 0)
    ChrSetPos(0x0011, 570, 1500, 84590, 180)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_312D')
    def lambda_312D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 90, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_312D)

    ChrClearFlags(0x0011, 0x0080)
    ChrMoveToRelativeAsync(0x0011, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, 100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, -100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, 50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, -50, 0, 0, 300, 0x00)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 500)
    ChrSetFlags(0x0011, 0x0080)

    Return()

# id: 0x0009 offset: 0x31C7
@scena.Code('func_09_31C7')
def func_09_31C7():
    ChrSetSubChip(0x0012, 0)
    ChrSetPos(0x0012, 570, 1500, 84590, 180)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_31EE')
    def lambda_31EE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 90, 500)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_31EE)

    ChrClearFlags(0x0012, 0x0080)
    ChrMoveToRelativeAsync(0x0012, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0012, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0012, -100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0012, 100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0012, -50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0012, 50, 0, 0, 300, 0x00)
    ChrSetRGBAMask(0x0012, 255, 255, 255, 0, 500)
    ChrSetFlags(0x0012, 0x0080)

    Return()

# id: 0x000A offset: 0x3288
@scena.Code('func_0A_3288')
def func_0A_3288():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(210, 0, 53260, 0)
    OP_67(0, 8540, -10000, 0)
    CameraSetDistance(2860, 0)
    OP_6C(45000, 0)
    OP_6E(551, 0)
    ChrSetPos(0x000D, -1190, 1500, 85710, 0)
    ChrClearFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_32F7')
    def lambda_32F7():
        CameraMove(-970, 5670, 90410, 8000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_32F7)

    @scena.Lambda('lambda_330F')
    def lambda_330F():
        OP_67(0, 4170, -10000, 8000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_330F)

    @scena.Lambda('lambda_3327')
    def lambda_3327():
        CameraSetDistance(3050, 8000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_3327)

    @scena.Lambda('lambda_3337')
    def lambda_3337():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_3337)

    @scena.Lambda('lambda_3347')
    def lambda_3347():
        OP_6E(449, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3347)

    OP_71(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x000D, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(-450, 1500, 86520, 0)
    OP_67(0, 5960, -10000, 0)
    CameraSetDistance(2920, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    OP_71(0x0004, 0x0004)
    OP_79(0x09, 0x0002)
    OP_7B()
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0190400522V#850F#2P呵呵，相当\n',
            '令人期待不是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190400523V看这个样子，\n',
            '今天就能到达中枢塔了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190400524V#855F不过，如果就这么照计划进行，\n',
            '『观察者』的意义就不存在了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 180, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0190400525V#853F#5P在真正的最终幕上演之前，\n',
            '似乎还有点时间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190400526V#854F在此之前去捉弄一下\n',
            '基尔巴特来取乐好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，艾丝蒂尔等人\n',
            '和空贼们一起从『古罗力亚斯』逃了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '途中与追赶上来的强化猎兵\n',
            '数次展开交战之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人甩开追击，\n',
            '设法回到了居住区域。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C5801._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
