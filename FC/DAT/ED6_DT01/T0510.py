import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0510   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0510.x'
    header.mapIndex       = 18
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0510._SN', 'ED6_DT01/T0510_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00005DC0,
            dword_04        = 0x00000000,
            dword_08        = 0x0000CB20,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 18,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00005E24,
            dword_04        = 0x00000000,
            dword_08        = 0x0000DB88,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 18,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00005E24,
            dword_04        = 0x00000000,
            dword_08        = 0x0000DB88,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 18,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0x130
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿斯顿队长',
            x                   = 29850,
            z                   = 0,
            y                   = -73420,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '戴恩副长',
            x                   = 26800,
            z                   = 0,
            y                   = 29900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 28310,
            triggerZ            = 0,
            triggerY            = -73420,
            triggerRange        = 500,
            actorX              = 29850,
            actorZ              = 1500,
            actorY              = -73420,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28250,
            triggerZ            = 0,
            triggerY            = 29800,
            triggerRange        = 500,
            actorX              = 26800,
            actorZ              = 1500,
            actorY              = 29900,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 20640,
            triggerZ            = 0,
            triggerY            = 33000,
            triggerRange        = 1000,
            actorX              = 20640,
            actorZ              = 1000,
            actorY              = 33000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x20E
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_21A'),
        (-1, 'loc_232'),
    )

    def _loc_21A(): pass

    label('loc_21A')

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_22F',
    )

    OP_28(0x0008, 0x02, 0x4000)
    Event(1, 0x0001)

    def _loc_22F(): pass

    label('loc_22F')

    Jump('loc_232')

    def _loc_232(): pass

    label('loc_232')

    Return()

# id: 0x0001 offset: 0x233
@scena.Code('func_01_233')
def func_01_233():
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x27D
@scena.Code('func_02_27D')
def func_02_27D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_292',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_27D')

    def _loc_292(): pass

    label('loc_292')

    Return()

# id: 0x0003 offset: 0x293
@scena.Code('func_03_293')
def func_03_293():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x298
@scena.Code('func_04_298')
def func_04_298():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_A0D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 3, 0x303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_353',
    )

    EventBegin(0x00)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x000A,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000A, 1000)

    ChrTalk(
        0x0008,
        (
            '#1130020256V艾丝蒂尔……\n',
            '啊，约修亚也来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020257V#000F阿斯顿队长，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 1, 0x281)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E9',
    )

    SetScenaFlags(ScenaFlag(0x0050, 1, 0x281))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0102,
        (
            '#0020020258V#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020259V啊啊，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020260V我都听说了，\n',
            '我家的鲁克给你们添了很多麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020261V作为父亲，真是感到惭愧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020262V#001F没事，像他这种年纪的男孩子\n',
            '喜欢恶作剧也是没有办法的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020263V就算是我，\n',
            '小的时候也经常到城镇外面乱跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020264V#017F你不是女孩子吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020265V哈哈，还是这么精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E9(): pass

    label('loc_4E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 3, 0x303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_99A',
    )

    ChrTalk(
        0x0008,
        (
            '#1130020266V那边的那位……\n',
            '不就是雪拉扎德小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020267V#020F你好啊，队长先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020268V这次是来向你申请\n',
            '往柏斯地区的通行许可证的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020269V不会是……\n',
            '和之前发生的那个事件有关吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020270V#003F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '众人说明了关于卡西乌斯乘坐了\n',
            '行踪不明的定期船的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#1130020271V怎么会，卡西乌斯先生他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020272V这可是件大事。\n',
            '这就给你们办理通行许可证吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0008)
    Sleep(500)

    ChrTurnDirection(0x0008, 0x0000, 400)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    AddItem(0x032F, 1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '通行许可证',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010020273V#001F谢谢，阿斯顿队长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020274V#000F可是，这就行了？\n',
            '这么简单就办理了通行许可证……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020275V没什么，都是熟人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020276V而且，作为王国军，\n',
            '也应该鼎力协助游击士协会才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020277V啊，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020278V#004F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020279V……要是到北边的哈肯门去的话，\n',
            '有件事需要你们注意一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020280V到那里的时候\n',
            '最好还是隐瞒自己游击士的身份。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020281V#012F为什么这么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020282V不好意思，\n',
            '我不能再往下说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020283V总之，要是你们打算调查这件事的话，\n',
            '行动的时候还是谨慎点比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1130020284V我也会向空之女神\n',
            '祈祷卡西乌斯先生平安归来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    SetScenaFlags(ScenaFlag(0x0060, 3, 0x303))

    Jump('loc_A0A')

    def _loc_99A(): pass

    label('loc_99A')

    ChrTalk(
        0x0008,
        (
            '要是你们打算调查这件事的话，\n',
            '行动的时候还是谨慎点比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我也会向空之女神\n',
            '祈祷卡西乌斯先生平安归来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A0A(): pass

    label('loc_A0A')

    Jump('loc_14D6')

    def _loc_A0D(): pass

    label('loc_A0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_E90',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 1, 0x281)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C61',
    )

    SetScenaFlags(ScenaFlag(0x0050, 1, 0x281))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0008,
        (
            '哦哦，\n',
            '这不是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F阿斯顿队长，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊啊，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我都听说了，\n',
            '我家的鲁克给你们添了不少麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '作为父亲，真是感到惭愧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F没事，像他这种年纪的男孩子\n',
            '喜欢恶作剧也是没有办法的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F就算是我，\n',
            '小的时候也经常到城镇外面乱跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#017F你不是女孩子吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，还是这么精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说起来，\n',
            '听说柏斯地区相继\n',
            '发生了多宗的盗窃案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F柏斯？\n',
            '真是多事之秋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，这下我们守备队\n',
            '也必须提高警惕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是总觉得\n',
            '我的部下紧张感不足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真伤脑筋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DA5')

    def _loc_C61(): pass

    label('loc_C61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CEA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '最近柏斯地区\n',
            '接连发生了强盗事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们守备队\n',
            '也必须提高警惕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是总觉得\n',
            '我的部下紧张感不足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D46')

    def _loc_CEA(): pass

    label('loc_CEA')

    ChrTalk(
        0x0008,
        (
            '柏斯发生了空贼事件，\n',
            '我们守备队必须提高警惕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是总觉得\n',
            '我的部下紧张感不足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D46(): pass

    label('loc_D46')

    Jump('loc_DA5')

    def _loc_D49(): pass

    label('loc_D49')

    ChrTalk(
        0x0008,
        (
            '柏斯发生了空贼事件，\n',
            '我们守备队必须提高警惕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是总觉得\n',
            '我的部下紧张感不足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DA5(): pass

    label('loc_DA5')

    Jump('loc_E8D')

    def _loc_DA8(): pass

    label('loc_DA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E37',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '最近柏斯地区好像\n',
            '接连发生了强盗事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们在这里也\n',
            '丝毫不能掉以轻心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望部下们能够\n',
            '活用在训练中取得的经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E8D')

    def _loc_E37(): pass

    label('loc_E37')

    ChrTalk(
        0x0008,
        (
            '柏斯地区好像\n',
            '接连发生了强盗事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望部下们能够\n',
            '活用在训练中取得的经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E8D(): pass

    label('loc_E8D')

    Jump('loc_14D6')

    def _loc_E90(): pass

    label('loc_E90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_107B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EB1',
    )

    Call(1, 0x0000)

    Jump('loc_1078')

    def _loc_EB1(): pass

    label('loc_EB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F1C',
    )

    ChrTalk(
        0x0008,
        (
            '能站在对方的角度去思考，\n',
            '就可以非常的客观公正了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望你们能够在今后的舞台中大展身手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1078')

    def _loc_F1C(): pass

    label('loc_F1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1005',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '训练辛苦了。\n',
            '对士兵们应该是一剂强心剂啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不好意思，你们在城里的时候，\n',
            '帮我看着点鲁克那小子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那家伙从一生出来\n',
            '就不是一个听话的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我母亲拿他\n',
            '也没什么办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '或许我应该\n',
            '更加严厉地管教他才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1078')

    def _loc_1005(): pass

    label('loc_1005')

    ChrTalk(
        0x0008,
        (
            '鲁克那小子\n',
            '真不是一个听话的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我母亲拿他\n',
            '也没什么办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不好意思，\n',
            '今后请你们也多照顾一下鲁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1078(): pass

    label('loc_1078')

    Jump('loc_14D6')

    def _loc_107B(): pass

    label('loc_107B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_11FF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_109C',
    )

    Call(1, 0x0000)

    Jump('loc_11FC')

    def _loc_109C(): pass

    label('loc_109C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1107',
    )

    ChrTalk(
        0x0008,
        (
            '能站在对方的角度去思考，\n',
            '就可以非常的客观公正了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望你们能够在今后的舞台中大展身手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FC')

    def _loc_1107(): pass

    label('loc_1107')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11A2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '从新进士兵的态度来看，\n',
            '他们似乎感到非常不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这次的训练好像让他们\n',
            '找回点紧张感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，今后也有必要\n',
            '对他们进行严厉地锻炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FC')

    def _loc_11A2(): pass

    label('loc_11A2')

    ChrTalk(
        0x0008,
        (
            '这次的训练好像让士兵们\n',
            '找回点紧张感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，今后也有必要\n',
            '对他们进行严厉地锻炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FC(): pass

    label('loc_11FC')

    Jump('loc_14D6')

    def _loc_11FF(): pass

    label('loc_11FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_14D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13F7',
    )

    SetScenaFlags(ScenaFlag(0x0050, 1, 0x281))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '哦哦，\n',
            '这不是艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F阿斯顿队长，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊啊，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我都听说了，\n',
            '我家的鲁克给你们添了不少麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '作为父亲，真是感到惭愧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F没事，像他这种年纪的男孩子\n',
            '喜欢恶作剧也是没有办法的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F就算是我，\n',
            '小的时候也经常到城镇外面乱跑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#017F你不是女孩子吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，还是这么精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说实话，\n',
            '我也想早点回洛连特去\n',
            '和家人团聚啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过来这里接任的时间还很短。\n',
            '要做的事情还有很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D6')

    def _loc_13F7(): pass

    label('loc_13F7')

    ChrTalk(
        0x0008,
        (
            '在１０年前的战争中，\n',
            '关所在封锁帝国军各部队的战斗上\n',
            '起了非常重要的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然现在通行的人很少，\n',
            '但是守备也绝不能马虎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是，\n',
            '这里的新进士兵态度实在是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '既然我来到这里了，\n',
            '就有必要进行一次严格的训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14D6(): pass

    label('loc_14D6')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x14DA
@scena.Code('func_05_14DA')
def func_05_14DA():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x14DF
@scena.Code('func_06_14DF')
def func_06_14DF():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_15AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_157A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '听说失踪的定期船\n',
            '已经被发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像是情报部和国境守备队\n',
            '联合起来解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真～是的，\n',
            '这下终于能够恢复普通执勤了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A9')

    def _loc_157A(): pass

    label('loc_157A')

    ChrTalk(
        0x0009,
        (
            '真～是的，\n',
            '这下终于能够恢复普通执勤了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A9(): pass

    label('loc_15A9')

    Jump('loc_1AB0')

    def _loc_15AC(): pass

    label('loc_15AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_16A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1658',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '虽然消息还没有确认，\n',
            '但听说不仅是国境守备队，\n',
            '连新设的情报部也出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，这样拖延下去，\n',
            '也关系到军队的威严啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望他们能好好加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16A6')

    def _loc_1658(): pass

    label('loc_1658')

    ChrTalk(
        0x0009,
        (
            '虽然消息还没有确认，\n',
            '但是听说不仅是国境守备队，\n',
            '连新设的情报部也出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16A6(): pass

    label('loc_16A6')

    Jump('loc_1AB0')

    def _loc_16A9(): pass

    label('loc_16A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_178E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_173B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '行踪不明的定期船\n',
            '终于被发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但是，\n',
            '还是没有收到解除盘查的命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这是怎么一回事呢。\n',
            '我想要情报啊，情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178B')

    def _loc_173B(): pass

    label('loc_173B')

    ChrTalk(
        0x0009,
        (
            '行踪不明的定期船\n',
            '终于被发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '但是，\n',
            '还是没有收到解除盘查的命令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178B(): pass

    label('loc_178B')

    Jump('loc_1AB0')

    def _loc_178E(): pass

    label('loc_178E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_18B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1863',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '说起来，\n',
            '定期船竟然整个消失不见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是无奇不有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么庞大的家伙，\n',
            '应该能够马上就发现的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就算是摩尔根将军，\n',
            '这次也遇到难题了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊呀，\n',
            '说这种话要被队长骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18B5')

    def _loc_1863(): pass

    label('loc_1863')

    ChrTalk(
        0x0009,
        (
            '就算是摩尔根将军，\n',
            '这次也遇到难题了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊呀，\n',
            '说这种话要被队长骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18B5(): pass

    label('loc_18B5')

    Jump('loc_1AB0')

    def _loc_18B8(): pass

    label('loc_18B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1957',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1927',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '好像只是解除了\n',
            '钢壁之路的封锁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而且不是因为找到了定期船，\n',
            '那到底发生了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1954')

    def _loc_1927(): pass

    label('loc_1927')

    ChrTalk(
        0x0009,
        (
            '还有，\n',
            '定期船到底什么时候能恢复航行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1954(): pass

    label('loc_1954')

    Jump('loc_1AB0')

    def _loc_1957(): pass

    label('loc_1957')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1A5E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19FB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '说起来，\n',
            '不仅禁止了全地区的飞行，\n',
            '而且连钢壁之路都封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看来这次可要来大手笔的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可以看出国境守备队的那些人\n',
            '也非常焦急呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5B')

    def _loc_19FB(): pass

    label('loc_19FB')

    ChrTalk(
        0x0009,
        (
            '说起来，\n',
            '不仅禁止了全地区的飞行，\n',
            '而且连钢壁之路都封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看来这次可要来大手笔的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A5B(): pass

    label('loc_1A5B')

    Jump('loc_1AB0')

    def _loc_1A5E(): pass

    label('loc_1A5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1AB0',
    )

    ChrTalk(
        0x0009,
        (
            '哦，这次是游击士吗？\n',
            '步行过来还真是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AB0(): pass

    label('loc_1AB0')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1AB4
@scena.Code('func_07_1AB4')
def func_07_1AB4():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CCD',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 50)
    OP_73(0x0001)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    ChrSetPos(0x0000, 21970, 0, 33230, 269)
    ChrSetPos(0x0001, 21970, 0, 33230, 269)
    ChrSetPos(0x0002, 21970, 0, 33230, 269)
    ChrSetPos(0x0003, 21970, 0, 33230, 269)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_1CCD(): pass

    label('loc_1CCD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CE7',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_1CE7(): pass

    label('loc_1CE7')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
