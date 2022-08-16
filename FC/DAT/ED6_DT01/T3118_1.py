import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3118_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3118_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3118.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-2930, 0, 6630, 0)
    ChrSetPos(0x0101, -2950, 0, 6740, 90)
    ChrSetPos(0x0102, -2810, 0, 5490, 45)
    ChrSetPos(0x0107, -3850, 0, 6140, 90)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_479',
    )

    ChrTalk(
        0x00FE,
        (
            '#2000180924V呼，真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180925V我绝对不会\n',
            '放过这个家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 1, 0x589)),
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 2, 0x58A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2C9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180926V#000F米妮亚姆医生，您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180927V#060F您好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180928V哎呀，你好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180929V啊，还有两位客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180930V#000F我们是看了公告板而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180931V啊，说起来\n',
            '还没有自我介绍过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180932V我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170616V#010F和她一样，我叫约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180934V好像发生了什么案件呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    Jump('loc_3F7')

    def _loc_2C9(): pass

    label('loc_2C9')

    SetScenaFlags(ScenaFlag(0x00B1, 1, 0x589))
    SetScenaFlags(ScenaFlag(0x00B1, 2, 0x58A))

    ChrTalk(
        0x0107,
        (
            '#0070180935V#060F米妮亚姆医生，您好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180928V哎呀，你好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180929V啊，还有两位客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180938V#000F嗯，我们是看了公告板而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180932V我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170616V#010F和她一样，我叫约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180934V好像发生了什么案件呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    def _loc_3F7(): pass

    label('loc_3F7')

    ChrTalk(
        0x00FE,
        (
            '#2000180942V嗯……实际上是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180943V如果可以的话，\n',
            '我希望你们现在就展开调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180944V可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CD')

    def _loc_479(): pass

    label('loc_479')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180950V哎呀，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180951V如何？\n',
            '现在可以进行调查了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4CD(): pass

    label('loc_4CD')

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
        10,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0001)

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

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_621',
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010180945V#505F嗯～\n',
            '现在还不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180946V这可就麻烦了，\n',
            '情况很紧急呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180947V可是既然你们没空，\n',
            '那也就没办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180948V#006F对不起，\n',
            '我们会尽快回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180949V嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x2000)

    @scena.Lambda('lambda_0616')
    def lambda_0616():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0616)

    EventEnd(0x00)

    Return()

    def _loc_621(): pass

    label('loc_621')

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010180952V#006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180953V#012F请您立刻说明案件详情吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180954V说起来其实很简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180955V不知道是谁从这个橱柜里\n',
            '把香烟拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180956V#505F这里是医务室啊，\n',
            '怎么会有香烟呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180957V在我的倡导下，\n',
            '工房这几年都在开展禁烟运动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180958V这个运动中所没收的香烟，\n',
            '都被集中到这里来放置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180959V#012F这么说来，\n',
            '有嫌疑的就是以前香烟被没收过的人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180960V拿走香烟的很可能就是那些人。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180961V#064F啊，的确是这样呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180962V嗯，我也是这么估计的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180963V现在，禁烟运动\n',
            '好不容易才算得到了推广……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180964V如果让这个不守规矩的家伙\n',
            '再这么恣意妄为下去，\n',
            '持续至今的努力就会化为泡影了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180965V#012F总而言之，\n',
            '嫌疑就集中在原来那些吸烟者身上吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180966V有没有怀疑的对象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180967V最为可疑的就是\n',
            '演算室的特莱斯主任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180968V主任看上去就是那种\n',
            '老烟鬼级别的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180969V他刚开始戒烟不久，\n',
            '具有非常充分的动机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180970V#505F呼～不太记得他的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180971V#004F……啊，我要先做一下笔记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180972V然后就是\n',
            '设计室的雨果先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180973V他现在应该在\n',
            '一楼的大厅和别人谈话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180974V他很早以前就来工房工作了，\n',
            '也有吸烟的习惯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180975V#064F哦～原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180976V#010F演算室的特莱斯主任以及\n',
            '在一楼和别人谈话的雨果先生对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180977V还有什么别的情报吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180978V没有的话我们就展开调查了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180979V对了，还有一件事，\n',
            '不知道能不能对你们有帮助……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180980V当时有一个目击者哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180981V#004F………………啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180982V这、这不就是\n',
            '决定性的线索吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180983V#012F目击者是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x000B, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180984V就在你们后面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180985V安东尼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D3B',
    )

    @scena.Lambda('lambda_0D33')
    def lambda_0D33():
        ChrTurnDirection(0x0001, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0D33)

    def _loc_D3B(): pass

    label('loc_D3B')

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D5A',
    )

    @scena.Lambda('lambda_0D52')
    def lambda_0D52():
        ChrTurnDirection(0x0002, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0D52)

    def _loc_D5A(): pass

    label('loc_D5A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D74',
    )

    @scena.Lambda('lambda_0D6C')
    def lambda_0D6C():
        ChrTurnDirection(0x0003, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0D6C)

    def _loc_D74(): pass

    label('loc_D74')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D8E',
    )

    @scena.Lambda('lambda_0D86')
    def lambda_0D86():
        ChrTurnDirection(0x0004, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0D86)

    def _loc_D8E(): pass

    label('loc_D8E')

    ChrTurnDirection(0x0000, 0x000B, 400)
    Sleep(800)

    OP_4A(0x000B, 255)
    OP_62(0x000B, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(400)

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000B,
        (
            '#2030180986V喵～～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180987V#004F小、小猫～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2000180988V明白了吧？\n',
            '所以我才说不知道能不能帮上你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180989V#018F……原来如此，我了解了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070180990V#063F可、可是，\n',
            '安东尼是一只很聪明的小猫呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180991V也许它真的知道犯人是谁呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180992V是啊，如果带着它进行搜查，\n',
            '所不定会找到什么线索呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180993V猫的嗅觉也是很灵敏的呢，\n',
            '与狗相比也毫不逊色哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180994V#000F啊，真期待它的表现呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180995V如果把它喜欢的\n',
            '『新鲜牛奶』拿来的话， \n',
            '它一定会很高兴地跟随在你们后面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180996V如果实在找不到线索，\n',
            '那就一定要用它来试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180997V#000F嗯，我们会参考这一点的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10BA')
    def lambda_10BA():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_10BA)

    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180998V#010F如果我们有什么收获，\n',
            '会立刻来通知您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2000180999V期待你们的表现。\n',
            '一定要抓住犯人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x04, 0x08)
    OP_28(0x002C, 0x04, 0x04)
    OP_28(0x002C, 0x01, 0x0001)
    OP_28(0x002C, 0x01, 0x0002)
    OP_28(0x002C, 0x01, 0x0004)
    ChrClearFlags(0x00FE, 0x0010)

    @scena.Lambda('lambda_1163')
    def lambda_1163():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1163)

    EventEnd(0x00)
    OP_4B(0x000B, 255)

    Return()

# id: 0x0003 offset: 0x1172
@scena.Code('func_03_1172')
def func_03_1172():
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
            TXT(0x00, '【喂它新鲜牛奶】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11CE',
    )

    Return()

    def _loc_11CE(): pass

    label('loc_11CE')

    RemoveItem(0x038A, 1)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1257',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181000V#507F乖，安东尼，\n',
            '你最喜欢的牛奶哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '#2030181001V喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1356')

    def _loc_1257(): pass

    label('loc_1257')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12CF',
    )

    ChrTalk(
        0x0102,
        (
            '#0020181002V#019F安东尼。\n',
            '给，牛奶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '#2030181001V喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1356')

    def _loc_12CF(): pass

    label('loc_12CF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1356',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181004V#066F安东尼～乖孩子～\n',
            '我给你带来了牛奶哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '#2030181001V喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1356(): pass

    label('loc_1356')

    Fade(1000)
    ChrSetFlags(0x000B, 0x0080)
    FormationAddMember(0x3B, 0xFF)
    OP_0D()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x1368
@scena.Code('func_04_1368')
def func_04_1368():
    EventBegin(0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1380',
    )

    FormationDelMember(0x3B, 0xFF)
    ChrClearFlags(0x000B, 0x0080)

    def _loc_1380(): pass

    label('loc_1380')

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    OP_4A(0x0008, 0)
    CameraMove(-6080, 0, 7020, 0)
    OP_6C(16000, 0)
    ChrSetPos(0x0008, -6740, 0, 7040, 135)
    ChrSetPos(0x000D, -5840, 0, 6240, 315)
    ChrSetPos(0x000B, -7340, 0, 6050, 130)
    ChrSetPos(0x0101, -4730, 0, 6330, 225)
    ChrSetPos(0x0102, -5570, 0, 5260, 315)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_141C',
    )

    ChrSetPos(0x0107, -4620, 0, 5220, 324)

    def _loc_141C(): pass

    label('loc_141C')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_143B',
    )

    ChrSetPos(0x0106, -3390, 0, 6350, 267)

    def _loc_143B(): pass

    label('loc_143B')

    OP_0D()
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#2000181151V……真是的，\n',
            '我真是想不吃惊都不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181152V我怎么也想不到，\n',
            '竟然是工房长您的所为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0550181153V#805F#2P实、实在对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181154V我其实只是想抽一支而已。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181155V没想到就鬼使神差地……\n',
            '我不知道怎么形容才好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181156V#803F米妮亚姆医生……\n',
            '我真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181157V可是，工房长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181158V我的确记得很早以前\n',
            '您就已经戒烟了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0550181159V#802F#2P啊、啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181160V已经差不多戒了十年了吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181161V#004F啊？那么久了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181162V可怎么会突然之间\n',
            '又想要抽烟了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 45, 400)

    ChrTalk(
        0x000D,
        (
            '#0550181163V#806F#2P唔唔，\n',
            '连我自己也不是很清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181164V导力停止现象之后，\n',
            '市民的抱怨变得很厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181165V我一直在想怎么解决，\n',
            '那时不知为何\n',
            '竟然又想抽起烟来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181166V呼啊～…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(120)

    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070181167V#065F工、工房长叔叔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181168V#561F对、对不起啊。\n',
            '都是爷爷的缘故……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x000D, 135, 400)

    ChrTalk(
        0x000D,
        (
            '#0550181169V#805F#2P不、不是的，提妲。\n',
            '你用不着道歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181170V这次的事情和博士无关，\n',
            '是我的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181171V#003F工房长您还是好好休息一下吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181172V#017F想吸烟的原因\n',
            '很可能是由于压力过高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181173V工房长…………\n',
            '事情我已经明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181174V这次的事情\n',
            '就既往不咎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrSetDirection(0x000D, 315, 400)

    ChrTalk(
        0x000D,
        (
            '#0550181175V#802F#2P啊？\n',
            '真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181176V不过我希望……\n',
            '您能好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181177V这样子下去\n',
            '身体会吃不消的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0550181178V#806F#2P啊，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181179V#806F等事情告一段落之后，\n',
            '我保证会好好休息的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181180V#803F米妮亚姆医生……\n',
            '今天实在是太过意不去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181181V好了，过去的就算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181182V保重身体才是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0550181183V#800F#2P啊，我会好好注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 135, 400)

    ChrTalk(
        0x000D,
        (
            '#0550181184V#800F#2P那么我就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B59')
    def lambda_1B59():
        ChrTurnDirection(0x0008, 0x000D, 0)
        Yield()

        Jump('lambda_1B59')

    DispatchAsync2(0x0008, 0x0001, lambda_1B59)

    @scena.Lambda('lambda_1B6A')
    def lambda_1B6A():
        ChrTurnDirection(0x0101, 0x000D, 0)
        Yield()

        Jump('lambda_1B6A')

    DispatchAsync2(0x0101, 0x0001, lambda_1B6A)

    @scena.Lambda('lambda_1B7B')
    def lambda_1B7B():
        ChrTurnDirection(0x0102, 0x000D, 0)
        Yield()

        Jump('lambda_1B7B')

    DispatchAsync2(0x0102, 0x0001, lambda_1B7B)

    @scena.Lambda('lambda_1B8C')
    def lambda_1B8C():
        ChrTurnDirection(0x0107, 0x000D, 0)
        Yield()

        Jump('lambda_1B8C')

    DispatchAsync2(0x0107, 0x0001, lambda_1B8C)

    ChrSetFlags(0x000D, 0x0040)
    ChrWalkTo(0x000D, -6480, 0, 5030, 3000, 0x00)
    ChrWalkTo(0x000D, -6140, 0, 1980, 3000, 0x00)
    ChrWalkTo(0x000D, -3030, 0, 750, 3000, 0x00)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0107, 0x01)
    ChrWalkTo(0x000D, -310, 0, 950, 3000, 0x00)
    PlaySE(109, 0x00, 0x64)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x000D, 0x0040)
    Sleep(800)

    PlaySE(109, 0x00, 0x64)

    @scena.Lambda('lambda_1C1B')
    def lambda_1C1B():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C1B)

    @scena.Lambda('lambda_1C29')
    def lambda_1C29():
        ChrSetDirection(0x0102, 315, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1C29)

    @scena.Lambda('lambda_1C37')
    def lambda_1C37():
        ChrSetDirection(0x0107, 315, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1C37)

    ChrSetDirection(0x0008, 135, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010181185V#007F呼～真是好可怜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181186V并不是因为工房长自身的缘故而犯的错误……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181187V#010F可是，作为工房的领导者，\n',
            '认真负责也是工作的内容之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181188V啊，的确是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181189V……嗯。\n',
            '我对你们大家真是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181190V这次事件\n',
            '你们解决得很漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181191V#001F不用谢啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181192V#000F还要多亏了安东尼的帮忙呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181193V#061F呵呵呵，是～啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181194V呵呵，\n',
            '看来我的推荐起了不少作用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181195V以后再碰见它\n',
            '可要好好照顾它哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181196V#006F嗯，好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181197V那么，\n',
            '今天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2000181198V如果以后有什么事的话，\n',
            '还要拜托你们多多帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181199V#010F彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181200V那么我们就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181201V#000F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【禁烟强化周】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x0008, 0)
    OP_28(0x002C, 0x04, 0x10)
    OP_28(0x002C, 0x01, 0x1000)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x1FB1
@scena.Code('func_05_1FB1')
def func_05_1FB1():
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '猫语日常会话入门',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0340, 1)
    ChrSetFlags(0x000E, 0x0080)
    OP_64(0x00, 0x0001)
    OP_28(0x002D, 0x01, 0x0010)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
