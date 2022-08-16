import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C6003_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C6003   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C6003.x'
    header.mapIndex       = 1
    header.bgm            = 62
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
    )

# id: 0x10002 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xC8
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
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10004 offset: 0x108
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
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x150
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_161',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0A_1F4D)

    Jump('loc_16F')

    def _loc_161(): pass

    label('loc_161')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_16F',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_11_3C22)

    def _loc_16F(): pass

    label('loc_16F')

    Return()

# id: 0x0001 offset: 0x170
@scena.Code('func_01_170')
def func_01_170():
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
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Return,
        ),
        'loc_1C3',
    )

    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 950)
    OP_6F(0x0003, 240)

    def _loc_1C3(): pass

    label('loc_1C3')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)

    Return()

# id: 0x0002 offset: 0x1D5
@scena.Code('func_02_1D5')
def func_02_1D5():
    EventBegin(0x00)
    OP_72(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 5, 0x2205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E85',
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

    @scena.Lambda('lambda_0251')
    def lambda_0251():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0251)

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

    @scena.Lambda('lambda_0361')
    def lambda_0361():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0361)

    @scena.Lambda('lambda_0379')
    def lambda_0379():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0379)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_03A4')
    def lambda_03A4():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03A4)

    Sleep(2000)

    CreateThread(0x0101, 0x01, 0x00, func_03_15F5)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_162C)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_1663)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_169A)
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
        'loc_4D8',
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

    Jump('loc_8BE')

    def _loc_4D8(): pass

    label('loc_4D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_570',
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

    Jump('loc_8BE')

    def _loc_570(): pass

    label('loc_570')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5DD',
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

    Jump('loc_8BE')

    def _loc_5DD(): pass

    label('loc_5DD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_651',
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

    Jump('loc_8BE')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6CA',
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

    Jump('loc_8BE')

    def _loc_6CA(): pass

    label('loc_6CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_740',
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

    Jump('loc_8BE')

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7C2',
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

    Jump('loc_8BE')

    def _loc_7C2(): pass

    label('loc_7C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_836',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390976V#035F#6P呼，看来这就是\n',
            '『光环轨道』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040391488V什么样的原理倒是无从得知……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BE')

    def _loc_836(): pass

    label('loc_836')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BE',
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

    def _loc_8BE(): pass

    label('loc_8BE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_954',
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

    Jump('loc_D71')

    def _loc_954(): pass

    label('loc_954')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9DC',
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

    Jump('loc_D71')

    def _loc_9DC(): pass

    label('loc_9DC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A5C',
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

    Jump('loc_D71')

    def _loc_A5C(): pass

    label('loc_A5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE2',
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

    Jump('loc_D71')

    def _loc_AE2(): pass

    label('loc_AE2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B62',
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

    Jump('loc_D71')

    def _loc_B62(): pass

    label('loc_B62')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BE0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390990V#555F#6P像矿车一样\n',
            '在轨道上跑的交通工具啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390991V#551F透明的轨道真是\n',
            '感觉怪怪的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D71')

    def _loc_BE0(): pass

    label('loc_BE0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C5C',
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

    Jump('loc_D71')

    def _loc_C5C(): pass

    label('loc_C5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD4',
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

    Jump('loc_D71')

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D71',
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

    def _loc_D71(): pass

    label('loc_D71')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DF4',
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

    def _loc_DF4(): pass

    label('loc_DF4')

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

    Jump('loc_154F')

    def _loc_E85(): pass

    label('loc_E85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 2, 0x220A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1104',
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

    @scena.Lambda('lambda_0EF5')
    def lambda_0EF5():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0EF5)

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

    @scena.Lambda('lambda_0FCF')
    def lambda_0FCF():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0FCF)

    @scena.Lambda('lambda_0FE7')
    def lambda_0FE7():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FE7)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1012')
    def lambda_1012():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1012)

    CreateThread(0x0101, 0x01, 0x00, func_03_15F5)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_162C)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_1663)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_169A)
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

    Jump('loc_154F')

    def _loc_1104(): pass

    label('loc_1104')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 3, 0x220B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1315',
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

    @scena.Lambda('lambda_1179')
    def lambda_1179():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1179)

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

    @scena.Lambda('lambda_11E6')
    def lambda_11E6():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11E6)

    @scena.Lambda('lambda_11FE')
    def lambda_11FE():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11FE)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1229')
    def lambda_1229():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1229)

    CreateThread(0x0101, 0x01, 0x00, func_03_15F5)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_162C)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_1663)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_169A)
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

    Jump('loc_154F')

    def _loc_1315(): pass

    label('loc_1315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 4, 0x220C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_154F',
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

    @scena.Lambda('lambda_138A')
    def lambda_138A():
        CameraMove(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_138A)

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

    @scena.Lambda('lambda_13F7')
    def lambda_13F7():
        CameraMove(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13F7)

    @scena.Lambda('lambda_140F')
    def lambda_140F():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_140F)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_143A')
    def lambda_143A():
        ChrWalkTo(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_143A)

    CreateThread(0x0101, 0x01, 0x00, func_03_15F5)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_04_162C)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_05_1663)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_06_169A)
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

    def _loc_154F(): pass

    label('loc_154F')

    SetScenaFlags(ScenaFlag(0x0441, 1, 0x2209))
    OP_28(0x009F, 0x01, 0x0001)
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

# id: 0x0003 offset: 0x15F5
@scena.Code('func_03_15F5')
def func_03_15F5():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 2620, 5000, 18360, 5000, 0x00)

    @scena.Lambda('lambda_1620')
    def lambda_1620():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1620')

    DispatchAsync2(0x00FE, 0x0002, lambda_1620)

    Return()

# id: 0x0004 offset: 0x162C
@scena.Code('func_04_162C')
def func_04_162C():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 3630, 5000, 18380, 5000, 0x00)

    @scena.Lambda('lambda_1657')
    def lambda_1657():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1657')

    DispatchAsync2(0x00FE, 0x0002, lambda_1657)

    Return()

# id: 0x0005 offset: 0x1663
@scena.Code('func_05_1663')
def func_05_1663():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 2240, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_168E')
    def lambda_168E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_168E')

    DispatchAsync2(0x00FE, 0x0002, lambda_168E)

    Return()

# id: 0x0006 offset: 0x169A
@scena.Code('func_06_169A')
def func_06_169A():
    ChrSetPos(0x00FE, 13930, 4000, 17320, 270)
    ChrWalkTo(0x00FE, 4070, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_16C5')
    def lambda_16C5():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_16C5')

    DispatchAsync2(0x00FE, 0x0002, lambda_16C5)

    Return()

# id: 0x0007 offset: 0x16D1
@scena.Code('func_07_16D1')
def func_07_16D1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16DA',
    )

    Return()

    def _loc_16DA(): pass

    label('loc_16DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 6, 0x220E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A96',
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
        'loc_1835',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1869')

    def _loc_1835(): pass

    label('loc_1835')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1857',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1869')

    def _loc_1857(): pass

    label('loc_1857')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_1869(): pass

    label('loc_1869')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_188B',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_18BF')

    def _loc_188B(): pass

    label('loc_188B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18AD',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_18BF')

    def _loc_18AD(): pass

    label('loc_18AD')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_18BF(): pass

    label('loc_18BF')

    Sleep(1500)

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

    Jump('loc_1B20')

    def _loc_1A96(): pass

    label('loc_1A96')

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
    def _loc_1B20(): pass

    label('loc_1B20')

    Jump('loc_1E00')

    def _loc_1B23(): pass

    label('loc_1B23')

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
        'loc_1C00',
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

    def _loc_1C00(): pass

    label('loc_1C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Return,
        ),
        'loc_1C29',
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

    def _loc_1C29(): pass

    label('loc_1C29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Return,
        ),
        'loc_1C52',
    )

    OP_CC(0x01, 0x00, '【第７法克特里亚站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1C52(): pass

    label('loc_1C52')

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
        'loc_1C95',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D17')

    def _loc_1C95(): pass

    label('loc_1C95')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C9F(): pass

    label('loc_1C9F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D17',
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CB9',
    )

    Jump('loc_1D17')

    def _loc_1CB9(): pass

    label('loc_1CB9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D0A',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1CF3',
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
        'loc_1CF0',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1CF0(): pass

    label('loc_1CF0')

    Jump('loc_1D0A')

    def _loc_1CF3(): pass

    label('loc_1CF3')

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

    Jump('loc_1CB9')

    def _loc_1D0A(): pass

    label('loc_1D0A')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1C9F')

    def _loc_1D17(): pass

    label('loc_1D17')

    MapSetFlags(0x00100000)

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D35'),
        (0x00000001, 'loc_1D73'),
        (0x00000002, 'loc_1DB1'),
        (0x00000003, 'loc_1DEF'),
        (-1, 'loc_1DF2'),
    )

    def _loc_1D35(): pass

    label('loc_1D35')

    SetScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    SetScenaFlags(ScenaFlag(0x0442, 4, 0x2214))
    CreateThread(0x0101, 0x01, 0x00, func_08_1E01)

    @scena.Lambda('lambda_1D48')
    def lambda_1D48():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1D48)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF2')

    def _loc_1D73(): pass

    label('loc_1D73')

    SetScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    SetScenaFlags(ScenaFlag(0x0442, 5, 0x2215))
    CreateThread(0x0101, 0x01, 0x00, func_08_1E01)

    @scena.Lambda('lambda_1D86')
    def lambda_1D86():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1D86)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF2')

    def _loc_1DB1(): pass

    label('loc_1DB1')

    SetScenaFlags(ScenaFlag(0x0442, 3, 0x2213))
    SetScenaFlags(ScenaFlag(0x0442, 6, 0x2216))
    CreateThread(0x0101, 0x01, 0x00, func_08_1E01)

    @scena.Lambda('lambda_1DC4')
    def lambda_1DC4():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DC4)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1DF2')

    def _loc_1DEF(): pass

    label('loc_1DEF')

    Jump('loc_1DF2')

    def _loc_1DF2(): pass

    label('loc_1DF2')

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
    def _loc_1E00(): pass

    label('loc_1E00')

    Return()

# id: 0x0008 offset: 0x1E01
@scena.Code('func_08_1E01')
def func_08_1E01():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    CreateThread(0x0101, 0x02, 0x00, func_09_1EF9)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_09_1EF9)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_09_1EF9)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_09_1EF9)
    Sleep(1500)

    OP_6F(0x0001, 950)
    OP_70(0x0001, 1100)
    Sleep(300)

    PlaySE(107, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 6, 0x2216)),
            Expr.Return,
        ),
        'loc_1EAD',
    )

    OP_6F(0x0001, 1100)
    OP_70(0x0001, 1300)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1E78')
    def lambda_1E78():
        CameraMove(8300, 5000, 21350, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E78)

    @scena.Lambda('lambda_1E90')
    def lambda_1E90():
        OP_6C(12000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E90)

    @scena.Lambda('lambda_1EA0')
    def lambda_1EA0():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1EA0)

    Jump('loc_1EE8')

    def _loc_1EAD(): pass

    label('loc_1EAD')

    OP_6F(0x0001, 300)
    OP_70(0x0001, 500)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_1EC6')
    def lambda_1EC6():
        CameraMove(-2860, 5000, 21710, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EC6)

    @scena.Lambda('lambda_1EDE')
    def lambda_1EDE():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1EDE)

    def _loc_1EE8(): pass

    label('loc_1EE8')

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()

    Return()

# id: 0x0009 offset: 0x1EF9
@scena.Code('func_09_1EF9')
def func_09_1EF9():
    ChrWalkTo(0x00FE, 3080, 5000, 19030, 2000, 0x00)
    ChrWalkTo(0x00FE, 3010, 5110, 20330, 2000, 0x00)

    @scena.Lambda('lambda_1F27')
    def lambda_1F27():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 800)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F27)

    ChrWalkTo(0x00FE, 3100, 5110, 24220, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x1F4D
@scena.Code('func_0A_1F4D')
def func_0A_1F4D():
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
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 0, 0x2210)),
            Expr.Return,
        ),
        'loc_2056',
    )

    CameraMove(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 800)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_2041')
    def lambda_2041():
        CameraMove(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2041)

    Jump('loc_20CE')

    def _loc_2056(): pass

    label('loc_2056')

    CameraMove(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 1300)
    OP_70(0x0001, 1600)
    PlaySE(318, 0x00, 0x64)

    @scena.Lambda('lambda_20AC')
    def lambda_20AC():
        CameraMove(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_20AC)

    @scena.Lambda('lambda_20C4')
    def lambda_20C4():
        OP_6C(0, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20C4)

    def _loc_20CE(): pass

    label('loc_20CE')

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
        'loc_299D',
    )

    CreateThread(0x0101, 0x01, 0x00, func_0B_2AA7)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_0C_2AFE)
    Sleep(800)

    @scena.Lambda('lambda_212A')
    def lambda_212A():
        CameraMove(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_212A)

    @scena.Lambda('lambda_2142')
    def lambda_2142():
        CameraSetDistance(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2142)

    CreateThread(0x00F8, 0x01, 0x00, func_0D_2B50)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_0E_2BA2)
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
        'loc_22EF',
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

    Jump('loc_24EA')

    def _loc_22EF(): pass

    label('loc_22EF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2335',
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

    Jump('loc_24EA')

    def _loc_2335(): pass

    label('loc_2335')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2376',
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

    Jump('loc_24EA')

    def _loc_2376(): pass

    label('loc_2376')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23B1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391024V#021F#5P呵呵……有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_23B1(): pass

    label('loc_23B1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23E9',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391025V#1061F#5P哈哈，没错～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_23E9(): pass

    label('loc_23E9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2426',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391026V#031F#5P呵呵……我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_2426(): pass

    label('loc_2426')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_246E',
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

    Jump('loc_24EA')

    def _loc_246E(): pass

    label('loc_246E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24A7',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391028V#071F#5P哈哈……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24EA')

    def _loc_24A7(): pass

    label('loc_24A7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24EA',
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

    def _loc_24EA(): pass

    label('loc_24EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_258C',
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

    Jump('loc_2997')

    def _loc_258C(): pass

    label('loc_258C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_260B',
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

    Jump('loc_2997')

    def _loc_260B(): pass

    label('loc_260B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2684',
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

    Jump('loc_2997')

    def _loc_2684(): pass

    label('loc_2684')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2727',
    )

    ChrTalk(
        0x010F,
        (
            '#0100391036V#179Fだが、これのおかげで\n',
            'ずいぶん探索が楽になりそうだ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100391037V#170F新しい駅を発見したら\n',
            'すぐに使えるようにしてしまおう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2997')

    def _loc_2727(): pass

    label('loc_2727')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27A7',
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

    Jump('loc_2997')

    def _loc_27A7(): pass

    label('loc_27A7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_281F',
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

    Jump('loc_2997')

    def _loc_281F(): pass

    label('loc_281F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2896',
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

    Jump('loc_2997')

    def _loc_2896(): pass

    label('loc_2896')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2918',
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

    Jump('loc_2997')

    def _loc_2918(): pass

    label('loc_2918')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2997',
    )

    ChrTalk(
        0x0107,
        (
            '#0070391046V#061F#5P嘿嘿，不过有了这个\n',
            '探索就方便得多了阿⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070391047V#560F发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2997(): pass

    label('loc_2997')

    SetScenaFlags(ScenaFlag(0x0441, 7, 0x220F))

    Jump('loc_29F5')

    def _loc_299D(): pass

    label('loc_299D')

    CreateThread(0x0101, 0x01, 0x00, func_0B_2AA7)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_0C_2AFE)
    Sleep(800)

    @scena.Lambda('lambda_29BB')
    def lambda_29BB():
        CameraMove(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_29BB)

    @scena.Lambda('lambda_29D3')
    def lambda_29D3():
        CameraSetDistance(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_29D3)

    CreateThread(0x00F8, 0x01, 0x00, func_0D_2B50)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_0E_2BA2)
    Sleep(500)

    def _loc_29F5(): pass

    label('loc_29F5')

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

# id: 0x000B offset: 0x2AA7
@scena.Code('func_0B_2AA7')
def func_0B_2AA7():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2ABD')
    def lambda_2ABD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2ABD)

    ChrWalkTo(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    ChrWalkTo(0x00FE, 3790, 5000, 17270, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrClearFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x2AFE
@scena.Code('func_0C_2AFE')
def func_0C_2AFE():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2B14')
    def lambda_2B14():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B14)

    ChrWalkTo(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    ChrWalkTo(0x00FE, 2550, 5000, 17250, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x2B50
@scena.Code('func_0D_2B50')
def func_0D_2B50():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2B66')
    def lambda_2B66():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B66)

    ChrWalkTo(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    ChrWalkTo(0x00FE, 4230, 5000, 18440, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x000E offset: 0x2BA2
@scena.Code('func_0E_2BA2')
def func_0E_2BA2():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2BB8')
    def lambda_2BB8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2BB8)

    ChrWalkTo(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    ChrWalkTo(0x00FE, 1970, 5000, 18340, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x000F offset: 0x2BF4
@scena.Code('func_0F_2BF4')
def func_0F_2BF4():
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
        'loc_2C19',
    )

    Call(0, 0x0012)
    Call(0, 0x0013)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_2C19(): pass

    label('loc_2C19')

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
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』中枢塔前站\n',
            '\n',
            '\n',
            '※现在『光环轨道』的运行受到了\n',
            '  大幅度的限制，麻烦请您在本终端\n',
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

    def _loc_2D64(): pass

    label('loc_2D64')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A69',
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
        0,
        (
            TXT(0x00, '【中枢塔向导】\n'),
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
        (0x00000000, 'loc_2DEA'),
        (0x00000001, 'loc_36D3'),
        (0x00000002, 'loc_37EC'),
        (0x00000003, 'loc_39DC'),
        (0x00000004, 'loc_3A4C'),
        (-1, 'loc_3A59'),
    )

    def _loc_2DEA(): pass

    label('loc_2DEA')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#0150401054V#1S诸位游击士，欢迎你们。\n',
            '\n',
            '我猜想诸位能够来到这里，\n',
            '于是就在此留言了。\n',
            '\n',
            '『福音计划』已经进入最后一部分，\n',
            '『辉之环』也接近真正的觉醒了。\n',
            '\n',
            '我希望你们也能\n',
            '亲临现场做个见证，\n',
            '不过光是为你们带路的话也颇为无趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#0150401055V#1S因此我们来玩个游戏吧。\n',
            '\n',
            '在中枢塔的各处，\n',
            '都有我的协助者们在把守着。\n',
            '\n',
            '如果能突破他们的防线，来到塔顶的话\n',
            '我就向诸位展示『环』的复活过程。\n',
            '\n',
            '接下来就让我期待你们的表现吧。\n',
            '\n',
            '\n',
            '『蛇之使徒』第三柱——盖鲁格·怀斯曼',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#0150401056V#1SP.S.致约修亚。\n',
            '我很高兴你能和\n',
            '重要的家人以及同伴再会。\n',
            '\n',
            '不过，你可别小看了\n',
            '莱维和玲哦。\n',
            '\n',
            '我特地给你们准备了机会，\n',
            '你们就尽情地聊聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 1, 0x2231)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36D0',
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020401057V#1042F#5P………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30E8',
    )

    ChrTalk(
        0x010F,
        (
            '#0100401058V#173F<FIXME>こ、これは……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_30E8(): pass

    label('loc_30E8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_311F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070401059V#065F#6P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_311F(): pass

    label('loc_311F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3153',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401060V#1163F#6P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_3153(): pass

    label('loc_3153')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3187',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401061V#1063F#6P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_3187(): pass

    label('loc_3187')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31BE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401062V#022F#6P……这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_31BE(): pass

    label('loc_31BE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31F5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401063V#032F#6P哟，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_31F5(): pass

    label('loc_31F5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3228',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401064V#057F#6P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_3228(): pass

    label('loc_3228')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_325F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080401065V#072F#6P……这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_329B')

    def _loc_325F(): pass

    label('loc_325F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_329B',
    )

    ChrTalk(
        0x010B,
        (
            '#0090401066V#216F<FIXME>こ、これって……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_329B(): pass

    label('loc_329B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32EB',
    )

    ChrTalk(
        0x0110,
        (
            '#0110401067V#270F<FIXME>……随分と\n',
            '悪趣味な男のようだな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_32EB(): pass

    label('loc_32EB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_335A',
    )

    ChrTalk(
        0x010B,
        (
            '#0090401068V#212F#6P我不大了解\n',
            '这个教授……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090401069V不过感觉他真是个\n',
            '趣味低级的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_335A(): pass

    label('loc_335A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3397',
    )

    ChrTalk(
        0x0108,
        (
            '#0080401070V#072F#6P趣味低级的男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_3397(): pass

    label('loc_3397')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_33D8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401071V#057F#6P哼……趣味低级的白痴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_33D8(): pass

    label('loc_33D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_344F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401072V#035F#6P呼，不得了不得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040401073V#030F看来是个令人心服口服的\n',
            '趣味低级人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_344F(): pass

    label('loc_344F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_348E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401074V#022F#6P……趣味低级的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_348E(): pass

    label('loc_348E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34DF',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401075V#1063F#6P怎么说呢……\n',
            '还真是个趣味低级的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_34DF(): pass

    label('loc_34DF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3519',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401076V#1162F#6P……趣味低级。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355B')

    def _loc_3519(): pass

    label('loc_3519')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_355B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070401077V#065F<FIXME>……ひ、ひどいよ………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_355B(): pass

    label('loc_355B')

    ChrTalk(
        0x0101,
        (
            '#0010401078V#1007F#6P嗯……是一个性格\n',
            '完全扭曲的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010401079V#1025F#2P我说，约修亚。\n',
            '你不必介意那种人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020401080V#1035F#5P……没关系，我不介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401081V#1040F不过，莱维他们\n',
            '看来似乎真的在那里面呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401082V我们必须打起精神来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010401083V#1006F#2P……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0446, 1, 0x2231))

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0102, 0, 400)
    SetMessageWindowPos(330, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    def _loc_36D0(): pass

    label('loc_36D0')

    Jump('loc_3A66')

    def _loc_36D3(): pass

    label('loc_36D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_378A',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '要启动『中枢塔前站』的\n',
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
        (0x00000000, 'loc_376B'),
        (0x00000001, 'loc_3781'),
        (-1, 'loc_3787'),
    )

    def _loc_376B(): pass

    label('loc_376B')

    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)
    FadeIn(300, 0)
    Call(0, 0x0002)

    Return()

    def _loc_3781(): pass

    label('loc_3781')

    OP_5F(0x0001)

    Jump('loc_3787')

    def _loc_3787(): pass

    label('loc_3787')

    Jump('loc_37E9')

    def _loc_378A(): pass

    label('loc_378A')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '『中枢塔前站』的紧急运行\n',
            '模式已经启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_37E9(): pass

    label('loc_37E9')

    Jump('loc_3A66')

    def _loc_37EC(): pass

    label('loc_37EC')

    FadeIn(300, 0)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>《レールハイロゥ》アクシスピラー前駅　　　　\n',
            '\n',
            '※現在《レールハイロゥ》の運行に\n',
            '  大幅な制限が加えられています。\n',
            '  お手数ですが、当端末から\n',
            '  可能なサービスを手動で入力してください。\n',
            '\n',
            '《リベル＝アーク》市·交通管理センター',
            TxtCtl.Enter,
        ),
    )

    OP_A9(0xF3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S<FIXME>《レールハイロゥ》アクシスピラー前駅　　　　\n',
            '\n',
            '※現在《レールハイロゥ》の運行に\n',
            '  大幅な制限が加えられています。\n',
            '  お手数ですが、当端末から\n',
            '  可能なサービスを手動で入力してください。\n',
            '\n',
            '《リベル＝アーク》市·交通管理センター',
            TxtCtl.Enter,
        ),
    )

    FadeOut(300, 0, 100)

    Jump('loc_3A66')

    def _loc_39DC(): pass

    label('loc_39DC')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S地下通道２４６号\n',
            '已经可以使用了。\n',
            '\n',
            '对面的地下大门\n',
            '是通向公园区域的避难通道。\n',
            '\n',
            '只能在紧急时刻使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A66')

    def _loc_3A4C(): pass

    label('loc_3A4C')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3A66')

    def _loc_3A59(): pass

    label('loc_3A59')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3A66')

    def _loc_3A66(): pass

    label('loc_3A66')

    Jump('loc_2D64')

    def _loc_3A69(): pass

    label('loc_3A69')

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

# id: 0x0010 offset: 0x3B17
@scena.Code('func_10_3B17')
def func_10_3B17():
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

    @scena.Lambda('lambda_3BC3')
    def lambda_3BC3():
        CameraMove(-13000, -25000, 490, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3BC3)

    @scena.Lambda('lambda_3BDB')
    def lambda_3BDB():
        OP_67(0, 3890, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3BDB)

    @scena.Lambda('lambda_3BF3')
    def lambda_3BF3():
        CameraSetDistance(5200, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3BF3)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x01C3)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x3C22
@scena.Code('func_11_3C22')
def func_11_3C22():
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

    @scena.Lambda('lambda_3CC8')
    def lambda_3CC8():
        CameraMove(-13000, 0, 2000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3CC8)

    @scena.Lambda('lambda_3CE0')
    def lambda_3CE0():
        OP_67(0, 3880, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3CE0)

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
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x3DDD
@scena.Code('func_12_3DDD')
def func_12_3DDD():
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
            TXT(0x00, '【◇雪拉扎德在队伍内】\n'),
            TXT(0x01, '【◇阿加特在队伍内】\n'),
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
        (0x00000000, 'loc_3E53'),
        (0x00000001, 'loc_3E59'),
        (-1, 'loc_3E5F'),
    )

    def _loc_3E53(): pass

    label('loc_3E53')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3E5F')

    def _loc_3E59(): pass

    label('loc_3E59')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3E5F')

    def _loc_3E5F(): pass

    label('loc_3E5F')

    Return()

# id: 0x0013 offset: 0x3E60
@scena.Code('func_13_3E60')
def func_13_3E60():
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

# id: 0x0014 offset: 0x3EF3
@scena.Code('func_14_3EF3')
def func_14_3EF3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '≡ 前面的月台\n',
            '　　　中枢塔前站',
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
