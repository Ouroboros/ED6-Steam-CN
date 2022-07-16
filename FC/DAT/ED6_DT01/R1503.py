import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1503_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1503   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '王国军士兵'),
    TXT(0x02, '拉文努山道方向'),
    TXT(0x03, '拉文努山道方向'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1503.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xD51
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
            word_3A         = 59,
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -112680,
            z                   = -50,
            y                   = 21490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -111060,
            z                   = -20,
            y                   = -19200,
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
        ScenaNpcData(
            x                   = 1140,
            z                   = 10,
            y                   = -19200,
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

# id: 0x10003 offset: 0x112
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x112
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -112190,
            y           = -1000,
            z           = 23280,
            range       = -106880,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000619E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x132
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2000,
            triggerZ            = 0,
            triggerY            = 22680,
            triggerRange        = 1700,
            actorX              = 2100,
            actorZ              = 1000,
            actorY              = 23270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -114320,
            triggerZ            = 0,
            triggerY            = 6860,
            triggerRange        = 1500,
            actorX              = -114320,
            actorZ              = 50,
            actorY              = 6860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2180,
            triggerZ            = 0,
            triggerY            = 6860,
            triggerRange        = 1500,
            actorX              = -2180,
            actorZ              = 50,
            actorY              = 6860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x19E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1AA',
    )

    ClearChrFlags(0x0008, 0x0080)

    def _loc_1AA(): pass

    label('loc_1AA')

    Return()

# id: 0x0001 offset: 0x1AB
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1BF'),
        (0x00000065, 'loc_1D9'),
        (0x00000066, 'loc_1D9'),
        (-1, 'loc_1F3'),
    )

    def _loc_1BF(): pass

    label('loc_1BF')

    OP_16(0x02, 4000, -127000, -121000, 196715)
    ClearChrFlags(0x0009, 0x0004)

    Jump('loc_1F3')

    def _loc_1D9(): pass

    label('loc_1D9')

    OP_16(0x02, 4000, -239000, -121000, 196642)
    ClearChrFlags(0x000A, 0x0004)

    Jump('loc_1F3')

    def _loc_1F3(): pass

    label('loc_1F3')

    Return()

# id: 0x0002 offset: 0x1F4
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_209',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_209(): pass

    label('loc_209')

    Return()

# id: 0x0003 offset: 0x20A
@scena.Code('func_03_20A')
def func_03_20A():
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '现在王国军队\n',
            '正在里面进行现场勘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不允许平民进入。\n',
            '当然游击士也包含在内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x267
@scena.Code('func_04_267')
def func_04_267():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 7, 0x31F)),
            Expr.Return,
        ),
        'loc_271',
    )

    Jump('loc_C14')

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 6, 0x31E)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0063, 7, 0x31F))
    OP_28(0x0036, 0x01, 0x0100)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上套着一把结实的挂锁，\n',
            '入口被紧紧地封住了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_323',
    )

    ChrTalk(
        0x0101,
        (
            '#0010021749V#000F好了，赶快用从村长\n',
            '那里借来的钥匙开门吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38A')

    def _loc_323(): pass

    label('loc_323')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_356',
    )

    ChrTalk(
        0x0102,
        (
            '#0020021750V#010F用借来的钥匙吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38A')

    def _loc_356(): pass

    label('loc_356')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030021751V#020F那么，用钥匙试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38A(): pass

    label('loc_38A')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(115, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '废坑的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(110, 0x00, 0x64)
    CameraMove(-110000, 0, 21330, 0)
    SetChrPos(0x0101, -110000, 0, 21330, 0)
    SetChrPos(0x0102, -110700, 0, 20190, 0)
    SetChrPos(0x0103, -109100, 0, 20200, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021752V#007F呼，好结实的门啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021753V#012F那么……\n',
            '我们赶快进去调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021754V#022F空贼就不用说了，\n',
            '这里好像还有魔兽出没的迹象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021755V要集中注意力才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0009, 0x0004)
    OP_16(0x02, 4000, -239000, -121000, 196642)
    ClearChrFlags(0x000A, 0x0004)
    EventEnd(0x00)

    Jump('loc_C14')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_55B',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上套着一把结实的挂锁，\n',
            '入口被紧紧地封住了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_C14')

    def _loc_55B(): pass

    label('loc_55B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_BBD',
    )

    SetScenaFlags(ScenaFlag(0x0063, 5, 0x31D))
    OP_28(0x0036, 0x01, 0x0020)
    OP_28(0x0036, 0x01, 0x0040)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    Fade(1000)
    CameraMove(2610, 0, 22670, 0)
    SetChrPos(0x0101, 2298, 0, 22143, 0)
    SetChrPos(0x0102, 1217, 0, 21146, 0)
    SetChrPos(0x0103, 2841, 0, 20998, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上套着一把结实的挂锁，\n',
            '入口被紧紧地封住了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020021669V#010F这里似乎就是废坑的入口了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021670V#000F#1P确实，这里有着和\n',
            '玛鲁加矿山一样的气氛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021671V相当的荒凉啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021672V#020F这里好像很早以前就被封闭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021673V锁销和锁头都生锈了。\n',
            '没有近期内被打开过的痕迹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021674V#013F也就是说，\n',
            '那些空贼不会从这门进入……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021675V所以军队也就没有调查这里面是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021676V#007F#1P嗯，就算调查矿山里面\n',
            '也应该找不到什么线索…… ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021677V#002F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021678V#023F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 181, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021679V#002F#1P是不是我神经过敏呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021680V从里面，好像有风吹过来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021681V#023F里面？是从废坑的里面？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021682V#002F#1P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021683V#012F等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08A6')
    def lambda_08A6():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_08A6')

    DispatchAsync2(0x0101, 0x0001, lambda_08A6)

    ChrWalkTo(0x0102, 1200, 0, 22670, 2000, 0x00)
    TerminateThread(0x0101, 0xFF)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚把食指放在口中吮了一下，\n',
            '然后竖在门边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020021684V#015F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0102,
        (
            '#0020021685V#014F真的……\n',
            '虽然很微弱，但确实有风过吹来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021686V#501F#1P啊，没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09BC')
    def lambda_09BC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09BC)

    ChrTalk(
        0x0103,
        (
            '#0030021687V#023F你呀，时不时地让人吃一惊，\n',
            '感觉还真是敏锐呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021688V#021F真不愧是老师的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021689V#007F#1P这和老爸才没有关系呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021690V#006F不过这里面……\n',
            '你们不觉得有点可疑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021691V#010F是啊，\n',
            '也许这里能通向哪里也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021692V看起来有调查一下的价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021693V#001F#1P好了，就这么决定，\n',
            '我们赶快把锁给砸开……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021694V#025F喂喂，先别急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021695V#020F总之还是先回村子\n',
            '和村长商量一下再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021696V说不定他有钥匙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021697V#007F#1P唉～真是遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_C14')

    def _loc_BBD(): pass

    label('loc_BBD')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上套着一把结实的挂锁，\n',
            '入口被紧紧地封住了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_C14(): pass

    label('loc_C14')

    Return()

# id: 0x0005 offset: 0xC15
@scena.Code('func_05_C15')
def func_05_C15():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_D05',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0008, 0x0000, 400)
    OP_4A(0x0008, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C82',
    )

    ChrTalk(
        0x0008,
        (
            '#2490030254V我不是说了禁止入内吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2490030255V你们想被关进\n',
            '哈肯门的地下牢吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD8')

    def _loc_C82(): pass

    label('loc_C82')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#2490030256V喂，那边禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2490030257V如果不遵从命令的话\n',
            '可是会遭到逮捕的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD8(): pass

    label('loc_CD8')

    @scena.Lambda('lambda_0CDE')
    def lambda_0CDE():
        SetChrDirection(0x0008, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CDE)

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x0008, 255)

    def _loc_D05(): pass

    label('loc_D05')

    Return()

# id: 0x0006 offset: 0xD06
@scena.Code('func_06_D06')
def func_06_D06():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉文努矿山',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
