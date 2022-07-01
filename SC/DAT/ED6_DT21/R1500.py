import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉文努村'),
    TXT(0x02, '西柏斯街道方向'),
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
    header.mapName        = 'Bose'
    header.mapModel       = 'R1500.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xBB7
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
        ('ED6_DT09/CH10030._CH', 'ED6_DT09/CH10030P._CP'),
        ('ED6_DT09/CH10031._CH', 'ED6_DT09/CH10031P._CP'),
        ('ED6_DT09/CH10860._CH', 'ED6_DT09/CH10860P._CP'),
        ('ED6_DT09/CH10861._CH', 'ED6_DT09/CH10861P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10330._CH', 'ED6_DT09/CH10330P._CP'),
        ('ED6_DT09/CH10331._CH', 'ED6_DT09/CH10331P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -170710,
            z                   = 12010,
            y                   = 95390,
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
            x                   = -204960,
            z                   = -100,
            y                   = -46530,
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

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -191470,
            z           = 3990,
            y           = 18830,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180300,
            z           = 3990,
            y           = -3330,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -166330,
            z           = 11950,
            y           = 8590,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0130,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -206780,
            z           = 1860,
            y           = -1570,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -158080,
            z           = 10080,
            y           = -4750,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1B6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1B6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -191900,
            triggerZ            = 3950,
            triggerY            = 23540,
            triggerRange        = 1000,
            actorX              = -191900,
            actorZ              = 3950,
            actorY              = 24150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -146910,
            triggerZ            = 7980,
            triggerY            = 11710,
            triggerRange        = 1000,
            actorX              = -146830,
            actorZ              = 7980,
            actorY              = 12540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_20A'),
        (-1, 'loc_227'),
    )

    def _loc_20A(): pass

    label('loc_20A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 1, 0x1A11)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_224',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    def _loc_224(): pass

    label('loc_224')

    Jump('loc_227')

    def _loc_227(): pass

    label('loc_227')

    Return()

# id: 0x0001 offset: 0x228
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFB6C20, 0xFFFE6DA8, 0x0023001F)
    ClearMapFlags(0x02000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 1, 0x1B21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_251',
    )

    OP_6F(0x0001, 0)

    Jump('loc_258')

    def _loc_251(): pass

    label('loc_251')

    OP_6F(0x0001, 60)

    def _loc_258(): pass

    label('loc_258')

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_276',
    )

    OP_10(0x01, 0x00)
    OP_10(0x03, 0x01)

    Jump('loc_283')

    def _loc_276(): pass

    label('loc_276')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_283',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    def _loc_283(): pass

    label('loc_283')

    Return()

# id: 0x0002 offset: 0x284
@scena.Code('ReInit')
def ReInit():
    Return()

# id: 0x0003 offset: 0x285
@scena.Code('func_03_285')
def func_03_285():
    UnlockAchievement(0x02, 0xD8, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 1, 0x1B21)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_362',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_2F9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B21)

    Jump('loc_35F')

    def _loc_2F9(): pass

    label('loc_2F9')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
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

    def _loc_35F(): pass

    label('loc_35F')

    Jump('loc_393')

    def _loc_362(): pass

    label('loc_362')

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
    def _loc_393(): pass

    label('loc_393')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x3A1
@scena.Code('func_04_3A1')
def func_04_3A1():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BE',
    )

    Call(0, 0x0005)

    def _loc_3BE(): pass

    label('loc_3BE')

    OP_6D(-204280, -140, -31340, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -205400, -50, -35380, 0)
    SetChrPos(0x00F8, -206050, -50, -36380, 0)
    SetChrPos(0x00F9, -204840, -50, -36370, 0)
    SetChrPos(0x0106, -205400, -50, -37370, 0)

    @scena.Lambda('lambda_0445')
    def lambda_0445():
        OP_8E(0x00FE, -204830, 20, -28040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0445)

    Sleep(100)

    @scena.Lambda('lambda_0465')
    def lambda_0465():
        OP_8E(0x00FE, -205380, -170, -29900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0465)

    Sleep(100)

    @scena.Lambda('lambda_0485')
    def lambda_0485():
        OP_8E(0x00FE, -204050, -100, -30060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0485)

    Sleep(100)

    @scena.Lambda('lambda_04A5')
    def lambda_04A5():
        OP_8E(0x00FE, -204630, -150, -32650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_04A5)

    FadeIn(2000, 0)
    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050300766V#555F#2P喂……\n',
            '那边是拉文努村。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300767V我说过了，等手边的工作\n',
            '告一段落后再过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_053D')
    def lambda_053D():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_053D)

    Sleep(50)

    @scena.Lambda('lambda_0550')
    def lambda_0550():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0550)

    Sleep(50)

    OP_8C(0x00F9, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300768V#1008F啊哈哈……\n',
            '说来也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300769V#1016F但是，既然来到这边\n',
            '顺便绕个路也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_82A',
    )

    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0107,
        (
            '#0070300770V#065F#2P姐、姐姐……\n',
            '不可以勉强人家啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300771V#1006F但是，提妲\n',
            '也想过去看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300772V#562F#2P虽、虽然是没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300773V#055F#2P啊～少说废话了。\n',
            '赶快回去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0106, 180, 500)

    @scena.Lambda('lambda_06B7')
    def lambda_06B7():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06B7)

    @scena.Lambda('lambda_06C5')
    def lambda_06C5():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_06C5)

    OP_8E(0x0106, -205090, -50, -43660, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010300774V#1007F嗯……\n',
            '好像很可疑呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300775V#1019F那么不想向我们\n',
            '介绍你妹妹吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300776V#063F#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300777V难不成我……\n',
            '误解了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300778V#1004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8C(0x0107, 0, 400)

    ChrTalk(
        0x0107,
        (
            '#0070300779V#067F#2P不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300780V#560F好了，姐姐。\n',
            '去追阿加特哥哥吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_82A(): pass

    label('loc_82A')

    ChrTalk(
        0x0106,
        (
            '#0050300781V#055F啊～少说废话了。\n',
            '赶快回去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0106, 180, 500)
    OP_8E(0x0106, -205090, -50, -43660, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010300774V#1007F嗯……\n',
            '好像很可疑呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300775V#1019F那么不想向我们\n',
            '介绍你妹妹吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_943',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300784V#524F嗯……\n',
            '说不定有很多隐情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300785V总之，现在还是\n',
            '听阿加特的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_943(): pass

    label('loc_943')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300786V#030F嗯……\n',
            '说不定有很多隐情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300787V#031F总之，现在还是\n',
            '听阿加特兄的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_9B8(): pass

    label('loc_9B8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A22',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300788V#074F嗯……\n',
            '总之，有很多的隐情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300789V#070F现在还是听他的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A95')

    def _loc_A22(): pass

    label('loc_A22')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A95',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300790V#047F说不定是一言难尽呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300791V#040F我想现在还是先听\n',
            '阿加特先生的话比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A95(): pass

    label('loc_A95')

    FadeIn(1500, 0)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R1201._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xAAC
@scena.Code('func_05_AAC')
def func_05_AAC():
    FadeOut(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_B63'),
        (0x00000001, 'loc_B69'),
        (-1, 'loc_B6F'),
    )

    def _loc_B63(): pass

    label('loc_B63')

    OP_A2(0x1200)

    Jump('loc_B6F')

    def _loc_B69(): pass

    label('loc_B69')

    OP_A2(0x1201)

    Jump('loc_B6F')

    def _loc_B6F(): pass

    label('loc_B6F')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x00FF,
            0x00FF,
        ),
        (
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
