import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3131_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3131.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x10B4
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_67(0, 5630, -10000, 1000)
    OP_4A(0x0009, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_85E',
    )

    ChrTalk(
        0x0009,
        (
            '#2100180782V哦，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170235V#010F您正在工作啊，打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180786V我们看了公告板，\n',
            '把您要的食材带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B')

    def _loc_14B(): pass

    label('loc_14B')

    ChrTalk(
        0x0101,
        (
            '#0010180783V#000F打扰一下可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180784V我们看了公告板，\n',
            '把您要的食材带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19B(): pass

    label('loc_19B')

    ChrTalk(
        0x0101,
        (
            '#0010180787V#000F因为我们还有急事，\n',
            '所以请快一点好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2100180788V哦，好的。\n',
            '让我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2100180789V唔唔哦哦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0009)

    If(
        (
            (Expr.Eval, "OP_40(0x0385)"),
            Expr.Return,
        ),
        'loc_7B8',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2100180790V…………………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180791V哦，\n',
            '让我看看这个西红柿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '苦西红柿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0009,
        (
            '#2100180792V我来尝尝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180793V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2100180794V…………呸、呸呸！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2100180795V这、这是什么啊！？\n',
            '简直苦得要命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180796V#506F对吧？\n',
            '这个西红柿很难吃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180797V唔唔～嗯，的确，\n',
            '这个样子是没法吃的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180798V但就凭这个强烈的味道和香味，\n',
            '如果精心调配的话，\n',
            '说不定可以弄出很有趣的料理来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180799V#501F如、如果调配之后还是弄不出好味道，\n',
            '应该就没有吃的必要了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180800V不见得。\n',
            '难吃的食材反而会\n',
            '含有许多对人体很有益的成分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180801V因此遵照传统，\n',
            '蔡斯这里的料理\n',
            '采用了各种各样刺激性的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180802V#509F奇、奇怪的料理～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180803V总、总之这样\n',
            '委托就算完成了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180804V哦，是啊。\n',
            '你们等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2100180805V……嗯，和肉类搭配起来，\n',
            '这个苦味也可能成为美味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180806V给，试验第１号作品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '苦西红柿三明治',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010180807V#506F啊、啊哈哈……\n',
            '多谢您的款待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180808V呵呵，别介意，尝尝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180809V那么，我也要开工了。\n',
            '今天谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180810V#000F嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180811V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    RemoveItem(0x0385, 1)
    AddItem(0x0199, 1)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【寻找新奇食材】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002B, 0x04, 0x10)
    OP_28(0x002B, 0x01, 0x0004)
    OP_28(0x002B, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_85B')

    def _loc_7B8(): pass

    label('loc_7B8')

    ChrTalk(
        0x0009,
        (
            '#2100180812V……唔～还不到位啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180813V我需要更加有个性的、\n',
            '更加有味道的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180814V#505F唔～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180815V#000F那我们再去找其它的来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002B, 0x01, 0x0001)
    OP_28(0x002B, 0x01, 0x0002)

    def _loc_85B(): pass

    label('loc_85B')

    Jump('loc_10A7')

    def _loc_85E(): pass

    label('loc_85E')

    ChrTalk(
        0x0009,
        (
            '#2100180782V哦，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8DC',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170235V#010F您正在工作啊，打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180786V我们看了公告板，\n',
            '把您要的食材带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98C')

    def _loc_8DC(): pass

    label('loc_8DC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_935',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180821V#060F你好，贝恩师傅。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180822V我们是来给您\n',
            '送料理用的食材的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98C')

    def _loc_935(): pass

    label('loc_935')

    ChrTalk(
        0x0101,
        (
            '#0010180783V#000F打扰一下可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180784V我们看了公告板，\n',
            '把您要的食材带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    def _loc_98C(): pass

    label('loc_98C')

    ChrTalk(
        0x0009,
        (
            '#2100180823V好，让我看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2100180789V唔唔哦哦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0009)

    If(
        (
            (Expr.Eval, "OP_40(0x0385)"),
            Expr.Return,
        ),
        'loc_1004',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2100180790V…………………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180791V哦，\n',
            '让我看看这个西红柿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '苦西红柿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0009,
        (
            '#2100180827V看起来是个普通的西红柿，\n',
            '但是香味要浓得多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180828V我来尝尝，哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180793V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2100180794V…………呸、呸呸！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#2100180795V这、这是什么啊！？\n',
            '简直苦得要命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180832V#506F对吧？\n',
            '这个西红柿很难吃呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180833V应该是研究的副产品，\n',
            '好像不能拿来吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2100180797V唔唔～嗯，的确，\n',
            '这个样子是没法吃的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180798V但就凭这个强烈的味道和香味，\n',
            '如果精心调配的话，\n',
            '说不定可以弄出很有趣的料理来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180799V#501F如、如果调配之后还是弄不出好味道，\n',
            '应该就没有吃的必要了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180800V不见得。\n',
            '难吃的食材反而会\n',
            '含有许多对人体很有益的成分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180801V因此遵照传统，\n',
            '蔡斯这里的料理\n',
            '采用了各种各样刺激性的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180839V#509F奇、奇怪的料理～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070180840V#067F哈，哈哈……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DB0(): pass

    label('loc_DB0')

    OP_62(0x0009, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#2100180805V……嗯，和肉类搭配起来，\n',
            '这个苦味也可能成为美味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180842V看吧，\n',
            '新料理之试验第１号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180843V就作为你们\n',
            '帮我寻找优秀食材的奖品吧。\n',
            '不要顾虑，放心品尝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '苦西红柿三明治',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010180807V#506F啊、啊哈哈……\n',
            '多谢您的款待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180845V嗯，那好。\n',
            '我也要开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180846V谢了。\n',
            '今天多亏你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180847V#000F嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180848V#010F那么我们就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    RemoveItem(0x0385, 1)
    AddItem(0x0199, 1)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【寻找新奇食材】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002B, 0x04, 0x10)
    OP_28(0x002B, 0x01, 0x0004)
    OP_28(0x002B, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_10A7')

    def _loc_1004(): pass

    label('loc_1004')

    ChrTalk(
        0x0009,
        (
            '#2100180812V……唔～还不到位啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2100180813V我需要更加有个性的、\n',
            '更加有味道的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180814V#505F唔～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180815V#000F那我们再去找其它的来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002B, 0x01, 0x0001)
    OP_28(0x002B, 0x01, 0x0002)
    def _loc_10A7(): pass

    label('loc_10A7')

    EventEnd(0x01)
    OP_4B(0x0009, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
