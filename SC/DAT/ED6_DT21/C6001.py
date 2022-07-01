import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C6001_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C6001   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '目标'),
    TXT(0x02, '原福音'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C6001.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0x0010
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4215
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
        ('ED6_DT26/CH20353._CH', 'ED6_DT26/CH20353P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xFA
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

# id: 0x10005 offset: 0x13A
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

# id: 0x0000 offset: 0x182
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_193',
    )

    OP_A3(0x10F0)
    Event(0, 0x000A)

    Jump('loc_1B2')

    def _loc_193(): pass

    label('loc_193')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1A4',
    )

    OP_A3(0x10F1)
    Event(0, 0x0011)

    Jump('loc_1B2')

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_1B2',
    )

    OP_A3(0x10F2)
    Event(0, 0x0013)

    def _loc_1B2(): pass

    label('loc_1B2')

    Return()

# id: 0x0001 offset: 0x1B3
@scena.Code('Init')
def Init():
    OP_22(0x01C3, 0x01, 0x64)
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
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Return,
        ),
        'loc_206',
    )

    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 950)
    OP_6F(0x0003, 240)

    def _loc_206(): pass

    label('loc_206')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)

    Return()

# id: 0x0002 offset: 0x218
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_72(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 5, 0x2205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC4',
    )

    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x000000F0)
    Sleep(500)

    @scena.Lambda('lambda_0294')
    def lambda_0294():
        OP_6D(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0294)

    OP_22(0x013D, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
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
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_03A4')
    def lambda_03A4():
        OP_6D(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03A4)

    @scena.Lambda('lambda_03BC')
    def lambda_03BC():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03BC)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 0x00000320)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_03E7')
    def lambda_03E7():
        OP_8E(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03E7)

    Sleep(2000)

    CreateThread(0x0101, 0x01, 0x00, 0x0003)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x0004)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0005)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x0006)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 0x000003B6)
    Sleep(500)

    OP_22(0x006B, 0x00, 0x64)
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
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_51B',
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

    Jump('loc_8FD')

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B3',
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

    Jump('loc_8FD')

    def _loc_5B3(): pass

    label('loc_5B3')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_620',
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

    Jump('loc_8FD')

    def _loc_620(): pass

    label('loc_620')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_694',
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

    Jump('loc_8FD')

    def _loc_694(): pass

    label('loc_694')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_70D',
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

    Jump('loc_8FD')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_783',
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

    Jump('loc_8FD')

    def _loc_783(): pass

    label('loc_783')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_805',
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

    Jump('loc_8FD')

    def _loc_805(): pass

    label('loc_805')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_875',
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

    Jump('loc_8FD')

    def _loc_875(): pass

    label('loc_875')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8FD',
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

    def _loc_8FD(): pass

    label('loc_8FD')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_993',
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

    Jump('loc_DB0')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A1B',
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

    Jump('loc_DB0')

    def _loc_A1B(): pass

    label('loc_A1B')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A9D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390984V#030F#6P呼，好像是帝国\n',
            '铁路的进化版一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040390985V#031F不过，透明的轨道\n',
            '还是相当惊险的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB0')

    def _loc_A9D(): pass

    label('loc_A9D')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B1F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390986V#1064F#6P好像是一些国家使用的\n',
            '铁路的进化版。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390987V#1068F透明的轨道\n',
            '很让人感到不安啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB0')

    def _loc_B1F(): pass

    label('loc_B1F')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B9F',
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

    Jump('loc_DB0')

    def _loc_B9F(): pass

    label('loc_B9F')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C1D',
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

    Jump('loc_DB0')

    def _loc_C1D(): pass

    label('loc_C1D')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C99',
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

    Jump('loc_DB0')

    def _loc_C99(): pass

    label('loc_C99')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D13',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390994V#1164F#6P好像是帝国铁路的\n',
            '进化版一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060390995V这透明的轨道\n',
            '是用什么做出来的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB0')

    def _loc_D13(): pass

    label('loc_D13')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB0',
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

    def _loc_DB0(): pass

    label('loc_DB0')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E33',
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

    def _loc_E33(): pass

    label('loc_E33')

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
    OP_A2(0x2205)
    OP_28(0x009D, 0x01, 0x0020)

    Jump('loc_158C')

    def _loc_EC4(): pass

    label('loc_EC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 2, 0x220A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1141',
    )

    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x000000F0)
    Sleep(500)

    @scena.Lambda('lambda_0F34')
    def lambda_0F34():
        OP_6D(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F34)

    OP_22(0x013D, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    OP_6D(1980, 2000, 1300, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(4500, 0)
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
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_100E')
    def lambda_100E():
        OP_6D(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_100E)

    @scena.Lambda('lambda_1026')
    def lambda_1026():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1026)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 0x00000320)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_1051')
    def lambda_1051():
        OP_8E(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1051)

    CreateThread(0x0101, 0x01, 0x00, 0x0003)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x0004)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0005)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x0006)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 0x000003B6)
    Sleep(300)

    OP_22(0x006B, 0x00, 0x64)
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
            '马上试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x220A)

    Jump('loc_158C')

    def _loc_1141(): pass

    label('loc_1141')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 3, 0x220B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1352',
    )

    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x000000F0)
    Sleep(500)

    @scena.Lambda('lambda_11B6')
    def lambda_11B6():
        OP_6D(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11B6)

    OP_22(0x013D, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_1223')
    def lambda_1223():
        OP_6D(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1223)

    @scena.Lambda('lambda_123B')
    def lambda_123B():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_123B)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 0x00000320)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_1266')
    def lambda_1266():
        OP_8E(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1266)

    CreateThread(0x0101, 0x01, 0x00, 0x0003)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x0004)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0005)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x0006)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 0x000003B6)
    Sleep(300)

    OP_22(0x006B, 0x00, 0x64)
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
    OP_A2(0x220B)

    Jump('loc_158C')

    def _loc_1352(): pass

    label('loc_1352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 4, 0x220C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_158C',
    )

    Fade(500)
    OP_6D(-7060, 5000, 19260, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(4960, 0)
    OP_6C(347000, 0)
    OP_6E(268, 0)
    SetChrPos(0x0008, -25730, 5110, 21310, 90)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x000000F0)
    Sleep(500)

    @scena.Lambda('lambda_13C7')
    def lambda_13C7():
        OP_6D(17390, 5000, 16010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13C7)

    OP_22(0x013D, 0x00, 0x64)
    OP_73(0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    OP_6D(-7920, 5000, 21760, 0)
    OP_67(0, 9120, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_1434')
    def lambda_1434():
        OP_6D(3080, 5110, 21340, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1434)

    @scena.Lambda('lambda_144C')
    def lambda_144C():
        OP_67(0, 6030, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_144C)

    OP_6F(0x0001, 500)
    OP_70(0x0001, 0x00000320)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_1477')
    def lambda_1477():
        OP_8E(0x00FE, 3140, 5110, 21050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1477)

    CreateThread(0x0101, 0x01, 0x00, 0x0003)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, 0x0004)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x0005)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x0006)
    OP_73(0x0001)
    OP_23(0x013E)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 0x000003B6)
    Sleep(300)

    OP_22(0x006B, 0x00, 0x64)
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
    OP_A2(0x220C)
    OP_28(0x009F, 0x01, 0x0002)

    def _loc_158C(): pass

    label('loc_158C')

    OP_A2(0x2207)
    OP_28(0x009D, 0x01, 0x0200)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0000, 3060, 5000, 18520, 0)
    SetChrPos(0x0001, 3060, 5000, 18520, 0)
    SetChrPos(0x0002, 3060, 5000, 18520, 0)
    SetChrPos(0x0003, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x1632
@scena.Code('func_03_1632')
def func_03_1632():
    SetChrPos(0x00FE, 13930, 4000, 17320, 270)
    OP_8E(0x00FE, 2620, 5000, 18360, 5000, 0x00)

    @scena.Lambda('lambda_165D')
    def lambda_165D():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_165D')

    DispatchAsync2(0x00FE, 0x0002, lambda_165D)

    Return()

# id: 0x0004 offset: 0x1669
@scena.Code('func_04_1669')
def func_04_1669():
    SetChrPos(0x00FE, 13930, 4000, 17320, 270)
    OP_8E(0x00FE, 3630, 5000, 18380, 5000, 0x00)

    @scena.Lambda('lambda_1694')
    def lambda_1694():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1694')

    DispatchAsync2(0x00FE, 0x0002, lambda_1694)

    Return()

# id: 0x0005 offset: 0x16A0
@scena.Code('func_05_16A0')
def func_05_16A0():
    SetChrPos(0x00FE, 13930, 4000, 17320, 270)
    OP_8E(0x00FE, 2240, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_16CB')
    def lambda_16CB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_16CB')

    DispatchAsync2(0x00FE, 0x0002, lambda_16CB)

    Return()

# id: 0x0006 offset: 0x16D7
@scena.Code('func_06_16D7')
def func_06_16D7():
    SetChrPos(0x00FE, 13930, 4000, 17320, 270)
    OP_8E(0x00FE, 4070, 5000, 17190, 5000, 0x00)

    @scena.Lambda('lambda_1702')
    def lambda_1702():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1702')

    DispatchAsync2(0x00FE, 0x0002, lambda_1702)

    Return()

# id: 0x0007 offset: 0x170E
@scena.Code('func_07_170E')
def func_07_170E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1717',
    )

    Return()

    def _loc_1717(): pass

    label('loc_1717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 6, 0x2206)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 6, 0x220E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AE2',
    )

    EventBegin(0x00)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2620, 5000, 18360, 0)
    SetChrPos(0x0102, 3630, 5000, 18380, 0)
    SetChrPos(0x00F8, 2240, 5000, 17190, 0)
    SetChrPos(0x00F9, 4070, 5000, 17190, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('合成音')

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
    SetChrName('合成音')

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
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1877',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_18AB')

    def _loc_1877(): pass

    label('loc_1877')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1899',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_18AB')

    def _loc_1899(): pass

    label('loc_1899')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_18AB(): pass

    label('loc_18AB')

    Sleep(50)

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
    OP_A2(0x220E)
    OP_28(0x009D, 0x01, 0x0040)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0000, 3060, 5000, 18520, 0)
    SetChrPos(0x0001, 3060, 5000, 18520, 0)
    SetChrPos(0x0002, 3060, 5000, 18520, 0)
    SetChrPos(0x0003, 3060, 5000, 18520, 0)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_1B6C')

    def _loc_1AE2(): pass

    label('loc_1AE2')

    EventBegin(0x02)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('合成音')

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
    SetChrName('合成音')

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
    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_1B6C(): pass

    label('loc_1B6C')

    Jump('loc_1E46')

    def _loc_1B6F(): pass

    label('loc_1B6F')

    EventBegin(0x00)
    Fade(500)
    OP_6D(3080, 5110, 21340, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2620, 5000, 18360, 0)
    SetChrPos(0x0102, 3630, 5000, 18380, 0)
    SetChrPos(0x00F8, 2240, 5000, 17190, 0)
    SetChrPos(0x00F9, 4070, 5000, 17190, 0)
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
        'loc_1C4C',
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

    def _loc_1C4C(): pass

    label('loc_1C4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 0, 0x2208)),
            Expr.Return,
        ),
        'loc_1C75',
    )

    OP_CC(0x01, 0x00, '【第７法克特里亚站】')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1C75(): pass

    label('loc_1C75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 1, 0x2209)),
            Expr.Return,
        ),
        'loc_1C98',
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

    def _loc_1C98(): pass

    label('loc_1C98')

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
        'loc_1CDB',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D5D')

    def _loc_1CDB(): pass

    label('loc_1CDB')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CE5(): pass

    label('loc_1CE5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D5D',
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CFF',
    )

    Jump('loc_1D5D')

    def _loc_1CFF(): pass

    label('loc_1CFF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D50',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1D39',
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
        'loc_1D36',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1D36(): pass

    label('loc_1D36')

    Jump('loc_1D50')

    def _loc_1D39(): pass

    label('loc_1D39')

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

    Jump('loc_1CFF')

    def _loc_1D50(): pass

    label('loc_1D50')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1CE5')

    def _loc_1D5D(): pass

    label('loc_1D5D')

    SetMapFlags(0x00100000)

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D7B'),
        (0x00000001, 'loc_1DB9'),
        (0x00000002, 'loc_1DF7'),
        (0x00000003, 'loc_1E35'),
        (-1, 'loc_1E38'),
    )

    def _loc_1D7B(): pass

    label('loc_1D7B')

    OP_A2(0x2211)
    OP_A2(0x2214)
    CreateThread(0x0101, 0x01, 0x00, 0x0008)

    @scena.Lambda('lambda_1D8E')
    def lambda_1D8E():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1D8E)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E38')

    def _loc_1DB9(): pass

    label('loc_1DB9')

    OP_A2(0x2211)
    OP_A2(0x2216)
    CreateThread(0x0101, 0x01, 0x00, 0x0008)

    @scena.Lambda('lambda_1DCC')
    def lambda_1DCC():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DCC)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E38')

    def _loc_1DF7(): pass

    label('loc_1DF7')

    OP_A2(0x2211)
    OP_A2(0x2217)
    CreateThread(0x0101, 0x01, 0x00, 0x0008)

    @scena.Lambda('lambda_1E0A')
    def lambda_1E0A():
        OP_67(0, 5450, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E0A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C6010._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1E38')

    def _loc_1E35(): pass

    label('loc_1E35')

    Jump('loc_1E38')

    def _loc_1E38(): pass

    label('loc_1E38')

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
    def _loc_1E46(): pass

    label('loc_1E46')

    Return()

# id: 0x0008 offset: 0x1E47
@scena.Code('func_08_1E47')
def func_08_1E47():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    CreateThread(0x0101, 0x02, 0x00, 0x0009)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, 0x0009)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, 0x0009)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x0009)
    Sleep(1500)

    OP_6F(0x0001, 950)
    OP_70(0x0001, 0x0000044C)
    Sleep(300)

    OP_22(0x006B, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 4, 0x2214)),
            Expr.Return,
        ),
        'loc_1EE3',
    )

    OP_6F(0x0001, 300)
    OP_70(0x0001, 0x000001F4)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_1EBE')
    def lambda_1EBE():
        OP_6D(-2860, 5000, 21710, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EBE)

    @scena.Lambda('lambda_1ED6')
    def lambda_1ED6():
        OP_6B(5000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1ED6)

    Jump('loc_1F2E')

    def _loc_1EE3(): pass

    label('loc_1EE3')

    OP_6F(0x0001, 1100)
    OP_70(0x0001, 0x00000514)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_1EFC')
    def lambda_1EFC():
        OP_6D(8300, 5000, 21350, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EFC)

    @scena.Lambda('lambda_1F14')
    def lambda_1F14():
        OP_6C(12000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F14)

    @scena.Lambda('lambda_1F24')
    def lambda_1F24():
        OP_6B(5000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1F24)

    def _loc_1F2E(): pass

    label('loc_1F2E')

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()

    Return()

# id: 0x0009 offset: 0x1F3F
@scena.Code('func_09_1F3F')
def func_09_1F3F():
    OP_8E(0x00FE, 3080, 5000, 19030, 2000, 0x00)
    OP_8E(0x00FE, 3010, 5110, 20330, 2000, 0x00)

    @scena.Lambda('lambda_1F6D')
    def lambda_1F6D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000320)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F6D)

    OP_8E(0x00FE, 3100, 5110, 24220, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x1F93
@scena.Code('func_0A_1F93')
def func_0A_1F93():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(3100, 5110, 23900, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 3050, 5110, 21510, 180)
    SetChrPos(0x0102, 3050, 5110, 21510, 180)
    SetChrPos(0x00F8, 3050, 5110, 21510, 180)
    SetChrPos(0x00F9, 3050, 5110, 21510, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0442, 2, 0x2212)),
            Expr.Return,
        ),
        'loc_20AC',
    )

    OP_6D(12690, 5000, 20450, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 1300)
    OP_70(0x0001, 0x00000640)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_2087')
    def lambda_2087():
        OP_6D(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2087)

    @scena.Lambda('lambda_209F')
    def lambda_209F():
        OP_6C(0, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_209F)

    Jump('loc_2114')

    def _loc_20AC(): pass

    label('loc_20AC')

    OP_6D(-9950, 5000, 20680, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 0x00000320)
    OP_22(0x013E, 0x00, 0x64)

    @scena.Lambda('lambda_2102')
    def lambda_2102():
        OP_6D(2890, 5000, 22450, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2102)

    def _loc_2114(): pass

    label('loc_2114')

    OP_A3(0x2210)
    OP_A3(0x2211)
    OP_A3(0x2212)
    OP_A3(0x2213)
    FadeIn(1000, 0)
    OP_73(0x0001)
    OP_23(0x013E)
    OP_6F(0x0001, 800)
    OP_70(0x0001, 0x000003B6)
    Sleep(300)

    OP_22(0x006B, 0x00, 0x64)
    OP_73(0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 7, 0x220F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29EC',
    )

    CreateThread(0x0101, 0x01, 0x00, 0x000B)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, 0x000C)
    Sleep(800)

    @scena.Lambda('lambda_2170')
    def lambda_2170():
        OP_6D(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2170)

    @scena.Lambda('lambda_2188')
    def lambda_2188():
        OP_6B(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2188)

    CreateThread(0x00F8, 0x01, 0x00, 0x000D)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x000E)
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
            '真想它能跑得慢一点，\n',
            '让我好好欣赏一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2335',
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

    Jump('loc_2530')

    def _loc_2335(): pass

    label('loc_2335')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_237B',
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

    Jump('loc_2530')

    def _loc_237B(): pass

    label('loc_237B')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23BC',
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

    Jump('loc_2530')

    def _loc_23BC(): pass

    label('loc_23BC')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23F7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391024V#021F#5P呵呵……有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2530')

    def _loc_23F7(): pass

    label('loc_23F7')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_242F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391025V#1061F#5P哈哈，没错～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2530')

    def _loc_242F(): pass

    label('loc_242F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_246C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391026V#031F#5P呵呵……我有同感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2530')

    def _loc_246C(): pass

    label('loc_246C')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24B4',
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

    Jump('loc_2530')

    def _loc_24B4(): pass

    label('loc_24B4')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24ED',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391028V#071F#5P哈哈……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2530')

    def _loc_24ED(): pass

    label('loc_24ED')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2530',
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

    def _loc_2530(): pass

    label('loc_2530')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25D2',
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

    Jump('loc_29E6')

    def _loc_25D2(): pass

    label('loc_25D2')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2651',
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

    Jump('loc_29E6')

    def _loc_2651(): pass

    label('loc_2651')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26CA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080391034V#070F#5P不过，有了这个，\n',
            '探索就轻松许多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080391035V发现了新的车站\n',
            '就赶快启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_26CA(): pass

    label('loc_26CA')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2774',
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

    Jump('loc_29E6')

    def _loc_2774(): pass

    label('loc_2774')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27F6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040391038V#035F#5P呵呵，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040391039V#030F发现新的车站之后\n',
            '要赶快将它启动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_27F6(): pass

    label('loc_27F6')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_286E',
    )

    ChrTalk(
        0x0109,
        (
            '#0180391040V#1060F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180391041V发现了新的车站\n',
            '就赶紧启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_286E(): pass

    label('loc_286E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28E5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030391042V#027F#5P不过，有了这个\n',
            '探索就方便得多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030391043V发现了新的车站\n',
            '就赶紧启用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29E6')

    def _loc_28E5(): pass

    label('loc_28E5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2967',
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

    Jump('loc_29E6')

    def _loc_2967(): pass

    label('loc_2967')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29E6',
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

    def _loc_29E6(): pass

    label('loc_29E6')

    OP_A2(0x220F)

    Jump('loc_2A44')

    def _loc_29EC(): pass

    label('loc_29EC')

    CreateThread(0x0101, 0x01, 0x00, 0x000B)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, 0x000C)
    Sleep(800)

    @scena.Lambda('lambda_2A0A')
    def lambda_2A0A():
        OP_6D(3100, 5000, 18850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A0A)

    @scena.Lambda('lambda_2A22')
    def lambda_2A22():
        OP_6B(4000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2A22)

    CreateThread(0x00F8, 0x01, 0x00, 0x000D)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x000E)
    Sleep(500)

    def _loc_2A44(): pass

    label('loc_2A44')

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    SetChrPos(0x0000, 3060, 5000, 18520, 180)
    SetChrPos(0x0001, 3060, 5000, 18520, 180)
    SetChrPos(0x0002, 3060, 5000, 18520, 180)
    SetChrPos(0x0003, 3060, 5000, 18520, 180)
    OP_6D(3060, 5000, 18520, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    ClearMapFlags(0x00100000)

    Return()

# id: 0x000B offset: 0x2AF6
@scena.Code('func_0B_2AF6')
def func_0B_2AF6():
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_2B0C')
    def lambda_2B0C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B0C)

    OP_8E(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    OP_8E(0x00FE, 3790, 5000, 17270, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    ClearChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x2B4D
@scena.Code('func_0C_2B4D')
def func_0C_2B4D():
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_2B63')
    def lambda_2B63():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B63)

    OP_8E(0x00FE, 3100, 5000, 18910, 2000, 0x00)
    OP_8E(0x00FE, 2550, 5000, 17250, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x2B9F
@scena.Code('func_0D_2B9F')
def func_0D_2B9F():
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_2BB5')
    def lambda_2BB5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2BB5)

    OP_8E(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    OP_8E(0x00FE, 4230, 5000, 18440, 2000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x000E offset: 0x2BF1
@scena.Code('func_0E_2BF1')
def func_0E_2BF1():
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_2C07')
    def lambda_2C07():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C07)

    OP_8E(0x00FE, 3160, 5000, 19120, 2000, 0x00)
    OP_8E(0x00FE, 1970, 5000, 18340, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x000F offset: 0x2C43
@scena.Code('func_0F_2C43')
def func_0F_2C43():
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
        'loc_2C68',
    )

    Call(0, 0x0014)
    Call(0, 0x0015)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_2C68(): pass

    label('loc_2C68')

    Fade(500)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2480, 2000, 500, 0)
    SetChrPos(0x0102, 1480, 2000, 500, 0)
    SetChrPos(0x00F8, 2450, 1600, -1400, 0)
    SetChrPos(0x00F9, 1560, 1600, -1220, 0)
    OP_0D()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    def _loc_2DB9(): pass

    label('loc_2DB9')

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
            TXT(0x00, '【克雷德尔向导】\n'),
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
        (0x00000000, 'loc_2E41'),
        (0x00000001, 'loc_2F3E'),
        (0x00000002, 'loc_3061'),
        (0x00000003, 'loc_31D1'),
        (0x00000004, 'loc_395E'),
        (-1, 'loc_396B'),
    )

    def _loc_2E41(): pass

    label('loc_2E41')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『克雷德尔』是\n',
            '位于利贝尔·方舟市南区的\n',
            '普通市民居住区。\n',
            '\n',
            '现在其中虽然有１２８个区域，\n',
            '但由于最近几十年出生率的低下，\n',
            '有三分之一的区域已经被关闭。\n',
            '此外，『克雷德尔』的各个区域\n',
            '都设有车站、市政厅、社交场所等公共设施，\n',
            '为市民提供丰富的服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3978')

    def _loc_2F3E(): pass

    label('loc_2F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 7, 0x2207)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FFB',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '要启动『第３５克雷德尔站』的\n',
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
        (0x00000000, 'loc_2FDC'),
        (0x00000001, 'loc_2FF2'),
        (-1, 'loc_2FF8'),
    )

    def _loc_2FDC(): pass

    label('loc_2FDC')

    OP_5F(0x0000)
    OP_5F(0x0001)
    OP_56(0x00)
    FadeIn(300, 0)
    Call(0, 0x0002)

    Return()

    def _loc_2FF2(): pass

    label('loc_2FF2')

    OP_5F(0x0001)

    Jump('loc_2FF8')

    def _loc_2FF8(): pass

    label('loc_2FF8')

    Jump('loc_305E')

    def _loc_2FFB(): pass

    label('loc_2FFB')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在『光环轨道』的运行受到了\n',
            '大幅度的限制。\n',
            '\n',
            '『第３５克雷德尔站』的紧急运行\n',
            '模式已经启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_305E(): pass

    label('loc_305E')

    Jump('loc_3978')

    def _loc_3061(): pass

    label('loc_3061')

    FadeIn(300, 0)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    OP_A9(0xF1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    def _loc_31D1(): pass

    label('loc_31D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 4, 0x221C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3921',
    )

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S当『光环轨道』\n',
            '由于各种原因而无法使用时，\n',
            '可以解除车站周边大门的锁定\n',
            '并进入地下通道之中。\n',
            '\n',
            '【警告】\n',
            '根据来自『中枢塔』的指示，\n',
            '解除锁定必须先进行身份认证。\n',
            '\n',
            '请在此终端前使用\n',
            '您携带的『福音』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    OP_56(0x00)
    OP_5F(0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33F2',
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
            TXT(0x00, '【◇第一次看到（未持有福音）的情况下】\n'),
            TXT(0x01, '【◇第一次看到（持有福音）的情况下】\n'),
            TXT(0x02, '【◇第二次（以上）看到（未持有福音）的情况下】\n'),
            TXT(0x03, '【◇第二次（以上）看到（持有福音）的情况下】\n'),
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
        (0x00000000, 'loc_33C6'),
        (0x00000001, 'loc_33D1'),
        (0x00000002, 'loc_33DC'),
        (0x00000003, 'loc_33E7'),
        (-1, 'loc_33F2'),
    )

    def _loc_33C6(): pass

    label('loc_33C6')

    OP_A3(0x221A)
    RemoveItem(ItemTable['原福音'], 1)

    Jump('loc_33F2')

    def _loc_33D1(): pass

    label('loc_33D1')

    OP_A3(0x221A)
    AddItem(ItemTable['原福音'], 1)

    Jump('loc_33F2')

    def _loc_33DC(): pass

    label('loc_33DC')

    OP_A2(0x221A)
    RemoveItem(ItemTable['原福音'], 1)

    Jump('loc_33F2')

    def _loc_33E7(): pass

    label('loc_33E7')

    OP_A2(0x221A)
    AddItem(ItemTable['原福音'], 1)

    Jump('loc_33F2')

    def _loc_33F2(): pass

    label('loc_33F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 2, 0x221A)),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x040F, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3552',
    )

    ChrTalk(
        0x0101,
        (
            '#0010391461V#1004F#6P这是什么意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391462V#1035F#6P看来这次和以前\n',
            '不一样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391463V#1043F『福音』啊……\n',
            '有没有办法拿到呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    Jump('loc_390B')

    def _loc_3552(): pass

    label('loc_3552')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 2, 0x221A)),
            Expr.Ez,
            (Expr.Eval, "OP_40(0x040F, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_36C2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010391461V#1004F#6P这是什么意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391462V#1035F#6P看来这次和以前\n',
            '不一样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391466V#1043F如果把刚才拿到的『福音』\n',
            '在这个终端前使用的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    Jump('loc_390B')

    def _loc_36C2(): pass

    label('loc_36C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 2, 0x221A)),
            (Expr.Eval, "OP_40(0x040F, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37F1',
    )

    ChrTalk(
        0x0102,
        (
            '#0020391467V#1035F#6P看来要解除锁定\n',
            '就需要『福音』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391468V#1043F有没有办法拿到呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    Jump('loc_390B')

    def _loc_37F1(): pass

    label('loc_37F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 2, 0x221A)),
            (Expr.Eval, "OP_40(0x040F, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_390B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020391469V#1040F#6P如果把刚才拿到的『福音』\n',
            '在这个终端前使用好象就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 78, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S『光环轨道』第３５克雷德尔站\n',
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

    def _loc_390B(): pass

    label('loc_390B')

    OP_A2(0x221A)
    OP_28(0x009D, 0x01, 0x0400)
    FadeOut(300, 0, 100)

    Jump('loc_395B')

    def _loc_3921(): pass

    label('loc_3921')

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S现在，第３５克雷德尔站附近的\n',
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

    Jump('loc_2DB9')

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
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0000, 2020, 2000, 40, 180)
    SetChrPos(0x0001, 2020, 2000, 40, 180)
    SetChrPos(0x0002, 2020, 2000, 40, 180)
    SetChrPos(0x0003, 2020, 2000, 40, 180)
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
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 4, 0x221C)),
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
        'loc_3BD3',
    )

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Yield()
    EventBegin(0x00)
    Fade(1000)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2730, 2000, 270, 315)
    SetChrPos(0x0102, 1150, 2000, 310, 45)
    SetChrPos(0x00F8, 2430, 1600, -1200, 0)
    SetChrPos(0x00F9, 1550, 1600, -1200, 0)
    OP_0D()
    Sleep(1000)

    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 0)
    SetChrSubChip(0x0101, 9)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 1)
    SetChrPos(0x0009, 2400, 2650, 500, 0)
    OP_0D()
    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp007_00.eff')
    OP_22(0x0090, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x0009, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5801._SN', 103, 0, 0)
    IdleLoop()

    Jump('loc_3C23')

    def _loc_3BD3(): pass

    label('loc_3BD3')

    SetMapFlags(0x00000080)
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
    ClearMapFlags(0x00000080)

    Return()

    def _loc_3C23(): pass

    label('loc_3C23')

    Return()

# id: 0x0011 offset: 0x3C24
@scena.Code('func_11_3C24')
def func_11_3C24():
    EventBegin(0x00)
    OP_6D(1950, 2000, 2470, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2480, 2000, 500, 0)
    SetChrPos(0x0102, 1480, 2000, 500, 0)
    SetChrPos(0x00F8, 2450, 1600, -1400, 0)
    SetChrPos(0x00F9, 1560, 1600, -1220, 0)
    FadeIn(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('合成音')

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

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '地下通道１２５号已经可以使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    Fade(500)
    OP_6D(2020, 2000, 40, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0000, 2020, 2000, 40, 180)
    SetChrPos(0x0001, 2020, 2000, 40, 180)
    SetChrPos(0x0002, 2020, 2000, 40, 180)
    SetChrPos(0x0003, 2020, 2000, 40, 180)
    OP_0D()
    OP_A2(0x221C)
    OP_28(0x009D, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x3DB0
@scena.Code('func_12_3DB0')
def func_12_3DB0():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(-13000, 0, 2000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_89(0x0101, -12000, 0, 2000, 90)
    OP_89(0x0102, -13000, 0, 3000, 90)
    OP_89(0x00F8, -13000, 0, 1000, 90)
    OP_89(0x00F9, -14000, 0, 2000, 90)
    OP_0D()
    Sleep(100)

    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x000004B0)

    @scena.Lambda('lambda_3E5C')
    def lambda_3E5C():
        OP_6D(-13000, -25000, 490, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E5C)

    @scena.Lambda('lambda_3E74')
    def lambda_3E74():
        OP_67(0, 3890, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3E74)

    @scena.Lambda('lambda_3E8C')
    def lambda_3E8C():
        OP_6B(5200, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3E8C)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x01C3)
    Sleep(500)

    OP_A2(0x10F1)
    NewScene('ED6_DT21/C5801._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x3EBB
@scena.Code('func_13_3EBB')
def func_13_3EBB():
    EventBegin(0x00)
    OP_6D(-13000, -12750, 490, 0)
    OP_67(0, 3890, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_6F(0x0000, 300)
    Yield()
    OP_89(0x0101, -12000, -23000, 2000, 90)
    OP_89(0x0102, -13000, -23000, 3000, 90)
    OP_89(0x00F8, -13000, -23000, 1000, 90)
    OP_89(0x00F9, -14000, -23000, 2000, 90)
    OP_22(0x00EB, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_70(0x0000, 0x00000000)

    @scena.Lambda('lambda_3F61')
    def lambda_3F61():
        OP_6D(-13000, 0, 2000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3F61)

    @scena.Lambda('lambda_3F79')
    def lambda_3F79():
        OP_67(0, 3880, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3F79)

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
    OP_6D(-7000, 0, 2000, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    SetChrPos(0x0000, -7000, 0, 2000, 90)
    SetChrPos(0x0001, -7000, 0, 2000, 90)
    SetChrPos(0x0002, -7000, 0, 2000, 90)
    SetChrPos(0x0003, -7000, 0, 2000, 90)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x4076
@scena.Code('func_14_4076')
def func_14_4076():
    FadeOut(0, 0, -1)
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
        (0x00000000, 'loc_40F0'),
        (0x00000001, 'loc_40F6'),
        (-1, 'loc_40FC'),
    )

    def _loc_40F0(): pass

    label('loc_40F0')

    OP_A2(0x1200)

    Jump('loc_40FC')

    def _loc_40F6(): pass

    label('loc_40F6')

    OP_A2(0x1201)

    Jump('loc_40FC')

    def _loc_40FC(): pass

    label('loc_40FC')

    Return()

# id: 0x0015 offset: 0x40FD
@scena.Code('func_15_40FD')
def func_15_40FD():
    FadeOut(0, 0, -1)
    OP_6D(-545830, 30000, 755590, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
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
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0016 offset: 0x4190
@scena.Code('func_16_4190')
def func_16_4190():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '≡ 前面的月台\n',
            '　　　第３５克雷德尔站',
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
