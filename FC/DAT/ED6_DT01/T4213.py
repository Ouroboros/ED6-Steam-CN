import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4213_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4213   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4213.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT06/CH20039._CH', 'ED6_DT06/CH20039P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_214',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_214(): pass

    label('loc_214')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_220'),
        (-1, 'loc_23F'),
    )

    def _loc_220(): pass

    label('loc_220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x00CC, 1, 0x661))
    Event(0, func_04_454)

    def _loc_23C(): pass

    label('loc_23C')

    Jump('loc_23F')

    def _loc_23F(): pass

    label('loc_23F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_266',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 74910, 0, -38410, 99)
    CreateThread(0x000D, 0x00, 0x00, func_02_2B5)

    Jump('loc_295')

    def _loc_266(): pass

    label('loc_266')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_270',
    )

    Jump('loc_295')

    def _loc_270(): pass

    label('loc_270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_27A',
    )

    Jump('loc_295')

    def _loc_27A(): pass

    label('loc_27A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_284',
    )

    Jump('loc_295')

    def _loc_284(): pass

    label('loc_284')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_28E',
    )

    Jump('loc_295')

    def _loc_28E(): pass

    label('loc_28E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_295',
    )

    def _loc_295(): pass

    label('loc_295')

    Return()

# id: 0x0001 offset: 0x296
@scena.Code('func_01_296')
def func_01_296():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2AB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2AB(): pass

    label('loc_2AB')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x2B5
@scena.Code('func_02_2B5')
def func_02_2B5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2CA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2B5')

    def _loc_2CA(): pass

    label('loc_2CA')

    Return()

# id: 0x0003 offset: 0x2CB
@scena.Code('func_03_2CB')
def func_03_2CB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_37E',
    )

    ChrTalk(
        0x0112,
        (
            '#0101060007V#170F这次的事情让我深刻体会到\n',
            '自己还远远没有成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060008V卡西乌斯上校也回来了。\n',
            '为了不再辱没亲卫队的名声，\n',
            '我更要借此机会身心兼顾地认真修炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_450')

    def _loc_37E(): pass

    label('loc_37E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0112,
        (
            '#0101060004V#170F呼～\n',
            '终于又回到这里来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060005V这次的事情让我深刻体会到\n',
            '自己还远远没有成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060006V卡西乌斯上校也回来了。\n',
            '为了不再辱没亲卫队的名声，\n',
            '我更要借此机会身心兼顾地认真修炼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_450(): pass

    label('loc_450')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x454
@scena.Code('func_04_454')
def func_04_454():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0108, 8)
    ChrSetChipByIndex(0x0104, 10)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0102, 66560, 0, -30890, 186)
    ChrSetPos(0x0108, 65640, 0, -29760, 182)
    ChrSetPos(0x0104, 67130, 0, -29550, 172)
    ChrSetPos(0x0008, 68760, 0, -39520, 135)
    ChrSetPos(0x0009, 69890, 0, -40660, 315)
    ChrSetPos(0x000B, 65730, 0, -41730, 270)
    ChrSetPos(0x000C, 64099, 0, -41250, 90)
    CameraMove(68190, 0, -42370, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    CameraMove(67700, 0, -42570, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6F(0x0000, 60)
    OP_72(0x0000, 0x0010)
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_05D3')
    def lambda_05D3():
        CameraMove(66270, 0, -37030, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_05D3)

    @scena.Lambda('lambda_05EB')
    def lambda_05EB():
        OP_6E(300, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_05EB)

    @scena.Lambda('lambda_05FB')
    def lambda_05FB():
        OP_67(0, 5550, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_05FB)

    @scena.Lambda('lambda_0613')
    def lambda_0613():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0613)

    Sleep(100)

    @scena.Lambda('lambda_0626')
    def lambda_0626():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0626)

    Sleep(100)

    @scena.Lambda('lambda_0639')
    def lambda_0639():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0639)

    Sleep(100)

    @scena.Lambda('lambda_064C')
    def lambda_064C():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_064C)

    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#2620131139V#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2670131140V#5P岂有此理，是侵入者！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131141V#031F#6P哈·哈·哈。\n',
            '被侵入的一方肯定是会这么说的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131142V#070F#6P用不着和他们解释什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020131143V#016F#6P……我们上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0744')
    def lambda_0744():
        ChrWalkTo(0x00FE, 66130, 0, -52310, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0744)

    @scena.Lambda('lambda_075F')
    def lambda_075F():
        ChrWalkTo(0x00FE, 66130, 0, -52310, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_075F)

    Sleep(50)

    @scena.Lambda('lambda_077F')
    def lambda_077F():
        ChrWalkTo(0x00FE, 66130, 0, -52310, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_077F)

    @scena.Lambda('lambda_079A')
    def lambda_079A():
        CameraMove(65930, 0, -40190, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_079A)

    @scena.Lambda('lambda_07B2')
    def lambda_07B2():
        OP_6E(225, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_07B2)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x0008, 4)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x000B, 4)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x0009, 13)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x000C, 13)
    Sleep(350)

    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)
    Battle(0x000003A9, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_851'),
        (-1, 'loc_854'),
    )

    def _loc_851(): pass

    label('loc_851')

    OP_B4(0x00)

    Return()

    def _loc_854(): pass

    label('loc_854')

    EventBegin(0x00)
    CameraMove(69880, 0, -41130, 0)
    OP_6E(309, 0)
    ChrSetPos(0x0102, 70860, 0, -41870, 270)
    ChrSetPos(0x0104, 70610, 0, -40330, 225)
    ChrSetPos(0x0108, 69080, 0, -40260, 180)
    ChrSetPos(0x0008, 68030, 0, -44480, 135)
    ChrSetPos(0x0009, 68470, 0, -46180, 107)
    ChrSetPos(0x000B, 67960, 0, -42620, 270)
    ChrSetPos(0x000C, 66830, 0, -45880, 180)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 5)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetChipByIndex(0x0009, 5)
    ChrSetChipByIndex(0x000C, 5)
    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetFlags(0x000A, 0x0800)
    ChrSetFlags(0x000B, 0x0800)
    ChrSetFlags(0x000C, 0x0800)

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0104,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0108, 8)
    ChrSetChipByIndex(0x0104, 10)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080131144V#070F好的，先胜一局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131145V#035F哎呀，真不过瘾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetDirection(0x0102, 90, 600)
    ChrSetFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_09FF')
    def lambda_09FF():
        ChrWalkTo(0x00FE, 73970, 0, -42150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09FF)

    ChrSetChipByIndex(0x0104, 65535)
    ChrSetChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_0A24')
    def lambda_0A24():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_0A24')

    DispatchAsync2(0x0108, 0x0001, lambda_0A24)

    @scena.Lambda('lambda_0A35')
    def lambda_0A35():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_0A35')

    DispatchAsync2(0x0104, 0x0001, lambda_0A35)

    CameraMove(72350, 0, -40970, 1500)
    WaitForThreadExit(0x0102, 0x0001)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)

    ChrTalk(
        0x0102,
        (
            '#0020131146V#016F现在我就开始操作城门的开关装置！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131147V如果敌人来了请将其击退！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131148V#076F#5P噢，没问题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AEA')
    def lambda_0AEA():
        OP_69(0x00FE, 800)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0AEA)

    ChrSetDirection(0x0108, 270, 400)
    ChrSetChipByIndex(0x0108, 8)
    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0108,
        (
            '#0080131149V#077F#5P我以『不动』之名保证，\n',
            '决不会让任何敌人攻入！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 180, 400)
    ChrSetFlags(0x0104, 0x0002)

    ExecExpressionWithValue(
        0x0104,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0104, 15)
    ChrSetSubChip(0x0104, 0)
    OP_99(0x0104, 0x00, 0x03, 2000)
    Sleep(300)

    OP_99(0x0104, 0x03, 0x0A, 1600)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040131150V#035F#5P哈·哈·哈。\n',
            '此刻就是天空之门打开之时了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0104, 0x0002)

    ExecExpressionWithValue(
        0x0104,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0104, 65535)
    ChrSetSubChip(0x0104, 0)

    @scena.Lambda('lambda_0BED')
    def lambda_0BED():
        OP_69(0x00FE, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0BED)

    ChrSetDirection(0x0104, 270, 400)
    ChrSetChipByIndex(0x0104, 10)
    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0104,
        (
            '#0040131151V#030F#5P最终的乐章奏响了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004E, 0x04, 0x02)
    OP_28(0x004E, 0x04, 0x04)
    OP_28(0x004E, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4200._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
