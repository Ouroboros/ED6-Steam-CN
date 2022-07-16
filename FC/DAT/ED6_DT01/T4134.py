import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4134_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4134   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '修女艾伦'),
    TXT(0x02, '尤莉亚中尉'),
    TXT(0x03, '男人的声音'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4134.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1821
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
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT06/CH20112._CH', 'ED6_DT06/CH20112P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x11A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_12D',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_12D(): pass

    label('loc_12D')

    Return()

# id: 0x0001 offset: 0x12E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x12F
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(80, 0, -470, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -30, 1000, 17550, 180)
    SetChrPos(0x0009, -30, 1000, 17550, 0)
    SetChrPos(0x0102, 10, 0, 450, 0)
    SetChrPos(0x0101, -360, -250, -3700, 0)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    FadeIn(500, 0)
    ChrWalkTo(0x0101, -520, 0, -1330, 2000, 0x00)
    Sleep(500)

    OP_63(0x0102)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020111310V#012F……不好意思，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111311V好像是我搞错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111312V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0100111313V#3P……呵呵。\n',
            '你们果然来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_02A5')
    def lambda_02A5():
        CameraMove(-290, 1000, 16930, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02A5)

    WaitForThreadExit(0x0101, 0x0002)
    Fade(1000)
    CameraMove(10, 8100, 16470, 0)
    OP_6C(0, 0)
    OP_6E(582, 0)
    OP_67(0, 3500, -10000, 0)
    CameraSetDistance(1490, 0)
    SetChrPos(0x0101, -510, 0, 9550, 0)
    SetChrPos(0x0102, 500, 0, 9640, 0)
    CameraMove(0, 500, 16500, 3000)

    ChrTalk(
        0x0102,
        (
            '#0020111314V#012F您是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111315V#004F你难道是……\n',
            '在周游道遇到过的修女小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100111316V那个时候\n',
            '真是谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100111317V凭那封信的内容就来到这里，\n',
            '你们俩的胆量和智慧真值得嘉许。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111318V#505F那封信，是修女小姐写的啊……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111319V可是，你到底为什么要\n',
            '做出这么耐人寻味的事情呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111320V#015F原来如此……终于明白了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111321V#010F原来是您啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111322V#004F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100111323V呵呵……\n',
            '约修亚真是敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100111324V那么，不好意思……\n',
            '我要把这件闷热的衣服脱掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)

    @scena.Lambda('lambda_052B')
    def lambda_052B():
        CameraMove(10, 500, 19000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_052B)

    SetChrDirection(0x0008, 90, 400)
    SetChrDirection(0x0008, 0, 400)
    PlaySE(203, 0x00, 0x64)
    SetChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrDirection(0x0009, 270, 400)
    SetChrDirection(0x0009, 180, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010111325V#004F#5S啊啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_05A2')
    def lambda_05A2():
        ChrWalkTo(0x00FE, -20, 0, 12850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_05A2)

    @scena.Lambda('lambda_05BD')
    def lambda_05BD():
        OP_67(0, 5010, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_05BD)

    CameraMove(-10, 0, 12730, 3000)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0100111326V#460F我是王室亲卫队独立中队长，\n',
            '尤莉亚·舒华兹中尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111327V很久不见了。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111328V我相信你们一定会来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111329V#010F很久不见了，尤莉亚中尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111330V自从在卢安的飞艇坪分别之后\n',
            '就没有再见过面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111331V#461F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111332V呵呵，明明没过多长时间，\n',
            '感觉却像很久之前的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111333V#509F等、等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111334V为什么尤莉亚小姐\n',
            '会装扮成这个样子呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111335V而且……\n',
            '为什么要把我们叫到这个地方来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111336V#460F我一个一个回答好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111337V首先，这个装扮……\n',
            '七耀教会和利贝尔王家\n',
            '很久以前就有很深厚的关系了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111338V由于理查德上校的阴谋，\n',
            '我们亲卫队不得不过着逃亡的生活，\n',
            '幸亏得到了教会的诸多帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111339V#007F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111340V#460F另外一个问题……\n',
            '叫你们来其实是想拜托你们一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111341V如果你们在明天的决赛中获胜，\n',
            '就能被款待入王城参加晚餐会对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111342V那个时候，我希望你们能和\n',
            '在格兰赛尔城里的女王陛下会面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111343V#004F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111344V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111345V#464F我知道这个请求可能有些自私。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111346V但我们现在被王国军通缉中，\n',
            '所以是不可能潜入王城里去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111347V只能拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111348V#506F……那个。\n',
            '还真是巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111349V#010F我们就是为了与女王陛下见面\n',
            '才参加这次武术大会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111350V#463F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚向尤莉亚说明了\n',
            '雷斯顿要塞的事情和接受拉赛尔博士的委托\n',
            '要向女王传言的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0100111351V#463F原来有这样的事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111352V#465F啊啊～女神啊。\n',
            '感谢您伟大的慈悲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111353V这样的话，\n',
            '我要拜托你们的事情就只有一件了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111354V#460F希望你们能和深陷困境的陛下好好谈谈。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111355V#006F嗯，本来就打算这么做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111356V#010F虽然协会有不干涉国家内政的规约，\n',
            '但对目前的事态也是不能袖手旁观的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111357V我们会在允许的范围内\n',
            '尽自己所能去完成您的委托的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111358V#461F实在是太感谢你们了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111359V那么，你们拿上这个吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0009, -130, 0, 10610, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '尤莉亚的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x036C, 1)
    ChrMoveTo(0x0009, -40, 0, 11940, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010111360V#505F这是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111361V#460F#5P这是给城里的女官长\n',
            '希尔丹夫人的介绍信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111362V#465F陛下现在大概还在\n',
            '那些特务兵的严密监视之下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111363V贴身服侍的希尔丹夫人\n',
            '应该能想出办法让你们见到陛下的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111364V#501F哎～还有这样的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111365V#010F我知道了。\n',
            '进城后我们就去找她商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111366V#460F#5P拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111367V#465F呼呼……真是羞愧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111040V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111369V#464F#5P被那些人设下的无耻奸计陷害，\n',
            '无法守护身边重要的人，这种屈辱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111370V明明向上天发过誓就算拼上性命也要\n',
            '讨伐奸贼、救出陛下……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111371V可这次不得不借用你们的力量，\n',
            '这个没用的我还真是可悲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111372V#505F不、不要这样责备自己啊……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111373V#007F而且，明天的比赛\n',
            '我们也有输掉的可能性呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111374V#461F#5P呵呵……\n',
            '你们一定没有问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111375V那个来自东方的武术家\n',
            '也拥有相当厉害的身手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111376V而且不管怎么说，\n',
            '你们毕竟是卡西乌斯上校的孩子啊。',
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
            '#0010111377V#004F哎～？\n',
            '尤莉亚小姐也认识老爸吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111378V#465F#5P卡西乌斯上校作为王国军的智囊，\n',
            '同时又是被称为『剑圣』的最强剑士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111379V#460F从王国军退役之前，\n',
            '受邀担当了士官学校的武术教官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111380V所以，他可以说是我的剑术老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111381V#505F真、真是难以置信……\n',
            '老爸明明只使用棒术的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111382V#465F#5P我听说，他退伍成为游击士的时候，\n',
            '就放弃了用剑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111383V这样做不是单单为了杀敌，\n',
            '更是为了坚守自己的信念去惩强扶弱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111384V#460F正因为抱着这样一种精神，\n',
            '所以他选择了棒术作为守护别人的武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101014V#007F原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111386V棒术原来有这样的含义啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111387V#010F而且，\n',
            '这种精神已经被你完全地继承下来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111388V我觉得这是你应该引以为荣的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111389V#008F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111390V#460F#5P你们是上校培养和锻炼出来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111391V我相信你们一定会取得胜利的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1449')
    def lambda_1449():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1449)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111392V#506F嘿嘿……\n',
            '尤莉亚小姐也这么说了，\n',
            '我也感觉更有自信了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111393V#010F我们会全力以赴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000A, 0, 0, 1870, 0)
    PlaySE(114, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_152F')
    def lambda_152F():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_152F)

    @scena.Lambda('lambda_153D')
    def lambda_153D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_153D)

    @scena.Lambda('lambda_154B')
    def lambda_154B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_154B)

    CameraMove(0, 0, 9920, 1000)

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#4190111394V#5P……对不起，我们是王都警卫队！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#4190111395V#5P作为恐怖活动的应付对策之一，\n',
            '我们正在进行主要设施的巡视工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#4190111396V#5P很抱歉，这么晚了还来打扰，\n',
            '不过能不能让我们进去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111397V#005F（糟了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100111398V#461F啊……真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111399V请稍等一下，\n',
            '我这就去开门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)

    @scena.Lambda('lambda_16B8')
    def lambda_16B8():
        CameraMove(-10, 0, 12730, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_16B8)

    @scena.Lambda('lambda_16D0')
    def lambda_16D0():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16D0)

    ChrTurnDirection(0x0101, 0x0009, 400)
    SetChrDirection(0x0009, 90, 600)
    SetChrDirection(0x0009, 0, 600)
    PlaySE(203, 0x00, 0x64)
    SetChrChipByIndex(0x0009, 0)
    SetChrDirection(0x0009, 270, 600)
    SetChrDirection(0x0009, 180, 600)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0100111400V#5P（祭坛房间那边有通往外面的后门。）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100111401V（你们从那里离开吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111402V#006F（知、知道了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111403V#012F（尤莉亚中尉，您也要小心啊。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_17D3',
    )

    Jump('loc_180E')

    def _loc_17D3(): pass

    label('loc_17D3')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_17EE',
    )

    OP_2B(0x0045, 0x0001)

    Jump('loc_180E')

    def _loc_17EE(): pass

    label('loc_17EE')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1809',
    )

    OP_2B(0x0045, 0x0003)

    Jump('loc_180E')

    def _loc_1809(): pass

    label('loc_1809')

    OP_2B(0x0045, 0x0005)

    def _loc_180E(): pass

    label('loc_180E')

    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4151._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
