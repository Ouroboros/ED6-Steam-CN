import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5314_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5314   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5314.x'
    header.mapIndex       = 1
    header.bgm            = 65
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '升降梯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '坏了的德尔基昂',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xE8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xE8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xE8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 29120,
            triggerZ            = 0,
            triggerY            = 5080,
            triggerRange        = 1200,
            actorX              = 29120,
            actorZ              = 0,
            actorY              = 5080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x10C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_11A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_277)

    def _loc_11A(): pass

    label('loc_11A')

    Return()

# id: 0x0001 offset: 0x11B
@scena.Code('func_01_11B')
def func_01_11B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 5, 0x223D)),
            Expr.Return,
        ),
        'loc_133',
    )

    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 300)
    OP_72(0x0000, 0x0020)

    def _loc_133(): pass

    label('loc_133')

    OP_10(0x00, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A1',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 29120, 1000, 5080, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 250)

    Jump('loc_1AD')

    def _loc_1A1(): pass

    label('loc_1A1')

    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 250)

    def _loc_1AD(): pass

    label('loc_1AD')

    ChrSetPos(0x0009, 4500, -9000, 24000, 260)
    OP_A1(0x0009, 0x0002)
    OP_72(0x0002, 0x0004)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 1150)
    LoadEffect(0x02, 'map\\\\mpsmk0.eff')
    LoadEffect(0x03, 'Scraft\\\\sc000_31.eff')
    PlayEffect(0x02, 0xFF, 0x0009, 4500, 3200, -3200, 0, 0, 0, 800, 1000, 800, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x0009, 11500, 2000, -200, 0, 0, 0, 1600, 1800, 1600, 0x00FF, 0, 0, 0, 0)
    MapSetFlags(0x02000000)
    OP_E8(0xD0, 0x07, 0x00, 0x00)

    Return()

# id: 0x0002 offset: 0x277
@scena.Code('func_02_277')
def func_02_277():
    EventBegin(0x00)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_292',
    )

    Call(0, 0x0003)
    Call(0, 0x0004)
    FormationDelMember(0x01, 0xFF)

    def _loc_292(): pass

    label('loc_292')

    CameraMove(12460, 4000, 12240, 0)
    OP_67(0, 12140, -10000, 0)
    CameraSetDistance(10700, 0)
    OP_6C(45000, 0)
    OP_6E(221, 0)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 500)
    OP_70(0x0000, 330)
    Yield()
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x00F8, 0x0020)
    ChrSetBattleFlags(0x00F9, 0x0020)
    OP_89(0x0101, 880, 40000, 130, 90)
    OP_89(0x00F8, -410, 40000, -520, 90)
    OP_89(0x00F9, -330, 40000, 620, 90)
    PlaySE(235, 0x01, 0x64)
    MapClearFlags(0x00100000)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_033E')
    def lambda_033E():
        CameraMove(1960, 10, 2380, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_033E)

    @scena.Lambda('lambda_0356')
    def lambda_0356():
        OP_67(0, 6930, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0356)

    OP_C8(0x0200, 0x0046, 'C_PLAC28._CH', 0x00, 0x05DC)
    OP_73(0x0000)
    OP_23(0x00EB)
    PlaySE(200, 0x00, 0x64)

    @scena.Lambda('lambda_038E')
    def lambda_038E():
        OP_7C(0, 100, 3000, 100)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_038E)

    OP_6F(0x0000, 330)
    OP_70(0x0000, 300)
    OP_73(0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(220, 710, 270, 0)
    OP_67(0, 8310, -10000, 0)
    CameraSetDistance(3690, 0)
    OP_6C(45000, 0)
    OP_6E(221, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010420160V#1007F#5P总、总算……\n',
            '来到了终点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420161V#1002F这里……\n',
            '就是『根源区域』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EA',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420162V#270F<FIXME>……圧倒的な力が\n',
            '奥の通路から流れている……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110420163Vどうやら間違いないようだな……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_4EA(): pass

    label('loc_4EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_55C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420164V#032F#6P啊……一种压倒性的\n',
            '力量从里面涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040420165V看样子是没错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_55C(): pass

    label('loc_55C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420166V#1065F#6P啊……一种可怕的\n',
            '力量从里面涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180420167V#1063F看样子是没错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_5D3(): pass

    label('loc_5D3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_648',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420168V#026F#6P……一种压倒性的\n',
            '力量从里面涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030420169V#022F看样子是没错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_648(): pass

    label('loc_648')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6BF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420170V#1167F#6P……一种压倒性的\n',
            '力量从里面涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060420171V#1162F看样子是没错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_6BF(): pass

    label('loc_6BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_734',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420172V#053F#6P……一种压倒性的\n',
            '力量从里面涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050420173V#057F看样子是没错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_734(): pass

    label('loc_734')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420174V#074F#6P……一种压倒性的\n',
            '力量从里面涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080420175V#072F看样子是没错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_7A9(): pass

    label('loc_7A9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_838',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420176V#176F<FIXME>……圧倒的な力が\n',
            '奥の通路から流れてきている……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100420177V#178Fどうやら間違いなさそうだな……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B2')

    def _loc_838(): pass

    label('loc_838')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B2',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420178V#216F#6P……从里面有\n',
            '一股很厉害的力量涌出来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090420179V#212F……看样子是没错了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B2(): pass

    label('loc_8B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_90F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420180V#062F#6P那，那就是说…\n',
            '约修亚哥哥\n',
            '和『辉之环』就在前面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_90F(): pass

    label('loc_90F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_967',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420181V#212F#6P那、那就是说约修亚和\n',
            '和『辉之环』就在前面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_967(): pass

    label('loc_967')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C5',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420182V#178F<FIXME>つまり《輝く環》が\n',
            'この先にあるということか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_9C5(): pass

    label('loc_9C5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A09',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420183V#072F#6P『辉之环』\n',
            '就在前面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_A09(): pass

    label('loc_A09')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420184V#057F#6P『辉之环』\n',
            '就在前面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_A4D(): pass

    label('loc_A4D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420185V#1162F#6P那么……约修亚和\n',
            '和『辉之环』就在前面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_AA2(): pass

    label('loc_AA2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420186V#022F#6P『辉之环』\n',
            '就在前面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_AE6(): pass

    label('loc_AE6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B2B',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420187V#1063F#6P『辉之环』\n',
            '就在前面吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B99')

    def _loc_B2B(): pass

    label('loc_B2B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B99',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420188V#032F<FIXME>つまり、ヨシュア君と\n',
            '《輝く環》はこの先に……\n',
            '……ということだね？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B99(): pass

    label('loc_B99')

    ChrTalk(
        0x0101,
        (
            '#0010420189V#1002F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420190V#1003F……这应该是\n',
            '最后的战斗了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420191V#1010F不管是为了阻止异变\n',
            '而对付辉之环也好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010420192V为了从那个『白面』那里\n',
            '救回约修亚也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010420193V#1005F#2P二位……\n',
            '请将最后的力量借给我吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CF8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080420194V#070F#6P……明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF8(): pass

    label('loc_CF8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D30',
    )

    ChrTalk(
        0x0106,
        (
            '#0050420195V#051F#6P不用你说我也会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D30(): pass

    label('loc_D30')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D6D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060420196V#1168F#6P嗯……你不嫌弃的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D6D(): pass

    label('loc_D6D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DA5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030420197V#027F#6P呵呵……当然了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DA5(): pass

    label('loc_DA5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DDE',
    )

    ChrTalk(
        0x0109,
        (
            '#0180420198V#1061F#6P嘿嘿，交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DDE(): pass

    label('loc_DDE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E18',
    )

    ChrTalk(
        0x0107,
        (
            '#0070420199V#061F#6P嗯……我会努力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E18(): pass

    label('loc_E18')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E58',
    )

    ChrTalk(
        0x0110,
        (
            '#0110420200V#277F<FIXME>元よりそのつもりだ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E58(): pass

    label('loc_E58')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E96',
    )

    ChrTalk(
        0x010B,
        (
            '#0090420201V#210F#6P嘿嘿……真拿你没办法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E96(): pass

    label('loc_E96')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EDC',
    )

    ChrTalk(
        0x010F,
        (
            '#0100420202V#171F<FIXME>微力を尽くさせてもらおう！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EDC(): pass

    label('loc_EDC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F27',
    )

    ChrTalk(
        0x0104,
        (
            '#0040420203V#031F#6P哼哼……\n',
            '我会奉献我全部的爱和力量！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F27(): pass

    label('loc_F27')

    SetScenaFlags(ScenaFlag(0x0447, 5, 0x223D))
    OP_28(0x009F, 0x01, 0x2000)
    OP_28(0x00A0, 0x04, 0x02)
    OP_28(0x00A0, 0x04, 0x08)
    OP_28(0x00A0, 0x01, 0x0001)
    Sleep(100)

    Fade(1000)

    @scena.Lambda('lambda_0F50')
    def lambda_0F50():
        CameraSetDistance(4000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F50)

    @scena.Lambda('lambda_0F60')
    def lambda_0F60():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F60)

    @scena.Lambda('lambda_0F6E')
    def lambda_0F6E():
        OP_6E(262, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F6E)

    OP_30(0x00)
    WaitForThreadExit(0x0101, 0x0001)
    MapSetFlags(0x00000001)
    EventEnd(0x02)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0003 offset: 0xF8C
@scena.Code('func_03_F8C')
def func_03_F8C():
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
        (0x00000000, 'loc_1006'),
        (0x00000001, 'loc_100C'),
        (-1, 'loc_1012'),
    )

    def _loc_1006(): pass

    label('loc_1006')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1012')

    def _loc_100C(): pass

    label('loc_100C')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1012')

    def _loc_1012(): pass

    label('loc_1012')

    Return()

# id: 0x0004 offset: 0x1013
@scena.Code('func_04_1013')
def func_04_1013():
    FadeOut(0, 0, -1)
    CameraMove(-211220, -20490, -48190, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
            ChrTable['尤莉亚上尉'],
            ChrTable['穆拉'],
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0005 offset: 0x10AA
@scena.Code('func_05_10AA')
def func_05_10AA():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10FB',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_129D')

    def _loc_10FB(): pass

    label('loc_10FB')

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
            TXT(0x00, '在这里休息\n'),
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
        'loc_1282',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 300)
    OP_70(0x0001, 500)
    OP_73(0x0001)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 700)
    OP_71(0x0001, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 29120, 1000, 5080, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 29120, 1000, 5080, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_1282(): pass

    label('loc_1282')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_129C',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_129C(): pass

    label('loc_129C')

    Return()

    def _loc_129D(): pass

    label('loc_129D')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
