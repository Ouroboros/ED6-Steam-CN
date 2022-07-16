import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4101_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4101_2 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4101.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x919A
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
    Call(2, 0x0001)

    Return()

# id: 0x0001 offset: 0xAD
@scena.Code('Init')
def Init():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 2, 0x61A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8D3',
    )

    SetScenaFlags(ScenaFlag(0x00C3, 2, 0x61A))
    OP_28(0x0047, 0x01, 0x0004)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(108440, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    CameraSetDistance(2910, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0108, 107670, 1250, 24030, 135)
    SetChrPos(0x0101, 107510, 1250, 23130, 90)
    SetChrPos(0x0102, 107680, 1250, 22250, 45)
    SetChrPos(0x0104, 106450, 1250, 22690, 90)
    ChrTurnDirection(0x000A, 0x0108, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080110024V#070F哟，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110025V啊，是金选手。\n',
            '早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110026V今天的比赛从中午才开始，\n',
            '现在来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110027V#071F我已经找齐同伴了，\n',
            '想来这里帮他们登记一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110028V可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110029V啊呀，真是恭喜了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110030V刚开始听到您一个人参赛的时候，\n',
            '就觉得很不得了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#2180110031V啊，你们是昨天的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110032V#008F嘿嘿，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110033V#010F这次我们是作为金先生的帮手，\n',
            '来参加武术大会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110034V是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110035V那么请你们在这张纸上\n',
            '填写必要的事项。',
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
            '艾丝蒂尔、约修亚和奥利维尔\n',
            '在选手登记的单子上填写了必要事项。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '#2180110036V啊，这边的两位\n',
            '原来是游击士协会的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110037V那么……\n',
            '那一位的身份是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110038V『漂泊的诗人，\n',
            '　身兼首屈一指的天才演奏家。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110039V『身为爱与和平的使者，\n',
            '　现在正热烈募集恋人中』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110040V…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110041V#031F哈·哈·哈。\n',
            '哎呀，真是难为情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110042V#030F怎么样？\n',
            '比赛结束之后和我去喝一杯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110043V#509F啊～～好了好了。\n',
            '小姐你不要管这个白痴就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110044V#010F登记的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110045V好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110046V好了，\n',
            '这样正式赛的选手登记就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110047V小组成员以金选手为代表，\n',
            '加上艾丝蒂尔选手、约修亚选手\n',
            '和奥利维尔选手共计四名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110048V请注意，以后如果有人缺席，\n',
            '就再也不能再换人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110049V#070F哦哦，知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110050V#006F逐渐有感觉了呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110051V对了，\n',
            '今天比赛的对手已经确定了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110052V对阵表已经确定了，\n',
            '但为了防止赌博行为，\n',
            '比赛之前是不会公布的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110053V不过，根据自己被安排到的休息室，\n',
            '就可以把对手的范围缩小了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110054V#010F原来如此……\n',
            '也就是说，是和另一边的休息室里\n',
            '其中一个小组进行对战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110055V嘻嘻，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110056V那么，各位参赛选手，\n',
            '请把这个拿好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0372, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '选手登记卡',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '#2180110057V把这张卡片让那边的接待员看一下，\n',
            '就可以进入场内了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180110058V好了，\n',
            '祝你们胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_15AA')

    def _loc_8D3(): pass

    label('loc_8D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 4, 0x60C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F61',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 2, 0x672)),
            Expr.Return,
        ),
        'loc_9BC',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 107600, 1250, 23440, 90)
    SetChrPos(0x0102, 107500, 1250, 22630, 90)
    ChrTurnDirection(0x000A, 0x0101, 0)
    OP_6C(90000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#2180100855V欢迎来到王立竞技场。\n',
            '是来买票的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100857V两个人的票合计是\n',
            '１０００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D51')

    def _loc_9BC(): pass

    label('loc_9BC')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(109490, 1250, 23040, 0)
    OP_67(0, 7080, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 107600, 1250, 23440, 90)
    SetChrPos(0x0102, 107500, 1250, 22630, 90)
    ChrTurnDirection(0x000A, 0x0101, 0)
    OP_6C(90000, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x00CE, 2, 0x672))

    ChrTalk(
        0x000A,
        (
            '#2180100855V欢迎来到王立竞技场。\n',
            '是来买票的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AA2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010100859V#006F啊，是的。\n',
            '请给我们两张票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACB')

    def _loc_AA2(): pass

    label('loc_AA2')

    ChrTalk(
        0x0102,
        (
            '#0020100856V#010F是的。\n',
            '请给我们两张票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ACB(): pass

    label('loc_ACB')

    ChrTalk(
        0x000A,
        (
            '#2180100860V要看正式赛的话，\n',
            '是从明天开始连续三天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100861V要买哪一天的票呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100862V#505F正式赛……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100863V#014F那个……\n',
            '不是从明天开始的，\n',
            '我们想看今天的预选赛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100864V啊，真是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100865V比赛已经进行过一半了，\n',
            '我以为不会有人再来买票……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100866V这样你们还要买吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100867V#006F啊，没关系没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100868V那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100869V两个人的票合计是\n',
            '１０００米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100870V#004F哇，还真是贵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100871V#014F我听说诞辰庆典的武术大会\n',
            '应该是有打折的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100872V真是抱歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100873V今年好像实行了\n',
            '许多特殊的措施……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100874V#501F嗯……\n',
            '这样的话也没办法啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100875V嗯，１０００米拉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D51(): pass

    label('loc_D51')

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
            TXT(0x00, '【付给１０００米拉】\n'),
            TXT(0x01, '【不付钱】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_DC2'),
        (0x00000001, 'loc_F2F'),
        (-1, 'loc_F5E'),
    )

    def _loc_DC2(): pass

    label('loc_DC2')

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x3E8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_ED1',
    )

    PlaySE(20, 0x00, 0x64)

    ExecExpressionWithVar(
        0x12,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#2180100876V谢谢光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100877V那么，\n',
            '请拿好门票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到两张',
            (TxtCtl.SetColor, 0x2),
            '观战门票',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x036B, 2)
    SetScenaFlags(ScenaFlag(0x00C1, 4, 0x60C))
    SetScenaFlags(ScenaFlag(0x00C1, 4, 0x60C))
    OP_28(0x0045, 0x01, 0x0800)

    ChrTalk(
        0x000A,
        (
            '#2180100878V竞技场的入口\n',
            '就在左边的正门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2180100879V把票让门口的工作人员看一下\n',
            '就可以进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F2A')

    def _loc_ED1(): pass

    label('loc_ED1')

    ChrTalk(
        0x0101,
        (
            '#0010100880V#004F（糟了……\n',
            '　米拉好像不够了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100881V#017F（只好一会儿再来了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F2A(): pass

    label('loc_F2A')

    EventEnd(0x00)

    Jump('loc_F5E')

    def _loc_F2F(): pass

    label('loc_F2F')

    ChrTalk(
        0x000A,
        (
            '#2180100882V我知道了。\n',
            '期待你们再次光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_F5E')

    def _loc_F5E(): pass

    label('loc_F5E')

    Jump('loc_15AA')

    def _loc_F61(): pass

    label('loc_F61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_102F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_FB9',
    )

    ChrTalk(
        0x000A,
        (
            '街上的人们\n',
            '个个脸上喜气洋洋的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '女王陛下的影响力果然很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_102C')

    def _loc_FB9(): pass

    label('loc_FB9')

    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))

    ChrTalk(
        0x000A,
        (
            '诞辰庆典能顺利举行，\n',
            '真的是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '街上的人们\n',
            '个个脸上喜气洋洋的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '女王陛下的影响力果然很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_102C(): pass

    label('loc_102C')

    Jump('loc_15AA')

    def _loc_102F(): pass

    label('loc_102F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_108B',
    )

    ChrTurnDirection(0x000A, 0x0108, 400)

    ChrTalk(
        0x000A,
        (
            '哎呀，这不是优胜组的选手们吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '表情这么严肃，\n',
            '是发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_108B(): pass

    label('loc_108B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_10CE',
    )

    ChrTalk(
        0x000A,
        (
            '虽然武术大会平安地结束了，\n',
            '可是诞辰庆典会怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_10CE(): pass

    label('loc_10CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_11A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_1124',
    )

    ChrTalk(
        0x000A,
        (
            '各位，恭喜你们获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天各位就请  \n',
            '好好享受王城的晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119E')

    def _loc_1124(): pass

    label('loc_1124')

    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))

    ChrTalk(
        0x000A,
        (
            '各位，恭喜你们获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我虽然不能去看，\n',
            '但应该是一场\n',
            '很精彩的比赛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天各位就请\n',
            '好好享受王城的晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_119E(): pass

    label('loc_119E')

    Jump('loc_15AA')

    def _loc_11A1(): pass

    label('loc_11A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_11F4',
    )

    ChrTalk(
        0x000A,
        (
            '各位，总决赛就要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '准备好了的话，\n',
            '请告诉入口处的接待员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_11F4(): pass

    label('loc_11F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_12D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_1257',
    )

    ChrTalk(
        0x000A,
        (
            '呵呵，\n',
            '随着你们不断取胜，\n',
            '你们的崇拜者也在不断增加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明天也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12CF')

    def _loc_1257(): pass

    label('loc_1257')

    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))

    ChrTalk(
        0x000A,
        (
            '各位，\n',
            '明天终于要迎来决赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵，\n',
            '随着你们不断取胜，\n',
            '你们的崇拜者也在不断增加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明天也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12CF(): pass

    label('loc_12CF')

    Jump('loc_15AA')

    def _loc_12D2(): pass

    label('loc_12D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1332',
    )

    ChrTurnDirection(0x000A, 0x0108, 400)

    ChrTalk(
        0x000A,
        (
            '金先生，终于到第二回合比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '准备好了的话，\n',
            '请告诉入口处的接待员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_1332(): pass

    label('loc_1332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1397',
    )

    ChrTalk(
        0x000A,
        (
            '第一回合比赛胜利，\n',
            '恭喜你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明天的比赛\n',
            '是从下午开始，\n',
            '请在那之前来这里报到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_1397(): pass

    label('loc_1397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1402',
    )

    ChrTalk(
        0x000A,
        (
            '把选手登记卡\n',
            '给那边入口的接待员看一下，\n',
            '就可以进入场内了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '各位请这边走。\n',
            '祝你们胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_1402(): pass

    label('loc_1402')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1466',
    )

    ChrTalk(
        0x000A,
        (
            '武术大会的正式赛\n',
            '将于明日下午开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不用对号入座，\n',
            '入场后请选择自己喜欢的座位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_1466(): pass

    label('loc_1466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_15AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 4, 0x60C)),
            Expr.Return,
        ),
        'loc_14C9',
    )

    ChrTalk(
        0x000A,
        (
            '竞技场的入口\n',
            '在正面的右手边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '把票让门口的工作人员看一下\n',
            '就可以进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_14C9(): pass

    label('loc_14C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Return,
        ),
        'loc_1503',
    )

    ChrTalk(
        0x000A,
        (
            '买过票之后\n',
            '就可以直接从\n',
            '正面的入口入场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_1503(): pass

    label('loc_1503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_154D',
    )

    ChrTalk(
        0x000A,
        (
            '离入场开始\n',
            '还有一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '请各位观众\n',
            '耐心等待一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15AA')

    def _loc_154D(): pass

    label('loc_154D')

    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))

    ChrTalk(
        0x000A,
        (
            '欢迎来到王立竞技场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '离入场开始\n',
            '还有一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '请各位观众\n',
            '耐心等待一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15AA(): pass

    label('loc_15AA')

    TalkEnd(0x000A)

    Return()

# id: 0x0002 offset: 0x15AE
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x000B)
    SetChrDirection(0x000B, 270, 0)
    SetChrSubChip(0x000B, 0)
    EventBegin(0x00)
    Fade(1500)

    @scena.Lambda('lambda_15CA')
    def lambda_15CA():
        CameraMove(108230, 1250, 32820, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15CA)

    @scena.Lambda('lambda_15E2')
    def lambda_15E2():
        OP_6C(135000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_15E2)

    SetChrPos(0x0101, 107830, 1250, 33580, 90)
    SetChrPos(0x0102, 107750, 1250, 32470, 90)
    SetChrDirection(0x000B, 270, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1634',
    )

    SetChrPos(0x0108, 106450, 1250, 32450, 90)

    def _loc_1634(): pass

    label('loc_1634')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1653',
    )

    SetChrPos(0x0104, 106450, 1250, 33600, 90)

    def _loc_1653(): pass

    label('loc_1653')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_182F',
    )

    ChrTalk(
        0x000B,
        (
            '#2190111490V各位，\n',
            '欢迎来到王立竞技场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110060V一旦进去的话，\n',
            '在比赛结束之前\n',
            '就不能再出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110061V已经做好准备了吗？',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【做好准备了】\n'),
            TXT(0x01, '【等一会儿再来】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1755'),
        (0x00000001, 'loc_17E8'),
        (-1, 'loc_182C'),
    )

    def _loc_1755(): pass

    label('loc_1755')

    SetScenaFlags(ScenaFlag(0x00C6, 1, 0x631))
    OP_28(0x0049, 0x01, 0x0004)

    ChrTalk(
        0x000B,
        (
            '#2190110062V知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110063V你们的休息室是进入大厅之后，\n',
            '在右边的『苍之组』休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110064V那么祝你们胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x007E, 5, 0x3F5))
    NewScene('ED6_DT01/T4136._SN', 111, 0, 0)
    IdleLoop()

    Jump('loc_182C')

    def _loc_17E8(): pass

    label('loc_17E8')

    ChrTalk(
        0x000B,
        (
            '#2190110062V我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110066V还有一些时间，\n',
            '请准备好再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_182C')

    def _loc_182C(): pass

    label('loc_182C')

    Jump('loc_1EF2')

    def _loc_182F(): pass

    label('loc_182F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A0B',
    )

    ChrTalk(
        0x000B,
        (
            '#2190110627V这不是金大人吗。\n',
            '欢迎您来到竞技场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110060V一旦进去的话，\n',
            '在比赛结束之前\n',
            '就不能再出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110061V已经做好准备了吗？',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【做好准备了】\n'),
            TXT(0x01, '【等一会儿再来】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1938'),
        (0x00000001, 'loc_19C4'),
        (-1, 'loc_1A08'),
    )

    def _loc_1938(): pass

    label('loc_1938')

    SetScenaFlags(ScenaFlag(0x00C4, 3, 0x623))
    OP_28(0x0048, 0x01, 0x0004)

    ChrTalk(
        0x000B,
        (
            '#2190110062V知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110063V你们的休息室是进入大厅之后，\n',
            '在右边的『苍之组』休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110064V那么请加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1A08')

    def _loc_19C4(): pass

    label('loc_19C4')

    ChrTalk(
        0x000B,
        (
            '#2190110062V我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110066V还有一些时间，\n',
            '请准备好再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A08')

    def _loc_1A08(): pass

    label('loc_1A08')

    Jump('loc_1EF2')

    def _loc_1A0B(): pass

    label('loc_1A0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 2, 0x61A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BFB',
    )

    ChrTalk(
        0x000B,
        (
            '#2190110059V那张卡片……\n',
            '你们是参加正式赛的选手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110060V有一点请各位注意。\n',
            '就是只要进入竞技场，\n',
            '比赛结束之前是不能再出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110061V已经做好准备了吗？',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【做好准备了】\n'),
            TXT(0x01, '【等一会儿再来】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B2C'),
        (0x00000001, 'loc_1BB4'),
        (-1, 'loc_1BF8'),
    )

    def _loc_1B2C(): pass

    label('loc_1B2C')

    SetScenaFlags(ScenaFlag(0x00C3, 3, 0x61B))
    OP_28(0x0047, 0x01, 0x0008)

    ChrTalk(
        0x000B,
        (
            '#2190110062V知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110063V你们的休息室是进入大厅之后，\n',
            '在右边的『苍之组』休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110064V请加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1BF8')

    def _loc_1BB4(): pass

    label('loc_1BB4')

    ChrTalk(
        0x000B,
        (
            '#2190110062V我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190110066V还有一些时间，\n',
            '请准备好再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BF8')

    def _loc_1BF8(): pass

    label('loc_1BF8')

    Jump('loc_1EF2')

    def _loc_1BFB(): pass

    label('loc_1BFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 2, 0x61A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CA6',
    )

    ChrTalk(
        0x000B,
        (
            '#2190100891V现在，王立竞技场内\n',
            '将要举行武术大会的正式赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190100892V要作为参赛者出场的话，\n',
            '先要进行选手登记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190100893V选手登记\n',
            '请在右边的售票处进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF2')

    def _loc_1CA6(): pass

    label('loc_1CA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 4, 0x60C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E56',
    )

    ChrTalk(
        0x000B,
        (
            '#2190100883V现在，王立竞技场内\n',
            '正在举行武术大会的预选赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190100884V想要入场的话，\n',
            '请先出示门票。',
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【交出门票】\n'),
            TXT(0x01, '【不交出门票】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D83'),
        (0x00000001, 'loc_1E0F'),
        (-1, 'loc_1E53'),
    )

    def _loc_1D83(): pass

    label('loc_1D83')

    SetScenaFlags(ScenaFlag(0x00C1, 5, 0x60D))
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出两张',
            (TxtCtl.SetColor, 0x2),
            '观战门票',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x036B, 2)

    ChrTalk(
        0x000B,
        (
            '#2190100885V好，可以了。\n',
            '两位请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4136._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E53')

    def _loc_1E0F(): pass

    label('loc_1E0F')

    ChrTalk(
        0x000B,
        (
            '#2190100886V可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190100887V今天买的门票\n',
            '只能在今天使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E53')

    def _loc_1E53(): pass

    label('loc_1E53')

    Jump('loc_1EF2')

    def _loc_1E56(): pass

    label('loc_1E56')

    ChrTalk(
        0x000B,
        (
            '#2190100883V现在，王立竞技场内\n',
            '正在举行武术大会的预选赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190100884V想要入场的话，\n',
            '请先出示门票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2190100890V还没有买票的观众，\n',
            '请到右手边的售票处购票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EF2(): pass

    label('loc_1EF2')

    EventEnd(0x00)
    TalkEnd(0x000B)

    Return()

# id: 0x0003 offset: 0x1EF8
@scena.Code('func_03_1EF8')
def func_03_1EF8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1F05',
    )

    Jump('loc_20AA')

    def _loc_1F05(): pass

    label('loc_1F05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1F0F',
    )

    Jump('loc_20AA')

    def _loc_1F0F(): pass

    label('loc_1F0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1F19',
    )

    Jump('loc_20AA')

    def _loc_1F19(): pass

    label('loc_1F19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1F23',
    )

    Jump('loc_20AA')

    def _loc_1F23(): pass

    label('loc_1F23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1F2D',
    )

    Jump('loc_20AA')

    def _loc_1F2D(): pass

    label('loc_1F2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1F37',
    )

    Jump('loc_20AA')

    def _loc_1F37(): pass

    label('loc_1F37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F41',
    )

    Jump('loc_20AA')

    def _loc_1F41(): pass

    label('loc_1F41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_208F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1FD0',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120141538V#819F今天早上工作的时候，\n',
            '被军队纠缠了好一会儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141537V因为恐怖分子曾经\n',
            '乔装过游击士的缘故，\n',
            '不得不小心行事了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_208C')

    def _loc_1FD0(): pass

    label('loc_1FD0')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0120141535V#810F今天早晨，\n',
            '我到艾尔贝离宫附近执行任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141536V#819F军队那些人知道我是游击士后，\n',
            '纠缠了我好一会儿呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141537V因为恐怖分子曾经\n',
            '乔装过游击士的缘故，\n',
            '不得不小心行事了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_208C(): pass

    label('loc_208C')

    Jump('loc_20AA')

    def _loc_208F(): pass

    label('loc_208F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2099',
    )

    Jump('loc_20AA')

    def _loc_2099(): pass

    label('loc_2099')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_20A3',
    )

    Jump('loc_20AA')

    def _loc_20A3(): pass

    label('loc_20A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_20AA',
    )

    def _loc_20AA(): pass

    label('loc_20AA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x20AE
@scena.Code('func_04_20AE')
def func_04_20AE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_20BB',
    )

    Jump('loc_2171')

    def _loc_20BB(): pass

    label('loc_20BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_20C5',
    )

    Jump('loc_2171')

    def _loc_20C5(): pass

    label('loc_20C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_20CF',
    )

    Jump('loc_2171')

    def _loc_20CF(): pass

    label('loc_20CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_20D9',
    )

    Jump('loc_2171')

    def _loc_20D9(): pass

    label('loc_20D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_20E3',
    )

    Jump('loc_2171')

    def _loc_20E3(): pass

    label('loc_20E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2142',
    )

    ChrTalk(
        0x00FE,
        (
            '为了给妻子\n',
            '拿个观战的好位置，\n',
            '我决定现在就排队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '这就是爱的代价吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2171')

    def _loc_2142(): pass

    label('loc_2142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_214C',
    )

    Jump('loc_2171')

    def _loc_214C(): pass

    label('loc_214C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2156',
    )

    Jump('loc_2171')

    def _loc_2156(): pass

    label('loc_2156')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2160',
    )

    Jump('loc_2171')

    def _loc_2160(): pass

    label('loc_2160')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_216A',
    )

    Jump('loc_2171')

    def _loc_216A(): pass

    label('loc_216A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2171',
    )

    def _loc_2171(): pass

    label('loc_2171')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x2175
@scena.Code('func_05_2175')
def func_05_2175():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_22C0',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_21D8',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22BD')

    def _loc_21D8(): pass

    label('loc_21D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2243',
    )

    ChrTalk(
        0x00FE,
        (
            '一到诞辰庆典，\n',
            '人就多得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '据说帝国的帝都就算平常\n',
            '也比王都现在的人还要多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22BD')

    def _loc_2243(): pass

    label('loc_2243')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '一到诞辰庆典，\n',
            '人就多得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '据说帝国的帝都就算平常\n',
            '也比王都现在的人还要多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我简直无法想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22BD(): pass

    label('loc_22BD')

    Jump('loc_2E20')

    def _loc_22C0(): pass

    label('loc_22C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2395',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_2321',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2392')

    def _loc_2321(): pass

    label('loc_2321')

    ChrTalk(
        0x00FE,
        (
            '其他的王国军士兵\n',
            '好像都撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我因为还没有\n',
            '接到新的命令，\n',
            '所以继续在这里守卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是我的使命啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2392(): pass

    label('loc_2392')

    Jump('loc_2E20')

    def _loc_2395(): pass

    label('loc_2395')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_244B',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_23F6',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2448')

    def _loc_23F6(): pass

    label('loc_23F6')

    ChrTalk(
        0x00FE,
        (
            '我负责不让奥利维尔先生\n',
            '从大使馆逃出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以现在\n',
            '也不能让你们进去见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2448(): pass

    label('loc_2448')

    Jump('loc_2E20')

    def _loc_244B(): pass

    label('loc_244B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_25C7',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_24AC',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C4')

    def _loc_24AC(): pass

    label('loc_24AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_251E',
    )

    ChrTalk(
        0x00FE,
        (
            '穆拉大人是最近\n',
            '才到王都来的帝国驻外武官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很年轻，但在帝国军中\n',
            '好像是个很了不起的人物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C4')

    def _loc_251E(): pass

    label('loc_251E')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '穆拉大人是最近\n',
            '才到王都来的帝国驻外武官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很年轻，但在帝国军中\n',
            '好像是个很了不起的人物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个奥利维尔先生现在好像\n',
            '也老老实实地呆在大使馆里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25C4(): pass

    label('loc_25C4')

    Jump('loc_2E20')

    def _loc_25C7(): pass

    label('loc_25C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2750',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_2628',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274D')

    def _loc_2628(): pass

    label('loc_2628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_26B2',
    )

    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生，\n',
            '如果您又跑出去的话，\n',
            '那个人也不会袖手旁观的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且他和我说过，\n',
            '要是您太过放纵的话就要向他汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274D')

    def _loc_26B2(): pass

    label('loc_26B2')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生，\n',
            '您今天又要外出吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您又跑出去的话，\n',
            '那个人也不会袖手旁观的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且他和我说过，\n',
            '要是您太过放纵的话就要向他汇报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_274D(): pass

    label('loc_274D')

    Jump('loc_2E20')

    def _loc_2750(): pass

    label('loc_2750')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2811',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_27B1',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_280E')

    def _loc_27B1(): pass

    label('loc_27B1')

    ChrTalk(
        0x00FE,
        (
            '帝国大使馆的人\n',
            '如果能将奥利维尔先生\n',
            '关在里面就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么还让他\n',
            '每天都外出呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_280E(): pass

    label('loc_280E')

    Jump('loc_2E20')

    def _loc_2811(): pass

    label('loc_2811')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_29A0',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_2872',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_299D')

    def _loc_2872(): pass

    label('loc_2872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_28FF',
    )

    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生，\n',
            '请不要再做出让市民\n',
            '怨声载道的行为了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他的帝国人\n',
            '都很讲究纪律和礼仪，\n',
            '您也稍微向他们学习一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_299D')

    def _loc_28FF(): pass

    label('loc_28FF')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生，\n',
            '您今天又要外出吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请不要再做出让市民\n',
            '怨声载道的行为了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他的帝国人\n',
            '都很讲究纪律和礼仪，\n',
            '您也稍微向他们学习一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_299D(): pass

    label('loc_299D')

    Jump('loc_2E20')

    def _loc_29A0(): pass

    label('loc_29A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2A66',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_2A01',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A63')

    def _loc_2A01(): pass

    label('loc_2A01')

    ChrTalk(
        0x00FE,
        (
            '能在武术大会出场是\n',
            '王国军军人的至高荣誉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能够有机会的话，\n',
            '我也好想参加武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A63(): pass

    label('loc_2A63')

    Jump('loc_2E20')

    def _loc_2A66(): pass

    label('loc_2A66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2C82',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_2AC7',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_2AC7(): pass

    label('loc_2AC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2B3B',
    )

    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生……\n',
            '请您不要在街道上\n',
            '过于放纵好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您陷入了什么\n',
            '麻烦的事件中就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_2B3B(): pass

    label('loc_2B3B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x00FE, 0x0104, 400)

    ChrTalk(
        0x00FE,
        (
            '奥利维尔先生，\n',
            '您现在要回大使馆吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#035F呵呵，你在开玩笑吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '美丽眩目的街道映入眼帘，\n',
            '来来往往的人们兴味盎然，\n',
            '以及无数味美绝伦的料理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#030F这充满美妙的王都正在呼唤着我，\n',
            '如果我回去不就太失礼了吗。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这样的话，\n',
            '请您不要在街道上\n',
            '过于放纵好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您陷入了什么\n',
            '麻烦的事件中就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C7F(): pass

    label('loc_2C7F')

    Jump('loc_2E20')

    def _loc_2C82(): pass

    label('loc_2C82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2DCB',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_2CE3',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC8')

    def _loc_2CE3(): pass

    label('loc_2CE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2D37',
    )

    ChrTalk(
        0x00FE,
        (
            '帝国大使馆的人\n',
            '个个都很率直，\n',
            '而且朴实刚健。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那个人就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC8')

    def _loc_2D37(): pass

    label('loc_2D37')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '帝国大使馆的人\n',
            '个个都很率直，\n',
            '而且朴实刚健。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那个人就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每次他在大街上引起骚乱，\n',
            '市民们就都跑到我这里，\n',
            '不停地抱怨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC8(): pass

    label('loc_2DC8')

    Jump('loc_2E20')

    def _loc_2DCB(): pass

    label('loc_2DCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2E20',
    )

    ChrTalk(
        0x00FE,
        (
            '这里就是\n',
            '埃雷波尼亚帝国大使馆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有事的话，\n',
            '是不允许进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E20(): pass

    label('loc_2E20')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x2E24
@scena.Code('func_06_2E24')
def func_06_2E24():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 1, 0x611)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_348A',
    )

    EventBegin(0x00)
    OP_69(0x0023, 1000)
    SetScenaFlags(ScenaFlag(0x00C2, 2, 0x612))
    OP_28(0x0046, 0x01, 0x0008)
    OP_28(0x0046, 0x01, 0x0010)

    ChrTalk(
        0x0023,
        (
            '#2220101224V你们好。\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101225V有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101226V#000F士兵大哥，你好。\n',
            '我们有事来找住在这里的金先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101227V#010F能麻烦您帮忙通知一下吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101228V哎～\n',
            '你们是来找金先生的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101229V我第一次见到那个人的时候，\n',
            '差点吓得尿裤子了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101230V当时就想着\n',
            '『王都里面竟然有熊吗！？』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101231V#001F啊哈哈，金先生体型太大了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101232V不过和他谈过话之后，\n',
            '发现他为人很和气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101233V换班之前肚子正饿的时候，\n',
            '他还给我拿来了肉包子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101234V#502F嗯嗯。\n',
            '就像很靠得住的大哥一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101235V#015F咳咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101236V#010F那么，能帮我们通知金先生吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101237V啊，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101238V金先生刚才回来了，\n',
            '不过立刻又出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101239V好像是为了备战武术大会的正式赛，\n',
            '寻找可以修行的地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101240V#004F修、修行的地方？\n',
            '金先生还真是专业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101241V#010F他有没有提到具体会去什么地方呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101242V好像是去郊外的\n',
            '『艾尔贝周游道』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101243V那里就像森林中的公园一样，\n',
            '应该可以安静地修行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101244V#010F『艾尔贝周游道』啊……\n',
            '明白了，那么我们也去看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101245V#006F当然了！\n',
            '要早点和他商量一下啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101246V啊，如果你们要去周游道的话，\n',
            '有件事情请一定要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101247V那附近有一处名为\n',
            '『艾尔贝离宫』的王家宫殿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101248V#002F啊，那个之前听说过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101249V#012F因为作为恐怖事件的搜查本部，\n',
            '所以军队不让任何人进入对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101250V什么，已经知道了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101251V……在那里守备的家伙很麻烦，\n',
            '请你们一定要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#2220101252V最好是不要靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101253V#505F呼～很麻烦的家伙们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101254V#501F不想被他们看见，\n',
            '还是尽量不要靠近那里对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101255V#010F谢谢您的提醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_3FF1')

    def _loc_348A(): pass

    label('loc_348A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3570',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_3504',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_356D')

    def _loc_3504(): pass

    label('loc_3504')

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '每年的这个日子都非常热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游客这么多，\n',
            '不知道其中有没有什么坏人，\n',
            '得更严格地看守才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_356D(): pass

    label('loc_356D')

    Jump('loc_3FF1')

    def _loc_3570(): pass

    label('loc_3570')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_365B',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_35EA',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3658')

    def _loc_35EA(): pass

    label('loc_35EA')

    ChrTalk(
        0x00FE,
        (
            '王国军的同伴们都撤走了，\n',
            '代之而来的是特务兵那群家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我因为还没有接到命令，\n',
            '所以留在这里了，呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3658(): pass

    label('loc_3658')

    Jump('loc_3FF1')

    def _loc_365B(): pass

    label('loc_365B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_372F',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_36D5',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372C')

    def _loc_36D5(): pass

    label('loc_36D5')

    ChrTalk(
        0x00FE,
        (
            '女王的诞辰庆典该怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '共和国的大使还没能定下行程，\n',
            '正为此事感到困扰呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_372C(): pass

    label('loc_372C')

    Jump('loc_3FF1')

    def _loc_372F(): pass

    label('loc_372F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3926',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_37A9',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3923')

    def _loc_37A9(): pass

    label('loc_37A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_380C',
    )

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '金先生，恭喜你们获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直支持的\n',
            '金先生获胜了，\n',
            '让我也感到很骄傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3923')

    def _loc_380C(): pass

    label('loc_380C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '金先生，恭喜你们获胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直支持的\n',
            '金先生获胜了，\n',
            '让我也感到很骄傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大使馆的各位，\n',
            '也非常开心呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，谢谢。\n',
            '我本想回大使馆报告一声呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过今天我不能回大使馆了，\n',
            '要住在王城里，\n',
            '麻烦你帮我传达一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请您万事小心呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3923(): pass

    label('loc_3923')

    Jump('loc_3FF1')

    def _loc_3926(): pass

    label('loc_3926')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_39EE',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_39A0',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39EB')

    def _loc_39A0(): pass

    label('loc_39A0')

    ChrTalk(
        0x00FE,
        (
            '今天是总决赛的日子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位请努力迎战！\n',
            '我相信你们一定能获胜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39EB(): pass

    label('loc_39EB')

    Jump('loc_3FF1')

    def _loc_39EE(): pass

    label('loc_39EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3ACC',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_3A68',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AC9')

    def _loc_3A68(): pass

    label('loc_3A68')

    ChrTalk(
        0x00FE,
        (
            '我如果不用工作的话，\n',
            '也想和金先生\n',
            '一起去参加比赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们一定要\n',
            '连我这一份一起加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AC9(): pass

    label('loc_3AC9')

    Jump('loc_3FF1')

    def _loc_3ACC(): pass

    label('loc_3ACC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3B96',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_3B46',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B93')

    def _loc_3B46(): pass

    label('loc_3B46')

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '金先生，\n',
            '祝您在准决赛胜出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也在为您助威，\n',
            '请一定要加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B93(): pass

    label('loc_3B93')

    Jump('loc_3FF1')

    def _loc_3B96(): pass

    label('loc_3B96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_3C85',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_3C10',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C82')

    def _loc_3C10(): pass

    label('loc_3C10')

    ChrTalk(
        0x00FE,
        (
            '金先生一向一视同仁地待人，\n',
            '所以在大使馆里面也很受欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果说他有什么缺点的话，\n',
            '就是拿妙龄女子没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C82(): pass

    label('loc_3C82')

    Jump('loc_3FF1')

    def _loc_3C85(): pass

    label('loc_3C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_3E31',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_3CFF',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2E')

    def _loc_3CFF(): pass

    label('loc_3CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_3D68',
    )

    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '金先生，\n',
            '今天正式赛就要开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然不能去看比赛，\n',
            '但也要在这里支持你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2E')

    def _loc_3D68(): pass

    label('loc_3D68')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x00FE, 0x0108, 400)

    ChrTalk(
        0x00FE,
        (
            '金先生，\n',
            '今天正式赛就要开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然不能去看比赛，\n',
            '但也要在这里支持你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F啊啊，\n',
            '现在有了这几位协助我的人，\n',
            '目标就是冠军了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我不想让自己后悔，\n',
            '所以会拼命努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E2E(): pass

    label('loc_3E2E')

    Jump('loc_3FF1')

    def _loc_3E31(): pass

    label('loc_3E31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_3F8A',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_3EAB',
    )

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F87')

    def _loc_3EAB(): pass

    label('loc_3EAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 1, 0x611)),
            Expr.Return,
        ),
        'loc_3F20',
    )

    ChrTalk(
        0x00FE,
        (
            '要找金先生的话，\n',
            '他好像是去郊外的\n',
            '『艾尔贝周游道』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们去的时候最好\n',
            '不要靠近『艾尔贝离宫』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F87')

    def _loc_3F20(): pass

    label('loc_3F20')

    ChrTalk(
        0x00FE,
        (
            '#2220101224V你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F87(): pass

    label('loc_3F87')

    Jump('loc_3FF1')

    def _loc_3F8A(): pass

    label('loc_3F8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3FF1',
    )

    ChrTalk(
        0x00FE,
        (
            '你们好，\n',
            '这里是卡尔瓦德共和国大使馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，如果不是来办事的话，\n',
            '这里是禁止进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FF1(): pass

    label('loc_3FF1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x3FF5
@scena.Code('func_07_3FF5')
def func_07_3FF5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_403B',
    )

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅公主\n',
            '真是好漂亮啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让人无比向往啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_403B(): pass

    label('loc_403B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_407C',
    )

    ChrTalk(
        0x00FE,
        (
            '大街上随处可见\n',
            '那些黑衣的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是在训练吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_407C(): pass

    label('loc_407C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_40DC',
    )

    ChrTalk(
        0x00FE,
        (
            '呀嗬～！\n',
            '武术大会结束之后，\n',
            '接下来就是诞辰庆典了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～的，尽情地狂欢吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_40DC(): pass

    label('loc_40DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4136',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我已经拼尽全力加油了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会果然很棒，\n',
            '明年我一定还来现场看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_4136(): pass

    label('loc_4136')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4181',
    )

    ChrTalk(
        0x00FE,
        (
            '呀嗬～！\n',
            '总决赛终于开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟哪个小组会获得冠军呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_4181(): pass

    label('loc_4181')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_41C6',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～啊，\n',
            '决赛的双方都是黑马呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '完全没有预料到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_41C6(): pass

    label('loc_41C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_41FD',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，今天的比赛\n',
            '也是一场都不能错过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_41FD(): pass

    label('loc_41FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_422E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '不管哪场比赛都有精彩的看点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_422E(): pass

    label('loc_422E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4261',
    )

    ChrTalk(
        0x00FE,
        (
            '呀嗬～！\n',
            '今天也要鼓足干劲支持他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_4261(): pass

    label('loc_4261')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_42A3',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '从预选赛的情况来看，\n',
            '今年就支持游击士小组吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42C9')

    def _loc_42A3(): pass

    label('loc_42A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_42C9',
    )

    ChrTalk(
        0x00FE,
        (
            '呀嗬～！\n',
            '今年支持谁好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42C9(): pass

    label('loc_42C9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x42CD
@scena.Code('func_08_42CD')
def func_08_42CD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_42DA',
    )

    Jump('loc_4671')

    def _loc_42DA(): pass

    label('loc_42DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_42E4',
    )

    Jump('loc_4671')

    def _loc_42E4(): pass

    label('loc_42E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_434A',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，\n',
            '昨天喝过头了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连是和谁喝的酒\n',
            '都记不清了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～头疼得好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_434A(): pass

    label('loc_434A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4354',
    )

    Jump('loc_4671')

    def _loc_4354(): pass

    label('loc_4354')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_43AB',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然今天来得比往常要早，\n',
            '不过已经有这么多人了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是总决赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_43AB(): pass

    label('loc_43AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_44E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4425',
    )

    ChrTalk(
        0x00FE,
        (
            '支持空贼组的人\n',
            '好像没有几个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，我觉得他们\n',
            '能在这次大会上堂堂正正地战斗，\n',
            '非常了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E3')

    def _loc_4425(): pass

    label('loc_4425')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '支持空贼组的人\n',
            '好像没有几个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们输的时候\n',
            '大家还一同欢呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，我觉得他们\n',
            '能在这次大会上堂堂正正地战斗，\n',
            '非常了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后希望他们也能\n',
            '这样正大光明地生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44E3(): pass

    label('loc_44E3')

    Jump('loc_4671')

    def _loc_44E6(): pass

    label('loc_44E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_453E',
    )

    ChrTalk(
        0x00FE,
        (
            '今天终于到了\n',
            '准决赛的比赛日子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟哪一组会\n',
            '取得最终的胜利呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_453E(): pass

    label('loc_453E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_459E',
    )

    ChrTalk(
        0x00FE,
        (
            '空、空贼战胜了王国军，\n',
            '总感觉不太妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军的选手们\n',
            '也要加把劲才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_459E(): pass

    label('loc_459E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_45DB',
    )

    ChrTalk(
        0x00FE,
        (
            '快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正式赛真是\n',
            '让人异常激动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_45DB(): pass

    label('loc_45DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4633',
    )

    ChrTalk(
        0x00FE,
        (
            '难道从今年开始\n',
            '就变成团体战了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对个人战的方式\n',
            '更要感兴趣一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4671')

    def _loc_4633(): pass

    label('loc_4633')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4671',
    )

    ChrTalk(
        0x00FE,
        (
            '为何今年与往常不同呢，\n',
            '对战的规则似乎改变了不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4671(): pass

    label('loc_4671')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x4675
@scena.Code('func_09_4675')
def func_09_4675():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4682',
    )

    Jump('loc_4B49')

    def _loc_4682(): pass

    label('loc_4682')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_468C',
    )

    Jump('loc_4B49')

    def _loc_468C(): pass

    label('loc_468C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4696',
    )

    Jump('loc_4B49')

    def _loc_4696(): pass

    label('loc_4696')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_46A0',
    )

    Jump('loc_4B49')

    def _loc_46A0(): pass

    label('loc_46A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_47FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_4756',
    )

    ChrTalk(
        0x00FE,
        (
            '好，我决定了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就给共和国的\n',
            '金选手加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不行不行，还是觉得\n',
            '特务部队从名字上听起来更强……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……也就是说，\n',
            '果然还是要反过来支持游击士小组了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47F8')

    def _loc_4756(): pass

    label('loc_4756')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '那～么……\n',
            '支持哪一组好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我之前支持的小组\n',
            '在今年的比赛里都输掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是不是还是不要支持\n',
            '我希望胜利的小组会好一些呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得很矛盾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47F8(): pass

    label('loc_47F8')

    Jump('loc_4B49')

    def _loc_47FB(): pass

    label('loc_47FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_48E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_4854',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我支持的小组又输了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我难道被什么\n',
            '不祥之物附体了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48DE')

    def _loc_4854(): pass

    label('loc_4854')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我支持的小组又输了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我难道被什么\n',
            '不祥之物附体了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……说起来，\n',
            '街上的士兵一直在增加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48DE(): pass

    label('loc_48DE')

    Jump('loc_4B49')

    def _loc_48E1(): pass

    label('loc_48E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_49A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_4921',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我要为游击士的\n',
            '格兰赛尔支部小组加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49A3')

    def _loc_4921(): pass

    label('loc_4921')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '今天我要为游击士的\n',
            '格兰赛尔支部小组加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天还有前天，\n',
            '我支持的小组都\n',
            '悉数败下阵来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望他们今天能取得胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49A3(): pass

    label('loc_49A3')

    Jump('loc_4B49')

    def _loc_49A6(): pass

    label('loc_49A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_49FC',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～\n',
            '渡鸦帮也输掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么我支持过的小组\n',
            '都一一败下阵来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B49')

    def _loc_49FC(): pass

    label('loc_49FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4AC1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_4A47',
    )

    ChrTalk(
        0x00FE,
        (
            '观战的时候\n',
            '就是要先选好自己支持哪一方\n',
            '才会更有意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ABE')

    def _loc_4A47(): pass

    label('loc_4A47')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这场比赛让我想起了\n',
            '以前我也有一段叛逆的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为觉得很有亲切感，\n',
            '所以我支持那个叫做『渡鸦帮』的小组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4ABE(): pass

    label('loc_4ABE')

    Jump('loc_4B49')

    def _loc_4AC1(): pass

    label('loc_4AC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4B11',
    )

    ChrTalk(
        0x00FE,
        (
            '我支持的\n',
            '国境守备队输了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到摩尔根将军\n',
            '今年没有参加……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B49')

    def _loc_4B11(): pass

    label('loc_4B11')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4B49',
    )

    ChrTalk(
        0x00FE,
        (
            '勿庸置疑，今年肯定也是\n',
            '国境守备队取得优胜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B49(): pass

    label('loc_4B49')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x4B4D
@scena.Code('func_0A_4B4D')
def func_0A_4B4D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4B74',
    )

    ChrTalk(
        0x00FE,
        (
            '真的是王室御用的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E18')

    def _loc_4B74(): pass

    label('loc_4B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4B7E',
    )

    Jump('loc_4E18')

    def _loc_4B7E(): pass

    label('loc_4B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4B88',
    )

    Jump('loc_4E18')

    def _loc_4B88(): pass

    label('loc_4B88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4B92',
    )

    Jump('loc_4E18')

    def _loc_4B92(): pass

    label('loc_4B92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4C06',
    )

    ChrTalk(
        0x00FE,
        (
            '考虑了很久\n',
            '要支持哪一支队伍……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0027, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '最后我还是决定支持\n',
            '约修亚君一个人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E18')

    def _loc_4C06(): pass

    label('loc_4C06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4CC1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_4C60',
    )

    ChrTalk(
        0x00FE,
        (
            '那个黑发男孩子很可爱，\n',
            '而且感觉也很酷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想紧紧地抱抱他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CBE')

    def _loc_4C60(): pass

    label('loc_4C60')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '那个黑发男孩子不错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅很可爱，\n',
            '而且感觉也很酷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想紧紧地抱抱他啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CBE(): pass

    label('loc_4CBE')

    Jump('loc_4E18')

    def _loc_4CC1(): pass

    label('loc_4CC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4CF4',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～这就是那个\n',
            '粗俗公爵的所作所为～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E18')

    def _loc_4CF4(): pass

    label('loc_4CF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4D12',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，说得对～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E18')

    def _loc_4D12(): pass

    label('loc_4D12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4D43',
    )

    ChrTalk(
        0x00FE,
        (
            '那些身着黑色铠甲的人\n',
            '应该很强吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E18')

    def _loc_4D43(): pass

    label('loc_4D43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4DAD',
    )

    ChrTalk(
        0x00FE,
        (
            '那个叫做金的人，\n',
            '对自己的实力好像很有信心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一个人去面对其他对手，\n',
            '的确是个男子汉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E18')

    def _loc_4DAD(): pass

    label('loc_4DAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4E18',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队居然不出场，\n',
            '简直难以置信～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～啊，我原本可是专门来看\n',
            '尤莉亚中尉矫健身姿的呢～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E18(): pass

    label('loc_4E18')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x4E1C
@scena.Code('func_0B_4E1C')
def func_0B_4E1C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4E70',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，不太清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然大家都说好吃，\n',
            '不过味道不是也就一般吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_4E70(): pass

    label('loc_4E70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_4E7A',
    )

    Jump('loc_50BC')

    def _loc_4E7A(): pass

    label('loc_4E7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_4E84',
    )

    Jump('loc_50BC')

    def _loc_4E84(): pass

    label('loc_4E84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4E8E',
    )

    Jump('loc_50BC')

    def _loc_4E8E(): pass

    label('loc_4E8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4EB3',
    )

    ChrTalk(
        0x00FE,
        (
            '什么？\n',
            '只支持一个人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_4EB3(): pass

    label('loc_4EB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4F0B',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来啊，\n',
            '我也是这么想的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '觉得我外表看上去\n',
            '有散发出母性的本能吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_4F0B(): pass

    label('loc_4F0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_4F3A',
    )

    ChrTalk(
        0x00FE,
        (
            '说实话～\n',
            '那些空贼难道不危险吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_4F3A(): pass

    label('loc_4F3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_4FC0',
    )

    ChrTalk(
        0x00FE,
        (
            '那个带红色面具的人，\n',
            '虽然看不见他的脸，\n',
            '但是不觉得他很酷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0028, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '而且看起来也很强的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_4FC0(): pass

    label('loc_4FC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5026',
    )

    ChrTalk(
        0x00FE,
        (
            '哦～\n',
            '你是说王国军的那个特别小组吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每个人都是同一种装束，\n',
            '真是一点个性也没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_5026(): pass

    label('loc_5026')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5086',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，虽说很强，\n',
            '但只不过是个大叔啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的格斗家果然\n',
            '还是要偶像派的才好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50BC')

    def _loc_5086(): pass

    label('loc_5086')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_50BC',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～我到底是为了什么\n',
            '才买了预售的门票啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50BC(): pass

    label('loc_50BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x50C0
@scena.Code('func_0C_50C0')
def func_0C_50C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_50F2',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典啊……\n',
            '大家都很高兴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595E')

    def _loc_50F2(): pass

    label('loc_50F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5138',
    )

    ChrTalk(
        0x00FE,
        (
            '利库斯一直是\n',
            '悠然自得的样子，\n',
            '因为他没有想做的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595E')

    def _loc_5138(): pass

    label('loc_5138')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_518E',
    )

    ChrTalk(
        0x00FE,
        (
            '像利库斯那样的\n',
            '乐天派是不会\n',
            '明白我的心情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁来可怜可怜我啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595E')

    def _loc_518E(): pass

    label('loc_518E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_52EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Return,
        ),
        'loc_52A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_51CF',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，这下又回到\n',
            '毫无干劲的那个我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52A5')

    def _loc_51CF(): pass

    label('loc_51CF')

    ChrTalk(
        0x00FE,
        (
            '……我向经常经过这里的\n',
            '那个漂亮姑娘告白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你猜她说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『我讨厌你这种\n',
            '　总用奇怪的眼神盯着别人看的人。』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来以为她就算拒绝，\n',
            '也会用更温柔委婉的说法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '这下子我的干劲全没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52A5(): pass

    label('loc_52A5')

    Jump('loc_52E9')

    def _loc_52A8(): pass

    label('loc_52A8')

    ChrTalk(
        0x00FE,
        (
            '啊～啊，\n',
            '今天又平平淡淡地度过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的人生在何方呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_52E9(): pass

    label('loc_52E9')

    Jump('loc_595E')

    def _loc_52EC(): pass

    label('loc_52EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5642',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Return,
        ),
        'loc_5324',
    )

    ChrTalk(
        0x00FE,
        (
            '好，就趁这个势头\n',
            '试试向她告白吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_563F')

    def _loc_5324(): pass

    label('loc_5324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_5436',
    )

    SetScenaFlags(ScenaFlag(0x00DD, 3, 0x6EB))

    ChrTalk(
        0x00FE,
        (
            '太好啦——！\n',
            '她从这里经过三次了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我真的想感谢\n',
            '世界上的每一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢，谢谢！\n',
            '我就在这里哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢你们！\n',
            '把这个作为纪念吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x021C, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第11卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '好，就趁这个势头\n',
            '试试向她告白吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_563F')

    def _loc_5436(): pass

    label('loc_5436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_5497',
    )

    ChrTalk(
        0x00FE,
        (
            '还有一次！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再看见她一次，\n',
            '我就会干劲十足了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没错，她就是我的女神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_563F')

    def _loc_5497(): pass

    label('loc_5497')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_5569',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔，\n',
            '她快点从这里经过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有两次……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再看见她两次，\n',
            '我就能看到活下去的希望了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，万一她要是\n',
            '不再从这里经过怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经过……不经过……\n',
            '经过……不经过……经过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_563F')

    def _loc_5569(): pass

    label('loc_5569')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '有个漂亮的姑娘\n',
            '经常会经过这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一天能见到她好几次，\n',
            '真是幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果今天能\n',
            '见到她经过这里三次的话，\n',
            '我一定会充满干劲的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，在她来之前，\n',
            '我就先装作一副读书的样子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_563F(): pass

    label('loc_563F')

    Jump('loc_595E')

    def _loc_5642(): pass

    label('loc_5642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5740',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_56AF',
    )

    ChrTalk(
        0x00FE,
        (
            '现在街上到处都是节日的气氛，\n',
            '没办法去找工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我到底什么时候\n',
            '才能找到工作啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_573D')

    def _loc_56AF(): pass

    label('loc_56AF')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '唉，好不容易我拿出干劲\n',
            '开始去找工作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在街上到处都是节日的气氛，\n',
            '没办法去找工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我到底什么时候\n',
            '才能找到工作啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_573D(): pass

    label('loc_573D')

    Jump('loc_595E')

    def _loc_5740(): pass

    label('loc_5740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_57D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_577E',
    )

    ChrTalk(
        0x00FE,
        (
            '利库斯为什么就能\n',
            '那么悠闲自得地生活呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_57D5')

    def _loc_577E(): pass

    label('loc_577E')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '从昨天开始到今天，\n',
            '我也渐渐地有些干劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我打算这就去\n',
            '找找适合我的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_57D5(): pass

    label('loc_57D5')

    Jump('loc_595E')

    def _loc_57D8(): pass

    label('loc_57D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_583E',
    )

    ChrTalk(
        0x00FE,
        (
            '今天又无所事事地\n',
            '度过了一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少还是得去找找工作吧，\n',
            '要想办法改变现状才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595E')

    def _loc_583E(): pass

    label('loc_583E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5895',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '今天又是无所事事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去我就\n',
            '只有毫无作为地\n',
            '了却一生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595E')

    def _loc_5895(): pass

    label('loc_5895')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_58E3',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～啊，\n',
            '今天又在无所事事中\n',
            '度过了一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一点干劲都没有～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595E')

    def _loc_58E3(): pass

    label('loc_58E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_595E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '如果我有女朋友的话，\n',
            '就可以一起去观看武术大会了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有个漂亮的姑娘\n',
            '经常会经过这里，\n',
            '她真的很不错呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_595E(): pass

    label('loc_595E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x5962
@scena.Code('func_0D_5962')
def func_0D_5962():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_59B0',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，真热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天看来是睡不成午觉了，\n',
            '到处溜达溜达吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_59B0(): pass

    label('loc_59B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5A0E',
    )

    ChrTalk(
        0x00FE,
        (
            '想做的事情吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算一次也好，\n',
            '好想在格兰赛尔城的\n',
            '空中庭园好好睡一觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5A0E(): pass

    label('loc_5A0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5A65',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，现在对安敦说什么，\n',
            '恐怕他都听不进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁都会有烦恼的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5A65(): pass

    label('loc_5A65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5AEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Return,
        ),
        'loc_5AB7',
    )

    ChrTalk(
        0x00FE,
        (
            '……光看着安敦那家伙\n',
            '是不能满足的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来干点什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AE8')

    def _loc_5AB7(): pass

    label('loc_5AB7')

    ChrTalk(
        0x00FE,
        (
            '……我今天又悠闲地度过了一天，\n',
            '真是满足呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AE8(): pass

    label('loc_5AE8')

    Jump('loc_5DEA')

    def _loc_5AEB(): pass

    label('loc_5AEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5BF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Return,
        ),
        'loc_5B60',
    )

    ChrTalk(
        0x00FE,
        (
            '从某种意义上来说，\n',
            '安敦那家伙也挺幸福的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么非要让自己紧张起来呢？\n',
            '我真是不能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BF1')

    def _loc_5B60(): pass

    label('loc_5B60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_5B95',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙\n',
            '就光会想些莫名其妙的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BF1')

    def _loc_5B95(): pass

    label('loc_5B95')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '今天好像是武术大会的决赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我还是向平常一样\n',
            '在这里悠闲度过今天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5BF1(): pass

    label('loc_5BF1')

    Jump('loc_5DEA')

    def _loc_5BF4(): pass

    label('loc_5BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5C50',
    )

    ChrTalk(
        0x00FE,
        (
            '……安敦的坏习惯\n',
            '又要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他不是找不到工作，\n',
            '而是找不到人生的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5C50(): pass

    label('loc_5C50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5C82',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的天气也很好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5C82(): pass

    label('loc_5C82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5CFF',
    )

    ChrTalk(
        0x00FE,
        (
            '我那朋友今天又是一幅\n',
            '在为什么而烦恼的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果把找工作这个目标\n',
            '作为人生的目标来看待，\n',
            '那就太过局限了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5CFF(): pass

    label('loc_5CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5D59',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦他啊，\n',
            '有什么好顾虑的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有了想法的话，\n',
            '放手去做不就行了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5D59(): pass

    label('loc_5D59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5D8A',
    )

    ChrTalk(
        0x00FE,
        (
            '好吧，\n',
            '在人多起来之前先去吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DEA')

    def _loc_5D8A(): pass

    label('loc_5D8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5DEA',
    )

    ChrTalk(
        0x00FE,
        (
            '我对武术大会没什么兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，不管是什么样的活动，\n',
            '我还是会和平常一样生活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5DEA(): pass

    label('loc_5DEA')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x5DEE
@scena.Code('func_0E_5DEE')
def func_0E_5DEE():
    TalkBegin(0x00FE)
    ClearScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5DFE',
    )

    Jump('loc_5E7A')

    def _loc_5DFE(): pass

    label('loc_5DFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5E0B',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E0B(): pass

    label('loc_5E0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5E18',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E18(): pass

    label('loc_5E18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_5E25',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E25(): pass

    label('loc_5E25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_5E32',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E32(): pass

    label('loc_5E32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_5E3F',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E3F(): pass

    label('loc_5E3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_5E49',
    )

    Jump('loc_5E7A')

    def _loc_5E49(): pass

    label('loc_5E49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_5E56',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E56(): pass

    label('loc_5E56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5E63',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E63(): pass

    label('loc_5E63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5E70',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    Jump('loc_5E7A')

    def _loc_5E70(): pass

    label('loc_5E70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5E7A',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    def _loc_5E7A(): pass

    label('loc_5E7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_5EED',
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
        'loc_5EDC',
    )

    OP_0D()
    OP_A9(0x74)
    OP_56(0x00)
    TalkEnd(0x00FE)

    Return()

    def _loc_5EDC(): pass

    label('loc_5EDC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EED',
    )

    TalkEnd(0x00FE)

    Return()

    def _loc_5EED(): pass

    label('loc_5EED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_5F6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_5F2B',
    )

    ChrTalk(
        0x00FE,
        (
            '今、今天的确要比\n',
            '以往任何时候都要忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F6A')

    def _loc_5F2B(): pass

    label('loc_5F2B')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '请拿好，\n',
            '这是薄荷巧克力品种的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢惠顾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x00FE, 0x0010)

    def _loc_5F6A(): pass

    label('loc_5F6A')

    Jump('loc_64E8')

    def _loc_5F6D(): pass

    label('loc_5F6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_5FAE',
    )

    ChrTalk(
        0x00FE,
        (
            '士兵们好像\n',
            '都很忙的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E8')

    def _loc_5FAE(): pass

    label('loc_5FAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_5FFF',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '亲卫队的那些人怎么样了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你知道什么后续消息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E8')

    def _loc_5FFF(): pass

    label('loc_5FFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_615F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_60A4',
    )

    ChrTalk(
        0x00FE,
        (
            '本日特售的冰淇淋有\n',
            '巧克力味、草莓味、\n',
            '香草味、柠檬味这几种哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还有优胜组的金选手、\n',
            '艾丝蒂尔选手、约修亚选手\n',
            '和奥利维尔选手的形象哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_615C')

    def _loc_60A4(): pass

    label('loc_60A4')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～！\n',
            '本日特售的冰淇淋\n',
            '客人要来一份吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '巧克力味、草莓味、\n',
            '香草味、柠檬味都有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还有优胜组的金选手、\n',
            '艾丝蒂尔选手、约修亚选手\n',
            '和奥利维尔选手的形象哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_615C(): pass

    label('loc_615C')

    Jump('loc_64E8')

    def _loc_615F(): pass

    label('loc_615F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_61CE',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店预定在今天武术大会结束后\n',
            '推出一种限定数量的冰淇淋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要过来尝尝哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E8')

    def _loc_61CE(): pass

    label('loc_61CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6221',
    )

    ChrTalk(
        0x00FE,
        (
            '明天终于到决赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实际上我正在计划一种\n',
            '仅限明天供应的冰淇淋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E8')

    def _loc_6221(): pass

    label('loc_6221')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_62F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_6287',
    )

    ChrTalk(
        0x00FE,
        (
            '从武术大会到诞辰庆典这段时间，\n',
            '将用特别优惠的价格回报大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请抓住机会哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62EF')

    def _loc_6287(): pass

    label('loc_6287')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从武术大会到诞辰庆典这段时间，\n',
            '将用特别优惠的价格回报大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请抓住机会哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62EF(): pass

    label('loc_62EF')

    Jump('loc_64E8')

    def _loc_62F2(): pass

    label('loc_62F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_63C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_6357',
    )

    ChrTalk(
        0x00FE,
        (
            '本店的冰淇淋\n',
            '虽然种类不多，\n',
            '但每种都是经过精心制作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要品尝一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63BE')

    def _loc_6357(): pass

    label('loc_6357')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店的冰淇淋\n',
            '虽然种类不多，\n',
            '但每种都是经过精心制作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要品尝一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63BE(): pass

    label('loc_63BE')

    Jump('loc_64E8')

    def _loc_63C1(): pass

    label('loc_63C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6455',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都说我的店子\n',
            '是王室御用的，\n',
            '其实只是传言而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，科洛蒂娅公主\n',
            '如果偷溜出城到街上来玩，\n',
            '说不定真的会光临我这里一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E8')

    def _loc_6455(): pass

    label('loc_6455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_64B0',
    )

    ChrTalk(
        0x00FE,
        (
            '在大会上助威呐喊辛苦了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用凉爽的冰淇淋来\n',
            '滋润一下干燥的喉咙怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E8')

    def _loc_64B0(): pass

    label('loc_64B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_64E8',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来点凉爽美味的\n',
            '冰淇淋如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64E8(): pass

    label('loc_64E8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x64EC
@scena.Code('func_0F_64EC')
def func_0F_64EC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_656A',
    )

    ChrTalk(
        0x00FE,
        (
            '我为了维持家庭生计\n',
            '而忙于工作，\n',
            '不能照顾好孩子们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管他们的前程会怎样，\n',
            '关键还是在于自身的努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_670D')

    def _loc_656A(): pass

    label('loc_656A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_65DA',
    )

    ChrTalk(
        0x00FE,
        (
            '我们原本打算在诞辰庆典之前\n',
            '一直呆在王都的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是最近定期船时常停运，\n',
            '有些担心家里的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_670D')

    def _loc_65DA(): pass

    label('loc_65DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6609',
    )

    ChrTalk(
        0x00FE,
        (
            '男孩子就是要\n',
            '充满阳光感才好哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_670D')

    def _loc_6609(): pass

    label('loc_6609')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6678',
    )

    ChrTalk(
        0x00FE,
        (
            '这位夫人是\n',
            '定期船的空中乘务员哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为大家都是\n',
            '有工作有儿女的人，\n',
            '所以谈起话来会更加投缘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_670D')

    def _loc_6678(): pass

    label('loc_6678')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_66D4',
    )

    ChrTalk(
        0x00FE,
        (
            '这个冰淇淋店的\n',
            '冰淇淋真的非常好吃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说这个店子\n',
            '在王都非常有名吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_670D')

    def _loc_66D4(): pass

    label('loc_66D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_66DE',
    )

    Jump('loc_670D')

    def _loc_66DE(): pass

    label('loc_66DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_66E8',
    )

    Jump('loc_670D')

    def _loc_66E8(): pass

    label('loc_66E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_66F2',
    )

    Jump('loc_670D')

    def _loc_66F2(): pass

    label('loc_66F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_66FC',
    )

    Jump('loc_670D')

    def _loc_66FC(): pass

    label('loc_66FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6706',
    )

    Jump('loc_670D')

    def _loc_6706(): pass

    label('loc_6706')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_670D',
    )

    def _loc_670D(): pass

    label('loc_670D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x6711
@scena.Code('func_10_6711')
def func_10_6711():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_674B',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈去给我买冰淇淋了，\n',
            '让我在这儿等着～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68BC')

    def _loc_674B(): pass

    label('loc_674B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_677C',
    )

    ChrTalk(
        0x00FE,
        (
            '卢希娅啊，\n',
            '还想再吃一个冰淇淋呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68BC')

    def _loc_677C(): pass

    label('loc_677C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_67FB',
    )

    ChrTalk(
        0x00FE,
        (
            '卢希娅住的村子啊，\n',
            '离海边很近很近哦～\n',
            '还盛开着纯白色的花儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且，我还有波利他们\n',
            '那样很多很多的朋友哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68BC')

    def _loc_67FB(): pass

    label('loc_67FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6846',
    )

    ChrTalk(
        0x00FE,
        (
            '卢希娅我好想\n',
            '快点进王城看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但现在已经不能进去了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68BC')

    def _loc_6846(): pass

    label('loc_6846')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6883',
    )

    ChrTalk(
        0x00FE,
        (
            '冰淇淋～\n',
            '真的很好吃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是妈妈买给我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68BC')

    def _loc_6883(): pass

    label('loc_6883')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_688D',
    )

    Jump('loc_68BC')

    def _loc_688D(): pass

    label('loc_688D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6897',
    )

    Jump('loc_68BC')

    def _loc_6897(): pass

    label('loc_6897')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_68A1',
    )

    Jump('loc_68BC')

    def _loc_68A1(): pass

    label('loc_68A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_68AB',
    )

    Jump('loc_68BC')

    def _loc_68AB(): pass

    label('loc_68AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_68B5',
    )

    Jump('loc_68BC')

    def _loc_68B5(): pass

    label('loc_68B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_68BC',
    )

    def _loc_68BC(): pass

    label('loc_68BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x68C0
@scena.Code('func_11_68C0')
def func_11_68C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_6A1D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_695C',
    )

    ChrTalk(
        0x00FE,
        (
            '托这次庆典的福，\n',
            '和孩子一起好好的玩耍了一番，\n',
            '也交到了很好的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来就要开始繁忙的工作了，\n',
            '不管怎么说，\n',
            '也得更加努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A1A')

    def _loc_695C(): pass

    label('loc_695C')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '下次我要作为\n',
            '『赛希莉亚号』的乘务员出航。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过托这次庆典的福，\n',
            '和孩子一起好好的玩耍了一番，\n',
            '也交到了很好的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来就要开始繁忙的工作了，\n',
            '不管怎么说，\n',
            '也得更加努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A1A(): pass

    label('loc_6A1A')

    Jump('loc_7014')

    def _loc_6A1D(): pass

    label('loc_6A1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_6A9D',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '今天开始本来可以去上班的，\n',
            '但空港却又被封锁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是为了逮捕\n',
            '在逃中的恐怖分子，\n',
            '但总觉得不太平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7014')

    def _loc_6A9D(): pass

    label('loc_6A9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6AD8',
    )

    ChrTalk(
        0x00FE,
        (
            '见到卡拉的孩子，\n',
            '就会觉得有个女儿也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7014')

    def _loc_6AD8(): pass

    label('loc_6AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6BB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_6B30',
    )

    ChrTalk(
        0x00FE,
        (
            '这位夫人\n',
            '和她丈夫一起\n',
            '经营一家旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听起来\n',
            '就觉得很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BAE')

    def _loc_6B30(): pass

    label('loc_6B30')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '我们儿女关系很好，\n',
            '家长谈起话来\n',
            '也会很投缘呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这位夫人\n',
            '和她丈夫一起\n',
            '经营一家旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听起来\n',
            '就觉得很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BAE(): pass

    label('loc_6BAE')

    Jump('loc_7014')

    def _loc_6BB1(): pass

    label('loc_6BB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6C4B',
    )

    ChrTalk(
        0x00FE,
        (
            '这个冰淇淋店卖的\n',
            '冰淇淋真的很不错哦，\n',
            '在王都也受到一致的好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说科洛蒂娅公主\n',
            '也微服来这里光顾过，\n',
            '所以这里还被称为王室御用的店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7014')

    def _loc_6C4B(): pass

    label('loc_6C4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6CAC',
    )

    ChrTalk(
        0x00FE,
        (
            '回家之前在\n',
            '这个公园里面\n',
            '稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没带小孩一起出来玩了，\n',
            '好累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7014')

    def _loc_6CAC(): pass

    label('loc_6CAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6CF3',
    )

    ChrTalk(
        0x00FE,
        (
            '我家孩子似乎\n',
            '相当喜欢武术大会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是男孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7014')

    def _loc_6CF3(): pass

    label('loc_6CF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_6E1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_6D7F',
    )

    ChrTalk(
        0x00FE,
        (
            '在武术大会上，\n',
            '绑架了我们的空贼竟然也出场了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为余兴节目，\n',
            '他也许会觉得很有趣，\n',
            '但对我们来说心情真是复杂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E1C')

    def _loc_6D7F(): pass

    label('loc_6D7F')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '在武术大会上，\n',
            '绑架了我们的空贼竟然也出场了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '杜南公爵\n',
            '到底在想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为余兴节目，\n',
            '他也许会觉得很有趣，\n',
            '但对我们来说心情真是复杂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E1C(): pass

    label('loc_6E1C')

    Jump('loc_7014')

    def _loc_6E1F(): pass

    label('loc_6E1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6E8A',
    )

    ChrTalk(
        0x00FE,
        (
            '孩子总是催我，\n',
            '所以今天打算带他去看武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '这样下去会不会变得\n',
            '过于溺爱孩子了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7014')

    def _loc_6E8A(): pass

    label('loc_6E8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6F90',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_6EFD',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会期间\n',
            '从各地前来观战的人很多，\n',
            '定期船也应该是非常拥挤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公社那边真的没问题吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F8D')

    def _loc_6EFD(): pass

    label('loc_6EFD')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '武术大会期间\n',
            '从各地前来观战的人很多，\n',
            '定期船也应该是非常拥挤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种时期休假，\n',
            '感觉有些过意不去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公社那边真的没问题吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F8D(): pass

    label('loc_6F8D')

    Jump('loc_7014')

    def _loc_6F90(): pass

    label('loc_6F90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_7014',
    )

    ChrTalk(
        0x00FE,
        (
            '因为我在柏斯的空贼事件里\n',
            '一直被囚禁在空贼基地，\n',
            '所以公司现在让我休假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样就能够长时间和孩子在一起了，\n',
            '真是开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7014(): pass

    label('loc_7014')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x7018
@scena.Code('func_12_7018')
def func_12_7018():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7068',
    )

    ChrTalk(
        0x00FE,
        (
            '果然还是这里的\n',
            '冰淇淋好吃呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很喜欢吃薄荷巧克力味的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_7068(): pass

    label('loc_7068')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_7095',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈她们总是\n',
            '在那里说个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_7095(): pass

    label('loc_7095')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_70CF',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀～我啊，\n',
            '真是好想去\n',
            '卢希娅的家里玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_70CF(): pass

    label('loc_70CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_70F8',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '我也进过王城的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_70F8(): pass

    label('loc_70F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_713B',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～冰淇淋真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家店的\n',
            '冰淇淋非常好吃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_713B(): pass

    label('loc_713B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_716B',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈很快就累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好没劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_716B(): pass

    label('loc_716B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_718F',
    )

    ChrTalk(
        0x00FE,
        (
            '今天也想去看比赛呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_718F(): pass

    label('loc_718F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_71DB',
    )

    ChrTalk(
        0x00FE,
        (
            '比武大会，\n',
            '实在太有气魄了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我简直都激动得\n',
            '要飞上天了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_71DB(): pass

    label('loc_71DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_7224',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '今天我要去看武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们是不是很羡慕啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_7224(): pass

    label('loc_7224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_7270',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈总是\n',
            '可以乘坐飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等我长大了，\n',
            '也想在飞艇上工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7298')

    def _loc_7270(): pass

    label('loc_7270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_7298',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～\n',
            '今天能和妈妈一起玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7298(): pass

    label('loc_7298')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x729C
@scena.Code('func_13_729C')
def func_13_729C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_735D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_72DD',
    )

    ChrTalk(
        0x00FE,
        (
            '我一直这样坚信\n',
            '亲卫队是不会背叛陛下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_735A')

    def _loc_72DD(): pass

    label('loc_72DD')

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '我一直这样坚信\n',
            '亲卫队是不会背叛陛下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '发动政变的居然是理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也着实让人有些无法理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_735A(): pass

    label('loc_735A')

    Jump('loc_77A0')

    def _loc_735D(): pass

    label('loc_735D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_73A8',
    )

    ChrTalk(
        0x00FE,
        (
            '王都守卫队\n',
            '怎么都匆匆忙忙撤离了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……有种不祥的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_73A8(): pass

    label('loc_73A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7414',
    )

    ChrTalk(
        0x00FE,
        (
            '距离诞辰庆典只有几天了，\n',
            '但是王城内却没有发布任何公告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概都忙着搜捕\n',
            '亲卫队去了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_7414(): pass

    label('loc_7414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_748A',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校和尤莉亚中尉\n',
            '要是能携手合作，\n',
            '我想利贝尔一定会国泰民安的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到却变成了这个样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_748A(): pass

    label('loc_748A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_7505',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说那些特务部队的人\n',
            '是理查德上校的部下，\n',
            '不过却不招人喜欢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到王国军里\n',
            '竟然会有这样的一个组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_7505(): pass

    label('loc_7505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_755D',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来尤莉亚中尉\n',
            '相当热衷于去教会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做弥撒的时候\n',
            '看见过她好多次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_755D(): pass

    label('loc_755D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_75DE',
    )

    ChrTalk(
        0x00FE,
        (
            '以前在这一带\n',
            '常常可以看见\n',
            '尤莉亚中尉巡查市区的身影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我腰疼的时候还得到她的照顾，\n',
            '真是一个善良又体贴的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_75DE(): pass

    label('loc_75DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_7653',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤号』在空港\n',
            '被军队扣押住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此，\n',
            '亲卫队还是在蔡斯出现了，\n',
            '他们会来进攻王都吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_7653(): pass

    label('loc_7653')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_76C9',
    )

    ChrTalk(
        0x00FE,
        (
            '在市民心中，\n',
            '亲卫队的人气是非常高的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且每年都会在武术大会中出场，\n',
            '让诞辰庆典的气氛高涨起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_76C9(): pass

    label('loc_76C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_776B',
    )

    ChrTalk(
        0x00FE,
        (
            '不管怎样，对于亲卫队\n',
            '会来阻碍女王诞辰庆典的说法，\n',
            '我还是不敢相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算他们有反叛的意图，\n',
            '也会堂堂正正地进行战斗，\n',
            '而不是采用这种低劣的手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_77A0')

    def _loc_776B(): pass

    label('loc_776B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_77A0',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是去观看武术大会的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_77A0(): pass

    label('loc_77A0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x77A4
@scena.Code('func_14_77A4')
def func_14_77A4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7826',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然把女王陛下幽禁起来，\n',
            '还把科洛蒂娅公主诱拐走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这些事实面前，\n',
            '已经无法再称赞\n',
            '理查德上校的功绩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7826(): pass

    label('loc_7826')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_78A6',
    )

    ChrTalk(
        0x00FE,
        (
            '出来买东西的时候……\n',
            '感觉街上的气氛和平时不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警备的士兵们都换了，\n',
            '而且虽然街上有人，但是感觉异常安静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_78A6(): pass

    label('loc_78A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_78FC',
    )

    ChrTalk(
        0x00FE,
        (
            '现在似乎还是\n',
            '不能进王城参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '远道而来的游客\n',
            '想必感到很遗憾吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_78FC(): pass

    label('loc_78FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_7977',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '你们不就是获得优胜的选手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恭喜！\n',
            '是场很棒的比赛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起特务部队，\n',
            '你们取得优胜更好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7977(): pass

    label('loc_7977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_7C05',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 3, 0x6EB)),
            Expr.Return,
        ),
        'loc_79DE',
    )

    ChrTalk(
        0x00FE,
        (
            '那个人总用奇怪的眼神\n',
            '盯着我看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不知道他想干什么，\n',
            '不过真是太没礼貌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_79DE(): pass

    label('loc_79DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_7A3E',
    )

    ChrTalk(
        0x00FE,
        (
            '那个人总用奇怪的眼神\n',
            '盯着我看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我不知道他想干什么，\n',
            '不过真是太没礼貌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_7A3E(): pass

    label('loc_7A3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_7B08',
    )

    OP_63(0x0031)

    ChrTalk(
        0x00FE,
        (
            '那边的那个人，\n',
            '从刚才开始就一直在盯着我看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好可怕，不想从这里经过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0031, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊，你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了，\n',
            '有游击士在身边就感觉安全多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0002, 5, 0x15))
    OP_4B(0x0031, 255)

    Jump('loc_7C02')

    def _loc_7B08(): pass

    label('loc_7B08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_7B6C',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才又不小心\n',
            '看到了那个男人的目光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉有点可怕……\n',
            '我想还是不要从那边经过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_7B6C(): pass

    label('loc_7B6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_7BB7',
    )

    ChrTalk(
        0x00FE,
        (
            '在百货店前有个男人\n',
            '一直在盯着我看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉有点恶心呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C02')

    def _loc_7BB7(): pass

    label('loc_7BB7')

    ChrTalk(
        0x00FE,
        (
            '从昨天开始就有士兵在大街上晃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道他们已经\n',
            '找到了亲卫队的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C02(): pass

    label('loc_7C02')

    Jump('loc_7D5D')

    def _loc_7C05(): pass

    label('loc_7C05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_7C63',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队竟然\n',
            '被赶出王城了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是因为杜南公爵嫉妒亲卫队\n',
            '而下达了这个命令吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7C63(): pass

    label('loc_7C63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_7CA6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '今天也是个清爽的早晨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '心情真是不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7CA6(): pass

    label('loc_7CA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_7CCF',
    )

    ChrTalk(
        0x00FE,
        (
            '比赛的结果\n',
            '怎么样了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7CCF(): pass

    label('loc_7CCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_7CF7',
    )

    ChrTalk(
        0x00FE,
        (
            '大会终于进入正式环节了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7CF7(): pass

    label('loc_7CF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_7D24',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '街上果然变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5D')

    def _loc_7D24(): pass

    label('loc_7D24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_7D5D',
    )

    ChrTalk(
        0x00FE,
        (
            '东街区这个冰淇淋店\n',
            '卖的冰淇淋\n',
            '简直太好吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D5D(): pass

    label('loc_7D5D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x7D61
@scena.Code('func_15_7D61')
def func_15_7D61():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_7D99',
    )

    ChrTalk(
        0x00FE,
        (
            '能够看到女王陛下的尊容，\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7D99(): pass

    label('loc_7D99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_7DE9',
    )

    ChrTalk(
        0x00FE,
        (
            '平常的那些士兵们\n',
            '都已经不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王城那里\n',
            '发生什么事了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7DE9(): pass

    label('loc_7DE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7E63',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下如果不能参加诞辰庆典，\n',
            '就只能看见杜南公爵那家伙了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在庆典开始之前\n',
            '病情一定要好转起来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7E63(): pass

    label('loc_7E63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_7EB7',
    )

    ChrTalk(
        0x00FE,
        (
            '决胜战好有魄力呀，\n',
            '连我也很兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '是时候回家做晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7EB7(): pass

    label('loc_7EB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_7F0F',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '我在大圣堂见到一位\n',
            '以前从没见过的修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她好像是新来的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7F0F(): pass

    label('loc_7F0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_7F48',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，在艾德尔百货店\n',
            '买了东西再回去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7F48(): pass

    label('loc_7F48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_7F88',
    )

    ChrTalk(
        0x00FE,
        (
            '因为下午还有比赛，\n',
            '就在这会儿把\n',
            '事情全部办完吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7F88(): pass

    label('loc_7F88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_7FBD',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～武术大会的比赛我看了，\n',
            '真精彩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7FBD(): pass

    label('loc_7FBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_7FF5',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的比赛会怎么样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_7FF5(): pass

    label('loc_7FF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_8036',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，虽说是预选赛，\n',
            '但值得一看的比赛也有不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8079')

    def _loc_8036(): pass

    label('loc_8036')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_8079',
    )

    ChrTalk(
        0x00FE,
        (
            '这个武术大会啊，\n',
            '是王都市民每年的\n',
            '一项重要娱乐活动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8079(): pass

    label('loc_8079')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x807D
@scena.Code('func_16_807D')
def func_16_807D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_80DD',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典开始后，\n',
            '这附近就变得比较冷清了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为如此，更要加强戒备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8263')

    def _loc_80DD(): pass

    label('loc_80DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_80E7',
    )

    Jump('loc_8263')

    def _loc_80E7(): pass

    label('loc_80E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8128',
    )

    ChrTalk(
        0x00FE,
        (
            '果然啊，大会结束了之后\n',
            '这一带就变得有些冷清了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8263')

    def _loc_8128(): pass

    label('loc_8128')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_81A1',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士小组获胜了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特务部队是最精锐的部队，\n',
            '我还以为他们一定会赢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果还是被游击士打败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8263')

    def _loc_81A1(): pass

    label('loc_81A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_81EE',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是总决赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须做好警备工作，\n',
            '以防让任何事故发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8263')

    def _loc_81EE(): pass

    label('loc_81EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_8234',
    )

    ChrTalk(
        0x00FE,
        (
            '来看武术大会的人\n',
            '实在太多了，\n',
            '执行警备工作也相当辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8263')

    def _loc_8234(): pass

    label('loc_8234')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_823E',
    )

    Jump('loc_8263')

    def _loc_823E(): pass

    label('loc_823E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_8248',
    )

    Jump('loc_8263')

    def _loc_8248(): pass

    label('loc_8248')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_8252',
    )

    Jump('loc_8263')

    def _loc_8252(): pass

    label('loc_8252')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_825C',
    )

    Jump('loc_8263')

    def _loc_825C(): pass

    label('loc_825C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_8263',
    )

    def _loc_8263(): pass

    label('loc_8263')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x8267
@scena.Code('func_17_8267')
def func_17_8267():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_82C0',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军整体\n',
            '最近要进行重组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是希望能够有一个\n',
            '亲切的人作上司啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8457')

    def _loc_82C0(): pass

    label('loc_82C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_82CA',
    )

    Jump('loc_8457')

    def _loc_82CA(): pass

    label('loc_82CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8347',
    )

    ChrTalk(
        0x00FE,
        (
            '恐怖事件的犯人\n',
            '好像还没有抓到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此，\n',
            '还得继续保持这样的警戒状态……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也觉得\n',
            '多少有些累了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8457')

    def _loc_8347(): pass

    label('loc_8347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_83B0',
    )

    ChrTalk(
        0x00FE,
        (
            '因为昨天的巡逻\n',
            '导致睡眠不足，\n',
            '今天要早点睡才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大会也顺利结束了，\n',
            '好想放会儿假啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8457')

    def _loc_83B0(): pass

    label('loc_83B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_83F1',
    )

    ChrTalk(
        0x00FE,
        (
            '我昨天通宵\n',
            '在王都里巡逻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经睡眠不足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8457')

    def _loc_83F1(): pass

    label('loc_83F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_8428',
    )

    ChrTalk(
        0x00FE,
        (
            '为了对付恐怖分子，\n',
            '今天也要在街上巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8457')

    def _loc_8428(): pass

    label('loc_8428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_8432',
    )

    Jump('loc_8457')

    def _loc_8432(): pass

    label('loc_8432')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_843C',
    )

    Jump('loc_8457')

    def _loc_843C(): pass

    label('loc_843C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_8446',
    )

    Jump('loc_8457')

    def _loc_8446(): pass

    label('loc_8446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_8450',
    )

    Jump('loc_8457')

    def _loc_8450(): pass

    label('loc_8450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_8457',
    )

    def _loc_8457(): pass

    label('loc_8457')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x845B
@scena.Code('func_18_845B')
def func_18_845B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_84BA',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军整体\n',
            '最近要进行重组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是希望能给\n',
            '既诚实又有真本领的人当部下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_861B')

    def _loc_84BA(): pass

    label('loc_84BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_84C4',
    )

    Jump('loc_861B')

    def _loc_84C4(): pass

    label('loc_84C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_852A',
    )

    ChrTalk(
        0x00FE,
        (
            '不仅街上在进行警戒，\n',
            '关所似乎也暂时封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抓到那些恐怖分子\n',
            '也只是时间的问题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_861B')

    def _loc_852A(): pass

    label('loc_852A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_8557',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来就该到\n',
            '百货店里巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_861B')

    def _loc_8557(): pass

    label('loc_8557')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_859F',
    )

    ChrTalk(
        0x00FE,
        (
            '如果发现了亲卫队\n',
            '或者形迹可疑的人，\n',
            '请务必马上告知我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_861B')

    def _loc_859F(): pass

    label('loc_859F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_85EC',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然让空贼那群人\n',
            '参加武术大会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵到底在想些什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_861B')

    def _loc_85EC(): pass

    label('loc_85EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_85F6',
    )

    Jump('loc_861B')

    def _loc_85F6(): pass

    label('loc_85F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_8600',
    )

    Jump('loc_861B')

    def _loc_8600(): pass

    label('loc_8600')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_860A',
    )

    Jump('loc_861B')

    def _loc_860A(): pass

    label('loc_860A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_8614',
    )

    Jump('loc_861B')

    def _loc_8614(): pass

    label('loc_8614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_861B',
    )

    def _loc_861B(): pass

    label('loc_861B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x861F
@scena.Code('func_19_861F')
def func_19_861F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_862C',
    )

    Jump('loc_86B6')

    def _loc_862C(): pass

    label('loc_862C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_865F',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂，\n',
            '不要在这里乱看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86B6')

    def _loc_865F(): pass

    label('loc_865F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8669',
    )

    Jump('loc_86B6')

    def _loc_8669(): pass

    label('loc_8669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_8673',
    )

    Jump('loc_86B6')

    def _loc_8673(): pass

    label('loc_8673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_867D',
    )

    Jump('loc_86B6')

    def _loc_867D(): pass

    label('loc_867D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_8687',
    )

    Jump('loc_86B6')

    def _loc_8687(): pass

    label('loc_8687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_8691',
    )

    Jump('loc_86B6')

    def _loc_8691(): pass

    label('loc_8691')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_869B',
    )

    Jump('loc_86B6')

    def _loc_869B(): pass

    label('loc_869B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_86A5',
    )

    Jump('loc_86B6')

    def _loc_86A5(): pass

    label('loc_86A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_86AF',
    )

    Jump('loc_86B6')

    def _loc_86AF(): pass

    label('loc_86AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_86B6',
    )

    def _loc_86B6(): pass

    label('loc_86B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x86BA
@scena.Code('func_1A_86BA')
def func_1A_86BA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_86C7',
    )

    Jump('loc_8774')

    def _loc_86C7(): pass

    label('loc_86C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_871D',
    )

    ChrTalk(
        0x00FE,
        (
            '这几天在城里\n',
            '都没有看见理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是外出\n',
            '到什么地方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8774')

    def _loc_871D(): pass

    label('loc_871D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8727',
    )

    Jump('loc_8774')

    def _loc_8727(): pass

    label('loc_8727')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_8731',
    )

    Jump('loc_8774')

    def _loc_8731(): pass

    label('loc_8731')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_873B',
    )

    Jump('loc_8774')

    def _loc_873B(): pass

    label('loc_873B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_8745',
    )

    Jump('loc_8774')

    def _loc_8745(): pass

    label('loc_8745')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_874F',
    )

    Jump('loc_8774')

    def _loc_874F(): pass

    label('loc_874F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_8759',
    )

    Jump('loc_8774')

    def _loc_8759(): pass

    label('loc_8759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_8763',
    )

    Jump('loc_8774')

    def _loc_8763(): pass

    label('loc_8763')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_876D',
    )

    Jump('loc_8774')

    def _loc_876D(): pass

    label('loc_876D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_8774',
    )

    def _loc_8774(): pass

    label('loc_8774')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x8778
@scena.Code('func_1B_8778')
def func_1B_8778():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_8785',
    )

    Jump('loc_88B6')

    def _loc_8785(): pass

    label('loc_8785')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_885F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_87E4',
    )

    ChrTalk(
        0x00FE,
        (
            '哼，我不认为决赛时\n',
            '洛伦斯队长使出了全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长肯定是\n',
            '手下留情了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_885C')

    def _loc_87E4(): pass

    label('loc_87E4')

    SetScenaFlags(ScenaFlag(0x0002, 7, 0x17))

    ChrTalk(
        0x00FE,
        (
            '你们好像是\n',
            '武术大会取得优胜的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，我不认为决赛时\n',
            '洛伦斯队长使出了全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长肯定是\n',
            '手下留情了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_885C(): pass

    label('loc_885C')

    Jump('loc_88B6')

    def _loc_885F(): pass

    label('loc_885F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8869',
    )

    Jump('loc_88B6')

    def _loc_8869(): pass

    label('loc_8869')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_8873',
    )

    Jump('loc_88B6')

    def _loc_8873(): pass

    label('loc_8873')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_887D',
    )

    Jump('loc_88B6')

    def _loc_887D(): pass

    label('loc_887D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_8887',
    )

    Jump('loc_88B6')

    def _loc_8887(): pass

    label('loc_8887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_8891',
    )

    Jump('loc_88B6')

    def _loc_8891(): pass

    label('loc_8891')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_889B',
    )

    Jump('loc_88B6')

    def _loc_889B(): pass

    label('loc_889B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_88A5',
    )

    Jump('loc_88B6')

    def _loc_88A5(): pass

    label('loc_88A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_88AF',
    )

    Jump('loc_88B6')

    def _loc_88AF(): pass

    label('loc_88AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_88B6',
    )

    def _loc_88B6(): pass

    label('loc_88B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x88BA
@scena.Code('func_1C_88BA')
def func_1C_88BA():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '好～的，\n',
            '接下来去百货店看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x88E6
@scena.Code('func_1D_88E6')
def func_1D_88E6():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '怎么也要在王都\n',
            '买到流行的衣服才回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x8918
@scena.Code('func_1E_8918')
def func_1E_8918():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '为何会有那么多人\n',
            '在那边排队呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟是在排什么队呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x8960
@scena.Code('func_1F_8960')
def func_1F_8960():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我、我已经不是小孩了，\n',
            '怎么会想吃那种东西！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x8998
@scena.Code('func_20_8998')
def func_20_8998():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，是吗，\n',
            '你已经不是小孩了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那老爸我要开始吃了哦～\n',
            '哈～哈～哈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x89F3
@scena.Code('func_21_89F3')
def func_21_89F3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呀哈……\n',
            '好热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x8A13
@scena.Code('func_22_8A13')
def func_22_8A13():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今天有一点热呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想吃点凉爽的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0023 offset: 0x8A4A
@scena.Code('func_23_8A4A')
def func_23_8A4A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能插队哦，\n',
            '快到后面去排着吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0024 offset: 0x8A82
@scena.Code('func_24_8A82')
def func_24_8A82():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '等呀等呀等～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0025 offset: 0x8A9F
@scena.Code('func_25_8A9F')
def func_25_8A9F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '当听说政变的时候我很担忧，\n',
            '幸亏被亲卫队和游击士阻止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来我就开始\n',
            '担心王国军是否还好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0026 offset: 0x8B10
@scena.Code('func_26_8B10')
def func_26_8B10():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呵呵，历史资料馆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束之后，\n',
            '一定要去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0027 offset: 0x8B58
@scena.Code('func_27_8B58')
def func_27_8B58():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '人啊，\n',
            '要活到老，学到老。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0028 offset: 0x8B7E
@scena.Code('func_28_8B7E')
def func_28_8B7E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '痛痛痛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王都太大了，走的路过多，\n',
            '结果脚都给磨破了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～啊，好惨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0029 offset: 0x8BDC
@scena.Code('func_29_8BDC')
def func_29_8BDC():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '如果鞋子适脚的话，\n',
            '走起来就会很舒服的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002A offset: 0x8C12
@scena.Code('func_2A_8C12')
def func_2A_8C12():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '爸～爸，你好～差劲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002B offset: 0x8C33
@scena.Code('func_2B_8C33')
def func_2B_8C33():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '噗噜噗噜噗噜…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果政变得逞的话，\n',
            '那个杜南公爵\n',
            '就会成为国王吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样一来这个王国就完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002C offset: 0x8CA8
@scena.Code('func_2C_8CA8')
def func_2C_8CA8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '所谓恐怖事件不就是\n',
            '情报部自导自演的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直不认为亲卫队是坏人，\n',
            '所以很放心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002D offset: 0x8D0B
@scena.Code('func_2D_8D0B')
def func_2D_8D0B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '百货店好像在搞\n',
            '诞辰庆典纪念大酬宾哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各种商品都\n',
            '变得很便宜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002E offset: 0x8D5C
@scena.Code('func_2E_8D5C')
def func_2E_8D5C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呀啊～真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快快，现在立刻就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x002F offset: 0x8D95
@scena.Code('func_2F_8D95')
def func_2F_8D95():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，没想到在政变之后\n',
            '还能有如此盛大的庆典。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0030 offset: 0x8DCF
@scena.Code('func_30_8DCF')
def func_30_8DCF():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哦，这里就是共和国大使馆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想进去看看，哪怕一次也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0031 offset: 0x8E1C
@scena.Code('func_31_8E1C')
def func_31_8E1C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我是第一次来王都呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太～棒了，好宽的大街啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0032 offset: 0x8E5B
@scena.Code('func_32_8E5B')
def func_32_8E5B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '喂～不要跑那么远～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我担心女儿\n',
            '会不小心迷路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0033 offset: 0x8E9B
@scena.Code('func_33_8E9B')
def func_33_8E9B():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '今年的航运杂乱无章，\n',
            '害我没能欣赏到\n',
            '武术大会的盛况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且竟然是理查德上校\n',
            '发动的政变导致的这一切。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '我可是上校的忠实支持者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0034 offset: 0x8F34
@scena.Code('func_34_8F34')
def func_34_8F34():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我想买一个\n',
            '玩具飞艇～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0035 offset: 0x8F56
@scena.Code('func_35_8F56')
def func_35_8F56():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '孙子一直缠着我，\n',
            '就只好带他到百货店去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0036 offset: 0x8F8C
@scena.Code('func_36_8F8C')
def func_36_8F8C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这种话只能在\n',
            '一切都结束了才能说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会的优胜者\n',
            '阻止了此次政变，\n',
            '真是让人痛快之极啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市民的情绪这么高涨\n',
            '也不是没有原因的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0037 offset: 0x9023
@scena.Code('func_37_9023')
def func_37_9023():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '从帝国大使馆门前走过时\n',
            '不知为何就紧张起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很可能是看到了那扇大门，\n',
            '产生了压迫感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0038 offset: 0x908A
@scena.Code('func_38_908A')
def func_38_908A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '明明说好了你要自己走路的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，拿你没办法呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0039 offset: 0x90D3
@scena.Code('func_39_90D3')
def func_39_90D3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '姐姐，背我嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x003A offset: 0x90EE
@scena.Code('func_3A_90EE')
def func_3A_90EE():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '典礼已经结束了，\n',
            '这下可以在市区内逛逛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
