import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5901_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5901   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5901.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奈尔',
            x                   = 550,
            z                   = -8000,
            y                   = -84180,
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
            name                = '朵洛希',
            x                   = 4500,
            z                   = -8000,
            y                   = -74410,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '公园区域『卡尔玛丽』1',
            x                   = -10,
            z                   = 0,
            y                   = -46260,
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

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 0,
            y           = -6000,
            z           = -105000,
            range       = 2000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10004 offset: 0x13A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 28020,
            triggerZ            = -7650,
            triggerY            = -71570,
            triggerRange        = 1000,
            actorX              = 28320,
            actorZ              = -6350,
            actorY              = -71070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x15E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_190',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_170',
    )

    Jump('loc_190')

    def _loc_170(): pass

    label('loc_170')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17B',
    )

    Jump('loc_190')

    def _loc_17B(): pass

    label('loc_17B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_190',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_190')

    def _loc_190(): pass

    label('loc_190')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1A1',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_05_742)

    Jump('loc_1DF')

    def _loc_1A1(): pass

    label('loc_1A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1B2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_07_B77)

    Jump('loc_1DF')

    def _loc_1B2(): pass

    label('loc_1B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_1C3',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_0A_E06)

    Jump('loc_1DF')

    def _loc_1C3(): pass

    label('loc_1C3')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_1CF'),
        (-1, 'loc_1DF'),
    )

    def _loc_1CF(): pass

    label('loc_1CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 2, 0x2202)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DF',
    )

    Event(0, func_06_7B6)

    def _loc_1DF(): pass

    label('loc_1DF')

    Return()

# id: 0x0001 offset: 0x1E0
@scena.Code('func_01_1E0')
def func_01_1E0():
    OP_16(0x02, 4000, -128000, -208000, 2293882)

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0003, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0441, 5, 0x220D)),
            Expr.Return,
        ),
        'loc_215',
    )

    OP_71(0x0003, 0x0010)
    OP_64(0x00, 0x0001)
    OP_71(0x0004, 0x0004)

    def _loc_215(): pass

    label('loc_215')

    PlaySE(458, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x21B
@scena.Code('func_02_21B')
def func_02_21B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_23E',
    )

    OP_8D(0x00FE, -1490, -89750, 1490, -74630, 2000)

    Jump('func_02_21B')

    def _loc_23E(): pass

    label('loc_23E')

    Return()

# id: 0x0003 offset: 0x23F
@scena.Code('func_03_23F')
def func_03_23F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 3, 0x22D3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_349',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010390870V#1004F咦，奈尔……\n',
            '你在这里干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270390871V#140F哦，我稍微走远一点来看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390872V飞船的周围\n',
            '基本上都拍过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390873V不过这风景还真让人\n',
            '想不到是在天上呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390874V看来这里的确是\n',
            '公园区域呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x045A, 3, 0x22D3))

    Jump('loc_45F')

    def _loc_349(): pass

    label('loc_349')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EF',
    )

    ChrTalk(
        0x0008,
        (
            '#0270390875V#140F哦，空中的湖泊和\n',
            '从那里流下的瀑布啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390876V看来这里的确是\n',
            '公园区域呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390877V总之让朵洛希那家伙\n',
            '先拍几张照片吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_45F')

    def _loc_3EF(): pass

    label('loc_3EF')

    ChrTalk(
        0x0008,
        (
            '#0270390878V#140F空中的湖和\n',
            '从那里流下的瀑布啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270390879V#141F嘿嘿，这或许正合适\n',
            '作为特刊的封面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45F(): pass

    label('loc_45F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x463
@scena.Code('func_04_463')
def func_04_463():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 3, 0x22D3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C0',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010390880V#1004F咦，朵洛希……\n',
            '你在这里干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280390881V#150F嗯，我正在拍\n',
            '杂志封面用的照片～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390882V但是到处都是我想拍的风景，\n',
            '所以有点眼花缭乱的～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390883V接下来去拍拍\n',
            '那个升降梯吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390884V#151F啊，反正机会难得，\n',
            '上去看看或许也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390885V#1016F你、你可别就这么\n',
            '走丢了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x045A, 3, 0x22D3))

    Jump('loc_73E')

    def _loc_5C0(): pass

    label('loc_5C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A6',
    )

    ChrTalk(
        0x0009,
        (
            '#0280390886V#150F嗯～到处都是我想拍的风景，\n',
            '所以有点眼花缭乱的～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390887V先听前辈的话\n',
            '去拍那个瀑布吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390888V接下来去那边拍拍\n',
            '那个升降梯吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390889V#151F啊，反正机会难得，\n',
            '上去看看或许也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_73E')

    def _loc_6A6(): pass

    label('loc_6A6')

    ChrTalk(
        0x0009,
        (
            '#0280390890V#150F先听前辈的话\n',
            '去拍那个瀑布吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390888V接下来去拍拍\n',
            '那个升降梯吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280390892V坐那个升降梯……\n',
            '看起来好像非常舒服的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_73E(): pass

    label('loc_73E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x742
@scena.Code('func_05_742')
def func_05_742():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-980, 0, -103450, 0)
    OP_67(0, 5900, -10000, 0)
    CameraSetDistance(27200, 0)
    OP_6C(21000, 0)
    OP_6E(236, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    PlaySE(124, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x7B6
@scena.Code('func_06_7B6')
def func_06_7B6():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
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
        'loc_7D8',
    )

    Call(0, 0x000B)
    Call(0, 0x000C)

    def _loc_7D8(): pass

    label('loc_7D8')

    CameraMove(-21660, -2500, -66230, 0)
    OP_67(0, 4770, -10000, 0)
    CameraSetDistance(1150, 0)
    OP_6C(33000, 0)
    OP_6E(602, 0)
    ChrSetPos(0x0101, 1320, -500, -56520, 180)
    ChrSetPos(0x0102, 150, -500, -56440, 180)
    ChrSetPos(0x00F8, 1220, -500, -55050, 180)
    ChrSetPos(0x00F9, -170, -500, -55050, 180)
    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_0869')
    def lambda_0869():
        CameraMove(9270, -8000, -86360, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0869)

    @scena.Lambda('lambda_0881')
    def lambda_0881():
        OP_67(0, 8039, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0881)

    @scena.Lambda('lambda_0899')
    def lambda_0899():
        CameraSetDistance(9070, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0899)

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        OP_6C(336000, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_08A9)

    @scena.Lambda('lambda_08B9')
    def lambda_08B9():
        OP_6E(600, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_08B9)

    OP_C8(0x0200, 0x0046, 'C_PLAC26._CH', 0x00, 0x0FA0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    Fade(500)
    CameraMove(1870, -500, -56280, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4030, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_95B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070311126V#560F#5P哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95B(): pass

    label('loc_95B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_98E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060390860V#1168F#5P好漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_98E(): pass

    label('loc_98E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030390861V#027F#5P好棒的风景呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C6(): pass

    label('loc_9C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9FD',
    )

    ChrTalk(
        0x0109,
        (
            '#0180390862V#1064F#5P哇～了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FD(): pass

    label('loc_9FD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A3E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040390863V#031F#5P哟……\n',
            '很不错的视觉享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A3E(): pass

    label('loc_A3E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A72',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390864V#052F#5P这还真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A72(): pass

    label('loc_A72')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AAF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080390865V#070F#5P嗯……\n',
            '好清爽的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AAF(): pass

    label('loc_AAF')

    ChrTalk(
        0x0101,
        (
            '#0010390866V#1016F#5P怎、怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390867V#1008F实在让人想不到\n',
            '这是在天上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390868V#1035F#6P古代塞姆里亚文明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390869V#1040F看来不仅仅是一个\n',
            '技术发达的社会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0440, 2, 0x2202))
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xB77
@scena.Code('func_07_B77')
def func_07_B77():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(140, -6000, -104620, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_6F(0x0000, 500)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0BE0')
    def lambda_0BE0():
        CameraMove(27920, -7650, -71810, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BE0)

    OP_6C(327000, 7000)
    Fade(500)
    CameraMove(26130, -8000, -68590, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(327000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    OP_71(0x0004, 0x0004)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C6000._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0xC6A
@scena.Code('func_08_C6A')
def func_08_C6A():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xCA0
@scena.Code('func_09_CA0')
def func_09_CA0():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(0, -6000, -105000, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0101, 0, -6000, -104000, 0)
    OP_89(0x0102, -1000, -6000, -105000, 0)
    OP_89(0x00F8, 1000, -6000, -105000, 0)
    OP_89(0x00F9, 0, -6000, -106000, 0)
    OP_0D()
    Sleep(100)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 600)

    @scena.Lambda('lambda_0D4C')
    def lambda_0D4C():
        CameraMove(0, 45000, -105000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D4C)

    @scena.Lambda('lambda_0D64')
    def lambda_0D64():
        OP_67(0, 10500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D64)

    @scena.Lambda('lambda_0D7C')
    def lambda_0D7C():
        OP_6C(320000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D7C)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_24(0x01CA, 0x5A)
    Sleep(100)

    OP_24(0x01CA, 0x50)
    Sleep(100)

    OP_24(0x01CA, 0x46)
    Sleep(100)

    OP_24(0x01CA, 0x3C)
    Sleep(100)

    OP_24(0x01CA, 0x32)
    Sleep(100)

    OP_24(0x01CA, 0x28)
    Sleep(100)

    OP_24(0x01CA, 0x1E)
    Sleep(100)

    OP_24(0x01CA, 0x14)
    Sleep(100)

    OP_24(0x01CA, 0x0A)
    Sleep(100)

    OP_23(0x01CA)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C6000._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0xE06
@scena.Code('func_0A_E06')
def func_0A_E06():
    EventBegin(0x00)
    CameraMove(0, 40000, -105000, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(319000, 0)
    OP_6E(262, 0)
    OP_6F(0x0000, 500)
    Yield()
    OP_89(0x0101, 0, 100000, -104000, 0)
    OP_89(0x0102, -1000, 100000, -105000, 0)
    OP_89(0x00F8, 1000, 100000, -105000, 0)
    OP_89(0x00F9, 0, 100000, -106000, 0)
    PlaySE(235, 0x00, 0x64)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0EA5')
    def lambda_0EA5():
        CameraMove(0, -6000, -105000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EA5)

    @scena.Lambda('lambda_0EBD')
    def lambda_0EBD():
        OP_67(0, 6500, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EBD)

    @scena.Lambda('lambda_0ED5')
    def lambda_0ED5():
        OP_6C(315000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0ED5)

    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(200)

    Fade(500)
    CameraMove(0, -5990, -102670, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 0, -6000, -102670, 0)
    ChrSetPos(0x0001, 0, -6000, -102670, 0)
    ChrSetPos(0x0002, 0, -6000, -102670, 0)
    ChrSetPos(0x0003, 0, -6000, -102670, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0xF80
@scena.Code('func_0B_F80')
def func_0B_F80():
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
        (0x00000000, 'loc_FFA'),
        (0x00000001, 'loc_1000'),
        (-1, 'loc_1006'),
    )

    def _loc_FFA(): pass

    label('loc_FFA')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1006')

    def _loc_1000(): pass

    label('loc_1000')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1006')

    def _loc_1006(): pass

    label('loc_1006')

    Return()

# id: 0x000C offset: 0x1007
@scena.Code('func_0C_1007')
def func_0C_1007():
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
