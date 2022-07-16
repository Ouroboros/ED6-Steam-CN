import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2600   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '基库'),
    TXT(0x02, '米克'),
    TXT(0x03, '艾福托老师'),
    TXT(0x04, '王立学院·小道'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2600.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2600._SN', 'ED6_DT01/T2600_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xD0D
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
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3600,
            z                   = 0,
            y                   = -6100,
            direction           = 270,
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
            x                   = 300,
            z                   = 0,
            y                   = -3000,
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
            x                   = 170,
            z                   = 0,
            y                   = -16239,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x142
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2090,
            y           = -1000,
            z           = 4090,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x000008C0,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000000,
        ),
    )

# id: 0x10005 offset: 0x162
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 1000,
            triggerY            = 9720,
            triggerRange        = 800,
            actorX              = 0,
            actorZ              = 2000,
            actorY              = 9720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33200,
            triggerZ            = 0,
            triggerY            = 14410,
            triggerRange        = 1000,
            actorX              = 32509,
            actorZ              = 0,
            actorY              = 14410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1AA
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_1BA'),
        (0x00000067, 'loc_1DB'),
        (-1, 'loc_1F1'),
    )

    def _loc_1BA(): pass

    label('loc_1BA')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D8',
    )

    OP_28(0x0027, 0x01, 0x8000)
    Event(1, 0x0002)

    def _loc_1D8(): pass

    label('loc_1D8')

    Jump('loc_1F1')

    def _loc_1DB(): pass

    label('loc_1DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 3, 0x433)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1EE',
    )

    SetScenaFlags(ScenaFlag(0x0086, 3, 0x433))
    Event(0, 0x0002)

    def _loc_1EE(): pass

    label('loc_1EE')

    Jump('loc_1F1')

    def _loc_1F1(): pass

    label('loc_1F1')

    Return()

# id: 0x0001 offset: 0x1F2
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -106000, 196686)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_225',
    )

    OP_B1('t2600_y')

    Jump('loc_22E')

    def _loc_225(): pass

    label('loc_225')

    OP_B1('t2600_n')

    def _loc_22E(): pass

    label('loc_22E')

    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_246',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0010)

    Jump('loc_263')

    def _loc_246(): pass

    label('loc_246')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x2000)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_263',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0010)

    def _loc_263(): pass

    label('loc_263')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 1, 0x4C9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_275',
    )

    OP_6F(0x0002, 0)

    Jump('loc_27C')

    def _loc_275(): pass

    label('loc_275')

    OP_6F(0x0002, 60)

    def _loc_27C(): pass

    label('loc_27C')

    Return()

# id: 0x0002 offset: 0x27D
@scena.Code('ReInit')
def ReInit():
    SetMapFlags(0x10000000)
    FormationAddMember(0x01, 0xFF)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(29000, 5000, 27750, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0102, 28100, 5000, 28150, 90)
    SetChrPos(0x0101, 15980, 5000, 27660, 0)
    SetChrPos(0x0105, 15980, 5000, 28860, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020060412V#013F#5P奇怪了……\n',
            '刚才还看到这里有动静的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060413V#013F……但是，难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060414V#4P约修亚～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_039E')
    def lambda_039E():
        CameraMove(27000, 5000, 28210, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_039E)

    @scena.Lambda('lambda_03B6')
    def lambda_03B6():
        ChrWalkTo(0x00FE, 26850, 5000, 27660, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03B6)

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(200)

    ChrWalkTo(0x0105, 26410, 5000, 28860, 5000, 0x00)
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060415V#014F艾丝蒂尔、科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060416V#007F#1P真是的，\n',
            '别惹人担心嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060417V听说你去追那个银发男子，\n',
            '吓了我们一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060418V#014F咦？……你们怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060419V#040F是波利告诉我们的。\n',
            '说你看到了那个银发男子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060420V因为那孩子好像也看见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060421V#010F是吗，好敏锐的孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060422V#013F我隐约看见一个背影，\n',
            '然后一直追到了这里来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060423V可惜被他甩掉了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060424V#043F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060425V#002F#1P居然能把约修亚甩掉，\n',
            '看来那家伙不会是普通人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060426V他到底是什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060427V#015F……不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060428V#010F不过，我想他应该不是\n',
            '纵火烧孤儿院的犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060429V但这也只是我的直觉而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060430V#006F#1P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060431V#007F不过话说回来……\n',
            '为什么要一个人行动啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060432V#043F的确是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060433V至少也应该\n',
            '给我们捎个口信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060434V#013F对不起。\n',
            '让你们为我担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060435V#503F#1P也、也没有特别担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060436V只是想告诉你\n',
            '团队合作的重要性啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060437V#048F呵呵呵，真不坦率。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060438V我看见你刚才\n',
            '明明就是一副很慌乱的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060439V#008F哪、哪有这回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060440V科洛丝你才是呢，\n',
            '刚才一副那～么严肃的表情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060441V#542F那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060442V#019F哈哈……\n',
            '总之谢谢你们两个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(196, 0x00, 0x50)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrDirection(0x0102, 180, 400)
    SetChrDirection(0x0101, 180, 400)
    SetChrDirection(0x0105, 180, 0)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('女性的声音')

    Talk(
        (
            '#1560060443V',
            (TxtCtl.SetColor, 0x5),
            '……现在播送通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1560060444V',
            (TxtCtl.SetColor, 0x5),
            '请舞台剧的演出人员和工作人员\n',
            '马上前往礼堂开始准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1560060445V',
            (TxtCtl.SetColor, 0x5),
            '重复一遍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#1560060446V',
            (TxtCtl.SetColor, 0x5),
            '请舞台剧的演出人员和工作人员\n',
            '马上前往礼堂开始准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010060447V#006F是啊……\n',
            '已经这个时候了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060448V#040F是啊，我想换完服装之后，\n',
            '舞台剧就会马上开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060449V#001F好～啦，\n',
            '终于轮到我们上阵了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060450V#004F#1P啊……\n',
            '那个银发男子怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0105, 135, 0)
    SetChrDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060451V#013F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060452V看来只能通知卡露娜小姐，\n',
            '让她帮我们留意一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们将银发男子的事情告诉卡露娜之后，\n',
            '就接着赶去了礼堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '３０分钟之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ClearMapFlags(0x00000800)
    OP_28(0x003D, 0x01, 0x2000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2523._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xB79
@scena.Code('func_03_B79')
def func_03_B79():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0xBC9
@scena.Code('func_04_BC9')
def func_04_BC9():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 1, 0x4C9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CBF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FE, 1)"),
            Expr.Return,
        ),
        'loc_C41',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0099, 1, 0x4C9))

    Jump('loc_CBC')

    def _loc_C41(): pass

    label('loc_C41')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_CBC(): pass

    label('loc_CBC')

    Jump('loc_CF5')

    def _loc_CBF(): pass

    label('loc_CBF')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0xA2)
    def _loc_CF5(): pass

    label('loc_CF5')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
