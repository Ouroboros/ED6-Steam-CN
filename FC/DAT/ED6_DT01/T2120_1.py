import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2120_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2120_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2120.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    TalkBegin(0x00FF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_88',
    )

    OP_2A(0x0024, 0x0021, 0x0022, 0x0026, 0x001D, 0x001E, 0x001F, 0x0020, 0x0023, 0x0025, 0xFFFF)

    Jump('loc_101')

    def _loc_88(): pass

    label('loc_88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_A9',
    )

    OP_2A(0x0024, 0x0021, 0x0022, 0x0026, 0x001D, 0x001E, 0x001F, 0x0020, 0x0023, 0x0025, 0xFFFF)

    Jump('loc_101')

    def _loc_A9(): pass

    label('loc_A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_C8',
    )

    OP_2A(0x0024, 0x0021, 0x0022, 0x0026, 0x001D, 0x001E, 0x001F, 0x0020, 0x0023, 0xFFFF)

    Jump('loc_101')

    def _loc_C8(): pass

    label('loc_C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_E7',
    )

    OP_2A(0x0024, 0x0021, 0x0022, 0x0026, 0x001D, 0x001E, 0x001F, 0x0020, 0x0023, 0xFFFF)

    Jump('loc_101')

    def _loc_E7(): pass

    label('loc_E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_FC',
    )

    OP_2A(0x0024, 0x0021, 0x0022, 0x0026, 0xFFFF)

    Jump('loc_101')

    def _loc_FC(): pass

    label('loc_FC')

    OP_2A(0x0024, 0xFFFF)

    def _loc_101(): pass

    label('loc_101')

    TalkEnd(0x00FF)

    Return()

# id: 0x0001 offset: 0x105
@scena.Code('func_01_105')
def func_01_105():
    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_274',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    OP_28(0x001D, 0x01, 0x8000)

    ChrTalk(
        0x000B,
        (
            '#1750160243V哦，\n',
            '看样子进行得很顺利嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160244V#010F是的，\n',
            '已经安全地送到弗科特老人手里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160245V#001F老爷爷他也十分精神健康呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160246V哦，是吗。\n',
            '那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160247V再见了。\n',
            '以后有什么事情还得拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141612V#010F彼此彼此，请多多关照。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160249V#001F嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EB')

    def _loc_274(): pass

    label('loc_274')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B7',
    )

    ChrTalk(
        0x000B,
        (
            '#1750160250V哦，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0003)

    Jump('loc_3EB')

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_322',
    )

    ChrTalk(
        0x000B,
        (
            '#1750160251V哦，办完事情了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160252V运送维修工具箱的工作\n',
            '可以开始了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    Jump('loc_3EB')

    def _loc_322(): pass

    label('loc_322')

    ChrTalk(
        0x0101,
        (
            '#0010160239V#000F请问您是索姆茨先生吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160240V我们是游击士协会派来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160241V哦，是运送维修工具箱的事吧。\n',
            '我正在等你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160242V如何，\n',
            '可以现在就去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0002)

    def _loc_3EB(): pass

    label('loc_3EB')

    TalkEnd(0x000B)

    Return()

# id: 0x0002 offset: 0x3EF
@scena.Code('func_02_3EF')
def func_02_3EF():
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_44E'),
        (0x00000001, 'loc_1025'),
        (-1, 'loc_10E9'),
    )

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_5ED',
    )

    OP_28(0x001D, 0x04, 0x08)

    ChrTalk(
        0x000B,
        (
            '#1750160253V太好了，\n',
            '那么我就把这个庞然大物交给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '维修工具箱',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0326, 1)

    ChrTalk(
        0x000B,
        (
            '#1750160254V把这个箱子\n',
            '亲手交给巴伦诺灯塔的\n',
            '弗科特老人就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160255V因为都是些比较昂贵的物品，\n',
            '所以一定要小心才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160256V巴伦诺灯塔\n',
            '位于玛诺利亚村西面、\n',
            '三叉路口南面的海角上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160257V……就是这样的。\n',
            '那么就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Jump('loc_1022')

    def _loc_5ED(): pass

    label('loc_5ED')

    OP_28(0x001D, 0x04, 0x04)
    OP_28(0x001D, 0x04, 0x08)
    OP_28(0x001D, 0x01, 0x0001)
    OP_28(0x001D, 0x01, 0x0002)

    ChrTalk(
        0x000B,
        (
            '#1750160258V太好了，\n',
            '那么我就把这个庞然大物交给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160259V#004F庞、庞然大物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0000, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160260V有点重，小心点哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '维修工具箱',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0326, 1)

    ChrTalk(
        0x000B,
        (
            '#1750160261V你们能行吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160262V交换用的导力器部件\n',
            '和套装工具等东西\n',
            '全部都装在里面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160263V#000F运送到巴伦诺灯塔就可以了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160264V啊，是的，\n',
            '一定要亲手交给看守灯塔的\n',
            '弗科特老人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160255V因为都是些比较昂贵的物品，\n',
            '所以一定要小心才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160266V……对了，\n',
            '我听嘉恩那小子说了哦。\n',
            '说实话，我还真没想到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160267V#000F嗯？什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160268V当然是关于你们啊，\n',
            '虽然听说你们身手敏捷、活蹦乱跳的，\n',
            '但没有想到竟然如此年轻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160269V#506F活、活蹦乱跳……\n',
            '我又不是小兔子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160270V不过啊，\n',
            '现在我反而对你们这么年轻感到担忧呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160271V#009F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160272V我说叔叔！\n',
            '年轻是年轻，\n',
            '但不见得年纪小就没能力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#1750160273V啊，不、不是！\n',
            '我不是那个意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160274V……我是认为弗科特老人\n',
            '可能会这么想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001C, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_B65',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160275V#505F哦～原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160276V怎么了，\n',
            '你们认识他老人家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160277V#506F嗯，\n',
            '的确是位比较难应付的老爷爷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160278V#017F唉，我们之前受过他的训导……\n',
            '所以对他的事情也略知一二。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160279V哈哈哈～\n',
            '听你们这么说就没问题了，\n',
            '看来你们明白我的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C90')

    def _loc_B65(): pass

    label('loc_B65')

    ChrTalk(
        0x0101,
        (
            '#0010160280V#000F弗科特老人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160281V#010F那位老人家怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160282V唔～\n',
            '事实上弗科特老人他\n',
            '是一个性格有点乖僻的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160283V他经常会针对年轻人\n',
            '说一些过分挑剔的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160284V#509F……总之就是一个怪人，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160285V……嗯，\n',
            '这么说的确也毫不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C90(): pass

    label('loc_C90')

    ChrTurnDirection(0x000B, 0x0000, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160286V不过，\n',
            '你们也得理解他老人家的心情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160287V看守灯塔是一件很孤独的工作，\n',
            '性格变得倔犟也是情有可原的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160288V#040F对于航行中的船只而言，\n',
            '灯塔就像安全带一样重要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160289V看守灯塔的工作\n',
            '是要肩负很重大的责任的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160290V#003F这样啊……\n',
            '的确是很费力的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160291V在他老人家还是个渔夫的时候，\n',
            '总是爱去『拉旺塔尔』喝酒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160292V但是现在一直住在灯塔，\n',
            '几乎就没什么机会再去喝\n',
            '那里著名的鸡尾酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160293V真是沉重的话题啊。\n',
            '我好想把酒\n',
            '也给他捎去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160294V哦，\n',
            '我一说起来就没完没了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160295V就是因为我说的这些原因，\n',
            '他老人家如果说了什么不中听的话，\n',
            '你们可别往心里去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160296V#000F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160297V那我们这就出发了，\n',
            '您还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160298V不，已经没了。\n',
            '如果有疑问或者想取消任务的话，\n',
            '就再到这里来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160299V那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1022(): pass

    label('loc_1022')

    Jump('loc_10E9')

    def _loc_1025(): pass

    label('loc_1025')

    OP_28(0x001D, 0x01, 0x4000)

    ChrTalk(
        0x0101,
        (
            '#0010160300V#505F唔，\n',
            '现在有些不太方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160301V这样啊。\n',
            '那么等你们办完事情之后\n',
            '再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160302V我这里的事情有些急，\n',
            '如果可以的话，\n',
            '还请你们尽快过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10E9')

    def _loc_10E9(): pass

    label('loc_10E9')

    TalkEnd(0x000B)

    Return()

# id: 0x0003 offset: 0x10ED
@scena.Code('func_03_10ED')
def func_03_10ED():
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【再次确认委托内容】\n'),
            TXT(0x01, '【取消委托任务】\n'),
            TXT(0x02, '【没什么事】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1175'),
        (0x00000001, 'loc_1230'),
        (0x00000002, 'loc_1384'),
        (-1, 'loc_13A7'),
    )

    def _loc_1175(): pass

    label('loc_1175')

    ChrTalk(
        0x000B,
        (
            '#1750160303V把给你们的维修工具箱\n',
            '亲手交给巴伦诺灯塔的\n',
            '弗科特老人就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160256V巴伦诺灯塔\n',
            '位于玛诺利亚村西面、\n',
            '三叉路口南面的海角上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160305V那么就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A7')

    def _loc_1230(): pass

    label('loc_1230')

    OP_28(0x001D, 0x03, 0x08)
    OP_28(0x001D, 0x01, 0x4000)

    ChrTalk(
        0x0101,
        (
            '#0010160306V#007F抱歉，索姆茨先生。\n',
            '我们突然有件很急的事要办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#1750160307V哦，我知道了。\n',
            '这种事情是没办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1750160308V那就暂且先把\n',
            '工具箱还给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '维修工具箱',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0326, 1)

    ChrTalk(
        0x000B,
        (
            '#1750160302V我这里的事情有些急，\n',
            '如果可以的话，\n',
            '还请你们尽快过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A7')

    def _loc_1384(): pass

    label('loc_1384')

    ChrTalk(
        0x000B,
        (
            '#1750160305V那么就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A7')

    def _loc_13A7(): pass

    label('loc_13A7')

    TalkEnd(0x000B)

    Return()

# id: 0x0004 offset: 0x13AB
@scena.Code('func_04_13AB')
def func_04_13AB():
    OP_28(0x0022, 0x04, 0x10)
    OP_28(0x0022, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    RemoveItem(0x0067, 1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 4, 0x42C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_176D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170945V#501F那个试制的导力枪\n',
            '是不是就是这个呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '试·零式导力枪',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1890170946V哎呀……！\n',
            '怎、怎么会！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170947V为、为什么，\n',
            '你们从哪儿得到的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170948V#010F从在『绀碧之塔』消灭的通缉魔兽那里得到的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170949V很可能是由于\n',
            '导力器里的七耀石吸引了它们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170950V啊啊，女神啊！\n',
            '由衷地感谢您！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170951V呼～～\n',
            '找到了就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170952V#000F那么这样任务就算完成了吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170953V#010F对不起，\n',
            '我们这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1890170954V啊，\n',
            '不用那么急急忙忙的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170955V稍等一下，\n',
            '请你们务必收下这个东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '攻击２',
            (TxtCtl.SetColor, 0x0),
            '的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#1890170956V这是我小小的心意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170957V你们在日后的工作中\n',
            '也要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170958V#508F嗯，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F65')

    def _loc_176D(): pass

    label('loc_176D')

    ChrTalk(
        0x0101,
        (
            '#0010170959V#002F……啊，难道是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170960V那个试制的导力枪\n',
            '是不是就是这个呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '试·零式导力枪',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1890170946V哎呀……！\n',
            '怎、怎么会！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170947V为、为什么，\n',
            '你们从哪儿得到的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170948V#010F从在『绀碧之塔』消灭的通缉魔兽那里得到的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170949V很可能是由于\n',
            '导力器里的七耀石吸引了它们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170950V啊啊，女神啊！\n',
            '由衷地感谢您！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170966V啊啊啊啊，你们！\n',
            '我已经激动地说不出话了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170967V总、总之现在让我\n',
            '紧紧拥抱你们亲上几口以表谢意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170968V#008F哇哇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170969V我、我就免了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1A66',
    )

    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060170970V#045F我、我也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A66(): pass

    label('loc_1A66')

    ChrTalk(
        0x0102,
        (
            '#0020170971V#018F……我也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170972V呼呼～～～～\n',
            '是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020170973V#010F这个试制品有这么重要吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170974V啊，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170975V不管怎么说这可是\n',
            '蔡斯中央工房研究中的试制品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170976V离预定的上市日期\n',
            '还有一段时间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170977V#004F啊～听你这么说，\n',
            '它的性能应该相当不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170978V你对武器很有兴趣吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170979V哦，你们是游击士，\n',
            '关心这类商品也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170980V那么，我就把这个结晶回路\n',
            '送给你们作为谢礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170981V如果你们能用得上它的话\n',
            '就再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '攻击２',
            (TxtCtl.SetColor, 0x0),
            '的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020170982V#014F真过意不去，\n',
            '还送我们这么好的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170983V没什么没什么，\n',
            '你们帮了我很大的忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170984V正式的报酬我也会通过协会支付给你们的，\n',
            '请放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170985V#004F哎，\n',
            '还要支付米拉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1890170986V嗯，不要介意啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170987V反正都是记在\n',
            '中央工房的金库的账上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170988V#509F不、不是，\n',
            '我不是这个意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170989V这样不是也很好吗。\n',
            '这种情况下\n',
            '就不要推托了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170990V总之，\n',
            '今天谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1890170991V如果再有什么事情的话，\n',
            '还得麻烦你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F65(): pass

    label('loc_1F65')

    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【搜寻试制品】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    AddItem(0x025F, 1)
    ChrSetDirection(0x00FE, 0, 400)
    EventEnd(0x01)
    TalkEnd(0x000C)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
