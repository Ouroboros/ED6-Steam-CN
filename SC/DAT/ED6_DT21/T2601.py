import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2601   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2601.x'
    header.mapIndex       = 1
    header.bgm            = 32
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
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡片',
            x                   = 0,
            z                   = 1000,
            y                   = 8450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589824,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王立学院·小道',
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

# id: 0x10002 offset: 0x102
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x102
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x102
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 24940,
            triggerZ            = 5000,
            triggerY            = 24830,
            triggerRange        = 800,
            actorX              = 24940,
            actorZ              = 5000,
            actorY              = 24830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33200,
            triggerZ            = 0,
            triggerY            = 14520,
            triggerRange        = 1000,
            actorX              = 32570,
            actorZ              = 0,
            actorY              = 14530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x14A
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_156'),
        (-1, 'loc_16A'),
    )

    def _loc_156(): pass

    label('loc_156')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 4, 0x1224)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_167',
    )

    MapSetFlags(0x10000000)
    Event(0, func_03_2F1)

    def _loc_167(): pass

    label('loc_167')

    Jump('loc_16A')

    def _loc_16A(): pass

    label('loc_16A')

    Return()

# id: 0x0001 offset: 0x16B
@scena.Code('func_01_16B')
def func_01_16B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 0, 0x1340)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D',
    )

    OP_6F(0x0002, 0)

    Jump('loc_184')

    def _loc_17D(): pass

    label('loc_17D')

    OP_6F(0x0002, 60)

    def _loc_184(): pass

    label('loc_184')

    OP_16(0x02, 4000, -128000, -106000, 2293838)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 6, 0x1226)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 7, 0x1227)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1A6',
    )

    OP_64(0x00, 0x0001)

    def _loc_1A6(): pass

    label('loc_1A6')

    Return()

# id: 0x0002 offset: 0x1A7
@scena.Code('func_02_1A7')
def func_02_1A7():
    UnlockAchievement(0x02, 0x01FD, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0268, 0, 0x1340)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 30)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddSepith(0x00, 10)
    AddSepith(0x01, 10)
    AddSepith(0x02, 10)
    AddSepith(0x03, 10)
    AddSepith(0x04, 10)
    AddSepith(0x05, 10)
    AddSepith(0x06, 10)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0268, 0, 0x1340))

    Jump('loc_2DF')

    def _loc_2C5(): pass

    label('loc_2C5')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_2DF(): pass

    label('loc_2DF')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x2F1
@scena.Code('func_03_2F1')
def func_03_2F1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_302',
    )

    Call(0, 0x000A)

    def _loc_302(): pass

    label('loc_302')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, 210, 0, -7580, 0)
    ChrSetPos(0x0105, 940, 0, -9530, 0)
    ChrSetPos(0x00F7, -1100, 0, -10140, 0)
    ChrSetPos(0x0104, 800, 0, -11070, 0)
    ChrSetPos(0x0127, -680, 0, -11530, 0)
    CameraMove(340, 1000, 10340, 0)
    OP_67(0, 9440, -10000, 0)
    CameraSetDistance(6060, 0)
    OP_6C(36000, 0)
    OP_6E(262, 0)
    OP_12(0x00009470, 0x0002BF20, 0x00000000)
    OP_72(0x0003, 0x0004)
    OP_C8(0x0200, 0x0046, 'C_PLAC07._CH', 0x00, 0x07D0)
    ShowPlaceName('旧校舍')
    FadeIn(2000, 0)

    @scena.Lambda('lambda_03D9')
    def lambda_03D9():
        CameraMove(350, 0, 2160, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03D9)

    @scena.Lambda('lambda_03F1')
    def lambda_03F1():
        OP_67(0, 9440, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03F1)

    @scena.Lambda('lambda_0409')
    def lambda_0409():
        ChrWalkTo(0x00FE, 1130, 0, 1270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0409)

    Sleep(200)

    @scena.Lambda('lambda_0429')
    def lambda_0429():
        ChrWalkTo(0x00FE, -680, 0, -20, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0429)

    Sleep(200)

    @scena.Lambda('lambda_0449')
    def lambda_0449():
        ChrWalkTo(0x00FE, 1180, 0, -390, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0449)

    @scena.Lambda('lambda_0464')
    def lambda_0464():
        ChrWalkTo(0x00FE, -40, 0, -1070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_0464)

    Sleep(200)

    @scena.Lambda('lambda_0484')
    def lambda_0484():
        ChrWalkTo(0x00FE, 210, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0484)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0127, 0x0001)
    Fade(1000)
    CameraMove(210, 0, 1760, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_52C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211454V#057F#6P原来如此……\n',
            '这就是旧校舍吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_563')

    def _loc_52C(): pass

    label('loc_52C')

    ChrTalk(
        0x0103,
        (
            '#0030211455V#027F#6P原来如此……\n',
            '这就是旧校舍啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_563(): pass

    label('loc_563')

    ChrTalk(
        0x0104,
        (
            '#0040211456V#031F#2P呵呵……\n',
            '挺像那么回事的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211457V毫无疑问，\n',
            '都让人毛骨悚然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211458V#151F哈哈哈……\n',
            '都起鸡皮疙瘩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0127, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211459V#1019F看起来觉得\n',
            '一点也不恐怖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060211460V#044F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211461V#1004F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211462V#043F艾丝蒂尔，门前……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    @scena.Lambda('lambda_06E1')
    def lambda_06E1():
        CameraMove(0, 1000, 8010, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_06E1)

    @scena.Lambda('lambda_06F9')
    def lambda_06F9():
        OP_67(0, 8000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_06F9)

    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0737')
    def lambda_0737():
        CameraMove(0, 1000, 9000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0737)

    @scena.Lambda('lambda_074F')
    def lambda_074F():
        OP_67(0, 8000, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_074F)

    CreateThread(0x0101, 0x01, 0x00, func_04_D42)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x00, func_05_D57)
    Sleep(200)

    CreateThread(0x00F7, 0x01, 0x00, func_06_D73)
    Sleep(200)

    CreateThread(0x0104, 0x01, 0x00, func_07_DA3)
    Sleep(100)

    CreateThread(0x0127, 0x01, 0x00, func_08_DB8)
    WaitForThreadExit(0x0127, 0x0001)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010211463V#1002F#6P这是……卡片？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211464V好像写着什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraSetDistance(2780, 1000)
    Fade(250)
    OP_71(0x0003, 0x0004)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170211465V　　不速之客啊\n',
            '欢迎来到我暂住之所',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211466V若不畏惧千年的诅咒\n',
            '就来到我面前吧',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170211467V　第一个诅咒在大厅\n',
            '　目标是『虚无之炎』',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    LoadEffect(0x00, 'map\\\\mpfire6.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -150, 1700, 9440, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(134, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#1K#1020F#6P哇哇……！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060211469V#1K#043F#2P呀……！',
            TxtCtl.Enter,
        ),
    )

    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_09B4')
    def lambda_09B4():
        ChrMoveTo(0x0105, 700, 1000, 8330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_09B4)

    ChrMoveTo(0x0101, -220, 1000, 8470, 2000, 0x00)
    Sleep(500)

    OP_56(0x01)
    OP_59()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡片突然着火烧没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A5A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211470V#055F#6P怎、怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A82')

    def _loc_A5A(): pass

    label('loc_A5A')

    ChrTalk(
        0x0103,
        (
            '#0030211471V#023F#6P什、什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A82(): pass

    label('loc_A82')

    ChrTalk(
        0x0127,
        (
            '#0280211472V#154F#6P搞不好是\n',
            '自燃现象～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211473V闹鬼的时候\n',
            '好像常常发生～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211474V#035F#4P唔……\n',
            '相当有挑战性的幽灵呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211475V给我们设下了谜题吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211476V#1005F#6P正、正合我意！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211477V可别小看\n',
            '活着的人哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C1E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211478V#6P#051F逞强逞到\n',
            '这个地步也不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211479V#053F话说回来……\n',
            '『目标是虚无之炎』对吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8E')

    def _loc_C1E(): pass

    label('loc_C1E')

    ChrTalk(
        0x0103,
        (
            '#0030211480V#6P#020F逞强能逞到\n',
            '这个地步也算不错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211481V#026F话说回来……\n',
            '『目标是虚无之炎』对吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C8E(): pass

    label('loc_C8E')

    ChrTurnDirection(0x0105, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060211482V#042F#2P『大厅』应该是\n',
            '指进了这扇门\n',
            '之后的大门厅吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211483V看来有必要调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211484V#1002F#6P嗯、嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0244, 4, 0x1224))
    OP_28(0x0084, 0x01, 0x0001)
    OP_28(0x0084, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xD42
@scena.Code('func_04_D42')
def func_04_D42():
    ChrWalkTo(0x00FE, -240, 1000, 9000, 5000, 0x00)

    Return()

# id: 0x0005 offset: 0xD57
@scena.Code('func_05_D57')
def func_05_D57():
    ChrWalkTo(0x00FE, 620, 1000, 8410, 5000, 0x00)
    ChrSetDirection(0x00FE, 327, 400)

    Return()

# id: 0x0006 offset: 0xD73
@scena.Code('func_06_D73')
def func_06_D73():
    ChrWalkTo(0x00FE, -960, 1000, 6400, 5000, 0x00)
    ChrWalkTo(0x00FE, -1930, 1000, 7980, 5000, 0x00)
    ChrSetDirection(0x00FE, 42, 400)

    Return()

# id: 0x0007 offset: 0xDA3
@scena.Code('func_07_DA3')
def func_07_DA3():
    ChrWalkTo(0x00FE, -360, 1000, 6650, 5000, 0x00)

    Return()

# id: 0x0008 offset: 0xDB8
@scena.Code('func_08_DB8')
def func_08_DB8():
    ChrWalkTo(0x00FE, -960, 1000, 6400, 5000, 0x00)
    ChrWalkTo(0x00FE, -1830, 1000, 6810, 5000, 0x00)
    ChrSetDirection(0x00FE, 30, 400)

    Return()

# id: 0x0009 offset: 0xDE8
@scena.Code('func_09_DE8')
def func_09_DE8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E02',
    )

    Call(0, 0x000A)
    FadeIn(0, 0)

    def _loc_E02(): pass

    label('loc_E02')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 23920, 5000, 25980, 135)
    ChrSetPos(0x00F7, 24140, 5000, 24250, 104)
    ChrSetPos(0x0105, 25000, 5000, 26400, 180)
    ChrSetPos(0x0104, 26660, 5000, 24580, 261)
    ChrSetPos(0x0127, 25940, 5000, 23050, 345)
    CameraMove(23920, 5000, 25980, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060211505V#040F#2P『庭园』的『落下的头』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211506V感觉似乎附和条件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211507V#1006F嗯……\n',
            '我想大概没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '石质的箱形花盆中\n',
            '放着卡片和旧钥匙',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(300)

    Fade(250)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS127._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170211508V此刻诅咒即将实现\n',
            '通过最后的试炼\n',
            '立刻来到我面前',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    LoadEffect(0x00, 'map\\\\mpfire6.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 24440, 5900, 25460, 0, 0, 0, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    PlaySE(134, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(1000)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡片突然着火烧没了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['旧钥匙']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['旧钥匙'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010211509V#1007F看来谜题到这里就结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211510V#1019F『诅咒实现』，\n',
            '感觉真是不爽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211511V#035F呵，无论如何，\n',
            '都要用那个钥匙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211512V#030F去找找与之相符的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(23920, 5000, 25980, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 23920, 5000, 25980, 135)
    ChrSetPos(0x00F7, 23920, 5000, 25980, 135)
    ChrSetPos(0x0105, 23920, 5000, 25980, 135)
    ChrSetPos(0x0104, 23920, 5000, 25980, 135)
    ChrSetPos(0x0127, 23920, 5000, 25980, 135)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0244, 7, 0x1227))
    OP_28(0x0084, 0x01, 0x0010)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x1263
@scena.Code('func_0A_1263')
def func_0A_1263():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_12DD'),
        (0x00000001, 'loc_12E3'),
        (-1, 'loc_12E9'),
    )

    def _loc_12DD(): pass

    label('loc_12DD')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_12E9')

    def _loc_12E3(): pass

    label('loc_12E3')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_12E9')

    def _loc_12E9(): pass

    label('loc_12E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_12F7',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_12FB')

    def _loc_12F7(): pass

    label('loc_12F7')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_12FB(): pass

    label('loc_12FB')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
