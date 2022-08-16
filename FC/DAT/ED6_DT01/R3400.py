import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3400.x'
    header.mapIndex       = 1
    header.bgm            = 30
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
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT09/CH10760._CH', 'ED6_DT09/CH10760P._CP'),
        ('ED6_DT09/CH10761._CH', 'ED6_DT09/CH10761P._CP'),
        ('ED6_DT09/CH10770._CH', 'ED6_DT09/CH10770P._CP'),
        ('ED6_DT09/CH10771._CH', 'ED6_DT09/CH10771P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾尔·雷登关所方向',
            x                   = -26110,
            z                   = -20,
            y                   = -38940,
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
            name                = '蔡斯方向',
            x                   = 189780,
            z                   = -20,
            y                   = -27490,
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

# id: 0x10002 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 45900,
            z           = 20,
            y           = -46160,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 40140,
            z           = -10,
            y           = -13510,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 121900,
            z           = -40,
            y           = -57020,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 115250,
            z           = 10,
            y           = -35350,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
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
        ScenaActorData(
            triggerX            = 19790,
            triggerZ            = 0,
            triggerY            = -14460,
            triggerRange        = 1000,
            actorX              = 19250,
            actorZ              = 10,
            actorY              = -15050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 55120,
            triggerZ            = -70,
            triggerY            = 8740,
            triggerRange        = 1000,
            actorX              = 55870,
            actorZ              = -70,
            actorY              = 8740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 19690,
            triggerZ            = -90,
            triggerY            = 11550,
            triggerRange        = 1000,
            actorX              = 19240,
            actorZ              = -90,
            actorY              = 11060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 124260,
            triggerZ            = -30,
            triggerY            = -53650,
            triggerRange        = 1000,
            actorX              = 124760,
            actorZ              = -30,
            actorY              = -53160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x22A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_238',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_2B0)

    def _loc_238(): pass

    label('loc_238')

    Return()

# id: 0x0001 offset: 0x239
@scena.Code('func_01_239')
def func_01_239():
    OP_16(0x02, 4000, -45000, -151000, 196663)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 2, 0x592)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25D',
    )

    OP_6F(0x000E, 0)

    Jump('loc_264')

    def _loc_25D(): pass

    label('loc_25D')

    OP_6F(0x000E, 60)

    def _loc_264(): pass

    label('loc_264')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 3, 0x593)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_276',
    )

    OP_6F(0x000F, 0)

    Jump('loc_27D')

    def _loc_276(): pass

    label('loc_276')

    OP_6F(0x000F, 60)

    def _loc_27D(): pass

    label('loc_27D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 4, 0x594)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28F',
    )

    OP_6F(0x0010, 0)

    Jump('loc_296')

    def _loc_28F(): pass

    label('loc_28F')

    OP_6F(0x0010, 60)

    def _loc_296(): pass

    label('loc_296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 5, 0x595)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A8',
    )

    OP_6F(0x0011, 0)

    Jump('loc_2AF')

    def _loc_2A8(): pass

    label('loc_2A8')

    OP_6F(0x0011, 60)

    def _loc_2AF(): pass

    label('loc_2AF')

    Return()

# id: 0x0002 offset: 0x2B0
@scena.Code('func_02_2B0')
def func_02_2B0():
    EventBegin(0x00)
    CameraMove(-11200, 0, -38700, 0)
    OP_6C(45000, 0)
    CameraSetDistance(2600, 0)
    OP_B8(0x04)
    FormationDelMember(0x04, 0xFF)
    ChrSetPos(0x0101, -13400, 0, -38700, 0)
    ChrSetPos(0x0102, -15200, 0, -39000, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_030B')
    def lambda_030B():
        CameraMove(5400, -20, -39270, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_030B)

    @scena.Lambda('lambda_0323')
    def lambda_0323():
        ChrWalkTo(0x00FE, 7040, -20, -39240, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0323)

    ChrWalkTo(0x0102, 4630, -20, -39200, 3000, 0x00)
    ChrSetDirection(0x0102, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020070334V#014F……………………………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    ChrWalkTo(0x0101, 6040, -20, -39240, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010070335V#004F怎么了，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070336V#012F没什么……\n',
            '感觉好像有什么人过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070337V#501F哎？除了我们之外，\n',
            '还有其他人要通过这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(2400, -20, -39270, 1500)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x0101)
    OP_63(0x0102)

    ChrTalk(
        0x0101,
        (
            '#0010070338V#000F……谁也没来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070339V#015F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04D6')
    def lambda_04D6():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04D6)

    CameraMove(5400, -20, -39270, 1200)

    ChrTalk(
        0x0102,
        (
            '#0020070340V#010F看来是我弄错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070341V#004F啊，我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070342V#507F约修亚也真是的～\n',
            '还对科洛丝恋恋不舍啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070343V#014F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070344V你在说什么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070345V#502F别害羞、别害羞。\n',
            '姐姐我可是很明白你的心情哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070346V#503F不、不过也难怪嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070347V虽说只是演戏性质，\n',
            '但已经亲密到接吻的地步了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070348V#014F………哎………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070349V#008F还有什么想说的情话，\n',
            '现在回去找她还来得及哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070350V我想应该会有满意的回应吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070351V#014F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070352V#017F……难道说\n',
            '那天你完全没发现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070353V#004F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070354V没发现什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070355V#017F就是说，最后那个场景啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070356V#018F那是假装的啊，假的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070357V角度刚好错开了，\n',
            '从旁边看去当然像真的那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070358V#002F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070359V……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010070360V#005F#5S你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 100, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070361V#017F受不了你了，\n',
            '到现在也还是那么粗心大意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070362V剧本的注释上\n',
            '不是也写得清清楚楚的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070363V#008F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070364V是吗，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 0, 800)
    ChrSetDirection(0x0101, 90, 800)

    ChrTalk(
        0x0101,
        (
            '#0010070365V#503F（哎呀！我真是的……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070366V（怎么会感觉\n',
            '　这样反而松了口气呢～！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020070367V#014F怎么了……艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070368V你没发烧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 20, 0, 400, 4000)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 0, 800)
    ChrSetDirection(0x0101, 270, 800)

    ChrTalk(
        0x0101,
        (
            '#0010070369V#001F啊哈哈！没、没事啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070370V好了啦，\n',
            '马上出发去蔡斯吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0xAED
@scena.Code('func_03_AED')
def func_03_AED():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 2, 0x592)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BDD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000E, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_B63',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B2, 2, 0x592))

    Jump('loc_BDA')

    def _loc_B63(): pass

    label('loc_B63')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000E, 60)
    OP_70(0x000E, 0)

    def _loc_BDA(): pass

    label('loc_BDA')

    Jump('loc_C13')

    def _loc_BDD(): pass

    label('loc_BDD')

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
    WaitEffect(0x0F, 0x9B)
    def _loc_C13(): pass

    label('loc_C13')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0xC21
@scena.Code('func_04_C21')
def func_04_C21():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 3, 0x593)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D11',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FB, 1)"),
            Expr.Return,
        ),
        'loc_C97',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '痊愈之药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B2, 3, 0x593))

    Jump('loc_D0E')

    def _loc_C97(): pass

    label('loc_C97')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '痊愈之药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '痊愈之药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_D0E(): pass

    label('loc_D0E')

    Jump('loc_D47')

    def _loc_D11(): pass

    label('loc_D11')

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
    WaitEffect(0x0F, 0x9C)
    def _loc_D47(): pass

    label('loc_D47')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xD55
@scena.Code('func_05_D55')
def func_05_D55():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 4, 0x594)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E45',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0010, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_DCB',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B2, 4, 0x594))

    Jump('loc_E42')

    def _loc_DCB(): pass

    label('loc_DCB')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0010, 60)
    OP_70(0x0010, 0)

    def _loc_E42(): pass

    label('loc_E42')

    Jump('loc_E7B')

    def _loc_E45(): pass

    label('loc_E45')

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
    WaitEffect(0x0F, 0x9D)
    def _loc_E7B(): pass

    label('loc_E7B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xE89
@scena.Code('func_06_E89')
def func_06_E89():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 5, 0x595)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F79',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0011, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0287, 1)"),
            Expr.Return,
        ),
        'loc_EFF',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B2, 5, 0x595))

    Jump('loc_F76')

    def _loc_EFF(): pass

    label('loc_EFF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0)

    def _loc_F76(): pass

    label('loc_F76')

    Jump('loc_FAF')

    def _loc_F79(): pass

    label('loc_F79')

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
    WaitEffect(0x0F, 0x9E)
    def _loc_FAF(): pass

    label('loc_FAF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
