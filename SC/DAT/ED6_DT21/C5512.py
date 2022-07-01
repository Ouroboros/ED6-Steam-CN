import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5512_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5512   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5512.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C5511._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xABE
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
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT29/CH12180._CH', 'ED6_DT29/CH12180P._CP'),
        ('ED6_DT29/CH12181._CH', 'ED6_DT29/CH12181P._CP'),
        ('ED6_DT29/CH12230._CH', 'ED6_DT29/CH12230P._CP'),
        ('ED6_DT29/CH12231._CH', 'ED6_DT29/CH12231P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
        ('ED6_DT29/CH12360._CH', 'ED6_DT29/CH12360P._CP'),
        ('ED6_DT29/CH12361._CH', 'ED6_DT29/CH12361P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -19850,
            z           = -4000,
            y           = -5550,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23550,
            z           = -4000,
            y           = -23640,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15630,
            z           = -4000,
            y           = 11180,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19630,
            z           = -4000,
            y           = 33560,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -30080,
            z           = 0,
            y           = 11750,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -55630,
            z           = 0,
            y           = 4340,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46020,
            z           = 0,
            y           = -11250,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1CE
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -51600,
            y           = -100,
            z           = 46300,
            range       = -40600,
            dword_10    = 0x00002A94,
            dword_14    = 0x0000DFD4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x1EE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -51110,
            triggerZ            = 0,
            triggerY            = 21930,
            triggerRange        = 800,
            actorX              = -51640,
            actorZ              = 1000,
            actorY              = 22460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -24980,
            triggerZ            = -4000,
            triggerY            = 35970,
            triggerRange        = 1000,
            actorX              = -25600,
            actorZ              = -4000,
            actorY              = 36000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -50740,
            triggerZ            = 1000,
            triggerY            = 6930,
            triggerRange        = 1000,
            actorX              = -50040,
            actorZ              = 1000,
            actorY              = 6840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x25A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_268',
    )

    OP_A3(0x10F0)
    Event(0, 0x0004)

    def _loc_268(): pass

    label('loc_268')

    Return()

# id: 0x0001 offset: 0x269
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0xDAC),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x01CD, 0x00, 0x64)
    OP_22(0x01CE, 0x01, 0x50)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 1, 0x1011)),
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28C',
    )

    OP_10(0x02, 0x00)

    def _loc_28C(): pass

    label('loc_28C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 6, 0x1136)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29E',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2A5')

    def _loc_29E(): pass

    label('loc_29E')

    OP_6F(0x0000, 60)

    def _loc_2A5(): pass

    label('loc_2A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 7, 0x1137)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B7',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2BE')

    def _loc_2B7(): pass

    label('loc_2B7')

    OP_6F(0x0001, 60)

    def _loc_2BE(): pass

    label('loc_2BE')

    Return()

# id: 0x0002 offset: 0x2BF
@scena.Code('ReInit')
def ReInit():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x2C4
@scena.Code('func_03_2C4')
def func_03_2C4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 0, 0x1010)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 1, 0x1011)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_47E',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(-51390, 0, 21380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -51390, 0, 21380, 315)
    SetChrPos(0x010A, -50750, 0, 22020, 315)
    OP_0D()
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【圣科洛瓦森林】',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '除了巡逻训练之外，\n',
            '也推荐进行生存训练等等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010191245V#1004F啊，这个牌子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191246V#811F嗯，好像是指示牌呢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191247V#1310F记得昨天经过这里，\n',
            '那前面一定就是出口了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191248V#1006F太好了！\n',
            '这样就能离开森林了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1010)
    OP_28(0x007F, 0x01, 0x1000)
    EventEnd(0x00)

    Jump('loc_4F3')

    def _loc_47E(): pass

    label('loc_47E')

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【圣科洛瓦森林】',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '除了巡逻训练之外，\n',
            '也推荐进行生存训练等等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    def _loc_4F3(): pass

    label('loc_4F3')

    Return()

# id: 0x0004 offset: 0x4F4
@scena.Code('func_04_4F4')
def func_04_4F4():
    EventBegin(0x00)
    OP_6D(-45960, 0, 42730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -47410, 0, 40720, 184)
    SetChrPos(0x010A, -46250, 0, 42000, 184)

    @scena.Lambda('lambda_055B')
    def lambda_055B():
        OP_8E(0x0101, -47410, 0, 26380, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_055B)

    @scena.Lambda('lambda_0576')
    def lambda_0576():
        OP_8E(0x010A, -46250, 0, 26400, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0576)

    @scena.Lambda('lambda_0591')
    def lambda_0591():
        OP_6D(-46460, 0, 25850, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0591)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    OP_8C(0x0101, 0, 500)
    WaitForThreadExit(0x010A, 0x0001)
    OP_8C(0x010A, 270, 500)
    OP_8C(0x010A, 0, 500)
    WaitForThreadExit(0x0101, 0x0002)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010191279V#1007F呼……\n',
            '好像没追上来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191280V#1316F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191281V#812F大概打算和同伴\n',
            '会合之后再追捕我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191282V不趁现在打倒的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x681
@scena.Code('func_05_681')
def func_05_681():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 1, 0x1011)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_68E',
    )

    Return()

    def _loc_68E(): pass

    label('loc_68E')

    EventBegin(0x00)
    Fade(1000)
    OP_6D(-46840, 0, 47650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -47380, 0, 47720, 0)
    SetChrPos(0x010A, -45870, 0, 47720, 0)
    OP_0D()
    ChrTurnDirection(0x010A, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x010A, 400)

    ChrTalk(
        0x010A,
        (
            '#0120191283V#812F刚才的女猎兵\n',
            '应该还在前面才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191284V艾丝蒂尔，准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【进行准备】\n'),
            TXT(0x01, '【挑战战斗】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7EC',
    )

    Fade(1000)
    SetChrPos(0x0101, -46320, 0, 45210, 172)
    SetChrPos(0x010A, -46320, 0, 45210, 172)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_7EC(): pass

    label('loc_7EC')

    ChrTalk(
        0x0101,
        (
            '#0010191285V#1002F那么就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191286V#815F上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x010A, 2)

    @scena.Lambda('lambda_083B')
    def lambda_083B():
        OP_90(0x0101, 0, 0, 10000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_083B)

    Sleep(200)

    OP_90(0x010A, 0, 0, 10000, 7000, 0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5507._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x876
@scena.Code('func_06_876')
def func_06_876():
    UnlockAchievement(0x02, 0x9C, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 6, 0x1136)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_953',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大自然恩惠之水'], 1)"),
            Expr.Return,
        ),
        'loc_8EA',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大自然恩惠之水']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1136)

    Jump('loc_950')

    def _loc_8EA(): pass

    label('loc_8EA')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大自然恩惠之水']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大自然恩惠之水']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_950(): pass

    label('loc_950')

    Jump('loc_984')

    def _loc_953(): pass

    label('loc_953')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_984(): pass

    label('loc_984')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x992
@scena.Code('func_07_992')
def func_07_992():
    UnlockAchievement(0x02, 0x9D, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 7, 0x1137)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A6F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_A06',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1137)

    Jump('loc_A6C')

    def _loc_A06(): pass

    label('loc_A06')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_A6C(): pass

    label('loc_A6C')

    Jump('loc_AA0')

    def _loc_A6F(): pass

    label('loc_A6F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_AA0(): pass

    label('loc_AA0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
