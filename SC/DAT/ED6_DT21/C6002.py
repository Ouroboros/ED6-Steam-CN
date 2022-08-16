import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C6002_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C6002   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C6002.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0x0010
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
        ('ED6_DT26/CH20353._CH', 'ED6_DT26/CH20353P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '原福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65537,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
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
        ScenaEventData(
            x           = 2000,
            y           = 4500,
            z           = 19500,
            range       = 4000,
            dword_10    = 0x00001964,
            dword_14    = 0x00004E20,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -12900,
            y           = 0,
            z           = 2140,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000012,
        ),
    )

# id: 0x10004 offset: 0x142
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2000,
            triggerZ            = 2000,
            triggerY            = 1560,
            triggerRange        = 1000,
            actorX              = 2000,
            actorZ              = 2000,
            actorY              = 1560,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5200,
            triggerZ            = 0,
            triggerY            = 12110,
            triggerRange        = 1000,
            actorX              = 5200,
            actorZ              = 1200,
            actorY              = 13110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x18A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_19B',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0A_1F8E)

    Jump('loc_1BA')

    def _loc_19B(): pass

    label('loc_19B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1AC',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_11_4283)

    Jump('loc_1BA')

    def _loc_1AC(): pass

    label('loc_1AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_1BA',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_13_4527)

    def _loc_1BA(): pass

    label('loc_1BA')

    Return()

# id: 0x0001 offset: 0x1BB
@scena.Code('func_01_1BB')
def func_01_1BB():
    PlaySE(451, 0x01, 0x64)
    OP_12(0x000124F8, 0x000493E0, 0x00000000)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 500)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 0)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Return,
        ),
        'loc_20E',
    )

    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 950)
    OP_6F(0x0003, 240)

    def _loc_20E(): pass

    label('loc_20E')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)

    Return()

# id: 0x0002 offset: 0x220
@scena.Code('func_02_220')
def func_02_220():
    EventBegin(0x00)
    OP_72(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 5, 0x2205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ECC',
    )

    Fade(500)
    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_029C')
    def lambda_029C():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_029C)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    CameraMove(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391470V#1004F#6P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390960V#1044F#6P……有东西过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_03AC')
    def lambda_03AC():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03AC)

    @scena.Lambda('lambda_03C4')
    def lambda_03C4():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03C4)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_03EF')
    def lambda_03EF():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03EF)

    Sleep(2000)

    CreateThread(0x0101, 0x01, 0x00, func_03_163C)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_1673)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_16AA)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_16E1)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(500)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010390961V#1004F#6P那、那是什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_523',
    )

    ChrTalk(
        0x0102,
        (
            '#0020390962V#1040F#5P<FIXME>どうやらこれが\n',
            '《レールハイロゥ》みたいだね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390963Vどういう仕組みなんだろう……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_523(): pass

    label('loc_523')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BB',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390964V#173F<FIXME>どうやらこれが\n',
            '《レールハイロゥ》のようだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390965V#178Fしかし一体\n',
            'どういう仕組みなのだろうか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_5BB(): pass

    label('loc_5BB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_628',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390966V#1165F#6P看来这就是\n',
            '『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391478V是通过什么样的原理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_628(): pass

    label('loc_628')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_69C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390968V#026F#6P呼呼……\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030391480V是通过什么样的原理呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_715',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390970V#053F#6P哟，\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050391482V虽然不知道是\n',
            '通过什么样的原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_78B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390972V#074F#6P呼呼。\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080391484V什么样的原理倒是无从得知……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_78B(): pass

    label('loc_78B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_80D',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390974V#1064F#6P哈……\n',
            '看来这就是『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180391486V虽然完全搞不清楚\n',
            '是通过什么样的原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_80D(): pass

    label('loc_80D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_87D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390976V#035F#6P呼，看来这就是\n',
            '『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040391488V虽然不了解是什么原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_905')

    def _loc_87D(): pass

    label('loc_87D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_905',
    )

    ChrTalk(
        0x010B,
        (
            '#0090390978V#216F#5P<FIXME>ど、どうやらこれが\n',
            '《レールハイロゥ》みたいだけど……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390979V一体どうなってんの？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_905(): pass

    label('loc_905')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_99B',
    )

    ChrTalk(
        0x0110,
        (
            '#0110390980V#278F<FIXME>……帝国を走る鉄道と\n',
            '雰囲気は似ているな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110390981V#277F透明なレールというのが\n',
            'やや落ち着かんが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_99B(): pass

    label('loc_99B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A23',
    )

    ChrTalk(
        0x010B,
        (
            '#0090390982V#213F#6P……但感觉和帝国的\n',
            '铁路有点相似。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390983V#413F不过，透明的轨道\n',
            '还是令人有点胆战心惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_A23(): pass

    label('loc_A23')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390984V#030F#6P呼，好像是帝国\n',
            '铁路的进化版一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390985V#031F不过透明的轨道\n',
            '还是相当惊险的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_AA3(): pass

    label('loc_AA3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B29',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390986V#1064F#6P好像是一些国家使用的\n',
            '铁路的进化版。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390987V#1068F不过透明的轨道\n',
            '很让人感到不安啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_B29(): pass

    label('loc_B29')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390988V#073F#6P像矿车一样\n',
            '在轨道上跑的交通工具啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080390989V#075F透明的轨道还真\n',
            '让人不放心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_BA9(): pass

    label('loc_BA9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C27',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390990V#555F#6P像矿车一样\n',
            '在轨道上跑的交通工具啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390991V#551F透明的轨道实在\n',
            '感觉怪怪的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_C27(): pass

    label('loc_C27')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA3',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390992V#020F#6P像矿车一样\n',
            '在轨道上跑的交通工具。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390993V#524F透明的轨道\n',
            '总让人有点不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_CA3(): pass

    label('loc_CA3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D1B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390994V#1164F#6P好像是帝国铁路的\n',
            '进化版一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390995V这透明的轨道\n',
            '是用什么做出来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_D1B(): pass

    label('loc_D1B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB8',
    )

    ChrTalk(
        0x010F,
        (
            '#0100390996V#176F<FIXME>帝国で運用されている\n',
            '鉄道に似ているようだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100390997V#178F透明なレールというのは\n',
            'さすがに落ち着かないが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DB8(): pass

    label('loc_DB8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390998V#064F#6P说、说不定是\n',
            '在空中展开了某种力场\n',
            '所形成的轨道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390999V#067F了、了不起的技术啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3B(): pass

    label('loc_E3B')

    ChrTalk(
        0x0101,
        (
            '#0010391000V#1006F#6P嗯，虽然没什么头绪，\n',
            '不过既然是一种移动的手段，\n',
            '就没有不尝试的道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391001V#1018F快点坐上去看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0440, 5, 0x2205))
    OP_28(0x009D, 0x01, 0x0020)

    Jump('loc_1596')

    def _loc_ECC(): pass

    label('loc_ECC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 2, 0x220A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_114B',
    )

    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_0F3C')
    def lambda_0F3C():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F3C)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(205, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010391002V#1006F#6P来了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_1016')
    def lambda_1016():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1016)

    @scena.Lambda('lambda_102E')
    def lambda_102E():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_102E)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1059')
    def lambda_1059():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1059)

    CreateThread(0x0101, 0x01, 0x00, func_03_163C)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_1673)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_16AA)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_16E1)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010391003V#1006F#6P好了，这样一来总算\n',
            '可以使用这个东西了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391004V#1040F#6P是啊……\n',
            '马上试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 2, 0x220A))

    Jump('loc_1596')

    def _loc_114B(): pass

    label('loc_114B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 3, 0x220B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_135C',
    )

    Fade(500)
    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_11C0')
    def lambda_11C0():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11C0)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_122D')
    def lambda_122D():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_122D)

    @scena.Lambda('lambda_1245')
    def lambda_1245():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1245)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1270')
    def lambda_1270():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1270)

    CreateThread(0x0101, 0x01, 0x00, func_03_163C)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_1673)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_16AA)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_16E1)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010391005V#1015F#6P嗯，现在可以来往于\n',
            '３个车站了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391006V#1040F#6P嗯……\n',
            '变得相当方便了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 3, 0x220B))

    Jump('loc_1596')

    def _loc_135C(): pass

    label('loc_135C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 4, 0x220C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1596',
    )

    Fade(500)
    CameraMove(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 240)
    Sleep(500)

    @scena.Lambda('lambda_13D1')
    def lambda_13D1():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13D1)

    PlaySE(317, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_143E')
    def lambda_143E():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_143E)

    @scena.Lambda('lambda_1456')
    def lambda_1456():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1456)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1481')
    def lambda_1481():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1481)

    CreateThread(0x0101, 0x01, 0x00, func_03_163C)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_1673)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_16AA)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_16E1)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)

    ChrTalk(
        0x0102,
        (
            '#0020391007V#1035F#6P好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391008V#1040F现在从『卡尔玛丽』\n',
            '到『中枢塔』都能\n',
            '方便地来回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391009V#1007F#6P呼……好长的距离啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 4, 0x220C))
    OP_28(0x009F, 0x01, 0x0002)

    def _loc_1596(): pass

    label('loc_1596')

    SetScenaFlags(ScenaFlag(0x0441, 0, 0x2208))
    OP_28(0x009E, 0x01, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0000, 3060, 5000, 18520, 0)
    ChrSetPos(0x0001, 3060, 5000, 18520, 0)
    ChrSetPos(0x0002, 3060, 5000, 18520, 0)
    ChrSetPos(0x0003, 3060, 5000, 18520, 0)
    CameraMove(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x163C
@scena.Code('func_03_163C')
def func_03_163C():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 2620, 5000, 18360, 5000, 0x00)

    @scena.Lambda('lambda_1667')
    def lambda_1667():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1667')

    DispatchAsync2(0x00FE, 0x0002, lambda_1667)

    Return()

# id: 0x0004 offset: 0x1673
@scena.Code('func_04_1673')
def func_04_1673():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 3630, 5000, 18380, 5000, 0x00)

    @scena.Lambda('lambda_169E')
    def lambda_169E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_169E')

    DispatchAsync2(0x00FE, 0x0002, lambda_169E)

    Return()

# id: 0x0005 offset: 0x16AA
@scena.Code('func_05_16AA')
def func_05_16AA():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 2240, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_16D5')
    def lambda_16D5():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_16D5')

    DispatchAsync2(0x00FE, 0x0002, lambda_16D5)

    Return()

# id: 0x0006 offset: 0x16E1
@scena.Code('func_06_16E1')
def func_06_16E1():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 4070, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_170C')
    def lambda_170C():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_170C')

    DispatchAsync2(0x00FE, 0x0002, lambda_170C)

    Return()

# id: 0x0007 offset: 0x1718
@scena.Code('func_07_1718')
def func_07_1718():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1721',
    )

    Return()

    def _loc_1721(): pass

    label('loc_1721')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B6A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 6, 0x220E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ADD',
    )

    EventBegin(0x00)
    Fade(500)
    CameraMove(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2620, 5000, 18360, 0)
    ChrSetPos(0x0102, 3630, 5000, 18380, 0)
    ChrSetPos(0x00F8, 2240, 5000, 17190, 0)
    ChrSetPos(0x00F9, 4070, 5000, 17190, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在其它车站的紧急运行\n',
            '模式尚未启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『光环轨道』无法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_187C',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_18B0')

    def _loc_187C(): pass

    label('loc_187C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_189E',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_18B0')

    def _loc_189E(): pass

    label('loc_189E')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_18B0(): pass

    label('loc_18B0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18D2',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1906')

    def _loc_18D2(): pass

    label('loc_18D2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18F4',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1906')

    def _loc_18F4(): pass

    label('loc_18F4')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_1906(): pass

    label('loc_1906')

    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x00F8)
    OP_63(0x00F9)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391010V#1019F#6P……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391011V#1035F#6P……看来不启动其它\n',
            '车站的『紧急运行模式』的话\n',
            '就不能使用这个来移动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391012V#1040F很遗憾，\n',
            '现在只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391013V#1007F#6P唔～……\n',
            '害我空欢喜了一场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391014V#1015F没办法，先找其他路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0441, 6, 0x220E))
    OP_28(0x009D, 0x01, 0x0040)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0000, 3060, 5000, 18520, 0)
    ChrSetPos(0x0001, 3060, 5000, 18520, 0)
    ChrSetPos(0x0002, 3060, 5000, 18520, 0)
    ChrSetPos(0x0003, 3060, 5000, 18520, 0)
    CameraMove(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_1B67')

    def _loc_1ADD(): pass

    label('loc_1ADD')

    EventBegin(0x02)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在其它车站的紧急运行\n',
            '模式尚未启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『光环轨道』无法使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_1B67(): pass

    label('loc_1B67')

    Jump('loc_1E41')

    def _loc_1B6A(): pass

    label('loc_1B6A')

    EventBegin(0x00)
    Fade(500)
    CameraMove(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2620, 5000, 18360, 0)
    ChrSetPos(0x0102, 3630, 5000, 18380, 0)
    ChrSetPos(0x00F8, 2240, 5000, 17190, 0)
    ChrSetPos(0x00F9, 4070, 5000, 17190, 0)
    OP_0D()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
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

    OP_CC(0x00, 0x00, 0x000A, 0x000A, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Return,
        ),
        'loc_1C47',
    )

    OP_CC(0x01, 0x00, '【西卡尔玛丽站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1C47(): pass

    label('loc_1C47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Return,
        ),
        'loc_1C70',
    )

    OP_CC(0x01, 0x00, '【第３５克雷德尔站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1C70(): pass

    label('loc_1C70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Return,
        ),
        'loc_1C93',
    )

    OP_CC(0x01, 0x00, '【中枢塔前站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1C93(): pass

    label('loc_1C93')

    OP_CC(0x01, 0x00, '【放弃使用】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    OP_CC(0x02, 0x00)
    MenuEnd(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1CD6',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D58')

    def _loc_1CD6(): pass

    label('loc_1CD6')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CE0(): pass

    label('loc_1CE0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D58',
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CFA',
    )

    Jump('loc_1D58')

    def _loc_1CFA(): pass

    label('loc_1CFA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D4B',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1D34',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D31',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1D31(): pass

    label('loc_1D31')

    Jump('loc_1D4B')

    def _loc_1D34(): pass

    label('loc_1D34')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Div2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_1CFA')

    def _loc_1D4B(): pass

    label('loc_1D4B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1CE0')

    def _loc_1D58(): pass

    label('loc_1D58')

    MapSetFlags(0x00100000)

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D76'),
        (0x00000001, 'loc_1DB4'),
        (0x00000002, 'loc_1DF2'),
        (0x00000003, 'loc_1E30'),
        (-1, 'loc_1E33'),
    )

    def _loc_1D76(): pass

    label('loc_1D76')

    SetScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    SetScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    CreateThread(0x0101, 0x01, 0x00, func_08_1E42)

    @scena.Lambda('lambda_1D89')
    def lambda_1D89():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1D89)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E33')

    def _loc_1DB4(): pass

    label('loc_1DB4')

    SetScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    SetScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    CreateThread(0x0101, 0x01, 0x00, func_08_1E42)

    @scena.Lambda('lambda_1DC7')
    def lambda_1DC7():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DC7)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E33')

    def _loc_1DF2(): pass

    label('loc_1DF2')

    SetScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    SetScenaFlags(ScenaFlag(0x0442, 7, 0x2217))
    CreateThread(0x0101, 0x01, 0x00, func_08_1E42)

    @scena.Lambda('lambda_1E05')
    def lambda_1E05():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E05)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E33')

    def _loc_1E30(): pass

    label('loc_1E30')

    Jump('loc_1E33')

    def _loc_1E33(): pass

    label('loc_1E33')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    EventEnd(0x00)
    def _loc_1E41(): pass

    label('loc_1E41')

    Return()

# id: 0x0008 offset: 0x1E42
@scena.Code('func_08_1E42')
def func_08_1E42():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    CreateThread(0x0101, 0x02, 0x00, func_09_1F3A)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_09_1F3A)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_09_1F3A)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_09_1F3A)
    Sleep(1500)

    OP_6F(0x0001, 950)
    OP_70(0x0001, 1100)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 5, 0x2215)),
            Expr.Return,
        ),
        'loc_1EEE',
    )

    OP_6F(0x0001, 1100)
    OP_70(0x0001, 1300)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1EB9')
    def lambda_1EB9():
        CameraMove(8300, 5000, 21350, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EB9)

    @scena.Lambda('lambda_1ED1')
    def lambda_1ED1():
        OP_6C(12000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1ED1)

    @scena.Lambda('lambda_1EE1')
    def lambda_1EE1():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1EE1)

    Jump('loc_1F29')

    def _loc_1EEE(): pass

    label('loc_1EEE')

    OP_6F(0x0001, 300)
    OP_70(0x0001, 500)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1F07')
    def lambda_1F07():
        CameraMove(-2860, 5000, 21710, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F07)

    @scena.Lambda('lambda_1F1F')
    def lambda_1F1F():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F1F)

    def _loc_1F29(): pass

    label('loc_1F29')

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()

    Return()

# id: 0x0009 offset: 0x1F3A
@scena.Code('func_09_1F3A')
def func_09_1F3A():
    ChrWalkTo(0x00FE, 3080, 5000, 19030, 2000, 0x00)
    ChrWalkTo(0x00FE, 3010, 5110, 20330, 2000, 0x00)

    @scena.Lambda('lambda_1F68')
    def lambda_1F68():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F68)

    ChrWalkTo(0x00FE, 3100, 5110, 24220, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x1F8E
@scena.Code('func_0A_1F8E')
def func_0A_1F8E():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(3100, 5110, 23900, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 3050, 5110, 21510, 180)
    ChrSetPos(0x0102, 3050, 5110, 21510, 180)
    ChrSetPos(0x00F8, 3050, 5110, 21510, 180)
    ChrSetPos(0x00F9, 3050, 5110, 21510, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 3, 0x2213)),
            Expr.Return,
        ),
        'loc_2097',
    )

    CameraMove(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_2082')
    def lambda_2082():
        CameraMove(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2082)

    Jump('loc_210F')

    def _loc_2097(): pass

    label('loc_2097')

    CameraMove(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 1300)
    OP_70(0x0001, 1600)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_20ED')
    def lambda_20ED():
        CameraMove(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_20ED)

    @scena.Lambda('lambda_2105')
    def lambda_2105():
        OP_6C(0, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2105)

    def _loc_210F(): pass

    label('loc_210F')

    ClearScenaFlags(ScenaFlag(0x0442, 0, 0x2210))
    ClearScenaFlags(ScenaFlag(0x0442, 1, 0x2211))
    ClearScenaFlags(ScenaFlag(0x0442, 2, 0x2212))
    ClearScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    FadeIn(1000, 0)
    OP_73(0x0001)
    OP_23(0x013E)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 950)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 7, 0x220F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29E5',
    )

    CreateThread(0x0101, 0x01, 0x00, func_0B_2AEF)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_0C_2B46)
    Sleep(800)

    @scena.Lambda('lambda_216B')
    def lambda_216B():
        CameraMove(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_216B)

    @scena.Lambda('lambda_2183')
    def lambda_2183():
        CameraSetDistance(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2183)

    CreateThread(0x00F8, 0x01, 0x00, func_0D_2B98)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_0E_2BEA)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010391015V#1004F#4P好、好像一转眼\n',
            '就到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391016V#1035F#6P速度很快，\n',
            '却几乎没有摇晃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391017V#1040F真是了不起的技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391018V#1015F#4P确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391019V#1016F不过难得有那么棒的景色，\n',
            '真希望它能跑得慢一点\n',
            '让我好好欣赏一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2330',
    )

    ChrTalk(
        0x010B,
        (
            '#0090391020V#413F#5P真是的……\n',
            '你还真是悠哉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391021V#210F……不过确实也\n',
            '有点可惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_2330(): pass

    label('loc_2330')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2376',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391022V#067F#5P嘿嘿……\n',
            '的确可以这么说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_2376(): pass

    label('loc_2376')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23B7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391023V#1168F#5P呵呵……\n',
            '确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_23B7(): pass

    label('loc_23B7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23F2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391024V#021F#5P呵呵……有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_23F2(): pass

    label('loc_23F2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_242A',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391025V#1061F#5P哈哈，没错～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_242A(): pass

    label('loc_242A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2467',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391026V#031F#5P呵呵……我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_2467(): pass

    label('loc_2467')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24AF',
    )

    ChrTalk(
        0x010F,
        (
            '#0100391027V#171F<FIXME>ふふ……\n',
            'それもそうだな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_24AF(): pass

    label('loc_24AF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24E8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391028V#071F#5P哈哈……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_252B')

    def _loc_24E8(): pass

    label('loc_24E8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_252B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391029V#051F<FIXME>へっ……\n',
            'まあ確かにな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_252B(): pass

    label('loc_252B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25CD',
    )

    ChrTalk(
        0x0110,
        (
            '#0110391030V#278F<FIXME>だが、これのおかげで\n',
            '探索が楽になりそうだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110391031V#277F新しい駅を見つけたら\n',
            'すぐに使えるようにすべきだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_25CD(): pass

    label('loc_25CD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_264C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050391032V#051F#5P不过，多亏有这东西，\n',
            '探索变得轻松许多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050391033V发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_264C(): pass

    label('loc_264C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26C5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391034V#070F#5P不过，有了这东西\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080391035V发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_26C5(): pass

    label('loc_26C5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_276F',
    )

    ChrTalk(
        0x010F,
        (
            '#0100391036V#179F<FIXME>だが、これのおかげで\n',
            'ずいぶん探索が楽になりそうだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100391037V#170F新しい駅を発見したら\n',
            'すぐに使えるようにしてしまおう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_276F(): pass

    label('loc_276F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27EF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391038V#035F#5P呵呵，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040391039V#030F发现了新的车站\n',
            '还真想赶快启用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_27EF(): pass

    label('loc_27EF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2867',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391040V#1060F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180391041V发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_2867(): pass

    label('loc_2867')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28DE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391042V#027F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030391043V发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_28DE(): pass

    label('loc_28DE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2960',
    )

    ChrTalk(
        0x0105,
        (
            '#0060391044V#1167F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060391045V#1168F发现了新的车站\n',
            '还真想赶快启用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29DF')

    def _loc_2960(): pass

    label('loc_2960')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29DF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391046V#061F#5P嘿嘿，不过有了这个\n',
            '探索就轻松许多了阿⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070391047V#560F发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29DF(): pass

    label('loc_29DF')

    SetScenaFlags(ScenaFlag(0x0441, 7, 0x220F))

    Jump('loc_2A3D')

    def _loc_29E5(): pass

    label('loc_29E5')

    CreateThread(0x0101, 0x01, 0x00, func_0B_2AEF)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_0C_2B46)
    Sleep(800)

    @scena.Lambda('lambda_2A03')
    def lambda_2A03():
        CameraMove(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A03)

    @scena.Lambda('lambda_2A1B')
    def lambda_2A1B():
        CameraSetDistance(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2A1B)

    CreateThread(0x00F8, 0x01, 0x00, func_0D_2B98)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_0E_2BEA)
    Sleep(500)

    def _loc_2A3D(): pass

    label('loc_2A3D')

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    ChrSetPos(0x0000, 3060, 5000, 18520, 180)
    ChrSetPos(0x0001, 3060, 5000, 18520, 180)
    ChrSetPos(0x0002, 3060, 5000, 18520, 180)
    ChrSetPos(0x0003, 3060, 5000, 18520, 180)
    CameraMove(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapClearFlags(0x00100000)

    Return()

# id: 0x000B offset: 0x2AEF
@scena.Code('func_0B_2AEF')
def func_0B_2AEF():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2B05')
    def lambda_2B05():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B05)

    ChrWalkTo(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    ChrWalkTo(0x00FE, 3790, 5000, 17270, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrClearFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x2B46
@scena.Code('func_0C_2B46')
def func_0C_2B46():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2B5C')
    def lambda_2B5C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B5C)

    ChrWalkTo(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    ChrWalkTo(0x00FE, 2550, 5000, 17250, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x2B98
@scena.Code('func_0D_2B98')
def func_0D_2B98():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2BAE')
    def lambda_2BAE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2BAE)

    ChrWalkTo(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    ChrWalkTo(0x00FE, 4230, 5000, 18440, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x000E offset: 0x2BEA
@scena.Code('func_0E_2BEA')
def func_0E_2BEA():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2C00')
    def lambda_2C00():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C00)

    ChrWalkTo(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    ChrWalkTo(0x00FE, 1970, 5000, 18340, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x000F offset: 0x2C3C
@scena.Code('func_0F_2C3C')
def func_0F_2C3C():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C61',
    )

    Call(0, 0x0014)
    Call(0, 0x0015)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_2C61(): pass

    label('loc_2C61')

    Fade(500)
    CameraMove(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2480, 2000, 500, 0)
    ChrSetPos(0x0102, 1480, 2000, 500, 0)
    ChrSetPos(0x00F8, 2450, 1600, -1400, 0)
    ChrSetPos(0x00F9, 1560, 1600, -1220, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2DB2(): pass

    label('loc_2DB2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_397B',
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
        20,
        100,
        1,
        (
            TXT(0x00, '【法克特里亚向导】\n'),
            TXT(0x01, '【使用光环轨道】\n'),
            TXT(0x02, '【网络商城】\n'),
            TXT(0x03, '【解除门锁】\n'),
            TXT(0x04, '【停止服务】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E3C'),
        (0x00000001, 'loc_2F28'),
        (0x00000002, 'loc_304D'),
        (0x00000003, 'loc_31BD'),
        (0x00000004, 'loc_395E'),
        (-1, 'loc_396B'),
    )

    def _loc_2E3C(): pass

    label('loc_2E3C')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『法克特里亚』是\n',
            '位于利贝尔·方舟市东区的\n',
            '工业计划区域。\n',
            '\n',
            '食品、服装、医疗、机械、住宅等\n',
            '城市生活所需的各类工业产品\n',
            '都由区内的工厂负责制造。\n',
            '\n',
            '此外，在６４个区域当中，\n',
            '第１到第８区内设有港湾设施，\n',
            '成为了都市之间贸易的窗口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3978')

    def _loc_2F28(): pass

    label('loc_2F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FE5',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '要启动『第７法克特里亚站』的\n',
            '紧急运行模式吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Menu(
        1,
        130,
        240,
        0,
        (
            TXT(0x00, '【启动】\n'),
            TXT(0x01, '【不启动】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2FC6'),
        (0x00000001, 'loc_2FDC'),
        (-1, 'loc_2FE2'),
    )

    def _loc_2FC6(): pass

    label('loc_2FC6')

    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)
    FadeIn(300, 0)
    Call(0, 0x0002)

    Return()

    def _loc_2FDC(): pass

    label('loc_2FDC')

    OP_5F(0x0001)

    Jump('loc_2FE2')

    def _loc_2FE2(): pass

    label('loc_2FE2')

    Jump('loc_304A')

    def _loc_2FE5(): pass

    label('loc_2FE5')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '『第７法克特里亚站』的紧急运行\n',
            '模式已经启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_304A(): pass

    label('loc_304A')

    Jump('loc_3978')

    def _loc_304D(): pass

    label('loc_304D')

    FadeIn(300, 0)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    OP_A9(0xF2)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    FadeOut(300, 0, 100)

    Jump('loc_3978')

    def _loc_31BD(): pass

    label('loc_31BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 6, 0x222E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3923',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S当『光环轨道』\n',
            '由于各种原因而无法使用时，\n',
            '可以解除车站周边大门的锁定\n',
            '并进入地下通道之中。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S【警告】\n',
            '根据来自『中枢塔』的指示，\n',
            '安全等级提高了。\n',
            '\n',
            '请在此终端前使用\n',
            '您携带的『福音』之后\n',
            '输入密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    OP_56(0x00)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3414',
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
        0,
        (
            TXT(0x00, '【◇第一次调查的情况下】\n'),
            TXT(0x01, '【◇第二次（以上）调查的情况下（没向吉尔打听&空贼团救出前）】\n'),
            TXT(0x02, '【◇第二次（以上）调查的情况下（没向吉尔打听&空贼团救出后）】\n'),
            TXT(0x03, '【◇第二次（以上）调查的情况下（已向吉尔打听）】\n'),
            TXT(0x04, '【◇什么也没有变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_33E4'),
        (0x00000001, 'loc_33F0'),
        (0x00000002, 'loc_33FC'),
        (0x00000003, 'loc_3408'),
        (-1, 'loc_3414'),
    )

    def _loc_33E4(): pass

    label('loc_33E4')

    ClearScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    ClearScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    ClearScenaFlags(ScenaFlag(0x0445, 4, 0x222C))

    Jump('loc_3414')

    def _loc_33F0(): pass

    label('loc_33F0')

    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    ClearScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    ClearScenaFlags(ScenaFlag(0x0445, 4, 0x222C))

    Jump('loc_3414')

    def _loc_33FC(): pass

    label('loc_33FC')

    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    ClearScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))

    Jump('loc_3414')

    def _loc_3408(): pass

    label('loc_3408')

    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    SetScenaFlags(ScenaFlag(0x0445, 5, 0x222D))
    SetScenaFlags(ScenaFlag(0x0445, 4, 0x222C))

    Jump('loc_3414')

    def _loc_3414(): pass

    label('loc_3414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 7, 0x221F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3578',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400025V#1004F#6P密、密码是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400026V#1035F#6P受到网络管理中枢的\n',
            '操作了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400027V#1042F看来『结社』对这座城市的\n',
            '功能掌握得相当透彻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_390D')

    def _loc_3578(): pass

    label('loc_3578')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36A1',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400028V#1035F#6P……现在只能\n',
            '不管这个终端了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400029V#1040F等发现了什么线索\n',
            '再来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_390D')

    def _loc_36A1(): pass

    label('loc_36A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 5, 0x222D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37E0',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400030V#1035F#6P如果『结社』\n',
            '最近设置了密码的话\n',
            '仅凭我们手头的情报恐怕不够。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400031V#1040F如果有人知道的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_390D')

    def _loc_37E0(): pass

    label('loc_37E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 5, 0x222D)),
            Expr.Return,
        ),
        'loc_390D',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400032V#1040F#6P我想应该试试\n',
            '吉尔先生提供的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400033V在终端前使用『福音』之后\n',
            '说出那个词吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第７法克特里亚站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制。麻烦请您在本终端\n',
            '  手动输入我们可以为您提供的服务。\n',
            '\n',
            '\n',
            '『利贝尔·方舟』市·交通管理中心',
            TxtCtl.Enter,
        ),
    )

    def _loc_390D(): pass

    label('loc_390D')

    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))
    OP_28(0x009E, 0x01, 0x0002)
    FadeOut(300, 0, 100)

    Jump('loc_395B')

    def _loc_3923(): pass

    label('loc_3923')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在第７法克特里亚站附近的\n',
            '大门锁定已经解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_395B(): pass

    label('loc_395B')

    Jump('loc_3978')

    def _loc_395E(): pass

    label('loc_395E')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3978')

    def _loc_396B(): pass

    label('loc_396B')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3978')

    def _loc_3978(): pass

    label('loc_3978')

    Jump('loc_2DB2')

    def _loc_397B(): pass

    label('loc_397B')

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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(100, 0)
    Sleep(100)

    Fade(500)
    CameraMove(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, 2020, 2000, 40, 180)
    ChrSetPos(0x0001, 2020, 2000, 40, 180)
    ChrSetPos(0x0002, 2020, 2000, 40, 180)
    ChrSetPos(0x0003, 2020, 2000, 40, 180)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x3A29
@scena.Code('func_10_3A29')
def func_10_3A29():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x40F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A36',
    )

    Return()

    def _loc_3A36(): pass

    label('loc_3A36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 5, 0x222D)),
            Expr.Ez,
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x640),
            Expr.Neg,
            Expr.Geq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x15E0),
            Expr.Leq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x44C),
            Expr.Neg,
            Expr.Geq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x640),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DE5',
    )

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Yield()
    EventBegin(0x00)
    Fade(1000)
    CameraMove(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2480, 2000, 500, 0)
    ChrSetPos(0x0102, 1480, 2000, 500, 0)
    ChrSetPos(0x00F8, 2450, 1600, -1400, 0)
    ChrSetPos(0x00F9, 1560, 1600, -1220, 0)
    OP_0D()
    Sleep(300)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【警告】\n',
            '根据来自『中枢塔』的指示，\n',
            '安全等级提高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '麻烦请在此终端前\n',
            '输入密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(300)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 7, 0x221F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C5A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010400025V#1004F#6P密、密码是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400026V#1035F#6P受到网络管理中枢的\n',
            '操作了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400027V#1042F看来『结社』对这座城市的\n',
            '功能掌握得相当透彻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0443, 7, 0x221F))

    Jump('loc_3D55')

    def _loc_3C5A(): pass

    label('loc_3C5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CCE',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400028V#1035F#6P……现在只能\n',
            '不管这个终端了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400029V#1040F等发现了什么线索\n',
            '再来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D55')

    def _loc_3CCE(): pass

    label('loc_3CCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 5, 0x222D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D55',
    )

    ChrTalk(
        0x0102,
        (
            '#0020400030V#1035F#6P如果『结社』\n',
            '最近设置了密码的话\n',
            '仅凭我们手头的情报恐怕不够。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400031V#1040F如果有人知道的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D55(): pass

    label('loc_3D55')

    Sleep(100)

    Fade(500)
    CameraMove(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, 2020, 2000, 40, 180)
    ChrSetPos(0x0001, 2020, 2000, 40, 180)
    ChrSetPos(0x0002, 2020, 2000, 40, 180)
    ChrSetPos(0x0003, 2020, 2000, 40, 180)
    EventEnd(0x00)

    Jump('loc_4282')

    def _loc_3DE5(): pass

    label('loc_3DE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 6, 0x222E)),
            Expr.Ez,
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x640),
            Expr.Neg,
            Expr.Geq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x15E0),
            Expr.Leq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x44C),
            Expr.Neg,
            Expr.Geq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x640),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4232',
    )

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Yield()
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E68',
    )

    Call(0, 0x0014)
    Call(0, 0x0015)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_3E68(): pass

    label('loc_3E68')

    Fade(1000)
    CameraMove(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2730, 2000, 270, 315)
    ChrSetPos(0x0102, 1150, 2000, 310, 45)
    ChrSetPos(0x00F8, 2430, 1600, -1200, 0)
    ChrSetPos(0x00F9, 1550, 1600, -1200, 0)
    OP_0D()
    Sleep(1000)

    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetSubChip(0x0101, 9)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetSubChip(0x0009, 1)
    ChrSetPos(0x0009, 2400, 2650, 500, 0)
    OP_0D()
    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp007_00.eff')
    PlaySE(144, 0x00, 0x64)
    PlayEffect(0x01, 0x00, 0x0009, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    StopEffect(0x00, 0x02)
    OP_23(0x0090)
    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '福音已经确认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请您于控制台\n',
            '输入密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Fade(250)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0009, 0x0080)
    OP_0D()
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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '输入密码',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【Ｏ．Ｒ．Ｆ．Ｅ．Ｕ．Ｈ．Ｓ】\n'),
            TXT(0x01, '【Ｏ．Ｒ．Ｐ．Ｈ．Ｅ．Ｕ．Ｓ】\n'),
            TXT(0x02, '【Ｏ．Ｌ．Ｐ．Ｈ．Ｅ．Ｕ．Ｓ】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_40E0'),
        (0x00000002, 'loc_40E0'),
        (0x00000001, 'loc_41F2'),
        (-1, 'loc_422F'),
    )

    def _loc_40E0(): pass

    label('loc_40E0')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '密码错误。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请再次使用『福音』并输入\n',
            '正确的密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    Fade(500)
    CameraMove(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0000, 65535)
    ChrSetChipByIndex(0x0001, 65535)
    ChrSetChipByIndex(0x0002, 65535)
    ChrSetChipByIndex(0x0003, 65535)
    ChrSetPos(0x0000, 2020, 2000, 40, 180)
    ChrSetPos(0x0001, 2020, 2000, 40, 180)
    ChrSetPos(0x0002, 2020, 2000, 40, 180)
    ChrSetPos(0x0003, 2020, 2000, 40, 180)
    EventEnd(0x00)
    EventEnd(0x00)

    Jump('loc_422F')

    def _loc_41F2(): pass

    label('loc_41F2')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '密码确认。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5701._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_422F')

    def _loc_422F(): pass

    label('loc_422F')

    Jump('loc_4282')

    def _loc_4232(): pass

    label('loc_4232')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Yield()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '什么也没发生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    MapClearFlags(0x00000080)

    Return()

    def _loc_4282(): pass

    label('loc_4282')

    Return()

# id: 0x0011 offset: 0x4283
@scena.Code('func_11_4283')
def func_11_4283():
    EventBegin(0x00)
    CameraMove(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2480, 2000, 500, 0)
    ChrSetPos(0x0102, 1480, 2000, 500, 0)
    ChrSetPos(0x00F8, 2450, 1600, -1400, 0)
    ChrSetPos(0x00F9, 1560, 1600, -1220, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '本站附近的大门锁定\n',
            '已经解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '地下通道２４６号已经可以使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    Fade(500)
    CameraMove(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, 2020, 2000, 40, 180)
    ChrSetPos(0x0001, 2020, 2000, 40, 180)
    ChrSetPos(0x0002, 2020, 2000, 40, 180)
    ChrSetPos(0x0003, 2020, 2000, 40, 180)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0445, 6, 0x222E))
    OP_28(0x009E, 0x01, 0x0400)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x441C
@scena.Code('func_12_441C')
def func_12_441C():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-13000, 0, 2000, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_89(0x0101, -12000, 0, 2000, 90)
    OP_89(0x0102, -13000, 0, 3000, 90)
    OP_89(0x00F8, -13000, 0, 1000, 90)
    OP_89(0x00F9, -14000, 0, 2000, 90)
    OP_0D()
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 1200)

    @scena.Lambda('lambda_44C8')
    def lambda_44C8():
        CameraMove(-13000, -25000, 490, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44C8)

    @scena.Lambda('lambda_44E0')
    def lambda_44E0():
        OP_67(0, 3890, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44E0)

    @scena.Lambda('lambda_44F8')
    def lambda_44F8():
        CameraSetDistance(5200, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_44F8)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x01C3)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5701._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x4527
@scena.Code('func_13_4527')
def func_13_4527():
    EventBegin(0x00)
    CameraMove(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0000, 300)
    Yield()
    OP_89(0x0101, -12000, -23000, 2000, 90)
    OP_89(0x0102, -13000, -23000, 3000, 90)
    OP_89(0x00F8, -13000, -23000, 1000, 90)
    OP_89(0x00F9, -14000, -23000, 2000, 90)
    PlaySE(235, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_70(0x0000, 0)

    @scena.Lambda('lambda_45CD')
    def lambda_45CD():
        CameraMove(-13000, 0, 2000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_45CD)

    @scena.Lambda('lambda_45E5')
    def lambda_45E5():
        OP_67(0, 3880, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_45E5)

    Sleep(4000)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    OP_73(0x0000)
    Sleep(200)

    Fade(500)
    CameraMove(-7000, 0, 2000, 0)
    OP_67(0, 5700, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    ChrSetPos(0x0000, -7000, 0, 2000, 90)
    ChrSetPos(0x0001, -7000, 0, 2000, 90)
    ChrSetPos(0x0002, -7000, 0, 2000, 90)
    ChrSetPos(0x0003, -7000, 0, 2000, 90)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0445, 7, 0x222F))
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x46E5
@scena.Code('func_14_46E5')
def func_14_46E5():
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
            TXT(0x01, '【◇阿加特在队伍中】\n'),
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
        (0x00000000, 'loc_475D'),
        (0x00000001, 'loc_4763'),
        (-1, 'loc_4769'),
    )

    def _loc_475D(): pass

    label('loc_475D')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4769')

    def _loc_4763(): pass

    label('loc_4763')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4769')

    def _loc_4769(): pass

    label('loc_4769')

    Return()

# id: 0x0015 offset: 0x476A
@scena.Code('func_15_476A')
def func_15_476A():
    FadeOut(0, 0, -1)
    CameraMove(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
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

# id: 0x0016 offset: 0x47FD
@scena.Code('func_16_47FD')
def func_16_47FD():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '≡ 前面的月台\n',
            '　　　第７法克特里亚站',
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
